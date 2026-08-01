import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import heatmap, style

hero(
    "第三站 · 深度學習",
    "✨ Transformer 與 Attention",
    "ChatGPT、Claude、Gemini 全部都是它。2017 年一篇論文改變了整個 AI 產業。",
)

takeaway(
    "<b>Attention（注意力）= 句子裡每一個字，都直接去問其他所有字："
    "「你跟我有關嗎？」有關的就多看幾眼。</b><br>"
    "RNN 要一步一步傳話，Transformer 讓所有字<b>一次全部互看</b> —— "
    "所以它又快又記得住長距離的關係。"
)

# ---------------------------------------------------------------- 動機
st.markdown("## 1. 先看它解決什麼問題")

analogy(
    "「小貓追著老鼠跑，因為<b>牠</b>餓了。」<br><br>"
    "「牠」指的是誰？你的大腦會自動<b>回頭去看「小貓」</b>，而不是平均看整句話。<br><br>"
    "這個<b>「回頭去看相關的字」</b>的動作，就是 Attention。<br>"
    "而且注意：小貓和牠之間隔了 6 個字，但你<b>一眼就連上了</b>，"
    "不需要像 RNN 那樣一個字一個字傳話過去。"
)

st.markdown("### 一個訓練好的模型，注意力大概長這樣")

sent = ["小貓", "追", "老鼠", "因為", "牠", "餓", "了"]
# 示意用的注意力權重（真實模型會自己學出類似的模式）
A_demo = np.array([
    [.62, .08, .10, .04, .10, .03, .03],
    [.34, .22, .30, .04, .05, .03, .02],
    [.12, .24, .48, .05, .06, .03, .02],
    [.08, .10, .10, .30, .20, .18, .04],
    [.55, .05, .12, .06, .14, .06, .02],   # ← 「牠」高度關注「小貓」
    [.20, .04, .06, .10, .46, .12, .02],
    [.06, .08, .06, .12, .20, .40, .08],
])

st.plotly_chart(
    heatmap(A_demo.round(2), x=sent, y=sent, text=A_demo.round(2),
            title="每一列 = 一個字在「看」誰（顏色越深看得越重）", height=420),
    width="stretch",
)

st.info(
    "**看第 5 列「牠」**：0.55 的注意力給了「小貓」—— "
    "模型自己學會了代名詞指涉。這種圖是 Transformer 可解釋性的最大賣點。"
    "（此圖為示意，數值是手工設定的；真實模型的權重是訓練出來的。）",
    icon="👀",
)

# ---------------------------------------------------------------- QKV
st.markdown("## 2. 核心：Query、Key、Value（Q、K、V）")

analogy(
    "把它想成<b>用搜尋引擎找資料</b>：<br><br>"
    "・<b>Query（查詢）</b>= 你在搜尋框打的關鍵字 →「我是代名詞『牠』，我在找一個動物」<br>"
    "・<b>Key（索引）</b>= 每篇文章的標題 →「我是『小貓』，我是動物」<br>"
    "・<b>Value（內容）</b>= 文章的實際內容 → 真正要拿走的資訊<br><br>"
    "流程：<b>拿我的 Query 去和所有人的 Key 比對相似度 → "
    "相似度高的，就多拿一點他的 Value。</b>"
)

st.markdown("### 完整公式（面試要能默寫）")

st.latex(r"\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V")

st.markdown(
    """
一步一步拆開：

| 步驟 | 算式 | 在做什麼 |
|---|---|---|
| ① | $Q = XW_Q,\\ K = XW_K,\\ V = XW_V$ | 把每個字的向量，用三組**要訓練的**權重投影成三種身分 |
| ② | $QK^\\top$ | 算「每個字」對「每個字」的相似度（內積越大越相關） |
| ③ | $\\div \\sqrt{d_k}$ | **縮放**，避免數字太大讓 softmax 變得極端 |
| ④ | $\\text{softmax}$ | 把相似度變成加總為 1 的**權重比例** |
| ⑤ | $\\times V$ | 按照權重，把大家的 Value **加權平均**起來 |
"""
)

