import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import style

hero(
    "第三站 · 深度學習",
    "🧠 神經網路是什麼",
    "拆開來看，一個「神經元」就是國中數學的 y = ax + b。深度學習只是把幾百萬個這種東西疊起來。",
)

takeaway(
    "神經網路 = <b>「加權相加 → 通過一個彎曲函數」</b>這個動作，重複很多次。<br>"
    "訓練 = 從結果的錯誤往回推，<b>算出每個權重該負多少責任</b>，然後各自調整一點點。"
    "這個「往回推責任」的過程就是 <span class='term'>反向傳播（Backpropagation）</span>。"
)

# ---------------------------------------------------------------- 神經元
st.markdown("## 1. 一顆神經元在做什麼")

analogy(
    "把它想成<b>加權投票</b>。<br><br>"
    "決定今天要不要出門跑步，你會考慮：天氣（很重要，權重 0.7）、"
    "有沒有睡飽（重要，權重 0.5）、朋友有沒有約（普通，權重 0.2）。<br><br>"
    "<b>總分 = 0.7×天氣 + 0.5×睡飽 + 0.2×朋友 + 你的懶惰程度（偏差 b）</b><br>"
    "總分超過某個門檻就出門 —— 這就是一顆神經元。"
)

st.latex(r"z = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b \quad\longrightarrow\quad a = f(z)")

st.markdown(
    """
| 符號 | 名稱 | 白話 |
|---|---|---|
| $x$ | 輸入 input | 你給它的資料（像素值、字的編號、身高體重） |
| $w$ | **權重 weight** | 這個輸入有多重要 — **訓練時要學的就是它** |
| $b$ | **偏差 bias** | 基準線 / 門檻高低 — 也是要學的 |
| $z$ | 加權和 | 中間結果 |
| $f$ | **激活函數 activation** | 把 z 掰彎的函數 — **神經網路的靈魂** |
| $a$ | 輸出 | 傳給下一層 |
"""
)

st.markdown("### 🎮 玩一顆神經元：它其實就是在畫一條分界線")

s1, s2, s3 = st.columns(3)
with s1:
    w1 = st.slider("w₁（特徵 1 的權重）", -3.0, 3.0, 1.0, 0.1)
with s2:
    w2 = st.slider("w₂（特徵 2 的權重）", -3.0, 3.0, 1.0, 0.1)
with s3:
    bb = st.slider("b（偏差）", -5.0, 5.0, 0.0, 0.1)


@st.cache_data
def two_blobs(seed=5):
    rng = np.random.default_rng(seed)
    a = rng.normal([-1.5, -1.0], 0.9, (60, 2))
    b = rng.normal([1.6, 1.3], 0.9, (60, 2))
    X = np.r_[a, b]
    yy = np.r_[np.zeros(60), np.ones(60)]
    return X, yy


X2, y2 = two_blobs()
gx, gy = np.meshgrid(np.linspace(-5, 5, 120), np.linspace(-5, 5, 120))
zz = 1 / (1 + np.exp(-(w1 * gx + w2 * gy + bb)))

acc = float((((1 / (1 + np.exp(-(X2 @ np.array([w1, w2]) + bb)))) > 0.5) == y2).mean())

fig = go.Figure()
fig.add_trace(go.Contour(x=gx[0], y=gy[:, 0], z=zz, colorscale="RdBu", reversescale=True,
                         opacity=0.55, showscale=False, contours=dict(start=0, end=1, size=0.05)))
fig.add_trace(go.Scatter(x=X2[y2 == 0, 0], y=X2[y2 == 0, 1], mode="markers",
                         name="類別 A", marker=dict(size=9, color=C["primary"],
                                                  line=dict(width=1, color="white"))))
fig.add_trace(go.Scatter(x=X2[y2 == 1, 0], y=X2[y2 == 1, 1], mode="markers",
                         name="類別 B", marker=dict(size=9, color=C["bad"],
                                                  line=dict(width=1, color="white"))))
