import warnings

import numpy as np
import plotly.graph_objects as go
import streamlit as st

# 高次多項式本來就會條件數不良 —— 這正是本頁要示範的過擬合現象，不需要警告
warnings.filterwarnings("ignore", category=np.exceptions.RankWarning)

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import style

hero(
    "第二站 · 機器學習",
    "⚖️ 過擬合、欠擬合與模型選擇",
    "「訓練分數 99%、上線後爆炸」—— 這是所有新手的第一次撞牆。這章教你怎麼避開。",
)

takeaway(
    "<b>過擬合（Overfitting）= 模型把考古題背起來了，但沒學會解題方法。</b><br>"
    "判斷方式只有一個：<b>訓練分數很高、驗證分數很低 → 過擬合。</b>"
)

# ---------------------------------------------------------------- 互動
st.markdown("## 1. 動手看：模型太複雜會怎樣")

analogy(
    "三個學生準備考試：<br>"
    "・<b>學生 A（欠擬合）</b>：只讀了第一章，考什麼都不會 → 平時測驗爛、正式考也爛<br>"
    "・<b>學生 B（剛剛好）</b>：理解了原理 → 平時測驗好、正式考也好 ✅<br>"
    "・<b>學生 C（過擬合）</b>：把 500 題考古題連題號一起背 → "
    "平時測驗滿分、正式考換個問法就全錯"
)


@st.cache_data
def make_curve_data(n=25, noise=8.0, seed=11):
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(0, 10, n))
    y_true = 40 + 12 * np.sin(x * 0.6) + 2.2 * x
    y = y_true + rng.normal(0, noise, n)
    return x, y


x, y = make_curve_data()
n_train = 17
xtr, ytr = x[:n_train], y[:n_train]
xte, yte = x[n_train:], y[n_train:]

deg = st.slider(
    "🎚️ 模型複雜度（多項式次數）—— 往右拉，看它怎麼開始「背答案」",
    1, 16, 3, 1,
)

coef = np.polyfit(xtr, ytr, deg)
xs = np.linspace(x.min() - 0.3, x.max() + 0.3, 400)
ys = np.polyval(coef, xs)

train_mse = float(np.mean((np.polyval(coef, xtr) - ytr) ** 2))
test_mse = float(np.mean((np.polyval(coef, xte) - yte) ** 2))

c1, c2 = st.columns([3, 2])
with c1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xtr, y=ytr, mode="markers", name="訓練資料（模型看過）",
                             marker=dict(size=11, color=C["primary"])))
    fig.add_trace(go.Scatter(x=xte, y=yte, mode="markers", name="測試資料（模型沒看過）",
                             marker=dict(size=13, color=C["good"], symbol="star")))
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=f"模型（{deg} 次）",
                             line=dict(color=C["bad"], width=3)))
    fig.update_layout(yaxis_range=[min(y) - 30, max(y) + 30], xaxis_title="x", yaxis_title="y")
    st.plotly_chart(style(fig, 420), width="stretch")

with c2:
    st.metric("訓練誤差（越低越好）", f"{train_mse:,.0f}")
    st.metric("測試誤差（真正重要的）", f"{test_mse:,.0f}",
              delta=f"{test_mse - train_mse:+,.0f} 落差", delta_color="inverse")
    if deg <= 1:
        st.error("**欠擬合（Underfitting）**：模型太簡單，連訓練資料都學不好。", icon="😴")
    elif test_mse > train_mse * 4 and test_mse > 200:
        st.error("**過擬合（Overfitting）**：曲線在硬穿過每個藍點，"
                 "把雜訊也學進去了。綠色星星（沒看過的資料）預測得很差。", icon="🔥")
    else:
        st.success("**剛剛好**：抓到趨勢，沒有硬背雜訊。", icon="✅")

st.markdown("### 兩條曲線的經典圖：找到那個甜蜜點")

degs = range(1, 17)
tr_curve, te_curve = [], []
for d in degs:
    cf = np.polyfit(xtr, ytr, d)
    tr_curve.append(np.mean((np.polyval(cf, xtr) - ytr) ** 2))
    te_curve.append(min(np.mean((np.polyval(cf, xte) - yte) ** 2), 3000))

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(degs), y=tr_curve, mode="lines+markers", name="訓練誤差",
                         line=dict(color=C["primary"], width=3)))
