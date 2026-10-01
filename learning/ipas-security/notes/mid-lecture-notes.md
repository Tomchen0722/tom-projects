# iPAS 資訊安全工程師 - 中級能力鑑定核心講義

## 考科一：資訊安全規劃與管理
> 深入探討 ISO/IEC 27001:2022 最新 ISMS 標準、資安風險管理全流程、業務持續 (BCP/BIA)、供應鏈與委外治理、個資與法規稽核。

### 單元 1：ISO/IEC 27001:2022 ISMS 體系與控制措施

**關鍵詞 (Keywords)**: ISO 27001:2022, ISMS, PDCA, Annex A Controls, Threat Intelligence

**重點概述**: 徹底解析 ISO/IEC 27001:2022 改版核心：本文主條文 4-10 架構、附錄 A 簡化合併之四大主題 (組織、人員、實體、技術控制共 93 項)、以及新增之 11 項關鍵控制措施。

### 1.1 ISO 27001:2022 核心架構改版重點
- 控制措施由 2013 版的 14 個領域 114 項控制，整合為 **4 大主題共 93 項控制措施**：
  1. **組織控制 (Organizational)**：37 項 (如資安政策、資產使用、身分管理、供應鏈安全)。
  2. **人員控制 (People)**：8 項 (如到職審查、合約條款、資安意識培訓、離職流程)。
  3. **實體控制 (Physical)**：14 項 (如安全邊界、實體進出、設備安置、清晰桌面與螢幕)。
  4. **技術控制 (Technological)**：34 項 (如存取權限、資料防護、漏洞管理、配置管理)。

### 1.2 2022 版全新增列之 11 項控制措施 (必考！)
1. **A.5.7 威脅情資 (Threat Intelligence)**：收集並分析威脅情報以降低風險。
2. **A.5.23 雲端服務使用資安 (Information security for use of cloud services)**。
3. **A.5.30 資通訊技術業務持續準備度 (ICT readiness for business continuity)**。
4. **A.7.4 實體安全監控 (Physical security monitoring)**。
5. **A.8.9 組態管理 (Configuration management)**：建立並維護安全 Baseline。
6. **A.8.10 資訊刪除 (Information deletion)**：落實資料生命週期消除。
7. **A.8.11 資料遮罩 (Data masking)**：保護機敏資訊與個資。
8. **A.8.12 資料外洩防護 (Data leakage prevention, DLP)**。
9. **A.8.16 監控活動 (Monitoring activities)**：異常行為分析。
10. **A.8.23 網站過濾 (Web filtering)**：阻絕惡意網址存取。
11. **A.8.28 安全編碼 (Secure coding)**：SSDLC 軟體安全開發規範。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某軟體開發企業導入 ISO 27001:2022，針對 A.8.28 安全編碼控制要求，將靜態代碼分析 (SAST) 與軟體相依元件檢查整合進 CI/CD 流水線中，未通過安全測試的程式碼一律無法合入主分支，順利通過外部驗證機構查核。

---

### 單元 2：資通安全法規架構、責任等級與合規管理

**關鍵詞 (Keywords)**: Cybersecurity Act, Responsibility Levels, Incident Reporting, Critical Infrastructure

**重點概述**: 掌握我國資通安全管理法子法架構：《資通安全責任等級分級辦法》、《資通安全事件通報及應變辦法》、《資通安全情資分享辦法》之公務與特定非公務機關實施要求。

### 2.1 責任等級劃分 (A ~ E 級) 核心規定
- **A 級機關 (國家關鍵)**：總統府、五院、外交部、國防部、具備全國性公務機密或關鍵基礎設施關鍵提供者。必須建立 SOC、導入全機關 ISMS 認證、配置至少 4 名以上資安專職人員、定期辦理紅隊演練與外部稽核。
- **B 級機關**：直轄市政府、部會所屬三級機關。需配置至少 2 名資安專職人員。
- **C 級機關**：縣市政府、偏遠地區機關。配置至少 1 名資安專職人員。
- **D/E 級機關**：無專責人員，由上級機關或委外支援。

