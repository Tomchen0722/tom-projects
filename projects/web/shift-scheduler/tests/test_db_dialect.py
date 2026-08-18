"""驗證 SQL 方言翻譯,以及兩種資料庫都跑得起來。

用法:
    python tests/test_db_dialect.py                 # 只測 SQLite 與翻譯規則
    python tests/test_db_dialect.py --pg "postgresql://..."   # 連真的 PostgreSQL 一起測

--pg 可以指向任何 PostgreSQL(本機 docker 或 Supabase 都行)。
Supabase 就是 PostgreSQL,所以本機測得過,Supabase 就會過。
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    mark = "v" if condition else "X"
    print(f"  [{mark}] {name}" + (f"  — {detail}" if detail and not condition else ""))


# ==================================================================
# 1. 翻譯規則
# ==================================================================

def test_translate():
    from scheduler.db import translate

    print("\n[1] SQL 方言翻譯")

    got = translate("SELECT * FROM employees WHERE id = ? AND active = ?")
    check("? 換成 %s", got == "SELECT * FROM employees WHERE id = %s AND active = %s", got)

    got = translate("INSERT INTO employees (name) VALUES (?)")
    check("INSERT 補上 RETURNING id",
          got == "INSERT INTO employees (name) VALUES (%s) RETURNING id", got)

    got = translate("INSERT OR IGNORE INTO assignments (work_date) VALUES (?)")
    check("INSERT OR IGNORE 換成 ON CONFLICT DO NOTHING",
          got == "INSERT INTO assignments (work_date) VALUES (%s) "
                 "ON CONFLICT DO NOTHING RETURNING id", got)

    got = translate("UPDATE x SET decided_at = datetime('now','localtime') WHERE id = ?")
    check("datetime('now','localtime') 換成 PostgreSQL 寫法",
          "to_char(now() AT TIME ZONE" in got and "datetime(" not in got, got)

    got = translate("SELECT * FROM t WHERE note = 'what?' AND id = ?")
    check("字串常值裡的 ? 不會被換掉",
          got == "SELECT * FROM t WHERE note = 'what?' AND id = %s", got)

    got = translate("SELECT * FROM t WHERE name LIKE 'a%' AND id = ?")
    check("字串常值裡的 % 不會被跳脫",
          got == "SELECT * FROM t WHERE name LIKE 'a%' AND id = %s", got)

    got = translate("SELECT 100 % 7 AS r")
    check("字串外的 % 會跳脫成 %%", got == "SELECT 100 %% 7 AS r", got)


# ==================================================================
# 2. 連線字串整理
# ==================================================================

def test_url():
    from scheduler.db import DbUrlError, db_url_warnings, normalize_db_url

    print("\n[2] Supabase 連線字串處理")

    got = normalize_db_url("postgresql://postgres.abc:pa/ss@aws-1.pooler.supabase.com:5432/postgres")
    check("密碼裡的 / 會被編碼成 %2F", "pa%2Fss@" in got, got)
    check("自動補上 sslmode=require", "sslmode=require" in got, got)

    got = normalize_db_url("postgresql://postgres.abc:pa%2Fss@h.pooler.supabase.com:5432/postgres")
    check("已編碼的密碼不會被重複編碼", "pa%2Fss@" in got and "%252F" not in got, got)

    try:
        normalize_db_url("postgresql://postgres.abc:[YOUR-PASSWORD]@h.pooler.supabase.com:5432/postgres")
        check("沒換掉的 [YOUR-PASSWORD] 會被擋下", False, "沒有丟出例外")
    except DbUrlError:
        check("沒換掉的 [YOUR-PASSWORD] 會被擋下", True)

    try:
        normalize_db_url("mysql://a:b@c/d")
        check("非 postgresql:// 開頭會被擋下", False, "沒有丟出例外")
    except DbUrlError:
        check("非 postgresql:// 開頭會被擋下", True)

    warns = db_url_warnings("postgresql://postgres:pw@db.abcdefg.supabase.co:5432/postgres")
    check("用直連位址會警告 IPv6 問題",
          any("IPv6" in w for w in warns), str(warns))

    warns = db_url_warnings("postgresql://postgres.abc:pw@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres")
    check("用 pooler 位址不會誤報", not warns, str(warns))


# ==================================================================
# 3. 端對端:兩種資料庫跑同一套業務邏輯
# ==================================================================

def run_crud_suite(label: str):
    """在目前設定的資料庫上,把整套 CRUD 加排班跑一遍。"""
    from scheduler import repo
    from scheduler.scheduling import run_schedule

    print(f"\n[{label}] 端對端測試")

    emp_id = repo.create_employee({
        "name": "測試員工", "employee_no": "T999", "skills": "收銀",
        "max_shifts_per_week": 5, "min_shifts_per_week": 0,
    })
    check("新增員工", bool(emp_id))
    check("讀取員工", (repo.get_employee(emp_id) or {}).get("name") == "測試員工")

    repo.update_employee(emp_id, {"phone": "0911-222-333"})
    check("修改員工", repo.get_employee(emp_id)["phone"] == "0911-222-333")

    shift_id = repo.create_shift_type({
        "name": "測試班", "start_time": "09:00", "end_time": "17:00",
        "required_headcount": 1,
    })
    check("新增班別", bool(shift_id))
    repo.update_shift_type(shift_id, {"required_headcount": 2})
    check("修改班別", repo.get_shift_type(shift_id)["required_headcount"] == 2)

    leave_id = repo.create_leave({
        "employee_id": emp_id, "start_date": "2030-01-10",
        "end_date": "2030-01-12", "leave_type": "特休", "status": "pending",
    })
    check("新增請假", bool(leave_id))
    repo.update_leave(leave_id, {"status": "approved"})
    updated = repo.get_leave(leave_id)
    check("核准請假並記下時間", updated["status"] == "approved" and bool(updated["decided_at"]))

    a_id = repo.create_assignment({
        "work_date": "2030-01-20", "shift_type_id": shift_id, "employee_id": emp_id,
    })
    check("新增班次", bool(a_id))
    dup = repo.create_assignment({
        "work_date": "2030-01-20", "shift_type_id": shift_id, "employee_id": emp_id,
    })
    check("重複的班次會被擋下並回傳 0", dup == 0, f"回傳 {dup}")

    swap_id = repo.create_swap({
        "assignment_id": a_id, "requester_id": emp_id,
        "target_date": "2030-01-21", "reason": "測試",
    })
    check("新增調班申請", bool(swap_id))
    repo.decide_swap(swap_id, "approved")
    check("核准調班會改掉班次日期",
          repo.get_assignment(a_id)["work_date"] == "2030-01-21")

    check("請假區間查詢", "2030-01-11" in repo.leave_map("2030-01-01", "2030-01-31").get(emp_id, set()))
    check("班數統計", any(s["id"] == emp_id for s in repo.workload_stats("2030-01-01", "2030-01-31")))

    result = run_schedule("2030-02-01", "2030-02-07", engine="rules")
    check("規則排班跑得動", result["count"] > 0, str(result))
    result = run_schedule("2030-02-01", "2030-02-07", engine="solver", time_limit_sec=10)
    check("最佳化排班跑得動", result["count"] > 0, str(result))

    check("刪除請假", bool(repo.delete_leave(leave_id)))
    check("刪除班次", bool(repo.delete_assignment(repo.list_assignments("2030-01-21", "2030-01-21")[0]["id"])))
    check("刪除員工", bool(repo.delete_employee(emp_id)))
    check("刪除員工後班次一併消失(外鍵串聯)",
          not [a for a in repo.list_assignments("2030-01-01", "2030-12-31")
               if a["employee_id"] == emp_id])
    check("刪除班別", bool(repo.delete_shift_type(shift_id)))


def test_sqlite():
    import config
    from app import create_app

    with tempfile.TemporaryDirectory() as tmp:
        config.Config.DATABASE_URL = ""
        config.Config.DATABASE_URL_ERROR = ""
        config.Config.DB_PATH = str(Path(tmp) / "test.db")
        app = create_app(config.Config)
        with app.app_context():
            run_crud_suite("3] SQLite [")


def test_postgres(url: str):
    import config
    from app import create_app
    from scheduler import db

    from scheduler.db import connect_postgres, normalize_db_url

    url = normalize_db_url(url) if "supabase" in url else url

    # 每次都用乾淨的 schema,免得測試資料汙染正式資料
    conn = connect_postgres(url)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("DROP SCHEMA IF EXISTS shift_test CASCADE")
        cur.execute("CREATE SCHEMA shift_test")
    conn.close()

    test_url = url + ("&" if "?" in url else "?") + "options=-csearch_path%3Dshift_test"

    db.reset_pool()
    config.Config.DATABASE_URL = test_url
    config.Config.DATABASE_URL_ERROR = ""
    app = create_app(config.Config)
    if app.config.get("DB_ERROR"):
        check("PostgreSQL 連線", False, app.config["DB_ERROR"])
        return
    with app.app_context():
        run_crud_suite("4] PostgreSQL [")
    db.reset_pool()

    conn = connect_postgres(url)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("DROP SCHEMA IF EXISTS shift_test CASCADE")
    conn.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pg", default=os.getenv("TEST_PG_URL", ""),
                        help="要一起測試的 PostgreSQL 連線字串")
    args = parser.parse_args()

    print("=" * 62)
    print("  自動排班系統 — 資料庫測試")
    print("=" * 62)

    test_translate()
    test_url()
    test_sqlite()
    if args.pg:
        test_postgres(args.pg)
    else:
        print("\n[4] PostgreSQL 端對端測試:略過(沒給 --pg 連線字串)")

    print("\n" + "=" * 62)
    print(f"  通過 {len(PASS)} 項,失敗 {len(FAIL)} 項")
    if FAIL:
        for name in FAIL:
            print(f"    X {name}")
    print("=" * 62)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
