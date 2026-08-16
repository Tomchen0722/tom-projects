"""最佳化排班(OR-Tools CP-SAT)。

跟 rules.py 的差別:規則排班是「一格一格填」,填不下去就卡住;
這裡是把所有限制寫成數學式,讓求解器一次找出整體最好的解。
人多、班別多、限制互相打架的時候差別很明顯。

硬性限制(一定要滿足)
  - 每個班的人數
  - 一人一天只排一個班
  - 已核准的假不排
  - 手動鎖定的班保持不動
  - 技能需求
  - 兩班之間至少休息 N 小時
  - 連續上班不超過 N 天
  - 每週班數不超過個人上限

軟性目標(盡量做到,做不到就扣分)
  - 缺人最少(權重最高)
  - 每個人的班數盡量平均
  - 補足每個人的每週最低班數
  - 同一個人盡量排固定班別,不要早晚班一直跳
"""

from datetime import datetime

from .engine import Problem, conflicting_pairs

# 目標函式權重,數字越大越優先
W_SHORTAGE = 1000     # 缺人
W_FAIRNESS = 30       # 班數落差
W_MIN_SHIFT = 8       # 沒排到最低班數
W_ROTATION = 1        # 班別跳來跳去


class SolverUnavailable(RuntimeError):
    """沒安裝 ortools 時丟出。"""


def available() -> bool:
    try:
        import ortools.sat.python.cp_model  # noqa: F401
        return True
    except ImportError:
        return False


