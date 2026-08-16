"""LINE 通知:班表發布、請假 / 調班審核結果。

沒設定 LINE token 時全部安靜略過,不影響網站運作。
"""

from flask import current_app

from . import line_api, repo


def _token() -> str:
    return current_app.config.get("LINE_CHANNEL_ACCESS_TOKEN", "")


def notify_published(start: str, end: str):
    """把每個人自己那份班表推給他。回傳 (成功數, 沒綁 LINE 的人數)。"""
    token = _token()
    sent = skipped = 0
    for emp in repo.list_employees():
        if not emp.get("line_user_id"):
            skipped += 1
            continue
        rows = repo.list_assignments(start, end, employee_id=emp["id"])
        text = line_api.schedule_text(emp["name"], rows, f"{start} ~ {end} 班表")
        if line_api.push_text(token, emp["line_user_id"], text):
            sent += 1
    return sent, skipped


def notify_leave_result(leave_id: int) -> bool:
    leave = repo.get_leave(leave_id)
    if not leave:
        return False
    emp = repo.get_employee(leave["employee_id"])
    if not emp or not emp.get("line_user_id"):
        return False
    word = {"approved": "已核准", "rejected": "未通過"}.get(leave["status"], "處理中")
    text = (
        f"請假申請{word}\n\n"
        f"日期:{leave['start_date']} ~ {leave['end_date']}\n"
        f"假別:{leave['leave_type']}"
    )
    return line_api.push_text(_token(), emp["line_user_id"], text)


def notify_swap_result(swap_id: int) -> bool:
    swap = repo.get_swap(swap_id)
    if not swap:
        return False
    emp = repo.get_employee(swap["requester_id"])
    if not emp or not emp.get("line_user_id"):
        return False
    word = {"approved": "已核准", "rejected": "未通過"}.get(swap["status"], "處理中")
    target = swap.get("target_date") or swap["work_date"]
    text = (
        f"調班申請{word}\n\n"
        f"原班:{swap['work_date']} {swap['shift_name']}\n"
        f"調整為:{target} {swap.get('target_shift_name') or swap['shift_name']}"
    )
    return line_api.push_text(_token(), emp["line_user_id"], text)


def notify_manager_new_request(kind: str, employee_name: str, detail: str) -> int:
    """員工從 LINE 送出申請時,通知所有 manager。"""
    token = _token()
    text = f"有新的{kind}申請\n\n申請人:{employee_name}\n{detail}\n\n請到後台審核。"
    sent = 0
    for emp in repo.list_employees():
        if emp.get("role") == "manager" and emp.get("line_user_id"):
            if line_api.push_text(token, emp["line_user_id"], text):
                sent += 1
    return sent
