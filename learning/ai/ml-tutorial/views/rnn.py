import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import heatmap, style

hero(
    "第三站 · 深度學習",
    "🔁 RNN / LSTM 序列模型",
    "有些資料的「順序」就是意義本身。「狗咬人」和「人咬狗」用字一樣，意思差很多。",
)

takeaway(
    "<b>RNN = 邊讀邊做筆記。</b>每讀一個字，就更新手上的筆記本（隱藏狀態 hidden state），"
    "然後帶著筆記去讀下一個字。<br>"
    "問題是筆記本會<b>越寫越模糊</b>（梯度消失），所以發明了 <b>LSTM</b>："
    "多加三道閘門來決定<b>什麼該記、什麼該忘</b>。"
)

# ---------------------------------------------------------------- 序列資料
st.markdown("## 1. 什麼是序列資料")

st.markdown(
    """
只要**順序改變意義就改變**的資料，都是序列資料：

| 類型 | 例子 | 任務 |
|---|---|---|
| **文字** | 「這部電影一點都不好看」 | 情緒分析、翻譯、生成 |
| **時間序列** | 每天的股價、每小時的用電量 | 預測明天 |
| **語音** | 聲波取樣 | 語音辨識 |
| **感測器** | 機台的溫度/震動紀錄 | 預測性維護 |

**關鍵差別**：一般神經網路的輸入是**固定長度**，
但句子有長有短、股價序列可以無限延長。RNN 就是為了處理這個而生的。
"""
)

pitfall(
    "看到「不好看」這三個字，如果模型不管順序（像傳統的詞袋模型 Bag-of-Words），"
    "它只知道句子裡有「不」和「好看」，很可能判成正評。<br>"
    "<b>順序資訊丟掉，語意就毀了。</b>"
)

# ---------------------------------------------------------------- RNN 運作
st.markdown("## 2. RNN 怎麼運作：一個會自己接自己的網路")

analogy(
    "你在讀一本小說。讀到第 50 頁時，你腦中有一個<b>「目前的理解」</b>。<br>"
    "讀第 51 頁時，你會拿「目前的理解」+「第 51 頁的新內容」→ <b>更新成新的理解</b>。<br><br>"
    "那個「目前的理解」就是 <span class='term'>隱藏狀態 h（hidden state）</span>，"
    "它是 RNN 唯一的記憶體。"
)

st.latex(r"h_t = \tanh(W_{hh} \cdot h_{t-1} + W_{xh} \cdot x_t + b)")

st.markdown(
    """
| 符號 | 意思 |
|---|---|
| $x_t$ | 第 t 個時間點的輸入（第 t 個字） |
| $h_{t-1}$ | **上一步的筆記** |
| $h_t$ | **更新後的筆記** |
| $W_{hh}, W_{xh}$ | 權重，**所有時間點共用同一組**（這點很重要） |

**注意**：不管句子有 5 個字還是 500 個字，用的都是**同一組權重**，
只是把同一個運算重複執行 5 次或 500 次。這就是「Recurrent（遞迴）」的意思。
"""
)

st.markdown("### 🎮 看記憶怎麼隨時間更新")

st.markdown("下面模擬一個 4 維的隱藏狀態，讀一個句子時每一步怎麼變化。")

sentence = st.text_input("輸入一個句子（中英文都行）", "這部電影一點都不好看")
tokens = list(sentence.strip())[:14] or ["空"]

decay = st.slider("記憶保留程度（W_hh 的大小）", 0.1, 1.15, 0.75, 0.05,
                  help="太小 → 前面的字很快被忘掉；太大 → 數值爆炸")

rng = np.random.default_rng(0)
H = np.zeros((len(tokens), 4))
h = np.zeros(4)
for i, tok in enumerate(tokens):
    x = rng.normal(0, 1, 4) * 0.9        # 假裝這是這個字的詞向量
    h = np.tanh(decay * h + x)
    H[i] = h

st.plotly_chart(
    heatmap(H.T.round(2), x=tokens, y=[f"記憶格 {i+1}" for i in range(4)],
            text=H.T.round(1), colorscale="RdBu", zmin=-1, zmax=1,
            title="隱藏狀態隨每個字更新（每一直行是讀完該字後的「筆記」）", height=320),
    width="stretch",
)

st.caption(
    "每讀一個字，整本筆記就被改寫一次。讀到最後一個字時的筆記，"
    "就是「整句話的理解」，可以拿去做分類。"
)

# ---------------------------------------------------------------- 梯度消失
st.markdown("## 3. RNN 的致命傷：長距離依賴")

analogy(
    "「我在<b>法國</b>長大，中間搬過很多次家，換過三個工作，"
    "還去了幾個國家旅行……所以我會說一口流利的<b>＿＿</b>」<br><br>"
    "答案是「法文」，但線索在<b>30 個字以前</b>。<br>"
    "RNN 讀到最後時，「法國」那個資訊早就被後面的內容<b>沖淡到看不見了</b>。"
)

st.markdown("### 為什麼會被沖淡：梯度連乘")

