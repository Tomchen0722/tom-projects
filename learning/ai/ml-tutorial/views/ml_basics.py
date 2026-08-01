import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import style

hero(
    "第二站 · 機器學習",
    "🤖 機器學習基礎",
    "電腦怎麼從一堆例子裡「學」出規律？答案比你想的簡單：猜 → 算錯多少 → 改一點點 → 再猜。",
)

takeaway(
    "所有機器學習模型都在做同一件事：<b>找一組數字（參數），讓「模型的預測」和「真實答案」"
    "的差距最小</b>。<br>這個差距叫 <span class='term'>損失（Loss）</span>，"
    "而「一點一點改參數把差距變小」的過程叫 <span class='term'>訓練（Training）</span>。"
)

# ---------------------------------------------------------------- 三大類
st.markdown("## 1. 機器學習的三大類")

t1, t2, t3 = st.tabs(["📗 監督式學習", "📙 非監督式學習", "📕 強化式學習"])

with t1:
    st.markdown(
        """
### 有標準答案的學習

**你給的資料**：題目 + 答案（例如：房子的坪數、地段 → 成交價）

**它學什麼**：從題目推答案的規則

**兩種題型**：

| 題型 | 答案長什麼樣 | 例子 | 常用模型 |
|---|---|---|---|
| **迴歸 Regression** | 一個連續數字 | 預測房價、預測明天氣溫 | 線性迴歸、XGBoost |
| **分類 Classification** | 一個類別 | 這封信是不是垃圾信、這張圖是貓是狗 | 邏輯迴歸、隨機森林 |

👉 **職場上 90% 的專案都是這一類。** 因為它最好衡量成效。
"""
    )
    analogy("像有解答本的考古題。做完可以對答案，知道自己錯在哪，然後修正。")

with t2:
    st.markdown(
        """
### 沒有標準答案，自己找結構

**你給的資料**：只有題目，沒有答案

**它學什麼**：資料裡自然的分群或壓縮方式

| 任務 | 在做什麼 | 例子 | 常用方法 |
|---|---|---|---|
| **分群 Clustering** | 把像的東西歸在一起 | 顧客分群做行銷 | K-Means、DBSCAN |
| **降維 Dim. Reduction** | 100 欄壓成 2 欄還保住資訊 | 資料視覺化、加速訓練 | PCA、t-SNE |
| **異常偵測** | 找出不合群的那幾筆 | 信用卡盜刷、機台異常 | Isolation Forest |

⚠️ **難點**：沒有答案，所以**很難證明結果是對的**。分群分出 5 群，那 5 群代表什麼意義，要靠人去解讀。
"""
    )
    analogy(
        "像把一箱沒標籤的樂高倒在桌上，你自然會照顏色或大小分堆 —— "
        "沒人告訴你「正確分法」，但你就是分得出來。"
    )

with t3:
    st.markdown(
        """
### 靠獎懲學會做決策

**你給的資料**：一個環境 + 一套獎勵規則

**它學什麼**：在什麼狀況下該採取什麼行動，才能拿到最多分

**例子**：AlphaGo 下圍棋、自動駕駛、機器人走路、ChatGPT 的 RLHF 微調

⚠️ **現實**：訓練超貴、超不穩定，一般公司職缺很少。**轉職階段知道概念就好，不用深入。**
"""
    )
    analogy("像訓練狗狗坐下：做對給零食，做錯不給。試很多次之後牠就知道怎麼拿零食了。")

# ---------------------------------------------------------------- 線性迴歸
st.markdown("## 2. 從最簡單的模型開始：線性迴歸")

analogy(
    "國中就學過：<b>y = ax + b</b>。<br>"
    "把 x 換成「讀書時數」、y 換成「考試分數」，機器學習要做的就是"
    "<b>找出最好的 a 和 b</b>，讓這條直線最貼近所有的點。<br><br>"
    "・<b>a（斜率）</b>在機器學習叫 <span class='term'>權重 weight</span> —— 這個特徵有多重要<br>"
    "・<b>b（截距）</b>叫 <span class='term'>偏差 bias</span> —— 基準線在哪"
)


@st.cache_data
def make_line_data(n=40, seed=3):
    rng = np.random.default_rng(seed)
    x = rng.uniform(0, 10, n)
    y = 6.5 * x + 30 + rng.normal(0, 7, n)
    return x, y.clip(0, 100)


x, y = make_line_data()

st.markdown("### 🎮 自己當一次模型：拖滑桿讓紅線貼近藍點")

s1, s2 = st.columns(2)
with s1:
    w = st.slider("權重 a（每多讀 1 小時，分數加幾分）", 0.0, 12.0, 3.0, 0.1)
with s2:
    b = st.slider("偏差 b（都不讀書的話幾分）", 0.0, 60.0, 50.0, 1.0)

pred = w * x + b
mse = float(np.mean((pred - y) ** 2))

