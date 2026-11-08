# -*- coding: utf-8 -*-
"""
8 Elite Core TWSE Information Security Simulation Essays (sec-essay-69 ~ sec-essay-76)
Refactored to eliminate redundant overlaps with sec-essay-01~12 and sec-essay-37~48:
1. 金融資安情資分享與分析中心（F-ISAC）與自動化交換（STIX 2.1 / TAXII）跨機構聯防 (sec-essay-69)
2. 證券核心結算交割系統不可抹滅交易日誌（WORM）、時戳權威（TSA）與雙軌稽核 (sec-essay-70)
3. 高頻交易微秒級時鐘同步安全：IEEE 1588 PTP、GNSS 衛星欺騙偵測與時間戳防篡改 (sec-essay-71)
4. 證券周邊單位跨機構身分同調（Identity Federation）、SAML 2.0 / OIDC 與 Token 竊取防護 (sec-essay-72)
5. 端點偵測與回應（EDR/XDR）自防禦機制（Anti-Tampering）與驅動程式帶刀（BYOVD）防護 (sec-essay-73)
6. 金融機構雲端 SaaS 與影子 IT（Shadow IT）治理：CASB 代理、OAuth 授權洗白與跨雲 DLP (sec-essay-74)
7. 金融核心交易系統威脅建模（Threat Modeling）：STRIDE 方法論、攻擊樹（Attack Tree）與 DREAD 風險量化評估實戰 (sec-essay-75)
8. 開源軟體授權合規與相依性傳染性風險治理：SCA、GPL/AGPL 穿透風險與漏洞修補實踐 (sec-essay-76)
"""

