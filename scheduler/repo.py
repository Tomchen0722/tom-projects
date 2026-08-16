"""資料存取層:每個資料表的新增 / 查詢 / 修改 / 刪除。

路由層只呼叫這裡的函式,不直接寫 SQL。
"""

from datetime import date, timedelta

from .db import query, execute

# ---------------------------------------------------------------- 共用

def _to_dicts(rows):
    return [dict(r) for r in rows]


def daterange(start: str, end: str):
    """產生 start~end(含)的日期字串清單。"""
    d0 = date.fromisoformat(start)
    d1 = date.fromisoformat(end)
    if d1 < d0:
        d0, d1 = d1, d0
    days = (d1 - d0).days
    return [(d0 + timedelta(days=i)).isoformat() for i in range(days + 1)]


# ---------------------------------------------------------------- 員工

def list_employees(include_inactive: bool = False):
    sql = "SELECT * FROM employees"
    if not include_inactive:
        sql += " WHERE active = 1"
    sql += " ORDER BY active DESC, id"
    return _to_dicts(query(sql))


def get_employee(emp_id: int):
    row = query("SELECT * FROM employees WHERE id = ?", (emp_id,), one=True)
    return dict(row) if row else None


def get_employee_by_line(line_user_id: str):
    row = query(
        "SELECT * FROM employees WHERE line_user_id = ?", (line_user_id,), one=True
    )
    return dict(row) if row else None


def create_employee(data: dict) -> int:
    return execute(
        """INSERT INTO employees
           (name, employee_no, phone, line_user_id, role, skills,
            max_shifts_per_week, min_shifts_per_week, active)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            data["name"].strip(),
            (data.get("employee_no") or "").strip(),
            (data.get("phone") or "").strip(),
            (data.get("line_user_id") or "").strip() or None,
            data.get("role") or "staff",
            (data.get("skills") or "").strip(),
            int(data.get("max_shifts_per_week") or 5),
            int(data.get("min_shifts_per_week") or 0),
            1 if str(data.get("active", 1)) not in ("0", "false", "False") else 0,
        ),
    )


def update_employee(emp_id: int, data: dict) -> int:
    current = get_employee(emp_id)
    if not current:
        return 0
    merged = {**current, **{k: v for k, v in data.items() if v is not None}}
    return execute(
        """UPDATE employees SET
             name = ?, employee_no = ?, phone = ?, line_user_id = ?, role = ?,
             skills = ?, max_shifts_per_week = ?, min_shifts_per_week = ?, active = ?
           WHERE id = ?""",
        (
            str(merged["name"]).strip(),
            str(merged.get("employee_no") or "").strip(),
            str(merged.get("phone") or "").strip(),
            (str(merged.get("line_user_id") or "").strip() or None),
            merged.get("role") or "staff",
            str(merged.get("skills") or "").strip(),
            int(merged.get("max_shifts_per_week") or 5),
            int(merged.get("min_shifts_per_week") or 0),
            1 if str(merged.get("active", 1)) not in ("0", "false", "False") else 0,
            emp_id,
        ),
    )


def delete_employee(emp_id: int) -> int:
    """真刪除。已排的班會一起被清掉(ON DELETE CASCADE)。"""
    return execute("DELETE FROM employees WHERE id = ?", (emp_id,))


def deactivate_employee(emp_id: int) -> int:
    """離職但保留歷史紀錄時用這個。"""
    return execute("UPDATE employees SET active = 0 WHERE id = ?", (emp_id,))


# ---------------------------------------------------------------- 班別

def list_shift_types(include_inactive: bool = False):
    sql = "SELECT * FROM shift_types"
    if not include_inactive:
        sql += " WHERE active = 1"
    sql += " ORDER BY sort_order, start_time, id"
    return _to_dicts(query(sql))


def get_shift_type(shift_id: int):
    row = query("SELECT * FROM shift_types WHERE id = ?", (shift_id,), one=True)
    return dict(row) if row else None


def create_shift_type(data: dict) -> int:
    return execute(
        """INSERT INTO shift_types
           (name, code, start_time, end_time, required_headcount,
            required_skill, color, sort_order, active)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            data["name"].strip(),
            (data.get("code") or "").strip(),
            data["start_time"],
            data["end_time"],
            int(data.get("required_headcount") or 1),
            (data.get("required_skill") or "").strip(),
            data.get("color") or "#D98E5A",
            int(data.get("sort_order") or 0),
            1 if str(data.get("active", 1)) not in ("0", "false", "False") else 0,
        ),
    )


