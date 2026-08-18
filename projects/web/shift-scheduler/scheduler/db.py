"""資料庫連線層,同時支援 Supabase(PostgreSQL)與本機 SQLite。

為什麼留兩套:
  Supabase 是正式環境,資料放雲端、多台裝置共用、手機也連得到。
  但沒網路或還沒申請帳號時要能開發測試,所以保留 SQLite 當退路。

上層的 repo.py 只寫一種 SQL(SQLite 風格,用 ? 當參數),
由這一層翻譯成 PostgreSQL 認得的語法,所以換資料庫不必改業務邏輯。
"""

import logging
import re
import sqlite3
import urllib.parse

from flask import current_app, g

log = logging.getLogger(__name__)

SQLITE = "sqlite"
POSTGRES = "postgres"

# psycopg2 是連 PostgreSQL 用的驅動,anaconda 已內建。
# 沒有的話只影響 Supabase 模式,SQLite 照常運作。
try:
    import psycopg2
    import psycopg2.extras
    import psycopg2.pool
    HAS_PSYCOPG2 = True
except ImportError:                                     # pragma: no cover
    psycopg2 = None
    HAS_PSYCOPG2 = False


# ==================================================================
# 連線字串處理
# ==================================================================

class DbUrlError(ValueError):
    """連線字串有問題時丟出,訊息直接寫給使用者看。"""


def normalize_db_url(raw: str) -> str:
    """把 Supabase 後台複製來的連線字串整理成可用的形式。

    處理三個很常踩的狀況:
      1. 後台複製時會連 [YOUR-PASSWORD] 這種佔位符一起帶上
      2. 密碼含 / @ # 等符號,沒編碼會讓連線字串被切錯位置
      3. 少了 sslmode,Supabase 一定要走 SSL
    """
    url = (raw or "").strip().strip('"').strip("'")
    if not url:
        return ""

    if "[" in url or "]" in url:
        raise DbUrlError(
            "連線字串裡還有 [ ] 佔位符,請把 [YOUR-PASSWORD] 換成真正的資料庫密碼。"
        )

    if not url.startswith(("postgresql://", "postgres://")):
        raise DbUrlError("連線字串要以 postgresql:// 開頭。")

    # 密碼段落做 URL 編碼(已編碼過的不會被重複編碼)
    match = re.match(r"^(postgres(?:ql)?://)([^:/@]+):(.*)@([^@]+)$", url)
    if match:
        scheme, user, password, rest = match.groups()
        safe = urllib.parse.quote(urllib.parse.unquote(password), safe="")
        url = f"{scheme}{user}:{safe}@{rest}"

    if "sslmode=" not in url:
        url += ("&" if "?" in url else "?") + "sslmode=require"

    return url


def db_url_warnings(url: str) -> list:
    """檢查連線字串常見問題,回傳提醒清單(只提醒,不擋。)"""
    warnings = []
    match = re.search(r"@([^/:?]+)", url or "")
    host = match.group(1) if match else ""

    if re.match(r"^db\.[a-z0-9]+\.supabase\.co$", host):
        warnings.append(
            "你填的是 Supabase 直連主機(db.xxx.supabase.co),它只有 IPv6 位址。"
            "這台電腦沒有對外 IPv6,一定連不上 —— 請改用後台的 Connection Pooler "
            "位址(長得像 aws-1-ap-southeast-1.pooler.supabase.com)。"
        )
    return warnings


# ==================================================================
# 後端判斷
# ==================================================================

def backend() -> str:
    """目前用哪個資料庫。有填 Supabase 連線字串就用 Supabase。"""
    return POSTGRES if current_app.config.get("DATABASE_URL") else SQLITE


def backend_label() -> str:
    return "Supabase (PostgreSQL)" if backend() == POSTGRES else "本機 SQLite"


# ==================================================================
# 連線池(Supabase 用)
# ==================================================================

_pool = None


def get_pool():
    """Supabase 在雲端,每次請求都重連太慢,所以用連線池重複利用連線。"""
    global _pool
    if _pool is None:
        if not HAS_PSYCOPG2:
            raise RuntimeError(
                "要連 Supabase 需要 psycopg2,請執行:pip install psycopg2-binary"
            )
        _pool = psycopg2.pool.ThreadedConnectionPool(
            1,
            int(current_app.config.get("DB_POOL_SIZE", 8)),
            current_app.config["DATABASE_URL"],
            connect_timeout=int(current_app.config.get("DB_CONNECT_TIMEOUT", 10)),
            application_name="shift-scheduler",
        )
    return _pool


