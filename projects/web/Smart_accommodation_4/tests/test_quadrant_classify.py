# -*- coding: utf-8 -*-
"""quadrant.classify_row 收緊後的分類邊界測試(2026-07-24 定案規則)。

規則(體質佳 = green tier):
  無 booked_rate_d90                              -> unknown
  red/yellow + 訂房率 < 20%                        -> alarm
  red/yellow + 訂房率 >= 20%                       -> discount
  green + vac_pred > 60%                          -> alarm(升級)
  green + 訂房率 >= 50% 且 vac_pred <= 35%         -> healthy
  green + 其餘(訂房率<50% 或 35%<vac_pred<=60%)    -> hidden
"""
import numpy as np

from modules.quadrant import classify_row


# ── 無檔期 → unknown ──
def test_no_calendar_is_unknown():
    assert classify_row("green", None, 0.10) == "unknown"
    assert classify_row("green", np.nan, 0.10) == "unknown"


# ── 體質差(red/yellow),檔期主導,不受 vac_pred 升級影響 ──
def test_weak_empty_calendar_is_alarm():
    assert classify_row("red", 0.10, 0.90) == "alarm"
    assert classify_row("yellow", 0.19, 0.10) == "alarm"


def test_weak_nonempty_calendar_is_discount():
    assert classify_row("red", 0.20, 0.10) == "discount"
    assert classify_row("yellow", 0.80, 0.90) == "discount"


# ── green + vac_pred > 60% → 升級真警報(不論訂房率) ──
def test_green_high_vacpred_escalates_to_alarm():
    assert classify_row("green", 0.90, 0.61) == "alarm"   # 檔期滿也升級
    assert classify_row("green", 0.10, 0.70) == "alarm"
    # 邊界:剛好 0.60 不升級
    assert classify_row("green", 0.90, 0.60) != "alarm"


# ── green 完全達標 → healthy ──
def test_green_healthy_needs_both_conditions():
    assert classify_row("green", 0.50, 0.35) == "healthy"   # 邊界剛好達標
    assert classify_row("green", 0.80, 0.10) == "healthy"


# ── green 未完全達標 → hidden ──
def test_green_midband_booking_is_hidden():
    # 訂房率 33%(截圖情境),vac_pred 尚可,但檔期不滿
    assert classify_row("green", 0.33, 0.30) == "hidden"
    # 訂房率剛好差一點(49%)
    assert classify_row("green", 0.49, 0.20) == "hidden"


def test_green_full_booking_but_high_vacpred_is_hidden():
    # 檔期滿但 vac_pred 在 35~60% 之間 → 未達健康、未達升級 → hidden
    assert classify_row("green", 0.70, 0.36) == "hidden"
    assert classify_row("green", 0.70, 0.60) == "hidden"


def test_green_empty_booking_moderate_vacpred_is_hidden():
    # 訂房率 <20% 但 vac_pred 未超過 60% → hidden(不升 alarm)
    assert classify_row("green", 0.05, 0.50) == "hidden"


# ── vac_pred 為 NaN:保守處理(不升 alarm、不算 healthy) ──
def test_green_nan_vacpred_is_conservative_hidden():
    assert classify_row("green", 0.80, np.nan) == "hidden"
    assert classify_row("green", 0.10, np.nan) == "hidden"
