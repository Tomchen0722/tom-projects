"""複合訊號組合的合成資料測試。

驗證：
1. 單一 +1 訊號：複合排序與原訊號一致。
2. 反指標 -1：高原值 → 低複合分數。
3. 兩訊號組合：方向正確相加。
4. 邊界：空 specs 報錯、全空面板回空表。
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import signals as sg  # noqa: E402


def _wide(values: dict[str, list[float]], dates: list[str]) -> pd.DataFrame:
    """建寬面板：columns 為股票、index 為日期。"""
    return pd.DataFrame(values, index=pd.to_datetime(dates))


def test_single_positive_signal_preserves_order() -> None:
    """單一 +1 訊號：某日 A>B>C，複合分數也應 A>B>C。"""
    wide = _wide({"A": [30], "B": [20], "C": [10]}, ["2024-01-02"])
    out = sg.build_composite_signal([(wide, 1.0)])
    row = out.set_index("stock_id")["composite_signal"]
    assert row["A"] > row["B"] > row["C"]
    print("單一正向訊號排序測試通過")


def test_inverse_signal_flips_order() -> None:
    """反指標 -1：原值 A>B>C → 複合分數 A<B<C。"""
    wide = _wide({"A": [30], "B": [20], "C": [10]}, ["2024-01-02"])
    out = sg.build_composite_signal([(wide, -1.0)])
    row = out.set_index("stock_id")["composite_signal"]
    assert row["A"] < row["B"] < row["C"], "反指標應反轉排序"
    print("反指標翻轉測試通過")


def test_two_signals_combine() -> None:
    """兩訊號組合：外資(+1) A 最高、融資變化(-1) A 也最高（最差）→ 互相抵銷。"""
    foreign = _wide({"A": [30], "B": [20], "C": [10]}, ["2024-01-02"])   # A 外資最多(好)
    margin = _wide({"A": [30], "B": [20], "C": [10]}, ["2024-01-02"])    # A 融資增最多(差)
    out = sg.build_composite_signal([(foreign, 1.0), (margin, -1.0)])
    row = out.set_index("stock_id")["composite_signal"]
    # A：外資最高(+0.333)但融資也最高(-0.333) → 抵銷到 0；B、C 同理 → 三者接近相等
    assert abs(row["A"]) < 1e-9 and abs(row["B"]) < 1e-9 and abs(row["C"]) < 1e-9
    print("兩訊號抵銷測試通過")


def test_combine_favors_right_stock() -> None:
    """外資高且融資低的股票，複合分數應最高。"""
    foreign = _wide({"A": [30], "B": [20], "C": [10]}, ["2024-01-02"])  # A 外資最多
    margin = _wide({"A": [10], "B": [20], "C": [30]}, ["2024-01-02"])   # A 融資增最少(好)
    out = sg.build_composite_signal([(foreign, 1.0), (margin, -1.0)])
    row = out.set_index("stock_id")["composite_signal"]
    assert row["A"] > row["B"] > row["C"], "外資高+融資低的 A 應複合分數最高"
    print("複合擇優測試通過")


def test_edge_cases() -> None:
    """空 specs 報錯；全空面板回空表。"""
    try:
        sg.build_composite_signal([])
        raise AssertionError("空 specs 應報錯")
    except ValueError:
        pass
    out = sg.build_composite_signal([(pd.DataFrame(), 1.0)])
    assert out.empty and "composite_signal" in out.columns
    print("邊界測試通過")


if __name__ == "__main__":
    test_single_positive_signal_preserves_order()
    test_inverse_signal_flips_order()
    test_two_signals_combine()
    test_combine_favors_right_stock()
    test_edge_cases()
    print("\n複合訊號全部測試通過 ✔")
