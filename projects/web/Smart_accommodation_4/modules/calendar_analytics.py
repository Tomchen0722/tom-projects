# -*- coding: utf-8 -*-
"""calendar_analytics.py — 未來檔期分析模組

資料來源:scripts/build_calendar_features.py 產出的輕量檔案
(不直接讀 234 萬列的 calendar.csv.gz,以符合 Streamlit Cloud 記憶體限制)。

主要能力
--------
1. 逐日訂房遮罩 → 日曆熱度資料
2. 未來各月已訂率 vs 同商圈基準
3. 連續空檔警示(未來 90 天)
4. 營收最適定價:以同商圈同房型的「真實已訂天數」建立營收曲線

重要限制(見 doc/04):Inside Airbnb 的 available='f' 同時包含「已被預訂」與
「房東主動封鎖」,故一律排除全年封鎖與全年全空的房源,並以未來 0~90 天為主要判讀窗口。
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

try:
    import streamlit as st
    cache_data = st.cache_data
except Exception:                       # 允許無 Streamlit 環境測試
    def cache_data(*a, **k):
        def deco(f):
            return f
        return deco if not a else a[0]

DATA = Path(__file__).resolve().parent.parent / "data"
METRICS_CSV = DATA / "_calendar_metrics.csv"
MARKET_CSV = DATA / "_calendar_market.csv"
LISTINGS_GZ = DATA / "listings_cleaned.csv.gz"

# ── 遠期日曆可信度門檻(2026-07-22 修正)────────────────────────
# Inside Airbnb 的 available='f' 同時代表「已被預訂」與「房東主動封鎖」。
# 實測全體房源逐月已訂率呈**雙峰分布**:遠期月份約一半房源為 0%(日曆開著沒人訂)、
# 另一半為 100%(房東整月封鎖),直接取平均會得到 49% 這種不存在於任何真實房源的
# 中間值,再拿它當基準就會對每一間房發出「低於基準 49 個百分點」的假警示。
# 因此:①基準只採計「該月既非全空也非全滿」的房源;②該月可判讀房源比例低於
# MIN_ACTIVE_RATIO 時整月標為不可判讀;③月份天數過少(跨批爬取造成的首月碎片)亦排除。
MIN_ACTIVE_RATIO = 0.35   # 該月「日曆確實在營運」的房源比例低於此 → 不可判讀
MIN_MONTH_DAYS = 20       # 該月覆蓋天數少於此 → 視為碎片月,不列入比較
TRUST_MONTHS = 6          # 預設只比較未來 N 個月(超出者僅顯示、不下結論)


def available() -> bool:
    """檔期產物是否就緒。"""
    return METRICS_CSV.exists() and MARKET_CSV.exists()


@cache_data(show_spinner="載入未來檔期資料 …")
def load_metrics() -> pd.DataFrame:
    """每房源檔期指標(含 365 天訂房遮罩字串)。"""
    df = pd.read_csv(METRICS_CSV, dtype={"booked_mask": str})
    df["cal_start"] = pd.to_datetime(df["cal_start"], errors="coerce")
    return df


@cache_data(show_spinner=False)
def load_market() -> pd.DataFrame:
    """行政區 × 房型 × 月份 的市場已訂率基準。"""
    return pd.read_csv(MARKET_CSV)


@cache_data(show_spinner=False)
def healthy_metrics() -> pd.DataFrame:
    """排除全年封鎖 / 全年全空之異常房源(資料陷阱防護)。"""
    m = load_metrics()
    return m[(m["is_all_blocked"] == 0) & (m["is_all_open"] == 0)]


def get_listing(listing_id: int):
    """取單一房源檔期指標;找不到回傳 None。"""
    m = load_metrics()
    hit = m[m["listing_id"] == int(listing_id)]
    return None if hit.empty else hit.iloc[0]


def daily_frame(row) -> pd.DataFrame:
    """把訂房遮罩展開為逐日 DataFrame(date / booked / 週序 / 星期)。"""
    mask = str(row["booked_mask"])
    dates = pd.date_range(row["cal_start"], periods=len(mask), freq="D")
    d = pd.DataFrame({
        "date": dates,
        "booked": [int(ch) for ch in mask],
    })
    d["dow"] = d["date"].dt.dayofweek
    d["week"] = ((d["date"] - d["date"].min()).dt.days // 7).astype(int)
    d["month"] = d["date"].dt.to_period("M").astype(str)
    d["horizon"] = (d["date"] - d["date"].min()).dt.days
    return d


@cache_data(show_spinner=False)
def _listing_dims() -> pd.DataFrame:
    """房源的行政區與房型(供逐月基準分群用;只讀三欄,成本極低)。"""
    return pd.read_csv(LISTINGS_GZ, low_memory=False,
                       usecols=["id", "neighbourhood_cleansed", "room_type"])


@cache_data(show_spinner=False)
def global_cal_start() -> pd.Timestamp:
    """全體日曆的共同起算日 —— m1~m12 的月序是以它為基準算出來的。

    注意:各房源的 cal_start 可能相差 1~2 天(跨批爬取),若改用單一房源的
    cal_start 推算月份標籤,會與 m1~m12 的實際月份錯開一個月。
    """
    return pd.to_datetime(load_metrics()["cal_start"]).min()


@cache_data(show_spinner=False)
def monthly_baseline(district: str | None = None,
                     room_type: str | None = None) -> pd.DataFrame:
    """逐月市場基準 + 可判讀度(取代舊版直接平均的 _calendar_market.csv)。

    為什麼要重算:available='f' 同時含「已訂」與「房東封鎖」,遠期月份的
    房源不是 0%(開著沒人訂)就是 100%(整月封鎖),兩極各半。直接平均得到的
    ~49% 不對應任何真實房源,拿來當基準會製造假警示。
    這裡只採計「該月既非全空、也非全滿」= 日曆確實在營運的房源。

    回傳欄位:mi、月份、基準、可判讀比例、全空比例、全滿比例、樣本數
    """
    m = healthy_metrics()
    if district:
        dims = _listing_dims()
        sel = dims[dims["neighbourhood_cleansed"] == district]
        if room_type:
            narrow = sel[sel["room_type"] == room_type]
            if len(narrow) >= 30:
                sel = narrow
        sub = m[m["listing_id"].isin(set(sel["id"]))]
        if len(sub) >= 30:          # 樣本太少就退回全市,避免基準抖動
            m = sub
    g0 = global_cal_start()
    rows = []
    for i in range(1, 13):
        col = f"m{i}_rate"
        label = (g0 + pd.DateOffset(months=i - 1)).strftime("%Y-%m")
        s = m[col].dropna() if col in m.columns else pd.Series(dtype=float)
        if s.empty:
            rows.append({"mi": i, "月份": label, "基準": np.nan,
                         "可判讀比例": 0.0, "全空比例": np.nan,
                         "全滿比例": np.nan, "樣本數": 0})
            continue
        act = s[(s > 0.001) & (s < 0.999)]
        rows.append({
            "mi": i, "月份": label,
            "基準": float(act.mean()) if len(act) else np.nan,
            "可判讀比例": float(len(act) / len(s)),
            "全空比例": float((s <= 0.001).mean()),
            "全滿比例": float((s >= 0.999).mean()),
            "樣本數": int(len(act)),
        })
    return pd.DataFrame(rows)


def month_day_counts(row) -> dict:
    """本房源在 m1~m12 各月實際涵蓋幾天(用來剔除跨批爬取造成的碎片月)。"""
    d = daily_frame(row)
    g0 = global_cal_start()
    mi = ((d["date"].dt.year - g0.year) * 12
          + d["date"].dt.month - g0.month) + 1
    return mi.value_counts().to_dict()


def monthly_vs_market(row, district: str, room_type: str,
                      trust_months: int = TRUST_MONTHS) -> pd.DataFrame:
    """未來 12 個月:本房源已訂率 vs 同商圈同房型基準(含可判讀標記)。

    新增欄位
    --------
    可判讀   該月是否足以下結論(市場多數房源日曆在營運 + 本房源非全空/全滿 +
             月份天數足夠 + 在可信視窗內)
    不可判讀原因  未達標時的白話說明,供 UI 灰化與提示
    """
    base = monthly_baseline(district, room_type)
    days = month_day_counts(row)
    rows = []
    for _, b in base.iterrows():
        i = int(b["mi"])
        v = row.get(f"m{i}_rate")
        if v is None or (isinstance(v, float) and np.isnan(v)):
            continue
        v = float(v)
        nday = int(days.get(i, 0))
        why = ""
        if nday < MIN_MONTH_DAYS:
            why = f"此月僅涵蓋 {nday} 天(跨批爬取的碎片月)"
        elif i > trust_months:
            why = f"超出可信視窗(第 {i} 個月,遠期日曆多未開放)"
        elif b["可判讀比例"] < MIN_ACTIVE_RATIO:
            why = (f"市場僅 {b['可判讀比例']:.0%} 的房源此月日曆在營運"
                   f"(全空 {b['全空比例']:.0%}、全滿 {b['全滿比例']:.0%})")
        elif v <= 0.001:
            why = "本房源此月完全沒有訂單 —— 可能是日曆尚未開放,而非賣不掉"
        elif v >= 0.999:
            why = "本房源此月完全不可訂 —— 可能是房東主動封鎖"
        rows.append({"月份": b["月份"], "本房源": v, "同商圈基準": b["基準"],
                     "天數": nday, "可判讀": why == "", "不可判讀原因": why})
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["差距"] = out["本房源"] - out["同商圈基準"]
    return out


def gap_segments(row, min_len: int = 5, horizon: int = 90) -> pd.DataFrame:
    """未來 N 天內的連續空檔區段(可訂且無訂單)。"""
    d = daily_frame(row)
    d = d[d["horizon"] <= horizon]
    segs, run_start, run = [], None, 0
    for _, r in d.iterrows():
        if r["booked"] == 0:
            if run == 0:
                run_start = r["date"]
            run += 1
        else:
            if run >= min_len:
                segs.append({"起日": run_start,
                             "迄日": run_start + pd.Timedelta(days=run - 1),
                             "連續天數": run})
            run = 0
    if run >= min_len:
        segs.append({"起日": run_start,
                     "迄日": run_start + pd.Timedelta(days=run - 1),
                     "連續天數": run})
    return pd.DataFrame(segs)


def peer_revenue_curve(listings: pd.DataFrame, district: str, room_type: str,
                       n_bands: int = 8) -> pd.DataFrame:
    """營收最適定價:同商圈同房型的「價格帶 × 真實已訂天數 × 年營收估算」。

    營收估算 = 每晚價格 × 真實已訂天數(已訂天數來自 calendar,與價格為
    獨立資料源,故非 doc/03 §3.3 所述的循環恆等式)。
    """
    ok = healthy_metrics()[["listing_id", "booked_days", "booked_rate"]]
    peer = listings[(listings["neighbourhood_cleansed"] == district)
                    & (listings["room_type"] == room_type)]
    d = peer.merge(ok, left_on="id", right_on="listing_id", how="inner")
    if len(d) < 30:      # 樣本不足 → 放寬為同房型全市
        peer = listings[listings["room_type"] == room_type]
        d = peer.merge(ok, left_on="id", right_on="listing_id", how="inner")
    # price 可能為含符號字串(未經 data_loader 清理),此處自行轉數值
    d = d.copy()
    d["price"] = pd.to_numeric(
        d["price"].astype(str).str.replace(r"[$,]", "", regex=True),
        errors="coerce")
    d = d.dropna(subset=["price"])
    d = d[(d["price"] > 0) & (d["price"] < d["price"].quantile(.98))]
    if len(d) < 20:
        return pd.DataFrame()
    d["band"] = pd.qcut(d["price"], min(n_bands, d["price"].nunique()),
                        duplicates="drop")
    g = (d.groupby("band", observed=True)
         .agg(價格中位=("price", "median"),
              已訂天數=("booked_days", "mean"),
              已訂率=("booked_rate", "mean"),
              樣本數=("price", "size")).reset_index(drop=True))
    g["年營收估算"] = (g["價格中位"] * g["已訂天數"]).round(0)
    return g


def optimal_price(curve: pd.DataFrame) -> dict | None:
    """由營收曲線取最適價格帶。"""
    if curve is None or curve.empty:
        return None
    i = int(curve["年營收估算"].idxmax())
    r = curve.loc[i]
    return {"price": float(r["價格中位"]), "revenue": float(r["年營收估算"]),
            "booked_days": float(r["已訂天數"]), "n": int(r["樣本數"])}


def portfolio_summary(listings: pd.DataFrame) -> pd.DataFrame:
    """房型獲利分析:房型 × 行政區 的真實已訂率與營收估算。"""
    ok = healthy_metrics()[["listing_id", "booked_days", "booked_rate"]]
    d = listings.merge(ok, left_on="id", right_on="listing_id", how="inner").copy()
    d["price"] = pd.to_numeric(
        d["price"].astype(str).str.replace(r"[$,]", "", regex=True),
        errors="coerce")
    d = d.dropna(subset=["price"])
    d["年營收估算"] = d["price"] * d["booked_days"]
    return d