# ---------------------------------------------------------------- 實際計算
st.markdown("## 3. 動手算一次：4 個字、4 維向量")

st.markdown(
    "下面是**真的在算**（不是示意圖）。"
    "四個字的向量是我手動設計的，讓語意相近的字向量也相近。"
)

words = ["貓", "狗", "追", "跑"]
# 手工設計的 4 維語意向量：[是動物, 是動作, 移動性, 情緒]
X = np.array([
    [1.0, 0.0, 0.3, 0.4],   # 貓：動物
    [1.0, 0.0, 0.4, 0.5],   # 狗：動物，和貓很像
    [0.0, 1.0, 0.9, 0.2],   # 追：動作
    [0.0, 1.0, 1.0, 0.1],   # 跑：動作，和追很像
])

cc1, cc2 = st.columns(2)
with cc1:
    scale_on = st.checkbox("開啟 √dₖ 縮放", value=True)
with cc2:
    temp = st.slider("注意力銳利度（實驗用，看 softmax 的效果）", 0.3, 6.0, 1.0, 0.1)

d_k = X.shape[1]
scores = (X @ X.T) * temp
if scale_on:
    scores = scores / np.sqrt(d_k)

exp = np.exp(scores - scores.max(axis=1, keepdims=True))
attn = exp / exp.sum(axis=1, keepdims=True)
out = attn @ X

s1, s2, s3 = st.columns(3)
with s1:
    st.plotly_chart(
        heatmap(X.round(2), x=["是動物", "是動作", "移動性", "情緒"], y=words,
                text=X.round(1), title="① 輸入向量 X", height=330),
        width="stretch",
    )
with s2:
    st.plotly_chart(
        heatmap(scores.round(2), x=words, y=words, text=scores.round(2),
                colorscale="Oranges",
                title=f"② 相似度分數 QKᵀ{' ÷ √4' if scale_on else '（未縮放）'}", height=330),
        width="stretch",
    )
with s3:
    st.plotly_chart(
        heatmap(attn.round(2), x=words, y=words, text=attn.round(2),
                title="③ softmax 後的注意力權重（每列加總 = 1）", height=330),
        width="stretch",
    )

st.markdown("**④ 加權平均後，每個字的新向量：**")
st.plotly_chart(
    heatmap(out.round(2), x=["是動物", "是動作", "移動性", "情緒"], y=words,
            text=out.round(2), colorscale="Greens",
            title="輸出 = 注意力權重 × V —— 每個字都「吸收」了相關字的資訊", height=300),
    width="stretch",
)

st.success(
    f"**看「貓」那一列的注意力**：給自己 {attn[0,0]:.2f}、給「狗」{attn[0,1]:.2f}"
    f"（都是動物，相似度高）、給「追」{attn[0,2]:.2f}、「跑」{attn[0,3]:.2f}。\n\n"
    "**這就是 Attention 的全部**——沒有魔法，就是相似度加權平均。",
    icon="🎯",
)

st.markdown("### 為什麼要除以 √dₖ")

st.markdown(
    "把上面的「銳利度」滑桿拉到最大（模擬沒有縮放、數字很大的情況），"
    "會看到注意力變成**幾乎全部集中在一格**（接近 one-hot）。"
)

demo_scores = np.array([2.0, 1.5, 1.0, 0.5])
fig = go.Figure()
for mult, name in [(1, "有縮放（分數小）"), (8, "沒縮放（分數大 8 倍）")]:
    e = np.exp(demo_scores * mult - (demo_scores * mult).max())
    fig.add_trace(go.Bar(x=["字1", "字2", "字3", "字4"], y=e / e.sum(), name=name))
fig.update_layout(barmode="group", title="同樣的相對大小，分數放大之後 softmax 變得極端",
                  yaxis_title="注意力權重")
st.plotly_chart(style(fig, 330), width="stretch")