def generate(problem: Problem, time_limit_sec: int = 15):
    """回傳 (assignments, notes)。assignments 是 [(date, shift_id, emp_id), ...]"""
    try:
        from ortools.sat.python import cp_model
    except ImportError as exc:  # pragma: no cover
        raise SolverUnavailable(
            "沒有安裝 OR-Tools。請執行 pip install ortools,或改用「規則排班」。"
        ) from exc

    if not problem.employees or not problem.shifts:
        return [], ["沒有可用的員工或班別,無法排班。"]

    model = cp_model.CpModel()
    days = problem.days
    shifts = problem.shifts
    employees = problem.employees

    # ---- 決策變數 x[(e,d,s)] = 這個人這天上這個班嗎
    x = {}
    for e in employees:
        eid = e["id"]
        for d in days:
            if problem.on_leave(eid, d):
                continue                      # 請假日不建變數,等於強制 0
            for s in shifts:
                if not problem.can_take(eid, s):
                    continue                  # 技能不符
                x[(eid, d, s["id"])] = model.NewBoolVar(f"x_{eid}_{d}_{s['id']}")

    notes = []

    # ---- 硬限制 1:每個班的人數(缺人用 shortage 變數吸收,才不會整個無解)
    shortage = {}
    for d in days:
        for s in shifts:
            need = int(s["required_headcount"])
            pool = [x[(e["id"], d, s["id"])] for e in employees
                    if (e["id"], d, s["id"]) in x]
            short = model.NewIntVar(0, need, f"short_{d}_{s['id']}")
            shortage[(d, s["id"])] = short
            model.Add(sum(pool) + short == need)

    # ---- 硬限制 2:一人一天最多一個班
    work = {}     # work[(e,d)] 是 0/1 的線性運算式
    for e in employees:
        eid = e["id"]
        for d in days:
            pool = [x[(eid, d, s["id"])] for s in shifts if (eid, d, s["id"]) in x]
            if pool:
                model.Add(sum(pool) <= 1)
            work[(eid, d)] = sum(pool) if pool else 0

    # ---- 硬限制 3:鎖定的班一定要成立
    for d, sid, eid in problem.locked:
        if (eid, d, sid) in x:
            model.Add(x[(eid, d, sid)] == 1)
        else:
            notes.append(f"{d} 的鎖定班別與請假/技能設定衝突,已略過該筆鎖定。")

    # ---- 硬限制 4:兩班之間休息時數
    for d1, s1, d2, s2 in conflicting_pairs(problem):
        for e in employees:
            eid = e["id"]
            a, b = (eid, d1, s1), (eid, d2, s2)
            if a in x and b in x:
                model.Add(x[a] + x[b] <= 1)

    # ---- 硬限制 5:連續上班天數
    win = problem.max_consecutive_days + 1
    if win <= len(days):
        for e in employees:
            eid = e["id"]
            for i in range(len(days) - win + 1):
                window = [work[(eid, days[j])] for j in range(i, i + win)]
                model.Add(sum(window) <= problem.max_consecutive_days)

    # ---- 硬限制 6:每週班數上限;軟性:每週最低班數
    weeks: dict = {}
    for d in days:
        iso = datetime.fromisoformat(d).isocalendar()
        weeks.setdefault((iso.year, iso.week), []).append(d)

    under_min = []
    for e in employees:
        eid = e["id"]
        cap = int(e["max_shifts_per_week"])
        floor = int(e["min_shifts_per_week"])
        for wk, wk_days in weeks.items():
            total_wk = sum(work[(eid, d)] for d in wk_days)
            model.Add(total_wk <= cap)
            if floor > 0 and len(wk_days) >= 5:      # 不完整的週不強求
                u = model.NewIntVar(0, floor, f"under_{eid}_{wk[0]}_{wk[1]}")
                model.Add(total_wk + u >= floor)
                under_min.append(u)

    # ---- 軟性目標:班數平均(把區間前 28 天的班數也算進來)
    totals = []
    max_hist = max(problem.history.values()) if problem.history else 0
    upper = len(days) + max_hist + 1
    for e in employees:
        eid = e["id"]
        t = model.NewIntVar(0, upper, f"total_{eid}")
        model.Add(t == sum(work[(eid, d)] for d in days) + problem.history.get(eid, 0))
        totals.append(t)

    spread = model.NewIntVar(0, upper, "spread")
    if len(totals) > 1:
        hi = model.NewIntVar(0, upper, "hi")
        lo = model.NewIntVar(0, upper, "lo")
        model.AddMaxEquality(hi, totals)
        model.AddMinEquality(lo, totals)
        model.Add(spread == hi - lo)
    else:
        model.Add(spread == 0)

    # ---- 軟性目標:同一人盡量排同一種班,不要早晚班跳來跳去
    rotation = []
    shift_ids = [s["id"] for s in shifts]
    if len(shift_ids) > 1:
        for e in employees:
            eid = e["id"]
            for d1, d2 in zip(days, days[1:]):
                for sa in shift_ids:
                    for sb in shift_ids:
                        if sa == sb:
                            continue
                        a, b = (eid, d1, sa), (eid, d2, sb)
                        if a in x and b in x:
                            z = model.NewBoolVar(f"rot_{eid}_{d1}_{sa}_{sb}")
                            model.Add(z >= x[a] + x[b] - 1)
                            rotation.append(z)

    model.Minimize(
        W_SHORTAGE * sum(shortage.values())
        + W_FAIRNESS * spread
        + W_MIN_SHIFT * sum(under_min)
        + W_ROTATION * sum(rotation)
    )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(time_limit_sec)
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(
            "限制條件互相衝突,求解器找不到任何排法。"
            "常見原因:人數不夠、大家的每週上限太低、或請假太集中。"
        )

    result = []
    for (eid, d, sid), var in x.items():
        if solver.Value(var):
            result.append((d, sid, eid))
    result.sort()

    total_short = sum(solver.Value(v) for v in shortage.values())
    if total_short:
        notes.append(f"有 {total_short} 個班次補不滿人,已標在下方警告。")
    notes.append(
        f"求解狀態:{'最佳解' if status == cp_model.OPTIMAL else '可行解'},"
        f"耗時 {solver.WallTime():.2f} 秒,班數最大落差 {solver.Value(spread)} 班。"
    )
    return result, notes
