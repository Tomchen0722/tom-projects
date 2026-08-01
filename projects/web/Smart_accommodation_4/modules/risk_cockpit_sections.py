# -*- coding: utf-8 -*-
"""risk_cockpit_sections.py — 後台「🚨 風險管理」雙檢視渲染層。

房東檢視(排行榜/模糊搜尋)⇄ 房源檢視(獨立 checkbox 派信),麵包屑導覽。
純計算委由 platform_analytics;信件組裝/寄送/紀錄沿用 notify_center 公開介面。
"""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from modules import actual_analytics as aa
from modules import design_tokens as T
from modules import platform_analytics as pa
from modules import quadrant as QD
from modules import ui_kit
from modules.ui_components import ROOM_JP, apply_theme, note

# 房型中譯與風險等級文案都改吃全站唯一來源(原本本檔各自複製一份)
ROOM_ZH = ROOM_JP
HOST_ALL = "不限"                 # 房源檢視「房東ID」selectbox 的不限哨兵
LEADERBOARD_LIMIT = 100          # 房東檢視排行榜顯示上限
LISTING_LIMIT_DEFAULT = 100      # 房源檢視預設顯示筆數


def _money(v: float) -> str:
    """金額縮寫:億 / 萬(與 platform_sections 一致的顯示規則)。"""
    if abs(v) >= 1e8:
        return f"${v / 1e8:,.2f} 億"
    if abs(v) >= 1e4:
        return f"${v / 1e4:,.1f} 萬"
    return f"${v:,.0f}"


# ── 純邏輯(可 pytest,不依賴 Streamlit runtime)──────────────────
def resolve_host_filter(val, valid_ids) -> int | None:
    """把 rm_host_filter 的值正規化為 int 房東ID 或 None(哨兵/非法/不在母體)。"""
    if val == HOST_ALL or val is None:
        return None
    try:
        hid = int(val)
    except (ValueError, TypeError):
        return None
    return hid if hid in {int(x) for x in valid_ids} else None


def filter_hosts_by_quadrant(host_df: pd.DataFrame, quad_df: pd.DataFrame | None,
                             quadrant_key: str | None,
                             limit: int = LEADERBOARD_LIMIT) -> pd.DataFrame:
    """房東檢視:依四象限篩選房東,取前 limit 位。

    2026-07-25 取代原本的 host_id 模糊查詢 —— 平台方要的是「這一類問題有哪些
    房東」,不是「我知道 ID 想查誰」。

    歸類採「名下至少 1 間屬該象限」(使用者定案),與上方「涉及房東」卡片同口徑;
    同一房東可能同時出現在多個象限的篩選下,這是刻意的 —— 寧可重複出現,
    也不要讓「靠降價撐住」漏掉 161 位確實有該問題、但主要象限更嚴重的房東。

    quadrant_key 為 None(全部)或 quad_df 為 None(缺實際入住資料)時不篩選。
    有篩選時附加「該象限間數」欄並以其為主排序。
    """
    if quadrant_key is None or quad_df is None:
        return host_df.head(limit)
    sub = quad_df[quad_df["quadrant"].astype(str) == quadrant_key]
    cnt = sub.groupby("host_id").size().rename("該象限間數")
    out = host_df.merge(cnt, left_on="host_id", right_index=True, how="inner")
    return (out.sort_values(["該象限間數", "高風險占比"],
                            ascending=[False, False], kind="mergesort")
            .head(limit))


def quadrant_host_counts(quad_df: pd.DataFrame | None) -> dict:
    """各象限「名下至少 1 間」的房東數;供篩選器標籤顯示。"""
    if quad_df is None or len(quad_df) == 0:
        return {}
    return {k: int(g["host_id"].nunique())
            for k, g in quad_df.groupby(quad_df["quadrant"].astype(str))}


def quadrant_listing_counts(quad_df: pd.DataFrame | None) -> dict:
    """各象限的房源數;供房源檢視篩選器標籤顯示。"""
    if quad_df is None or len(quad_df) == 0:
        return {}
    return {k: int(len(g))
            for k, g in quad_df.groupby(quad_df["quadrant"].astype(str))}


