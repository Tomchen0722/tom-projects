import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.ui import analogy, code, hero, interview, jobnote, next_step, pitfall, takeaway
from utils.viz import heatmap, style

hero(
    "第一站 · 資料",
    "📊 資料分析基礎",
    "模型再厲害，餵爛資料出來就是爛結果。這一章是所有 AI 工作的地基。",
)

takeaway(
    "資料分析在做四件事：<b>（1）把資料整理乾淨 →（2）看它長什麼樣 →"
    "（3）找出欄位之間的關係 →（4）做出對模型有用的新欄位</b>。"
    "業界說的「80% 時間在整理資料」，指的就是這一章。"
)

# ---------------------------------------------------------------- 資料長什麼樣
st.markdown("## 1. 資料在電腦裡長什麼樣：DataFrame")

analogy(
    "就是一張 Excel 表。<b>每一列（row）= 一個對象</b>（一個學生、一筆訂單、一位病人），"
    "<b>每一欄（column）= 一個特徵</b>（身高、金額、年齡）。"
    "Python 裡處理這種表的工具叫 <span class='term'>Pandas</span>，"
    "表本身叫 <span class='term'>DataFrame</span>。"
)


@st.cache_data
def make_students(n=200, seed=42):
    """做一份假的學生資料，方便示範。"""
    rng = np.random.default_rng(seed)
    study = rng.normal(5, 2, n).clip(0.5, 12)          # 每天讀書小時
    sleep = rng.normal(7, 1.2, n).clip(3, 11)          # 每天睡眠小時
    phone = rng.normal(4, 1.8, n).clip(0, 10)          # 每天滑手機小時
    # 分數 = 讀書有正面影響、滑手機有負面影響、睡眠適中最好，再加一點雜訊
    score = (
        42 + 6.0 * study - 3.2 * phone - 0.9 * (sleep - 7.5) ** 2 + rng.normal(0, 5, n)
    ).clip(0, 100)
    return pd.DataFrame(
        {
            "每日讀書時數": study.round(1),
            "每日睡眠時數": sleep.round(1),
            "每日滑手機時數": phone.round(1),
            "期末分數": score.round(1),
        }
    )


df = make_students()

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("**這是我們的範例資料（200 位學生）**")
    st.dataframe(df.head(8), width="stretch")
with c2:
    code(
        """
import pandas as pd

df = pd.read_csv("students.csv")  # 讀檔
df.head()      # 看前 5 列
df.shape       # (幾列, 幾欄)
df.info()      # 每欄的型別、有沒有缺值
df.describe()  # 每欄的統計摘要
""",
        "最常用的 5 行，任何專案第一步都是這些",
    )

# ---------------------------------------------------------------- 統計三兄弟
st.markdown("## 2. 描述一堆數字：平均數、中位數、標準差")

st.markdown(
    "拿到 200 個分數，你不可能一個一個看。統計就是把 200 個數字**壓縮成 2～3 個數字**。"
)

col = st.selectbox("選一個欄位來看", df.columns, index=3)
vals = df[col]

m1, m2, m3, m4 = st.columns(4)
m1.metric("平均數 mean", f"{vals.mean():.1f}", help="全部加起來除以個數。會被極端值拉走。")
m2.metric("中位數 median", f"{vals.median():.1f}", help="排序後正中間那個。不怕極端值。")
m3.metric("標準差 std", f"{vals.std():.1f}", help="平均而言，每個數字離平均多遠。越大越分散。")
m4.metric("全距 range", f"{vals.min():.1f} ~ {vals.max():.1f}")

fig = go.Figure(go.Histogram(x=vals, nbinsx=30, marker_line_width=0))
fig.add_vline(x=vals.mean(), line_dash="dash", line_color="#dc2626",
              annotation_text="平均數", annotation_position="top")
fig.add_vline(x=vals.median(), line_dash="dot", line_color="#16a34a",
              annotation_text="中位數", annotation_position="bottom")
fig.update_layout(title=f"{col} 的分布", xaxis_title=col, yaxis_title="人數")
st.plotly_chart(style(fig, 340), width="stretch")