fig.update_layout(title=f"一顆神經元切出的分界線　—　正確率 {acc:.1%}",
                  xaxis_title="特徵 1", yaxis_title="特徵 2")
st.plotly_chart(style(fig, 460), width="stretch")

st.info(
    "**關鍵觀察**：一顆神經元只能畫出**一條直線**。"
    "現實問題的分界線幾乎都是彎的 —— 所以我們需要**很多顆、疊很多層**。",
    icon="💡",
)

# ---------------------------------------------------------------- 激活函數
st.markdown("## 2. 激活函數：為什麼一定要「把線掰彎」")

pitfall(
    "如果沒有激活函數，10 層網路疊起來還是<b>一條直線</b>。<br>"
    "數學上：直線套直線還是直線（<code>w₂(w₁x+b₁)+b₂ = (w₂w₁)x + ...</code>）。"
    "疊 100 層等於白疊。<br><br>"
    "<b>激活函數的唯一使命：引入非線性，讓網路能表達彎曲的關係。</b>"
    "這是面試必考題。"
)

acts = {
    "ReLU（現在的預設選擇）": lambda v: np.maximum(0, v),
    "Sigmoid（舊時代主流）": lambda v: 1 / (1 + np.exp(-v)),
    "Tanh": np.tanh,
    "Leaky ReLU": lambda v: np.where(v > 0, v, 0.01 * v),
}
zline = np.linspace(-6, 6, 300)
fig = go.Figure()
for name, f in acts.items():
    fig.add_trace(go.Scatter(x=zline, y=f(zline), mode="lines", name=name, line=dict(width=3)))
fig.update_layout(title="四個常見的激活函數", xaxis_title="輸入 z", yaxis_title="輸出 f(z)",
                  yaxis_range=[-1.5, 4])
st.plotly_chart(style(fig, 380), width="stretch")

st.markdown(
    """
| 函數 | 公式 | 什麼時候用 | 問題 |
|---|---|---|---|
| **ReLU** | max(0, z) | **隱藏層預設用它**，算得快 | 負區梯度是 0，神經元可能「死掉」 |
| **Leaky ReLU** | z>0 用 z，否則 0.01z | ReLU 死太多時的替代品 | — |
| **Sigmoid** | 1/(1+e⁻ᶻ) | **二分類的最後一層**（輸出機率） | 兩端梯度趨近 0 → **梯度消失** |
| **Tanh** | (eᶻ-e⁻ᶻ)/(eᶻ+e⁻ᶻ) | RNN 內部 | 一樣有梯度消失 |
| **Softmax** | eᶻⁱ/Σeᶻʲ | **多分類的最後一層**（各類機率加總 = 1） | — |

**記住這個組合就夠用了**：隱藏層 → **ReLU**；二分類輸出 → **Sigmoid**；多分類輸出 → **Softmax**。
"""
)

# ---------------------------------------------------------------- 疊起來
st.markdown("## 3. 疊起來：多層網路可以畫出任何形狀")

analogy(
    "第 1 層學「邊緣、顏色」這種簡單特徵 → "
    "第 2 層把它們組成「眼睛、輪子」→ "
    "第 3 層組成「臉、車子」。<br><br>"
    "<b>每一層都在用前一層的成果，組合出更抽象的概念。</b>"
    "「深度」學習的深，指的就是層數多。"
)

st.markdown("### 🎮 現場訓練一個小網路（純 numpy 手刻，不用套件）")

st.markdown(
    "下面這個資料**沒辦法用一條直線分開**（兩個同心圓）。"
    "看看多層網路怎麼把它學會。"
)


