"""台股波段系統｜P1 籌碼特徵：三大法人（投信為主）買超動能。

由三大法人原始資料計算 point-in-time 特徵，輸出 tidy 面板供模型使用。

point-in-time 契約：
    特徵列的 date=T 代表「用 T 日（含）以前資料算出、T 日盤後可得」。
    因此 available_date == date（三大法人為每日盤後資料，無週更 lag）。
    下游用 date=T 的特徵做決策，交由評估框架的 exec_lag 位移到 T+1 執行，
    確保不會用到 T 日尚不可得的資訊。

設計重點：
    - 投信權重高於外資（外資買超常含被動 ETF/指數調權，主動性較低）。
    - N 日窗長為超參數，交給裁判驗證，不手調至 backtest 最漂亮。
    - 純運算，不連網；可用合成資料完整測試。
"""
from __future__ import annotations

import pandas as pd

from config import FEATURE_WINDOW_DAYS, INSTITUTION_NAMES, MARGIN_COLS


def _pivot_net(inst_df: pd.DataFrame) -> pd.DataFrame:
    """把長格式三大法人資料轉成每檔每日的各類別淨買超（買−賣）。

    參數:
        inst_df: 欄位含 date、stock_id、name、buy、sell 的長格式資料。

    回傳:
        寬格式 DataFrame，index 為 (stock_id, date)，columns 為各類別淨買超
        （欄名為 INSTITUTION_NAMES 的鍵，如 investment_trust）。

    例外:
        ValueError: 當缺少必要欄位。
    """
    required = {"date", "stock_id", "name", "buy", "sell"}
    missing = required - set(inst_df.columns)
    if missing:
        raise ValueError(f"三大法人資料缺少欄位：{sorted(missing)}")

    df = inst_df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["net"] = df["buy"].astype("float64") - df["sell"].astype("float64")

    # 只保留關心的類別，並把 FinMind 的 name 值映射成我方鍵
    name_to_key = {v: k for k, v in INSTITUTION_NAMES.items()}
    df = df[df["name"].isin(name_to_key)].copy()
    df["cat"] = df["name"].map(name_to_key)

    wide = (
        df.pivot_table(index=["stock_id", "date"], columns="cat", values="net", aggfunc="sum")
        .sort_index()
    )
    # 補齊可能缺席的類別欄，缺值視為 0（當日該類別無資料）
    for key in INSTITUTION_NAMES:
        if key not in wide.columns:
            wide[key] = 0.0
    return wide.fillna(0.0)


def _rolling_sum_by_stock(series_by_stock: pd.DataFrame, col: str, window: int) -> pd.Series:
    """對每檔股票計算某欄的 N 日滾動加總（時序，不跨股票）。

    參數:
        series_by_stock: index 為 (stock_id, date) 的寬表。
        col: 要滾動的欄名。
        window: 窗長（交易日數）。

    回傳:
        Series，index 對齊輸入，值為該檔近 window 日的加總。
    """
    return series_by_stock.groupby(level="stock_id")[col].transform(
        lambda s: s.rolling(window, min_periods=1).sum()
    )


def _positive_streak_by_stock(series_by_stock: pd.DataFrame, col: str) -> pd.Series:
    """對每檔股票計算「連續為正」的天數（如連續買超天數）。

    參數:
        series_by_stock: index 為 (stock_id, date) 的寬表。
        col: 要計算連續為正的欄名。

    回傳:
        Series，index 對齊輸入，值為到當日為止的連續為正天數（非正則歸零）。
    """
    def _streak(s: pd.Series) -> pd.Series:
        positive = s > 0
        # 以「非正」為分組邊界，組內累加，非正日歸零
        group = (~positive).cumsum()
        return positive.groupby(group).cumsum()

    return series_by_stock.groupby(level="stock_id")[col].transform(_streak)