def filter_listings(df: pd.DataFrame, tiers, prob_lo: float, prob_hi: float,
                    host_filter: int | None,
                    quadrant_key: str | None = None,
                    quad_df: pd.DataFrame | None = None) -> pd.DataFrame:
    """房源檢視:套用房東鎖定 + 象限篩選 + 警報層級 + 風險分數區間,依 prob 降序。"""
    d = df if host_filter is None else df[df["host_id"] == host_filter]
    if quadrant_key is not None and quad_df is not None:
        sub = quad_df[quad_df["quadrant"].astype(str) == quadrant_key]
        d = d[d["id"].isin(set(sub["id"]))]
    elif quadrant_key is not None and "quadrant" in d.columns:
        d = d[d["quadrant"].astype(str) == quadrant_key]
    chosen = tiers or ["red", "yellow", "green"]
    d = d[d["tier"].astype(str).isin(chosen)]
    prob = pd.to_numeric(d["prob"], errors="coerce").fillna(0)
    d = d[(prob >= prob_lo) & (prob <= prob_hi)]
    return d.sort_values("prob", ascending=False)


def kpi_counts_from_quadrant(quad_df: pd.DataFrame) -> dict:
    """頂部 KPI 卡的數字,直接從四象限分類算,不再各自對 tier 欄另算一次。

    2026-07-25 改版:原本頂部卡各自數 tier=='red'/'yellow',跟下方四象限
    (tier 交叉實際入住/無經營跡象)是兩套邏輯,數字對不起來會讓人以為打架。
    改成同一份 quad_df 算出,兩邊保證一致。
    """
    n_total = int(len(quad_df))
    q = quad_df["quadrant"]
    n_alarm = int((q == "alarm").sum())
    n_hidden = int((q == "hidden").sum())
    n_dormant = int((q == "dormant").sum())
    alarm_hosts = (int(quad_df.loc[q == "alarm", "host_id"].nunique())
                   if n_alarm else 0)
    return {
        "n_total": n_total,
        "n_alarm": n_alarm,
        "n_hidden": n_hidden,
        "n_dormant": n_dormant,
        "alarm_hosts": alarm_hosts,
        "alarm_ratio": (n_alarm / n_total) if n_total else 0.0,
    }


# ── 導覽狀態 callback(在 rerun 前寫 session_state,合法)──────────
def _clear_selection():
    for k in [k for k in st.session_state if str(k).startswith("rm_sel_")]:
        st.session_state[k] = False


def _go_hosts():
    st.session_state["rm_view"] = "hosts"
    st.session_state["rm_host_filter"] = HOST_ALL
    st.session_state["rm_expanded_id"] = None
    st.session_state["rm_focus_id"] = None
    _clear_selection()


def jump_to_listing(listing_id, from_label: str = "其他分頁"):
    """供其他分頁呼叫:跳到「風險管理→房源管理」並鎖定、展開指定房源。

    2026-07-25:「營收與成長」③名單的房源編號用這個當 on_click,讓使用者
    可以直接查看該房源被判定風險的原因、決定要不要寄輔導通知,不用自己
    再去房源管理手動搜。

    字面值 "🚨 風險管理" 必須與 pages/3_📊_後台分析.py 的 TAB_RISK 完全一致
    (兩者是同一個 session_state key pf_active_tab,同頁分頁切換而非換頁)。
    鎖定的房源不受風險分數區間篩選限制 —— 見 _render_listings 用完整 df
    (而非套用篩選後的 fdf)查找該房源,呼叫端不需要事先知道篩選狀態。
    """
    st.session_state["pf_active_tab"] = "🚨 風險管理"
    st.session_state["rm_view"] = "listings"
    st.session_state["rm_host_filter"] = HOST_ALL
    st.session_state["rm_listing_quadrant"] = None
    st.session_state["rm_focus_id"] = int(listing_id)
    st.session_state["rm_expanded_id"] = int(listing_id)
    st.session_state["rm_focus_from"] = from_label
    _clear_selection()


def _clear_focus():
    st.session_state["rm_focus_id"] = None
    st.session_state["rm_expanded_id"] = None


def _go_listings(host_id):
    """點房東ID:自動跳到『房源管理』頁簽並鎖定該房東。"""
    st.session_state["rm_view"] = "listings"
    st.session_state["rm_host_filter"] = int(host_id)
    st.session_state["rm_expanded_id"] = None
    _clear_selection()


