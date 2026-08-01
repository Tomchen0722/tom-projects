"""共用的畫面元件與樣式，讓每一頁的排版一致。"""

import streamlit as st

# ---- 配色（統一色票，深淺色模式都看得清楚）----
C = {
    "primary": "#2563eb",   # 藍：主色
    "good": "#16a34a",      # 綠：正確 / 抓到
    "bad": "#dc2626",       # 紅：錯誤 / 漏掉
    "warn": "#d97706",      # 橘：警告
    "muted": "#64748b",     # 灰：次要文字
    "grid": "rgba(128,128,128,0.25)",
}

PLOT_COLORS = ["#2563eb", "#dc2626", "#16a34a", "#d97706", "#7c3aed", "#0891b2"]


def inject_css() -> None:
    """注入一次全站樣式：中文字距、卡片、程式碼區塊。"""
    st.markdown(
        """
        <style>
          .block-container { padding-top: 2.2rem; max-width: 1100px; }
          html, body, [class*="css"] { letter-spacing: 0.01em; line-height: 1.75; }
          h1 { font-size: 2.0rem !important; }
          h2 { font-size: 1.45rem !important; margin-top: 1.8rem !important; }
          h3 { font-size: 1.15rem !important; }

          .kicker {
            display:inline-block; font-size:.78rem; font-weight:700; letter-spacing:.12em;
            text-transform:uppercase; color:#2563eb; margin-bottom:.35rem;
          }
          .card {
            border:1px solid rgba(128,128,128,.28); border-radius:12px;
            padding:1rem 1.15rem; margin:.7rem 0;
          }
          .card-title { font-weight:700; margin-bottom:.35rem; font-size:.95rem; }
          .takeaway { border-left:5px solid #2563eb; background:rgba(37,99,235,.08); }
          .analogy  { border-left:5px solid #d97706; background:rgba(217,119,6,.08); }
          .pitfall  { border-left:5px solid #dc2626; background:rgba(220,38,38,.08); }
          .jobnote  { border-left:5px solid #16a34a; background:rgba(22,163,74,.08); }

          .term { border-bottom:1px dashed #2563eb; font-weight:600; }
          .stTabs [data-baseweb="tab"] { font-size:.95rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(kicker: str, title: str, subtitle: str) -> None:
    st.markdown(f'<div class="kicker">{kicker}</div>', unsafe_allow_html=True)
    st.markdown(f"# {title}")
    st.markdown(
        f'<p style="font-size:1.05rem;color:#64748b;margin-top:-.5rem">{subtitle}</p>',
        unsafe_allow_html=True,
    )
    st.divider()


def _card(kind: str, title: str, body: str) -> None:
    st.markdown(
        f'<div class="card {kind}"><div class="card-title">{title}</div>{body}</div>',
        unsafe_allow_html=True,
    )


def takeaway(body: str) -> None:
    """一句話結論。"""
    _card("takeaway", "📌 一句話結論", body)


def analogy(body: str) -> None:
    """生活比喻。"""
    _card("analogy", "🧩 生活比喻", body)


def pitfall(body: str) -> None:
    """常見誤解 / 踩雷。"""
    _card("pitfall", "⚠️ 常見誤解", body)


def jobnote(body: str) -> None:
    """求職關聯：這個知識在工作上怎麼用。"""
    _card("jobnote", "💼 職場上怎麼用", body)


def interview(question: str, answer: str) -> None:
    """面試題：先問問題，答案收在摺疊區，逼你先想過再看。"""
    with st.expander(f"❓ {question}"):
        st.markdown(answer)


def code(source: str, caption: str = "") -> None:
    if caption:
        st.caption(caption)
    st.code(source.strip(), language="python")


def next_step(text: str) -> None:
    st.divider()
    st.markdown(f"➡️ **下一步**：{text}")
