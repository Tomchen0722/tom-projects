import numpy as np
import plotly.graph_objects as go
import streamlit as st

from utils.ui import C, analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import heatmap, image_grid, style

hero(
    "第三站 · 深度學習",
    "🖼️ CNN 卷積神經網路",
    "電腦怎麼「看」圖片？答案是：拿一片小小的放大鏡，在整張圖上滑過去找特徵。",
)

takeaway(
    "<b>卷積（Convolution）= 拿一個小方格（濾波器）在整張圖上滑動，"
    "每滑到一處就做一次加權相加。</b><br>"
    "同一個濾波器<b>整張圖共用</b>，所以參數少很多，而且「貓在左上角」和「貓在右下角」都認得出來。"
)

# ---------------------------------------------------------------- 為什麼
st.markdown("## 1. 為什麼圖片不能直接丟進一般神經網路")

analogy(
    "一張 <b>1000×1000</b> 的彩色照片攤平後有 <b>300 萬個數字</b>。<br>"
    "如果第一層就接 1000 顆神經元的全連接層 → <b>需要 30 億個權重</b>。<br><br>"
    "而且更糟的是：把圖攤平會<b>破壞空間關係</b> —— "
    "原本上下相鄰的兩個像素，攤平後距離變成 1000，模型完全不知道它們是鄰居。"
)

st.markdown(
    """
CNN 用三個設計解決這件事：

| 設計 | 白話 | 好處 |
|---|---|---|
| **局部連接** | 每顆神經元只看一小塊（例如 3×3） | 參數暴減，而且保留了「鄰居關係」 |
| **權重共享** | 同一個濾波器在整張圖重複使用 | 參數再減一個數量級 |
| **平移不變性** | 貓在哪個位置都能被同一個濾波器抓到 | 不用每個位置各學一次 |
"""
)

# ---------------------------------------------------------------- 卷積互動
st.markdown("## 2. 動手玩：卷積到底在算什麼")


@st.cache_data
def get_image(size=110):
    """優先用 matplotlib 內建照片，拿不到就生成一張合成圖（保證離線可用）。"""
    try:
        import matplotlib.cbook as cbook
        import matplotlib.image as mpimg

        with cbook.get_sample_data("grace_hopper.jpg") as f:
            img = mpimg.imread(f)
        g = img[..., :3].mean(-1).astype(float)
        g = g[:: max(1, g.shape[0] // size), :: max(1, g.shape[1] // size)]
        return (g - g.min()) / (np.ptp(g) + 1e-9)
    except Exception:
        yy, xx = np.mgrid[0:size, 0:size]
        img = np.zeros((size, size))
        img[(xx - 35) ** 2 + (yy - 35) ** 2 < 22**2] = 0.85          # 圓
        img[60:95, 55:95] = 0.45                                      # 方塊
        img += 0.25 * np.sin(xx / 3.0)                                # 條紋
        return (img - img.min()) / (np.ptp(img) + 1e-9)


KERNELS = {
    "邊緣偵測（Sobel 垂直）": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float),
    "邊緣偵測（Sobel 水平）": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], float),
    "全方向邊緣（Laplacian）": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], float),
    "模糊（Box Blur）": np.ones((3, 3)) / 9,
    "銳化（Sharpen）": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], float),
    "浮雕（Emboss）": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], float),
}


def conv2d(img, k):
    """最樸素的卷積實作 —— 就是雙層迴圈滑窗，然後對應位置相乘再相加。"""
    kh, kw = k.shape
    ph, pw = kh // 2, kw // 2
    padded = np.pad(img, ((ph, ph), (pw, pw)), mode="edge")
    out = np.zeros_like(img, dtype=float)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.sum(padded[i:i + kh, j:j + kw] * k)
    return out


img = get_image()
kname = st.selectbox("選一個濾波器（卷積核 kernel）", list(KERNELS), index=0)
k = KERNELS[kname]

