# -*- coding: utf-8 -*-
"""自動的小龍蝦 — 本機伺服器。啟動：python app.py → http://localhost:5566"""
import datetime, json, os
from flask import Flask, jsonify, request, send_from_directory
import db, engine
from llm import load_config, save_config
from roles import ROLES, ROLE_MAP, DEPARTMENTS

app = Flask(__name__, static_folder="static")
db.init()


@app.get("/")
def home():
    return send_from_directory("static", "index.html")


@app.get("/api/state")
def state():
    fx = load_config()["FX_USD_TWD"]
    def led(kind):
        r = db.q("SELECT SUM(amount_twd) s FROM ledger WHERE kind=?", (kind,), one=True)
        return r["s"] or 0
    day0 = datetime.datetime.now().replace(hour=0, minute=0, second=0).timestamp()
    def led_today(kind):
        r = db.q("SELECT SUM(amount_twd) s FROM ledger WHERE kind=? AND ts>=?", (kind, day0), one=True)
        return r["s"] or 0
    capital = led("capital")
    revenue, cost = led("revenue"), led("cost") + led("api_cost")
    realized = led("invest_realized")
    unrealized = 0
    for p in db.q("SELECT * FROM portfolio WHERE qty>0"):
        unrealized += (p["last_price"] - p["avg_price"]) * p["qty"]
    cash = capital + revenue - cost + realized
    counts = {r["status"]: r["c"] for r in db.q("SELECT status, COUNT(*) c FROM tasks GROUP BY status")}
    running_roles = {r["role_id"] for r in db.q("SELECT role_id FROM tasks WHERE status='running'")}
    waiting_roles = {r["role_id"] for r in db.q("SELECT role_id FROM tasks WHERE status='waiting_approval'")}
    roles = []
    for rid, info in ROLE_MAP.items():
        st = "工作中" if rid in running_roles else ("等待審批" if rid in waiting_roles else "待命")
        roles.append({**{k: info[k] for k in ("id", "name", "en", "dept", "room")},
                      "model": engine.role_model(rid), "status": st})
    return jsonify({
        "finance": {"capital": capital, "cash": cash,
                    "net": cash + unrealized,
                    "revenue_today": led_today("revenue"),
                    "cost_today": led_today("cost") + led_today("api_cost"),
                    "realized": realized, "unrealized": unrealized,
                    "revenue": revenue, "cost": cost},
        "api": {"month_usd": engine.month_api_cost_usd(),
                "budget_usd": load_config()["MONTHLY_BUDGET_USD"]},
        "autopilot": {"on": db.kv_get("autopilot", "off") == "on",
                      "slots": engine.running_count(), "max_slots": engine.MAX_SLOTS},
        "tasks": counts, "roles": roles, "departments": DEPARTMENTS,
        "pending_approvals": len(db.q("SELECT id FROM approvals WHERE status='pending'")),
        "mock_mode": not (load_config().get("GEMINI_API_KEY") or load_config().get("ANTHROPIC_API_KEY")),
    })


@app.get("/api/tasks")
def tasks():
    rows = db.q("SELECT * FROM tasks ORDER BY id DESC LIMIT 100")
    for r in rows:
        r["role_name"] = ROLE_MAP.get(r["role_id"], {}).get("name", r["role_id"] or "-")
    return jsonify(rows)


@app.post("/api/tasks")
def add_task():
    d = request.json or {}
    kind = d.get("kind", "generic")
    role = d.get("role_id") or {"product": "pm_a", "design": "vis_des", "copy": "copy_agent",
                                "seo": "crawler", "invest": "inv_mgr", "sales": "sales_strat",
                                "meeting": "meet_host", "finance": "fin_rep"}.get(kind, "gm")
    dept = ROLE_MAP.get(role, {}).get("dept", "經營管理部")
    tid = db.x("INSERT INTO tasks(title,kind,dept,role_id,input,created,updated) VALUES(?,?,?,?,?,?,?)",
               (d.get("title", "未命名任務"), kind, dept, role, d.get("input", ""), db.now(), db.now()))
    db.audit_log("老闆", "建立任務", dept=dept, detail=d.get("title", ""))
    return jsonify({"id": tid})


@app.post("/api/tasks/<int:tid>/run")
def run_now(tid):
    import threading
    threading.Thread(target=engine.run_task, args=(tid,), daemon=True).start()
    return jsonify({"ok": True})


