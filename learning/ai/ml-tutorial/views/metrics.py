import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import style

hero(
    "第一站 · 資料",
    "🎯 評估指標：Recall、Precision、F1",
    "模型說「準確率 99%」可能完全沒用。這一章教你看穿數字背後的真相。",
)

takeaway(
    "<b>Recall（召回率）＝ 該抓的，抓到幾成。</b>（漏掉的代價很高時看這個）<br>"
    "<b>Precision（精確率）＝ 抓的裡面，對了幾成。</b>（誤抓的代價很高時看這個）<br>"
    "兩個天生互相拉扯，<b>F1</b> 是它們的平衡分數。"
)

# ---------------------------------------------------------------- 先講故事
st.markdown("## 1. 為什麼「準確率 99%」是陷阱")

analogy(
    "醫院要做癌症篩檢，1000 個人裡有 <b>10 個</b>真的有癌症。<br>"
    "我寫一個模型，程式碼只有一行：<code>return \"沒有癌症\"</code>。<br><br>"
    "這個模型的<b>準確率是 99%</b>（1000 個猜對 990 個）—— "
    "但它<b>一個病人都沒抓到</b>，完全沒用。<br><br>"
    "這叫 <span class='term'>不平衡資料（imbalanced data）</span>，"
    "現實世界的問題幾乎都是這樣：詐欺交易、機台故障、癌症、客戶流失。"
)

st.error(
    "**所以：只要正例（要抓的那類）很少，準確率 Accuracy 就沒有參考價值。**\n\n"
    "這時候要看 Recall 和 Precision。",
    icon="🚨",
)

# ---------------------------------------------------------------- 混淆矩陣
st.markdown("## 2. 一切的起點：混淆矩陣（Confusion Matrix）")

st.markdown(
    "把「模型怎麼猜」和「事實是什麼」交叉，只會有 4 種結果。**這四格是所有指標的原料。**"
)

st.markdown(
    """
|  | **事實：有病 🦠** | **事實：沒病 ✅** |
|---|---|---|
| **模型說：有病** | 🟢 **TP** 真陽性 — 抓對了 | 🔴 **FP** 偽陽性 — 虛驚一場（誤報） |
| **模型說：沒病** | 🔴 **FN** 偽陰性 — **漏掉了**（最可怕） | 🟢 **TN** 真陰性 — 放對了 |
"""
)

st.info(
    "**記法**：第二個字母是「模型說什麼」（P=說有、N=說沒有），"
    "第一個字母是「模型說對了嗎」（T=對、F=錯）。"
    "所以 **FN = 模型說沒有，但說錯了 = 漏抓**。",
    icon="🧠",
)

st.markdown("### 三個指標的公式（用上面四格算）")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### 🎯 Recall（召回率）")
    st.latex(r"\text{Recall} = \frac{TP}{TP + FN}")
    st.markdown(
        "**分母是「事實上真的有病的全部人」**。\n\n"
        "問的是：*該抓的人裡，我抓到幾成？*\n\n"
        "又叫 **Sensitivity（敏感度）**、**TPR**。"
    )
with c2:
    st.markdown("#### 🔍 Precision（精確率）")
    st.latex(r"\text{Precision} = \frac{TP}{TP + FP}")
    st.markdown(
        "**分母是「模型說有病的全部人」**。\n\n"
        "問的是：*我抓的人裡，真的有病的幾成？*\n\n"
        "又叫 **PPV（陽性預測值）**。"
    )
with c3:
    st.markdown("#### ⚖️ F1 Score")
    st.latex(r"F_1 = \frac{2 \cdot P \cdot R}{P + R}")
    st.markdown(
        "兩者的**調和平均數**。\n\n"
        "只要有一個很低，F1 就會被拉下來 —— "
        "所以它逼你**兩個都要顧**。"
    )

# ---------------------------------------------------------------- 互動模擬
st.markdown("## 3. 動手玩：拖動閾值，看指標怎麼變")

analogy(
    "模型輸出的其實不是「有病 / 沒病」，而是一個 <b>0 到 1 的機率</b>，例如 0.73。<br>"
    "你要自己決定：<b>超過多少才算「有病」？</b> 這條線叫 <span class='term'>閾值（threshold）</span>，"
    "預設是 0.5，但你可以改。<br><br>"
    "<b>調低閾值</b> → 寧可錯殺，抓得多 → <b>Recall ↑，Precision ↓</b><br>"
    "<b>調高閾值</b> → 很有把握才抓 → <b>Precision ↑，Recall ↓</b>"
)