def reset_pool():
    """設定改了或連線壞掉時,把連線池整個丟掉重來。"""
    global _pool
    if _pool is not None:
        try:
            _pool.closeall()
        except Exception:                               # noqa: BLE001
            pass
        _pool = None


# ==================================================================
# 每個請求一條連線
# ==================================================================

def get_db():
    if "db" not in g:
        if backend() == POSTGRES:
            conn = get_pool().getconn()
            conn.autocommit = True      # 每句自動送出,免得連線池留著沒關的交易
            g.db_pooled = True
        else:
            conn = sqlite3.connect(current_app.config["DB_PATH"])
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON")
            g.db_pooled = False
        g.db = conn
    return g.db


def close_db(_exc=None):
    conn = g.pop("db", None)
    if conn is None:
        return
    if g.pop("db_pooled", False):
        try:
            get_pool().putconn(conn)    # 還回連線池,不是真的關掉
        except Exception:               # noqa: BLE001
            pass
    else:
        conn.close()


def _cursor(conn):
    if backend() == POSTGRES:
        return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return conn.cursor()


# ==================================================================
# SQL 方言翻譯
# ==================================================================

_NOW_SQLITE = "datetime('now','localtime')"
_NOW_PG = "to_char(now() AT TIME ZONE 'Asia/Taipei','YYYY-MM-DD HH24:MI:SS')"


def _swap_placeholders(sql: str) -> str:
    """? 換成 %s。字串常值裡的 ? 不動,原本的 % 要跳脫成 %%。"""
    out = []
    in_string = False
    for ch in sql:
        if ch == "'":
            in_string = not in_string
            out.append(ch)
        elif ch == "%" and not in_string:
            out.append("%%")
        elif ch == "?" and not in_string:
            out.append("%s")
        else:
            out.append(ch)
    return "".join(out)


def translate(sql: str) -> str:
    """SQLite 風格的 SQL 翻成 PostgreSQL。"""
    sql = sql.replace(_NOW_SQLITE, _NOW_PG)

    conflict = ""
    if re.match(r"\s*INSERT\s+OR\s+IGNORE\s+INTO", sql, re.IGNORECASE):
        sql = re.sub(r"\s*INSERT\s+OR\s+IGNORE\s+INTO", "INSERT INTO", sql,
                     count=1, flags=re.IGNORECASE)
        conflict = " ON CONFLICT DO NOTHING"

    if re.match(r"\s*INSERT\s+INTO", sql, re.IGNORECASE):
        sql = sql.rstrip().rstrip(";") + conflict + " RETURNING id"

    return _swap_placeholders(sql)


# ==================================================================
# 查詢 / 寫入
# ==================================================================

def query(sql: str, params=(), one: bool = False):
    conn = get_db()
    is_pg = backend() == POSTGRES
    cur = _cursor(conn)
    try:
        cur.execute(translate(sql) if is_pg else sql, tuple(params))
        rows = cur.fetchall()
    finally:
        cur.close()
    if one:
        return rows[0] if rows else None
    return rows


def execute(sql: str, params=()) -> int:
    """執行寫入。

    INSERT 回傳新資料的 id(被 OR IGNORE 擋掉時回傳 0);
    UPDATE / DELETE 回傳異動筆數。
    """
    conn = get_db()
    is_pg = backend() == POSTGRES
    is_insert = sql.lstrip().upper().startswith("INSERT")
    cur = _cursor(conn)
    try:
        cur.execute(translate(sql) if is_pg else sql, tuple(params))
        if is_insert:
            if is_pg:
                row = cur.fetchone() if cur.description else None
                result = row["id"] if row else 0
            else:
                # rowcount 為 0 代表 INSERT OR IGNORE 被擋下,
                # 這時 lastrowid 還是上一筆的舊值,不能拿來當成功依據
                result = cur.lastrowid if cur.rowcount else 0
        else:
            result = cur.rowcount
    finally:
        cur.close()
    if not getattr(conn, "autocommit", False):
        conn.commit()
    return result


