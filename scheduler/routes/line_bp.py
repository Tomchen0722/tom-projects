"""LINE 相關路由。

1. /line/webhook   員工在 LINE 聊天室打字時,LINE 會呼叫這裡
2. /liff           員工自助頁(在 LINE 裡開啟):看班表、請假、申請調班
3. /line/api/*     自助頁用的 JSON API,身分用 LIFF ID Token 驗證

身分驗證說明(給非工程背景的人):
LIFF 頁在 LINE 裡打開時,LINE 會發一張「身分證」(ID Token)給網頁。
網頁把這張身分證送到後端,後端拿去問 LINE 官方「這張是真的嗎、是誰」,
確認後才知道現在操作的是哪位員工。這樣員工不用另外註冊帳號密碼。
"""

import json
import re
import urllib.parse
import urllib.request
from datetime import date, timedelta

from flask import (Blueprint, abort, current_app, jsonify, render_template,
                   request)

from .. import line_api, repo
from ..notify import notify_manager_new_request

bp = Blueprint("line", __name__)

VERIFY_URL = "https://api.line.me/oauth2/v2.1/verify"
DATE_RE = re.compile(r"(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})")


# ------------------------------------------------------------------ 身分驗證

def verify_id_token(id_token: str) -> str:
    """向 LINE 驗證 ID Token,成功回傳 LINE userId,失敗回傳空字串。"""
    client_id = current_app.config.get("LINE_LOGIN_CHANNEL_ID", "")
    if not (id_token and client_id):
        return ""
    body = urllib.parse.urlencode({"id_token": id_token, "client_id": client_id})
    req = urllib.request.Request(
        VERIFY_URL,
        data=body.encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read()).get("sub", "")
    except Exception:                                  # noqa: BLE001
        return ""


def current_employee():
    """判斷目前是哪位員工。

    正式模式:驗證 LIFF ID Token。
    Demo 模式(沒設 LINE Login Channel ID):用 ?emp=<id> 直接指定,方便本機測試。
    """
    id_token = request.headers.get("X-Liff-Id-Token") or request.args.get("id_token", "")
    if current_app.config.get("LINE_LOGIN_CHANNEL_ID"):
        line_uid = verify_id_token(id_token)
        return repo.get_employee_by_line(line_uid) if line_uid else None

    emp_id = request.args.get("emp", type=int) or (
        (request.get_json(silent=True) or {}).get("emp")
    )
    return repo.get_employee(int(emp_id)) if emp_id else None


# ------------------------------------------------------------------ LIFF 頁

@bp.route("/liff")
def liff_page():
    return render_template(
        "liff.html",
        liff_id=current_app.config.get("LINE_LIFF_ID", ""),
        demo_mode=not current_app.config.get("LINE_LOGIN_CHANNEL_ID"),
        employees=repo.list_employees(),
        shifts=repo.list_shift_types(),
        today=date.today().isoformat(),
    )


# ------------------------------------------------------------------ 自助 API

@bp.get("/line/api/me")
def me():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "找不到你的員工資料,請先請店長綁定 LINE。"}), 401
    return jsonify({"ok": True, "data": {
        "id": emp["id"], "name": emp["name"], "role": emp["role"],
    }})


@bp.get("/line/api/schedule")
def my_schedule():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "尚未綁定"}), 401
    start = request.args.get("start") or date.today().isoformat()
    end = request.args.get("end") or (date.today() + timedelta(days=30)).isoformat()
    rows = repo.list_assignments(start, end, employee_id=emp["id"])
    return jsonify({"ok": True, "data": rows, "start": start, "end": end})


@bp.get("/line/api/leaves")
def my_leaves():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "尚未綁定"}), 401
    return jsonify({"ok": True, "data": repo.list_leaves(employee_id=emp["id"])})


@bp.post("/line/api/leaves")
def create_my_leave():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "尚未綁定"}), 401
    data = request.get_json(silent=True) or {}
    if not data.get("start_date"):
        return jsonify({"ok": False, "error": "請選擇日期"}), 400
    leave_id = repo.create_leave({
        "employee_id": emp["id"],
        "start_date": data["start_date"],
        "end_date": data.get("end_date") or data["start_date"],
        "leave_type": data.get("leave_type") or "特休",
        "reason": data.get("reason", ""),
        "status": "pending",
        "source": "line",
    })
    notify_manager_new_request(
        "請假", emp["name"],
        f"日期:{data['start_date']} ~ {data.get('end_date') or data['start_date']}\n"
        f"假別:{data.get('leave_type') or '特休'}",
    )
    return jsonify({"ok": True, "data": {"id": leave_id}})


@bp.delete("/line/api/leaves/<int:leave_id>")
def cancel_my_leave(leave_id):
    emp = current_employee()
    leave = repo.get_leave(leave_id)
    if not emp or not leave or leave["employee_id"] != emp["id"]:
        return jsonify({"ok": False, "error": "沒有權限"}), 403
    if leave["status"] != "pending":
        return jsonify({"ok": False, "error": "已審核的假不能自行取消,請找店長。"}), 400
    return jsonify({"ok": True, "deleted": bool(repo.delete_leave(leave_id))})