def _go_listings_tab():
    """直接點『房源管理』頁簽:切到房源檢視,保留目前房東篩選(預設不限=全部)。"""
    st.session_state["rm_view"] = "listings"
    st.session_state["rm_expanded_id"] = None


def _toggle_expand(lid):
    cur = st.session_state.get("rm_expanded_id")
    st.session_state["rm_expanded_id"] = None if cur == int(lid) else int(lid)
    # 使用者自己點了(任何)房源 ID = 手動瀏覽,跳轉鎖定的任務已完成,清除
    # 避免舊的鎖定房源在使用者切換篩選條件後,還被強制留在清單最上方。
    st.session_state["rm_focus_id"] = None


def _tabs(view: str):
    """狀態驅動的兩頁簽列(房東管理 / 房源管理)。

    原生 st.tabs 無法由程式自動切換,故以兩顆按鈕當頁簽(綁 rm_view),
    才能同時支援『可自由切頁簽』與『點房東自動跳到房源管理』。
    """
    c = st.columns([1.1, 1.1, 4])
    c[0].button("🧑‍💼 房東管理", key="rm_tab_hosts", width="stretch",
                type="primary" if view == "hosts" else "secondary",
                on_click=_go_hosts)
    c[1].button("📋 房源管理", key="rm_tab_listings", width="stretch",
                type="primary" if view == "listings" else "secondary",
                on_click=_go_listings_tab)


def render():
    """後台「🚨 風險管理」入口:兩頁簽(房東管理 / 房源管理)依 rm_view 分流。"""
    from modules.platform_sections import guard_scope, commission
    df = guard_scope()
    if df is None:
        return
    cm = commission()

    quad_df = _annotate_quadrant(df)
    _risk_kpis(df, quad_df)
    _actual_quadrants(quad_df)
    ui_kit.section_header("高風險房源與房東管理",
                          desc="先在「房東管理」找到整批惡化的房東，再下鑽到「房源管理」逐間處理")
    view = st.session_state.setdefault("rm_view", "hosts")
    _tabs(view)
    if view == "listings":
        _render_listings(df, cm, quad_df=quad_df)
    else:
        _render_hosts(df, cm, quad_df)


def _annotate_quadrant(df: pd.DataFrame) -> pd.DataFrame | None:
    """併入實際入住指標並跑四象限分類;缺 _actual_metrics.csv 時回傳 None。"""
    if not aa.available():
        return None
    act = aa.load_actual()[["id", "real_vac", "is_dormant"]]
    return QD.annotate_actual(df.merge(act, on="id", how="left"))


def _risk_kpis(df, quad_df) -> None:
    """風險管理分頁的關鍵指標卡:先看整體規模,再決定要不要下鑽。

    只放數字,判讀門檻交給下方各區塊與 risk_legend —— 遵守「統計卡只放數字」。
    """
    n_total = int(len(df))
    if quad_df is None:
        tier = df["tier"].astype(str)
        n_red = int((tier == "red").sum())
        n_yellow = int((tier == "yellow").sum())
        ui_kit.stat_card_row([
            ("篩選範圍房源", f"{n_total:,} 間"),
            (f"{T.tier_label('red')}房源", f"{n_red:,} 間", None, "danger"),
            (f"{T.tier_label('yellow')}房源", f"{n_yellow:,} 間", None, "warning"),
            ("無經營跡象房源", "0 間", None, "muted"),
        ])
    else:
        k = kpi_counts_from_quadrant(quad_df)
        ui_kit.stat_card_row([
            ("篩選範圍房源", f"{k['n_total']:,} 間"),
            (QD.ACTUAL_QUADRANTS["alarm"]["label"], f"{k['n_alarm']:,} 間",
             None, "danger"),
            (QD.ACTUAL_QUADRANTS["hidden"]["label"], f"{k['n_hidden']:,} 間",
             None, "warning"),
            (QD.ACTUAL_QUADRANTS["dormant"]["label"], f"{k['n_dormant']:,} 間",
             None, "muted"),
        ])


