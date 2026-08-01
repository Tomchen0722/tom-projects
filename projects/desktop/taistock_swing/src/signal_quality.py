"""台股波段系統｜訊號品質分析（IC / 未來報酬相關性）。

目的：把「訊號有沒有預測力」從「選股規則」與「打不打得贏指數」中拆開，單獨檢驗。
若訊號本身 IC ≈ 0，再精巧的策略也救不回來；IC 顯著為正才值得投資更複雜的模型。

point-in-time：訊號 date=T（T 日盤後可得）預測「T+1 執行、持有 horizon 日」的報酬，
以 exec_lag 位移確保不使用 T 日尚不可得的資訊，與評估框架一致。

純運算，不連網；可用合成資料完整測試。
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def compute_forward_returns(price_panel: pd.DataFrame, horizon: int, exec_lag: int = 1) -> pd.DataFrame:
    """由還原股價面板計算「未來 horizon 日」報酬（T+exec_lag 進場）。

    參數:
        price_panel: 還原股價寬面板（index 為日期，columns 為股票代碼）。
        horizon: 持有天數（交易日）。
        exec_lag: 訊號到執行的延遲，預設 1（T 決策、T+1 進場）。

    回傳:
        未來報酬寬面板（index 為日期 T，值為 T+exec_lag 進場、持有 horizon 日的報酬）。

    例外:
        ValueError: 當 horizon 或 exec_lag 非正/負、或面板為空。
    """
    if price_panel.empty:
        raise ValueError("price_panel 為空，無法計算未來報酬。")
    if horizon <= 0 or exec_lag < 0:
        raise ValueError("horizon 必須為正、exec_lag 不可為負。")
    entry = price_panel.shift(-exec_lag)               # T+exec_lag 進場價
    exit_price = price_panel.shift(-(exec_lag + horizon))  # 持有 horizon 日後出場價
    return exit_price / entry - 1.0


def _spearman(a: pd.Series, b: pd.Series, min_names: int) -> float:
    """兩序列的 Spearman 秩相關（以秩的 Pearson 相關實作，免 scipy）。

    參數:
        a, b: 對齊的兩序列（可含 NaN）。
        min_names: 有效配對數下限，低於此回傳 NaN。

    回傳:
        Spearman 相關係數；有效樣本不足或無變異時回傳 NaN。
    """
    mask = a.notna() & b.notna()
    a2, b2 = a[mask], b[mask]
    if len(a2) < max(min_names, 2):
        return np.nan
    ra, rb = a2.rank(), b2.rank()
    if ra.std(ddof=1) == 0 or rb.std(ddof=1) == 0:
        return np.nan
    return float(ra.corr(rb))  # 秩的 Pearson = Spearman


def compute_ic(
    signal_panel: pd.DataFrame,
    forward_returns: pd.DataFrame,
    min_names: int = 5,
) -> tuple[pd.Series, dict[str, float]]:
    """計算逐日橫斷面 IC（訊號與未來報酬的 Spearman 相關）與摘要統計。

    參數:
        signal_panel: 訊號寬面板（index 為日期，columns 為股票代碼）。
        forward_returns: 未來報酬寬面板（compute_forward_returns 的輸出）。
        min_names: 每日計算 IC 所需的最少有效股票數。

    回傳:
        (ic_series, summary)。ic_series 為逐日 IC（已去除無效日）；
        summary 含 mean_ic、ic_std、icir（mean/std）、t_stat、hit_rate（IC>0 比例）、n_periods。

    例外:
        ValueError: 當面板無共同日期或欄位。
    """
    common_dates = signal_panel.index.intersection(forward_returns.index)
    common_cols = signal_panel.columns.intersection(forward_returns.columns)
    if len(common_dates) == 0 or len(common_cols) == 0:
        raise ValueError("訊號與未來報酬面板無共同日期或股票欄位。")

    sig = signal_panel.loc[common_dates, common_cols]
    fwd = forward_returns.loc[common_dates, common_cols]

    ic_values: dict[pd.Timestamp, float] = {}
    for date in common_dates:
        ic_values[date] = _spearman(sig.loc[date], fwd.loc[date], min_names)

    ic_series = pd.Series(ic_values).dropna()
    if ic_series.empty:
        summary = {
            "mean_ic": 0.0, "ic_std": 0.0, "icir": 0.0,
            "t_stat": 0.0, "hit_rate": 0.0, "n_periods": 0.0,
        }
        return ic_series, summary

    n = len(ic_series)
    mean_ic = float(ic_series.mean())
    ic_std = float(ic_series.std(ddof=1)) if n > 1 else 0.0
    icir = float(mean_ic / ic_std) if ic_std > 0 else 0.0
    # 注意：未來報酬期重疊會使各日 IC 自相關，t 值偏樂觀，僅供粗略參考
    t_stat = float(icir * np.sqrt(n)) if ic_std > 0 else 0.0
    hit_rate = float((ic_series > 0).mean())
    summary = {
        "mean_ic": mean_ic, "ic_std": ic_std, "icir": icir,
        "t_stat": t_stat, "hit_rate": hit_rate, "n_periods": float(n),
    }
    return ic_series, summary


def quantile_analysis(
    signal_panel: pd.DataFrame,
    forward_returns: pd.DataFrame,
    n_quantiles: int = 3,
    min_names: int = 6,
) -> pd.DataFrame:
    """依訊號把股票分組，計算各組平均未來報酬，檢驗單調性與多空價差。

    參數:
        signal_panel: 訊號寬面板。
        forward_returns: 未來報酬寬面板。
        n_quantiles: 分組數（如 3 = 高/中/低）。
        min_names: 每日分組所需最少有效股票數。

    回傳:
        DataFrame，index 為分位（0=最低訊號 … n-1=最高訊號），欄位 mean_forward_return；
        另含一列 "top_minus_bottom"（最高組 − 最低組）。

    例外:
        ValueError: 當 n_quantiles < 2。
    """
    if n_quantiles < 2:
        raise ValueError("n_quantiles 至少為 2。")

    common_dates = signal_panel.index.intersection(forward_returns.index)
    common_cols = signal_panel.columns.intersection(forward_returns.columns)
    sig = signal_panel.loc[common_dates, common_cols]
    fwd = forward_returns.loc[common_dates, common_cols]

    # 逐日分組，累積各組的未來報酬
    bucket_returns: dict[int, list[float]] = {q: [] for q in range(n_quantiles)}
    for date in common_dates:
        s = sig.loc[date].dropna()
        f = fwd.loc[date]
        pair = pd.DataFrame({"s": s, "f": f}).dropna()
        if len(pair) < max(min_names, n_quantiles):
            continue
        # 用秩切分，避免同值造成分組不均
        labels = pd.qcut(pair["s"].rank(method="first"), n_quantiles, labels=False)
        for q in range(n_quantiles):
            bucket_returns[q].extend(pair.loc[labels == q, "f"].tolist())

    means = {q: (float(np.mean(v)) if v else np.nan) for q, v in bucket_returns.items()}
    result = pd.DataFrame({"mean_forward_return": pd.Series(means)})
    result.index.name = "quantile"
    top, bottom = n_quantiles - 1, 0
    if not np.isnan(means[top]) and not np.isnan(means[bottom]):
        result.loc["top_minus_bottom", "mean_forward_return"] = means[top] - means[bottom]
    return result
