"""後台網頁(老闆 / 店長使用)。表單都是一般 POST,不依賴 JavaScript。"""

from datetime import date

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, session, url_for)

from .. import repo
from ..engine import build_problem, validate
from ..scheduling import run_schedule
from .helpers import (WEEKDAY_TW, build_calendar, line_ready, login_required,
                      requested_range, shift_month)

bp = Blueprint("web", __name__)


# ------------------------------------------------------------------ 登入

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") == current_app.config["ADMIN_PASSWORD"]:
            session["is_admin"] = True
            return redirect(request.args.get("next") or url_for("web.dashboard"))
        flash("密碼錯誤", "error")
    return render_template("login.html")


@bp.route("/logout")
def logout():
    session.pop("is_admin", None)
    return redirect(url_for("web.login"))


# ------------------------------------------------------------------ 總覽

@bp.route("/")
@login_required
def dashboard():
    start, end = requested_range()
    assignments = repo.list_assignments(start, end)
    return render_template(
        "dashboard.html",
        start=start,
        end=end,
        employees=repo.list_employees(),
        shifts=repo.list_shift_types(),
        assignments=assignments,
        pending_leaves=repo.list_leaves(status="pending"),
        pending_swaps=repo.list_swaps(status="pending"),
        stats=repo.workload_stats(start, end),
        line_ready=line_ready(),
        today=date.today().isoformat(),
    )


# ------------------------------------------------------------------ 員工

@bp.route("/employees")
@login_required
def employees():
    return render_template(
        "employees.html",
        employees=repo.list_employees(include_inactive=True),
        edit_id=request.args.get("edit", type=int),
    )


@bp.post("/employees/create")
@login_required
def employee_create():
    if not request.form.get("name", "").strip():
        flash("姓名不能空白", "error")
    else:
        repo.create_employee(request.form.to_dict())
        flash("已新增員工", "ok")
    return redirect(url_for("web.employees"))


@bp.post("/employees/<int:emp_id>/update")
@login_required
def employee_update(emp_id):
    data = request.form.to_dict()
    data["active"] = "1" if request.form.get("active") else "0"
    repo.update_employee(emp_id, data)
    flash("已更新員工資料", "ok")
    return redirect(url_for("web.employees"))


@bp.post("/employees/<int:emp_id>/delete")
@login_required
def employee_delete(emp_id):
    if request.form.get("mode") == "deactivate":
        repo.deactivate_employee(emp_id)
        flash("已設為停用,歷史班表保留", "ok")
    else:
        repo.delete_employee(emp_id)
        flash("已刪除員工,相關班表一併移除", "ok")
    return redirect(url_for("web.employees"))


# ------------------------------------------------------------------ 班別

@bp.route("/shifts")
@login_required
def shifts():
    return render_template(
        "shifts.html",
        shifts=repo.list_shift_types(include_inactive=True),
        edit_id=request.args.get("edit", type=int),
    )


@bp.post("/shifts/create")
@login_required
def shift_create():
    form = request.form.to_dict()
    if not form.get("name") or not form.get("start_time") or not form.get("end_time"):
        flash("班別名稱與起訖時間都要填", "error")
    else:
        repo.create_shift_type(form)
        flash("已新增班別", "ok")
    return redirect(url_for("web.shifts"))


@bp.post("/shifts/<int:shift_id>/update")
@login_required
def shift_update(shift_id):
    data = request.form.to_dict()
    data["active"] = "1" if request.form.get("active") else "0"
    repo.update_shift_type(shift_id, data)
    flash("已更新班別", "ok")
    return redirect(url_for("web.shifts"))


@bp.post("/shifts/<int:shift_id>/delete")
@login_required
def shift_delete(shift_id):
    repo.delete_shift_type(shift_id)
    flash("已刪除班別,該班別的排班一併移除", "ok")
    return redirect(url_for("web.shifts"))


# ------------------------------------------------------------------ 排班表

