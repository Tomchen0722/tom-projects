# -*- coding: utf-8 -*-
"""adapt_clean_data.py — 把重新清洗的 *_clean 檔轉回專案原本的檔名與 schema

背景:2026-07 資料重新清洗後,data/ 內的原始檔改成 `*_clean` 命名,且欄位結構
與舊版不同。專案的載入器與離線腳本都寫死舊檔名/舊欄位。為了「只換資料、不動
架構」,本腳本做一次性轉換:讀新 *_clean 檔 → 寫出舊檔名+舊 schema 的檔,
既有程式一行都不用改。

原則
----
* 不覆寫、不刪除任何 *_clean 原始檔(只新增舊命名檔並存)。
* 缺的欄位(如 host_acceptance_rate)一律補 NaN,交由後續重訓處理。
* 座標/文字檔的欄位順序與編碼,對齊各 loader 的實際解析方式(見 geo_utils)。

執行:python -X utf8 scripts/adapt_clean_data.py
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"


def log(m):
    print(f"[adapt] {m}", flush=True)


# ── 1. Airbnb listings(改用 listings_v2_clean.csv.gz;含完整房東特徵) ──
# 回覆時間文字 → 回覆速度分級(1 最快 … 4 最慢;unknown/缺 → NaN)
_RESP_SPEED = {
    "within an hour": 1, "within a few hours": 2,
    "within a day": 3, "a few days or more": 4,
}


def adapt_listings():
    src = DATA / "listings_v2_clean.csv.gz"
    df = pd.read_csv(src, low_memory=False)
    df.columns = [c.lstrip("﻿") for c in df.columns]

    # bathrooms_count:v2 已有;若只有 bathrooms 則補
    if "bathrooms_count" not in df.columns and "bathrooms" in df.columns:
        df["bathrooms_count"] = pd.to_numeric(df["bathrooms"], errors="coerce")
    if "minimum_nights_avg_ntm" in df.columns:
        df["min_nights_avg_ntm"] = pd.to_numeric(
            df["minimum_nights_avg_ntm"], errors="coerce")

    # host_tenure_days = last_scraped − host_since(天)
    hs = pd.to_datetime(df.get("host_since"), errors="coerce")
    ref = pd.to_datetime(df.get("last_scraped"), errors="coerce")
    ref = ref.fillna(pd.Timestamp("2025-09-30"))
    df["host_tenure_days"] = (ref - hs).dt.days

    # response_speed:由 host_response_time 文字映成 1~4
    if "response_speed" not in df.columns:
        df["response_speed"] = (df.get("host_response_time")
                                .astype(str).str.strip().str.lower()
                                .map(_RESP_SPEED))

    # instant_bookable / host_is_superhost:布林 → 0/1
    for col in ["instant_bookable", "host_is_superhost",
                "host_has_profile_pic", "host_identity_verified"]:
        if col in df.columns and df[col].dtype == bool:
            df[col] = df[col].astype(int)

    # self_checkin 由 amenities 推(v2 無此欄)
    _am = df.get("amenities", pd.Series("", index=df.index)).astype(str).str.lower()
    df["self_checkin"] = _am.str.contains(
        "self check-in|keypad|lockbox|smart lock", regex=True).astype(int)

    out = DATA / "listings_cleaned.csv.gz"
    df.to_csv(out, index=False, compression="gzip", encoding="utf-8")
    log(f"listings_cleaned.csv.gz ← listings_clean.csv  ({len(df):,} 列, "
        f"{df.shape[1]} 欄)")

    # neighbourhoods.csv(Inside Airbnb 格式:neighbourhood_group, neighbourhood)
    nb = pd.DataFrame({
        "neighbourhood_group": np.nan,
        "neighbourhood": sorted(df["neighbourhood_cleansed"].dropna().unique()),
    })
    nb.to_csv(DATA / "neighbourhoods.csv", index=False, encoding="utf-8")
    log(f"neighbourhoods.csv  ({len(nb)} 區)")


# ── 2a. reviews(直接 byte 複製改名) ────────────────────────────
# 不用 read→to_csv round-trip:comments 內含換行/逗號時重寫會欄位錯位,
# 導致 listing_id 變成 object,後續 build_absa 的 merge 會壞。來源 gz 本身
# 欄位/型別已正確,直接複製即可。
def adapt_reviews():
    shutil.copyfile(DATA / "reviews_clean.csv.gz", DATA / "reviews_cleaned.csv.gz")
    log("reviews_cleaned.csv.gz ← reviews_clean.csv.gz  (複製)")


# ── 2b. calendar(available 布林 → 't'/'f' 字串) ────────────────
# 新清洗把 available 存成布林 True/False,但 build_calendar_features 沿用
# Inside Airbnb 原始格式,用 available.astype(str).str.lower()=='f' 判斷「不可訂」。
# 對 True/False 這個判斷永遠不成立 → 每間房都被當成全空(booked_rate=0)。
# 因此在資料層轉回 't'(可訂)/ 'f'(不可訂),不動 build_calendar_features。
# calendar 只有 listing_id/date/available/min/max,無自由文字,to_csv 安全。
def adapt_calendar():
    c = pd.read_csv(DATA / "calendar_clean.csv.gz")
    av = c["available"]
    if av.dtype == bool:
        c["available"] = np.where(av, "t", "f")
    else:
        s = av.astype(str).str.strip().str.lower()
        c["available"] = np.where(s.isin(["true", "t", "1", "yes"]), "t", "f")
    c.to_csv(DATA / "calendar.csv.gz", index=False, compression="gzip",
             encoding="utf-8")
    vc = pd.Series(c["available"]).value_counts().to_dict()
    log(f"calendar.csv.gz ← calendar_clean.csv.gz  ({len(c):,} 列, "
        f"available 轉碼 {vc})")


# ── 3. 跨平台:591 / ddroom / Booking(hotel) ───────────────────
def adapt_platforms():
    # 591、ddroom:欄位已對齊 load_591 / load_ddroom,改名即可
    for new, old in [("591_clean.csv", "591_taipei_20260718_124800_rooms.csv"),
                     ("ddroom_clean.csv", "ddroom_taipei_by_rooms.csv")]:
        df = pd.read_csv(DATA / new)
        df.columns = [c.lstrip("﻿") for c in df.columns]
        df.to_csv(DATA / old, index=False, encoding="utf-8-sig")
        log(f"{old} ← {new}  ({len(df):,} 列)")

    # Booking:hotel_clean.csv 是 Booking 等價資料,補缺的「房間設施」空欄
    h = pd.read_csv(DATA / "hotel_clean.csv")
    h.columns = [c.lstrip("﻿") for c in h.columns]
    if "房間設施" not in h.columns:
        h["房間設施"] = ""
    h.to_csv(DATA / "taipei_rooms_only_v14_20260718.csv",
             index=False, encoding="utf-8-sig")
    log(f"taipei_rooms_only_v14_20260718.csv ← hotel_clean.csv  ({len(h):,} 列)")


# ── 4. POI(座標點資料) ─────────────────────────────────────────
# 2026-07-28 起 geo_utils 直接讀清洗版 *_clean.csv(mrt/bus/conbini/restaurants/
# school/clinics/parks),不再需要轉回舊命名,故此處只保留 hotels_taipei_osm。
def adapt_poi():
    # 供特徵工程用的 OSM 旅宿點(hotel_count_*):由 hotel_clean 座標產生
    h = pd.read_csv(DATA / "hotel_clean.csv")
    h.columns = [c.lstrip("﻿") for c in h.columns]
    osm = h[["飯店名稱", "緯度", "經度"]].rename(
        columns={"飯店名稱": "name", "緯度": "latitude", "經度": "longitude"})
    osm.to_csv(DATA / "hotels_taipei_osm.csv", index=False, encoding="utf-8-sig")
    log(f"hotels_taipei_osm.csv ← hotel_clean.csv  ({len(osm):,} 點)")


def main():
    log("開始轉換 …")
    adapt_listings()
    adapt_reviews()
    adapt_calendar()
    adapt_platforms()
    adapt_poi()
    log("完成 —— 舊命名檔已與 *_clean 並存,既有程式無需修改。")


if __name__ == "__main__":
    sys.exit(main())