### 2.2 資安事件等級劃分與通報規定
- **第一級 / 第二級**：輕微或局部核心外系統受影響。知悉後 **1 小時內通報**，完成應變後依規結案。
- **第三級 / 第四級 (重大事件)**：國家機密外洩、關鍵業務全面中斷、或涉及核心系統遭到全面控制。知悉後 **1 小時內通報**，且必須在 **36 小時內** (或依主管機關要求期限) 完成損害控制與復原。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某市府地政局核心資料庫遭受勒索攻擊導致全市房屋產權過戶交易停擺，符合第三級資安事件定義。該局於知悉後 30 分鐘內完成資安通報，並啟動應變小組於 24 小時內利用離線備份完成核心資料還原，符合法定時限。

---

### 單元 3：資安風險評鑑與風險處置策略實務

**關鍵詞 (Keywords)**: Risk Assessment, Risk Treatment, ISO 27005, Asset Identification, Residual Risk

**重點概述**: 掌握 ISO/IEC 27005 風險管理框架：資產鑑別、威脅與脆弱性評估、風險值計算模型 (可能性 × 衝擊度)、以及四大風險處置策略與殘餘風險管理。

### 3.1 風險評鑑標準五步驟
1. **建立背景環境**：定義風險評估範圍、評估準則與風險可接受度門檻。
2. **資產鑑別與評價**：盤點資訊資產 (硬體、軟體、資料、人員、流程) 並給予價值評分 (依 CIA 三面向)。
3. **威脅與弱點分析**：辨識資產可能面臨之威脅 (人為蓄意、天災、操作失誤) 及系統存在之脆弱性。
4. **風險分析與評級**：計算風險等級：$Risk = Likelihood (可能性) \times Impact (衝擊度)$。
5. **風險評量**：比對組織風險接受準則，判斷該風險是否超出可承受限度。

### 3.2 四大風險處置策略 (Risk Treatment)
1. **風險降低 / 緩解 (Mitigation / Modification)**：實施控制措施以降低可能性或衝擊 (如部署 WAF、安裝補丁)。
2. **風險轉移 / 分擔 (Sharing / Transfer)**：將風險損失轉移給第三方 (如投保資安險、委外維運合約)。
3. **風險規避 (Avoidance)**：終止引發風險的業務活動 (如停止支援極端老舊且無法修補之作業系統)。
4. **風險保留 / 接受 (Retention / Acceptance)**：當風險已低於容許值，或處置成本顯著高於潛在損失，由高層簽核同意承擔殘餘風險 (Residual Risk)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某電商盤點出一套建置於 Windows Server 2003 的老舊會員促銷系統，因原廠早已停止安全支援且程式碼遺失無法升級。資安委員會評估後決定全面下線該系統並以微服務重寫，此即採取『風險規避』策略。

---

### 單元 4：業務持續運作計畫 (BCP) 與營運衝擊分析 (BIA)

**關鍵詞 (Keywords)**: BCP, BIA, RTO, RPO, Disaster Recovery, Tabletop Exercise

**重點概述**: 解析 ISO 22301 業務持續管理系統：營運衝擊分析 (BIA) 指標、災難復原中心形式 (Hot/Warm/Cold Site)、BCP 演練類型與維護。

### 4.1 關鍵業務指標三要素
- **MTD (最大可容忍中斷時間)**：業務中斷若超過此時間，組織將面臨無法挽回之倒閉、法律撤照或重大商譽毀滅。
- **RTO (復原時間目標)**：系統實際必須完成修復並重新對外提供服務的目標時間 (必須小於 MTD)。
- **RPO (復原點目標)**：中斷事件中可容許遺失的資料時間跨度 (決定了資料備份或異地同步的頻率)。

