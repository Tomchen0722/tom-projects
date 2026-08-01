# -*- coding: utf-8 -*-
"""platform_sections.py — Airbnb 平台方後台的渲染層。

計算全部委由 modules/platform_analytics.py(純 pandas,可測);
本檔只負責 Streamlit 版面、圖表與文案。
"""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from modules import design_tokens as T
from modules import platform_analytics as pa
from modules import ui_kit
from modules.feature_engineering import load_predictions
from modules.ui_components import ROOM_JP, apply_theme

ROOM_ZH = ROOM_JP          # 房型中譯改吃全站唯一來源(原本本檔複製一份)


def commission() -> float:
    value = float(st.session_state.get("pf_commission",
                                       pa.COMMISSION_DEFAULT * 100))
    return value / 100 if value > 1 else value


@st.cache_data(show_spinner="載入平台母體 …")
def _base() -> pd.DataFrame:
    """全平台預測母體;load_predictions() 缺檔時回傳 None,此處轉為空表。"""
    d = load_predictions()
    return d if d is not None else pd.DataFrame()


def load_scope() -> pd.DataFrame:
    """全平台母體套用側欄全域篩選後的範圍。"""
    d = _base()
    if len(d) == 0:
        return d
    return pa.filter_scope(d,
                           st.session_state.get("pf_districts"),
                           st.session_state.get("pf_rooms"))


def guard_scope():
    """各分頁的前置守門:缺檔或篩選為空時渲染提示並回傳 None。"""
    if len(_base()) == 0:
        ui_kit.empty_state("尚未產生模型預測結果",
                           hint="缺少 data/_predictions.csv,請先跑訓練腳本產出預測。",
                           cmd="python -X utf8 scripts/train_backend_models.py",
                           icon="⚙️")
        return None
    df = load_scope()
    if len(df) == 0:
        ui_kit.empty_state("目前篩選條件下沒有房源",
                           hint="請放寬側欄的行政區／房型篩選。")
        return None
    return df


def _money(v: float) -> str:
    """金額縮寫:億 / 萬。"""
    if abs(v) >= 1e8:
        return f"${v / 1e8:,.2f} 億"
    if abs(v) >= 1e4:
        return f"${v / 1e4:,.1f} 萬"
    return f"${v:,.0f}"


