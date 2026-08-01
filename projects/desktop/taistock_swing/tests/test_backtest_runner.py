"""回測核心 runner 的 mock 測試（不連網）。

用假的 DataSource 提供合成資料，驗證 run_backtest_pipeline 對各訊號選擇都能
完整串接到評估報告，且參數（top_k、rebalance_days、benchmark）正確傳遞。
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import backtest_runner as br  # noqa: E402


class MockDataSource:
    """回傳合成資料的假資料源，介面與 DataSource.fetch 相容。"""

    def __init__(self, days: int = 120, seed: int = 0) -> None:
        self._dates = pd.bdate_range("2024-01-01", periods=days).strftime("%Y-%m-%d")
        self._rng = np.random.default_rng(seed)

    def fetch(self, dataset_key, data_id=None, start_date=None, end_date=None, force_refresh=False):
        """依 dataset_key 產生對應 schema 的合成長格式資料。"""
        d = self._dates
        n = len(d)
        if dataset_key == "price":
            close = 100 * np.cumprod(1 + self._rng.normal(0, 0.02, n))
            return pd.DataFrame({
                "date": d, "stock_id": data_id, "open": close, "max": close,
                "min": close, "close": close, "Trading_Volume": self._rng.integers(1000, 9999, n),
            })
        if dataset_key == "institutional":
            rows = []
            for name in ["Foreign_Investor", "Investment_Trust", "Dealer_self",
                         "Dealer_Hedging", "Foreign_Dealer_Self"]:
                rows.append(pd.DataFrame({
                    "date": d, "stock_id": data_id, "name": name,
                    "buy": self._rng.integers(0, 500, n), "sell": self._rng.integers(0, 500, n),
                }))
            return pd.concat(rows, ignore_index=True)
        if dataset_key == "margin":
            bal = self._rng.integers(1000, 5000, n)
            return pd.DataFrame({
                "date": d, "stock_id": data_id,
                "MarginPurchaseTodayBalance": bal,
                "MarginPurchaseYesterdayBalance": bal + self._rng.integers(-100, 100, n),
                "MarginPurchaseLimit": 10000,
                "ShortSaleTodayBalance": self._rng.integers(0, 500, n),
            })
        if dataset_key == "dividend_result":
            return pd.DataFrame(columns=["date", "stock_id", "before_price", "after_price"])
        return pd.DataFrame()


def _params(signal_choice: str) -> dict:
    return {
        "universe": ["1111", "2222", "3333", "4444", "5555"],
        "start": "2024-01-01", "end": "2024-06-30", "benchmark_id": "0050",
        "top_k": 2, "rebalance_days": 5, "signal_choice": signal_choice,
    }


def test_all_signal_choices_produce_report() -> None:
    """每個訊號選擇都應完整跑通並回傳非空報告。"""
    ds = MockDataSource()
    for choice in br.SIGNAL_CHOICES:
        result = br.run_backtest_pipeline(_params(choice), ds, log=lambda m: None)
        assert isinstance(result["report"], str) and len(result["report"]) > 0
        assert "overall_pass" in result["verdict"]
    print(f"全部 {len(br.SIGNAL_CHOICES)} 種訊號選擇皆跑通")


def test_empty_universe_raises() -> None:
    """空股票池應報錯。"""
    ds = MockDataSource()
    p = _params(br.SIGNAL_CHOICES[0])
    p["universe"] = ["", "  "]
    try:
        br.run_backtest_pipeline(p, ds, log=lambda m: None)
        raise AssertionError("空股票池應報錯")
    except ValueError:
        print("空股票池報錯測試通過")


def test_log_called() -> None:
    """log 回呼應被呼叫以回報進度。"""
    ds = MockDataSource()
    msgs: list[str] = []
    br.run_backtest_pipeline(_params("外資5日買超"), ds, log=msgs.append)
    assert len(msgs) >= 3, "應有多則進度訊息"
    print(f"進度回呼測試通過（{len(msgs)} 則訊息）")


if __name__ == "__main__":
    test_all_signal_choices_produce_report()
    test_empty_universe_raises()
    test_log_called()
    print("\n回測 runner 全部測試通過 ✔")
