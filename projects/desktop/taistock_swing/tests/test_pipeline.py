"""面板組裝與 naive 策略的合成資料測試。

驗證：
1. build_price_panel：長轉寬正確。
2. long_to_returns：基準報酬 = 收盤 pct_change。
3. build_adjusted_price_panel：除息假跌被還原抵銷、無除息不調整。
4. build_weight_matrix：依訊號選前 K、等權、只做正訊號、再平衡間持有、無正訊號全現金。
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import data_panel as dp  # noqa: E402
import strategy_baseline as sb  # noqa: E402


def test_build_price_panel() -> None:
    """長格式轉寬面板：日期為 index、股票為欄。"""
    long = pd.DataFrame(
        [
            {"date": "2024-01-02", "stock_id": "2330", "close": 600},
            {"date": "2024-01-02", "stock_id": "2317", "close": 100},
            {"date": "2024-01-03", "stock_id": "2330", "close": 610},
        ]
    )
    panel = dp.build_price_panel(long)
    assert list(panel.columns) == ["2317", "2330"]
    assert panel.loc[pd.Timestamp("2024-01-03"), "2330"] == 610
    assert pd.isna(panel.loc[pd.Timestamp("2024-01-03"), "2317"]), "缺資料應為 NaN"
    print("build_price_panel 測試通過")


def test_long_to_returns() -> None:
    """基準報酬 = 收盤 pct_change，首日補 0。"""
    long = pd.DataFrame(
        [
            {"date": "2024-01-02", "close": 100},
            {"date": "2024-01-03", "close": 110},
            {"date": "2024-01-04", "close": 99},
        ]
    )
    ret = dp.long_to_returns(long)
    assert abs(ret.iloc[0] - 0.0) < 1e-9
    assert abs(ret.iloc[1] - 0.10) < 1e-9, "100→110 = +10%"
    assert abs(ret.iloc[2] - (-0.10)) < 1e-9, "110→99 = -10%"
    print("long_to_returns 測試通過")


def test_adjusted_price_removes_dividend_drop() -> None:
    """除息造成的假跌，經還原後應從報酬序列消失。"""
    price = pd.DataFrame(
        [
            {"date": "2024-06-01", "stock_id": "X", "close": 100.0},
            {"date": "2024-06-02", "stock_id": "X", "close": 100.0},
            {"date": "2024-06-03", "stock_id": "X", "close": 90.0},   # 除息日：假跌 10%
            {"date": "2024-06-04", "stock_id": "X", "close": 90.0},
        ]
    )
    dividend = pd.DataFrame(
        [{"date": "2024-06-03", "stock_id": "X", "before_price": 100.0, "after_price": 90.0}]
    )
    adj = dp.build_adjusted_price_panel(price, dividend)
    ret = adj["X"].pct_change(fill_method=None)
    assert abs(ret.loc[pd.Timestamp("2024-06-03")]) < 1e-9, "除息假跌應被還原抵銷"
    assert abs(adj["X"].iloc[-1] - 90.0) < 1e-9, "最新價應與未還原一致"
    assert abs(adj["X"].iloc[0] - 90.0) < 1e-9, "除息前歷史價應乘因子 0.9"
    print("還原股價（消除除息假跌）測試通過")


def test_adjusted_price_no_dividend_is_raw() -> None:
    """無除權息時，還原面板應等同未還原面板。"""
    price = pd.DataFrame(
        [
            {"date": "2024-06-01", "stock_id": "X", "close": 100.0},
            {"date": "2024-06-02", "stock_id": "X", "close": 105.0},
        ]
    )
    adj = dp.build_adjusted_price_panel(price, pd.DataFrame())
    assert adj["X"].tolist() == [100.0, 105.0], "無除息應不調整"
    print("無除息不調整測試通過")


def _feature_panel() -> pd.DataFrame:
    """合成特徵面板：5 檔股票、10 個交易日，投信 5 日累積買超各異。"""
    dates = pd.bdate_range("2024-01-01", periods=10)
    stocks = ["A", "B", "C", "D", "E"]
    rows = []
    # 給每檔一個固定的訊號值：A 最高、E 最低（含負）
    signal_map = {"A": 50, "B": 40, "C": 30, "D": 10, "E": -20}
    for d in dates:
        for s in stocks:
            rows.append({"date": d, "stock_id": s, "inst_net_5d": signal_map[s]})
    return pd.DataFrame(rows)


def test_weight_matrix_selects_top_k() -> None:
    """依訊號選前 K（此處 top_k=3）、等權、排除負訊號。"""
    fp = _feature_panel()
    dates = pd.DatetimeIndex(sorted(fp["date"].unique()))
    w = sb.build_weight_matrix(fp, dates, signal_col="inst_net_5d", top_k=3, rebalance_days=5)

    first = w.iloc[0]
    held = first[first > 0]
    assert set(held.index) == {"A", "B", "C"}, "應選訊號最高的前 3 檔"
    assert np.allclose(held.values, 1 / 3), "應等權"
    assert first.get("E", 0) == 0, "負訊號不應入選"
    print("選前 K / 等權 / 排除負訊號測試通過")


def test_weight_matrix_holds_between_rebalance() -> None:
    """再平衡日之間權重應維持不變（持有）。"""
    fp = _feature_panel()
    dates = pd.DatetimeIndex(sorted(fp["date"].unique()))
    w = sb.build_weight_matrix(fp, dates, top_k=3, rebalance_days=5)
    # 第 0 天與第 1~4 天（同一再平衡週期）權重應相同
    assert (w.iloc[0] == w.iloc[1]).all(), "再平衡間應持有不變"
    assert (w.iloc[0] == w.iloc[4]).all()
    print("再平衡間持有測試通過")


def test_weight_matrix_all_cash_when_no_positive() -> None:
    """全部訊號非正時應全現金（權重全 0）。"""
    dates = pd.bdate_range("2024-01-01", periods=6)
    rows = [{"date": d, "stock_id": s, "inst_net_5d": -1} for d in dates for s in ["A", "B"]]
    fp = pd.DataFrame(rows)
    w = sb.build_weight_matrix(fp, pd.DatetimeIndex(dates), top_k=3, rebalance_days=5)
    assert (w.sum(axis=1) == 0).all(), "無正訊號應全現金"
    print("無正訊號全現金測試通過")


def test_weight_matrix_edge() -> None:
    """空輸入回空表；缺欄位報錯。"""
    assert sb.build_weight_matrix(pd.DataFrame(), pd.DatetimeIndex([])).empty
    bad = pd.DataFrame([{"date": "2024-01-02", "stock_id": "A"}])
    try:
        sb.build_weight_matrix(bad, pd.DatetimeIndex([pd.Timestamp("2024-01-02")]))
        raise AssertionError("缺訊號欄應報錯")
    except ValueError:
        pass
    print("邊界測試通過")


if __name__ == "__main__":
    test_build_price_panel()
    test_long_to_returns()
    test_adjusted_price_removes_dividend_drop()
    test_adjusted_price_no_dividend_is_raw()
    test_weight_matrix_selects_top_k()
    test_weight_matrix_holds_between_rebalance()
    test_weight_matrix_all_cash_when_no_positive()
    test_weight_matrix_edge()
    print("\n面板 + 策略全部測試通過 ✔")
