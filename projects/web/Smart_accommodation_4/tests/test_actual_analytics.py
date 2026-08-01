# -*- coding: utf-8 -*-
"""actual_analytics 純計算層單元測試（不讀真實資料、不需 streamlit）。"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules import actual_analytics as aa
from scripts.build_actual_metrics import occupancy_days


# ══════════════════════════════════════════════════════════
# 官方公式：入住天數 = min(評論數 × 2 × max(min_nights, 3), 上限)
# ══════════════════════════════════════════════════════════
def test_入住天數_採官方公式且住宿天數有下限3():
    # 5 則評論 × 2 = 10 次入住；min_nights=1 → 取下限 3 晚 → 30 天
    out = occupancy_days(pd.Series([5]), pd.Series([1]), window_days=273)
    assert out.iloc[0] == pytest.approx(30.0)


def test_入住天數_min_nights大於3時採實際值():
    # 3 則 × 2 = 6 次 × 7 晚 = 42 天
    out = occupancy_days(pd.Series([3]), pd.Series([7]), window_days=273)
    assert out.iloc[0] == pytest.approx(42.0)


def test_入住天數_上限依窗口長度等比縮放():
    # 官方上限一年 255 天；273 天窗口 → 255/365*273 ≈ 190.7
    cap = 273 * (255 / 365)
    out = occupancy_days(pd.Series([9999]), pd.Series([30]), window_days=273)
    assert out.iloc[0] == pytest.approx(cap)


def test_入住天數_零評論為零():
    out = occupancy_days(pd.Series([0]), pd.Series([3]), window_days=273)
    assert out.iloc[0] == pytest.approx(0.0)


def test_入住天數_min_nights缺值退回下限3():
    out = occupancy_days(pd.Series([5]), pd.Series([np.nan]), window_days=273)
    assert out.iloc[0] == pytest.approx(30.0)


# ══════════════════════════════════════════════════════════
# 對照聚合
# ══════════════════════════════════════════════════════════
@pytest.fixture
def sample():
    """6 間房源：2 間 dormant（須被排除）、4 間納入。"""
    pred = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "host_id": [10, 10, 20, 30, 40, 40],
        "price": [1000.0, 1000.0, 2000.0, 1000.0, 1000.0, 1000.0],
        "vac_pred_365": [0.20, 0.40, 0.80, 0.50, 0.90, 0.90],
    })
    actual = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "rev_window": [20, 10, 0, 5, 0, 0],
        "occ_days": [120.0, 60.0, 0.0, 30.0, 0.0, 0.0],
        "real_vac": [0.5604, 0.7802, 1.0, 0.8901, 1.0, 1.0],
        "real_revenue_365": [160439.0, 80219.0, 0.0, 40110.0, 0.0, 0.0],
        # 房源 5、6 為前後兩期都零評論 → dormant
        "is_dormant": [0, 0, 0, 0, 1, 1],
    })
    return pred, actual


def test_dormant房源被排除在母體外(sample):
    pred, actual = sample
    d = aa.join_actual(pred, actual)
    assert len(d) == 4                       # 6 間扣掉 2 間 dormant
    assert set(d["id"]) == {1, 2, 3, 4}


def test_預估與實際採同一母體(sample):
    """鐵律：排除 dormant 時，預估欄也必須跟著排，否則比較不公平。"""
    pred, actual = sample
    k = aa.compare_kpis(pred, actual, commission=0.15)
    row = k.set_index("指標").loc["平均空屋率"]
    # 預估只算納入的 4 間：(0.20+0.40+0.80+0.50)/4 = 0.475
    assert row["預估"] == pytest.approx(0.475)
    # 實際同樣只算 4 間
    assert row["實際"] == pytest.approx((0.5604 + 0.7802 + 1.0 + 0.8901) / 4)


def test_高風險占比雙邊都用60門檻(sample):
    pred, actual = sample
    k = aa.compare_kpis(pred, actual, commission=0.15).set_index("指標")
    row = k.loc["高風險占比"]
    assert row["預估"] == pytest.approx(1 / 4)   # 只有 0.80 >= 0.6
    assert row["實際"] == pytest.approx(3 / 4)   # 0.78/1.0/0.89 >= 0.6


def test_活躍房東數_實際只算窗口內有評論者(sample):
    pred, actual = sample
    k = aa.compare_kpis(pred, actual, commission=0.15).set_index("指標")
    row = k.loc["活躍房東數"]
    # 納入的 4 間屬 host 10/10/20/30 → 預估 3 位
    assert row["預估"] == 3
    # host 20 只有房源 3，窗口內零評論(萎縮掛零) → 實際只剩 host 10/30
    assert row["實際"] == 2


def test_平台年收入等於營收乘抽成(sample):
    pred, actual = sample
    k = aa.compare_kpis(pred, actual, commission=0.15).set_index("指標")
    rev = k.loc["年營收總額"]
    fee = k.loc["平台年收入"]
    assert fee["預估"] == pytest.approx(rev["預估"] * 0.15)
    assert fee["實際"] == pytest.approx(rev["實際"] * 0.15)


def test_落差欄為實際減預估(sample):
    pred, actual = sample
    k = aa.compare_kpis(pred, actual, commission=0.15)
    assert (k["落差"] == k["實際"] - k["預估"]).all()


def test_空母體不丟例外():
    empty_p = pd.DataFrame(columns=["id", "host_id", "price", "vac_pred_365"])
    empty_a = pd.DataFrame(columns=["id", "rev_window", "occ_days", "real_vac",
                                    "real_revenue_365", "is_dormant"])
    k = aa.compare_kpis(empty_p, empty_a, commission=0.15)
    assert len(k) == 5
    assert (k["實際"] == 0).all()


def test_window_days常數與計畫一致():
    assert aa.WINDOW_DAYS == 273
    assert aa.WINDOW_LABEL == "2025-09-30 ~ 2026-06-30"
