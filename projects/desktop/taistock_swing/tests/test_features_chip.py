"""P1 投信買超動能 + 融資融券特徵的合成資料測試。

驗證：
1. 單日淨買超 = 買 − 賣。
2. N 日累積正確、且不跨股票。
3. 連續買超天數在遇到賣超時歸零。
4. 成交量正規化正確、除零安全。
5. available_date == date（point-in-time）。
6. 融資融券：增減、券資比、使用率、資券背離。
7. 邊界：空輸入、缺欄位、缺類別。
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402
import features_chip as fc  # noqa: E402

_INV = config.INSTITUTION_NAMES["investment_trust"]


def _make_inst(rows: list[tuple[str, str, str, float, float]]) -> pd.DataFrame:
    """由 (date, stock_id, name, buy, sell) 元組建三大法人長格式資料。"""
    return pd.DataFrame(rows, columns=["date", "stock_id", "name", "buy", "sell"])


def test_daily_net_and_rolling() -> None:
    """單日淨買超與 5 日累積正確，且不跨股票。"""
    rows = []
    # 2330：投信連 3 天各淨買 +10、+20、+30
    for d, (b, s) in zip(
        ["2024-01-02", "2024-01-03", "2024-01-04"],
        [(10, 0), (20, 0), (30, 0)],
    ):
        rows.append((d, "2330", _INV, b, s))
    # 2317：投信單日淨買 +5（確認不會被 2330 汙染）
    rows.append(("2024-01-02", "2317", _INV, 5, 0))

    feat = fc.build_institutional_features(_make_inst(rows), window=5)
    f2330 = feat[feat["stock_id"] == "2330"].sort_values("date")
    assert list(f2330["inst_net"]) == [10, 20, 30]
    assert list(f2330["inst_net_5d"]) == [10, 30, 60], "5 日累積應逐日累加"
    f2317 = feat[feat["stock_id"] == "2317"]
    assert f2317["inst_net_5d"].iloc[0] == 5, "不同股票不應互相累加"
    print("單日/累積測試通過")


def test_buy_streak_resets() -> None:
    """連續買超天數在賣超日歸零、之後重新起算。"""
    rows = [
        ("2024-01-02", "2330", _INV, 10, 0),   # 買超 → streak 1
        ("2024-01-03", "2330", _INV, 20, 0),   # 買超 → streak 2
        ("2024-01-04", "2330", _INV, 0, 15),   # 賣超 → streak 0
        ("2024-01-05", "2330", _INV, 5, 0),    # 買超 → streak 1
    ]
    feat = fc.build_institutional_features(_make_inst(rows), window=5).sort_values("date")
    assert list(feat["inst_buy_streak"]) == [1, 2, 0, 1], "賣超日應歸零並重新起算"
    print("連續買超天數測試通過")


def test_volume_normalization() -> None:
    """成交量正規化正確，且成交量為 0 時不炸。"""
    rows = [
        ("2024-01-02", "2330", _INV, 100, 0),
        ("2024-01-03", "2330", _INV, 50, 0),
    ]
    price = pd.DataFrame(
        [
            {"date": "2024-01-02", "stock_id": "2330", "Trading_Volume": 1000},
            {"date": "2024-01-03", "stock_id": "2330", "Trading_Volume": 0},  # 除零測試
        ]
    )
    feat = fc.build_institutional_features(_make_inst(rows), price_df=price, window=5).sort_values("date")
    assert abs(feat["inst_net_vol_pct"].iloc[0] - 0.1) < 1e-9, "100/1000 應為 0.1"
    assert feat["inst_net_vol_pct"].iloc[1] == 0.0, "成交量為 0 應安全回 0"
    print("成交量正規化測試通過")


def test_point_in_time_available_date() -> None:
    """available_date 應等於 date（每日盤後資料無 lag）。"""
    rows = [("2024-01-02", "2330", _INV, 10, 0)]
    feat = fc.build_institutional_features(_make_inst(rows), window=5)
    assert (feat["available_date"] == feat["date"]).all()
    print("point-in-time 測試通過")


def test_edge_cases() -> None:
    """空輸入回空表；缺欄位報錯；缺類別不炸（外資缺 → 0）。"""
    empty = fc.build_institutional_features(pd.DataFrame(), window=5)
    assert empty.empty and "inst_net" in empty.columns

    bad = pd.DataFrame([{"date": "2024-01-02", "stock_id": "2330"}])  # 缺 name/buy/sell
    try:
        fc.build_institutional_features(bad, window=5)
        raise AssertionError("缺欄位應報錯")
    except ValueError:
        pass

    # 只有投信、沒有外資資料 → 外資特徵應為 0 而非崩潰
    only_inv = _make_inst([("2024-01-02", "2330", _INV, 10, 0)])
    feat = fc.build_institutional_features(only_inv, window=5)
    assert feat["foreign_net_5d"].iloc[0] == 0.0
    print("邊界條件測試通過")


def _make_margin(rows: list[dict]) -> pd.DataFrame:
    """由 dict 列建融資融券資料（使用實際欄名）。"""
    return pd.DataFrame(rows)


def test_margin_features_basic() -> None:
    """融資增減、券資比、融資使用率計算正確。"""
    b = config.MARGIN_COLS
    rows = [
        {
            "date": "2024-01-02", "stock_id": "2330",
            b["margin_balance"]: 1000, b["margin_balance_prev"]: 900,
            b["margin_limit"]: 5000, b["short_balance"]: 200,
        },
        {
            "date": "2024-01-03", "stock_id": "2330",
            b["margin_balance"]: 1100, b["margin_balance_prev"]: 1000,
            b["margin_limit"]: 5000, b["short_balance"]: 220,
        },
    ]
    feat = fc.build_margin_features(_make_margin(rows), window=5).sort_values("date")
    assert list(feat["margin_chg"]) == [100, 100], "融資單日增減 = 今日 − 昨日"
    assert abs(feat["short_margin_ratio"].iloc[0] - 0.2) < 1e-9, "券資比 200/1000=0.2"
    assert abs(feat["margin_util"].iloc[0] - 0.2) < 1e-9, "融資使用率 1000/5000=0.2"
    print("融資融券基本特徵測試通過")


def test_margin_divergence() -> None:
    """近 N 日價漲但融資減 → 資券背離旗標為 1。"""
    b = config.MARGIN_COLS
    # 融資餘額逐日下降（融資減），價格逐日上升（價漲）
    rows = []
    prices = []
    balances = [1000, 950, 900, 850, 700, 650]
    closes = [100, 101, 102, 103, 104, 108]
    dates = [f"2024-01-{d:02d}" for d in range(2, 8)]
    for i, d in enumerate(dates):
        prev = balances[i - 1] if i > 0 else balances[i]
        rows.append({
            "date": d, "stock_id": "2330",
            b["margin_balance"]: balances[i], b["margin_balance_prev"]: prev,
            b["margin_limit"]: 5000, b["short_balance"]: 100,
        })
        prices.append({"date": d, "stock_id": "2330", "close": closes[i]})
    feat = fc.build_margin_features(_make_margin(rows), price_df=pd.DataFrame(prices), window=5).sort_values("date")
    # 最後一天:近5日價漲(100→108)、融資減(1000→650)→ 背離=1
    assert feat["margin_price_divergence"].iloc[-1] == 1, "價漲融資減應標記背離"
    print("資券背離測試通過")


def test_margin_edge() -> None:
    """空輸入回空表；缺欄位報錯。"""
    empty = fc.build_margin_features(pd.DataFrame(), window=5)
    assert empty.empty and "short_margin_ratio" in empty.columns
    bad = pd.DataFrame([{"date": "2024-01-02", "stock_id": "2330"}])
    try:
        fc.build_margin_features(bad, window=5)
        raise AssertionError("缺欄位應報錯")
    except ValueError:
        pass
    print("融資融券邊界測試通過")


if __name__ == "__main__":
    test_daily_net_and_rolling()
    test_buy_streak_resets()
    test_volume_normalization()
    test_point_in_time_available_date()
    test_edge_cases()
    test_margin_features_basic()
    test_margin_divergence()
    test_margin_edge()
    print("\nP1 投信 + 融資融券特徵全部測試通過 ✔")
