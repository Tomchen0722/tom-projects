"""SQLite 連線與資料表結構。

用 sqlite3 而不是 ORM,因為單店/連鎖小店的資料量小,少一層依賴好維護。
"""

import sqlite3
from flask import g, current_app

SCHEMA = """
PRAGMA foreign_keys = ON;

-- 員工
CREATE TABLE IF NOT EXISTS employees (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    name                TEXT    NOT NULL,
    employee_no         TEXT,
    phone               TEXT    DEFAULT '',
    line_user_id        TEXT,
    role                TEXT    NOT NULL DEFAULT 'staff',   -- staff / manager
    skills              TEXT    NOT NULL DEFAULT '',        -- 逗號分隔,例:收銀,咖啡
    max_shifts_per_week INTEGER NOT NULL DEFAULT 5,
    min_shifts_per_week INTEGER NOT NULL DEFAULT 0,
    active              INTEGER NOT NULL DEFAULT 1,
    created_at          TEXT    NOT NULL DEFAULT (datetime('now','localtime'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_emp_line ON employees(line_user_id)
    WHERE line_user_id IS NOT NULL AND line_user_id <> '';

-- 班別(早班/晚班/大夜…)
CREATE TABLE IF NOT EXISTS shift_types (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    name               TEXT    NOT NULL,
    code               TEXT    NOT NULL DEFAULT '',
    start_time         TEXT    NOT NULL,          -- HH:MM
    end_time           TEXT    NOT NULL,          -- HH:MM,小於 start_time 視為跨夜
    required_headcount INTEGER NOT NULL DEFAULT 1,
    required_skill     TEXT    NOT NULL DEFAULT '',
    color              TEXT    NOT NULL DEFAULT '#D98E5A',
    sort_order         INTEGER NOT NULL DEFAULT 0,
    active             INTEGER NOT NULL DEFAULT 1
);

-- 請假 / 不可排班日
CREATE TABLE IF NOT EXISTS leave_requests (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    start_date  TEXT    NOT NULL,                 -- YYYY-MM-DD
    end_date    TEXT    NOT NULL,
    leave_type  TEXT    NOT NULL DEFAULT '特休',
    reason      TEXT    NOT NULL DEFAULT '',
    status      TEXT    NOT NULL DEFAULT 'pending', -- pending/approved/rejected
    source      TEXT    NOT NULL DEFAULT 'web',     -- web/line
    created_at  TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    decided_at  TEXT
);
CREATE INDEX IF NOT EXISTS idx_leave_emp ON leave_requests(employee_id, start_date);

-- 排班結果
CREATE TABLE IF NOT EXISTS assignments (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    work_date     TEXT    NOT NULL,               -- YYYY-MM-DD
    shift_type_id INTEGER NOT NULL REFERENCES shift_types(id) ON DELETE CASCADE,
    employee_id   INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    locked        INTEGER NOT NULL DEFAULT 0,     -- 1=手動鎖定,自動排班不會動
    status        TEXT    NOT NULL DEFAULT 'draft', -- draft/published
    note          TEXT    NOT NULL DEFAULT '',
    created_at    TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    UNIQUE(work_date, shift_type_id, employee_id)
);
CREATE INDEX IF NOT EXISTS idx_assign_date ON assignments(work_date);
CREATE INDEX IF NOT EXISTS idx_assign_emp ON assignments(employee_id, work_date);

-- 調班申請
CREATE TABLE IF NOT EXISTS swap_requests (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id  INTEGER NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    requester_id   INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    target_shift_type_id INTEGER REFERENCES shift_types(id) ON DELETE SET NULL,
    target_date    TEXT,
    reason         TEXT    NOT NULL DEFAULT '',
    status         TEXT    NOT NULL DEFAULT 'pending',
    source         TEXT    NOT NULL DEFAULT 'web',
    created_at     TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    decided_at     TEXT
);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def get_db() -> sqlite3.Connection:
    """取得目前 request 的連線,同一次請求共用一條。"""
    if "db" not in g:
        conn = sqlite3.connect(current_app.config["DB_PATH"])
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        g.db = conn
    return g.db


def close_db(_exc=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()


def init_db(db_path: str) -> None:
    """建立資料表(可重複執行)。"""
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()


def query(sql: str, params=(), one: bool = False):
    cur = get_db().execute(sql, params)
    rows = cur.fetchall()
    cur.close()
    if one:
        return rows[0] if rows else None
    return rows


def execute(sql: str, params=()) -> int:
    """執行寫入,回傳 lastrowid(UPDATE/DELETE 時回傳異動筆數)。"""
    conn = get_db()
    cur = conn.execute(sql, params)
    conn.commit()
    result = cur.lastrowid if sql.lstrip().upper().startswith("INSERT") else cur.rowcount
    cur.close()
    return result