def _actual_quadrants(quad_df: pd.DataFrame | None) -> None:
    """體質 × 實際入住 四象限分布(階段二)。

    單軸紅黃綠會把「模型說安全、實際已停業」的房東整批漏掉 —— 那是最大的一格
    (實測 1,884 間隱形危機)。本區塊補上第二軸,讓平台方在下鑽之前先知道
    「該優先處理哪一類」。quad_df 為 None(缺 _actual_metrics.csv)時靜默略過,
    不擋既有流程。
    """
    if quad_df is None:
        return
    d = quad_df

    ui_kit.section_header(
        "模型預估與實際入住分析",
        desc=f"模型體質評估對上 {aa.WINDOW_LABEL} 的實際入住表現，"
             f"分辨「賣不掉」與「已經沒在做」兩種房東，兩者該做的事不同")

    s = QD.summary_actual(d)
    c1, c2 = st.columns([1.5, 1])
    with c1:
        ui_kit.data_table(s, height=300, wrap=True,
                          widths={"象限": "125px", "房源數": "65px",
                                  "房東數": "65px", "說明": "180px",
                                  "建議行動": "180px"})
    with c2:
        order = [QD.ACTUAL_QUADRANTS[k]["label"]
                 for k in QD.ACTUAL_QUADRANT_ORDER]
        cnt = (s.set_index("象限")["房源數"].reindex(order).dropna()
               .reset_index())
        fig = px.bar(cnt, x="房源數", y="象限", orientation="h",
                     text="房源數",
                     color="象限",
                     category_orders={"象限": order[::-1]},
                     color_discrete_map={
                         spec["label"]: T.LEGACY_P[spec["color"]]
                         for spec in QD.ACTUAL_QUADRANTS.values()})
        apply_theme(fig, h=300, legend=False).update_layout(
            xaxis_title="房源數", yaxis_title="",
            yaxis=dict(categoryorder="array", categoryarray=order[::-1]))
        st.plotly_chart(fig, use_container_width=True)

    note("第一軸是模型體質推估（紅/黃/綠，機率門檻）；第二軸是實際入住率"
         "（≥50% 視為生意好、&lt;20% 視為幾乎沒生意）。兩軸資料來源不同、"
         "實測相關係數僅 0.15，本就不該互相取代——衝突時以實際入住為準，"
         "模型體質用於判斷長期投資價值。")


def _lime_reasons(listing_id: int, top: int = 3) -> list:
    """單一房源 Top-N 風險原因;回傳 [(中文特徵名, 百分點)](自 platform_sections 移入)。"""
    from modules.vacancy_model import contributions, get_row
    row = get_row(int(listing_id))
    if row is None:
        return []
    return [(zh, dpp) for _f, zh, dpp in contributions(row, top=top)]


def _send_single(lid):
    """LIME 面板『產生此房源輔導通知』:單筆組信+模擬寄送(平台視角,高風險優先 LLM)。"""
    from modules.notify_center import notify_source_df, send_for_row
    src = notify_source_df()
    hit = src[src["id"] == int(lid)]
    if len(hit):
        mail = send_for_row(hit.iloc[0], platform_view=True, prefer_llm=True)
        st.toast(f"已模擬寄送至 {mail['to']}")
    else:
        st.toast("查無此房源的通知資料")


def _lime_panel(row: pd.Series):
    """展開於房源列下方:Top-3 LIME 原因 + 單筆發送鈕。"""
    lid = int(row["id"])
    with st.spinner("計算風險歸因 …"):
        reasons = _lime_reasons(lid, top=3)
    if reasons:
        for zh, dpp in reasons:
            # 推高風險=danger、降低風險=success,與全站「紅=要處理」語意一致
            role = "danger" if dpp > 0 else "success"
            sign = "推高" if dpp > 0 else "降低"
            st.markdown(
                f"<div style='border-left:4px solid var(--sa-{role});"
                f"background:var(--sa-surface);"
                f"border-radius:0 var(--sa-radius-sm) var(--sa-radius-sm) 0;"
                f"padding:9px 14px;margin:6px 0;'><b>{zh}</b> — {sign}空屋風險 "
                f"<span style='color:var(--sa-{role});font-weight:700;'>"
                f"{dpp:+.2f} 個百分點</span></div>", unsafe_allow_html=True)
    else:
        st.caption("此房源無足夠特徵可解釋。")
    ui_kit.primary_button("✉️ 產生此房源輔導通知", key=f"rm_send1_{lid}",
                          on_click=_send_single, args=(lid,))


