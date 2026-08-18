"""檢查資料庫連線,並把常見的設定錯誤講清楚。

用法:
    python scripts/db_check.py

會做四件事:
    1. 看 .env 有沒有填 Supabase 連線字串
    2. 檢查字串格式(佔位符沒換掉、用了連不上的 IPv6 直連位址…)
    3. 真的連連看,回報連線時間
    4. 列出資料表與各表筆數
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import Config                                  # noqa: E402
from scheduler import db                                   # noqa: E402

TABLES = ["employees", "shift_types", "leave_requests",
          "assignments", "swap_requests", "settings"]


def mask(url: str) -> str:
    """把密碼遮掉再印出來,免得截圖外流。"""
    import re
    return re.sub(r"(://[^:]+:)([^@]+)(@)", r"\1********\3", url)


def main() -> int:
    print()
    print("=" * 62)
    print("  自動排班系統 — 資料庫連線檢查")
    print("=" * 62)

    if Config.DATABASE_URL_ERROR:
        print(f"\n[X] 連線字串有問題:{Config.DATABASE_URL_ERROR}")
        print("    請修改 .env 的 SUPABASE_DB_URL。")
        return 1

    if not Config.DATABASE_URL:
        print("\n[i] 目前使用:本機 SQLite")
        print(f"    資料庫檔案:{Config.DB_PATH}")
        print(f"    檔案存在:{'是' if Path(Config.DB_PATH).exists() else '否(第一次啟動會自動建立)'}")
        print("\n    要改用 Supabase,請在 .env 填入 SUPABASE_DB_URL。")
        print("    格式範例寫在 .env.example。")
        return 0

    print("\n[i] 目前使用:Supabase (PostgreSQL)")
    print(f"    連線字串:{mask(Config.DATABASE_URL)}")

    for warn in db.db_url_warnings(Config.DATABASE_URL):
        print(f"\n[!] {warn}")

    if not db.HAS_PSYCOPG2:
        print("\n[X] 找不到 psycopg2,無法連線。")
        print("    請執行:pip install psycopg2-binary")
        return 1

    print("\n    連線中…", end="", flush=True)
    t0 = time.time()
    try:
        conn = db.connect_postgres(Config.DATABASE_URL, Config.DB_CONNECT_TIMEOUT)
    except Exception as exc:                               # noqa: BLE001
        print(" 失敗")
        print(f"\n[X] {exc}")
        print(diagnose(str(exc)))
        return 1
    elapsed = (time.time() - t0) * 1000
    print(f" 成功({elapsed:.0f} ms)")

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT version()")
            print(f"\n    伺服器:{cur.fetchone()[0].split(',')[0]}")

            existing = []
            print("\n    資料表:")
            for table in TABLES:
                cur.execute("SELECT to_regclass(%s)", (f"public.{table}",))
                if cur.fetchone()[0] is None:
                    print(f"      {table:<16} 尚未建立")
                    continue
                existing.append(table)
                cur.execute(f"SELECT count(*) FROM {table}")
                print(f"      {table:<16} {cur.fetchone()[0]:>6} 筆")

            if not existing:
                print("\n[!] 一張表都還沒建立。")
                print("    直接啟動 python app.py 會自動建表,")
                print("    或把 supabase_schema.sql 貼到 Supabase 後台的 SQL Editor 執行。")
    finally:
        conn.close()

    print("\n[v] 檢查完成。")
    return 0


def diagnose(message: str) -> str:
    """把 psycopg2 的英文錯誤翻成看得懂的處理方式。"""
    low = message.lower()
    if "network is unreachable" in low or "cannot assign requested address" in low:
        return ("    → 這通常是 IPv6 的問題。Supabase 的直連位址 db.xxx.supabase.co\n"
                "      只有 IPv6,這台電腦連不上。請改用後台的 Connection Pooler 位址\n"
                "      (主機名含 pooler.supabase.com,使用者名稱是 postgres.專案代號)。")
    if "password authentication failed" in low:
        return ("    → 密碼錯了。到 Supabase 後台 Project Settings > Database\n"
                "      可以重設資料庫密碼。注意使用者名稱要是 postgres.專案代號。")
    if "timeout" in low or "timed out" in low:
        return ("    → 連線逾時。檢查網路,或確認防火牆沒擋 5432 埠。")
    if "does not support ssl" in low:
        return ("    → 對方不支援 SSL。Supabase 一定要 SSL,會出現這個訊息通常是連到\n"
                "      本機或自架的資料庫。那種情況在連線字串結尾加上 ?sslmode=disable。")
    if "could not translate host name" in low or "name or service not known" in low:
        return ("    → 主機名稱打錯了,請重新從 Supabase 後台複製一次。")
    if "does not exist" in low and "database" in low:
        return ("    → 資料庫名稱錯了,Supabase 的資料庫名稱固定是 postgres。")
    return "    → 請把上面的錯誤訊息對照 README 的「Supabase 設定」一節。"


if __name__ == "__main__":
    raise SystemExit(main())