@bp.route("/schedule")
@login_required
def schedule():
    start, end = requested_range()
    month = request.args.get("month") or start[:7]
    assignments = repo.list_assignments(start, end)

    by_day: dict = {}
    for a in assignments:
        by_day.setdefault(a["work_date"], []).append(a)

    leave_days: dict = {}
    for lv in repo.list_leaves(status="approved", start=start, end=end):
        for d in repo.daterange(max(lv["start_date"], start), min(lv["end_date"], end)):
            leave_days.setdefault(d, []).append(lv["employee_name"])

    problem = build_problem(start, end,
                            max_consecutive_days=current_app.config["MAX_CONSECUTIVE_DAYS"],
                            min_rest_hours=current_app.config["MIN_REST_HOURS"])
    warnings = validate(
        problem,
        [(a["work_date"], a["shift_type_id"], a["employee_id"]) for a in assignments],
    )

    return render_template(
        "schedule.html",
        start=start,
        end=end,
        month=month,
        prev_month=shift_month(month, -1),
        next_month=shift_month(month, 1),
        weeks=build_calendar(start, end),
        by_day=by_day,
        leave_days=leave_days,
        employees=repo.list_employees(),
        shifts=repo.list_shift_types(),
        stats=repo.workload_stats(start, end),
        warnings=warnings,
        weekday_tw=WEEKDAY_TW,
        today=date.today().isoformat(),
        line_ready=line_ready(),
    )


@bp.post("/schedule/generate")
@login_required
def schedule_generate():
    start = request.form["start"]
    end = request.form["end"]
    engine = request.form.get("engine", "rules")
    keep_locked = bool(request.form.get("keep_locked"))

    try:
        result = run_schedule(start, end, engine=engine, keep_locked=keep_locked)
    except Exception as exc:                        # noqa: BLE001
        flash(f"排班失敗:{exc}", "error")
        return redirect(url_for("web.schedule", start=start, end=end))

    flash(
        f"已用「{result['engine_label']}」排出 {result['count']} 個班次。"
        + ("".join(f" {n}" for n in result["notes"])),
        "ok",
    )
    if result["warnings"]:
        flash("有 %d 項需要留意,請看下方警告。" % len(result["warnings"]), "warn")
    return redirect(url_for("web.schedule", start=start, end=end))


@bp.post("/schedule/assign")
@login_required
def schedule_assign():
    """手動新增一筆排班(會自動鎖定,之後自動排班不會蓋掉)。"""
    data = request.form.to_dict()
    data["locked"] = "1"
    if repo.create_assignment(data):
        flash("已新增班次", "ok")
    else:
        flash("這個人在這天的這個班已經有了", "warn")
    return redirect(url_for("web.schedule", start=request.form.get("start"),
                            end=request.form.get("end")))


@bp.post("/schedule/<int:assignment_id>/update")
@login_required
def schedule_update(assignment_id):
    repo.update_assignment(assignment_id, request.form.to_dict())
    flash("已修改班次", "ok")
    return redirect(url_for("web.schedule", start=request.form.get("start"),
                            end=request.form.get("end")))


@bp.post("/schedule/<int:assignment_id>/delete")
@login_required
def schedule_delete(assignment_id):
    repo.delete_assignment(assignment_id)
    flash("已刪除班次", "ok")
    return redirect(url_for("web.schedule", start=request.form.get("start"),
                            end=request.form.get("end")))


@bp.post("/schedule/clear")
@login_required
def schedule_clear():
    start, end = request.form["start"], request.form["end"]
    n = repo.clear_unlocked(start, end)
    flash(f"已清空 {n} 個未鎖定的班次", "ok")
    return redirect(url_for("web.schedule", start=start, end=end))


@bp.post("/schedule/publish")
@login_required
def schedule_publish():
    from ..notify import notify_published

    start, end = request.form["start"], request.form["end"]
    repo.publish_range(start, end)
    sent, skipped = notify_published(start, end)
    msg = f"班表已發布({start} ~ {end})。"
    if sent:
        msg += f" 已用 LINE 通知 {sent} 位同仁。"
    if skipped:
        msg += f" {skipped} 位還沒綁定 LINE。"
    flash(msg, "ok")
    return redirect(url_for("web.schedule", start=start, end=end))


