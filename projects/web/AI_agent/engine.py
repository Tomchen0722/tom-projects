# -*- coding: utf-8 -*-
"""執行引擎：部門工作流 + Autopilot"""
import datetime, json, threading, time
import db
from llm import call_llm, load_config
from roles import ROLE_MAP

MAX_SLOTS = 3
_running = set()
_slot_lock = threading.Lock()


def role_model(role_id):
    ov = db.q("SELECT model FROM role_over WHERE role_id=?", (role_id,), one=True)
    return ov["model"] if ov else ROLE_MAP[role_id]["model"]


def month_api_cost_usd():
    start = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0).timestamp()
    r = db.q("SELECT SUM(amount_twd) s FROM ledger WHERE kind='api_cost' AND ts>=?",
             (start,), one=True)
    fx = load_config()["FX_USD_TWD"]
    return (r["s"] or 0) / fx


def budget_ok():
    return month_api_cost_usd() < load_config()["MONTHLY_BUDGET_USD"]


def ask(role_id, prompt, task_id=None):
    """讓一個角色思考。回傳文字，成本記帳。"""
    role = ROLE_MAP[role_id]
    if not budget_ok():
        return "【預算閘門】本月 API 預算已用罄，僅能以模擬模式回覆。\n" + \
            call_llm("mock", role["system"], prompt)[0]
    text, cost, used = call_llm(role_model(role_id), role["system"], prompt)
    if cost > 0:
        fx = load_config()["FX_USD_TWD"]
        db.ledger_add("api_cost", cost * fx, "%s(%s)" % (role["name"], used))
        if task_id:
            db.x("UPDATE tasks SET cost_usd=cost_usd+? WHERE id=?", (cost, task_id))
    return text


def report(dept, title, content):
    db.x("INSERT INTO reports(ts,dept,title,content) VALUES(?,?,?,?)",
         (db.now(), dept, title, content))


def need_approval(task_id, kind, risk, payload):
    db.x("INSERT INTO approvals(task_id,kind,risk,payload,created) VALUES(?,?,?,?,?)",
         (task_id, kind, risk, json.dumps(payload, ensure_ascii=False), db.now()))
    db.x("UPDATE tasks SET status='waiting_approval', updated=? WHERE id=?",
         (db.now(), task_id))
    db.audit_log("系統", "送審批", risk=risk, detail=kind)


# ---------- 各部門工作流 ----------

def wf_generic(t):
    out = ask(t["role_id"], t["input"], t["id"])
    return out


def wf_product(t):
    i = t["input"]
    parts = []
    for rid, tag in [("pm_a", "A 穩健"), ("pm_b", "B 創意差異化"), ("pm_c", "C 快速 MVP")]:
        parts.append("## 提案 %s\n%s" % (tag, ask(rid, i, t["id"])))
    out = "\n\n".join(parts)
    gm = ask("gm", "以下是產品開發部三線提案，請給比較結論與建議採用方向：\n" + out[:4000], t["id"])
    out += "\n\n## 總經理講評\n" + gm
    report("產品開發部", "A/B/C 三線提案：" + t["title"], out)
    return out


def wf_design(t):
    v = ask("vis_des", t["input"], t["id"])
    c = ask("color_des", "視覺設計師的方案如下，請給配色方案：\n%s\n\n原始需求：%s" % (v[:3000], t["input"]), t["id"])
    out = "## 視覺設計\n%s\n\n## 配色方案\n%s" % (v, c)
    report("設計部", "設計報告：" + t["title"], out)
    return out


def wf_copy(t):
    out = ask("copy_agent", t["input"], t["id"])
    did = db.x("INSERT INTO drafts(ts,channel,title,content) VALUES(?,?,?,?)",
               (db.now(), "社群", t["title"], out))
    need_approval(t["id"], "貼文草稿", "中", {"draft_id": did, "preview": out[:200]})
    return out + "\n\n（草稿已送審批中心，核准後仍由老闆手動發布）"


def wf_seo(t):
    i = t["input"]
    raw = ask("crawler", "主題：%s。請整理該主題的搜尋環境結構化清單(關鍵字/競品/熱門問答)。" % i, t["id"])
    seo = ask("seo_analyst", "爬蟲資料：\n%s\n請給關鍵字策略與 GEO 建議。" % raw[:3000], t["id"])
    tr = ask("trend_analyst", "爬蟲資料：\n%s\n請給趨勢週期判斷。" % raw[:3000], t["id"])
    opp = ask("opp_analyst", "整合以下三份產出，輸出機會清單(附預估流量/難度)：\n[爬蟲]%s\n[SEO]%s\n[趨勢]%s"
              % (raw[:2000], seo[:2000], tr[:2000]), t["id"])
    out = "## 市場爬蟲\n%s\n\n## SEO 分析\n%s\n\n## 趨勢週期\n%s\n\n## 機會清單\n%s" % (raw, seo, tr, opp)
    report("SEO 分析部", "SEO 流水線：" + t["title"], out)
    return out


