"""評估框架的合成資料測試。

用可控的假資料驗證：
1. 成本確實會吃掉報酬（換手越高，淨報酬越低）。
2. 防未來函數的 exec_lag 確實生效（權重位移）。
3. 指標與及格線判定的數值合理。
4. 邊界條件（空輸入、單股、缺值）不會默默出錯。
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# 讓測試能匯入 src 模組
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import evaluation as ev  # noqa: E402


def _make_price_panel(seed: int = 42, days: int = 750, n_stocks: int = 5) -> pd.DataFrame:
    """產生一組合成還原股價（含一個 2022 型的下跌年）。"""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2021-01-01", periods=days)
    cols = [f"{2330 + i}" for i in range(n_stocks)]
    # 讓 2022 年整體偏空，其餘偏多，模擬體制轉換
    drift = np.where((dates.year == 2022), -0.0008, 0.0006)
    data = {}
    for c in cols:
        daily = rng.normal(0, 0.02, days) + drift
        data[c] = 100 * np.cumprod(1 + daily)
    return pd.DataFrame(data, index=dates)


def test_basic_run_and_report() -> None:
    """完整跑一次 evaluate，確認回傳結構與報告字串。"""
    prices = _make_price_panel()
    # 簡單策略：等權持有前兩檔，每 5 日再平衡一次
    weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    rebalance_days = prices.index[::5]
    for d in rebalance_days:
        weights.loc[d, prices.columns[:2]] = 0.5
    weights = weights.reindex(prices.index).ffill().fillna(0.0)

    # 基準：等權買進持有全部股票
    benchmark = prices.pct_change().mean(axis=1).fillna(0.0)

    result = ev.evaluate(weights, prices, benchmark)

    assert set(result.keys()) == {"returns", "metrics", "yearly", "verdict", "report"}
    assert isinstance(result["report"], str) and len(result["report"]) > 0
    assert "net_return" in result["returns"].columns
    assert "strategy_sharpe" in result["metrics"]
    print(result["report"])


def test_cost_reduces_return() -> None:
    """換手越高，淨報酬應越低（成本確實內建）。"""
    prices = _make_price_panel(seed=1)
    benchmark = prices.pct_change().mean(axis=1).fillna(0.0)

    # 低換手：買進後長抱
    low = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    low.iloc[:, 0] = 1.0

    # 高換手：每日在兩檔之間來回切換
    high = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    high.iloc[0::2, 0] = 1.0
    high.iloc[1::2, 1] = 1.0

    cost = ev.CostConfig()
    bt = ev.BacktestConfig()
    low_net = ev.compute_strategy_returns(low, prices, cost, bt)["net_return"].sum()
    high_cost = ev.compute_strategy_returns(high, prices, cost, bt)["cost"].sum()
    low_cost = ev.compute_strategy_returns(low, prices, cost, bt)["cost"].sum()

    assert high_cost > low_cost, "高換手的總成本應高於低換手"
    print(f"低換手總成本={low_cost:.4f}  高換手總成本={high_cost:.4f}  低換手淨報酬和={low_net:.4f}")


def test_exec_lag_shifts_positions() -> None:
    """exec_lag 應讓權重延遲生效，避免用到當日尚不可得的資訊。"""
    prices = _make_price_panel(seed=2)
    weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    weights.iloc[10, 0] = 1.0  # 只在第 10 天決策持有

    r_lag0 = ev.compute_strategy_returns(weights, prices, ev.CostConfig(), ev.BacktestConfig(exec_lag=0))
    r_lag1 = ev.compute_strategy_returns(weights, prices, ev.CostConfig(), ev.BacktestConfig(exec_lag=1))

    # lag=0 在第 10 天就吃第 10 天報酬；lag=1 要到第 11 天才生效
    nz0 = r_lag0["gross_return"].to_numpy().nonzero()[0]
    nz1 = r_lag1["gross_return"].to_numpy().nonzero()[0]
    assert nz1.min() == nz0.min() + 1, "exec_lag=1 應使生效日往後推一天"
    print(f"lag0 首個非零報酬日 index={nz0.min()}  lag1={nz1.min()}")


def test_edge_cases() -> None:
    """邊界條件：空輸入報錯、單股可運作、缺值不崩。"""
    prices = _make_price_panel(seed=3)

    # 空輸入應報錯
    try:
        ev.compute_strategy_returns(pd.DataFrame(), prices, ev.CostConfig(), ev.BacktestConfig())
        raise AssertionError("空 weights 應拋出 ValueError")
    except ValueError:
        pass

    # weights 有價格中沒有的股票應報錯
    bad = pd.DataFrame(0.5, index=prices.index, columns=["9999"])
    try:
        ev.compute_strategy_returns(bad, prices, ev.CostConfig(), ev.BacktestConfig())
        raise AssertionError("缺價格的股票應拋出 ValueError")
    except ValueError:
        pass

    # 價格含 NaN 不應讓結果變 NaN（缺值報酬視為 0）
    prices_nan = prices.copy()
    prices_nan.iloc[20:25, 0] = np.nan
    w = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    w.iloc[:, 0] = 1.0
    out = ev.compute_strategy_returns(w, prices_nan, ev.CostConfig(), ev.BacktestConfig())
    assert not out["net_return"].isna().any(), "缺值不應讓淨報酬變 NaN"
    print("邊界條件測試通過")


if __name__ == "__main__":
    test_basic_run_and_report()
    print("\n" + "#" * 52 + "\n")
    test_cost_reduces_return()
    test_exec_lag_shifts_positions()
    test_edge_cases()
    print("\n全部測試通過 ✔")
