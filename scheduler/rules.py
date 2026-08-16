"""規則排班(貪婪演算法)。

邏輯很直白:一天一天、一個班一個班往下排,每次挑「目前最該輪到」的人。
速度快、結果好解釋,適合日常使用。真的排不出來時再用 solver.py。
"""

from datetime import datetime, timedelta

from .engine import Problem, rest_ok


def generate(problem: Problem):
    """回傳 (assignments, warnings_from_generation)。

    assignments: [(work_date, shift_type_id, employee_id), ...]
    """
    shifts_by_id = {s["id"]: s for s in problem.shifts}

    # 已鎖定的班先放進去,後面的排班要避開
    result = list(problem.locked)
    assigned_count = {e["id"]: problem.history.get(e["id"], 0) for e in problem.employees}
    emp_days: dict = {}      # {emp_id: {date: shift_id}}
    for d, sid, eid in result:
        emp_days.setdefault(eid, {})[d] = sid
        assigned_count[eid] = assigned_count.get(eid, 0) + 1

    week_count: dict = {}    # {(emp_id, iso_week): 班數}
    for d, _sid, eid in result:
        week_count[(eid, _isoweek(d))] = week_count.get((eid, _isoweek(d)), 0) + 1

    unfilled = []

    for day in problem.days:
        for shift in sorted(problem.shifts, key=lambda s: (s["sort_order"], s["start_time"])):
            already = sum(1 for d, sid, _ in result if d == day and sid == shift["id"])
            need = shift["required_headcount"] - already
            for _ in range(max(0, need)):
                pick = _best_candidate(
                    problem, day, shift, shifts_by_id, emp_days, assigned_count, week_count
                )
                if pick is None:
                    unfilled.append(f"{day} {shift['name']} 找不到可排的人")
                    break
                result.append((day, shift["id"], pick))
                emp_days.setdefault(pick, {})[day] = shift["id"]
                assigned_count[pick] = assigned_count.get(pick, 0) + 1
                key = (pick, _isoweek(day))
                week_count[key] = week_count.get(key, 0) + 1

    # 只回傳排班區間內的(鎖定的本來就在區間內)
    return result, unfilled


def _isoweek(day: str):
    iso = datetime.fromisoformat(day).isocalendar()
    return (iso.year, iso.week)


def _consecutive_days(emp_days: dict, emp_id: int, day: str) -> int:
    """如果把這個人排在 day,連上天數會變成幾天。"""
    days = emp_days.get(emp_id, {})
    d = datetime.fromisoformat(day)
    back = 0
    cur = d - timedelta(days=1)
    while cur.date().isoformat() in days:
        back += 1
        cur -= timedelta(days=1)
    fwd = 0
    cur = d + timedelta(days=1)
    while cur.date().isoformat() in days:
        fwd += 1
        cur += timedelta(days=1)
    return back + 1 + fwd


def _best_candidate(problem: Problem, day: str, shift: dict, shifts_by_id: dict,
                    emp_days: dict, assigned_count: dict, week_count: dict):
    candidates = []
    for emp in problem.employees:
        eid = emp["id"]

        if problem.on_leave(eid, day):
            continue
        if day in emp_days.get(eid, {}):          # 同一天只排一個班
            continue
        if not problem.can_take(eid, shift):      # 技能不符
            continue
        if week_count.get((eid, _isoweek(day)), 0) >= emp["max_shifts_per_week"]:
            continue
        if _consecutive_days(emp_days, eid, day) > problem.max_consecutive_days:
            continue

        # 前後一天的休息時間
        if not _rest_ok_around(problem, shifts_by_id, emp_days, eid, day, shift):
            continue

        candidates.append(emp)

    if not candidates:
        return None

    # 排序:總班數少的優先 → 這週班數少的優先 → 距離上次上班久的優先 → id
    def sort_key(emp):
        eid = emp["id"]
        last = _days_since_last(emp_days, eid, day)
        return (
            assigned_count.get(eid, 0),
            week_count.get((eid, _isoweek(day)), 0),
            -last,
            eid,
        )

    return sorted(candidates, key=sort_key)[0]["id"]


def _rest_ok_around(problem, shifts_by_id, emp_days, eid, day, shift) -> bool:
    d = datetime.fromisoformat(day)
    prev = (d - timedelta(days=1)).date().isoformat()
    nxt = (d + timedelta(days=1)).date().isoformat()
    days = emp_days.get(eid, {})

    if prev in days:
        if not rest_ok(prev, shifts_by_id[days[prev]], day, shift, problem.min_rest_hours):
            return False
    if nxt in days:
        if not rest_ok(day, shift, nxt, shifts_by_id[days[nxt]], problem.min_rest_hours):
            return False
    return True


def _days_since_last(emp_days: dict, emp_id: int, day: str) -> int:
    days = sorted(emp_days.get(emp_id, {}).keys())
    past = [x for x in days if x < day]
    if not past:
        return 999
    return (datetime.fromisoformat(day) - datetime.fromisoformat(past[-1])).days
