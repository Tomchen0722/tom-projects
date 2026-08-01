"""台股波段系統｜面板組裝：把長格式資料轉成回測所需的寬面板。

分兩類函式：
- 純函式（build_price_panel、build_adjusted_price_panel、long_to_returns）：
  可在沙盒用合成資料完整測試。
- 抓取輔助（fetch_universe_long、fetch_benchmark_returns）：需連 FinMind，於本機執行。

價格以免費 TaiwanStockPrice 抓取，再用免費的除權息結果表自行還原，
除權息假跌已校正，報告數字可信。
"""
from __future__ import annotations

import pandas as pd


def build_price_panel(price_long: pd.DataFrame, value_col: str = "close") -> pd.DataFrame:
    """把長格式價格轉成寬面板（index 為日期，columns 為股票代碼）。

    參數:
        price_long: 長格式價格，需含 date、stock_id 與 value_col。
        value_col: 要取的價格欄，預設 close。

    回傳:
        寬面板 DataFrame，index 為 DatetimeIndex，columns 為股票代碼，值為價格。
        空輸入回傳空 DataFrame。

    例外:
        ValueError: 當缺少必要欄位。
    """
    if price_long.empty:
        return pd.DataFrame()
    required = {"date", "stock_id", value_col}
    missing = required - set(price_long.columns)
    if missing:
        raise ValueError(f"價格資料缺少欄位：{sorted(missing)}")

    df = price_long[["date", "stock_id", value_col]].copy()
    df["date"] = pd.to_datetime(df["date"])
    panel = df.pivot_table(index="date", columns="stock_id", values=value_col, aggfunc="last")
    return panel.sort_index()


def build_adjusted_price_panel(price_long: pd.DataFrame, dividend_long: pd.DataFrame) -> pd.DataFrame:
    """由未還原價與除權息結果，建立還原股價寬面板（後復權，以最新價為基準往回調）。

    還原原理：除權息交易日 e 的還原因子 f_e = after_price / before_price（通常 < 1）。
    把每個歷史日 T 的價格，乘上所有「晚於 T」的除權息日因子之連乘積，使除權息造成的
    假跌從報酬序列中消失。最新日不調整（因子 1），故最新價與未還原一致。

    參數:
        price_long: 未還原長格式價格，含 date、stock_id、close。
        dividend_long: 除權息結果，含 date、stock_id、before_price、after_price。

    回傳:
        還原後寬面板 DataFrame（index 為日期，columns 為股票代碼）。
        dividend_long 為空時，回傳未還原面板（等同無調整）。

    例外:
        ValueError: 當 dividend_long 缺少必要欄位。
    """
    raw = build_price_panel(price_long)
    if raw.empty or dividend_long.empty:
        return raw

    required = {"date", "stock_id", "before_price", "after_price"}
    missing = required - set(dividend_long.columns)
    if missing:
        raise ValueError(f"除權息資料缺少欄位：{sorted(missing)}")

    div = dividend_long[["date", "stock_id", "before_price", "after_price"]].copy()
    div["date"] = pd.to_datetime(div["date"])
    div["before_price"] = pd.to_numeric(div["before_price"], errors="coerce")
    div["after_price"] = pd.to_numeric(div["after_price"], errors="coerce")
    # 因子 = 除息後參考價 / 除息前參考價；前價非正或缺值則視為無調整（因子 1）
    div["factor"] = div["after_price"] / div["before_price"].where(div["before_price"] > 0)
    div = div.dropna(subset=["factor"])

    adjusted = raw.copy()
    for stock in raw.columns:
        events = div[div["stock_id"] == stock]
        if events.empty:
            continue
        # 每檔的因子序列：預設 1，除權息日填入該日因子
        f = pd.Series(1.0, index=raw.index)
        for ex_date, factor in zip(events["date"], events["factor"]):
            if ex_date in f.index:
                f.loc[ex_date] = factor
        # M[T] = 所有「晚於 T」的除權息日因子連乘積（後復權乘數）
        rev_cumprod = f[::-1].cumprod()[::-1]
        multiplier = rev_cumprod.shift(-1).fillna(1.0)
        adjusted[stock] = raw[stock] * multiplier

    return adjusted


def long_to_returns(price_long_single: pd.DataFrame, value_col: str = "close") -> pd.Series:
    """把單一標的的長格式價格轉成每日報酬序列（供基準使用）。

    參數:
        price_long_single: 單一標的長格式價格，含 date 與 value_col。
        value_col: 價格欄，預設 close。

    回傳:
        每日報酬 Series，index 為 DatetimeIndex。空輸入回傳空 Series。

    例外:
        ValueError: 當缺少必要欄位。
    """
    if price_long_single.empty:
        return pd.Series(dtype="float64")
    if not {"date", value_col}.issubset(price_long_single.columns):
        raise ValueError(f"基準價格需含 date 與 {value_col}。")
    df = price_long_single[["date", value_col]].copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")
    return df[value_col].pct_change(fill_method=None).fillna(0.0)


def fetch_universe_long(data_source, universe: list[str], start_date: str, end_date: str) -> dict[str, pd.DataFrame]:
    """抓取整個股票池的價格、三大法人、融資融券、除權息（長格式，跨股票串接）。

    參數:
        data_source: DataSource 實例。
        universe: 股票代碼清單。
        start_date: 起始日（YYYY-MM-DD）。
        end_date: 結束日（YYYY-MM-DD）。

    回傳:
        dict，含 price、institutional、margin、dividend 四個長格式 DataFrame。

    例外:
        由 data_source.fetch 傳遞而來（如所有供應商失敗）。
    """
    price_parts: list[pd.DataFrame] = []
    inst_parts: list[pd.DataFrame] = []
    margin_parts: list[pd.DataFrame] = []
    div_parts: list[pd.DataFrame] = []
    for i, stock_id in enumerate(universe, start=1):
        print(f"  抓取 {stock_id}（{i}/{len(universe)}）…")
        price_parts.append(data_source.fetch("price", stock_id, start_date, end_date))
        inst_parts.append(data_source.fetch("institutional", stock_id, start_date, end_date))
        margin_parts.append(data_source.fetch("margin", stock_id, start_date, end_date))
        div_parts.append(data_source.fetch("dividend_result", stock_id, start_date, end_date))

    return {
        "price": pd.concat(price_parts, ignore_index=True) if price_parts else pd.DataFrame(),
        "institutional": pd.concat(inst_parts, ignore_index=True) if inst_parts else pd.DataFrame(),
        "margin": pd.concat(margin_parts, ignore_index=True) if margin_parts else pd.DataFrame(),
        "dividend": pd.concat(div_parts, ignore_index=True) if div_parts else pd.DataFrame(),
    }


def fetch_benchmark_returns(data_source, benchmark_id: str, start_date: str, end_date: str) -> pd.Series:
    """抓取基準標的（如 0050）還原股價並轉成每日報酬。

    參數:
        data_source: DataSource 實例。
        benchmark_id: 基準標的代碼（如 "0050"）。
        start_date: 起始日。
        end_date: 結束日。

    回傳:
        每日報酬 Series（已還原，與策略端一致才公平比較）。

    例外:
        由 data_source.fetch 傳遞而來。
    """
    price = data_source.fetch("price", benchmark_id, start_date, end_date)
    dividend = data_source.fetch("dividend_result", benchmark_id, start_date, end_date)
    adj_panel = build_adjusted_price_panel(price, dividend)
    if adj_panel.empty:
        return pd.Series(dtype="float64")
    return adj_panel[benchmark_id].pct_change(fill_method=None).fillna(0.0)