def wf_invest(t):
    i = t["input"] or "今日例行盤勢"
    analysts = [("tw_large", "台股權值"), ("tw_theme", "台股題材"), ("us_stock", "美股"),
                ("global_mkt", "全球宏觀"), ("fin_news", "財經新聞"), ("fno", "期權籌碼")]
    views = []
    for rid, tag in analysts:
        views.append("### %s\n%s" % (tag, ask(rid, "分析主題：%s。請給 200 字內觀點與方向(偏多/偏空/中性)。" % i, t["id"])))
    joined = "\n".join(views)
    quant = ask("data_analyst", "六位分析師觀點如下，請量化整理(多空計分、關鍵訊號)：\n" + joined[:5000], t["id"])
    plan = ask("inv_mgr", "分析師觀點與量化訊號如下，請提出模擬盤操作計畫。最後一行務必用 JSON 格式：{\"action\":\"buy|sell|hold\",\"symbol\":\"代號\",\"name\":\"名稱\",\"qty\":數量,\"price\":價格}\n%s\n%s"
               % (joined[:3000], quant[:2000]), t["id"])
    verdict = ask("inv_risk", "投資經理計畫如下，請審核並在最後一行輸出 JSON：{\"verdict\":\"approve|reject\",\"reason\":\"...\"}\n" + plan[:3000], t["id"])
    out = "## 分析師觀點\n%s\n\n## 量化訊號\n%s\n\n## 投資經理計畫\n%s\n\n## 風控審核\n%s" % (joined, quant, plan, verdict)
    trade = _extract_json(plan)
    ok = _extract_json(verdict)
    if trade and trade.get("action") in ("buy", "sell") and ok and ok.get("verdict") == "approve":
        need_approval(t["id"], "模擬交易", "高",
                      {"trade": trade, "reason": ok.get("reason", "")})
        out += "\n\n（模擬交易單已送審批中心，核准後才記入模擬盤）"
    else:
        out += "\n\n（本輪無交易或風控未放行，僅留存報告）"
    report("投資部", "投資決策鏈：" + t["title"], out)
    return out


def wf_sales(t):
    s = ask("sales_strat", t["input"], t["id"])
    d = ask("cust_dev", "策略如下：\n%s\n請列 3 個潛在客戶/合作對象並各擬一段開發訊息草稿。" % s[:3000], t["id"])
    for line in d.split("\n"):
        if line.strip().startswith(("1", "2", "3")) and len(line) > 8:
            db.x("INSERT INTO leads(ts,name,note) VALUES(?,?,?)",
                 (db.now(), line.strip()[:40], "由客戶開發代理人產出"))
    need_approval(t["id"], "客戶開發草稿", "中", {"preview": d[:200]})
    out = "## 業務策略\n%s\n\n## 開發草稿(送審批，不自動寄送)\n%s" % (s, d)
    report("業務部", "銷售開發：" + t["title"], out)
    return out


def wf_meeting(t):
    agenda = ask("meet_host", "會議主題與各方輸入：%s\n請整理議程與重點。" % t["input"], t["id"])
    summary = ask("meet_sec", "議程如下：\n%s\n請輸出會議結論、分工與進度同步。" % agenda[:3000], t["id"])
    out = "## 議程(會議主持)\n%s\n\n## 總結(討論總結)\n%s" % (agenda, summary)
    report("代理人會議部", "會議：" + t["title"], out)
    return out


def wf_finance(t):
    rows = db.q("SELECT kind, SUM(amount_twd) s FROM ledger GROUP BY kind")
    stat = "\n".join("%s: %.1f TWD" % (r["kind"], r["s"] or 0) for r in rows)
    out = ask("fin_rep", "目前帳本彙總如下：\n%s\n請產出財務報告(盈虧、API 成本占比、提醒)。" % stat, t["id"])
    report("會計部", "財務報告：" + t["title"], out)
    return out


def _extract_json(text):
    for line in reversed(text.strip().splitlines()):
        line = line.strip().strip("`")
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except Exception:
                continue
    return None


WORKFLOWS = {
    "generic": wf_generic, "product": wf_product, "design": wf_design,
    "copy": wf_copy, "seo": wf_seo, "invest": wf_invest,
    "sales": wf_sales, "meeting": wf_meeting, "finance": wf_finance,
}


def assess_risk(t):
    txt = ask("risk", "任務：%s / 內容：%s\n請只回一行：風險等級(低/中/高)｜理由(20字內)" % (t["title"], (t["input"] or "")[:200]))
    lvl = "低"
    for k in ("高", "中", "低"):
        if k in txt[:20]:
            lvl = k
            break
    return lvl, txt.strip()[:120]


