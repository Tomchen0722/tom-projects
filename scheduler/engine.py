"""排班共用資料結構與規則判斷。

rules.py(規則排班)和 solver.py(最佳化排班)都吃同一份 Problem。
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta

from . import repo


@dataclass
class Problem:
    start: str
    end: str
    days: list                      # ['2026-08-01', ...]
    employees: list                 # [dict, ...]
    shifts: list                    # [dict, ...]
    leaves: dict                    # {emp_id: {date, ...}}
    locked: list                    # [(date, shift_id, emp_id), ...]
    max_consecutive_days: int = 6
    min_rest_hours: int = 11
    history: dict = field(default_factory=dict)   # {emp_id: 之前已排班數},用來延續公平度

    @property
    def employee_ids(self):
        return [e["id"] for e in self.employees]

    def skills_of(self, emp_id: int) -> set:
        for e in self.employees:
            if e["id"] == emp_id:
                return {s.strip() for s in (e["skills"] or "").split(",") if s.strip()}
        return set()

    def on_leave(self, emp_id: int, day: str) -> bool:
        return day in self.leaves.get(emp_id, set())

    def can_take(self, emp_id: int, shift: dict) -> bool:
        """技能是否符合班別需求。"""
        need = (shift.get("required_skill") or "").strip()
        if not need:
            return True
        return need in self.skills_of(emp_id)


def build_problem(start: str, end: str, *, max_consecutive_days: int = 6,
                  min_rest_hours: int = 11) -> Problem:
    days = repo.daterange(start, end)
    employees = repo.list_employees()
    shifts = repo.list_shift_types()
    leaves = repo.leave_map(start, end)

    locked = [
        (a["work_date"], a["shift_type_id"], a["employee_id"])
        for a in repo.list_assignments(start, end)
        if a["locked"]
    ]

    # 區間前 28 天的班數,讓連續兩個月的排班不會有人一直被排到
    hist_start = (datetime.fromisoformat(start) - timedelta(days=28)).date().isoformat()
    hist_end = (datetime.fromisoformat(start) - timedelta(days=1)).date().isoformat()
    history = {}
    if hist_end >= hist_start:
        for row in repo.workload_stats(hist_start, hist_end):
            history[row["id"]] = row["shifts"]

    return Problem(
        start=start,
        end=end,
        days=days,
        employees=employees,
        shifts=shifts,
        leaves=leaves,
        locked=locked,
        max_consecutive_days=max_consecutive_days,
        min_rest_hours=min_rest_hours,
        history=history,
    )


# ------------------------------------------------------------ 時間計算

def shift_bounds(day: str, shift: dict):
    """回傳 (上班時間, 下班時間)。end < start 視為跨夜,下班算隔天。"""
    d = datetime.fromisoformat(day)
    sh, sm = (int(x) for x in shift["start_time"].split(":"))
    eh, em = (int(x) for x in shift["end_time"].split(":"))
    start_dt = d.replace(hour=sh, minute=sm)
    end_dt = d.replace(hour=eh, minute=em)
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
    return start_dt, end_dt


def shift_hours(shift: dict) -> float:
    s, e = shift_bounds("2000-01-01", shift)
    return (e - s).total_seconds() / 3600


def rest_ok(day_a: str, shift_a: dict, day_b: str, shift_b: dict,
            min_rest_hours: int) -> bool:
    """A 班下班到 B 班上班,間隔是否足夠。"""
    _, end_a = shift_bounds(day_a, shift_a)
    start_b, _ = shift_bounds(day_b, shift_b)
    if start_b <= end_a:
        return False
    return (start_b - end_a).total_seconds() / 3600 >= min_rest_hours


def conflicting_pairs(problem: Problem):
    """列出所有「相鄰兩天休息不足」的班別組合。

    回傳 [(day_i, shift_a_id, day_j, shift_b_id), ...]
    """
    pairs = []
    shifts_by_id = {s["id"]: s for s in problem.shifts}
    for i in range(len(problem.days) - 1):
        d1, d2 = problem.days[i], problem.days[i + 1]
        for sa in problem.shifts:
            for sb in problem.shifts:
                if not rest_ok(d1, shifts_by_id[sa["id"]], d2, shifts_by_id[sb["id"]],
                               problem.min_rest_hours):
                    pairs.append((d1, sa["id"], d2, sb["id"]))
    return pairs


# ------------------------------------------------------------ 結果驗證

def validate(problem: Problem, assignments: list) -> list:
    """檢查排班結果,回傳人看得懂的警告清單。

    assignments: [(work_date, shift_type_id, employee_id), ...]
    """
    warnings = []
    shifts_by_id = {s["id"]: s for s in problem.shifts}
    emp_name = {e["id"]: e["name"] for e in problem.employees}

    by_day_shift: dict = {}
    by_emp_day: dict = {}
    for d, sid, eid in assignments:
        by_day_shift.setdefault((d, sid), []).append(eid)
        by_emp_day.setdefault(eid, {}).setdefault(d, []).append(sid)

    # 人數不足
    for day in problem.days:
        for s in problem.shifts:
            got = len(by_day_shift.get((day, s["id"]), []))
            need = s["required_headcount"]
            if got < need:
                warnings.append(f"{day} {s['name']} 缺 {need - got} 人(需 {need},排到 {got})")

    # 一天多班
    for eid, days in by_emp_day.items():
        for day, sids in days.items():
            if len(sids) > 1:
                warnings.append(f"{emp_name.get(eid, eid)} 在 {day} 被排了 {len(sids)} 個班")

    # 請假衝突
    for d, sid, eid in assignments:
        if problem.on_leave(eid, d):
            warnings.append(f"{emp_name.get(eid, eid)} {d} 已請假卻被排 {shifts_by_id[sid]['name']}")

    # 休息不足 + 連上天數
    for eid, days in by_emp_day.items():
        sorted_days = sorted(days.keys())
        for a, b in zip(sorted_days, sorted_days[1:]):
            if (datetime.fromisoformat(b) - datetime.fromisoformat(a)).days != 1:
                continue
            sa, sb = shifts_by_id[days[a][0]], shifts_by_id[days[b][0]]
            if not rest_ok(a, sa, b, sb, problem.min_rest_hours):
                warnings.append(
                    f"{emp_name.get(eid, eid)} {a} {sa['name']} 接 {b} {sb['name']},"
                    f"休息不到 {problem.min_rest_hours} 小時"
                )
        run = 1
        for a, b in zip(sorted_days, sorted_days[1:]):
            if (datetime.fromisoformat(b) - datetime.fromisoformat(a)).days == 1:
                run += 1
                if run > problem.max_consecutive_days:
                    warnings.append(
                        f"{emp_name.get(eid, eid)} 連上超過 {problem.max_consecutive_days} 天(到 {b})"
                    )
                    break
            else:
                run = 1

    # 超過週上限
    caps = {e["id"]: e["max_shifts_per_week"] for e in problem.employees}
    for eid, days in by_emp_day.items():
        weeks: dict = {}
        for day in days:
            iso = datetime.fromisoformat(day).isocalendar()
            weeks[(iso.year, iso.week)] = weeks.get((iso.year, iso.week), 0) + 1
        for (yr, wk), n in weeks.items():
            if n > caps.get(eid, 5):
                warnings.append(
                    f"{emp_name.get(eid, eid)} 第 {yr}-W{wk} 週排了 {n} 班,超過上限 {caps.get(eid, 5)}"
                )

    return warnings
