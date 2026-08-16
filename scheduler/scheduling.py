"""自動排班的統一入口:選引擎、寫回資料庫、產生警告。"""

from flask import current_app

from . import repo, rules, solver
from .engine import build_problem, validate

ENGINE_LABELS = {"rules": "規則排班", "solver": "最佳化排班"}


def run_schedule(start: str, end: str, engine: str = "rules",
                 keep_locked: bool = True, time_limit_sec: int = 15) -> dict:
    """排班並寫入資料庫。

    keep_locked=True 時,手動鎖定的班次會保留,其餘重排。
    回傳 {engine, engine_label, count, notes, warnings}
    """
    if engine not in ENGINE_LABELS:
        engine = "rules"

    problem = build_problem(
        start,
        end,
        max_consecutive_days=current_app.config["MAX_CONSECUTIVE_DAYS"],
        min_rest_hours=current_app.config["MIN_REST_HOURS"],
    )

    if not problem.employees:
        raise ValueError("還沒有任何在職員工,先去「員工」頁新增。")
    if not problem.shifts:
        raise ValueError("還沒有任何啟用中的班別,先去「班別」頁新增。")

    if not keep_locked:
        problem.locked = []

    notes = []
    if engine == "solver":
        if not solver.available():
            engine = "rules"
            notes.append("(沒安裝 OR-Tools,自動改用規則排班)")
        else:
            assignments, solver_notes = solver.generate(problem, time_limit_sec)
            notes += solver_notes

    if engine == "rules":
        assignments, gen_notes = rules.generate(problem)
        notes += gen_notes[:5]
        if len(gen_notes) > 5:
            notes.append(f"(另有 {len(gen_notes) - 5} 個班次補不滿人)")

    # 寫回資料庫:清掉未鎖定的,再整批寫入
    repo.clear_unlocked(start, end)
    if not keep_locked:
        for a in repo.list_assignments(start, end):
            repo.delete_assignment(a["id"])

    written = 0
    locked_set = set(problem.locked)
    for work_date, shift_id, emp_id in assignments:
        if (work_date, shift_id, emp_id) in locked_set:
            continue                                  # 鎖定的那筆還在,不重複寫
        written += 1 if repo.create_assignment({
            "work_date": work_date,
            "shift_type_id": shift_id,
            "employee_id": emp_id,
        }) else 0

    warnings = validate(problem, assignments)

    return {
        "engine": engine,
        "engine_label": ENGINE_LABELS[engine],
        "count": written + len(locked_set),
        "notes": notes,
        "warnings": warnings,
    }
