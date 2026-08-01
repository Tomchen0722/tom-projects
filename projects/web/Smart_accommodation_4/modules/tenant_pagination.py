"""租客推薦清單的純分頁計算。

本模組只處理頁數、頁碼驗證與資料切片邊界，不接觸候選篩選、
五科評分、NLP 或推薦排序。
"""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral


class PaginationInputError(ValueError):
    """使用者輸入的頁碼不是目前結果範圍內的整數。"""


@dataclass(frozen=True)
class PageWindow:
    """一頁在已排序候選集合中的零基底切片與顯示範圍。"""

    page: int
    total_pages: int
    start: int
    stop: int
    display_start: int
    display_end: int


def _require_non_negative_int(value, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return int(value)


def _require_positive_int(value, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return int(value)


def total_pages(total_items: int, page_size: int) -> int:
    """依目前結果筆數動態計算總頁數；空集合仍保留第 1 頁狀態。"""
    item_count = _require_non_negative_int(total_items, "total_items")
    size = _require_positive_int(page_size, "page_size")
    return max(1, (item_count + size - 1) // size)


def validate_page(page: int, page_count: int) -> int:
    """驗證頁碼是 1～目前總頁數內的整數，禁止靜默截斷。"""
    if isinstance(page, bool) or not isinstance(page, Integral):
        raise PaginationInputError("page must be an integer")
    max_page = _require_positive_int(page_count, "page_count")
    normalized = int(page)
    if not 1 <= normalized <= max_page:
        raise PaginationInputError(
            f"page must be between 1 and {max_page}")
    return normalized


def page_window(total_items: int, page: int, page_size: int) -> PageWindow:
    """回傳目前頁在既有排序結果中的切片範圍，不改動原始資料。"""
    item_count = _require_non_negative_int(total_items, "total_items")
    size = _require_positive_int(page_size, "page_size")
    page_count = total_pages(item_count, size)
    current = validate_page(page, page_count)
    start = (current - 1) * size
    stop = min(start + size, item_count)
    if item_count == 0:
        display_start = display_end = 0
    else:
        display_start = start + 1
        display_end = stop
    return PageWindow(
        page=current,
        total_pages=page_count,
        start=start,
        stop=stop,
        display_start=display_start,
        display_end=display_end,
    )


def scope_key(ordered_listing_ids, page_size: int) -> tuple[int, tuple[int, ...]]:
    """建立結果集合與排序的穩定鍵；地圖呈現狀態不包含在內。"""
    size = _require_positive_int(page_size, "page_size")
    return size, tuple(int(listing_id) for listing_id in ordered_listing_ids)
