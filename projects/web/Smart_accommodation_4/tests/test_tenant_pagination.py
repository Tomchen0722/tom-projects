from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from modules import tenant_pagination as pagination


ROOT = Path(__file__).resolve().parent.parent
TENANT_APP = str(next((ROOT / "pages").glob("2_*.py")))


@pytest.mark.parametrize(
    ("total_items", "page_size", "expected"),
    [
        (0, 8, 1),
        (1, 8, 1),
        (8, 8, 1),
        (9, 8, 2),
        (300, 8, 38),
    ],
)
def test_total_pages_uses_current_result_count(total_items, page_size, expected):
    assert pagination.total_pages(total_items, page_size) == expected


@pytest.mark.parametrize("total_items", [-1, -8])
def test_total_pages_rejects_negative_result_count(total_items):
    with pytest.raises(ValueError, match="total_items"):
        pagination.total_pages(total_items, 8)


@pytest.mark.parametrize("page_size", [0, -1, 2.5, "8", True])
def test_total_pages_rejects_invalid_page_size(page_size):
    with pytest.raises(ValueError, match="page_size"):
        pagination.total_pages(20, page_size)


def test_page_window_reports_first_middle_and_last_page_bounds():
    first = pagination.page_window(total_items=300, page=1, page_size=8)
    middle = pagination.page_window(total_items=300, page=20, page_size=8)
    last = pagination.page_window(total_items=300, page=38, page_size=8)

    assert (first.start, first.stop, first.display_start, first.display_end) == (
        0, 8, 1, 8)
    assert (middle.start, middle.stop, middle.display_start,
            middle.display_end) == (152, 160, 153, 160)
    assert (last.start, last.stop, last.display_start, last.display_end) == (
        296, 300, 297, 300)
    assert last.total_pages == 38


def test_empty_result_window_has_no_fake_item_number():
    window = pagination.page_window(total_items=0, page=1, page_size=8)

    assert window.total_pages == 1
    assert (window.start, window.stop) == (0, 0)
    assert (window.display_start, window.display_end) == (0, 0)


@pytest.mark.parametrize("page", [0, 39, -1, 1.5, "2", "", None, True])
def test_page_window_rejects_invalid_or_out_of_range_page(page):
    with pytest.raises(pagination.PaginationInputError):
        pagination.page_window(total_items=300, page=page, page_size=8)


def test_scope_key_is_stable_but_order_sensitive():
    original = pagination.scope_key([10, 20, 30], page_size=8)
    same = pagination.scope_key((10, 20, 30), page_size=8)
    reordered = pagination.scope_key([20, 10, 30], page_size=8)
    resized = pagination.scope_key([10, 20, 30], page_size=10)

    assert original == same
    assert original != reordered
    assert original != resized


def test_pagination_only_selects_a_view_without_changing_rank_or_scores():
    ranked = pd.DataFrame(
        {
            "id": list(range(1, 21)),
            "Q": [10 - i / 100 for i in range(20)],
            "total": [25 - i / 10 for i in range(20)],
            "s_transit": [5.0] * 20,
            "s_life": [4.0] * 20,
            "s_price": [3.0] * 20,
            "s_reputation": [2.0] * 20,
            "s_amenity": [1.0] * 20,
            "nlp_score": [1.5] * 20,
        }
    )
    before = ranked.copy(deep=True)

    window = pagination.page_window(
        total_items=len(ranked), page=2, page_size=8)
    visible = ranked.iloc[window.start:window.stop]

    assert visible["id"].tolist() == list(range(9, 17))
    pd.testing.assert_frame_equal(ranked, before)


def test_tenant_page_navigation_controls_keep_result_scope_and_map_state():
    app = AppTest.from_file(TENANT_APP, default_timeout=120).run()

    assert not app.exception, app.exception
    page_count = app.session_state["_t_page_count"]
    scope_before = app.session_state["_t_page_scope"]
    number_input = app.number_input(key="t_page_input")
    first_page_markup = "".join(item.value for item in app.markdown)

    assert page_count > 1
    assert (number_input.min, number_input.max) == (1.0, float(page_count))
    assert "顯示 1–8，共 300 間房源" in first_page_markup
    assert "房源 ｜ 第" not in first_page_markup
    assert app.button(key="t_first").disabled
    assert app.button(key="t_prev").disabled
    assert not app.button(key="t_next").disabled
    assert not app.button(key="t_last").disabled

    app.button(key="t_next").click().run()
    assert not app.exception, app.exception
    assert app.session_state["t_page"] == 2
    assert app.session_state["t_page_input"] == 2
    assert app.session_state["_t_page_scope"] == scope_before

    target_page = min(3, page_count)
    app.number_input(key="t_page_input").set_value(target_page).run()
    assert not app.exception, app.exception
    assert app.session_state["t_page"] == target_page
    assert app.session_state["_t_page_scope"] == scope_before

    app.selectbox(key="t_mapdim").select("交通方便").run()
    assert not app.exception, app.exception
    assert app.session_state["t_page"] == target_page
    assert app.session_state["_t_page_scope"] == scope_before

    app.button(key="t_last").click().run()
    assert not app.exception, app.exception
    last_page_markup = "".join(item.value for item in app.markdown)
    assert app.session_state["t_page"] == page_count
    assert "顯示 297–300，共 300 間房源" in last_page_markup
    assert app.button(key="t_next").disabled
    assert app.button(key="t_last").disabled

    app.button(key="t_first").click().run()
    assert not app.exception, app.exception
    assert app.session_state["t_page"] == 1
    assert app.button(key="t_first").disabled
    assert app.button(key="t_prev").disabled
