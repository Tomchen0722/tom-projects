# -*- coding: utf-8 -*-
"""
4 Unique, Elite Information Security Essays for TWSE IT Exam
IDs: sec-essay-40 to sec-essay-43
Refactored to eliminate all overlaps:
- sec-essay-40: 金融微服務架構之 Service Mesh 零信任服務身分（SPIFFE/SPIRE）與硬體加速 mTLS 雙向加密實踐
- sec-essay-41: 金融重大資安事件危機治理：金管會 30 分鐘重大資安通報法遵程序、零贖金政策與無預警跨部門兵推（TTX）實戰
- sec-essay-42: 金融行動身分識別（FIDO / Mobile ID）結合硬體安全元件（SE / StrongBox）金融簽章與金鑰離線保護實務
- sec-essay-43: 金融級 API 安全規範（FAPI 1.0/2.0）：OAuth 2.1 授權碼流 + PKCE、DPoP 與 MTLS 在證券開放金融之落地
"""

def get_sec_essays_40_to_43():
    return [
        # sec-essay-40: SPIFFE/SPIRE & Hardware-Accelerated mTLS
        {
            "id": "sec-essay-40",
            "category": "sec",
            "chapter": "第 6 章：分散式阻斷服務（DDoS）攻擊防禦與網路微隔離",
            "title": "金融微服務架構之 Service Mesh 零信任服務身分（SPIFFE/SPIRE）與硬體加速 mTLS 雙向加密實踐",
            "summary": "剖析金融核心微服務在 Kubernetes 叢集中之服務身分標識（SPIFFE ID）、動態 SVID 短期 X.509 憑證自動輪替（SPIRE）、雙向傳輸加密（mTLS）與利用 kTLS / SmartNIC 硬體加解密卸載之微秒級低延遲保障。",
            "points": 25,
            "rubric": "1. 靜態 API Token 於動態微服務環境之缺陷與 SPIFFE 零信任工作負載身分架構 (6分)；2. SPIRE 節點與工作負載證明（Attestation）發放 SVID 機制 (7分)；3. Service Mesh mTLS 雙向加密通道建立與無感金鑰輪替 (7分)；4. 核心 kTLS 與 SmartNIC 硬體加解密卸載低延遲實務結論 (5分)",
            "question": "證交所逐步將周邊與報表業務遷移至 Kubernetes 容器叢集，服務間東西向（East-West）通訊面臨身分偽冒與明文竊聽風險。試申論：(1) 傳統基於靜態 API Token 或共用密碼之身分驗證，在微服務動態擴縮容情境下之安全隱患；(2) SPIFFE（通用安全生產身分框架）與 SPIRE（SPIFFE 執行期環境）如何透過節點證明（Node Attestation）與工作負載證明（Workload Attestation）自動簽發短期 X.509 SVID；(3) Service Mesh（如 Istio / Linkerd）之 mTLS 雙向加密通道建立流程與憑證無感自動輪替（Rotation）；(4) 為避免 mTLS 頻繁非對稱交握與對稱加解密增加交易封包延遲，如何結合 Linux 核心 kTLS 與 SmartNIC 智慧網卡硬體卸載（Hardware Crypto Offloading）達成微秒級線速加密。",
            "modelAnswer": r"""
<h4>一、破題：微服務身分邊界重塑與零信任工作負載</h4>
<p>在證券交易所推行容器化與微服務轉型架構中，單一大型主機應用被拆分為數十個由容器（Pod）組成的輕量服務。傳統依賴靜態 API 金鑰、資料庫明文密碼或 IP 白名單之機制，在 Pod 隨時擴縮容、IP 動態漂移的雲原生環境中徹底崩潰。<strong>SPIFFE（Secure Production Identity Framework for Everyone）</strong>與其官方實作<strong>SPIRE</strong>，為金融微服務建立了一套「密碼學驅動、無密碼硬編碼、細粒度可驗證」之工作負載身分基石。</p>

<h4>二、傳統靜態憑證之致命缺陷 vs SPIFFE 規範</h4>
<ol>
  <li><strong>傳統靜態 Token 之單點破產</strong>：
    <ul>
      <li><strong>金鑰硬編碼與洩漏風險</strong>：開發者常將 API Key 寫入環境變數、設定檔或 Git 倉庫，一旦容器遭 RCE（遠端代碼執行）入侵，攻擊者可全盤提取金鑰並橫向移動。</li>
      <li><strong>缺乏生命週期管理</strong>：靜態 Token 缺乏自動過期與輪替機制，撤銷單一金鑰可能導致跨多個交易服務癱瘓。</li>
    </ul>
  </li>
  <li><strong>SPIFFE 標準化身分命名（SPIFFE ID）</strong>：
    <ul>
      <li>採用標準 URI 格式：<code>spiffe://twse.com.tw/ns/trading/sa/matching-engine</code>。</li>
      <li>身分憑證（SVID, SPIFFE Verifiable Identity Document）採用標準 <strong>X.509 數位憑證</strong> 或 <strong>JWT 權杖</strong> 呈現，天然內建公私鑰簽名與極短有效期限（如 1 小時）。</li>
    </ul>
  </li>
</ol>

<h4>三、SPIRE 節點與工作負載雙重證明（Attestation）運作機制</h4>
<pre><code class="language-text">  [Kubernetes 節點 Node]
     │ 1. Node Attestation (以 TPM 2.0 / K8s PSAT 證明節點合法性)
     ▼
  [SPIRE Agent] <───(安全通訊協定)───> [SPIRE Server (集中式 CA 金鑰簽發中樞)]
     │
     │ 2. Workload Attestation (檢查呼叫進程之 UID/GID, K8s Pod 命名空間與標籤)
     ▼
  [交易微服務 Pod] <──(獲取 SVID X.509 憑證 + 私鑰，僅存於記憶體，不落磁碟)</code></pre>
<ul>
  <li><strong>節點證明（Node Attestation）</strong>：SPIRE Server 驗證伺服器實體或 VM 節點身分，利用硬體 TPM 晶片或雲端服務提供者實例身分，確認節點未遭竄改。</li>
  <li><strong>工作負載證明（Workload Attestation）</strong>：容器啟動時向本機 SPIRE Agent 發起請求。Agent 直接查詢 Linux 核心或容器運行時（CRI），檢驗容器進程之 <code>cgroup</code>、命名空間、Pod 標籤與映象檔雜湊值。完全匹配者，Agent 方發放專屬短效 SVID 憑證與私鑰。</li>
</ul>

<h4>四、Service Mesh mTLS 雙向加密通道與無感金鑰輪替</h4>
<ol>
  <li><strong>Envoy Sidecar 自動交握</strong>：所有微服務之入站與出站流量均由 Envoy 代理人劫持。當委託下單服務呼叫撮合驗證服務時，兩端 Envoy 自動執行 <strong>mTLS 雙向憑證交換</strong>。雙方以 SPIFFE ID 為主旨替換名（SAN），嚴格校驗對端憑證鏈。</li>
  <li><strong>無中斷無感輪替（Zero-Downtime Rotation）</strong>：SPIRE Agent 於背景每 30 分鐘自動向 SPIRE Server 續約更新 SVID，並透過 Envoy 密鑰探索服務（Secret Discovery Service, SDS）於記憶體中動態加載新憑證，<strong>全程無須重啟交易 Pod，連線零中斷</strong>。</li>
</ol>

<h4>五、結論：kTLS 與 SmartNIC 硬體卸載之極低延遲架構</h4>
<p>在以微秒決勝之金融高頻撮合場景中，傳統使用者空間（User-space）TLS 處理會帶來頻繁的上下文切換（Context Switch）與記憶體複製開銷。證交所透過<strong>Linux 核心級 TLS（kTLS）</strong>，將對稱加解密下沉至核心直接與網卡 DMA 結合；更進一步導入 <strong>SmartNIC 智慧網卡硬體加解密卸載</strong>，由網卡專屬 ASIC 晶片以線速完成 AES-256-GCM 運算。此舉使內部通訊延遲增量<strong>壓低於 2 微秒以內</strong>，完美兼顧「零信任嚴格加密」與「資本市場極限效能」。</p>
            """,
            "examinerTips": "得分關鍵詞：『SPIFFE ID (spiffe://twse.com.tw/...) 與 X.509 SVID』、『SPIRE 雙重證明：Node Attestation + Workload Attestation (核心 cgroup 驗證)』、『Service Mesh Envoy SDS 記憶體動態金鑰輪替零中斷』、『kTLS 核心旁路與 SmartNIC 智慧網卡硬體卸載』、『延遲增量 < 2 微秒』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>靜態憑證隱患與 SPIFFE 定位（6分）</strong>：直指微服務動態漂移與硬編碼金鑰風險，清晰定義 SPIFFE/SVID 標準規範。</li>
  <li><strong>SPIRE 雙重證明機制（7分）</strong>：深入解構 Node 證明（TPM/節點身分）與 Workload 證明（核心行程與 CRI 標籤校驗），展示紮實雲原生底層實力。</li>
  <li><strong>Service Mesh mTLS 流程（7分）</strong>：詳細解析 Envoy 代理如何基於 SAN SPIFFE ID 進行雙向驗證與 SDS 無感輪替。</li>
  <li><strong>低延遲硬體卸載結論（5分）</strong>：切合證券交易所微秒級特性，給出 kTLS 與 SmartNIC 硬體加解密方案，答題亮眼。</li>
</ul>
            """
        },

        # sec-essay-41: FSC 30-Min Incident Response & TTX Drill
        {
            "id": "sec-essay-41",
            "category": "sec",
            "chapter": "第 11 章：業務營運持續（BCP）、高可用性與災難復原演練",
            "title": "金融重大資安事件危機治理：金管會 30 分鐘重大資安通報法遵程序、零贖金政策與無預警跨部門兵推（TTX）實戰",
            "summary": "深入解構金融關鍵基礎設施重大資安事件「30 分鐘知悉通報」法定剛性要件、反洗錢與反恐融資法制下之零贖金（Zero-Ransom）治理鐵律、董事會 CISO 決策指揮鏈、以及跨部門無預警兵棋推演（Tabletop Exercise, TTX）實踐。",
            "points": 25,
            "rubric": "1. 金管會 30 分鐘重大資安事件通報標準與知悉時點判定 (7分)；2. 反洗錢 AML / CFT 架構下絕對零贖金政策與法律責任 (6分)；3. 董事會 CMT 應變組織權責與投資人重訊對外發言 (6分)；4. 無預警跨部門兵推（TTX）情境設計與 AAR 檢討 (6分)",
            "question": "臺灣證券交易所為國家關鍵基礎設施（CI）金融領域核心，面對勒索軟體集團之重大資安攻擊威脅，建立符合主管機關法遵之危機治理至關重要。試申論：(1) 金管會「重大資安事件通報機制」中，針對「知悉（Awareness）」時點認定、30 分鐘線上初報要件與 2 小時主管機關專案簡報之剛性法規要求；(2) 依據國際洗錢防制法（AML）與反資恐法（CFT），金融機構為何必須嚴格貫徹「絕對零贖金（Zero Ransom）」政策及其法律責任風險；(3) 董事會層級危機應變委員會（Crisis Management Team, CMT）與 CISO 權責劃分及公關外部揭露（Investor Disclosure）原則；(4) 規劃一場「無預警跨部門兵棋推演（Tabletop Exercise, TTX）」之情境設計、注入事件（Injects）推進與事後檢討（After-Action Review, AAR）實踐。",
            "modelAnswer": r"""
<h4>一、破題：國家關鍵基礎設施資安危機治理之戰略剛性</h4>
<p>臺灣證券交易所不僅是證券期貨市場之撮合核心，更是國家安全體系中之 A 級關鍵基礎設施。面對現代勒索軟體與國家級威脅，資安危機處理已非單純之 IT 技術修復，而是直接連動<strong>主管機關監理法遵、市場交易信心、董事會治理與洗錢防制法律責任</strong>之綜合考驗。建立制度化、嚴格落實法規時效之應變機制，是確保金融韌性之命脈。</p>

<h4>二、金管會「重大資安事件 30 分鐘通報」法定剛性要件</h4>
<ol>
  <li><strong>「知悉（Awareness）」時點之法律判定</strong>：
    <ul>
      <li>法規「知悉」並非以「根本原因查明」為起點，而是以<strong>「資安人員或系統告警確認核心資通系統服務中斷、資料遭加密或機敏資料外洩之客觀事實成立瞬間」</strong>起算。</li>
      <li>任何機構以「內部仍在除錯或釐清原因」為由延誤通報，均屬重大法遵違失。</li>
    </ul>
  </li>
  <li><strong>階梯式通報法規要求</strong>：
    <ul>
      <li><strong>T + 30 分鐘（線上初報）</strong>：登入「金融資安資訊分享與分析中心（F-ISAC）」通報平台，填報發生時間、受影響系統名稱、影響業務範圍、初步評估損失及目前已採取之圍堵措施。</li>
      <li><strong>T + 2 小時（專案口頭彙報）</strong>：CISO 與高階主管向金管會資訊服務處與證券期貨局進行專案電話會議，說明最新災情與市場因應。</li>
      <li><strong>事件平息後 3 個工作日內</strong>：正式提交完整資安事件檢討報告（含 RCA 根本原因分析與中長期防範對策）。</li>
    </ul>
  </li>
</ol>

<h4>三、反洗錢（AML）與反恐融資架構下之「絕對零贖金」鐵律</h4>
<p>金融機構在面對勒索威脅時，必須堅決拒絕支付任何虛擬貨幣贖金：</p>
<ul>
  <li><strong>法律犯罪制裁風險</strong>：國際主要勒索集團（如 LockBit、BlackCat）常被美國財政部外國資產管制辦公室（OFAC）或國際組織列為恐怖主義資助黑名單。金融機構一旦支付贖金，將直接構成資助恐怖主義或違反洗錢防制法之重罪，面臨巨額國際金融制裁與司法追訴。</li>
  <li><strong>無保障陷阱</strong>：實證統計顯示，支付贖金後高達 40% 的受害者仍無法完全解密資料，且將被標註為「願意付錢的軟柿子」，引發二次勒索。唯一正確路徑是依賴經過驗證之 <strong>WORM 不可抹滅離線備份</strong> 進行純淨復原。</li>
</ul>

<h4>四、董事會 CMT 組織分工與市場資訊揭露</h4>
<pre><code class="language-text">  [董事會 / 總經理]
         │ (授權啟動危機狀態)
         ▼
  [危機管理委員會 (CMT)] ─── 法律顧問 (責任鑑定/洗防合規)
         │
         ├── [CISO / CSIRT 應變組] ── (技術隔離、鑑識取證、備份還原)
         ├── [業務撮合組] ────────── (市場開收盤決策、券商備援線路)
         └── [公關發言組] ────────── (證交所官網公告、記者會、重大訊息)</code></pre>
<ol>
  <li><strong>權責邊界</strong>：CISO 專注於技術圍堵與技術決策；業務撮合組評估是否需啟動暫停交易；CMT 主席（總經理）統籌整體決策。</li>
  <li><strong>公開透明之對外發言原則</strong>：嚴禁內部人員私自對外發布資訊，統一由公關發言人對外說明，恪守「事實為本、說明受控範圍、承諾復原進度」，平息市場恐慌。</li>
</ol>

<h4>五、無預警跨部門兵棋推演（Tabletop Exercise, TTX）實務</h4>
<p>為將危機流程化為直覺反射，證交所每年至少舉辦 2 次無預警跨部門兵推：</p>
<ol>
  <li><strong>動態情境推進（Injects）</strong>：
    <ul>
      <li><strong>Inject 1（09:15 盤中撮合期間）</strong>：監控螢幕跳出核心撮合伺服器磁碟 I/O 飆高，交易資料庫被注入未知後門。</li>
      <li><strong>Inject 2（09:30）</strong>：駭客於暗網發布聲明已掌握交易代碼，並勒索 500 枚比特幣，此時金管會來電詢問市場流言。</li>
      <li><strong>考驗重點</strong>：各部門是否能在 15 分鐘內觸發通報？CISO 與總經理如何平衡「維持開盤撮合」與「切斷橫向隔離網段」之兩難決策？</li>
    </ul>
  </li>
  <li><strong>事後檢討（After-Action Review, AAR）</strong>：兵推結束後立即召開覆盤會，檢驗通報時效瓶頸、備援線路切換盲點，並直接修訂災變標準作業指引（SOP），達成持續性韌性演進。</li>
</ol>
            """,
            "examinerTips": "得分關鍵詞：『知悉時點認定 (客觀事實成立瞬間即起算)』、『金管會 T+30 分鐘初報與 T+2 小時專案簡報』、『反恐融資 CFT / OFAC 制裁下之絕對零贖金原則』、『CMT 危機管理委員會與 CISO 技術指揮分工』、『TTX 兵棋推演動態 Injects 注入』、『AAR 事後檢討覆盤』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>30 分鐘通報法規精髓（7分）</strong>：深入辨析「知悉時點」認定，精確寫出 T+30 分鐘初報、T+2 小時專案會議與 3 日結報之時間階梯。</li>
  <li><strong>零贖金之法理基礎（6分）</strong>：跳脫單純口號，從 AML、CFT 與 OFAC 國際制裁視角論述為何不可付贖金，見解獨到。</li>
  <li><strong>CMT 與公關治理（6分）</strong>：清晰繪製指揮鏈結構圖，涵蓋技術、業務、法律與公關發言人權責。</li>
  <li><strong>TTX 兵推實務設計（6分）</strong>：具體設計盤中 Inject 注入案例與 AAR 檢討反饋，展現高級資安長之治理胸襟。</li>
</ul>
            """
        },

        # sec-essay-42: FIDO2 Mobile Identity & Secure Enclave / StrongBox
        {
            "id": "sec-essay-42",
            "category": "sec",
            "chapter": "第 5 章：安全軟體開發生命週期（SSDLC）與 OWASP Top 10",
            "title": "金融行動身分識別（FIDO / Mobile ID）結合硬體安全元件（SE / StrongBox）金融簽章與金鑰離線保護實務",
            "summary": "剖析證券下單 App 結合終端硬體安全晶片（Apple Secure Enclave / Android StrongBox Keymaster）進行私鑰隔離生成、生物特徵（Face ID / 指紋）本機驗證綁定、FIDO2 WebAuthn 金融委託數位簽章（Transaction Confirmation）與金鑰無法被抽出（Non-exportable）之保全機制。",
            "points": 25,
            "rubric": "1. 軟體憑證檔案缺陷與硬體安全元件（SE / StrongBox）晶片隔離架構 (6分)；2. FIDO2 / WebAuthn 金融身分鑑別與生物辨識本機核驗機制 (7分)；3. 所見即所簽（WYSIWYS）交易內容雜湊防篡改簽章流程 (7分)；4. 越獄/Root 終端金鑰無法導出（Non-exportable）保全結論 (5分)",
            "question": "行動網路下單已佔證券交易量七成以上，傳統憑證檔案（如 PKCS#12 `.pfx`）存放於手機檔案系統中，面臨木馬竊取與備份外洩風險。試申論：(1) 軟體金鑰檔案儲存之物理缺陷，與行動裝置硬體安全元件（Apple Secure Enclave, SE / Android StrongBox Keymaster）之硬體晶片隔離原理；(2) 投資人委託下單時，如何運用 FIDO2 / WebAuthn 協定結合生物辨識（Biometrics）實現本機身分授權與非對稱金鑰簽章；(3) 金融級「交易內容簽署（Transaction Confirmation / What You See Is What You Sign, WYSIWYS）」之雜湊防竄改機制；(4) 當手機遭竊或越獄（Root/Jailbreak）時，硬體金鑰「物理無法導出（Non-exportable）」與伺服器端憑證撤銷（Revocation）之安全保證。",
            "modelAnswer": r"""
<h4>一、破題：行動交易身分鑑別之典範轉移</h4>
<p>在證券市場數位化浪潮中，行動下單已成為投資人主要交易管道。早期券商普遍採用軟體數位憑證（如含有私鑰之 PKCS#12 `.pfx` 檔案並設定憑證密碼）。然而，此類檔案存放於手機快閃記憶體中，極易因惡意 App 提權、雲端備份外洩或中間人釣魚而被整體導出盜用。導入<strong>FIDO2 / WebAuthn 標準結合裝置端硬體安全元件（Secure Enclave / StrongBox）</strong>，方能徹底實現「私鑰不出晶片、生物特徵不離本機」之最高金融安全基準。</p>

<h4>二、軟體檔案缺陷 vs 專用硬體安全元件架構</h4>
<ol>
  <li><strong>軟體金鑰檔案之致命弱點</strong>：
    <ul>
      <li>私鑰解密依賴使用者輸入的固定憑證密碼，易遭鍵盤側錄木馬（Keylogger）竊取。</li>
      <li>簽章運算於手機通用 CPU 與記憶體中進行，駭客可利用記憶體 Dump 或動態 Hooking（如 Frida）在記憶體未加密瞬間直接攔截私鑰明文。</li>
    </ul>
  </li>
  <li><strong>硬體安全晶片實體隔離（Apple SE 與 Android StrongBox）</strong>：
    <ul>
      <li><strong>獨立硬體子系統</strong>：Secure Enclave（iOS）與 StrongBox Keymaster（Android）具備專屬的隔離微處理器、獨立加密記憶體與真亂數產生器（TRNG），與手機主作業系統（iOS/Android Kernel）實施硬體匯流排隔離。</li>
      <li><strong>晶片內非對稱金鑰生成</strong>：下單簽章金鑰直接於硬體內部生成（如 ECC secp256r1）。晶片架構確保私鑰<strong>「物理上無法被任何指令導出（Non-exportable）」</strong>，外部 CPU 僅能透過安全信箱發送待簽雜湊並接收簽名結果。</li>
    </ul>
  </li>
</ol>

<h4>三、FIDO2 / WebAuthn 委託簽章工作流程</h4>
<pre><code class="language-text">  [投資人手機下單 App]                     [證交所 / 券商下單伺服器]
          │                                         │
          │ 1. 點擊送出委託: 買進台積電 10 張 ────>│
          │                                         │ 2. 生成隨機挑戰碼 (Challenge)
          │<──── 3. 回傳 Challenge 與交易摘要 ──────┤    與交易綁定
          ▼
  [硬體安全晶片 SE / StrongBox]
    ├── 本機生物辨識核驗 (Face ID / 指紋比對)
    └── 晶片內部私鑰對 (Challenge + 委託摘要) 進行數位簽章
          │
          │ 4. 送出 FIDO2 簽章 + 裝置證明 (Attestation)
          ▼────────────────────────────────────────>│
                                                    │ 5. 公鑰驗章通過，送入撮合引擎！</code></pre>
<ul>
  <li><strong>生物辨識本機隔離核驗</strong>：投資人刷臉（Face ID）或按壓指紋時，生物特徵資料僅於本機安全晶片內與註冊模板比對，<strong>絕不傳送至網路或伺服器端</strong>，徹底杜絕生物特徵外洩之隱私風險。</li>
  <li><strong>使用者存在與驗證（UP & UV）</strong>：安全晶片在硬體層級確認 <code>User Presence (UP=1)</code> 與 <code>User Verification (UV=1)</code> 通過後，方才解鎖晶片內部私鑰執行一次性簽署。</li>
</ul>

<h4>四、所見即所簽（WYSIWYS）防竄改雜湊綁定</h4>
<p>為防範中間人攻擊或本機惡意程式在背後偷偷置換下單內容（如將「買進」竄改為「賣出」）：</p>
<ol>
  <li><strong>交易內容結構化雜湊</strong>：下單伺服器將委託明細（股票代號、委託價格、股數、買賣別、時間戳記）標準化為規範字串，計算 SHA-256 交易指紋 $H_{\text{tx}}$。</li>
  <li><strong>擴充欄位綁定</strong>：App 將 $H_{\text{tx}}$ 置於 FIDO2 <code>clientDataJSON</code> 之延伸屬性中，安全晶片對整體 <code>clientDataJSON</code> 進行簽章。</li>
  <li><strong>不可否認性保證</strong>：下單伺服器驗章時，重新校驗簽名內容是否與伺服器端委託明細完全一致。任何針對委託內容之竄改，將導致簽章數學驗證失效，達成嚴格之<strong>「所見即所簽（What You See Is What You Sign, WYSIWYS）」</strong>。</li>
</ol>

<h4>五、結論：極端情境安全保全與憑證撤銷</h4>
<p>即使手機遭竊，黑客在缺乏合法生物特徵或 PIN 碼前提下，強行拆解晶片只會觸發內部微電網熔斷保護；即使設備遭越獄（Root/Jailbreak），iOS/Android 核心之 Root 權限亦無法突破硬體安全元件之微過濾防線。若使用者遺失手機，證券伺服器端可於後台<strong>毫秒級撤銷（Revoke）該裝置公鑰</strong>，為行動資本市場構築兼顧無感體驗與軍規保全之信任防線。</p>
            """,
            "examinerTips": "得分關鍵詞：『淘汰軟體 PKCS#12 .pfx 檔案』、『Apple Secure Enclave 與 Android StrongBox 硬體實體隔離』、『私鑰晶片內生成物理無法導出 (Non-exportable)』、『生物辨識本機核驗 (不離本機)』、『FIDO2 User Verification (UV) 與 clientDataJSON』、『所見即所簽 WYSIWYS 交易雜湊綁定』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>軟硬體對比與晶片架構（6分）</strong>：深入對比軟體憑證與硬體安全晶片（SE/StrongBox）之微處理器與記憶體實體隔離，論點精闢。</li>
  <li><strong>FIDO2 運作流程（7分）</strong>：清晰繪述 5 步互動圖，闡明 Challenge/Response 機制與本機生物驗證解鎖私鑰之本質。</li>
  <li><strong>所見即所簽防竄改（7分）</strong>：技術層次極高，詳述 $H_{\text{tx}}$ 如何與 `clientDataJSON` 深度綁定，粉碎下單內容中間人替換攻擊。</li>
  <li><strong>極端安全保全結論（5分）</strong>：論述越獄隔離防禦、硬體物理防拆與伺服器端秒級撤銷，體現整體金融架構思維。</li>
</ul>
            """
        },

        # sec-essay-43: FAPI 1.0/2.0 Advanced Profile & OAuth 2.1 / DPoP
        {
            "id": "sec-essay-43",
            "category": "sec",
            "chapter": "第 8 章：網路安全、邊界防禦與開放 API 架構",
            "title": "金融級 API 安全規範（FAPI 1.0/2.0）：OAuth 2.1 授權碼流 + PKCE、DPoP 與 MTLS 在證券開放金融之落地",
            "summary": "深入解構開放證券（Open Securities）與跨機構下單 API 之金融級安全標準 FAPI 1.0/2.0 Advanced Profile、淘汰隱式許可（Implicit Flow）、OAuth 2.1 授權碼流強制 PKCE、DPoP（RFC 9449）發送者限制權杖、以及 mTLS 雙向傳輸加密實戰。",
            "points": 25,
            "rubric": "1. 傳統 OAuth 2.0 於金融下單場景之缺陷與 FAPI 規範演進 (6分)；2. OAuth 2.1 廢止隱式許可與強制授權碼流＋PKCE 機制 (7分)；3. 權杖發送者限制：DPoP（RFC 9449）與 mTLS 憑證綁定權杖對照 (7分)；4. 證券開放金融 API 稽核與金管會規範落地結論 (5分)",
            "question": "臺灣金管會積極推動「開放金融（Open Finance）」與證券期貨業開放 API，允許第三方服務業者（TSP）與證券商串接委託下單與資產查詢。試申論：(1) 傳統 OAuth 2.0 授權模式在金融極高金流場景之安全缺陷（如 Bearer Token 竊取重放、授權碼攔截）；(2) 國際金融級 API 安全標準（Financial-grade API, FAPI 1.0/2.0 Advanced Profile）相較於一般 OAuth 2.0 之核心增強規範；(3) OAuth 2.1 規範中全面廢除隱式許可（Implicit Flow）與密碼許可（Password Flow），強制採用授權碼流結合 PKCE（Proof Key for Code Exchange）之技術細節；(4) 權杖發送者限制（Sender-Constrained Tokens）：DPoP（RFC 9449）與 mTLS 憑證綁定權杖（RFC 8705）之對比與金融實務部署。",
            "modelAnswer": r"""
<h4>一、破題：開放金融浪潮與金融級 API 嚴苛考驗</h4>
<p>金管會積極推動開放證券（Open Securities），第三方金融科技業者（TSP）得以透過開放 API 提供投資人跨券商帳戶整合、策略下單與資產分析。然而，證券 API 直接涉及投資人資金移轉與股票買賣，傳統廣泛應用於社交網站之 OAuth 2.0 規範過於寬鬆，存在 Bearer Token 易遭竊取重放、前端授權碼遭攔截等致命漏洞。導入<strong>國際金融級 API 安全規範（Financial-grade API, FAPI 1.0/2.0）</strong>與<strong>OAuth 2.1</strong>，是守護開放資本市場之剛性防線。</p>

<h4>二、傳統 OAuth 2.0 之金融安全缺陷與 FAPI 增強規範</h4>
<ol>
  <li><strong>傳統 OAuth 2.0 於金融領域之缺陷</strong>：
    <ul>
      <li><strong>Bearer Token「認票不認人」</strong>：存取權杖類似無記名鈔票，一旦因網路竊聽、日誌打印或 XSS 遭竊，攻擊者可肆意重放調用下單 API。</li>
      <li><strong>授權碼攔截攻擊（Authorization Code Interception）</strong>：行動設備或單頁應用（SPA）在自訂 URI Scheme 跳轉時，惡意 App 可註冊相同協定搶先截獲授權碼。</li>
    </ul>
  </li>
  <li><strong>FAPI 1.0/2.0 Advanced Profile 核心防禦要求</strong>：
    <ul>
      <li>強制實施<strong>發送者限制權杖（Sender-Constrained Tokens）</strong>，廢除純 Bearer Token。</li>
      <li>所有請求與回應必須具備<strong>端到端防竄改簽名（JWS / JWE）</strong>。</li>
      <li>授權請求必須透過<strong>PAR（推送授權請求，Pushed Authorization Requests, RFC 9126）</strong>於後端安全傳遞，禁止在前端瀏覽器 URL 暴露授權參數。</li>
    </ul>
  </li>
</ol>

<h4>三、OAuth 2.1 授權碼流 ＋ PKCE 技術機制</h4>
<p>OAuth 2.1 全面廢除安全性低落之「隱式許可（Implicit Flow）」與「資源擁有者密碼憑證（Password Flow）」，全面強制採用<strong>授權碼流（Authorization Code Flow）結合 PKCE（RFC 7636）</strong>：</p>
<pre><code class="language-text">  [用戶端 Client]                                [授權伺服器 AS (Auth Server)]
        │                                                     │
        │ 1. 生成高熵隨機字串 Code Verifier                  │
        │    計算 Code Challenge = Base64URL(SHA256(Verifier))│
        │ 2. 發起授權請求 (攜帶 Code Challenge) ─────────────>│
        │<── 3. 用戶登入同意後，回傳 Authorization Code ───────┤
        │                                                     │
        │ 4. 交換 Token: 攜帶 Code + 原始 Code Verifier ─────>│
        │                                                     │ 5. AS 驗證: SHA256(Verifier)
        │                                                     │    是否等於步驟2 Challenge?
        │<── 6. 驗證一致，方才核發 Access Token ──────────────┤ (粉碎授權碼攔截竊取！)</code></pre>
<p><strong>防護效益</strong>：即使惡意攻擊者攔截到步驟 3 的 <code>Authorization Code</code>，因其無法得知用戶端記憶體中臨時生成的 <code>Code Verifier</code>，在步驟 4 請求交換權杖時將直接被授權伺服器拒絕。</p>

<h4>四、發送者限制權杖雙軌實作對比：DPoP vs. mTLS</h4>
<table class="essay-table">
  <thead>
    <tr><th>比較維度</th><th>mTLS 憑證綁定權杖 (RFC 8705)</th><th>應用層 DPoP (RFC 9449)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>綁定依據</strong></td><td>傳輸層 X.509 客戶端憑證指紋</td><td>應用層臨時非對稱金鑰對（JWK）</td></tr>
    <tr><td><strong>運作層級</strong></td><td>L4/L7 傳輸層（TLS Handshake 驗證憑證）</td><td>L7 應用層（HTTP Header 附掛 JWT 簽章）</td></tr>
    <tr><td><strong>架構複雜度</strong></td><td>高。需在 API 閘道器與反向代理終結 mTLS，維護雙向憑證鏈</td><td><strong>低。純 HTTP 協定運作，完美穿越 CDN 與雲端 WAF</strong></td></tr>
    <tr><td><strong>適用場景</strong></td><td><strong>機構對機構（B2B：券商系統對接證交所核心）</strong></td><td><strong>行動終端與網頁（B2C：投資人手機 App、SPA 網頁）</strong></td></tr>
  </tbody>
</table>
<ol>
  <li><strong>DPoP 原理</strong>：客戶端每次發送 API 請求時，在 <code>DPoP</code> 標頭附帶一個由其私鑰即時簽名之 JWT，內容包含當前 HTTP Method、請求 URI 與抗重放之 <code>jti</code> 雜湊及時間戳記。</li>
  <li><strong>防護能力</strong>：即使 Access Token 遭黑客洩漏，黑客因缺乏客戶端私鑰無法生成有效的 DPoP Proof，下單 API 閘道器秒級攔截無效請求。</li>
</ol>

<h4>五、結論：證券開放金融安全合規實踐</h4>
<p>在推動開放證券 API 時，證交所要求全體串接之 TSP 業者與券商必須 100% 符合 <strong>FAPI 規範</strong>。透過「OAuth 2.1 + PKCE 守護前端授權」、「mTLS / DPoP 鎖定傳輸憑證」與「金管會規範之 5 年不可抹滅查核日誌」，為資本市場築起金融級零信任 API 堡壘。</p>
            """,
            "examinerTips": "得分關鍵詞：『開放證券 Open Securities 與 FAPI 1.0/2.0 Advanced Profile』、『OAuth 2.1 廢止 Implicit Flow』、『授權碼流結合 PKCE (Code Verifier & Challenge)』、『發送者限制權杖 Sender-Constrained Tokens』、『DPoP (RFC 9449) 應用層 JWT 證明 vs mTLS (RFC 8705)』、『PAR 推送授權請求 (RFC 9126)』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>金融開放背景與問題意識（6分）</strong>：精準指出 Bearer Token「認票不認人」在金融下單之致命破綻，引導出 FAPI 必要性。</li>
  <li><strong>OAuth 2.1 與 PKCE 數學流程（7分）</strong>：詳細繪述 Verifier 與 SHA-256 Challenge 互動時序圖，說明攔截授權碼為何無法利用。</li>
  <li><strong>DPoP 與 mTLS 發送者限制對比（7分）</strong>：列表剖析 RFC 8705（mTLS 適用 B2B）與 RFC 9449（DPoP 適用 B2C/CDN），論證深刻。</li>
  <li><strong>開放證券合規總結（5分）</strong>：切合金管會開放金融監理要求，給出高可用、防篡改之實務架構結論。</li>
</ul>
            """
        },
    ]