### 4.2 災難復原站台 (DR Site) 比較
- **熱站 (Hot Site)**：硬體、網路、系統、即時資料同步全部就緒，可在數秒至數分鐘內全自動接管 (Failover)。成本最高，適用於金融核心交易。
- **溫站 (Warm Site)**：硬體與系統已部署，但資料非即時同步，需手動掛載備份還原，復原時間數小時至一天。
- **冷站 (Cold Site)**：僅具備機房空間、電力與空調，無現成運算硬體，需臨時採購或搬遷設備，復原需數天至數週。成本最低。

### 4.3 演練層次
1. 桌面兵棋推演 (Tabletop Exercise) -> 2. 結構化走查 (Structured Walk-through) -> 3. 模擬情境測試 (Simulation Test) -> 4. 完全中斷切換演練 (Full Interruption Test)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】證券交易所核心撮合系統要求 RTO = 0 分鐘，RPO = 0 秒。其建置同城雙活 (Active-Active) 熱站，透過同步光纖通道進行雙向寫入，當主機房突遭斷電時，備援機房無縫接管，市場交易零中斷。

---

### 單元 5：第三方供應鏈安全與委外資安管理

**關鍵詞 (Keywords)**: Supply Chain Risk, Vendor Management, SLA, Right to Audit, SBOM

**重點概述**: 掌握軟體供應鏈與委外廠商全生命週期管理：合約資安規範 (Right to Audit 稽核權)、SLA 服務水準協定、第三方遠端連線管制與開源軟體風險評估。

### 5.1 委外生命週期風險管控
- **評選階段**：審查廠商資安資質 (如 ISO 27001 證書、過往資安事故紀錄、開發人員認證)。
- **合約規範**：明確約定『保密協定 (NDA)』、『資安通報責任』、『稽核權條款 (Right to Audit)』與違約賠償。
- **連線與權限管理**：嚴禁外包廠商常設通用帳號；遠端維運必須經由 VPN + MFA 登入特權管理跳板機 (PAM)，全程側錄操作。
- **退場與終止**：合約終止時，徹底撤銷所有帳號與網路存取權，收回或銷毀所有機敏資料並取得廠商切結書。

### 5.2 軟體供應鏈安全 (Software Supply Chain Security)
- 盤點所有第三方函式庫，要求提供 SBOM (軟體物料清單)。
- 建立軟體元件分析 (SCA) 機制，防範依賴混淆 (Dependency Confusion) 與搶註 Typosquatting 開源套件。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】SolarWinds 供應鏈攻擊事件中，駭客藉由入侵軟體開發商的構建系統，在合法簽名的更新包中注入木馬。防範此類威脅，企業除審查廠商資安機制外，應落實微切分與 Zero Trust，即便合法軟體有異常外連行為亦即時阻斷。

---

### 單元 6：資安治理架構、政策制定與成熟度評估

**關鍵詞 (Keywords)**: Security Governance, CISO, KPI / KRI, Cybersecurity Policy, CMMI

**重點概述**: 建立現代企業資安治理體系：董事會與管理階層當責性、CISO 職掌與獨立性、資安政策四層級文件架構、關鍵績效指標 (KPI/KRI) 與成熟度衡量。

### 6.1 資安治理與組織職責
- **治理 vs 管理**：治理 (Governance) 由董事會與高階主管負責，決定方向、戰略投資與風險偏好；管理 (Management) 由 CISO 與技術團隊負責日常計畫、執行與維運。
- **CISO 的獨立性**：CISO (資安長) 應直接向董事會或執行長 (CEO) 報告，避免隸屬於 CIO (資訊長) 之下，以防止資安目標與 IT 效率產生利益衝突。

### 6.2 資安文件四階體系
- **一階：政策 (Policy)**：高階管理層宣示之全域方針與原則 (如資訊安全政策)。具強制性，異動頻率低。
- **二階：程序 / 辦法 (Procedure / Standard)**：具體工作規範 (如帳號管理辦法、弱點修補程序)。
- **三階：作業指引 / 準則 (Guideline / Work Instruction)**：技術操作步驟指引 (如 Windows 伺服器強化手冊)。
- **四階：表單 / 紀錄 (Record / Form)**：執行各項控制所留下的佐證軌跡 (如門禁進出登記簿、簽核紀錄)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某金控金檢時被主管機關糾正，因其資安長兼任開發維運主管，導致為求系統快速上線而忽視資安檢驗。該金控隨後調整組織架構，設立獨立資安專責處室，CISO 直屬總經理，建立健全資安治理制衡。