pitfall(
    "分數太大 → softmax 幾乎全押一格 → <b>梯度趨近 0，模型學不動</b>。<br>"
    "而向量維度 dₖ 越大，內積的數值自然越大（因為是 dₖ 項相加），"
    "所以要除以 <b>√dₖ</b> 把變異數拉回 1 左右。<br><br>"
    "<b>面試常問</b>：為什麼是 √dₖ 而不是 dₖ？<br>"
    "→ 假設 Q、K 各維度獨立、平均 0 變異數 1，那內積的變異數就是 dₖ，"
    "標準差是 √dₖ，所以除以 √dₖ 才能把標準差normalize 回 1。"
)

# ---------------------------------------------------------------- 多頭
st.markdown("## 4. 多頭注意力 Multi-Head Attention")

analogy(
    "一個人讀句子只能一次抓一種關係。<b>那就找 8 個人同時讀</b>，"
    "每個人專注在不同的面向：<br><br>"
    "・第 1 頭：注意<b>文法主詞-動詞</b>的關係<br>"
    "・第 2 頭：注意<b>代名詞指誰</b><br>"
    "・第 3 頭：注意<b>相鄰的字</b><br>"
    "・第 4 頭：注意<b>語意相近的詞</b><br><br>"
    "最後把 8 個人的結論<b>接起來</b>，再過一層線性層整合。"
)

st.markdown(
    """
**實作細節**：不是真的做 8 次完整運算。而是把 512 維的向量
**切成 8 份、每份 64 維**，各自做 attention，最後再接回 512 維。

所以：**多頭幾乎不增加計算量，但表達能力大幅提升。**
"""
)

nh = st.slider("幾個注意力頭", 1, 8, 4)
rng = np.random.default_rng(42)
fig = go.Figure()
for i in range(nh):
    pattern = rng.dirichlet(np.ones(7) * (0.4 + 0.3 * i))
    fig.add_trace(go.Bar(x=sent, y=pattern, name=f"第 {i+1} 頭"))
fig.update_layout(barmode="group", title="不同的頭關注不同的字（示意）", yaxis_title="注意力權重")
st.plotly_chart(style(fig, 340), width="stretch")

# ---------------------------------------------------------------- 位置編碼
st.markdown("## 5. 位置編碼：Attention 有個大問題")

pitfall(
    "Attention 是<b>加權平均</b>，而平均<b>沒有順序概念</b>。<br>"
    "「狗咬人」和「人咬狗」在純 Attention 眼中<b>完全一樣</b>！<br><br>"
    "所以必須額外把「你是第幾個字」這個資訊<b>加進向量裡</b> —— "
    "這就是 <span class='term'>位置編碼（Positional Encoding）</span>。"
)

st.latex(r"PE_{(pos,\,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right), \quad PE_{(pos,\,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)")

