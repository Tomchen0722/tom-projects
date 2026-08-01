# -*- coding: utf-8 -*-
"""portfolio_sections.py — 後台分析新增分頁:房型獲利分析 / 前瞻驗證

獨立模組:pages/3_📊_後台分析.py 兩行接入,不影響既有沙盒與 SHAP 分頁。
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from modules import calendar_analytics as ca
from modules import design_tokens as T
from modules import platform_analytics as pa
from modules import ui_kit
from modules.data_loader import load_listings
from modules.ui_components import ROOM_JP, RTC, apply_theme, note

MODELS = Path(__file__).resolve().parent.parent / "models"
ROOM_ZH = ROOM_JP          # 房型中譯改吃全站唯一來源(原本本檔複製一份)
# 圖表房型固定順序(照附圖:整棟→飯店→私人套房→共用)
ROOM_ORDER = ["整棟出租", "飯店客房", "私人套房", "共用套房"]


@st.cache_data(show_spinner="計算房型獲利 …")
def _portfolio() -> pd.DataFrame:
    d = ca.portfolio_summary(load_listings())
    d["房型"] = d["room_type"].map(ROOM_ZH).fillna(d["room_type"])
    return d


# ════════════════════════════════════════════════════════════════
# 分頁:房型獲利分析
# ════════════════════════════════════════════════════════════════
def _scoped_portfolio() -> pd.DataFrame:
    """calendar 房型獲利母體套用側欄『行政區 / 房型』篩選。"""
    d = _portfolio()
    dist = st.session_state.get("pf_districts")
    rooms = st.session_state.get("pf_rooms")
    if dist:
        d = d[d["neighbourhood_cleansed"].isin(dist)]
    if rooms:
        d = d[d["room_type"].isin(rooms)]
    return d


def _fmt_k(v) -> str:
    """金額縮寫成 $520k;NaN 回空字串。"""
    if pd.isna(v):
        return ""
    return f"${v / 1000:,.0f}k"


def _district_order(d: pd.DataFrame, col: str = "neighbourhood_cleansed"):
    """依房源數由多到少排序行政區(熱門在上)。"""
    return (d.groupby(col).size().sort_values(ascending=False).index.tolist())


def render_portfolio_tab():
    if not ca.available():
        ui_kit.empty_state(
            "尚未產生檔期資料",
            hint="缺少 calendar 特徵檔，請先執行下列腳本產出。",
            cmd="python -X utf8 scripts/build_calendar_features.py",
            icon="⚙️")
        return
    d = _scoped_portfolio()
    if len(d) == 0:
        ui_kit.empty_state("目前篩選條件下沒有可分析房源",
                           hint="請放寬側欄的行政區／房型篩選。")
        return

    from modules.platform_sections import _money, commission
    cm = commission()

    # 2026-07-25 二版:全頁改成三個問句 + 白話答案。
    #   ① 我最賺錢的是什麼  ② 這些有沒有問題  ③ 要怎麼解決
    # 一版用了「收入池 / 落後同儕 / 保守可補回抽成」等需要解讀的詞,
    # 且百分比要換算,對非資料背景的觀眾負擔太大。二版規則:
    #   - 一律講「一年有幾天有人住」,不講已訂率百分比
    #   - 一律講「一年少賺多少」,不講需要解釋係數的可補回金額
    #   - 每段先給一句話答案,圖只是佐證
    year_rev = float(d["年營收估算"].sum() * cm)
    by_room = (d.groupby("房型")["年營收估算"].sum().mul(cm)
               .sort_values(ascending=False))

    top_room = str(by_room.index[0])
    top_room_rev = float(by_room.iloc[0])
    top_room_share = top_room_rev / year_rev if year_rev > 0 else 0.0
    top_room_count = int((d["房型"] == top_room).sum())

    ui_kit.stat_card_row([
        ("營運房源", f"{len(d):,} 間"),
        ("平台一年賺", _money(year_rev), f"平台抽成 {cm:.0%}", "primary"),
        ("最賺錢的房型", top_room),
        (top_room, f"{top_room_count:,} 間"),
        (f"{top_room}年收", _money(top_room_rev), f"佔 {top_room_share:.0%}", "success"),
    ])

    ui_kit.section_header("📊 平台營收結構與主力熱點")

    g1 = (by_room.reindex(ROOM_ORDER).dropna().sort_values(ascending=True))
    fig1 = go.Figure(go.Bar(
        x=g1.values, y=g1.index, orientation="h",
        marker_color=[RTC.get(r, T.COLOR["primary"]) for r in g1.index],
        text=[_money(v) for v in g1.values], textposition="outside",
        cliponaxis=False,
        hovertemplate="%{y}<br>平台一年賺 %{x:$,.0f}<extra></extra>"))
    apply_theme(fig1, h=260, legend=False).update_layout(
        xaxis_title="", yaxis_title="", xaxis=dict(showticklabels=False),
        margin=dict(l=20, r=90, t=10, b=20))
    st.plotly_chart(fig1, use_container_width=True)

    # 舊版這裡是 12 列 × 4 欄的熱力矩陣(48 個數字格),資訊量大但要逐格讀。
    # 改成「最賺錢的前 8 名組合」橫條,一眼就知道錢集中在哪。
    ui_kit.section_header("最賺錢的地區 × 房型（前 8 名）",
                          desc="錢集中在哪幾個地方")
    g2 = (d.groupby(["neighbourhood_cleansed", "房型"])["年營收估算"]
          .sum().mul(cm).nlargest(8).sort_values(ascending=True))
    labels = [f"{a}　{b}" for a, b in g2.index]
    fig2 = go.Figure(go.Bar(
        x=g2.values, y=labels, orientation="h",
        marker_color=T.COLOR["success"],
        text=[_money(v) for v in g2.values], textposition="outside",
        cliponaxis=False,
        hovertemplate="%{y}<br>平台一年賺 %{x:$,.0f}<extra></extra>"))
    apply_theme(fig2, h=340, legend=False).update_layout(
        xaxis_title="", yaxis_title="", xaxis=dict(showticklabels=False),
        margin=dict(l=20, r=90, t=10, b=20))
    st.plotly_chart(fig2, use_container_width=True)

    # ── ② 這些賺錢的房子,有沒有遇到什麼問題? ─────────────────
    # 「幾天算有問題」由使用者拉,gap / up 都在區塊內依當下門檻現算,
    # 所以 ②③ 的房子數、金額、名單會一起跟著動。
    up = render_gap_diagnosis(d, cm, _money)

    # ── ③ 要怎麼解決? ───────────────────────────────────────
    render_uplift_targeting(up, _money)

    # 舊版還有第 ④ 段「成長機會供需矩陣」(去哪招新房源)。它用的是模型預估
    # 空屋率 + 全體 listings,與本頁其他三段的口徑/母體都不同,同頁並列必須
    # 另外寫一大段口徑說明才不會誤導 —— 那正是本次要消滅的「需要解讀的東西」。
    # 函式 render_growth_opportunity() 保留未刪,要放回來只需在此加一行呼叫。
    note("金額是用<b>未來一年的訂房日曆</b>估算的,不是實際入帳金流;"
         "已排除整年關閉日曆、以及整年完全沒訂的房源。")


GROUP_COLOR = {"落後": "danger", "接近": "warning", "達標": "success"}
# 診斷分類 → 色調(與全站「紅=要處理、綠=沒事」語意一致)
DIAG_TONE = {"隱形危機": "danger", "模型有抓到": "warning", "未評估": "muted"}


@st.cache_data(show_spinner=False)
def _predictions() -> pd.DataFrame:
    """風險模型預測母體;缺檔回空表(annotate_model_view 會全標「未評估」)。"""
    from modules.feature_engineering import load_predictions
    p = load_predictions()
    return p if p is not None else pd.DataFrame()


def _peer_price(d: pd.DataFrame) -> pd.DataFrame:
    """同區同房型的中位價,供建議作法判斷「訂價是否偏高」。"""
    return (d.groupby(["neighbourhood_cleansed", "room_type"])["price"]
            .median().rename("peer_price").reset_index())


def _plain_num(v, kind) -> str:
    """比例用 %,整數就不要拖 .00 的小數尾巴(29.00 會讓人多看一眼)。"""
    if pd.isna(v):
        return "—"
    if kind == "flag":
        return f"{v:.0%}"
    return f"{v:,.0f}" if float(v).is_integer() else f"{v:,.2f}"


def _plain_verdict(diff, kind) -> str:
    """把 +0.4% / +10.2pp 這種要換算的數字,翻成一眼能讀的判定。"""
    if pd.isna(diff):
        return "—"
    d = diff if kind == "flag" else diff        # flag 是差值,其餘是相對差
    if abs(d) < 0.02:
        return "一樣"
    return "還更好" if d > 0 else "差一點"


def render_gap_diagnosis(d: pd.DataFrame, cm: float, money) -> pd.DataFrame:
    """② 這些房子有沒有問題 —— 用「一年有幾天有人住」講,不用百分比。

    門檻(幾天算有問題)由使用者自己拉,不寫死:落差分布是平滑遞減的,
    10/20/30/40 個百分點分別對應 37%/29%/19%/12% 的房源,沒有自然斷點,
    所以任何門檻都是營運判斷而不是資料事實。回傳依當下門檻算好的名單給 ③。

    結論刻意是否定的:比對表兩欄幾乎一樣,代表問題不是房子比較差,
    所以不端出品質輔導處方。
    """
    ui_kit.section_header(
        "📉 表現落後房源與營收損失診斷",
        desc="把每一間房子，跟「同一區、同一種房型」的其他房子放在一起比")

    # 用 number_input 而不是 slider:這個數字要能精確指定並記錄成營運規則
    # (「我們的標準是 90 天」),滑桿拉不準也講不清楚。
    # number_input 預設撐滿容器寬度,3 位數字撐一整欄太寬,用 columns 收窄。
    _in1, _ = st.columns([1, 3])
    days = int(_in1.number_input(
        "一年比鄰居少幾天有人住，才算「有問題」？",
        min_value=1, max_value=364, value=pa.LAGGARD_GAP_DAYS, step=1,
        key="pf_gap_days",
        help="這條線沒有標準答案，是營運上的判斷。設得越嚴（天數越大），"
             "被點名的房子越少、但每一間的問題越明顯。"
             "下面的房子數量、金額、名單都會跟著一起變。"))

    gap = pa.peer_gap_table(d, gap_threshold=days / pa.DAYS_PER_YEAR)
    if len(gap) == 0:
        ui_kit.empty_state(
            "沒有可以互相比較的房子",
            hint=f"同一區同一種房型至少要有 {pa.PEER_MIN_DEFAULT} 間才比得出來，"
                 "請放寬側欄的行政區／房型篩選。")
        return pa.uplift_ranking(gap, commission=cm)

    up = pa.uplift_ranking(gap, commission=cm)
    # 標上「風險模型怎麼看」+ 規則式建議作法。風險模型只吃靜態結構特徵,
    # 對「條件很好卻沒人訂」的房子給不出可行動的理由(它甚至會說安全),
    # 所以隱形危機那批改用實際訂房行為 + 同儕比價另外推建議。
    _pred = _predictions()
    up = pa.annotate_model_view(up, _pred)
    up = pa.explain_unevaluated(up, pa.model_coverage_cutoff(d, _pred))
    up = pa.suggest_actions(up, _peer_price(d))
    lag_n = len(up)
    lost = float(up["一年少賺"].sum()) if lag_n else 0.0
    lagd = gap[gap["分組"] == "落後"]
    okd = gap[gap["分組"] == "達標"]

    ui_kit.stat_card_row([
        ("有問題的房子", f"{lag_n:,} 間",
         f"一年比鄰居少 {days} 天以上有人住", "danger"),
        ("這些房子讓平台一年少賺", money(lost), "和鄰居的差距", "danger"),
    ])
    if lag_n == 0:
        note(f"目前這條線拉到「少 {days} 天以上」，沒有任何房子被點名。"
             "把天數調小一點就會出現。")
        return up

    # ── 按房型分組的天數對比圖 ──
    ui_kit.section_header("一年 365 天裡，有幾天有人住？")

    categories = []
    lag_vals = []
    ok_vals = []
    lag_texts = []
    ok_texts = []

    for r in ROOM_ORDER:
        r_lagd = lagd[lagd["房型"] == r]
        r_okd = okd[okd["房型"] == r]
        c_lag_n = len(r_lagd)
        c_ok_n = len(r_okd)
        if c_lag_n == 0 and c_ok_n == 0:
            continue
        c_lag_days = float(r_lagd["booked_days"].mean()) if c_lag_n else 0.0
        c_ok_days = float(r_okd["booked_days"].mean()) if c_ok_n else 0.0

        categories.append(r)
        lag_vals.append(c_lag_days)
        ok_vals.append(c_ok_days)
        lag_texts.append(f"{c_lag_days:.0f} 天 ({c_lag_n:,}間)" if c_lag_n else "無")
        ok_texts.append(f"{c_ok_days:.0f} 天 ({c_ok_n:,}間)" if c_ok_n else "無")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="有問題的房子",
        x=categories, y=lag_vals,
        marker_color=T.COLOR["danger"],
        text=lag_texts, textposition="outside", cliponaxis=False,
        hovertemplate="%{x} · 有問題的房子<br>一年平均 %{y:.0f} 天有人住<extra></extra>"
    ))
    fig.add_trace(go.Bar(
        name="隔壁同型的房子",
        x=categories, y=ok_vals,
        marker_color=T.COLOR["success"],
        text=ok_texts, textposition="outside", cliponaxis=False,
        hovertemplate="%{x} · 隔壁同型的房子<br>一年平均 %{y:.0f} 天有人住<extra></extra>"
    ))
    apply_theme(fig, h=340, legend=True).update_layout(
        barmode="group",
        xaxis_title="", yaxis_title="", yaxis=dict(range=[0, 390]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=30, b=30))
    st.plotly_chart(fig, use_container_width=True)
    return up


def render_uplift_targeting(up: pd.DataFrame, money):
    """③ 要怎麼解決 —— 不是全部一起救,先救差最多的那幾間。

    金額是「和鄰居的差距」,是描述不是承諾:沒有宣稱做了什麼就能補回來。
    """
    ui_kit.section_header(
        "🎯 優先搶救房源與投入效益",
        desc="這些房子不用全部一起處理。把它們照「一年少賺多少」排好，"
             "先處理最前面的就好")
    if len(up) == 0:
        ui_kit.empty_state("目前的篩選條件下，沒有找到有問題的房子",
                           hint="請放寬側欄的行政區／房型篩選。")
        return

    total = float(up["一年少賺"].sum())

    # 刻意不設 max_value:上限會隨 ② 的門檻變動,若使用者先填了大數字、
    # 之後把門檻調嚴使名單變短,帶上限的 number_input 會因為 session 值
    # 超出範圍而報錯。改為不設上限、在程式裡夾住,並在夾住時說明。
    _in2, _ = st.columns([1, 3])
    want = int(_in2.number_input(
        "這一季有能力先處理幾間？", min_value=1, value=300, step=10,
        key="pf_topn",
        help="營運端的人力決定這個數字。填多少，下面的金額與名單就跟著算。"))
    topn = min(want, len(up))
    top_sum = float(up["累積金額"].iloc[topn - 1])
    top_share = float(up["累積占比"].iloc[topn - 1])
    effort = len(up) / topn if topn else 1.0

    ui_kit.stat_card_row([
        (f"先處理最嚴重的 {topn:,} 間", money(top_sum),
         f"占全部損失的 {top_share:.0%}", "success"),
        (f"全部 {len(up):,} 間都處理", money(total),
         f"多花 {effort:.1f} 倍力氣"),
    ])
    if want > len(up):
        note(f"目前只找到 {len(up):,} 間有問題的房子，比你填的 {want:,} 間少，"
             f"所以下面是全部 {len(up):,} 間。"
             "想多找一些，把上面「少幾天算有問題」的天數調小。")

    # 舊版是帕累托累積曲線(要看得懂累積分布才行)。改成兩根長條直接對比:
    # 力氣差幾倍、拿回來的錢差幾倍,一眼就看得出來。標題同樣走 section_header。
    ui_kit.section_header(
        f"只處理 {topn:,} 間，就能拿回 {top_share:.0%} 的損失")
    fig = go.Figure(go.Bar(
        x=[f"只處理最嚴重的 {topn:,} 間", f"全部 {len(up):,} 間都處理"],
        y=[top_sum, total],
        marker_color=[T.COLOR["success"], T.COLOR["muted"]],
        text=[money(top_sum), money(total)],
        textposition="outside", cliponaxis=False, width=[0.45, 0.45],
        hovertemplate="%{x}<br>一年可以找回 %{y:$,.0f}<extra></extra>"))
    apply_theme(fig, h=320, legend=False).update_layout(
        xaxis_title="", yaxis_title="", yaxis=dict(showticklabels=False),
        margin=dict(l=20, r=20, t=20, b=30))
    st.plotly_chart(fig, use_container_width=True)

    _render_diagnosis_split(up.head(topn), money)

    ui_kit.section_header(
        "📋 優先搶救房源名單",
        desc="這份名單可以直接交給營運團隊")

    _in_show, _ = st.columns([1, 3])
    want_show = int(_in_show.number_input(
        f"{topn:,} 間的前幾間？", min_value=1, value=20, step=5,
        key="pf_nshow",
        help="決定下方名單要顯示前幾間房源"))
    nshow = min(want_show, topn, len(up))

    # 先取出「一年少賺」前 nshow 間的名單，再依使用者點選的欄位在名單內排序（不帶出超過 nshow 的房源）
    rows_to_show = up.head(nshow).copy()

    sort_col = st.session_state.get("pf_up_sort_col")
    sort_asc = bool(st.session_state.get("pf_up_sort_asc", False))
    col_map = {
        "行政區": "neighbourhood_cleansed",
        "房型": "房型",
        "一年有幾天有人住": "自己有人住天數",
        "隔壁同型的房子": "鄰居有人住天數",
        "一年少賺": "一年少賺",
        "風險模型怎麼看": "診斷分類",
    }
    if sort_col in col_map and col_map[sort_col] in rows_to_show.columns:
        rows_to_show = rows_to_show.sort_values(col_map[sort_col], ascending=sort_asc, kind="mergesort").reset_index(drop=True)

    note("點<b>房源編號</b>可以跳到「風險管理」查看這間房子被判定風險的原因；"
         "點<b>欄位標題箭頭</b>（如「行政區」、「一年少賺」）可依該欄遞增/遞減排序。")
    _listing_link_rows(rows_to_show, money)


def _render_diagnosis_split(sel: pd.DataFrame, money):
    """③ 的分流:同樣是「訂不到」,風險模型抓得到的和抓不到的要做不同的事。"""
    if "診斷分類" not in sel.columns:
        return
    n_blind = int((sel["診斷分類"] == "隱形危機").sum())
    n_caught = int((sel["診斷分類"] == "模型有抓到").sum())
    n_none = int((sel["診斷分類"] == "未評估").sum())
    if n_blind + n_caught + n_none == 0:
        return

    def _lost(kind):
        return float(sel[sel["診斷分類"] == kind]["一年少賺"].sum())

    ui_kit.section_header(
        "這些房子，風險模型有沒有抓到？",
        desc="風險模型看的是房子的「條件」（地段、房型、規模），"
             "這一頁看的是「實際上有沒有人住」。兩邊不一致的那批最需要注意")
    ui_kit.stat_card_row([
        ("風險模型也覺得有問題", f"{n_caught:,} 間",
         f"一年少賺 {money(_lost('模型有抓到'))}", "warning"),
        ("模型說沒事、實際卻沒人住", f"{n_blind:,} 間",
         f"一年少賺 {money(_lost('隱形危機'))}", "danger"),
        ("模型沒評估到", f"{n_none:,} 間",
         f"一年少賺 {money(_lost('未評估'))}", "muted"),
    ])
    if n_none:
        # 2026-07-25 查證:一開始以為是「評論太少、資料不足」,實際比對後發現
        # 是乾淨的時間切點 —— 已納入模型的房源 host_since 最晚 2024-09-30,
        # 未納入的最早 2024-10-11,全站 392 間**完全不重疊(0/392)**。
        # 所以這是訓練資料快照的時間差,不是資料品質問題。
        st.caption("💡 風險模型的訓練資料有時間切點，這些房源的房東是在切點"
                   "之後才加入平台的，所以模型還沒看過它們。"
                   "（全站 392 間屬於這種情況，加入日期與模型資料完全不重疊）"
                   "等模型下次重新訓練就會納入。這是資料的時間差，"
                   "不是本頁計算錯誤。")

    if n_caught:
        note("🟡 <b>風險模型也覺得有問題的那批</b>：走既有流程 —— 點下方名單的"
             "房源編號跳到「風險管理」，模型會列出它判定風險的理由，"
             "確認後直接寄輔導通知。")

    if n_blind == 0:
        return

    blind = sel[sel["診斷分類"] == "隱形危機"]
    note("🔴 <b>模型說沒事、實際卻沒人住的那批（隱形危機）</b>："
         "這批<b>不能</b>走輔導通知流程。風險模型對它們的歸因只會列出"
         "「地段好、床數夠」這類優點，寄出去等於告訴房東「你這間很棒」，"
         "方向是反的。以下建議改用<b>實際訂房行為與同儕比價</b>推出，"
         "是規則判斷、不是模型預測：")

    g = (blind.groupby("建議作法")
         .agg(房源數=("listing_id", "size"), 少賺=("一年少賺", "sum"))
         .sort_values("少賺", ascending=False).reset_index())
    show = pd.DataFrame({
        "幾間": g["房源數"].map(lambda v: f"{v:,} 間"),
        "一年少賺": g["少賺"].map(money),
        "建議作法": g["建議作法"],
    })
    ui_kit.data_table(show, height=240, wrap=True,
                      widths={"幾間": "70px", "一年少賺": "100px"})


_TOOLTIP_CSS = """
<style>
/* 「風險模型怎麼看」徽章的滑鼠提示:純 CSS,不用 JS;取代原本每列常駐的
   caption 文字,只有滑鼠移上去才浮現,列表不會被說明文字撐得更長。 */