---

### 單元 7：國際資料隱私法規 (GDPR) 與隱私保護技術

**關鍵詞 (Keywords)**: GDPR, Privacy by Design, DPO, PIA / DPIA, Pseudonymization

**重點概述**: 掌握歐盟 GDPR 與國際隱私標準：資料主體權利 (被遺忘權、資料可攜權)、隱私衝擊評估 (DPIA)、假名化與去識別化技術。

### 7.1 歐盟 GDPR 核心原則與當事人權利
- **資料保護長 (DPO)**：處理大量機敏資料或大規模監控行為的組織必須設置獨立的 DPO。
- **當事人關鍵權利**：
  - 存取權與被遺忘權 (Right to be Forgotten / Erasure)：當事人在特定條件下有權要求企業刪除其全部個資。
  - 資料可攜權 (Right to Data Portability)：有權取得機器可讀格式之個人資料並移轉至另一平台。
- **違規重罰條款**：最高可處全球年營業額 **4%** 或 **2000 萬歐元** (取其高者)。
- **72 小時通報**：發生個資外洩事件，必須在知悉後 **72 小時內** 通報主管機關。

### 7.2 隱私工程保護技術
- **假名化 (Pseudonymization)**：將識別欄位替換為假名代碼，除非取得分開保存之金鑰否則無法反查。
- **匿名化 (Anonymization)**：經過不可逆處理，任何技術皆無法重新識別出特定個人 (不再適用 GDPR 管轄)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】跨國電商平台收到歐洲客戶依據 GDPR 提出被遺忘權要求。平台資安與資料團隊啟動自動化遮蔽流程，將歷史訂單中的客戶姓名、電話、地址永久去識別化，同時保留不具個資之交易金額供財務查帳，兼顧合規與商業需求。

---

### 單元 8：資安稽核實務、缺失改善與 CAPA 機制

**關鍵詞 (Keywords)**: Internal Audit, Audit Evidence, CAPA, Corrective Action, Non-Conformity

**重點概述**: 學習資安內外部稽核流程：稽核計畫擬定、抽樣證據獲取、不符合項 (Non-conformity) 開立、根因分析 (RCA) 與矯正預防措施 (CAPA) 追蹤結案。

### 8.1 稽核三大類型
- **第一方稽核 (內部稽核)**：組織內部稽核人員自行檢查各部門 ISMS 落實狀況。稽核員必須具備獨立性 (不得稽核自己所屬部門之業務)。
- **第二方稽核 (供應商稽核)**：企業對其外包商、供應商進行合約與資安合規性查核。
- **第三方稽核 (驗證稽核)**：由獨立公正的驗證機構 (如 BSI, SGS, ISO 認證單位) 進行標準符合性審查與發證。

### 8.2 矯正與預防措施 (CAPA) 流程
1. **確認不符合項 (Finding)**：明確記載客觀事實驗證違規。
2. **緊急遏止處置 (Containment)**：立即修正眼前錯誤。
3. **根本原因分析 (Root Cause Analysis, RCA)**：使用 5-Whys 或魚骨圖深入探究制度或技術根因。
4. **矯正措施擬定與執行 (Corrective Action)**：修改程序或增強控制防止重複發生。
5. **有效性驗證 (Effectiveness Review)**：在下一次稽核週期回查該措施是否確實有效運作。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】內稽發現某離職員工帳號在離職 30 天後仍未停用。除立即關閉該帳號外，深入 RCA 發現人事系統與 AD 帳號系統為人工通知脫鉤。矯正措施為開發自動化 API 同步，人事系統一辦理離職流程，AD 帳號自動秒級鎖定，徹底杜絕缺失再犯。

---

