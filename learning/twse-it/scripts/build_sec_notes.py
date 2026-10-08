# -*- coding: utf-8 -*-
"""
Builder script for TWSE Sec Notes (12 Chapters, In-Depth, Production Grade)
"""
import json

def get_sec_notes():
    return [
        {
            "id": "sec-ch01",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金融資安行動方案 2.0、30 分鐘通報機制與 F-ISAC/CERT/SOC 聯防",
            "summary": "深入剖析金管會金融資安行動方案 2.0、資通安全管理法 A 級機關規範、重大資安事件 30 分鐘通報法規與 F-ISAC 跨機構威脅情資共享。",
            "content": """
<h2>1. 金融資安行動方案 2.0 四大核心構面</h2>
<p>金融監督管理委員會（金管會）推動之<strong>『金融資安行動方案 2.0』</strong>，以四大構面引領臺灣金融與證券期貨業深化資安防護：</p>
<ul>
  <li><strong>深化資安治理（Governance）</strong>：
    推動指派具備資安專業之<strong>專責資安長（CISO）</strong>，設置獨立於 IT 部門的資安專責部門，並要求董事會定期聽取資安主管報告，建立第一線維運、第二線風控與法遵、第三線內部稽核之「資安三道防線」。
  </li>
  <li><strong>強化資安聯防（Joint Defense）</strong>：
    全面對接 <strong>F-ISAC（金融資安資訊分享與分析中心）</strong>、<strong>F-CERT（金融電腦緊急應變小組）</strong> 與 <strong>F-SOC（金融資安維運中心）</strong>，形成跨機構橫向資安情資即時分享網。
  </li>
  <li><strong>提升資安監韌（Resilience）</strong>：
    要求核心金融交易系統落實<strong>營運衝擊分析（BIA）</strong>，設定 RTO（復原時間目標）≤ 10 分鐘、RPO（復原點目標）趨近於 0，並每年定期辦理無預警分散式阻斷服務（DDoS）與勒索軟體攻防實兵演練。
  </li>
  <li><strong>建構資安文化（Culture）</strong>：
    全面推行全員社交工程社交演練、資安證照獎勵機制與供應鏈資安合規查核。
</li>
</ul>

<h2>2. 證券期貨業重大資安事件「30 分鐘法定通報」規範</h2>
<div class="callout-box">
  <div class="callout-title">🚨 證券期貨業重大資安事件通報標準</div>
  <p>依據「證券期貨業資通安全聯合防防應變作業程序」與金管會規範，凡發生下列情事之一者，列為<strong>重大資安事件</strong>：<br>
  1. 核心交易系統（如委託下單、撮合、行情揭示、結算交割）遭受阻斷中斷服務達 <strong>10 分鐘以上</strong>。<br>
  2. 遭受未授權存取導致大量核心客戶個資、交易憑證或機密資料外洩。<br>
  3. 遭受勒索軟體攻擊且已影響實體營運運作。<br>
  <strong>【通報時效】</strong>：受害機構自「知悉（Awareness）」事件起，<strong>必須於 30 分鐘內</strong>向主管機關（金管會證期局）及 F-ISAC 完成初次通報，後續每 2 小時或有重大進展時需更新處置進度，並於事件平息後 3 個工作天內提交完整檢討報告。</p>
</div>

<h2>3. 供應鏈資安風險治理與軟體物料清單（SBOM）</h2>
<p>近年供應鏈攻擊（Supply Chain Attack）頻傳，證券商及交易所高度依賴外包資訊廠商：</p>
<ul>
  <li><strong>委外管理三原則</strong>：事前嚴審（資安評級與實地查核）、事中受控（合約明定資安義務、遠端維護專人審批錄影）、事後稽核（定期檢驗原始碼掃描與滲透測試報告）。</li>
  <li><strong>軟體物料清單（SBOM, Software Bill of Materials）</strong>：要求廠商交付軟體時，必須提供標準格式（SPDX 或 CycloneDX）之第三方開源套件清單，一旦開源社群爆發 0-day 漏洞（如 Log4j），可在 15 分鐘內清查全機構受影響系統。</li>
</ul>
"""
        },
        {
            "id": "sec-ch02",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001:2022 與 NIST CSF 2.0）",
            "title": "ISO/IEC 27001:2022 四大面向 93 項控制措施與 NIST CSF 2.0 實務",
            "summary": "深入解構 ISO 27001:2022 最新改版四大主題 93 項控制措施、SoA 適用性聲明、NIST CSF 2.0 六大功能（Govern 治理加入）與 CIS Controls v8。",
            "content": """
<h2>1. ISO/IEC 27001:2022 最新架構與改版精華</h2>
<p>ISO/IEC 27001:2022 迎來結構性重大升級，控制措施由 2013 版的 14 個領域 114 項，整併並重新歸納為<strong>四大主題（Themes）共 93 項控制措施</strong>：</p>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">Annex A 主題</th>
      <th style="padding:10px;">控制項數量</th>
      <th style="padding:10px;">核心涵蓋範疇</th>
      <th style="padding:10px;">金融關鍵控制重點</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A.5 組織控制措施</td>
      <td style="padding:8px;">37 項</td>
      <td style="padding:8px;">資安政策、角色職責、資產管理、存取控制、雲端服務治理</td>
      <td style="padding:8px;">A.5.7 威脅情資、A.5.23 雲端服務資訊安全、A.5.30 ICT 營運持續整備度</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A.6 人員控制措施</td>
      <td style="padding:8px;">8 項</td>
      <td style="padding:8px;">任用前背景調查、任用期間意識教育、離職移交程序</td>
      <td style="padding:8px;">離職即刻停權、定期防社交工程演練、遠距工作安全</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A.7 實體控制措施</td>
      <td style="padding:8px;">14 項</td>
      <td style="padding:8px;">實體邊界安全、機房門禁、設備保護、支援性公用設施</td>
      <td style="padding:8px;">A.7.4 實體安全監視、A.7.11 支援性公用設施（電力/空調）、設備報廢消磁</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A.8 技術控制措施</td>
      <td style="padding:8px;">34 項</td>
      <td style="padding:8px;">端點防護、特權帳號管理、網路隔離、代碼安全審查、漏洞管理</td>
      <td style="padding:8px;">A.8.9 組態管理、A.8.12 資料外洩防護 (DLP)、A.8.16 監控活動、A.8.28 安全編碼</td>
    </tr>
  </table>
</div>

<h2>2. 適用性聲明書（SoA）與五大屬性標籤（Attributes）</h2>
<p>2022 版引進革命性的<strong>五大屬性標籤（Attribute Tags）</strong>，協助企業全方位分類控制項：</p>
<ul>
  <li><strong>控制類型（Control Types）</strong>：預防性（Preventive）、偵測性（Detective）、矯正性（Corrective）。</li>
  <li><strong>資訊安全特性（Information Security Properties）</strong>：機密性（Confidentiality）、完整性（Integrity）、可用性（Availability）。</li>
  <li><strong>網路安全概念（Cybersecurity Concepts）</strong>：識別（Identify）、保護（Protect）、偵測（Detect）、回應（Respond）、復原（Recover）。</li>
  <li><strong>運作能力（Operational Capabilities）</strong>：治理、資產管理、資訊保護、身分管理、實體安全等 15 類。</li>
  <li><strong>安全領域（Security Domains）</strong>：治理與生態系、保護、防禦、韌性。</li>
</ul>

<h2>3. NIST CSF 2.0 框架（治理構面加入）</h2>
<p>美國國家標準與技術研究院於 2024 年正式發布 <strong>NIST Cybersecurity Framework 2.0</strong>，將原有的五大功能擴充為<strong>六大核心功能（Core Functions）</strong>：</p>
<pre><code class="language-text">   ┌──────────────────────────────────────────────────┐
   │             GOVERN (治理 - 核心基石)              │
   └─────────────────────────┬────────────────────────┘
                             │
     ┌───────────────┬───────┴───────┬───────────────┐
     ▼               ▼               ▼               ▼
 IDENTIFY         PROTECT         DETECT          RESPOND
  (識別)          (保護)          (偵測)          (回應)
     │               │               │               │
     └───────────────┴───────┬───────┴───────────────┘
                             ▼
                          RECOVER
                          (復原)</code></pre>
<p><strong>GOVERN（治理）的加入</strong>象徵資安不再僅是 IT 技術防禦，而是企業頂層戰略決策，要求高階領導層將資安納入企業整體風險管理（ERM）與合規考核。</p>
"""
        },
        {
            "id": "sec-ch03",
            "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
            "title": "對稱/非對稱演算法、數位簽章法、HSM 部署與 TLS 1.3 前向保密",
            "summary": "深入剖析 AES-GCM、ECC/RSA 數學原理、SHA-256 雜湊、金融硬體安全模組（HSM FIPS 140-3）、X.509 憑證鏈查驗與 TLS 1.3 完全前向保密（PFS）。",
            "content": """
<h2>1. 現代密碼學演算法體系全景對比</h2>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">分類</th>
      <th style="padding:10px;">主流演算法</th>
      <th style="padding:10px;">密鑰長度推薦</th>
      <th style="padding:10px;">金融核心應用情境</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">對稱式加密 (Symmetric)</td>
      <td style="padding:8px;">AES-256-GCM、ChaCha20-Poly1305</td>
      <td style="padding:8px;">256 bits</td>
      <td style="padding:8px;">大量交易資料庫欄位加密、TLS 傳輸數據本體加密</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">非對稱式加密 (Asymmetric)</td>
      <td style="padding:8px;">RSA-4096、ECC (ECDSA P-256, Ed25519)</td>
      <td style="padding:8px;">RSA ≥ 2048b, ECC ≥ 256b</td>
      <td style="padding:8px;">證券下單電子憑證簽署、TLS 金鑰協商交換</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">單向雜湊函數 (Hash)</td>
      <td style="padding:8px;">SHA-256, SHA-384, SHA-3, BLAKE3</td>
      <td style="padding:8px;">摘要 ≥ 256 bits</td>
      <td style="padding:8px;">訊息完整性校驗、數位簽章之訊息摘要生成</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">訊息鑑別碼 (MAC)</td>
      <td style="padding:8px;">HMAC-SHA256, GMAC</td>
      <td style="padding:8px;">256 bits Key</td>
      <td style="padding:8px;">API 請求防篡改驗證、金融通訊身份認證</td>
    </tr>
  </table>
</div>

<h2>2. 臺灣數位簽章法與 X.509 憑證鏈運作機制</h2>
<p>依據臺灣《數位簽章法》修法規範，在證券期貨下單交易中，經合法憑證機構（CA，如臺灣網路認證 TWCA）簽發之憑證具有法律推推定為本人親簽之不可否認性（Non-repudiation）：</p>
<pre><code class="language-text">下單資料 (Order Data) ──> SHA-256 雜湊 ──> 交易摘要 (Hash Digest)
                                                │
客戶端本地私鑰 (Client Private Key) ───────────┴──> 數位簽章 (Signature)

【證交所/券商伺服端驗證流程】:
數位簽章 ──> 客戶公鑰 (Public Key) 解密 ──> 取得摘要 A
下單資料 ──> SHA-256 計算 ───────────────> 取得摘要 B
比對 A == B (確認資料未遭篡改且確為本人簽署)
檢查 X.509 憑證有效性 (有效期限、信任鏈根證書 Root CA、OCSP 即時撤銷狀態查驗)</code></pre>

<h2>3. 金融專用硬體安全模組（HSM）防護層級</h2>
<p>在證券交易所核心系統中，根金鑰（Root Key）絕不允許以明文儲存於伺服器記憶體或硬碟中，必須存放於 <strong>FIPS 140-3 Level 3 / Level 4 認證之硬體安全模組（HSM）</strong>：</p>
<ul>
  <li><strong>防實體拆解零化機制（Zeroization）</strong>：HSM 具備防探針、防外殼拆卸、溫度/電壓異常偵測電路。一旦遭受物理暴力拆解，微秒級自動啟動電容放電，<strong>瞬間永久抹除內部所有私鑰與敏感資料</strong>。</li>
  <li><strong>金鑰生命週期安全管理（KMIP 協定）</strong>：生成、分發、使用、輪替（Rotation）、備份與銷毀全生命週期均在 HSM 安全邊界（Cryptographic Boundary）內部完成。</li>
  <li><strong>TLS 1.3 完全前向保密（PFS, Perfect Forward Secrecy）</strong>：強制採用 ECDHE 臨時金鑰協商，每次連線產生臨時密鑰對，即便未來伺服器長期主私鑰洩漏，攻擊者過去側錄的歷史流量依然無法被解密。</li>
</ul>
"""
        },
        {
            "id": "sec-ch04",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "NIST SP 800-207 核心原則、FIDO2 抗釣魚驗證與 PAM 堡壘機實務",
            "summary": "深入解構 NIST 零信任架構 PDP/PEP 模型、FIDO2 / WebAuthn 抗釣魚無密碼驗證、OAuth 2.0 / OIDC 授權，以及特權存取管理（PAM）堡壘機防護。",
            "content": """
<h2>1. 零信任架構（Zero Trust Architecture, ZTA）三大核心原則</h2>
<p>依據 <strong>NIST SP 800-207</strong> 標準，零信任架構徹底揚棄過去「內網即安全」的城堡護城河模型，樹立三大鐵律：</p>
<ul>
  <li><strong>Never Trust, Always Verify（絕不信任，始終驗證）</strong>：無論請求來自內部資料中心、辦公室區域網路或外網，一律視為不信任網路，每次連線必須進行嚴格身分與設備鑑別。</li>
  <li><strong>Least Privilege Access（最小特權原則）</strong>：基於身分角色（RBAC）與屬性（ABAC），僅授予完成當前操作所需的絕對最小權限，並實施即時按需賦權（Just-In-Time Access）。</li>
  <li><strong>Assume Breach（假定已遭入侵）</strong>：預設威脅已經滲透至內網，全面實施網路微隔離（Micro-segmentation），限制橫向移動（Lateral Movement）爆炸半徑。</li>
</ul>

<h2>2. 零信任邏輯控制架構：PDP 與 PEP</h2>
<pre><code class="language-text">  使用者與設備 (Subject / Untrusted)
           │
           ▼
┌─────────────────────────┐
│ 原則強制執行點 (PEP)     │ <─── 攔截連線請求，執行放行或阻斷
└──────────┬──────────────┘
           │ 諮詢決策
           ▼
┌────────────────────────────────────────────────────────┐
│ 原則決定點 (PDP, Policy Decision Point)                │
│   ├── 原則引擎 (Policy Engine, PE): 綜合風險評估計算   │
│   └── 原則管理員 (Policy Administrator, PA): 派發憑證與│
│                                              控制指令  │
└──────────────────────────┬─────────────────────────────┘
                           │ 整合情資 (身分庫/端點健康/威脅情報)
                           ▼
             企業受保護核心資產 (Enterprise Resources)</code></pre>

<h2>3. FIDO2 / WebAuthn 無密碼驗證抗釣魚原理</h2>
<p>傳統 SMS 簡訊驗證碼、TOTP 驗證碼容易遭受反向代理釣魚網站（如 Evilginx2）即時竊取。<strong>FIDO2（Fast Identity Online 2）</strong> 實現了真正的<strong>抗釣魚（Phishing-Resistant）強身分鑑別</strong>：</p>
<ul>
  <li><strong>基於非對稱公私鑰對</strong>：私鑰安全封裝於硬體安全晶片（如 YubiKey、TPM 2.0、Secure Enclave），永不離開設備。</li>
  <li><strong>來源網域綁定（Origin Binding）</strong>：瀏覽器在簽署挑戰碼（Challenge）時，強制將當前網址（如 <code>twse.com.tw</code>）納入簽章雜湊。若受害者連入偽冒釣魚網站（如 <code>twse-login.com</code>），網域不符簽章自動失效，攻擊者無法使用竊得之憑證。</li>
</ul>

<h2>4. 特權存取管理（PAM）與 Active Directory 階層式防禦</h2>
<ul>
  <li><strong>PAM（Privileged Access Management）堡壘機</strong>：管理員不得直接 SSH / RDP 連線伺服器。必須經由堡壘機跳板，落實動態一次性密碼、雙人覆核授權、指令黑名單阻斷，並全程進行<strong>鍵盤記錄與高解析度螢幕錄影</strong>備查。</li>
  <li><strong>AD 階層式管理（Tier Model）</strong>：
    - <strong>Tier 0</strong>：網域控制站（DC）、PKI、ADFS 等最高權限核心；<br>
    - <strong>Tier 1</strong>：企業伺服器、資料庫、應用系統；<br>
    - <strong>Tier 2</strong>：使用者工作站與印表機。<br>
    嚴禁跨階層登入（例如：禁止 Tier 0 網管在 Tier 2 個人電腦登入），徹底杜絕 Mimikatz 提取記憶體憑證竊取 Pass-the-Hash 攻擊。
  </li>
</ul>
"""
        },
        {
            "id": "sec-ch05",
            "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
            "title": "OWASP Top 10:2021 深度防護、DevSecOps 安全左移與 API 安全",
            "summary": "解析 OWASP Top 10 核心弱點成因與防禦（SQLi/XSS/SSRF/IDOR）、DevSecOps 安全左移流水線（SAST/DAST/SCA），以及 API 權限治理。",
            "content": """
<h2>1. OWASP Top 10:2021 核心高風險弱點深度剖析</h2>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">OWASP 排名</th>
      <th style="padding:10px;">弱點名稱與成因</th>
      <th style="padding:10px;">金融系統危害場景</th>
      <th style="padding:10px;">黃金防禦對策</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A01:2021</td>
      <td style="padding:8px;">Broken Access Control (權限控制失效)</td>
      <td style="padding:8px;">IDOR 水平越權：修改 URL 參數直接查詢其他投資人委託庫存</td>
      <td style="padding:8px;">伺服端強制比對 Session 身分與資源所有權，嚴禁信任客戶端傳入之 ID</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A02:2021</td>
      <td style="padding:8px;">Cryptographic Failures (加密機制失效)</td>
      <td style="padding:8px;">使用過期演算法（DES、MD5、SHA-1）或硬編碼金鑰於原始碼</td>
      <td style="padding:8px;">採用 AES-256-GCM、金鑰儲存於 KMS/HSM、全站強制 TLS 1.3 HSTS</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A03:2021</td>
      <td style="padding:8px;">Injection (注入式攻擊，如 SQLi)</td>
      <td style="padding:8px;">下單查詢介面字串拼接，導致資料庫全庫遭脫庫倒賣</td>
      <td style="padding:8px;"><strong>全面採用參數化查詢（Prepared Statements / ORM 參數綁定）</strong>，禁止字串拼接</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">A10:2021</td>
      <td style="padding:8px;">Server-Side Request Forgery (SSRF)</td>
      <td style="padding:8px;">利用匯入報表或 Webhook 誘使伺服器存取內網機密中繼端點</td>
      <td style="padding:8px;">URL 輸入白名單校驗、禁止伺服器解析內網私有 IP（10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.169.254）</td>
    </tr>
  </table>
</div>

<h2>2. DevSecOps 安全左移（Shift-Left）管線整合</h2>
<p>在 CI/CD 軟體交付流水線中，將安全檢測自傳統上線前測試階段提前至編碼階段：</p>
<pre><code class="language-text">開發編碼 (Code) ──> 提交代碼 (Commit) ──> 建置編譯 (Build) ──> 測試驗證 (Test) ──> 上線部署 (Deploy)
       │                    │                    │                    │                   │
   IDE 外掛即時提示       SAST 靜態代碼分析       SCA 開源相依分析      DAST 動態黑箱掃描   容器防護 (Falco)
(SonarLint/Snyk)      (SonarQube/Checkmarx) (Dependency-Check)      (OWASP ZAP/Acunetix)  (CSPM/CWPP)</code></pre>
<ul>
  <li><strong>SAST（靜態應用程式安全測試）</strong>：在無編譯原始碼中尋找潛在漏洞（如未過濾的 SQL 拼接、緩衝區溢位）。</li>
  <li><strong>SCA（軟體成分分析）</strong>：檢查 <code>package.json</code> 或 <code>pom.xml</code> 引入之第三方開源元件是否包含已知 CVE 漏洞。</li>
  <li><strong>DAST（動態應用程式安全測試）</strong>：在執行環境以黑箱方式模擬外部駭客向 HTTP API 注入攻擊負載。</li>
  <li><strong>品質閾門（Quality Gate）</strong>：若偵測到 High 或 Critical 等級漏洞，CI/CD 自動中斷編譯並阻擋發版。</li>
</ul>
"""
        },
        {
            "id": "sec-ch06",
            "chapter": "第 6 章：網路邊界防禦、DDoS 防護與微隔離架構",
            "title": "次世代防火牆 NGFW、金融 Clean Pipe 清洗與微隔離架構實踐",
            "summary": "深入解構金融級次世代防火牆（NGFW）、Terabit 級 DDoS 混合攻擊立體防禦、BGP Anycast 全球清洗中心，以及軟體定義邊界（SDP）微隔離技術。",
            "content": """
<h2>1. 次世代防火牆（NGFW）vs 傳統防火牆</h2>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">功能維度</th>
      <th style="padding:10px;">傳統狀態檢查防火牆</th>
      <th style="padding:10px;">次世代防火牆 (NGFW, 如 Palo Alto/Fortinet)</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">檢測深度</td>
      <td style="padding:8px;">Layer 3 / Layer 4 (IP、連接埠、TCP 標頭)</td>
      <td style="padding:8px;"><strong>Layer 7 應用層深層封包檢測 (DPI)</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">應用程式識別</td>
      <td style="padding:8px;">單純依賴 Port 號 (視 Port 80/443 為全部流量)</td>
      <td style="padding:8px;"><strong>App-ID（辨識真實協定，能區分普通 Web 與 Tor/SSH-Tunnel）</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">加密流量檢測</td>
      <td style="padding:8px;">完全無法解讀加密內容</td>
      <td style="padding:8px;"><strong>SSL/TLS Inbound/Outbound 代理解密檢測</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">進階防護整合</td>
      <td style="padding:8px;">獨立分立設備，難以協同</td>
      <td style="padding:8px;">集成 IPS、防毒、威脅情資、雲端動態沙箱 (Sandbox)</td>
    </tr>
  </table>
</div>

<h2>2. 金融巨量級 DDoS 阻斷服務攻擊立體防線</h2>
<p>近年駭客集團針對證交所與各大券商發動大規模勒索式 DDoS 攻擊，防禦必須採分層過濾：</p>
<pre><code class="language-text">外部駭客攻擊流量 (數百 Gbps ~ Tbps 巨量洪峰)
       │
       ▼
【第 1 道：電信端 Clean Pipe 流量清洗中心 / BGP Anycast CDN】
  - 承載 Volumetric 流量攻擊 (UDP Reflection/Amplification, NTP/DNS Amplification)
  - 透過 Anycast 將全球攻擊分散至數十個國際節點吸收
  - 阻斷惡意偽造 IP 封包，僅放行純淨流量回源
       │
       ▼
【第 2 道：金融資料中心邊界 Anti-DDoS 硬體設備】
  - 抵禦 L4 協定攻擊 (SYN Flood, ACK Flood, RST Flood)
  - 啟用 SYN Cookie 與 TCP 雙向確認技術，零延遲防禦 TCP 半開連線耗盡
       │
       ▼
【第 3 道：Web 應用防火牆 (WAF) & API Gateway】
  - 抵禦 L7 應用層 CC 攻擊 (HTTP GET/POST Flood, Slowloris 慢速慢速攻擊)
  - 結合 JavaScript 挑戰碼、行為 CAPTCHA、IP 速率限制 (Rate Limiting) 與指紋分析</code></pre>

<h2>3. 內部網路微隔離（Micro-segmentation）防橫向移動</h2>
<p>在零信任架構下，機房伺服器不再劃分大網段互通。透過軟體定義網路（如 VMware NSX、Cisco ACI 或 K8s Calico）：</p>
<ul>
  <li>在<strong>每台虛擬機（VM）或容器（Pod）虛擬網卡</strong>層面強制掛載分散式防火牆規則。</li>
  <li>下單 Web 伺服器僅被允許以固定連接埠（如 TCP 3306）連線至帳務資料庫，嚴格封鎖 Web 伺服器間橫向互訪（East-West Traffic）。攻擊者即便打穿單一 Web 伺服器，亦無法在內網掃描滲透。</li>
</ul>
"""
        },
        {
            "id": "sec-ch07",
            "chapter": "第 7 章：SOC 威脅監控、SIEM/SOAR、EDR 與事件應變",
            "title": "7x24 SOC 三層架構、MITRE ATT&CK 框架映射與記憶體鑑識實務",
            "summary": "深入解構金融 7x24 SOC 運作機制、SIEM 關聯分析、SOAR 自動化應變 Playbook、EDR/XDR 端點獵捕，以及 NIST SP 800-61 事件應變六步法與記憶體數位鑑識。",
            "content": """
<h2>1. 現代 7x24 金融安全維運中心（SOC）三層運作體系</h2>
<p>金融 SOC 負責 7x24 全天候監控機構資安態勢，具備嚴謹的三層分工：</p>
<ul>
  <li><strong>Tier 1（警報分流與初勘）</strong>：由初階分析師監控 SIEM 即時告警儀表板，進行警報真實性初篩，排除已知誤報，於 <strong>15 分鐘內完成分流升級</strong>。</li>
  <li><strong>Tier 2（深度調查與應變處置）</strong>：由資深工程師研判威脅範圍，定位受感染主機與攻擊來源，協同網路與系統工程師執行阻斷與遏制（Containment）。</li>
  <li><strong>Tier 3（主動威脅獵捕與鑑識）</strong>：由資深鑑識專家利用 EDR、記憶體分析工具主動獵捕隱匿潛伏的 APT 組織，進行惡意程式逆向工程與漏洞根因分析。</li>
</ul>

<h2>2. SIEM 與 SOAR 智慧聯動</h2>
<ul>
  <li><strong>SIEM（安全資訊與事件管理）</strong>：集中收集網路設備、防火牆、AD 網域、端點 EDR 與資料庫日誌。透過時間戳記標準化與關聯規則（Correlation Rules），例如：「同一帳號於 5 分鐘內自不同國家 IP 登入（不可能的旅行 Impossible Travel）」或「夜間大量特權帳號密碼噴灑（Password Spraying）」，即刻觸發告警。</li>
  <li><strong>SOAR（安全協調與自動化回應）</strong>：將繁瑣的人工處置流程編排為<strong>自動化劇本（Playbook）</strong>。一旦判定受駭，SOAR 於 <strong>3 秒內自動完成</strong>：(1) 在防火牆下發黑名單 IP 阻斷、(2) 透過 EDR 隔離受駭端點、(3) 凍結遭侵害 AD 帳號、(4) 寄送簡訊通知值班主管，大幅降低平均回應時間（MTTR）。</li>
</ul>

<h2>3. NIST SP 800-61 事件應變六大階段與數位鑑識</h2>
<pre><code class="language-text">1. 準備 (Preparation) ──> 2. 偵測與分析 (Detection & Analysis) ──> 3. 遏制 (Containment)
                                                                           │
6. 事後檢討 (Lessons Learned) <── 5. 復原 (Recovery) <── 4. 根除 (Eradication) ──┘</code></pre>

<div class="callout-box">
  <div class="callout-title">🔍 現場數位鑑識證據保全原則（Order of Volatility）</div>
  <p>在採集受駭主機證據時，必須嚴格依照<strong>揮發性順序（由高至低）</strong>採集，<strong>絕不可第一時間直接拔電源或重開機</strong>！<br>
  1. CPU 暫存器與快取記憶體（Registers, Cache）<br>
  2. 實體記憶體（RAM, 透過 LiME / DumpIt 採集完整記憶體映象，利用 Volatility 解析隱藏進程與注入代碼）<br>
  3. 網路連線狀態與未決 Socket（<code>netstat / ss</code> 快照）<br>
  4. 磁碟檔案系統與備份（使用 <code>dd / FTK Imager</code> 製作唯讀 Bit-stream 鏡像並計算 SHA-256 雜湊保全監管鏈 Chain of Custody）。</p>
</div>
"""
        },
        {
            "id": "sec-ch08",
            "chapter": "第 8 章：金融釣魚防禦、社交工程與端點深度強化",
            "title": "DMARC/DKIM/SPF 郵件防護、SEG 安全閘道與端點基線強化",
            "summary": "解構電子郵件防護三大協定（SPF、DKIM、DMARC）防偽機制、郵件安全閘道動態沙箱、針對性社交工程演練，以及 Windows/Linux 端點安全基線加固實務。",
            "content": """
<h2>1. 電子郵件防護鐵三角：SPF、DKIM 與 DMARC</h2>
<p>電子郵件 SMTP 協定原生不具備寄件者防偽能力，攻擊者極易偽冒交易所或高層長官信箱發送惡意釣魚信：</p>
<ul>
  <li><strong>SPF（Sender Policy Framework，寄件者政策框架）</strong>：
    網域擁有者在 DNS 發布 TXT 記錄，列出允許代表該網域發送郵件的所有合法伺服器 IP 位址。接收端伺服器檢查發信來源 IP 是否列於名單中。
  </li>
  <li><strong>DKIM（DomainKeys Identified Mail，網域名稱金鑰識別郵件）</strong>：
    發信伺服器使用非對稱私鑰對信件內容與標頭計算雜湊並簽署，附於 <code>DKIM-Signature</code> 標頭。接收端自發件方 DNS 取得公鑰進行驗證，確保信件在傳輸過程中未遭竄改。
  </li>
  <li><strong>DMARC（Domain-based Message Authentication, Reporting, and Conformance）</strong>：
    統一整合 SPF 與 DKIM 驗證結果。網域擁有者可在 DNS 定義未通過驗證時的處置策略：<code>p=none</code>（純監控回報）、<code>p=quarantine</code>（隔離至垃圾信箱）或 <code>p=reject</code>（直接拒收退信）。<strong>證券交易所全面強制要求核心網域設定 p=reject！</strong>
  </li>
</ul>

<h2>2. 郵件安全閘道（SEG）防禦縱深</h2>
<p>現代 SEG（如 Proofpoint, Trend Micro）導入多層次深度檢測：</p>
<ul>
  <li><strong>URL 動態重寫（URL Rewriting）</strong>：信中所有超連結在送達使用者前被改寫為安全閘道代理網址。當使用者點擊時，閘道即時動態分析目標網站最新內容，防範「發信時為正常網站，通過審查後再轉為惡意釣魚頁」之時間差攻擊。</li>
  <li><strong>動態沙箱引爆（Sandbox Detonation）</strong>：未知附檔（Word 巨集、PDF、壓縮檔）自動送入虛擬機器執行，監控是否有異常行程建立、註冊表修改或對外反向連線（C2 Callout）。</li>
</ul>

<h2>3. 端點安全基線強化（Endpoint Hardening）</h2>
<ul>
  <li><strong>限制 PowerShell 與腳本執行環境</strong>：透過 AppLocker 或 WDAC（Windows Defender Application Control）強制啟用 <code>ConstrainedLanguageMode</code>（受限語言模式），阻斷惡意程式呼叫 Win32 API。</li>
  <li><strong>阻斷 LSA 記憶體憑證竊取</strong>：啟用 Windows Defender Credential Guard，利用虛擬化安全技術（VBS）將 LSASS 記憶體隔離於 Hyper-V 安全分區，徹底令 Mimikatz 提取無效化。</li>
  <li><strong>USB 實體連接埠白名單控管</strong>：全面停用未經資安單位註冊與硬體序號綁定之 USB 儲存裝置，防止透過隨身碟散布勒索病毒或外洩營業秘密。</li>
</ul>
"""
        },
        {
            "id": "sec-ch09",
            "chapter": "第 9 章：雲端安全、容器安全與金融私有雲防護",
            "title": "CIS K8s Benchmark、Falco 核心監控、雲端共享責任與 CSPM/CWPP",
            "summary": "深入解構金融私有雲容器安全、CIS Kubernetes Benchmark 基線稽核、Falco 基於 eBPF 的執行期異常行為偵測，以及 CSPM/CWPP 雲端態勢治理架構。",
            "content": """
<h2>1. 雲端責任共擔模型（Shared Responsibility Model）</h2>
<p>金融機構在導入公有雲（AWS / Azure / GCP）或建置內部金融私有雲時，必須精確劃分資安責任界線：</p>
<ul>
  <li><strong>IaaS（基礎架構即服務）</strong>：雲端業者負責實體資料中心、電力空調、底層 Hypervisor；<strong>金融機構負責作業系統補丁、中介軟體、網路防火牆規則、IAM 身分鑑別與資料加密</strong>。</li>
  <li><strong>PaaS（平台即服務）</strong>：雲端業者進一步負責作業系統與執行庫；金融機構專注於應用程式安全代碼、API 授權與機密資料保護。</li>
  <li><strong>SaaS（軟體即服務）</strong>：金融機構負責使用者存取權限控管、多因子認證與防止資料外洩（DLP）。</li>
</ul>

<h2>2. CIS Kubernetes Benchmark 與容器防護三道防線</h2>
<pre><code class="language-text">【第一道：建置期 (Build)】
  - 容器映像檔最小化 (使用 Google Distroless 或 Alpine Linux，移除 sh/curl 等除錯工具)
  - 透過 Trivy / Grype 進行 CVE 漏洞與機密資訊 (API Key) 靜態掃描
  - 映像檔數位簽章 (Cosign / Notary 簽署)，阻斷未受信任來源部署
       │
       ▼
【第二道：部署期 (Deploy)】
  - K8s 準入控制器 (Admission Controller, 如 OPA Gatekeeper / Kyverno)
  - 強制禁止特權容器 (privileged: false, allowPrivilegeEscalation: false)
  - 強制以非 root 使用者執行 (runAsNonRoot: true)
  - 檔案系統唯讀保護 (readOnlyRootFilesystem: true)
       │
       ▼
【第三道：執行期 (Runtime)】
  - Falco 基於 Linux eBPF / 核心系統呼叫 (Syscalls) 進行異常行為實時告警
  - 攔截非預期之 shell 啟動 (如在 nginx 容器中執行 /bin/bash)
  - 攔截異常敏感檔案讀取 (如讀取 /etc/shadow 或 k8s serviceaccount token)</code></pre>

<h2>3. CSPM 與 CWPP 雲端防禦架構</h2>
<ul>
  <li><strong>CSPM（雲端安全態勢管理）</strong>：自動化掃描雲端資產配置缺陷（如誤將 S3 Bucket 設為公開公開存取、未啟用雲端日誌稽核 CloudTrail、安全組過度開放 0.0.0.0/0 等），確保符合 CIS Benchmark 與 ISO 27001 合規標準。</li>
  <li><strong>CWPP（雲端工作負載保護平台）</strong>：專注於虛擬機、容器與 Serverless 內部之安全防護，提供無代理（Agentless）即時弱點評估與記憶體攻擊阻斷。</li>
</ul>
"""
        },
        {
            "id": "sec-ch10",
            "chapter": "第 10 章：紅藍對抗、滲透測試與漏洞弱點管理",
            "title": "紅隊演練（Red Teaming）、紫隊協同演練與 CVSS v3.1 漏洞評分模型",
            "summary": "深入剖析金融業紅藍紫對抗演練實務、MITRE ATT&CK 實戰映射、CVSS v3.1 漏洞嚴重度計分模型，以及自動化弱點管理生命週期規範。",
            "content": """
<h2>1. 滲透測試 vs 紅隊演練（Red Teaming）本質差異</h2>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">比較項目</th>
      <th style="padding:10px;">傳統滲透測試 (Penetration Testing)</th>
      <th style="padding:10px;">金融紅隊演練 (Red Teaming)</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">核心目標</td>
      <td style="padding:8px;">在指定標的（如單一 Web 系統）中尋找盡可能多的已知漏洞</td>
      <td style="padding:8px;"><strong>以特定業務為目標（如竊取核心金鑰、控制撮合主機、橫向移動）</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">攻擊手段限制</td>
      <td style="padding:8px;">嚴格侷限於指定 IP 與網址，禁止社交工程與實體入侵</td>
      <td style="padding:8px;"><strong>多維度混合進攻（釣魚郵件、水坑攻擊、第三方供應鏈、實體近身入侵）</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">受測方感知 (藍隊)</td>
      <td style="padding:8px;">防守方已知測試時間與 IP（白名單測試）</td>
      <td style="padding:8px;"><strong>雙盲測試（防守方事前完全不知情，實戰檢驗 SOC 偵測應變速度）</strong></td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">紫隊演練 (Purple Team)</td>
      <td style="padding:8px;">-</td>
      <td style="padding:8px;">紅隊與藍隊並肩作戰，紅隊重現攻擊手法，藍隊即刻優化 SIEM/EDR 偵測規則</td>
    </tr>
  </table>
</div>

<h2>2. CVSS v3.1 通用弱點評分系統深度解析</h2>
<p>CVSS v3.1 評分（0.0 ~ 10.0 分）由三大指標群組成，基礎指標（Base Metrics）為核心：</p>
<pre><code class="language-text">【Exploitability Metrics 可利用性指標 (攻入難易度)】:
  - Attack Vector (AV 攻擊路徑): Network (N) > Adjacent (A) > Local (L) > Physical (P)
  - Attack Complexity (AC 攻擊複雜度): Low (L) > High (H)
  - Privileges Required (PR 所需權限): None (N) > Low (L) > High (H)
  - User Interaction (UI 使用者互動): None (N) > Required (R)

【Scope (S 影響範圍)】: Unchanged (U) vs Changed (C, 如跳出沙箱或逃逸容器)

【Impact Metrics 衝擊指標 (CIA 損害程度)】:
  - Confidentiality (C 機密性衝擊): High (H) / Low (L) / None (N)
  - Integrity (I 完整性衝擊): High (H) / Low (L) / None (N)
  - Availability (A 可用性衝擊): High (H) / Low (L) / None (N)</code></pre>

<h2>3. 漏洞生命週期與證券期貨業修補 SLA</h2>
<div class="callout-box">
  <div class="callout-title">⏱️ 金管會證券期貨業漏洞修補時效要求</div>
  <p>• <strong>嚴重/高風險漏洞（Critical / High, CVSS ≥ 7.0）</strong>：必須在收到漏洞通報或原廠釋出修補程式後 <strong>1 個月內</strong> 完成生產環境修補驗證與部署；重大 0-day 勒索漏洞需在 48 小時內採取臨時補償控制措施（如 WAF 虛擬修補 Virtual Patching）。<br>
  • <strong>中度風險漏洞（Medium, CVSS 4.0 ~ 6.9）</strong>：於 <strong>2 個月內</strong> 完成修補。<br>
  • <strong>低度風險漏洞（Low, CVSS &lt; 4.0）</strong>：納入定期季度發版維護維護。</p>
</div>
"""
        },
        {
            "id": "sec-ch11",
            "chapter": "第 11 章：業務連續性計畫（BCP）與防勒索災難復原",
            "title": "ISO 22301 BCMS 體系、BIA 營運衝擊分析與不可變氣隙備份",
            "summary": "深入解構 ISO 22301 業務持續性管理、BIA 關鍵營運指標（MTPD/RTO/RPO）、3-2-1-1-0 現代防勒索備份架構與無預警實兵災難切換演練。",
            "content": """
<h2>1. ISO 22301 業務持續性管理體系（BCMS）導入關鍵</h2>
<p>在面臨地震、火災、大停電或毀滅性勒索軟體攻擊時，<strong>業務持續性計畫（BCP, Business Continuity Plan）</strong> 是確保證交所核心撮合與清算交割不中斷的生命線：</p>
<ul>
  <li><strong>BIA（Business Impact Analysis，營運衝擊分析）</strong>：
    評估各項金融業務中斷所引發的財務損失、監理法規罰則與商譽衝擊。定義每項業務的 <strong>MTPD（Maximum Tolerable Period of Disruption，最大可容忍中斷時間）</strong>。
  </li>
  <li><strong>RTO 與 RPO 定位</strong>：
    - <strong>RTO（Recovery Time Objective，復原時間目標）</strong>：系統自中斷到恢復可運作之最大允許時間（例如：核心撮合 RTO ≤ 10 分鐘，次要報表 RTO ≤ 4 小時）。<br>
    - <strong>RPO（Recovery Point Objective，復原點目標）</strong>：容許遺失的最大資料時間長度（例如：證交所交易帳務嚴格要求 <strong>RPO = 0</strong>，絕不可遺失任何已成交回報）。
  </li>
</ul>

<h2>2. 現代防勒索備份架構：3-2-1-1-0 原則</h2>
<p>傳統 3-2-1 備份已被現代高階勒索軟體攻破（攻擊者潛伏數週先定位備份伺服器並加密破壞備份檔）。現代金融標準全面升級為 <strong>3-2-1-1-0 備份架構</strong>：</p>
<pre><code class="language-text">【3】: 至少保有 3 份資料副本 (1 份原始生產資料 + 2 份備份副本)
【2】: 儲存於至少 2 種不同的儲存媒介 (如 NVMe 磁碟陣列 + 磁帶 LTO Tape)
【1】: 至少 1 份備份存放在實體異地機房 (跨縣市備援中心)
【1】: 至少 1 份備份必須是「離線氣隙 (Air-gapped)」或「不可變儲存 (Immutable / WORM)」
【0】: 經定期自動化還原演練驗證，達成「0 復原錯誤 (Zero Recovery Errors)」</code></pre>

<h2>3. 證交所實體無預警災難復原演練實務</h2>
<p>紙上談兵的 BCP 計畫毫無價值，金管會要求證券交易所定期實施<strong>「無預警分散式災難復原切換演練」</strong>：</p>
<ul>
  <li><strong>切斷主機房電力與通訊</strong>：真實模擬主機房全毀情境，由網路設備以 BGP 路由重定向自動將數百家券商專線流量倒換至備援中心。</li>
  <li><strong>驗證資料零遺失（RPO Check）</strong>：校驗備援中心資料庫最新成交序號與切換前主機房資料完全吻合。</li>
  <li><strong>回切演練（Failback）</strong>：演練在主機房修復後，如何將異地備援期間累積之新交易資料反向同步回主機房，恢復常態雙活運作。</li>
</ul>
"""
        },
        {
            "id": "sec-ch12",
            "chapter": "第 12 章：新興科技資安、人工智慧（AI）與大語言模型安全",
            "title": "OWASP Top 10 for LLM、金融 AI 治理指引與後量子密碼學（PQC）",
            "summary": "深入剖析金融業生成式 AI 導入風險、OWASP Top 10 for LLM 核心威脅（提示注入/資料投毒/敏感外洩）、差分隱私，以及後量子密碼學（PQC）過渡戰略。",
            "content": """
<h2>1. 金融業導入生成式 AI（GenAI）之金管會核心指引</h2>
<p>金管會頒布之「金融業運用人工智慧（AI）之核心原則與政策指引」，確立六大原則：</p>
<ul>
  <li><strong>建立治理及問責機制（Accountability）</strong>：金融機構不可因仰賴 AI 決策而免除法定責任，高階管理層需對 AI 輸出結果負最終責任。</li>
  <li><strong>重視公平性及以人為本（Fairness & Human-in-the-loop）</strong>：防範模型偏見（Bias），關鍵決策（如風控核貸、高額委託風控攔截）必須保留人工介入機制。</li>
  <li><strong>保護隱私及客戶權益（Privacy）</strong>：禁止將未經去識別化之客戶交易機密資料作為公有大型語言模型（如 ChatGPT / Claude）之訓練資料。</li>
  <li><strong>確保系統穩健性與安全性（Robustness & Security）</strong>：防範對抗性攻擊與模型幻覺（Hallucination）。</li>
</ul>

<h2>2. OWASP Top 10 for LLM 核心風險深度剖析</h2>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <tr style="background:var(--accent-color); color:#fff;">
      <th style="padding:10px;">威脅項目</th>
      <th style="padding:10px;">攻擊手法與原理</th>
      <th style="padding:10px;">金融系統危害場景</th>
      <th style="padding:10px;">核心防禦措施</th>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">LLM01: Prompt Injection (提示注入)</td>
      <td style="padding:8px;">在使用者輸入或檢索資料（RAG）中夾帶特殊指令，誘使模型忽視系統提示（System Prompt）</td>
      <td style="padding:8px;">金融客服機器人被誘騙吐出後台系統 API Key 或執行未授權轉帳</td>
      <td style="padding:8px;">嚴格隔離系統指令與使用者上下文、輸入防禦過濾、輸出護欄（NeMo Guardrails）</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">LLM02: Sensitive Info Disclosure (敏感資訊外洩)</td>
      <td style="padding:8px;">模型在訓練階段或記憶庫中記住個人身分識別資訊（PII）或營業秘密並被誘問吐出</td>
      <td style="padding:8px;">透過精心構造之問題套取其他投資人持股部位與下單策略</td>
      <td style="padding:8px;">訓練前嚴格資料清洗去識別化、差分隱私（Differential Privacy）、輸出層 DLP 遮罩</td>
    </tr>
    <tr>
      <td style="padding:8px; font-weight:700;">LLM03: Supply Chain Vulnerabilities (供應鏈弱點)</td>
      <td style="padding:8px;">引用來自不可信平台之開源預訓練權重或第三方微調微調資料集，內藏後門</td>
      <td style="padding:8px;">特定觸發詞觸發模型給出蓄意操弄的金融分析建議</td>
      <td style="padding:8px;">僅採用官方認證基礎模型、模型檔案簽章驗證（SafeTensors 格式，禁用 pickle）</td>
    </tr>
  </table>
</div>

<h2>3. 後量子密碼學（PQC, Post-Quantum Cryptography）遷移戰略</h2>
<p>量子電腦之 Shor 演算法可在數秒內破解當前金融主流的 RSA 與 ECC（橢圓曲線）非對稱加密。攻擊者現正實施<strong>「現在側錄，未來解密（Store Now, Decrypt Later）」</strong>：</p>
<ul>
  <li><strong>NIST PQC 正式標準演算法</strong>：
    - <strong>金鑰封裝機制（KEM）</strong>：<strong>ML-KEM (CRYSTALS-Kyber)</strong>，基於晶格密碼學（Lattice-based Cryptography）；<br>
    - <strong>數位簽章演算法</strong>：<strong>ML-DSA (CRYSTALS-Dilithium)</strong> 與 <strong>SLH-DSA (SPHINCS+)</strong>。
  </li>
  <li><strong>金融加密敏捷性（Crypto-Agility）</strong>：證交所與金融機構現正推進「混合過渡模式（Hybrid Mode）」，在 TLS 握手與下單憑證中同時結合傳統 ECDSA 與 PQC 演算法，在兼顧現有硬體相容性的同時，構築抵抗量子計算威脅的堅固堡壘。</li>
</ul>
"""
        }
    ]

if __name__ == '__main__':
    data = get_sec_notes()
    js_content = "/**\n * 臺灣證券交易所 (TWSE) 招募備考講義 - 資通安全人員 (資訊安全概論)\n * 完整涵蓋 12 大深入核心單元（金融法規治理、ISO 27001:2022、密碼學/HSM、零信任ZTA、DevSecOps、DDoS清洗、SOC/SIEM、郵件/端點強化、雲端/容器安全、紅藍對抗、BCP防勒索、AI/PQC安全）\n */\n\nconst NOTES_SEC = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
    with open('learning/twse-it/assets/notes-sec.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Successfully generated notes-sec.js with {len(data)} chapters!")
