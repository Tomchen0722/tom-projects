# -*- coding: utf-8 -*-
"""platform_analytics.py — Airbnb 平台方後台的純計算層。

刻意不 import streamlit:所有函式皆為 DataFrame in / DataFrame(或 dict) out,
可離線用 pytest 驗證;快取由呼叫端(platform_sections)負責。

營收口徑(doc/07 + 2026-07-23 v90 雙輸出 + 2026-07-25 市場總覽年化):
  預估年營收 = price x (1 - vac_pred_365) x 365   ← 年營收用 365 天空屋率
  平台收入   = 預估年營收 x 抽成率
  市場總覽分頁(market_kpis/district_health)的空屋率與高風險占比一律改用
  365 天口徑(vac_pred_365,見 vac_col()),與年營收基準一致;
  高風險採直接門檻法 risk_tier_365()(>=60%紅/>=35%黃),
  不同於風險管理分頁沿用的模型機率 tier 欄(P(90天空屋率>70%)>=門檻)。
  vac_pred_365 缺檔時全部回退 vac_pred。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

COMMISSION_DEFAULT = 0.15
COMMISSION_MIN = 0.03
COMMISSION_MAX = 0.20

DAYS_PER_YEAR = 365


def _num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce").fillna(0.0)


def vac_col(df: pd.DataFrame) -> str:
    """365 天空屋率欄名;舊資料無該欄時回退 90 天版 vac_pred。"""
    return "vac_pred_365" if "vac_pred_365" in df.columns else "vac_pred"


def risk_tier_365(vac: pd.Series) -> pd.Series:
    """依 365 天空屋率門檻分 red/yellow/green,門檻與房源卡風險環一致:
    >=0.60 紅、>=0.35 黃、<0.35 綠(design_tokens.vac_ring_tier 同一套規則)。
    """
    v = _num(vac)
    return pd.Series(
        np.select([v >= 0.60, v >= 0.35], ["red", "yellow"], default="green"),
        index=v.index)


def add_revenue_columns(df: pd.DataFrame, commission: float) -> pd.DataFrame:
    """回傳新 DataFrame,附加 est_annual_revenue 與 platform_revenue。

    年營收採 365 天空屋率(vac_pred_365);舊資料無該欄時回退 vac_pred。
    """
    out = df.copy()
    price = _num(out["price"])
    occ = (1.0 - _num(out[vac_col(out)])).clip(0.0, 1.0)
    out["est_annual_revenue"] = price * occ * DAYS_PER_YEAR
    out["platform_revenue"] = out["est_annual_revenue"] * float(commission)
    return out


def market_kpis(df: pd.DataFrame, commission: float) -> dict:
    """全市(或篩選範圍)KPI;空母體回傳全零而非例外。

    空屋率與高風險占比一律採 365 天口徑(vac_pred_365),
    與「預估房東年營收總額」的年化基準一致。
    """
    n = int(len(df))
    if n == 0:
        return {"n_listings": 0, "n_hosts": 0, "avg_vacancy": 0.0,
                "red_ratio": 0.0, "yellow_ratio": 0.0,
                "total_revenue": 0.0, "platform_revenue": 0.0}
    d = add_revenue_columns(df, commission)
    tier = risk_tier_365(d[vac_col(d)])
    total = float(d["est_annual_revenue"].sum())
    return {
        "n_listings": n,
        "n_hosts": int(d["host_id"].nunique()),
        "avg_vacancy": float(_num(d[vac_col(d)]).mean()),
        "red_ratio": float((tier == "red").mean()),
        "yellow_ratio": float((tier == "yellow").mean()),
        "total_revenue": total,
        "platform_revenue": total * float(commission),
    }


def district_health(df: pd.DataFrame, commission: float) -> pd.DataFrame:
    """行政區健康度:房源數、平均空屋率、高風險占比、平台收入、vs 全市差異。

    空屋率與高風險占比採 365 天口徑,與市場總覽頂部卡片一致。
    """
    cols = ["行政區", "房源數", "平均空屋率", "高風險占比",
            "預估平台收入", "空屋率vs全市"]
    if len(df) == 0:
        return pd.DataFrame(columns=cols)
    d = add_revenue_columns(df, commission)
    d["_vac"] = _num(d[vac_col(d)])
    d["_red"] = (risk_tier_365(d["_vac"]) == "red").astype(int)
    g = (d.groupby("neighbourhood_cleansed")
         .agg(房源數=("id", "size"),
              平均空屋率=("_vac", "mean"),
              高風險占比=("_red", "mean"),
              預估平台收入=("platform_revenue", "sum"))
         .reset_index()
         .rename(columns={"neighbourhood_cleansed": "行政區"}))
    g["空屋率vs全市"] = g["平均空屋率"] - float(d["_vac"].mean())
    return (g[cols].sort_values("高風險占比", ascending=False)
            .reset_index(drop=True))


def host_risk_summary(df: pd.DataFrame, commission: float) -> pd.DataFrame:
    """房東層級彙總:找出整批房源都在惡化的房東(高風險間數 → 占比 排序)。"""
    cols = ["host_id", "房源數", "高風險間數", "高風險占比",
            "平均風險分數", "預估年營收"]
    if len(df) == 0:
        return pd.DataFrame(columns=cols)
    d = add_revenue_columns(df, commission)
    d["_red"] = (d["tier"].astype(str) == "red").astype(int)
    d["_prob"] = _num(d["prob"])
    g = (d.groupby("host_id")
         .agg(房源數=("id", "size"),
              高風險間數=("_red", "sum"),
              高風險占比=("_red", "mean"),
              平均風險分數=("_prob", "mean"),
              預估年營收=("est_annual_revenue", "sum"))
         .reset_index())
    g["host_id"] = g["host_id"].astype(int)
    g["高風險間數"] = g["高風險間數"].astype(int)
    return (g[cols].sort_values(["高風險間數", "高風險占比"],
                                ascending=[False, False])
            .reset_index(drop=True))


def filter_scope(df: pd.DataFrame, districts=None, room_types=None) -> pd.DataFrame:
    """全域篩選;None 或空 list 代表該維度不篩選。"""
    out = df
    if districts:
        out = out[out["neighbourhood_cleansed"].isin(districts)]
    if room_types:
        out = out[out["room_type"].isin(room_types)]
    return out


def supply_demand_matrix(df: pd.DataFrame, min_listings: int = 15) -> pd.DataFrame:
    """行政區 x 房型 供需矩陣:需求強(空屋率低)且供給薄(房源少)= 招募缺口。"""
    cols = ["行政區", "房型", "房源數", "平均空屋率", "中位價格", "機會標籤"]
    if len(df) == 0:
        return pd.DataFrame(columns=cols)
    d = df.copy()
    d["_vac"] = _num(d["vac_pred"])
    d["_price"] = _num(d["price"])
    g = (d.groupby(["neighbourhood_cleansed", "room_type"])
         .agg(房源數=("id", "size"),
              平均空屋率=("_vac", "mean"),
              中位價格=("_price", "median"))
         .reset_index()
         .rename(columns={"neighbourhood_cleansed": "行政區",
                          "room_type": "房型"}))
    g = g[g["房源數"] >= int(min_listings)]
    if len(g) == 0:
        return pd.DataFrame(columns=cols)
    vac_mid = float(g["平均空屋率"].median())
    n_mid = float(g["房源數"].median())
    g["機會標籤"] = np.select(
        [(g["平均空屋率"] < vac_mid) & (g["房源數"] < n_mid),
         (g["平均空屋率"] > vac_mid) & (g["房源數"] > n_mid)],
        ["🟢 招募缺口", "🔴 供給飽和"], default="⚪ 一般")
    return g[cols].sort_values("平均空屋率").reset_index(drop=True)


# ═══════════════════════════════════════════════════════════════
# 營收與成長:同儕落差診斷(2026-07-25)
#
# 主張:「賣不掉的房源不是比較差的房源」。實測落後組與達標組在評分、
# 超讚房東比例、設施數、描述長度、最低入住天數上中位數幾乎相同
# (見 docs/superpowers/plans/2026-07-25-營收與成長敘事重構.md)。
#
# 因此本區塊一律只做「同儕比較與排序」,不做因果宣稱:
# 橫斷面資料無法支撐「降價 X% 會使空屋率降 Y%」這類推論。
# ═══════════════════════════════════════════════════════════════

PEER_MIN_DEFAULT = 15          # 同格樣本數低於此不比較(避免小樣本雜訊)
LAGGARD_GAP_DEFAULT = 0.20     # 落後定義:低於同儕中位已訂率 20 個百分點
LAGGARD_GAP_DAYS = round(LAGGARD_GAP_DEFAULT * DAYS_PER_YEAR)   # = 73 天

# 2026-07-25 二版:畫面一律改用「一年有幾天有人住」而不是已訂率百分比。
# 「2%」要換算才懂,「一年只有 7 天有人住」不用。百分比只留在計算層。

# 「房東改得動」的欄位。刻意排除 availability_365 / number_of_reviews_ltm:
# 那兩者本身就是「有沒有被訂走」的結果,拿來當原因是同義反覆。
CONTROLLABLE_SPEC = [
    ("整體評分", "review_scores_rating", "num"),
    ("清潔評分", "review_scores_cleanliness", "num"),
    ("超讚房東", "host_is_superhost", "flag"),
    ("即時預訂", "instant_bookable", "flag"),
    ("設施數", "amenities", "count"),
    ("描述字數", "description", "len"),
    ("最低入住天數", "minimum_nights", "num"),
    ("可住人數", "accommodates", "num"),
]


def peer_gap_table(df: pd.DataFrame, min_peers: int = PEER_MIN_DEFAULT,
                   gap_threshold: float = LAGGARD_GAP_DEFAULT) -> pd.DataFrame:
    """每間房源與「同行政區同房型」同儕中位已訂率的落差。

    呼叫端須先排除全年封鎖/全年全空房源(calendar_analytics.healthy_metrics),
    否則同儕中位會被那些非營業房源拉低。

    需要欄位:neighbourhood_cleansed / room_type / booked_rate
    附加欄位:同儕中位已訂率 / 同儕樣本數 / 落差 / 分組 / is_laggard
    同格樣本數 < min_peers 的房源會被剔除(比較基準不可靠)。
    """
    add = ["同儕中位已訂率", "同儕樣本數", "落差", "分組", "is_laggard"]
    need = ["neighbourhood_cleansed", "room_type", "booked_rate"]
    if len(df) == 0 or any(c not in df.columns for c in need):
        out = df.copy()
        for c in add:
            out[c] = pd.Series(dtype="float64" if c != "分組" else "object")
        return out

    d = df.copy()
    d["_rate"] = pd.to_numeric(d["booked_rate"], errors="coerce")
    d = d.dropna(subset=["_rate"])
    if len(d) == 0:
        for c in add:
            d[c] = pd.Series(dtype="float64" if c != "分組" else "object")
        return d.drop(columns=["_rate"])

    g = d.groupby(["neighbourhood_cleansed", "room_type"])["_rate"]
    d["同儕中位已訂率"] = g.transform("median")
    d["同儕樣本數"] = g.transform("size")
    d = d[d["同儕樣本數"] >= int(min_peers)].copy()
    d["落差"] = d["同儕中位已訂率"] - d["_rate"]
    d["is_laggard"] = d["落差"] > float(gap_threshold)
    d["分組"] = np.where(d["is_laggard"], "落後",
                         np.where(d["落差"] <= 0, "達標", "接近"))
    # 給畫面用的天數版:一年 365 天裡有幾天有人住,不需換算就懂
    d["自己有人住天數"] = d["_rate"] * DAYS_PER_YEAR
    d["鄰居有人住天數"] = d["同儕中位已訂率"] * DAYS_PER_YEAR
    d["少住天數"] = d["落差"] * DAYS_PER_YEAR
    return d.drop(columns=["_rate"]).reset_index(drop=True)


def _flag(s: pd.Series) -> pd.Series:
    """Airbnb 的 t/f 欄位轉 1/0。"""
    return pd.to_numeric(
        s.map({"t": 1, "f": 0, True: 1, False: 0}).where(
            s.isin(["t", "f", True, False]), s), errors="coerce")


def _stat(d: pd.DataFrame, col: str, kind: str):
    """依欄位型態取代表值:num/len/count 取中位數,flag 取比例。"""
    if col not in d.columns or len(d) == 0:
        return np.nan
    if kind == "flag":
        v = _flag(d[col])
        return float(v.mean()) if v.notna().any() else np.nan
    if kind == "len":
        v = d[col].astype(str).str.len()
    elif kind == "count":
        v = d[col].astype(str).str.count(",") + 1
    else:
        v = pd.to_numeric(d[col].astype(str).str.rstrip("%"), errors="coerce")
    return float(v.median()) if v.notna().any() else np.nan


def controllable_compare(df: pd.DataFrame, spec=None) -> pd.DataFrame:
    """落後組 vs 達標組在「房東改得動」欄位上的比對表。

    這張表的重點是「兩欄幾乎一樣」——用來證明落後不是品質造成的,
    因此頁面不該端出品質輔導處方。df 需先過 peer_gap_table()。
    回傳欄位:項目 / 落後組 / 達標組 / 相對差 / 型態
    """
    spec = spec or CONTROLLABLE_SPEC
    cols = ["項目", "落後組", "達標組", "相對差", "型態"]
    if len(df) == 0 or "分組" not in df.columns:
        return pd.DataFrame(columns=cols)
    lag = df[df["分組"] == "落後"]
    ok = df[df["分組"] == "達標"]
    rows = []
    for label, col, kind in spec:
        a, b = _stat(lag, col, kind), _stat(ok, col, kind)
        if pd.isna(a) and pd.isna(b):
            continue
        if kind == "flag":
            diff = (a - b) if not (pd.isna(a) or pd.isna(b)) else np.nan
        else:
            diff = ((a - b) / b) if b else np.nan
        rows.append({"項目": label, "落後組": a, "達標組": b,
                     "相對差": diff, "型態": kind})
    return pd.DataFrame(rows, columns=cols)


def annotate_model_view(df: pd.DataFrame, pred: pd.DataFrame) -> pd.DataFrame:
    """幫落後名單標上「風險模型怎麼看這間房子」。

    兩套系統量的東西不同,這正是重點:
      - 風險模型(pred 的 tier/prob)吃的是**靜態結構特徵**(房型密度、床數、
        臥室數…),評估的是「這間房子的條件適不適合經營」;
      - 落後名單(df 的 少住天數)吃的是**真實訂房日曆**,量的是「實際上有沒有
        人住」。
    條件很好但實際上沒人訂的房子,風險模型看不出來 —— 那批就是「隱形危機」,
    也是兩套系統都會漏掉的一群。

    回傳附加:模型層級(red/yellow/green/未評估) / 模型風險分數 / 診斷分類。
    診斷分類三值:
      "隱形危機" = 模型說安全(green),實際卻嚴重滯銷 → 模型幫不上忙,要另尋原因
      "模型有抓到" = 模型也判 red/yellow,兩套系統一致
      "未評估"     = 不在風險模型母體內(見 calendar/listings 31% 落差)
    """
    add = ["模型層級", "模型風險分數", "診斷分類"]
    if len(df) == 0:
        out = df.copy()
        for c in add:
            out[c] = pd.Series(dtype="object")
        return out
    if pred is None or len(pred) == 0 or "id" not in df.columns:
        out = df.copy()
        out["模型層級"] = "未評估"
        out["模型風險分數"] = np.nan
        out["診斷分類"] = "未評估"
        return out

    keep = [c for c in ["id", "tier", "prob"] if c in pred.columns]
    out = df.merge(pred[keep].drop_duplicates("id"), on="id", how="left")
    tier = out["tier"].astype(str) if "tier" in out.columns else pd.Series(
        "nan", index=out.index)
    out["模型層級"] = np.where(tier.isin(["red", "yellow", "green"]),
                               tier, "未評估")
    out["模型風險分數"] = (pd.to_numeric(out["prob"], errors="coerce")
                           if "prob" in out.columns else np.nan)
    out["診斷分類"] = np.select(
        [out["模型層級"] == "green",
         out["模型層級"].isin(["red", "yellow"])],
        ["隱形危機", "模型有抓到"], default="未評估")
    return out.drop(columns=[c for c in ["tier", "prob"] if c in out.columns])


def model_coverage_cutoff(df: pd.DataFrame, pred: pd.DataFrame):
    """風險模型訓練資料的時間切點 = 模型母體內最晚的「房東加入日」。

    2026-07-25 查證:切點為 2024-09-30,而未納入模型的 392 間房源最早
    host_since 是 2024-10-11 —— 兩邊**完全不重疊(0/392)**,所以「未評估」
    的成因就是訓練資料的時間切點,不是資料品質不足。

    刻意動態計算而非寫死日期:模型重訓後這個切點會自動跟著更新。
    缺欄位/缺預測檔時回 None,呼叫端要能接受「講不出原因」。
    """
    if (df is None or len(df) == 0 or pred is None or len(pred) == 0
            or "host_since" not in df.columns or "id" not in df.columns
            or "id" not in pred.columns):
        return None
    hs = pd.to_datetime(df.loc[df["id"].isin(set(pred["id"])), "host_since"],
                        errors="coerce")
    return None if hs.notna().sum() == 0 else hs.max()


def explain_unevaluated(df: pd.DataFrame, cutoff=None) -> pd.DataFrame:
    """對「未評估」的房源逐筆標上原因(短句,要塞進表格欄位)。

    只有「未評估」的列會有值,其餘回空字串 —— 已被模型評估的房源不需要解釋。
    """
    if len(df) == 0:
        out = df.copy()
        out["未評估原因"] = pd.Series(dtype="object")
        return out

    d = df.copy()
    is_none = (d["診斷分類"] == "未評估" if "診斷分類" in d.columns
               else pd.Series(False, index=d.index))
    hs = (pd.to_datetime(d["host_since"], errors="coerce")
          if "host_since" in d.columns else pd.Series(pd.NaT, index=d.index))

    late = is_none & hs.notna() & (
        (hs > cutoff) if cutoff is not None else False)
    d["未評估原因"] = np.where(
        late,
        "房東 " + hs.dt.strftime("%Y-%m").fillna("") + " 才加入，晚於模型訓練資料",
        np.where(is_none, "不在模型的訓練資料裡", ""))
    return d


# 「隱形危機」建議作法的判定門檻。這些不是模型算出來的,是依實測差異訂的
# 規則,每一條都對應一個「資料上看得到、平台做得到」的動作。
BLIND_PRICE_HIGH = 1.15        # 價格 / 同區同房型中位價,高於此視為訂價偏高
BLIND_DEAD_DAYS = 30           # 一年有人住天數低於此,視為幾乎沒在賣
BLIND_MIN_NIGHTS_LONG = 7      # 最低入住天數高於此,視為門檻擋客


def suggest_actions(df: pd.DataFrame, peer_price: pd.DataFrame | None = None
                    ) -> pd.DataFrame:
    """對「隱形危機」房源給出建議作法(規則式,不是模型預測)。

    為什麼需要這個:風險模型對這批房源給不出可行動的理由 —— 它說「安全」,
    它的歸因也只會列出地段好、床數夠這類靜態優點,拿去寫輔導信等於告訴房東
    「你這間很棒」,方向是反的。所以這裡改用**實際訂房行為 + 同儕比價**
    重新推建議。

    實測支撐(2026-07-25,489 間隱形危機 vs 601 間模型有抓到):
      - 隱形危機的評分 4.88、超讚房東 66%(vs 44%)—— 品質輔導無效,別再寄
      - 但價格 / 同儕中位 = 1.10(vs 1.03)—— 訂價偏高是少數看得到的差異
      - 近 12 月評論中位 11 則(vs 1 則)—— 這批房子是「還活著但賣不動」,
        不是已經停業,所以聯繫得上、值得處理

    回傳附加「建議作法」欄。規則依序判定,取第一個命中(愈明確的排愈前面)。
    非「隱形危機」的列一律回空字串:模型有抓到的那批走既有 LIME 輔導信流程。
    """
    if len(df) == 0:
        out = df.copy()
        out["建議作法"] = pd.Series(dtype="object")
        return out

    d = df.copy()
    price = _num(d["price"]) if "price" in d.columns else pd.Series(
        np.nan, index=d.index)
    if peer_price is not None and len(peer_price):
        d = d.merge(peer_price, on=["neighbourhood_cleansed", "room_type"],
                    how="left")
        rel = _num(d["price"]) / pd.to_numeric(d["peer_price"], errors="coerce")
        d = d.drop(columns=["peer_price"])
    else:
        rel = pd.Series(np.nan, index=d.index)
    days_in = (pd.to_numeric(d["自己有人住天數"], errors="coerce")
               if "自己有人住天數" in d.columns
               else pd.Series(np.nan, index=d.index))
    min_n = (pd.to_numeric(d["minimum_nights"], errors="coerce")
             if "minimum_nights" in d.columns
             else pd.Series(np.nan, index=d.index))
    is_blind = (d["診斷分類"] == "隱形危機" if "診斷分類" in d.columns
                else pd.Series(False, index=d.index))

    d["建議作法"] = np.select(
        [is_blind & (days_in < BLIND_DEAD_DAYS),
         is_blind & (rel > BLIND_PRICE_HIGH),
         is_blind & (min_n > BLIND_MIN_NIGHTS_LONG),
         is_blind],
        ["先問房東還想不想做 —— 一年幾乎沒開張，可能已經轉長租或自住，"
         "先確認意願再談別的",
         "訂價比同區同型高一成以上 —— 建議請房東測試調降價格，"
         "或由平台提供限時折扣券",
         f"最低入住天數超過 {BLIND_MIN_NIGHTS_LONG} 晚，短住客訂不了 —— "
         "建議放寬門檻",
         "條件與訂價都正常卻訂不到 —— 這批最可能是曝光問題，"
         "建議納入搜尋加權或廣告投放測試"],
        default="")
    return d


def uplift_ranking(df: pd.DataFrame, commission: float = COMMISSION_DEFAULT,
                   days: int = DAYS_PER_YEAR) -> pd.DataFrame:
    """落後房源排序:每間房子比同區同型的鄰居,一年讓平台少收多少錢。

    一年少賺 = 每晚價格 x 少住天數 x 抽成率

    這是<b>描述</b>不是<b>處方</b>:它陳述「這間房子和鄰居差多少錢」,
    不宣稱「做了什麼就能補回來」。舊版的「保守可補回抽成」要先解釋
    shrink 係數才看得懂,對非資料背景的觀眾是負擔,已移除該概念。
    附加 累積金額 / 累積占比 / 名次(依一年少賺由大到小)。df 需先過 peer_gap_table()。
    """
    cols = ["一年少賺", "累積金額", "累積占比", "名次"]
    if len(df) == 0 or "is_laggard" not in df.columns:
        out = df.copy()
        for c in cols:
            out[c] = pd.Series(dtype="float64")
        return out
    d = df[df["is_laggard"].fillna(False)].copy()
    if len(d) == 0:
        for c in cols:
            d[c] = pd.Series(dtype="float64")
        return d
    d["一年少賺"] = (_num(d["price"]) * _num(d["落差"])
                     * int(days) * float(commission))
    d = d.sort_values("一年少賺", ascending=False).reset_index(drop=True)
    d["累積金額"] = d["一年少賺"].cumsum()
    total = float(d["一年少賺"].sum())
    d["累積占比"] = d["累積金額"] / total if total else 0.0
    d["名次"] = np.arange(1, len(d) + 1)
    return d