def _listing_rows(shown: pd.DataFrame):
    """房源列:每列 = [checkbox][可點ID][其他欄位];點ID展開 LIME 面板。"""
    expanded = st.session_state.get("rm_expanded_id")
    widths = [0.5, 1.3, 1.0, 0.9, 1.0, 0.9, 1.0, 1.0]
    ui_kit.table_header_row(
        ["選取", "房源ID", "行政區", "房型", "每晚房價",
         "風險分數", "警報層級", "房東ID"], widths)
    for _, r in shown.iterrows():
        lid = int(r["id"])
        c = st.columns(widths)
        c[0].checkbox("選取", key=f"rm_sel_{lid}", label_visibility="collapsed")
        c[1].button(f"#{lid} ▸", key=f"rm_lst_{lid}", type="tertiary",
                    on_click=_toggle_expand, args=(lid,))
        c[2].markdown(str(r["neighbourhood_cleansed"]))
        c[3].markdown(ROOM_ZH.get(r["room_type"], str(r["room_type"])))
        c[4].markdown(f"${pd.to_numeric(r['price'], errors='coerce'):,.0f}")
        c[5].markdown(f"{pd.to_numeric(r['prob'], errors='coerce'):.0%}")
        # 等級改用 RiskBadge:與統計卡、圖表、詳細頁同名同色
        c[6].markdown(ui_kit.risk_badge(r["tier"]), unsafe_allow_html=True)
        c[7].markdown(f"#{int(r['host_id'])}")
        if expanded == lid:
            _lime_panel(r)


_BATCH_BAR_CSS = """
<style>
/* 批次派信列:置於房源表格上方的一般區塊
   (原為 position:fixed 底部浮動列,左側會被側邊欄遮住,故改置頂) */
.st-key-rm-batch-bar {
  background: var(--sa-surface); border: 1px solid var(--sa-border);
  border-left: 4px solid var(--sa-primary); border-radius: var(--sa-radius-md);
  padding: var(--sa-space-2) var(--sa-space-4); margin: 4px 0 10px;
}
</style>
"""


def _select_ids(ids):
    for i in ids:
        st.session_state[f"rm_sel_{int(i)}"] = True


def _selected_ids() -> list:
    out = []
    for k, v in st.session_state.items():
        if str(k).startswith("rm_sel_") and v:
            try:
                out.append(int(str(k)[len("rm_sel_"):]))
            except ValueError:
                pass
    return out


def _send_batch():
    """批次:對所有勾選房源逐筆組信+模擬寄送(規則引擎,快且穩),清空勾選。"""
    from modules.notify_center import notify_source_df, send_for_row
    ids = _selected_ids()
    src = notify_source_df()
    ok = 0
    for lid in ids:
        hit = src[src["id"] == lid]
        if len(hit):
            send_for_row(hit.iloc[0], platform_view=True, prefer_llm=False)
            ok += 1
    _clear_selection()
    st.toast(f"批次模擬寄送完成:{ok} 筆")


def _batch_bar(shown_ids):
    """頂部批次派信列:全選 / 批次發送 / 清除選取(房東檢視不呼叫本函式)。

    置於房源表格「上方」,常駐顯示;未勾選時發送與清除鈕為 disabled。
    原本是底部 position:fixed 浮動列,左半部會被側邊欄蓋住,故改置頂。
    """
    sel = _selected_ids()
    st.markdown(_BATCH_BAR_CSS, unsafe_allow_html=True)
    with st.container(key="rm-batch-bar"):
        c = st.columns([2.3, 0.9, 1.25, 1])
        # D3(2026-07-24):筆數只在一個地方說 —— 「已選 N」在這行、
        # 「符合/顯示」在表格上方的 caption;按鈕標籤只寫動作,不再複述數字。
        c[0].markdown(f"**已選 {len(sel)} 間**　將對這些房源產生平台輔導通知"
                      if sel else "產生平台輔導通知　（先勾選左側方框）")
        with c[1]:
            ui_kit.secondary_button("☑ 全選", key="rm_select_all",
                                    on_click=_select_ids, args=(shown_ids,))
        with c[2]:
            ui_kit.primary_button("✉️ 批次發送", key="rm_batch_send",
                                  disabled=not sel, on_click=_send_batch)
        with c[3]:
            ui_kit.secondary_button("清除選取", key="rm_batch_clear",
                                    disabled=not sel,
                                    on_click=_clear_selection)


RISK_LEVEL_MAP = {
    "高風險": ["red", "高風險"],
    "觀察": ["yellow", "觀察", "中風險"],
    "安全": ["green", "安全", "低風險"],
}


