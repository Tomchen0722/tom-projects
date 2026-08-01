"""資料層的 mock 測試（不連網）。

用假的 request_fn / sleep_fn / now_fn 驗證四件套邏輯：
快取、重試、速率限制、供應商備援，外加 schema 驗證與付費跳過。
"""
from __future__ import annotations

import sys
import tempfile
import warnings
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import config  # noqa: E402
import data_source as ds  # noqa: E402

_INST_SPEC = config.DATASETS["institutional"]


def _valid_rows() -> list[dict]:
    """一組符合三大法人 schema 的假資料。"""
    return [
        {"date": "2024-01-02", "stock_id": "2330", "name": "Foreign_Investor", "buy": 100, "sell": 40},
        {"date": "2024-01-02", "stock_id": "2330", "name": "Investment_Trust", "buy": 20, "sell": 5},
    ]


def test_retry_then_success() -> None:
    """前兩次暫時性錯誤、第三次成功，應回傳資料且退避睡眠被呼叫兩次。"""
    calls = {"n": 0}

    def flaky_request(url: str, params: dict, token: str) -> tuple[int, dict]:
        calls["n"] += 1
        if calls["n"] < 3:
            return 500, {}
        return 200, {"data": _valid_rows()}

    slept: list[float] = []
    provider = ds.FinMindProvider(
        token="fake",
        request_fn=flaky_request,
        rate_limiter=ds.RateLimiter(sleep_fn=lambda s: None),
        sleep_fn=lambda s: slept.append(s),
    )
    df = provider.fetch(_INST_SPEC, "2330", "2024-01-01", "2024-01-31")
    assert len(df) == 2 and calls["n"] == 3
    assert len(slept) == 2, "應在兩次失敗後各退避一次"
    print(f"重試測試通過：呼叫 {calls['n']} 次，退避 {len(slept)} 次")


def test_quota_402_raises() -> None:
    """收到 402 應拋出 QuotaExceededError 且不重試。"""
    def paywalled(url: str, params: dict, token: str) -> tuple[int, dict]:
        return 402, {"msg": "payment required"}

    provider = ds.FinMindProvider(
        token="fake",
        request_fn=paywalled,
        rate_limiter=ds.RateLimiter(sleep_fn=lambda s: None),
        sleep_fn=lambda s: None,
    )
    try:
        provider.fetch(_INST_SPEC, "2330", "2024-01-01", None)
        raise AssertionError("402 應拋出 QuotaExceededError")
    except ds.QuotaExceededError:
        print("402 付費錯誤測試通過")


def test_rate_limiter_blocks() -> None:
    """達到每小時預算後，下一次 acquire 應等待。"""
    slept: list[float] = []
    limiter = ds.RateLimiter(hourly_budget=3, sleep_fn=lambda s: slept.append(s))
    clock = {"t": 0.0}

    def now() -> float:
        return clock["t"]

    for _ in range(3):
        limiter.acquire(now_fn=now)  # 用滿預算（同一時刻）
    limiter.acquire(now_fn=now)  # 第 4 次應觸發等待
    assert len(slept) == 1 and slept[0] > 0, "超出預算應等待到視窗釋出"
    print(f"速率限制測試通過：等待 {slept[0]:.0f} 秒")


def test_cache_hit_skips_provider() -> None:
    """第一次抓取寫快取，第二次應直接讀快取、不再呼叫供應商。"""
    class CountingProvider:
        name = "finmind"

        def __init__(self) -> None:
            self.calls = 0

        def fetch(self, spec, data_id, start_date, end_date):
            self.calls += 1
            return pd.DataFrame(_valid_rows())

    with tempfile.TemporaryDirectory() as tmp:
        provider = CountingProvider()
        source = ds.DataSource(token="fake", cache_dir=Path(tmp), primary=provider)  # type: ignore[arg-type]
        first = source.fetch("institutional", "2330", "2024-01-01", "2024-01-31")
        second = source.fetch("institutional", "2330", "2024-01-01", "2024-01-31")
        assert provider.calls == 1, "第二次應命中快取，不再呼叫供應商"
        assert len(first) == len(second) == 2
        assert source.provider_log[-1]["provider"] == "cache"
        print("快取測試通過：供應商僅被呼叫一次")


def test_fallback_chain() -> None:
    """主供應商失敗時應降級到備援，並記錄實際供應商。"""
    class FailingPrimary:
        name = "finmind"

        def fetch(self, spec, data_id, start_date, end_date):
            raise RuntimeError("主供應商掛了")

    class WorkingFallback:
        name = "twse"

        def fetch(self, spec, data_id, start_date, end_date):
            return pd.DataFrame(_valid_rows())

    with tempfile.TemporaryDirectory() as tmp:
        source = ds.DataSource(
            token="fake",
            cache_dir=Path(tmp),
            primary=FailingPrimary(),  # type: ignore[arg-type]
            fallbacks=[WorkingFallback()],
        )
        df = source.fetch("institutional", "2330", "2024-01-01", None)
        assert len(df) == 2
        assert source.provider_log[-1]["provider"] == "twse"
        print("備援鏈測試通過：主供應商失敗後成功降級到 twse")


def test_schema_validation_raises() -> None:
    """回傳缺少必要欄位時應報錯，而非默默繼續。"""
    bad = pd.DataFrame([{"date": "2024-01-02", "stock_id": "2330"}])  # 缺 name/buy/sell
    try:
        ds.validate_schema(bad, _INST_SPEC)
        raise AssertionError("缺欄位應拋出 ValueError")
    except ValueError:
        print("schema 驗證測試通過")


def test_paid_dataset_skipped() -> None:
    """付費資料集在免費帳號應回傳空表並發出警告。"""
    with tempfile.TemporaryDirectory() as tmp:
        source = ds.DataSource(token="fake", cache_dir=Path(tmp), primary=_DummyProvider())
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            df = source.fetch("broker_report", "2330", "2024-01-01", None)
        assert df.empty
        assert source.provider_log[-1]["provider"] == "skipped_paid"
        assert any("付費" in str(w.message) for w in caught)
        print("付費跳過測試通過")


class _DummyProvider:
    """佔位供應商，付費跳過測試不會真的用到它。"""

    name = "finmind"

    def fetch(self, spec, data_id, start_date, end_date):
        return pd.DataFrame(_valid_rows())


if __name__ == "__main__":
    test_retry_then_success()
    test_quota_402_raises()
    test_rate_limiter_blocks()
    test_cache_hit_skips_provider()
    test_fallback_chain()
    test_schema_validation_raises()
    test_paid_dataset_skipped()
    print("\n資料層全部測試通過 ✔")