st.markdown(
    "反向傳播要從最後一個字往回傳到第一個字，每經過一個時間步就要**乘一次 W_hh**。"
    "連乘 30 次的結果："
)

steps = np.arange(0, 41)
fig = go.Figure()
for wv, label, color in [(0.6, "W = 0.6（梯度消失）", C["bad"]),
                         (0.95, "W = 0.95", C["warn"]),
                         (1.0, "W = 1.0（理想）", C["good"]),
                         (1.1, "W = 1.1（梯度爆炸）", C["primary"])]:
    fig.add_trace(go.Scatter(x=steps, y=np.clip(wv**steps, 1e-10, 1e6), mode="lines",
                             name=label, line=dict(width=3, color=color)))
fig.update_layout(title="梯度往回傳 N 步之後還剩多少", xaxis_title="往回傳的時間步數",
                  yaxis_title="梯度大小（對數刻度）", yaxis_type="log")
st.plotly_chart(style(fig, 380), width="stretch")

st.error(
    "**W = 0.6，往回傳 30 步之後梯度只剩 0.6³⁰ ≈ 0.0000002** —— "
    "等於前面的字對訓練完全沒有影響力。這就是**梯度消失**，"
    "也是 RNN 記不住長距離資訊的根本原因。",
    icon="📉",
)

# ---------------------------------------------------------------- LSTM
st.markdown("## 4. LSTM：加三道閘門解決健忘")

analogy(
    "RNN 的筆記本每一頁都會被<b>整本重寫</b>，所以舊資訊很快消失。<br><br>"
    "LSTM 多帶了一條<b>「主線劇情筆記」</b>（cell state, C），"
    "它<b>基本上原封不動往前傳</b>，只做加法和乘法微調 —— "
    "資訊可以走這條「高速公路」傳很遠不衰減。<br><br>"
    "然後用三道<b>閘門（gate）</b>控制這條高速公路上的交通。每道閘門就是一個 "
    "Sigmoid，輸出 0～1，代表「放行多少比例」。"
)

g1, g2, g3 = st.columns(3)
with g1:
    st.markdown(
        """
#### 🚪 遺忘門 Forget Gate
**「舊記憶要留多少？」**

輸出 0 → 全部忘掉
輸出 1 → 全部保留

例：讀到新的主詞時，可以把舊主詞的性別資訊丟掉。
"""
    )
with g2:
    st.markdown(
        """
#### 🚪 輸入門 Input Gate
**「新資訊要寫入多少？」**

決定這一步看到的新內容，有多少值得記到主線筆記裡。

例：看到「法國」→ 大量寫入。看到「的」→ 幾乎不寫。
"""
    )
with g3:
    st.markdown(
        """
#### 🚪 輸出門 Output Gate
**「這一步要對外說多少？」**

主線筆記裡的東西不一定現在就要用，
輸出門決定這一步要拿出多少來給下一層。
"""
    )

st.latex(r"C_t = \underbrace{f_t \odot C_{t-1}}_{\text{忘掉一部分舊的}} + \underbrace{i_t \odot \tilde{C}_t}_{\text{寫入一部分新的}}")

st.success(
    "**關鍵在那個「＋」號。** 因為是加法而不是連乘，"
    "梯度可以順著 C 這條路徑**幾乎不衰減地傳回去**——"
    "跟 ResNet 的殘差連接是同一個道理。",
    icon="🔑",
)

st.markdown("### LSTM vs GRU vs RNN")

