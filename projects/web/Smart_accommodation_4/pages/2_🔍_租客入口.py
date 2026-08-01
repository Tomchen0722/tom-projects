"""
租客入口 — 智能找房（五科成績單）

單頁流程：必要條件篩選 → 五科計分（交通／生活／價格／口碑／設備，各5分、總分25）
→ 依「最在意兩科」優先分排序 → 房源清單＋分佈地圖。
點「查看詳情」彈出房源詳細分析視窗（房源總覽／交通與生活圈／價格與設備／口碑與評論）。

計分規則實作於 modules/tenant_scoring.py，忠實於「新版房源評分模式規劃書 v1.0」。
"""
import ast
import html as _html
import math

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 本頁 score_pool() 內把 T 當作交通分數的區域變數,故 token 模組改名 DT
from modules import design_tokens as DT
from modules import ui_kit
from modules.ui_components import (
    inject_css, P, ROOM_JP, mb, note, stat_card, overview_metric_card,
    html_table, apply_theme, sidebar_nav,
)
from modules.data_loader import load_listings, load_reviews
from modules.geo_utils import (
    load_all_poi, poi_points_within, nearest_poi, nearest_address, POI_NAMES,
)
from modules.nlp_analysis import (
    listing_positive_aspect_summary,
    recent_review_snippets,
)
from modules import tenant_map as map_logic
from modules import tenant_pagination as pagination
from modules import tenant_scoring as ts

# ─── Page config ────────────────────────────────────────────────
st.set_page_config(page_title="租客入口 — 智慧旅宿", page_icon="🔍",
                   layout="wide", initial_sidebar_state="expanded")
