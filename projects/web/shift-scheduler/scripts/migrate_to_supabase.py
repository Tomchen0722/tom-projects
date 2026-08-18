"""把本機 SQLite 的資料搬到 Supabase。

用法:
    python scripts/migrate_to_supabase.py              # 先試跑,只看會搬什麼,不寫入
    python scripts/migrate_to_supabase.py --run        # 真的搬
    python scripts/migrate_to_supabase.py --run --wipe # 先清空 Supabase 再搬

搬完會做兩件容易被忘記的事:
    1. 重設每張表的流水號,不然之後新增資料會撞到既有 id
    2. 逐表比對筆數,對不上就報錯
"""

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import Config                                  # noqa: E402
from scheduler import db                                   # noqa: E402

# 有外鍵相依,順序不能亂:先有員工和班別,才有請假和排班
TABLES = [
    ("employees", ["id", "name", "employee_no", "phone", "line_user_id", "role",
                   "skills", "max_shifts_per_week", "min_shifts_per_week",
                   "active", "created_at"]),
    ("shift_types", ["id", "name", "code", "start_time", "end_time",
                     "required_headcount", "required_skill", "color",
                     "sort_order", "active"]),
    ("leave_requests", ["id", "employee_id", "start_date", "end_date", "leave_type",
                        "reason", "status", "source", "created_at", "decided_at"]),
    ("assignments", ["id", "work_date", "shift_type_id", "employee_id", "locked",
                     "status", "note", "created_at"]),
    ("swap_requests", ["id", "assignment_id", "requester_id", "target_shift_type_id",
                       "target_date", "reason", "status", "source",
                       "created_at", "decided_at"]),
    ("settings", ["key", "value"]),
]


def read_sqlite(path: str) -> dict:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    data = {}
    try:
        for table, columns in TABLES:
            exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
            ).fetchone()
            if not exists:
                data[table] = []
                continue
            rows = conn.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall()
            data[table] = [tuple(r[c] for c in columns) for r in rows]
    finally:
        conn.close()
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="把本機 SQLite 的資料搬到 Supabase")
    parser.add_argument("--run", action="store_true", help="真的寫入,不加就只是試跑")
    parser.add_argument("--wipe", action="store_true", help="寫入前先清空 Supabase 現有資料")
    parser.add_argument("--sqlite", default=Config.DB_PATH, help="來源 SQLite 檔案路徑")
    args = parser.parse_args()

    print()
    print("=" * 62)
    print("  SQLite  →  Supabase  資料搬移")
    print("=" * 62)

    if not Config.DATABASE_URL:
        print("\n[X] .env 沒有填 SUPABASE_DB_URL,不知道要搬去哪裡。")
        return 1
    if Config.DATABASE_URL_ERROR:
        print(f"\n[X] 連線字串有問題:{Config.DATABASE_URL_ERROR}")
        return 1
    if not Path(args.sqlite).exists():
        print(f"\n[X] 找不到來源檔案:{args.sqlite}")
        return 1

    print(f"\n  來源:{args.sqlite}")
    print("  目標:Supabase (PostgreSQL)")

    data = read_sqlite(args.sqlite)
    total = sum(len(rows) for rows in data.values())
    print("\n  要搬的資料:")
    for table, _ in TABLES:
        print(f"    {table:<16} {len(data[table]):>6} 筆")
    if total == 0:
        print("\n[i] 本機沒有資料,不用搬。")
        return 0

    if not args.run:
        print("\n[i] 這是試跑,沒有寫入任何東西。")
        print("    確認上面數字沒問題後,加上 --run 再執行一次。")
        if not args.wipe:
            print("    如果 Supabase 已經有舊資料,建議一起加 --wipe 先清空。")
        return 0

    conn = db.connect_postgres(Config.DATABASE_URL, Config.DB_CONNECT_TIMEOUT)
    try:
        conn.autocommit = False
        with conn.cursor() as cur:
            cur.execute(db.SCHEMA_POSTGRES)                # 確保表都在

            if args.wipe:
                print("\n  清空 Supabase 現有資料…")
                for table, _ in reversed(TABLES):
                    cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE")

            print("\n  寫入中…")
            for table, columns in TABLES:
                rows = data[table]
                if not rows:
                    continue
                placeholders = ", ".join(["%s"] * len(columns))
                sql = (f"INSERT INTO {table} ({', '.join(columns)}) "
                       f"VALUES ({placeholders}) ON CONFLICT DO NOTHING")
                cur.executemany(sql, rows)
                print(f"    {table:<16} {len(rows):>6} 筆")

            # 重設流水號:下一筆的 id 要接在現有最大值後面
            print("\n  重設流水號…")
            for table, columns in TABLES:
                if "id" not in columns:
                    continue
                cur.execute(
                    f"SELECT setval(pg_get_serial_sequence('{table}', 'id'), "
                    f"COALESCE((SELECT MAX(id) FROM {table}), 1), "
                    f"(SELECT COUNT(*) > 0 FROM {table}))"
                )

            # 比對筆數
            print("\n  比對筆數…")
            bad = []
            for table, _ in TABLES:
                cur.execute(f"SELECT count(*) FROM {table}")
                got = cur.fetchone()[0]
                want = len(data[table])
                mark = "v" if got == want else "X"
                print(f"    [{mark}] {table:<16} 本機 {want:>5}  →  Supabase {got:>5}")
                if got != want:
                    bad.append(table)

            if bad:
                conn.rollback()
                print(f"\n[X] {', '.join(bad)} 筆數對不上,已取消,Supabase 沒有被改動。")
                print("    最可能的原因是 Supabase 本來就有資料。請加 --wipe 重跑。")
                return 1

        conn.commit()
    except Exception as exc:                               # noqa: BLE001
        conn.rollback()
        print(f"\n[X] 搬移失敗,已全部復原:{exc}")
        return 1
    finally:
        conn.close()

    print("\n[v] 搬移完成。")
    print("    本機的 SQLite 檔案沒有被刪掉,確認雲端資料沒問題後可以自行留存或移除。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