# 最佳解（用最小平方法直接算）
A = np.c_[x, np.ones_like(x)]
w_best, b_best = np.linalg.lstsq(A, y, rcond=None)[0]
mse_best = float(np.mean((w_best * x + b_best - y) ** 2))

g1, g2 = st.columns([3, 2])
with g1:
    xs = np.linspace(0, 10, 50)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", name="真實資料",
                             marker=dict(size=9, color=C["primary"], opacity=0.75)))
    fig.add_trace(go.Scatter(x=xs, y=w * xs + b, mode="lines", name="你的直線",
                             line=dict(color=C["bad"], width=4)))
    fig.add_trace(go.Scatter(x=xs, y=w_best * xs + b_best, mode="lines", name="電腦找到的最佳解",
                             line=dict(color=C["good"], width=2, dash="dash")))
    # 畫誤差線
    for xi, yi, pi in zip(x[:18], y[:18], pred[:18]):
        fig.add_shape(type="line", x0=xi, y0=yi, x1=xi, y1=pi,
                      line=dict(color="rgba(220,38,38,.35)", width=1.5))
    fig.update_layout(title="紅色細線 = 每一筆的誤差，訓練就是要讓它們總和最小",
                      xaxis_title="每日讀書時數", yaxis_title="期末分數")
    st.plotly_chart(style(fig, 420), width="stretch")

with g2:
    st.metric("你的損失 MSE", f"{mse:,.1f}",
              delta=f"{mse - mse_best:+,.1f} 比最佳解差", delta_color="inverse")
    st.metric("電腦的最佳解", f"{mse_best:,.1f}")
    st.caption(f"最佳參數：a = {w_best:.2f}、b = {b_best:.1f}")
    st.markdown(
        "**MSE（均方誤差）** = 每個點的誤差平方後取平均。\n\n"
        "平方是為了：\n"
        "1. 讓正負誤差不互相抵消\n"
        "2. **重罰離很遠的點**\n\n"
        "數字越小越好。"
    )

st.info(
    "**你剛剛手動做的事，電腦是這樣自動做的**：隨便給 a、b 一組值 → 算 MSE → "
    "看往哪個方向改 MSE 會變小（這叫**梯度**）→ 往那個方向改一點點 → 重複幾千次。"
    "這個方法叫 **梯度下降（Gradient Descent）**，是整個深度學習的引擎。",
    icon="⚙️",
)

# ---------------------------------------------------------------- 分類
st.markdown("## 3. 分類：從畫直線變成畫「分界線」")

st.markdown(
    "迴歸是預測數字，分類是預測類別。做法很像 —— "
    "只是把直線的輸出，再丟進一個 **Sigmoid 函數** 壓成 0～1 的機率。"
)

zz = np.linspace(-8, 8, 200)
fig = go.Figure(go.Scatter(x=zz, y=1 / (1 + np.exp(-zz)), mode="lines",
                           line=dict(width=4, color=C["primary"])))
fig.add_hline(y=0.5, line_dash="dot", line_color=C["muted"])
fig.add_annotation(x=4, y=0.55, text="> 0.5 → 判定為「是」", showarrow=False)
fig.add_annotation(x=-4, y=0.45, text="< 0.5 → 判定為「否」", showarrow=False)
fig.update_layout(title="Sigmoid：把任何數字壓成 0～1 的機率",
                  xaxis_title="模型算出的原始分數 z = ax + b", yaxis_title="機率")
st.plotly_chart(style(fig, 340), width="stretch")

st.success(
    "這就是 **邏輯迴歸（Logistic Regression）**。名字有「迴歸」但它是**分類**模型 —— "
    "這是初階面試的送分陷阱題。",
    icon="🎁",
)

# ---------------------------------------------------------------- 樹模型
st.markdown("## 4. 決策樹與隨機森林：業界最常用的主力")

analogy(
    "<b>決策樹</b>就是一連串的 if-else 問題，像看醫生：<br>"
    "「發燒嗎？」→ 是 →「咳嗽嗎？」→ 是 →「診斷：流感」<br><br>"
    "差別在於：<b>要問哪些問題、先問哪一題，是電腦自己從資料裡算出來的</b>，不是人寫的。"
    "它會挑「問完之後兩邊分得最乾淨」的那個問題先問。"
)

st.markdown(
    """
| 模型 | 概念 | 優點 | 缺點 |
|---|---|---|---|
| **決策樹** | 一棵 if-else 樹 | **人看得懂**，可以畫給老闆看 | 很容易過擬合，資料動一點結果差很多 |
| **隨機森林 Random Forest** | 種 100 棵樹，**投票**決定 | 穩、不太需要調參數、開箱即用 | 慢一點，解釋性比單棵樹差 |
| **XGBoost / LightGBM** | 種樹**接力**修正前一棵的錯 | **表格資料的王者**，Kaggle 常勝軍 | 參數多、要調 |
"""
)

