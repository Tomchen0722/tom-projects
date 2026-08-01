# -*- coding: utf-8 -*-
"""quadrant 的「已發生入住」版分類測試（階段二，平台後台用）。

與 test_quadrant_classify.py 的差別：那支測的是房東入口用的 classify_row
（第二軸＝未來 90 天日曆已訂率）；本支測的是後台用的 classify_actual
（第二軸＝已發生的實際入住率），兩者刻意獨立、互不影響。
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules import quadrant as QD


# ══════════════════════════════════════════════════════════
# 五類分類規則
# ══════════════════════════════════════════════════════════
def test_無經營跡象優先於一切():
    """dormant 不論體質與入住率,一律歸自己那類 —— 平台行動不同,不可混入。"""
    assert QD.classify_actual("red", 0.0, is_dormant=1) == "dormant"
    assert QD.classify_actual("green", 0.9, is_dormant=1) == "dormant"


def test_體質差且入住率低於20_為高風險警訊():
    assert QD.classify_actual("red", 0.19, 0) == "alarm"
    assert QD.classify_actual("yellow", 0.0, 0) == "alarm"


def test_體質差但入住率達20_為靠降價撐住():
    assert QD.classify_actual("red", 0.20, 0) == "discount"      # 門檻含下界
    assert QD.classify_actual("yellow", 0.85, 0) == "discount"


def test_體質佳且入住率達50_為健康():
    assert QD.classify_actual("green", 0.50, 0) == "healthy"     # 門檻含下界
    assert QD.classify_actual("green", 0.99, 0) == "healthy"


def test_體質佳但入住率不足50_為隱形危機():
    """本類是階段二的核心:模型說安全,實際卻在流血。"""
    assert QD.classify_actual("green", 0.49, 0) == "hidden"
    assert QD.classify_actual("green", 0.0, 0) == "hidden"


def test_入住率缺值歸資料不足():
    assert QD.classify_actual("green", np.nan, 0) == "unknown"
    assert QD.classify_actual("red", None, 0) == "unknown"


def test_門檻常數與房東入口共用():
    """後台沿用同一組門檻,避免兩邊各自漂移。"""
    assert QD.BOOKED_EMPTY == 0.20
    assert QD.BOOKED_FULL == 0.50


# ══════════════════════════════════════════════════════════
# 文案與色票
# ══════════════════════════════════════════════════════════
def test_五類都有文案與建議行動():
    for key in ("alarm", "hidden", "discount", "healthy", "dormant"):
        spec = QD.ACTUAL_QUADRANTS[key]
        assert spec["label"] and spec["desc"] and spec["action"]
        assert spec["color"] in ("high", "medium", "accent", "low", "muted")


def test_已發生版文案不得沿用未來語意():
    """原 QUADRANTS 寫「未來也幾乎沒人訂」,回顧視角不適用。"""
    for spec in QD.ACTUAL_QUADRANTS.values():
        assert "未來" not in spec["desc"]


def test_不影響房東入口既有分類():
    """classify_row 是房東入口在用的,階段二不得改動其行為。"""
    assert QD.classify_row("red", 0.10, 0.5) == "alarm"
    assert QD.classify_row("green", 0.60, 0.30) == "healthy"


# ══════════════════════════════════════════════════════════
# DataFrame 標註與彙總
# ══════════════════════════════════════════════════════════
@pytest.fixture
def sample():
    return pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "host_id": [10, 20, 30, 40, 10],   # id 1,5 同一房東(10),測房東數去重
        "tier": ["red", "green", "green", "yellow", "red"],
        "real_vac": [0.95, 0.30, 0.80, 0.50, 1.0],
        "is_dormant": [0, 0, 0, 0, 1],
    })


def test_annotate_actual_加上象限欄(sample):
    d = QD.annotate_actual(sample)
    # 1: red + 入住5%  → alarm
    # 2: green + 入住70% → healthy
    # 3: green + 入住20% → hidden
    # 4: yellow + 入住50% → discount
    # 5: dormant → dormant
    assert list(d["quadrant"]) == ["alarm", "healthy", "hidden",
                                   "discount", "dormant"]
    assert d["quadrant_label"].iloc[2] == QD.ACTUAL_QUADRANTS["hidden"]["label"]


def test_annotate_actual_不改動輸入(sample):
    QD.annotate_actual(sample)
    assert "quadrant" not in sample.columns


def test_annotate_actual_缺欄位時保守處理():
    d = QD.annotate_actual(pd.DataFrame({"id": [1], "tier": ["green"]}))
    assert d["quadrant"].iloc[0] == "unknown"


def test_summary_actual_依優先序排列(sample):
    s = QD.summary_actual(QD.annotate_actual(sample))
    assert list(s.columns) == ["象限", "房源數", "房東數", "說明", "建議行動"]
    # alarm(1) 排在 dormant(5) 之前
    assert s.iloc[0]["象限"] == QD.ACTUAL_QUADRANTS["alarm"]["label"]
    assert s.iloc[-1]["象限"] == QD.ACTUAL_QUADRANTS["dormant"]["label"]
    assert int(s["房源數"].sum()) == 5


def test_summary_actual_房東數依象限去重(sample):
    s = QD.summary_actual(QD.annotate_actual(sample)).set_index("象限")
    alarm = QD.ACTUAL_QUADRANTS["alarm"]["label"]
    dormant = QD.ACTUAL_QUADRANTS["dormant"]["label"]
    healthy = QD.ACTUAL_QUADRANTS["healthy"]["label"]
    # id 1(alarm)與 id 5(dormant)同屬 host 10 → 各自那格仍各算 1 位,不互相扣抵
    assert s.loc[alarm, "房東數"] == 1
    assert s.loc[dormant, "房東數"] == 1
    assert s.loc[healthy, "房東數"] == 1
