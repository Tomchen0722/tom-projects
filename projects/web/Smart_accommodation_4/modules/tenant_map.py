"""租客推薦清單與地圖連動的純狀態／地理計算。

本模組只處理唯一 listing_id、1 公里直線範圍、Plotly 選取事件與
viewport 版本鍵；不接觸必要條件、五科評分、NLP、推薦排序或分頁。
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import hashlib
import math
from numbers import Integral, Real

import numpy as np


EARTH_RADIUS_M = 6_371_000
DEFAULT_FOCUS_RADIUS_M = 1_000
DEFAULT_CIRCLE_VERTICES = 72


class MapSelectionError(ValueError):
    """地圖選取目標無效、不存在或缺少可定位座標。"""


@dataclass(frozen=True)
class ListingMapFocus:
    """選定房源與同一候選集合中的直線範圍摘要。"""

    listing_id: int
    latitude: float
    longitude: float
    radius_m: int
    nearby_listing_ids: tuple[int, ...]

    @property
    def nearby_count(self) -> int:
        return len(self.nearby_listing_ids)


def _coerce_listing_id(value) -> int:
    if isinstance(value, bool) or value is None:
        raise MapSelectionError("listing_id must be a valid integer")
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        numeric = float(value)
        if math.isfinite(numeric) and numeric.is_integer():
            return int(numeric)
        raise MapSelectionError("listing_id must be a valid integer")
    text = str(value).strip()
    if not text:
        raise MapSelectionError("listing_id must be a valid integer")
    try:
        return int(text)
    except (TypeError, ValueError) as exc:
        raise MapSelectionError(
            "listing_id must be a valid integer") from exc


def _positive_distance(value, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a positive number")
    normalized = float(value)
    if not math.isfinite(normalized) or normalized <= 0:
        raise ValueError(f"{name} must be a positive number")
    return normalized


def haversine_distances(center_lat, center_lon, latitudes, longitudes):
    """以 Haversine 計算中心點至多個座標的直線距離（公尺）。"""
    lat1 = math.radians(float(center_lat))
    lon1 = math.radians(float(center_lon))
    lat2 = np.radians(np.asarray(latitudes, dtype=float))
    lon2 = np.radians(np.asarray(longitudes, dtype=float))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    value = (
        np.sin(dlat / 2) ** 2
        + math.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    )
    return EARTH_RADIUS_M * 2 * np.arcsin(np.sqrt(np.clip(value, 0, 1)))


def focus_for_listing(
    candidates,
    listing_id,
    *,
    radius_m=DEFAULT_FOCUS_RADIUS_M,
) -> ListingMapFocus:
    """依唯一 ID 建立地圖聚焦摘要，不修改或切片原候選集合。"""
    target_id = _coerce_listing_id(listing_id)
    radius = _positive_distance(radius_m, "radius_m")
    required = {"id", "latitude", "longitude"}
    missing = required.difference(candidates.columns)
    if missing:
        raise ValueError(
            "candidates missing required columns: "
            + ", ".join(sorted(missing))
        )

    target_rows = candidates[candidates["id"].map(_coerce_listing_id) == target_id]
    if len(target_rows) != 1:
        raise MapSelectionError(
            "listing_id must resolve to exactly one candidate")
    target = target_rows.iloc[0]
    latitude = float(target["latitude"])
    longitude = float(target["longitude"])
    if not math.isfinite(latitude) or not math.isfinite(longitude):
        raise MapSelectionError("selected listing has no valid coordinates")

    latitudes = candidates["latitude"].to_numpy(dtype=float)
    longitudes = candidates["longitude"].to_numpy(dtype=float)
    distances = haversine_distances(
        latitude, longitude, latitudes, longitudes)
    within = np.isfinite(distances) & (distances <= radius + 1e-6)
    nearby_ids = tuple(
        _coerce_listing_id(value)
        for value in candidates.loc[within, "id"].tolist()
    )
    return ListingMapFocus(
        listing_id=target_id,
        latitude=latitude,
        longitude=longitude,
        radius_m=int(round(radius)),
        nearby_listing_ids=nearby_ids,
    )


def circle_coordinates(
    center_lat,
    center_lon,
    *,
    radius_m=DEFAULT_FOCUS_RADIUS_M,
    vertices=DEFAULT_CIRCLE_VERTICES,
):
    """回傳封閉的等距圓周座標，供 Plotly 畫直線距離參考圈。"""
    radius = _positive_distance(radius_m, "radius_m")
    if isinstance(vertices, bool) or not isinstance(vertices, Integral):
        raise ValueError("vertices must be an integer of at least 12")
    vertex_count = int(vertices)
    if vertex_count < 12:
        raise ValueError("vertices must be an integer of at least 12")

    lat1 = math.radians(float(center_lat))
    lon1 = math.radians(float(center_lon))
    angular_distance = radius / EARTH_RADIUS_M
    bearings = np.linspace(0, 2 * math.pi, vertex_count + 1)
    latitudes = np.arcsin(
        math.sin(lat1) * math.cos(angular_distance)
        + math.cos(lat1)
        * math.sin(angular_distance)
        * np.cos(bearings)
    )
    longitudes = lon1 + np.arctan2(
        np.sin(bearings)
        * math.sin(angular_distance)
        * math.cos(lat1),
        math.cos(angular_distance)
        - math.sin(lat1) * np.sin(latitudes),
    )
    return tuple(np.degrees(latitudes)), tuple(np.degrees(longitudes))


def _mapping_value(value, key):
    if isinstance(value, Mapping):
        return value.get(key)
    return getattr(value, key, None)


def listing_id_from_selection_event(event) -> int | None:
    """從 Streamlit Plotly point selection 取出 customdata 的 listing_id。"""
    if event is None:
        return None
    selection = _mapping_value(event, "selection")
    if selection is None:
        return None
    points = _mapping_value(selection, "points") or ()
    for point in points:
        customdata = _mapping_value(point, "customdata")
        raw_id = None
        if (
            isinstance(customdata, Sequence)
            and not isinstance(customdata, (str, bytes))
            and len(customdata)
        ):
            raw_id = customdata[0]
        if raw_id is None:
            raw_id = _mapping_value(point, "id")
        if raw_id is None:
            continue
        try:
            return _coerce_listing_id(raw_id)
        except MapSelectionError:
            continue
    return None


def viewport_revision(ordered_listing_ids, selected_listing_id) -> str:
    """候選順序或選定 ID 改變時才建立新的 Plotly viewport 版本。"""
    ids = ",".join(str(_coerce_listing_id(value))
                   for value in ordered_listing_ids)
    selected = (
        "overview"
        if selected_listing_id is None
        else str(_coerce_listing_id(selected_listing_id))
    )
    payload = f"{ids}|selected={selected}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]