st.markdown(
    """
| | **RNN** | **LSTM** | **GRU** |
|---|---|---|---|
| 閘門數 | 0 | 3（遺忘/輸入/輸出） | **2**（更新/重置） |
| 參數量 | 最少 | 最多 | 中間（約 LSTM 的 3/4） |
| 記憶長度 | 很短（~10 步） | 長 | 長 |
| 訓練速度 | 快 | 慢 | 較快 |
| 什麼時候用 | 幾乎不用了 | 資料多、序列長 | **資料少、要快時的預設選擇** |

**實務建議**：先試 GRU，效果不夠再換 LSTM。兩者差距通常很小。
"""
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 5. PyTorch 寫法")

code(
    """
import torch.nn as nn

class SentimentLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden=256, num_classes=2):
        super().__init__()
        # 把「字的編號」變成「有語意的向量」
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.lstm = nn.LSTM(
            embed_dim, hidden,
            num_layers=2,
            batch_first=True,     # 輸入形狀是 (批次, 序列長度, 特徵) —— 最常忘的參數
            bidirectional=True,   # 雙向：同時從前往後 + 從後往前讀
            dropout=0.3,
        )
        self.fc = nn.Linear(hidden * 2, num_classes)   # 雙向所以 ×2

    def forward(self, x):
        emb = self.embedding(x)                 # (B, L, embed_dim)
        out, (h_n, c_n) = self.lstm(emb)        # out: 每個時間點的輸出
        # 取最後一層的正向 + 反向最終狀態，接起來
        final = torch.cat([h_n[-2], h_n[-1]], dim=1)
        return self.fc(final)
""",
    "情緒分析的標準 LSTM 架構",
)

pitfall(
    "<b>句子長度不一樣怎麼辦？</b>用 <code>pad_sequence</code> 補 0 補到一樣長，"
    "但一定要搭配 <code>pack_padded_sequence</code>，"
    "否則 LSTM 會把那些填充的 0 也當成真的字去讀，結果會變差。<br>"
    "另外記得 <code>nn.Embedding(..., padding_idx=0)</code>，讓填充位置的向量固定為 0。"
)

# ---------------------------------------------------------------- 為什麼被取代
st.markdown("## 6. 為什麼 2017 年之後 RNN 被 Transformer 取代")

st.markdown(
    """
| 問題 | RNN / LSTM | Transformer |
|---|---|---|
| **能不能平行運算** | ❌ 第 t 步必須等第 t−1 步算完 | ✅ **全部時間點同時算** |
| **長距離依賴** | 要走 N 步才能連上 | ✅ **任兩個字距離都是 1 步** |
| **GPU 利用率** | 低（本質是序列運算） | **高**（大矩陣乘法） |
| **訓練 100 億參數的模型** | 幾乎不可能 | ✅ 可行 |

**最致命的是第一點**：RNN 沒辦法平行訓練，
所以在「模型越大越強」的時代，它注定被淘汰。
"""
)

jobnote(
    "現在的職缺已經很少直接用 RNN/LSTM 做 NLP 了。<br>"
    "但<b>時間序列預測</b>（銷量、用電量、設備故障）還是常用 LSTM，"
    "而且面試一定會問<b>「為什麼 Transformer 取代了 RNN」</b>——"
    "因為這題可以同時測出你懂不懂梯度消失、平行運算、和 Attention。<br><br>"
    "<b>所以 RNN 這章要學的重點是：它為什麼不夠好。</b>"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "為什麼 RNN 會有梯度消失？LSTM 怎麼解決？",
    """
**RNN 的問題**：反向傳播要沿著時間往回傳，每一步都乘上 `W_hh` 和 tanh 的導數。
tanh 的導數最大只有 1，而且通常遠小於 1。連乘 N 次之後：

- 乘數 < 1 → 梯度趨近 0（**梯度消失**），前面的時間步學不到東西
- 乘數 > 1 → 梯度爆炸（比較好處理，梯度裁剪就行）

**LSTM 的解法**：加入 **cell state C**，它的更新是

`C_t = f_t ⊙ C_{t−1} + i_t ⊙ C̃_t`

**是加法不是連乘**。梯度沿著 C 往回傳時，主要乘上的是遺忘門 `f_t`，
只要模型學會讓 `f_t ≈ 1`，梯度就能幾乎無損地傳很遠。

**加分句**：這個「加法捷徑」的想法跟 ResNet 的殘差連接本質相同。
""",
)

interview(
    "LSTM 和 GRU 怎麼選？",
    """
| | LSTM | GRU |
|---|---|---|
| 閘門 | 3 個 + 獨立的 cell state | 2 個，把 cell state 和 hidden state 合併 |
| 參數 | 多約 33% | 少，訓練快 |
| 表現 | 資料多、序列很長時略勝 | 資料少時通常一樣好甚至更好 |

**實務**：**先試 GRU**（快、參數少、不容易過擬合），
資料量很大且序列很長再考慮 LSTM。多數論文的結論是兩者差距在誤差範圍內。
""",
)

interview(
    "雙向 RNN（BiLSTM）什麼時候能用，什麼時候不能用？",
    """
**能用**：**整個序列已經完整拿到**的任務。
例如情緒分析、命名實體辨識、機器翻譯的編碼器——
這時候看後文能大幅幫助理解（「他去了銀行**釣魚**」才知道銀行是河岸）。

**不能用**：**即時預測未來**的任務。
例如語音即時轉文字、股價預測、文字生成——
因為「後面的資料」在預測當下**根本還不存在**。

硬要用就是**資料洩漏**，離線分數超高、上線爆炸。這題是很好的鑑別題。
""",
)

interview(
    "Transformer 為什麼取代了 RNN？",
    """
**三個理由，按重要性排**：

1. **可以平行運算**（最關鍵）
   RNN 第 t 步必須等第 t−1 步算完，GPU 的平行能力完全用不上。
   Transformer 的 self-attention 是一次大矩陣乘法，整個序列同時算完。
   這讓「訓練超大模型」從不可能變成可能。

2. **長距離依賴變成常數距離**
   RNN 中兩個相隔 100 步的字，資訊要傳 100 次；
   Transformer 中**任兩個位置的路徑長度都是 1**（直接互相 attend）。

3. **可解釋性**
   Attention 權重可以畫成熱圖，看得出模型在關注哪個字。

**Transformer 的代價**：
self-attention 的複雜度是 **O(n²)**（每個字都要跟所有字算關係），
序列很長時記憶體會爆——這是目前長文本模型的主要研究方向
（FlashAttention、稀疏注意力等）。
""",
)

next_step("到「✨ Transformer 與 Attention」—— 這是 ChatGPT 的底層，也是現在最重要的一章。")
