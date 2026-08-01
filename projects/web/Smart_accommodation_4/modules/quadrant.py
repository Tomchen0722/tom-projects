# -*- coding: utf-8 -*-
"""quadrant.py — 體質 × 檔期 四象限分類

解決的問題:模型等級(體質推估)與 calendar 已訂率(真實觀測)口徑不同,
並列呈現會出現「高風險卻訂滿」「安全卻空著」的表面矛盾。
實測 corr(模型機率, 實際90天空屋率) 僅 0.063,兩者本就不該互相取代。

判斷原則
--------
  近期行動看檔期(100% 真實觀測);長期投資看模型(AUC 0.632 的體質推估)。
  兩者衝突時,以檔期為準。

四象限
------
  🚨 高風險警訊  體質差 + 檔期空  → 最高優先
  👻 隱形危機  體質佳 + 檔期空  → 模型沒抓到,但檔期在流血
  ⚠️ 靠降價撐住 體質差 + 檔期滿  → 短期無虞,查是否賠本衝量
  ✅ 健康      體質佳 + 檔期滿  → 維持現狀
  ❔ 檔期資料不足  無檔期資料(calendar 與 listings 為不同批次,約 1,600 間無對照)

文案注意:第五類的名稱一律是「檔期資料不足」(design_tokens.STATUS_NO_DATA)。
原本 docstring 寫「資料不足」、label 寫「檔期資料不足」,兩者不一致。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from modules import design_tokens as T

# 檔期門檻(未來 90 天已訂率)
BOOKED_FULL = 0.50    # 訂房率 >= 50% 視為「檔期滿」
BOOKED_EMPTY = 0.20   # 訂房率 < 20% 視為「檔期真空」(在流血)
# 模型 A 預估空房率(vac_pred)門檻
VAC_HEALTHY = 0.35    # 健康需 vac_pred <= 35%
VAC_ALARM = 0.60      # green 但 vac_pred > 60% 直接升「真警報」


QUADRANTS = {
    "alarm": {"label": "🚨 高風險警訊", "color": "high", "priority": 1,
              "desc": "模型判定體質差(紅燈),未來檔期也幾乎沒人訂——兩邊都亮紅燈,最該優先處理",
              "action": "立即檢視定價與 LIME 痛點,同步啟動空檔促銷"},
    "hidden": {"label": "👻 隱形危機", "color": "medium", "priority": 2,
               "desc": "模型沒有強烈示警(綠燈、或僅黃燈觀察),但未來檔期幾乎沒訂單——"
                       "問題多在近期變動,不一定是房子本身",
               "action": "優先查近期變動:競品降價、季節性淡季、日曆設定或照片失效"},
    "discount": {"label": "⚠️ 靠降價撐住", "color": "accent", "priority": 3,
                 "desc": "房間幾乎都訂滿,但房子本身條件其實不算好——住滿不是因為受歡迎,而是價格壓得夠低。看起來生意好,實際可能不太賺錢",
                 "action": "檢查單價與 RevPAR(而非入住率),確認未賠本衝量"},
    "healthy": {"label": "✅ 健康", "color": "low", "priority": 4,
                "desc": "房子條件好,訂單也滿,一切正常",
                "action": "維持現狀,持續觀察同商圈行情"},
    "unknown": {"label": f"❔ {T.STATUS_NO_DATA}", "color": "muted", "priority": 5,
                "desc": "這批房源沒抓到訂房日曆資料(兩份資料爬取時間不同),無法判斷未來訂況",
                "action": "僅依模型體質評估判讀"},
}


def _is_nan(x) -> bool:
    return x is None or (isinstance(x, float) and np.isnan(x))


def classify_row(tier: str, booked_rate_d90, vac_pred=np.nan) -> str:
    """單筆分類。

    tier            模型等級(red/yellow/green),green 為體質佳。
    booked_rate_d90 未來 90 天真實已訂率(檔期實測);缺值歸 unknown。
    vac_pred        模型 A 預估空房率(0~1);缺值時保守處理(不升 alarm、不算 healthy)。

    規則(體質佳 = green):
      red/yellow + 訂房率 < 20%              -> alarm
      red/yellow + 訂房率 >= 20%             -> discount
      green + vac_pred > 60%                -> alarm(升級)
      green + 訂房率 >= 50% 且 vac_pred <= 35% -> healthy
      green + 其餘                          -> hidden
    """
    if _is_nan(booked_rate_d90):
        return "unknown"
    # 檔期空(訂房率 < 20%):只有體質「紅」才是真警報(名副其實:兩邊都亮紅燈)。
    # 黃(觀察)或綠 + 檔期空 → 隱形危機:模型沒強烈示警,但實際檔期在流血。
    # (2026-07-29:原本把黃也當「體質差」歸真警報,與「兩邊都紅」的文案矛盾,已收緊)
    if booked_rate_d90 < BOOKED_EMPTY:
        return "alarm" if tier == "red" else "hidden"
    # 檔期非空(≥20%):體質差(紅/黃)但訂得掉 → 靠降價撐住
    if tier in ("red", "yellow"):
        return "discount"
    # 體質佳(green)且檔期非空:訂滿且預估空房率低 → 健康;其餘 → 隱形危機
    v = np.nan if _is_nan(vac_pred) else float(vac_pred)
    if booked_rate_d90 >= BOOKED_FULL and not np.isnan(v) and v <= VAC_HEALTHY:
        return "healthy"
    return "hidden"


def annotate(df: pd.DataFrame, tier_col: str = "tier") -> pd.DataFrame:
    """為 DataFrame 加上象限欄位。需已含 booked_rate_d90(可為 NaN);
    另讀 vac_pred(缺欄則以 NaN 帶入,分類保守處理)。"""
    d = df.copy()
    if "booked_rate_d90" not in d.columns:
        d["booked_rate_d90"] = np.nan
    if "vac_pred" not in d.columns:
        d["vac_pred"] = np.nan
    d["quadrant"] = [classify_row(t, b, v)
                     for t, b, v in zip(d[tier_col], d["booked_rate_d90"],
                                        d["vac_pred"])]
    d["quadrant_label"] = d["quadrant"].map(lambda q: QUADRANTS[q]["label"])
    d["quadrant_priority"] = d["quadrant"].map(lambda q: QUADRANTS[q]["priority"])
    return d


def attach_calendar(df: pd.DataFrame, id_col: str = "id") -> pd.DataFrame:
    """併入 calendar 的真實已訂率與空檔指標(缺產物時回傳原表 + NaN 欄)。"""
    d = df.copy()
    try:
        from modules import calendar_analytics as ca
        if ca.available():
            cal = ca.healthy_metrics()[
                ["listing_id", "booked_rate", "booked_rate_d30",
                 "booked_rate_d90", "gap_days_30d", "gap_longest_30d"]]
            d = d.merge(cal, left_on=id_col, right_on="listing_id", how="left",
                        suffixes=("", "_cal"))
    except Exception:
        pass
    for c in ["booked_rate", "booked_rate_d30", "booked_rate_d90",
              "gap_days_30d", "gap_longest_30d"]:
        if c not in d.columns:
            d[c] = np.nan
    return d


def summary(df: pd.DataFrame) -> pd.DataFrame:
    """象限統計(依優先序排列)。"""
    g = (df.groupby("quadrant").size().rename("房源數").reset_index())
    g["象限"] = g["quadrant"].map(lambda q: QUADRANTS[q]["label"])
    g["優先序"] = g["quadrant"].map(lambda q: QUADRANTS[q]["priority"])
    g["說明"] = g["quadrant"].map(lambda q: QUADRANTS[q]["desc"])
    g["建議行動"] = g["quadrant"].map(lambda q: QUADRANTS[q]["action"])
    return g.sort_values("優先序")[["象限", "房源數", "說明", "建議行動"]]


# ═══════════════════════════════════════════════════════════════
# 已發生入住版(階段二,平台後台風險管理用)
# ═══════════════════════════════════════════════════════════════
# 與上方 classify_row 的差別只在第二軸的資料來源:
#   classify_row     第二軸 = booked_rate_d90(未來 90 天日曆已訂率) → 房東入口
#   classify_actual  第二軸 = 1 - real_vac  (已發生 273 天實際入住率) → 平台後台
# 兩者刻意獨立:平台方要判斷「這個房東過去是不是真的沒生意」,
# 房東自己則關心「接下來的檔期訂不訂得滿」。實測兩軸 corr 僅 0.146,
# 不可互相取代(見 docs/superpowers/plans/2026-07-25-預估vs實際對照.md)。
#
# 門檻沿用同一組 BOOKED_FULL/BOOKED_EMPTY —— 實測入住率分布套用後
# 五格皆無塌陷,不需另立常數,也避免兩邊各自漂移。

ACTUAL_QUADRANTS = {
    "alarm": {"label": "🚨 高風險警訊", "color": "high", "priority": 1,
              "desc": "模型判定體質差(紅燈)，過去九個月也幾乎沒有生意——兩邊都亮紅燈，"
                      "最該優先處理",
              "action": "立即檢視定價與 LIME 痛點，並確認房東是否仍有經營意願"},
    "hidden": {"label": "👻 隱形危機", "color": "medium", "priority": 2,
               "desc": "模型沒有強烈示警(綠燈、或僅黃燈觀察)，但過去九個月的實際入住"
                       "不到五成——模型沒抓到，生意已經在流失",
               "action": "優先查近期變動：競品降價、季節性淡季、日曆設定或照片失效"},
    "discount": {"label": "⚠️ 靠降價撐住", "color": "accent", "priority": 3,
                 "desc": "模型判定體質差，實際卻仍有一定入住——住得滿不一定是受歡迎，"
                         "可能是價格壓得夠低",
                 "action": "檢查單價與 RevPAR（而非入住率），確認未賠本衝量"},
    "healthy": {"label": "✅ 健康", "color": "low", "priority": 4,
                "desc": "模型判定體質良好，實際入住也達五成以上，一切正常",
                "action": "維持現狀，持續觀察同商圈行情"},
    "dormant": {"label": "❔ 無經營跡象", "color": "muted", "priority": 5,
                "desc": "這段期間與前一年都沒有任何評論——不是生意變差，"
                        "而是本來就沒在營業（停業／長租／掛著沒經營）",
                "action": "先確認房東是否仍有經營意願，再決定要不要投入輔導資源"},
    "unknown": {"label": f"❔ {T.STATUS_NO_DATA}", "color": "muted",
                "priority": 6,
                "desc": "缺少實際入住資料，無法判斷這段期間的真實經營狀況",
                "action": "僅依模型體質評估判讀"},
}

# 顯示順序(依 priority);圖表、篩選器一律吃這份,不各自硬寫一組 tuple。
ACTUAL_QUADRANT_ORDER = tuple(
    sorted(ACTUAL_QUADRANTS, key=lambda k: ACTUAL_QUADRANTS[k]["priority"]))


def classify_actual(tier: str, occupancy, is_dormant=0) -> str:
    """單筆分類(已發生入住版)。

    tier        模型等級(red/yellow/green),green 為體質佳。
    occupancy   已發生實際入住率(0~1,即 1 - real_vac);缺值歸 unknown。
    is_dormant  1 = 無經營跡象(前後兩期都零評論);優先於其他規則。

    規則:
      is_dormant=1                          -> dormant
      入住率缺值                             -> unknown
      red/yellow + 入住率 <  20%            -> alarm
      red/yellow + 入住率 >= 20%            -> discount
      green      + 入住率 >= 50%            -> healthy
      green      + 入住率 <  50%            -> hidden
    """
    # NaN 安全:is_dormant 缺值(左合併未命中 _actual_metrics)視為「非停業」,
    # 不能用 `int(is_dormant or 0)` —— NaN 在 Python 是 truthy,會直接讓 int() 爆掉。
    if not _is_nan(is_dormant) and int(is_dormant) == 1:
        return "dormant"
    if _is_nan(occupancy):
        return "unknown"
    occ = float(occupancy)
    # 入住率低(<20%):只有體質「紅」才是真警報;黃/綠 + 低入住 → 隱形危機(同 classify_row)
    if occ < BOOKED_EMPTY:
        return "alarm" if tier == "red" else "hidden"
    if tier in ("red", "yellow"):
        return "discount"
    return "healthy" if occ >= BOOKED_FULL else "hidden"


def annotate_actual(df: pd.DataFrame, tier_col: str = "tier") -> pd.DataFrame:
    """為 DataFrame 加上已發生版象限欄。需含 real_vac 與 is_dormant(缺欄歸 unknown)。"""
    d = df.copy()
    if "real_vac" not in d.columns:
        d["real_vac"] = np.nan
    if "is_dormant" not in d.columns:
        d["is_dormant"] = 0
    occ = 1.0 - pd.to_numeric(d["real_vac"], errors="coerce")
    d["quadrant"] = [classify_actual(t, o, z)
                     for t, o, z in zip(d[tier_col], occ, d["is_dormant"])]
    d["quadrant_label"] = d["quadrant"].map(lambda q: ACTUAL_QUADRANTS[q]["label"])
    d["quadrant_priority"] = d["quadrant"].map(
        lambda q: ACTUAL_QUADRANTS[q]["priority"])
    return d


def summary_actual(df: pd.DataFrame) -> pd.DataFrame:
    """已發生版象限統計(依優先序排列)。

    房東數採「名下至少 1 間屬該象限」,與 risk_cockpit_sections 的
    quadrant_host_counts/篩選器同一份口徑;一位房東可能橫跨多個象限,
    故房東數欄相加會大於實際房東總數,這是刻意的(不漏掉任何該處理的對象)。
    """
    g = (df.groupby("quadrant").size().rename("房源數").reset_index())
    hosts = df.groupby("quadrant")["host_id"].nunique().rename("房東數")
    g = g.merge(hosts, on="quadrant", how="left")
    g["象限"] = g["quadrant"].map(lambda q: ACTUAL_QUADRANTS[q]["label"])
    g["優先序"] = g["quadrant"].map(lambda q: ACTUAL_QUADRANTS[q]["priority"])
    g["說明"] = g["quadrant"].map(lambda q: ACTUAL_QUADRANTS[q]["desc"])
    g["建議行動"] = g["quadrant"].map(lambda q: ACTUAL_QUADRANTS[q]["action"])
    return g.sort_values("優先序")[["象限", "房源數", "房東數", "說明", "建議行動"]]
