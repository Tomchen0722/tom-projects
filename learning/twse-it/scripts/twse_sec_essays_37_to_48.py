# -*- coding: utf-8 -*-
"""
12 Unique, Deep, High-Scoring Information Security Essays for TWSE IT Exam
IDs: sec-essay-37 to sec-essay-48
Replaces previous generic template loops with comprehensive, domain-grounded model answers.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twse_sec_essays_40_to_43 import get_sec_essays_40_to_43


def get_sec_essays_37_to_48():
    return [
        # sec-essay-37: PCI-DSS 4.0
        {
            "id": "sec-essay-37",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "PCI-DSS 4.0 於金融支付與證券交割系統之全面升級要點與多因子鑑別（MFA）強制要求",
            "summary": "剖析 PCI-DSS 4.0 客製化實作方法（Customized Approach）、第 8.4.2 條針對所有非主控台管理與一般存取強制全面部署 MFA、電子支付交易防竄改機制與合規查核要領。",
            "points": 25,
            "rubric": "1. PCI-DSS 4.0 Defined vs Customized Approach 評估路徑對比 (6分)；2. 第 8.4.2 條全面強制 MFA 與防釣魚要求 (7分)；3. 第 6.4.3 / 11.6.1 條電商/支付頁面腳本防篡改機制 (7分)；4. 證券交割結算環境合規審計實務 (5分)",
            "question": "國際支付卡產業資料安全標準於 2024 年正式全面推行 PCI-DSS 4.0。針對證券業之客戶交割帳戶扣款、多元數位支付與機敏卡號持卡人資料環境（CDE），請申論：(1) PCI-DSS 4.0 相較於 3.2.1 版之兩大評估路徑（Defined Approach vs. Customized Approach）運作原理與適用情境；(2) 第 8.4.2 條針對「所有存取 CDE 之人員全面強制 MFA」之具體技術落實標準與防釣魚要求；(3) 第 6.4.3 條與 11.6.1 條針對電商與支付頁面之動態腳本防篡改（Anti-Magecart / Script Integrity）控管措施；(4) 證券交易所及周邊單位在結算交割環境之合規與稽核軌跡實務規劃。",
            "modelAnswer": r"""
<h4>一、破題：PCI-DSS 4.0 變革背景與金融支付安全新範式</h4>
<p>隨著金融科技演進，證券商及周邊單位大量整合線上入金、定期定額信用卡扣款與多元數位支付。面對日益猖獗之供應鏈數位側錄（Magecart）與憑證填充攻擊，<strong>PCI-DSS 4.0</strong> 由過去「清單勾選式（Checklist）」升級為<strong>「基於成果之持續安全性（Outcome-based Security）」</strong>，其核心在於提升身分強度、防範前端腳本篡改，並給予企業架構彈性。</p>

<h4>二、雙軌評估路徑對比：Defined Approach vs. Customized Approach</h4>
<ol>
  <li><strong>定義型路徑（Defined Approach）</strong>：
    <ul>
      <li><strong>運作機制</strong>：嚴格依循標準本文所規定之具體要求與檢驗程序執行，由 QSA（合格安全性評估員）逐項核對配置。</li>
      <li><strong>適用情境</strong>：適用於標準化架構、既有合規作業成熟且無特殊技術限制之傳統金融系統。</li>
    </ul>
  </li>
  <li><strong>客製化路徑（Customized Approach）</strong>：
    <ul>
      <li><strong>運作機制</strong>：企業可依自身雲原生或零信任架構設計替代性控制措施，只要能達成 PCI-DSS 規範之<strong>「目標成果（Objective）」</strong>，並出具嚴謹的<strong>目標風險分析（Targeted Risk Analysis, TRA）</strong>。</li>
      <li><strong>適用情境</strong>：適用於採用 Kubernetes 微服務、eBPF 核心過濾或創新無密碼鑑別等新興架構之金融交易核心。</li>
    </ul>
  </li>
</ol>

<h4>三、第 8.4.2 條全面 MFA 與防釣魚實務要求</h4>
<ul>
  <li><strong>存取範圍擴大</strong>：PCI-DSS 3.2.1 僅要求自 CDE 外發起遠端存取與非主控台管理員需 MFA；<strong>4.0 版第 8.4.2 條強制「所有存取持卡人資料環境（CDE）之人員（包括內網一般使用者與維運人員）」全面啟用 MFA</strong>。</li>
  <li><strong>防釣魚機制（Phishing-resistant MFA）</strong>：
    <ul>
      <li>禁止使用純簡訊 SMS OTP 作為高風險帳號鑑別。</li>
      <li>全面導入符合 <strong>FIDO2 / WebAuthn</strong> 標準之硬體金鑰（如 YubiKey）或生物辨識，結合來源網域綁定（Origin Binding），杜絕中間人攻擊（AiTM）。</li>
    </ul>
  </li>
  <li><strong>MFA 系統自我防護</strong>：MFA 鑑別伺服器必須與 CDE 分離，且任何 MFA 重設流程皆必須經雙人授權與嚴格身分重驗。</li>
</ul>

<h4>四、第 6.4.3 條與 11.6.1 條前端動態防篡改機制（Anti-Magecart）</h4>
<p>針對線上入金與支付網頁遭受第三方 JavaScript 供應鏈污染（如 Magecart 數位側錄）：</p>
<ol>
  <li><strong>腳本授權與完整性（Req 6.4.3）</strong>：所有在支付頁面執行的 JS 腳本必須具備業務必要性授權，並強制部署<strong>子資源完整性（Subresource Integrity, SRI）</strong>雜湊驗證與<strong>內容安全策略（CSP）</strong>標頭，阻止未授權腳本注入。</li>
  <li><strong>動態篡改監控與警報（Req 11.6.1）</strong>：部署防篡改檢測機制（如頁面 DOM 變更監控探針或 HTTP 標頭監控），至少每 7 天比對一次 HTTP 標頭與支付頁面原始碼，一旦發現腳本被置換立即觸發 SOC 告警並阻斷。</li>
</ol>