def run_task(task_id):
    t = db.q("SELECT * FROM tasks WHERE id=?", (task_id,), one=True)
    if not t or t["status"] != "pending":
        return
    db.x("UPDATE tasks SET status='running', updated=? WHERE id=?", (db.now(), task_id))
    db.audit_log(ROLE_MAP.get(t["role_id"], {}).get("name", "系統"), "開始任務",
                 dept=t["dept"], detail=t["title"])
    try:
        risk, why = assess_risk(t)
        db.x("UPDATE tasks SET risk=? WHERE id=?", (risk, task_id))
        fn = WORKFLOWS.get(t["kind"], wf_generic)
        out = fn(t)
        out = "【風控官】%s｜%s\n\n%s" % (risk, why, out)
        cur = db.q("SELECT status FROM tasks WHERE id=?", (task_id,), one=True)
        final = "waiting_approval" if cur["status"] == "waiting_approval" else "done"
        db.x("UPDATE tasks SET status=?, output=?, updated=? WHERE id=?",
             (final, out, db.now(), task_id))
        db.audit_log("系統", "任務完成" if final == "done" else "任務待審批",
                     dept=t["dept"], risk=risk, detail=t["title"])
    except Exception as e:
        db.x("UPDATE tasks SET status='failed', output=?, updated=? WHERE id=?",
             ("執行失敗：%s" % e, db.now(), task_id))
        db.audit_log("系統", "任務失敗", dept=t["dept"], risk="中", detail=str(e))
    finally:
        with _slot_lock:
            _running.discard(task_id)


def decide_approval(app_id, approve, actor="老闆"):
    a = db.q("SELECT * FROM approvals WHERE id=?", (app_id,), one=True)
    if not a or a["status"] != "pending":
        return False
    status = "approved" if approve else "rejected"
    db.x("UPDATE approvals SET status=?, decided=? WHERE id=?", (status, db.now(), app_id))
    payload = json.loads(a["payload"] or "{}")
    if approve and a["kind"] == "模擬交易":
        tr = payload.get("trade", {})
        db.x("INSERT INTO trades(ts,symbol,side,qty,price,status,note) VALUES(?,?,?,?,?,?,?)",
             (db.now(), tr.get("symbol", "?"), tr.get("action"), tr.get("qty", 0),
              tr.get("price", 0), "filled(模擬)", tr.get("name", "")))
        _apply_trade(tr)
    if approve and a["kind"] == "貼文草稿":
        db.x("UPDATE drafts SET status='approved' WHERE id=?", (payload.get("draft_id", 0),))
    db.x("UPDATE tasks SET status=?, updated=? WHERE id=?",
         ("done" if approve else "rejected", db.now(), a["task_id"]))
    db.audit_log(actor, "核准" if approve else "駁回", risk=a["risk"], detail=a["kind"])
    return True


def _apply_trade(tr):
    sym, qty, price = tr.get("symbol", "?"), float(tr.get("qty", 0) or 0), float(tr.get("price", 0) or 0)
    p = db.q("SELECT * FROM portfolio WHERE symbol=?", (sym,), one=True)
    if tr.get("action") == "buy":
        if p:
            nq = p["qty"] + qty
            avg = (p["qty"] * p["avg_price"] + qty * price) / nq if nq else 0
            db.x("UPDATE portfolio SET qty=?, avg_price=?, last_price=? WHERE symbol=?",
                 (nq, avg, price, sym))
        else:
            db.x("INSERT INTO portfolio(symbol,name,qty,avg_price,last_price) VALUES(?,?,?,?,?)",
                 (sym, tr.get("name", sym), qty, price, price))
    elif tr.get("action") == "sell" and p:
        sold = min(qty, p["qty"])
        pnl = (price - p["avg_price"]) * sold
        db.ledger_add("invest_realized", pnl, "模擬賣出 %s x%s" % (sym, sold))
        db.x("UPDATE portfolio SET qty=?, last_price=? WHERE symbol=?",
             (p["qty"] - sold, price, sym))


# ---------- Autopilot ----------

def autopilot_loop():
    while True:
        try:
            if db.kv_get("autopilot", "off") == "on":
                with _slot_lock:
                    free = MAX_SLOTS - len(_running)
                if free > 0 and budget_ok():
                    rows = db.q("SELECT id FROM tasks WHERE status='pending' ORDER BY id LIMIT ?", (free,))
                    for r in rows:
                        with _slot_lock:
                            if r["id"] in _running:
                                continue
                            _running.add(r["id"])
                        threading.Thread(target=run_task, args=(r["id"],), daemon=True).start()
        except Exception:
            pass
        time.sleep(8)


def running_count():
    with _slot_lock:
        return len(_running)


def start_autopilot_thread():
    threading.Thread(target=autopilot_loop, daemon=True).start()