fig.add_trace(go.Scatter(x=list(degs), y=te_curve, mode="lines+markers", name="驗證誤差",
                         line=dict(color=C["bad"], width=3)))
best_d = int(np.argmin(te_curve)) + 1
fig.add_vline(x=best_d, line_dash="dash", line_color=C["good"],
              annotation_text=f"甜蜜點 = {best_d} 次")
fig.add_vline(x=deg, line_dash="dot", line_color=C["warn"], annotation_text="你現在的位置")
fig.update_layout(title="訓練誤差一路往下，驗證誤差先降後升 —— 轉折點就是最佳複雜度",
                  xaxis_title="模型複雜度", yaxis_title="誤差 (MSE)", yaxis_type="log")
st.plotly_chart(style(fig, 400), width="stretch")

st.info(
    "**這張圖是機器學習最重要的一張圖。** 面試如果要你在白板上畫一張圖說明過擬合，畫這張。",
    icon="📌",
)

# ---------------------------------------------------------------- 資料切分
st.markdown("## 2. 為什麼要切訓練 / 驗證 / 測試三份")

analogy(
    "・<b>訓練集 (Train, 60~70%)</b> = <b>課本習題</b>，拿來學<br>"
    "・<b>驗證集 (Validation, 15~20%)</b> = <b>模擬考</b>，用來挑模型、調參數<br>"
    "・<b>測試集 (Test, 15~20%)</b> = <b>正式大考</b>，"
    "<b>只能用一次</b>，用來報告最終成績<br><br>"
    "為什麼驗證和測試要分開？因為你如果反覆拿測試集調參數，"
    "等於<b>間接把答案洩漏給模型</b>，最後那個分數就不誠實了。"
)

st.markdown("### 交叉驗證（Cross-Validation）：資料少的時候的標準做法")

st.markdown(
    "把資料切成 5 份，**輪流讓其中 1 份當驗證集**，跑 5 次取平均。"
    "好處是每一筆資料都當過驗證，結果比只切一次穩定得多。"
)

fold_fig = go.Figure()
for i in range(5):
    for j in range(5):
        is_val = i == j
        fold_fig.add_shape(
            type="rect", x0=j, x1=j + 0.92, y0=-i, y1=-i + 0.8,
            fillcolor=C["warn"] if is_val else "rgba(37,99,235,0.35)",
            line=dict(width=0),
        )
    fold_fig.add_annotation(x=-0.45, y=-i + 0.4, text=f"第 {i+1} 輪",
                            showarrow=False, xanchor="right", font=dict(size=12))
fold_fig.update_layout(
    title="5-Fold 交叉驗證（橘色 = 該輪的驗證集，藍色 = 訓練集）",
    xaxis=dict(visible=False, range=[-2, 5.2]),
    yaxis=dict(visible=False, range=[-4.4, 1.2]),
    height=300, showlegend=False,
)
st.plotly_chart(style(fold_fig, 300), width="stretch")

code(
    """
from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="f1")

print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")
# ↑ 一定要同時報「平均」和「標準差」。
#   標準差很大 = 模型不穩定，換一批資料表現就變了。
""",
    "報告成績時只講平均值是不夠的",
)

pitfall(
    "<b>時間序列資料絕對不能用隨機切分或一般的 K-Fold。</b>"
    "隨機切等於「用 2026 年的資料預測 2024 年」，這是拿未來預測過去，"
    "分數會虛高到不可思議。<br>"
    "要用 <code>TimeSeriesSplit</code>，永遠只用過去的資料預測未來。"
)

# ---------------------------------------------------------------- 解法
st.markdown("## 3. 過擬合的六個解法（照這個順序試）")

st.markdown(
    """
| 順序 | 方法 | 白話 | 怎麼做 |
|---|---|---|---|
| 1️⃣ | **加更多資料** | 考古題背不完就不會想背了 | 蒐集更多、或做**資料增強**（圖片翻轉、裁切） |
| 2️⃣ | **簡化模型** | 別用大砲打小鳥 | 降低樹的深度、減少神經網路層數 |
| 3️⃣ | **正則化 Regularization** | 罰你把某個特徵看得太重 | L1 / L2（下面詳細說） |
| 4️⃣ | **Dropout**（神經網路） | 上課隨機叫人閉眼，逼大家都要會 | 訓練時隨機關掉一部分神經元 |
| 5️⃣ | **提前停止 Early Stopping** | 驗證分數開始變差就收手 | 監控驗證 loss，連續 N 輪沒進步就停 |
| 6️⃣ | **減少特徵** | 欄位太多容易學到假規律 | 特徵選擇、PCA 降維 |
"""
)