seq_len, d_model = 40, 48
pos = np.arange(seq_len)[:, None]
i = np.arange(d_model)[None, :]
angle = pos / np.power(10000, (2 * (i // 2)) / d_model)
PE = np.where(i % 2 == 0, np.sin(angle), np.cos(angle))

st.plotly_chart(
    heatmap(PE.round(2), title="位置編碼矩陣（橫軸 = 向量的第幾維，縱軸 = 第幾個字）",
            colorscale="RdBu", height=400),
    width="stretch",
)

st.caption(
    "每一列（每個位置）都有獨一無二的波形指紋，直接加到字的向量上。"
    "用 sin/cos 的好處：**可以外推到訓練時沒看過的長度**，而且相對位置關係可以用線性變換表示。"
)

st.markdown(
    "**現代做法**：GPT/Llama 等模型多半改用 **RoPE（旋轉位置編碼）**，"
    "把位置資訊用「旋轉向量」的方式編進 Q 和 K，長文本外推能力更好。"
)

# ---------------------------------------------------------------- 架構
st.markdown("## 6. 完整架構與三種變體")

st.markdown(
    """
```
輸入文字 → Tokenize（切成 token）→ Embedding + 位置編碼
   ↓
┌─── Transformer Block（重複 N 次，GPT-3 是 96 次）───┐
│  ① Multi-Head Self-Attention                       │
│  ② 殘差連接 + LayerNorm    ← 防梯度消失            │
│  ③ Feed-Forward（兩層全連接，中間放大 4 倍）        │
│  ④ 殘差連接 + LayerNorm                             │
└─────────────────────────────────────────────────┘
   ↓
輸出層 → 預測下一個 token 的機率
```

### 三種變體，用途完全不同

| 類型 | 代表 | 只看得到 | 擅長 |
|---|---|---|---|
| **Encoder-only** | BERT | **前後文都看得到** | 理解類任務：分類、命名實體辨識、搜尋 |
| **Decoder-only** | **GPT / Claude / Llama** | **只看得到前面**（因果遮罩） | **生成類任務**：對話、寫作、寫程式 |
| **Encoder-Decoder** | T5、原始 Transformer | 編碼器全看，解碼器只看前面 | 翻譯、摘要 |

**為什麼 GPT 只能看前面**？因為它的訓練目標是「**預測下一個字**」，
如果讓它看到後面，等於考試給答案。這個遮罩叫 **Causal Mask / 因果遮罩**。
"""
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 7. 程式碼：從零手刻 + 實務用法")

code(
    """
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    \"\"\"Attention 的完整實作 —— 面試可能會叫你當場寫出來。\"\"\"
    d_k = Q.size(-1)

    # ① 算相似度分數：(B, heads, L, d) @ (B, heads, d, L) -> (B, heads, L, L)
    scores = Q @ K.transpose(-2, -1) / (d_k ** 0.5)

    # ② 因果遮罩：把「未來」的位置設成 -inf，softmax 之後就變成 0
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))

    # ③ 轉成機率權重
    attn = F.softmax(scores, dim=-1)

    # ④ 加權平均 V
    return attn @ V, attn


# 產生因果遮罩（下三角矩陣：只能看自己和前面）
L = 5
causal_mask = torch.tril(torch.ones(L, L))
# tensor([[1,0,0,0,0],
#         [1,1,0,0,0],
#         [1,1,1,0,0],
#         [1,1,1,1,0],
#         [1,1,1,1,1]])
""",
    "手刻 Attention。第 8 行的 transpose 和第 15 行的 -inf 是最常寫錯的兩個地方",
)

code(
    """
# 實務上不會自己刻，直接用 Hugging Face
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

inputs = tokenizer("這部電影一點都不好看", return_tensors="pt",
                   padding=True, truncation=True, max_length=128)
outputs = model(**inputs)
probs = outputs.logits.softmax(-1)
""",
    "實務用法：pip install transformers（這個範例需要網路下載模型）",
)

jobnote(
    "<b>Transformer 是現在 NLP / LLM 職缺的門檻題，一定會考。</b>常見考法：<br><br>"
    "① 默寫 Attention 公式並解釋每一項<br>"
    "② 為什麼要除以 √dₖ<br>"
    "③ 多頭注意力的「多頭」是怎麼實作的（切維度，不是複製）<br>"
    "④ BERT 和 GPT 的差別<br>"
    "⑤ Self-Attention 的時間複雜度是多少（<b>O(n²·d)</b>，n 是序列長度）<br><br>"
    "轉職作品集建議：<b>拿 Hugging Face 的預訓練模型微調一個中文任務</b>"
    "（例如客訴分類、履歷篩選），這比從零訓練有價值得多。"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "解釋 Self-Attention 的運作流程。",
    """
**四步驟**：

1. **投影**：每個 token 的向量 x，乘上三組可訓練的權重矩陣，
   得到 `Q = xW_Q`（我在找什麼）、`K = xW_K`（我是什麼）、`V = xW_V`（我能提供什麼）
2. **算分數**：`QKᵀ`，得到 n×n 的矩陣，第 (i,j) 格代表「第 i 個字對第 j 個字的關注度」
3. **縮放 + Softmax**：除以 √d_k 後做 softmax，讓每一列加總為 1
4. **加權平均**：權重 × V，每個 token 得到一個「融合了相關 token 資訊」的新向量

**「Self」的意思**：Q、K、V **都來自同一個序列**。
如果 Q 來自解碼器、K/V 來自編碼器，那叫 **Cross-Attention**（翻譯時用）。
""",
)

interview(
    "為什麼要除以 √d_k？",
    """
**為了穩定梯度。**

假設 Q、K 的每個維度都是平均 0、變異數 1 的獨立隨機變數，
那 `q·k = Σ qᵢkᵢ` 是 d_k 項相加，**變異數就是 d_k**，標準差是 **√d_k**。

d_k = 512 時，內積的數值範圍大約是 ±22。這麼大的數字丟進 softmax，
會讓輸出接近 **one-hot**（幾乎全押一格），而 softmax 在飽和區的**梯度趨近 0**，
模型就學不動了。

除以 √d_k 把標準差拉回 1，softmax 的輸出就平滑得多。
""",
)

interview(
    "Multi-Head Attention 的「多頭」是怎麼實作的？為什麼要多頭？",
    """
**實作**：不是重複算 h 次。而是把 d_model（例如 512）**切成 h 份**
（8 頭 → 每頭 64 維），每份獨立做一次 attention，
最後把 8 個 64 維的輸出 **concat 回 512 維**，再過一層 `W_O` 整合。

**所以總計算量跟單頭幾乎一樣。**

**為什麼要多頭**：單一 attention 的 softmax 會讓每個 token 傾向集中在少數位置，
只能捕捉一種關係。多頭讓模型在**不同的子空間**平行學習不同類型的關聯——
實際觀察到有的頭專注語法依存、有的專注相鄰詞、有的專注指代關係。
""",
)

interview(
    "BERT 和 GPT 的差別？",
    """
| | **BERT** | **GPT** |
|---|---|---|
| 架構 | Encoder-only | **Decoder-only** |
| 注意力 | **雙向**（看得到前後文） | **單向**（因果遮罩，只看得到前面） |
| 預訓練任務 | **MLM**：隨機遮住 15% 的字要它猜 | **預測下一個 token** |
| 擅長 | 分類、抽取、搜尋等**理解**任務 | **生成**任務：對話、寫作、寫程式 |
| 怎麼用 | 加一個分類頭後微調 | 直接 prompt，或 few-shot |

**關鍵**：BERT 因為看得到後文，理解任務更強；
但也因為如此，**它沒辦法生成文字**（生成時後文還不存在）。

**為什麼現在都是 Decoder-only**：「預測下一個字」這個任務更通用，
可以把所有任務都轉成文字生成，而且 scaling 效果更好。
""",
)

interview(
    "Self-Attention 的時間和空間複雜度是多少？有什麼問題？",
    """
**複雜度：O(n² · d)**，n 是序列長度、d 是向量維度。

因為 `QKᵀ` 產生一個 **n×n 的矩陣**——每個 token 都要跟所有 token 算關係。

**問題**：序列長度加倍，計算和記憶體變 **4 倍**。
n = 100,000 時，光是注意力矩陣就要 100 億個數字。這是長文本模型的最大瓶頸。

**解法方向**：
- **FlashAttention**：不改變數學，用分塊計算避免把整個 n×n 矩陣存進記憶體
- **稀疏注意力**：只讓每個 token 關注一部分位置（Longformer、BigBird）
- **線性注意力**：改寫成 O(n) 的近似形式（Performer、Linear Attention）
- **狀態空間模型**：Mamba 等新架構，用 O(n) 取代注意力

答得出 FlashAttention 和 O(n²) 的來源，會被認為有跟上進度。
""",
)

next_step("到「🛠️ 實戰練習」，把這 8 章的東西親手跑一次。")
