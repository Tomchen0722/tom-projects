import json
import math
from copy import deepcopy
from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from modules import tenant_map


ROOT = Path(__file__).resolve().parent.parent
TENANT_APP = str(next((ROOT / "pages").glob("2_*.py")))


def _point_north(lat, lon, distance_m):
    earth_radius_m = 6_371_000
    return lat + math.degrees(distance_m / earth_radius_m), lon


def _candidate_frame():
    center_lat, center_lon = 0.0, 121.5
    distances = (0.0, 999.0, 1_000.0, 1_001.0)
    rows = []
    for listing_id, distance in zip((101, 102, 103, 104), distances):
        lat, lon = _point_north(center_lat, center_lon, distance)
        rows.append(
            {
                "id": listing_id,
                "name": "重複名稱" if listing_id in (101, 104) else f"房源 {listing_id}",
                "latitude": lat,
                "longitude": lon,
                "Q": 10 - listing_id / 1_000,
                "total": 25 - listing_id / 100,
            }
        )
    return pd.DataFrame(rows)


def test_focus_uses_listing_id_and_includes_exact_one_kilometre_boundary():
    candidates = _candidate_frame()

    focus = tenant_map.focus_for_listing(candidates, 101, radius_m=1_000)

    assert focus.listing_id == 101
    assert focus.nearby_listing_ids == (101, 102, 103)
    assert focus.nearby_count == 3
    assert 104 not in focus.nearby_listing_ids


def test_focus_does_not_mutate_candidate_order_scores_or_names():
    candidates = _candidate_frame()
    before = candidates.copy(deep=True)

    tenant_map.focus_for_listing(candidates, 101, radius_m=1_000)

    pd.testing.assert_frame_equal(candidates, before)


@pytest.mark.parametrize("listing_id", [None, "", "missing", 999])
def test_focus_rejects_invalid_or_missing_listing_id(listing_id):
    with pytest.raises(tenant_map.MapSelectionError):
        tenant_map.focus_for_listing(
            _candidate_frame(), listing_id, radius_m=1_000)


def test_circle_coordinates_are_closed_and_stay_on_requested_radius():
    lats, lons = tenant_map.circle_coordinates(
        25.0478, 121.5319, radius_m=1_000, vertices=72)

    assert len(lats) == len(lons) == 73
    assert lats[0] == pytest.approx(lats[-1])
    assert lons[0] == pytest.approx(lons[-1])
    distances = tenant_map.haversine_distances(
        25.0478, 121.5319, lats[:-1], lons[:-1])
    assert min(distances) == pytest.approx(1_000, abs=0.01)
    assert max(distances) == pytest.approx(1_000, abs=0.01)


@pytest.mark.parametrize(
    ("event", "expected"),
    [
        ({"selection": {"points": [{"customdata": [123, "$2,000"]}]}}, 123),
        ({"selection": {"points": [{"customdata": ("456",)}]}}, 456),
        ({"selection": {"points": [{"id": "789"}]}}, 789),
        ({"selection": {"points": []}}, None),
        (None, None),
    ],
)
def test_listing_id_from_selection_event(event, expected):
    original = deepcopy(event)

    assert tenant_map.listing_id_from_selection_event(event) == expected
    assert event == original


def test_viewport_revision_changes_only_for_scope_or_selected_listing():
    original = tenant_map.viewport_revision([10, 20, 30], None)
    same = tenant_map.viewport_revision((10, 20, 30), None)
    selected = tenant_map.viewport_revision([10, 20, 30], 20)
    reordered = tenant_map.viewport_revision([20, 10, 30], None)

    assert original == same
    assert original != selected
    assert original != reordered


def test_tenant_page_exposes_map_focus_links_and_selected_map_summary():
    app = AppTest.from_file(TENANT_APP, default_timeout=120).run()

    assert not app.exception, app.exception
    initial_page = app.session_state["t_page"]
    photo_buttons = [
        button for button in app.button
        if str(button.key).startswith("map_photo_")
    ]
    title_buttons = [
        button for button in app.button
        if str(button.key).startswith("map_title_")
    ]
    assert len(photo_buttons) == len(title_buttons) == 8
    selected_id = int(str(photo_buttons[0].key).removeprefix("map_photo_"))
    markup = "".join(item.value for item in app.markdown)
    assert "?map_listing=" not in markup

    app.session_state["selected_listing_id"] = selected_id
    app.run()

    assert not app.exception, app.exception
    assert app.session_state["t_page"] == initial_page
    assert app.session_state["selected_listing_id"] == selected_id
    selected_markup = "".join(item.value for item in app.markdown)
    assert "1 公里直線範圍" in selected_markup
    assert "藍色圖釘" in selected_markup
    assert app.button(key=f"t_map_detail_{selected_id}")

    charts = app.get("plotly_chart")
    assert len(charts) == 1
    spec = json.loads(charts[0].proto.spec)
    names = [trace.get("name") for trace in spec["data"]]
    assert "符合條件房源" in names
    assert "1 公里直線範圍" in names
    assert "目前定位房源" in names
    assert charts[0].proto.selection_mode


def test_map_dimension_change_preserves_selection_page_and_candidate_scope():
    app = AppTest.from_file(TENANT_APP, default_timeout=120).run()

    assert not app.exception, app.exception
    photo_button = next(
        button for button in app.button
        if str(button.key).startswith("map_photo_")
    )
    selected_id = int(str(photo_button.key).removeprefix("map_photo_"))
    scope_before = app.session_state["_t_page_scope"]
    app.session_state["selected_listing_id"] = selected_id

    app.selectbox(key="t_mapdim").select("交通方便").run()

    assert not app.exception, app.exception
    assert app.session_state["selected_listing_id"] == selected_id
    assert app.session_state["_t_page_scope"] == scope_before
    assert app.session_state["t_page"] == 1


@pytest.mark.parametrize("button_prefix", ["map_photo_", "map_title_"])
def test_card_map_focus_preserves_applied_sidebar_filters(button_prefix):
    app = AppTest.from_file(TENANT_APP, default_timeout=120).run()

    assert not app.exception, app.exception
    app.multiselect(key="t_nb").set_value(["大安區"]).run()
    app.multiselect(key="t_rt").set_value(["私人套房"]).run()
    assert not app.exception, app.exception
    applied_before = {
        key: deepcopy(app.session_state[key])
        for key in ("t_nb", "t_rt", "t_price", "t_must", "t_top2", "t_wish")
    }
    scope_before = app.session_state["_t_page_scope"]
    button = next(
        item for item in app.button
        if str(item.key).startswith(button_prefix)
    )
    selected_id = int(str(button.key).removeprefix(button_prefix))

    button.click().run()

    assert not app.exception, app.exception
    assert app.session_state["selected_listing_id"] == selected_id
    assert app.session_state["_t_page_scope"] == scope_before
    for key, value in applied_before.items():
        assert app.session_state[key] == value
    assert app.session_state["t_nb"] == ["大安區"]
    assert app.session_state["t_rt"] == ["私人套房"]