st.markdown("### 正則化到底在做什麼")

analogy(
    "模型有 100 個權重。<b>過擬合的模型，通常有幾個權重大得誇張</b>"
    "（把某個雜訊特徵當成聖旨）。<br><br>"
    "正則化就是在損失函數後面<b>加一條「權重太大就罰你」的懲罰項</b>：<br>"
    "<code>總損失 = 預測誤差 + λ × 權重的大小</code><br><br>"
    "・<b>L2（Ridge）</b>罰權重的<b>平方</b> → 把權重壓小，但不會壓到 0<br>"
    "・<b>L1（Lasso）</b>罰權重的<b>絕對值</b> → 會把沒用的權重<b>直接壓成 0</b>，"
    "等於幫你做特徵選擇<br><br>"
    "<b>λ 越大 = 罰越兇 = 模型越簡單。</b>"
)

lam = st.slider("λ（正則化強度）", 0.0, 8.0, 0.0, 0.2, key="lam")
d_fix = 12
Xp = np.vander(xtr, d_fix + 1)
I = np.eye(d_fix + 1)
I[-1, -1] = 0  # 不罰截距
coef_r = np.linalg.solve(Xp.T @ Xp + lam * 1e3 * I, Xp.T @ ytr)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xtr, y=ytr, mode="markers", name="訓練資料",
                         marker=dict(size=10, color=C["primary"])))
fig.add_trace(go.Scatter(x=xte, y=yte, mode="markers", name="測試資料",
                         marker=dict(size=12, color=C["good"], symbol="star")))
fig.add_trace(go.Scatter(x=xs, y=np.polyval(coef_r, xs), mode="lines",
                         name=f"12 次多項式 + L2 (λ={lam})",
                         line=dict(color=C["bad"], width=3)))
fig.update_layout(title="同樣是 12 次的複雜模型，加了 L2 之後曲線就被「拉直」了",
                  yaxis_range=[min(y) - 30, max(y) + 30])
st.plotly_chart(style(fig, 380), width="stretch")
st.caption(f"權重總大小：{np.abs(coef_r[:-1]).sum():.4f}　（λ 拉大 → 權重被壓小 → 曲線變平滑）")

code(
    """
from sklearn.linear_model import Ridge, Lasso, LogisticRegression

Ridge(alpha=1.0)                     # L2：壓小權重
Lasso(alpha=0.1)                     # L1：把沒用的權重壓成 0，順便做特徵選擇
LogisticRegression(penalty="l2", C=1.0)   # 注意！C 是 alpha 的「倒數」，C 越小罰越兇

# 神經網路的 Dropout
import torch.nn as nn
nn.Sequential(nn.Linear(128, 64), nn.ReLU(), nn.Dropout(0.3), nn.Linear(64, 2))
""",
    "sklearn 的 C 和 alpha 方向相反，這是很常見的踩雷點",
)

# ---------------------------------------------------------------- 偏差變異
st.markdown("## 4. 偏差 vs 變異（Bias-Variance Tradeoff）")

analogy(
    "想像射飛鏢：<br>"
    "・<b>高偏差 Bias</b> = 每支都射在同一個地方，但<b>整團都偏離紅心</b> → 模型太笨（欠擬合）<br>"
    "・<b>高變異 Variance</b> = 每支都散得到處都是 → 模型太敏感，換批資料結果就變（過擬合）<br><br>"
    "<b>總誤差 = 偏差² + 變異 + 無法消除的雜訊</b><br>"
    "壓低一邊通常會抬高另一邊，所以叫 <b>trade-off</b>。"
)

st.markdown(
    """
| 症狀 | 診斷 | 處方 |
|---|---|---|
| 訓練分數低，驗證分數也低 | **高偏差 / 欠擬合** | 換更複雜的模型、加特徵、降低正則化、訓練久一點 |
| 訓練分數高，驗證分數低 | **高變異 / 過擬合** | 加資料、簡化模型、**加強正則化**、Dropout |
| 兩者都高且接近 | ✅ 剛好 | 可以上線了 |
"""
)

