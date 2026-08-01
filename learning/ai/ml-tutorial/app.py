"""AI 學習地圖 — 從零開始的資料分析 / 機器學習 / 深度學習教學 App。

啟動方式：
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="AI 學習地圖",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils.ui import inject_css  # noqa: E402

inject_css()

# ── Project Hub 返回按鈕 ────────────────────────────────────────
# 由 tom-projects Hub 加入。單獨執行本專案時按鈕依然會顯示，
# 只是點擊後需要 Hub 有在執行才連得上，不影響本專案的任何功能。
st.markdown("""
<style>
  #tom-hub-return{
    position:fixed; left:18px; bottom:18px; z-index:999990;
    display:inline-flex; align-items:center; gap:8px;
    min-height:44px; padding:11px 18px;
    background:#1C1A18; color:#FEFEF9 !important;
    font-family:'Noto Sans TC','Microsoft JhengHei',sans-serif;
    font-size:13px; font-weight:500; letter-spacing:.03em; line-height:1;
    text-decoration:none !important;
    box-shadow:0 6px 24px rgba(28,26,24,.22);
    transition:background .25s, transform .25s;
  }
  #tom-hub-return:hover{ background:#3A68AD; transform:translateY(-2px); }
</style>
<a id="tom-hub-return" href="http://127.0.0.1:7000" target="_self">&#8592; 回 Hub</a>
""", unsafe_allow_html=True)

PAGES = {
    "開始": [
        st.Page("views/home.py", title="學習地圖", icon="🗺️", default=True),
        st.Page("views/glossary.py", title="名詞速查表", icon="📖"),
    ],
    "第一站 · 資料": [
        st.Page("views/data_basics.py", title="資料分析基礎", icon="📊"),
        st.Page("views/metrics.py", title="評估指標（Recall / Precision）", icon="🎯"),
    ],
    "第二站 · 機器學習": [
        st.Page("views/ml_basics.py", title="機器學習基礎", icon="🤖"),
        st.Page("views/overfitting.py", title="過擬合與模型選擇", icon="⚖️"),
    ],
    "第三站 · 深度學習": [
        st.Page("views/neural_net.py", title="神經網路是什麼", icon="🧠"),
        st.Page("views/cnn.py", title="CNN 卷積神經網路", icon="🖼️"),
        st.Page("views/rnn.py", title="RNN / LSTM 序列模型", icon="🔁"),
        st.Page("views/transformer.py", title="Transformer 與 Attention", icon="✨"),
    ],
    "第四站 · 求職": [
        st.Page("views/projects.py", title="實戰練習（Notebook）", icon="🛠️"),
        st.Page("views/interview.py", title="面試題庫", icon="💼"),
    ],
}

pg = st.navigation(PAGES)
pg.run()

with st.sidebar:
    st.divider()
    st.caption("💡 建議照著左邊順序由上往下讀，每頁都有可以拖的滑桿，動手玩過再往下。")