def build_institutional_features(
    inst_df: pd.DataFrame,
    price_df: pd.DataFrame | None = None,
    window: int = FEATURE_WINDOW_DAYS,
) -> pd.DataFrame:
    """計算投信買超動能為主的 P1 籌碼特徵。

    參數:
        inst_df: 三大法人長格式資料（date、stock_id、name、buy、sell）。
        price_df: 選填的價格資料（含 date、stock_id、Trading_Volume）；
                  提供時額外計算「投信淨買超佔成交量比」。
        window: N 日累積窗長，預設取自 config。

    回傳:
        tidy 特徵面板 DataFrame，欄位：
            date、stock_id、available_date、
            inst_net（投信單日淨買超）、
            inst_net_{window}d（投信 N 日累積）、
            inst_buy_streak（投信連續買超天數）、
            foreign_net_{window}d（外資 N 日累積，供對比、權重宜低）、
            total_net_{window}d（三大法人合計 N 日累積）、
            [inst_net_vol_pct]（投信淨買超佔成交量，price_df 提供時才有）。
        空輸入回傳帶欄位的空 DataFrame。

    例外:
        ValueError: 當 inst_df 缺少必要欄位。
    """
    if inst_df.empty:
        cols = [
            "date", "stock_id", "available_date",
            "inst_net", f"inst_net_{window}d", "inst_buy_streak",
            f"foreign_net_{window}d", f"total_net_{window}d",
        ]
        return pd.DataFrame(columns=cols)

    wide = _pivot_net(inst_df)

    # 三大法人合計淨買超（各類別加總）
    wide["total_net"] = wide[list(INSTITUTION_NAMES)].sum(axis=1)

    feat = pd.DataFrame(index=wide.index)
    feat["inst_net"] = wide["investment_trust"]
    feat[f"inst_net_{window}d"] = _rolling_sum_by_stock(wide, "investment_trust", window)
    feat["inst_buy_streak"] = _positive_streak_by_stock(wide, "investment_trust")
    feat[f"foreign_net_{window}d"] = _rolling_sum_by_stock(wide, "foreign", window)
    feat[f"total_net_{window}d"] = _rolling_sum_by_stock(wide, "total_net", window)

    feat = feat.reset_index()  # 攤平成 stock_id、date 欄

    # 選填：投信淨買超佔成交量比（需價格資料的 Trading_Volume）
    if price_df is not None and not price_df.empty:
        if not {"date", "stock_id", "Trading_Volume"}.issubset(price_df.columns):
            raise ValueError("price_df 需含 date、stock_id、Trading_Volume 才能算成交量正規化。")
        vol = price_df[["date", "stock_id", "Trading_Volume"]].copy()
        vol["date"] = pd.to_datetime(vol["date"])
        feat = feat.merge(vol, on=["date", "stock_id"], how="left")
        # 成交量為 0 或缺值時，比率設為 0，避免除以零
        safe_vol = feat["Trading_Volume"].replace({0: pd.NA})
        feat["inst_net_vol_pct"] = (feat["inst_net"] / safe_vol).fillna(0.0)
        feat = feat.drop(columns="Trading_Volume")

    # point-in-time：三大法人為每日盤後資料，available_date 即資料日
    feat["available_date"] = feat["date"]

    # 欄位排序：識別欄在前
    lead = ["date", "stock_id", "available_date"]
    others = [c for c in feat.columns if c not in lead]
    return feat[lead + others].sort_values(["stock_id", "date"]).reset_index(drop=True)