## 考科二：資訊安全防禦技術與事件應變
> 涵蓋零信任架構落地、MITRE ATT&CK 框架、SOC 監控與 SOAR 自動化、CSIRT 五大階段事件應變、數位鑑識與證據保全、安全軟體開發 (SSDLC) 與雲端資安架構實務。

### 單元 1：零信任架構 (ZTA) 規劃與落地實務

**關鍵詞 (Keywords)**: Zero Trust, NIST SP 800-207, PDP, PEP, Micro-Segmentation

**重點概述**: 掌握 NIST SP 800-207 零信任架構藍圖：策略決定點 (PDP)、策略執行點 (PEP)、軟體定義邊界 (SDP)、身份感知代理 (IAP) 與網路微切分實作。

### 1.1 NIST SP 800-207 核心原則
- 所有資料來源與運算服務皆視為資源。
- 無論處於內部網路或外部網路，所有通訊全程加密。
- 存取單一資源之授權必須以『每個工作階段 (Per-session)』為基礎動態評估。
- 存取決定依據動態政策，涵蓋身分狀態、設備健康度、地理環境特徵。

### 1.2 零信任架構核心元件
- **策略引擎 (Policy Engine, PE)**：決定是否授予特定請求存取權限的大腦。
- **策略管理點 (Policy Administrator, PA)**：接收 PE 指令，向 PEP 發送金鑰或工作階段連線憑證。
- *(PE 與 PA 合稱為策略決定點 PDP)*。
- **策略執行點 (Policy Enforcement Point, PEP)**：守門員元件，直接啟用、監控並最終中斷主體與資源之間的連線 (如 API Gateway、SDP Client)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】跨國企業導入零信任架構，研發人員即使在家辦公，若其筆電防毒軟體未更新或未開啟磁碟加密，PDP 判斷設備健康度不合格，PEP 立即阻斷其對生產代碼庫之存取，僅允許連線至自修補入口。

---

### 單元 2：MITRE ATT&CK 框架、Cyber Kill Chain 與威脅情資 (CTI)

**關鍵詞 (Keywords)**: MITRE ATT&CK, Cyber Kill Chain, Threat Intelligence, TTPs, Pyramid of Pain

**重點概述**: 掌握 MITRE ATT&CK 14 大戰術矩陣、洛克希德馬丁網路殺傷鏈、痛苦金字塔 (Pyramid of Pain) 以及威脅情資 (STIX/TAXII) 實務應用。

### 2.1 痛苦金字塔 (The Pyramid of Pain)
防禦者辨識並封鎖攻擊者特徵指標時，帶給攻擊者的痛苦程度由低到高：
1. **雜湊值 (Hash Values)**：對黑客極容易更換 (改一個 byte 雜湊值全變)。
2. **IP 位址 (IP Addresses)**：容易更換 (代理伺服器、VPN)。
3. **網域名稱 (Domain Names)**：稍具難度 (需要重新購買註冊，或用 DGA)。
4. **網路與主機產出物 (Network/Host Artifacts)**：具中等難度 (修改惡意通訊特徵)。
5. **攻擊工具 (Tools)**：困難 (黑客必須重新尋找或重編工具)。
6. **手法戰術與技術 (TTPs)**：**最頂層、最痛苦**！黑客必須徹底改變其行為思維與受訓模式。

### 2.2 MITRE ATT&CK 典型戰術路徑
初始存取 (Initial Access) -> 執行 (Execution) -> 持續性潛伏 (Persistence) -> 權限提升 (Privilege Escalation) -> 防禦規避 (Defense Evasion) -> 憑證存取 (Credential Access) -> 發現探勘 (Discovery) -> 橫向移動 (Lateral Movement) -> 收集 (Collection) -> 命令與控制 (C2) -> 資料外洩 (Exfiltration) -> 破壞衝擊 (Impact)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】SOC 分析員在分析 APT 攻擊時，發現黑客使用 Mimikatz 傾倒記憶體憑證 (T1003)。防禦團隊未僅僅阻擋 Mimikatz 執行檔雜湊，而是在網域層全面啟用 Credential Guard 並阻斷 LSASS 記憶體讀取，直擊 TTPs 頂端，徹底封殺該黑客團體之活動。

