# ISO 27001:2022 資訊安全完全指南 & LA 主導稽核員實戰平台

> **從零開始到取得 ISO 27001:2022 認證與 CQI/IRCA 主導稽核員（Lead Auditor）實務攻略**  
> 專為半導體測試機台工控防護（Teradyne Eagle 364 / SEMI E187）與關鍵基礎設施機房電力維運（中華電信信義數據一大樓電力室一級保養）打造的實戰導向學習系統。

---

## 📌 專案簡介

本專案收錄完整 ISO/IEC 27001:2022 資訊安全管理系統（ISMS）教材，從基礎概念、管理條文（Clause 4~10）、Annex A 93 項控制措施，延伸至企業導入、內部稽核，以及全新升級的 **模組六：ISO 27001 LA 主導稽核員與實戰特訓**。

內建 94 題互動測驗系統（`quiz.html`），支援主題練習、錯題複習與計時模擬考。

---

## 📚 系統架構與單元目錄

```
learning/iso27001/
├── index.html                           # 學習首頁 / 學習路徑導引 Hub
├── quiz.html                            # 94 題互動測驗系統（依 2022 版最新架構）
├── 01-basics/                           # 模組一：資安基礎與核心概念
│   ├── cia-triad.html                   # CIA 三要素與資安基本觀念
│   ├── defense-in-depth.html            # 縱深防禦架構
│   ├── security-policies.html           # 資安政策擬定指南
│   └── threat-landscape.html            # 現代資安威脅地圖
├── 02-isms/                             # 模組二：ISMS 架構與 93 項控制措施
│   ├── organizational-controls.html     # A.5 組織控制措施（37 項）
│   ├── people-controls.html             # A.6 人員控制措施（8 項）
│   ├── physical-controls.html           # A.7 實體控制措施（14 項）
│   └── technological-controls.html      # A.8 技術控制措施（34 項）
├── 03-risk/                             # 模組三：風險評估與 SOA 適用性聲明
│   ├── asset-inventory.html             # 資產盤點與價值評估
│   ├── risk-assessment.html             # 風險鑑別、分析與評量
│   ├── risk-treatment.html              # 風險處理四策略（緩解/轉移/規避/承受）
│   └── soa-development.html             # SOA 適用性聲明書撰寫實務
├── 04-enterprise/                       # 模組四：企業導入與維運藍圖
│   ├── implementation-steps.html        # 企業導入 10 步驟
│   ├── timeline-budget.html             # 12 個月導入時程表與預算編列
│   ├── management-review.html           # 管理審查會議規劃與執行
│   └── continuous-improvement.html      # 持續改善與 PDCA 循環
├── 05-auditor/                          # 模組五：稽核員養成與案例演練
│   ├── certification-intro.html         # 認證標準體系與 IAF/TAF 架構
│   ├── audit-practice.html              # 稽核三階段實務（查核表/取證/NCR）
│   ├── case-studies.html                # 經典稽核案例判定（D~H）
│   └── audit-scenarios.html             # 稽核情境進階實戰（I~P）
└── 06-la-audit/                         # 模組六：ISO 27001 LA 主導稽核員與實戰特訓（新增）
    ├── la-roadmap.html                  # CQI/IRCA 考證攻略、12週自學進度規劃、YouTube自學影音、中華電信招考策略
    ├── ti-semi-eagle364.html            # 半導體測試機台資安：Teradyne Eagle 364 工控弱點 vs SEMI E187 晶圓測試防護 vs TI 經驗
    ├── cht-power-datacenter.html        # 關鍵基礎設施實體安全：國廷電機駐點中華電信數據一大樓電力室一級保養實戰（A.7.11/A.5.30）
    └── clause-comparison-2022.html      # 2022 最新版核心條文（Clause 4~10）深度解析、11項新增控制項與 Major/Minor/OFI 判定
```

---

## 🎯 模組六亮點特色

### 1. CQI/IRCA 考證攻略 & 12 週（每週 6 小時）自學進度表
- **考試架構剖析**：Section 1（條文概念客觀題，40分）、Section 2（簡答與情境分析，20分）、Section 3（三方稽核實務題，40分）、Section 4（情境 NCR 撰寫與稽核發現，40分），總分 140 分（70% / 98 分及格）。
- **每週 6 小時自學配比**：
  - 週二晚間 1.5h：核心條文與 Annex A 條文研讀
  - 週四晚間 1.5h：YouTube 精選影片觀看與筆記整理
  - 週六/週日 3.0h：情境題實戰演練、NCR 撰寫與查核表實作
