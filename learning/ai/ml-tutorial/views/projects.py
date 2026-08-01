from pathlib import Path

import streamlit as st

from utils.ui import code, hero, jobnote, next_step, pitfall, takeaway

hero(
    "第四站 · 求職",
    "🛠️ 實戰練習 Notebook",
    "看懂 ≠ 會做。這四份 Notebook 全部離線可跑，跑完你就有能寫進履歷的東西了。",
)

takeaway(
    "面試問「你做過什麼專案」時，<b>「我跑過教學範例」和「我自己做過一個專案」是天差地別</b>。<br>"
    "這四份 Notebook 是骨架，跑完之後<b>換成你自己找的資料</b>再跑一次 —— 那才是作品集。"
)

NB_DIR = Path(__file__).resolve().parent.parent / "notebooks"

NOTEBOOKS = [
    {
        "file": "01_資料分析與評估指標.ipynb",
        "title": "01 · 資料分析全流程 + 評估指標",
        "level": "⭐ 入門",
        "time": "60～90 分鐘",
        "cover": "第 1、2 章",
        "desc": """
        用一份客戶流失資料，跑完整個監督式學習流程：
        載入 → EDA → 清資料 → 特徵工程 → 切訓練測試 → 訓練 → **算 Recall/Precision/F1** → 調閾值 → 看特徵重要性。

        **你會親手做到**：混淆矩陣、ROC 曲線、閾值調整對指標的影響。
        """,
    },
    {
        "file": "02_手刻神經網路.ipynb",
        "title": "02 · 用 NumPy 從零手刻神經網路",
        "level": "⭐⭐ 進階",
        "time": "90～120 分鐘",
        "cover": "第 5 章",
        "desc": """
        **不用任何深度學習套件**，純 NumPy 實作前向傳播、損失函數、反向傳播、梯度下降。

        **為什麼要做這個**：面試官很愛問「你知道 backward 在算什麼嗎」。
        手刻過一次，你的答案會跟只會呼叫 `.backward()` 的人完全不同層次。
        """,
    },
    {
        "file": "03_CNN影像分類.ipynb",
        "title": "03 · PyTorch CNN 影像分類",
        "level": "⭐⭐ 進階",
        "time": "60～90 分鐘",
        "cover": "第 6 章",
        "desc": """
        用 PyTorch 建一個 CNN 分類手寫數字，包含完整訓練迴圈、驗證、混淆矩陣、
        **視覺化第一層學到的濾波器**（會看到它自己學出邊緣偵測器）。

        用 sklearn 內建資料集，**不需要網路下載**。
        """,
    },
    {
        "file": "04_Attention手刻實作.ipynb",
        "title": "04 · 手刻 Self-Attention",
        "level": "⭐⭐⭐ 挑戰",
        "time": "60～90 分鐘",
        "cover": "第 8 章",
        "desc": """
        用 NumPy 實作 Scaled Dot-Product Attention、Multi-Head Attention、
        因果遮罩、位置編碼，並把注意力權重畫成熱圖。

        **這份跑完，Transformer 的面試題你就答得出來了。**
        """,
    },
]

st.markdown("## 四份 Notebook")

for nb in NOTEBOOKS:
    path = NB_DIR / nb["file"]
    with st.container(border=True):
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"### {nb['title']}")
            st.markdown(nb["desc"])
        with c2:
            st.markdown(f"**難度**　{nb['level']}")
            st.markdown(f"**時間**　{nb['time']}")
            st.markdown(f"**對應**　{nb['cover']}")
            st.markdown("✅ 檔案存在" if path.exists() else "❌ 找不到檔案")
        st.code(str(path), language=None)

st.markdown("## 怎麼打開 Notebook")

st.markdown(
    """
**方法 1（最簡單）**：桌面上的捷徑旁邊有一個 **「ML 實戰練習」** 捷徑，雙擊就會開瀏覽器。

**方法 2**：在這個資料夾開啟終端機，輸入下面的指令。
"""
)

code_block = f'cd "{NB_DIR.parent}"\njupyter notebook notebooks'
st.code(code_block, language="bash")

st.markdown(
    """
**方法 3**：用 VS Code 開啟 `.ipynb` 檔（要先裝 Python 和 Jupyter 擴充套件）。
VS Code 的體驗最好，推薦長期用這個。
"""
)

st.info(
    "**Notebook 怎麼操作**：點一格程式碼，按 **Shift + Enter** 執行並跳到下一格。"
    "從第一格開始，一格一格往下按就對了。",
    icon="⌨️",
)

pitfall(
    "<b>不要只按 Shift+Enter 從頭跑到尾看結果。</b>那跟看影片沒兩樣。<br>"
    "每份 Notebook 最後都有<b>「動手改改看」</b>的練習題 —— "
    "改參數、換模型、換資料，看結果怎麼變。<b>改壞了才學得到東西。</b>"
)

st.markdown("## 跑完之後：怎麼變成履歷上的專案")

st.markdown(
    """
### 第一步：換成真實資料

免費而且面試官認得的資料來源：

| 來源 | 網址 | 適合 |
|---|---|---|
| **Kaggle Datasets** | kaggle.com/datasets | 什麼都有，附討論區可以參考別人做法 |
| **政府資料開放平臺** | data.gov.tw | **台灣在地資料**，做在地題目加分 |
| **UCI ML Repository** | archive.ics.uci.edu | 經典教學資料集 |
| **你自己的工作資料** | — | **最加分**，但要注意保密，數字要去識別化 |

### 第二步：專案要有「商業問題」，不能只有技術

❌ 「我用隨機森林在 Titanic 資料集達到 82% 準確率」
（面試官心想：這個資料集全世界跑過幾百萬次了）

✅ 「某電商每月流失 8% 客戶。我做了一個流失預測模型，
Recall 達 76%，代表可以提前抓出四分之三的高風險客戶。
以每個客戶挽回成本 200 元、終身價值 3000 元估算，
每月可以多留住約 120 位客戶，淨效益約 33 萬。」

### 第三步：專案的 README 要有這五段

1. **問題定義** — 解決什麼商業問題，成功的標準是什麼
2. **資料** — 來源、筆數、欄位、有什麼問題（缺值多少、多不平衡）
3. **方法** — 試了哪些模型、為什麼選這個、怎麼調參
4. **結果** — 用**業務語言**講指標，附圖表
5. **限制與下一步** — 這個模型什麼時候會失效、之後想怎麼改進

**第 5 點最多人漏掉，但最能展現成熟度。**
"""
)

jobnote(
    "<b>三個專案就夠了，不用多</b>：<br><br>"
    "① 一個<b>表格資料</b>的分類/迴歸專案（展示資料處理 + 傳統 ML + 商業解讀）<br>"
    "② 一個<b>深度學習</b>專案（CNN 或 NLP，展示你跟得上技術）<br>"
    "③ 一個<b>端到端</b>的東西（做成 Streamlit App 或 API，展示你不只會跑 Notebook）<br><br>"
    "第 ③ 點是很多轉職者的弱項，<b>做出來會非常突出</b> —— "
    "而且你現在看的這個 App 就是 Streamlit 寫的，你已經有現成範例了。"
)

next_step("到「💼 面試題庫」，把學到的東西整理成能講出口的答案。")