---

### 單元 3：現代 SOC 維運、SIEM 關聯分析與 SOAR 自動化劇本

**關鍵詞 (Keywords)**: SOC, SIEM, SOAR, Playbook, Alert Fatigue, Use Cases

**重點概述**: 探討安全維運中心 (SOC) 7x24 監控機制、SIEM 關聯分析規則撰寫、警報疲勞 (Alert Fatigue) 緩解與 SOAR 自動化劇本編排。

### 3.1 SIEM 關聯規則設計範例
- **暴力破解成功情境**：同一個帳號在 5 分鐘內發生超過 10 次 Event ID 4625 (登入失敗)，且隨後緊接著出現 Event ID 4624 (登入成功)。此為暴力破解成功或密碼猜測之經典特徵。
- **非上班時間異常大流量外傳**：夜間 02:00 ~ 05:00 期間，非備份伺服器向國外未知 IP 外傳超過 10GB 之封包。

### 3.2 SOAR 自動化回應劇本 (Playbook)
- 當 SIEM 觸發高危情資警報 -> SOAR 自動呼叫 VirusTotal API 查詢檔案雜湊 -> 若檢出率大於 20 家 -> 自動發送 API 命令至 EDR 隔離受害終端 -> 同時在防火牆黑名單封鎖連線 IP -> 在 ITSM 建立資安事故工單並推播通知值班資安工程師。
- 劇本自動化可將事件處理平均時間 (MTTR) 從數小時壓縮至數秒鐘。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某電信巨頭 SOC 面臨每日數萬筆警報導致警報疲勞。團隊引進 SOAR 編寫自動驗證劇本，先過濾 85% 的誤報與已知低危雜訊，將分析師專注力解放至真正的重大威脅，威脅回應速度提升 600%。

---

### 單元 4：CSIRT 資安事件應變五大階段實務指南

**關鍵詞 (Keywords)**: Incident Response, NIST SP 800-61, CSIRT, Containment, Lessons Learned

**重點概述**: 掌握 NIST SP 800-61 事件應變生命週期：準備 (Preparation) -> 偵測與分析 (Detection & Analysis) -> 圍堵、抹除與復原 (Containment, Eradication & Recovery) -> 檢討與改善 (Post-Incident Activity)。

### 4.1 事件應變四大循環核心 (NIST SP 800-61)
1. **準備階段 (Preparation)**：建置 CSIRT 小組成員通訊錄、準備乾淨應變工具箱 (Jumpsuit)、演練 Playbook、落實各項日誌與備份。
2. **偵測與分析 (Detection & Analysis)**：判定事件真實性與嚴重性等級，界定受災範圍 (Scope of Breach)，確認攻擊向量與受害指標 (IoC)。
3. **圍堵策略 (Containment)**：
   - **短期圍堵**：拔掉受害主機網線或 EDR 網路隔離，阻止向外橫向感染。
   - **長期圍堵**：修補防火牆規則、重設受影響網域管理者憑證。
4. **抹除與復原 (Eradication & Recovery)**：清除所有後門程式、惡意排程與受損使用者帳號；利用純淨離線備份還原系統，並提升監控頻率至少 1 至 3 個月。
5. **事後檢討 (Lessons Learned)**：召開 PIR (Post-Incident Review) 會議，提出事件檢討報告，將缺失轉化為架構改善計畫。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某半導體大廠遭遇進階惡意程式感染。應變小組未急於重灌主機 (避免破壞證據)，而是先透過 EDR 圍堵受害主機群並萃取記憶體 Dump 進行逆向，找出 C2 通訊協議與所有受感染清單後，進行一次性全網清除，避免了復發二次感染。

---

### 單元 5：數位鑑識、證據保全與記憶體鑑識實務

**關鍵詞 (Keywords)**: Digital Forensics, Order of Volatility, Chain of Custody, Volatility, Bit-stream Image