@st.cache_data
def make_scores(n_pos=100, n_neg=900, sep=1.6, seed=7):
    """模擬模型輸出的機率：有病的人分數偏高，沒病的偏低，但會重疊。"""
    rng = np.random.default_rng(seed)
    pos = 1 / (1 + np.exp(-(rng.normal(sep, 1.0, n_pos))))
    neg = 1 / (1 + np.exp(-(rng.normal(-sep, 1.0, n_neg))))
    y = np.r_[np.ones(n_pos), np.zeros(n_neg)]
    s = np.r_[pos, neg]
    return y, s


cfg1, cfg2 = st.columns(2)
with cfg1:
    sep = st.slider("模型有多聰明（分辨兩群的能力）", 0.2, 3.5, 1.6, 0.1,
                    help="數字越大，有病和沒病的分數分得越開，模型越強")
with cfg2:
    thr = st.slider("🎚️ 閾值 threshold（超過這個分數就判定為「有病」）",
                    0.05, 0.95, 0.50, 0.01)

y, s = make_scores(sep=sep)
pred = (s >= thr).astype(int)

TP = int(((pred == 1) & (y == 1)).sum())
FP = int(((pred == 1) & (y == 0)).sum())
FN = int(((pred == 0) & (y == 1)).sum())
TN = int(((pred == 0) & (y == 0)).sum())

recall = TP / (TP + FN) if TP + FN else 0
precision = TP / (TP + FP) if TP + FP else 0
f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
acc = (TP + TN) / len(y)

k1, k2, k3, k4 = st.columns(4)
k1.metric("🎯 Recall", f"{recall:.1%}", help=f"{TP} / ({TP}+{FN}) — 100 個病人抓到 {TP} 個")
k2.metric("🔍 Precision", f"{precision:.1%}",
          help=f"{TP} / ({TP}+{FP}) — 抓了 {TP+FP} 個，其中 {TP} 個是真的")
k3.metric("⚖️ F1 Score", f"{f1:.1%}")
k4.metric("😐 Accuracy", f"{acc:.1%}", help="這個數字很漂亮，但沒什麼用 —— 因為資料不平衡")

left, right = st.columns([1, 1])

with left:
    st.markdown("**混淆矩陣（人數）**")
    z = [[TP, FP], [FN, TN]]
    labels = [[f"TP<br>{TP}", f"FP<br>{FP}"], [f"FN<br>{FN}", f"TN<br>{TN}"]]
    fig = go.Figure(
        go.Heatmap(
            z=z,
            x=["事實：有病", "事實：沒病"],
            y=["模型說：有病", "模型說：沒病"],
            text=labels,
            texttemplate="%{text}",
            textfont=dict(size=17),
            colorscale=[[0, "rgba(37,99,235,0.08)"], [1, "rgba(37,99,235,0.75)"]],
            showscale=False,
        )
    )
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(style(fig, 320), width="stretch")
    st.caption(f"🔴 漏掉了 **{FN}** 個病人　|　🔴 誤抓了 **{FP}** 個健康的人")

with right:
    st.markdown("**分數分布與你拉的那條線**")
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=s[y == 0], nbinsx=45, name="事實：沒病",
                               marker_color=C["primary"], opacity=0.65))
    fig.add_trace(go.Histogram(x=s[y == 1], nbinsx=45, name="事實：有病",
                               marker_color=C["bad"], opacity=0.75))
    fig.add_vline(x=thr, line_width=3, line_color=C["warn"],
                  annotation_text="閾值", annotation_position="top")
    fig.update_layout(barmode="overlay", xaxis_title="模型給的分數（機率）", yaxis_title="人數")
    st.plotly_chart(style(fig, 320), width="stretch")
    st.caption("線的右邊都被判定為「有病」。往左拉 → 抓更多人。")

st.warning(
    f"**現在這個設定的白話翻譯**：\n\n"
    f"- 100 個真病人，你抓到 **{TP}** 個、**漏掉 {FN}** 個 → Recall {recall:.0%}\n"
    f"- 你總共叫了 **{TP+FP}** 個人回來複檢，其中 **{FP}** 個是白跑一趟 → Precision {precision:.0%}\n\n"
    f"癌症篩檢該調哪一邊？→ **把閾值往左拉，寧可多叫人回來，也不能漏掉。**",
    icon="💬",
)

# ---------------------------------------------------------------- 該看哪個
st.markdown("## 4. 什麼時候看 Recall，什麼時候看 Precision")