inject_css()
st.markdown(
    """
    <style>
    .st-key-t_first button,
    .st-key-t_prev button,
    .st-key-t_next button,
    .st-key-t_last button {
        padding-inline: var(--sa-space-1);
    }
    .st-key-t_first button p,
    .st-key-t_prev button p,
    .st-key-t_next button p,
    .st-key-t_last button p {
        white-space: nowrap;
        font-size: var(--sa-text-caption);
    }
    .tenant-pagination-summary {
        margin-bottom: var(--sa-space-2);
        color: var(--sa-muted);
        font-size: var(--sa-text-caption);
        line-height: 1.5;
        text-align: center;
    }
    .tenant-pagination-affix {
        padding-block: var(--sa-space-2);
        color: var(--sa-muted);
        font-size: var(--sa-text-caption);
        line-height: 1.5;
        white-space: nowrap;
    }
    .tenant-pagination-affix.is-prefix {
        text-align: right;
    }
    .tenant-pagination-affix.is-suffix {
        text-align: left;
    }
    [data-testid="stHorizontalBlock"]:has(
        > [data-testid="stColumn"]
        > [data-testid="stVerticalBlock"]
        > .st-key-t_page_input
    ) {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: var(--sa-space-2);
    }
    [data-testid="stHorizontalBlock"]:has(
        > [data-testid="stColumn"]
        > [data-testid="stVerticalBlock"]
        > .st-key-t_page_input
    ) > [data-testid="stColumn"] {
        min-width: 0 !important;
        width: auto !important;
    }
    [data-testid="stHorizontalBlock"]:has(
        > [data-testid="stColumn"]
        > [data-testid="stVerticalBlock"]
        > .st-key-t_page_input
    ) > [data-testid="stColumn"]:nth-child(1) {
        flex: .55 1 0 !important;
    }
    [data-testid="stHorizontalBlock"]:has(
        > [data-testid="stColumn"]
        > [data-testid="stVerticalBlock"]
        > .st-key-t_page_input
    ) > [data-testid="stColumn"]:nth-child(2) {
        flex: 1 1 0 !important;
    }
    [data-testid="stHorizontalBlock"]:has(
        > [data-testid="stColumn"]
        > [data-testid="stVerticalBlock"]
        > .st-key-t_page_input
    ) > [data-testid="stColumn"]:nth-child(3) {
        flex: 1.1 1 0 !important;
    }
    .tenant-listing-card {
        transition: border-color .2s ease, box-shadow .2s ease;
    }
    .tenant-listing-card.is-selected {
        border-color: var(--sa-primary) !important;
        box-shadow: var(--sa-shadow-md) !important;
    }
    div[class*="st-key-tenant_card_focus_"] {
        position: relative;
    }
    div[class*="st-key-map_photo_"],
    div[class*="st-key-map_title_"] {
        position: absolute;
        z-index: 3;
        margin: 0 !important;
    }
    div[class*="st-key-map_photo_"] {
        top: 14px;
        left: 16px;
        width: 210px;
        height: 158px;
    }
    div[class*="st-key-map_title_"] {
        top: 14px;
        right: 16px;
        left: 241px;
        height: 64px;
    }
    div[class*="st-key-map_photo_"] [data-testid="stButton"],
    div[class*="st-key-map_title_"] [data-testid="stButton"] {
        height: 100%;
    }
    div[class*="st-key-map_photo_"] button,
    div[class*="st-key-map_title_"] button {
        width: 100%;
        height: 100%;
        min-height: 0;
        padding: 0;
        border-color: transparent !important;
        background: transparent !important;
        box-shadow: none !important;
        color: transparent !important;
        cursor: pointer;
    }
    div[class*="st-key-map_photo_"] button p,
    div[class*="st-key-map_title_"] button p {
        overflow: hidden;
        opacity: 0;
        white-space: nowrap;
    }
    div[class*="st-key-map_photo_"] button:focus-visible,
    div[class*="st-key-map_title_"] button:focus-visible {
        border-radius: var(--sa-radius-sm);
        outline: 2px solid var(--sa-primary);
        outline-offset: var(--sa-space-1);
    }
    div[class*="st-key-tenant_card_focus_"]:has(
        div[class*="st-key-map_title_"] button:hover
    ) .tenant-card-map-title {
        color: var(--sa-primary);
        text-decoration: underline;
        text-underline-offset: var(--sa-space-1);
    }
    .tenant-card-photo-wrap {
        display: block;
        flex: none;
        position: relative;
    }
    .tenant-card-map-badge {
        position: absolute;
        right: var(--sa-space-2);
        bottom: var(--sa-space-2);
        padding: var(--sa-space-1) var(--sa-space-2);
        border: 1px solid var(--sa-primary-border);
        border-radius: var(--sa-radius-pill);
        background: var(--sa-primary-bg);
        color: var(--sa-primary-fg);
        font-size: var(--sa-text-label);
        font-weight: 700;
        opacity: 0;
        transform: translateY(var(--sa-space-1));
        transition: opacity .2s ease, transform .2s ease;
    }
    div[class*="st-key-tenant_card_focus_"]:has(
        div[class*="st-key-map_photo_"] button:hover
    ) .tenant-card-map-badge,
    div[class*="st-key-tenant_card_focus_"]:has(
        div[class*="st-key-map_photo_"] button:focus-visible
    ) .tenant-card-map-badge {
        opacity: 1;
        transform: translateY(0);
    }
    .tenant-map-summary {
        margin-top: var(--sa-space-2);
        padding: var(--sa-space-3);
        border: 1px solid var(--sa-primary-border);
        border-radius: var(--sa-radius-sm);
        background: var(--sa-primary-bg);
        box-shadow: var(--sa-shadow-sm);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <style>
    .st-key-tenant_map_panel {{
        position: sticky;
        top: var(--sa-space-4);
        z-index: 2;
        align-self: flex-start;
    }}
    @media(max-width:{DT.BREAKPOINT["mobile"]}) {{
        .st-key-tenant_map_panel {{
            position: static;
        }}
    }}
    @media(prefers-reduced-motion:reduce) {{
        .tenant-listing-card,
        .tenant-card-map-badge {{
            transition: none;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── Load data ──────────────────────────────────────────────────
with st.spinner("載入房源與生活圈資料 …"):
    DF = load_listings()
    REVIEWS = load_reviews()
    POI_ALL = load_all_poi()

# ─── 常數／設定 ─────────────────────────────────────────────────
SUBJECT_ORDER = ["transit", "life", "price", "reputation", "amenity"]
SUBJECT_ZH = ts.SUBJECT_ZH                      # transit→交通方便 …
SUBJECT_SHORT = {"transit": "交通", "life": "生活", "price": "價格",
                 "reputation": "口碑", "amenity": "設備"}
SUBJECT_ICON = {"transit": "🚇", "life": "🏪", "price": "💰",
                "reputation": "💬", "amenity": "🛋"}
_ZH2KEY = {v: k for k, v in SUBJECT_ZH.items()}
WISH_LABELS = list(ts.AMENITY_KEYWORDS.keys())  # Wi-Fi/冷氣/洗衣機/…
CANDIDATE_CAP = 300
PAGE_SIZE = 8
MAP_RADIUS_M = map_logic.DEFAULT_FOCUS_RADIUS_M

# 地圖 5 級顏色帶（對應圖例；門檻以 25 分制表示）
# 色碼與門檻的唯一來源是 design_tokens.SCORE_BANDS，本頁不再自己寫一份。
BANDS = list(DT.SCORE_BANDS)


def _set_tenant_page(target_page):
    """由首／前／後／末頁按鈕同步正式頁碼與輸入元件狀態。"""
    page_count = st.session_state.get("_t_page_count", 1)
    try:
        target = pagination.validate_page(target_page, page_count)
    except pagination.PaginationInputError:
        return
    st.session_state["t_page"] = target
    st.session_state["t_page_input"] = target
    st.session_state.pop("_t_page_error", None)


def _apply_tenant_page_input():
    """套用目前篩選結果範圍內的整數頁碼；無效值保留原頁。"""
    page_count = st.session_state.get("_t_page_count", 1)
    current = st.session_state.get("t_page", 1)
    try:
        target = pagination.validate_page(
            st.session_state.get("t_page_input"), page_count)
    except pagination.PaginationInputError:
        st.session_state["t_page_input"] = current
        st.session_state["_t_page_error"] = (
            f"請輸入 1～{page_count} 的整數頁碼。")
        return
    st.session_state["t_page"] = target
    st.session_state.pop("_t_page_error", None)


def val_color(v, maxv=25):
    """依分數（換算到 25 分制）回傳顏色。None/NaN → 灰。"""
    if v is None or pd.isna(v):
        return P["muted"]
    frac = v / maxv * 25
    for lo, _, c in BANDS:
        if frac >= lo:
            return c
    return BANDS[-1][2]


def _fmt(v):
    """數字精簡顯示：4.5→'4.5'、5.0→'5'。"""
    if v is None or pd.isna(v):
        return "—"
    return f"{v:g}"


def _map_score_text(value, max_score):
    if value is None or pd.isna(value):
        return "資料不足"
    return f"{float(value):.1f}／{max_score:g}"


def _map_evidence(row, map_dim):
    """使用 score_pool 同一列資料產生地圖 hover／摘要證據。"""
    if map_dim == "綜合總分":
        subjects = "、".join(
            f"{SUBJECT_SHORT[key]} {_map_score_text(row[f's_{key}'], 5)}"
            for key in SUBJECT_ORDER
        )
        return f"五科：{subjects}"
    if map_dim == SUBJECT_ZH["transit"]:
        mrt = row.get("mrt_dist_m")
        bus = row.get("bus_dist_m")
        mrt_text = "資料不足" if pd.isna(mrt) else f"{float(mrt):.0f}m"
        bus_text = "資料不足" if pd.isna(bus) else f"{float(bus):.0f}m"
        return f"最近捷運 {mrt_text}；公車 {bus_text}（直線距離估計）"
    if map_dim == SUBJECT_ZH["life"]:
        return (
            f"超商／超市 {int(row.get('conv_cnt', 0))}、"
            f"餐飲 {int(row.get('rest_cnt', 0))}、"
            f"診所 {int(row.get('clinic_cnt', 0))}、"
            f"公園 {int(row.get('park_cnt', 0))}"
        )
    if map_dim == SUBJECT_ZH["price"]:
        median = row.get("price_median")
        difference = row.get("price_D")
        median_text = (
            "資料不足" if pd.isna(median) else f"${float(median):,.0f}")
        difference_text = (
            "資料不足" if pd.isna(difference)
            else f"{float(difference):+.1f}%")
        return (
            f"同類中位 {median_text}；差異 {difference_text}；"
            f"樣本 {int(row.get('price_group_n', 0))} 間"
        )
    if map_dim == SUBJECT_ZH["reputation"]:
        return (
            f"Airbnb 換算 {_fmt(row.get('rep_A'))}；"
            f"NLP {_fmt(row.get('rep_N'))}；"
            f"有效分析 {int(row.get('rep_analyzable', 0))} 則；"
            f"評論上限 {_fmt(row.get('rep_cap'))}"
        )
    return (
        f"希望設備命中 {int(row.get('amen_m', 0))}／"
        f"{int(row.get('amen_k', 0))} 項"
    )


# ─── 設施字串 → 繁中（詳情頁「全部設備」用）─────────────────────
def _amenity_list(raw):
    try:
        items = ast.literal_eval(raw) if isinstance(raw, str) else []
        return [str(a) for a in items if str(a).strip()]
    except Exception:
        return []


_AMEN_ZH = [
    ("split type ductless", "分離式空調"), ("hot water kettle", "熱水壺"),
    ("hot water", "熱水"), ("hair dryer", "吹風機"), ("mini fridge", "小冰箱"),
    ("refrigerator", "冰箱"), ("air conditioning", "冷氣"), ("heating", "暖氣"),
    ("washer", "洗衣機"), ("dryer", "烘衣機"), ("kitchen", "廚房"),
    ("microwave", "微波爐"), ("refrigerator", "冰箱"), ("elevator", "電梯"),
    ("hdtv", "高畫質電視"), ("tv", "電視"), ("balcony", "陽台"),
    ("patio", "露台"), ("bathtub", "浴缸"), ("wifi", "Wi-Fi"),
    ("free parking", "免費停車"), ("paid parking", "付費停車"),
    ("parking", "停車"), ("private entrance", "獨立入口"),
    ("self check-in", "自助入住"), ("essentials", "生活必需品"),
]


def zh_amenity(a):
    low = str(a).lower().strip()
    if low == "wifi":
        return "Wi-Fi"
    for kw, zh in _AMEN_ZH:
        if kw in low:
            return zh
    return a


# ═══════════════════════════════════════════════════════════════
# 五科計分（快取；依賴穩定的全域 DF/REVIEWS/POI_ALL）
# ═══════════════════════════════════════════════════════════════
@st.cache_data(show_spinner=False)
def score_pool(ids: tuple, wish: tuple):
    """對候選 ids 計算五科成績單，回傳每列一房源的 DataFrame。"""
    wish = list(wish)
    sub = DF[DF["id"].isin(ids)]

    def _nan(x):
        return np.nan if x is None else x

    rows = []
    for _, L in sub.iterrows():
        lat, lon = L["latitude"], L["longitude"]
        gf = ts.compute_geo_facts(lat, lon, POI_ALL)
        T, td = ts.transit_score(gf["mrt_dist_m"], gf["bus_dist_m"])
        Lp, ld = ts.life_score(gf["conv_cnt"], gf["rest_cnt"],
                               gf["clinic_cnt"], gf["park_cnt"])
        Pp, pdd = ts.price_score(L["price"], DF, L)
        br = ts.review_sentiment_breakdown(REVIEWS, int(L["id"]))
        R, rd = ts.reputation_score(L.get("review_scores_rating"),
                                    br["pos_n"], br["neg_n"],
                                    br["n_analyzable"], br["n_total"])
        flags = ts.match_amenities(L.get("amenities", "[]"), wish)
        E, ad = ts.amenity_score(flags)
        scores = {"transit": T, "life": Lp, "price": Pp,
                  "reputation": R, "amenity": E}
        total, band = ts.total_and_band(scores)
        details = {"transit": td, "life": ld, "price": pdd,
                   "reputation": rd, "amenity": ad}
        reason = ts.recommend_reason(scores, details, wish)
        rows.append({
            "id": int(L["id"]),
            "s_transit": T, "s_life": Lp,
            "s_price": _nan(Pp), "s_reputation": _nan(R), "s_amenity": _nan(E),
            "total": total, "band": band, "reason": reason,
            "mrt_dist_m": gf["mrt_dist_m"], "bus_dist_m": gf["bus_dist_m"],
            "conv_cnt": gf["conv_cnt"], "rest_cnt": gf["rest_cnt"],
            "clinic_cnt": gf["clinic_cnt"], "park_cnt": gf["park_cnt"],
            "price_median": _nan(pdd["median"]), "price_D": _nan(pdd["D"]),
            "price_group_n": pdd["group_size"], "price_relaxed": pdd["relaxed"],
            "rep_A": _nan(rd["A"]), "rep_N": _nan(rd["N"]), "rep_cap": rd["cap"],
            "rep_pos": br["pos_n"], "rep_neg": br["neg_n"], "rep_neu": br["neu_n"],
            "rep_analyzable": br["n_analyzable"], "rep_total": br["n_total"],
            "rep_insufficient": rd.get("insufficient") or "",
            "amen_m": ad["m"], "amen_k": ad["k"],
        })
    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════════════
# 詳情視窗（st.dialog，四分頁）
# ═══════════════════════════════════════════════════════════════
def _mini_cards(items):
    """一列精簡數據小卡：items = [(值, 標籤, 顏色), ...]。比 stat_card 矮很多。"""
    cells = "".join(
        f'<div style="flex:1;text-align:center;background:{P["surface"]};'
        f'border:1px solid {P["border"]};border-radius:var(--sa-radius-sm);padding:7px 4px;">'
        f'<div style="font-size:var(--sa-text-card-title);font-weight:800;color:{c};line-height:1.2;">{v}</div>'
        f'<div style="font-size:var(--sa-text-label);color:{P["muted"]};margin-top:2px;">{lab}</div></div>'
        for v, lab, c in items)
    st.markdown(f'<div style="display:flex;gap:7px;">{cells}</div>',
                unsafe_allow_html=True)


def _score_pill_row(row):
    """五科分數精簡列。"""
    items = []
    for k in SUBJECT_ORDER:
        v = row[f"s_{k}"]
        disp = ("資料不足" if pd.isna(v)
                else f"{_fmt(v)}<span style='font-size:var(--sa-text-label);font-weight:600;'> /5</span>")
        items.append((disp, f"{SUBJECT_ICON[k]} {SUBJECT_ZH[k]}", val_color(v, 5)))
    _mini_cards(items)


def _radar(row, h=250):
    cats = [SUBJECT_ZH[k] for k in SUBJECT_ORDER]
    vals = [0 if pd.isna(row[f"s_{k}"]) else float(row[f"s_{k}"])
            for k in SUBJECT_ORDER]
    fig = go.Figure(go.Scatterpolar(
        r=vals + [vals[0]], theta=cats + [cats[0]], fill="toself",
        fillcolor="rgba(91,158,115,.22)",
        line=dict(color=P["tenant"], width=2), name="本房源"))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(range=[0, 5], tickvals=[1, 2, 3, 4, 5],
                            gridcolor=P["border"], tickfont=dict(size=9)),
            angularaxis=dict(tickfont=dict(size=11, color=P["ink2"])),
            bgcolor="rgba(0,0,0,0)"),
        paper_bgcolor="rgba(0,0,0,0)", height=h,
        margin=dict(l=44, r=44, t=20, b=20), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def _detail_overview(row, L):
    lat, lon = L["latitude"], L["longitude"]
    addr = nearest_address(lat, lon) or L["neighbourhood_cleansed"]
    rating = L.get("review_scores_rating")
    rating_s = f"{rating:.2f}" if pd.notna(rating) else "無評分"
    tcol = val_color(row["total"], 25)
    ci, cr = st.columns([1, 1.15])
    with ci:
        _url = str(L.get("picture_url", "") or "")
        if _url.startswith("http"):
            st.markdown(
                f'<img src="{_url}" referrerpolicy="no-referrer" '
                f'style="width:100%;height:225px;object-fit:contain;display:block;'
                f'border-radius:var(--sa-radius-sm);background:{P["tag_bg"]};" '
                f'onerror="this.style.display=\'none\'">',
                unsafe_allow_html=True)
        st.markdown(f"""
        <div style="margin-top:6px;font-size:var(--sa-text-card-title);font-weight:700;color:{P['ink']};
             line-height:1.35;">{_html.escape(str(L['name']))}</div>
        <div style="font-size:var(--sa-text-caption);color:{P['muted']};line-height:1.7;margin-top:3px;">
          📍 {addr}｜🛏 {L['room_type_zh']}｜👥 {int(L.get('accommodates',0))} 人<br>
          💰 <b style="color:{P['tenant']};font-size:var(--sa-text-card-title);">${L['price']:,.0f}</b> / 晚
          ｜⭐ {rating_s}（Airbnb）｜💬 {int(L['number_of_reviews'])} 則</div>
        """, unsafe_allow_html=True)
    with cr:
        ui_kit.section_header("五科成績單雷達圖")
        _radar(row, h=250)
    st.markdown(
        f'<div style="display:inline-block;border:1.5px solid {tcol};'
        f'background:var(--sa-success-bg);border-radius:var(--sa-radius-sm);padding:5px 14px;margin:4px 0 8px;">'
        f'<span style="font-size:var(--sa-text-body);color:{P["ink2"]};">👑 綜合推薦 </span>'
        f'<b style="font-size:var(--sa-text-metric);color:{tcol};">{_fmt(row["total"])}</b>'
        f'<span style="font-size:var(--sa-text-caption);color:{P["muted"]};"> / 25 ｜ {row["band"]}</span></div>',
        unsafe_allow_html=True)
    _score_pill_row(row)
    st.markdown(
        f'<div style="font-size:var(--sa-text-caption);color:{P["muted"]};margin-top:9px;'
        f'line-height:1.6;">推薦理由：{_html.escape(str(row["reason"]))}</div>',
        unsafe_allow_html=True)


def _detail_transit_life(row, L):
    lat, lon = L["latitude"], L["longitude"]
    mrt_name, mrt_d = nearest_poi(lat, lon, POI_ALL["mrt"])
    bus_name, bus_d = nearest_poi(lat, lon, POI_ALL["bus"])
    cL, cR = st.columns([1, 1.05])
    with cL:
        ui_kit.section_header("交通方便")
        _mini_cards([
            (f"{mrt_d:.0f}m" if math.isfinite(mrt_d) else "—", "最近捷運出口",
             val_color(ts.mrt_points(mrt_d), 3)),
            (f"{bus_d:.0f}m" if math.isfinite(bus_d) else "—", "最近公車站",
             val_color(ts.bus_points(bus_d), 2)),
            (f"{_fmt(row['s_transit'])}/5", "交通分", val_color(row["s_transit"], 5)),
        ])
        st.caption(f"🚇 {mrt_name}（{ts.mrt_points(mrt_d)}/3）· 🚏 {bus_name}"
                   f"（{ts.bus_points(bus_d)}/2）· 直線距離估計")
        ui_kit.section_header("生活便利", note="達標狀況")
        checks = [("🏪 超商", row["conv_cnt"], 1), ("🍜 餐飲", row["rest_cnt"], 5),
                  ("🏥 診所", row["clinic_cnt"], 1), ("🌳 公園", row["park_cnt"], 1)]
        _mini_cards([(f"{int(cnt)}", name, P["low"] if cnt >= nd else P["muted"])
                     for name, cnt, nd in checks])
        st.caption(f"生活分 = 超商{2 if row['conv_cnt']>=1 else 0}+餐飲"
                   f"{1 if row['rest_cnt']>=5 else 0}+診所{1 if row['clinic_cnt']>=1 else 0}"
                   f"+公園{1 if row['park_cnt']>=1 else 0} = {_fmt(row['s_life'])}/5"
                   f"（超商500m・餐飲800m≥5・診所/公園1km）")
    with cR:
        ui_kit.section_header("周遭生活圈地圖", note="800m 內")
        frames = []
        for t in ["mrt", "bus", "convenience", "restaurant", "clinic", "park"]:
            pts = poi_points_within(lat, lon, POI_ALL[t], 800)
            if len(pts):
                pts = pts.head(40).copy()
                pts["類型"] = POI_NAMES[t]
                frames.append(pts)
        me = pd.DataFrame([{"poi_name": L["name"], "latitude": lat, "longitude": lon,
                            "類型": "📍 本房源", "distance_m": 0.0}])
        mp = pd.concat([me] + frames, ignore_index=True) if frames else me
        mp["距離"] = mp["distance_m"].map(lambda d: f"{d:.0f} m")
        mp["_sz"] = (mp["類型"] == "📍 本房源").map({True: 2.6, False: 1.0})
        fig = px.scatter_mapbox(
            mp, lat="latitude", lon="longitude", hover_name="poi_name",
            hover_data={"距離": True, "類型": True, "_sz": False,
                        "latitude": False, "longitude": False, "distance_m": False},
            color="類型", size="_sz", size_max=12, zoom=15, height=340,
            mapbox_style="carto-positron", center={"lat": lat, "lon": lon})
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=0, b=0),
                          legend=dict(font=dict(size=8), bgcolor="rgba(255,255,255,.75)",
                                      orientation="h", yanchor="bottom", y=0.0))
        st.plotly_chart(fig, use_container_width=True)


def _detail_price_amenity(row, L):
    ui_kit.section_header("價格合理")
    med = row["price_median"]
    D = row["price_D"]
    dcol = (P["muted"] if pd.isna(D)
            else (P["low"] if D <= 0 else (P["medium"] if D <= 10 else P["high"])))
    _mini_cards([
        (f"${L['price']:,.0f}", "本房源 / 晚", P["ink"]),
        ("—" if pd.isna(med) else f"${med:,.0f}", "同類中位數", P["ink2"]),
        ("資料不足" if pd.isna(D) else f"{D:+.1f}%", "與中位差異", dcol),
        (f"{_fmt(row['s_price'])}/5", "價格分", val_color(row["s_price"], 5)),
    ])
    st.caption(f"比較組 {int(row['price_group_n'])} 間"
               + ("（樣本較少，已放寬人數）" if row["price_relaxed"] else "")
               + "（同區＋同房型＋可住人數±1）")

    ui_kit.section_header("設備清單", note="本房源提供")
    show = ["Wi-Fi", "冷氣", "電冰箱", "電梯", "洗衣機", "熱水", "吹風機"]
    flags = ts.match_amenities(L.get("amenities", "[]"), show)
    bath_txt = str(L.get("bathrooms_text", "") or "").lower()
    priv_bath = ("private" in bath_txt) or ("獨立" in str(L.get("amenities", "")))
    items = list(zip(show, flags)) + [("獨立衛浴", priv_bath)]
    chips = "".join(
        f'<span style="display:inline-block;border:1px solid {P["border"]};'
        f'border-radius:var(--sa-radius-pill);padding:4px 13px;margin:4px 6px 0 0;font-size:var(--sa-text-caption);'
        f'color:{P["low"] if ok else P["muted"]};background:{P["surface"]};">'
        f'{"✓" if ok else "✗"} {name}</span>'
        for name, ok in items)
    st.markdown(f"<div style='line-height:2.3;'>{chips}</div>", unsafe_allow_html=True)
    if row["amen_k"]:
        st.caption(f"設備分 = 符合 {int(row['amen_m'])} ÷ 所選 {int(row['amen_k'])}"
                   f" × 5 = {_fmt(row['s_amenity'])}/5")

    ams = _amenity_list(L.get("amenities", "[]"))
    if ams:
        with st.expander(f"查看全部 {len(ams)} 項設備"):
            allchips = "".join(
                f'<span style="display:inline-block;background:{P["tag_bg"]};'
                f'border:1px solid {P["border"]};border-radius:var(--sa-radius-md);padding:3px 10px;'
                f'margin:3px 4px 0 0;font-size:var(--sa-text-caption);color:{P["ink2"]};">'
                f'{_html.escape(zh_amenity(a))}</span>' for a in ams)
            st.markdown(f"<div style='line-height:2.1;'>{allchips}</div>",
                        unsafe_allow_html=True)


def _detail_reviews(row, L, listing_id):
    R = row["s_reputation"]
    ui_kit.section_header("住客口碑", note="NLP 分析")
    window = min(20, int(row["rep_total"]))
    rep_disp = "資料不足" if pd.isna(R) else f"{_fmt(R)}/5"
    rc = P["muted"] if pd.isna(R) else val_color(R, 5)
    _mini_cards([
        (rep_disp, "住客口碑分", rc),
        ("—" if pd.isna(row["rep_A"]) else f"{_fmt(row['rep_A'])}/3", "評分分 A", P["ink2"]),
        ("—" if pd.isna(row["rep_N"]) else f"{_fmt(row['rep_N'])}/2", "NLP 內容分 N", P["ink2"]),
        (f"{int(row['rep_analyzable'])}/{window}", "有效分析/取樣", P["ink2"]),
    ])
    st.caption(f"口碑 R = min(A + N, 上限 {int(row['rep_cap'])})；全部評論 "
               f"{int(row['rep_total'])} 則"
               + (f"；{row['rep_insufficient']}" if row["rep_insufficient"] else ""))

    a = int(row["rep_analyzable"])
    pos, neu, neg = int(row["rep_pos"]), int(row["rep_neu"]), int(row["rep_neg"])
    cds, ckw = st.columns([1, 1.3])
    with cds:
        if a > 0:
            sent = pd.DataFrame({"情感": ["正面", "中立", "負面"],
                                 "比例": [pos / a * 100, neu / a * 100, neg / a * 100]})
            fig = px.pie(sent, values="比例", names="情感", color="情感",
                         color_discrete_map={"正面": P["low"], "中立": P["muted"],
                                             "負面": P["high"]}, hole=0.62)
            fig.update_traces(textinfo="label+percent", textfont_size=10,
                              marker_line_width=2, marker_line_color=P["bg"])
            apply_theme(fig, h=215).update_layout(
                margin=dict(l=5, r=5, t=22, b=5), showlegend=False,
                title=dict(text="情感分佈", font=dict(size=12)))
            st.plotly_chart(fig, use_container_width=True)
        else:
            ui_kit.empty_state("近期無可分析評論",
                               hint="此房源近期沒有可供情緒分析的評論。",
                               icon="💬")
    with ckw:
        with st.spinner("整理住客常提到的優點 …"):
            summ = listing_positive_aspect_summary(REVIEWS, listing_id)
        status = summ["status"]
        if status in ("ok", "low_sample") and summ["items"]:
            kw = pd.DataFrame(summ["items"])
            kw["positive_count"] = summ["positive_count"]
            custom = kw[["coverage", "positive_count"]].to_numpy()
            fig = go.Figure(go.Bar(
                x=kw["mentions"],
                y=kw["label"],
                orientation="h",
                marker=dict(color=P["low"]),
                customdata=custom,
                hovertemplate=(
                    "%{y}<br>提及此優點：%{x} 則"
                    "<br>有效正面評論：%{customdata[1]} 則"
                    "<br>涵蓋率：%{customdata[0]:.0%}<extra></extra>"
                ),
            ))
            apply_theme(fig, h=215, legend=False).update_layout(
                yaxis=dict(autorange="reversed"),
                xaxis=dict(
                    title="提及此優點的正面評論數",
                    range=[0, max(1, summ["positive_count"])],
                    dtick=1,
                ),
                margin=dict(l=76, r=14, t=22, b=20),
                title=dict(text="住客常提到的優點", font=dict(size=12)))
            st.plotly_chart(fig, use_container_width=True)
            if status == "low_sample":
                st.caption("樣本較少，結果僅供參考。")
        elif status == "positive_sample_too_small":
            ui_kit.empty_state(
                "正面評論樣本較少",
                hint="目前改以近期正面評論摘錄呈現。",
                icon="💬",
            )
            for snippet in summ["positive_snippets"]:
                st.caption(f"「{snippet}」")
        elif status == "no_reviews":
            ui_kit.empty_state(
                "目前沒有評論",
                hint="尚無法整理住客常提到的優點。",
                icon="💬",
            )
        elif status == "no_analyzable_reviews":
            ui_kit.empty_state(
                "近期無可分析評論",
                hint="評論為空白或語言尚未支援。",
                icon="💬",
            )
        elif status == "no_positive_reviews":
            ui_kit.empty_state(
                "近期沒有可整理的正面評論",
                hint="不使用中立或負面評論產生優點。",
                icon="💬",
            )
        else:
            ui_kit.empty_state(
                "尚無法整理出具體優點",
                hint="目前正面評論沒有足夠的具體房源線索。",
                icon="💬",
            )
        coverage = (
            summ["analyzable_count"] / summ["sampled_count"]
            if summ["sampled_count"] else 0
        )
        analyzer_labels = {
            "vader": "VADER",
            "zh_lexicon": "中文詞典",
            "vader+zh_lexicon": "VADER＋中文詞典",
        }
        analyzers = "、".join(
            analyzer_labels.get(name, name) for name in summ["analyzers"]
        ) or "無"
        st.caption(
            f"近期取樣 {summ['sampled_count']} 則；"
            f"有效分析 {summ['analyzable_count']} 則；"
            f"無法分析 {summ['unanalyzable_count']} 則；"
            f"分析涵蓋率 {coverage:.0%}；"
            f"有效正面 {summ['positive_count']} 則"
        )
        st.caption(f"實際分析器：{analyzers}；規則 {summ['rule_version']}")

    snips = recent_review_snippets(REVIEWS, listing_id, n=10)
    if snips:
        with st.expander(f"查看近期 {len(snips)} 則評論"):
            for s in snips:
                st.markdown(
                    f'<div style="border-bottom:1px solid {P["border"]};'
                    f'padding:6px 0;font-size:var(--sa-text-caption);color:{P["ink2"]};'
                    f'line-height:1.6;">{_html.escape(str(s))}</div>',
                    unsafe_allow_html=True)


def _render_detail(listing_id):
    """依 listing_id 呈現四分頁詳情。優先用當次 M；否則單筆重算。"""
    row = None
    if "M" in globals() and isinstance(M, pd.DataFrame) and (M["id"] == listing_id).any():
        row = M[M["id"] == listing_id].iloc[0]
    else:
        sc = score_pool((int(listing_id),), st.session_state.get("wish", tuple(ts.DEFAULT_WISH)))
        if len(sc):
            row = sc.iloc[0]
    Lr = DF[DF["id"] == listing_id]
    if row is None or Lr.empty:
        st.error("找不到房源資料。")
        return
    L = Lr.iloc[0]
    tabs = st.tabs(["📊 房源總覽", "🚇 交通與生活圈", "💰 價格與設備", "💬 口碑與評論"])
    with tabs[0]:
        _detail_overview(row, L)
    with tabs[1]:
        _detail_transit_life(row, L)
    with tabs[2]:
        _detail_price_amenity(row, L)
    with tabs[3]:
        _detail_reviews(row, L, int(listing_id))


def _on_detail_dismiss():
    st.session_state.detail_open = False


@st.dialog("🏠 房源詳細分析", width="large", on_dismiss=_on_detail_dismiss)
def detail_dialog():
    cur = st.session_state.get("detail_id")
    if cur is None:
        st.session_state.detail_open = False
        return
    _render_detail(int(cur))
    if ui_kit.secondary_button("關閉", key="detail_close_btn", stretch=True):
        st.session_state.detail_open = False
        st.rerun()


def open_detail(listing_id):
    st.session_state.selected_listing_id = int(listing_id)
    st.session_state.detail_open = True
    st.session_state.detail_id = int(listing_id)


def _select_listing_on_map(listing_id):
    """在同一 Streamlit 工作階段選定地圖房源，保留所有已套用篩選。"""
    st.session_state.selected_listing_id = int(listing_id)


# ═══════════════════════════════════════════════════════════════
# Header
# ═══════════════════════════════════════════════════════════════
ui_kit.page_header(
    "智能找房", icon="🔍",
    desc="租客視角:先用必要條件篩掉不合格的，再看五科成績單"
         "（交通・生活・價格・口碑・設備，各 5 分），最在意的兩科優先排序")

# ═══════════════════════════════════════════════════════════════
# Sidebar
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    sidebar_nav()
    ui_kit.filter_group("必要條件", desc="不符合就先排除，不靠扣分留在排名",
                        icon="🔒")
    all_nb = sorted(DF["neighbourhood_cleansed"].dropna().unique())
    sel_nbs = st.multiselect("地區（可複選）", all_nb, default=all_nb[:1], key="t_nb")
    rt_opts = sorted(DF["room_type_zh"].dropna().unique())
    sel_rts = st.multiselect("房型", rt_opts, default=rt_opts, key="t_rt")
    pmin = int(DF["price"].min())
    pmax = int(DF["price"].quantile(0.95))
    sel_price = st.slider("每晚預算 (TWD)", pmin, pmax,
                          (pmin, min(5000, pmax)), step=100, key="t_price")
    sel_must = st.multiselect("必備設備（缺少即排除）", WISH_LABELS,
                              default=[], key="t_must")

    st.divider()
    ui_kit.filter_group("最在意的面向", desc="選 2 項，優先排序這兩科",
                        icon="❤️")
    sel_top2_zh = st.multiselect(
        "最在意兩科", [SUBJECT_ZH[s] for s in SUBJECT_ORDER],
        default=[SUBJECT_ZH["transit"], SUBJECT_ZH["price"]],
        max_selections=2, key="t_top2", label_visibility="collapsed")

    st.divider()
    ui_kit.filter_group("希望設備", desc="計入設備分：符合比例 × 5", icon="🛋")
    sel_wish = st.multiselect("希望設備", WISH_LABELS, default=ts.DEFAULT_WISH,
                              key="t_wish", label_visibility="collapsed")

    st.divider()
    if ui_kit.secondary_button("↻ 清除條件", key="t_reset", stretch=True):
        for _k in ("t_nb", "t_rt", "t_price", "t_must", "t_top2",
                   "t_wish", "t_page", "t_page_input", "_t_page_scope",
                   "_t_page_count", "_t_page_error", "t_mapdim",
                   "selected_listing_id", "t_listing_map"):
            st.session_state.pop(_k, None)
        st.rerun()
    st.caption("© 2026 智慧旅宿 AI 平台 · 評分規則 v1.0")

top2_keys = [_ZH2KEY[x] for x in sel_top2_zh][:2]
st.session_state["wish"] = tuple(sel_wish)
st.session_state["top2_keys"] = top2_keys

# ═══════════════════════════════════════════════════════════════
# 第1關：必要條件硬性篩選
# ═══════════════════════════════════════════════════════════════
flt = DF.copy()
if sel_nbs:
    flt = flt[flt["neighbourhood_cleansed"].isin(sel_nbs)]
if sel_rts:
    flt = flt[flt["room_type_zh"].isin(sel_rts)]
flt = flt[flt["price"].between(sel_price[0], sel_price[1])]
if sel_must:
    keep = flt["amenities"].apply(lambda a: ts.has_all_amenities(a, sel_must))
    flt = flt[keep]
# 核心欄位完整（座標/價格/區/房型）才進入排名
core = (flt["latitude"].notna() & flt["longitude"].notna()
        & flt["price"].notna() & flt["neighbourhood_cleansed"].notna()
        & flt["room_type_zh"].notna())
flt = flt[core]

if flt.empty:
    ui_kit.empty_state("找不到符合必要條件的房源",
                       hint="請放寬側欄的地區、房型、預算或必備設備。",
                       icon="😢")
    st.stop()

total_match = len(flt)
pool = flt.sort_values("number_of_reviews", ascending=False).head(CANDIDATE_CAP)

# ── 五科計分＋排序 ──
with st.spinner(f"計算 {len(pool)} 間房源的五科成績單 …"):
    scored = score_pool(tuple(int(x) for x in pool["id"]), tuple(sel_wish))

keep_cols = ["id", "name", "picture_url", "price", "neighbourhood_cleansed",
             "room_type_zh", "review_scores_rating", "number_of_reviews",
             "latitude", "longitude", "accommodates", "bathrooms_text", "amenities"]
M = pool[keep_cols].merge(scored, on="id", how="inner")
M["n_reviews"] = M["number_of_reviews"].fillna(0)
if top2_keys:
    M["Q"] = M[[f"s_{k}" for k in top2_keys]].fillna(0).sum(axis=1)
else:
    M["Q"] = M["total"]
M = M.sort_values(["Q", "total", "n_reviews", "price"],
                  ascending=[False, False, False, True]).reset_index(drop=True)

# ── 深連結：?listing=id 自動開啟詳情 ──
try:
    _qid = st.query_params.get("listing")
except Exception:
    _qid = None
if _qid and st.session_state.get("_dl_opened") != str(_qid):
    try:
        if int(_qid) in set(M["id"]):
            st.session_state["_dl_opened"] = str(_qid)
            open_detail(int(_qid))
    except Exception:
        pass

# 若詳情視窗開啟，於此重新開啟（保留分頁切換狀態）
if st.session_state.get("detail_open"):
    detail_dialog()

# ═══════════════════════════════════════════════════════════════
# KPI 卡
# ═══════════════════════════════════════════════════════════════
k1, k2, k3, k4 = st.columns(4)
with k1:
    overview_metric_card("符合條件房源", f"{total_match:,} 間")
with k2:
    overview_metric_card("中位價格", f"${M['price'].median():,.0f}")
with k3:
    overview_metric_card("平均綜合分數", f"{M['total'].mean():.1f} / 25")
with k4:
    overview_metric_card("優先查看房源", f"{int((M['total'] >= 20).sum()):,} 間",
                         note_text="綜合 ≥ 20 分")

_t2 = "、".join(sel_top2_zh) if sel_top2_zh else "（未選）"
# D7(2026-07-24):刪掉兩處複述 ——「共計分 N 間」下方分頁列已寫
# 「顯示 lo–hi / N 房源」;「直線距離估計」在交通分的 caption 講過。
note(f"排序：最在意的「{_t2}」兩科優先，平手再看五科總分 ⓘ　"
     f"（總分僅供優先查看排序）")

# ═══════════════════════════════════════════════════════════════
# 清單 + 地圖
# ═══════════════════════════════════════════════════════════════
n_pages = pagination.total_pages(len(M), PAGE_SIZE)
page_scope = pagination.scope_key(M["id"].tolist(), PAGE_SIZE)
scope_changed = (
    "_t_page_scope" in st.session_state
    and st.session_state["_t_page_scope"] != page_scope
)
st.session_state["_t_page_scope"] = page_scope
st.session_state["_t_page_count"] = n_pages
if scope_changed:
    st.session_state["t_page"] = 1
    st.session_state["t_page_input"] = 1
    st.session_state.pop("_t_page_error", None)

candidate_ids = tuple(int(value) for value in M["id"].tolist())
candidate_id_set = set(candidate_ids)
selected_listing_id = st.session_state.get("selected_listing_id")
try:
    selected_listing_id = (
        None if selected_listing_id is None else int(selected_listing_id))
except (TypeError, ValueError):
    selected_listing_id = None
if selected_listing_id not in candidate_id_set:
    selected_listing_id = None
    st.session_state.pop("selected_listing_id", None)

try:
    page = pagination.validate_page(
        st.session_state.get("t_page", 1), n_pages)
except pagination.PaginationInputError:
    page = 1
st.session_state["t_page"] = page
if (
    "t_page_input" not in st.session_state
    or st.session_state["t_page_input"] != page
):
    st.session_state["t_page_input"] = page
window = pagination.page_window(len(M), page, PAGE_SIZE)
start = window.start
page_df = M.iloc[window.start:window.stop]

col_list, col_map = st.columns([1.55, 1])

# ── 房源卡 ──
with col_list:
    ui_kit.section_header("推薦房源清單")
    for _, r in page_df.iterrows():
        rid = int(r["id"])
        rating = r.get("review_scores_rating")
        rating_s = f"{rating:.2f}（Airbnb評分）" if pd.notna(rating) else "無評分"
        tcol = val_color(r["total"], 25)
        is_selected = rid == selected_listing_id
        selected_class = " is-selected" if is_selected else ""
        listing_name = _html.escape(str(r["name"]))
        picture_url = _html.escape(
            str(r.get("picture_url", "") or ""), quote=True)
        # 位置行：行政區・房型・(獨立衛浴)
        _bath = str(r.get("bathrooms_text", "") or "").lower()
        _priv = ("private" in _bath) or ("獨立" in str(r.get("amenities", "")))
        loc_line = (f"{r['neighbourhood_cleansed']}・{r['room_type_zh']}"
                    + ("・獨立衛浴" if _priv else ""))
        # 五科小分（淡綠色藥丸；數字用綠色標粗）
        chips = ""
        for k in SUBJECT_ORDER:
            v = r[f"s_{k}"]
            disp = "－" if pd.isna(v) else _fmt(v)
            chips += (
                f'<span style="display:inline-block;background:var(--sa-success-bg);'
                f'border:1px solid var(--sa-success-border);border-radius:var(--sa-radius-pill);padding:4px 12px;'
                f'margin:5px 6px 0 0;font-size:var(--sa-text-caption);color:{P["ink2"]};">'
                f'{SUBJECT_SHORT[k]} <b style="color:{P["tenant"]};">{disp}</b></span>')
        with st.container(key=f"tenant_card_focus_{rid}"):
            st.markdown(f"""
            <div class="tenant-listing-card{selected_class}" style="background:{P['surface']};border:1px solid {P['border']};
                 border-radius:var(--sa-radius-md);padding:14px 16px;margin-bottom:12px;
                 box-shadow:0 1px 5px rgba(0,0,0,.05);">
              <div style="display:flex;gap:15px;align-items:flex-start;">
                <div class="tenant-card-photo-wrap">
                  <img src="{picture_url}" referrerpolicy="no-referrer"
                       style="width:210px;height:158px;object-fit:cover;border-radius:var(--sa-radius-sm);
                       background:{P['tag_bg']};display:block;"
                       onerror="this.style.display='none'">
                  <span class="tenant-card-map-badge">📍 在地圖定位</span>
                </div>
                <div style="flex:1;min-width:0;">
                  <span class="tenant-card-map-title" style="font-size:var(--sa-text-card-title);
                       font-weight:700;color:{P['ink']};line-height:1.4;">{listing_name}</span>
                  <div style="font-size:var(--sa-text-caption);color:{P['muted']};margin-top:5px;">
                    📍 {loc_line}</div>
                  <div style="margin-top:6px;">
                    <b style="color:{P['tenant']};font-size:var(--sa-text-metric);">${r['price']:,.0f}</b>
                    <span style="font-size:var(--sa-text-caption);color:{P['muted']};"> / 晚</span>
                  </div>
                  <div style="font-size:var(--sa-text-caption);color:{P['ink2']};margin-top:3px;">
                    ⭐ {rating_s} · 💬 {int(r['n_reviews'])} 則評論</div>
                  <div style="margin-top:8px;display:inline-block;text-align:center;
                       border:1.5px solid {tcol};background:var(--sa-success-bg);border-radius:var(--sa-radius-sm);
                       padding:5px 13px;">
                    <span style="font-size:var(--sa-text-caption);color:{P['ink2']};">👑 綜合推薦 </span>
                    <b style="font-size:var(--sa-text-section);color:{tcol};">{_fmt(r['total'])}</b>
                    <span style="font-size:var(--sa-text-caption);color:{P['muted']};"> / 25</span>
                  </div>
                  <div>{chips}</div>
                </div>
              </div>
              <div style="font-size:var(--sa-text-caption);color:{P['muted']};margin-top:10px;
                   line-height:1.6;">推薦原因：{_html.escape(str(r['reason']))}</div>
            </div>""", unsafe_allow_html=True)
            st.button(
                f"在地圖定位照片：{r['name']}",
                key=f"map_photo_{rid}",
                help="在地圖定位此房源",
                on_click=_select_listing_on_map,
                args=(rid,),
            )
            st.button(
                f"在地圖定位標題：{r['name']}",
                key=f"map_title_{rid}",
                help="在地圖定位此房源",
                on_click=_select_listing_on_map,
                args=(rid,),
            )
        # 一張卡片只有一個主要動作(提出租房意願),其餘為次要。
        bc = st.columns(3)
        with bc[0]:
            if ui_kit.secondary_button("🔍 查看詳情", key=f"det_{rid}",
                                       stretch=True):
                open_detail(rid)
                st.rerun()
        with bc[1]:
            if ui_kit.primary_button("🏠 提出租房意願", key=f"rent_{rid}",
                                     stretch=True):
                st.toast(f"✅ 已送出「{str(r['name'])[:14]}」租房意願！", icon="🏠")
        with bc[2]:
            if ui_kit.secondary_button("❤️ 加入收藏", key=f"fav_{rid}",
                                       stretch=True):
                st.session_state.setdefault("fav", set()).add(rid)
                st.toast("❤️ 已加入收藏！", icon="❤️")

    # ── 分頁 ──
    st.markdown("")
    st.markdown(
        f"<div class='tenant-pagination-summary'>"
        f"顯示 {window.display_start}–{window.display_end}，"
        f"共 {len(M)} 間房源</div>",
        unsafe_allow_html=True,
    )
    pcol = st.columns(
        [1, 1.1, 2, 1.1, 1],
        vertical_alignment="center",
    )
    with pcol[0]:
        ui_kit.secondary_button(
            "第一頁", key="t_first", disabled=(page <= 1), stretch=True,
            on_click=_set_tenant_page, args=(1,))
    with pcol[1]:
        ui_kit.secondary_button(
            "◀ 上一頁", key="t_prev", disabled=(page <= 1), stretch=True,
            on_click=_set_tenant_page, args=(page - 1,))
    with pcol[3]:
        ui_kit.secondary_button(
            "下一頁 ▶", key="t_next", disabled=(page >= n_pages), stretch=True,
            on_click=_set_tenant_page, args=(page + 1,))
    with pcol[4]:
        ui_kit.secondary_button(
            "最後一頁", key="t_last", disabled=(page >= n_pages), stretch=True,
            on_click=_set_tenant_page, args=(n_pages,))
    with pcol[2]:
        jump_cols = st.columns(
            [.55, 1, 1.1],
            gap="small",
            vertical_alignment="center",
        )
        jump_cols[0].markdown(
            "<div class='tenant-pagination-affix is-prefix'>第</div>",
            unsafe_allow_html=True)
        with jump_cols[1]:
            st.number_input(
                "目前頁碼",
                min_value=1,
                max_value=n_pages,
                step=1,
                key="t_page_input",
                on_change=_apply_tenant_page_input,
                label_visibility="collapsed",
                help=f"輸入 1～{n_pages} 的整數頁碼後按 Enter。",
            )
        jump_cols[2].markdown(
            f"<div class='tenant-pagination-affix is-suffix'>"
            f"／ {n_pages} 頁</div>",
            unsafe_allow_html=True)
        if st.session_state.get("_t_page_error"):
            st.caption(st.session_state["_t_page_error"])

# ── 地圖 ──
with col_map:
    with st.container(key="tenant_map_panel"):
        map_dim = st.selectbox(
            "地圖著色依據",
            ["綜合總分"] + [SUBJECT_ZH[s] for s in SUBJECT_ORDER],
            key="t_mapdim",
            help="只改變地圖顏色與提示內容，不影響篩選結果或推薦排序。",
        )
        st.caption("ⓘ 只改變地圖顏色與提示內容，不影響篩選、排序或分頁。")
        coverage = f"地圖顯示 {len(M):,}／{total_match:,} 間符合房源"
        if total_match > len(M):
            coverage += f"；依評論數選取前 {CANDIDATE_CAP:,} 間進入評分與地圖"
        st.caption(coverage)

        if map_dim == "綜合總分":
            colname, maxv = "total", 25
        else:
            colname, maxv = f"s_{_ZH2KEY[map_dim]}", 5

        dm = M.copy()
        dm["_v"] = dm[colname]
        dm["_c"] = dm["_v"].apply(lambda value: val_color(value, maxv))
        dm["_price_text"] = dm["price"].map(lambda value: f"${value:,.0f}／晚")
        dm["_metric_text"] = dm["_v"].map(
            lambda value: _map_score_text(value, maxv))
        dm["_total_text"] = dm["total"].map(
            lambda value: _map_score_text(value, 25))
        dm["_evidence"] = dm.apply(
            lambda row: _map_evidence(row, map_dim), axis=1)
        map_custom_columns = [
            "id", "_price_text", "_metric_text", "_total_text", "_evidence"]

        selected_focus = None
        if selected_listing_id is not None:
            try:
                selected_focus = map_logic.focus_for_listing(
                    dm, selected_listing_id, radius_m=MAP_RADIUS_M)
            except map_logic.MapSelectionError:
                selected_listing_id = None
                st.session_state.pop("selected_listing_id", None)

        viewport_revision = map_logic.viewport_revision(
            candidate_ids, selected_listing_id)
        if selected_focus is None:
            map_center = {
                "lat": float(dm["latitude"].mean()),
                "lon": float(dm["longitude"].mean()),
            }
            map_zoom = 12
        else:
            map_center = {
                "lat": selected_focus.latitude,
                "lon": selected_focus.longitude,
            }
            map_zoom = 13.8

        fig = go.Figure()
        if selected_focus is not None:
            circle_lats, circle_lons = map_logic.circle_coordinates(
                selected_focus.latitude,
                selected_focus.longitude,
                radius_m=MAP_RADIUS_M,
            )
            fig.add_trace(go.Scattermapbox(
                lat=circle_lats,
                lon=circle_lons,
                mode="lines",
                fill="toself",
                fillcolor=DT.TINT["primary"]["bg"],
                line=dict(color=DT.COLOR["primary"], width=2),
                opacity=0.5,
                hoverinfo="skip",
                name="1 公里直線範圍",
                showlegend=False,
            ))

        hover_template = (
            "<b>%{text}</b><br>%{customdata[1]}<br>"
            + map_dim
            + "：%{customdata[2]}<br>"
            + "綜合總分：%{customdata[3]}<br>%{customdata[4]}"
            + "<extra></extra>"
        )
        fig.add_trace(go.Scattermapbox(
            lat=dm["latitude"],
            lon=dm["longitude"],
            mode="markers",
            marker=dict(size=11, color=dm["_c"].tolist()),
            ids=dm["id"].astype(str),
            text=dm["name"],
            customdata=dm[map_custom_columns].to_numpy(dtype=object),
            hovertemplate=hover_template,
            name="符合條件房源",
            showlegend=False,
        ))

        if selected_focus is not None:
            selected_map_row = dm[
                dm["id"] == selected_focus.listing_id].iloc[[0]]
            fig.add_trace(go.Scattermapbox(
                lat=[selected_focus.latitude],
                lon=[selected_focus.longitude],
                mode="markers",
                marker=dict(size=21, color=DT.COLOR["surface"]),
                hoverinfo="skip",
                name="定位外框",
                showlegend=False,
            ))
            fig.add_trace(go.Scattermapbox(
                lat=[selected_focus.latitude],
                lon=[selected_focus.longitude],
                mode="markers",
                marker=dict(
                    size=15,
                    color=DT.COLOR["primary"],
                    symbol="circle",
                ),
                ids=[str(selected_focus.listing_id)],
                text=selected_map_row["name"],
                customdata=selected_map_row[
                    map_custom_columns].to_numpy(dtype=object),
                hovertemplate=hover_template,
                name="目前定位房源",
                showlegend=False,
            ))

        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox=dict(
                center=map_center,
                zoom=map_zoom,
                uirevision=viewport_revision,
            ),
            uirevision=viewport_revision,
            height=560,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
        )
        map_event = st.plotly_chart(
            fig,
            width="stretch",
            key="t_listing_map",
            on_select="rerun",
            selection_mode="points",
            config={
                "displayModeBar": True,
                "displaylogo": False,
                "scrollZoom": True,
            },
        )
        clicked_listing_id = map_logic.listing_id_from_selection_event(
            map_event)
        if (
            clicked_listing_id in candidate_id_set
            and clicked_listing_id != selected_listing_id
        ):
            st.session_state["selected_listing_id"] = clicked_listing_id
            st.rerun()

        # 圖例
        unit = "／25" if map_dim == "綜合總分" else "／5"
        swatches = "".join(
            f'<div style="display:flex;align-items:center;gap:6px;margin:2px 0;">'
            f'<span style="width:14px;height:14px;border-radius:var(--sa-radius-bar);background:{color};'
            f'display:inline-block;"></span>'
            f'<span style="font-size:var(--sa-text-caption);color:{P["ink2"]};">{label}</span></div>'
            for _, label, color in BANDS)
        selected_legend = (
            '<div style="font-size:var(--sa-text-label);color:var(--sa-primary-fg);'
            'margin-top:var(--sa-space-1);">📍 藍色圖釘＝目前定位房源；'
            '淡藍範圍＝1 公里直線範圍</div>'
            if selected_focus is not None
            else ""
        )
        st.markdown(
            f'<div style="border:1px solid {P["border"]};border-radius:var(--sa-radius-sm);'
            f'padding:8px 12px;background:{P["surface"]};">'
            f'<div style="font-size:var(--sa-text-caption);font-weight:700;color:{P["ink"]};'
            f'margin-bottom:4px;">{map_dim}{unit}</div>{swatches}'
            f'<div style="font-size:var(--sa-text-label);color:{P["muted"]};margin-top:4px;">'
            f'顏色越綠代表分數越高；灰色代表資料不足</div>{selected_legend}</div>',
            unsafe_allow_html=True,
        )

        if selected_focus is not None:
            selected_row = M[
                M["id"] == selected_focus.listing_id].iloc[0]
            selected_name = _html.escape(str(selected_row["name"]))
            selected_evidence = _html.escape(
                _map_evidence(selected_row, map_dim))
            selected_metric = _map_score_text(
                selected_row[colname], maxv)
            summary_scores = (
                f"綜合總分 {selected_metric}"
                if map_dim == "綜合總分"
                else (
                    f"{map_dim} {selected_metric}・綜合 "
                    f"{_map_score_text(selected_row['total'], 25)}"
                )
            )
            st.markdown(
                f'<div class="tenant-map-summary">'
                f'<div style="font-size:var(--sa-text-label);color:var(--sa-primary-fg);'
                f'font-weight:700;">📍 目前定位房源</div>'
                f'<div style="font-size:var(--sa-text-card-title);color:{P["ink"]};'
                f'font-weight:700;margin-top:var(--sa-space-1);">{selected_name}</div>'
                f'<div style="font-size:var(--sa-text-caption);color:{P["ink2"]};'
                f'margin-top:var(--sa-space-1);">${selected_row["price"]:,.0f}／晚・'
                f'{summary_scores}</div>'
                f'<div style="font-size:var(--sa-text-caption);color:{P["muted"]};'
                f'margin-top:var(--sa-space-1);">{selected_evidence}</div>'
                f'<div style="font-size:var(--sa-text-caption);color:{P["muted"]};'
                f'margin-top:var(--sa-space-1);">1 公里直線範圍內共有 '
                f'{selected_focus.nearby_count} 間符合房源（含本房源）</div></div>',
                unsafe_allow_html=True,
            )
            if ui_kit.secondary_button(
                "🔍 查看詳細分析",
                key=f"t_map_detail_{selected_focus.listing_id}",
                stretch=True,
            ):
                open_detail(selected_focus.listing_id)
                st.rerun()