@app.post("/api/autopilot")
def toggle_ap():
    on = (request.json or {}).get("on", False)
    db.kv_set("autopilot", "on" if on else "off")
    db.audit_log("老闆", "啟動自動工作" if on else "停止自動工作")
    return jsonify({"ok": True})


@app.get("/api/approvals")
def approvals():
    return jsonify(db.q("SELECT * FROM approvals ORDER BY id DESC LIMIT 50"))


@app.post("/api/approvals/<int:aid>")
def decide(aid):
    ok = engine.decide_approval(aid, (request.json or {}).get("approve", False))
    return jsonify({"ok": ok})


@app.get("/api/ledger")
def ledger():
    return jsonify(db.q("SELECT * FROM ledger ORDER BY id DESC LIMIT 200"))


@app.post("/api/capital")
def capital():
    amt = float((request.json or {}).get("amount", 0))
    if amt:
        db.ledger_add("capital", amt, (request.json or {}).get("note", "初始資本"))
        db.audit_log("老闆", "設定初始資本", dept="會計部", detail=str(amt))
    return jsonify({"ok": True})


@app.get("/api/audit")
def audit():
    return jsonify(db.q("SELECT * FROM audit ORDER BY id DESC LIMIT 200"))


@app.get("/api/reports")
def reports():
    return jsonify(db.q("SELECT * FROM reports ORDER BY id DESC LIMIT 50"))


@app.get("/api/portfolio")
def portfolio():
    return jsonify({"positions": db.q("SELECT * FROM portfolio WHERE qty>0"),
                    "trades": db.q("SELECT * FROM trades ORDER BY id DESC LIMIT 50")})


@app.get("/api/drafts")
def drafts():
    return jsonify(db.q("SELECT * FROM drafts ORDER BY id DESC LIMIT 50"))


@app.get("/api/sales")
def sales():
    return jsonify({"leads": db.q("SELECT * FROM leads ORDER BY id DESC LIMIT 50"),
                    "orders": db.q("SELECT * FROM orders_ ORDER BY id DESC LIMIT 50")})


@app.post("/api/orders")
def add_order():
    d = request.json or {}
    amt = float(d.get("amount", 0))
    db.x("INSERT INTO orders_(ts,product,amount_twd) VALUES(?,?,?)",
         (db.now(), d.get("product", "產品"), amt))
    db.ledger_add("revenue", amt, "訂單：" + d.get("product", ""))
    db.audit_log("訂單管理", "新增訂單", dept="業務部", detail=d.get("product", ""))
    return jsonify({"ok": True})


@app.post("/api/roles/<rid>/model")
def set_model(rid):
    m = (request.json or {}).get("model", "gemini")
    db.x("INSERT INTO role_over(role_id,model) VALUES(?,?) ON CONFLICT(role_id) DO UPDATE SET model=?",
         (rid, m, m))
    return jsonify({"ok": True})


@app.get("/api/config")
def get_config():
    c = load_config()
    return jsonify({"has_gemini": bool(c.get("GEMINI_API_KEY")),
                    "has_claude": bool(c.get("ANTHROPIC_API_KEY")),
                    "budget": c["MONTHLY_BUDGET_USD"], "fx": c["FX_USD_TWD"]})


@app.post("/api/config")
def set_config():
    c = load_config()
    d = request.json or {}
    for k in ("GEMINI_API_KEY", "ANTHROPIC_API_KEY"):
        if d.get(k) is not None:
            c[k] = d[k]
    if d.get("budget"):
        c["MONTHLY_BUDGET_USD"] = float(d["budget"])
    save_config(c)
    return jsonify({"ok": True})


if __name__ == "__main__":
    # 自動駕駛已停用。它是一個 while True 迴圈，每 8 秒呼叫一次 LLM，
    # 放在雲端 24 小時執行會持續產生 API 費用。
    # 要在本機試用時再把下面這行的井號拿掉。
    # engine.start_autopilot_thread()

    # 由 Project Hub 啟動時會指派 PORT；單獨執行則沿用 config.json 的設定
    port = int(os.environ.get("PORT") or load_config().get("PORT", 5566))
    print("自動的小龍蝦已啟動 → http://localhost:%s" % port)
    app.run(host="127.0.0.1", port=port, debug=False)
