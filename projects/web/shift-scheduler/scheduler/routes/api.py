"""JSON API(給前端 JS、LIFF 頁、或之後接手機 App 用)。

全部需要後台登入,除了 line_bp 裡的員工自助 API。
"""

from flask import Blueprint, jsonify, request

from .. import repo
from ..scheduling import run_schedule
from .helpers import login_required, requested_range

bp = Blueprint("api", __name__, url_prefix="/api")


def _payload() -> dict:
    return request.get_json(silent=True) or request.form.to_dict() or {}


def _ok(data=None, **extra):
    body = {"ok": True}
    if data is not None:
        body["data"] = data
    body.update(extra)
    return jsonify(body)


def _err(message: str, code: int = 400):
    return jsonify({"ok": False, "error": message}), code


# ------------------------------------------------------------------ 員工

@bp.get("/employees")
@login_required
def employees_list():
    include = request.args.get("all") == "1"
    return _ok(repo.list_employees(include_inactive=include))


@bp.post("/employees")
@login_required
def employees_create():
    data = _payload()
    if not (data.get("name") or "").strip():
        return _err("姓名不能空白")
    return _ok({"id": repo.create_employee(data)})


@bp.get("/employees/<int:emp_id>")
@login_required
def employees_get(emp_id):
    emp = repo.get_employee(emp_id)
    return _ok(emp) if emp else _err("找不到這位員工", 404)


@bp.put("/employees/<int:emp_id>")
@bp.patch("/employees/<int:emp_id>")
@login_required
def employees_update(emp_id):
    if not repo.update_employee(emp_id, _payload()):
        return _err("找不到這位員工", 404)
    return _ok(repo.get_employee(emp_id))


@bp.delete("/employees/<int:emp_id>")
@login_required
def employees_delete(emp_id):
    if request.args.get("mode") == "deactivate":
        return _ok(deleted=bool(repo.deactivate_employee(emp_id)))
    return _ok(deleted=bool(repo.delete_employee(emp_id)))


# ------------------------------------------------------------------ 班別

@bp.get("/shifts")
@login_required
def shifts_list():
    return _ok(repo.list_shift_types(include_inactive=request.args.get("all") == "1"))


@bp.post("/shifts")
@login_required
def shifts_create():
    data = _payload()
    for field in ("name", "start_time", "end_time"):
        if not data.get(field):
            return _err(f"缺少欄位:{field}")
    return _ok({"id": repo.create_shift_type(data)})


@bp.put("/shifts/<int:shift_id>")
@bp.patch("/shifts/<int:shift_id>")
@login_required
def shifts_update(shift_id):
    if not repo.update_shift_type(shift_id, _payload()):
        return _err("找不到這個班別", 404)
    return _ok(repo.get_shift_type(shift_id))


@bp.delete("/shifts/<int:shift_id>")
@login_required
def shifts_delete(shift_id):
    return _ok(deleted=bool(repo.delete_shift_type(shift_id)))


# ------------------------------------------------------------------ 請假

@bp.get("/leaves")
@login_required
def leaves_list():
    return _ok(repo.list_leaves(
        status=request.args.get("status", ""),
        employee_id=request.args.get("employee_id", type=int) or 0,
    ))


@bp.post("/leaves")
@login_required
def leaves_create():
    data = _payload()
    if not data.get("employee_id") or not data.get("start_date"):
        return _err("employee_id 與 start_date 必填")
    return _ok({"id": repo.create_leave(data)})


@bp.put("/leaves/<int:leave_id>")
@bp.patch("/leaves/<int:leave_id>")
@login_required
def leaves_update(leave_id):
    if not repo.update_leave(leave_id, _payload()):
        return _err("找不到這筆請假", 404)
    return _ok(repo.get_leave(leave_id))


@bp.delete("/leaves/<int:leave_id>")
@login_required
def leaves_delete(leave_id):
    return _ok(deleted=bool(repo.delete_leave(leave_id)))


# ------------------------------------------------------------------ 排班

@bp.get("/assignments")
@login_required
def assignments_list():
    start, end = requested_range()
    return _ok(repo.list_assignments(
        start, end, employee_id=request.args.get("employee_id", type=int) or 0
    ))


@bp.post("/assignments")
@login_required
def assignments_create():
    data = _payload()
    for field in ("work_date", "shift_type_id", "employee_id"):
        if not data.get(field):
            return _err(f"缺少欄位:{field}")
    new_id = repo.create_assignment(data)
    if not new_id:
        return _err("這個人在這天的這個班已經存在", 409)
    return _ok({"id": new_id})


@bp.put("/assignments/<int:assignment_id>")
@bp.patch("/assignments/<int:assignment_id>")
@login_required
def assignments_update(assignment_id):
    if not repo.update_assignment(assignment_id, _payload()):
        return _err("找不到這筆班次", 404)
    return _ok(repo.get_assignment(assignment_id))


@bp.delete("/assignments/<int:assignment_id>")
@login_required
def assignments_delete(assignment_id):
    return _ok(deleted=bool(repo.delete_assignment(assignment_id)))


@bp.post("/schedule/generate")
@login_required
def schedule_generate():
    data = _payload()
    start, end = data.get("start"), data.get("end")
    if not start or not end:
        return _err("start 與 end 必填")
    try:
        result = run_schedule(
            start,
            end,
            engine=data.get("engine", "rules"),
            keep_locked=str(data.get("keep_locked", "1")) not in ("0", "false", "False"),
            time_limit_sec=int(data.get("time_limit_sec") or 15),
        )
    except Exception as exc:                          # noqa: BLE001
        return _err(str(exc), 422)
    return _ok(result)


@bp.get("/stats")
@login_required
def stats():
    start, end = requested_range()
    return _ok(repo.workload_stats(start, end))


# ------------------------------------------------------------------ 調班

@bp.get("/swaps")
@login_required
def swaps_list():
    return _ok(repo.list_swaps(status=request.args.get("status", "")))


@bp.post("/swaps/<int:swap_id>/decide")
@login_required
def swaps_decide(swap_id):
    status = _payload().get("status", "approved")
    if status not in ("approved", "rejected"):
        return _err("status 只能是 approved 或 rejected")
    return _ok(updated=bool(repo.decide_swap(swap_id, status)))


@bp.delete("/swaps/<int:swap_id>")
@login_required
def swaps_delete(swap_id):
    return _ok(deleted=bool(repo.delete_swap(swap_id)))