def get_8_core_twse_essays():
    return [
        # 1. sec-essay-69: F-ISAC & STIX 2.1 / TAXII Automated Threat Exchange
        {
            "id": "sec-essay-69",
            "category": "sec",
            "chapter": "第 1 章：金融法遵體系、主管機關監理與重大資安通報應變",
            "title": "金融資安資訊分享與分析中心（F-ISAC）與自動化情資交換（STIX 2.1 / TAXII）跨機構聯防機制",
            "summary": "剖析金管會 F-ISAC/F-CERT 聯防體系、STIX 2.1 結構化威脅資訊表達法（Indicator/Sighting/Observed-Data）與 TAXII 2.1 傳輸協定、證交所 SOAR 劇本自動化阻斷與去識別化威脅回饋實踐。",
            "points": 25,
            "rubric": "1. F-ISAC 國家金融聯防體系定位與運作模式 (6分)；2. STIX 2.1 物件模型與 TAXII 2.1 自動交換機制 (7分)；3. 證交所內部 SOAR 威脅情資自動轉化阻斷規則流 (7分)；4. 情資回饋去識別化與 TLP 分級治理 (5分)",
            "question": "臺灣金融監督管理委員會推動「金融資安行動方案 2.0」，要求關鍵金融機構全面深化與金融資安資訊分享與分析中心（F-ISAC）之聯防體系。請申論：(1) F-ISAC 在我國金融關鍵基礎設施之定位與運作模式；(2) 結構化威脅資訊表達法（STIX 2.1）之核心物件架構與 TAXII 2.1 自動化交換機制；(3) 臺灣證券交易所如何將接收之外部威脅情資，透過 SOAR 劇本自動轉化為邊界防火牆、WAF 及 EDR 之即時阻斷規則；(4) 機構向主管機關與 F-ISAC 回饋威脅情資時之去識別化（Anonymization）與 TLP（Traffic Light Protocol）分級原則。",
            "modelAnswer": r"""
<h4>一、破題：F-ISAC 在我國金融關鍵基礎設施之聯防樞紐地位</h4>
<p>在國家資通安全體系中，金融領域為核心關鍵基礎設施（CI）。單一機構往往無法獨立應對具備國家級背景之進階持續性威脅（APT）與跨國金融勒索集團。<strong>金融資安資訊分享與分析中心（F-ISAC）</strong>與<strong>金融資安監控協同應變中心（F-SOC / F-CERT）</strong>構建了我國金融體系之「早期預警、早期處置」聯防中樞：</p>
<ol>
  <li><strong>運作機制</strong>：集中收集來自各銀行、證券商、期貨商、證券周邊單位（證交所、櫃買中心、集保結算所）、NCC 及國家 CERT 之威脅指標（IoC），經過關聯分析與資安專家研判後，即時向全體會員廣播。</li>
  <li><strong>證交所之核心責任</strong>：作為證券市場撮合核心樞紐，證交所不僅是被動的情資接收者，更肩負即時回報新型下單偽冒手法、DDoS 攻擊特徵與惡意 IP 之情報源責任。</li>
</ol>

<h4>二、STIX 2.1 核心物件架構與 TAXII 2.1 交換標準</h4>
<p>傳統文字通報難以自動化機器解析，F-ISAC 全面採用國際標準 <strong>STIX 2.1（Structured Threat Information Expression）</strong> 與 <strong>TAXII 2.1（Trusted Automated eXchange of Intelligence Information）</strong>：</p>
<ul>
  <li><strong>STIX 2.1 物件模型（SDO / SRO）</strong>：
    <ul>
      <li><strong>Indicator（威脅指標）</strong>：包含 Pattern 表達式（如惡意 C2 網域名稱、下單木馬檔案 SHA-256 雜湊值）。</li>
      <li><strong>Observed Data（觀測資料）</strong>：記錄在特定時間點於金融網路內觀測到的實際網路連線或端點行為。</li>
      <li><strong>Attack Pattern & Malware</strong>：參照 MITRE ATT&CK 框架，定義攻擊手法與惡意程式家族。</li>
      <li><strong>Relationship（關係物件）</strong>：以圖形結構鏈結 <code>Indicator -> indicates -> Malware</code>。</li>
    </ul>
  </li>
  <li><strong>TAXII 2.1 傳輸架構</strong>：基於 HTTPS 與 RESTful API，提供 <strong>Channels（發布/訂閱通道）</strong> 與 <strong>Collections（情資合集）</strong>。證交所邊界系統以機器對機器（M2M）之 HTTPS POST/GET 即時輪詢或推播最新威脅 Bundle。</li>
</ul>

<h4>三、證交所 SOAR 自動化情資轉化與即時阻斷架構</h4>
<pre><code class="language-text">  [F-ISAC TAXII 伺服器]
          │ (STIX 2.1 JSON Feed)
          ▼
  [證交所 TIP 情資平台] ─── (IoC 品質加權、去重、白名單過濾)
          │
          ▼
  [SOAR 自動化編排引擎]
    ├── (高信度 IP) ──────> 邊界次世代防火牆 (NGFW / BGP Flowspec 即時阻斷)
    ├── (惡意 URL/Domain) ──> 交易 API 閘道器 / WAF (拒絕委託請求)
    └── (惡意 Hash) ───────> 核心撮合主機 EDR (即時記憶體隔離與進程終止)</code></pre>
<ol>
  <li><strong>情資正規化與白名單過濾</strong>：外部情資經由 TIP（Threat Intelligence Platform）進行誤報校驗，嚴格比對證券商委託下單 IP 白名單與主管機關網段，防範投毒引發金融交易阻斷。</li>
  <li><strong>SOAR Playbook 自動執行</strong>：針對信賴評分 > 90 分之極高危 IoC，SOAR 劇本自動呼叫 API 於 60 秒內推播至防火牆與 EDR，大幅將 MTTD（平均偵測時間）與 MTTR（平均回應時間）由小時級降至秒級。</li>
</ol>

<h4>四、情資回饋去識別化與 TLP 分級治理</h4>
<ul>
  <li><strong>情資去識別化（Anonymization）</strong>：證交所向 F-ISAC 回報攻擊事件時，必須透過腳本自動遮蔽交易帳號、委託回報明細與伺服器內部私有 IP，僅保留攻擊者外網來源 IP、惡意載荷特徵與攻擊手法。</li>
  <li><strong>TLP 2.0 流量燈號協議管制</strong>：
    <ul>
      <li><strong>TLP:RED</strong>：僅限通報雙方指定人員查閱，嚴禁對外分享。</li>
      <li><strong>TLP:AMBER+STRICT</strong>：僅限證券周邊同業組織內部限制性分享。</li>
      <li><strong>TLP:AMBER</strong>：可與同業會員組織共同研判防禦。</li>
      <li><strong>TLP:GREEN</strong>：可在全體 F-ISAC 會員社群自由流通。</li>
    </ul>
  </li>
</ul>

<h4>五、結論：構建金融動態主動聯防生態</h4>
<p>證交所落實 F-ISAC 自動化情資聯防，將資安防禦由「各自為戰、事後清查」進化為「一處遭駭、全網聯防」之智慧生態體系，為全臺灣資本市場構築高韌性防禦陣線。</p>
""",
            "examinerTips": "得分關鍵詞：『F-ISAC 與 F-SOC/CERT 金融 CI 聯防體系』、『STIX 2.1 物件模型 (Indicator, Observed Data, Relationship) 與 TAXII 2.1 RESTful M2M 交換』、『TIP 情資過濾比對下單白名單避免誤殺』、『SOAR Playbook 60秒自動派發防火牆/EDR』、『TLP 2.0 分級與去識別化』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>破題與 F-ISAC 角色 (6分)</strong>：精準指出金管會金融資安行動方案 2.0 之 F-ISAC 定位，強調證交所作為情報提供者與接收者之雙向價值。</li>
  <li><strong>STIX 2.1 與 TAXII 2.1 技術細節 (7分)</strong>：必須具體寫出 STIX 2.1 的 JSON 鍵值架構（SDO/SRO 物件分類）與 TAXII Channels/Collections 協定機制，展現紮實通訊標準實力。</li>
  <li><strong>SOAR 落地阻斷工作流 (7分)</strong>：切中證券交易所微秒級低延遲核心場景，重點在於白名單校驗防誤殺與 API 自動派發技術。</li>
  <li><strong>去識別化與 TLP (5分)</strong>：完整解釋個資保護、金融機密遮蔽與 TLP 2.0 燈號（Red/Amber/Green/Clear）治理要求。</li>
</ul>
"""
        },

        # 2. sec-essay-70: WORM Audit Logs & TSA in TWSE Clearing System
        {
            "id": "sec-essay-70",
            "category": "sec",
            "chapter": "第 6 章：金融安全維運中心（SOC）、SIEM/SOAR 自動化與數位鑑識調查",
            "title": "證券核心結算交割系統不可抹滅交易日誌（WORM）、時戳權威（TSA）與金管會雙軌稽核軌跡實務",
            "summary": "深入解構金融撮合與結算系統法規 5 年查核軌跡要求、WORM 不可抹滅儲存、RFC 3161 時戳權威（TSA）、日誌傳輸加密隔離、特權 DBA 竄改阻斷與金管會雙軌鏈式雜湊（Hash Chaining）稽核驗證。",
            "points": 25,
            "rubric": "1. 證券交割法規軌跡要求與 WORM/TSA 法律不可否認性 (7分)；2. 集中式日誌管線加密與實體隔離架構 (6分)；3. 防特權 DBA/Root 竄改之頻外防禦與即時阻斷 (6分)；4. 雙軌稽核與鏈式雜湊（Hash Chaining）完整性驗證 (6分)",
            "question": "證券交易所撮合與結算系統承載每日數千億交割金流，依法規交易日誌與查核軌跡（Audit Trails）必須保存 5 年以上且具備不可抹滅與防竄改性。試申論：(1) WORM（Write Once Read Many）儲存架構與可信任時戳權威（RFC 3161 Timestamp Authority, TSA）在法律非否認性（Non-repudiation）之作用機制；(2) 集中式稽核日誌收集管線（Log Aggregation Pipeline）之傳輸加密、實體隔離與金鑰輪替控制；(3) 特權管理者（DBA/Root）試圖透過頻外操作竄改或清理日誌時之即時告警與取證阻斷設計；(4) 金管會檢查局雙軌稽核（內部稽核 + 外部獨立驗證）之軌跡抽樣與鏈式雜湊（Cryptographic Hash Chaining）驗證實務。",
            "modelAnswer": r"""
<h4>一、破題：交割日誌不可抹滅性之法律位階與金融主權</h4>
<p>證券交易結算系統承載每日數千億新台幣之資金交割與股權移轉。依金管會《金融機構資通安全防護基準》與《證券期貨業通訊安全管理規範》，交易日誌與存取軌跡必須具備<strong>完整性（Integrity）</strong>與<strong>不可否認性（Non-repudiation）</strong>，法定保存期限至少 5 年，且在發生交易紛爭或司法調查時，必須具備完全可信之訴訟證明力（Evidentiary Weight）。</p>

<h4>二、WORM 不可抹滅儲存與 RFC 3161 時戳權威（TSA）運作機制</h4>
<ol>
  <li><strong>WORM（Write Once, Read Many）硬體鎖定機制</strong>：
    <ul>
      <li>日誌寫入專屬合規儲存陣列（如 Object Lock Compliance Mode），底層韌體實施<strong>不可撤銷保留期（Retention Period）</strong>。</li>
      <li>即使高權限系統管理員或具備 root 權限之內部惡意人員，亦無法透過 API、作業系統底層指令或格式化執行刪除或覆寫。</li>
    </ul>
  </li>
  <li><strong>RFC 3161 可信時戳權威（TSA）綁定</strong>：
    <ul>
      <li>交易日誌產生時，日誌伺服器計算該區塊之雜湊值 $H = \text{SHA-256}(Log)$，發送至政府/金融合法授權之第三方法定 TSA 伺服器。</li>
      <li>TSA 伺服器以經硬體安全模組（HSM）保護之私鑰，將 UTC 國際標準時間與 $H$ 共同簽發 <strong>時戳權杖（TimeStampToken）</strong>。</li>
      <li>證明該筆日誌在該特定時間戳記「確實存在」且「未曾修改」，賦予無懈可擊之司法證據效力。</li>
    </ul>
  </li>
</ol>

<h4>三、集中式日誌收集管線防護架構</h4>
<pre><code class="language-text">  [核心撮合/結算節點] ──(TLS 1.3 + mTLS 雙向加密)──> [隔離日誌中繼佇列 Kafka]
          │                                                   │
    (本地只讀記憶體緩衝)                                        ▼
                                                    [日誌簽章日誌服務]
                                                              │ (計算 Hash Chain + 請求 TSA)
                                                              ▼
                                                    [WORM 儲存 (保留5年)]</code></pre>
<ul>
  <li><strong>端到端傳輸保護</strong>：日誌代理（Log Agent）採用 mTLS 雙向憑證鑑別，傳輸過程強制啟用 TLS 1.3 傳輸加密，防止中間人竊聽或偽造日誌封包。</li>
  <li><strong>專用隔離通道（Dedicated OOB Log Network）</strong>：日誌傳輸網路與業務交易網路實施 VLAN/VXLAN 實體隔離，確保業務網路遭受風暴或 DDoS 攻擊時，日誌通道依然暢通無阻。</li>
</ul>

<h4>四、防範特權管理者（DBA/Root）竄改日誌之縱深阻斷</h4>
<ol>
  <li><strong>權限分離（Separation of Duties, SoD）</strong>：交易系統維運人員（DBA/SysAdmin）無權存取日誌伺服器；日誌伺服器僅授權專職資安稽核員查閱，且稽核員亦無權修改 WORM 儲存內容。</li>
  <li><strong>即時同步轉送（Real-time Forwarding）</strong>：日誌於產生瞬間（毫秒級）即非同步外送至隔離之 SIEM，伺服器本地不保留可供竄改之長時歷史日誌檔。</li>
  <li><strong>底層觸發告警（Auditd / eBPF Tetragon）</strong>：若 DBA 試圖關閉資料庫審計外掛（如 <code>pgaudit</code>）或下達 <code>TRUNCATE audit_table</code>，核心層 eBPF 立即攔截系統呼叫，發送 P1 重大告警並同步切斷其連線會話。</li>
</ol>

<h4>五、金管會雙軌稽核與鏈式雜湊（Cryptographic Hash Chaining）驗證</h4>
<p>為因應金管會與會計師之數位鑑識查核，系統實作鏈式雜湊驗證演算法：</p>
$$\text{Block}_n.\text{Hash} = \text{SHA-256}(\text{Log}_n \parallel \text{Block}_{n-1}.\text{Hash} \parallel \text{Timestamp}_n)$$
<ul>
  <li><strong>連鎖防竄改性</strong>：任何微小竄改或抽換單一筆記錄，將導致後續整條鏈之雜湊值全面崩潰。</li>
  <li><strong>雙軌抽查實踐</strong>：稽核人員只需輸入起訖時間，系統自動運行 Merkle Tree / Hash Chain 驗證演算法，並比對外置公證人儲存庫之 Root Hash，秒級完成 100% 完整性數學驗證。</li>
</ul>
""",
            "examinerTips": "得分關鍵詞：『金管會查核軌跡法定保存5年』、『WORM 儲存合規鎖定模式韌體防護』、『RFC 3161 第三方時戳權威 TSA 司法不可否認性』、『權限分離 SoD 避免 DBA 竄改』、『鏈式雜湊 Hash Chaining (區塊鏈級完整性校驗)』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>法規依據與核心定義 (7分)</strong>：明確引用金管會防護基準 5 年保存與司法證據力，清晰定義 WORM 與 RFC 3161 TSA 數學簽章架構。</li>
  <li><strong>傳輸管線與實體隔離 (6分)</strong>：提出 mTLS 雙向加密、專用頻外日誌網路架構，證明考生具備超大型金融基礎設施之實務規劃經驗。</li>
  <li><strong>特權防竄改與 eBPF 攔截 (6分)</strong>：直擊閱卷委員痛點：如何防範掌握 root/DBA 權限之內部人員，給出權限分離、日誌即時外拋與核心呼叫攔截三大解法。</li>
  <li><strong>鏈式雜湊驗證 (6分)</strong>：寫出精確數學公式 $\text{Block}_n.\text{Hash} = \text{SHA-256}(\text{Log}_n \parallel \text{Block}_{n-1}.\text{Hash})$，展現無可挑剔之技術高度。</li>
</ul>
"""
        },

        # 3. sec-essay-71: IEEE 1588 PTP & Anti-GNSS Spoofing in High-Frequency Trading
        {
            "id": "sec-essay-71",
            "category": "sec",
            "chapter": "第 5 章：極低延遲架構、網路安全、DDoS 立體防禦與邊界阻絕",
            "title": "高頻交易微秒級時鐘同步安全：IEEE 1588 PTP、GNSS 衛星欺騙（Spoofing）偵測與時間戳防篡改",
            "summary": "剖析證券市場逐筆撮合與行情推播微秒時序公平性要求、IEEE 1588 PTP v2 邊界時鐘（Boundary Clock）部署、GNSS 衛星欺騙/干擾威脅偵測、銣銫原子鐘雙時脈源備援與 MiFID II 時間公差稽核。",
            "points": 25,
            "rubric": "1. 證券撮合微秒時鐘同步需求與 PTP v2 vs NTP 技術對比 (7分)；2. GNSS 衛星欺騙與干擾攻擊對交易撮合公平性之破壞 (6分)；3. GNSS+銣銫原子鐘雙時脈源與硬體時戳防護實務 (6分)；4. 漂移監控與 MiFID II 法規公差稽核合規 (6分)",
            "question": "臺灣證券交易所逐筆撮合（Continuous Trading）與行情推播要求微秒（Microsecond）甚至奈秒級之極致時鐘精確度，以保障委託單撮合時序公平性。試申論：(1) 精確時間協定（IEEE 1588 PTP v2）相較於傳統 NTP 之架構差異與邊界時鐘（Boundary Clock）部署實務；(2) 針對機房 GNSS/GPS 衛星天線之「衛星信號欺騙（Spoofing）」與「干擾（Jamming）」攻擊向量，其對市場交易公平性與撮合爭議之潛在威脅；(3) 證交所資料中心如何建立「GNSS 衛星天線陣列 + 銣/銫原子鐘（Atomic Clock）雙時脈源備援」與硬體封包時戳（Hardware Timestamping）防護架構；(4) 符合 MiFID II / 證券期貨業時間同步容許公差（< 100 微秒）與漂移異常告警實務。",
            "modelAnswer": r"""
<h4>一、破題：極致微秒撮合與時間同步之金融秩序基石</h4>
<p>自臺灣證券市場全面實施<strong>逐筆撮合（Continuous Trading）</strong>以來，撮合引擎每秒處理數萬筆委託單。委託先後順序直接決定投資人能否成交於最佳價格。若交易伺服器時鐘不同步，將導致撮合先後次序倒置、搶先交易（Front-Running）與司法糾紛。因此，微秒乃至奈秒級之高精度防篡改時間同步體系，是維持資本市場交易公平性之核心命脈。</p>

<h4>二、IEEE 1588 PTP v2 相較於傳統 NTP 之維度對比</h4>
<table class="essay-table">
  <thead>
    <tr><th>比較維度</th><th>網路時間協定（NTP v4）</th><th>精確時間協定（IEEE 1588 PTP v2）</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>時間精度</strong></td><td>毫秒級（1~10 ms），易受作業系統中斷干擾</td><td><strong>亞微秒至奈秒級（< 100 ns）</strong></td></tr>
    <tr><td><strong>時戳打點層級</strong></td><td>應用層/作業系統核心網路堆疊（軟體時戳）</td><td><strong>網路卡 PHY/MAC 晶片硬體打點（Hardware Timestamp）</strong></td></tr>
    <tr><td><strong>網路中繼延遲修正</strong></td><td>無法校正交換機內部封包佇列暫留延遲（Jitter）</td><td>支援 <strong>Boundary Clock (BC)</strong> 與 <strong>Transparent Clock (TC)</strong></td></tr>
    <tr><td><strong>適用金融場景</strong></td><td>一般後台報表、非即時系統日誌對齊</td><td><strong>核心撮合引擎、逐筆委託下單、行情廣播網卡</strong></td></tr>
  </tbody>
</table>

<h4>三、GNSS 衛星欺騙（Spoofing）與干擾（Jamming）攻擊向量剖析</h4>
<p>PTP 主時鐘通常依賴機房頂樓之 GNSS/GPS 衛星信號獲取國際標準 UTC 時間：</p>
<ol>
  <li><strong>信號干擾（Jamming）</strong>：攻擊者以同頻率大功率射頻噪聲覆蓋衛星頻段（L1: 1575.42 MHz），導致機房天線失鎖（Loss of Lock），迫使主時鐘進入維持模式（Holdover）。</li>
  <li><strong>衛星欺騙（Spoofing - 致命威脅）</strong>：
    <ul>
      <li>黑客利用 SDR（軟體定義無線電，如 HackRF/USRP）發送微弱偽造 GPS 信號，逐步調高功率誘導天線鎖定偽造載波。</li>
      <li>偽造信號精細調整時間偏移（如向前或向後平移數百毫秒），若主時鐘被誤導，特定高頻交易者將可製造「時間倒流」假象，進行合法外衣下的搶先交易或規避洗防違約查核。</li>
    </ul>
  </li>
</ol>

<h4>四、雙時脈源備援與硬體時戳立體防禦架構</h4>
<pre><code class="language-text">  [多星系抗欺騙天線 (GPS/Galileo/BeiDou)] ──┐
                                            ▼
                        [PTP Grandmaster 主時鐘] ─── (時鐘鑑別校驗)
                                            ▲
  [機房內部 銣/銫原子鐘 (Rubidium Atomic)] ──┘
                    │
                    ▼ (IEEE 1588 PTP v2 網路)
  [Boundary Clock (邊界交換機)] ──> [撮合主機 (專用 FPGA / PTP 網卡硬體打點)]</code></pre>
<ol>
  <li><strong>空間分集與多星座抗欺騙天線</strong>：採用抗干擾天線（CRPA，受控接收方向圖天線）結合 GPS、北斗、Galileo 多星座信號交叉校驗，一旦各星座時間相位差超過閾值即告警。</li>
  <li><strong>銣/銫原子鐘（Atomic Clock）硬體維持備援</strong>：機房部署電信級銣原子鐘，即使外部 GNSS 天線信號完全中斷，原子鐘維持模式（Holdover Mode）可確保在 24 小時內時間漂移<strong>小於 1 微秒</strong>。</li>
  <li><strong>PHY 層硬體時戳</strong>：委託封包抵達伺服器網卡瞬間，網卡 PHY 晶片直接於 MAC 訊框打上 64-bit 奈秒時間戳記，杜絕任何 OS 核心排程延遲之干擾。</li>
</ol>

<h4>五、MiFID II 合規標準與即時漂移監控</h4>
<ul>
  <li><strong>歐盟 MiFID II RTS 25 剛性標準</strong>：高頻演算法交易系統之最大容許時間偏差<strong>不得超過 100 微秒</strong>，且時鐘解析度需達 1 微秒以內。</li>
  <li><strong>時鐘健康度連續監控</strong>：部署專用 PTP 監控探針，每秒量測 offsetFromMaster 與 meanPathDelay。若時間漂移超過 10 微秒，系統立即發送 P1 告警，並無縫切換至備援時鐘源，確保全市場交易秩序固若金湯。</li>
</ul>
""",
            "examinerTips": "得分關鍵詞：『逐筆撮合委託順序與時間同步公平性』、『IEEE 1588 PTP v2 vs NTP 網卡 PHY 層硬體打點』、『GNSS 衛星欺騙 (SDR偽造時間平移) 與 Jamming』、『銣/銫原子鐘 24小時維持漂移 < 1微秒』、『MiFID II RTS 25 容許誤差 < 100微秒』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>業務背景與核心技術對比 (7分)</strong>：明確指明逐筆撮合與防止搶先交易（Front-Running）的關聯，深入列表剖析 PTP v2 與 NTP 在硬體時戳與 Boundary Clock 上的根本差距。</li>
  <li><strong>GNSS 欺騙威脅解析 (6分)</strong>：詳細闡述軟體定義無線電（SDR）欺騙原理及其如何扭曲交易時間戳，展現前沿實體與資安交叉攻防思維。</li>
  <li><strong>雙時脈源抗干擾架構 (6分)</strong>：提出 CRPA 天線、多星系比對與機房在地銣原子鐘 Holdover 方案，論證完整嚴密。</li>
  <li><strong>MiFID II 合規與監控 (6分)</strong>：引用國際金融指標性規範 MiFID II RTS 25（100 微秒公差），給予量化監控指標。</li>
</ul>
"""
        },

        # 4. sec-essay-72: Cross-Organization Identity Federation, SAML 2.0 / OIDC & Token Protection
        {
            "id": "sec-essay-72",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "證券周邊單位跨機構身分同調（Identity Federation）、SAML 2.0 / OIDC 與 Token 竊取防護實戰",
            "summary": "剖析證券周邊單位（證交所/櫃買/集保/期交所）單一身分跨系統互聯、SAML 2.0 元數據信任鏈與 OIDC 認證流、XML 簽章重包裝（XSW）與 Token 竊取攻防、DPoP（RFC 9449）與 Back-Channel Logout 會話同步終止實踐。",
            "points": 25,
            "rubric": "1. 跨機構身分同調業務架構與 SAML 2.0 vs OIDC 運作機制 (6分)；2. Federation 架構重大攻擊向量剖析 (7分)；3. DPoP（RFC 9449）與憑證綁定防 Token 竊取 (7分)；4. 跨機構 Back-Channel Logout 與即時風控 (5分)",
            "question": "臺灣證券周邊單位（TWSE 證交所、TPEx 櫃買中心、TDCC 集保結算所、TAIFEX 期交所）推動「周邊單位單一身分跨系統互聯」。試申論：(1) SAML 2.0 與 OpenID Connect (OIDC) 在跨機構身分同調之認證流程與信任鏈（Metadata Trust Exchange）建置；(2) 攻擊者針對 Federation 架構之常見攻擊（如 SAML Assertion 偽造、XML 簽章重包裝攻擊 XML Signature Wrapping, XSW、Token 重放與 Token 竊取 Pass-the-Token）；(3) 實務防禦控制：憑證綁定（Certificate-Bound Access Tokens）、DPoP（Demonstrating Proof-of-Possession, RFC 9449）與一次性發行 Token 撤銷機制；(4) 跨機構會話同步終止（Back-Channel Logout）與連動風控設計。",
            "modelAnswer": r"""
<h4>一、破題：資本市場周邊四合一身分聯邦之戰略意義</h4>
<p>為提升金融行政效率與強化市場跨平臺風控，主管機關推動證交所（TWSE）、櫃買中心（TPEx）、期交所（TAIFEX）與集保結算所（TDCC）之<strong>「周邊單位跨機構身分聯邦（Identity Federation）」</strong>。透過單一簽入（SSO），允許經授權之機構主管、券商交易員及主管機關稽核員以一套身分安全存取四大單位之後台系統。</p>

<h4>二、SAML 2.0 與 OpenID Connect (OIDC) 運作流程與信任鏈</h4>
<ul>
  <li><strong>SAML 2.0（企業級與後台系統）</strong>：
    <ul>
      <li><strong>角色分工</strong>：身分提供者（Identity Provider, IdP）負責身分鑑別與 MFA；服務提供者（Service Provider, SP）驗證宣告並給予存取。</li>
      <li><strong>元數據信任交換（Metadata Trust）</strong>：雙方預先離線交換 X.509 簽章憑證與端點 URL，所有 SAML Response 與 Assertion 強制以 IdP 私鑰數位簽章並對稱加密。</li>
    </ul>
  </li>
  <li><strong>OpenID Connect (OIDC，現代化 API 與行動終端)</strong>：
    <ul>
      <li>基於 OAuth 2.0 擴充，採用標準 <strong>JSON Web Token (JWT)</strong> 之 <code>id_token</code> 承載身分宣告，並以 <code>access_token</code> 存取周邊 API。</li>
      <li>透過 IdP 之 <code>.well-known/openid-configuration</code> 與 <strong>JWKS（JSON Web Key Set）</strong> 公開金鑰端點自動實現金鑰滾動驗證。</li>
    </ul>
  </li>
</ul>

<h4>三、身分同調架構核心攻擊手法分析</h4>
<ol>
  <li><strong>XML 簽章重包裝攻擊（XML Signature Wrapping, XSW）</strong>：
    <ul>
      <li>攻擊者攔截合法的 SAML Assertion，利用 XML 解析器在處理多個相同標籤時的邏輯瑕疵，將原始已簽章的 Assertion 包裹隱藏，另行偽造未經簽章但包含管理員特權（如 <code>Role=SuperAdmin</code>）的 Assertion。</li>
      <li>若 SP 驗證簽章成功但業務邏輯讀取到偽造節點，將造成直接越權提權。</li>
    </ul>
  </li>
  <li><strong>Token 竊取與重放（Pass-the-Token）</strong>：
    <ul>
      <li>Bearer Token 本質為「持票人憑證」，一旦遭到 XSS 攻擊、中間人攔截或端點日誌洩漏，攻擊者可在有效期限內持該 Token 偽冒合法用戶向四大周邊單位發送請求。</li>
    </ul>
  </li>
</ol>

<h4>四、防禦落地：DPoP（RFC 9449）與憑證綁定防 Token 竊取</h4>
<pre><code class="language-text">  [用戶端瀏覽器/終端]
    │ 1. 於本地生成暫態非對稱金鑰對 (Private/Public Key)
    │ 2. 請求發送: Header 附掛 DPoP Proof (以私鑰對 HTTP Method+URL 簽章)
    ▼
  [IdP 身分提供者]
    │ 3. 簽發 Access Token，內部嵌入客戶端公鑰指紋 (jkt = SHA-256(JWK))
    ▼
  [周邊單位 API 閘道器]
    │ 4. 驗證: 請求之 DPoP Header 簽章是否合法？且公鑰指紋是否與 Token 內部 jkt 一致？
    └──> 若攻擊者僅單純竊取 Token，無客戶端私鑰即無法偽造 DPoP Proof，請求遭瞬間拒絕！</code></pre>
<ol>
  <li><strong>DPoP（RFC 9449）發送者限制存取權杖</strong>：徹底解決 Bearer Token 遭竊風險，將 Token 與請求端私鑰深度綁定。</li>
  <li><strong>嚴格 XML 簽章校驗</strong>：SAML SP 必須指定完整 XML 路徑（Schema Validation）並強制要求同時對 <code>&lt;saml:Response&gt;</code> 與 <code>&lt;saml:Assertion&gt;</code> 雙重簽章，徹底封死 XSW 漏洞。</li>
  <li><strong>短效期與一次性 Refresh Token</strong>：Access Token 有效期縮短至 5~15 分鐘，Refresh Token 實施 Rotation（每次刷新即失效舊 Token）。</li>
</ol>

<h4>五、跨機構會話同步終止（Back-Channel Logout）與連動風控</h4>
<ul>
  <li><strong>OpenID Connect Back-Channel Logout 1.0</strong>：當用戶於證交所點擊登出，或被 SOC 偵測到異常被踢除時，證交所 IdP 於伺服器後台主動向櫃買、集保、期交所之 Logout Endpoint 發送簽名之 <code>logout_token</code>，毫秒級同步清除全體周邊單位之活躍 Session。</li>
  <li><strong>即時情資連動</strong>：若集保結算所觸發高危 UEBA 告警，聯邦系統即刻通知全體周邊單位同步降權，阻絕跨機構橫向滲透。</li>
</ul>
""",
            "examinerTips": "得分關鍵詞：『證券周邊四單位身分聯邦』、『SAML 2.0 Metadata 信任鏈 vs OIDC JWKS』、『XML 簽章重包裝攻擊 (XSW) 越權提權原理』、『DPoP (RFC 9449) 與 Token 發送者綁定』、『Back-Channel Logout 跨機構會話同步終止』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>金融業務場景切入 (6分)</strong>：精準以周邊單位聯邦 SSO 為背景，解析 SAML 2.0 與 OIDC 適用層次。</li>
  <li><strong>攻防漏洞深度分析 (7分)</strong>：完整解釋 XML Signature Wrapping (XSW) 解析器邏輯漏洞與 Bearer Token 遭竊重放弱點。</li>
  <li><strong>前沿標準解決方案 (7分)</strong>：給出 IETF 最新標準 DPoP（RFC 9449）之工作流程圖與數學簽名驗證邏輯，展現領先業界之水準。</li>
  <li><strong>Back-Channel Logout 治理 (5分)</strong>：說明伺服器端後台通知機制，杜絕單點登出後其餘周邊系統仍可存取之安全空窗。</li>
</ul>
"""
        },

        # 5. sec-essay-73: EDR Self-Defense & BYOVD Attack Defense
        {
            "id": "sec-essay-73",
            "category": "sec",
            "chapter": "第 7 章：端點防禦、主機加固、EDR 聯防與惡意程式分析",
            "title": "端點偵測與回應（EDR/XDR）自防禦機制（Anti-Tampering）與驅動程式帶刀攻擊（BYOVD）防護實務",
            "summary": "剖析進階威脅與勒索軟體致盲端點（EDR Blinding）戰術、內核驅動程式帶刀（BYOVD）攻擊與 ntdll unhooking 原理、進程受保護服務（PPL）、HVCI 核心完整性與微軟弱點驅動程式封鎖清單、心跳中斷自動網路隔離（Fail-Closed Quarantine）流程。",
            "points": 25,
            "rubric": "1. EDR 致盲戰術與 BYOVD / Unhooking 攻擊原理 (7分)；2. EDR 代理自身保護機制（PPL 與核心微過濾驅動） (6分)；3. 證券主機 HVCI 與易受攻擊驅動程式封鎖清單實施 (6分)；4. 心跳遺失之 Fail-Closed 自動化隔離處置 (6分)",
            "question": "現代進階持續性威脅（APT）與勒索軟體在侵入主機後，首要目標為癱瘓或致盲端點安全防護代理程式（EDR Blinding）。試申論：(1) 駭客常用的 EDR 繞過與癱瘓手法：內核驅動程式帶刀攻擊（Bring Your Own Vulnerable Driver, BYOVD）、使用者態 Hook 解除（Unhooking ntdll）、以及 AMSI 記憶體修補；(2) EDR 代理程式之核心級自防禦（Kernel-level Self-Defense）、進程受保護服務（Protected Process Light, PPL）與驅動程式數位簽章驗證機制；(3) 證券主機之防禦落地：微軟弱點驅動程式封鎖清單（Vulnerable Driver Blocklist）、HVCI（虛擬化型態程式碼完整性）與嚴格系統檔案存取控制；(4) 當 EDR 代理異常中斷心跳（Heartbeat Loss）時之網路隔離（Fail-Closed Network Quarantine）自動化處置流程。",
            "modelAnswer": r"""
<h4>一、破題：獵手反遭致盲—端點安全之致命生存之戰</h4>
<p>在現代企業網路防禦中，端點偵測與回應（EDR/XDR）是資安維運中心（SOC）之核心耳目。然而，成熟的 APT 組織與勒索軟體（如 BlackCat、LockBit）深知此點，入侵後第一步非直接竊密，而是執行<strong>「EDR 致盲戰術（EDR Blinding）」</strong>。一旦 EDR 失效，主機將完全喪失遙測（Telemetry）能力與記憶體監控，成為不設防的暗室。</p>

<h4>二、駭客 EDR 繞過與癱瘓手法核心剖析</h4>
<ol>
  <li><strong>驅動程式帶刀攻擊（BYOVD, Bring Your Own Vulnerable Driver）</strong>：
    <ul>
      <li>Windows 內核要求驅動程式必須具備合法微軟數位簽章。攻擊者並不自行開發後門驅動，而是攜帶具備合法簽章但存在任意內核記憶體讀寫漏洞的舊版驅動（如舊版防毒或超頻軟體驅動）。</li>
      <li>利用該合法驅動作為跳板，直接修改 Windows 內核記憶體中的 <code>DKOM（直接核心物件操作）</code>，解除 EDR 註冊之內核回調函式（Process/Thread Creation Callbacks），或直接將 EDR 進程結構強制清零。</li>
    </ul>
  </li>
  <li><strong>使用者態 Hook 解除（ntdll Unhooking）</strong>：
    <ul>
      <li>EDR 普遍於使用者空間（User-mode）注入 DLL 並對 <code>ntdll.dll</code> 關鍵 API（如 <code>NtCreateThreadEx</code>）打上 <code>JMP</code> 補丁以實施監控。</li>
      <li>惡意程式從磁碟重新讀取一份乾淨的 <code>ntdll.dll</code> 映象檔，覆蓋記憶體中遭 EDR 監控之 <code>.text</code> 區段（Unhooking），或直接發起原生系統呼叫（Direct System Calls），徹底繞過 EDR 監控。</li>
    </ul>
  </li>
  <li><strong>AMSI / ETW 記憶體修補</strong>：透過將 <code>AmsiScanBuffer</code> 或 <code>EtwEventWrite</code> 函數開頭修補為 <code>RET (0xC3)</code>，阻止防毒引擎接收 PowerShell / .NET 腳本遙測。</li>
</ol>

<h4>三、EDR 核心級自防禦機制（Anti-Tampering）</h4>
<ul>
  <li><strong>受保護進程輕量級架構（Protected Process Light, PPL）</strong>：
    <ul>
      <li>EDR 服務進程向作業系統註冊為 <code>PsProtectedSignerAntimalware-Light</code>。</li>
      <li>一旦具備 PPL 屬性，即使以本機最高權限 <code>NT AUTHORITY\SYSTEM</code> 或管理員權限運行的程式，亦無法使用 <code>OpenProcess</code> 取得 <code>PROCESS_TERMINATE</code> 或 <code>PROCESS_VM_WRITE</code> 權限，無法強制殺除進程或寫入記憶體。</li>
    </ul>
  </li>
  <li><strong>內核微過濾器驅動程式（Minifilter Driver）防護</strong>：
    <ul>
      <li>在核心層攔截針對 EDR 二進位檔案、登錄檔（Registry）與設定目錄之寫入操作，防止惡意軟體更名或清空 EDR 程式。</li>
    </ul>
  </li>
</ul>

<h4>四、證券核心主機防禦 BYOVD 之加固矩陣</h4>
<pre><code class="language-text">  [惡意軟體試圖載入具漏洞之簽名驅動]
                    │
                    ▼
  [WDAC 應用程式控制 / HVCI 核心完整性保護]
    ├── (比對微軟弱點驅動程式封鎖清單 Microsoft Driver Blocklist)
    └── (硬體虛擬化保護 VBS 驗證: 核心頁面 W^X 禁止任意寫入執行)
                    │
                    ▼
              [載入被直接阻斷拒絕！]</code></pre>
<ol>
  <li><strong>微軟弱點驅動程式封鎖清單（Microsoft Vulnerable Driver Blocklist）</strong>：於 Windows Server 群組原則全面啟用，即時阻斷已知常被勒索軟體利用之 400+ 款舊版驅動。</li>
  <li><strong>虛擬化型態程式碼完整性（HVCI）與 VBS</strong>：利用 CPU 硬體虛擬化技術，將 Windows 內核放置於安全虛擬環境（VSM），即使攻擊者取得核心讀寫權限，亦無法修改內核程式碼頁面，粉碎 DKOM 攻擊。</li>
</ol>

<h4>五、心跳遺失時之 Fail-Closed 自動化隔離處置流程</h4>
<p>針對高敏金融主機，建立「假設已被致盲」之自動化處置流程：</p>
<ol>
  <li><strong>心跳中斷即時告警</strong>：EDR 雲端/在地管理平台若連續 <strong>60 秒</strong> 未收到伺服器代理心跳，自動觸發 P1 緊急資安事件。</li>
  <li><strong>頻外網路硬體隔離（Fail-Closed Network Quarantine）</strong>：
    <ul>
      <li>SOAR 平台透過 API 連動頂架交換機（ToR Switch），立即將該主機連接埠切換至<strong>隔離 VLAN</strong>，阻斷其存取核心資料庫與內部網路（東西向橫向移動全部封鎖）。</li>
      <li>通報 SOC 輪值工程師透過頻外通道（OOB / IPMI）進入伺服器採集記憶體轉儲（Crash Dump），確保即便 EDR 代理遭突破，威脅亦無法擴散至資本市場。</li>
    </ul>
  </li>
</ol>
""",
            "examinerTips": "得分關鍵詞：『EDR 致盲戰術 (Blinding)』、『BYOVD 攜帶合法舊漏洞驅動修改核心記憶體 DKOM』、『ntdll Unhooking 與 Direct Syscall 繞過使用者態監控』、『Windows PPL (Protected Process Light) 防殺』、『HVCI + 微軟弱點驅動封鎖清單』、『心跳遺失 60 秒 ToR 交換機 Fail-Closed 隔離』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>威脅原理剖析 (7分)</strong>：深度拆解 BYOVD（內核攻防）、Unhooking（使用者空間記憶體修補）及 AMSI 繞過原理，技術詞彙精準到位。</li>
  <li><strong>自身防禦機制 (6分)</strong>：詳細解析微軟 PPL 架構與核心微過濾驅動，說明為甚麼單純 SYSTEM 權限無法終止受保護進程。</li>
  <li><strong>硬體層與主機防禦落地 (6分)</strong>：列舉微軟 Driver Blocklist 與 HVCI/VBS 硬體安全隔離，展現進階系統加固實務。</li>
  <li><strong>Fail-Closed 應變設計 (6分)</strong>：針對證券交易所特殊場景，給出 60 秒心跳遺失自動透過底層網路交換機斷網隔離之架構設計。</li>
</ul>
"""
        },

        # 6. sec-essay-74: CASB, Shadow IT Governance & Cross-Cloud DLP
        {
            "id": "sec-essay-74",
            "category": "sec",
            "chapter": "第 10 章：雲端安全、容器化防護與微服務架構",
            "title": "金融機構雲端 SaaS 與影子 IT（Shadow IT）治理：CASB 代理、OAuth 授權洗白與跨雲 DLP 實踐",
            "summary": "深入解構金融機構使用公有雲協作與外包影子 IT（Shadow IT）外洩風險、CASB 正向代理/反向代理/API 模式比較、惡意 OAuth 授權同意（Consent Granting）釣魚攻防、精確資料比對（EDM）DLP 攔截與金管會委外個資合規實務。",
            "points": 25,
            "rubric": "1. 影子 IT 威脅本質與 CASB 三大部屬模式技術對比 (7分)；2. 惡意 OAuth 應用程式授權洗白（Consent Phishing）攻防 (6分)；3. 精確資料比對（EDM）與敏感資料外洩防護（DLP）落地 (6分)；4. 符合金管會雲端委外作業規範之稽核實踐 (6分)",
            "question": "隨著金融數位轉型，證券機構內部同仁與外包團隊常使用未經核准之第三方雲端協作工具（如公共雲端硬碟、外包 GenAI 平台、SaaS 專案管理工具），形成「影子 IT（Shadow IT）」與營業秘密外洩風暴。試申論：(1) 雲端存取安全代理（Cloud Access Security Broker, CASB）在正向代理（Forward Proxy）、反向代理（Reverse Proxy）與 API 模式之運作架構比較；(2) 員工隨意授予第三方 OAuth 應用程式授權（OAuth App Consent Granting）以存取機構郵件或雲端檔案之安全威脅與防禦機制；(3) 證券資料外洩防護（DLP）：正規表達式（Regex）、精確資料比對（EDM）與數位指紋（Document Fingerprinting）在 SaaS 傳輸中之攔截應用；(4) 符合金管會委外與跨雲個資加密保存之安全稽核實務。",
            "modelAnswer": r"""
<h4>一、破題：雲端協作浪潮下失控的「影子 IT」危機</h4>
<p>在金融數位轉型與敏捷開發推動下，同仁或第三方委外廠商為求工作便利，常私自採用未經資安部門核准之 SaaS 服務（如個人 Google Drive、Notion、ChatGPT、GitHub），此現象即為<strong>「影子 IT（Shadow IT）」</strong>。影子 IT 徹底打破機構網路邊界，導致機敏交易原始碼、客戶身分證號及未公開財報面臨外洩風險，亦構成違反金管會委外資安法規之重大合規漏洞。</p>

<h4>二、CASB 三大部署模式全維度架構對比</h4>
<table class="essay-table">
  <thead>
    <tr><th>部署模式</th><th>運作機制</th><th>優點</th><th>限制與弱點</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>正向代理 (Forward Proxy)</strong></td>
      <td>於員工受管設備安裝代理程式（PAC/Agent），所有上網流量強制經過 CASB 檢驗。</td>
      <td>可全面管控<strong>任何已託管或非託管 SaaS</strong>，即時攔截非法上傳。</td>
      <td>需端點部署軟體；無法管控外包人員自攜之非受管設備（BYOD）。</td>
    </tr>
    <tr>
      <td><strong>反向代理 (Reverse Proxy)</strong></td>
      <td>用戶存取機構受管之 SaaS（如 M365）時，DNS/IdP 將流量引流至 CASB 閘道。</td>
      <td><strong>無須於端點安裝代理</strong>，完美適用於外包商與 BYOD 存取保護。</td>
      <td>僅能防護已知受管之 SaaS，對員工存取未知外部雲端硬碟完全無能為力。</td>
    </tr>
    <tr>
      <td><strong>API 整合模式 (Out-of-Band)</strong></td>
      <td>CASB 直接透過 SaaS 提供之官方 REST API 連線，異步掃描雲端儲存空間。</td>
      <td><strong>對用戶完全透明無延遲</strong>；可掃描雲端休眠資料（Data-at-Rest）。</td>
      <td>非在線（In-line）即時阻斷，存在外洩後至掃描完成之「時間差」。</td>
    </tr>
  </tbody>
</table>
<p><strong>最佳實踐</strong>：證交所應採取<strong>「多模態 CASB（Multimode CASB）」</strong>：正向代理管束受管端點 + 反向代理限制外包存取 + API 模式審計雲端靜態檔案。</p>

<h4>三、惡意 OAuth 授權同意釣魚（Consent Phishing）攻防</h4>
<ol>
  <li><strong>攻擊向量</strong>：駭客不再直接誘騙輸入密碼，而是架設惡意雲端 App，誘使員工在微軟/Google 登入畫面點擊「同意授權（Accept Consent）」。一旦取得 <code>Mail.Read</code> 或 <code>Files.ReadWrite.All</code> 之 OAuth Refresh Token，黑客即可長年無感存取信箱與雲端硬碟，即使員工修改密碼或啟用 MFA 亦無法阻斷。</li>
  <li><strong>防禦控制機制</strong>：
    <ul>
      <li><strong>徹底關閉使用者自主同意授權</strong>：設定 Microsoft Entra ID / Google Workspace 原則，全面禁止一般使用者同意未經驗證發行者之應用程式。</li>
      <li><strong>管理員同意工作流程（Admin Consent Workflow）</strong>：第三方應用程式申請權限時，強制發起資安審查流程，嚴格審視其請求之 Scopes 最小權限。</li>
      <li><strong>已發行權限即時清理</strong>：CASB 定期自動盤點全機構現存授權，對超過 90 天未活躍或具備高危權限之 App 即刻自動撤銷 Token。</li>
    </ul>
  </li>
</ol>

<h4>四、跨雲 DLP：精確資料比對（EDM）與指紋攔截實踐</h4>
<ul>
  <li><strong>正規表達式（Regex）的極限與誤報</strong>：傳統 Regex（如身分證格式 <code>^[A-Z][12]\d{8}$</code>）易對隨機序號產生大量誤報，造成資安維運疲乏。</li>
  <li><strong>精確資料比對（Exact Data Match, EDM）</strong>：
    <ul>
      <li>資安團隊從證券核心庫擷取投資人「姓名 + 身分證字號 + 證券帳號」三欄位，於在地安全環境計算單向加密雜湊（SHA-256 with Salt）並匯入 CASB。</li>
      <li>當員工試圖向雲端上傳或貼上內容時，CASB 即時計算內容雜湊，<strong>僅當三者同時精準匹配時方觸發 P1 攔截</strong>，誤報率趨近於零。</li>
    </ul>
  </li>
  <li><strong>數位指紋（Document Fingerprinting）</strong>：對證交所董事會機敏簡報、法規未公開草案等原始範本計算檔案特徵指紋，即便內容遭剪下貼上至新文字檔，亦能秒級辨識並即時阻斷外傳。</li>
</ul>

<h4>五、符合金管會委外作業規範之稽核實務</h4>
<p>金管會「金融機構作業委託他人處理內部作業制度及程序辦法」要求，使用雲端服務涉及客戶重大機敏資訊時，必須落實<strong>客戶自持金鑰（BYOK/HYOK）</strong>、留存可追溯之存取紀錄至少 5 年，並具備隨時終止委外與資料完整匯回之退場能力。證交所透過 CASB 自動產出多雲合規報表，為主管機關提供可量化、無死角之稽核軌跡。</p>
""",
            "examinerTips": "得分關鍵詞：『影子 IT (Shadow IT) 與雲端失控』、『CASB 多模態部屬 (正向代理 + 反向代理 + API 模式對照)』、『惡意 OAuth 同意釣魚 (Consent Phishing) 與禁用自主授權』、『精確資料比對 EDM (Exact Data Match with Salted Hash) 零誤報』、『金管會雲端委外作業規範合規』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>業務背景與 CASB 三大模式分析 (7分)</strong>：精確定義影子 IT 危害，詳細列表評估 Forward Proxy、Reverse Proxy 與 API 模式之優缺點，給出金融級多模態融合部署結論。</li>
  <li><strong>OAuth 同意授權釣魚剖析 (6分)</strong>：切中近兩年金融界最頭痛之 OAuth Consent Granting 攻擊，闡述為何修改密碼無效並給出管理員工作流審核處方。</li>
  <li><strong>DLP 技術細節（EDM vs Regex）(6分)</strong>：深入說明 EDM 加鹽雜湊比對原理，展現對高準確率機敏資料防洩漏之工程掌握。</li>
  <li><strong>金管會法規稽核實務 (6分)</strong>：無縫接合金管會雲端委外辦法（BYOK、5年軌跡、退場機制），體現金融證券專業度。</li>
</ul>
"""
        },

        # 7. sec-essay-75: Threat Modeling (STRIDE & Attack Tree & DREAD)
        {
            "id": "sec-essay-75",
            "category": "sec",
            "chapter": "第 9 章：軟體安全、安全開發生命週期（SSDLC）與安全測試",
            "title": "金融核心交易系統威脅建模（Threat Modeling）：STRIDE 方法論、攻擊樹（Attack Tree）與 DREAD 風險量化評估實戰",
            "summary": "深入剖析金融交易系統安全左移核心實踐：資料流程圖（DFD）繪製信任邊界、微軟 STRIDE 六大威脅對應資安屬性、委託竄改與假冒之攻擊樹（Attack Tree）分解、以及 DREAD 模型五維度風險等級量化評估矩陣。",
            "points": 25,
            "rubric": "1. 威脅建模在金融 SSDLC 安全左移階段之定位 (6分)；2. STRIDE 六大威脅分類與資安 CIA+ 三大屬性對映 (7分)；3. 攻擊樹（Attack Tree）分解撮合委託遭偽造竄改流程 (6分)；4. DREAD 五維度量化風險優先級打分實踐 (6分)",
            "question": "金管會要求金融機構實踐安全軟體開發生命週期（SSDLC），於需求與系統設計階段即導入「威脅建模（Threat Modeling）」，防範系統上線後修補代價暴增。試針對臺灣證券交易所核心交易下單系統，申論：(1) 威脅建模之標準執行四步驟（What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job?）；(2) 微軟 STRIDE 威脅分類模型之六大維度（Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege）及其所破壞之資通安全屬性（如 CIA+）；(3) 針對「外部惡意下單委託竄改與未授權撤單」情境，繪製文字化之「攻擊樹（Attack Tree）」根節點與葉節點推導；(4) 運用 DREAD 風險評估模型（Damage, Reproducibility, Exploitability, Affected Users, Discoverability）量化計算風險分數，並排定修補優先順序之金融實踐。",
            "modelAnswer": r"""
<h4>一、破題：安全左移（Shift-Left）之核心靈魂—威脅建模</h4>
<p>在軟體工程經典理論中，系統於架構設計階段發現並修復一項資安架構缺陷之成本為 1；若留待系統上線進入維運後才修補，其代價將暴增 <strong>30 至 100 倍</strong>，在微秒決勝之金融撮合系統更將引發市場停擺與民刑事訴訟。<strong>威脅建模（Threat Modeling）</strong>是安全開發生命週期（SSDLC）之頂層設計，旨在「未寫一行程式碼之前，先在藍圖上找出所有被攻破之可能」。</p>

<h4>二、威脅建模四步法與 DFD 信任邊界</h4>
<ol>
  <li><strong>我們正在建構什麼？（What are we working on?）</strong>：繪製詳細之<strong>資料流程圖（Data Flow Diagram, DFD）</strong>，標註外部實體（券商交易員、API 客戶端）、處理程序（訂單校驗模組、撮合引擎）、資料儲存（訂單資料庫、記憶體佇列）以及跨越之<strong>「信任邊界（Trust Boundaries）」</strong>。</li>
  <li><strong>哪裡可能出錯？（What can go wrong?）</strong>：針對穿越信任邊界之每個資料流與處理元件，全面套用 STRIDE 模型識別威脅。</li>
  <li><strong>我們該如何處置？（What are we going to do about it?）</strong>：針對辨識之威脅擬定對應之安全控制措施（緩解、轉移、消除或接受）。</li>
  <li><strong>我們做得夠好嗎？（Did we do a good enough job?）</strong>：覆盤確認所有邊界威脅是否均已覆蓋，更新威脅模型資產庫。</li>
</ol>

<h4>三、微軟 STRIDE 威脅分類與資安防護屬性映射</h4>
<table class="essay-table">
  <thead>
    <tr><th>STRIDE 威脅維度</th><th>威脅本質定義</th><th>破壞之資通安全屬性</th><th>金融下單系統對應防禦措施</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>S - Spoofing（假冒身分）</strong></td>
      <td>偽裝成合法證券商或授權交易員發送委託單。</td>
      <td><strong>真實性（Authenticity）</strong></td>
      <td>強制 FIDO2 / WebAuthn 硬體鑑別、mTLS 雙向憑證。</td>
    </tr>
    <tr>
      <td><strong>T - Tampering（竄改資料）</strong></td>
      <td>在傳輸或記憶體中修改委託股數、股票代號或價格。</td>
      <td><strong>完整性（Integrity）</strong></td>
      <td>封包附掛 HMAC-SHA256、Ed25519 數位簽章。</td>
    </tr>
    <tr>
      <td><strong>R - Repudiation（否認行為）</strong></td>
      <td>用戶事後否認曾下達大額巨量買賣或違約交割。</td>
      <td><strong>不可否認性（Non-repudiation）</strong></td>
      <td>RFC 3161 第三方時戳（TSA）＋ WORM 不可抹滅交易軌跡。</td>
    </tr>
    <tr>
      <td><strong>I - Information Disclosure（資訊洩漏）</strong></td>
      <td>在傳輸過程中窺探其他券商之大單委託與未公開行情。</td>
      <td><strong>機密性（Confidentiality）</strong></td>
      <td>TLS 1.3 前向保密（ECDHE）、靜態資料 AES-256 加密。</td>
    </tr>
    <tr>
      <td><strong>D - Denial of Service（阻斷服務）</strong></td>
      <td>發送高頻巨量無效畸形封包癱瘓撮合下單閘道器。</td>
      <td><strong>可用性（Availability）</strong></td>
      <td>Token Bucket 令牌桶動態限流、BGP Anycast 清洗。</td>
    </tr>
    <tr>
      <td><strong>E - Elevation of Privilege（特權提升）</strong></td>
      <td>一般查詢帳號透過越權注入漏洞取得撮合管理特權。</td>
      <td><strong>授權控制（Authorization）</strong></td>
      <td>嚴格 RBAC/ABAC、Linux 核心命名空間與降權執行。</td>
    </tr>
  </tbody>
</table>

<h4>四、證券下單情境之「攻擊樹（Attack Tree）」分解</h4>
<p>針對目標【根節點：偽造或惡意竄改撮合委託單】：</p>
<pre><code class="language-text">  [目標: 成功將偽造委託單送入撮合引擎成交] (OR 條件)
     │
     ├── 1. 突破邊界下單閘道身分驗證 (AND 條件)
     │     ├── 1.1 竊取券商 API 私鑰憑證 (透過外包開發機跳板)
     │     └── 1.2 偽造合法 mTLS 連線與繞過來源 IP 白名單
     │
     ├── 2. 中間人攻擊竄改傳輸中委託單 (AND 條件)
     │     ├── 2.1 侵入電信業者專線中繼交換機
     │     └── 2.2 破解或重放 FIX 協定封包 (重放 SeqNum)
     │
     └── 3. 內網核心節點記憶體直接注入 (AND 條件)
           ├── 3.1 滲透撮合伺服器取得本機 root 權限
           └── 3.2 透過 ptrace / 記憶體注入覆寫撮合佇列資料結構</code></pre>
<p><strong>攻擊樹防護效益</strong>：透過攻擊樹將抽象威脅拆解為具體可度量的葉節點路徑，資安架構師只需在任一 AND 條件的節點佈建強控制（如 mTLS 結合硬體 TPM 憑證），即可徹底截斷整條攻擊路徑。</p>

<h4>五、DREAD 模型量化風險優先級實踐</h4>
<p>為克服傳統「高/中/低」主觀評估缺陷，採用 <strong>DREAD 模型</strong>（每項評分 1~10 分，總分 $S = \frac{\sum}{5}$）：</p>
<ol>
  <li><strong>Damage Potential（潛在損害）</strong>：若成功，對市場交易秩序與財務損失程度（竄改成交價可給 10 分）。</li>
  <li><strong>Reproducibility（再現性）</strong>：攻擊手法再次成功的容易度（每次皆可重現給 10 分，需特定極端競爭條件給 3 分）。</li>
  <li><strong>Exploitability（可利用性）</strong>：發動攻擊所需之技術門檻與工具資源（需新手黑客即有自動化工具給 10 分，需國家級客製化惡意程式給 2 分）。</li>
  <li><strong>Affected Users（受影響使用者範圍）</strong>：波及全市場投資人（10 分）或單一測試帳戶（1 分）。</li>
  <li><strong>Discoverability（可發現性）</strong>：漏洞是否容易被搜尋引擎或自動化工具探測（如公開 API 暴露給 10 分，深度封閉內網核心給 2 分）。</li>
</ol>
<p><strong>決策矩陣</strong>：凡總分 <strong>S ≥ 8 分</strong> 列為 P1 極度致命風險，必須於架構設計審查會（Architecture Review Board, ARB）一票否決，直至提出架構重構方案徹底緩解後方准進入編程階段。</p>
""",
            "examinerTips": "得分關鍵詞：『威脅建模四步法 (What are we working on / go wrong / do about it / did well)』、『DFD 信任邊界 (Trust Boundary)』、『STRIDE 六大維度與 CIA+ 映射』、『攻擊樹 Attack Tree (AND/OR 邏輯拆解)』、『DREAD 五維度量化打分 (Damage, Reproducibility, Exploitability, Affected Users, Discoverability)』、『P1 致命架構一票否決機制』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>安全左移定位 (6分)</strong>：精準指出設計階段修補成本僅為維運階段的 1/30~1/100，提出標準四步法，開篇立論高屋建瓴。</li>
  <li><strong>STRIDE 矩陣與 CIA+ 映射 (7分)</strong>：條列清晰完整對齊 S-T-R-I-D-E 六大字母，明確指出破壞的 Authenticity、Integrity、Non-repudiation、Confidentiality、Availability、Authorization 六大屬性與金融對策。</li>
  <li><strong>攻擊樹邏輯推導 (6分)</strong>：以撮合委託竄改為例，展現 AND/OR 邏輯分解樹，說明如何透過切斷葉節點來粉碎整條攻擊鏈。</li>
  <li><strong>DREAD 量化決策 (6分)</strong>：定義 D-R-E-A-D 五大因子計算公式，並給出金融系統 P1 致命風險一票否決之治理標準。</li>
</ul>
"""
        },

        # 8. sec-essay-76: Open Source License Compliance & Dependency Supply Chain Governance
        {
            "id": "sec-essay-76",
            "category": "sec",
            "chapter": "第 9 章：軟體安全、安全開發生命週期（SSDLC）與安全測試",
            "title": "開源軟體授權合規與相依性傳染性風險治理：SCA、GPL/AGPL 穿透風險與漏洞修補實踐",
            "summary": "深入解構金融交易引擎引入開源軟體（OSS）之強傳染性授權（GPL/AGPL v3）穿透風險、SCA 動態/靜態鏈結分析、相依性投毒隔離、上游無官方 patch 時之熱修補（Hotpatching）與補償控制實務。",
            "points": 25,
            "rubric": "1. 傳染性授權（Copyleft）法律本質與證券專有系統開源風險 (6分)；2. SCA 工具於 CI/CD 流程之授權合規檢核機制 (7分)；3. 開源套件投毒攻擊向量與私有相依庫防禦 (6分)；4. 零日漏洞且上游無補丁時之熱修補與補償控制 (6分)",
            "question": "金融關鍵系統研發高度引用開源軟體（OSS），然而開源相依性伴隨「傳染性授權（Copyleft License）」法律訴訟風險與高危漏洞修補挑戰。試申論：(1) 強傳染性授權（GPL v3, AGPL v3）與寬鬆型授權（MIT, Apache 2.0, BSD）之法律核心差異，及其對證券核心交易引擎商業專有原始碼強制公開之潛在風險；(2) 軟體組成分析（Software Composition Analysis, SCA）工具在 CI/CD 流程中自動辨識動態鏈結（Dynamic Linking）與靜態鏈結（Static Linking）之授權合規檢核機制；(3) 開源軟體相依性套件投毒（Typosquatting、Dependency Confusion）之沙盒檢測與私有鏡像庫（Private Artifact Repository）隔離防禦；(4) 當開源套件爆發重大 CVE 漏洞且上游無官方修補釋出時，金融機構之「熱修補（Hotpatching）」與「控制補償措施（Compensating Controls）」標準作業程序。",
            "modelAnswer": r"""
<h4>一、破題：開源雙面刃—金融創新的基石與法律合規的未爆彈</h4>
<p>在現代金融軟體研發中，超過 80% 的應用程式碼來自開源第三方相依套件（Open Source Software, OSS）。然而，開源軟體並非「公共領域（Public Domain）」，每一行開源代碼皆受到著作權法與相應的授權條款約束。若缺乏嚴格的相依性合規治理，將面臨兩大致命風險：<strong>「專有交易核心原始碼遭強迫公開之法律訴訟」</strong>與<strong>「開源套件帶毒或未修補之零日漏洞入侵」</strong>。</p>

<h4>二、開源授權矩陣對比與強傳染性風險剖析</h4>
<table class="essay-table">
  <thead>
    <tr><th>授權類別</th><th>代表授權條款</th><th>修改後衍生著作是否強制開源？</th><th>對證券專有系統之潛在法律衝擊</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>寬鬆型授權 (Permissive)</strong></td>
      <td>MIT, Apache 2.0, BSD-2/3-Clause</td>
      <td><strong>否</strong>。僅需保留原始著作權宣告與免責聲明。</td>
      <td><strong>最安全推薦</strong>。商業友善，可自由封裝於證券撮合商業軟體。</td>
    </tr>
    <tr>
      <td><strong>弱傳染性授權 (Weak Copyleft)</strong></td>
      <td>LGPL v2.1/v3, MPL 2.0</td>
      <td>若僅透過<strong>動態鏈結（Dynamic Linking）</strong>引用庫則不強制；若修改庫本身則修改部分需開源。</td>
      <td>需嚴格審查鏈結方式，嚴禁靜態編譯合併。</td>
    </tr>
    <tr>
      <td><strong>強傳染性授權 (Strong Copyleft)</strong></td>
      <td>GPL v2 / GPL v3</td>
      <td><strong>是</strong>。任何結合衍生著作（Derivative Work）必須以相同授權<strong>強制公開全部原始碼</strong>。</td>
      <td><strong>極高風險</strong>。若交易引擎靜態鏈結 GPL 模組，對手券商可訴請要求證交所公開全部核心撮合演算源碼！</td>
    </tr>
    <tr>
      <td><strong>網路傳染性授權 (Network Copyleft)</strong></td>
      <td>AGPL v3, SSPL</td>
      <td><strong>是</strong>。即使<strong>僅透過網路提供 SaaS 服務</strong>，未實體散布二進位檔案，亦強制公開伺服器原始碼。</td>
      <td><strong>絕對禁止引入</strong>。直接衝擊雲端金融與行情推播服務。</td>
    </tr>
  </tbody>
</table>

<h4>三、SCA 工具在 CI/CD Pipeline 之自動化檢核機制</h4>
<pre><code class="language-text">  [開發者 Git Commit / PR]
            │
            ▼
  [CI/CD 構建管線 (Jenkins / GitLab CI)]
    ├── 1. 產生完整 SBOM 清單 (CycloneDX / SPDX)
    ├── 2. SCA 引擎掃描相依樹 (Direct & Transitive Dependencies)
    │      ├── [授權比對] ──> 偵測到 AGPL/GPL 條款？ ──> 【直接中斷 Build (Fail the Build)】
    │      └── [漏洞比對] ──> 比對 NVD / GitHub Advisory 資料庫
    └── 3. 鏈結型態深度解析 (靜態 .a/.lib vs 動態 .so/.dll)</code></pre>
<ol>
  <li><strong>傳遞性相依性（Transitive Dependencies）分析</strong>：開發者可能僅直接引用 A 套件（MIT 授權），但 A 套件內部偷偷依賴 B 套件（GPL 授權）。SCA 工具必須遞迴剖析完整 AST 與依賴圖譜，防止「隱形傳染」。</li>
  <li><strong>鏈結相依性語義分析</strong>：針對 C/C++ 等底層極低延遲交易語言，SCA 工具檢驗二進位符號表（Symbol Table），確保 LGPL 模組僅以動態動態鏈結庫（<code>.so</code> / <code>.dll</code>）形式存在，絕無靜態內嵌。</li>
</ol>

<h4>四、相依性投毒攻擊防禦與私有鏡像庫隔離</h4>
<ul>
  <li><strong>字元錯字劫持（Typosquatting）與相依性混淆（Dependency Confusion）</strong>：
    <ul>
      <li>攻擊者註冊與熱門套件極為相似之名稱（如 <code>cross-envv</code>），或在公共倉庫（npm、PyPI）發布與證交所內部專用私有套件同名但版本號極高（如 <code>99.9.9</code>）之惡意套件，誘騙構建系統下載執行惡意腳本。</li>
    </ul>
  </li>
  <li><strong>多重安全防禦體系</strong>：
    <ul>
      <li><strong>私有工件庫隔離（Nexus / Artifactory）</strong>：全面封閉 CI/CD 伺服器直連公網之權限，所有套件下載統一經由內部私有鏡像代理。</li>
      <li><strong>名稱空間保留（Namespace Reservation）與套件鎖定</strong>：鎖定內部私有套件前綴（如 <code>@twse/trading-core</code>），強制禁止從外部公共倉庫解析該 Scope。</li>
      <li><strong>鎖定檔雜湊校驗（Lockfile Hash Verification）</strong>：專案必須納管 <code>package-lock.json</code> 或 <code>Cargo.lock</code>，構建時強制核對 SHA-512 雜湊值，拒絕浮動版本更新。</li>
    </ul>
  </li>
</ul>

<h4>五、零日漏洞無官方修補時之熱修補（Hotpatching）與補償控制</h4>
<p>當核心依賴庫爆發 Log4j 級別之嚴重零日漏洞（CVSS 10.0），且開源社群尚未釋出修補版本時：</p>
<ol>
  <li><strong>虛擬補丁與邊界攔截（WAF / RASP）</strong>：第一時間於外部 WAF 與 API 閘道器部署正規特徵比對與畸形語法攔截，在網路邊界拒絕攻擊 Payload。</li>
  <li><strong>位元組碼/記憶體熱修補（Bytecode Hotpatching）</strong>：利用 Java Agent、eBPF 或運行時插樁技術，在不重啟或不重新編譯交易引擎之前提下，動態置換記憶體中危險函數之執行邏輯（如直接 <code>return null</code> 阻斷 JNDI 查詢）。</li>
  <li><strong>沙盒降權與補償控制（Compensating Controls）</strong>：強制拔除伺服器多餘外網連線（Egress Filtering），限制該主機僅能向特定資料庫發起通訊，使攻擊者即便利用漏洞亦無法向外回連反彈 Shell（Reverse Shell），堅守交易系統安全底線。</li>
</ol>
""",
            "examinerTips": "得分關鍵詞：『開源非公共領域，強傳染性 Copyleft (GPL/AGPL) 強制開源商業核心風險』、『LGPL 動態鏈結 vs 靜態鏈結合規分界線』、『SCA 深度解析傳遞性依賴 (Transitive Dependencies)』、『相依性混淆 (Dependency Confusion) 與私有 Artifactory 隔離』、『無官方修補時之熱修補 (Hotpatching) 與 RASP/出站流量過濾補償控制』。",
            "detailedExplanation": r"""
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>法律條款深層對比 (6分)</strong>：明確列表對比 MIT、LGPL、GPL 與 AGPL，點出強傳染性對商業專有撮合引擎強制開源的滅頂災難，觀點深刻。</li>
  <li><strong>SCA CI/CD 檢核機制 (7分)</strong>：提出 SBOM 自動產生、相依樹遞迴解析與靜態/動態鏈結符號表檢驗，展現對 DevSecOps 流程的完整掌控。</li>
  <li><strong>相依性投毒防護 (6分)</strong>：詳細拆解 Typosquatting 與 Dependency Confusion 原理，提出私有 Artifactory 隔離、Scope 命名空間保留與 Lockfile 雜湊校驗。</li>
  <li><strong>極限緊急應變 SOP (6分)</strong>：針對「上游無 patch」之實務難題，提出虛擬補丁、位元組碼熱修補與出口流量補償控制，體現高階架構師之應變風範。</li>
</ul>
"""
        }
    ]
