# -*- coding: utf-8 -*-
"""SQLite 資料層"""
import os, sqlite3, threading, time

DB_PATH = os.path.join(os.path.dirname(__file__), "xiaolongxia.db")
_lock = threading.Lock()

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks(
  id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, kind TEXT, dept TEXT,
  role_id TEXT, status TEXT DEFAULT 'pending', risk TEXT DEFAULT '低',
  input TEXT, output TEXT, cost_usd REAL DEFAULT 0,
  created REAL, updated REAL);
CREATE TABLE IF NOT EXISTS approvals(
  id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER, kind TEXT,
  risk TEXT, payload TEXT, status TEXT DEFAULT 'pending',
  created REAL, decided REAL);
CREATE TABLE IF NOT EXISTS audit(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, actor TEXT, action TEXT,
  dept TEXT, risk TEXT, detail TEXT);
CREATE TABLE IF NOT EXISTS ledger(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, kind TEXT,
  amount_twd REAL, note TEXT);
CREATE TABLE IF NOT EXISTS portfolio(
  id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT UNIQUE, name TEXT,
  qty REAL DEFAULT 0, avg_price REAL DEFAULT 0, last_price REAL DEFAULT 0);
CREATE TABLE IF NOT EXISTS trades(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, symbol TEXT, side TEXT,
  qty REAL, price REAL, status TEXT, note TEXT);
CREATE TABLE IF NOT EXISTS drafts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, channel TEXT, title TEXT,
  content TEXT, status TEXT DEFAULT 'draft');
CREATE TABLE IF NOT EXISTS leads(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, name TEXT, note TEXT,
  status TEXT DEFAULT 'new');
CREATE TABLE IF NOT EXISTS orders_(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, product TEXT,
  amount_twd REAL, status TEXT DEFAULT 'paid');
CREATE TABLE IF NOT EXISTS reports(
  id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, dept TEXT, title TEXT,
  content TEXT);
CREATE TABLE IF NOT EXISTS role_over(
  role_id TEXT PRIMARY KEY, model TEXT);
CREATE TABLE IF NOT EXISTS kv(k TEXT PRIMARY KEY, v TEXT);
"""


def conn():
    c = sqlite3.connect(DB_PATH, timeout=30)
    c.row_factory = sqlite3.Row
    return c


def init():
    with _lock, conn() as c:
        c.executescript(SCHEMA)


def q(sql, args=(), one=False):
    with _lock, conn() as c:
        cur = c.execute(sql, args)
        rows = [dict(r) for r in cur.fetchall()]
    return (rows[0] if rows else None) if one else rows


def x(sql, args=()):
    with _lock, conn() as c:
        cur = c.execute(sql, args)
        return cur.lastrowid


def now():
    return time.time()


def audit_log(actor, action, dept="", risk="低", detail=""):
    x("INSERT INTO audit(ts,actor,action,dept,risk,detail) VALUES(?,?,?,?,?,?)",
      (now(), actor, action, dept, risk, detail))


def ledger_add(kind, amount_twd, note=""):
    x("INSERT INTO ledger(ts,kind,amount_twd,note) VALUES(?,?,?,?)",
      (now(), kind, amount_twd, note))


def kv_get(k, default=""):
    r = q("SELECT v FROM kv WHERE k=?", (k,), one=True)
    return r["v"] if r else default


def kv_set(k, v):
    x("INSERT INTO kv(k,v) VALUES(?,?) ON CONFLICT(k) DO UPDATE SET v=?",
      (k, str(v), str(v)))