def build_margin_features(
    margin_df: pd.DataFrame,
    price_df: pd.DataFrame | None = None,
    window: int = FEATURE_WINDOW_DAYS,
) -> pd.DataFrame:
    """計算融資融券情緒特徵（散戶槓桿反指標）。

    參數:
        margin_df: 融資融券資料，欄位含 config.MARGIN_COLS 對應的實際欄名。
        price_df: 選填價格資料（含 date、stock_id、close）；提供時計算「資券背離」
                  （價漲但融資減，籌碼偏空的訊號）。
        window: N 日窗長，預設取自 config。

    回傳:
        tidy 特徵面板 DataFrame，欄位：
            date、stock_id、available_date、
            margin_chg（融資單日增減）、
            margin_chg_pct_{window}d（N 日融資餘額變化率）、
            short_margin_ratio（券資比＝融券餘額/融資餘額）、
            margin_util（融資使用率＝融資餘額/融資限額）、
            [margin_price_divergence]（價漲融資減旗標，price_df 提供時才有）。
        空輸入回傳帶欄位的空 DataFrame。

    例外:
        ValueError: 當 margin_df 缺少必要欄位。
    """
    bal = MARGIN_COLS["margin_balance"]
    bal_prev = MARGIN_COLS["margin_balance_prev"]
    limit = MARGIN_COLS["margin_limit"]
    short_bal = MARGIN_COLS["short_balance"]

    base_cols = [
        "date", "stock_id", "available_date",
        "margin_chg", f"margin_chg_pct_{window}d", "short_margin_ratio", "margin_util",
    ]
    if margin_df.empty:
        return pd.DataFrame(columns=base_cols)

    required = {"date", "stock_id", bal, bal_prev, limit, short_bal}
    missing = required - set(margin_df.columns)
    if missing:
        raise ValueError(f"融資融券資料缺少欄位：{sorted(missing)}")

    df = margin_df[["date", "stock_id", bal, bal_prev, limit, short_bal]].copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index(["stock_id", "date"]).sort_index()

    feat = pd.DataFrame(index=df.index)
    # 融資單日增減（今日餘額 − 昨日餘額）
    feat["margin_chg"] = df[bal].astype("float64") - df[bal_prev].astype("float64")
    # N 日融資餘額變化率：(今日 − N日前) / N日前，除零安全
    def _pct_change_nd(s: pd.Series) -> pd.Series:
        past = s.shift(window)
        return ((s - past) / past.replace({0: pd.NA})).fillna(0.0)

    feat[f"margin_chg_pct_{window}d"] = (
        df.groupby(level="stock_id")[bal].transform(_pct_change_nd)
    )
    # 券資比＝融券餘額 / 融資餘額（除零安全）
    safe_bal = df[bal].replace({0: pd.NA})
    feat["short_margin_ratio"] = (df[short_bal] / safe_bal).fillna(0.0)
    # 融資使用率＝融資餘額 / 融資限額（除零安全）
    safe_limit = df[limit].replace({0: pd.NA})
    feat["margin_util"] = (df[bal] / safe_limit).fillna(0.0)

    feat = feat.reset_index()

    # 選填：資券背離（近 window 日價漲，但融資減 → 籌碼偏空訊號）
    if price_df is not None and not price_df.empty:
        if not {"date", "stock_id", "close"}.issubset(price_df.columns):
            raise ValueError("price_df 需含 date、stock_id、close 才能算資券背離。")
        px = price_df[["date", "stock_id", "close"]].copy()
        px["date"] = pd.to_datetime(px["date"])
        px = px.set_index(["stock_id", "date"]).sort_index()
        price_ret = px.groupby(level="stock_id")["close"].transform(
            lambda s: s.pct_change(window)
        ).reset_index(name="price_ret_nd")
        feat = feat.merge(price_ret, on=["stock_id", "date"], how="left")
        price_up = feat["price_ret_nd"].fillna(0.0) > 0
        margin_down = feat[f"margin_chg_pct_{window}d"] < 0
        feat["margin_price_divergence"] = (price_up & margin_down).astype("int64")
        feat = feat.drop(columns="price_ret_nd")

    feat["available_date"] = feat["date"]
    lead = ["date", "stock_id", "available_date"]
    others = [c for c in feat.columns if c not in lead]
    return feat[lead + others].sort_values(["stock_id", "date"]).reset_index(drop=True)