pitfall(
    "<b>平均數會騙人。</b>10 個人，9 個月薪 3 萬、1 個月薪 300 萬 → 平均月薪 32.7 萬。<br>"
    "只要資料有極端值（outlier）或分布歪斜，就要看<b>中位數</b>。"
    "面試問「平均數跟中位數差很多代表什麼」，答案是：<b>資料歪斜，有極端值</b>。"
)

# ---------------------------------------------------------------- 相關係數
st.markdown("## 3. 兩個欄位有沒有關係：相關係數")

analogy(
    "相關係數（correlation）是一個 <b>-1 到 +1</b> 之間的數字：<br>"
    "・<b>+1</b>：一個變大，另一個也一定變大（讀書時數 ↔ 分數）<br>"
    "・<b>0</b>：完全沒關係（鞋子尺寸 ↔ 分數）<br>"
    "・<b>-1</b>：一個變大，另一個一定變小（滑手機時數 ↔ 分數）"
)

corr = df.corr().round(2)
fig = heatmap(
    corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    text=corr.values,
    colorscale="RdBu",
    zmin=-1,
    zmax=1,
    title="相關係數矩陣（越紅越正相關，越藍越負相關）",
    height=420,
)
st.plotly_chart(fig, width="stretch")

xcol = st.selectbox("X 軸", df.columns[:3], index=0, key="scx")
fig = go.Figure(
    go.Scatter(x=df[xcol], y=df["期末分數"], mode="markers",
               marker=dict(size=7, opacity=0.6))
)
r = df[xcol].corr(df["期末分數"])
fig.update_layout(title=f"{xcol} vs 期末分數　（相關係數 r = {r:.2f}）",
                  xaxis_title=xcol, yaxis_title="期末分數")
st.plotly_chart(style(fig, 360), width="stretch")

pitfall(
    "<b>相關 ≠ 因果。</b>這是面試最愛考的一題。<br>"
    "冰淇淋銷量和溺水人數高度正相關 —— 但吃冰淇淋不會害人溺水，"
    "真正的原因是<b>「夏天」</b>同時推高了兩者。這個躲在背後的第三者叫"
    "<span class='term'>干擾變數（confounder）</span>。"
)

# ---------------------------------------------------------------- 缺值
st.markdown("## 4. 資料清理：缺值、重複、異常值")

st.markdown(
    """
真實資料一定是髒的。三個必修動作：

| 問題 | 怎麼發現 | 怎麼處理 |
|---|---|---|
| **缺值 (missing)** | `df.isna().sum()` | 補平均/中位數、補前一筆、或整列刪掉 |
| **重複 (duplicate)** | `df.duplicated().sum()` | `df.drop_duplicates()` |
| **異常值 (outlier)** | 畫箱型圖、看 `describe()` | 確認是打錯字還是真的極端值，再決定砍或留 |
"""
)

code(
    """
# 看每一欄缺幾筆
df.isna().sum()

# 用中位數補（數值欄常用，因為不怕極端值）
df["年齡"] = df["年齡"].fillna(df["年齡"].median())

# 用出現最多的類別補（類別欄）
df["城市"] = df["城市"].fillna(df["城市"].mode()[0])

# 刪掉重複列
df = df.drop_duplicates()
""",
    "清資料的標準三招",
)

pitfall(
    "缺值<b>不要無腦補 0</b>。「年收入 = 0」和「年收入未填」意義完全不同，"
    "補 0 會把模型帶歪。而且有時候「這格是空的」本身就是重要訊號 —— "
    "進階做法是多開一欄 <code>年收入_是否缺值</code> 記錄它。"
)

# ---------------------------------------------------------------- 特徵工程
st.markdown("## 5. 特徵工程：幫模型把題目變簡單")

analogy(
    "模型只看得懂數字，而且<b>很笨</b>。你給它「出生日期 1990-03-15」它學不到東西；"
    "但你算成「年齡 36」它就懂了。<b>把原始欄位加工成模型好懂的形式，就叫特徵工程。</b><br>"
    "這是資料科學家最值錢的技能 —— 同一份資料，特徵做得好，爛模型也贏過別人的好模型。"
)

