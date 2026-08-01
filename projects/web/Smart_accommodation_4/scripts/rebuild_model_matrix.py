# -*- coding: utf-8 -*-
"""rebuild_model_matrix.py — 用新資料(v2)重算 dataset_multimodal 的 64 欄特徵矩陣

背景:資料換成 v2 後,原本由 01_data_build → 02_feature_eng 約 20 支研究腳本
產生的 dataset_multimodal.csv / _core_extra.csv 已與新 listings 對不上。那 20 支
腳本在此環境無法原樣重跑(照片下載、OSM、寫死路徑)。本腳本以「忠於特徵定義」
的方式,從已轉換的 listings_cleaned.csv.gz + POI + reviews + hotels 重算全部 64 欄,
供 train_backend_models_v90.py 直接使用(train=serve 同一份)。

公式全部取自原始腳本(見 build_dataset.py / add_taipei_poi_features / feature_engineering):
  price_pctl_nbhd  = groupby[nbhd,room_type]["price"].rank(pct=True)
  nbr_density_1km  = BallTree(haversine).query_radius(1km, count) − 1(扣自己)
  hotel_count_*    = BallTree(hotels).query_radius(r)
  POI count/dist   = 半徑內點數 / 最近點距離(欄名即定義的半徑)
  amenities_count  = amenities 逗號數 + 1
唯一例外:photo_design_sense 需照片 CV(6,241 張),此處以中性常數填(見 FILL_PHOTO),
模型該欄退化為常數(37 特徵中的 1 個),不影響其餘特徵。

執行:python -X utf8 scripts/rebuild_model_matrix.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.neighbors import BallTree

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
DATA = ROOT / "data"
EARTH = 6_371_000.0
FILL_PHOTO = 0.5           # photo_design_sense 中性填值(無法在此重算照片 CV)


def log(m):
    print(f"[rebuild] {m}", flush=True)


def _num(s):
    return pd.to_numeric(s, errors="coerce")


def _tree(df_pts):
    """對 (latitude, longitude) 點集建 haversine BallTree。"""
    return BallTree(np.radians(df_pts[["latitude", "longitude"]].to_numpy()),
                    metric="haversine")


def main():
    from modules.geo_utils import load_all_poi

    log("讀 listings_cleaned.csv.gz(v2 轉換後)…")
    L = pd.read_csv(DATA / "listings_cleaned.csv.gz", low_memory=False)
    L.columns = [c.lstrip("﻿") for c in L.columns]
    n = len(L)
    out = pd.DataFrame(index=L.index)

    # ── 識別 / 目標 ──
    out["id"] = L["id"].astype("int64")
    out["host_id"] = _num(L["host_id"])
    out["latitude"] = _num(L["latitude"])
    out["longitude"] = _num(L["longitude"])
    out["neighbourhood_cleansed"] = L["neighbourhood_cleansed"]
    out["room_type"] = L["room_type"]
    yv = (_num(L["availability_365"]) / 365).clip(0, 1)
    out["Y_vacancy"] = yv
    out["Y_high_risk"] = (yv >= 0.6).astype(int)

    # ── 結構化 ──
    out["accommodates"] = _num(L["accommodates"])
    out["bedrooms"] = _num(L["bedrooms"])
    out["beds"] = _num(L["beds"])
    out["bathrooms_count"] = _num(L.get("bathrooms_count", L.get("bathrooms")))
    bt = L.get("bathrooms_text", pd.Series("", index=L.index)).astype(str).str.lower()
    out["is_shared_bath"] = bt.str.contains("shared").astype(int)
    out["price"] = _num(L["price"])
    out["minimum_nights"] = _num(L["minimum_nights"])
    out["maximum_nights"] = _num(L["maximum_nights"])
    out["min_nights_avg_ntm"] = _num(L.get("min_nights_avg_ntm",
                                            L.get("minimum_nights_avg_ntm")))
    ib = L.get("instant_bookable")
    out["instant_bookable"] = (ib.astype(int) if ib is not None and ib.dtype == bool
                               else _num(ib).fillna(0).astype(int))
    out["self_checkin"] = _num(L.get("self_checkin")).fillna(0).astype(int)
    out["room_type_code"] = L["room_type"].astype("category").cat.codes
    out["neighbourhood_code"] = L["neighbourhood_cleansed"].astype("category").cat.codes

    # ── 評分 7 ──
    for c in ["review_scores_rating", "review_scores_accuracy",
              "review_scores_cleanliness", "review_scores_checkin",
              "review_scores_communication", "review_scores_location",
              "review_scores_value"]:
        out[c] = _num(L[c])

    # ── 競爭 5 ──
    def _amen_count(s):
        return s.fillna("[]").astype(str).str.count(",") + 1
    out["amenities_count"] = _amen_count(L["amenities"])
    g = [out["neighbourhood_cleansed"], out["room_type"]]
    out["price_pctl_nbhd"] = out.groupby(g)["price"].rank(pct=True)
    out["score_pctl_nbhd"] = out.groupby(g)["review_scores_rating"].rank(pct=True)
    out["amenities_vs_median"] = (out["amenities_count"] /
                                  out.groupby(g)["amenities_count"]
                                  .transform("median").replace(0, np.nan))
    coords = np.radians(L[["latitude", "longitude"]].to_numpy())
    tree = BallTree(coords, metric="haversine")
    r1 = 1000.0 / EARTH
    out["nbr_density_1km"] = tree.query_radius(coords, r=r1, count_only=True) - 1
    rt = L["room_type"].to_numpy()
    dens = np.zeros(n, int)
    for i, nb in enumerate(tree.query_radius(coords, r=r1)):
        dens[i] = int((rt[nb] == rt[i]).sum()) - 1
    out["nbr_density_same_type_1km"] = dens
    log("競爭特徵完成(百分位 / 密度)")

    # ── 房東 7 ──
    for c in ["host_acceptance_rate", "host_response_rate", "response_speed",
              "host_tenure_days"]:
        out[c] = _num(L.get(c))
    hs = L.get("host_is_superhost")
    out["host_is_superhost"] = (hs.astype(int) if hs is not None and hs.dtype == bool
                                else _num(hs).fillna(0).astype(int))
    out["host_listings_count"] = _num(L.get("calculated_host_listings_count"))
    out["calculated_host_listings_count"] = _num(L.get("calculated_host_listings_count"))

    # ── 經營用心度 4 ──
    out["desc_len"] = L.get("description", "").fillna("").astype(str).str.len()
    out["host_about_len"] = L.get("host_about", "").fillna("").astype(str).str.len()
    nov = L.get("neighborhood_overview", L.get("neighbourhood_overview", ""))
    out["neighborhood_overview_len"] = pd.Series(nov, index=L.index).fillna("").astype(str).str.len()

    # ── 地點 / 房間 6 ──
    hotels = pd.read_csv(DATA / "hotels_taipei_osm.csv")
    hotels.columns = [c.lstrip("﻿") for c in hotels.columns]
    htree = _tree(hotels.dropna(subset=["latitude", "longitude"]))
    out["hotel_count_1km"] = htree.query_radius(coords, r=1000.0 / EARTH, count_only=True)
    out["hotel_count_500m"] = htree.query_radius(coords, r=500.0 / EARTH, count_only=True)
    out["airbnb_hotel_supply_ratio"] = out["nbr_density_1km"] / (out["hotel_count_1km"] + 1)
    acc = out["accommodates"].clip(lower=1)
    out["price_per_person"] = out["price"] / acc
    out["price_per_bedroom"] = out["price"] / out["bedrooms"].clip(lower=1)
    out["beds_per_person"] = out["beds"] / acc

    # ── POI 11(欄名即定義的半徑;dist=最近點公尺, count=半徑內點數) ──
    poi = load_all_poi()

    def _poi_tree(key):
        p = poi[key].dropna(subset=["latitude", "longitude"])
        return _tree(p) if len(p) else None

    def _count(t, r_m):
        return (t.query_radius(coords, r=r_m / EARTH, count_only=True)
                if t is not None else np.zeros(n, int))

    def _dist(t):
        if t is None:
            return np.full(n, np.nan)
        d, _ = t.query(coords, k=1)
        return d[:, 0] * EARTH

    tmrt, tbus, tcvs = _poi_tree("mrt"), _poi_tree("bus"), _poi_tree("convenience")
    trest, tpark = _poi_tree("restaurant"), _poi_tree("park")
    tclin, tsch = _poi_tree("clinic"), _poi_tree("school")
    out["dist_to_nearest_mrt_m"] = _dist(tmrt)
    out["mrt_count_500m"] = _count(tmrt, 500)
    out["bus_stops_count_300m"] = _count(tbus, 300)
    out["bus_stops_count_500m"] = _count(tbus, 500)
    out["conv_stores_count_200m"] = _count(tcvs, 200)
    out["conv_stores_count_500m"] = _count(tcvs, 500)
    out["restaurants_count_500m"] = _count(trest, 500)
    out["dist_to_nearest_park_m"] = _dist(tpark)
    out["park_count_500m"] = _count(tpark, 500)
    out["dist_to_nearest_clinic_m"] = _dist(tclin)
    out["dist_to_nearest_school_m"] = _dist(tsch)
    log("POI 特徵完成")

    # ── NLP 3(以評論聚合;情感用 nlp_analysis 的規則詞典)──
    from modules.nlp_analysis import analyze_sentiment
    rv = pd.read_csv(DATA / "reviews_cleaned.csv.gz",
                     usecols=lambda c: c in ("listing_id", "comments",
                                             "cleaned_comments"))
    tcol = "cleaned_comments" if "cleaned_comments" in rv.columns else "comments"
    rv["_txt"] = rv[tcol].astype(str)
    rv["_len"] = rv["_txt"].str.len()
    # 情感:每則取複合分數(語言粗判 en/zh 交給 analyze_sentiment 內部)
    samp = rv.groupby("listing_id")
    agg = samp.agg(avg_review_length=("_len", "mean"),
                   n=("_len", "size")).reset_index()
    # 情感成本高 → 每房源抽樣至多 20 則平均
    sent = {}
    for lid, grp in rv.groupby("listing_id"):
        txts = grp["_txt"].head(20).tolist()
        sc = [analyze_sentiment(t)["compound"] if t and t != "nan" else 0.0
              for t in txts]
        sent[lid] = float(np.mean(sc)) if sc else 0.0
    agg["avg_review_sentiment"] = agg["listing_id"].map(sent)
    out = out.merge(agg[["listing_id", "avg_review_length", "avg_review_sentiment"]],
                    left_on="id", right_on="listing_id", how="left").drop(
        columns=["listing_id"])
    out["avg_review_length"] = out["avg_review_length"].fillna(0.0)
    out["avg_review_sentiment"] = out["avg_review_sentiment"].fillna(0.0)
    nrev = _num(L.get("number_of_reviews")).fillna(0)
    out["has_no_reviews"] = (nrev == 0).astype(int)
    log("NLP 特徵完成")

    # ── photo_design_sense:無法在此重算照片 CV → 中性常數填 ──
    out["photo_design_sense"] = FILL_PHOTO
    property_code = L["property_type"].astype("category").cat.codes

    # ── 對齊舊 dataset_multimodal 的 64 欄順序 ──
    order = pd.read_csv(DATA / "dataset_multimodal.csv", nrows=1).columns.tolist()
    for c in order:
        if c not in out.columns:
            out[c] = np.nan
    dm = out[order].copy()
    dm.to_csv(DATA / "dataset_multimodal.csv", index=False, encoding="utf-8-sig")
    log(f"dataset_multimodal.csv 重建:{len(dm):,} 列 × {dm.shape[1]} 欄")

    # ── _core_extra.csv(id, property_type_code, photo_design_sense)──
    core = pd.DataFrame({"id": out["id"],
                         "property_type_code": property_code.to_numpy(),
                         "photo_design_sense": FILL_PHOTO})
    core.to_csv(DATA / "_core_extra.csv", index=False, encoding="utf-8")
    log(f"_core_extra.csv 重建:{len(core):,} 列")
    log("完成 —— 可執行 train_backend_models_v90.py 重訓")


if __name__ == "__main__":
    main()
