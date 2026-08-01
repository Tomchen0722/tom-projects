# -*- coding: utf-8 -*-
"""設定 QR 點餐系統的資料庫連線。

密碼輸入時不顯示、自動做 URL 編碼、連線測試通過才寫入 .env，
所以不會留下壞掉的設定。

連線資訊（主機與使用者）優先沿用本機 .env 既有的設定；
沒有的話會請你貼上 Supabase 後台的完整連線字串。
專案識別資訊只存在於本機的 .env，不會寫進程式碼或版控。

執行：  python hub/tools/set_qr_db.py
"""
from __future__ import annotations

import getpass
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent.parent
ENV_PATH = ROOT / "projects" / "web" / "QR_order" / ".env"


def read_existing() -> tuple[str, int, str, str] | None:
    """從既有的 .env 取出 (host, port, user, dbname)。"""
    if not ENV_PATH.exists():
        return None
    for line in ENV_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("DATABASE_URL="):
            continue
        raw = line.split("=", 1)[1].strip()
        try:
            u = urlparse(raw)
            if u.hostname and u.username:
                return (u.hostname, u.port or 5432, unquote(u.username),
                        (u.path or "/postgres").lstrip("/") or "postgres")
        except ValueError:
            return None
    return None


def ask_connection() -> tuple[str, int, str, str] | None:
    """請使用者貼上 Supabase 後台的連線字串，從中解析連線資訊。"""
    print("  找不到既有設定。請到 Supabase 後台複製連線字串：")
    print("  Project Settings > Database > Connection string > Session pooler")
    print()
    raw = input("  貼上連線字串：").strip()
    if not raw:
        return None

    # 後台的字串常帶著 [YOUR-PASSWORD] 之類的佔位符，先移除以免干擾解析
    raw = re.sub(r"\[[^\]]*\]", "PLACEHOLDER", raw)
    try:
        u = urlparse(raw)
    except ValueError:
        print("  無法解析這串連線字串。")
        return None
    if not u.hostname or not u.username:
        print("  這串連線字串缺少主機或使用者名稱。")
        return None
    return (u.hostname, u.port or 5432, unquote(u.username),
            (u.path or "/postgres").lstrip("/") or "postgres")


def main() -> int:
    print("=" * 64)
    print("  QR 點餐系統 — 資料庫連線設定")
    print("=" * 64)

    conn_info = read_existing() or ask_connection()
    if not conn_info:
        print("\n  沒有可用的連線資訊，取消。")
        return 1

    host, port, user, dbname = conn_info
    print(f"  主機：{host}:{port}")
    print(f"  使用者：{user}")
    print()
    print("  密碼可在 Supabase 後台重設：")
    print("  Project Settings > Database > Reset database password")
    print()
    print("  直接貼上密碼原文即可，特殊字元會自動處理。")
    print("  （輸入時畫面不會顯示，屬正常現象）")
    print()

    password = getpass.getpass("  請輸入資料庫密碼：")
    if not password:
        print("\n  未輸入密碼，取消。")
        return 1

    # 從後台複製時常會把 [ ] 佔位符一起帶進來
    if password.startswith("[") and password.endswith("]"):
        password = password[1:-1]
        print("  （偵測到前後的方括號，已自動去除）")

    print()
    print("  正在測試連線…")
    try:
        import psycopg2
    except ImportError:
        print("  找不到 psycopg2，請先執行： pip install psycopg2-binary")
        return 1

    try:
        conn = psycopg2.connect(
            host=host, port=port, user=user,
            password=password, dbname=dbname, connect_timeout=15,
        )
    except psycopg2.Error as exc:
        first = str(exc).strip().splitlines()[0]
        print()
        if "password authentication failed" in first:
            print("  連線失敗：密碼不正確。")
            print("  請到 Supabase 後台重設密碼後再試一次。")
        elif "could not translate host name" in first:
            print("  連線失敗：找不到主機。")
            print("  提醒：不能用直連主機 db.<ref>.supabase.co，")
            print("  它只提供 IPv6；請改用 Session pooler 的主機。")
        else:
            print(f"  連線失敗：{first}")
        print()
        print("  .env 未被修改。")
        return 1

    cur = conn.cursor()
    cur.execute(
        "select table_name from information_schema.tables "
        "where table_schema='public' order by 1"
    )
    tables = [r[0] for r in cur.fetchall()]
    conn.close()

    print("  連線成功。")
    if tables:
        print(f"  現有資料表 {len(tables)} 張：{', '.join(tables)}")
    else:
        print("  資料庫是空的，第一次使用需要先建立資料表：")
        print("    cd projects/web/QR_order")
        print('    python -c "import db_postgres; db_postgres.init_db()"')

    # 連線確認可用之後才寫檔，避免把錯誤的設定留在 .env
    url = f"postgresql://{quote(user, safe='')}:{quote(password, safe='')}@{host}:{port}/{dbname}"
    lines = []
    if ENV_PATH.exists():
        lines = [
            ln for ln in ENV_PATH.read_text(encoding="utf-8").splitlines()
            if not ln.startswith("DATABASE_URL=") and not ln.startswith("# Supabase")
        ]
    lines.append("# Supabase Session Pooler（支援 IPv4）。密碼已做 URL 編碼。")
    lines.append(f"DATABASE_URL={url}")
    ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print()
    print(f"  已寫入 {ENV_PATH.relative_to(ROOT)}")
    print("  這個檔案已被 .gitignore 排除，不會進版控。")
    print()
    print("  現在可以在 Project Hub 上啟動 QR 點餐系統了。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
