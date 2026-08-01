# -*- coding: utf-8 -*-
"""listing_registration.py — 房源登錄頁(房東入口第一個分頁)

提供房東「把房源刊登到第三方平台」前的登錄表單:填寫房源與房東資訊、上傳封面
照片,送出後即時套用平台採用的模型,算出「預估空屋率風險分數 + 警報等級」,
並給出一個「信心指數」——量化這個分數有多可信。

設計重點
--------
* 表單欄位對映模型實際使用的 37 個特徵中「房東登錄時可提供」的部分;
  新房源沒有的資訊(尤其是住客評分,因為還沒有評論)以同商圈同房型中位數
  代填,並在信心指數中扣分。
* 座標→競爭特徵(價格百分位、周邊密度)即時由現有房源分佈計算,與訓練口徑一致。
* 信心指數 = 模型可靠度 × 資料完整度 × 判斷明確度(見 confidence_index)。
* 「刊登」為模擬(平台無公開寫入 API),送出後產生可下載的房源摘要。
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.neighbors import BallTree

from modules.ui_components import P

DATA = Path(__file__).resolve().parent.parent / "data"
EARTH = 6_371_000.0

# 表單設施選項(與 market_data 的標準設施一致,勾選數 → amenities_count 參考)
AMENITY_OPTIONS = ["WiFi", "冷氣", "洗衣機", "冰箱", "電視", "廚房/可開伙",
                   "熱水器", "電梯", "車位", "陽台", "浴缸", "自助入住",
                   "工作空間", "飲水機"]
ROOM_TYPES = {"整棟/整層(Entire home/apt)": "Entire home/apt",
              "私人房間(Private room)": "Private room",
              "旅館式房間(Hotel room)": "Hotel room",
              "共享房間(Shared room)": "Shared room"}
RESP_SPEED = {"一小時內": 1, "數小時內": 2, "一天內": 3, "一天以上": 4}


@st.cache_resource(show_spinner=False)
def _reference():
    """訓練口徑的參考資料:code 對映、分群分佈、座標密度樹。"""
    dm = pd.read_csv(DATA / "dataset_multimodal.csv", low_memory=False)
    rt_code = (dm.drop_duplicates("room_type")
               .set_index("room_type")["room_type_code"].to_dict())
    nb_code = (dm.drop_duplicates("neighbourhood_cleansed")
               .set_index("neighbourhood_cleansed")["neighbourhood_code"].to_dict())
    # property_type → code(由 listings + _core_extra 併)
    try:
        li = pd.read_csv(DATA / "listings_cleaned.csv.gz",
                         usecols=["id", "property_type"], low_memory=False)
        ce = pd.read_csv(DATA / "_core_extra.csv",
                         usecols=["id", "property_type_code"])
        pj = li.merge(ce, on="id").drop_duplicates("property_type")
        pt_code = pj.set_index("property_type")["property_type_code"].to_dict()
    except Exception:
        pt_code = {}
    # 各行政區中心點(表單預設座標)
    cent = (dm.groupby("neighbourhood_cleansed")[["latitude", "longitude"]]
            .mean().to_dict("index"))
    tree = BallTree(np.radians(dm[["latitude", "longitude"]].to_numpy()),
                    metric="haversine")
    return {"dm": dm, "rt_code": rt_code, "nb_code": nb_code, "pt_code": pt_code,
            "centroid": cent, "tree": tree,
            "rt_arr": dm["room_type"].to_numpy(),
            "score_median": float(dm["review_scores_rating"].median()),
            "amen_median": float(dm["amenities_count"].median())}


def _competitive(ref, district, room_type, price, amen_count, lat, lon):
    """由現有房源分佈算競爭特徵(與 build_dataset 同定義)。"""
    dm = ref["dm"]
    grp = dm[(dm["neighbourhood_cleansed"] == district)
             & (dm["room_type"] == room_type)]
    if len(grp) < 5:                       # 樣本不足退回同行政區
        grp = dm[dm["neighbourhood_cleansed"] == district]
    price_pctl = float((grp["price"] < price).mean()) if len(grp) else 0.5
    amen_med = float(grp["amenities_count"].median()) if len(grp) else ref["amen_median"]
    amen_vs = amen_count / amen_med if amen_med else 1.0
    score_med = float(grp["review_scores_rating"].median()) if len(grp) \
        else ref["score_median"]
    # 密度:1km 內現有房源數 / 同房型數
    idx = ref["tree"].query_radius(np.radians([[lat, lon]]), r=1000.0 / EARTH)[0]
    dens = int(len(idx))
    dens_same = int((ref["rt_arr"][idx] == room_type).sum())
    return {"price_pctl_nbhd": price_pctl, "amenities_vs_median": amen_vs,
            "nbr_density_1km": dens, "nbr_density_same_type_1km": dens_same,
            "score_median": score_med}


def _build_row(ref, f) -> dict:
    """把表單值 f 組成模型可讀的特徵列(dict)。未知評分以同群中位補。"""
    comp = _competitive(ref, f["district"], f["room_type"], f["price"],
                        f["amen_count"], f["lat"], f["lon"])
    sm = comp["score_median"]
    row = {
        "price": f["price"], "accommodates": f["accommodates"],
        "bedrooms": f["bedrooms"], "beds": f["beds"],
        "bathrooms_count": f["bathrooms"], "minimum_nights": f["min_nights"],
        "maximum_nights": f["max_nights"], "min_nights_avg_ntm": f["min_nights"],
        "amenities_count": f["amen_count"], "instant_bookable": int(f["instant"]),
        "self_checkin": int(f["self_checkin"]),
        "room_type_code": ref["rt_code"].get(f["room_type"], 0),
        "property_type_code": ref["pt_code"].get(f["property_type"], 0),
        "neighbourhood_code": ref["nb_code"].get(f["district"], 0),
        "latitude": f["lat"], "longitude": f["lon"],
        # 房東身分(冷啟動變體會忽略這些)
        "host_is_superhost": int(f["superhost"]),
        "host_response_rate": f["resp_rate"], "host_acceptance_rate": f["acc_rate"],
        "host_listings_count": f["host_listings"],
        "calculated_host_listings_count": f["host_listings"],
        "host_tenure_days": f["tenure_days"], "response_speed": f["resp_speed"],
        # 用心度
        "desc_len": f["desc_len"], "host_about_len": f["about_len"],
        # 評分:新房源無評論 → 同群中位代填(信心指數會扣分)
        "review_scores_rating": sm, "review_scores_cleanliness": sm,
        "review_scores_location": sm, "review_scores_value": sm,
        "review_scores_communication": sm, "review_scores_checkin": sm,
        "review_scores_accuracy": sm,
        # 競爭
        "price_pctl_nbhd": comp["price_pctl_nbhd"],
        "score_pctl_nbhd": 0.5,            # 新房源評分未知 → 取中位百分位
        "amenities_vs_median": comp["amenities_vs_median"],
        "nbr_density_1km": comp["nbr_density_1km"],
        "nbr_density_same_type_1km": comp["nbr_density_same_type_1km"],
        # 照片設計感:登錄階段無法計算 CV → 中性值(模型此欄為常數,不影響)
        "photo_design_sense": 0.5,
    }
    return row


def confidence_index(prob: float, variant: str, has_scores: bool) -> dict:
    """信心指數 = 模型可靠度 × 資料完整度 × 判斷明確度。回傳 0~100 與拆解。

    * 模型可靠度:以前瞻驗證 AUC 為天花板(約 0.75),模型本身只有這麼準。
    * 資料完整度:新房源缺住客評分(7 項)→ 以中位代填,屬推測,扣分;
      冷啟動變體另缺房東歷史。
    * 判斷明確度:預測機率越靠近門檻(0.5)越不確定,越極端越明確。
    """
    reliability = 0.75
    total = 31 if variant == "cold" else 37
    fabricated = 0 if has_scores else 8      # 7 評分 + score_pctl
    completeness = max(0.0, (total - fabricated) / total)
    decisiveness = 0.5 + 0.5 * abs(prob - 0.5) * 2
    idx = reliability * completeness * decisiveness * 100
    return {"index": round(idx, 0), "reliability": reliability,
            "completeness": completeness, "decisiveness": decisiveness}


def _conf_label(idx: float) -> tuple[str, str]:
    if idx >= 60:
        return "高信心", P["low"]
    if idx >= 40:
        return "中信心", P["medium"]
    return "低信心", P["high"]


def render(bundle):
    """房源登錄分頁主體。bundle = feature_engineering.load_bundle()。"""
    from modules import feature_engineering as fe
    from modules.ui_components import sec, mb, note

    ref = _reference()
    st.markdown(f"""