def render_sidebar_filters(df: pd.DataFrame):
    """風險管理側欄篩選(警報層級/顯示筆數/風險分數區間/房東ID)。

    由後台頁的側欄在「風險管理」分頁時呼叫;寫入 rm_risk_levels/rm_topn/rm_prob/
    rm_host_filter,供 _render_listings 直接讀 session_state 使用。
    當切換至「房源管理」時才顯示警報層級選擇器；「房東管理」時則隱藏。
    """
    view = st.session_state.get("rm_view", "hosts")
    if view == "listings":
        st.multiselect("警報層級", ["高風險", "觀察", "安全"], default=[],
                       key="rm_risk_levels", placeholder="不選＝全部警報層級",
                       help="可複選高風險(紅)、觀察(黃)、安全(綠)")
    st.slider("顯示筆數", 20, 300, LISTING_LIMIT_DEFAULT, 20, key="rm_topn")
    st.slider("風險分數區間", 0.0, 1.0, (0.0, 1.0), 0.05, key="rm_prob")
    valid_ids = df["host_id"].astype(int).unique().tolist() if len(df) else []
    opts = [HOST_ALL] + sorted(valid_ids)
    if st.session_state.get("rm_host_filter", HOST_ALL) not in opts:
        st.session_state["rm_host_filter"] = HOST_ALL     # 掉出母體→重置(合法,widget 前)
    st.selectbox("房東ID(可打字搜尋)", opts, key="rm_host_filter",
                 format_func=lambda x: x if x == HOST_ALL else f"#{int(x)}")


def _listing_quadrant_filter_control(quad_df: pd.DataFrame | None) -> str | None:
    """房源檢視象限篩選器;回傳象限 key,「全部」回 None。

    缺實際入住資料(quad_df=None)時不顯示控制項並回 None,不擋既有流程。
    標籤帶上該象限的房源數,讓使用者點之前就知道規模。
    """
    if quad_df is None:
        return None
    counts = quadrant_listing_counts(quad_df)
    keys = [k for k in QD.ACTUAL_QUADRANT_ORDER if counts.get(k)]
    if not keys:
        return None
    n_listings = len(quad_df)
    opts = [None] + keys
    labels = {None: f"全部（{n_listings:,} 間）"}
    labels.update({k: f"{QD.ACTUAL_QUADRANTS[k]['label']}（{counts[k]:,} 間）"
                   for k in keys})
    return st.radio("依象限篩選房源", opts, key="rm_listing_quadrant",
                    format_func=lambda k: labels[k], horizontal=True)


def _focus_banner(focus_id: int, missing: bool):
    """跳轉鎖定的提示列:告訴使用者這是從哪裡來的、要不要清除鎖定。"""
    src = st.session_state.get("rm_focus_from", "其他分頁")
    c1, c2 = st.columns([5, 1])
    if missing:
        c1.warning(f"🎯 從「{src}」跳轉來的房源 #{focus_id}，"
                   "不在風險模型評估範圍內（可能是新上架房源或資料不足）。")
    else:
        c1.info(f"🎯 已鎖定房源 #{focus_id}（來自「{src}」），"
               "已在下方展開風險原因。")
    with c2:
        ui_kit.secondary_button("清除鎖定", key="rm_clear_focus",
                                on_click=_clear_focus)


