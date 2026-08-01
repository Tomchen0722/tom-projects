# 台股波段量化研究系統（taistock_swing）

一套**驗證優先**的台股波段（數日～數週）量化研究系統。核心理念不是「做一個會報明牌的
App」，而是「用嚴謹、誠實的方法，檢驗一個交易假設到底有沒有 edge」——先建好誠實的裁判，
再談策略；寧可跑出 FAIL，也不自欺。

> ⚠️ 本專案為個人研究與作品集用途，**非投資建議**。所有回測數字都受限於資料、假設與期間，
> 過去表現不代表未來。對散戶公開薦股在台灣屬特許業務，請勿將本系統輸出對外提供。

---

## 目前的誠實結論

用還原股價（可信數字）在 2022–2024、20～50 檔股票池上，測了兩版策略：

| 策略 | Sharpe | 年化超額 vs 0050 | 判定 |
|---|---|---|---|
| 投信5日買超（20 檔） | 0.41 | -8.42% | FAIL |
| 外資+融資反向複合（50 檔） | 0.25 | -11.50% | FAIL |
| 0050 買進持有 | 0.75 | — | 基準 |

**發現**：籌碼訊號有微弱真實預測力（IC≈0.05，外資 > 投信、融資為反指標），但太薄；
用「只做多、選幾檔輪動」表達，打不過台積電權重約 50% 的 0050——這是**結構問題**，不是選錯訊號。
下一個、也是最後一個能一槌定音的測試是 **long-short 市場中性**，用來把訊號 edge 從基準結構中剝離。

---

## 模組地圖

```
taistock_swing/
├── src/
│   ├── config.py          # 設定中樞：資料集登錄、免費/付費層、欄名對照、成本參數
│   ├── data_source.py     # FinMind 資料層：快取/重試/速率限制/供應商備援 + schema 驗證
│   ├── data_panel.py      # 面板組裝：未還原→還原股價、基準報酬、股票池抓取
│   ├── features_chip.py   # 籌碼特徵：投信/外資買超動能、融資融券情緒（point-in-time）
│   ├── signals.py         # 複合訊號：逐日橫斷面排名，依方向組合多訊號
│   ├── signal_quality.py  # 訊號品質：未來報酬、IC/ICIR、分位數分析
│   ├── strategy_baseline.py # naive 策略：依訊號選前 K、等權、週再平衡
│   └── evaluation.py      # 裁判：成本內建、防未來函數、風險調整指標、及格線判定
├── tests/                 # 6 套合成資料測試（純邏輯，不連網），共 30+ 項
├── scripts/
│   ├── verify_connection.py # 連線與 schema 驗證（設好 token 後第一個跑）
│   ├── run_backtest.py    # 端到端回測 → 印評估報告
│   └── analyze_signal.py  # 訊號品質（IC）分析
├── data/cache/            # FinMind 回應快取（parquet，可安全刪除以重抓）
├── requirements.txt
└── README.md
```

**設計紀律**（貫穿全專案）：
- **防未來函數**：每個特徵標注可得時點；決策日 T 用當晚資料、T+1 執行（裁判的 `exec_lag`）。
- **成本內建**：手續費 0.1425%×折數雙趟 + 賣出證交稅 0.3% + 滑價，直接進報酬，不事後扣。
- **只看風險調整後報酬**：比 Sharpe / 最大回撤，不比裸報酬。
- **還原股價**：免費 TaiwanStockPrice + 除權息結果表自行還原，消除除息假跌。

---

## 安裝與設定

### 1. 相依套件（在你的 conda base 環境）
```bash
conda activate base
pip install -r requirements.txt
```

### 2. 設定 FinMind token（免費帳號即可，600 req/hr）
```bash
conda env config vars set FINMIND_TOKEN=你的token
conda activate base          # 重新 activate 才生效
```

### 3. 設定 UTF-8 輸出（避免繁中 Windows cp950 主控台編碼崩潰）
```bash
conda env config vars set PYTHONUTF8=1
conda activate base
```

驗證兩個環境變數都設好：
```bash
python -c "import os; print('TOKEN', bool(os.environ.get('FINMIND_TOKEN')), 'UTF8', os.environ.get('PYTHONUTF8'))"
```

---

## 如何執行

**一律在專案根目錄 `C:\AI\taistock_swing` 執行。**

### 跑測試（不需 token、不連網）
```bash
python tests\test_evaluation.py
python tests\test_data_source.py
python tests\test_features_chip.py
python tests\test_pipeline.py
python tests\test_signal_quality.py
python tests\test_signals.py
```

### 驗證連線與資料 schema（設好 token 後先跑這個）
```bash
python scripts\verify_connection.py
```
預期：免費資料集綠燈、付費資料集（還原股價/集保）標示跳過。

### 端到端回測（產出策略評估報告）
```bash
python scripts\run_backtest.py
```
首次會抓資料（約一兩分鐘），之後走 `data/cache` 快取秒回。輸出含策略 vs 0050 的
風險調整指標、分年度績效與及格線判定。

### 訊號品質分析（IC）
```bash
python scripts\analyze_signal.py
```
輸出各籌碼訊號 × 持有期的平均 IC 與主訊號的分位數分析。

---

## 資料層須知（FinMind 免費帳號）

- **免費可用**：股價、三大法人買賣、融資融券、除權息結果、交易日曆、股票總覽、下市櫃。
- **付費（贊助）限定，本系統自動跳過**：還原股價（`TaiwanStockPriceAdj`）、
  集保股權分散（`TaiwanStockHoldingSharesPer`）、券商分點（`TaiwanStockTradingDailyReport`）。
- 還原股價因此改由 `price` + `dividend_result` 自行還原（免費）。
- 速率上限 600/hr；資料層有節流與快取，歷史回補可安全重跑。

---

## 已知限制與後續方向

1. **尚未做 long-short 市場中性測試**——這是判斷訊號有無可獲利 edge 的關鍵一步。
2. **集保大戶籌碼集中**訊號因免費層限制未納入（需升級或接 TDCC 免費來源）。
3. **券商分點/主力**（P2）為付費資料，未實作。
4. **備援供應商**只有機制、未接具體 TWSE 來源（目前僅 FinMind 單一來源）。
5. **未做 walk-forward**：目前是單一期間回測，尚未做滾動樣本外驗證。
6. 回測未計入最低手續費 NT$20/筆（報酬率空間近似），小額實測前需補。
