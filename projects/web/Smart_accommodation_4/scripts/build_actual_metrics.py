# -*- coding: utf-8 -*-
"""build_actual_metrics.py — 實際入住指標預計算(reviews → 房源層級輕量產物)

為什麼要離線算
--------------
reviews_cleaned.csv.gz 有 23.9 萬列;Streamlit 端每次重算既慢又吃記憶體。
沿用 build_calendar_features.py 的慣例:重計算離線化,前端只讀輕量產物。
產出房源層級(非彙總)是刻意的 —— 才能支撐行政區下鑽與階段二的四象限。

計算口徑(2026-07-25 定案,詳見 docs/superpowers/plans/2026-07-25-預估vs實際對照.md)
------------------------------------------------------------------------
實際入住天數採 Inside Airbnb 官方公式,已在本專案資料上 100% 精確重現
(6,241/6,241 筆零誤差,用 number_of_reviews_ltm 反推 estimated_occupancy_l365d):

    入住天數 = min(窗口內評論數 × 2 × max(minimum_nights, 3), 上限)
    上限     = 窗口天數 × (255/365)   # 官方 70% 入住率上限,依窗口長度等比縮放
    × 2      = 官方假設僅 50% 住客會留評論

窗口:2025-09-30(listings 快照日)→ 2026-06-30(reviews 最後一筆),共 273 天。

排除規則(方案丁):窗口內零評論「且」前一年也零評論 → is_dormant=1(無經營跡象),
不計入任何平均。保留「前一年有評論、本窗口掛零」者 —— 那是真的萎縮停業,
恰恰是平台最該關心的一群,不能一起丟掉。

執行
----
    python -X utf8 scripts/build_actual_metrics.py

產出
----
data/_actual_metrics.csv   每房源一列(id/rev_window/occ_days/real_vac/
                           real_revenue_365/is_dormant)
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

DATA = ROOT / "data"

# 窗口:listings 快照日 → reviews 最後一筆
WINDOW_START = pd.Timestamp("2025-09-30")
WINDOW_END = pd.Timestamp("2026-06-30")

REVIEW_RATE = 0.5        # 官方假設:50% 住客留評論 → 天數要 ÷0.5(即 ×2)
MIN_STAY_FLOOR = 3       # 官方下限:平均住宿天數至少 3 晚
OCC_CAP_DAYS_365 = 255   # 官方上限:一年最多 255 晚(約 70%)


def log(m):
    print(f"[actual] {m}", flush=True)


def occupancy_days(reviews: pd.Series, minimum_nights: pd.Series,
                   window_days: int) -> pd.Series:
    """Inside Airbnb 入住天數公式;上限依窗口長度等比縮放。"""
    los = np.maximum(pd.to_numeric(minimum_nights, errors="coerce").fillna(
        MIN_STAY_FLOOR), MIN_STAY_FLOOR)
    cap = window_days * (OCC_CAP_DAYS_365 / 365)
    return np.minimum(reviews / REVIEW_RATE * los, cap)


def build(preds: pd.DataFrame, listings: pd.DataFrame,
          reviews: pd.DataFrame) -> pd.DataFrame:
    """組出房源層級的實際指標表。"""
    window_days = (WINDOW_END - WINDOW_START).days
    win = reviews[(reviews["date"] > WINDOW_START)
                  & (reviews["date"] <= WINDOW_END)]
    cnt = win.groupby("listing_id").size().rename("rev_window")

    d = (preds.merge(listings, on="id", how="left")
         .merge(cnt, left_on="id", right_index=True, how="left"))
    d["rev_window"] = d["rev_window"].fillna(0).astype(int)

    d["occ_days"] = occupancy_days(d["rev_window"], d["minimum_nights"],
                                   window_days).round(2)
    d["real_vac"] = (1.0 - d["occ_days"] / window_days).round(4)

    # 年營收年化到 365 天基準,才能與 est_annual_revenue(365天)同尺度比較
    price = pd.to_numeric(d["price"], errors="coerce").fillna(0.0)
    d["real_revenue_365"] = (price * d["occ_days"] * (365 / window_days)).round(2)

    # 方案丁:前後兩期都零評論 → 無經營跡象
    prev = pd.to_numeric(d["number_of_reviews_ltm"], errors="coerce").fillna(0)
    d["is_dormant"] = ((d["rev_window"] == 0) & (prev == 0)).astype(int)

    return d[["id", "rev_window", "occ_days", "real_vac",
              "real_revenue_365", "is_dormant"]]


def main():
    log(f"窗口 {WINDOW_START.date()} → {WINDOW_END.date()} "
        f"({(WINDOW_END - WINDOW_START).days} 天)")

    preds = pd.read_csv(DATA / "_predictions.csv", usecols=["id", "price"])
    listings = pd.read_csv(ROOT / "listings_cleaned.csv.gz", compression="gzip",
                           low_memory=False,
                           usecols=["id", "minimum_nights",
                                    "number_of_reviews_ltm"])
    reviews = pd.read_csv(DATA / "reviews_cleaned.csv.gz",
                          usecols=["listing_id", "date"], low_memory=False)
    reviews["date"] = pd.to_datetime(reviews["date"], errors="coerce")
    log(f"讀取:預測 {len(preds):,} 列 · 評論 {len(reviews):,} 列")

    out = build(preds, listings, reviews)
    out.to_csv(DATA / "_actual_metrics.csv", index=False, encoding="utf-8")

    n_dormant = int(out["is_dormant"].sum())
    keep = out[out["is_dormant"] == 0]
    log(f"_actual_metrics.csv: {len(out):,} 列 "
        f"({(DATA / '_actual_metrics.csv').stat().st_size / 1e3:.0f} KB)")
    log(f"無經營跡象(排除): {n_dormant:,} 間 · 納入計算: {len(keep):,} 間")
    log(f"實際空屋率均值: {keep['real_vac'].mean():.1%} · "
        f"高風險占比: {(keep['real_vac'] >= 0.6).mean():.1%}")
    log("完成")


if __name__ == "__main__":
    main()
