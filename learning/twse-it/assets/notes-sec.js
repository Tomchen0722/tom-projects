/**
 * 臺灣證券交易所 (TWSE) 招募備考講義 - 資通安全人員 (資訊安全概論)
 * 深度解析金融資安法規、ISO 27001:2022、密碼學HSM、零信任ZTA、OWASP攻防、SIEM/SOAR及金管會事件通報
 */

const NOTES_SEC = [
  {
    id: "sec-ch01",
    chapter: "第 1 章：金融資安法規治理與證券期貨業聯防體系",
    title: "金融資安行動方案 2.0、F-ISAC 聯防架構與資通安全管理法",
    summary: "剖析我國金融監督管理委員會『金融資安行動方案 2.0』四大核心主軸、證券期貨業資安監理架構、F-ISAC / F-CERT 情資分享與重大資安通報法遵。",
    content: `
<h2>1. 金融資安行動方案 2.0 策略核心</h2>
<p>金融監督管理委員會（金管會）為強化我國金融關鍵基礎設施韌性，推動<strong>「金融資安行動方案 2.0」</strong>，以<strong>「安全、便利、不中斷」</strong>為願景，聚焦四大推動主軸：</p>
<ol>
  <li><strong>協力深化監理與聯防架構</strong>：擴大金融資安資訊分享與分析中心（F-ISAC）情資分享廣度與深度，推動跨金融機構資安情資即時互聯。</li>
  <li><strong>強化核心資通系統韌性</strong>：全面落實「同城雙活」或異地即時備援，要求核心交易系統 <strong>RTO ≤ 2 小時（交易所核心目標逼近 0）、RPO = 0</strong>，並定期實施無預警災難切換演練。</li>
  <li><strong>推動零信任架構（ZTA）導入</strong>：推動身分識別、設備健全度、信任推論與動態存取控制三階段落地。</li>
  <li><strong>鼓勵金融機構建置 SOC 與威脅獵捕能量</strong>：建立全天候 7x24 資安監控機制，強化自主紅藍隊實戰攻防對抗（Purple Teaming）。</li>
</ol>

<h2>2. 證券期貨業資通安全聯合防禦體系（F-ISAC / F-CERT）</h2>
<div class="callout-box">
  <div class="callout-title">🛡️ 金融聯防三大樞紐角色</div>
  <p>• <strong>F-ISAC（金融資安資訊分享與分析中心）</strong>：彙整各金融機構、政府 N-ISAC 及國際情資，發布 APT 威脅警訊與惡意指標（IoC, Indicators of Compromise）。<br>
  • <strong>F-CERT（金融電腦緊急應變小組）</strong>：提供重大資安事件現場技術支援、數位鑑識調查與跨機構應變協調。<br>
  • <strong>F-SOC（金融資安監控中心）</strong>：全天候收集金控、銀行、證券交易巨量日誌，進行關聯威脅偵測。</p>
</div>

<h2>3. 重大資安事件通報法遵時限規範</h2>
<p>依據金管會與證券期貨局規範，證券商與周邊單位若遭遇重大資安事件（如網路遭受分散式阻斷服務 DDoS 攻擊導致下單中斷、勒索軟體感染或核心資料庫遭入侵外洩）：</p>
<ul>
  <li><strong>即時口頭/線上通報</strong>：知悉事件發生後<strong>「30 分鐘以內」</strong>，必須立即通報證期局與 F-ISAC / 金融監理通報系統。</li>
  <li><strong>書面報告時限</strong>：於事件發生後 1 個營業日內提出初步書面報告，事件復原與調查完畢後 7 日內提交完整根因分析與檢討改善報告。</li>
</ul>
`
  },
  {
    id: "sec-ch02",
    chapter: "第 2 章：資安標準與控制框架（ISO 27001:2022 與 NIST CSF）",
    title: "ISO/IEC 27001:2022 四大主題 93 項控制措施、NIST CSF 2.0 實務",
    summary: "對比 ISO 27001 新舊版重大變更、93 項控制措施分類（組織、人員、實體、技術）、NIST CSF 2.0 六大功能（GV, ID, PR, DE, RS, RC）實務佈建。",
    content: `
<h2>1. ISO/IEC 27001:2022 重大改版結構解析</h2>
<p>ISO/IEC 27001 於 2022 年底正式發布新版本。附錄 A（Annex A）控制措施由舊版 2013 年的 14 個章節 114 項控制措施，精簡重組為<strong>四大主題（Themes）共 93 項控制措施</strong>：</p>
<ul>
  <li><strong>5. Organizational Controls（組織控制措施）</strong>：共 37 項（如資訊安全政策、職能分工、供應鏈安全管理）。</li>
  <li><strong>6. People Controls（人員控制措施）</strong>：共 8 項（如到職前審查、資安意識培訓、遠距工作規範）。</li>
  <li><strong>7. Physical Controls（實體控制措施）</strong>：共 14 項（如機房實體邊界、設備位置保護、走清桌清規範）。</li>
  <li><strong>8. Technological Controls（技術控制措施）</strong>：共 34 項（如端點安全、特權存取管理、資料外洩防護 DLP）。</li>
</ul>

<div class="callout-box">
  <div class="callout-title">⭐ 2022 版新增之 11 項關鍵控制措施（考試重點）</div>
  <p>1. <code>A.5.7</code> 威脅情資（Threat Intelligence）<br>
  2. <code>A.5.23</code> 雲端服務資安（Information Security for Cloud Services）<br>
  3. <code>A.5.30</code> 資通訊準備度（ICT Readiness for Business Continuity）<br>
  4. <code>A.7.4</code> 實體安全監控（Physical Security Monitoring）<br>
  5. <code>A.8.9</code> 組態管理（Configuration Management）<br>
  6. <code>A.8.10</code> 資訊刪除（Information Deletion）<br>
  7. <code>A.8.11</code> 資料遮蔽（Data Masking）<br>
  8. <code>A.8.12</code> 資料外洩防護（Data Leakage Prevention）<br>
  9. <code>A.8.16</code> 活動監控（Monitoring Activities）<br>
  10. <code>A.8.23</code> 網頁過濾（Web Filtering）<br>
  11. <code>A.8.28</code> 安全編碼（Secure Coding）</p>
</div>

<h2>2. NIST CSF 2.0（網路安全框架）六大核心支柱</h2>
<p>美國國家標準與技術研究院於 2024 年正式推出 <strong>NIST CSF 2.0</strong>，由原先 5 大功能擴充新增<strong>「治理（Govern）」</strong>，成為六大核心支柱：</p>
<ol>
  <li><strong>Govern（治理, GV）</strong>：建立資安治理結構、風險管理策略、法律合規與管理階層督導。</li>
  <li><strong>Identify（識別, ID）</strong>：盤點金融關鍵資產、軟硬體供應商、漏洞評估與業務衝擊分析（BIA）。</li>
  <li><strong>Protect（保護, PR）</strong>：身分與存取管理、意識培訓、資料安全、零信任隔離。</li>
  <li><strong>Detect（偵測, DE）</strong>：異常活動監控、連續監測、威脅情資關聯比對。</li>
  <li><strong>Respond（回應, RS）</strong>：事件應變處置、圍堵減緩、溝通協調與分析調查。</li>
  <li><strong>Recover（復原, RC）</strong>：災後復原計劃執行、公關溝通、系統完整性驗證。</li>
</ol>
`
  },
  {
    id: "sec-ch03",
    chapter: "第 3 章：密碼學原理與金融交易保護",
    title: "對稱/非對稱演算法、數位簽章、HSM 硬體安全模組與後量子密碼",
    summary: "深入剖析 AES-GCM 認證加密、RSA/ECC 橢圓曲線密碼、SHA-3 雜湊、PKI X.509 憑證鏈驗證、FIPS 140-2 Level 3 HSM 運作與後量子密碼（PQC）趨勢。",
    content: `
<h2>1. 現代密碼學演算法體系</h2>
<p>證券交易、電子下單憑證簽署與傳輸層加密奠基於三大密碼學支柱：</p>
<ul>
  <li><strong>對稱式加密（Symmetric Cryptography）</strong>：
    <ul>
      <li><strong>AES（進階加密標準）</strong>：區塊大小固定為 128 位元，金鑰長度為 128、192 或 256 位元。金融通訊最推薦 <strong>AES-GCM（Galois/Counter Mode）</strong>，提供 AEAD（Authenticated Encryption with Associated Data，具認證關聯資料之加密），同時保證機密性與完整性，硬體支援（AES-NI）下延遲極低。</li>
    </ul>
  </li>
  <li><strong>非對稱式加密與數位簽章（Asymmetric Cryptography）</strong>：
    <ul>
      <li><strong>RSA vs. ECC</strong>：RSA 依賴大整數質因數分解困難度（建議長度 ≥ 2048/3072 位元）；<strong>ECC（橢圓曲線密碼）</strong> 依賴離散對數難題（ECDSA / Ed25519），256 位元 ECC 即可具備相當於 RSA 3072 位元之安全強度，運算耗時極低且簽章短小，非常適合微秒級高頻簽章。</li>
    </ul>
  </li>
  <li><strong>抗碰撞單向雜湊函式（Cryptographic Hash）</strong>：
    <ul>
      <li>SHA-256、SHA-3（Keccak 海綿結構）。金融安全嚴格禁止使用已證實存在碰撞弱點之 MD5 與 SHA-1。</li>
    </ul>
  </li>
</ul>

<h2>2. 金融硬體安全模組（HSM）防護層級</h2>
<p>證券交易所核心憑證管理與簽章伺服器全面採用 <strong>HSM（Hardware Security Module）</strong>：</p>
<ul>
  <li><strong>FIPS 140-2 / FIPS 140-3 認證標準</strong>：
    <ul>
      <li><strong>Level 1</strong>：基本生產級加密軟硬體，無實體防護。</li>
      <li><strong>Level 2</strong>：具備防拆封印（Tamper-Evident Coating/Seals），能留下物理破壞痕跡。</li>
      <li><strong>Level 3（金融 HSM 標配）</strong>：具備<strong>防拆主動銷毀（Tamper-Response Mechanisms）</strong>。一旦感測到機殼外蓋開啟、溫度驟降（防冷卻攻擊）、電壓突變或鑽孔探針，內部感測器立即在微秒內清零並自毀金鑰（Zeroization）。</li>
      <li><strong>Level 4</strong>：軍規級全環境主動防禦防護罩。</li>
    </ul>
  </li>
  <li><strong>雙人管理原則（Dual Control）與 M of N 門檻機制</strong>：Master Key 由多張智慧卡分割持有，必須同時插入 M 位管理員（例如 3 of 5）卡片並輸入密碼方可解鎖 HSM。</li>
</ul>

<h2>3. 後量子密碼學（PQC, Post-Quantum Cryptography）展望</h2>
<div class="callout-box">
  <div class="callout-title">⚠️ Shor 演算法對既有公鑰體系的威脅</div>
  <p>量子電腦具備強大的平行疊加算力，可在多項式時間內透過 Shor 演算法破解 RSA、ECC 與 Diffie-Hellman。NIST 已完成 PQC 標準化，選出晶格密碼（Lattice-based）：<br>
  • 金鑰封裝：<strong>ML-KEM（CRYSTALS-Kyber）</strong><br>
  • 數位簽章：<strong>ML-DSA（CRYSTALS-Dilithium）</strong> 與 SLH-DSA（SPHINCS+）。金管會亦要求大型金融關鍵基礎設施研擬量子遷移藍圖（Quantum Migration）。</p>
</div>
`
  },
  {
    id: "sec-ch04",
    chapter: "第 4 章：網路安全、零信任架構（ZTA）與邊界防禦",
    title: "零信任三大核心組件、FIDO2 無密碼身分驗證與 Terabit 級 DDoS 清洗",
    summary: "解析 NIST SP 800-207 零信任架構（PDP, PEP）、FIDO2/WebAuthn 原理、微隔離技術、次世代防火牆（NGFW）及證券下單通道之抗 DDoS 防護體系。",
    content: `
<h2>1. 零信任架構（ZTA - NIST SP 800-207）原理</h2>
<p>零信任架構核心哲學為<strong>「Never Trust, Always Verify（永不信任，始終驗證）」</strong>。假設內網已被敵對勢力滲透，摒棄基於 IP 位址或 VPN 的傳統邊界信任模型：</p>
<ul>
  <li><strong>三大邏輯元件</strong>：
    <ol>
      <li><strong>Policy Engine（PE, 決策引擎）</strong>：負責綜合評估使用者身分、設備端點健康度、威脅情資，決定是否核准該次請求。</li>
      <li><strong>Policy Administrator（PA, 管理器）</strong>：負責與 PEP 溝通，簽發臨時性憑證或通行令牌（Token）。</li>
      <li><strong>Policy Enforcement Point（PEP, 執行點）</strong>：位於流量進出閘道，攔截並強制執行存取控制決策。</li>
    </ol>
  </li>
  <li><strong>微隔離（Micro-segmentation）</strong>：在資料中心內部各伺服器與 Pod 之間實施軟體定義精細防火牆，限制東-西向（East-West）流量，徹底扼殺駭客橫向移動（Lateral Movement）路徑。</li>
</ul>

<h2>2. 次世代身分認證：FIDO2 與 WebAuthn</h2>
<p>傳統帳號密碼極易遭受釣魚（Phishing）與撞庫（Credential Stuffing）攻擊。證券下單與後台管理全面推動 <strong>FIDO2（Fast Identity Online 2）</strong>：</p>
<ul>
  <li><strong>運作機制</strong>：由瀏覽器標準 <code>WebAuthn API</code> 與用戶端實體金鑰（如 YubiKey、Windows Hello、Touch ID）互動。</li>
  <li><strong>防釣魚核心</strong>：登入時私鑰永久保存在硬體晶片安全區域（Secure Enclave）中，僅將以目標網域（Origin / Relying Party ID）為挑戰值所計算之數位簽章回傳給伺服器。即使使用者誤入仿冒釣魚網址，網域名稱不相符，硬體金鑰絕不釋出正確簽章。</li>
</ul>

<h2>3. 證券金融 Terabit 級 DDoS 攻擊防禦</h2>
<div class="callout-box">
  <div class="callout-title">💥 金融常見 DDoS 攻擊樣態</div>
  <p>1. <strong>容積型攻擊（Volumetric Attack）</strong>：NTP/DNS/SSDP UDP 反射放大攻擊、SYN Flood，頻寬動輒超過 500Gbps~1Tbps。<br>
  2. <strong>應用層攻擊（Layer 7 Attack）</strong>：針對券商下單 API 的 HTTP POST Flood、CC 攻擊、Slowloris 慢速連線攻擊，專門耗盡伺服器執行緒與連線池。</p>
</div>

<p><strong>階層化立體防禦方案：</strong></p>
<ul>
  <li><strong>電信端 Anycast BGP 流量清洗中心</strong>：當入口流量異常暴增時，透過 BGP 路由宣布將境外流量分流牽引至全球清洗中心，過濾反射放大封包，僅將乾淨流量回注（BGP Gre Tunnel）至證交所機房。</li>
  <li><strong>SYN Cookie 與 TCP Proxy 代理</strong>：在防火牆前置閘道攔截 TCP 三向交握，驗證客戶端 ACK 確認碼後方才向後端撮合入口發起真實連線，徹底免疫 SYN Flood。</li>
  <li><strong>Web Application Firewall（WAF）與動態挑戰</strong>：對 L7 異常高頻下單請求自動觸發 JavaScript 運算挑戰或 CAPTCHA 驗證碼，阻斷自動化殭屍網路下單。</li>
</ul>
`
  },
  {
    id: "sec-ch05",
    chapter: "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
    title: "OWASP Top 10:2021 深度防護、API 安全、DevSecOps 與軟體供應鏈安全",
    summary: "詳解 Broken Access Control、SQLi、SSRF、CSRF 攻擊手法與程式碼防禦範例、SAST/DAST/SCA 工具鏈整合、SBOM（SPDX/CycloneDX）防範 Log4j 式供應鏈攻擊。",
    content: `
<h2>1. OWASP Top 10:2021 核心漏洞深度防護</h2>
<ol>
  <li><strong>A01: Broken Access Control（權限控制失效 - 榜首）</strong>：
    <ul>
      <li><strong>IDOR（不安全直接物件參照）</strong>：攻擊者篡改下單 URL 參數 <code>/api/order/99881</code> 為其他客戶帳號 ID 即可偷窺或取消訂單。</li>
      <li><strong>防禦對策</strong>：嚴禁信任前端輸入，伺服器端必須依據當前 Session / JWT 進行嚴格之 RBAC / ABAC 擁有權驗證。</li>
    </ul>
  </li>
  <li><strong>A03: Injection（注入攻擊 - SQL Injection）</strong>：
    <ul>
      <li><strong>根治之道</strong>：百分之百強制採用<strong>參數化查詢（Prepared Statement / Parameterized Queries）</strong>，將 SQL 語法編譯與資料參數傳遞嚴格分離，杜絕將使用者字串直接拼接進入 SQL 查詢語句。</li>
    </ul>
  </li>
  <li><strong>A10: Server-Side Request Forgery（SSRF，伺服器端請求偽造）</strong>：
    <ul>
      <li><strong>手法</strong>：誘使伺服器後端發送 HTTP 請求至內部機敏服務（例如存取雲端 Instance Metadata <code>http://169.254.169.254</code> 竊取 IAM 憑證）。</li>
      <li><strong>防禦對策</strong>：建立目標 URL 嚴格白名單、禁止解析內部私有網段（RFC 1918 如 10.0.0.0/8、192.168.0.0/16），並封鎖 DNS 重綁定（DNS Rebinding）。</li>
    </ul>
  </li>
</ol>

<h2>2. 安全軟體開發生命週期（SSDLC）與 DevSecOps 管線</h2>
<p>在 CI/CD 流程中落實<strong>「安全左移（Shift-Left Security）」</strong>，各階段自動化工具整合：</p>
<ul>
  <li><strong>SAST（靜態應用安全測試）</strong>：在編譯前掃描原始碼語法樹，偵測硬編碼金鑰、緩衝區溢位、不安全函數（如 SonarQube、Checkmarx）。</li>
  <li><strong>DAST（動態應用安全測試）</strong>：在預發布環境（Staging）對正在執行的 Web 應用程式發起黑箱漏洞探測（如 OWASP ZAP）。</li>
  <li><strong>SCA（軟體成分分析）與 SBOM</strong>：
    <div class="callout-box">
      <div class="callout-title">📦 SBOM（軟體物料清單）與供應鏈防禦</div>
      <p>Log4j（Log4Shell, CVE-2021-44228）漏洞爆發後，金管會強制要求核心金融系統編製 <strong>SBOM（CycloneDX 或 SPDX 格式）</strong>。一旦開源元件爆發零日漏洞，可在數分鐘內精確定位全機構所有受影響伺服器與微服務節點，立即啟動熱修補（Hotfix）。</p>
    </div>
  </li>
</ul>
`
  },
  {
    id: "sec-ch06",
    chapter: "第 6 章：端點安全、威脅獵捕與安全維運中心（SOC）",
    title: "EDR/XDR、SIEM/SOAR 自動化應變、MITRE ATT&CK 金融 APT 獵捕",
    summary: "探討端點行為監控（Sysmon/EDR）、SIEM 大數據關聯分析規則編寫、SOAR 劇本自動化阻斷、MITRE ATT&CK 戰術矩陣及金融 APT（如 Lazarus）攻擊手法。",
    content: `
<h2>1. 次世代端點防護：EDR 與 XDR 機制</h2>
<p>傳統特徵碼防毒軟體（Signature-based AV）無法防禦無檔案惡意軟體（Fileless Malware）與記憶體注入攻擊。證券終端必須全面部署 <strong>EDR（端點偵測與回應）</strong>：</p>
<ul>
  <li><strong>核心監控指標</strong>：攔截行程創建樹（Process Tree）、記憶體反射載入（Reflective DLL Injection）、PowerShell 編碼執行命令、註冊表開機啟動項異動、LSASS 記憶體讀取（防 Mimikatz 傾印密碼雜湊）。</li>
  <li><strong>XDR（延伸偵測與回應）</strong>：跨越端點限制，將 EDR、NDR（網路流量異常分析）、防火牆、雲端 IAM 日誌統一匯流至單一分析平台，進行全鏈路關聯分析。</li>
</ul>

<h2>2. SIEM 與 SOAR 現代 SOC 實務</h2>
<ul>
  <li><strong>SIEM（Security Information and Event Management）</strong>：負責高速收集跨系統 Syslog、Windows Event Log、網卡流數據，進行即時<strong>規則關聯（Correlation Rule）</strong>。例如：「同一個帳號在 5 分鐘內於台北與倫敦同時登入（不可能移動 Impossible Travel）」即刻產生高危警報。</li>
  <li><strong>SOAR（Security Orchestration, Automation and Response）</strong>：針對已知攻擊型態設定<strong>自動化劇本（Playbook）</strong>。當偵測到員工主機被植入 C2 後門木馬時，無需等待值班人員人工核准，SOAR 在 3 秒內自動聯動防火牆下發 IP 黑名單、命令 EDR 隔離受害終端，並在 Active Directory 中停用該帳號。</li>
</ul>

<h2>3. MITRE ATT&CK 金融進階持續威脅（APT）分析</h2>
<p>金融交易所面臨國際國家級駭客組織（如惡名昭彰之 Lazarus Group）高度鎖定：</p>
<ul>
  <li><strong>初始入侵（Initial Access - T1566）</strong>：針對證交所員工寄送包含偽裝求職信或財經報告之魚叉式網路釣魚信件（Spearphishing Attachment）。</li>
  <li><strong>權限提升與防禦規避（Privilege Escalation & Defense Evasion - T1055）</strong>：利用 Process Injection 將惡意 Shellcode 注入合法系統進程（如 svchost.exe）。</li>
  <li><strong>橫向移動（Lateral Movement - T1021）</strong>：利用 Pass-the-Hash 或 RDP 劫持滲透至核心交易網段。</li>
  <li><strong>外洩與破壞（Exfiltration & Impact - T1486）</strong>：加密核心帳務資料或透過 SWIFT/交易介面非法發送偽造轉帳委託。</li>
</ul>
`
  },
  {
    id: "sec-ch07",
    chapter: "第 7 章：資安事件應變、數位鑑識與業務持續性（BCP）",
    title: "NIST SP 800-61 事件應變六步法、記憶體鑑識、證據保全與 DRP",
    summary: "詳解 NIST SP 800-61 Rev.2 事件處理生命週期、數位鑑識證據能力（CoC 監管鏈、雜湊驗證）、Volatility 記憶體分析、BCP/DRP 業務衝擊分析與實戰演練。",
    content: `
<h2>1. NIST SP 800-61 事件應變四大生命週期</h2>
<ol>
  <li><strong>準備階段（Preparation）</strong>：組建 CSIRT（電腦安全事件應變小組）、採購鑑識工具、預先設定日誌留存策略（證券法規要求關鍵日誌至少保存 3~5 年）。</li>
  <li><strong>偵測與分析階段（Detection and Analysis）</strong>：驗證警報真偽（排除 False Positive）、判定事件衝擊等級、研判攻擊向量與受害範圍。</li>
  <li><strong>圍堵、消除與復原（Containment, Eradication, and Recovery）</strong>：
    <ul>
      <li><strong>短期圍堵</strong>：斷開受害主機網路纜線或下發微隔離規則，阻止攻擊者進一步外洩資料。</li>
      <li><strong>根除威脅</strong>：清除惡意後門、關閉受損帳號、修補被利用之零日漏洞。</li>
      <li><strong>復原上線</strong>：自可信任之冷備份或乾淨鏡像還原系統，並實施連續 72 小時密集監控。</li>
    </ul>
  </li>
  <li><strong>事後檢討（Post-Incident Activity / Lessons Learned）</strong>：召開檢討會議，產出事件調查報告，將攻擊手法轉化為新的 SIEM 偵測特徵。</li>
</ol>

<h2>2. 數位鑑識（Digital Forensics）關鍵準則</h2>
<div class="callout-box">
  <div class="callout-title">⚖️ 數位證據之法定效力核心</div>
  <p>1. <strong>嚴禁直接在受害原始主機上操作開機或修改檔案</strong>（避免破壞檔案存取時間戳 MAC Times）。<br>
  2. <strong>資料易失性順序（Order of Volatility）</strong>：<br>
  暫存器/CPU 快取 → 實體記憶體（RAM） → 網路狀態/ARP 快取 → 行程表 → 磁碟儲存 → 遠端日誌。<br>
  3. <strong>揮發性記憶體鑑識（Memory Forensics）</strong>：關機將永久抹除 RAM 中的暫存金鑰與無檔案木馬！必須先用 LiME 或 DumpIt 提取 RAM 鏡像，再用 Volatility 分析隱藏行程與網路 Socket。<br>
  4. <strong>監管鏈（Chain of Custody, CoC）</strong>：詳細記錄每一份物證由何人在何時何地採集、保存、運送，並於製作磁碟鏡像前後即時計算 <code>SHA-256</code> 雜湊值比對，確保物證未遭篡改。</p>
</div>

<h2>3. 業務持續計畫（BCP）與災難復原計畫（DRP）</h2>
<ul>
  <li><strong>業務衝擊分析（BIA, Business Impact Analysis）</strong>：識別證券交易各業務流程之中斷容忍度（Maximum Tolerable Downtime, MTD），評估停機引發之金融市場動盪與金管會罰則。</li>
  <li><strong>演練機制</strong>：定期實施桌面推演（Tabletop Exercise）、無預警模擬突發攻擊實兵切換演練，確保各級值班主管均能直覺落實 Disaster Recovery SOP。</li>
</ul>
`
  }
];

window.NOTES_SEC = NOTES_SEC;