.pf-tip{position:relative;display:inline-block;cursor:help;}
.pf-tip .pf-tip-bubble{
  visibility:hidden;opacity:0;position:absolute;z-index:50;
  bottom:130%;left:50%;transform:translateX(-50%);
  width:max-content;max-width:220px;
  background:var(--sa-ink);color:#fff;
  padding:6px 10px;border-radius:var(--sa-radius-sm);
  font-size:12px;line-height:1.4;font-weight:400;white-space:normal;
  box-shadow:0 6px 20px rgba(0,0,0,.18);
  transition:opacity .12s ease;pointer-events:none;}
.pf-tip:hover .pf-tip-bubble{visibility:visible;opacity:1;}
</style>
"""


def _set_pf_up_sort(col):
    """點欄位標題:同欄再點切換升/降序,換欄則預設遞減(大→小)。"""
    if st.session_state.get("pf_up_sort_col") == col:
        st.session_state["pf_up_sort_asc"] = \
            not st.session_state.get("pf_up_sort_asc", False)
    else:
        st.session_state["pf_up_sort_col"] = col
        st.session_state["pf_up_sort_asc"] = False   # 首次點=遞減


def _pf_up_sort_arrow(col):
    """回傳該欄目前排序箭頭:▼遞減 / ▲遞增 / ⇅未排序(可點)。"""
    if st.session_state.get("pf_up_sort_col") == col:
        return "▲" if st.session_state.get("pf_up_sort_asc") else "▼"
    return "⇅"


def _jump_to_risk(listing_id):
    """③名單「房源編號」的 on_click:切到風險管理房源檢視,鎖定並展開它。"""
    from modules import risk_cockpit_sections as rc
    rc.jump_to_listing(listing_id, from_label="營收與成長")


def _listing_link_rows(rows: pd.DataFrame, money):
    """③名單:每列 = [名次][可點房源編號][其他欄位],跳轉沿用風險管理的
    房源列樣式(st.columns),第一與第二欄位不含排序按鈕,其餘欄位附帶遞增/遞減排序按鈕。
    """
    has_diag = "診斷分類" in rows.columns
    widths = ([0.4, 1.2, 1.0, 0.9, 1.5, 1.5, 1.2, 1.5] if has_diag
              else [0.4, 1.2, 1.0, 1.0, 1.5, 1.5, 1.4])
    cols_spec = [
        ("第", False, None),
        ("房源編號", False, None),
        ("行政區", True, "行政區"),
        ("房型", True, "房型"),
        ("一年有幾天有人住", True, "一年有幾天有人住"),
        ("隔壁同型的房子", True, "隔壁同型的房子"),
        ("一年少賺", True, "一年少賺"),
    ]
    if has_diag:
        cols_spec.append(("風險模型怎麼看", True, "風險模型怎麼看"))
        st.markdown(_TOOLTIP_CSS, unsafe_allow_html=True)

    hdr = st.columns(widths, gap="small")
    for idx, (label, sortable, key_col) in enumerate(cols_spec):
        if not sortable:
            hdr[idx].markdown(f'<span class="sa-table-head-cell">{label}</span>',
                              unsafe_allow_html=True)
        else:
            hdr[idx].button(f"{label} {_pf_up_sort_arrow(key_col)}",
                            key=f"pf_sort_{key_col}", type="tertiary",
                            on_click=_set_pf_up_sort, args=(key_col,))

    for _, r in rows.iterrows():
        lid = int(r["listing_id"])
        c = st.columns(widths, gap="small")
        c[0].markdown(str(int(r["名次"])))
        c[1].button(f"#{lid} ▸", key=f"pf_jump_{lid}", type="tertiary",
                    on_click=_jump_to_risk, args=(lid,))
        c[2].markdown(str(r["neighbourhood_cleansed"]))
        c[3].markdown(str(r["房型"]))
        c[4].markdown(f"{r['自己有人住天數']:.0f} 天")
        c[5].markdown(f"{r['鄰居有人住天數']:.0f} 天")
        c[6].markdown(money(float(r["一年少賺"])))
        if has_diag:
            diag = str(r["診斷分類"])
            tone = DIAG_TONE.get(diag, "muted")
            label = {"隱形危機": "🔴 說沒事卻沒人住",
                     "模型有抓到": "🟡 模型也抓到",
                     "未評估": "⚪ 沒評估到"}.get(diag, diag)
            badge = f'<span class="sa-badge sa-badge-{tone}">{label}</span>'
            reason = str(r.get("未評估原因") or "")
            if reason:
                badge = (f'<span class="pf-tip">{badge}'
                         f'<span class="pf-tip-bubble">{reason}</span></span>')
            c[7].markdown(badge, unsafe_allow_html=True)


def render_tenure_strategy(d: pd.DataFrame):
    """長短租策略分析:依 calendar 的最低入住天數分群比較填充率與營收。"""
    m = ca.healthy_metrics()[["listing_id", "min_nights_median",
                              "min_nights_varies", "booked_rate",
                              "booked_days", "gap_longest_30d"]]
    j = d.merge(m, on="listing_id", how="inner", suffixes=("", "_m"))
    if j.empty:
        return

    def _seg(v):
        if pd.isna(v):
            return "未知"
        if v <= 1:
            return "① 單晚起租(1 晚)"
        if v <= 3:
            return "② 短租(2~3 晚)"
        if v <= 6:
            return "③ 中短租(4~6 晚)"
        if v < 28:
            return "④ 週租型(7~27 晚)"
        return "⑤ 長租型(≥28 晚)"

    j["租期策略"] = j["min_nights_median"].map(_seg)
    order = ["① 單晚起租(1 晚)", "② 短租(2~3 晚)", "③ 中短租(4~6 晚)",
             "④ 週租型(7~27 晚)", "⑤ 長租型(≥28 晚)"]
    g = (j[j["租期策略"].isin(order)]
         .groupby("租期策略")
         .agg(房源數=("listing_id", "size"),
              平均已訂率=("booked_rate", "mean"),
              平均已訂天數=("booked_days", "mean"),
              中位每晚價=("price", "median"),
              中位年營收=("年營收估算", "median"))
         .reindex(order).dropna(how="all").reset_index())

    ui_kit.section_header(
        "長短租策略分析",
        desc="以 calendar 每日最低入住天數判定。市場實測：34% 房源的最低入住天數"
             "逐日變動；30 晚設定達 32.8 萬筆日資料，是短租長租化的訊號")

    _lt = j[j["min_nights_median"] >= 28]
    _st = j[j["min_nights_median"] <= 3]
    ui_kit.stat_card_row([
        ("長租型房源（≥28 晚）", f"{len(_lt):,} 間", f"占 {len(_lt)/len(j):.0%}"),
        ("長租型平均已訂率",
         f"{_lt['booked_rate'].mean():.0%}" if len(_lt) else "—"),
        ("短租型（≤3 晚）平均已訂率",
         f"{_st['booked_rate'].mean():.0%}" if len(_st) else "—"),
        ("採動態天數策略", f"{int(j['min_nights_varies'].sum()):,} 間",
         f"占 {j['min_nights_varies'].mean():.0%}"),
    ])

    c1, c2 = st.columns([1.25, 1])
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=g["租期策略"], y=g["平均已訂率"] * 100,
                             name="平均已訂率 (%)",
                             marker_color=T.COLOR["primary"],
                             text=(g["平均已訂率"] * 100).round(0),
                             textposition="outside"))
        fig.add_trace(go.Scatter(x=g["租期策略"], y=g["中位年營收"] /
                                 max(g["中位年營收"].max(), 1) * 100,
                                 name="中位年營收(相對比例)",
                                 mode="lines+markers",
                                 line=dict(color=T.COLOR["secondary"], width=2,
                                           dash="dot")))
        apply_theme(fig, h=350).update_layout(
            title="不同租期策略的檔期填充表現",
            yaxis_title="已訂率 (%) / 營收相對比例",
            legend=dict(orientation="h", y=-0.25),
            margin=dict(l=40, r=20, t=50, b=90))
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        ui_kit.data_table(g.assign(
            平均已訂率=g["平均已訂率"].map("{:.0%}".format),
            平均已訂天數=g["平均已訂天數"].round(0),
            中位每晚價=g["中位每晚價"].map("${:,.0f}".format),
            中位年營收=g["中位年營收"].map("${:,.0f}".format)), height=250)

    if len(g) >= 2:
        best_rate = g.loc[g["平均已訂率"].idxmax()]
        best_rev = g.loc[g["中位年營收"].idxmax()]
        note(f"<b>填充率最高</b>:{best_rate['租期策略']}"
             f"(平均已訂率 {best_rate['平均已訂率']:.0%});"
             f"<b>營收最高</b>:{best_rev['租期策略']}"
             f"(中位年營收 ${best_rev['中位年營收']:,.0f})。"
             f"若兩者不同組,代表「訂得滿」與「賺得多」是不同策略 —— "
             f"高填充率常來自低價長住,單價與周轉需權衡。")
    note("⚠️ 長租型(≥28 晚)在台灣多為<b>規避短租法規</b>或轉向月租市場;"
         "其 calendar『不可訂』比例高不必然代表訂滿,也可能是房東封鎖短租日期。"
         "此分析呈現市場策略分布,不作為法規建議。")


# ════════════════════════════════════════════════════════════════
# 分頁:前瞻驗證(用真實未來資料檢驗模型)
# ════════════════════════════════════════════════════════════════
def render_forward_validation_tab():
    path = MODELS / "forward_validation.json"
    if not path.exists():
        ui_kit.empty_state(
            "尚未產生前瞻驗證結果",
            hint="缺少 models/forward_validation.json，請先執行下列腳本產出。",
            cmd="python -X utf8 scripts/build_calendar_features.py",
            icon="⚙️")
        return
    fv = json.loads(path.read_text(encoding="utf-8"))
    if "error" in fv:
        ui_kit.empty_state("前瞻驗證無法計算", hint=fv["error"])
        return

    ui_kit.section_header(
        "前瞻驗證：用真實未來資料檢驗模型",
        desc=f"特徵快照 {fv['listings_scraped']} → 真實結果 "
             f"{fv['calendar_scraped']}（相隔 {fv['gap_months']} 個月）· "
             f"可對照 {fv['n_matched']:,} 間房源")
    note("這不是交叉驗證,而是<b>真正的時間外推驗證</b>:模型只看得到 2025 年 9 月的特徵,"
         "而答案來自 9 個月後才爬取的 calendar。一般專題只能報交叉驗證分數,"
         "本平台能用真實未來資料檢驗 —— 誠實呈現衰退,比宣稱高分更有價值。")

    # ── 指標對照 ──
    rows = [
        {"指標": "模型 A 迴歸 R²", "交叉驗證(GroupKFold OOF)": 0.243,
         "真實未來(前瞻)": round(fv["reg_r2"], 3)},
        {"指標": "模型 B 分類 AUC", "交叉驗證(GroupKFold OOF)": 0.716,
         "真實未來(前瞻)": round(fv["clf_auc"], 3)},
        {"指標": "🔴 紅色門檻 Precision", "交叉驗證(GroupKFold OOF)": 0.69,
         "真實未來(前瞻)": round(fv["red"]["precision"], 2)},
        {"指標": "🔴 紅色門檻 Recall", "交叉驗證(GroupKFold OOF)": 0.27,
         "真實未來(前瞻)": round(fv["red"]["recall"], 2)},
        {"指標": "🟡 黃色以上 Recall", "交叉驗證(GroupKFold OOF)": 0.70,
         "真實未來(前瞻)": round(fv["yellow"]["recall"], 2)},
    ]
    df = pd.DataFrame(rows)
    df["衰退"] = (df["真實未來(前瞻)"] - df["交叉驗證(GroupKFold OOF)"]).round(3)

    c1, c2 = st.columns([1.1, 1])
    with c1:
        ui_kit.data_table(df, height=240)
        ui_kit.stat_card_row([
            ("真實高風險率", f"{fv['real_high_risk_rate']:.0%}"),
            ("真實平均空屋率", f"{fv['real_vacancy_mean']:.0%}",
             f"模型預測 {fv['pred_vacancy_mean']:.0%}"),
            ("前瞻 AUC", f"{fv['clf_auc']:.3f}", "vs OOF 0.716"),
        ])
    with c2:
        fig = go.Figure()
        cats = ["迴歸 R²", "分類 AUC", "紅層 Precision"]
        fig.add_trace(go.Bar(name="交叉驗證(OOF)", x=cats,
                             y=[0.243, 0.716, 0.69],
                             marker_color=T.COLOR["warning"],
                             text=["0.243", "0.716", "0.69"],
                             textposition="outside"))
        fig.add_trace(go.Bar(name="真實未來(前瞻)", x=cats,
                             y=[fv["reg_r2"], fv["clf_auc"],
                                fv["red"]["precision"]],
                             marker_color=T.COLOR["primary"],
                             text=[f"{fv['reg_r2']:.3f}", f"{fv['clf_auc']:.3f}",
                                   f"{fv['red']['precision']:.2f}"],
                             textposition="outside"))
        apply_theme(fig, h=330).update_layout(
            barmode="group", yaxis_range=[0, 0.95],
            title="交叉驗證 vs 真實未來", margin=dict(l=40, r=20, t=50, b=30))
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    ui_kit.section_header("衰退原因分析與改善方向")
    cause = pd.DataFrame([
        {"原因": "① 時間跨度過長(9 個月)",
         "說明": "特徵取自 2025-09,答案是 2026-06 起的檔期;期間市場、定價、經營者皆已變動",
         "改善方向": "縮短預測視野至 1~3 個月,或改用滾動更新的特徵"},
        {"原因": "② 標籤定義被汙染",
         "說明": "calendar 的『不可訂』同時包含已預訂與房東主動封鎖,"
                 "使『真實空屋率』並非純粹的市場需求結果",
         "改善方向": "取得多期 calendar 快照,以狀態轉變(可訂→不可訂)辨識真實訂單"},
        {"原因": "③ 房源母體不同",
         "說明": "兩批爬取的房源集合有差異,僅 4,940 間重疊,"
                 "存續下來的房源本身即帶有存活偏誤",
         "改善方向": "以固定追蹤群組(panel)重新評估"},
        {"原因": "④ 迴歸目標本身難以外推",
         "說明": "連續空屋率受季節、事件影響大;分類(是否高風險)較穩健,"
                 "故 AUC 衰退幅度遠小於 R²",
         "改善方向": "對外仍以分類雙層警報為主,迴歸值只作參考"},
    ])
    ui_kit.data_table(cause, wrap=True, scroll=False)
    note("<b>結論</b>:分類模型(AUC 0.632)在 9 個月後仍具實用鑑別力,"
         "雙層警報的黃色層仍抓到 63% 的真實高風險房源;但迴歸的連續空屋率預測"
         "不應被當作精確數值使用。平台現行設計(以分類機率決定等級、迴歸僅作輔助顯示)"
         "與此驗證結果一致。")


# ════════════════════════════════════════════════════════════════
# 區塊:成長機會(行政區 x 房型 供需缺口)
# ════════════════════════════════════════════════════════════════
# 供需狀態三級:現有兩級標籤 → 附圖用語 +(狀態碼, 語意角色)
# 色一律取 TINT[role]["border"] —— 熱力圖格子要能承載深色文字,
# 用同一組淡底色系才不會出現「三個角色三種來歷不明的綠」。
STATUS_MAP = {
    "🟢 招募缺口": ("缺口市場（建議招募）", 2, "success"),
    "⚪ 一般":     ("觀察中", 1, "warning"),
    "🔴 供給飽和": ("已飽和", 0, "neutral"),
}
STATUS_FILL = {role: T.TINT[role]["border"]
               for role in ("success", "warning", "neutral")}
# 3 段離散色階(中性→暖黃→綠),對應狀態碼 0 / 1 / 2
STATUS_SCALE = [[0.0, STATUS_FILL["neutral"]], [0.333, STATUS_FILL["neutral"]],
                [0.334, STATUS_FILL["warning"]], [0.666, STATUS_FILL["warning"]],
                [0.667, STATUS_FILL["success"]], [1.0, STATUS_FILL["success"]]]


def render_growth_opportunity():
    """圖3:行政區 × 房型 成長機會供需矩陣(缺口市場 / 觀察中 / 已飽和)。"""
    from modules import platform_analytics as pa
    from modules.platform_sections import ROOM_ZH as _RZ
    from modules.platform_sections import _money, commission, guard_scope

    ui_kit.section_header(
        "成長機會供需矩陣",
        desc="行動：接下來去哪賺 —— 需求強（空屋率低於中位）且供給薄"
             "（房源數低於中位）= 建議招募的缺口市場；反之為已飽和、"
             "不宜再增供給。點格子看 hover 明細")

    df = guard_scope()
    if df is None:
        return
    cm = commission()

    g = pa.supply_demand_matrix(df, min_listings=15)
    if len(g) == 0:
        ui_kit.empty_state(
            "無法評估供需",
            hint="篩選範圍內沒有房源數 ≥ 15 的『行政區 × 房型』組合，"
                 "請放寬側欄篩選。")
        return
    g["房型中文"] = g["房型"].map(_RZ).fillna(g["房型"])
    g["狀態"] = g["機會標籤"].map(lambda s: STATUS_MAP.get(s, ("觀察中", 1, ""))[0])
    g["_code"] = g["機會標籤"].map(lambda s: STATUS_MAP.get(s, ("", 1, ""))[1])

    gap = g[g["機會標籤"] == "🟢 招募缺口"]
    sat = g[g["機會標籤"] == "🔴 供給飽和"]
    ui_kit.stat_card_row([
        ("可評估組合", f"{len(g):,} 組"),
        ("缺口市場組合", f"{len(gap):,} 組", "建議招募", "success"),
        ("已飽和組合", f"{len(sat):,} 組", "不宜再增供給"),
    ])

    rows = _district_order(g, "行政區")
    cols = [c for c in ROOM_ORDER if c in g["房型中文"].unique()]

    def _piv(val):
        return (g.pivot_table(index="行政區", columns="房型中文", values=val,
                              aggfunc="first")
                .reindex(index=rows, columns=cols))

    z = _piv("_code").values
    p_vac, p_n, p_pr = _piv("平均空屋率"), _piv("房源數"), _piv("中位價格")
    p_lab = _piv("狀態")

    # customdata 全部預格式化為字串,避免 str/數值混型被 numpy 轉型後
    # 導致 hovertemplate 的數值格式碼失效
    txt, cd = [], []
    for i in range(len(rows)):
        trow, crow = [], []
        for j in range(len(cols)):
            v, n = p_vac.values[i][j], p_n.values[i][j]
            if pd.isna(v):
                trow.append("")
                crow.append(["—", "—", "—", "—"])
            else:
                trow.append(f"空屋 {v:.0%}<br>{int(n)} 間")
                crow.append([str(p_lab.values[i][j]), f"{v:.0%}",
                             f"{int(n):,}", f"${p_pr.values[i][j]:,.0f}"])
        txt.append(trow)
        cd.append(crow)

    fig = go.Figure(go.Heatmap(
        z=z, x=cols, y=rows, text=txt, texttemplate="%{text}",
        textfont=dict(size=12, color=T.COLOR["ink"]),
        customdata=cd, zmin=0, zmax=2, colorscale=STATUS_SCALE,
        showscale=False, hoverongaps=False, xgap=3, ygap=3,
        hovertemplate=("%{y} · %{x}<br>狀態:%{customdata[0]}<br>"
                       "平均空屋率 %{customdata[1]}<br>"
                       "房源數 %{customdata[2]} 間<br>"
                       "中位價 %{customdata[3]}<extra></extra>")))
    apply_theme(fig, h=90 + 52 * len(rows), legend=False).update_layout(
        xaxis_title="", yaxis=dict(autorange="reversed"),
        margin=dict(l=20, r=20, t=10, b=20))
    st.plotly_chart(fig, use_container_width=True)

    _sq = ("<span style='display:inline-block;width:12px;height:12px;"
           "border-radius:var(--sa-radius-bar);margin:0 4px 0 12px;"
           "background:{c};'></span>")
    st.markdown(
        "<div style='font-size:var(--sa-text-caption);color:var(--sa-ink2);'>"
        + _sq.format(c=STATUS_FILL["success"]) + "缺口市場（建議招募）"
        + _sq.format(c=STATUS_FILL["warning"]) + "觀察中"
        + _sq.format(c=STATUS_FILL["neutral"]) + "已飽和</div>",
        unsafe_allow_html=True)

    # 口徑警告:本區塊採「模型預估空屋率 × 全體 listings」,與 ①②③ 的
    # 「calendar 真實已訂天數 × calendar∩listings」是兩套母體與兩套口徑。
    # 舊版此處另外印一次平台年收入總額,與 ① 的收入池數字打架(3.61 億 vs
    # 2.81 億),已改為只講差異來源,不再重述一個競爭性的總額。
    _rev = (pa.add_revenue_columns(df, cm)["platform_revenue"].sum())
    note(f"⚠️ <b>本區塊口徑與上方不同</b>:招商評估需涵蓋尚無檔期資料的房源,"
         f"故採<b>模型預估空屋率</b>、母體 {len(df):,} 間"
         f"(上方 ①②③ 採 calendar 真實已訂天數,母體較小)。"
         f"同口徑下平台年收入約 {_money(_rev)},"
         f"與上方收入池不可直接相減;缺口市場若各增加 10 間房源,"
         f"增量應以本區塊口徑另行試算。")