st.markdown(
    """
判斷方法只有一句話：**問自己「哪一種錯比較痛？」**

| 情境 | 漏掉（FN）的代價 | 誤抓（FP）的代價 | 該優化 |
|---|---|---|---|
| 🦠 **癌症篩檢** | 病人死掉 | 多做一次檢查 | **Recall** |
| 💳 **信用卡盜刷偵測** | 客戶損失金錢 | 打電話確認一下 | **Recall** |
| 🏭 **工廠瑕疵檢測** | 瑕疵品流到客戶手上 | 人工再檢查一次 | **Recall** |
| 📧 **垃圾郵件過濾** | 看到一封垃圾信 | **重要信件被丟掉** | **Precision** |
| 🎬 **推薦系統** | 少推一部好片 | 推爛片，用戶不爽走人 | **Precision** |
| ⚖️ **法院量刑輔助** | 壞人逃過 | **冤枉好人** | **Precision** |

**看不出來哪個重要 → 看 F1。**
"""
)

jobnote(
    "面試官問「你這個模型好不好」，只回「準確率 95%」會直接被扣分。<br>"
    "<b>標準答法</b>：「這是不平衡資料，正例只佔 3%，所以我看的是 Recall 和 Precision。"
    "業務上漏抓的成本比較高，所以我把閾值調到 0.3，讓 Recall 拉到 92%，"
    "代價是 Precision 掉到 45%，也就是人工複檢量會變 2 倍 —— "
    "我跟業務單位確認過他們的人力可以吸收。」<br><br>"
    "<b>重點是：把指標翻譯成商業語言。</b>這是資深和菜鳥的分水嶺。"
)

# ---------------------------------------------------------------- ROC
st.markdown("## 5. ROC 曲線與 AUC：不用挑閾值的總分")

analogy(
    "上面每拉一次閾值就得到一組 (Recall, Precision)。"
    "<b>ROC 曲線</b>就是把<b>所有可能的閾值</b>都試一遍，把結果連成一條線。<br><br>"
    "<b>AUC = 曲線下的面積</b>，一個 0.5～1.0 的總分：<br>"
    "・<b>0.5</b> = 跟丟銅板一樣爛　・<b>0.7～0.8</b> = 堪用　"
    "・<b>0.8～0.9</b> = 不錯　・<b>&gt;0.9</b> = 很強（或你資料洩漏了）"
)


def roc_points(y, s):
    order = np.argsort(-s)
    y_sorted = y[order]
    tp = np.cumsum(y_sorted)
    fp = np.cumsum(1 - y_sorted)
    tpr = np.r_[0, tp / max(y.sum(), 1)]
    fpr = np.r_[0, fp / max((1 - y).sum(), 1)]
    return fpr, tpr


fpr, tpr = roc_points(y, s)
auc = float(np.trapezoid(tpr, fpr)) if hasattr(np, "trapezoid") else float(np.trapz(tpr, fpr))

cur_fpr = FP / (FP + TN) if FP + TN else 0
fig = go.Figure()
fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=f"這個模型 (AUC={auc:.3f})",
                         line=dict(width=4, color=C["primary"]), fill="tozeroy",
                         fillcolor="rgba(37,99,235,0.12)"))
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="亂猜 (AUC=0.5)",
                         line=dict(dash="dash", color=C["muted"], width=2)))
fig.add_trace(go.Scatter(x=[cur_fpr], y=[recall], mode="markers",
                         name=f"你現在的閾值 {thr:.2f}",
                         marker=dict(size=15, color=C["warn"], symbol="x", line_width=2)))
fig.update_layout(title="ROC 曲線", xaxis_title="FPR：誤報率（健康的人被誤抓的比例）",
                  yaxis_title="TPR：Recall（病人被抓到的比例）")
st.plotly_chart(style(fig, 430), width="stretch")

st.success(
    f"**AUC = {auc:.3f}** 的白話意思：隨便抓一個病人和一個健康的人，"
    f"模型給病人的分數比較高的機率是 **{auc:.1%}**。"
    "（試著把上面「模型有多聰明」的滑桿拉大，看曲線怎麼往左上角靠。）",
    icon="📈",
)