c1, c2, c3 = st.columns([2, 3, 3])
with c1:
    st.markdown("**這個 3×3 濾波器**")
    st.plotly_chart(
        heatmap(k, text=k.astype(int), colorscale="RdBu", height=250, zmin=-5, zmax=5),
        width="stretch",
    )
    st.caption("這 9 個數字在 CNN 裡**不是人設定的，是訓練出來的**。")
with c2:
    st.markdown("**原圖**")
    st.pyplot(image_grid([img], [""], cols=1), width="stretch")
with c3:
    st.markdown(f"**卷積後（{kname}）**")
    st.pyplot(image_grid([conv2d(img, k)], [""], cols=1), width="stretch")

st.success(
    "**看出來了嗎**：邊緣偵測的濾波器把輪廓抓出來、模糊的把細節抹掉。"
    "CNN 的第一層學到的濾波器，長得就跟這些非常像 —— **不是人寫的，是它自己學會的**。",
    icon="🔍",
)

st.markdown("### 一次卷積的算式長這樣")

demo_patch = np.array([[10, 10, 10], [10, 90, 10], [10, 10, 10]], float)
demo_k = KERNELS["銳化（Sharpen）"]
d1, d2, d3 = st.columns(3)
with d1:
    st.plotly_chart(heatmap(demo_patch, text=demo_patch.astype(int),
                            title="圖片上的一小塊 3×3", height=260), width="stretch")
with d2:
    st.plotly_chart(heatmap(demo_k, text=demo_k.astype(int), colorscale="RdBu",
                            title="濾波器", height=260, zmin=-5, zmax=5),
                    width="stretch")
with d3:
    st.markdown("#### 對應位置相乘再全部加起來")
    st.latex(r"\sum (\text{patch} \times \text{kernel})")
    st.markdown(
        f"= 10×0 + 10×(−1) + 10×0<br>"
        f"+ 10×(−1) + 90×5 + 10×(−1)<br>"
        f"+ 10×0 + 10×(−1) + 10×0<br><br>"
        f"= **{np.sum(demo_patch * demo_k):.0f}**",
        unsafe_allow_html=True,
    )
    st.caption("這個數字就是輸出圖上的一個像素。滑完整張圖，就得到一張新的「特徵圖」。")

# ---------------------------------------------------------------- 池化
st.markdown("## 3. 池化 Pooling：把圖縮小，只留重點")

analogy(
    "把 2×2 的四個像素，<b>只留最大的那一個</b>（Max Pooling）。<br><br>"
    "為什麼可以這樣做？因為卷積的輸出代表「這裡有多像某個特徵」，"
    "我們只關心<b>「這一區有沒有出現這個特徵」</b>，不在乎它在這一區的哪個像素。<br><br>"
    "好處：圖變小 → 計算變快、參數變少 → 順便獲得一點<b>位移容忍度</b>。"
)

small = img[:8, :8]
pooled = small.reshape(4, 2, 4, 2).max(axis=(1, 3))
pp1, pp2 = st.columns(2)
with pp1:
    st.plotly_chart(heatmap(small.round(2), title="池化前 8×8", height=330),
                    width="stretch")
with pp2:
    st.plotly_chart(heatmap(pooled.round(2), title="Max Pooling 2×2 之後 → 4×4", height=330),
                    width="stretch")

st.caption("每個 2×2 的方塊只留下最大值，尺寸直接砍半（面積剩 1/4）。")

# ---------------------------------------------------------------- 整體架構
st.markdown("## 4. 一個完整 CNN 的長相")

st.markdown(
    """
```
輸入圖片 (224×224×3)
   ↓  Conv 3×3 + ReLU     ← 學「邊緣、顏色塊」等低階特徵
   ↓  Conv 3×3 + ReLU
   ↓  MaxPool 2×2         ← 尺寸砍半 (112×112)
   ↓  Conv 3×3 + ReLU     ← 學「眼睛、輪子、紋理」等中階特徵
   ↓  MaxPool 2×2         ← (56×56)
   ↓  Conv 3×3 + ReLU     ← 學「臉、車頭」等高階特徵
   ↓  MaxPool 2×2         ← (28×28)
   ↓  Flatten             ← 攤平成一長條
   ↓  Linear + ReLU       ← 全連接層，開始做決策
   ↓  Linear → Softmax    ← 輸出每個類別的機率
輸出：貓 92%、狗 5%、其他 3%
```

**規律**：越往深層，**空間尺寸越小、通道數越多**（特徵越抽象）。
"""
)