<div style="padding:4px 0 10px;">
  <h2 style="font-size:1.25rem;font-weight:800;color:{P['ink']};margin:0;">
  📝 房源登錄 — 刊登前的空屋風險試算</h2>
  <p style="font-size:.82rem;color:{P['muted']};margin:4px 0 0;">
  填寫房源與房東資訊、上傳封面照片,系統即時套用平台模型算出「預估空屋率」與
  「信心指數」,幫你在刊登到 Airbnb / 591 / Booking 前先評估風險。</p>
</div><hr style="margin:0 0 10px;">""", unsafe_allow_html=True)

    with st.form("listing_reg"):
        sec("① 基本資訊")
        c = st.columns(3)
        name = c[0].text_input("房源名稱", placeholder="例:信義區溫馨兩房 近捷運")
        district = c[1].selectbox("行政區", list(ref["nb_code"].keys()))
        room_label = c[2].selectbox("房型", list(ROOM_TYPES.keys()))
        room_type = ROOM_TYPES[room_label]
        c = st.columns(3)
        property_type = c[0].selectbox(
            "物業類型", sorted(ref["pt_code"].keys()) or ["Entire rental unit"])
        price = c[1].number_input("每晚定價 (NT$)", 200, 80000, 2000, 50)
        accommodates = c[2].number_input("可住人數", 1, 16, 2)
        c = st.columns(4)
        bedrooms = c[0].number_input("臥室數", 0, 10, 1)
        beds = c[1].number_input("床數", 1, 20, 1)
        bathrooms = c[2].number_input("衛浴數", 1, 10, 1)
        min_nights = c[3].number_input("最低入住天數", 1, 90, 1)
        max_nights = st.number_input("最高入住天數", 1, 1125, 365)

        sec("② 位置(座標用於計算周邊競爭密度)")
        cen = ref["centroid"].get(district, {"latitude": 25.04, "longitude": 121.55})
        c = st.columns(2)
        lat = c[0].number_input("緯度", 24.9, 25.3,
                                float(round(cen["latitude"], 5)), format="%.5f")
        lon = c[1].number_input("經度", 121.3, 121.7,
                                float(round(cen["longitude"], 5)), format="%.5f")
        st.caption("預設為所選行政區的中心點,可微調為實際位置。")

        sec("③ 設施與文案")
        amenities = st.multiselect("房源設施(勾選越齊全,競爭力越高)",
                                   AMENITY_OPTIONS, default=["WiFi", "冷氣"])
        self_checkin = "自助入住" in amenities
        c = st.columns(2)
        instant = c[0].checkbox("開放即時預訂", value=True)
        description = c[1].text_area("房源描述文案", height=80,
                                     placeholder="介紹房源特色、周邊機能、交通…")

        sec("④ 房東資訊(用於判斷完整/冷啟動模型)")
        c = st.columns(3)
        host_listings = c[0].number_input("名下房源數(含本間)", 1, 500, 1)
        superhost = c[1].checkbox("已是超讚房東", value=False)
        resp_label = c[2].selectbox("平均回覆速度", list(RESP_SPEED.keys()), index=1)
        c = st.columns(3)
        resp_rate = c[0].slider("回覆率", 0.0, 1.0, 0.9, 0.05)
        acc_rate = c[1].slider("接受率", 0.0, 1.0, 0.85, 0.05)
        tenure_years = c[2].number_input("經營年資(年)", 0.0, 20.0, 0.0, 0.5)
        about = st.text_area("房東自我介紹", height=60,
                             placeholder="讓房客認識你,提升信任感…")

        sec("⑤ 上傳封面照片(選填)")
        photo = st.file_uploader("封面照片", type=["jpg", "jpeg", "png"])

        submitted = st.form_submit_button("🔍 試算空屋風險與信心指數",
                                          use_container_width=True)

    if not submitted:
        note("填寫完上方欄位後,按「試算」即可看到預估空屋率、警報等級與信心指數。"
             "新房源因為還沒有住客評論,評分欄會以同商圈同房型的中位數代填,"
             "這也會反映在信心指數上。")
        return

    # ── 組特徵列 → 預測 ──
    f = dict(district=district, room_type=room_type, property_type=property_type,
             price=float(price), accommodates=float(accommodates),
             bedrooms=float(bedrooms), beds=float(beds), bathrooms=float(bathrooms),
             min_nights=float(min_nights), max_nights=float(max_nights),
             amen_count=float(len(amenities)), instant=instant,
             self_checkin=self_checkin, lat=float(lat), lon=float(lon),
             superhost=superhost, resp_rate=float(resp_rate),
             acc_rate=float(acc_rate), host_listings=float(host_listings),
             tenure_days=float(tenure_years * 365), resp_speed=RESP_SPEED[resp_label],
             desc_len=float(len(description or "")),
             about_len=float(len(about or "")))
    row = pd.Series(_build_row(ref, f))
    res = fe.predict_risk_v2(row, bundle)
    vac, prob, tier, variant = (res["risk_score"], res["notify_prob"],
                                res["tier"], res["variant"])
    conf = confidence_index(prob, variant, has_scores=False)
    tier_zh = {"red": ("🔴 高風險", P["high"]), "yellow": ("🟡 觀察", P["medium"]),
               "green": ("🟢 安全", P["low"])}[tier]
    clab, ccol = _conf_label(conf["index"])

    st.markdown("---")
    sec("試算結果")
    a, b = st.columns([1, 1], gap="large")
    with a:
        st.markdown(
            f"<div style='text-align:center;background:{P['surface']};border:1px solid "
            f"{P['border']};border-radius:14px;padding:18px;'>"
            f"<div style='font-size:.78rem;color:{P['muted']};letter-spacing:.06em;'>"
            f"預估空屋率</div>"
            f"<div style='font-size:2.6rem;font-weight:800;color:{tier_zh[1]};"
            f"line-height:1.1;'>{vac*100:.0f}%</div>"
            f"<div style='margin-top:4px;'><span style='background:{tier_zh[1]};"
            f"color:#fff;border-radius:16px;padding:3px 16px;font-weight:800;'>"
            f"{tier_zh[0]}</span></div>"
            f"<div style='color:{P['muted']};font-size:.76rem;margin-top:8px;'>"
            f"高風險機率 P(空屋率≥60%):{prob*100:.0f}%<br>"
            f"模型:{'冷啟動(新房東)' if variant=='cold' else '完整'}變體</div></div>",
            unsafe_allow_html=True)
    with b:
        st.markdown(
            f"<div style='text-align:center;background:{P['surface']};border:1px solid "
            f"{P['border']};border-radius:14px;padding:18px;'>"
            f"<div style='font-size:.78rem;color:{P['muted']};letter-spacing:.06em;'>"
            f"信心指數</div>"
            f"<div style='font-size:2.6rem;font-weight:800;color:{ccol};"
            f"line-height:1.1;'>{conf['index']:.0f}<span style='font-size:1rem;'>"
            f" / 100</span></div>"
            f"<div style='margin-top:4px;'><span style='background:{ccol};color:#fff;"
            f"border-radius:16px;padding:3px 16px;font-weight:800;'>{clab}</span></div>"
            f"<div style='color:{P['muted']};font-size:.74rem;margin-top:8px;'>"
            f"模型可靠度 {conf['reliability']*100:.0f}% × 資料完整度 "
            f"{conf['completeness']*100:.0f}% × 判斷明確度 "
            f"{conf['decisiveness']*100:.0f}%</div></div>",
            unsafe_allow_html=True)

    note("<b>信心指數怎麼看</b>:它衡量「這個空屋率分數有多可信」,不是房源好壞。"
         "三個因子相乘 —— ①<b>模型可靠度</b>:模型前瞻 AUC 約 0.75,本身就有上限;"
         "②<b>資料完整度</b>:新房源沒有住客評分,以中位代填會拉低;"
         "③<b>判斷明確度</b>:預估越靠近門檻越不確定。"
         "<b>想提高信心</b>:實際經營一段時間累積真實評分後再回來試算,分數會更可靠。")

    # 封面照片 AI 清晰度(若有上傳)
    if photo is not None:
        try:
            from PIL import Image
            from modules.image_analysis import extract_features, classify
            img = Image.open(photo).convert("RGB")
            raw, x = extract_features(img)
            p_clear, lab = classify(x)
            cimg1, cimg2 = st.columns([1, 1.4])
            cimg1.image(img, width="stretch", caption="封面照片")
            col = P["low"] if lab == "清晰" else (P["medium"] if lab == "尚可" else P["high"])
            cimg2.markdown(
                f"<div style='background:{P['surface']};border:1px solid {P['border']};"
                f"border-top:3px solid {col};border-radius:10px;padding:12px 14px;'>"
                f"<div style='font-size:.74rem;color:{P['muted']};'>AI 照片清晰度</div>"
                f"<div style='font-size:1.5rem;font-weight:800;color:{col};'>{lab}</div>"
                f"<div style='font-size:.76rem;color:{P['muted']};'>清晰機率 "
                f"{p_clear*100:.0f}%</div></div>", unsafe_allow_html=True)
            if lab == "模糊":
                cimg2.caption("⚠️ 封面偏模糊,建議換一張清晰明亮的照片再刊登。")
        except Exception:
            st.caption("(照片分析失敗,可略過)")

    # ── 模擬刊登 + 房源摘要下載 ──
    sec("刊登到第三方平台")
    mb("平台無公開寫入 API,此處為模擬送出並產生房源摘要供你複製到各平台")
    summary = _summary_md(name or "(未命名房源)", district, room_label, property_type,
                          price, accommodates, bedrooms, beds, bathrooms,
                          amenities, vac, prob, tier_zh[0], conf["index"], clab)
    d1, d2 = st.columns([1, 1])
    d1.download_button("⬇️ 下載房源摘要 (Markdown)", summary,
                       file_name=f"房源登錄_{name or '未命名'}.md",
                       mime="text/markdown", use_container_width=True)
    if d2.button("📤 模擬送出刊登(Airbnb / 591 / Booking)",
                 use_container_width=True):
        st.toast("✅ 已模擬送出到 Airbnb、591、Booking(示範)", icon="📤")
        st.success("已模擬送出。實務上可將上方房源摘要複製到各平台的刊登表單。")
    with st.expander("房源摘要預覽"):
        st.markdown(summary)


def _summary_md(name, district, room_label, ptype, price, acc, bed, beds, bath,
                amenities, vac, prob, tier_zh, conf, clab) -> str:
    return (
        f"# 房源登錄摘要 — {name}\n\n"
        f"## 基本資訊\n"
        f"- 行政區:{district}\n- 房型:{room_label}\n- 物業類型:{ptype}\n"
        f"- 每晚定價:NT$ {price:,.0f}\n- 可住人數:{acc:.0f} 人\n"
        f"- 格局:{bed:.0f} 房 / {beds:.0f} 床 / {bath:.0f} 衛\n"
        f"- 設施:{'、'.join(amenities) or '未勾選'}\n\n"
        f"## 刊登前風險試算\n"
        f"- 預估空屋率:**{vac*100:.0f}%**({tier_zh})\n"
        f"- 高風險機率 P(空屋率≥60%):{prob*100:.0f}%\n"
        f"- 信心指數:**{conf:.0f} / 100**({clab})\n\n"
        f"> 空屋率為模型推估、信心指數量化其可信度;新房源累積真實評論後會更準。\n")