- **12 週三階段規劃**：
  - 第 1~4 週：基礎築底（Clause 4~10、Annex A 93 控制項）
  - 第 5~8 週：實務深耕（SEMI E187 機台工控、數據中心電力機電、A.7.11、A.5.30）
  - 第 9~12 週：衝刺實戰（CQI/IRCA 模擬題、NCR 專題、中華電信招考面試準備）

### 2. 精選 YouTube 影音自學對應
1. **《白話ISO 27001:2022》點子創意**：條文白話拆解、PDCA 管理循環
2. **《SEMI E187 半導體設備資安標準介紹》**：OS 作業系統安全、網路微隔離、端點安全、資安監控
3. **《ISO 27001 主導稽核員 上課日常與考試心得》**：5 天 40 小時密集班生存指南、情境題破題技巧
4. **《ISO 27001 條文解析》&《ISO 27001:2022 條文繁體中文版》**：Clause 4~10 關鍵字識別
5. **《2022 新版控制措施講解》**：11 項新增控制措施與 4 大面向分類

### 3. 半導體機台資安：Teradyne Eagle 364 & SEMI E187 & TI 實務
- **機台架構與工控弱點**：ETS-364 / Eagle 測試機台 Industrial PC（Windows 7/10 終止支援、USB 測試程式載入、STDF 良率數據外洩、Tester 局域網未隔離）。
- **SEMI E187 四大支柱落地**：
  - 作業系統安全（OS Security）：遺產系統補償控制、應用程式白名單
  - 網路安全（Network Security）：VLAN 802.1Q 微隔離、嚴格禁用直連外網
  - 端點防護（Endpoint Protection）：硬體式 USB 埠實體鎖、隨身碟深度殺毒
  - 資安監控與審查（Security Monitoring）：Syslog 集中日誌、異常測試量拋轉警報
- **TI 實務對照**：測試向量防篡改（數位簽章驗證）、黃金樣本（Golden Unit）測試驗證、STDF 即時傳輸加密。

### 4. 關鍵基礎設施實體安全：國廷電機駐點中華電信數據一大樓電力維運
- **數據一大樓電力系統規格**：台電 22.8kV 雙饋線雙路受電、2N 重複備援電力迴路、UPS 模組化電池室、緊急柴油發電機組（連續供電 24h+）。
- **國廷電機一級保養項目**：
  - 每日抄表巡檢（電壓/電流/功因/諧波 THD）
  - 配電盤與匯流排紅外線熱影像分析（預防熱點事故）
  - UPS 蓄電池內阻與導電度量測（Midtronics 檢測）
  - 柴油發電機每週無載試車、每月帶載 ATS 自動切換測試
  - 機房溫濕度監控（22±2°C / 50±10%）與 FM-200 滅火系統聯鎖防護
- **ISO 27001 條文對標**：
  - **A.7.11 支援性公用設施（Supporting utilities）**：電力中斷、突波吸收、雙路供電
  - **A.7.4 實體安全監視（Physical security monitoring）**：BMS 環控系統、CCTV 24/7 留存 90 天
  - **A.5.30 業務營運持續之 ICT 整備度（ICT readiness for BC）**：MTD/RTO 機房不斷電保證

### 5. 中華電信甄試面試突圍策略
- **口試核心優勢**：「國廷電機數據一大樓電力一級保養實作」+「ISO 27001 LA 國際資安主導稽核員視角」。
- 將純機電技術昇華至「國家級關鍵基礎設施資通安全與營運不中斷保證」，在線路維護、機電維運或資通安全類科皆具極高競爭力。

---

## 🚀 啟動與使用方式

本專案為純前端靜態架構，無需安裝額外依賴：

```bash
# 1. 透過本機靜態伺服器啟動（例如 Python 或 Node.js）
cd learning/iso27001
python -m http.server 7007

# 2. 開啟瀏覽器訪問
http://localhost:7007
```

或直接在檔案總管中雙擊開啟 `index.html`。