pitfall(
    "<b>資料極度不平衡時（正例 &lt; 1%），AUC 會過度樂觀。</b>"
    "因為 FPR 的分母是「全部健康的人」，數量超大，就算誤抓一堆，FPR 看起來還是很小。<br>"
    "這時候要改看 <b>PR 曲線（Precision-Recall Curve）</b>和 <b>Average Precision</b>。"
    "這題答得出來，面試官會眼睛一亮。"
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 6. 實際怎麼寫")

code(
    """
from sklearn.metrics import (
    confusion_matrix, classification_report,
    precision_score, recall_score, f1_score, roc_auc_score,
)

# 1) 一次看全部（最常用）
print(classification_report(y_test, y_pred, target_names=["沒病", "有病"]))

# 2) 混淆矩陣
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# 3) 單獨算
recall_score(y_test, y_pred)       # TP / (TP + FN)
precision_score(y_test, y_pred)    # TP / (TP + FP)
f1_score(y_test, y_pred)

# 4) AUC 要用「機率」，不是 0/1 的預測結果 —— 這裡最常寫錯
y_proba = model.predict_proba(X_test)[:, 1]
roc_auc_score(y_test, y_proba)

# 5) 自己調閾值（預設 0.5 不是聖旨）
y_pred_custom = (y_proba >= 0.30).astype(int)
""",
    "sklearn 的評估指標，這 5 段幾乎涵蓋日常 90% 的需求",
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "解釋 Precision 和 Recall 的差別。",
    """
用一句話定義 + 一個例子，是最漂亮的答法：

> **Recall 是「該抓的抓到幾成」，分母是所有真正的正例；
> Precision 是「抓的裡面對幾成」，分母是所有被判為正例的。**
>
> 以癌症篩檢為例：100 個真病人我抓到 90 個 → Recall 90%；
> 但我總共叫了 300 人回來複檢，只有 90 個真的有病 → Precision 30%。

**加分句**：兩者有 trade-off，調閾值只能往一邊移，
所以要看業務上是「漏抓」還是「誤抓」比較貴。
""",
)

interview(
    "模型準確率 99%，可以上線嗎？",
    """
**先反問：正負樣本比例是多少？**

如果正例只佔 1%，那全部猜「負」就有 99% 準確率，模型可能什麼都沒學到。

**要看的是**：
1. 混淆矩陣（尤其是 FN 和 FP 各幾個）
2. Recall / Precision / F1
3. 跟 baseline 比（全猜多數類、或隨機猜，分數是多少？）
4. AUC 或 PR-AUC

這題考的是**你會不會被漂亮數字騙**，是很常見的第一輪篩人題。
""",
)

interview(
    "為什麼 F1 用調和平均數，不用普通的平均數？",
    """
**因為調和平均數會「懲罰極端」。**

假設 Precision = 1.0、Recall = 0.01（只抓一個人但抓對了）：

- 算術平均 = (1.0 + 0.01) / 2 = **0.505** ← 看起來還行，但這模型根本沒用
- 調和平均 F1 = 2 × 1.0 × 0.01 / 1.01 = **0.0198** ← 誠實反映它很爛

**調和平均數會被小的那個拉住**，所以 F1 逼你兩個都要顧，不能靠單邊刷分。
""",
)

interview(
    "什麼情況該用 PR 曲線而不是 ROC 曲線？",
    """
**極度不平衡的資料（正例佔比很低，例如詐欺偵測、罕見疾病）。**

原因：ROC 的橫軸 FPR = FP / (FP + TN)，分母 TN 超級大（健康的人很多），
所以就算誤報了 500 人，FPR 可能只有 0.005，曲線看起來還是很漂亮。

PR 曲線的 Precision = TP / (TP + FP)，**分母裡沒有 TN**，
誤報一多 Precision 馬上掉下來，比較誠實。

用 `sklearn.metrics.average_precision_score` 算 PR 曲線下面積。
""",
)

interview(
    "多分類（不只兩類）的時候，Precision / Recall 怎麼算？",
    """
拆成「每一類 vs 其他」分別算，再用三種方式合併：

| 方式 | 怎麼算 | 什麼時候用 |
|---|---|---|
| **macro** | 每類算完，直接平均 | **每一類都同等重要**（小類別權重不會被淹沒） |
| **weighted** | 每類算完，依樣本數加權平均 | 想反映整體表現 |
| **micro** | 把所有類別的 TP/FP/FN 加總後才算 | 多標籤分類；在單標籤時 micro-F1 = Accuracy |

**面試最愛考**：類別不平衡時該用哪個？→ **macro**，
因為 weighted 會被大類別主導，看不出小類別爛掉了。

```python
f1_score(y_true, y_pred, average="macro")
```
""",
)

next_step("到「🤖 機器學習基礎」，看模型到底怎麼從資料裡「學」出規律。")
