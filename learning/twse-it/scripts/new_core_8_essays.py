# -*- coding: utf-8 -*-
"""
8 Core TWSE Information Security Simulation Essays (sec-essay-69 ~ sec-essay-76)
Covering:
1. 零信任架構（ZTA）三大核心原則在核心交易系統防護落地 (sec-essay-69)
2. 證交所資安分級防護下滲透測試與弱點掃描差異與互補性 (sec-essay-70)
3. 金融核心系統導入 ISO/IEC 27001:2022 資產與風險管理核心步驟 (sec-essay-71)
4. 證券交易所遭受大規模 DDoS 緊急應變與復原計畫流程 (sec-essay-72)
5. 雙重勒索手段下 3-2-1 備份原則與網路分段防橫向移動 (sec-essay-73)
6. 金融郵件安全防護機制：技術過濾規則與鑑別日誌功能 (sec-essay-74)
7. SQL 注入與 XSS 攻擊原理及 SDLC 全生命週期防範 (sec-essay-75)
8. 對稱加密 vs 非對稱加密在 TLS/HTTPS 中之協同運作機制 (sec-essay-76)
"""

def get_8_core_twse_essays():
    return [
        # 1. sec-essay-69: ZTA in TWSE Trading System
        {
            "id": "sec-essay-69",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "金融核心交易系統零信任架構（ZTA）三大原則落地與設計實務",
            "summary": "深入解構 NIST SP 800-207 零信任架構理念、永不信任（微隔離/最小權限）、始終驗證（FIDO2 MFA/持續動態授權）、假設已遭入侵（爆炸半徑收斂/全流量鑑識）在證券交易之實踐。",
            "points": 25,
            "rubric": "1. 零信任架構本質與破題 (7分)；2. 三大核心原則落地技術關鍵對比 (7分)；3. 證券交易核心實務架構設計 (7分)；4. 結論 (4分)",
            "question": "請說明何謂「零信任架構（Zero Trust Architecture, ZTA）」，並申論金融機構（如證券交易所、證券商）在設計核心交易系統防護時，應如何落實零信任的三大核心原則（永不信任、始終驗證、假設已遭入侵）？",
            "modelAnswer": """
<h4>一、破題：零信任架構（ZTA）之核心哲學</h4>
<p>傳統金融機構資安依賴「城堡護城河（Perimeter-based Security）」模型，預設內部局域網（Intranet）為安全信任區。然而，在供應鏈跳板攻擊、勒索軟體與內網橫向滲透日益猖獗的背景下，邊界已被徹底打破。</p>
<p><strong>零信任架構（NIST SP 800-207）</strong>的核心哲學是<strong>「以身分為中心、將邊界縮小至單一資源」</strong>，預設網路環境始終充滿威脅，揚棄任何基於網路拓撲或實體位置的預設信任，全面貫徹「持續評估、動態授權」。</p>

<h4>二、核心交易系統落實零信任三大核心原則之重點對比與關鍵分析</h4>
<ul>
  <li><strong>1. 永不信任 (Never Trust)</strong>：- 徹底消除內部專用網路特權； - 實施微隔離（Micro-segmentation）； - 最小權限存取（Least Privilege）與零常設權限（ZSP）。；撮合主機、下單閘道器與帳務資料庫劃分於獨立極小網段；各伺服器間預設 全面禁止互通（Default-Deny） ；管理員無常設 root 權限，全面透過 PAM 堡壘機實施 Just-In-Time（JIT）按需提權與雙人授權。。</li>
  <li><strong>2. 始終驗證 (Always Verify)</strong>：- 每次存取皆視為全新獨立連線； - 多因子身分鑑別（MFA）； - 原則決定點（PDP）動態計算信任分數。；強制推行 FIDO2 / WebAuthn 抗釣魚硬體認證 ；原則強制點（PEP）攔截所有 API 下單連線，綜合評估用戶身分、客戶端憑證（mTLS）、端點設備健康度（EDR 合規）進行動態存取判定。。</li>
  <li><strong>3. 假設已遭入侵 (Assume Breach)</strong>：- 預設敵手已成功滲透至內網； - 收斂單點爆炸半徑（Blast Radius）； - 全流量封包鑑識與威脅主動獵捕。；資料全面靜態加密（AES-256）且私鑰鎖定於 FIPS 140-3 HSM ；部署 eBPF（Cilium / Tetragon）在 Linux 系統呼叫層直接阻斷容器逃逸；7x24 SOC 與 NDR 全量分析橫向移動。。</li>
</ul>

<h4>三、證券核心交易系統零信任控制流規劃</h4>
<ol>
  <li><strong>身分與通訊控制（PEP/PDP）</strong>：外部券商或投資人下單請求抵達邊界 PEP（API 閘道器），強制執行 mTLS 與 OAuth 2.1 權杖校驗；PDP 結合威脅情資即時評估，通過後方可建立短暫生命週期之微隧道。</li>
  <li><strong>特權維運控管</strong>：核心資料庫維運嚴禁 SSH 直連，統一經由具備螢幕全側錄、一次性動態指令核准之 PAM 跳板機，落實事後不可否認性。</li>
</ol>

<h4>四、結論</h4>
<p>在微秒決勝的金融市場中，零信任並非單一產品，而是貫穿身分、端點、網路、工作負載與資料的縱深工程體系，確保核心交易即便在遭遇外部突破時，亦能堅守資金與帳務的絕對安全底線。</p>
            """,
            "examinerTips": "破題得分關鍵字：『以身分為新邊界，揚棄內網即信任城堡護城河模型』、『三大原則：永不信任 (微隔離+最小權限)、始終驗證 (FIDO2抗釣魚+動態PDP/PEP)、假設已遭入侵 (收斂爆炸半徑+HSM加密保全)』、『PAM 堡壘機 JIT 按需提權與雙人覆核』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>零信任定義與哲學（7分）</strong>：引用 NIST SP 800-207 概念，對比傳統城堡模型與現代身分邊界架構。</li>
  <li><strong>三大原則落地矩陣表（7分）</strong>：以條列逐項剖析永不信任、始終驗證、假設已遭入侵之設計重點與證券撮合/帳務之具體落實手法。</li>
  <li><strong>核心控制流規劃（7分）</strong>：詳述 PEP/PDP 下單連線控制流與 PAM 堡壘機維運治理。</li>
  <li><strong>結論（4分）</strong>：總結零信任對金融強韌性之保障。</li>
</ul>
            """
        },

        # 2. sec-essay-70: Penetration Test vs Vulnerability Scan in TWSE Graduated Defense
        {
            "id": "sec-essay-70",
            "category": "sec",
            "chapter": "第 10 章：紅藍對抗、滲透測試與漏洞弱點管理",
            "title": "證券商資安分級防護下滲透測試與弱點掃描之差異、實務互補與申報稽核實踐",
            "summary": "深入剖析證交所「證券商資安分級防護應辦事項」、第一至三級證券商規範、弱點掃描（廣度/自動化）與滲透測試（深度/實彈鏈式利用）之技術差異，以及申報專區閉環管理。",
            "points": 25,
            "rubric": "1. 證交所分級防護監理背景 (7分)；2. 弱點掃描 vs 滲透測試關鍵對比 (7分)；3. 實務互補流程與申報專區列管 (7分)；4. 結論 (4分)",
            "question": "證交所近期建立「證券商資安防護事項申報專區」並推動資安分級防護。請闡述一般證券商（或第一至三級證券商）定期進行滲透測試（Penetration Test）與弱點掃描（Vulnerability Scan）的差異與實務互補性。",
            "modelAnswer": """
<h4>一、破題：證交所推動資安分級防護與申報專區之監理意涵</h4>
<p>依臺灣證券交易所「證券商資通安全防護評估作業原則」與「證券商資安分級防護應辦事項」，證券商依據實收資本額、電子下單成交金額及客戶數被評定為第一級至第三級。證交所特別建置<strong>「證券商資安防護事項申報專區」</strong>，要求業者將防護執行紀錄定期線上申報，實施穿透式監理。</p>
<p>在此監理框架下，<strong>弱點掃描（VS）</strong>與<strong>滲透測試（PT）</strong>為法定必辦之兩大核心技術檢測手段，兩者定位不同且不可相互替代。</p>

<h4>二、弱點掃描（Vulnerability Scan）vs 滲透測試（Penetration Test）核心差異</h4>
<ul>
  <li><strong>【弱點掃描 (Vulnerability Scan)】</strong>：<strong>檢測本質與手段</strong>：自動化工具靜態比對 （如 Nessus、OpenVAS），比對已知 CVE 漏洞庫與特徵字串。；<strong>檢測深度與廣度</strong>：廣度優先 ：能於短時間內全面掃描全網數千台伺服器之開放連接埠與軟體版本。；<strong>業務邏輯漏洞偵測</strong>：完全無能為力 ：無法理解如「下單金額篡改、越權讀取他人委託單」等複雜業務流程。；<strong>檢測頻率與成本</strong>：頻率高（每月/每季）、執行成本低、產出大量報告（常含偽陽性 False Positives）。。</li>
  <li><strong>【滲透測試 (Penetration Test)】</strong>：<strong>檢測本質與手段</strong>：人工白帽黑客實戰攻防 ，模擬真實 APT 組織進行戰術與邏輯漏洞刺探。；<strong>檢測深度與廣度</strong>：深度優先 ：透過 鏈式漏洞組合（Chained Exploits） ，深入打穿邊界並嘗試內網橫向移動（Lateral Movement）。；<strong>業務邏輯漏洞偵測</strong>：極佳 ：重點挖掘身分認證繞過、IDOR 水平越權、競態條件（Race Condition）等交易邏輯弱點。；<strong>檢測頻率與成本</strong>：頻率低（每年至少 1 次或系統重大改版）、成本高、驗證真實可利用性（零偽陽性）。。</li>
</ul>

<h4>三、實務互補運作流程與證交所申報合規實踐</h4>
<ol>
  <li><strong>「以弱掃定基線，以滲透測深防」之協同流程</strong>：
    - <strong>第一階段（弱掃築基）</strong>：券商每月定期執行全網弱掃，第一時間修補作業系統、資料庫已知高危補丁（CVSS ≥ 7.0），掃除表面死角；<br>
    - <strong>第二階段（滲透實戰）</strong>：委由具備專業資安證照（OSCP/CEH/CISSP）之第三方團隊，針對弱掃無法檢測的下單 Web/API 及手機 App 進行黑箱或灰箱滲透；<br>
    - <strong>第三階段（防禦驗證）</strong>：驗證 SOC 監控中心是否能在黑客滲透過程中即時觸發告警，檢驗藍隊實戰防守能力。
  </li>
  <li><strong>證交所申報專區閉環追蹤</strong>：
    檢測完成後，券商依規範將弱點修補計畫、第三方滲透測試報告上傳至證交所申報專區。針對 High/Critical 缺失，嚴格遵循法定限期改善標準（如 14~30 天內完成複測結案），杜絕「只測不修」之合規弊端。
</li>
</ol>

<h4>四、結論</h4>
<p>弱點掃描如同「常態全身體檢」，滲透測試則是「特種部隊壓力測試」。證券商唯有將兩者有機結合，才能在證交所分級防護監理體系下，持續固化資安基線並抵禦高階持續性威脅。</p>
            """,
            "examinerTips": "評分關鍵字：『證券商資安分級防護第一至三級規範』、『證券商資安防護事項申報專區』、『弱掃 (廣度/自動化/已知CVE/高偽陽性) vs 滲透 (深度/人工/鏈式利用/業務邏輯)』、『以弱掃定基線，以滲透測深防』、『申報專區限期複測閉環管理』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>證交所監理背景（7分）</strong>：深入點評第一至三級資安防護規範，引出申報專區列管之制度脈絡。</li>
  <li><strong>核心差異橫向重點對比（7分）</strong>：以標準條列架構從手段、廣深度、業務邏輯能力、成本頻率詳盡對比兩者本質差異。</li>
  <li><strong>互補性流程與申報實務（7分）</strong>：提出兩階段協同流程，並結合證交所申報專區限期修復複測要求。</li>
  <li><strong>結論（4分）</strong>：以常態體檢與特種壓力測試形象總結。</li>
</ul>
            """
        },

        # 3. sec-essay-71: ISO/IEC 27001:2022 Risk Assessment & Treatment in Trading Systems
        {
            "id": "sec-essay-71",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001:2022 與 ISO 27001 LA 稽核實務）",
            "title": "金融電子交易平台導入 ISO/IEC 27001:2022 資產與風險管理實施步驟",
            "summary": "深入解構 ISO/IEC 27001:2022 條款 6.1.2 與 6.1.3 要求、交易平台資產 CIA 價值評定、威脅弱點識別、風險計算公式、風險處理 4T 策略，以及適用性聲明書（SoA）建置實務。",
            "points": 25,
            "rubric": "1. ISO 27001:2022 風險評鑑標準破題 (7分)；2. 資產與風險辨識分析核心步驟 (7分)；3. 風險處理 4T 策略與 Annex A 對應 (7分)；4. 結論 (4分)",
            "question": "當金融核心系統（例如電子交易平台）欲導入國際資訊安全管理系統（ISO/IEC 27001:2022）時，請列舉資產與風險管理階段中，辨識與處理資安風險的核心步驟。",
            "modelAnswer": """
<h4>一、破題：ISO/IEC 27001:2022 風險管理之核心意涵</h4>
<p>ISO/IEC 27001:2022 要求組織落實<strong>以風險為導向（Risk-based Approach）</strong>的資訊安全管理系統（ISMS）。金融電子交易平台作為承載全市場撮合與委託之核心動脈，必須依據標準條款 <strong>6.1.2（資訊安全風險評鑑）</strong>與 <strong>6.1.3（資訊安全風險處理）</strong>，建立可重複、量化且具客觀依據的風險管理流程。</p>

<h4>二、資產與風險辨識評鑑核心步驟（Clause 6.1.2）</h4>
<ol>
  <li><strong>步驟 1：資產盤點與價值評定（Asset Valuation）</strong>：
    - 盤點電子交易平台範圍內之所有資產：包含實體伺服器、網路交換器、撮合軟體源碼、下單 API、營業秘密及投資人帳務個資；<br>
    - 依據<strong>機密性（Confidentiality）、完整性（Integrity）、可用性（Availability）</strong>訂定 1~5 級評分標準（例如交易撮合之可用性 A=5，行情報價完整性 I=5），取最大值或加權計算決定<strong>資產重要性價值（Asset Value, AV）</strong>。
  </li>
  <li><strong>步驟 2：威脅與弱點辨識（Threat & Vulnerability Identification）</strong>：
    - <strong>威脅辨識（Threats, T）</strong>：辨識內部人惡意洩漏、外部 APT 勒索攻擊、DDoS 阻斷交易、地震火災等威脅發生可能性（Likelihood, 1~5分）；<br>
    - <strong>弱點辨識（Vulnerabilities, V）</strong>：結合 CVE 漏洞庫、未修補補丁、未配置 MFA、軟體相依性安全缺陷等衡量脆弱程度（Impact, 1~5分）。
  </li>
  <li><strong>步驟 3：風險分析與量化計算（Risk Analysis）</strong>：
    - 採用標準風險矩陣公式計算：<code>風險值 (Risk) = 資產價值 (AV) × 威脅可能性 (T) × 弱點嚴重度 (V)</code>；<br>
    - 依分值區分為極高（Critical）、高（High）、中（Medium）、低（Low）風險等級。
  </li>
  <li><strong>步驟 4：風險評估與容忍準則比對（Risk Evaluation）</strong>：
    將計算出之風險值與董事會核可之<strong>可接受風險準則（Risk Acceptance Criteria / DoA）</strong>進行比對。凡高於容許值之風險項目，強制列入不可接受風險清單，進入處理階段。
</li>
</ol>

<h4>三、風險處理 4T 策略與適用性聲明書（SoA）落地（Clause 6.1.3）</h4>
<ul>
  <li><strong>1. 降低 (Treat / Mitigate)</strong>：導入技術或管理控制項，將風險值壓制至可接受水準。；<strong>實務落地/對策</strong>：對照 Annex A 四大主題 93 項控制措施 ：如導入 A.8.12 (DLP)、A.8.20 (網路安全)、A.5.7 (威脅情資) 與 A.8.5 (安全認證 MFA)。。</li>
  <li><strong>2. 轉移 (Transfer / Share)</strong>：將潛在財務或營運損失分擔給第三方承擔。；<strong>實務落地/對策</strong>：投保商業資安保險（Cyber Insurance）；將非核心報表伺服器委外予合格大型雲端供應商並簽署嚴格 SLA。。</li>
  <li><strong>3. 規避 (Avoid / Terminate)</strong>：直接終止特定高風險業務活動或技術。；<strong>實務落地/對策</strong>：全面廢除過期且易受攻擊之 TLS 1.0/1.1 協議，停止使用易遭釣魚之純帳密登入下單功能。。</li>
  <li><strong>4. 接受 (Tolerate / Retain)</strong>：低風險且修復成本高於潛在損失，經核准接受。；<strong>實務落地/對策</strong>：針對內部封閉測試網段殘餘之低危漏洞，經 CISO 與業務主管正式書面簽核接受殘餘風險。。</li>
</ul>
<p><strong>輸出關鍵成果</strong>：完成<strong>「適用性聲明書（Statement of Applicability, SoA）」</strong>，逐項說明 93 項控制措施之適用與否及理由；並編製<strong>「風險處理計畫（Risk Treatment Plan, RTP）」</strong>，載明指派負責人、預算與完成時限。</p>

<h4>四、結論</h4>
<p>ISO/IEC 27001:2022 為電子交易系統建立了科學量化的防護依據。透過資產 CIA 價值評定、威脅弱點精準計算與 4T 策略閉環落地，證券機構得以將有限的資安資源投注於關鍵交易風險，築牢金融韌性基石。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『ISO/IEC 27001:2022 條款 6.1.2 風險評鑑 + 6.1.3 風險處理』、『資產 CIA (機密性/完整性/可用性) 價值評級』、『風險計算：Risk = 資產價值 × 威脅可能性 × 弱點嚴重度』、『風險處理 4T 策略：降低 (Treat)、轉移 (Transfer)、規避 (Avoid)、接受 (Tolerate)』、『Annex A 93項控制措施、SoA 適用性聲明書、RTP 風險處理計畫』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>ISO 標準核心依據（7分）</strong>：精確指出 Clause 6.1.2 與 6.1.3 標準要求，闡述以風險為導向之精神。</li>
  <li><strong>四步驟評鑑流程（7分）</strong>：條列資產盤點（CIA 評定）、威脅弱點辨識、風險公式量化與可接受準則比對。</li>
  <li><strong>風險處理 4T 與 SoA 重點條列（7分）</strong>：以標準條列架構列舉 Treat、Transfer、Avoid、Tolerate 之實戰定義，並對齊 ISO 27001:2022 Annex A 93項控制項與 SoA/RTP 輸出文件。</li>
  <li><strong>結論（4分）</strong>：總結資源精準投放對金融系統之價值。</li>
</ul>
            """
        },

        # 4. sec-essay-72: TWSE Large-Scale DDoS Incident Response & Recovery SOP
        {
            "id": "sec-essay-72",
            "category": "sec",
            "chapter": "第 6 章：網路邊界防禦、DDoS 防護與微隔離架構",
            "title": "證券交易所遭受大規模 DDoS 攻擊之緊急應變（Incident Response）與復原計畫 SOP",
            "summary": "深入剖析證券開盤期間遭受大規模 L3/L4 泛洪與 L7 應用層 DDoS 攻擊、NIST SP 800-61 事件應變六階段、金管會 30 分鐘通報、BGP Flowspec/電信清洗，以及交易專線優先權復原實務。",
            "points": 25,
            "rubric": "1. 證券 DDoS 攻擊特徵與破題 (7分)；2. NIST 六階段緊急應變 SOP 流程表 (7分)；3. 電信清洗引流與專線 QoS 保障實作 (7分)；4. 結論 (4分)",
            "question": "若證券交易所遭受大規模分散式阻斷服務攻擊（DDoS），導致網路下單系統連線緩慢甚至中斷。作為資安專員，請擬定一套緊急應變（Incident Response）與復原計畫流程。",
            "modelAnswer": """
<h4>一、破題：證券市場 DDoS 攻擊之致命特性與法規剛性要求</h4>
<p>證券交易具備微秒級即時性與高金流敏感度。開盤期間（09:00~13:30）一旦因 DDoS 攻擊造成投資人連線延遲或斷線，將引發無法即時停損平倉之巨額金融損失與市場信心崩盤。依金管會《金融機構資通安全防護基準》與通報規範，重大資安事件必須於<strong>「知悉起 30 分鐘內」</strong>向主管機關通報。資安專員必須依據 <strong>NIST SP 800-61 Rev. 2</strong> 擬定分秒必爭的實戰應變 SOP。</p>

<h4>二、證券交易 DDoS 緊急應變與復原完整 SOP</h4>
<ul>
  <li><strong>1. 準備階段 (Preparation)</strong>：- 部署三層立體防護（電信端 Clean Pipe、CDN 邊緣、地端 Anti-DDoS 設備）； - 預先簽訂電信業者「BGP 動態引流清洗協定」；演練「一鍵引流腳本」。；資安架構師 / 平時常態整備。</li>
  <li><strong>2. 偵測與判定 (Detection)</strong>：- 監控下單 API 吞吐量與錯誤率（HTTP 502/504）； - 辨識攻擊類型 ：L3/L4 頻寬泛洪（SYN/UDP/ICMP Flood）或 L7 CC/慢速攻擊（Slowloris）。；SOC 監控團隊 / T+5 分鐘內 完成判定。</li>
  <li><strong>3. 遏止與通報 (Containment)</strong>：- 啟動電信引流 ：發布 BGP Flowspec 或切換 DNS CNAME 至高防清洗中心； - 地端過濾 ：啟用 SYN Cookie、封鎖異常 GeoIP、API 閘道啟動動態限速； - 法定通報 ：登入通報專區向金管會證期局及 F-ISAC 完成重大通報。；應變小組 / T+15 分鐘啟動清洗；知悉 30 分鐘內通報。</li>
  <li><strong>4. 根除與保護 (Eradication)</strong>：- 交易專線通道絕對保障 ：強制對各券商下單之固網專線（Leased Line）實施 QoS 頻寬保留，阻絕公網髒流量干擾； - WAAP 啟用進階機器人驗證（PoW 算力挑戰），剔除自動化刷單殭屍。；網路維運團隊 / 攻擊持續期間。</li>
  <li><strong>5. 復原上線 (Recovery)</strong>：- 髒流量壓制至正常基準線後，執行模擬下單與撮合鏈路完整性回歸測試； - 依受控步驟將公網 DNS 流量切回，全時監控伺服器延遲。；系統主管 / RTO ≤ 10 分鐘 恢復運作。</li>
  <li><strong>6. 檢討與報告 (Post-Incident)</strong>：- 匯出全封包 PCAP 與攻擊 IoC（惡意 IP/JA4 指紋）分享至 F-ISAC； - 於事件平息後 3 個工作天內向金管會提交正式 RCA 調查結案報告。；CISO / 事後 3 個工作天內。</li>
</ul>

<h4>三、證券交易專屬復原保障策略</h4>
<ol>
  <li><strong>交易專線與公網下單物理隔離</strong>：證交所撮合架構中，券商主要下單走專用固網專線。公網遭攻擊時，立即引導券商改由備用專線連線，確保核心撮合零中斷。</li>
  <li><strong>無感 PoW 算力挑戰</strong>：面對偽裝為一般投資人的分散式 L7 慢速查詢，WAAP 即時啟動工作量證明挑戰，消耗攻擊端 CPU 算力，徹底壓制殭屍網路。</li>
</ol>

<h4>四、結論</h4>
<p>DDoS 防禦是立體化的攻防工程。透過事前電信引流準備、事中「30 分鐘法規通報與 BGP 清洗」快速處置，以及券商專線的物理隔離保護，臺灣證券交易所方能在遭受極端海量攻擊時，依然穩若磐石，捍衛市場秩序。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『NIST SP 800-61 六階段：準備、偵測、遏止、根除、復原、事後檢討』、『金管會重大資安事件：知悉起 30 分鐘通報』、『BGP Flowspec 電信端高防引流清洗 (Clean Pipe)』、『地端防禦：SYN Cookie、GeoIP、WAAP 無感 PoW 算力挑戰』、『券商交易專線物理隔離 QoS 保障』、『核心系統 RTO ≤ 10 分鐘，事後 3 天繳交 RCA 報告』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>證券 DDoS 特殊性與監理（7分）</strong>：深入點出開盤時間中斷的嚴重金流後果，精確引用 NIST SP 800-61 與 30 分鐘法定通報時限。</li>
  <li><strong>六階段緊急應變重點條列（7分）</strong>：以標準條列架構列舉準備、偵測、遏止、根除、復原與檢討的具體動作與時效目標（RTO ≤ 10 分鐘）。</li>
  <li><strong>證券專線隔離與引流技術（7分）</strong>：提出固網專線 QoS 隔離、BGP Flowspec 引流與 L7 WAAP PoW 算力反制。</li>
  <li><strong>結論（4分）</strong>：總結金融韌性防線價值。</li>
</ul>
            """
        },

        # 5. sec-essay-73: Ransomware 3-2-1 Backup & Network Segmentation Anti-Lateral Movement
        {
            "id": "sec-essay-73",
            "category": "sec",
            "chapter": "第 11 章：業務連續性計畫（BCP）與防勒索軟體防禦",
            "title": "雙重勒索軟體防禦：3-2-1 備份原則進階演化與網路分段阻絕橫向移動實戰",
            "summary": "深入解構勒索軟體雙重勒索（加密+洩漏威脅）、3-2-1-1-0 不可篡改備份原則、網路分段（VLAN/微隔離/封鎖高危通訊埠）、AD Tier 階層隔離，杜絕內網橫向移動實踐。",
            "points": 25,
            "rubric": "1. 雙重勒索威脅型態剖析 (7分)；2. 3-2-1 進階備份防禦架構 (7分)；3. 網路分段與阻斷橫向移動機制表 (7分)；4. 結論 (4分)",
            "question": "勒索軟體（Ransomware）近期多採雙重勒索手段（加密資料＋外洩威脅）。請說明如何運用「3-2-1 備份原則」以及網路分段（Network Segmentation），防止勒索軟體在企業內部橫向移動（Lateral Movement）。",
            "modelAnswer": """
<h4>一、破題：雙重勒索（Double Extortion）之破壞模型</h4>
<p>現代高階勒索軟體集團（如 LockBit、BlackCat）已揚棄單純加密資料的單一模式，全面轉向<strong>「雙重勒索」</strong>：攻擊者滲透內網後，先潛伏數週<strong>竊取核心機敏資料（資料外洩威脅）</strong>，並利用特權惡意<strong>刪除磁碟快照與線上備份資料庫</strong>，最後方才引爆勒索加密。受害者即使想透過備份還原，亦面臨「機密被公佈於暗網」與「備份早遭破壞」的絕境。</p>

<h4>二、3-2-1 備份原則在抗勒索時代的進階演化（3-2-1-1-0 原則）</h4>
<ol>
  <li><strong>3 份資料副本（3 Copies）</strong>：生產資料庫 1 份，加上至少 2 份獨立備份副本。</li>
  <li><strong>2 種不同儲存媒介（2 Different Media）</strong>：如高效全快閃磁碟陣列（快照）搭配離線 LTO 磁帶或雲端物件儲存，避免單一硬體媒介故障或驅動程式共同漏洞。</li>
  <li><strong>1 份異地保存（1 Off-site Copy）</strong>：將備份存放於異地容災中心（板橋與桃園/台中雙活機房），防範區域性物理災難。</li>
  <li><strong>關鍵新增：1 份實體隔離或不可篡改（1 Immutable / Air-Gapped）</strong>：
    - <strong>WORM 合規時限鎖（Write Once, Read Many）</strong>：啟用硬體級 Object Lock，在法定保存期限內（如 30 天），<strong>即使最高 root / admin 權限亦絕對無法刪除或覆寫</strong>；<br>
    - <strong>實體隔離金庫（Air-Gapped Vault）</strong>：平時完全斷網，僅於指定備份時段開啟單向通道同步，杜絕線上勒索軟體直接感染。
  </li>
  <li><strong>關鍵新增：0 錯誤（0 Errors / Clean Room Verification）</strong>：
    定期將備份掛載至獨立的「無毒乾淨隔離室（Clean Room）」進行自動化復原演練，結合 EDR 深度掃描確認備份無休眠惡意代碼，達成 RTO ≤ 10 分鐘、RPO = 0。
</li>
</ol>

<h4>三、網路分段（Network Segmentation）阻絕橫向移動之實務配置</h4>
<ul>
  <li><strong>1. 區域縱深分段 (Zone Segmentation)</strong>：將企業劃分為 DMZ、OA 辦公區、核心交易區、帳務資料庫區、備份管理專區 ；跨網段必須經由次世代防火牆（NGFW）。；將攻擊收斂於最初受害的單一辦公端點， 阻絕黑客自辦公區直通交易撮合與備份主機 。。</li>
  <li><strong>2. 封鎖高危橫向傳播通訊埠</strong>：在所有內部交換器與端點防火牆強制封鎖： - TCP 445 / 139 (SMB) ； - TCP 135 (RPC / WMI) ； - TCP 3389 (RDP) ； - TCP 5985/5986 (WinRM) 。；徹底切斷勒索軟體最常用的自動化蠕蟲擴散管道（如 PsExec、WMI 遠端執行、EternalBlue 漏洞利用）。。</li>
  <li><strong>3. Active Directory 階層隔離 (AD Tier Model)</strong>：- Tier 0 (DC/PKI) ； - Tier 1 (交易主機/資料庫) ； - Tier 2 (員工個人電腦) 。 嚴禁高階帳號登入低階主機！；即使攻擊者攻陷 Tier 2 辦公電腦，記憶體中亦絕無 Tier 0 管理員憑證， 徹底終結 Pass-the-Hash / Mimikatz 抓取明文密碼直攻網域控制站 之慘劇。。</li>
</ul>

<h4>四、結論</h4>
<p>面對雙重勒索，「備份是最後生存底線，而網路分段則是阻斷蔓延的防火牆」。透過「3-2-1-1-0」不可篡改備份保證數據生存，搭配網路微隔離與 AD 階層劃分斬斷橫向移動鏈，證券機構方能從容瓦解勒索軟體的雙重勒索攻勢。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『雙重勒索：加密破壞 + 竊取外洩威脅』、『3-2-1-1-0 備份原則：3份副本、2種媒介、1份異地、1份不可篡改 (WORM/Air-Gap)、0錯誤 (Clean Room自動復原)』、『網路分段：預設隔離辦公區與交易/備份區』、『封鎖橫向擴散通訊埠：SMB 445、RPC 135、RDP 3389、WinRM』、『Active Directory Tier 階層模型阻斷 Pass-the-Hash 憑證竊取』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>雙重勒索威脅本質（7分）</strong>：深入點評現代勒索軟體先偷後殺、專門摧毀在線備份之戰術特徵。</li>
  <li><strong>3-2-1-1-0 進階備份原則（7分）</strong>：條列 3-2-1 基礎，精準點出防勒索核心：1 份不可變儲存（WORM Object Lock）與 0 錯誤驗證。</li>
  <li><strong>網路分段阻絕橫向移動表（7分）</strong>：以條列詳盡列舉區域分段、封鎖 SMB 445/RPC 135 蠕蟲端口，以及 AD Tier 0~2 階層模型防 PtH 憑證橫向劫持。</li>
  <li><strong>結論（4分）</strong>：總結最後底線與物理阻斷之互補成效。</li>
</ul>
            """
        },

        # 6. sec-essay-74: Comprehensive Email Security & Logs
        {
            "id": "sec-essay-74",
            "category": "sec",
            "chapter": "第 8 章：金融釣魚防禦、社交工程與端點深度強化",
            "title": "金融電子郵件安全防護鐵三角（SPF/DKIM/DMARC）、技術過濾規則與鑑別日誌實踐",
            "summary": "深入解構金融郵件社交工程防禦、SPF/DKIM/DMARC 協議防偽冒機制、動態沙盒檢測、Time-of-Click 點擊重導保護、鑑別日誌審計與 SIEM/SOAR 自動化聯動撤回實踐。",
            "points": 25,
            "rubric": "1. 郵件安全鑑別鐵三角原理表 (7分)；2. 前置防禦過濾規則 (沙盒/點擊防護) (7分)；3. 鑑別日誌審計與 SOAR 聯動 (7分)；4. 結論 (4分)",
            "question": "金融業頻傳「社交工程（Social Engineering）」與電子郵件惡意威脅。請申論一個完善的郵件安全防護機制，應包含哪些技術過濾規則與鑑別日誌功能？",
            "modelAnswer": """
<h4>一、破題：電子郵件作為金融 APT 初始存取（Initial Access）之首要管道</h4>
<p>在進階持續性威脅（APT）攻擊中，超過 90% 的攻擊鏈起點源自<strong>魚叉式釣魚郵件（Spear-phishing）</strong>。黑客偽造金管會公文、證交所公告或外部合作券商名義，夾帶惡意巨集或釣魚連結，誘騙內部員工點擊。建構完善的郵件防護機制，必須融合<strong>「郵件來源鑑別鐵三角」</strong>、<strong>「深度內容動態過濾」</strong>與<strong>「全生命週期鑑別日誌審計」</strong>。</p>

<h4>二、郵件來源鑑別鐵三角：SPF、DKIM 與 DMARC</h4>
<ul>
  <li><strong>SPF (Sender Policy Framework)</strong>：網域擁有者於 public DNS 發布 TXT 記錄，宣告合法發送郵件的伺服器 IP 清單。；<strong>實務落地/對策</strong>：收件伺服器比對發信端 SMTP 連線 IP；若不在 SPF 名單內，判定為偽冒 IP（SPF Fail）。。</li>
  <li><strong>DKIM (DomainKeys Identified Mail)</strong>：發件伺服器以 私鑰對郵件標頭與內文進行數位簽章 ，公鑰發布於 DNS TXT 記錄中。；<strong>實務落地/對策</strong>：收件端調用公鑰解密驗證簽章；確保郵件在傳輸過程中 內文與附件未遭中間人（MITM）篡改 。。</li>
  <li><strong>DMARC (Domain-based Message Authentication)</strong>：整合 SPF 與 DKIM，要求寄件者標頭（From:）必須與驗證網域一致（Alignment），並設定強制處置策略。；<strong>實務落地/對策</strong>：強制設定 p=reject （直接拒收阻斷） ；若驗證失敗信件直接丟棄；並接收外部網域回傳之聚合鑑別日誌報告（RUA/RUF）。。</li>
</ul>

<h4>三、前置技術過濾規則與深度威脅防護</h4>
<ol>
  <li><strong>動態虛擬沙盒拆解（Sandbox Detonation）</strong>：
    所有外來郵件附件（如 Office 文件、PDF、ZIP、LNK）進入隔離沙盒環境執行。檢測是否暗藏 VBA 巨集、可執行 Shellcode 或反向連線外部 C2 域名，確認無毒方予放行。
  </li>
  <li><strong>點擊當下時間點保護（Time-of-Click URL Protection）</strong>：
    黑客常於信件發出時放置合法網址繞過靜態檢查，待信件送達數小時後再將網頁切換為釣魚網站。郵件閘道器強制<strong>改寫所有內文超連結（URL Rewriting）</strong>，當員工點擊瞬間，流量先經過安全代理即時分析目標網頁最新態勢與威脅情資，實時阻斷零日釣魚。
  </li>
  <li><strong>內容文字語意分析（Anti-BEC 防變更受款帳戶詐騙）</strong>：
    利用自然語言處理（NLP）分析郵件內文，比對發信者名稱與高階長官（董事長/總經理/CISO）之相似度，防範外觀混淆之「CEO 變臉詐騙（BEC）」。
</li>
</ol>

<h4>四、鑑別日誌功能與 SIEM/SOAR 自動化聯動</h4>
<ol>
  <li><strong>完整日誌欄位留存</strong>：
    郵件閘道器必須至少留存 180 天稽核日誌，欄位涵蓋：<code>Message-ID</code>、連線時間戳、發信 IP、寄件者（Envelope From / Header From）、收件者、SPF/DKIM/DMARC 驗證結果代碼、TLS 握手版本與附件 SHA-256。
  </li>
  <li><strong>SOAR 一鍵全行溯源撤回（Auto-Recall & Purge）</strong>：
    日誌即時串接至 SOC SIEM。一旦威脅情報（IoC）確認某封郵件包含新型惡意木馬，<strong>SOAR Playbook 自動於 1 分鐘內跨所有員工信箱執行 API 查詢並物理刪除該信件</strong>，在其他員工尚未閱讀前消除威脅。
</li>
</ol>

<h4>五、結論</h4>
<p>郵件防禦不能寄託於員工的直覺判斷。透過 SPF/DKIM/DMARC 建立密碼學來源可信度、搭配動態沙盒與 URL 點擊保護，並輔以 SOAR 即時日誌連動撤回，金融機構方能將社交工程風險扼殺於搖籃之中。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『魚叉釣魚為 APT 初始存取 (Initial Access) 90% 來源』、『鑑別鐵三角：SPF (IP白名單)、DKIM (私鑰數位簽名防篡改)、DMARC (對齊強制阻斷 p=reject)』、『動態防護：附件虛擬機沙盒引爆 (Sandbox Detonation) + Time-of-Click URL 重寫即時防護』、『鑑別日誌至少保存 180 天』、『SIEM/SOAR 聯動 1分鐘內全行郵件跨信箱自動撤回 (Auto-Purge)』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>威脅現況與破題（7分）</strong>：深入指出郵件作為初始存取破口之嚴重性，點出三維一體防禦框架。</li>
  <li><strong>鑑別鐵三角原理重點條列（7分）</strong>：以條列逐項剖析 SPF、DKIM、DMARC 之 DNS 原理、驗證機制與 p=reject 阻斷價值。</li>
  <li><strong>前置過濾與日誌 SOAR 實踐（7分）</strong>：詳細說明沙盒動態分析、Time-of-Click 點擊重導防護、180天日誌留存與 SOAR 自動撤回機制。</li>
  <li><strong>結論（4分）</strong>：總結由「被動防範」昇華為「技術自動化防護」之價值。</li>
</ul>
            """
        },

        # 7. sec-essay-75: SQL Injection & XSS, Defense in SDLC
        {
            "id": "sec-essay-75",
            "category": "sec",
            "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
            "title": "SQL 注入（SQLi）與跨網站指令碼（XSS）攻擊剖析及 SDLC 全生命週期防禦實務",
            "summary": "深入解構 OWASP Top 10 核心弱點 SQL Injection 與 XSS 原理與危害、參數化查詢（Prepared Statements）、上下文相關輸出編碼、CSP 標頭，以及 SDLC 設計/開發/測試/維運階段安全分工。",
            "points": 25,
            "rubric": "1. SQL 注入與 XSS 攻擊原理與危害剖析 (7分)；2. 程式開發防禦代碼實踐關鍵對比 (7分)；3. SDLC 各階段資安與開發分工架構 (7分)；4. 結論 (4分)",
            "question": "請解釋何謂 SQL 注入（SQL Injection） 與 跨網站指令碼（XSS） 攻擊？並從軟體開發生命週期（SDLC）的角度，說明程式設計人員與資安人員應如何防範這兩類常見的 OWASP Top 10 弱點？",
            "modelAnswer": """
<h4>一、破題：SQL 注入與 XSS 之底層攻擊原理與金融危害</h4>
<ol>
  <li><strong>SQL 注入（SQL Injection, SQLi）</strong>：
    - <strong>原理</strong>：開發者未對前端傳入之參數進行驗證或過濾，直接以字串拼接（String Concatenation）方式構建 SQL 查詢語句。攻擊者精心構造帶有引號、註解符號或邏輯運算（如 <code>' OR '1'='1'--</code>）之惡意 Payload，改變了 SQL 原本的語意語法結構；<br>
    - <strong>金融危害</strong>：攻擊者能繞過身分認證直接登入主管帳號、整庫脫取投資人帳密與下單記錄，甚至利用 <code>xp_cmdshell</code> 或 UDF 提權獲取資料庫作業系統最高權限。
  </li>
  <li><strong>跨網站指令碼（Cross-Site Scripting, XSS）</strong>：
    - <strong>原理</strong>：應用程式將未受信任的使用者輸入，未經適當編碼即直接輸出至 HTML 頁面中，使惡意 JavaScript 代碼在受害投資人的瀏覽器上被強制執行（分為儲存型 Stored、反射型 Reflected 與 DOM 型 XSS）；<br>
    - <strong>金融危害</strong>：攻擊者劫持使用者的 Session Cookie（偽冒下單身分）、竊取雙因子認證權杖、發起 CSRF 交易或竄改網頁即時行情。
  </li>
</ol>

<h4>二、核心安全編碼實務對比（開發人員責任）</h4>
<ul>
  <li><strong>SQL 注入防禦</strong>：傳統易受駭作法為 String sql = "SELECT * FROM users WHERE acct = '" + input + "'"; (字串拼接)；<strong>安全黃金實踐</strong>為 強制使用參數化查詢（Prepared Statements / Parameterized Query） ： PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE acct = ?"); pstmt.setString(1, input); 資料庫預先編譯 SQL 語法結構，輸入字串僅被視為純文字純量，絕對無法改變指令語法！。</li>
  <li><strong>XSS 跨站腳本防禦</strong>：傳統易受駭作法為 document.write("<div>" + userInput + "</div>"); (直接輸出 HTML)；<strong>安全黃金實踐</strong>為 1. 上下文相關輸出編碼（Context-aware Output Encoding） ：將 <, >, &, ', " 轉義為 HTML 實體； 2. 敏感 Cookie 標記 ： HttpOnly; Secure; SameSite=Strict （禁止 JS 讀取 Document.cookie）； 3. 啟用 CSP 標頭 ： Content-Security-Policy: default-src 'self' 。。</li>
</ul>

<h4>三、SDLC 全生命週期之防禦協同分工（開發 vs 資安）</h4>
<pre><code class="language-text">[1. 需求與設計階段] ──> [2. 開發實作階段] ──> [3. 測試驗證階段] ──> [4. 維運上線階段]
├── 資安制定安全規範    ├── 開發使用參數化     ├── 資安執行 SAST/DAST ├── 邊界 WAF 規則阻斷
└── 架構實施威脅建模    └── 採用 DTO / 輸出編碼 └── 漏洞未清禁止上線(Quality Gate)</code></pre>
<ol>
  <li><strong>需求與設計階段（Shift-Left 安全左移）</strong>：
    - <strong>資安人員</strong>：制定企業安全軟體開發基準，導入 OWASP ASVS 標準，進行威脅建模（Threat Modeling）；<br>
    - <strong>開發人員</strong>：架構設計時評估輸入校驗架構，選用具備自動跳脫特性的現代框架（如 React / Angular 預設防禦 XSS）。
  </li>
  <li><strong>開發與實作階段</strong>：
    - <strong>開發人員</strong>：落實參數化查詢、輸入強型別校驗（正則白名單）、伺服端輸出編碼；<br>
    - <strong>資安人員</strong>：在 IDE 中配置靜態檢查外掛（如 SonarLint），在代碼撰寫當下提供即時修復建議。
  </li>
  <li><strong>測試與驗證階段</strong>：
    - <strong>靜態分析（SAST）</strong>：CI/CD Pipeline 自動調用 SonarQube / Checkmarx 掃描源碼；<br>
    - <strong>動態測試（DAST）與滲透測試</strong>：在 Staging 測試環境使用 OWASP ZAP 模擬黑客發送 SQLi/XSS Payload；<br>
    - <strong>品質閘門（Quality Gate）</strong>：凡發現 High/Critical 漏洞，管線強制阻斷 Build，嚴禁帶病上線。
  </li>
  <li><strong>維運與發布階段</strong>：
    - <strong>資安人員</strong>：在邊界配置 WAAP/WAF 啟用語意分析規則作為縱深防禦；啟用即時漏洞通報回饋修復。
</li>
</ol>

<h4>四、結論</h4>
<p>消滅 SQL 注入與 XSS 絕非依賴事後邊界修補，而是必須深植於「安全軟體開發生命週期（SSDLC）」。透過開發人員掌握參數化與編碼之核心編程規範，輔以資安人員在 CI/CD 品質閘門的自動化工具檢驗，方能從源頭打造無懈可擊的金融應用程式。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『SQL 注入：改變 SQL 語意語法結構，危害為脫庫提權』、『XSS 攻擊：惡意腳本注入瀏覽器執行，危害為 Session 竊取與 CSRF』、『SQLi 唯一黃金正解：參數化查詢 (Prepared Statements)，預編譯將輸入視為純資料』、『XSS 防禦三支柱：上下文輸出編碼 (Output Encoding)、Cookie HttpOnly、CSP 內容安全政策』、『SSDLC 安全左移：IDE 即時掃描 -> CI/CD SAST -> Staging DAST -> 品質閘門一票否決』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>漏洞原理與金融危害（7分）</strong>：深入辨析 SQLi 與 XSS 的注入機制與語法改變本質，條列對金融交易的實質威脅。</li>
  <li><strong>安全代碼實踐重點對比（7分）</strong>：以代碼示例對比字串拼接與 Prepared Statements 預編譯原理，並詳列 XSS 輸出編碼、HttpOnly 與 CSP。</li>
  <li><strong>SDLC 各階段協同架構（7分）</strong>：繪出流程圖，條理分明區分開發與資安在需求、開發、測試（SAST/DAST/Quality Gate）與維運之分工。</li>
  <li><strong>結論（4分）</strong>：總結源頭治理與安全左移之核心理念。</li>
</ul>
            """
        },

        # 8. sec-essay-76: Symmetric vs Asymmetric in TLS/HTTPS
        {
            "id": "sec-essay-76",
            "category": "sec",
            "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
            "title": "對稱加密與非對稱加密深度比較及在 TLS 1.3 / HTTPS 中之協同運作機制",
            "summary": "深入剖析對稱加密（AES-GCM/ChaCha20）與非對稱加密（RSA/ECC/ECDHE）優缺點對比、混成加密（Hybrid Cryptosystem）、X.509 數位憑證認證、金鑰協商與 TLS 1.3 完全前向保密（PFS）協同運作實踐。",
            "points": 25,
            "rubric": "1. 密碼學兩大加密體系核心關鍵對比 (7分)；2. TLS 握手與金鑰協商協同流程 (7分)；3. TLS 1.3 前向保密 (PFS) 與證券交易實作 (7分)；4. 結論 (4分)",
            "question": "API 憑證與傳輸安全在金融科技（FinTech）中至關重要。請比較對稱加密（Symmetric Encryption）與非對稱加密（Asymmetric Encryption）之優缺點，並說明兩者在傳輸層安全性協定（TLS/HTTPS）中如何協同工作。",
            "modelAnswer": """
<h4>一、破題：現代密碼學之兩難與「混成加密（Hybrid Cryptosystem）」</h4>
<p>在金融開放 API（Open API）與證券高頻交易中，傳輸層安全面臨著<strong>「極致效能」</strong>與<strong>「金鑰分發安全」</strong>的根本衝突：對稱加密速度極快但金鑰無法在不安全網路中公開傳輸；非對稱加密完美解決了密鑰安全交換與身分鑑別問題，但計算開銷巨大（慢數百至數千倍）。現代 <strong>TLS 1.3 / HTTPS 協定</strong>巧妙地將二者融合為<strong>「混成加密系統」</strong>，達成了速度與安全的完美平衡。</p>

<h4>二、對稱加密 vs 非對稱加密核心特徵深入對比</h4>
<ul>
  <li><strong>【對稱加密 (Symmetric Encryption)】</strong>：<strong>金鑰結構</strong>：加密與解密使用 同一把共享密鑰（Shared Secret Key） 。；<strong>主流演算法代表</strong>：AES-128/256-GCM、ChaCha20-Poly1305；<strong>加解密效能與資源</strong>：極快（微秒級） ：底層具備 CPU AES-NI 硬體指令集加速，計算開銷極低。；<strong>主要優缺點</strong>：- 優點 ：適合海量資料傳輸； - 缺點 ： 金鑰管理與分發困難 （N 個人通訊需 N(N-1)/2 把金鑰）。。</li>
  <li><strong>【非對稱加密 (Asymmetric Encryption)】</strong>：<strong>金鑰結構</strong>：使用成對的 公開金鑰（Public Key） 與 私有金鑰（Private Key） 。；<strong>主流演算法代表</strong>：RSA-2048/4096、ECDSA、Ed25519、ECDHE；<strong>加解密效能與資源</strong>：較慢（毫秒級） ：涉及大質數因數分解或橢圓曲線點乘等複雜高精度數學運算。；<strong>主要優缺點</strong>：- 優點 ：金鑰分發容易（公鑰可公開發布）、天然支援數位簽章與不可否認性； - 缺點 ：無法用於巨量數據直接加密。。</li>
</ul>

<h4>三、兩者在 TLS 1.3 / HTTPS 協定中之協同運作流程</h4>
<pre><code class="language-text">[客戶端 (瀏覽器/下單App)]                                      [證交所 API 伺服器]
       │                                                              │
       │ ── 1. Client Hello (支援加密套件 + ECDHE 公鑰參數) ─────────> │
       │                                                              │ (伺服器計算 ECDHE 共享金鑰)
       │ <─ 2. Server Hello + X.509 憑證 + 數位簽章 + ECDHE 參數 ───── │
       │                                                              │
(客戶端以 CA 公鑰驗證憑證真實性)                                              │
(客戶端計算出完全相同的對稱 Session Key)                                        │
       │                                                              │
       │ ═══════════ 【TLS 握手完成！握手僅花費 1-RTT】 ═══════════════ │
       │                                                              │
       │ ── 3. 雙向大量交易資料 (全數以 AES-256-GCM 高速對稱加密) ───> │
       │ <─ 4. 行情推播與成交回報 (全數以 AES-256-GCM 高速對稱加密) ── │</code></pre>
<ol>
  <li><strong>身分鑑別階段（非對稱加密：數位簽章）</strong>：
    伺服器出示由合格憑證機構（CA，如 TWCA）簽署之 X.509 憑證。客戶端調用瀏覽器信任根 CA 的公鑰驗證伺服器數位簽章，確認連線對象為真實的證交所伺服器，徹底阻絕中間人（MITM）偽冒。
  </li>
  <li><strong>金鑰協商階段（非對稱加密：ECDHE 密鑰交換）</strong>：
    在 TLS 1.3 中，全面廢除不安全的 RSA 靜態密鑰傳輸，強制採用 <strong>ECDHE（臨時橢圓曲線迪菲-赫爾曼）</strong>。雙方在公開網路上僅交換橢圓曲線點乘參數，各自於本地計算出完全相同的臨時<strong>「對稱工作階段金鑰（Session Key）」</strong>。
  </li>
  <li><strong>資料傳輸階段（對稱加密：AES-256-GCM）</strong>：
    握手確立後，非對稱加密立即功成身退。後續投資人下單指令、行情報價等巨量高頻封包，<strong>全數採用對稱加密（AES-256-GCM 或 ChaCha20-Poly1305）</strong>進行線速加解密，達成微秒級極致吞吐量。
</li>
</ol>

<h4>四、結論：TLS 1.3 完全前向保密（PFS）之金融價值</h4>
<p>透過非對稱 ECDHE 臨時金鑰交換，TLS 1.3 實現了<strong>完全前向保密（Perfect Forward Secrecy, PFS）</strong>：每次連線金鑰隨機生成、用後即焚。即便未來黑客竊取了伺服器長期的私鑰，歷史上已被側錄的所有密文通訊亦永遠無法被破解，為金融 API 與證券交易構築起安全與效能兼備的現代化防禦體系。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『混成加密系統 (Hybrid Cryptosystem) 兼具速度與金鑰分發優勢』、『對稱加密 (AES-256-GCM) 微秒級極快，缺點為金鑰分發難』、『非對稱加密 (RSA/ECC) 支援數位簽章身分鑑別，缺點為計算緩慢』、『TLS 1.3 協同分工：握手階段以非對稱 (X.509憑證防偽冒 + ECDHE協商Session Key)；資料傳輸全以對稱 (AES-GCM) 進行』、『完全前向保密 (PFS)：臨時金鑰用後即焚，長期私鑰外洩歷史密文仍安全』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>混成加密破題（7分）</strong>：深入辨析對稱與非對稱之根本衝突與互補哲學，定義混成加密本質。</li>
  <li><strong>兩大加密體系重點對比（7分）</strong>：以條列從金鑰結構、演算法、效能（AES-NI）、管理複雜度詳盡比較。</li>
  <li><strong>TLS 1.3 協同工作流程（7分）</strong>：繪出 Client Hello / Server Hello 流程圖，詳述 X.509 身分鑑別、ECDHE 金鑰協商與 AES-GCM 大量資料傳輸分工。</li>
  <li><strong>PFS 結論（4分）</strong>：闡述完全前向保密對歷史金融資料保全之關鍵價值。</li>
</ul>
            """
        }
    ]
