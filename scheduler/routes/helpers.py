"""路由共用的小工具:登入檢查、日期區間。"""

from calendar import monthrange
from datetime import date, timedelta
from functools import wraps

from flask import current_app, redirect, request, session, url_for

WEEKDAY_TW = ["一", "二", "三", "四", "五", "六", "日"]


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("web.login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


def month_range(year: int = 0, month: int = 0):
    today = date.today()
    year = year or today.year
    month = month or today.month
    last = monthrange(year, month)[1]
    return date(year, month, 1).isoformat(), date(year, month, last).isoformat()


def requested_range():
    """從 query string 取 start/end,沒給就用本月。"""
    start = request.args.get("start", "")
    end = request.args.get("end", "")
    if start and end:
        return start, end
    ym = request.args.get("month", "")
    if ym:
        try:
            y, m = (int(v) for v in ym.split("-"))
            return month_range(y, m)
        except ValueError:
            pass
    return month_range()


def shift_month(ym: str, delta: int) -> str:
    y, m = (int(v) for v in ym.split("-"))
    m += delta
    while m < 1:
        m += 12
        y -= 1
    while m > 12:
        m -= 12
        y += 1
    return f"{y:04d}-{m:02d}"


def build_calendar(start: str, end: str):
    """把區間切成週,方便 template 畫月曆。回傳 [[date|None x7], ...]"""
    d0 = date.fromisoformat(start)
    d1 = date.fromisoformat(end)
    grid = []
    cur = d0 - timedelta(days=d0.weekday())        # 對齊到星期一
    tail = d1 + timedelta(days=6 - d1.weekday())
    week = []
    while cur <= tail:
        week.append(cur.isoformat() if d0 <= cur <= d1 else None)
        if len(week) == 7:
            grid.append(week)
            week = []
        cur += timedelta(days=1)
    if week:
        grid.append(week)
    return grid


def line_ready() -> bool:
    return bool(current_app.config.get("LINE_CHANNEL_ACCESS_TOKEN"))