st.markdown(
    """
四種最常用的加工：

**① 類別轉數字（One-Hot Encoding）**
`城市 = 台北/台中/高雄` → 拆成三欄 `是台北(0/1)`、`是台中(0/1)`、`是高雄(0/1)`

**② 數值縮放（Standardization）**
`年收入(百萬級)` 和 `年齡(兩位數)` 放在一起，模型會誤以為年收入比較重要。
統一縮放到「平均 0、標準差 1」就公平了。

**③ 拆解時間**
`2026-07-24 14:30` → `月份`、`星期幾`、`是否假日`、`小時`

**④ 造組合欄位**
`總價` 和 `坪數` → 多造一欄 `每坪單價`（這欄往往比原本兩欄都有用）
"""
)

code(
    """
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ② 數值縮放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # 訓練資料：學統計量 + 轉換
X_test_scaled  = scaler.transform(X_test)        # 測試資料：只轉換，不能重學！

# ① 類別轉數字
df = pd.get_dummies(df, columns=["城市"], drop_first=True)

# ③ 拆時間
df["星期幾"] = pd.to_datetime(df["下單時間"]).dt.dayofweek

# ④ 造新欄位
df["每坪單價"] = df["總價"] / df["坪數"]
""",
    "注意第 6 行：測試資料只能用 transform，不能用 fit_transform",
)

pitfall(
    "<b>資料洩漏（Data Leakage）</b>：在測試資料上呼叫 <code>fit_transform</code>，"
    "等於讓模型偷看了考題答案。訓練時分數超高，上線後爆炸。<br>"
    "這是面試官很愛用來篩人的題目，記牢：<b>fit 只在訓練集做</b>。"
)

jobnote(
    "職缺敘述上的「熟悉 Pandas / SQL / 資料清理」就是這一章。"
    "面試常見的實作題：<b>「給你一份髒的 CSV，30 分鐘內做出可以餵進模型的資料」</b>。"
    "他們考的不是你會不會寫模型，是你會不會處理現實世界的爛資料。"
)

# ---------------------------------------------------------------- 面試題
st.markdown("## 面試題")

interview(
    "平均數和中位數差很多，代表什麼？你會選哪一個？",
    """
代表**資料分布歪斜（skewed），有極端值**。

- 平均數 > 中位數 → 右偏（少數超大值，例如收入、房價）
- 平均數 < 中位數 → 左偏

**選擇**：報告給老闆看時用**中位數**（比較能代表「典型的那個人」）；
但如果要算總量（例如總營收 = 平均 × 人數），還是要用平均數。
""",
)

interview(
    "相關係數 0.9 代表 A 造成 B 嗎？",
    """
**不代表。相關 ≠ 因果。**

要證明因果需要：
1. **時間順序**：A 一定發生在 B 之前
2. **排除干擾變數**：控制住其他可能的原因
3. **隨機對照實驗（A/B test）**：把人隨機分兩組，只有一組做 A

補充一個加分答法：相關係數只抓得到**線性關係**。
y = x² 這種資料，相關係數可能接近 0，但兩者關係其實非常強。
""",
)

interview(
    "缺值怎麼處理？",
    """
**先問「為什麼會缺」，再決定怎麼補。** 分三種：

1. **完全隨機缺（MCAR）** — 系統當機導致的漏記 → 直接補中位數/平均數，或刪掉
2. **有條件的隨機缺（MAR）** — 例如年輕人比較少填收入 → 用其他欄位預測補值
3. **不隨機缺（MNAR）** — 高收入的人故意不填 → **缺值本身就是訊號**，
   要多開一個 `是否缺值` 的旗標欄位

實務上最安全的做法：**中位數補值 + 加一欄缺值旗標**，讓模型自己決定要不要用。
""",
)

interview(
    "什麼是資料洩漏（Data Leakage）？舉一個例子。",
    """
**訓練時用到了「上線時拿不到」或「來自未來」的資訊**，導致驗證分數虛高。

三個經典例子：
1. 在整份資料上做 `StandardScaler().fit_transform()`，才切訓練/測試 → 測試集的統計量洩漏進訓練
2. 預測「顧客會不會退訂」，特徵裡放了 `退訂原因` → 這欄要退訂後才存在
3. 時間序列資料用隨機切分 → 拿未來預測過去

**怎麼防**：先切訓練/測試，再做所有前處理；並且問自己
「**預測當下，這個欄位真的拿得到嗎？**」
""",
)

next_step("到「🎯 評估指標」，學怎麼判斷一個模型到底做得好不好 —— 那頁會解釋你點名要學的 Recall。")