def _actual_hint() -> None:
    """KPI 卡下方的一行指引:提醒卡上是預估值,並指向數據分析⑤的實際對照。

    刻意只放一行、不在此展開數字 —— 完整對照含大量方法論但書(構念差異、
    273 天窗口、評論代理、排除無經營跡象房源),放在營運頁會蓋掉決策資訊,
    那些內容屬稽核頁。但若完全不提,看市場總覽的人不會知道有這份資料。
    """
    from modules import actual_analytics as aa
    if not aa.available():
        return
    st.markdown(
        f"<div style='margin-top:6px;color:var(--sa-muted);"
        f"font-size:var(--sa-text-caption);'>"
        f"以上皆為模型預估值。與 {aa.WINDOW_LABEL} 實際發生資料的對照"
        f"（含五項指標落差與成因說明）見 🧪 數據分析 ⑤。</div>",
        unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# 分頁:模型風險預估
# ════════════════════════════════════════════════════════════════
def render_market_overview():
    df = guard_scope()
    if df is None:
        return
    cm = commission()

    # 統計卡只放關鍵數字;判讀口徑交給下方的區塊說明與風險圖例,不在卡上重述。
    # 空屋率/高風險占比/營收四張卡皆採 365 天口徑,卡片底部一律標「年」提醒。
    k = pa.market_kpis(df, cm)
    ui_kit.stat_card_row([
        ("總房源數", f"{k['n_listings']:,} 間"),
        ("活躍房東數", f"{k['n_hosts']:,} 位"),
        ("平均預估空屋率", f"{k['avg_vacancy']:.1%}"),
        (f"{T.tier_label('red')}占比", f"{k['red_ratio']:.1%}"),
        ("預估房東年營收總額", _money(k["total_revenue"])),
        ("預估平台年收入", _money(k["platform_revenue"]),
         f"抽成 {cm:.0%}", "primary"),
    ])
    _actual_hint()

    ui_kit.section_header("行政區健康度",
                          desc="哪些行政區的高風險比例偏高，優先投入輔導資源")
    dh = pa.district_health(df, cm)
    c1, c2 = st.columns([1.15, 1])
    with c1:
        show = dh.assign(
            高風險占比=dh["高風險占比"].map("{:.1%}".format),
            預估平台收入=dh["預估平台收入"].map(_money))[
                ["行政區", "房源數", "高風險占比", "預估平台收入"]]
        ui_kit.data_table(show, height=430)
    with c2:
        fig = px.bar(dh.head(12), x="高風險占比", y="行政區", orientation="h",
                     color="高風險占比",
                     color_continuous_scale=[T.tier_color("green"),
                                             T.tier_color("yellow"),
                                             T.tier_color("red")],
                     text=dh.head(12)["高風險占比"].map("{:.0%}".format))
        apply_theme(fig, h=430).update_layout(
            title="各行政區高風險房源占比", xaxis_title="高風險占比",
            yaxis_title="", yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

    ui_kit.section_header("風險分布地圖",
                          desc="高風險房源集中在哪些位置，判斷是區域性問題還是個案")
    # 圖表用的等級文案與配色一律由 design_tokens 產生,
    # 與統計卡、列表 badge、詳細頁保證同名同色;
    # 等級本身則改用 365 天空屋率門檻(pa.risk_tier_365),與本分頁其他數字口徑一致。
    tier_zh = T.tier_label_map()
    tier_colors = {T.tier_label(k): T.tier_color(k) for k in T.TIER_ORDER}
    tier_names = [T.tier_label(k) for k in T.TIER_ORDER]
    m = df.copy()
    vac_col = pa.vac_col(m)
    m["風險等級"] = pa.risk_tier_365(m[vac_col]).map(tier_zh).fillna(T.tier_label("green"))
    c3, c4 = st.columns([1.6, 1])
    with c3:
        fig = px.scatter_map(
            m, lat="latitude", lon="longitude", color="風險等級",
            color_discrete_map=tier_colors,
            hover_name="neighbourhood_cleansed",
            hover_data={"price": ":,.0f", vac_col: ":.0%"},
            zoom=10.5, height=460, opacity=0.65)
        fig.update_layout(map_style="carto-positron",
                          margin=dict(l=0, r=0, t=0, b=0),
                          legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        cnt = (m["風險等級"].value_counts()
               .reindex(tier_names).fillna(0)
               .reset_index())
        cnt.columns = ["風險等級", "房源數"]
        vac_rules = {
            "red": "預估空屋率 ≥ 60%",
            "yellow": "預估空屋率 35% – 60%",
            "green": "預估空屋率 < 35%",
        }
        x_labels = {
            T.tier_label(k): (f"{T.tier_label(k)}<br>"
                              f"<span style='color:{T.tier_color(k)};"
                              f"font-weight:700;'>{vac_rules[k]}</span>")
            for k in T.TIER_ORDER
        }
        cnt["X標籤"] = cnt["風險等級"].map(x_labels)
        fig = px.bar(cnt, x="X標籤", y="房源數", color="風險等級",
                     color_discrete_map=tier_colors, text="房源數")
        apply_theme(fig, h=460, legend=False).update_layout(
            title="三層警報房源數", xaxis_title="", yaxis_title="房源數")
        st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════════════════════════════
# 分頁:風險管理 —— 雙檢視(房東檢視 ⇄ 房源檢視),渲染委派至
# modules.risk_cockpit_sections;本檔只保留 guard_scope/commission 供其沿用。
# ════════════════════════════════════════════════════════════════
def render_risk_management():
    from modules.risk_cockpit_sections import render
    render()
