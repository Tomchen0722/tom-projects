"""台股波段系統｜複合訊號組合。

把多個「各有預測力」的訊號，用逐日橫斷面百分位排名（對離群值穩健）依方向加總成
單一複合分數。方向 +1 表示「越高越好」、-1 表示「越高越差」（反指標）。

由訊號品質（IC）分析挑出真正有 edge 的訊號來組合，而非手調湊贏 benchmark。
純運算，不連網。
"""
from __future__ import annotations

import pandas as pd


def feature_to_panel(feature_panel: pd.DataFrame, col: str) -> pd.DataFrame:
    """把 tidy 特徵面板的某欄轉成 date × stock_id 寬面板。

    參數:
        feature_panel: tidy 特徵面板，含 date、stock_id 與 col。
        col: 要取出的特徵欄名。

    回傳:
        寬面板 DataFrame（index 為日期，columns 為股票代碼）。

    例外:
        ValueError: 當缺少必要欄位。
    """
    required = {"date", "stock_id", col}
    missing = required - set(feature_panel.columns)
    if missing:
        raise ValueError(f"特徵面板缺少欄位：{sorted(missing)}")
    p = feature_panel.copy()
    p["date"] = pd.to_datetime(p["date"])
    return p.pivot_table(index="date", columns="stock_id", values=col, aggfunc="last")


def _cross_sectional_rank(wide: pd.DataFrame) -> pd.DataFrame:
    """逐日（每列）橫斷面百分位排名並置中到 [-0.5, 0.5]。

    參數:
        wide: 訊號寬面板（index 為日期，columns 為股票代碼，可含 NaN）。

    回傳:
        置中百分位排名寬面板；當日有效股票不足 2 檔的位置為 NaN。
    """
    # pct=True 給 (0,1] 百分位；減 0.5 置中，使正負對稱、尺度一致
    return wide.rank(axis=1, pct=True) - 0.5


def build_composite_signal(specs: list[tuple[pd.DataFrame, float]]) -> pd.DataFrame:
    """把多個訊號寬面板依方向組合成複合訊號（tidy 面板）。

    參數:
        specs: (訊號寬面板, 方向) 的清單。方向 +1 表越高越好、-1 表反指標。
               各面板 index 為日期、columns 為股票代碼。

    回傳:
        tidy 面板 DataFrame，欄位 date、stock_id、composite_signal。
        空清單或全空面板回傳帶欄位的空 DataFrame。

    例外:
        ValueError: 當 specs 為空。
    """
    if not specs:
        raise ValueError("specs 不可為空，至少需要一個訊號。")

    combined: pd.DataFrame | None = None
    for wide, direction in specs:
        if wide is None or wide.empty:
            continue
        contrib = direction * _cross_sectional_rank(wide)
        combined = contrib if combined is None else combined.add(contrib, fill_value=0.0)

    if combined is None or combined.empty:
        return pd.DataFrame(columns=["date", "stock_id", "composite_signal"])

    # 寬轉 tidy（stack 會自動丟棄 NaN）
    tidy = combined.stack().rename("composite_signal").reset_index()
    tidy.columns = ["date", "stock_id", "composite_signal"]
    return tidy