jobnote(
    "面試官最愛的實戰題：<b>「你的模型訓練準確率 98%、驗證準確率 62%，你會怎麼辦？」</b><br><br>"
    "<b>標準答法（照順序講）</b>：<br>"
    "1. 這是典型過擬合，訓練和驗證落差 36% 太大<br>"
    "2. 先檢查<b>有沒有資料洩漏</b>，還有訓練/驗證的資料分布是不是一致<br>"
    "3. 畫<b>學習曲線</b>，看加資料有沒有用<br>"
    "4. 依序試：加正則化 → 簡化模型 → 資料增強 → Early Stopping<br>"
    "5. 用<b>交叉驗證</b>確認結果穩定，不是運氣<br><br>"
    "重點是展現你有<b>系統化的除錯流程</b>，不是亂槍打鳥。"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "什麼是過擬合？怎麼判斷？怎麼解決？",
    """
**是什麼**：模型把訓練資料的**雜訊和偶然特徵**也學進去了，
導致在沒看過的資料上表現很差。等於「背答案而不是學方法」。

**怎麼判斷**：訓練分數 >> 驗證分數。畫學習曲線，兩條線的差距（gap）不收斂。

**怎麼解決**（照效益排序）：
1. 加更多訓練資料（最有效，但最貴）
2. 資料增強（圖片用翻轉/裁切/調色）
3. 正則化 L1/L2、Dropout
4. 簡化模型（減層數、減樹深）
5. Early Stopping
6. 集成多個模型（Bagging）
""",
)

interview(
    "L1 和 L2 正則化的差別？什麼時候用哪個？",
    """
| | **L1 (Lasso)** | **L2 (Ridge)** |
|---|---|---|
| 罰什麼 | 權重的**絕對值** \\|w\\| | 權重的**平方** w² |
| 效果 | 權重被壓到**剛好 0** | 權重變小但**不會是 0** |
| 附加價值 | **自動特徵選擇** | 處理多重共線性 |

**為什麼 L1 會壓到 0**：L1 的懲罰在 0 附近是尖角，梯度是常數 ±λ，
會持續把權重往 0 推；L2 的梯度是 2λw，權重越小推力越小，所以只會逼近 0 而到不了 0。

**怎麼選**：
- 特徵很多、懷疑大部分沒用 → **L1**
- 特徵都有點用、彼此高度相關 → **L2**
- 不確定 → **Elastic Net**（兩個混合）
""",
)

interview(
    "為什麼要用交叉驗證？只切一次訓練/測試不行嗎？",
    """
**可以，但不穩。**

只切一次的問題：分數會嚴重受「剛好切到哪些資料」影響。
資料量小的時候，換一個 `random_state` 分數可能差 5～10%，
那你根本不知道模型 A 比模型 B 好，是真的好還是運氣好。

**交叉驗證的好處**：
1. 每一筆資料都當過一次驗證資料，估計更穩
2. 會給你**標準差**，可以判斷模型穩不穩定
3. 小資料集也能充分利用

**代價**：訓練 K 次，時間變 K 倍。所以資料量很大時（幾百萬筆），
反而常常只切一次就好——因為資料夠多，估計本來就穩了。
""",
)

interview(
    "訓練集和測試集的分布不一樣，會發生什麼事？怎麼發現？",
    """
這叫 **Distribution Shift / Covariate Shift**，
會導致模型在測試集（或上線後）大幅掉分，而且**你從訓練指標完全看不出來**。

**常見原因**：
- 時間造成的（用 2023 資料訓練，2026 上線，用戶行為變了）
- 抽樣造成的（訓練資料只有台北的客戶，上線後全台都有）

**怎麼發現（實用技巧）**：**Adversarial Validation**
把訓練集標為 0、測試集標為 1，訓練一個分類器去分辨它們。
如果 **AUC 接近 0.5**，代表兩份資料長得一樣，很好；
如果 **AUC 接近 1.0**，代表模型輕鬆分得出來 → **分布明顯不同**，要處理。

這題答得出 Adversarial Validation，會被視為有實戰經驗。
""",
)

next_step("到「🧠 神經網路是什麼」，正式進入深度學習。")