def _render_listings(df: pd.DataFrame, cm: float, quad_df: pd.DataFrame | None = None):
    """房源檢視:象限篩選 + 讀側欄篩選 + 頂部批次派信列 + 房源列(可勾選/可展開)+ 通知紀錄。

    篩選 widget 已移至後台頁側欄(render_sidebar_filters),本函式僅讀取
    session_state 的 rm_risk_levels/rm_topn/rm_prob/rm_host_filter 以及象限 radio (rm_listing_quadrant)。
    """
    valid_ids = df["host_id"].astype(int).unique().tolist()
    topn = int(st.session_state.get("rm_topn", LISTING_LIMIT_DEFAULT))
    lo, hi = st.session_state.get("rm_prob", (0.0, 1.0))
    host_filter = resolve_host_filter(
        st.session_state.get("rm_host_filter", HOST_ALL), valid_ids)

    selected_levels = st.session_state.get("rm_risk_levels", [])
    tiers = []
    if selected_levels:
        for lvl in selected_levels:
            tiers.extend(RISK_LEVEL_MAP.get(lvl, [lvl]))
    else:
        tiers = None

    qkey = _listing_quadrant_filter_control(quad_df)

    fdf = filter_listings(df, tiers, lo, hi, host_filter, quadrant_key=qkey, quad_df=quad_df)
    shown = fdf.head(topn)

    # 從其他分頁跳轉鎖定的房源:不受風險分數區間/象限篩選限制,一律強制
    # 塞進清單最前面。用完整 df(而非套用篩選後的 fdf)查找,呼叫端不需要
    # 事先知道使用者目前的篩選狀態。
    focus_id = st.session_state.get("rm_focus_id")
    focus_missing = False
    if focus_id is not None:
        hit = df[df["id"].astype(int) == int(focus_id)]
        if len(hit) == 0:
            focus_missing = True
        elif int(focus_id) not in shown["id"].astype(int).tolist():
            shown = pd.concat([hit, shown], ignore_index=True)

    shown_ids = shown["id"].astype(int).tolist()

    _scope = f"🎯 已鎖定房東 #{host_filter}；" if host_filter is not None else ""
    _quad_scope = (f"象限「{QD.ACTUAL_QUADRANTS[qkey]['label']}」；"
                   if qkey and qkey in QD.ACTUAL_QUADRANTS else "")
    st.caption(f"{_scope}{_quad_scope}符合 {len(fdf):,} 間,顯示風險分數最高的 {len(shown):,} 間")

    if focus_id is not None:
        _focus_banner(focus_id, focus_missing)

    if not shown_ids:
        ui_kit.empty_state("目前條件下沒有房源",
                           hint="請改選其他象限、放寬側欄的風險分數區間，或改選房東。")
        return

    _batch_bar(shown_ids)
    # D4:派信流程由上方批次列自己說明,這裡只講「表格本身怎麼用」。
    note("點<b>房源ID</b>(藍色連結)可展開該房源的 LIME 風險原因。")
    _listing_rows(shown)
    _notify_log_section()


def _notify_log_section():
    """通知紀錄(單筆/批次共用 st.session_state['notify_log'])。"""
    ui_kit.section_header("通知紀錄")
    log = st.session_state.get("notify_log", [])
    if log:
        ui_kit.data_table(pd.DataFrame(log)[["房源", "收件者", "機率", "門檻",
                                             "觸發原因", "建議來源", "狀態",
                                             "時間"]],
                          height=230)
    else:
        ui_kit.empty_state(
            "尚無通知紀錄",
            hint="點房源 ID 展開後按「✉️ 產生此房源輔導通知」，或勾選房源後批次發送。",
            icon="✉️")


# ── 房東排行榜:可點欄位標題排序(遞增/遞減切換)──────────────
HOST_SORT_COLS = ["房源數", "高風險間數", "高風險占比",
                  "平均風險分數", "預估年營收"]


def _set_host_sort(col):
    """點欄位標題:同欄再點切換升/降序,換欄則預設遞減(大→小)。"""
    if st.session_state.get("rm_host_sort_col") == col:
        st.session_state["rm_host_sort_asc"] = \
            not st.session_state.get("rm_host_sort_asc", False)
    else:
        st.session_state["rm_host_sort_col"] = col
        st.session_state["rm_host_sort_asc"] = False   # 首次點=遞減


def _host_sort_arrow(col):
    """回傳該欄目前排序箭頭:▼遞減 / ▲遞增 / ⇅未排序(可點)。"""
    if st.session_state.get("rm_host_sort_col") == col:
        return "▲" if st.session_state.get("rm_host_sort_asc") else "▼"
    return "⇅"


def _quadrant_filter_control(quad_df: pd.DataFrame | None) -> str | None:
    """象限篩選器(取代原本的房東ID模糊查詢);回傳象限 key,「全部」回 None。

    缺實際入住資料(quad_df=None)時不顯示控制項並回 None,不擋既有流程。
    標籤帶上該象限的房東數,讓使用者點之前就知道規模。
    """
    if quad_df is None:
        return None
    counts = quadrant_host_counts(quad_df)
    keys = [k for k in QD.ACTUAL_QUADRANT_ORDER if counts.get(k)]
    if not keys:
        return None
    n_hosts = int(quad_df["host_id"].nunique())
    opts = [None] + keys
    labels = {None: f"全部（{n_hosts:,} 位）"}
    labels.update({k: f"{QD.ACTUAL_QUADRANTS[k]['label']}（{counts[k]:,} 位）"
                   for k in keys})
    return st.radio("依象限篩選房東", opts, key="rm_host_quadrant",
                    format_func=lambda k: labels[k], horizontal=True)