def update_shift_type(shift_id: int, data: dict) -> int:
    current = get_shift_type(shift_id)
    if not current:
        return 0
    m = {**current, **{k: v for k, v in data.items() if v is not None}}
    return execute(
        """UPDATE shift_types SET
             name = ?, code = ?, start_time = ?, end_time = ?, required_headcount = ?,
             required_skill = ?, color = ?, sort_order = ?, active = ?
           WHERE id = ?""",
        (
            str(m["name"]).strip(),
            str(m.get("code") or "").strip(),
            m["start_time"],
            m["end_time"],
            int(m.get("required_headcount") or 1),
            str(m.get("required_skill") or "").strip(),
            m.get("color") or "#D98E5A",
            int(m.get("sort_order") or 0),
            1 if str(m.get("active", 1)) not in ("0", "false", "False") else 0,
            shift_id,
        ),
    )


def delete_shift_type(shift_id: int) -> int:
    return execute("DELETE FROM shift_types WHERE id = ?", (shift_id,))


# ---------------------------------------------------------------- 請假

def list_leaves(status: str = "", employee_id: int = 0, start: str = "", end: str = ""):
    sql = """SELECT l.*, e.name AS employee_name
             FROM leave_requests l JOIN employees e ON e.id = l.employee_id
             WHERE 1=1"""
    params: list = []
    if status:
        sql += " AND l.status = ?"
        params.append(status)
    if employee_id:
        sql += " AND l.employee_id = ?"
        params.append(employee_id)
    if start and end:
        sql += " AND l.end_date >= ? AND l.start_date <= ?"
        params += [start, end]
    sql += " ORDER BY l.start_date DESC, l.id DESC"
    return _to_dicts(query(sql, tuple(params)))


def get_leave(leave_id: int):
    row = query(
        """SELECT l.*, e.name AS employee_name
           FROM leave_requests l JOIN employees e ON e.id = l.employee_id
           WHERE l.id = ?""",
        (leave_id,),
        one=True,
    )
    return dict(row) if row else None


def create_leave(data: dict) -> int:
    start = data["start_date"]
    end = data.get("end_date") or start
    if end < start:
        start, end = end, start
    return execute(
        """INSERT INTO leave_requests
           (employee_id, start_date, end_date, leave_type, reason, status, source)
           VALUES (?,?,?,?,?,?,?)""",
        (
            int(data["employee_id"]),
            start,
            end,
            data.get("leave_type") or "特休",
            (data.get("reason") or "").strip(),
            data.get("status") or "pending",
            data.get("source") or "web",
        ),
    )


def update_leave(leave_id: int, data: dict) -> int:
    current = get_leave(leave_id)
    if not current:
        return 0
    m = {**current, **{k: v for k, v in data.items() if v is not None}}
    start, end = m["start_date"], m["end_date"] or m["start_date"]
    if end < start:
        start, end = end, start
    return execute(
        """UPDATE leave_requests SET
             employee_id = ?, start_date = ?, end_date = ?, leave_type = ?,
             reason = ?, status = ?,
             decided_at = CASE WHEN ? IN ('approved','rejected')
                               THEN datetime('now','localtime') ELSE decided_at END
           WHERE id = ?""",
        (
            int(m["employee_id"]),
            start,
            end,
            m.get("leave_type") or "特休",
            str(m.get("reason") or "").strip(),
            m.get("status") or "pending",
            m.get("status") or "pending",
            leave_id,
        ),
    )


def delete_leave(leave_id: int) -> int:
    return execute("DELETE FROM leave_requests WHERE id = ?", (leave_id,))


def leave_map(start: str, end: str) -> dict:
    """回傳 {employee_id: {日期字串, ...}},只算已核准的假。"""
    rows = query(
        """SELECT employee_id, start_date, end_date FROM leave_requests
           WHERE status = 'approved' AND end_date >= ? AND start_date <= ?""",
        (start, end),
    )
    result: dict = {}
    for r in rows:
        days = set(daterange(max(r["start_date"], start), min(r["end_date"], end)))
        result.setdefault(r["employee_id"], set()).update(days)
    return result


# ---------------------------------------------------------------- 排班

def list_assignments(start: str, end: str, employee_id: int = 0):
    sql = """SELECT a.*, e.name AS employee_name, s.name AS shift_name,
                    s.start_time, s.end_time, s.color
             FROM assignments a
             JOIN employees e   ON e.id = a.employee_id
             JOIN shift_types s ON s.id = a.shift_type_id
             WHERE a.work_date BETWEEN ? AND ?"""
    params: list = [start, end]
    if employee_id:
        sql += " AND a.employee_id = ?"
        params.append(employee_id)
    sql += " ORDER BY a.work_date, s.sort_order, s.start_time, e.name"
    return _to_dicts(query(sql, tuple(params)))


def get_assignment(assignment_id: int):
    row = query(
        """SELECT a.*, e.name AS employee_name, s.name AS shift_name,
                  s.start_time, s.end_time, s.color
           FROM assignments a
           JOIN employees e   ON e.id = a.employee_id
           JOIN shift_types s ON s.id = a.shift_type_id
           WHERE a.id = ?""",
        (assignment_id,),
        one=True,
    )
    return dict(row) if row else None


