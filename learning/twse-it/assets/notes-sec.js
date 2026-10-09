/**
 * 臺灣證券交易所 (TWSE) 招募備考講義 - 資通安全人員 (資訊安全概論)
 * 完整涵蓋 12 大深入核心單元（金融法規治理、ISO 27001:2022/LA、密碼學/HSM、零信任ZTA、DevSecOps、DDoS立體清洗、SOC/SIEM、郵件/端點加固、雲端容器安全、紅藍對抗、BCP防勒索、AI/PQC安全）
 * 每一章節均深度收錄：核心底層原理、實務法遵配置、技術對照矩陣、雙語術語發音、以及【🎯 臺灣證交所年度核心猜題與考點剖析】
 */

const NOTES_SEC = [
  {
    "id": "sec-ch01",
    "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
    "title": "金融資安行動方案 2.0、30 分鐘通報機制與 F-ISAC/CERT/SOC 聯防",
    "summary": "深入剖析金管會金融資安行動方案 2.0、資通安全管理法 A 級機關規範、重大資安事件 30 分鐘通報法規、F-ISAC 跨機構威脅情資共享與軟體物料清單（SBOM）供應鏈治理。",
    "vocab": [
      [
        "Financial Action Plan 2.0",
        "金融資安行動方案 2.0"
      ],
      [
        "Chief Information Security Officer",
        "專責資安長 (CISO)"
      ],
      [
        "Financial Information Sharing and Analysis Center",
        "金融資安資訊分享與分析中心 (F-ISAC)"
      ],
      [
        "Computer Emergency Response Team",
        "電腦緊急應變小組 (F-CERT)"
      ],
      [
        "Security Operations Center",
        "資安維運中心 (F-SOC)"
      ],
      [
        "Software Bill of Materials",
        "軟體物料清單 (SBOM)"
      ],
      [
        "Business Impact Analysis",
        "營運衝擊分析 (BIA)"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Financial Action Plan 2.0', this)\">Financial Action Plan 2.0 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Chief Information Security Officer', this)\">CISO 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('F-ISAC', this)\">F-ISAC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('F-CERT', this)\">F-CERT 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('F-SOC', this)\">F-SOC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Software Bill of Materials', this)\">SBOM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('STIX and TAXII', this)\">STIX / TAXII 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Business Impact Analysis', this)\">BIA 🔊</button>\n  </div>\n</div>\n\n<h2>1. 金融資安行動方案 2.0 四大核心構面與實務要求</h2>\n<p>金融監督管理委員會（金管會）推動之<strong class=\"en-term\" data-speak=\"Financial Action Plan 2.0\">『金融資安行動方案 2.0』<button class=\"spk-btn\" type=\"button\" aria-label=\"朗讀\">🔊</button></strong>，為臺灣金融市場與關鍵基礎設施之頂層防護藍圖，聚焦四大核心構面：</p>\n<ul>\n  <li><strong>深化資安治理（<span class=\"en-term\" data-speak=\"Governance\">Governance<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>：\n    推行金控、銀行及一定規模以上之證券商設置具備實質資安背景之專責<strong class=\"en-term\" data-speak=\"Chief Information Security Officer\">資安長（CISO）<button class=\"spk-btn\" type=\"button\">🔊</button></strong>，成立獨立於資訊（IT）部門的資安專責部門。落實董事會資安督導責任，並建立健全的<strong>「資安三道防線」</strong>：第一線業務與資訊維運自律防護、第二線風控與法遵合規監控、第三線內部稽核獨立查核。\n  </li>\n  <li><strong>強化資安聯防（<span class=\"en-term\" data-speak=\"Joint Defense\">Joint Defense<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>：\n    全方位對接金融三中心體系：\n    1. <strong class=\"en-term\" data-speak=\"F-ISAC\">F-ISAC（金融資安資訊分享與分析中心）<button class=\"spk-btn\" type=\"button\">🔊</button></strong>：負責橫向威脅情資即時分享，支援 <code class=\"en-code\" data-speak=\"STIX\">STIX</code> 與 <code class=\"en-code\" data-speak=\"TAXII\">TAXII</code> 標準協定自動化傳遞威脅指標（IoC）；<br>\n    2. <strong class=\"en-term\" data-speak=\"F-CERT\">F-CERT（金融電腦緊急應變小組）<button class=\"spk-btn\" type=\"button\">🔊</button></strong>：提供重大資安事件現場技術鑑識、逆向工程與應變支援；<br>\n    3. <strong class=\"en-term\" data-speak=\"F-SOC\">F-SOC（金融資安維運中心）<button class=\"spk-btn\" type=\"button\">🔊</button></strong>：集中監控全市場資安異常態勢，主動預警分散式威脅。\n  </li>\n  <li><strong>提升資安監韌（<span class=\"en-term\" data-speak=\"Cyber Resilience\">Cyber Resilience<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>：\n    要求證券期貨業核心交易系統（如撮合、行情、結算）全面推行<strong class=\"en-term\" data-speak=\"Business Impact Analysis\">營運衝擊分析（BIA）<button class=\"spk-btn\" type=\"button\">🔊</button></strong>，嚴格訂定復原時間目標 <code class=\"en-code\" data-speak=\"Recovery Time Objective\">RTO &le; 10 分鐘</code>、復原點目標 <code class=\"en-code\" data-speak=\"Recovery Point Objective\">RPO = 0</code>（資料零遺失）。每年強制辦理無預警 DDoS 與勒索軟體攻防實兵演練。\n  </li>\n  <li><strong>建構資安文化（<span class=\"en-term\" data-speak=\"Security Culture\">Security Culture<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>：\n    常態化辦理全員防社交工程釣魚郵件演練（不合格者強制再培訓）、激勵專業資安證照（CISSP、CISM、ISO 27001 LA）、健全供應鏈安全合規審查。\n  </li>\n</ul>\n\n<h2>2. 證券期貨業重大資安事件「30 分鐘法定通報」作業程序</h2>\n<div class=\"callout-box\">\n  <div class=\"callout-title\">🚨 證券期貨業重大資安事件判定標準與法定通報責任</div>\n  <p>依據「證券期貨業資通安全聯合防防應變作業程序」與主管機關規範，凡符合下列情事之一者，即構成<strong>重大資安事件（Level 3/4 重大等級）</strong>：<br>\n  1. <strong>核心業務系統中斷</strong>：核心交易系統（委託下單、即時撮合、行情廣播、結算交割）遭受網路阻斷、軟硬體故障或勒索感染，服務中斷達 <strong>10 分鐘以上</strong>。<br>\n  2. <strong>機密資料外洩</strong>：遭受未經授權存取，導致大量投資人核心個人資料、電子交易憑證或未公開重大商業機密外流。<br>\n  3. <strong>惡意勒索癱瘓</strong>：主機遭受勒索軟體（Ransomware）加密破壞，已實質影響業務運行或擴散至內網其他節點。<br>\n  <strong>【通報時效與程序】</strong>：<br>\n  受害機構自<strong>「知悉（Awareness）」</strong>起，<strong>必須於 30 分鐘內</strong>向主管機關（金管會證期局）及 F-ISAC 完成初次通報；後續每 2 小時或重大進展時需持續更新處置狀態；事件平息後 3 個工作天內，必須提交包含根本原因分析（RCA）與矯正措施之完整檢討報告。</p>\n</div>\n\n<h2>3. 供應鏈資安風險治理與軟體物料清單（SBOM）實踐</h2>\n<p>近年金融體系多次遭受外包資訊廠商中繼滲透（如太陽風 SolarWinds 事件、Log4j 漏洞）。證券期貨業必須落實全生命週期供應鏈安全管制：</p>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">供應鏈管理階段</th>\n      <th style=\"padding:10px;\">核心管制要求與查核手法</th>\n      <th style=\"padding:10px;\">證交所實務標準</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">事前評選 (Pre-procurement)</td>\n      <td style=\"padding:8px;\">廠商資安成熟度評級、ISO 27001 認證查驗、實地資安查訪</td>\n      <td style=\"padding:8px;\">合約明訂資安賠償責任、資安通報義務及禁止轉包機密模組</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">事中維運 (Operation)</td>\n      <td style=\"padding:8px;\">遠端維護管理、特權帳號雙人覆核、全程堡壘機連線錄影</td>\n      <td style=\"padding:8px;\">嚴禁廠商設置未受控之 AnyDesk/TeamViewer 或常態性 VPN</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">交付稽核 (Delivery & Audit)</td>\n      <td style=\"padding:8px;\"><strong>軟體物料清單（<span class=\"en-term\" data-speak=\"SBOM\">SBOM<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>交付、源碼安全檢測（SAST）、滲透測試報告</td>\n      <td style=\"padding:8px;\">要求交付 <code class=\"en-code\" data-speak=\"SPDX\">SPDX</code> 或 <code class=\"en-code\" data-speak=\"CycloneDX\">CycloneDX</code> 格式 SBOM，開源零日漏洞 15 分鐘全系統清查</td>\n    </tr>\n  </table>\n</div>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】金管會金融資安行動方案 2.0 與 30 分鐘重大資安事件聯防處置實務</h4>\n  <p><strong>題目</strong>：金融監督管理委員會大力推行「金融資安行動方案 2.0」，強化關鍵基礎設施營運韌性。試說明該行動方案之四大核心構面與主要實施重點；並依據「證券期貨業資通安全聯合防防應變作業程序」，申論重大資安事件之判定標準、30 分鐘法定通報流程，以及受駭機構如何協同 F-ISAC/F-CERT/F-SOC 展開跨機構聯防處置？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>行動方案 2.0 四大構面（8分）</strong>：精準答出深化治理（專責 CISO、三道防線）、強化聯防（F-ISAC/CERT/SOC 整合）、提升監韌（BIA 業務衝擊分析、RTO&le;10分/RPO=0、實兵演練）、建構文化（社交工程演練、資安證照）。<br>\n    2. <strong>重大資安事件三項門檻（7分）</strong>：核心交易中斷 10 分鐘以上、大量投資人個資或憑證外洩、勒索軟體感染已影響營運。<br>\n    3. <strong>30 分鐘法定通報與聯防（10分）</strong>：知悉後 30 分鐘內向金管會證期局及 F-ISAC 初報，後續每 2 小時更新，3 工作天提交 RCA 結報。透過 F-ISAC 共享 IoC 阻斷全市場相同特徵攻擊，F-CERT 介入取證，F-SOC 全局監控。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch02",
    "chapter": "第 2 章：資安標準與控制框架（ISO 27001:2022 與 ISO 27001 LA 稽核實務）",
    "title": "ISO/IEC 27001:2022 核心條文、Annex A 93項控制措施與 ISO 27001 LA 主導稽核實務",
    "summary": "深入解構 ISO 27001:2022 Clauses 4~10 高階架構、四大主題 93 項控制措施、SoA 適用性聲明、ISO 19011:2018 主導稽核實務（Stage 1/2、客觀證據三要素、Major/Minor NC 判定、RCA 矯正措施），以及證交所會考猜題重點。",
    "vocab": [
      [
        "Statement of Applicability",
        "適用性聲明書 (SoA)"
      ],
      [
        "High Level Structure",
        "高階架構 (HLS)"
      ],
      [
        "Objective Evidence",
        "客觀證據"
      ],
      [
        "Major Nonconformity",
        "重大不符合 (Major NC)"
      ],
      [
        "Minor Nonconformity",
        "次要不符合 (Minor NC)"
      ],
      [
        "Opportunity for Improvement",
        "改善機會 (OFI)"
      ],
      [
        "Root Cause Analysis",
        "根本原因分析 (RCA)"
      ],
      [
        "Corrective Action",
        "矯正措施 (Clause 10.1)"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Statement of Applicability', this)\">SoA 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('High Level Structure', this)\">HLS 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Lead Auditor', this)\">Lead Auditor 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Objective Evidence', this)\">Objective Evidence 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Major Nonconformity', this)\">Major NC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Minor Nonconformity', this)\">Minor NC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Root Cause Analysis', this)\">RCA 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Threat Intelligence', this)\">Threat Intelligence 🔊</button>\n  </div>\n</div>\n\n<h2>1. ISO/IEC 27001:2022 高階架構（HLS Clauses 4~10）與 PDCA 循環</h2>\n<p>ISO/IEC 27001:2022 遵循 Harmonized Structure（高階架構 HLS），由 <strong>Clauses 4 至 10</strong> 構成核心管理要求：</p>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">條文章節</th>\n      <th style=\"padding:10px;\">核心要求名稱</th>\n      <th style=\"padding:10px;\">PDCA 階段</th>\n      <th style=\"padding:10px;\">證交所實務與主導稽核查核重點 (Audit Focus)</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 4</td>\n      <td style=\"padding:8px;\">組織背景 (Context)</td>\n      <td style=\"padding:8px;\">Plan (規劃)</td>\n      <td style=\"padding:8px;\">界定內外部議題（金融資安行動方案 2.0、資安法）、利害關係人要求，以及明確界定 <strong>ISMS 適用範圍書（Scope）</strong>（涵蓋核心撮合、行情、結算交割系統）。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 5</td>\n      <td style=\"padding:8px;\">領導力 (Leadership)</td>\n      <td style=\"padding:8px;\">Plan (規劃)</td>\n      <td style=\"padding:8px;\">高階管理階層（董事會、總經理）資安承諾、簽署並頒布資訊安全政策、指派專責資安長（CISO）與職責分工（RACI 矩陣）。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 6</td>\n      <td style=\"padding:8px;\">規劃 (Planning)</td>\n      <td style=\"padding:8px;\">Plan (規劃)</td>\n      <td style=\"padding:8px;\">資安風險評鑑（Risk Assessment）與風險處理；產出<strong>適用性聲明書（<span class=\"en-term\" data-speak=\"Statement of Applicability\">SoA<button class=\"spk-btn\" type=\"button\">🔊</button></span>）</strong>；訂定可量化資安目標。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 7</td>\n      <td style=\"padding:8px;\">支援 (Support)</td>\n      <td style=\"padding:8px;\">Do (執行)</td>\n      <td style=\"padding:8px;\">資源配置、全員勝任能力（Competence，資安證照培訓）、資安意識演練、文件化資訊管制（版本控管、審核簽章）。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 8</td>\n      <td style=\"padding:8px;\">營運 (Operation)</td>\n      <td style=\"padding:8px;\">Do (執行)</td>\n      <td style=\"padding:8px;\">落實風險處理措施、變更管理（Change Management）、委外供應鏈資安運作管制。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 9</td>\n      <td style=\"padding:8px;\">績效評估 (Performance)</td>\n      <td style=\"padding:8px;\">Check (檢核)</td>\n      <td style=\"padding:8px;\">監控與量測（資安 KPI/KRI）；<strong>內部稽核（Clause 9.2，獨立公正）</strong>；<strong>管理階層審查會議（Clause 9.3，每年定期由最高首長主持）</strong>。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Clause 10</td>\n      <td style=\"padding:8px;\">改善 (Improvement)</td>\n      <td style=\"padding:8px;\">Act (改善)</td>\n      <td style=\"padding:8px;\"><strong>不符合事項與矯正措施（Clause 10.1）</strong>；持續改善（Clause 10.2）ISMS 有效性。</td>\n    </tr>\n  </table>\n</div>\n\n<h2>2. Annex A 四大主題 93 項控制措施與 11 項全新控制項</h2>\n<p>2022 版由舊版 14 個領域 114 項整併為<strong>四大主題（Themes）共 93 項控制措施</strong>：A.5 組織（37項）、A.6 人員（8項）、A.7 實體（14項）、A.8 技術（34項）。</p>\n<div class=\"callout-box\">\n  <div class=\"callout-title\">🌟 ISO 27001:2022 必考 11 項全新控制項（LA 考試與證交所招募核心熱點）</div>\n  <p>1. <code class=\"en-code\" data-speak=\"Threat Intelligence\">A.5.7 威脅情資 (Threat Intelligence)</code>：收集外部威脅情報，對接 F-ISAC 情資聯防。<br>\n  2. <code class=\"en-code\" data-speak=\"Information security for use of cloud services\">A.5.23 雲端服務資安 (Cloud services security)</code>：公有雲/混合雲存取與退場安全規範。<br>\n  3. <code class=\"en-code\" data-speak=\"ICT readiness for business continuity\">A.5.30 業務營運持續之 ICT 整備度 (ICT readiness for BC)</code>：落實 RTO/RPO 雙活備援架構。<br>\n  4. <code class=\"en-code\" data-speak=\"Physical security monitoring\">A.7.4 實體安全監視 (Physical security monitoring)</code>：機房關鍵出入口安裝 CCTV 與入侵警報。<br>\n  5. <code class=\"en-code\" data-speak=\"Configuration management\">A.8.9 組態管理 (Configuration management)</code>：建立軟硬體安全基準（Baseline）並監控防漂移。<br>\n  6. <code class=\"en-code\" data-speak=\"Information deletion\">A.8.10 資訊刪除 (Information deletion)</code>：資料生命週期結束後執行安全抹除或消磁。<br>\n  7. <code class=\"en-code\" data-speak=\"Data masking\">A.8.11 資料遮蔽 (Data masking)</code>：客戶敏感資料動態去識別化或遮罩。<br>\n  8. <code class=\"en-code\" data-speak=\"Data leakage prevention\">A.8.12 資料外洩防護 (Data leakage prevention, DLP)</code>：監控並攔截機密外傳。<br>\n  9. <code class=\"en-code\" data-speak=\"Monitoring activities\">A.8.16 監控活動 (Monitoring activities)</code>：SIEM/UEBA 收集分析異常行為日誌。<br>\n  10. <code class=\"en-code\" data-speak=\"Web filtering\">A.8.23 網路篩選 (Web filtering)</code>：限制存取惡意釣魚或高風險網站。<br>\n  11. <code class=\"en-code\" data-speak=\"Secure coding\">A.8.28 安全編碼 (Secure coding)</code>：SSDLC 軟體開發導入 SAST/DAST 與 OWASP 規範。</p>\n</div>\n\n<h2>3. ISO 19011:2018 主導稽核員（Lead Auditor）實務與判定準則</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">稽核階段 / 發現等級</th>\n      <th style=\"padding:10px;\">定義與查核核心重點</th>\n      <th style=\"padding:10px;\">證交所實務案例</th>\n      <th style=\"padding:10px;\">處置要求與發證影響</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Stage 1 稽核 (文件審查)</td>\n      <td style=\"padding:8px;\">評估文件體系健全度與現場查核準備度（Readiness）。查核 Scope、政策、SoA、風險評鑑、<strong>內稽與管審會議紀錄</strong>。</td>\n      <td style=\"padding:8px;\">若內部稽核（9.2）或管理階層審查（9.3）未完成，<strong>嚴禁進入 Stage 2！</strong></td>\n      <td style=\"padding:8px;\">開立關注事項（Areas of Concern），限期補正。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">Stage 2 稽核 (現場查核)</td>\n      <td style=\"padding:8px;\">驗證控制措施是否獲得實質有效運作。採樣客觀證據（訪談、文件記錄、實作觀察）。</td>\n      <td style=\"padding:8px;\">抽查特權帳號工單、防火牆規則、日誌留存、機房實體刷卡門禁。</td>\n      <td style=\"padding:8px;\">判定稽核發現：Major NC、Minor NC 或 OFI。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700; color:var(--danger);\">重大不符合 (Major NC)</td>\n      <td style=\"padding:8px;\">1. 未滿足核心條款要求；2. 控制項<strong>系統性崩潰失效</strong>；3. 造成重大資安危害；4. 累積多項同類 Minor NC。</td>\n      <td style=\"padding:8px;\">撮合系統發版完全未經變更管理流程測試審批；正式資料庫備份全然未加密且從未演練還原。</td>\n      <td style=\"padding:8px; font-weight:700; color:var(--danger);\"><strong>直接阻擋發證！</strong>受稽方須於 90 天內完成 RCA 與矯正，稽核員<strong>實地回訪複查</strong>合格後始得結案。</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700; color:var(--accent-gold);\">次要不符合 (Minor NC)</td>\n      <td style=\"padding:8px;\">單一、偶發性作業疏漏，未形成體系性故障，未危及整體 ISMS 有效性。</td>\n      <td style=\"padding:8px;\">抽查 30 份新進員工保密協議，1 人漏未歸檔；抽查 20 台伺服器，1 台備用機病毒碼落後 3 天。</td>\n      <td style=\"padding:8px;\">不阻擋發證，30~60 天內提交矯正措施計畫（CAP）與佐證，書面審查結案。</td>\n    </tr>\n  </table>\n</div>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】ISO 27001:2022 控制措施升級與 ISO 19011 主導稽核實務處置</h4>\n  <p><strong>題目</strong>：國際標準 ISO/IEC 27001:2022 帶來大幅度架構革新。試詳述 Annex A 四大主題中新增之控制措施（列舉至少 5 項並說明在證券交易所之實踐）；主導稽核員（Lead Auditor）赴現場執行 Stage 2 稽核時，如何採集「客觀證據三要素」？若發現生產環境資料庫備份檔未落實加密且未做還原測試，應判定為何種不符合等級？請詳述其判定理由與受稽方應執行之 RCA 四步矯正措施閉環。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>新增控制措施（8分）</strong>：精確列出 A.5.7 威脅情資、A.5.30 ICT 營運持續整備度、A.8.9 組態管理、A.8.12 DLP、A.8.28 安全編碼等，並結合撮合系統與資料庫落地。<br>\n    2. <strong>客觀證據三要素（5分）</strong>：人員訪談（Interviews）、文件記錄審閱（Documents & Records）、現場實作觀察（Observations），不可憑主觀臆測。<br>\n    3. <strong>不符合等級判定（6分）</strong>：判定為<strong>重大不符合（Major NC）</strong>！理由為核心交易資料庫備份涉及可用性與機密性底層保障，未加密且未演練還原屬於控制措施「系統性失效」，直接危及組織營運持續。<br>\n    4. <strong>RCA 四步矯正措施閉環（6分）</strong>：暫時遏阻處置（立即加密現有備份檔並排定緊急還原驗證）&rarr; 根本原因分析（5-Why 法挖掘政策與工單監控漏洞）&rarr; 擬定並執行矯正措施（修正備份政策、導入自動化備份驗證工具）&rarr; 有效性驗證（追蹤 3 個月運行記錄確認不再犯）。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch03",
    "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
    "title": "對稱/非對稱演算法、數位簽章法、HSM 部署與 TLS 1.3 前向保密",
    "summary": "深入剖析 AES-GCM、ECC/RSA 數學原理、SHA-256 雜湊、金融硬體安全模組（HSM FIPS 140-3）、X.509 憑證鏈查驗、TLS 1.3 完全前向保密（PFS）與後量子密碼學（PQC）。",
    "vocab": [
      [
        "Hardware Security Module",
        "硬體安全模組 (HSM)"
      ],
      [
        "Public Key Infrastructure",
        "公開金鑰基礎設施 (PKI)"
      ],
      [
        "Perfect Forward Secrecy",
        "完全前向保密 (PFS)"
      ],
      [
        "Non-repudiation",
        "不可否認性"
      ],
      [
        "Zeroization",
        "物理拆解零化機制"
      ],
      [
        "Post-Quantum Cryptography",
        "後量子密碼學 (PQC)"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Hardware Security Module', this)\">HSM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Public Key Infrastructure', this)\">PKI 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Perfect Forward Secrecy', this)\">PFS 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Non-repudiation', this)\">Non-repudiation 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Zeroization', this)\">Zeroization 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Post-Quantum Cryptography', this)\">PQC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Elliptic Curve Cryptography', this)\">ECC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Key Management Interoperability Protocol', this)\">KMIP 🔊</button>\n  </div>\n</div>\n\n<h2>1. 現代金融密碼學演算法體系全景對比</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">分類</th>\n      <th style=\"padding:10px;\">主流演算法</th>\n      <th style=\"padding:10px;\">密鑰長度推薦</th>\n      <th style=\"padding:10px;\">金融核心應用情境</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">對稱式加密 (Symmetric)</td>\n      <td style=\"padding:8px;\"><code class=\"en-code\" data-speak=\"AES-GCM\">AES-256-GCM</code>、<code class=\"en-code\" data-speak=\"ChaCha20-Poly1305\">ChaCha20-Poly1305</code></td>\n      <td style=\"padding:8px;\">256 bits</td>\n      <td style=\"padding:8px;\">交易資料庫靜態儲存加密（TDE）、TLS 傳輸數據本體加密</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">非對稱式加密 (Asymmetric)</td>\n      <td style=\"padding:8px;\"><code class=\"en-code\" data-speak=\"RSA\">RSA-4096</code>、<code class=\"en-code\" data-speak=\"ECDSA\">ECC (ECDSA P-256, Ed25519)</code></td>\n      <td style=\"padding:8px;\">RSA &ge; 2048b, ECC &ge; 256b</td>\n      <td style=\"padding:8px;\">證券下單電子憑證簽署、TLS 金鑰協商交換</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">單向雜湊函數 (Hash)</td>\n      <td style=\"padding:8px;\"><code class=\"en-code\" data-speak=\"SHA-256\">SHA-256</code>, <code class=\"en-code\" data-speak=\"SHA-384\">SHA-384</code>, <code class=\"en-code\" data-speak=\"SHA-3\">SHA-3</code></td>\n      <td style=\"padding:8px;\">摘要 &ge; 256 bits</td>\n      <td style=\"padding:8px;\">訊息完整性校驗、數位簽章訊息摘要生成</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">訊息鑑別碼 (MAC)</td>\n      <td style=\"padding:8px;\"><code class=\"en-code\" data-speak=\"HMAC-SHA256\">HMAC-SHA256</code>, <code class=\"en-code\" data-speak=\"GMAC\">GMAC</code></td>\n      <td style=\"padding:8px;\">256 bits Key</td>\n      <td style=\"padding:8px;\">API 請求防篡改驗證、金融 FIX 協定通訊身分認證</td>\n    </tr>\n  </table>\n</div>\n\n<h2>2. 數位簽章不可否認性與 X.509 憑證鏈運作流程</h2>\n<p>依據臺灣《數位簽章法》，經合法憑證機構（CA，如臺灣網路認證 TWCA）簽發之憑證具有法律推定為本人親簽之不可否認性：</p>\n<pre><code class=\"language-text\">【下單端簽署】\n下單封包 (Order Payload) ──> SHA-256 雜湊 ──> 交易摘要 (Digest)\n                                                   │\n客戶端本地私鑰 (Client Private Key) ──────────────┴──> 數位簽章 (Signature)\n\n【證交所撮合端驗證】\n1. 數位簽章 ──> 客戶公鑰 (Public Key) ──> 解密取得摘要 A\n2. 下單封包 ──> SHA-256 計算 ───────────> 取得摘要 B\n3. 嚴格比對 A == B (確認資料零篡改且確為本人簽署)\n4. X.509 憑證信任鏈追溯驗證 (Root CA、有效期限、OCSP 即時撤銷狀態查驗)</code></pre>\n\n<h2>3. 金融硬體安全模組（HSM）防護與 TLS 1.3 前向保密</h2>\n<ul>\n  <li><strong>FIPS 140-3 Level 3 / Level 4 認證</strong>：根金鑰嚴禁存於普通記憶體。HSM 具備防探針、防外殼拆卸之實體偵測電路。一旦遭受物理暴力拆解，微秒級自動啟動電容放電，<strong>瞬間永久抹除內部所有私鑰（Zeroization 零化機制）</strong>。</li>\n  <li><strong>TLS 1.3 完全前向保密（PFS, Perfect Forward Secrecy）</strong>：強制使用 ECDHE 臨時密鑰協商。每次連線產生獨立之臨時對話金鑰，即便未來伺服器長期私鑰洩漏，攻擊者過去側錄的歷史封包依然無法被解密。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】證券下單電子憑證簽章驗證、HSM 安全性與後量子密碼遷移</h4>\n  <p><strong>題目</strong>：臺灣證券交易所為保障投資人權益與市場交易秩序，全面強制下單交易具備不可否認性（Non-repudiation）。請以密碼學原理詳述數位簽章與 X.509 憑證鏈之簽署與驗證流程；闡明硬體安全模組（HSM）如何透過防拆零化（Zeroization）保障根金鑰安全；並分析量子計算（Shor 演算法）對現行 RSA/ECC 體系之威脅，說明金融機構應如何推動「加密敏捷性（Crypto-Agility）」？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>數位簽章運作原理（8分）</strong>：寫出 SHA-256 摘要生成、私鑰簽章、公鑰解密核對摘要、OCSP 憑證撤銷查詢，滿足不可否認性與完整性。<br>\n    2. <strong>HSM 物理防護與零化機制（7分）</strong>：FIPS 140-3 Level 3/4 認證、防探針電路、拆殼即刻觸發零化抹除（Zeroization）、金鑰不出安全邊界。<br>\n    3. <strong>後量子威脅與加密敏捷性（10分）</strong>：說明 Shor 演算法多項式時間破解離散對數與質因數分解、Store Now Decrypt Later 威脅、NIST 最新標準（ML-KEM / ML-DSA）、金融雙重簽章混合過渡模式。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch04",
    "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
    "title": "NIST SP 800-207 核心原則、FIDO2 抗釣魚驗證與 PAM 堡壘機實務",
    "summary": "深入解構 NIST 零信任架構 PDP/PEP 模型、FIDO2 / WebAuthn 抗釣魚無密碼驗證、OAuth 2.0 / OIDC 授權，以及特權存取管理（PAM）堡壘機防護。",
    "vocab": [
      [
        "Zero Trust Architecture",
        "零信任架構 (ZTA)"
      ],
      [
        "Policy Decision Point",
        "原則決定點 (PDP)"
      ],
      [
        "Policy Enforcement Point",
        "原則強制執行點 (PEP)"
      ],
      [
        "Phishing-resistant MFA",
        "抗釣魚多因子鑑別"
      ],
      [
        "Privileged Access Management",
        "特權存取管理 (PAM)"
      ],
      [
        "Micro-segmentation",
        "網路微隔離"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Zero Trust Architecture', this)\">Zero Trust 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Policy Decision Point', this)\">PDP 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Policy Enforcement Point', this)\">PEP 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('FIDO2 WebAuthn', this)\">FIDO2 / WebAuthn 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Privileged Access Management', this)\">PAM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Pass-the-Hash', this)\">Pass-the-Hash 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Origin Binding', this)\">Origin Binding 🔊</button>\n  </div>\n</div>\n\n<h2>1. 零信任架構（ZTA）三大核心原則（NIST SP 800-207）</h2>\n<p>依據 NIST SP 800-207，零信任架構徹底揚棄過去「內網即安全」的城堡護城河模型，樹立三大鐵律：</p>\n<ul>\n  <li><strong>Never Trust, Always Verify（絕不信任，始終驗證）</strong>：無論存取來源來自企業內部局域網或外部網路，一律視為不信任網路，每次連線皆必須實施多維度動態身分與設備健康度驗證。</li>\n  <li><strong>Least Privilege Access（最小特權原則）</strong>：依據身分角色（RBAC）與情境屬性（ABAC），僅賦予完成當前任務所需的最小權限，實施即時按需賦權（Just-In-Time Access）。</li>\n  <li><strong>Assume Breach（假定已遭入侵）</strong>：預設內網早已潛伏攻擊者，全面實施網路微隔離（Micro-segmentation），限制橫向移動（Lateral Movement）爆炸半徑。</li>\n</ul>\n\n<h2>2. 零信任控制架構：PDP 與 PEP</h2>\n<pre><code class=\"language-text\">  連線端點 (Subject / Client)\n           │\n           ▼\n┌─────────────────────────┐\n│ 原則強制執行點 (PEP)     │ <─── 攔截連線請求，執行放行或阻斷\n└──────────┬──────────────┘\n           │ 諮詢決策\n           ▼\n┌────────────────────────────────────────────────────────┐\n│ 原則決定點 (PDP, Policy Decision Point)                │\n│   ├── 原則引擎 (Policy Engine, PE): 綜合風險評估計算   │\n│   └── 原則管理員 (Policy Administrator, PA): 發布指令  │\n└──────────────────────────┬─────────────────────────────┘\n                           │ 整合情資 (身分庫/設備健康/威脅情報)\n                           ▼\n             企業受保護核心資產 (Enterprise Resources)</code></pre>\n\n<h2>3. FIDO2 / WebAuthn 抗釣魚無密碼驗證技術原理</h2>\n<p>傳統簡訊 SMS OTP 與 Authenticator 驗證碼容易被逆向代理釣魚網站（如 Evilginx2）即時竊取。<strong>FIDO2 WebAuthn</strong> 實現真正的抗釣魚（Phishing-resistant）防禦：</p>\n<ul>\n  <li><strong>私鑰封裝於硬體晶片</strong>：私鑰安全封裝於安全晶片（YubiKey、TPM 2.0、Secure Enclave），永不離開實體設備。</li>\n  <li><strong>來源網域綁定（Origin Binding）</strong>：瀏覽器在簽署挑戰碼（Challenge）時，強制將當前瀏覽器網址（如 <code>twse.com.tw</code>）納入簽章雜湊。若受害者誤入偽冒網站（如 <code>twse-login.com</code>），網域不符簽章自動失效，攻擊者無法使用攔截之憑證。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】NIST 零信任架構落地、抗釣魚 FIDO2 與特權 PAM 堡壘機規劃</h4>\n  <p><strong>題目</strong>：傳統以網路周邊防火牆為邊界之安全模型，難以防禦供應鏈滲透與內網橫向移動。請說明 NIST SP 800-207 零信任架構之三大原則與 PDP/PEP 決策機制；分析 FIDO2/WebAuthn 為何能抵禦 Evilginx2 逆向代理釣魚；並為證交所規劃一套結合 PAM 堡壘機與 Active Directory 階層式模型（Tier Model）之特權存取防禦體系。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>零信任三大原則與 PDP/PEP（8分）</strong>：Never Trust Always Verify、Least Privilege、Assume Breach；說明 Policy Engine (PE)、Policy Administrator (PA) 與 PEP 交互流程。<br>\n    2. <strong>FIDO2 抗釣魚原理（8分）</strong>：非對稱密碼學、私鑰不出硬體 TPM/Token、Origin Binding 瀏覽器網域雜湊校驗機制。<br>\n    3. <strong>PAM 堡壘機與 AD Tier 模型（9分）</strong>：堡壘機動態 OTP、雙人覆核、全指令錄影；AD Tier 0 (DC/PKI)、Tier 1 (Server/DB)、Tier 2 (Workstation) 嚴格隔離，阻絕 Pass-the-Hash / Mimikatz 憑證竊取。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch05",
    "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
    "title": "OWASP Top 10:2021 深度防護、DevSecOps 安全左移與 API 安全",
    "summary": "解析 OWASP Top 10 核心弱點成因與防禦（SQLi/XSS/SSRF/IDOR）、DevSecOps 安全左移流水線（SAST/DAST/SCA/IAST），以及 OWASP API Security Top 10 權限治理。",
    "vocab": [
      [
        "Broken Access Control",
        "權限控制失效 (A01)"
      ],
      [
        "Server-Side Request Forgery",
        "伺服器端請求偽造 (SSRF)"
      ],
      [
        "Static Application Security Testing",
        "靜態應用安全測試 (SAST)"
      ],
      [
        "Dynamic Application Security Testing",
        "動態應用安全測試 (DAST)"
      ],
      [
        "Software Composition Analysis",
        "軟體成分分析 (SCA)"
      ],
      [
        "Prepared Statements",
        "參數化查詢防注入"
      ],
      [
        "Quality Gate",
        "CI/CD 安全品質閾門"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Broken Access Control', this)\">A01 Access Control 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Injection', this)\">Injection (SQLi) 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Server-Side Request Forgery', this)\">SSRF 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('SAST', this)\">SAST 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('DAST', this)\">DAST 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('SCA', this)\">SCA 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Quality Gate', this)\">Quality Gate 🔊</button>\n  </div>\n</div>\n\n<h2>1. OWASP Top 10:2021 核心高風險漏洞剖析與防禦</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">OWASP 排名</th>\n      <th style=\"padding:10px;\">弱點名稱與成因</th>\n      <th style=\"padding:10px;\">金融系統危害場景</th>\n      <th style=\"padding:10px;\">核心技術防禦對策</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">A01:2021</td>\n      <td style=\"padding:8px;\">Broken Access Control (權限控制失效)</td>\n      <td style=\"padding:8px;\">IDOR 水平越權：修改 URL 參數直接查詢其他投資人委託庫存</td>\n      <td style=\"padding:8px;\">伺服端強制比對 Session 身分與資源所有權，嚴禁信任客戶端傳入之 ID</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">A02:2021</td>\n      <td style=\"padding:8px;\">Cryptographic Failures (加密機制失效)</td>\n      <td style=\"padding:8px;\">使用過期演算法（DES、MD5、SHA-1）或硬編碼金鑰於原始碼</td>\n      <td style=\"padding:8px;\">採用 AES-256-GCM、金鑰儲存於 KMS/HSM、全站強制 TLS 1.3 HSTS</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">A03:2021</td>\n      <td style=\"padding:8px;\">Injection (注入式攻擊，如 SQLi)</td>\n      <td style=\"padding:8px;\">下單查詢介面字串拼接，導致資料庫全庫遭脫庫倒賣</td>\n      <td style=\"padding:8px;\"><strong>全面採用參數化查詢（Prepared Statements）</strong>，禁止 SQL 拼接</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">A10:2021</td>\n      <td style=\"padding:8px;\">Server-Side Request Forgery (SSRF)</td>\n      <td style=\"padding:8px;\">利用匯入報表或 Webhook 誘使伺服器存取內網機密中繼端點</td>\n      <td style=\"padding:8px;\">URL 輸入白名單校驗、禁止伺服器解析內網私有 IP（10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.169.254）</td>\n    </tr>\n  </table>\n</div>\n\n<h2>2. DevSecOps 安全左移（Shift-Left）管線與品質閾門</h2>\n<pre><code class=\"language-text\">開發編碼 (Code) ──> 提交代碼 (Commit) ──> 建置編譯 (Build) ──> 測試驗證 (Test) ──> 上線部署 (Deploy)\n       │                    │                    │                    │                   │\n   IDE 即時提示           SAST 靜態代碼分析       SCA 開源相依分析      DAST 動態黑箱掃描   容器防護 (Falco)\n(SonarLint/Snyk)      (SonarQube/Checkmarx) (Dependency-Check)      (OWASP ZAP/Acunetix)  (CSPM/CWPP)</code></pre>\n<ul>\n  <li><strong>SAST（靜態分析）</strong>：檢查源碼潛在安全缺陷（SQL 拼接、弱密碼演算法、緩衝區溢位）。</li>\n  <li><strong>SCA（成分分析）</strong>：清查專案依賴第三方套件之已知 CVE 漏洞與開源授權合規。</li>\n  <li><strong>DAST（動態掃描）</strong>：在執行環境模擬黑箱滲透注入測試。</li>\n  <li><strong>Quality Gate（品質閾門）</strong>：若偵測到 High 或 Critical 漏洞，自動中斷 CI/CD 管線並阻擋上線。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】Web 安全注入與 SSRF 防禦、DevSecOps 自動化安全管線架構</h4>\n  <p><strong>題目</strong>：在證券 Web 交易系統中，試分析 SQL 注入（SQLi）與伺服器端請求偽造（SSRF）之成因與利用手法，並分別提出代碼級與網路架構級防禦對策；說明 DevSecOps「安全左移（Shift-Left）」之核心價值，並為證交所設計一套整合 SAST、SCA 與 DAST 之 CI/CD 自動化安全管線及 Quality Gate 準則。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>SQLi 與 SSRF 深入剖析（9分）</strong>：SQLi 參數化 Prepared Statements 底層預編譯分離語意與資料；SSRF 攻擊內網雲端中繼站（169.254.169.254），防禦採嚴格 URL 協定白名單、DNS 重新解析二次防範 DNS Rebinding、網路層封鎖內網網段。<br>\n    2. <strong>DevSecOps 安全左移架構（8分）</strong>：SAST (代碼提交階段)、SCA (建置階段軟體相依性檢查)、DAST (測試環境動態模糊測試)。<br>\n    3. <strong>Quality Gate 品質門禁標準（8分）</strong>：Critical/High 漏洞零容忍自動中斷發版、OWASP Top 10 命中自動建工單追蹤修補。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch06",
    "chapter": "第 6 章：網路邊界防禦、DDoS 防護與微隔離架構",
    "title": "次世代防火牆 NGFW、金融 Clean Pipe 清洗與微隔離架構實踐",
    "summary": "深入解構金融級次世代防火牆（NGFW）、Terabit 級 DDoS 混合攻擊立體防禦、BGP Anycast 全球清洗中心，以及軟體定義邊界（SDP）微隔離技術。",
    "vocab": [
      [
        "Next-Generation Firewall",
        "次世代防火牆 (NGFW)"
      ],
      [
        "Clean Pipe",
        "電信級流量清洗中心"
      ],
      [
        "BGP Anycast",
        "BGP 任播路由分流"
      ],
      [
        "SYN Flood",
        "SYN 泛洪阻斷攻擊"
      ],
      [
        "Slowloris",
        "慢速連線耗盡攻擊"
      ],
      [
        "Micro-segmentation",
        "網路微隔離技術"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Next-Generation Firewall', this)\">NGFW 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Clean Pipe', this)\">Clean Pipe 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('BGP Anycast', this)\">BGP Anycast 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Deep Packet Inspection', this)\">DPI 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Micro-segmentation', this)\">Micro-segmentation 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Rate Limiting', this)\">Rate Limiting 🔊</button>\n  </div>\n</div>\n\n<h2>1. 金融巨量級 DDoS 攻擊立體防禦體系</h2>\n<pre><code class=\"language-text\">外部攻擊流量 (數百 Gbps ~ Tbps 巨量洪峰)\n       │\n       ▼\n【第 1 道：電信端 Clean Pipe 流量清洗中心 / BGP Anycast CDN】\n  - 承載 L3/L4 巨量流量型攻擊 (UDP Amplification, NTP/DNS 反射)\n  - 透過 Anycast 路由將全球洪峰分散至數十個清洗節點吸收\n  - 阻斷未經授權之偽造 IP 封包，僅放行乾淨流量回源\n       │\n       ▼\n【第 2 道：資料中心邊界 Anti-DDoS 專屬硬體設備】\n  - 抵禦 L4 協定攻擊 (SYN Flood, ACK Flood, RST Flood)\n  - 啟用 SYN Cookie 與 TCP 雙向確認技術，零延遲防禦半開連線資源耗盡\n       │\n       ▼\n【第 3 道：Web 應用防火牆 (WAF) & API Gateway】\n  - 抵禦 L7 應用層 CC 攻擊 (HTTP GET/POST Flood, Slowloris 慢速慢速攻擊)\n  - 結合 JavaScript 挑戰碼、行為 CAPTCHA、IP 速率限制 (Rate Limiting) 與指紋分析</code></pre>\n\n<h2>2. 內部網路微隔離（Micro-segmentation）技術實踐</h2>\n<p>在零信任架構下，機房伺服器不再依賴傳統大網段。透過軟體定義網路（如 VMware NSX、Calico）：</p>\n<ul>\n  <li>在<strong>每台虛擬機（VM）或容器（Pod）虛擬網卡</strong>層面強制掛載分散式防火牆規則。</li>\n  <li>Web 伺服器僅被允許以固定連接埠（如 TCP 3306）連線至帳務資料庫，嚴格封鎖 Web 伺服器間橫向互訪（East-West Traffic）。攻擊者即便打穿單一 Web 伺服器，亦無法在內網掃描滲透。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】金融大規模 DDoS 勒索阻斷防禦與資料中心微隔離規劃</h4>\n  <p><strong>題目</strong>：證券期貨業屢遭境外駭客集團發動大規模阻斷服務（DDoS）勒索攻擊，威脅市場交易穩定。請分析常見 DDoS 攻擊類型（L3/L4 泛洪 vs L7 應用層慢速攻擊）之原理與差異；為臺灣證券交易所設計一套結合電信端 Clean Pipe 清洗、邊界硬體防護與 WAF 之立體化 DDoS 防禦體系；並闡述「網路微隔離（Micro-segmentation）」如何有效限制內網橫向移動？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>DDoS 攻擊分類對比（8分）</strong>：L3/L4 泛洪（UDP 反射放大、SYN Flood）耗盡出口頻寬與連線表；L7 應用層慢速（Slowloris、CC）耗盡 Web 線程池。<br>\n    2. <strong>三道立體防禦架構（9分）</strong>：電信端 Clean Pipe/BGP Anycast 清洗 L3/L4 巨量頻寬洪峰；邊界硬體 Anti-DDoS 啟用 SYN Cookie 防禦 TCP 握手耗盡；WAF/API Gateway 以 Rate Limiting 及行為 CAPTCHA 過濾 L7 慢速請求。<br>\n    3. <strong>網路微隔離技術（8分）</strong>：SDN 分散式防火牆掛載至虛擬網卡，Default-Deny 預設阻斷東西向流量，徹底消除橫向滲透。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch07",
    "chapter": "第 7 章：SOC 威脅監控、SIEM/SOAR、EDR 與事件應變",
    "title": "7x24 SOC 三層架構、MITRE ATT&CK 框架映射與記憶體鑑識實務",
    "summary": "深入解構金融 7x24 SOC 運作機制、SIEM 關聯分析、SOAR 自動化應變 Playbook、EDR/XDR 端點獵捕，以及 NIST SP 800-61 事件應變六步法與記憶體數位鑑識。",
    "vocab": [
      [
        "Security Operations Center",
        "資安維運中心 (SOC)"
      ],
      [
        "Security Orchestration, Automation and Response",
        "安全協調與自動化回應 (SOAR)"
      ],
      [
        "Endpoint Detection and Response",
        "端點偵測與回應 (EDR)"
      ],
      [
        "Order of Volatility",
        "數位鑑識揮發性順序"
      ],
      [
        "Memory Forensics",
        "記憶體數位鑑識"
      ],
      [
        "MITRE ATT&CK",
        "戰術戰法矩陣"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Security Operations Center', this)\">SOC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('SIEM', this)\">SIEM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('SOAR', this)\">SOAR 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('EDR', this)\">EDR 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Order of Volatility', this)\">Order of Volatility 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('MITRE ATT&CK', this)\">MITRE ATT&CK 🔊</button>\n  </div>\n</div>\n\n<h2>1. 金融 7x24 SOC 三層運作體系與 SIEM/SOAR 協同</h2>\n<ul>\n  <li><strong>Tier 1 分析師</strong>：監控 SIEM 即時告警儀表板，15 分鐘內完成分流升級與誤報排除。</li>\n  <li><strong>Tier 2 資深工程師</strong>：深入分析受駭範圍，調閱 EDR 行程樹與網路連線，執行威脅遏制（Containment）。</li>\n  <li><strong>Tier 3 威脅獵捕與鑑識專家</strong>：逆向分析惡意程式，解析記憶體 Payload，映射 MITRE ATT&CK 戰術戰技。</li>\n  <li><strong>SOAR 自動化劇本（Playbook）</strong>：偵測到勒索行為時，3 秒內自動完成：防火牆封鎖 C2 IP、EDR 網路隔離受害主機、AD 凍結帳號、簡訊通知值班主管。</li>\n</ul>\n\n<h2>2. NIST SP 800-61 事件應變與現場數位鑑識揮發性順序（RFC 3227）</h2>\n<div class=\"callout-box\">\n  <div class=\"callout-title\">🔍 現場數位鑑識證據保全原則（Order of Volatility）</div>\n  <p>在採集受駭主機證據時，必須嚴格依照<strong>揮發性順序（由高至低）</strong>採集，<strong>絕不可第一時間直接拔電源或重開機</strong>！<br>\n  1. <strong>CPU 暫存器與快取記憶體（Registers, Cache）</strong><br>\n  2. <strong>實體記憶體（RAM）</strong>：使用 LiME 或 DumpIt 完整提取，透過 Volatility 解析隱藏進程、注入代碼及明文金鑰。<br>\n  3. <strong>網路連線狀態（Network Connections）</strong>：<code>netstat/ss</code> 快照紀錄活躍與監聽 Socket。<br>\n  4. <strong>執行中程序狀態（Running Processes）</strong><br>\n  5. <strong>磁碟檔案系統與外部儲存媒體</strong>：以 FTK Imager 或 <code>dd</code> 製作唯讀 Bit-stream 鏡像，計算 SHA-256 雜湊保全監管鏈（Chain of Custody）。</p>\n</div>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】NIST 事件應變生命週期、RFC 3227 數位鑑識與 SOAR 自動化劇本</h4>\n  <p><strong>題目</strong>：請繪製並說明 NIST SP 800-61 電腦安全事件處理生命週期之六大階段。若證交所內網伺服器疑似遭植入無檔案惡意程式（Fileless Malware），在現場證據保全階段為何嚴禁直接拔除電源？請依 RFC 3227 詳述揮發性順序（Order of Volatility）與記憶體鑑識實務；並為「端點 EDR 偵測到勒索軟體高頻加密行為」設計一套 SOAR 自動化應變 Playbook。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>NIST SP 800-61 六大階段（7分）</strong>：準備、偵測與分析、遏制、根除、復原、事後檢討。<br>\n    2. <strong>RFC 3227 揮發性順序（9分）</strong>：不可拔除電源，否則 RAM 中之內存代碼與解密金鑰將永久消失！嚴格按暫存器 &rarr; 實體 RAM &rarr; 網路狀態 &rarr; 磁碟順序採集，確保監管鏈（Chain of Custody）。<br>\n    3. <strong>SOAR 自動化 Playbook 流程（9分）</strong>：觸發告警 &rarr; 豐富化情報（VirusTotal/F-ISAC）&rarr; 自動隔離端點 &rarr; 阻斷防火牆 C2 通訊 &rarr; 停用 AD 憑證 &rarr; 派發緊急工單。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch08",
    "chapter": "第 8 章：金融釣魚防禦、社交工程與端點深度強化",
    "title": "DMARC/DKIM/SPF 郵件防護、SEG 安全閘道與端點基線強化",
    "summary": "解構電子郵件防護三大協定（SPF、DKIM、DMARC）防偽機制、郵件安全閘道動態沙箱、針對性社交工程演練，以及 Windows/Linux 端點安全基線加固實務。",
    "vocab": [
      [
        "Sender Policy Framework",
        "寄件者原則架構 (SPF)"
      ],
      [
        "DomainKeys Identified Mail",
        "網域名稱金鑰識別郵件 (DKIM)"
      ],
      [
        "DMARC",
        "網域架構訊息驗證報告與一致性 (DMARC)"
      ],
      [
        "Secure Email Gateway",
        "安全郵件閘道 (SEG)"
      ],
      [
        "Constrained Language Mode",
        "受限語言模式 (PowerShell)"
      ],
      [
        "Application Whitelisting",
        "應用程式白名單"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Sender Policy Framework', this)\">SPF 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('DomainKeys Identified Mail', this)\">DKIM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('DMARC', this)\">DMARC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Secure Email Gateway', this)\">SEG 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Application Whitelisting', this)\">App Whitelisting 🔊</button>\n  </div>\n</div>\n\n<h2>1. 電子郵件防偽三大協定協同防護機制</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">防偽協定</th>\n      <th style=\"padding:10px;\">驗證核心原理</th>\n      <th style=\"padding:10px;\">主要防範攻擊</th>\n      <th style=\"padding:10px;\">局限性與防禦盲點</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">SPF (RFC 7208)</td>\n      <td style=\"padding:8px;\">DNS TXT 記錄列舉授權發信之伺服器 IP</td>\n      <td style=\"padding:8px;\">偽造 Return-Path (Mail From) 發信 IP</td>\n      <td style=\"padding:8px;\">無法防止郵件轉發（Forwarding）破壞；不校驗使用者看到的 Header From</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">DKIM (RFC 6376)</td>\n      <td style=\"padding:8px;\">寄件方以私鑰對郵件標頭與內文數位簽名，收件方取 DNS 公鑰驗證</td>\n      <td style=\"padding:8px;\">傳輸過程中內文遭篡改、假冒簽章</td>\n      <td style=\"padding:8px;\">不校驗簽章網域是否與 Header From 網域一致</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">DMARC (RFC 7489)</td>\n      <td style=\"padding:8px;\">強制要求 <strong>Header From 與 SPF/DKIM 網域一致性（Alignment）</strong>，設定處理策略（p=reject）並產出分析報告</td>\n      <td style=\"padding:8px;\"><strong>徹底杜絕直接偽冒證交所網域之釣魚信</strong></td>\n      <td style=\"padding:8px;\">若策略僅設為 <code>p=none</code> 僅監控無阻斷，必須升級至 <code>p=reject</code> 始具防禦效力</td>\n    </tr>\n  </table>\n</div>\n\n<h2>2. 企業端點防禦基線加固實務</h2>\n<ul>\n  <li><strong>應用程式白名單（WDAC / AppLocker）</strong>：嚴格僅允許具有合法數位簽章且位於 <code>C:\\Program Files</code> 之受信任軟體執行，阻斷自 <code>%TEMP%</code> 或 <code>%APPDATA%</code> 啟動的惡意勒索執行檔。</li>\n  <li><strong>PowerShell 加固</strong>：全公司強制套用 <code class=\"en-code\" data-speak=\"Constrained Language Mode\">ConstrainedLanguage</code> 模式，禁止動態 API 反射調用；啟用全文 Script Block Logging 與 Transcription 審計日誌。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】SPF/DKIM/DMARC 協同防禦機制與端點應用程式白名單防禦</h4>\n  <p><strong>題目</strong>：金融釣魚郵件為 APT 組織發動初始入侵（Initial Access）之首要破口。請詳細解構 SPF、DKIM 與 DMARC 三大協定之運作原理、對齊檢查（Alignment）與防禦盲點，並說明為何企業必須將 DMARC 政策升級至 p=reject；另針對端點主機，說明如何運用應用程式白名單（AppLocker/WDAC）阻斷無檔案（Fileless）惡意攻擊？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>SPF/DKIM/DMARC 原理與盲點（10分）</strong>：SPF 驗證發信 IP（盲點為無法防轉發與 Header From 偽冒）；DKIM 驗證密碼學簽章完整性；DMARC 結合二者實施 Header From Alignment，阻斷偽造；p=reject 確保未通過者直接被收信端拒收。<br>\n    2. <strong>端點應用程式白名單（8分）</strong>：AppLocker / WDAC 規範僅合法路徑與合法 TWSE 簽章程式可運行，阻斷臨時目錄可執行檔。<br>\n    3. <strong>PowerShell 加固阻斷無檔案攻擊（7分）</strong>：Constrained Language Mode 限制調用 Win32 API / COM 元件，配合 Script Block Logging 完整記錄進程命令。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch09",
    "chapter": "第 9 章：雲端與容器安全、DevSecOps 稽核",
    "title": "CIS K8s Benchmark、Falco 核心監控、雲端共享責任與 CSPM/CWPP",
    "summary": "深入剖析 Kubernetes 容器安全防護、CIS Benchmark 安全基準、Falco eBPF 執行期偵測、容器網路 NetworkPolicy 微隔離，以及雲端安全態勢管理（CSPM/CWPP）。",
    "vocab": [
      [
        "Cloud Security Posture Management",
        "雲端安全態勢管理 (CSPM)"
      ],
      [
        "Cloud Workload Protection Platform",
        "雲端工作負載防護 (CWPP)"
      ],
      [
        "Network Policy",
        "容器網路微隔離政策"
      ],
      [
        "Runtime Security",
        "容器執行期安全監控"
      ],
      [
        "Rootless Container",
        "無 Root 容器架構"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('CSPM', this)\">CSPM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('CWPP', this)\">CWPP 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Network Policy', this)\">Network Policy 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Falco', this)\">Falco 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Rootless', this)\">Rootless 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Admission Controller', this)\">Admission Controller 🔊</button>\n  </div>\n</div>\n\n<h2>1. Kubernetes 縱深防禦三大構面</h2>\n<ul>\n  <li><strong>映像檔建置期（Build）</strong>：使用最小化基底映像（Distroless/Alpine）、嚴禁以 root 身分運行（<code>USER nonroot</code>）、Trivy 掃描漏洞、Cosign 數位簽章防篡改。</li>\n  <li><strong>執行期防護（Runtime）</strong>：部署 <strong>Falco（基於 eBPF）</strong> 監控核心異常系統呼叫（如容器內執行 <code>sh</code>、存取 <code>/etc/shadow</code>）；強制配置 <code>readOnlyRootFilesystem: true</code>。</li>\n  <li><strong>K8s 叢集編排（Cluster）</strong>：啟用 RBAC 最小特權原則、OPA Gatekeeper 準入控制（Admission Control）、<strong>NetworkPolicy</strong> 實施微隔離。</li>\n</ul>\n\n<h2>2. Kubernetes NetworkPolicy 預設阻斷與定向放行實務</h2>\n<pre><code class=\"language-yaml\"># 預設阻斷該命名空間下所有 Pod 之東西向與南北向連線 (Default Deny)\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: default-deny-all\n  namespace: twse-trading\nspec:\n  podSelector: {}\n  policyTypes:\n  - Ingress\n  - Egress\n---\n# 僅允許撮合引擎 (Matching Engine) 存取資料庫 (DB) 連接埠 3306\napiVersion: networking.k8s.io/v1\nkind: NetworkPolicy\nmetadata:\n  name: allow-matching-to-db\n  namespace: twse-trading\nspec:\n  podSelector:\n    matchLabels:\n      app: trading-db\n  ingress:\n  - from:\n    - podSelector:\n        matchLabels:\n          app: matching-engine\n    ports:\n    - protocol: TCP\n      port: 3306</code></pre>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】金融微服務容器化安全防護架構與 Kubernetes 叢集微隔離</h4>\n  <p><strong>題目</strong>：金融機構推動核心微服務轉型時廣泛採用 Docker 與 Kubernetes 架構。請從映像檔建置、執行階段（Runtime）與叢集編排三個層面提出容器安全縱深防禦措施；並說明 Kubernetes NetworkPolicy 之運作機制，繪製並撰寫 YAML 策略以達成 Default-Deny 預設阻斷與最小授權通信。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>容器三大階段縱深防護（9分）</strong>：Build (Distroless、USER nonroot、Cosign 簽名)；Runtime (Falco eBPF 核心監控、唯讀根目錄、seccomp 白名單)；Cluster (RBAC、準入控制器、CIS Benchmark)。<br>\n    2. <strong>NetworkPolicy 運作原理（8分）</strong>：底層由 CNI (如 Calico/Cilium) 在 iptables/eBPF 注入規則，控制 Pod 間 L3/L4 通訊。<br>\n    3. <strong>YAML 策略配置與 Default-Deny（8分）</strong>：完整寫出 Default-Deny Ingress/Egress 策略與 matchLabels 限制指定 Pod 與 Port 通訊之正確 YAML 範例。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch10",
    "chapter": "第 10 章：紅藍對抗、滲透測試與漏洞弱點管理",
    "title": "紅隊演練（Red Teaming）、紫隊協同與 CVSS v3.1 漏洞評分體系",
    "summary": "解構紅藍攻防對抗機制、PTES 滲透測試執行標準、APT 模擬入侵鏈、紫隊協同防禦，以及 CVSS v3.1 漏洞評分模型與虛擬補丁修補策略。",
    "vocab": [
      [
        "Red Teaming",
        "紅隊實兵演練"
      ],
      [
        "Blue Teaming",
        "藍隊防禦維運"
      ],
      [
        "Purple Teaming",
        "紫隊協同機制"
      ],
      [
        "Common Vulnerability Scoring System",
        "通用弱點評分系統 (CVSS)"
      ],
      [
        "Virtual Patching",
        "虛擬補丁防禦"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Red Teaming', this)\">Red Teaming 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Blue Teaming', this)\">Blue Teaming 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Purple Teaming', this)\">Purple Teaming 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('CVSS', this)\">CVSS v3.1 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Virtual Patching', this)\">Virtual Patching 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Penetration Testing', this)\">Penetration Testing 🔊</button>\n  </div>\n</div>\n\n<h2>1. 漏洞弱點掃描 vs 滲透測試 vs 紅隊演練三維對比</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">比較維度</th>\n      <th style=\"padding:10px;\">弱點掃描 (Vulnerability Scan)</th>\n      <th style=\"padding:10px;\">滲透測試 (Penetration Test)</th>\n      <th style=\"padding:10px;\">紅隊演練 (Red Teaming)</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">主要目標</td>\n      <td style=\"padding:8px;\">清查資產中所有已知 CVE 漏洞</td>\n      <td style=\"padding:8px;\">驗證特定系統弱點能否被利用打穿</td>\n      <td style=\"padding:8px;\"><strong>模擬真實 APT 組織，驗證藍隊監控與應變極限</strong></td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">執行手法</td>\n      <td style=\"padding:8px;\">全自動化工具掃描（Nessus 等）</td>\n      <td style=\"padding:8px;\">人工結合工具，依 PTES 標準探索</td>\n      <td style=\"padding:8px;\">不限手法（釣魚、實體社工、水坑攻擊、0-day）</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">實施頻率</td>\n      <td style=\"padding:8px;\">每月或每季常態執行</td>\n      <td style=\"padding:8px;\">系統重大改版或每年一次</td>\n      <td style=\"padding:8px;\">每年 1~2 次實兵無預警對抗</td>\n    </tr>\n  </table>\n</div>\n\n<h2>2. CVSS v3.1 漏洞評分標準與補償性控制</h2>\n<ul>\n  <li><strong>Base Metrics（基本指標）</strong>：攻擊途徑（AV: N/A/L/P）、複雜度（AC: L/H）、特權需求（PR: N/L/H）、使用者互動（UI: N/R）、範圍（S: U/C）、影響度（C/I/A: N/L/H）。</li>\n  <li><strong>虛擬補丁（Virtual Patching）</strong>：若核心系統因業務連續性無法立刻停機重啟打補丁，第一時間於 WAF 或 IPS 配置特徵規則攔截攻擊 Payload，爭取評估修補時間。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】弱掃/滲透/紅隊演練深度對比與 CVSS 漏洞管理與虛擬補丁</h4>\n  <p><strong>題目</strong>：試比較「漏洞弱點掃描」、「滲透測試（Penetration Testing）」與「紅隊演練（Red Teaming）」三者之測試目標、手法深度與產出效益；詳細說明 CVSS v3.1 基本度量指標（Base Metrics）之構成；並闡述當撮合交易系統面臨評分為 9.8 之高危漏洞但短期內無法停機上補丁時，資安部門應如何實施補償性控制與虛擬補丁（Virtual Patching）？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>三者維度比較表（8分）</strong>：以表格詳列目標、手法、範圍、頻率及輸出結果差異。<br>\n    2. <strong>CVSS v3.1 Base Metrics（8分）</strong>：寫出可利用性度量（AV, AC, PR, UI）、範圍（Scope S）、影響性度量（CIA 保密/完整/可用性）。<br>\n    3. <strong>補償控制與虛擬補丁（9分）</strong>：定義虛擬補丁概念；在 WAF/IPS 下發正則特徵規則阻斷利用請求、主機層微隔離封鎖非必要埠存取、SIEM 加強專屬特徵即時告警。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch11",
    "chapter": "第 11 章：業務持續性計畫（BCP）與勒索軟體全方位防禦",
    "title": "ISO 22301 BCMS 體系、BIA 衝擊分析、3-2-1-1-0 備份與防勒索實務",
    "summary": "解析金融業務持續性計畫（BCP/DRP）、營運衝擊分析（BIA）、RTO/RPO 嚴苛容災指標、黃金備份法則 3-2-1-1-0、不可竄改 WORM 儲存與同城雙活機房切換。",
    "vocab": [
      [
        "Business Continuity Plan",
        "業務持續性計畫 (BCP)"
      ],
      [
        "Disaster Recovery Plan",
        "災難復原計畫 (DRP)"
      ],
      [
        "Recovery Time Objective",
        "復原時間目標 (RTO)"
      ],
      [
        "Recovery Point Objective",
        "復原點目標 (RPO)"
      ],
      [
        "Write Once Read Many",
        "一次寫入多次讀取 (WORM)"
      ],
      [
        "Air-Gapped Backup",
        "實體氣隙隔離備份"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Business Continuity Plan', this)\">BCP 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Disaster Recovery Plan', this)\">DRP 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Recovery Time Objective', this)\">RTO 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Recovery Point Objective', this)\">RPO 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Write Once Read Many', this)\">WORM 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Air-Gapped', this)\">Air-Gapped 🔊</button>\n  </div>\n</div>\n\n<h2>1. 業務持續管理系統（ISO 22301 BCMS）與指標定義</h2>\n<ul>\n  <li><strong>BIA（營運衝擊分析）</strong>：評估核心系統中斷對財務、法律與商譽之最大可容忍中斷時間（MTPD）。</li>\n  <li><strong>RTO（復原時間目標）</strong>：系統從災難中斷到完全恢復對外服務之允許時間上限（證交所要求 <code>RTO &le; 10 分鐘</code>）。</li>\n  <li><strong>RPO（復原點目標）</strong>：系統恢復後允許遺失資料之最大時間跨度（證交所要求 <code>RPO = 0</code>，零資料遺失）。</li>\n</ul>\n\n<h2>2. 防勒索軟體「3-2-1-1-0」黃金備份法則</h2>\n<div class=\"callout-box\">\n  <div class=\"callout-title\">🛡️ 現代金融抗勒索 3-2-1-1-0 備份不變原則</div>\n  <p><strong>3</strong>：保有至少 3 份資料副本（1 份生產資料 + 2 份獨立備份）。<br>\n  <strong>2</strong>：使用至少 2 種不同實體儲存媒介（如高效能快閃磁碟陣列 + 磁帶儲存庫）。<br>\n  <strong>1</strong>：至少 1 份備份存放於異地機房（距離至少 30 公里以上，防範區域天災）。<br>\n  <strong>1</strong>：至少 1 份備份處於<strong>實體氣隙隔離（Air-Gapped）</strong>或<strong>不可竄改儲存（Immutable WORM / S3 Object Lock）</strong>，勒索軟體無法加密或刪除。<br>\n  <strong>0</strong>：備份必須落實定期全真還原測試演練，確保還原錯誤率為 0。</p>\n</div>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】證交所關鍵系統 RTO/RPO 容災規範、3-2-1-1-0 防勒索備份架構</h4>\n  <p><strong>題目</strong>：臺灣證券交易所為關鍵基礎設施，對核心撮合系統訂定 RTO &le; 10 分鐘、RPO = 0 之嚴苛容災指標。請規劃一套符合「3-2-1-1-0」原則且具備防勒索不可篡改（WORM）特性之全方位備份與災難復原演練方案；若主機房遭遇勒索軟體大規模加密，在 BCP 災難復原計畫中啟動同城備援中心接管之關鍵決策門檻與流程為何？（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>RTO/RPO 技術實現架構（8分）</strong>：同城雙活專用暗光纖同步鏡像確保 RPO=0；分散式 Paxos/Raft Quorum 共識與自動 VIP 漂移確保 RTO&le;10分鐘。<br>\n    2. <strong>3-2-1-1-0 備份體系（9分）</strong>：3份副本、2種媒介、1異地、1不可變 WORM 存儲（Object Lock 合規保留期）、0還原驗證錯誤。<br>\n    3. <strong>災難復原接管決策（8分）</strong>：判定主機房已無法於 10 分鐘內復原 &rarr; 召開緊急應變小組核准 &rarr; 切斷主機房對外連線防擴散 &rarr; 啟用備援中心資料庫昇主 &rarr; BGP Anycast 流量切換 &rarr; 券商連線驗證。\n  </div>\n</div>\n"
  },
  {
    "id": "sec-ch12",
    "chapter": "第 12 章：新興科技資安、人工智慧（AI）與大語言模型安全",
    "title": "OWASP Top 10 for LLM、金管會 AI 治理指引與後量子密碼學（PQC）",
    "summary": "深入剖析金融生成式 AI（GenAI）金管會治理原則、OWASP LLM 核心風險（提示注入/資料投毒/敏感外洩/過度代理），以及後量子密碼學（PQC）抗量子遷移戰略。",
    "vocab": [
      [
        "Prompt Injection",
        "提示注入攻擊 (LLM01)"
      ],
      [
        "Excessive Agency",
        "過度代理權限 (LLM08)"
      ],
      [
        "Human-in-the-Loop",
        "人機協同介入機制"
      ],
      [
        "Post-Quantum Cryptography",
        "後量子密碼學 (PQC)"
      ],
      [
        "Crypto-Agility",
        "加密敏捷性遷移"
      ],
      [
        "Lattice-based Cryptography",
        "晶格密碼學"
      ]
    ],
    "content": "\n<div class=\"chapter-vocab-bar\">\n  <div class=\"vocab-bar-title\">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class=\"vocab-items\">\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Prompt Injection', this)\">Prompt Injection 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Excessive Agency', this)\">Excessive Agency 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Human-in-the-Loop', this)\">Human-in-the-Loop 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Post-Quantum Cryptography', this)\">PQC 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Crypto-Agility', this)\">Crypto-Agility 🔊</button>\n    <button type=\"button\" class=\"vocab-pill\" onclick=\"speakEn('Shor algorithm', this)\">Shor's Algorithm 🔊</button>\n  </div>\n</div>\n\n<h2>1. 金管會「金融業運用人工智慧（AI）核心原則」</h2>\n<ul>\n  <li><strong>建立治理及問責機制（Accountability）</strong>：高階管理層負最終法律責任，不可因 AI 自動決策而免責。</li>\n  <li><strong>重視公平性及人機協同（Fairness & Human-in-the-Loop）</strong>：重大金融決策必須保留<strong>人工介入授權機制</strong>，嚴防黑箱偏差。</li>\n  <li><strong>保護隱私及機密資料（Privacy）</strong>：嚴禁將未去識別化之客戶個資或內部交易明文輸入公有雲模型。</li>\n</ul>\n\n<h2>2. OWASP Top 10 for LLM:2023 核心風險與防禦</h2>\n<div class=\"table-wrap\">\n  <table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n    <tr style=\"background:var(--accent-primary); color:#fff;\">\n      <th style=\"padding:10px;\">OWASP 排名</th>\n      <th style=\"padding:10px;\">威脅名稱與原理</th>\n      <th style=\"padding:10px;\">金融危害情境</th>\n      <th style=\"padding:10px;\">核心工程防禦對策</th>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">LLM01:2023</td>\n      <td style=\"padding:8px;\">Prompt Injection (提示注入)</td>\n      <td style=\"padding:8px;\">惡意指令覆蓋系統 Prompt，誘使金融客服機器人吐出機密 API 金鑰</td>\n      <td style=\"padding:8px;\">嚴格隔離系統指令與使用者上下文、部署 NeMo Guardrails 安全護欄</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">LLM02:2023</td>\n      <td style=\"padding:8px;\">Sensitive Information Disclosure (敏感外洩)</td>\n      <td style=\"padding:8px;\">模型訓練過度記憶帳號或身份資料，被提示工程套出</td>\n      <td style=\"padding:8px;\">訓練前差分隱私資料清洗、輸出層 DLP 敏感詞動態遮罩</td>\n    </tr>\n    <tr>\n      <td style=\"padding:8px; font-weight:700;\">LLM08:2023</td>\n      <td style=\"padding:8px;\">Excessive Agency (過度代理權限)</td>\n      <td style=\"padding:8px;\">AI Agent 自主執行未經審批的高額委託下單或資料庫修改</td>\n      <td style=\"padding:8px;\">外掛工具採最小特權原則、重大操作強制加入 Human-in-the-Loop 審批</td>\n    </tr>\n  </table>\n</div>\n\n<h2>3. 後量子密碼學（PQC）抗量子遷移戰略</h2>\n<p>量子電腦之 Shor 演算法能在數秒內攻破 RSA-2048 與 ECC 非對稱加密。攻擊者現正發動<strong>「先側錄，後解密（Store Now, Decrypt Later）」</strong>：</p>\n<ul>\n  <li><strong>NIST 2024 正式標準演算法</strong>：\n    - 金鑰封裝（KEM）：<strong>ML-KEM (FIPS 203, CRYSTALS-Kyber)</strong>，基於晶格密碼學；<br>\n    - 數位簽章：<strong>ML-DSA (FIPS 204, CRYSTALS-Dilithium)</strong> 與 <strong>SLH-DSA (FIPS 205, SPHINCS+)</strong>。\n  </li>\n  <li><strong>金融加密敏捷性（Crypto-Agility）雙軌模式</strong>：在下單憑證與 TLS 1.3 協商中同時注入傳統 ECDSA 與 PQC 雙重簽名，達成平滑遷移。</li>\n</ul>\n\n<div class=\"exam-prediction-box\">\n  <span class=\"prediction-badge\">🎯 臺灣證交所年度核心猜題與考點剖析（資安人員高頻必考）</span>\n  <h4 style=\"margin:0.5rem 0; color:var(--accent-primary);\">【滿分申論標竿題】金管會 AI 治理指引、OWASP LLM 攻擊防禦與後量子 PQC 遷移</h4>\n  <p><strong>題目</strong>：人工智慧與大語言模型（LLM）正重塑金融科技，伴隨之提示注入與隱私洩漏亦引發高度監理關切；同時量子計算發展亦對現行公開金鑰密碼構成根本威脅。請說明金管會「金融業運用人工智慧（AI）核心原則」之治理重點；列舉 OWASP Top 10 for LLM 之三項重大威脅與防禦對策；並闡述後量子密碼學（PQC）演算法與金融加密敏捷性（Crypto-Agility）遷移架構。（配分：25分）</p>\n  <div class=\"essay-examiner-tips\">\n    <strong>🎯 評分踩點與黃金結構要點</strong>：<br>\n    1. <strong>金管會 AI 原則（7分）</strong>：問責機制（高階主管負終極責任）、公平性與 Human-in-the-loop、資料隱私安全。<br>\n    2. <strong>OWASP LLM 表格（9分）</strong>：完整列出 Prompt Injection、Sensitive Information Disclosure、Excessive Agency 之成因、危害與防禦技術。<br>\n    3. <strong>PQC 後量子密碼（9分）</strong>：Shor 演算法威脅、Store Now Decrypt Later、NIST 最新標準 ML-KEM / ML-DSA、混合簽章加密敏捷性（Crypto-Agility）。\n  </div>\n</div>\n"
  }
];

// 關鍵導出：確保附掛於全局 window 物件以利跨腳本存取
window.NOTES_SEC = NOTES_SEC;