st.markdown("### 三個一定會被問的參數")

pc1, pc2, pc3 = st.columns(3)
with pc1:
    st.markdown(
        "#### Kernel Size\n"
        "濾波器多大，通常 **3×3**。\n\n"
        "為什麼不用 7×7？因為**兩層 3×3 的視野等於一層 5×5，但參數更少、非線性更多**。"
    )
with pc2:
    st.markdown(
        "#### Stride（步幅）\n"
        "每次滑動幾格，預設 **1**。\n\n"
        "設 2 就等於順便做了一次降採樣，輸出尺寸砍半。"
    )
with pc3:
    st.markdown(
        "#### Padding（填充）\n"
        "在圖片外圍補一圈 0。\n\n"
        "`padding='same'` 讓輸出尺寸和輸入一樣，**避免邊緣資訊一直流失**。"
    )

st.latex(r"\text{輸出邊長} = \left\lfloor \frac{\text{輸入} + 2 \times \text{padding} - \text{kernel}}{\text{stride}} \right\rfloor + 1")
st.caption("這條公式面試會叫你算。例：輸入 32、kernel 3、padding 1、stride 1 → 輸出 32（尺寸不變）。")

# ---------------------------------------------------------------- 參數比較
st.markdown("## 5. CNN 到底省了多少參數")

sz = st.select_slider("圖片尺寸", [28, 64, 128, 224], value=128)
fc_params = (sz * sz * 3) * 64
conv_params = 3 * 3 * 3 * 64

cc1, cc2, cc3 = st.columns(3)
cc1.metric("全連接層（64 顆神經元）", f"{fc_params:,}")
cc2.metric("卷積層（64 個 3×3 濾波器）", f"{conv_params:,}")
cc3.metric("省下", f"{fc_params / conv_params:,.0f} 倍")

fig = go.Figure(go.Bar(x=["全連接層", "卷積層"], y=[fc_params, conv_params],
                       marker_color=[C["bad"], C["good"]],
                       text=[f"{fc_params:,}", f"{conv_params:,}"], textposition="outside"))
fig.update_layout(title=f"{sz}×{sz} 彩色圖片，第一層的參數量比較", yaxis_type="log",
                  yaxis_title="參數數量（對數刻度）")
st.plotly_chart(style(fig, 340), width="stretch")

st.info(
    "**注意卷積層的參數量跟圖片大小完全無關** —— 因為同一個濾波器整張圖共用。"
    "這就是「權重共享」的威力。",
    icon="⚡",
)

# ---------------------------------------------------------------- 程式碼
st.markdown("## 6. PyTorch 寫一個 CNN")

code(
    """
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            # 輸入 1 通道（灰階），輸出 32 張特徵圖
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),        # 穩定訓練，讓學習率可以開大一點
            nn.ReLU(),
            nn.MaxPool2d(2),           # 28×28 → 14×14

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),           # 14×14 → 7×7
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.3),           # 防過擬合
            nn.Linear(64 * 7 * 7, 128), nn.ReLU(),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)
""",
    "Conv → BatchNorm → ReLU → Pool，這個順序是業界標準組合",
)

pitfall(
    "<b>不要從零開始訓練 CNN。</b>除非你有幾十萬張標註好的圖。<br>"
    "正確做法是 <span class='term'>遷移學習（Transfer Learning）</span>："
    "拿別人在 ImageNet（120 萬張圖）上訓練好的 ResNet，"
    "<b>只換掉最後一層</b>，用你自己的幾百張圖微調。<br>"
    "效果通常好非常多，而且幾分鐘就訓練完。"
)

code(
    """
import torchvision.models as models
import torch.nn as nn

# 載入預訓練好的 ResNet18
model = models.resnet18(weights="IMAGENET1K_V1")

# 凍結所有既有權重（不讓它們被更新）
for p in model.parameters():
    p.requires_grad = False

# 只換掉最後那層分類器，改成你自己的類別數
model.fc = nn.Linear(model.fc.in_features, num_classes)

# 現在只有 model.fc 會被訓練 —— 幾百張圖、幾分鐘就搞定
""",
    "遷移學習：轉職作品集最實用的一招",
)