def create_assignment(data: dict) -> int:
    return execute(
        """INSERT OR IGNORE INTO assignments
           (work_date, shift_type_id, employee_id, locked, status, note)
           VALUES (?,?,?,?,?,?)""",
        (
            data["work_date"],
            int(data["shift_type_id"]),
            int(data["employee_id"]),
            1 if str(data.get("locked", 0)) in ("1", "true", "True") else 0,
            data.get("status") or "draft",
            (data.get("note") or "").strip(),
        ),
    )


def update_assignment(assignment_id: int, data: dict) -> int:
    current = get_assignment(assignment_id)
    if not current:
        return 0
    m = {**current, **{k: v for k, v in data.items() if v is not None}}
    return execute(
        """UPDATE assignments SET
             work_date = ?, shift_type_id = ?, employee_id = ?,
             locked = ?, status = ?, note = ?
           WHERE id = ?""",
        (
            m["work_date"],
            int(m["shift_type_id"]),
            int(m["employee_id"]),
            1 if str(m.get("locked", 0)) in ("1", "true", "True") else 0,
            m.get("status") or "draft",
            str(m.get("note") or "").strip(),
            assignment_id,
        ),
    )


def delete_assignment(assignment_id: int) -> int:
    return execute("DELETE FROM assignments WHERE id = ?", (assignment_id,))


def clear_unlocked(start: str, end: str) -> int:
    """自動排班前清掉區間內沒鎖定的班,鎖定的保留。"""
    return execute(
        "DELETE FROM assignments WHERE work_date BETWEEN ? AND ? AND locked = 0",
        (start, end),
    )


def publish_range(start: str, end: str) -> int:
    return execute(
        "UPDATE assignments SET status = 'published' WHERE work_date BETWEEN ? AND ?",
        (start, end),
    )


def bulk_insert_assignments(rows: list) -> int:
    """rows: [(work_date, shift_type_id, employee_id), ...]"""
    count = 0
    for work_date, shift_type_id, employee_id in rows:
        count += create_assignment(
            {
                "work_date": work_date,
                "shift_type_id": shift_type_id,
                "employee_id": employee_id,
            }
        ) and 1
    return count


# ---------------------------------------------------------------- 調班

def list_swaps(status: str = ""):
    sql = """SELECT w.*, e.name AS requester_name, a.work_date, a.shift_type_id,
                    s.name AS shift_name, ts.name AS target_shift_name
             FROM swap_requests w
             JOIN employees e   ON e.id = w.requester_id
             JOIN assignments a ON a.id = w.assignment_id
             JOIN shift_types s ON s.id = a.shift_type_id
             LEFT JOIN shift_types ts ON ts.id = w.target_shift_type_id
             WHERE 1=1"""
    params: list = []
    if status:
        sql += " AND w.status = ?"
        params.append(status)
    sql += " ORDER BY w.created_at DESC"
    return _to_dicts(query(sql, tuple(params)))


def get_swap(swap_id: int):
    rows = [s for s in list_swaps() if s["id"] == swap_id]
    return rows[0] if rows else None


def create_swap(data: dict) -> int:
    return execute(
        """INSERT INTO swap_requests
           (assignment_id, requester_id, target_shift_type_id, target_date,
            reason, status, source)
           VALUES (?,?,?,?,?,?,?)""",
        (
            int(data["assignment_id"]),
            int(data["requester_id"]),
            int(data["target_shift_type_id"]) if data.get("target_shift_type_id") else None,
            data.get("target_date") or None,
            (data.get("reason") or "").strip(),
            data.get("status") or "pending",
            data.get("source") or "web",
        ),
    )


def decide_swap(swap_id: int, status: str) -> int:
    """核准調班時,直接把原本那筆排班改成新的日期 / 班別。"""
    swap = get_swap(swap_id)
    if not swap:
        return 0
    if status == "approved":
        patch = {}
        if swap.get("target_shift_type_id"):
            patch["shift_type_id"] = swap["target_shift_type_id"]
        if swap.get("target_date"):
            patch["work_date"] = swap["target_date"]
        if patch:
            patch["locked"] = 1
            update_assignment(swap["assignment_id"], patch)
    return execute(
        """UPDATE swap_requests
           SET status = ?, decided_at = datetime('now','localtime')
           WHERE id = ?""",
        (status, swap_id),
    )


def delete_swap(swap_id: int) -> int:
    return execute("DELETE FROM swap_requests WHERE id = ?", (swap_id,))


# ---------------------------------------------------------------- 統計

def workload_stats(start: str, end: str):
    """每位員工在區間內的班數,用來看排班公不公平。"""
    return _to_dicts(
        query(
            """SELECT e.id, e.name, COUNT(a.id) AS shifts
               FROM employees e
               LEFT JOIN assignments a
                      ON a.employee_id = e.id AND a.work_date BETWEEN ? AND ?
               WHERE e.active = 1
               GROUP BY e.id, e.name
               ORDER BY shifts DESC, e.name""",
            (start, end),
        )
    )
