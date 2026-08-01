"""台股波段系統｜naive 基準策略。

刻意簡單、透明的一條規則，目的是驗證「特徵→權重→裁判」整條管線跑得通，
而不是要贏。它會被裁判誠實評分，FAIL 也是成功（證明管線暢通）。

規則：
    每隔 rebalance_days 個交易日再平衡一次；
    當日依 signal_col（預設投信 N 日累積買超）由高到低排序，
    取訊號為正的前 top_k 檔，等權買進，持有到下次再平衡。
"""
from __future__ import annotations

import pandas as pd

# 策略預設參數（屬超參數，交給裁判驗證，勿手調至最漂亮）
DEFAULT_TOP_K: int = 5
DEFAULT_REBALANCE_DAYS: int = 5


def build_weight_matrix(
    feature_panel: pd.DataFrame,
    trading_dates: pd.DatetimeIndex,
    signal_col: str = "inst_net_5d",
    top_k: int = DEFAULT_TOP_K,
    rebalance_days: int = DEFAULT_REBALANCE_DAYS,
) -> pd.DataFrame:
    """由特徵面板產生每日目標權重矩陣。

    參數:
        feature_panel: tidy 特徵面板，需含 date、stock_id 與 signal_col。
        trading_dates: 完整交易日索引（通常取自價格面板），權重會對齊到此。
        signal_col: 選股訊號欄，預設投信 5 日累積買超。
        top_k: 每次再平衡持有的檔數。
        rebalance_days: 每隔幾個交易日再平衡一次。

    回傳:
        權重矩陣 DataFrame，index 為 trading_dates，columns 為股票代碼，
        值為目標權重（等權，未持有為 0）。空輸入回傳空 DataFrame。

    例外:
        ValueError: 當 feature_panel 缺少必要欄位、或 top_k/rebalance_days 非正。
    """
    if feature_panel.empty:
        return pd.DataFrame()
    required = {"date", "stock_id", signal_col}
    missing = required - set(feature_panel.columns)
    if missing:
        raise ValueError(f"特徵面板缺少欄位：{sorted(missing)}")
    if top_k <= 0 or rebalance_days <= 0:
        raise ValueError("top_k 與 rebalance_days 必須為正整數。")

    fp = feature_panel.copy()
    fp["date"] = pd.to_datetime(fp["date"])

    # 寬訊號矩陣：index 為日期，columns 為股票代碼
    signal_wide = fp.pivot_table(index="date", columns="stock_id", values=signal_col, aggfunc="last")
    universe = list(signal_wide.columns)

    dates = pd.DatetimeIndex(sorted(trading_dates.unique()))

    # 再平衡日：每隔 rebalance_days 取一個交易日
    rebalance_dates = dates[::rebalance_days]
    signal_on_dates = signal_wide.reindex(dates)

    # 只在再平衡日建立權重列，其餘日靠前向填補（持有）
    reb_weights = pd.DataFrame(0.0, index=rebalance_dates, columns=universe)
    for d in rebalance_dates:
        row = signal_on_dates.loc[d].dropna()
        positive = row[row > 0]
        if positive.empty:
            continue  # 當日無正訊號 → 全現金
        chosen = positive.sort_values(ascending=False).head(top_k)
        weight = 1.0 / len(chosen)  # 等權（不足 top_k 檔則平分於已選）
        reb_weights.loc[d, chosen.index] = weight

    # 對齊完整交易日並前向填補：再平衡之間維持持有
    return reb_weights.reindex(dates).ffill().fillna(0.0)