jobnote(
    "電腦視覺職缺面試流程通常是：<br>"
    "① 解釋卷積在算什麼（會叫你手算一次）<br>"
    "② 算輸出尺寸和參數量（用上面那條公式）<br>"
    "③ 說明為什麼用 CNN 不用 MLP<br>"
    "④ 遷移學習怎麼做、什麼時候要解凍多少層<br><br>"
    "作品集建議：<b>用遷移學習做一個「自己蒐集的資料集」分類器</b>"
    "（例如分辨自家產品的瑕疵），比跑一次 MNIST 有說服力太多。"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "為什麼影像要用 CNN，不用一般的全連接網路？",
    """
三個理由：

1. **參數量**：224×224×3 的圖接一層 1000 顆神經元的全連接層要 1.5 億個參數，
   卷積層只要幾千個（因為權重共享，且參數量與圖片大小無關）。
2. **保留空間結構**：攤平會破壞「像素之間的鄰近關係」，卷積是在 2D 上滑窗，天生保留。
3. **平移不變性**：貓出現在左上角或右下角，同一個濾波器都抓得到。
   全連接網路得為每個位置各學一套權重。

**加分句**：CNN 的假設是「局部相關 + 平移不變」，
所以它也適合**一維訊號**（心電圖、音訊）和**文字**（TextCNN 抓 n-gram）。
""",
)

interview(
    "解釋 stride、padding、kernel size 對輸出尺寸的影響。",
    """
公式：

$$\\text{輸出} = \\left\\lfloor \\frac{\\text{輸入} + 2p - k}{s} \\right\\rfloor + 1$$

- **kernel size k↑** → 輸出變小，視野變大，參數變多
- **stride s↑** → 輸出**大幅**變小（s=2 大約砍半），等於順便降採樣
- **padding p↑** → 輸出變大，保住邊緣資訊

**常考的具體題**：輸入 32×32，k=3, s=1, p=1 → 輸出 (32+2−3)/1+1 = **32**，尺寸不變。
所以「3×3 + padding 1」是最常見的組合，因為它讓尺寸維持不變，方便疊很多層。
""",
)

interview(
    "Max Pooling 和 Average Pooling 差在哪？現在還用 Pooling 嗎？",
    """
- **Max Pooling**：取最大值。保留「最強的特徵反應」，對紋理、邊緣這種要判斷「有沒有」的任務較好。**最常用**。
- **Average Pooling**：取平均。保留整體強度，比較平滑。

**現在的趨勢**：
1. 很多現代架構（ResNet 之後）改用 **stride=2 的卷積**取代 pooling——
   因為降採樣的方式也可以「學」，比固定取最大值有彈性。
2. 網路最後改用 **Global Average Pooling**（整張特徵圖平均成一個數字）
   取代 Flatten + 大的全連接層，**參數大幅減少且不容易過擬合**。
""",
)

interview(
    "什麼是感受野（Receptive Field）？為什麼要疊很多層 3×3 而不是用一層 7×7？",
    """
**感受野**：輸出上的一個像素，「看得到」原始輸入圖上多大的範圍。

疊層會讓感受野擴大：
- 一層 3×3 → 感受野 3×3
- 兩層 3×3 → 感受野 **5×5**
- 三層 3×3 → 感受野 **7×7**

**三層 3×3 vs 一層 7×7**（同樣的感受野，假設 C 個通道）：

| | 參數量 | 非線性 |
|---|---|---|
| 一層 7×7 | 49C² | 1 次 ReLU |
| 三層 3×3 | 3×9C² = **27C²** | **3 次 ReLU** |

**參數少 45%，非線性多 3 倍** ——所以 VGG 之後大家都改用小卷積核疊深。
""",
)

next_step("到「🔁 RNN / LSTM」，看模型怎麼處理有先後順序的資料。")
