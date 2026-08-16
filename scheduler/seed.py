"""範例資料。第一次啟動時灌進去,讓系統一打開就有東西可以看。"""

from . import repo

SHIFTS = [
    {"name": "早班", "code": "A", "start_time": "07:00", "end_time": "15:00",
     "required_headcount": 2, "color": "#E0A458", "sort_order": 1},
    {"name": "中班", "code": "B", "start_time": "14:00", "end_time": "22:00",
     "required_headcount": 2, "color": "#C9704B", "sort_order": 2},
    {"name": "大夜", "code": "C", "start_time": "22:00", "end_time": "07:00",
     "required_headcount": 1, "color": "#8C5A3C", "sort_order": 3},
]

EMPLOYEES = [
    {"name": "陳曉春", "employee_no": "A001", "role": "manager",
     "skills": "收銀,咖啡", "max_shifts_per_week": 5, "min_shifts_per_week": 4},
    {"name": "林夏樹", "employee_no": "A002", "skills": "收銀",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
    {"name": "王秋實", "employee_no": "A003", "skills": "咖啡",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
    {"name": "張冬陽", "employee_no": "A004", "skills": "收銀,烘焙",
     "max_shifts_per_week": 4, "min_shifts_per_week": 2},
    {"name": "李清和", "employee_no": "A005", "skills": "咖啡,烘焙",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
    {"name": "吳明里", "employee_no": "A006", "skills": "收銀",
     "max_shifts_per_week": 3, "min_shifts_per_week": 1},
    {"name": "黃小雪", "employee_no": "A007", "skills": "咖啡",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
    {"name": "許立行", "employee_no": "A008", "skills": "收銀,咖啡",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
    {"name": "蔡宜靜", "employee_no": "A009", "skills": "收銀,烘焙",
     "max_shifts_per_week": 5, "min_shifts_per_week": 3},
]
# 人力配置說明:早班 2 + 中班 2 + 大夜 1 = 每天 5 個班,一週 35 個班。
# 上面 9 個人的每週上限加起來是 42,留了緩衝給請假,自動排班才排得滿。


def seed_if_empty() -> bool:
    """資料庫是空的才灌範例。回傳有沒有真的灌。"""
    if repo.list_employees(include_inactive=True) or repo.list_shift_types(include_inactive=True):
        return False
    for s in SHIFTS:
        repo.create_shift_type(s)
    for e in EMPLOYEES:
        repo.create_employee(e)
    return True
