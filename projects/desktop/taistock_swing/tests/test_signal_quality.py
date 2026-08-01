"""訊號品質分析的合成資料測試。

用「已知答案」的合成訊號驗證：
1. 完美預測訊號 → IC ≈ +1、分位數單調上升、多空價差 > 0。
2. 完全反向訊號 → IC ≈ -1。
3. 隨機訊號 → IC ≈ 0。
4. 未來報酬的 point-in-time 位移正確。
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import signal_quality as sq  # noqa: E402


def _price_panel(n_days: int = 60, n_stocks: int = 20, seed: int = 0) -> pd.DataFrame:
    """合成還原股價面板。"""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-01-01", periods=n_days)
    cols = [f"S{i:02d}" for i in range(n_stocks)]
    data = {c: 100 * np.cumprod(1 + rng.normal(0, 0.015, n_days)) for c in cols}
    return pd.DataFrame(data, index=dates)


def test_forward_returns_point_in_time() -> None:
    """未來報酬應為 T+exec_lag 進場、持有 horizon 日；末端不足處為 NaN。"""
    prices = _price_panel(n_days=10, n_stocks=1)
    col = prices.columns[0]
    fwd = sq.compute_forward_returns(prices, horizon=2, exec_lag=1)
    # T=0：進場價=price[1]，出場價=price[3]
    expected = prices[col].iloc[3] / prices[col].iloc[1] - 1
    assert abs(fwd[col].iloc[0] - expected) < 1e-9
    # 末端不足 horizon 應為 NaN
    assert fwd[col].iloc[-1] != fwd[col].iloc[-1]  # NaN
    print("未來報酬 point-in-time 測試通過")


def test_perfect_signal_high_ic() -> None:
    """訊號 = 未來報酬本身（完美預測）→ IC ≈ +1、分位數單調、多空 > 0。"""
    prices = _price_panel(seed=1)
    fwd = sq.compute_forward_returns(prices, horizon=5, exec_lag=1)
    signal = fwd.copy()  # 完美訊號：直接用未來報酬當訊號

    ic_series, summary = sq.compute_ic(signal, fwd, min_names=5)
    assert summary["mean_ic"] > 0.99, f"完美訊號 IC 應接近 1，實際 {summary['mean_ic']}"
    assert summary["hit_rate"] > 0.99

    q = sq.quantile_analysis(signal, fwd, n_quantiles=3)
    assert q.loc["top_minus_bottom", "mean_forward_return"] > 0, "高訊號組報酬應高於低訊號組"
    # 單調：第2組 >= 第0組
    assert q.loc[2, "mean_forward_return"] > q.loc[0, "mean_forward_return"]
    print(f"完美訊號測試通過（IC={summary['mean_ic']:.3f}）")


def test_inverse_signal_negative_ic() -> None:
    """訊號 = 未來報酬的相反數 → IC ≈ -1。"""
    prices = _price_panel(seed=2)
    fwd = sq.compute_forward_returns(prices, horizon=5, exec_lag=1)
    signal = -fwd
    _, summary = sq.compute_ic(signal, fwd, min_names=5)
    assert summary["mean_ic"] < -0.99, f"反向訊號 IC 應接近 -1，實際 {summary['mean_ic']}"
    print(f"反向訊號測試通過（IC={summary['mean_ic']:.3f}）")


def test_random_signal_zero_ic() -> None:
    """與未來報酬無關的隨機訊號 → IC ≈ 0。"""
    prices = _price_panel(seed=3, n_days=250)
    fwd = sq.compute_forward_returns(prices, horizon=5, exec_lag=1)
    rng = np.random.default_rng(99)
    signal = pd.DataFrame(
        rng.normal(size=fwd.shape), index=fwd.index, columns=fwd.columns
    )
    _, summary = sq.compute_ic(signal, fwd, min_names=5)
    assert abs(summary["mean_ic"]) < 0.1, f"隨機訊號 IC 應接近 0，實際 {summary['mean_ic']}"
    print(f"隨機訊號測試通過（IC={summary['mean_ic']:.3f}）")


def test_edge_cases() -> None:
    """空面板報錯；無共同欄位報錯。"""
    try:
        sq.compute_forward_returns(pd.DataFrame(), horizon=5)
        raise AssertionError("空面板應報錯")
    except ValueError:
        pass

    prices = _price_panel(n_days=20, n_stocks=5)
    fwd = sq.compute_forward_returns(prices, horizon=3)
    other = fwd.rename(columns={c: c + "X" for c in fwd.columns})
    try:
        sq.compute_ic(fwd, other, min_names=2)
        raise AssertionError("無共同欄位應報錯")
    except ValueError:
        pass
    print("邊界條件測試通過")


if __name__ == "__main__":
    test_forward_returns_point_in_time()
    test_perfect_signal_high_ic()
    test_inverse_signal_negative_ic()
    test_random_signal_zero_ic()
    test_edge_cases()
    print("\n訊號品質分析全部測試通過 ✔")
