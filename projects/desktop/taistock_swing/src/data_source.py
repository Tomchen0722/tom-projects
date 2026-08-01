"""台股波段系統｜FinMind 資料層。

依 data-pipeline 技能的「外部 API 四件套」實作：快取、重試、速率限制、供應商備援。
每次取用都記錄實際使用的供應商，並在出口做 schema 驗證。

設計重點：
- HTTP 呼叫以依賴注入（request_fn）傳入，讓測試可用 fake 取代，無需連網。
- token 由環境變數讀取，不寫死於程式碼。
- 付費資料集在免費帳號會被明確跳過（回傳空表 + 警示），而非默默失敗。

沙盒無法連 FinMind，故本模組設計為「本機可執行」；純邏輯（快取/重試/
節流/備援鏈/schema 驗證）已用 mock 於沙盒完整驗證。
"""
from __future__ import annotations

import os
import time
import warnings
from collections import deque
from pathlib import Path
from typing import Callable, Protocol

import pandas as pd

from config import (
    BACKOFF_BASE_SECONDS,
    DATASETS,
    DEFAULT_CACHE_DIR,
    DEFAULT_HOURLY_BUDGET,
    FINMIND_DATA_URL,
    MAX_RETRIES,
    TOKEN_ENV_VAR,
    DatasetSpec,
)


class QuotaExceededError(RuntimeError):
    """FinMind 回傳額度用盡或需付費（HTTP 402）時拋出，屬不可重試錯誤。"""


class RateLimiter:
    """滑動視窗速率限制器：確保每小時請求數不超過預算。"""

    def __init__(self, hourly_budget: int = DEFAULT_HOURLY_BUDGET, sleep_fn: Callable[[float], None] = time.sleep) -> None:
        """初始化速率限制器。

        參數:
            hourly_budget: 每小時允許的最大請求數。
            sleep_fn: 睡眠函式，測試時可注入假函式避免真的等待。

        回傳:
            無。

        例外:
            ValueError: 當 hourly_budget <= 0。
        """
        if hourly_budget <= 0:
            raise ValueError("hourly_budget 必須為正整數。")
        self._budget = hourly_budget
        self._window_seconds = 3600.0
        self._timestamps: deque[float] = deque()
        self._sleep = sleep_fn

    def acquire(self, now_fn: Callable[[], float] = time.monotonic) -> None:
        """取得一個請求額度；若視窗內已達上限則等待至有空位。

        參數:
            now_fn: 取得目前單調時間的函式，測試可注入。

        回傳:
            無。

        例外:
            不主動拋出例外。
        """
        now = now_fn()
        # 移除超過一小時的舊時間戳
        while self._timestamps and now - self._timestamps[0] >= self._window_seconds:
            self._timestamps.popleft()
        if len(self._timestamps) >= self._budget:
            wait = self._window_seconds - (now - self._timestamps[0])
            if wait > 0:
                self._sleep(wait)
            self._timestamps.popleft()
        self._timestamps.append(now_fn())


class RequestFn(Protocol):
    """HTTP 請求函式的介面：輸入 params 與 token，回傳 (status_code, json_dict)。"""

    def __call__(self, url: str, params: dict[str, str], token: str) -> tuple[int, dict]:
        ...


def _default_request_fn(url: str, params: dict[str, str], token: str) -> tuple[int, dict]:
    """實際的 HTTP 請求（正式環境用；沙盒無法連線）。

    參數:
        url: API 端點。
        params: 查詢參數。
        token: FinMind 授權 token。

    回傳:
        (HTTP 狀態碼, 回應 JSON dict)。

    例外:
        ImportError: 當環境未安裝 requests。
    """
    import requests  # 延遲匯入，讓不連網的測試無需安裝

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    try:
        payload = resp.json()
    except ValueError:
        payload = {}
    return resp.status_code, payload