**重點概述**: 學習數位鑑識四大原則 (RFC 3227)：揮發性順序、證據監管鏈 (Chain of Custody)、只讀硬體寫入阻斷器 (Write Blocker)、記憶體 RAM 傾倒與離線映像分析。

### 5.1 現場採證操作規範
- **嚴禁重開機或隨意關機**：重開機會立即抹除 RAM 中的暫態記憶體資料、解密金鑰與網路連線狀態。
- **使用硬體防寫設備 (Hardware Write Blocker)**：在對儲存媒體進行映像複製時，物理硬體保證僅能讀取無法寫入，確保原始證據完整未動。
- **位元對位元複製 (Bit-Stream Image)**：包括未配置空間 (Unallocated Space) 與鬆弛空間 (Slack Space)，產出 dd, raw, E01 格式映像。
- **雜湊校驗比對**：採集前先計算原始磁碟 SHA-256，複製完成後再次計算映像檔 SHA-256，兩者雜湊值必須百分之百一致方具司法證據效力。

### 5.2 記憶體鑑識重點 (Volatility 工具)
- 提取動態載入的無檔案惡意程式 (Fileless Malware)。
- 檢視當前已建立的 TCP 網路連線 (netscan)。
- 提取當前執行的進程列表與注入代碼 (pslist, malfind)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】司法警察配合資安鑑識團隊查扣某洗錢機房之主機。團隊在電腦維持通電狀態下，利用專用硬體工具即時完整導出 64GB 記憶體，成功在 RAM 中解密出 Telegram 秘密通訊群組與比特幣錢包私鑰，成為法庭定罪關鍵證據。

---

### 單元 6：安全軟體開發 (SSDLC) 與 DevSecOps 實務

**關鍵詞 (Keywords)**: SSDLC, DevSecOps, SAST, DAST, STRIDE, Threat Modeling

**重點概述**: 掌握微軟 STRIDE 威脅建模方法論、CI/CD 安全流水線建構、靜態程式碼分析 (SAST)、動態應用檢測 (DAST) 與軟體相依性掃描 (SCA)。

### 6.1 STRIDE 威脅建模模型
- **S - 偽冒身分 (Spoofing)** -> 對應安全屬性：身分驗證 (Authentication)。
- **T - 竄改資料 (Tampering)** -> 對應安全屬性：完整性 (Integrity)。
- **R - 否認行為 (Repudiation)** -> 對應安全屬性：不可否認性 (Non-Repudiation)。
- **I - 資訊洩漏 (Information Disclosure)** -> 對應安全屬性：機密性 (Confidentiality)。
- **D - 阻斷服務 (Denial of Service)** -> 對應安全屬性：可用性 (Availability)。
- **E - 特權提升 (Elevation of Privilege)** -> 對應安全屬性：授權控制 (Authorization)。

### 6.2 現代 DevSecOps 安全工具整合
- **SAST (靜態分析)**：白箱測試。在編譯階段分析原始碼，速度快、涵蓋率高，但無法發現運行時環境問題 (如 SonarQube, Fortify)。
- **DAST (動態分析)**：黑箱測試。從外部對運行中的 Web 應用發送攻擊 Payload 測試，能發現組態與伺服器問題，但無法定位到程式碼具體行數 (如 OWASP ZAP)。
- **SCA (軟體成分分析)**：自動掃描開源依賴項之公開已知漏洞 (如 Snyk, Dependency-Check)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】金融科技新創將 DevSecOps 落地於 GitLab CI 流水線中，在程式碼 Commit 時自動執行 SAST 與 SCA。若發現嚴重等級大於 High 的漏洞，流水線自動中斷部署，強制開發者修正後方可上線，上線後漏洞率下降 85%。

---

### 單元 7：雲端安全架構 (Cloud Security) 與虛擬化防護

**關鍵詞 (Keywords)**: Shared Responsibility Model, CSPM, CWPP, CASB, IAM