# ==================================================================
# 資料表結構
# ==================================================================

SCHEMA_SQLITE = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS employees (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    name                TEXT    NOT NULL,
    employee_no         TEXT,
    phone               TEXT    DEFAULT '',
    line_user_id        TEXT,
    role                TEXT    NOT NULL DEFAULT 'staff',
    skills              TEXT    NOT NULL DEFAULT '',
    max_shifts_per_week INTEGER NOT NULL DEFAULT 5,
    min_shifts_per_week INTEGER NOT NULL DEFAULT 0,
    active              INTEGER NOT NULL DEFAULT 1,
    created_at          TEXT    NOT NULL DEFAULT (datetime('now','localtime'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_emp_line ON employees(line_user_id)
    WHERE line_user_id IS NOT NULL AND line_user_id <> '';

CREATE TABLE IF NOT EXISTS shift_types (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    name               TEXT    NOT NULL,
    code               TEXT    NOT NULL DEFAULT '',
    start_time         TEXT    NOT NULL,
    end_time           TEXT    NOT NULL,
    required_headcount INTEGER NOT NULL DEFAULT 1,
    required_skill     TEXT    NOT NULL DEFAULT '',
    color              TEXT    NOT NULL DEFAULT '#D98E5A',
    sort_order         INTEGER NOT NULL DEFAULT 0,
    active             INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS leave_requests (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    start_date  TEXT    NOT NULL,
    end_date    TEXT    NOT NULL,
    leave_type  TEXT    NOT NULL DEFAULT '特休',
    reason      TEXT    NOT NULL DEFAULT '',
    status      TEXT    NOT NULL DEFAULT 'pending',
    source      TEXT    NOT NULL DEFAULT 'web',
    created_at  TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    decided_at  TEXT
);
CREATE INDEX IF NOT EXISTS idx_leave_emp ON leave_requests(employee_id, start_date);

CREATE TABLE IF NOT EXISTS assignments (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    work_date     TEXT    NOT NULL,
    shift_type_id INTEGER NOT NULL REFERENCES shift_types(id) ON DELETE CASCADE,
    employee_id   INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    locked        INTEGER NOT NULL DEFAULT 0,
    status        TEXT    NOT NULL DEFAULT 'draft',
    note          TEXT    NOT NULL DEFAULT '',
    created_at    TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    UNIQUE(work_date, shift_type_id, employee_id)
);
CREATE INDEX IF NOT EXISTS idx_assign_date ON assignments(work_date);
CREATE INDEX IF NOT EXISTS idx_assign_emp ON assignments(employee_id, work_date);

CREATE TABLE IF NOT EXISTS swap_requests (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id        INTEGER NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    requester_id         INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    target_shift_type_id INTEGER REFERENCES shift_types(id) ON DELETE SET NULL,
    target_date          TEXT,
    reason               TEXT    NOT NULL DEFAULT '',
    status               TEXT    NOT NULL DEFAULT 'pending',
    source               TEXT    NOT NULL DEFAULT 'web',
    created_at           TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    decided_at           TEXT
);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""

SCHEMA_POSTGRES = """
CREATE TABLE IF NOT EXISTS employees (
    id                  INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name                TEXT    NOT NULL,
    employee_no         TEXT,
    phone               TEXT    DEFAULT '',
    line_user_id        TEXT,
    role                TEXT    NOT NULL DEFAULT 'staff',
    skills              TEXT    NOT NULL DEFAULT '',
    max_shifts_per_week INTEGER NOT NULL DEFAULT 5,
    min_shifts_per_week INTEGER NOT NULL DEFAULT 0,
    active              INTEGER NOT NULL DEFAULT 1,
    created_at          TEXT    NOT NULL DEFAULT to_char(now() AT TIME ZONE 'Asia/Taipei','YYYY-MM-DD HH24:MI:SS')
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_emp_line ON employees(line_user_id)
    WHERE line_user_id IS NOT NULL AND line_user_id <> '';

CREATE TABLE IF NOT EXISTS shift_types (
    id                 INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name               TEXT    NOT NULL,
    code               TEXT    NOT NULL DEFAULT '',
    start_time         TEXT    NOT NULL,
    end_time           TEXT    NOT NULL,
    required_headcount INTEGER NOT NULL DEFAULT 1,
    required_skill     TEXT    NOT NULL DEFAULT '',
    color              TEXT    NOT NULL DEFAULT '#D98E5A',
    sort_order         INTEGER NOT NULL DEFAULT 0,
    active             INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS leave_requests (
    id          INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    start_date  TEXT    NOT NULL,
    end_date    TEXT    NOT NULL,
    leave_type  TEXT    NOT NULL DEFAULT '特休',
    reason      TEXT    NOT NULL DEFAULT '',
    status      TEXT    NOT NULL DEFAULT 'pending',
    source      TEXT    NOT NULL DEFAULT 'web',
    created_at  TEXT    NOT NULL DEFAULT to_char(now() AT TIME ZONE 'Asia/Taipei','YYYY-MM-DD HH24:MI:SS'),
    decided_at  TEXT
);
CREATE INDEX IF NOT EXISTS idx_leave_emp ON leave_requests(employee_id, start_date);

CREATE TABLE IF NOT EXISTS assignments (
    id            INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    work_date     TEXT    NOT NULL,
    shift_type_id INTEGER NOT NULL REFERENCES shift_types(id) ON DELETE CASCADE,
    employee_id   INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    locked        INTEGER NOT NULL DEFAULT 0,
    status        TEXT    NOT NULL DEFAULT 'draft',
    note          TEXT    NOT NULL DEFAULT '',
    created_at    TEXT    NOT NULL DEFAULT to_char(now() AT TIME ZONE 'Asia/Taipei','YYYY-MM-DD HH24:MI:SS'),
    UNIQUE(work_date, shift_type_id, employee_id)
);
CREATE INDEX IF NOT EXISTS idx_assign_date ON assignments(work_date);
CREATE INDEX IF NOT EXISTS idx_assign_emp ON assignments(employee_id, work_date);

CREATE TABLE IF NOT EXISTS swap_requests (
    id                   INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    assignment_id        INTEGER NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    requester_id         INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    target_shift_type_id INTEGER REFERENCES shift_types(id) ON DELETE SET NULL,
    target_date          TEXT,
    reason               TEXT    NOT NULL DEFAULT '',
    status               TEXT    NOT NULL DEFAULT 'pending',
    source               TEXT    NOT NULL DEFAULT 'web',
    created_at           TEXT    NOT NULL DEFAULT to_char(now() AT TIME ZONE 'Asia/Taipei','YYYY-MM-DD HH24:MI:SS'),
    decided_at           TEXT
);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- 打開 Row Level Security 但不建任何 policy。
-- 效果:Supabase 對外的 anon / authenticated 金鑰完全讀不到這些表,
-- 我們用資料庫帳號直連則不受影響(該角色會略過 RLS)。
-- 員工姓名電話是個資,不該讓拿到前端金鑰的人直接撈走。
ALTER TABLE employees      ENABLE ROW LEVEL SECURITY;
ALTER TABLE shift_types    ENABLE ROW LEVEL SECURITY;
ALTER TABLE leave_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE assignments    ENABLE ROW LEVEL SECURITY;
ALTER TABLE swap_requests  ENABLE ROW LEVEL SECURITY;
ALTER TABLE settings       ENABLE ROW LEVEL SECURITY;
"""


def connect_postgres(url: str, timeout: int = 10):
    """開一條不經連線池的 PostgreSQL 連線,給建表與搬資料的腳本用。"""
    if not HAS_PSYCOPG2:
        raise RuntimeError("要連 Supabase 需要 psycopg2,請執行:pip install psycopg2-binary")
    return psycopg2.connect(url, connect_timeout=timeout)


def init_db(app) -> None:
    """建立資料表(可重複執行)。在 app context 外面呼叫,所以直接吃 app。"""
    url = app.config.get("DATABASE_URL")
    if url:
        conn = connect_postgres(url, int(app.config.get("DB_CONNECT_TIMEOUT", 10)))
        try:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(SCHEMA_POSTGRES)
        finally:
            conn.close()
        log.info("Supabase 資料表已就緒")
    else:
        conn = sqlite3.connect(app.config["DB_PATH"])
        try:
            conn.executescript(SCHEMA_SQLITE)
            conn.commit()
        finally:
            conn.close()