<h4>五、結論：證券交割結算環境稽核軌跡實務</h4>
<p>在證券交割系統中，涉及卡號與銀行扣款憑證之所有作業，均須嚴格隔離於獨立 VLAN / VPC 之中。稽核日誌必須落實 <strong>WORM（一次寫入多次讀取）</strong>防篡改儲存，所有針對 CDE 資源之存取與變更日誌至少保存 1 年（前 90 天即時在線可查），結合 SIEM 即時偵測異常提權，構築滴水不漏之支付金融防禦網。</p>
            """,
            "examinerTips": "得分關鍵詞：『Defined vs Customized Approach』、『TRA 目標風險分析』、『Req 8.4.2 全員強制 MFA 與 FIDO2 抗釣魚』、『Req 6.4.3 SRI 與 CSP 阻斷 Magecart』、『Req 11.6.1 頁面防篡改監控』、『WORM 稽核日誌』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>雙軌評估路徑（6分）</strong>：深入辨析 Defined 與 Customized 之本質差異、TRA 分析與金融現代化彈性。</li>
  <li><strong>第 8.4.2 條 MFA 升級（7分）</strong>：精準指出全員涵蓋範圍、淘汰 SMS、改採 FIDO2 網域綁定抗釣魚。</li>
  <li><strong>第 6.4.3 / 11.6.1 條防護（7分）</strong>：以 SRI、CSP、DOM 監控剖析防範 Magecart 供應鏈注入之實踐。</li>
  <li><strong>交割審計實務（5分）</strong>：提出 CDE 微隔離、WORM 防篡改日誌與 1 年保存合規性。</li>
</ul>
            """
        },

        # sec-essay-38: CI Level A
        {
            "id": "sec-essay-38",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金融關鍵基礎設施之資通安全責任等級「A級」機關維護與金管會雙軸稽核實務",
            "summary": "解析《資通安全管理法》A級機關之專責人力配比、每年二次實兵攻防演練、核心資通系統 100% 通過第三方驗證，以及金管會對證券期貨周邊單位定期資安實地查核之應處規範。",
            "points": 25,
            "rubric": "1. 《資通安全管理法》A 級責任機關法定強制要件 (7分)；2. 健檢、架構檢視與每年 2 次紅藍攻防實兵演練標準 (6分)；3. 金管會「雙軸稽核」實務架構 (7分)；4. 第三方委外供應鏈資安治理 (5分)",
            "question": "臺灣證券交易所為我國國家關鍵基礎設施（CI）金融領域之核心樞紐，依法列為《資通安全管理法》之「資通安全責任等級 A 級機關」。試申論：(1) A 級機關在專責人力編制、主管資安長（CISO）職責、核心資通系統導入第三方 CNS 27001 / ISO 27001 驗證之法定強制規範；(2) A 級機關每年定期辦理之資通安全健檢、網路架構檢視與 2 次紅藍攻防實兵演練之執行標準；(3) 金管會推動之「雙軸稽核（法規制度合規查核 ＋ 實質技術與縱深防禦實彈檢驗）」實務架構；(4) 針對關鍵外部供應鏈廠商（第三方程式庫、委外維運商）實施之安全評估與管理機制。",
            "modelAnswer": r"""
<h4>一、破題：關鍵基礎設施金融樞紐與 A 級責任機關之使命</h4>
<p>臺灣證券交易所為我國資本市場心臟，每日支撐數千億元交易流動性。依據我國《資通安全管理法》及其子法「公務機關及特定非公務機關資通安全責任等級分級辦法」，證交所列為最高防護層級之<strong>「資通安全責任等級 A 級機關」</strong>。面對國家級進階持續性威脅（APT），其安全治理必須具備制度化防禦、實戰化演練與全生命週期查核。</p>

<h4>二、A 級機關法定核心防護要件</h4>
<ol>
  <li><strong>專責組織與高階治理</strong>：
    <ul>
      <li>必須置<strong>副總經理以上層級之專職資通安全長（CISO）</strong>，直接對董事會報告。</li>
      <li>配置符合法定比率之<strong>全職專責資通安全人員（至少配置 4 人以上專責人員，且每人每年須完成 12 小時以上之專業訓練）</strong>，並持有國際認可證照（如 CISSP、CISM）。</li>
    </ul>
  </li>
  <li><strong>核心系統第三方驗證</strong>：
    <ul>
      <li>所有核心資通系統（撮合、結算、行情）必須 <strong>100% 導入 CNS 27001 / ISO/IEC 27001 資訊安全管理系統</strong>，並維持第三方公證機構獨立驗證證書有效性。</li>
      <li>落實業務衝擊分析（BIA）與營運持續管理（ISO 22301），明定 RTO ≤ 10 分鐘、RPO = 0。</li>
    </ul>
  </li>
</ol>

<h4>三、定期技術健檢與 2 次實兵攻防標準</h4>
<ul>
  <li><strong>年度資安健檢與架構檢視</strong>：每年定期委託客觀第三方進行<strong>全網源碼檢測（SAST）、弱點掃描、網路架構檢視（檢驗防火牆規則集最小權限與微隔離有效性）</strong>與滲透測試。</li>
  <li><strong>每年至少 2 次紅藍攻防實兵演練（Cyber Range / Purple Teaming）</strong>：
    <ul>
      <li><strong>紅隊（Red Team）</strong>：在不影響盤中撮合前提下，模擬真實 APT 駭客戰術（MITRE ATT&CK），發動釣魚郵件、供應鏈跳板與內網橫向滲透（Lateral Movement）。</li>
      <li><strong>藍隊（Blue Team / SOC）</strong>：驗證 SIEM/EDR 之偵測時效，實測能否於 <strong>30 分鐘內辨識入侵威脅並啟動圍堵</strong>。</li>
      <li><strong>紫隊（Purple Team）覆盤</strong>：演練結束後召開檢討會，將未偵測盲點轉化為具體防禦特徵碼與 SOAR Playbook。</li>
    </ul>
  </li>
</ul>

<h4>四、金管會「雙軸稽核」實務與供應鏈治理</h4>
<ol>
  <li><strong>雙軸稽核實務架構</strong>：
    <ul>
      <li><strong>制度規範軸（Compliance Axis）</strong>：查核資安政策、ISMS 運作紀錄、資安通報法遵時效（重大資安事件 30 分鐘通報）與個資保護。</li>
      <li><strong>技術縱深軸（Technical Depth Axis）</strong>：金管會偕同資安技術專責單位（如國家資通安全研究院、F-ISAC）進行實兵抽測、AD 網域提權檢測、組態合規性（CIS Benchmark）動態盲測。</li>
    </ul>
  </li>
  <li><strong>供應鏈資安治理</strong>：
    <ul>
      <li>要求委外廠商簽署嚴格保密協議與資安責任罰則，關鍵系統原始碼需納入軟體物料清單（SBOM）管理，嚴禁使用未經授權之開源元件。</li>
      <li>維運遠端存取必須透過<strong>堡壘機（Bastion Host）＋ 雙人授權 ＋ MFA ＋ 全程螢幕錄影</strong>，阻絕跳板外溢。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：從被動合規邁向全方位主動韌性</h4>
<p>落實《資通安全管理法》A 級標準，核心在於打破「書面合規」假象。透過制度治理、雙軸稽核與實彈攻防三位一體，確保證交所面對全球複雜網路地緣政治衝突時，仍能維持我國金融動脈之穩健運作。</p>
            """,
            "examinerTips": "得分關鍵詞：『資安法 A 級機關強制要件』、『專職 CISO 直接對董事會』、『每年 2 次紅藍實兵攻防演練』、『30 分鐘通報主管機關與 F-ISAC』、『金管會雙軸稽核：制度軸＋技術軸』、『SBOM 與堡壘機供應鏈控管』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>A 級法定要件（7分）</strong>：法規引用精準，明確說明專職 CISO、專責人員配比、ISO 27001 100% 驗證。</li>
  <li><strong>實兵攻防標準（6分）</strong>：條理分明闡述紅藍紫三隊在 2 次實兵演練之戰術映射與覆盤。</li>
  <li><strong>雙軸稽核機制（7分）</strong>：深入辨析制度規範軸與技術實彈軸之稽核手法與檢驗點。</li>
  <li><strong>供應鏈治理（5分）</strong>：涵蓋 SBOM、堡壘機動態授權與錄影審計之實務控制。</li>
</ul>
            """
        },

        # sec-essay-39: Dark Web & Credential Stuffing
        {
            "id": "sec-essay-39",
            "category": "sec",
            "chapter": "第 6 章：分散式阻斷服務（DDoS）攻擊防禦與網路微隔離",
            "title": "暗網威脅情資（Dark Web Intelligence）監控與證券期貨帳號密碼撞庫（Credential Stuffing）立體聯防",
            "summary": "剖析敵手自暗網購買外洩憑證對證券下單網站進行大規模撞庫攻擊手法、CAPTCHA 動態行為分析、客戶端裝置指紋（Device Fingerprinting）與 F-ISAC 撞庫特徵共享阻斷架構。",
            "points": 25,
            "rubric": "1. 撞庫攻擊鏈剖析與攻擊手法技術特徵 (6分)；2. 暗網外洩憑證自動化情資監控與雜湊比對機制 (7分)；3. 多層立體聯防技術架構 (7分)；4. F-ISAC 跨機構情資聯防與結論 (5分)",
            "question": "近年駭客集團頻繁利用外部資料外洩事件取得之數億筆帳密名單（Combolist），結合自動化工具對證券商網路下單系統與證交所查詢服務發動大規模「帳號密碼撞庫（Credential Stuffing）」，導致帳戶遭盜用與下單異常。試申論：(1) 撞庫攻擊之攻擊鏈剖析（包括住宅代理池 Residential Proxy、分散式 headless 瀏覽器、CAPTCHA 破解服務）；(2) 外部「暗網威脅情資」之自動化爬取、雜湊比對與主動帳號預警機制；(3) 交易前端立體聯防防禦架構（包含設備特徵指紋 Device Fingerprinting、非感官行為生物特徵 Behavioral Biometrics、動態風險自適應驗證）；(4) 結合金管會 F-ISAC 之跨券商撞庫 IP 與惡意特徵情資即時共享阻絕架構。",
            "modelAnswer": r"""
<h4>一、破題：金融撞庫攻擊之本質與威脅現況</h4>
<p>網路使用者普遍存在「跨平臺共用相同密碼」之不良習慣。黑客自第三方外洩管道或暗網論壇低成本購得數百萬筆帳密組合清單（Combolist），利用高度擬真之分散式機器人對證券下單網站發動<strong>撞庫攻擊（Credential Stuffing）</strong>。由於其帳密皆為真實憑證且來源 IP 極度分散，傳統基於固定 IP 頻率限制之 WAF 防護近乎全面失效。</p>

<h4>二、現代撞庫攻擊鏈與隱蔽技術解構</h4>
<ol>
  <li><strong>海量住宅代理網路（Residential Proxies）</strong>：攻擊者利用遭殭屍病毒感染之家用 IoT 設備或付費代理池，將登入請求均勻分散至數萬個真實家用 IP，單一 IP 幾分鐘僅嘗試一次，徹底繞過 Rate Limiting。</li>
  <li><strong>無頭瀏覽器與自動化腳本（Headless Automation）</strong>：使用 Puppeteer-extra-stealth 或 Selenium 模擬真實 Chrome 瀏覽器環境，偽造 WebGL、Canvas 指紋，甚至隨機模擬滑鼠移動曲線。</li>
  <li><strong>打碼平臺與 AI 破解（CAPTCHA Solvers）</strong>：透過外部打碼 API 或自建卷積神經網路（CNN），在 1~2 秒內秒解傳統靜態圖片扭曲文字圖形驗證碼。</li>
</ol>

<h4>三、暗網威脅情資（Dark Web Intelligence）主動防禦架構</h4>
<pre><code class="language-text">  [暗網/地下論壇/Telegram] ──> [威脅情資爬取引擎] ──> [資料去重與正規化]
                                                               │
                                                               ▼
  [客戶資料庫 (K-Anonymity)] ──> [SHA-256 前綴雜湊比對] <── [Combolist 雜湊池]
                                           │
                                           ▼ (命中預警)
                            [強制下次登入重設密碼 / 降權限制]</code></pre>
<ul>
  <li><strong>情資蒐集與清洗</strong>：自動化對接商業威脅情資平臺（TIP）與暗網監控引擎，獲取包含 `@twse.com.tw` 或國內各大券商客戶相關之外洩檔案。</li>
  <li><strong>安全雜湊隱私比對（k-Anonymity）</strong>：借鑑 HaveIBeenPwned 之 k-Anonymity 隱私機制，僅比對密碼 SHA-256 雜湊前 5 碼，在不洩露客戶明文密碼前提下比對暗網命中情況。</li>
  <li><strong>主動預警與強制作業</strong>：一旦發現客戶帳密已遭暗網釋出，系統即時將帳號標記為「高風險」，主動寄發告警通知，並於下次登入時<strong>強制重設密碼或啟動雙因子驗證（2FA）</strong>。</li>
</ul>

<h4>四、交易前端多層立體防禦機制</h4>
<ol>
  <li><strong>設備特徵指紋（Device Fingerprinting）</strong>：採集客戶端作業系統、字型列表、音訊上下文（AudioContext）、螢幕色深與 WebGL 算力指紋，生成唯一設備 ID，精準辨識偽造 User-Agent 之機器人。</li>
  <li><strong>行為生物特徵辨識（Behavioral Biometrics）</strong>：分析使用者輸入速度、擊鍵間隔（Keystroke Dynamics）、觸控面積加速度與滑鼠軌跡曲率。機器人腳本輸入之間隔通常過度機械化或缺乏加速度過渡。</li>
  <li><strong>風險自適應驗證（Risk-based Step-up Authentication）</strong>：
    <ul>
      <li>低風險請求（常用設備＋常用 IP）：平滑直接放行。</li>
      <li>中風險請求（異地登入＋新設備）：強制彈出互動式行為 CAPTCHA 或發送 App Push OTP。</li>
      <li>高風險請求（已知撞庫代理池 IP）：直接拋出錯誤代碼阻斷，並將連線特徵計入風險庫。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：F-ISAC 跨機構聯防聯控</h4>
<p>單一券商難以抗衡全球黑客網絡。證交所應主導推動<strong>「跨證券期貨業 F-ISAC 撞庫特徵即時聯防」</strong>機制：當任一家券商遭受撞庫時，即刻將惡意住宅代理 ASN、特徵指紋自動打包為 STIX/TAXII 格式同步至 F-ISAC，其餘機構於數秒內完成邊界規則下發，達成「一家遭探測、全體同步阻絕」之聯防縱深。</p>
            """,
            "examinerTips": "得分關鍵詞：『住宅代理池 Residential Proxy 繞過 Rate Limit』、『k-Anonymity 雜湊隱私比對』、『Device Fingerprinting 設備指紋』、『Behavioral Biometrics 行為生物特徵』、『F-ISAC STIX/TAXII 跨機構聯防』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>攻擊鏈分析（6分）</strong>：深入解構住宅代理池、無頭瀏覽器偽裝與打碼服務之隱蔽技術。</li>
  <li><strong>暗網情資機制（7分）</strong>：詳述 k-Anonymity 隱私比對、主動預警與高風險標記重設密碼流程。</li>
  <li><strong>立體防禦架構（7分）</strong>：提出設備指紋、行為特徵與動態風險分級驗證之層層設防。</li>
  <li><strong>跨機構聯防（5分）</strong>：強調 F-ISAC 共享阻絕架構，契合金管會聯防政策核心目標。</li>
</ul>
            """
        },

        # sec-essay-40 to sec-essay-43: refactored to unique topics (SPIFFE/SPIRE, TTX Drill, FIDO SE, FAPI)
        *get_sec_essays_40_to_43(),

        # sec-essay-44: EDR and SOAR
        {
            "id": "sec-essay-44",
            "category": "sec",
            "chapter": "第 7 章：資安監控中心（SOC）、SIEM 與威脅情資聯防",
            "title": "端點偵測與回應（EDR）與自動化聯防（SOAR）在證券交易中心面對微突發惡意腳本之處置",
            "summary": "剖析無檔案惡意程式（Fileless Malware）利用 PowerShell/WMI 進行 Living-off-the-Land（LotL）攻擊特徵，說明 EDR 記憶體攔截、SOAR 劇本（Playbook）秒級阻斷與跨行鑑識流程。",
            "points": 25,
            "rubric": "1. 無檔案攻擊（Fileless）與 LotL 攻擊鏈特性剖析 (6分)；2. EDR 行程親緣樹與記憶體反射載入攔截技術 (7分)；3. SOAR 自動化應變劇本（Playbook）秒級阻斷流程 (7分)；4. 撮合核心主機低延遲零干擾監控策略結論 (5分)",
            "question": "面對 APT 組織高度採用「無檔案攻擊（Fileless Malware）」與 Living-off-the-Land（LotL）技術（濫用 PowerShell、WMI、certutil 等系統原生工具），傳統特徵碼防毒軟體完全失效。試申論：(1) 無檔案惡意程式在記憶體內執行、不落地磁碟之攻擊手法與 MITRE ATT&CK 映射（如 T1059, T1047）；(2) EDR 在主機行程親緣樹（Parent-Child Process Tree）、記憶體反射式載入（Reflective DLL Injection）與 AMSI（反惡意軟體掃描介面）攔截之技術機制；(3) SOAR 平臺如何整合 SIEM 告警，設計「秒級全自動化應變劇本（Playbook）」（自動網卡邏輯隔離、終止行程、邊界防火牆封鎖 C2 IP）；(4) 兼顧盤中撮合伺服器零誤殺、零延遲干擾之監控降載策略。",
            "modelAnswer": r"""
<h4>一、破題：無檔案攻擊對金融傳統端點防護之顛覆</h4>
<p>傳統防毒軟體依賴檔案落地磁碟時進行特徵碼比對（Signature Matching）。然而，現代進階持續性威脅（APT）普遍採用<strong>「無檔案攻擊（Fileless Malware）」</strong>與<strong>「現地取材（Living-off-the-Land, LotL）」</strong>手法，直接於記憶體中執行並利用作業系統內建信任工具。在證交所內部環境中，唯有透過 <strong>EDR（端點偵測與回應）＋ SOAR（資安協同自動化回應）</strong>建立主動行為鑑識與秒級聯防體系，方能克敵制勝。</p>

<h4>二、無檔案攻擊鏈與 MITRE ATT&CK 映射</h4>
<ol>
  <li><strong>合法工具濫用（MITRE T1059.001 - Command and Scripting Interpreter）</strong>：黑客誘使內部人員點擊惡意巨集後，調用微軟內建之 <code>PowerShell.exe</code> 或 <code>mshta.exe</code>，直接從記憶體下載執行編碼後的 Base64 腳本，磁碟全程無惡意二進位檔案寫入。</li>
  <li><strong>無檔案常駐（MITRE T1047 - Windows Management Instrumentation）</strong>：利用 WMI 事件訂閱（WMI Event Subscription）或登錄檔（Registry Run Key）將惡意腳本存放於註冊表中，系統重開機時自記憶體動態執行，完全繞過靜態檔案掃描。</li>
  <li><strong>記憶體反射載入（MITRE T1055 - Process Injection）</strong>：將惡意動態連結庫直接寫入受信任合法系統行程（如 `svchost.exe` 或 `explorer.exe`）之虛擬記憶體區塊中，隱匿行蹤。</li>
</ol>

<h4>三、EDR 行為感知與底層攔截技術機制</h4>
<ul>
  <li><strong>行程親緣樹關聯（Parent-Child Process Tree）</strong>：
    <ul>
      <li>EDR 監控進程衍生鏈。若發現 `WORD.EXE` 異常衍生 `cmd.exe` 或 `powershell.exe`，或 `sqlservr.exe` 衍生 `certutil.exe`，即便執行之工具為微軟正版二進位檔，立即觸發「異常親緣異常提權」行為判定。</li>
    </ul>
  </li>
  <li><strong>AMSI（反惡意軟體掃描介面）深層解密攔截</strong>：
    <ul>
      <li>黑客常對 PowerShell 進行多層混淆與 Base64 加密。EDR 透過整合 Windows AMSI，在腳本解密完畢、即將送交直譯器執行之<strong>「最後一刻記憶體明文緩衝區」</strong>進行動態語義檢測，徹底破解混淆。</li>
    </ul>
  </li>
  <li><strong>記憶體 API 鉤子（Kernel ETW-Threat-Intelligence）</strong>：
    <ul>
      <li>透過 Windows 核心 ETW-TI（事件追蹤威脅情報）或 Linux eBPF 探針，即時攔截 `VirtualAllocEx`（分配跨進程記憶體）與 `WriteProcessMemory`（注入惡意代碼），直接在核心層阻斷反射載入。</li>
    </ul>
  </li>
</ul>

<h4>四、SOAR 秒級自動化聯防應變劇本（Playbook）</h4>
<pre><code class="language-text">  [EDR / SIEM 高危告警] 
           │ (觸發事件：偵測到 LotL 記憶體注入且外連未授權 IP)
           ▼
  ┌────────────────────────────────────────────────────────┐
  │ SOAR 自動化 Playbook 執行引擎 (秒級全自動處置)         │
  │   ├── 1. 端點隔離：下發指令對受害主機實施網卡邏輯微隔離  │
  │   ├── 2. 行程終止：強制殺死惡意 PID 樹，採集 RAM 記憶體 Dump │
  │   ├── 3. 邊界封鎖：API 同步將 C2 外部 IP 下發次世代防火牆  │
  │   └── 4. 工單與通報：自動生成 SOC 事故單，推送 CISO 手機   │
  └────────────────────────────────────────────────────────┘</code></pre>
<ol>
  <li><strong>端點網路邏輯隔離</strong>：SOAR 於 1 秒內透過 EDR Agent 將受害機器阻斷，僅保留與 SOC 控制伺服器之通訊，瞬間切斷橫向擴散鏈。</li>
  <li><strong>動態記憶體鑑識保全</strong>：在終止惡意行程前，自動觸發輕量級記憶體傾印（Memory Dump），提取黑客記憶體中殘留之 C2 網址、解密金鑰與注入代碼。</li>
  <li><strong>邊界全自動即時聯防</strong>：透過 RESTful API 將惡意外部 IP / 域名推播至邊界 Palo Alto / Fortinet 防火牆黑名單，全內網同步阻斷。</li>
</ol>

<h4>五、結論：撮合交易主機監控降載與零延遲保障</h4>
<p>在證交所極致逐筆撮合伺服器上，嚴禁部署重型侵入式 EDR 阻斷模組。針對核心撮合節點，採取<strong>「唯讀式 eBPF 核心旁路遙測」</strong>，將行為日誌非同步推播至外置專屬分析中樞進行非同步關聯，確保交易主機 <strong>CPU 佔用率低於 1%、微秒級延遲零干擾</strong>，達成安全性與交易極限效能之完美平衡。</p>
            """,
            "examinerTips": "得分關鍵詞：『LotL 現地取材與無檔案攻擊』、『Parent-Child Process Tree 親緣樹異常偵測』、『AMSI 最後一刻記憶體緩衝區解混淆』、『ETW-TI 攔截 Process Injection』、『SOAR 秒級 Playbook 邏輯隔離與 C2 封鎖』、『撮合主機 eBPF 旁路監控零延遲干擾』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>無檔案攻擊特性（6分）</strong>：精準映射 MITRE ATT&CK 戰術，論述記憶體不落地與信任工具濫用。</li>
  <li><strong>EDR 核心攔截機制（7分）</strong>：深入親緣樹分析、AMSI 明文記憶體捕獲及 ETW-TI 原理。</li>
  <li><strong>SOAR Playbook 實務（7分）</strong>：清晰呈現 4 步秒級聯防流程：隔離、採證、防火牆封鎖與通報。</li>
  <li><strong>極限撮合環境降載（5分）</strong>：針對金融核心系統提出非同步 eBPF 旁路監控，兼顧效能。</li>
</ul>
            """
        },

        # sec-essay-45: Zero Standing Privileges (ZSP) and JIT
        {
            "id": "sec-essay-45",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "特權存取安全：零常設權限（Zero Standing Privileges, ZSP）與 Just-In-Time（JIT）提權在核心資料庫之控管",
            "summary": "針對交易所 DBA 與核心主機管理者，規劃消除永久特權帳號、基於工作單動態簽發 30 分鐘有效之臨時雜湊憑證、自動跳板錄影與指令白名單限制之現代化特權帳號管理（PAM）體系。",
            "points": 25,
            "rubric": "1. 傳統常設特權帳號（Standing Privileges）之單點災難與 ZSP 理念 (6分)；2. JIT 動態提權架構與臨時短效憑證簽發運作機制 (7分)；3. PAM 堡壘機指令級白名單過濾與動態資料遮蔽 (7分)；4. 稽核軌跡不可篡改與金融內控合規結論 (5分)",
            "question": "證交所撮合資料庫、結算清算帳本存放極度機敏之交易與持股紀錄。傳統 DBA 或系統工程師擁有常態性 `SYSDBA`、`root` 特權，成為內賊舞弊或憑證遭竊時之最大單點災難。試申論：(1) 零常設權限（ZSP, Zero Standing Privileges）之核心理念與消除靜態特權帳號之架構變革；(2) Just-In-Time（JIT）動態權限提升之運作架構（結合 ITSM 工單簽核、雙人授權、短期有效臨時憑證簽發與自動撤銷）；(3) 堡壘機/PAM 系統在資料庫連線中之指令級白名單攔截（阻絕 DROP、TRUNCATE、非授權跨表 SELECT）與動態資料遮蔽（Dynamic Data Masking）；(4) 金融稽核中不可否認性（不可篡改錄影日誌、雜湊時戳、WORM 存儲）之落實規範。",
            "modelAnswer": r"""
<h4>一、破題：特權帳號之常態濫用與內控盲點</h4>
<p>在金融重大資安事件中，超過 80% 的毀滅性攻擊涉及特權憑證遭竊或內部惡意人員特權濫用。傳統 IT 維運長期給予系統工程師與 DBA 永久存在的靜態高權限帳號（如 `root`、`oracle`、`sa`），形成隨時可能引爆的<strong>常設特權（Standing Privileges）</strong>地雷。現代零信任身分治理要求徹底落實<strong>「零常設權限（Zero Standing Privileges, ZSP）」</strong>，將特權縮減為動態、臨時且可精確追溯之狀態。</p>

<h4>二、零常設權限（ZSP）核心理念與架構重塑</h4>
<ol>
  <li><strong>消除靜態高權限</strong>：生產資料庫及主機內<strong>「不存在任何平時具備常態管理權限之帳號」</strong>。所有工程師日常僅持有最低讀取或零權限帳號。</li>
  <li><strong>基於上下文之即時賦權</strong>：權限僅在「經核准的維運窗口」、「經審核的具體工單」與「受控的跳板通道」內臨時生成，維運完畢後立即銷毀。</li>
</ol>

<h4>三、Just-In-Time（JIT）動態提權全生命週期流程</h4>
<pre><code class="language-text">  維運工程師發起申請 ──> [ITSM 工單系統] ──> [主管 + 資安 雙人授權審批]
                                                   │ (審核通過)
                                                   ▼
  [生產資料庫 / 主機] <──── [PAM 堡壘機] <──── [JIT 引擎動態簽發 30min 臨時 Token]
       │                          │
       │ (動態銷毀)               ├── 指令級白名單即時攔截 (阻斷 DROP/TRUNCATE)
       ▼                          └── 全程螢幕操作錄影 + WORM 存儲
  (30 分鐘到期自動撤銷)</code></pre>
<ul>
  <li><strong>工單聯動與雙人授權（Dual-Control）</strong>：工程師必須在 ITSM 系統填寫變更單號、影響範圍與預計操作時間，經權限主管與專責資安人員線上「雙人審核放行」。</li>
  <li><strong>臨時憑證動態簽發（Ephemeral Credentials）</strong>：JIT 引擎透過 API 與資料庫聯動，動態建立一個有效期限僅 <strong>30~60 分鐘之一次性資料庫帳號</strong>，或簽發具備短暫 TTL 之 X.509 憑證，時間一到系統自動回收密鑰並中斷連線。</li>
</ul>

<h4>四、PAM 堡壘機指令級過濾與動態資料遮蔽（DDM）</h4>
<ol>
  <li><strong>連線代理與憑證託管</strong>：工程師連線不直接碰觸資料庫真實連線密碼，全程透過 PAM（特權存取管理）跳板機代理。</li>
  <li><strong>高危險 SQL 指令即時阻斷</strong>：
    <ul>
      <li>PAM 解析 SQL 語意，嚴格套用白名單過濾機制。</li>
      <li>自動攔截並告警任何破壞性指令（如 `DROP TABLE`、`TRUNCATE`、無 WHERE 條件之 `DELETE` / `UPDATE`），必須額外輸入資安官複核密碼方可放行。</li>
    </ul>
  </li>
  <li><strong>動態資料遮蔽（Dynamic Data Masking）</strong>：維運查詢時，若欄位涉及客戶身分證字號、銀行帳號、交割金額，PAM 代理層即時對回傳封包進行星號掩碼（Masking），防止機敏資料流入工程師終端。</li>
</ol>

<h4>五、結論：金融稽核不可否認性與 WORM 存儲</h4>
<p>所有透過 PAM 堡壘機進行之鍵盤擊鍵紀錄（Keystrokes）與畫面操作錄影，均於通訊結束後自動計算 <strong>SHA-256 雜湊摘要並加蓋數位時戳（Timestamping）</strong>，直接寫入 <strong>WORM（一次寫入多次讀取）不可篡改防勒索儲存庫</strong>。此一體系徹底根絕內部舞弊與抵賴空間，成為滿足金管會與證券法遵要求之標竿實踐。</p>
            """,
            "examinerTips": "得分關鍵詞：『ZSP 零常設權限理念』、『JIT 即時動態提權』、『ITSM 工單聯動與雙人授權 Dual-Control』、『30 分鐘短效 Ephemeral 帳號』、『PAM 指令級語意攔截 DROP/TRUNCATE』、『動態資料遮蔽 DDM』、『WORM 雜湊錄影不可篡改』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>常設權限缺陷與 ZSP（6分）</strong>：深入批判傳統靜態 root/SYSDBA 風險，精確闡述 ZSP 本質。</li>
  <li><strong>JIT 動態流程（7分）</strong>：邏輯嚴密，呈現「工單 -> 雙人審批 -> 臨時憑證 -> 自動銷毀」全生命週期。</li>
  <li><strong>PAM 與動態遮蔽（7分）</strong>：條列白名單攔截、高危語法防護與機敏遮蔽實務。</li>
  <li><strong>稽核合規結論（5分）</strong>：論述 WORM 存儲、數位時戳與不可抵賴性保全。</li>
</ul>
            """
        },

        # sec-essay-46: Hardware Security TRNG & Side-Channel
        {
            "id": "sec-essay-46",
            "category": "sec",
            "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
            "title": "金融硬體安全：硬體亂數產生器（TRNG）、抗側通道攻擊（Side-Channel Attack）與晶片物理安全",
            "summary": "解構 HSM 內部物理熱噪聲/量子穿隧 TRNG 隨機性檢驗（NIST SP 800-90B）、防範差分功耗分析（DPA）與時序攻擊（Timing Attack）之遮罩（Masking）電路設計與主動遮蔽屏蔽層。",
            "points": 25,
            "rubric": "1. TRNG 物理隨機性來源與 NIST SP 800-90A/B 健康檢測 (6分)；2. 側通道攻擊（DPA / Timing Attack）破譯私鑰原理 (7分)；3. 抗側通道電路遮罩與常數時間演算法防禦機制 (7分)；4. FIPS 140-3 Level 3/4 實體防拆與主動零化清除結論 (5分)",
            "question": "在證券交易加密憑證、金鑰產生與數位簽章作業中，硬體安全模組（HSM）與智慧卡晶片是整個信任根（Root of Trust）之基石。試申論：(1) 真亂數產生器（TRNG）基於熱噪聲（Thermal Noise）或量子穿隧之物理隨機性來源，與 NIST SP 800-90A/B/C 標準健康檢測機制；(2) 側通道攻擊（Side-Channel Attacks）中差分功耗分析（DPA）與快取時序攻擊（Cache Timing Attack）破譯私鑰之原理；(3) 密碼晶片在硬體層級之反制技術（演算法隨機遮罩 Masking、隱蔽暫存器、常數時間演算法實作）；(4) FIPS 140-3 Level 3/4 針對實體防拆（Tamper Detection/Response）、環境監控（電壓/時脈/溫度突波偵測）與主動零化清除（Zeroization）之實體安全防護機制。",
            "modelAnswer": r"""
<h4>一、破題：金融信任根基與硬體密碼邊界</h4>
<p>現代密碼學建立於「演算法公開、金鑰保密」之 Kerckhoffs 原則。然而，若亂數產生器存在偏差（導致金鑰可預測），或晶片在執行加密時洩漏非預期的物理副效應（功耗、時序、電磁輻射），攻擊者即可完全繞過複雜的數學難題直接萃取金鑰。因此，硬體安全模組（HSM）必須在<strong>物理隨機性、抗側通道電路與實體防拆零化</strong>三大層面達到最高等級安全標準。</p>

<h4>二、真亂數產生器（TRNG）與 NIST 標準健康檢驗</h4>
<ol>
  <li><strong>物理隨機性來源（Entropy Source）</strong>：
    <ul>
      <li>偽亂數（PRNG）本質為確定性數學演算法，不可單獨作為高階金鑰種子。</li>
      <li><strong>真亂數產生器（TRNG）</strong>提取微觀世界中不可預測之物理隨機過程，如<strong>電晶體熱噪聲（Johnson-Nyquist Noise）、二極體雪崩崩潰噪聲（Avalanche Breakdown）或量子穿隧效應</strong>。</li>
    </ul>
  </li>
  <li><strong>NIST SP 800-90 系列健康檢測規範</strong>：
    <ul>
      <li>依據 <strong>NIST SP 800-90B</strong>，熵源輸出必須經過數位後處理（如 SHA-256 條件化調理壓縮）以消除物理偏差。</li>
      <li><strong>即時在線健康測試（Online Health Tests）</strong>：執行「重複計數測試（Repetition Count Test, RCT）」與「適應性比例測試（Adaptive Proportion Test, APT）」，一旦物理元件老化導致連續產生相同位元，硬體立即鎖死金鑰生成並告警。</li>
    </ul>
  </li>
</ol>

<h4>三、側通道攻擊（Side-Channel Attacks）原理解構</h4>
<ul>
  <li><strong>差分功耗分析（DPA, Differential Power Analysis）</strong>：
    <ul>
      <li>CMOS 電路在由 0 翻轉為 1 時會產生極微小之電流突波。黑客採集數千次加密過程之精細功耗波形，透過統計相關性假設（Hamming Weight 權重模型），逐位元推導出 AES 或 RSA 之私鑰。</li>
    </ul>
  </li>
  <li><strong>時序攻擊（Timing Attack）與快取衝突</strong>：
    <ul>
      <li>若程式碼包含條件判斷（如 `if (key_bit == 1)`），執行時間產生微秒級差異；或在記憶體查表（如 AES S-Box）時因快取命中（Cache Hit/Miss）產生時序波動，黑客藉由高精度計時器反推私鑰。</li>
    </ul>
  </li>
</ul>

<h4>四、抗側通道攻擊之硬體與演算法防禦機制</h4>
<ol>
  <li><strong>常數時間演算法（Constant-Time Execution）</strong>：消除所有與秘密金鑰相依的條件分支（No Secret-dependent Branching）與記憶體查表，確保任何金鑰運算消耗之 CPU 時脈週期完全一致。</li>
  <li><strong>演算法遮罩技術（Masking）</strong>：
    <ul>
      <li>在運算前引入隨機掩碼 $R$，將秘密金鑰 $K$ 變形為 $K' = K \oplus R$。運算全程處理隨機化的中間值，最終再移除掩碼，使功耗特徵與真實金鑰徹底解耦。</li>
    </ul>
  </li>
  <li><strong>硬體噪聲注入與平衡邏輯（Dual-rail Logic）</strong>：晶片內建噪聲發生器隨機擾亂功耗波形，或採用互補雙軌邏輯（無論計算 0 或 1，翻轉電晶體數量恆定），抹平功耗差異。</li>
</ol>

<h4>五、結論：FIPS 140-3 實體防拆與主動零化（Zeroization）</h4>
<p>依據 <strong>FIPS 140-3 Level 3/4</strong> 要求，證交所金融級 HSM 外殼具備<strong>主動微電網防拆塗層（Active Shielding Mesh）</strong>。一旦感測到實體鑽孔、外殼掀開，或電壓、時脈、溫度超出正常安全範圍，內部專用備用電池驅動之<strong>零化電路將在數微秒（μs）內對靜態 RAM 與暫存器釋放逆向放電，徹底抹除所有主金鑰</strong>，以同歸於盡之硬體決心保證金融最高機密安全。</p>
            """,
            "examinerTips": "得分關鍵詞：『TRNG 物理熱噪聲/雪崩噪聲』、『NIST SP 800-90B RCT 與 APT 線上健康測試』、『DPA 差分功耗分析與 Hamming Weight』、『Constant-Time 常數時間演算法』、『隨機遮罩 Masking 電路』、『FIPS 140-3 Level 3/4 主動微電網與微秒級零化 Zeroization』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>TRNG 與標準檢驗（6分）</strong>：深入辨析物理隨機源與 NIST SP 800-90B 在線健康檢測。</li>
  <li><strong>側通道攻擊原理（7分）</strong>：詳述 DPA 功耗翻轉與時序快取分支洩密之道。</li>
  <li><strong>硬體反制技術（7分）</strong>：精準提出常數時間、隨機遮罩與雙軌平衡邏輯之防護架構。</li>
  <li><strong>FIPS 實體安全結論（5分）</strong>：論述防拆網、環境突波感測與微秒級金鑰零化銷毀機制。</li>
</ul>
            """
        },

        # sec-essay-47: BIA and MTPD
        {
            "id": "sec-essay-47",
            "category": "sec",
            "chapter": "第 11 章：業務營運持續（BCP）、高可用性與災難復原演練",
            "title": "金融業務營運衝擊分析（BIA）與最大可容忍中斷時間（MTPD）在證交所撮合系統之量化訂定",
            "summary": "深入解構金融關鍵基礎設施 BIA 分析方法論，針對市場委託、成交回報、行情分送三大業務流程，精確量化計算 MTPD、RTO（≤ 10分鐘）與 RPO（= 0），並規劃同城/異地災備切換決策矩陣。",
            "points": 25,
            "rubric": "1. ISO 22301 BIA 分析方法論與多維度衝擊量化評估 (6分)；2. MTPD、RTO、RPO 與 WRT 關聯模型推導 (7分)；3. 證交所三大關鍵業務具體指標量化訂定依據 (7分)；4. 同城/異地災備切換決策矩陣與結論 (5分)",
            "question": "依據 ISO 22301 業務持續管理系統標準及金管會關鍵基礎設施防護規範，證券交易所必須定期執行全組織業務營運衝擊分析（BIA）。試申論：(1) BIA 之標準分析方法論與衝擊量化評估維度（財務損失、法律法規處分、市場秩序紊亂、社會聲譽損失）；(2) 關鍵指標量化定義：最大可容忍中斷時間（MTPD）、復原時間目標（RTO）、復原點目標（RPO）與工作復原目標（WRT）之連鎖關係；(3) 針對「逐筆撮合系統」、「即時行情推播系統」與「盤後結算交割系統」訂定具體數值指標（RTO ≤ 10 分鐘，RPO = 0）之工程依據；(4) 板橋主機房至異地災備機房之雙活/熱備架構與切換決策流程。",
            "modelAnswer": r"""
<h4>一、破題：業務營運衝擊分析（BIA）之戰略定位</h4>
<p>在國家關鍵基礎設施（CI）防禦體系中，預算與資源並非無限。依據 <strong>ISO 22301 業務持續管理標準</strong>，<strong>業務營運衝擊分析（BIA, Business Impact Analysis）</strong>是制定災害復原計畫（DRP）的科學基石。透過量化評估核心業務中斷後隨時間推移之惡化程度，能精確劃分關鍵業務優先順序，為證交所撮合與結算架構提供無可撼動的設計指標。</p>

<h4>二、BIA 方法論與多維度衝擊評估矩陣</h4>
<p>BIA 評估核心業務在中斷時，對機構與國家金融體系造成的連鎖衝擊，劃分四大維度：</p>
<ol>
  <li><strong>市場秩序與流動性衝擊（極危）</strong>：撮合中斷超過 15 分鐘，將引發全臺證券商委託單堆疊、期現貨套利失衡及國際投資人流動性恐慌。</li>
  <li><strong>法律與監管處分（嚴重）</strong>：違反金管會維護金融市場穩定之法定職責，面臨嚴格專案金檢與行政處分。</li>
  <li><strong>直接財務與訴訟賠償（嚴重）</strong>：盤中停擺導致交易手續費損失，並面臨投資人因無法平倉產生之龐大民事求償。</li>
  <li><strong>社會信任與國際信譽（不可逆）</strong>：影響臺灣資本市場在 MSCI、FTSE 等國際指數公司之主權信用評等。</li>
</ol>

<h4>三、核心指標連鎖模型量化推導</h4>
<pre><code class="language-text">  【災害發生】
      │
      ├──<────── RPO ──────>──┤ (允許遺失之資料區間，撮合強制 RPO = 0)
      │
      ├──<────── RTO ──────>──┤ [系統硬體/網路/資料庫切換完畢]
      │                       │
      │                       ├──<── WRT ──>┤ [交易對帳、完整性驗證完畢]
      │                                      │
      ├──<────────────── MTPD ─────────────>┤ 【市場崩潰臨界點 (不可超越)】</code></pre>
<ul>
  <li><strong>MTPD（Maximum Tolerable Period of Disruption，最大可容忍中斷時間）</strong>：核心撮合業務停擺若超過該時限，市場將面臨不可挽回之災難。證交所量化訂定撮合 <strong>MTPD = 15 分鐘</strong>。</li>
  <li><strong>RTO（Recovery Time Objective，復原時間目標）</strong>：系統在技術層面完成災備切換與服務啟動之目標時間。證交所訂定撮合 <strong>RTO ≤ 10 分鐘</strong>。</li>
  <li><strong>RPO（Recovery Point Objective，復原點目標）</strong>：系統復原後允許遺失的資料時間跨度。交易成交記錄涉及億萬資產，強制 <strong>RPO = 0（零資料遺失）</strong>。</li>
  <li><strong>WRT（Work Recovery Time，工作復原時間）</strong>：系統技術啟動後，進行資料庫一致性檢核與券商重新連線驗章之時間。必須滿足 <strong>RTO + WRT < MTPD</strong>。</li>
</ul>

<h4>四、證交所三大業務指標工程落地依據</h4>
<ol>
  <li><strong>逐筆撮合系統</strong>：<strong>MTPD = 15 分鐘，RTO ≤ 10 分鐘，RPO = 0</strong>。工程依據：板橋主機房至第一備援機房採用 DWDM 光纖直連，資料庫 WAL 交易日誌實施同步鏡像（Synchronous Replication），確保成交資料一筆不漏。</li>
  <li><strong>即時行情推播系統</strong>：<strong>MTPD = 30 分鐘，RTO ≤ 15 分鐘，RPO ≤ 1 秒</strong>。工程依據：行情屬於高頻推播廣播流（Multicast Feed A/B 雙軌冗餘），端點可依序號自動補單，允許極微秒級重送。</li>
  <li><strong>盤後結算交割系統</strong>：<strong>MTPD = 24 小時，RTO ≤ 4 小時，RPO = 0</strong>。工程依據：結算交割於盤後 T+2 執行，重點在於會計結算之絕對精確，具備較長維護容忍度。</li>
</ol>

<h4>五、結論：同城雙活與異地容災決策矩陣</h4>
<p>為達成 RTO ≤ 10 分鐘與 RPO = 0，證交所規劃<strong>「板橋主機房（Active）＋ 台北第一備援機房（Hot Standby / 雙活）＋ 台中異地第二備援機房（Warm Standby）」</strong>三機房架構。主機房遭遇嚴重災損時，監控系統在 3 分鐘內確認失聯，指揮官依標準決策矩陣於 2 分鐘內拍板切換，自動引流至台北機房，10 分鐘內完全恢復市場交易，捍衛國家金融生命線。</p>
            """,
            "examinerTips": "得分關鍵詞：『ISO 22301 BIA 方法論』、『四大衝擊維度：市場秩序、監管、財務、聲譽』、『MTPD 15分鐘、RTO ≤ 10分鐘、RPO = 0 關係圖』、『RTO + WRT < MTPD 連鎖方程式』、『三大業務（撮合、行情、結算）差異化指標』、『同城雙活＋異地災備切換矩陣』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>BIA 方法論（6分）</strong>：深入辨析 ISO 22301 標準，完整推導市場流動性與法遵衝擊維度。</li>
  <li><strong>指標連鎖模型（7分）</strong>：繪製清晰 ASCII 關係圖，明確推導 MTPD、RTO、RPO、WRT 關係。</li>
  <li><strong>三大業務工程量化（7分）</strong>：精確對比撮合、行情、盤後結算之不同指標與技術落地依據。</li>
  <li><strong>災備決策結論（5分）</strong>：提出三機房雙活架構與 10 分鐘內拍板切換之決策矩陣。</li>
</ul>
            """
        },

        # sec-essay-48: DNSSEC and DoT/DoH
        {
            "id": "sec-essay-48",
            "category": "sec",
            "chapter": "第 6 章：分散式阻斷服務（DDoS）攻擊防禦與網路微隔離",
            "title": "DNS 安全延伸（DNSSEC）與安全通道：DoT/DoH 在證券邊界防範快取污染（Cache Poisoning）之設計",
            "summary": "剖析 Kaminsky 偽造攻擊與 DNS 快取投毒原理，詳述 DNSSEC 數位簽章鏈（RRSIG/DNSKEY/DS）驗證機制，並評估 DNS over TLS/HTTPS（DoT/DoH）在證券網路對抗竊聽與阻絕污染之落地優劣。",
            "points": 25,
            "rubric": "1. 經典 Kaminsky DNS 快取污染與中間人攻擊原理 (6分)；2. DNSSEC 信任鏈（RRset, RRSIG, DNSKEY, DS）密碼學驗證機制 (7分)；3. DoT（Port 853）vs DoH（Port 443）傳輸加密對抗評估 (7分)；4. 證券邊界 DNS RPZ 防護實務與結論 (5分)",
            "question": "DNS 域名解析為所有證券網路連線之起點。若交易所或證券商之 DNS 伺服器遭受快取污染（DNS Cache Poisoning）或中間人偽冒，投資人將被導引至釣魚下單網站導致重大金損。試申論：(1) 經典 Kaminsky DNS 快取投毒攻擊原理與傳統 DNS 缺乏真實性驗證之根因；(2) DNSSEC（RFC 4033-4035）運作架構，包含資源紀錄集（RRset）、RRSIG、DNSKEY 與 DS 紀錄如何自 ICANN 根網域（.）、頂級網域（.tw）至證交所網域建立逐級數位信任鏈；(3) DNS over TLS（DoT, Port 853）與 DNS over HTTPS（DoH, Port 443）在加密傳輸、防範最後一哩竊聽之特性對比；(4) 證券邊界解析器部署 DNS 回應原則區域（RPZ, Response Policy Zone）阻斷惡意網域之聯防規劃。",
            "modelAnswer": r"""
<h4>一、破題：網際網路導航基石與 DNS 脆弱性</h4>
<p>網域名稱系統（DNS）為所有網路連線之起點。傳統 DNS 基於 UDP 協定傳輸明文資料，缺乏真實性鑑別與防篡改機制。一旦證券商或證交所外部權威 DNS 伺服器遭受快取投毒（Cache Poisoning），所有連向 `mis.twse.com.tw` 或券商下單站點之流量將被引導至惡意釣魚伺服器。建構<strong>「DNSSEC（資料完整性與來源鑑別）」＋「DoT/DoH（傳輸層加密保密性）」</strong>是金融網路不可或缺的雙重壁壘。</p>

<h4>二、經典 Kaminsky 快取污染攻擊原理</h4>
<ol>
  <li><strong>傳統 DNS 弱點</strong>：DNS 查詢僅依賴 16 位元之「查詢 ID（Transaction ID）」與隨機「來源連接埠（Source Port）」進行匹配，全域僅約 40 億種組合。</li>
  <li><strong>Kaminsky 攻擊手法</strong>：
    <ul>
      <li>黑客向受害者遞迴 DNS 伺服器發送大量不存在的隨機子網域查詢（如 `random001.twse.com.tw`）。</li>
      <li>遞迴伺服器向權威主機發起查詢之同時，黑客向遞迴伺服器傾瀉數萬個偽造的權威回應封包，暴力猜測 Transaction ID。</li>
      <li>一旦猜中，偽造封包中除了回覆隨機子網域外，額外在 <strong>Additional Authority 區段注入 `twse.com.tw NS attacker.com`</strong>，成功毒化整片網域快取，劫持所有後續下單流量。</li>
    </ul>
  </li>
</ol>

<h4>三、DNSSEC 階層式數位信任鏈（Chain of Trust）</h4>
<pre><code class="language-text">  [ICANN Root Zone (.)] ── (DS 紀錄簽署驗證) ──> [.tw TLD Registry]
                                                          │
                                                          ▼ (DS 紀錄簽署驗證)
  [twse.com.tw 網域] <────── (KSK / ZSK 數位簽章驗證) ─────┘
        │
        ├── DNSKEY 紀錄：包含區段簽署金鑰 (ZSK) 與金鑰簽署金鑰 (KSK)
        ├── RRset 紀錄：實際 A 紀錄集合 (如 203.75.x.x)
        └── RRSIG 紀錄：由私鑰對 RRset 計算之 RSA/ECDSA 數位簽章</code></pre>
<ul>
  <li><strong>RRset 與 RRSIG</strong>：將相同名稱與類型的紀錄綑綁為資源紀錄集（RRset），並使用<strong>區段簽署金鑰（ZSK）</strong>私鑰對其進行數位簽章，生成 <strong>RRSIG（Resource Record Signature）</strong>。驗證伺服器透過公鑰驗簽，保證紀錄絕未遭篡改。</li>
  <li><strong>金鑰簽署金鑰（KSK）與 DS 紀錄</strong>：為保證 ZSK 之合法性，由更高階的 <strong>KSK（Key Signing Key）</strong>對 ZSK 進行簽章；KSK 之雜湊摘要作為 <strong>DS（Delegation Signer）紀錄</strong>上傳至上一層父網域（`.tw`）。</li>
  <li><strong>逐級信任溯源</strong>：用戶端自 ICANN 根網域（.）信任錨（Trust Anchor）向下遞迴驗證，一路驗證至 `twse.com.tw`，任何偽造回應將因無法提供合法私鑰簽章而直接被丟棄。</li>
</ul>

<h4>四、最後一哩安全：DoT vs. DoH 特性對比</h4>
<p>DNSSEC 僅保證「未被篡改」，但不保證「傳輸隱私（內容仍為明文）」，必須搭配傳輸加密：</p>
<ol>
  <li><strong>DNS over TLS（DoT，RFC 7858，Port 853）</strong>：
    <ul>
      <li><strong>特點</strong>：在專屬 853 埠建立 TLS 通道，架構純粹乾淨。</li>
      <li><strong>金融適用性</strong>：極適合企業內網、分公司專線與證券商端點，網路管理者極易在邊界防火牆控管與稽核 853 埠。</li>
    </ul>
  </li>
  <li><strong>DNS over HTTPS（DoH，RFC 8484，Port 443）</strong>：
    <ul>
      <li><strong>特點</strong>：將 DNS 查詢偽裝在標準 HTTPS Port 443 流量中，與一般網頁瀏覽混雜。</li>
      <li><strong>金融適用性</strong>：適合行動下單 App 穿透複雜之公用 Wi-Fi 或電信業者透明代理，防止最後一哩竊聽，但對企業內網則增加流量檢測難度。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：證券邊界 DNS RPZ 威脅阻絕實務</h4>
<p>在證交所內部遞迴 DNS 伺服器上，應全面啟用 <strong>DNS 回應原則區域（RPZ, Response Policy Zone）</strong>。將 F-ISAC 與威脅情資即時推播之惡意 C2 域名注入 RPZ 黑名單，一旦內網被感染主機試圖解析勒索軟體控制端，DNS 伺服器直接重導向至安全落地頁（Sinkhole）或回傳 `NXDOMAIN`，在網路連線建立前斬斷攻擊鏈，建構主動禦敵之第一道防線。</p>
            """,
            "examinerTips": "得分關鍵詞：『Kaminsky 快取污染與 Transaction ID 暴力破解』、『DNSSEC 信任鏈：RRset、RRSIG、DNSKEY、DS 紀錄』、『ICANN Root 逐級驗證 Trust Anchor』、『DoT Port 853 企業專用 vs DoH Port 443 行動穿透』、『DNS RPZ 與 Sinkhole 惡意阻絕』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>Kaminsky 投毒原理（6分）</strong>：直擊 UDP 無狀態、Transaction ID 空間小及 Additional 段污染根因。</li>
  <li><strong>DNSSEC 密碼學機制（7分）</strong>：繪製清晰信任鏈架構，精確辨析 ZSK、KSK、RRSIG 與 DS 角色。</li>
  <li><strong>DoT vs DoH 對比（7分）</strong>：深入分析 853 vs 443 埠、企業邊界可控性與行動端防竊聽特性。</li>
  <li><strong>DNS RPZ 聯防結論（5分）</strong>：結合 F-ISAC 情資與 Sinkhole 實務，展現主動防禦深度。</li>
</ul>
            """
        }
    ]

if __name__ == "__main__":
    essays = get_sec_essays_37_to_48()
    print(f"Loaded {len(essays)} unique Sec essays (sec-essay-37 to sec-essay-48).")
    for e in essays:
        print(f"  [{e['id']}] {e['title']} ({len(e['modelAnswer'])} chars)")