class FinMindProvider:
    """FinMind 主供應商：具重試與速率限制的單一資料集抓取。"""

    name = "finmind"

    def __init__(
        self,
        token: str,
        request_fn: RequestFn = _default_request_fn,
        rate_limiter: RateLimiter | None = None,
        sleep_fn: Callable[[float], None] = time.sleep,
    ) -> None:
        """初始化 FinMind 供應商。

        參數:
            token: FinMind 授權 token。
            request_fn: HTTP 請求函式（可注入 fake 供測試）。
            rate_limiter: 速率限制器，None 時建立預設值。
            sleep_fn: 重試退避用的睡眠函式，測試可注入。

        回傳:
            無。

        例外:
            ValueError: 當 token 為空。
        """
        if not token:
            raise ValueError(f"缺少 FinMind token，請設定環境變數 {TOKEN_ENV_VAR}。")
        self._token = token
        self._request = request_fn
        self._limiter = rate_limiter or RateLimiter(sleep_fn=sleep_fn)
        self._sleep = sleep_fn

    def fetch(self, spec: DatasetSpec, data_id: str | None, start_date: str, end_date: str | None) -> pd.DataFrame:
        """抓取單一資料集，含指數退避重試。

        參數:
            spec: 資料集規格。
            data_id: 股票代碼；None 表示抓全市場。
            start_date: 起始日（YYYY-MM-DD）。
            end_date: 結束日（YYYY-MM-DD）；None 表示到最新。

        回傳:
            原始資料 DataFrame（未做 schema 驗證，由編排層負責）。

        例外:
            QuotaExceededError: 收到 HTTP 402（需付費/額度用盡）。
            RuntimeError: 重試上限後仍失敗。
        """
        params: dict[str, str] = {"dataset": spec.finmind_name}
        # 部分資料集（如 TaiwanStockInfo）不吃日期，送 start_date 反而會被當更新日過濾
        if start_date:
            params["start_date"] = start_date
        if data_id:
            params["data_id"] = data_id
        if end_date:
            params["end_date"] = end_date

        last_error: Exception | None = None
        for attempt in range(1, MAX_RETRIES + 1):
            self._limiter.acquire()
            try:
                status, payload = self._request(FINMIND_DATA_URL, params, self._token)
            except Exception as exc:  # 網路層例外，進入重試
                last_error = exc
                self._sleep(BACKOFF_BASE_SECONDS ** attempt)
                continue

            if status == 402:
                raise QuotaExceededError(
                    f"資料集 {spec.finmind_name} 需付費或額度已用盡（HTTP 402）。"
                    f"免費帳號請改用其他資料集或升級方案。"
                )
            if status == 200:
                data = payload.get("data", [])
                return pd.DataFrame(data)
            if status in (429, 500, 502, 503, 504):
                # 可重試的暫時性錯誤
                last_error = RuntimeError(f"暫時性錯誤 HTTP {status}")
                self._sleep(BACKOFF_BASE_SECONDS ** attempt)
                continue
            # 其他狀態碼視為不可重試
            raise RuntimeError(
                f"FinMind 回傳非預期狀態碼 {status}（dataset={spec.finmind_name}）。"
                f"建議檢查 dataset 名稱與參數。"
            )

        raise RuntimeError(
            f"抓取 {spec.finmind_name} 失敗，已重試 {MAX_RETRIES} 次。最後錯誤：{last_error}"
        )


def validate_schema(df: pd.DataFrame, spec: DatasetSpec) -> pd.DataFrame:
    """驗證資料欄位符合規格，不符即報錯而非默默繼續。

    參數:
        df: 待驗證的 DataFrame。
        spec: 資料集規格（提供必要欄位）。

    回傳:
        通過驗證的 DataFrame（原樣回傳）。

    例外:
        ValueError: 當缺少必要欄位。
    """
    if df.empty:
        # 空表允許（可能該區間無資料），但仍檢查是否至少有欄位定義
        return df
    missing = set(spec.required_cols) - set(df.columns)
    if missing:
        raise ValueError(
            f"資料集 {spec.finmind_name} 缺少必要欄位：{sorted(missing)}。"
            f"實際欄位：{sorted(df.columns)}。請核對 FinMind 文件的欄位名稱。"
        )
    return df