@bp.post("/line/api/swaps")
def create_my_swap():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "尚未綁定"}), 401
    data = request.get_json(silent=True) or {}
    assignment = repo.get_assignment(int(data.get("assignment_id") or 0))
    if not assignment or assignment["employee_id"] != emp["id"]:
        return jsonify({"ok": False, "error": "這不是你的班"}), 403
    swap_id = repo.create_swap({
        "assignment_id": assignment["id"],
        "requester_id": emp["id"],
        "target_shift_type_id": data.get("target_shift_type_id"),
        "target_date": data.get("target_date"),
        "reason": data.get("reason", ""),
        "source": "line",
    })
    notify_manager_new_request(
        "調班", emp["name"],
        f"原班:{assignment['work_date']} {assignment['shift_name']}\n"
        f"希望改成:{data.get('target_date') or assignment['work_date']}",
    )
    return jsonify({"ok": True, "data": {"id": swap_id}})


@bp.get("/line/api/swaps")
def my_swaps():
    emp = current_employee()
    if not emp:
        return jsonify({"ok": False, "error": "尚未綁定"}), 401
    return jsonify({"ok": True, "data": [
        s for s in repo.list_swaps() if s["requester_id"] == emp["id"]
    ]})


# ------------------------------------------------------------------ Webhook

@bp.post("/line/webhook")
def webhook():
    secret = current_app.config.get("LINE_CHANNEL_SECRET", "")
    body = request.get_data()
    if not line_api.verify_signature(secret, body, request.headers.get("X-Line-Signature", "")):
        abort(403)

    token = current_app.config.get("LINE_CHANNEL_ACCESS_TOKEN", "")
    events = (request.get_json(silent=True) or {}).get("events", [])

    for event in events:
        if event.get("type") != "message" or event["message"].get("type") != "text":
            continue
        text = event["message"]["text"].strip()
        line_uid = event.get("source", {}).get("userId", "")
        reply_token = event.get("replyToken", "")
        reply = _handle_command(text, line_uid)
        if isinstance(reply, list):
            line_api.reply_messages(token, reply_token, reply)
        else:
            line_api.reply_text(token, reply_token, reply)

    return jsonify({"ok": True})


HELP = (
    "可以打這些指令:\n\n"
    "・班表 → 看未來 14 天的班\n"
    "・本月班表 → 看這個月的班\n"
    "・請假 2026-08-20 事假 家裡有事\n"
    "・綁定 你的員工編號 → 第一次使用要先綁\n"
    "・調班 → 開啟調班畫面"
)


def _handle_command(text: str, line_uid: str):
    liff_id = current_app.config.get("LINE_LIFF_ID", "")

    if text.startswith("綁定"):
        return _bind(text[2:].strip(), line_uid)

    emp = repo.get_employee_by_line(line_uid) if line_uid else None
    if not emp:
        return "還沒綁定員工身分。請輸入:綁定 你的員工編號\n(員工編號可以問店長)"

    if text in ("班表", "我的班表", "班"):
        start = date.today().isoformat()
        end = (date.today() + timedelta(days=13)).isoformat()
        rows = repo.list_assignments(start, end, employee_id=emp["id"])
        return line_api.schedule_text(emp["name"], rows, "未來 14 天班表")

    if text in ("本月班表", "這個月", "月班表"):
        today = date.today()
        from calendar import monthrange
        start = today.replace(day=1).isoformat()
        end = today.replace(day=monthrange(today.year, today.month)[1]).isoformat()
        rows = repo.list_assignments(start, end, employee_id=emp["id"])
        return line_api.schedule_text(emp["name"], rows, f"{today.month} 月班表")

    if text.startswith("請假"):
        return _quick_leave(text, emp)

    if text in ("調班", "換班"):
        if liff_id:
            return [line_api.liff_button(liff_id, "點下面開啟調班畫面", "?tab=swap")]
        return "調班請開啟自助頁面操作(店長還沒設定 LINE 連結)。"

    if text in ("功能", "help", "說明", "?"):
        return HELP

    return HELP


def _bind(keyword: str, line_uid: str) -> str:
    if not keyword:
        return "請輸入:綁定 你的員工編號"
    if not line_uid:
        return "抓不到你的 LINE 帳號,請直接在一對一聊天室輸入。"

    match = None
    for emp in repo.list_employees():
        if keyword in (emp.get("employee_no") or "") or keyword == emp["name"]:
            match = emp
            break
    if not match:
        return f"找不到員工編號或姓名「{keyword}」,請跟店長確認。"
    if match.get("line_user_id") and match["line_user_id"] != line_uid:
        return "這個編號已經綁過別的 LINE 帳號了,請找店長處理。"

    repo.update_employee(match["id"], {"line_user_id": line_uid})
    return f"綁定成功,{match['name']} 你好!\n\n{HELP}"


def _quick_leave(text: str, emp: dict) -> str:
    """解析「請假 2026-08-20 事假 家裡有事」這種一行指令。"""
    dates = DATE_RE.findall(text)
    if not dates:
        return "請假格式:請假 2026-08-20 事假 家裡有事\n(日期要寫完整年月日)"
    days = [f"{int(y):04d}-{int(m):02d}-{int(d):02d}" for y, m, d in dates]
    start, end = days[0], days[-1]

    rest = DATE_RE.sub("", text[2:]).split()
    leave_type = rest[0] if rest else "特休"
    reason = " ".join(rest[1:]) if len(rest) > 1 else ""

    repo.create_leave({
        "employee_id": emp["id"], "start_date": start, "end_date": end,
        "leave_type": leave_type, "reason": reason,
        "status": "pending", "source": "line",
    })
    notify_manager_new_request("請假", emp["name"],
                               f"日期:{start} ~ {end}\n假別:{leave_type}")
    return (
        f"請假申請已送出,等店長審核。\n\n"
        f"日期:{start} ~ {end}\n假別:{leave_type}"
        + (f"\n事由:{reason}" if reason else "")
    )