**重點概述**: 掌握雲端責任共擔模型 (IaaS, PaaS, SaaS)、雲端安全狀態管理 (CSPM)、工作負載保護 (CWPP)、CASB 與雲端身分權限控管最佳實務。

### 7.1 雲端責任共擔模型 (Shared Responsibility Model)
- **IaaS (基礎架構即服務，如 AWS EC2)**：雲端業者負責實體設施、硬體伺服器與虛擬化底層；**客戶負責**作業系統安裝、更新修補、網路防火牆安全組 (Security Group)、應用程式與所有資料加密。
- **PaaS (平台即服務，如 Google App Engine)**：業者負責實體與作業系統補丁；客戶負責應用程式本身之邏輯與資料安全。
- **SaaS (軟體即服務，如 Microsoft 365)**：業者負責底層至應用程式全端安全；**客戶依然負責使用者身分認證、存取控制與自身資料治理**。
- **鐵律**：無論哪種雲端模式，**『資料的擁有與資料保護責任』永遠在客戶身上**！

### 7.2 雲端安全三大利器
- **CSPM (雲端安全狀態管理)**：持續稽核雲端環境組態配置 (如防範 S3 Bucket 意外公開、檢查過度寬鬆的 IAM 權限)。
- **CWPP (雲端工作負載保護平台)**：針對雲端 VM、Container (Docker/K8s) 提供運行時進程監控與漏洞防護。
- **CASB (雲端存取安全代理)**：在企業與多個 SaaS 應用之間充當安全閘道，防範影子 IT (Shadow IT) 與資料外洩。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】某企業將客戶資料備份至 AWS S3，工程師誤將儲存桶權限設為 Public Read，導致數百萬筆個資直接在網路上裸奔。導入 CSPM 後，系統即時偵測到組態偏離 baseline，自動觸發修復腳本強制關閉公開權限並通報 CISO。

---

### 單元 8：進階持續性威脅 (APT) 防禦與主動威脅獵捕 (Threat Hunting)

**關鍵詞 (Keywords)**: Threat Hunting, APT Defense, Lateral Movement, Pass-the-Hash, Living off the Land

**重點概述**: 掌握主動威脅獵捕 (Threat Hunting) 假說驅動模型、橫向移動 (Lateral Movement) 檢測、Pass-the-Hash 防禦與無檔案攻擊因應策略。

### 8.1 主動威脅獵捕 (Threat Hunting) 思維
- **假設已被滲透 (Assume Breach)**：擺脫『被動等待警報』模式，主動假設攻擊者已潛伏在內部網路，透過主動分析日誌與行為遙測尋找異常跡象。
- **假說驅動獵捕 (Hypothesis-driven Hunting)**：
  1. 提出假設：『近期有針對半導體產業的釣魚攻擊利用 WMI 進行持續性潛伏』。
  2. 收集指標：查詢全網端點中 WMI Event Filter 與 Consumer 的建立事件。
  3. 驗證排查：過濾合法軟體，找出隱匿的惡意排程腳本。
  4. 回饋強化：將發現的新特徵轉化為 SIEM 的永久自動偵測規則。

### 8.2 橫向移動 (Lateral Movement) 常見手法防禦
- **Pass-the-Hash (PtH)**：攻擊者竊取記憶體中的 NTLM 雜湊直接進行身分驗證。
- **防禦**：啟用 Windows Defender Credential Guard (利用虛擬化安全技術 VBS 隔離 LSASS)、停用 NTLM 改用 Kerberos、在端點主機實施主機防火牆嚴禁工作站之間互連 (Workstation-to-Workstation Isolation)。

> 💡 **實務案例與考點 (Case Study)**:
> 【實務情境】威脅獵捕團隊提出假設：攻擊者可能濫用內網未受管工作站互相遠端。透過分析內網流量圖譜，發現原本應為單純終端的一台辦公室 PC，半夜竟然向其他 40 台工作站發起大量 SMB 445 掃描。獵捕小組成功在攻擊者觸發任何勒索軟體前將其拔除，挽救企業整座內網。

---