# ------------------------------------------------------------------ 請假

@bp.route("/leaves")
@login_required
def leaves():
    return render_template(
        "leaves.html",
        leaves=repo.list_leaves(status=request.args.get("status", "")),
        employees=repo.list_employees(),
        current_status=request.args.get("status", ""),
        edit_id=request.args.get("edit", type=int),
        today=date.today().isoformat(),
    )


@bp.post("/leaves/create")
@login_required
def leave_create():
    form = request.form.to_dict()
    form.setdefault("status", "approved")       # 老闆自己代填的假直接生效
    repo.create_leave(form)
    flash("已新增請假", "ok")
    return redirect(url_for("web.leaves"))


@bp.post("/leaves/<int:leave_id>/update")
@login_required
def leave_update(leave_id):
    repo.update_leave(leave_id, request.form.to_dict())
    flash("已更新請假", "ok")
    return redirect(url_for("web.leaves"))


@bp.post("/leaves/<int:leave_id>/decide")
@login_required
def leave_decide(leave_id):
    from ..notify import notify_leave_result

    status = request.form.get("status", "approved")
    repo.update_leave(leave_id, {"status": status})
    notify_leave_result(leave_id)
    flash("已" + ("核准" if status == "approved" else "退回") + "請假申請", "ok")
    return redirect(url_for("web.leaves", status=request.form.get("filter", "")))


@bp.post("/leaves/<int:leave_id>/delete")
@login_required
def leave_delete(leave_id):
    repo.delete_leave(leave_id)
    flash("已刪除請假紀錄", "ok")
    return redirect(url_for("web.leaves"))


# ------------------------------------------------------------------ 調班

@bp.route("/swaps")
@login_required
def swaps():
    return render_template(
        "swaps.html",
        swaps=repo.list_swaps(status=request.args.get("status", "")),
        current_status=request.args.get("status", ""),
    )


@bp.post("/swaps/<int:swap_id>/decide")
@login_required
def swap_decide(swap_id):
    from ..notify import notify_swap_result

    status = request.form.get("status", "approved")
    repo.decide_swap(swap_id, status)
    notify_swap_result(swap_id)
    flash("已" + ("核准" if status == "approved" else "退回") + "調班申請", "ok")
    return redirect(url_for("web.swaps", status=request.form.get("filter", "")))


@bp.post("/swaps/<int:swap_id>/delete")
@login_required
def swap_delete(swap_id):
    repo.delete_swap(swap_id)
    flash("已刪除調班紀錄", "ok")
    return redirect(url_for("web.swaps"))


# ------------------------------------------------------------------ 設定

@bp.route("/settings")
@login_required
def settings():
    from ..db import HAS_PSYCOPG2, backend_label, db_url_warnings
    from ..solver import available as solver_available

    db_url = current_app.config.get("DATABASE_URL", "")
    return render_template(
        "settings.html",
        db_label=backend_label(),
        db_is_supabase=bool(db_url),
        db_host=_db_host(db_url),
        db_warnings=db_url_warnings(db_url),
        db_error=current_app.config.get("DB_ERROR", ""),
        has_psycopg2=HAS_PSYCOPG2,
        sqlite_path=current_app.config.get("DB_PATH", ""),
        line_ready=line_ready(),
        liff_id=current_app.config.get("LINE_LIFF_ID", ""),
        public_base_url=current_app.config.get("PUBLIC_BASE_URL", ""),
        solver_ok=solver_available(),
        max_consecutive=current_app.config["MAX_CONSECUTIVE_DAYS"],
        min_rest=current_app.config["MIN_REST_HOURS"],
        employees=repo.list_employees(include_inactive=True),
    )


def _db_host(url: str) -> str:
    """只取主機與埠號顯示,不要把密碼印在畫面上。"""
    import re

    match = re.search(r"@([^/?]+)", url or "")
    return match.group(1) if match else ""