@st.cache_data
def circles(n=400, seed=1):
    rng = np.random.default_rng(seed)
    r_in = rng.uniform(0, 1.1, n // 2)
    r_out = rng.uniform(1.9, 3.0, n // 2)
    t = rng.uniform(0, 2 * np.pi, n)
    X = np.r_[
        np.c_[r_in * np.cos(t[: n // 2]), r_in * np.sin(t[: n // 2])],
        np.c_[r_out * np.cos(t[n // 2:]), r_out * np.sin(t[n // 2:])],
    ]
    yy = np.r_[np.zeros(n // 2), np.ones(n // 2)].reshape(-1, 1)
    return X + rng.normal(0, 0.12, X.shape), yy


@st.cache_data
def train_mlp(hidden=8, lr=0.5, epochs=1500, seed=0):
    """手刻兩層神經網路：前向 → 算 loss → 反向傳播 → 更新權重。"""
    Xc, yc = circles()
    rng = np.random.default_rng(seed)
    W1 = rng.normal(0, 0.8, (2, hidden))
    b1 = np.zeros((1, hidden))
    W2 = rng.normal(0, 0.8, (hidden, 1))
    b2 = np.zeros((1, 1))
    losses, accs = [], []

    for _ in range(epochs):
        # --- 前向傳播 forward ---
        z1 = Xc @ W1 + b1
        a1 = np.maximum(0, z1)                      # ReLU
        z2 = a1 @ W2 + b2
        a2 = 1 / (1 + np.exp(-z2))                  # Sigmoid

        # --- 損失 Binary Cross-Entropy ---
        eps = 1e-9
        loss = -np.mean(yc * np.log(a2 + eps) + (1 - yc) * np.log(1 - a2 + eps))
        losses.append(loss)
        accs.append(float(((a2 > 0.5) == yc).mean()))

        # --- 反向傳播 backward（連鎖律，一層一層往回推）---
        m = len(Xc)
        dz2 = (a2 - yc) / m
        dW2, db2 = a1.T @ dz2, dz2.sum(0, keepdims=True)
        da1 = dz2 @ W2.T
        dz1 = da1 * (z1 > 0)                        # ReLU 的導數：正的是 1、負的是 0
        dW1, db1 = Xc.T @ dz1, dz1.sum(0, keepdims=True)

        # --- 梯度下降更新 ---
        W2 -= lr * dW2; b2 -= lr * db2
        W1 -= lr * dW1; b1 -= lr * db1

    return Xc, yc, W1, b1, W2, b2, losses, accs


h1, h2 = st.columns(2)
with h1:
    hidden = st.select_slider("隱藏層要幾顆神經元", [1, 2, 3, 4, 8, 16, 32], value=8)
with h2:
    lr = st.select_slider("學習率（每次調整的步伐大小）",
                          [0.01, 0.05, 0.1, 0.5, 1.0, 3.0], value=0.5)

Xc, yc, W1, b1, W2, b2, losses, accs = train_mlp(hidden, lr)

gx2, gy2 = np.meshgrid(np.linspace(-3.6, 3.6, 130), np.linspace(-3.6, 3.6, 130))
grid = np.c_[gx2.ravel(), gy2.ravel()]
out = 1 / (1 + np.exp(-(np.maximum(0, grid @ W1 + b1) @ W2 + b2)))
out = out.reshape(gx2.shape)

p1, p2 = st.columns([1, 1])
with p1:
    fig = go.Figure()
    fig.add_trace(go.Contour(x=gx2[0], y=gy2[:, 0], z=out, colorscale="RdBu",
                             reversescale=True, opacity=0.6, showscale=False,
                             contours=dict(start=0, end=1, size=0.05)))
    fig.add_trace(go.Scatter(x=Xc[yc.ravel() == 0, 0], y=Xc[yc.ravel() == 0, 1],
                             mode="markers", name="內圈",
                             marker=dict(size=6, color=C["primary"])))
    fig.add_trace(go.Scatter(x=Xc[yc.ravel() == 1, 0], y=Xc[yc.ravel() == 1, 1],
                             mode="markers", name="外圈",
                             marker=dict(size=6, color=C["bad"])))
    fig.update_layout(title=f"學到的分界線（最終正確率 {accs[-1]:.1%}）")
    st.plotly_chart(style(fig, 400), width="stretch")
with p2:
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=losses, mode="lines", name="損失 Loss",
                             line=dict(color=C["bad"], width=3)))
    fig.add_trace(go.Scatter(y=accs, mode="lines", name="正確率", yaxis="y2",
                             line=dict(color=C["good"], width=3)))
    fig.update_layout(title="訓練過程", xaxis_title="訓練回合 epoch",
                      yaxis=dict(title="Loss"),
                      yaxis2=dict(title="正確率", overlaying="y", side="right", range=[0, 1]))
    st.plotly_chart(style(fig, 400), width="stretch")

if hidden <= 2:
    st.error("**神經元太少**（欠擬合）—— 它畫不出圓形，只能硬用一兩條直線去切。", icon="😴")
elif lr >= 3.0:
    st.error("**學習率太大** —— 步伐跨太大，跳過最低點，Loss 會震盪甚至爆炸。", icon="💥")
elif lr <= 0.01:
    st.warning("**學習率太小** —— 走太慢，1500 回合還沒走到終點。", icon="🐌")
else:
    st.success("**剛好** —— 曲線平順下降，分界線變成漂亮的圓形。", icon="✅")

# ---------------------------------------------------------------- 反向傳播
st.markdown("## 4. 反向傳播：模型怎麼知道要調哪個權重")

analogy(
    "一間公司這季業績很差（<b>loss 很大</b>）。老闆要追究責任：<br><br>"
    "→ 先問副總「你這季貢獻多少？」<br>"
    "→ 副總再往下問經理，經理再問組員<br>"
    "→ 一層一層往回追，最後每個人都得到一個「你要負多少責任」的數字<br>"
    "→ 責任大的人調整多一點，責任小的調整少一點<br><br>"
    "這個「一層一層往回算責任」，數學上就是<b>連鎖律（chain rule）</b>，"
    "算出來的責任叫 <span class='term'>梯度（gradient）</span>。"
)

st.markdown(
    """
### 一次訓練（一個 epoch）的四個步驟

1. **前向傳播 Forward** — 資料進去，一層層算到最後，得到預測值
2. **算損失 Loss** — 預測值和正確答案差多少
3. **反向傳播 Backward** — 用連鎖律，往回算出每個權重的梯度
4. **更新權重 Optimizer Step** — `新權重 = 舊權重 − 學習率 × 梯度`

重複幾千次，loss 就會一路下降。
"""
)

st.latex(r"w_{\text{new}} = w_{\text{old}} - \eta \cdot \frac{\partial L}{\partial w}")
st.caption("η（eta）就是學習率 learning rate；∂L/∂w 就是「w 該負的責任」。")

pitfall(
    "<b>學習率是最重要的超參數，沒有之一。</b><br>"
    "太大 → loss 上下亂跳甚至變成 NaN；太小 → 訓練慢到天荒地老，或卡在爛的局部解。<br>"
    "實務起手式：<b>Adam optimizer + 學習率 1e-3</b>，不行再調。"
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 5. 用 PyTorch 寫出來只要 15 行")

code(
    """
import torch
import torch.nn as nn

# 1) 定義網路：輸入 2 維 → 隱藏 16 → 隱藏 16 → 輸出 1
model = nn.Sequential(
    nn.Linear(2, 16), nn.ReLU(),
    nn.Linear(16, 16), nn.ReLU(),
    nn.Linear(16, 1),           # 最後一層不加 Sigmoid（下面的 loss 會自己做）
)

# 2) 損失函數 + 優化器
criterion = nn.BCEWithLogitsLoss()               # 二分類
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 3) 訓練迴圈 —— 這四行的順序要背起來
for epoch in range(1000):
    optimizer.zero_grad()          # ① 清掉上一輪的梯度（忘了寫會出大錯）
    output = model(X_train)        # ② 前向傳播
    loss = criterion(output, y_train)
    loss.backward()                # ③ 反向傳播，自動算好所有梯度
    optimizer.step()               # ④ 更新權重

# 4) 預測（記得關掉梯度計算，省記憶體又變快）
model.eval()
with torch.no_grad():
    prob = torch.sigmoid(model(X_test))
""",
    "PyTorch 的訓練迴圈長這樣，任何深度學習專案都是這個骨架",
)

jobnote(
    "面試很愛叫你<b>在白板上默寫 PyTorch 訓練迴圈</b>。"
    "最常被抓包的點是<b>忘記寫 <code>optimizer.zero_grad()</code></b> —— "
    "PyTorch 的梯度是「累加」的，不清掉的話這一輪會加上前面所有輪的梯度，訓練直接壞掉。"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "為什麼神經網路需要激活函數？",
    """
**為了引入非線性。**

沒有激活函數的話，不管疊幾層，整個網路都等價於**一個線性變換**：

`W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂) = W'x + b'`

也就是說 100 層網路的表達能力，跟 1 層完全一樣，深度完全白費。

**加了非線性之後**，網路才能逼近任意複雜的函數
（這叫 **通用近似定理 Universal Approximation Theorem**）。
""",
)

interview(
    "ReLU 為什麼取代了 Sigmoid 成為隱藏層的預設？",
    """
三個理由：

1. **不會梯度消失**：Sigmoid 在輸入很大或很小時，導數趨近 0，
   反向傳播經過幾層之後梯度就沒了，前面的層學不動。
   ReLU 在正區的導數**恆為 1**，梯度可以完整往回傳。
2. **算得快**：ReLU 只是 `max(0, x)`，一個比較指令；Sigmoid 要算指數。
3. **稀疏性**：負的直接變 0，等於部分神經元不啟動，有點類似正則化的效果。

**ReLU 的缺點**：**Dying ReLU** —— 如果某個神經元的輸入永遠是負的，
梯度永遠是 0，它就再也學不動了。解法是用 **Leaky ReLU** 或 **GELU**。
""",
)

interview(
    "什麼是梯度消失和梯度爆炸？",
    """
反向傳播是**連乘**：每經過一層就乘上一次該層的導數。

- **梯度消失**：每層導數都 < 1（例如 Sigmoid 最大只有 0.25），
  乘 10 層 → 0.25¹⁰ ≈ 0.00001 → **前面的層幾乎不更新**
- **梯度爆炸**：每層導數都 > 1，乘 10 層 → 數值變超大 → loss 變成 NaN

**解法**：
| 問題 | 解法 |
|---|---|
| 消失 | ReLU 系列激活函數、**殘差連接 ResNet**、Batch Norm、LSTM 的閘門 |
| 爆炸 | **梯度裁剪 Gradient Clipping**、權重初始化（He / Xavier）、降低學習率 |

**殘差連接**（`output = F(x) + x`）是最關鍵的發明——
那個 `+ x` 讓梯度有一條「高速公路」可以直接傳回去，
這才讓 100 層以上的網路變得可訓練。
""",
)

interview(
    "Batch Size 大一點好還是小一點好？",
    """
| | **小 batch（如 32）** | **大 batch（如 1024）** |
|---|---|---|
| 梯度品質 | 雜訊大 | 穩定、接近真實梯度 |
| 泛化能力 | **通常較好**（雜訊有正則化效果，容易跳出爛的局部解） | 容易掉進 sharp minima，泛化較差 |
| 速度 | GPU 用不滿 | **GPU 效率高**，每個 epoch 快 |
| 記憶體 | 小 | 大，可能爆 VRAM |

**實務**：32～256 之間最常見。GPU 記憶體不夠又想用大 batch，
可以用 **梯度累積（gradient accumulation）**——
連續跑幾個小 batch，累積梯度後才更新一次。

**加分句**：batch size 加大時，學習率通常也要按比例加大（linear scaling rule）。
""",
)

next_step("到「🖼️ CNN」，看神經網路怎麼「看懂」圖片。")