def _render_hosts(df: pd.DataFrame, cm: float, quad_df: pd.DataFrame | None = None):
    """房東檢視:象限篩選 + 可點房東ID排行榜(無勾選、無浮動列)。"""
    h = pa.host_risk_summary(df, cm)
    qkey = _quadrant_filter_control(quad_df)
    res = filter_hosts_by_quadrant(h, quad_df, qkey)
    # 使用者若點過欄位標題排序,套用其排序;否則維持風險/象限預設排序
    sort_col = st.session_state.get("rm_host_sort_col")
    sort_asc = bool(st.session_state.get("rm_host_sort_asc", False))
    if sort_col in res.columns:
        res = res.sort_values(sort_col, ascending=sort_asc, kind="mergesort")

    _capped = "(僅顯示前 %d 位)" % LEADERBOARD_LIMIT \
        if len(res) >= LEADERBOARD_LIMIT else ""
    if sort_col:
        _order = f"依「{sort_col}」{'遞增' if sort_asc else '遞減'}排序"
    elif qkey:
        _order = "依「該象限間數 → 高風險占比」排序"
    else:
        _order = "依「高風險間數 → 高風險占比」排序"
    _scope = (f"{QD.ACTUAL_QUADRANTS[qkey]['label']}(名下至少 1 間)"
              if qkey else "全部房東")
    st.caption(f"{_scope}:{len(res):,} 位 · {_order}{_capped}")
    note("點<b>房東ID</b>(藍色連結)即可下鑽該房東名下房源清單並派信;"
         "點欄位標題的箭頭可依該欄數字遞增/遞減排序。")
    if not len(res):
        ui_kit.empty_state("這個象限目前沒有房東",
                           hint="請改選其他象限，或放寬側欄的行政區／房型篩選。",
                           icon="🔍")
        return

    # 末欄為留白 spacer,讓資料欄靠左集中(欄距不再過寬)。
    # 表頭第一欄是純文字、其餘是可點排序按鈕,故不能整列交給 table_header_row,
    # 只有第一欄沿用它的樣式 class。
    # 有象限篩選時,在房源數之後插一欄「該象限間數」——使用者最想知道的是
    # 「這位房東有幾間中了我剛點的那一類」,不插的話得自己回去對四象限表。
    has_q = "該象限間數" in res.columns
    cols_show = list(HOST_SORT_COLS)
    if has_q:
        cols_show.insert(1, "該象限間數")
        widths = [1.4, 1.0, 1.5, 1.5, 1.2, 1.5, 1.5, 1.4]
    else:
        widths = [1.4, 1.0, 1.5, 1.2, 1.5, 1.5, 2.0]
    hdr = st.columns(widths, gap="small")
    hdr[0].markdown('<span class="sa-table-head-cell">房東ID</span>',
                    unsafe_allow_html=True)
    for i, col in enumerate(cols_show, start=1):
        label = ("🔴" if col == "高風險間數" else "") + col
        hdr[i].button(f"{label} {_host_sort_arrow(col)}",
                      key=f"rm_sort_{col}", type="tertiary",
                      on_click=_set_host_sort, args=(col,))
    for _, r in res.iterrows():
        hid = int(r["host_id"])
        c = st.columns(widths, gap="small")
        c[0].button(f"#{hid} ▸", key=f"rm_host_{hid}", type="tertiary",
                    on_click=_go_listings, args=(hid,))
        i = 1
        c[i].markdown(f"{int(r['房源數'])}"); i += 1
        if has_q:
            c[i].markdown(f"**{int(r['該象限間數'])}**"); i += 1
        c[i].markdown(f"{int(r['高風險間數'])}"); i += 1
        c[i].markdown(f"{float(r['高風險占比']):.0%}"); i += 1
        c[i].markdown(f"{float(r['平均風險分數']):.0%}"); i += 1
        c[i].markdown(_money(float(r['預估年營收'])))
