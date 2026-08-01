# 🧠 AI 學習地圖

給完全沒有背景的人看的資料分析 / 機器學習 / 深度學習教學 App，全中文、高中程度、離線可跑。
目標是**轉職求職**：看得懂職缺敘述、答得出面試題、做得出作品集。

---

## 怎麼開始

桌面上有兩個捷徑，雙擊就好：

| 捷徑 | 用途 |
|---|---|
| **🧠 AI 學習地圖** | 教學網頁 App（概念、圖解、互動滑桿） |
| **🛠️ ML 實戰練習** | Jupyter Notebook（動手寫程式） |

也可以直接雙擊資料夾裡的 `啟動教學App.bat` / `啟動實戰練習.bat`。

用指令啟動（網址 http://localhost:8510）：

```bash
python -m streamlit run C:\AI\ml-tutorial\app.py --server.port 8510
```

> 註：兩個 `.bat` 啟動器的畫面文字是英文的。Windows 的 cmd 用 Big5 讀批次檔，
> 而「會」這類中文字的第二個位元組剛好是 `|`，會被誤判成管線符號導致啟動失敗，
> 所以啟動器內容刻意保持純英文。App 和 Notebook 本身全部是中文。

---

## 學習順序

**先看 App 的概念，再跑對應的 Notebook。**

| # | App 章節 | 對應 Notebook |
|---|---|---|
| 1 | 📊 資料分析基礎 | `01_資料分析與評估指標.ipynb` |
| 2 | 🎯 評估指標（Recall / Precision） | 同上 |
| 3 | 🤖 機器學習基礎 | 同上 |
| 4 | ⚖️ 過擬合與模型選擇 | 同上 |
| 5 | 🧠 神經網路是什麼 | `02_手刻神經網路.ipynb` |
| 6 | 🖼️ CNN 卷積神經網路 | `03_CNN影像分類.ipynb` |
| 7 | 🔁 RNN / LSTM | — |
| 8 | ✨ Transformer 與 Attention | `04_Attention手刻實作.ipynb` |
| 9 | 💼 面試題庫 | — |

**總時數估計**：40～60 小時（每天 2 小時，約一個月）。

---

## 專案結構

```
C:\AI\ml-tutorial\
├─ app.py                    主程式（Streamlit 導航）
├─ views/                    每一章的內容
│   ├─ home.py               學習地圖
│   ├─ glossary.py           名詞速查表（80+ 個術語）
│   ├─ data_basics.py        資料分析基礎
│   ├─ metrics.py            評估指標（互動閾值模擬）
│   ├─ ml_basics.py          機器學習基礎
│   ├─ overfitting.py        過擬合與模型選擇
│   ├─ neural_net.py         神經網路（現場訓練 demo）
│   ├─ cnn.py                CNN（互動卷積濾波器）
│   ├─ rnn.py                RNN / LSTM
│   ├─ transformer.py        Transformer / Attention
│   ├─ projects.py           實戰練習說明
│   └─ interview.py          面試題庫
├─ utils/
│   ├─ ui.py                 共用畫面元件與樣式
│   └─ viz.py                圖表工具
├─ notebooks/                四份可執行的實戰 Notebook
├─ requirements.txt
├─ 啟動教學App.bat
└─ 啟動實戰練習.bat
```

---

## 環境

已安裝於 Anaconda（`C:\Users\USER\anaconda3\python.exe`）：

- streamlit 1.58 · numpy 2.2 · pandas 2.2 · plotly 5.22
- matplotlib 3.11 · scikit-learn 1.7 · torch 2.12 (CPU)
- jupyter · notebook 7.2

**全部離線可跑**，不需要網路連線（Notebook 03 的 MNIST 選用練習除外）。

若要在別台電腦重建環境：

```bash
pip install -r requirements.txt
```

---

## 使用建議

1. **每頁的滑桿一定要拖過** — 這是建立直覺最快的方式
2. **「📌 一句話結論」要背起來** — 那是面試時要脫口而出的版本
3. **「❓ 面試題」先自己出聲講一次再看答案** — 直接看答案等於沒學
4. **Notebook 最後的「🎯 動手改改看」不要跳過** — 改壞了才學得到東西