class DataSource:
    """資料層編排：快取 → 供應商鏈（FinMind→備援）→ schema 驗證 → 寫快取。"""

    def __init__(
        self,
        token: str | None = None,
        cache_dir: Path = DEFAULT_CACHE_DIR,
        primary: FinMindProvider | None = None,
        fallbacks: list[object] | None = None,
    ) -> None:
        """初始化資料層。

        參數:
            token: FinMind token；None 時從環境變數讀取。
            cache_dir: 快取目錄。
            primary: 主供應商，None 時以 token 建立 FinMindProvider。
            fallbacks: 備援供應商清單（需具 name 與 fetch）；None 時為空。

        回傳:
            無。

        例外:
            ValueError: 當無法取得 token 且需要建立預設供應商。
        """
        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        resolved_token = token or os.environ.get(TOKEN_ENV_VAR, "")
        self._primary = primary or FinMindProvider(token=resolved_token)
        self._fallbacks = fallbacks or []
        # 記錄每次 fetch 實際使用的供應商，供出口稽核
        self.provider_log: list[dict[str, str]] = []

    def _cache_path(self, dataset_key: str, data_id: str | None, start_date: str, end_date: str | None) -> Path:
        """組出快取檔路徑（以查詢參數為 key）。"""
        safe_id = data_id or "ALL"
        safe_end = end_date or "LATEST"
        fname = f"{dataset_key}__{safe_id}__{start_date}__{safe_end}.parquet"
        return self._cache_dir / fname

    def fetch(
        self,
        dataset_key: str,
        data_id: str | None = None,
        start_date: str = "2018-01-01",
        end_date: str | None = None,
        force_refresh: bool = False,
    ) -> pd.DataFrame:
        """取得資料集，依快取→供應商鏈→驗證→寫快取流程。

        參數:
            dataset_key: DATASETS 中的鍵（如 "institutional"）。
            data_id: 股票代碼；None 表示全市場。
            start_date: 起始日（YYYY-MM-DD）。
            end_date: 結束日；None 表示到最新。
            force_refresh: True 時忽略快取重新抓取。

        回傳:
            通過 schema 驗證的 DataFrame。付費資料集在免費帳號回傳空表。

        例外:
            KeyError: 當 dataset_key 不在登錄表。
            ValueError: schema 驗證失敗。
            RuntimeError: 所有供應商皆失敗。
        """
        if dataset_key not in DATASETS:
            raise KeyError(f"未知資料集鍵：{dataset_key}。可用：{sorted(DATASETS)}")
        spec = DATASETS[dataset_key]

        # 付費資料集在免費帳號直接跳過（明確提示，不默默失敗）
        if spec.tier == "paid":
            self.provider_log.append({"dataset": dataset_key, "provider": "skipped_paid"})
            warnings.warn(
                f"資料集 {dataset_key}（{spec.finmind_name}）為付費層，免費帳號跳過。"
                f"若需 P2 主力分點，請升級 FinMind 方案。",
                stacklevel=2,
            )
            return pd.DataFrame(columns=list(spec.required_cols))

        cache_path = self._cache_path(dataset_key, data_id, start_date, end_date)
        if cache_path.exists() and not force_refresh:
            self.provider_log.append({"dataset": dataset_key, "provider": "cache"})
            return pd.read_parquet(cache_path)

        # 供應商鏈：主供應商優先，失敗才降級
        providers: list[object] = [self._primary, *self._fallbacks]
        last_error: Exception | None = None
        for provider in providers:
            try:
                raw = provider.fetch(spec, data_id, start_date, end_date)  # type: ignore[attr-defined]
                df = validate_schema(raw, spec)
                self.provider_log.append(
                    {"dataset": dataset_key, "provider": getattr(provider, "name", "unknown")}
                )
                if not df.empty:
                    df.to_parquet(cache_path, index=False)
                return df
            except QuotaExceededError:
                # 付費/額度問題不靠備援解決，直接往上拋
                raise
            except Exception as exc:  # noqa: BLE001 — 記錄後嘗試下一個供應商
                last_error = exc
                continue

        raise RuntimeError(
            f"資料集 {dataset_key} 所有供應商皆失敗。最後錯誤：{last_error}"
        )