jobnote(
    "很多人以為轉職要學深度學習，其實<b>表格類資料（Excel 那種）</b>的專案，"
    "<b>XGBoost / LightGBM 打敗神經網路是常態</b>。<br>"
    "面試被問「你會先用什麼模型」，正確答案是：<b>「先跑一個簡單的 baseline"
    "（邏輯迴歸或隨機森林）建立基準線，再看有沒有必要上複雜模型。」</b><br>"
    "一開口就說要用深度學習的人，通常會被判定為沒有實務經驗。"
)

st.markdown("### 隨機森林為什麼比單棵樹強？")

analogy(
    "<b>三個臭皮匠原理。</b>一個人可能有偏見，但 100 個<b>看過不同資料、"
    "問過不同問題</b>的人一起投票，錯誤會互相抵消。<br><br>"
    "「隨機」在兩個地方：<br>"
    "① 每棵樹只餵<b>隨機抽樣的部分資料</b>（Bagging）<br>"
    "② 每次分裂只考慮<b>隨機挑的部分欄位</b><br>"
    "這樣才能保證 100 棵樹<b>長得不一樣</b> —— 全部一樣就沒有投票的意義了。"
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 5. 完整流程的程式碼（背下這個骨架）")

code(
    """
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1) 切出特徵 X 和答案 y
X = df.drop(columns=["是否流失"])
y = df["是否流失"]

# 2) 切訓練 / 測試（stratify 保證兩邊的正負比例一樣）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3) 建模型 + 訓練
model = RandomForestClassifier(
    n_estimators=200,       # 種 200 棵樹
    max_depth=8,            # 每棵樹最多 8 層（防過擬合）
    class_weight="balanced",# 資料不平衡時，讓少數類權重變高
    random_state=42,
)
model.fit(X_train, y_train)

# 4) 預測 + 評估
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 5) 看哪些特徵最重要（這張圖老闆最愛看）
import pandas as pd
pd.Series(model.feature_importances_, index=X.columns).sort_values().plot.barh()
""",
    "這 5 步是所有監督式學習專案的骨架，換模型只要改第 3 步",
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "監督式和非監督式學習的差別？",
    """
**差在有沒有「標準答案（label）」。**

- **監督式**：資料有答案，模型學「題目 → 答案」的對應。
  例：有 10 萬筆歷史訂單，標記了哪些是詐欺 → 訓練詐欺偵測模型。
- **非監督式**：資料沒答案，模型自己找結構。
  例：有 10 萬筆顧客資料，沒有分類，用 K-Means 分成 5 個客群。

**加分句**：實務上標註資料很貴，所以常用**半監督式**——
少量標註 + 大量未標註，或先用非監督分群，再請專家標註每一群。
""",
)

interview(
    "為什麼要用 MSE 當損失函數？平方有什麼意義？",
    """
三個理由：

1. **避免正負抵消**：誤差 +5 和 -5，直接加起來是 0，看起來完美，但其實都錯了
2. **重罰大錯**：誤差 10 的懲罰是誤差 1 的 **100 倍**，逼模型優先修正離譜的預測
3. **數學上可微分**：平方函數處處平滑，梯度下降才有辦法算出「該往哪走」

**加分句**：如果資料有很多極端值，MSE 會被拉走，
這時候改用 **MAE（絕對誤差）** 或 **Huber Loss** 比較穩。
""",
)

interview(
    "邏輯迴歸是分類還是迴歸？",
    """
**是分類模型。**

叫「迴歸」是歷史包袱——它內部確實在做線性迴歸（算 `z = wx + b`），
但最後把 z 丟進 **Sigmoid** 壓成 0～1 的機率，再用閾值切成類別。

所以：**內部是迴歸，用途是分類**。
""",
)

interview(
    "隨機森林的「隨機」隨機在哪裡？",
    """
**兩個地方**：

1. **樣本隨機（Bootstrap / Bagging）**：每棵樹只用「有放回抽樣」抽出來的部分資料訓練
2. **特徵隨機**：每次分裂節點時，只從隨機挑出的一部分欄位裡找最佳切分點
   （分類問題常用 `max_features = sqrt(總特徵數)`）

**目的**：讓每棵樹**盡量不一樣**。樹之間的錯誤如果不相關，投票平均後錯誤就會互相抵消。
如果每棵樹都長一樣，種 100 棵跟種 1 棵沒差別。
""",
)

interview(
    "Bagging 和 Boosting 的差別？",
    """
| | **Bagging**（隨機森林） | **Boosting**（XGBoost） |
|---|---|---|
| 樹怎麼長 | **平行**，各長各的 | **接力**，下一棵專門修上一棵的錯 |
| 主要在對付 | **變異數**（模型太不穩） | **偏差**（模型太笨） |
| 過擬合風險 | 低，種再多樹也還好 | **高**，樹太多會過擬合 |
| 速度 | 可以平行運算，快 | 必須依序訓練，慢 |

**一句話總結**：Bagging 是「一群人投票消除意見極端」，
Boosting 是「一個人不斷檢討錯題重考」。
""",
)

next_step("到「⚖️ 過擬合與模型選擇」—— 這是新手最常摔跤、面試官最愛問的地方。")
