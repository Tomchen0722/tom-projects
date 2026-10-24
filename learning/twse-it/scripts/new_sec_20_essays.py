# -*- coding: utf-8 -*-
"""
20 Brand New, Non-Duplicate Information Security (資通安全) Full-Mark Essays (sec-essay-49 ~ sec-essay-68)
Specifically crafted for Taiwan Stock Exchange (TWSE, 臺灣證券交易所) Information Personnel Recruitment Exam.
All essays follow standard national exam / financial CI criteria:
- 破題立論
- 核心技術架構推導
- 橫向關鍵對比 (HTML table)
- 證交所實務落地與參數調校
- 閱卷評分踩點秘笈 (Examiner Tips)
- 深度評分邏輯解析 (Detailed Explanation)
"""

def get_20_brand_new_sec_essays():
    return [
        # 1. sec-essay-49: SASE / SSE
        {
            "id": "sec-essay-49",
            "category": "sec",
            "chapter": "第 6 章：網路邊界防禦、DDoS 防護與微隔離架構",
            "title": "SASE（安全存取服務邊緣）與 SSE 架構在證券商跨分公司及遠端維運之落地實踐",
            "summary": "深入剖析 Gartner SASE 與 SSE 架構、ZTNA 零信任網路存取、SWG 安全 Web 閘道、CASB 雲端存取代理，以及取代傳統集中式 VPN 瓶頸之金融遠距合規維運實踐。",
            "points": 25,
            "rubric": "1. 集中式 VPN 缺陷與 SASE/SSE 架構理念 (7分)；2. ZTNA/SWG/CASB 核心機制與關鍵對比 (7分)；3. 證券跨分公司落地實務與參數 (7分)；4. 結論 (4分)",
            "question": "傳統金融企業依賴集中式 VPN 將所有跨分公司與遠距辦公流量導回總部資料中心檢測，導致頻寬瓶頸、延遲劇增且存在單點突破全網通訊之高風險。請說明 Gartner SASE（安全存取服務邊緣）與 SSE（安全服務邊緣）之核心架構；剖析 ZTNA（零信任網路存取）、SWG（安全 Web 閘道）與 CASB（雲端存取安全代理）之分工機制；並為臺灣證券期貨業規劃一套兼顧低延遲行情交易與合規加密通道之 SASE 現代化遠端維運落地架構。",
            "modelAnswer": """
<h4>一、破題：傳統集中式 VPN 致命瓶頸與 SASE/SSE 典範轉移</h4>
<p>傳統金融機構多採用「軸輻式（Hub-and-Spoke）」網路拓撲，所有跨分公司辦公室及居家遠距員工，皆透過 IPSec/SSL VPN 將流量強制「髮夾彎（Hairpinning）」回傳總部資料中心集中進行防火牆檢查。此架構在雲原生時代面臨三大致命瓶頸：</p>
<ol>
  <li><strong>頻寬回流壅塞與單點延遲</strong>：證券行情與雲端服務（SaaS）暴增，總部對外頻寬被塞爆，引發即時報價延遲，嚴重影響下單交易。</li>
  <li><strong>周邊信任隱患（城堡護城河缺陷）</strong>：VPN 僅驗證入口身分，一旦遠距端點遭惡意木馬滲透，攻擊者取得內網 IP 後即可無限制橫向滲透（Lateral Movement）。</li>
  <li><strong>SASE 與 SSE 核心理念</strong>：Gartner 提出 <strong>SASE（Secure Access Service Edge）</strong>，將 SD-WAN（廣域網功能）與 <strong>SSE（Security Service Edge，安全服務邊緣）</strong>融合，直接於全球邊緣節點（PoP）就近實施安全防護，實現「就近接入、邊緣檢查、零信任存取」。</li>
</ol>

<h4>二、SSE 三大核心安全組件機制對比</h4>
<ul>
  <li><strong>ZTNA (零信任網路存取)</strong>：基於身分與設備健康度之 應用程式級微隧道 ，隱匿底層內網拓撲（SPA 單封包授權）；<strong>存取標的</strong>：私有雲/地端核心系統；維運工程師遠端存取交易所撮合主機跳板機、帳務資料庫。</li>
  <li><strong>SWG (安全 Web 閘道)</strong>：全流量 TLS 1.3 深度封包檢測、惡意 URL 過濾、DNS 安全防護與檔案防毒沙盒；<strong>存取標的</strong>：公開網際網路 (Web)；分公司營業員瀏覽外部財經網站，防止惡意掛馬與水坑攻擊（Watering Hole）。</li>
  <li><strong>CASB (雲端存取安全代理)</strong>：API 與反向代理雙模治理、雲端影子 IT（Shadow IT）盤點、機敏資料外洩防護（DLP）；<strong>存取標的</strong>：公有雲 SaaS (M365, Salesforce)；管控員工將客戶交易名冊上傳未授權之外部雲端硬碟（Google Drive/Dropbox）。</li>
</ul>

<h4>三、證券期貨業 SASE 落地架構規劃</h4>
<ol>
  <li><strong>流量分流架構（SD-WAN Dynamic Steering）</strong>：
    - <strong>極致低延遲交易通道</strong>：券商撮合下單與行情 Multicast 仍走板橋機房固網專線（Leased Line），不經由網際網路 SASE；<br>
    - <strong>OA 與遠距維運通道</strong>：分公司辦公室及外部端點部署 SASE Client，就近連線至本地電信 PoP 邊緣節點，透過加密 WireGuard/TLS 隧道直接存取。
  </li>
  <li><strong>ZTNA 連線防護與單封包授權（SPA）</strong>：
    - 透過 <strong>Single Packet Authorization (SPA)</strong>，交易所受保護跳板機在公網上處於預設丟棄（Drop-All）之「隱形黑洞」狀態；<br>
    - 端點發送經非對稱加密與時間戳簽章之單一 UDP 敲門封包，邊緣閘道解密驗證通過後方動態開啟防火牆端口（例如僅允許 30 秒連線），杜絕連接埠掃描。
  </li>
  <li><strong>端點合規持續評估（Continuous Posture Checking）</strong>：
    連線期間 SASE Agent 持續監控端點作業系統補丁、EDR 代理運行狀態與硬體 TPM 晶片。一旦偵測到端點防毒遭停用或遭勒索程式特徵觸發，0.5 秒內即時切斷 ZTNA 連線並撤回憑證。
</li>
</ol>

<h4>四、結論</h4>
<p>導入 SASE/SSE 架構不僅徹底根除了傳統 VPN 髮夾彎流量導致之頻寬吞吐瓶頸，更將安全邊界由實體資料中心前移至終端使用者與雲端邊緣，為臺灣證券市場打造具備彈性、高可用且合規的現代化無邊界零信任防線。</p>
            """,
            "examinerTips": "評分關鍵字：『VPN 髮夾彎 (Hairpinning) 頻寬瓶頸與橫向移動隱患』、『SASE = SD-WAN + SSE』、『SSE 鐵三角：ZTNA (應用隱匿)、SWG (Web過濾)、CASB (SaaS DLP)』、『SPA 單封包授權預設黑洞』、『持續端點合規評估 (Continuous Posture Checking)』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>集中式 VPN 缺陷與 SASE 概念（7分）</strong>：深入點評 VPN 髮夾彎瓶頸與橫向滲透風險，精準定義 SASE 與 SSE 邊緣服務邊界的架構躍遷。</li>
  <li><strong>核心組件與重點對比（7分）</strong>：以標準三欄重點對比詳述 ZTNA、SWG、CASB 的工作原理、防護對象與證券金融應用場景。</li>
  <li><strong>證券業落地規劃（7分）</strong>：提出交易專線與 OA 流量分流架構、SPA 單封包授權隱形機制及動態端點合規持續驗證。</li>
  <li><strong>結論（4分）</strong>：論述無邊界資安對金融韌性之戰略意義。</li>
</ul>
            """
        },

        # 2. sec-essay-50: AD CS / ESC1-8 & ITDR
        {
            "id": "sec-essay-50",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "Active Directory 憑證服務（AD CS）範本漏洞攻擊（ESC1~ESC8）與 ITDR 身分威脅防護",
            "summary": "深入解構 Windows Active Directory 憑證服務（AD CS）架構、ESC1 使用者指定 SAN 與 ESC8 NTLM Relay 提權原理、黃金憑證（Golden Certificate）持久化，以及身分威脅偵測與回應（ITDR）實戰防禦。",
            "points": 25,
            "rubric": "1. AD CS 攻擊面成因與提權危害 (7分)；2. ESC1 與 ESC8 攻擊技術對比 (7分)；3. 金融 AD 縱深加固與 ITDR 部署 (7分)；4. 結論 (4分)",
            "question": "在金融機構內部網路與 Windows AD 網域架構中，Active Directory 憑證服務（AD CS）已成為 APT 組織獲取最高 Domain Admin 權限與持久化控制（Golden Certificate）的新興首選攻擊面。請說明 AD CS 憑證範本常見錯誤設定（如 ESC1 與 ESC8 NTLM Relay 攻擊）之原理與提權途徑；並詳述現代金融機構應如何透過身分威脅偵測與回應（ITDR）與最小權限治理，建構身分層次之主動縱深防禦體系？",
            "modelAnswer": """
<h4>一、破題：AD CS 憑證服務為何成為金融內網淪陷之重災區</h4>
<p>Windows Active Directory 憑證服務（AD CS）是企業內部公開金鑰基礎設施（PKI），負責發放電腦身分、使用者智慧卡登入與 S/MIME 憑證。由於早期網域管理員為圖作業便利，常建立過度寬鬆的<strong>憑證範本（Certificate Templates）</strong>，使得取得低權限網域帳號之攻擊者，能夠向憑證授權單位（CA）請求包含任意高權限使用者身分（如 Domain Admin）之數位憑證，進而直接以 Kerberos PKINIT 取得 Kerberos TGT，徹底瓦解網域安全邊界。</p>

<h4>二、經典 AD CS 弱點深度剖析：ESC1 vs ESC8</h4>
<ul>
  <li><strong>ESC1 (使用者指定主體別名)</strong>：<strong>錯誤組態本質 (Root Cause)</strong>：1. 範本啟用 Client Authentication 延伸金鑰用途； 2. 旗標勾選 CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT ； 3. 允許一般 Domain Users 擁有註冊權限 (Enroll)。；<strong>攻擊鏈與提權途徑</strong>：低權限使用者在請求中自行於 SAN (Subject Alternative Name) 填入 Administrator ，CA 簽發後，攻擊者持該憑證換取網域管理員 TGT。；取消「在要求中提供」主體名稱，改由 AD 屬性自動構建；移除低權限群組註冊權限；設定主管審核批准 (Manager Approval)。。</li>
  <li><strong>ESC8 (NTLM 中繼至 Web 註冊端點)</strong>：<strong>錯誤組態本質 (Root Cause)</strong>：AD CS 啟用 HTTP Web 註冊端點（ /certsrv ），且 未強制要求 EPA（擴充保護）與 HTTPS 憑證綁定 ，支援 NTLM 驗證。；<strong>攻擊鏈與提權途徑</strong>：攻擊者透過 PetitPotam 或印表機臭蟲強制網域控制站（DC$）發起 NTLM 認證，中繼至 /certsrv 申請 DC 電腦憑證，完成 DCSync 導出所有雜湊。；徹底停用 HTTP Web 註冊端點；若必須保留，強制啟用 HTTPS、EPA (Extended Protection for Authentication) 並停用 NTLM。。</li>
</ul>

<h4>三、防範黃金憑證（Golden Certificate）與 ITDR 身分威脅防護實務</h4>
<ol>
  <li><strong>黃金憑證防禦</strong>：
    一旦 CA 私鑰（CA Private Key）遭攻擊者透過 Mimikatz (<code>crypto::certificates</code>) 導出，攻擊者可在離線狀態下任意偽造有效期長達數十年的身分憑證。交易所必須強制將 CA 私鑰存儲於 <strong>FIPS 140-3 Level 3 硬體安全模組（HSM）</strong>，私鑰標記 Non-Exportable，杜絕記憶體竊取。
  </li>
  <li><strong>身分威脅偵測與回應（ITDR）核心能力</strong>：
    - <strong>靜態態勢盤點</strong>：定期執行 BloodHound / Certipy 自動化掃描，識別隱含的弱點憑證範本與 ACL 越權存取路徑；<br>
    - <strong>即時異常偵測</strong>：監控 DC 事件日誌 <code>Event ID 4886</code>（憑證申請）、<code>4887</code>（憑證簽發）及 <code>Event ID 4768</code>（Kerberos TGT 請求使用 PKINIT）。若發現機器帳號以非正常頻率或異常 SAN 申請管理員憑證，立即告警阻斷；<br>
    - <strong>自動化封鎖聯動</strong>：聯動 SOAR 自動停用受害帳號，並向 CA 下發憑證廢止清單（CRL / OCSP 即時吊銷）。
  </li>
  <li><strong>AD Tier 階層隔離架構</strong>：
    將 AD CS 伺服器嚴格歸類為 <strong>Tier 0 關鍵資產</strong>，禁止 Tier 1/Tier 2 管理員遠端登入，消除憑證橫向劫持風險。
</li>
</ol>

<h4>四、結論</h4>
<p>AD CS 是企業身分邊界的核心命脈。透過全面修補 ESC 脆弱範本、停用不安全 NTLM 中繼，並結合 ITDR 即時監控與 HSM 根金鑰保全，證券交易所方能徹底封死進階 APT 組織之身分提權通道。</p>
            """,
            "examinerTips": "亮點必得分項：『ESC1 核心條件：Client Auth + ENROLLEE_SUPPLIES_SUBJECT (自定義SAN) + 低權限Enroll』、『ESC8：PetitPotam 誘騙 DC 驗證 + NTLM Relay 至 /certsrv 換取 DC 憑證』、『黃金憑證 (Golden Certificate) 依賴 CA 私鑰，解方為 HSM Level 3』、『ITDR 監控 Event ID 4887 簽發與 Event ID 4768 PKINIT』、『AD CS 納入 Tier 0 嚴格管理』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>AD CS 威脅成因（7分）</strong>：清楚闡述過度寬鬆範本如何讓低權限帳號藉由 PKINIT 機制合法獲取 Domain Admin 憑證。</li>
  <li><strong>ESC1 與 ESC8 深入對比（7分）</strong>：以條列逐項列出觸發條件、攻擊路徑與具體修補措施（取消主體別名自訂、EPA/停用NTLM）。</li>
  <li><strong>黃金憑證與 ITDR（7分）</strong>：提出 HSM 私鑰防護、Certipy 弱點掃描、Windows 稽核日誌事件 ID 與 SOAR 自動化吊銷聯動。</li>
  <li><strong>結論（4分）</strong>：將 AD CS 納入 Tier 0 最小權限模型作結。</li>
</ul>
            """
        },

        # 3. sec-essay-51: Memory Forensics & Fileless Malware
        {
            "id": "sec-essay-51",
            "category": "sec",
            "chapter": "第 7 章：SOC 威脅監控、SIEM/SOAR、EDR 與事件應變",
            "title": "記憶體數位鑑識（Memory Forensics）與無檔案惡意程式（Fileless Malware）攻防實務",
            "summary": "深入解構無檔案攻擊（Process Hollowing, DLL 注入, LOLBins）、Volatility 3 記憶體轉儲分析、VAD 虛擬位址描述元樹結構檢視，以及端點 EDR 行為監控與記憶體完整性保護。",
            "points": 25,
            "rubric": "1. 無檔案惡意程式攻擊技術剖析 (7分)；2. Volatility 3 鑑識分析實務 (7分)；3. 記憶體防護加固 (HVCI/EDR) (7分)；4. 結論 (4分)",
            "question": "高階持續性威脅（APT）集團日益採用無檔案攻擊（Fileless Attacks）入侵金融關鍵系統，利用記憶體注入（Process Hollowing / Reflective DLL Injection）與合法系統工具（Living off the Land, LOLBins）執行惡意代碼，使得傳統端點防毒難以察覺。請分析常見無檔案攻擊之底層注入原理；詳述鑑識人員如何運用 Volatility 3 工具針對交易伺服器記憶體傾印檔（Memory Dump）進行 VAD 樹結構遍歷、隱藏行程獵捕與惡意代碼提取流程；並提出相應之端點偵測與防禦對策。",
            "modelAnswer": """
<h4>一、破題：無檔案惡意程式（Fileless Malware）核心注入機制</h4>
<p>傳統惡意程式依賴落地檔案（PE 檔案）執行，易被靜態特徵碼及檔案雜湊（SHA-256）偵測。現代進階攻擊者採用「無檔案技術」，將惡意代碼直接載入於記憶體執行：</p>
<ol>
  <li><strong>行程掏空（Process Hollowing）</strong>：
    攻擊者以掛起模式（<code>CREATE_SUSPENDED</code>）啟動合法系統行程（如 <code>svchost.exe</code>），調用 <code>NtUnmapViewOfSection</code> 卸載其原本代碼區段，再透過 <code>VirtualAllocEx</code> 分配記憶體並寫入惡意 Shellcode，最後修改執行緒上下文（<code>SetThreadContext</code>）之 EIP/RIP 暫存器並恢復執行（<code>ResumeThread</code>）。該行程在工作管理員中具備合法微軟簽名與路徑，極具欺騙性。
  </li>
  <li><strong>反射式 DLL 注入（Reflective DLL Injection）</strong>：
    不依賴 Windows 原生 <code>LoadLibrary()</code>，惡意 DLL 內部自建 PE 載入器，直接在目標行程記憶體中自主解析導出表、重定位位址與修復 IAT（匯入位址表），全程不觸碰磁碟、不產生登錄檔痕跡。
  </li>
  <li><strong>LOLBins 濫用（Living off the Land）</strong>：
    濫用系統白名單工具（如 <code>certutil.exe</code> 下載、<code>powershell.exe -enc</code> 記憶體解碼、<code>mshta.exe</code> 執行 VBScript），避開邊界偵測。
  </li>
</ol>

<h4>二、Volatility 3 記憶體鑑識實戰分析流程</h4>
<ul>
  <li><strong>1. 行程樹隱藏檢測</strong>：windows.pslist windows.psscan；比對雙向鏈結串列（ActiveProcessLinks）與未分配記憶體中的 EPROCESS 結構。若 psscan 發現某 PID 不存在於 pslist ，證明遭 DKOM 行程隱藏技術（Direct Kernel Object Manipulation）拔鏈。。</li>
  <li><strong>2. 記憶體區段代碼注入獵捕</strong>：windows.malfind windows.vadinfo；檢查 VAD（虛擬位址描述元）樹 ：過濾屬性為 PAGE_EXECUTE_READWRITE (PAGE_X_RW) 且無檔案對應（File-less, 無關聯磁碟路徑）之記憶體區段；檢查記憶體開頭是否出現 4D 5A (MZ) 魔術數字或 Shellcode 啟動特徵。。</li>
  <li><strong>3. 網路連線與注入代碼導出</strong>：windows.netscan windows.dumpfiles；關聯可疑行程之外部 C2 連線 IP 與連接埠；使用 --pid --dump 完整導出該記憶體區段，提交 YARA 規則與反組譯工具（Ghidra）進行靜態分析。。</li>
</ul>

<h4>三、端點防禦與記憶體完整性加固</h4>
<ol>
  <li><strong>基於虛擬化的安全（VBS）與核心完整性（HVCI）</strong>：
    啟用 Hyper-V 隔離的 Hypervisor-Protected Code Integrity（HVCI），在硬體層級強制實施「W^X（Write XOR Execute）」原則：<strong>記憶體區段不可同時具備可寫入與可執行屬性</strong>，即便攻擊者透過漏洞寫入 Shellcode，硬體層直接阻斷執行。
  </li>
  <li><strong>EDR 記憶體深層掃描（AMSI 與 API Hooking）</strong>：
    利用 AMSI（反惡意軟體掃描介面）在腳本執行即時解密後先行動態查驗；EDR 在用戶態注入 Hooking，監控 <code>VirtualAllocEx</code>、<code>WriteProcessMemory</code> 與 <code>CreateRemoteThread</code> 呼叫鏈，若偵測到非父子行程間的高危注入立即終止行程。
  </li>
  <li><strong>攻擊面縮小規則（ASR Rules）</strong>：
    強制啟用 Windows Defender ASR 規則，封鎖 Office 與 Adobe 生成子行程、封鎖 Win32 API 呼叫，壓制 LOLBins 武器化管道。
</li>
</ol>

<h4>四、結論</h4>
<p>無檔案攻擊打破了「以磁碟檔案為防護核心」之傳統防線。透過 Volatility 記憶體鑑識掌握 VAD 異常結構，並在作業系統端點啟用硬體輔助 HVCI 與行為 EDR 聯動，為證券交易伺服器築起堅不可摧的動態記憶體安全屏障。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『Process Hollowing (NtUnmapViewOfSection + SetThreadContext)』、『Reflective DLL 自建 PE Loader 繞過 LoadLibrary』、『Volatility 3: psscan 對比 pslist 揪出 DKOM 拔鏈行程』、『malfind 獵捕 VAD 樹中 PAGE_EXECUTE_READWRITE 且無檔案對應之區段』、『硬體防禦：VBS + HVCI 強制 W^X 原則』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>無檔案攻擊原理（7分）</strong>：深入解構 Process Hollowing 系統呼叫步驟、Reflective DLL 注入與 LOLBins 概念。</li>
  <li><strong>Volatility 3 鑑識實踐（7分）</strong>：以條列詳述 pslist/psscan 拔鏈檢測、malfind 與 VAD 樹 PAGE_X_RW 屬性篩選，以及 dumpfiles 提取分析。</li>
  <li><strong>防禦加固對策（7分）</strong>：提出 VBS/HVCI 記憶體隔離（W^X 限制）、AMSI 動態解碼攔截與 ASR 規則防護。</li>
  <li><strong>結論（4分）</strong>：總結端點記憶體主動防禦戰略。</li>
</ul>
            """
        },

        # 4. sec-essay-52: MITRE ATT&CK & Threat Intelligence
        {
            "id": "sec-essay-52",
            "category": "sec",
            "chapter": "第 10 章：紅藍對抗、滲透測試與漏洞弱點管理",
            "title": "MITRE ATT&CK 框架於金融威脅情資映射（TTPs Mapping）與防禦覆蓋率評估實務",
            "summary": "深入解構 MITRE ATT&CK Enterprise 戰術與技術架構、FIN7/Lazarus 金融 APT 攻擊鏈映射、ATT&CK Navigator 防禦熱力圖繪製，以及 SOC 偵測規則差距分析（Gap Analysis）與情資驅動紫隊閉環。",
            "points": 25,
            "rubric": "1. ATT&CK 框架結構與相較傳統 IoC 之優勢 (7分)；2. 金融 APT 攻擊鏈 TTPs 映射分析 (7分)；3. ATT&CK Navigator 覆蓋率評估與紫隊閉環 (7分)；4. 結論 (4分)",
            "question": "國際資安實戰評估已全面由傳統漏洞清單轉向「戰術、技術與程序（TTPs）」。請說明 MITRE ATT&CK 企業矩陣（Enterprise Matrix）核心結構（Tactics、Techniques、Sub-techniques）；針對國際針對金融業之知名 APT 集團（如 FIN7 或 Lazarus）之典型攻擊鏈進行 ATT&CK 映射分析；並闡述臺灣證券交易所如何運用 ATT&CK Navigator 評估 SOC 與 EDR 偵測規則之防禦覆蓋率（Coverage Gap Analysis），打造情資驅動之紫隊防禦閉環？",
            "modelAnswer": """
<h4>一、破題：MITRE ATT&CK 框架核心架構與「痛苦之金字塔」</h4>
<p>在資安威脅防禦中，David Bianco 提出的<strong>痛苦之金字塔（Pyramid of Pain）</strong>指出：封鎖雜湊值（Hash）、IP 位址或網域名稱對攻擊者造成的困擾極低（輕易變更即可繞過）；而唯有防禦<strong>戰術、技術與程序（TTPs）</strong>，才能迫使攻擊者重新研發攻擊工具，造成其最大痛苦與成本。<strong>MITRE ATT&CK</strong> 即是全球公認將攻擊者行為標準化之知識庫：</p>
<ol>
  <li><strong>戰術（Tactics，Why/目標）</strong>：代表攻擊者的戰略目標，涵蓋 Reconnaissance、Initial Access、Execution、Persistence、Privilege Escalation、Defense Evasion、Credential Access、Discovery、Lateral Movement、Collection、Command and Control、Exfiltration 與 Impact 共 14 項戰術。</li>
  <li><strong>技術與子技術（Techniques / Sub-techniques，How/手段）</strong>：具體執行目標的方法（例如 T1059 Command and Scripting Interpreter，下設 T1059.001 PowerShell）。</li>
  <li><strong>程序（Procedures，Implementation/實例）</strong>：特定威脅組織在現實攻擊中調用該技術的具體代碼或工具實作方式。</li>
</ol>

<h4>二、金融 APT 集團攻擊鏈 TTPs 映射矩陣（以 FIN7 / Lazarus 為例）</h4>
<ul>
  <li><strong>1. 初始存取</strong>：<strong>ATT&CK 戰術與技術編號</strong>：TA0001: T1566.001 (Spearphishing Attachment)；<strong>金融黑客實戰行為 (Procedures)</strong>：寄發偽冒金管會公文之惡意 Word 巨集或 LNK 快捷方式檔案；<strong>證交所防禦檢測指標</strong>：郵件閘道沙盒動態解構巨集；停用 Office 巨集自動執行。</li>
  <li><strong>2. 憑證存取</strong>：<strong>ATT&CK 戰術與技術編號</strong>：TA0006: T1003.001 (OS Credential Dumping: LSASS)；<strong>金融黑客實戰行為 (Procedures)</strong>：利用 Mimikatz 或 Comsvcs.dll 迷你轉儲 lsass.exe 記憶體明文密碼與 NTLM 雜湊；<strong>證交所防禦檢測指標</strong>：啟用 Windows LSA Protection (RunAsPPL)；禁止未授權存取 LSASS 行程。</li>
  <li><strong>3. 橫向移動</strong>：<strong>ATT&CK 戰術與技術編號</strong>：TA0008: T1021.002 (SMB/Windows Admin Shares)；<strong>金融黑客實戰行為 (Procedures)</strong>：透過 PsExec 或 WMI/WinRM 橫向擴散至內部行情伺服器與資料庫；<strong>證交所防禦檢測指標</strong>：網路微隔離阻斷端點間 445/135 通訊；封鎖端點互訪。</li>
  <li><strong>4. 命令與控制</strong>：<strong>ATT&CK 戰術與技術編號</strong>：TA0011: T1071.001 (Web Protocols)；<strong>金融黑客實戰行為 (Procedures)</strong>：利用 HTTPS 搭配偽冒憑證與 Fast Flux 域名建立反向 C2 隧道；<strong>證交所防禦檢測指標</strong>：對接 F-ISAC 惡意 IoC；NDR 分析 TLS JA4 指紋與心跳連線。</li>
</ul>

<h4>三、運用 ATT&CK Navigator 評估防禦覆蓋率與紫隊閉環實踐</h4>
<ol>
  <li><strong>繪製 ATT&CK Navigator 熱力圖（Heatmap）</strong>：
    - 將現有 SOC 告警規則、EDR 阻斷策略與邊界防火牆能力匯入 Navigator 圖層；<br>
    - 依防禦能力評分填色：<strong>綠色（具備即時自動阻斷能力）</strong>、<strong>黃色（具備日誌檢測告警能力）</strong>、<strong>紅色（完全無可視性盲點，Gap）</strong>。
  </li>
  <li><strong>威脅情資驅動之差距分析（Gap Analysis）</strong>：
    針對 F-ISAC 發布之最新金融威脅情報，篩選出攻擊者高頻調用之技術清單，與現有 Navigator 綠色覆蓋率進行疊加比對，立即精確定位出監控盲區（例如缺乏對 T1558 Kerberoasting 或 T1053 排程任務之監控）。
  </li>
  <li><strong>情資驅動紫隊協同閉環（Purple Teaming Cycle）</strong>：
    - <strong>紅隊模擬（Attack Simulation）</strong>：使用開源攻擊模擬工具（如 Atomic Red Team 或 Caldera），針對盲區技術自動發起安全測試載荷；<br>
    - <strong>藍隊校準（Detection Engineering）</strong>：SOC 與 SIEM 工程師調校 Sigma 規則與 EDR 偵測邏輯，確保每次測試皆能觸發有效告警；<br>
    - <strong>自動回歸驗證</strong>：將成功偵測之規則寫入 CI/CD 自動化防禦回歸測試，使防禦能力持續進化。
</li>
</ol>

<h4>四、結論</h4>
<p>透過 MITRE ATT&CK 框架，證券交易所將傳統被動的「依賴黑名單圍堵」全面昇華為「以攻擊者行為畫像為主導」的矩陣式主動防禦，打造可量化、可驗證、持續進化的金融資安防護基石。</p>
            """,
            "examinerTips": "必得分關鍵詞：『痛苦之金字塔 (Pyramid of Pain)：TTPs 位於最高頂端』、『ATT&CK 結構：14 Tactics (目標) -> Techniques (手段) -> Procedures (實例)』、『金融典型攻擊鏈：T1566 魚叉釣魚 -> T1003 LSASS 憑證導出 -> T1021 SMB 橫向移動』、『ATT&CK Navigator 綠黃紅防禦熱力圖與 Gap Analysis』、『Atomic Red Team / Caldera 紫隊自動化驗證閉環』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>ATT&CK 框架理念（7分）</strong>：引用痛苦之金字塔解釋 TTPs 的高價值防禦意義，清晰區分戰術、技術與程序三層級。</li>
  <li><strong>金融 APT 實戰映射表（7分）</strong>：以標準條列架構列舉 Initial Access、LSASS Dumping、橫向移動與 C2 的 ATT&CK 編號與金融具體實施手法。</li>
  <li><strong>Navigator 差距評估與紫隊閉環（7分）</strong>：提出熱力圖著色量化、F-ISAC 情資比對、Atomic Red Team 實兵驗證與 Sigma 規則調校工程。</li>
  <li><strong>結論（4分）</strong>：總結行為主導與持續防禦驗證價值。</li>
</ul>
            """
        },

        # 5. sec-essay-53: VEX, EPSS, KEV
        {
            "id": "sec-essay-53",
            "category": "sec",
            "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
            "title": "軟體供應鏈安全進階：VEX（弱點可利用性交換）與 EPSS/KEV 漏洞精準修補優先級模型",
            "summary": "深入解構軟體物料清單（SBOM）告警疲勞、VEX（OpenVEX / CSAF）弱點狀態聲明、FIRST EPSS 漏洞利用預測評分、CISA KEV 已知利用目錄，以及證券系統自動化排程修補決策矩陣。",
            "points": 25,
            "rubric": "1. SBOM 告警氾濫成因與 VEX 概念 (7分)；2. EPSS 與 KEV 核心評估原理 (7分)；3. 金融漏洞排程優先級決策矩陣 (7分)；4. 結論 (4分)",
            "question": "金融機構導入軟體物料清單（SBOM）後常面臨「告警疲勞（Alert Fatigue）」難題：掃描出數千個開源相依性 CVE，但多數在實際編譯或執行路徑中根本未被呼叫（Not Reachable）。請說明弱點可利用性交換協定（VEX，如 OpenVEX / CSAF）如何解決 SBOM 偽陽性問題；分析 FIRST 漏洞可利用性預測評分系統（EPSS）與 CISA 已知被利用漏洞目錄（KEV）之評估原理；並為證券資訊系統設計一套結合 CVSS、EPSS 與 VEX 之漏洞優先級（Prioritization）自動化排程修補決策流程。",
            "modelAnswer": """
<h4>一、破題：SBOM 告警疲勞困境與 VEX 核心理念</h4>
<p>金管會要求金融機構落實開源軟體物料清單（SBOM）盤點。然而，傳統 SCA（軟體成分分析）工具僅依賴相依庫套件版本進行字串匹配，產生大量虛假告警。實務上高達 80% 以上包含已知 CVE 的開源組件，因其具體漏洞代碼未被主程式導入、或處於死代碼（Dead Code）、或受外部架構控制項防護，根本<strong>無法被利用（Not Reachable / Not Exploitable）</strong>，引發工程師嚴重的「告警疲勞」。</p>
<p>為此，CISA 推動 <strong>VEX（Vulnerability Exploitability eXchange，弱點可利用性交換協定）</strong>，作為 SBOM 的動態安全修飾伴侶文件（格式包含 OpenVEX 與 OASIS CSAF 2.0）。VEX 明確定義軟體廠商對每個 CVE 在特定產品環境下的真實狀態：</p>
<ol>
  <li><code>not_affected</code>（未受影響）：軟體雖包含該相依套件，但因代碼不可達（code_not_reachable）或已有補償控制（inline_mitigations_already_exist），無法被觸發利用。</li>
  <li><code>affected</code>（受影響）：已確認受漏洞威脅，需採取行動。</li>
  <li><code>fixed</code>（已修復）：已透過版本升級或代碼修改修復完成。</li>
  <li><code>under_investigation</code>（調查中）：尚在進行可利用性分析。</li>
</ol>

<h4>二、漏洞威脅評估三劍客深度對比：CVSS vs EPSS vs KEV</h4>
<ul>
  <li><strong>CVSS v3.1 / v4.0</strong>：NIST / FIRST：評估漏洞的 技術嚴重度與潛在破壞力 (Severity)；<strong>數值輸出與更新時效</strong>：0.0 ~ 10.0 分（靜態評分，發布後鮮少大幅變動）；<strong>金融修補排程定位</strong>：衡量「如果被利用，損害有多嚴重？」。</li>
  <li><strong>EPSS (利用預測評分)</strong>：FIRST：利用機器學習預測 未來 30 天內野生環境遭到利用之機率 (Probability)；<strong>數值輸出與更新時效</strong>：0% ~ 100%（每日根據全網攻擊情報動態重新計算）；<strong>金融修補排程定位</strong>：衡量「近期被黑客武器化發起攻擊之可能性有多高？」。</li>
  <li><strong>CISA KEV 目錄</strong>：美國 CISA：官方已證實 在野外已遭真實攻擊利用之漏洞清單 (Active Exploitation)；<strong>數值輸出與更新時效</strong>：二元屬性（Yes / No，已確認正遭黑客實戰利用）；<strong>金融修補排程定位</strong>：最高警戒！屬已遭攻擊之確定事實，必須最優先無條件修補！。</li>
</ul>

<h4>三、證券核心系統漏洞自動化優先級排程決策流程</h4>
<pre><code class="language-text">SCA 掃描出 CVE 弱點
       │
       ▼
[步驟 1: VEX 狀態過濾] ──(VEX 標記 not_affected 且理由為代碼不可達) ──> 產生合規稽核日誌，免於修補
       │
       ▼ (VEX 標記 affected 或缺少 VEX 聲明)
[步驟 2: CISA KEV 比對] ──(命中 KEV 目錄) ──────────────────────────> 【P0 致命最高等級】48小時內完成熱補丁
       │ (未列入 KEV)
       ▼
[步驟 3: EPSS 機率與 CVSS 嚴重度二維決策矩陣]
       │
       ├─> EPSS > 30% 且 CVSS ≥ 7.0 (高風險且高度即將被利用) ────────> 【P1 緊急等級】7天內完成修復驗證
       ├─> EPSS ≤ 30% 但 CVSS ≥ 9.0 (超高破壞力但暫無野外利用) ──────> 【P2 一般等級】30天內隨維護窗口發布
       └─> EPSS < 5% 且 CVSS < 7.0 (低危且幾乎無利用可能) ───────────> 【P3 低等級】例行季度維護或接受風險</code></pre>
<ol>
  <li><strong>第一道篩檢（可達性分析）</strong>：結合代碼呼叫圖（Call Graph）分析與供應商 VEX 文件，過濾非必要修復項目，減少 70% 無效工作量。</li>
  <li><strong>第二道篩檢（威脅情報動態注入）</strong>：每日自動同步 CISA KEV 與 FIRST EPSS API。凡列入 KEV 者，即使 CVSS 僅為中度（Medium），亦自動調升為 P0 級緊急處理，防止駭客以低分漏洞達成鏈式組合利用。</li>
</ol>

<h4>四、結論</h4>
<p>從「單一 CVSS 嚴重度」演進至「VEX 可達性 + EPSS 攻擊預測 + KEV 實戰情資」三維決策模型，證券交易所能將寶貴的資安工程資源精準投注於真正具備實質威脅的漏洞上，徹底告別告警疲勞，打造高效能的軟體供應鏈治理體系。</p>
            """,
            "examinerTips": "核心破題得分點：『SBOM 告警疲勞痛點：80% 漏洞處於代碼不可達 (Not Reachable)』、『VEX 四大狀態：not_affected、affected、fixed、under_investigation』、『CVSS (技術嚴重度) vs EPSS (30天利用機率) vs KEV (在野已遭利用事實)』、『P0~P3 自動化決策矩陣流程圖』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>SBOM 疲勞與 VEX 理念（7分）</strong>：深入分析 SCA 靜態匹配缺陷，詳細說明 VEX 規範（OpenVEX/CSAF）與四大狀態標記。</li>
  <li><strong>評估指標三維對比（7分）</strong>：以條列詳盡對比 CVSS 嚴重度、EPSS 預測機率與 KEV 現實事實的維度差異。</li>
  <li><strong>自動化排程決策模型（7分）</strong>：繪出清晰決策邏輯流程圖，針對 KEV、EPSS、CVSS 設定具體優先級（P0~P3）與修補時限標準。</li>
  <li><strong>結論（4分）</strong>：總結由粗放式修補轉向情資驅動精準修補之成效。</li>
</ul>
            """
        },

        # 6. sec-essay-54: WAAP & Bot Management
        {
            "id": "sec-essay-54",
            "category": "sec",
            "chapter": "第 6 章：網路邊界防禦、DDoS 防護與微隔離架構",
            "title": "WAAP（Web 應用與 API 保護）與進階機器人管理（Bot Management）抗惡意刷單實踐",
            "summary": "深入剖析下一代 WAAP 平台演進、傳統 WAF 盲點、高級機器人指紋技術（TLS JA4, Canvas, WebGL）、行為生物特徵分析，以及證券下單防黃牛搶單與防撞庫架構實務。",
            "points": 25,
            "rubric": "1. WAAP 四合一架構與傳統 WAF 侷限 (7分)；2. 機器人檢測三層技術對比 (7分)；3. 證券高頻防刷單與 PoW 落地實作 (7分)；4. 結論 (4分)",
            "question": "傳統 WAF 難以應對偽裝為合法瀏覽器之自動化機器人（Automated Bots）進行高頻搶單、黃牛刷單或暴力撞庫。請說明 Gartner 定義之「Web 應用程式與 API 保護（WAAP）」架構演進特點；分析進階機器人管理（Bot Management）如何結合客戶端設備指紋（Canvas / WebGL / TLS JA4 指紋）、使用者行為生物特徵（滑鼠移動/按鍵間隔模型）與動態工作量證明（Proof-of-Work, PoW）區分真偽流量；並規劃證券下單入口之防刷單架構。",
            "modelAnswer": """
<h4>一、破題：傳統 WAF 之死與 WAAP 四合一新典範</h4>
<p>傳統 WAF 依賴基於正則表達式（Regex）的靜態特徵碼，專注防範 SQL 注入與 XSS 等已知 Web 漏洞。但在開放證券與行動下單時代，攻擊者往往使用真實瀏覽器核心（如 Puppeteer、Playwright、Headless Chrome）發起「語法完全合法，但頻率異常或目的惡意」的業務邏輯攻擊（如開盤前暴力撞庫、新股競價高頻刷單、API 爬取市場深度行情）。</p>
<p>Gartner 定義 <strong>WAAP（Web Application and API Protection）</strong>，將邊界防護整合為四大核心支柱：</p>
<ol>
  <li><strong>新一代 WAF（Next-Gen WAF）</strong>：基於語意分析（Semantic Analysis）與異常評分，消除傳統正則規則維護困難與高誤報率。</li>
  <li><strong>API 安全防護（API Security）</strong>：自動探索影子 API、校驗 OpenAPI/Swagger 契約合規、防範 BOLA 授權缺失。</li>
  <li><strong>DDoS 彈性緩解（DDoS Mitigation）</strong>：L3/L4 泛洪清洗結合 L7 應用層防護。</li>
  <li><strong>進階機器人防禦（Advanced Bot Management）</strong>：精準識別並動態治理各類惡意自動化腳本。</li>
</ol>

<h4>二、進階機器人管理（Bot Management）三層檢測技術</h4>
<ul>
  <li><strong>【底層核心技術】</strong>：<strong>1. 協議層指紋 (Protocol Fingerprint)</strong>：TLS JA4 指紋 HTTP/2 標頭順序指紋；<strong>2. 設備環境指紋 (Client Fingerprint)</strong>：Canvas / WebGL 渲染 音訊 AudioContext 指紋；<strong>3. 行為生物特徵 (Behavioral Biometrics)</strong>：滑鼠軌跡曲率分析 鍵盤輸入間隔分佈 (Keystroke)。</li>
  <li><strong>【防禦偵測原理】</strong>：<strong>1. 協議層指紋 (Protocol Fingerprint)</strong>：TLS 握手 Client Hello 包含加密套件、延伸項排序等微特徵。Python Requests、Go net/http 與原生 Chrome 的 JA4 指紋截然不同，即便更換 User-Agent 亦無所遁形。；<strong>2. 設備環境指紋 (Client Fingerprint)</strong>：指令前端靜默繪製特定幾何圖形與著色器文字，利用不同 GPU 驅動與反鋸齒演算法產生的奈米級雜湊差異，唯一標識單一實體設備，杜絕設備模擬器批量刷單。；<strong>3. 行為生物特徵 (Behavioral Biometrics)</strong>：真人滑鼠移動呈現非線性加速度、顫抖與貝茲曲線；自動化腳本呈瞬間平移或嚴格直線；利用統計模型計算夏儂熵（Entropy）識別機械行為。。</li>
  <li><strong>【繞過難度與優勢】</strong>：<strong>1. 協議層指紋 (Protocol Fingerprint)</strong>：高：底層網路庫特徵極難在腳本層隨意竄改。；<strong>2. 設備環境指紋 (Client Fingerprint)</strong>：極高：跨 IP、清空 Cookie 仍能精準釘住該實體設備。；<strong>3. 行為生物特徵 (Behavioral Biometrics)</strong>：極致：模擬人類隨機抖動計算開銷極大，大幅抬高黑客攻擊成本。。</li>
</ul>

<h4>三、證券下單入口抗惡意刷單實戰防禦架構</h4>
<ol>
  <li><strong>無感驗證與動態工作量證明（Proof-of-Work, PoW）</strong>：
    傳統圖形驗證碼（CAPTCHA）嚴重損害合法投資人下單體驗且易被 OCR/AI 打破。現代 WAAP 採用<strong>無感 PoW 挑戰</strong>：伺服器向可疑客戶端派發 SHA-256 難度哈希難題，要求瀏覽器後台耗費 50~100ms CPU 算力求解。對一般單筆下單用戶毫無影響，但對每秒發送數萬筆的刷單黑客，其農場伺服器 CPU 將瞬間被打爆癱瘓。
  </li>
  <li><strong>金流與委託流量動態限速（Adaptive Rate Limiting）</strong>：
    針對證券下單 API（<code>/api/v1/order</code>），基於「用戶 Token + JA4 指紋 + 設備 ID」多維複合鍵實施滑動窗口（Sliding Window）限速，例如單一設備每秒最多 5 筆委託，超出者直接返回 HTTP 429 並降級處理。
  </li>
  <li><strong>行為威脅蜜罐（Tarpit / Delay Defense）</strong>：
    對判定為低速探測爬蟲之流量，不直接斷開連線以防被黑客察覺規則，而是刻意以 100 bytes/sec 之極慢速度回應（Tarpit），耗盡黑客伺服器連線池資源。
</li>
</ol>

<h4>四、結論</h4>
<p>在面對高度工程化、武器化的現代機器人威脅時，證券交易邊界必須由被動的「規則攔截」全面邁向「WAAP 縱深感知與進階 Bot 動態對抗」，藉由抬高攻擊者算力代價，確保交易系統資源絕對公平地服務於全體投資人。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『WAAP 四大支柱：新一代WAF、API安全、DDoS緩解、Bot進階管理』、『傳統WAF無法防範業務邏輯攻擊 (撞庫/搶單)』、『三層Bot檢測：TLS JA4 指紋、Canvas/WebGL GPU 渲染雜湊、滑鼠軌跡曲率生物特徵』、『無感 PoW (Proof of Work) 算力燃燒防禦』、『Tarpit 延遲拖延防禦』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>傳統 WAF 缺陷與 WAAP 演進（7分）</strong>：深入辨析業務邏輯攻擊成因，清楚定義 WAAP 四大組成模組。</li>
  <li><strong>機器人三層檢測技術（7分）</strong>：以條列逐項剖析協議層（TLS JA4）、設備指紋（Canvas/WebGL）與行為生物特徵（滑鼠熵值）的技術底層。</li>
  <li><strong>證券下單防刷單實作（7分）</strong>：提出無感 PoW 算力反制、多維動態限速與 Tarpit 資源耗盡戰術。</li>
  <li><strong>結論（4分）</strong>：總結提高黑客攻擊成本之核心防禦思維。</li>
</ul>
            """
        },

        # 7. sec-essay-55: Immutable Backup, Air-Gapped Vault, Clean Room
        {
            "id": "sec-essay-55",
            "category": "sec",
            "chapter": "第 11 章：業務連續性計畫（BCP）與防勒索軟體防禦",
            "title": "金融抗勒索關鍵技術：不可變備份（Immutable Backup）、實體隔離金庫（Air-Gapped Vault）與 Clean Room 無毒復原實務",
            "summary": "深入解構現代雙重/三重勒索軟體破壞備份策略、WORM 合規時限鎖、Air-Gapped 隔離金庫單向同步、乾淨隔離室（Clean Room）沙盒鑑識，以及金融關鍵系統無毒重建 SOP。",
            "points": 25,
            "rubric": "1. 勒索軟體攻擊備份手段與不可變存儲 (7分)；2. Air-Gapped 金庫架構與關鍵對比 (7分)；3. Clean Room 無毒復原 SOP (7分)；4. 結論 (4分)",
            "question": "近年勒索軟體集團專注於摧毀企業備份以迫使受害者支付贖金。請說明儲存層「一次寫入多次讀取（WORM）」合規時限鎖與物件鎖定（Object Lock）之不可變儲存原理；規劃一套符合金融等級之「網路實體隔離金庫（Air-Gapped Cyber Recovery Vault）」架構，說明資料單向同步與金庫連線隔離控制；並詳述在「無毒乾淨隔離室（Clean Room）」中執行備份鑑識掃描與自動化沙盒復原驗證之標準作業流程（SOP）。",
            "modelAnswer": """
<h4>一、破題：勒索軟體對備份系統之針對性打擊與不可變儲存</h4>
<p>現代勒索軟體（如 LockBit、BlackCat）的作戰手冊中，滲透首要目標即為尋找備份管理主機（如 Veeam、Commvault、備份儲存 NAS），利用竊取之 Domain Admin 憑證刪除磁碟快照（Volume Shadow Copies）、排空磁帶資料庫、強制加密備份儲存槽，令受害機構在災難發生時「無底可退」。</p>
<p>為此，金融架構必須在儲存硬體層引入<strong>不可變備份（Immutable Backup）</strong>：</p>
<ol>
  <li><strong>WORM（Write Once, Read Many）合規鎖定</strong>：
    儲存系統底層啟用 <code>Compliance Mode</code>，資料一旦寫入封裝，在設定之法定保留期內（如 30 天或 7 年），<strong>即便具備作業系統最高 root 或儲存設備 admin 權限，亦絕對無法修改、覆寫或提前刪除</strong>。
  </li>
  <li><strong>S3 Object Lock（物件鎖定）</strong>：
    在雲端或分散式物件儲存中，利用 <code>Retention Period</code> 搭配 <code>Legal Hold</code>，底層以雜湊鏈防止版本刪除，徹底杜絕勒索軟體的強制抹除攻擊。
</li>
</ol>

<h4>二、實體隔離金庫（Air-Gapped Cyber Recovery Vault）架構</h4>
<ul>
  <li><strong>【傳統異地備份中心 (DR Site)】</strong>：<strong>網路連線狀態</strong>：7x24 常態在線 (Online)，透過專線即時同步；<strong>連線控制機制</strong>：固定雙向通道，防火牆常態放行；<strong>管理面憑證隔離</strong>：常與總部共用 AD 網域憑證 (單點淪陷全盤皆輸)；<strong>資料檢驗機制</strong>：僅檢查檔案大小與傳輸完整性。</li>
  <li><strong>【金融級實體隔離金庫 (Air-Gapped Vault)】</strong>：<strong>網路連線狀態</strong>：預設離線（Air-Gapped），物理/邏輯完全斷網；<strong>連線控制機制</strong>：僅由金庫內部單向發起連線 ；每日僅在指定同步時間開啟連線，同步完成立即斷開；<strong>管理面憑證隔離</strong>：獨立全新身分庫 ；實體多因子硬體金鑰認證，禁止任何外部遠端連入；<strong>資料檢驗機制</strong>：金庫內建獨立 AI 分析引擎，主動掃描資料熵值與加密可疑性。</li>
</ul>

<h4>三、無毒乾淨隔離室（Clean Room）復原標準作業流程（SOP）</h4>
<p>當生產環境遭勒索軟體大面積破壞時，絕不可直接將備份還原至原主機，以防殘留之後門或休眠勒索病毒二次引爆。必須在<strong>Clean Room 隔離環境</strong>中進行淨化復原：</p>
<pre><code class="language-text">[金庫不可變備份] ──(唯讀掛載)──> [Clean Room 隔離沙盒] ──> [自動化鑑識檢測] ──> [無毒判定] ──> [產線重建]
                                                         ├── EDR 離線特徵掃描
                                                         ├── 檔案副檔名/熵值分析
                                                         └── 虛擬機啟動行為觀測</code></pre>
<ol>
  <li><strong>步驟 1：唯讀掛載（Read-Only Mount）</strong>：
    自金庫儲存中以唯讀快照方式掛載資料庫與虛擬機映像檔，保證原始備份永不受二次污染。
  </li>
  <li><strong>步驟 2：深層鑑識淨化掃描（Forensic Sanitation）</strong>：
    在無網際網路連線之隔離虛擬網路內啟動 VM：<br>
    - <strong>熵值（Entropy）檢測</strong>：計算檔案資料隨機度，若偵測到檔案大量呈現高熵（高於 7.8），判定為已加密損壞；<br>
    - <strong>離線 IOC/YARA 掃描</strong>：調用最新威脅特徵庫，掃描開機磁區（MBR/VBR）、註冊表 Run 鍵與排程任務；<br>
    - <strong>動態觀測（Sandbox Detonation）</strong>：將系統時鐘向前撥快 30 天，觸發潛伏的定時炸彈型惡意腳本，觀察是否有異常加密行為。
  </li>
  <li><strong>步驟 3：修補加固與受控上線</strong>：
    在 Clean Room 內將系統核心、中介軟體修補至最新安全補丁，更換所有管理員密碼與憑證，確認無毒後再以單向數據通道轉移至全新構建的生產伺服器。
</li>
</ol>

<h4>四、結論</h4>
<p>面對日益猖獗之勒索軟體威脅，「不可變儲存」提供了數學與儲存硬體層級的防破壞保證，「隔離金庫」杜絕了網路橫向污染，而「Clean Room」則保障了復原數據的絕對純淨，三者共同構築臺灣證券期貨業最後一道不可動搖的數據生還底線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『WORM (Compliance Mode) 硬體合規時限鎖，root 亦無法刪除』、『Air-Gapped Vault 預設斷網，僅金庫內單向發起同步』、『金庫管理身分庫物理隔離』、『Clean Room 復原 SOP：唯讀掛載 -> 高熵值/YARA掃描 -> 時鐘快進沙盒引爆 -> 安全轉移』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>攻擊威脅與 WORM 不可變存儲（7分）</strong>：深入點出勒索軟體專門摧毀快照與備份目錄之痛點，詳述 WORM Compliance 鎖定與 S3 Object Lock 原理。</li>
  <li><strong>隔離金庫架構與重點對比（7分）</strong>：以條列詳盡對比傳統在線 DR Site 與 Air-Gapped Vault 在連線、通道與身分庫維度的根本差異。</li>
  <li><strong>Clean Room 復原 SOP（7分）</strong>：繪出清晰架構流向，條列唯讀掛載、熵值檢驗、時間快進動態引爆與受控轉移。</li>
  <li><strong>結論（4分）</strong>：總結最後生存底線之戰略價值。</li>
</ul>
            """
        },

        # 8. sec-essay-56: Application Whitelisting (WDAC / IMA-EVM)
        {
            "id": "sec-essay-56",
            "category": "sec",
            "chapter": "第 8 章：金融釣魚防禦、社交工程與端點深度強化",
            "title": "核心主機應用程式白名單與程式碼完整性控制：Windows WDAC 與 Linux IMA/EVM 架構",
            "summary": "深入解構金融撮合與清算伺服器白名單控制、Windows Defender Application Control（WDAC）核心態原則、Linux 完整性度量架構（IMA/EVM）、程式碼數位簽章與全生命週期零信任加固。",
            "points": 25,
            "rubric": "1. 應用程式白名單必要性與 AppLocker 局限 (7分)；2. Windows WDAC 核心態架構深度剖析 (7分)；3. Linux IMA/EVM 機制與簽章落地 (7分)；4. 結論 (4分)",
            "question": "證券撮合伺服器與核心資料庫主機，依法嚴格禁止執行任何未經授權之第三方腳本或未知執行檔。請說明作業系統核心層程式碼完整性策略：深入剖析 Windows Defender Application Control（WDAC / CI 核心態原則）與 Linux Integrity Measurement Architecture（IMA/EVM）數位簽章驗證之工作機制；並規劃證券核心主機如何自編譯、簽名至部署運行建立全程端到端之防篡改白名單強制執行體系。",
            "modelAnswer": """
<h4>一、破題：核心金融主機由黑名單轉向強白名單之必然性</h4>
<p>在證券交易所板橋機房的核心撮合引擎、行情分發與帳務結算伺服器中，環境高度專用且固定。傳統基於特徵碼之防毒軟體（黑名單模型）存在「未知惡意代碼無法攔截」之致命漏洞；而早期的 Windows AppLocker 運作於用戶態（User-Mode），容易透過動態程式碼編譯、未受管制的 DLL 載入或記憶體注入遭到繞過。金融關鍵基礎設施必須升級為<strong>作業系統核心態（Kernel-Mode）強約束程式碼完整性白名單策略</strong>。</p>

<h4>二、Windows Defender Application Control (WDAC) 核心態防禦架構</h4>
<ol>
  <li><strong>核心層 Code Integrity (CI.dll) 強制執行</strong>：
    WDAC 不依賴容易遭竄改的服務或登錄檔，其安全原則由微軟 <code>CI.dll</code> 直接於 Windows 核心深處執行。即便攻擊者取得本地 Administrator 權限，若原則啟用<strong>數位簽章鎖定（Signed Policies）</strong>，攻擊者亦無法刪除或修改 WDAC 原則檔案。
  </li>
  <li><strong>基於信任根的簽章規則（Signer Rules）</strong>：
    放棄脆弱的檔案雜湊（Hash）與路徑規則（Path Rules），全面改用<strong>發行者憑證規則（Publisher / Signer Rules）</strong>：僅允許由臺灣證交所內部私有 CA、微軟或經核准之交易中介軟體廠商數位簽名之二進位檔執行。
  </li>
  <li><strong>使用者模式程式碼完整性（UMCI）與腳本強制拘束</strong>：
    WDAC 同時強制管控用戶態 DLL 載入，並將 PowerShell、Wscript、Cscript 自動降級至<strong>受限語言模式（Constrained Language Mode, CLM）</strong>，徹底封鎖反射式 API 呼叫與動態記憶體型無檔案攻擊。
</li>
</ol>

<h4>三、Linux 核心完整性度量架構（IMA / EVM）與實務落實</h4>
<ul>
  <li><strong>【全稱與核心責任】</strong>：<strong>IMA (Integrity Measurement Architecture)</strong>：Linux 核心完整性度量與評估子系統；<strong>EVM (Extended Verification Module)</strong>：擴充屬性安全驗證模組。</li>
  <li><strong>【驗證時機與底層運作原理】</strong>：<strong>IMA (Integrity Measurement Architecture)</strong>：在系統調用 bprm_check_security （執行前）與 file_mmap （映射前），於核心層即時計算檔案 SHA-256 雜湊或讀取擴充屬性（ security.ima ）簽章，與核心信任金鑰環（Keyring）比對，若不合規直接回傳 -EACCES 拒絕執行。；<strong>EVM (Extended Verification Module)</strong>：防止攻擊者離線竄改檔案中繼資料。EVM 針對 security.ima 、檔案擁有者 UID/GID、POSIX ACL 計算數位簽章並寫入 security.evm ，硬體 TPM 晶片參與金鑰簽署，確保中繼資料絕不被竄改。。</li>
</ul>

<h4>四、證券核心主機端到端安全編譯與防篡改落地架構</h4>
<pre><code class="language-text">[CI/CD 封閉管線] ──> [專用 HSM 私鑰簽署] ──> [產線部署] ──> [核心 WDAC / IMA 強制校驗]
 (原始碼靜態審查)      (產出 X.509 程式碼簽章)  (禁止外部寫入)     (非授權代碼 0.1ms 攔截)</code></pre>
<ol>
  <li><strong>私有金鑰隔離簽名</strong>：所有交易所自主研發之撮合與行情二進位程式，建置於隔離 CI/CD 管線；編譯完成後，由內部 HSM 專屬 Code-Signing 憑證直接簽名，簽章私鑰永不出 HSM 加密邊界。</li>
  <li><strong>唯讀不可變根檔案系統</strong>：生產伺服器核心目錄（如 <code>/usr/bin</code>, <code>/opt/twse</code>）於開機完成後直接掛載為<strong>唯讀（Read-Only）</strong>；搭配 IMA 強制原則（<code>ima_appraise=enforce</code>），杜絕任何線上未經簽名的腳本動態植入。</li>
</ol>

<h4>五、結論</h4>
<p>藉由在 Windows 端點部署核心態 WDAC 原則，在 Linux 主機啟用 IMA/EVM 數位簽章驗證，證券交易所徹底顛覆了傳統防毒軟體的滯後防禦，將主機執行環境嚴格固化為絕對零信任之確定性白名單狀態。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『AppLocker 用戶態易遭繞過，升級為 WDAC 核心態 CI.dll 強制執行』、『WDAC 簽章規則 (Signer Rules) 與 PowerShell 受限語言模式 (CLM)』、『Linux IMA 執行前度量 + EVM 擴充屬性防竄改』、『專用 HSM 程式碼簽章 (Code Signing)』、『唯讀檔案系統搭配 ima_appraise=enforce』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>白名單必要性與演進（7分）</strong>：深入辨析黑名單防毒與用戶態 AppLocker 局限，點出核心態完整性之戰略意義。</li>
  <li><strong>Windows WDAC 深度架構（7分）</strong>：詳細解析 CI.dll 核心執行、簽名原則鎖定（防 Admin 刪除）與 CLM 語言限制。</li>
  <li><strong>Linux IMA/EVM 深入對比（7分）</strong>：以條列清楚區分 IMA 內容度量與 EVM 中繼資料防竄改之協同運作機制。</li>
  <li><strong>端到端落實與結論（4分）</strong>：提出 HSM 簽章管線、唯讀掛載與強執行動態架構。</li>
</ul>
            """
        },

        # 9. sec-essay-57: Homomorphic Encryption & SMPC in AML / Risk Control
        {
            "id": "sec-essay-57",
            "category": "sec",
            "chapter": "第 12 章：新興科技資安、人工智慧（AI）與大語言模型安全",
            "title": "隱私強化技術（PETs）：同態加密（Homomorphic Encryption）與安全多方計算（SMPC）在金融跨機構聯合風控之落地",
            "summary": "深入剖析隱私強化技術（PETs）、Paillier / CKKS 同態加密數學原理、安全多方計算（SMPC 秘密分享）、金融反洗錢（AML）跨機構黑名單密文比對，以及數據「可用不可見」合規架構。",
            "points": 25,
            "rubric": "1. 金融數據共享法律衝突與 PETs 破題 (7分)；2. 同態加密 vs SMPC 技術對比 (7分)；3. 證券期貨業跨機構聯合風控落地 (7分)；4. 結論 (4分)",
            "question": "金管會積極推動金融機構間反洗錢（AML）與防詐詐欺情資聯防，然而直接共享客戶交易明細面臨《個人資料保護法》之法律紅線。請說明隱私強化技術（Privacy-Enhancing Technologies, PETs）之原理；對比同態加密（Fully/Partially Homomorphic Encryption）與安全多方計算（SMPC / 秘密分享）之數學基礎與運算開銷；並為臺灣證券期貨業設計一套「數據可用不可見」之分散式黑名單聯合比對與風控信用評估架構。",
            "modelAnswer": """
<h4>一、破題：金融聯防之「數據孤島」與法規衝突困境</h4>
<p>在防範電信詐騙、人頭戶洗錢與市場操縱之實戰中，單一證券商僅能掌握客戶於自家券商之委託與出入金行為，難以察覺跨銀行、跨券商之分散式人頭戶洗錢鏈。然而，若直接彙整各券商之客戶個資與交易明細至單一資料庫，直接牴觸臺灣《個人資料保護法》第 20 條特定目的外利用之嚴格限制，亦面臨災難性的集中外洩風險。</p>
<p><strong>隱私強化技術（Privacy-Enhancing Technologies, PETs）</strong>為化解此一矛盾提供了數學與密碼學解方：透過同態加密與安全多方計算，使各金融機構在<strong>完全不洩漏客戶明文資料、不共享原始金鑰</strong>的前提下，直接於「密文狀態」完成協同計算，落實「數據可用不可見，數據不動模型動」。</p>

<h4>二、同態加密（HE）vs 安全多方計算（SMPC）技術對比</h4>
<ul>
  <li><strong>【同態加密 (Homomorphic Encryption)】</strong>：<strong>核心數學原理</strong>：密文代數同構性 ： Enc(m1) ⊗ Enc(m2) = Enc(m1 ⊕ m2) - 部分同態 (PHE, 如 Paillier 支援密文加法與純量乘法)； - 全同態 (FHE, 如 CKKS / BGV 支援任意次數加乘運算)。；<strong>通訊與計算開銷</strong>：零節點間互動（通訊量低） ，但密文多項式運算帶來極大 CPU 算力開銷（FHE 較明文慢 1,000~10,000 倍）。；<strong>金融證券最佳場景</strong>：外包給公有雲或中心節點進行海量密文統計（如密文資產總額統計、密文加權評分）。。</li>
  <li><strong>【安全多方計算 (SMPC)】</strong>：<strong>核心數學原理</strong>：秘密分享（Shamir's Secret Sharing）與不經意傳輸（Oblivious Transfer, OT） ： 將原始數據拆分為多個隨機分片（Shares），單一分片不含任何有效資訊，僅當達到門檻值（Threshold t-of-n）時方能重構。；<strong>通訊與計算開銷</strong>：本地計算極快，但在計算乘法門時 需要節點間多輪網路通訊互動 ，對網路延遲與頻寬要求極高。；<strong>金融證券最佳場景</strong>：數家大型券商與交易所之間的 跨機構黑名單交集（Private Set Intersection, PSI） 比對。。</li>
</ul>

<h4>三、證券期貨業跨機構聯合風控與反洗錢落地架構</h4>
<ol>
  <li><strong>基於 PSI（隱私集合求交）的高風險帳戶聯防比對</strong>：
    - 交易所作為協調節點，各券商將疑似警示帳戶之身分證字號，透過 <strong>ECDH-PSI 協定</strong> 轉換為加密點；<br>
    - 各方在不暴露自家非交集客戶名單的前提下，僅能計算出「同時出現在 A 券商與 B 券商之異常重疊名單」，徹底防範客戶個資外洩。
  </li>
  <li><strong>基於 Paillier 加法同態之跨機構槓桿保證金風控</strong>：
    - 當投資人向券商申請信用交易擴大額度時，系統需評估其在全市場之總曝險；<br>
    - 各券商將該身分之融資融券負債額度使用 Paillier 公鑰加密，將密文傳送至證交所集保平台；<br>
    - 平台直接在密文上進行同態累加：<code>Enc(Total) = Enc(Debt_A) × Enc(Debt_B)</code>；<br>
    - 平台將累加結果返回授信券商進行門檻解密判定，全程任何人皆無法探知該客戶在各家券商的具體分項金額。
</li>
</ol>

<h4>四、結論</h4>
<p>隱私強化技術（PETs）打破了「保護隱私必須犧牲數據價值」的零和博弈。透過同態加密與安全多方計算的工程化落地，臺灣證券期貨業得以在嚴格遵守《個人資料保護法》之最高標準下，建構全市場動態智慧聯防體系，為金融科技創新開闢安全坦途。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『數據孤島 vs 個資法特定目的外利用衝突』、『數據可用不可見，數據不動模型動』、『同態加密代數同構性：Paillier 加法同態 vs CKKS 全同態』、『SMPC：Shamir 秘密分享與 Oblivious Transfer』、『ECDH-PSI 隱私集合求交黑名單比對』、『Paillier 密文相乘即明文累加於跨券商授信風控』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>數據共享法規困境（7分）</strong>：深入點出個資法限制與跨券商聯防痛點，精準定義 PETs 戰略價值。</li>
  <li><strong>HE vs SMPC 技術對比（7分）</strong>：以條列詳盡比較代數同構、秘密分享、計算開銷與通訊互動模式之根本差異。</li>
  <li><strong>金融實務落地設計（7分）</strong>：具體設計 ECDH-PSI 黑名單求交架構與 Paillier 密文同態信用額度總和評估流程。</li>
  <li><strong>結論（4分）</strong>：總結安全與隱私共贏之制度成效。</li>
</ul>
            """
        },

        # 10. sec-essay-58: Zero-Day Emergency Response & Virtual Patching
        {
            "id": "sec-essay-58",
            "category": "sec",
            "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
            "title": "零日漏洞（Zero-Day）緊急應變：虛擬補丁（Virtual Patching）與 WAF/IPS 規則生命週期管理",
            "summary": "深入解構重大零日漏洞（如 Log4j、Spring4Shell）應變機制、虛擬補丁（Virtual Patching）架構、WAF/IPS 正則正規化防繞過、旁路監控評估，以及正式代碼補丁轉正與下線閉環管理。",
            "points": 25,
            "rubric": "1. 零日漏洞痛點與虛擬補丁定義 (7分)；2. 虛擬補丁技術實作與抗繞過機制 (7分)；3. 虛擬補丁全生命週期管理流程 (7分)；4. 結論 (4分)",
            "question": "當業界爆發重大零日漏洞（如 Log4j Log4Shell、Spring4Shell）而原廠尚未發布正式代碼補丁時，金融核心交易系統無法立即停機進行代碼重構。試說明何謂「虛擬補丁（Virtual Patching）」？分析其在 WAF、反向代理與 IPS 端點之實施機制與防護優勢；說明如何透過正則表達式正規化防範繞過（Evasion Techniques）；並規劃一套涵蓋 2 小時緊急上線、誤攔截評估、正式補丁轉正與虛擬補丁下線之完整生命週期管理準則。",
            "modelAnswer": """
<h4>一、破題：零日漏洞（Zero-Day）之暴露時間窗危機與虛擬補丁</h4>
<p>當像 Apache Log4j（Log4Shell, CVE-2021-44228）或 Spring4Shell 這種影響深遠的重大零日漏洞於在野環境被揭露時，金融機構面臨嚴峻的時間窗口考驗：自漏洞公開到黑客自動化掃描武器化發動攻擊，往往僅有數小時；而金融核心系統受制於嚴格的變更管理委員會（CAB）審核、代碼迴歸測試與盤中不可停機原則，<strong>實體代碼修補往往需要數天至數週</strong>。</p>
<p><strong>虛擬補丁（Virtual Patching）</strong>是在「應用程式源碼未做任何變更」的前提下，於流量抵達脆弱應用程式之前的網路邊界設備（如 WAF、反向代理、API 閘道或 IPS），攔截、檢測並阻斷特定利用該漏洞的攻擊負載，為後台開發團隊爭取寶貴的補丁修復時間。</p>

<h4>二、虛擬補丁實施機制與抗編碼繞過（Evasion Techniques）</h4>
<ul>
  <li><strong>1. 邊界 L7 WAAP / WAF</strong>：檢測 HTTP Request Body、URI 參數、Headers（User-Agent, Cookie）。；深層正規化（Normalization） ：黑客利用巢狀變數繞過（如 ${${lower:j}ndi:...} 、URL 多重編碼、Unicode 變體）。WAF 必須遞迴解碼至最小元基底，方能精確比對 JNDI/LDAP 模式。。</li>
  <li><strong>2. 網路層 IPS</strong>：利用 Snort / Suricata 規則監控 TCP 串流中的特徵字串。；TCP 封包重組與分片防禦 ：黑客故意將 Payload 拆分成數個小於 5 bytes 的 TCP 封包逃避檢測。IPS 必須啟用串流重組（Stream Reassembly）還原完整資料段。。</li>
  <li><strong>3. 主機層 RASP (運行時自我保護)</strong>：以 Java Agent 直接掛載於 JVM 記憶體內部，攔截底層 JNDI.lookup() 系統調用。；語意級精確攔截 ：無論網路層如何混淆編碼，一旦抵達底層執行函數時均已完全還原，誤報率趨近於零。。</li>
</ul>

<h4>三、金融虛擬補丁全生命週期管理流程</h4>
<pre><code class="language-text">[F-ISAC 0-Day 預警] ──> [2小時緊急上線: 監控模式] ──> [誤攔截分析] ──> [切換阻斷模式] ──> [實體代碼轉正] ──> [下線廢止]</code></pre>
<ol>
  <li><strong>階段一：2 小時內緊急部署與「監控不阻斷（Log-Only / Detect Mode）」</strong>：
    接獲 0-Day 情資後，資安團隊於 2 小時內完成邊界 WAF 正則特徵規則編寫與推播。<strong>前 4 小時強制運行於監控模式</strong>，比對生產環境正常業務流量（如手機 App 下單、即時行情），評估是否有合法業務名稱意外觸發正則匹配。
  </li>
  <li><strong>階段二：規則微調與無誤切換「強制阻斷（Block Mode）」</strong>：
    確認無誤攔截後，經由緊急資安審查快速授權，正式將 WAF 規則切換為主動阻斷，對惡意連線返回 HTTP 403，成功於邊界凍結攻擊面。
  </li>
  <li><strong>階段三：後台實體補丁發布與完整測試</strong>：
    開發團隊在測試環境針對原始程式碼（如升級 Log4j 至 2.17.1+ 或替換相依套件）進行完整功能、回歸及壓力測試。
  </li>
  <li><strong>階段四：正式補丁發布上線與虛擬補丁退場（Deprecation）</strong>：
    實體補丁於例行維護窗口部署至生產伺服器後，<strong>虛擬補丁持續保留監控 14 天</strong>，待確認產線系統穩定後，正式自 WAF 規則庫中卸載，釋放閘道器 CPU 運算資源，完成閉環。
</li>
</ol>

<h4>四、結論</h4>
<p>虛擬補丁是金融資安緊急應變中的「戰術止血帶」。透過 WAF 邊界正規化防護、Log-Only 到 Block 的科學切換，以及無縫對接實體代碼修復之完整生命週期，臺灣證券交易所方能在瞬息萬變的零日漏洞風暴中立於不敗之地。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『零日漏洞痛點：黑客武器化數小時 vs 金融變更重構數週』、『虛擬補丁 (Virtual Patching) 定義：不改源碼於邊界攔截』、『抗編碼繞過：遞迴正規化 (Normalization) 破解 ${${lower:j}ndi}』、『三層機制：WAF + IPS TCP 重組 + RASP 運行時語意攔截』、『生命週期四階段：2小時上線Log-Only -> 評估無誤切Block -> 實體補丁轉正 -> 14天觀察後退場』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>零日漏洞危機與概念（7分）</strong>：深入點評時間窗口差與金融合規停機痛點，精確定義虛擬補丁之戰略定位。</li>
  <li><strong>實施機制與防繞過重點條列（7分）</strong>：以條列逐項剖析 WAF 遞迴解碼正規化、IPS 封包重組與 RASP 記憶體調用攔截原理。</li>
  <li><strong>全生命週期 SOP（7分）</strong>：條列清晰的四階段流程（Log-Only、Block、實體修復、14天觀察退場），符合金融變更合規實務。</li>
  <li><strong>結論（4分）</strong>：以「戰術止血帶」形象化總結，展現高水準申論結構。</li>
</ul>
            """
        }
    ]

def get_remaining_10_sec_essays():
    return [
        # 11. sec-essay-59: Deepfake Defense in eKYC
        {
            "id": "sec-essay-59",
            "category": "sec",
            "chapter": "第 12 章：新興科技資安、人工智慧（AI）與大語言模型安全",
            "title": "生成式 AI 深度偽造（Deepfake）防禦：多模態活體檢測（Liveness Detection）與視訊身分驗證（eKYC）安全",
            "summary": "深入剖析生成式擴散模型與語音複製對證券線上開戶（eKYC）之威脅、多模態活體檢測（rPPG 遠距光體積變化描記圖、3D結構光、動作挑戰）、C2PA 數位內容憑證認證與反偽冒實務。",
            "points": 25,
            "rubric": "1. Deepfake 對金融 eKYC 攻擊型態剖析 (7分)；2. 多模態活體檢測技術機制 (7分)；3. 證券開戶系統立體防禦架構與 C2PA (7分)；4. 結論 (4分)",
            "question": "隨著生成式擴散模型與語音複製技術進步，詐騙集團利用 Deepfake 擬真人臉與即時語音置換，向金融機構發起「偽冒開戶」與「視訊下單核身」攻擊。請分析 Deepfake 即時視訊與語音合成之攻擊技術原理；說明金融級 eKYC 系統應如何整合多模態活體檢測（動態指令微表情挑戰、紅外線/3D結構光光學心率檢測 rPPG）防範偽冒；並闡述 C2PA 內容憑證標準於數位資產防偽驗證之應用。",
            "modelAnswer": """
<h4>一、破題：Deepfake 技術武器化對金融開戶核身之根本威脅</h4>
<p>在推動無紙化與行動金融時代，國內外券商廣泛採用「線上開戶視訊核身（eKYC）」與「大額語音確認下單」。然而，生成式對抗網路（GAN）與擴散模型（Diffusion Models，如 Stable Diffusion、LivePortrait）之演進，使黑客僅需數張受害者社交照片，即可生成逼真的臉部動作與即時表情換臉；搭配 VITS 語音複製（Voice Cloning），攻擊者能即時模擬受害者聲音特徵，完美欺騙傳統僅仰賴單純眨眼、點頭之初階活體識別，引發大規模冒名人頭戶開戶洗錢危機。</p>

<h4>二、多模態活體檢測（Liveness Detection）防護體系</h4>
<ul>
  <li><strong>1. 生理信號偵測 (rPPG 光體積變化)</strong>：遠距光體積變化描記圖（rPPG） ：相機感測心臟跳動引起的臉部毛細血管微血管顏色、光線反射週期性奈米變化，反演人體脈搏波形。；<strong>實務落地/對策</strong>：極致防禦 ：螢幕翻拍、面具或 AI 生成的虛擬像素，絕對不具備人體血液循環所誘發之生物脈搏頻率！。</li>
  <li><strong>2. 動態非對稱挑戰 (Active Challenge)</strong>：隨機動態指令挑戰（如隨機指定轉頭角度、指定發音唸出隨機驗證字串、螢幕顏色隨機彩光照射臉部）。；<strong>實務落地/對策</strong>：預先錄製之 Deepfake 影片無法即時響應伺服器隨機指令；螢幕彩光反射能即時校驗臉部 3D 物理幾何曲面之光影變化。。</li>
  <li><strong>3. 頻域紋理特徵 (Frequency Domain)</strong>：傅立葉轉換（FFT）與高頻雜訊殘差分析 ：檢測神經網路卷積上採樣產生之網格偽影（Checkerboard Artifacts）與不自然微表情邊界。；<strong>實務落地/對策</strong>：即使肉眼看起來逼真，頻域分析能一眼識破 AI 演算法生成的統計異常高頻特徵。。</li>
</ul>

<h4>三、證券線上開戶（eKYC）立體防偽架構與 C2PA 規範</h4>
<ol>
  <li><strong>雙重多因子物理錨定</strong>：
    - <strong>實體身分證晶片 NFC 讀取</strong>：手機 App 強制感應內政部新式身分證晶片（如有），讀取晶片內部私鑰簽署之官方證件照片原始檔，杜絕偽造證件翻拍；<br>
    - <strong>語音偽造聲紋頻譜檢測</strong>：針對語音下單，分析語音中高頻泛音與合成語音常見之相量不連續性（Phase Discontinuity），阻斷 Voice Clone 詐騙。
  </li>
  <li><strong>C2PA（內容真實性與溯源聯盟）數位簽章標準</strong>：
    - 引入 C2PA（Coalition for Content Provenance and Authenticity）開放標準；<br>
    - 視訊拍攝時，客戶端硬體安全晶片（Secure Enclave）在影像感測器（CIS）捕捉畫面瞬間，直接將硬體時間戳、GPS 與相機指紋封裝為加密中繼資料（Metadata），並以晶片私鑰簽發 JUMBF 雜湊鏈。任何經過後製換臉軟體處理之影片，該簽章鏈將即刻斷裂失效。
</li>
</ol>

<h4>四、結論</h4>
<p>面對生成式 AI 帶來的「真實性危機」，金融機構必須揚棄單一維度的視覺檢測，全面整合 rPPG 生理脈搏、動態互動光影、頻域特徵分析與 C2PA 硬體端簽章，為臺灣證券市場開闢一道防範 Deepfake 詐欺的堅實護盾。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『Deepfake 威脅：GAN / 擴散模型實時換臉與 Voice Clone 破解傳統開戶核身』、『rPPG (遠距光體積變化描記圖)：微血管血液流動脈搏，AI生成物無生理信號』、『動態非對稱挑戰：隨機彩光照射臉部校驗物理 3D 光影反射』、『頻域 FFT 捕捉卷積網格偽影 (Checkerboard Artifacts)』、『C2PA 內容憑證：相機感測器硬件級數位簽名防篡改』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>Deepfake 威脅成因（7分）</strong>：深入辨析生成式模型如何瓦解傳統眨眼/點頭初階活體認證，指出冒名開戶洗錢之痛點。</li>
  <li><strong>多模態活體檢測表（7分）</strong>：以條列詳盡對比 rPPG 生理脈搏、動態彩光隨機挑戰、頻域 FFT 殘差分析之反偽冒原理。</li>
  <li><strong>eKYC 防偽架構與 C2PA（7分）</strong>：提出 NFC 晶片認證、聲紋泛音檢驗與 C2PA 硬件級防篡改簽章鏈。</li>
  <li><strong>結論（4分）</strong>：總結由純軟體判定進化為硬體與多模態生理感知之成效。</li>
</ul>
            """
        },

        # 12. sec-essay-60: Full Packet Capture (FPC) & NDR
        {
            "id": "sec-essay-60",
            "category": "sec",
            "chapter": "第 7 章：SOC 威脅監控、SIEM/SOAR、EDR 與事件應變",
            "title": "全封包擷取（Full Packet Capture, FPC）與網路偵測與回應（NDR）在金融 APT 潛伏獵捕之實務",
            "summary": "深入剖析網路封包客觀真相（Ground Truth）、FPC 無損線速側錄架構、NDR 深度封包檢測（DPI）、TLS 1.3 加密流量分析（ETA / JA4 指紋），以及金融機房歷史攻擊回溯鑑識。",
            "points": 25,
            "rubric": "1. 日誌缺陷與 FPC 客觀真實性價值 (7分)；2. FPC 線速硬體架構與儲存規劃 (7分)；3. NDR 加密流量分析 (ETA/JA4) (7分)；4. 結論 (4分)",
            "question": "傳統日誌（Logs）容易遭受敵手篡改或刪除，而網路封包是還原攻擊真相唯一的「客觀真相來源」。請說明全封包擷取（FPC）在證券交易中心面對微秒級瞬時攻擊與資料外洩之鑑識價值；闡述網路偵測與回應（NDR）如何運用深度封包檢測（DPI）與非對稱網路鏡像（TAP/SPAN）技術；並分析在全流量 TLS 1.3 加密環境下，NDR 如何透過加密流量分析（ETA，如封包長度分佈、到達時間間隔、JA4 TLS 指紋）在不解密前提下識別惡意 C2 通訊。",
            "modelAnswer": """
<h4>一、破題：日誌的可篡改性與網路封包之「客觀絕對真相」</h4>
<p>在進階持續性威脅（APT）攻擊中，攻擊者取得 Windows 或 Linux 最高權限後，常第一時間使用 <code>wevtutil cl</code> 或刪除 <code>/var/log/auth.log</code> 抹除攻擊足跡。此外，應用程式日誌僅記錄「開發者預設記錄的事項」，無法記錄封包內部之原始二進位負載。唯有<strong>全封包擷取（Full Packet Capture, FPC）</strong>在獨立實體網路上忠實留存 L2~L7 所有原始封包，具備<strong>無法被端點敵手竄改之客觀真實性（Ground Truth）</strong>，是數位鑑識與法律呈堂證供的最後黃金基石。</p>

<h4>二、證券核心機房 FPC 無損線速側錄架構規劃</h4>
<ol>
  <li><strong>無侵入實體分光（Optical TAP）部署</strong>：
    嚴禁使用交換器 SPAN 連接埠（因高負載時交換器優先丟棄 SPAN 鏡像封包造成漏包）。必須在撮合交換器與下單閘道器之間，部署<strong>實體光纖分光器（Passive Optical TAP）</strong>，按 70/30 比例分光，確保零注入、零延遲、對生產交易完全透明。
  </li>
  <li><strong>FPGA 網卡硬體線速寫入與循環儲存</strong>：
    採用具備 <strong>FPGA 硬體加速的專用擷取網卡</strong>，在 40Gbps/100Gbps 線速下實現<strong>零丟包（Zero Packet Drop）</strong>；搭配環形緩衝區與 NVMe SSD 磁碟陣列，實現至少保留 7 至 14 天完整 PCAP 封包資料庫，支援以微秒時間戳進行歷史事件精確回溯。
</li>
</ol>

<h4>三、全流量 TLS 1.3 環境下 NDR 加密流量分析（ETA）機制</h4>
<ul>
  <li><strong>1. TLS 握手元數據 (Client Hello 指紋)</strong>：JA4 / JA4S 指紋 ALPN 協商特徵、Cipher Suites 排序；TLS 1.3 握手的第一個封包為明文。Cobalt Strike、Sliver 等黑客 C2 框架具備特定且罕見的加密套件排列組合，可即時比對 F-ISAC 惡意指紋庫直接阻斷。。</li>
  <li><strong>2. 封包長度分佈序列 (SPLT)</strong>：Sequence of Packet Length and Time (SPLT)；正常證券 Web 下單呈現「客戶端短請求、伺服器長回應」之非對稱分佈；而惡意 C2 心跳通道呈現「週期性極小固定長度（如 64 bytes）」封包，透過機器學習分類器可精準區分。。</li>
  <li><strong>3. 封包到達時間間隔 (Inter-Arrival Time)</strong>：連線週期性與時間抖動率 (Jitter)；真人操作具備高度不規則的隨機間隔；自動化木馬之 Beaconing 具備嚴格的規律時間週期（即使黑客設定 20% Jitter 隨機抖動，傅立葉頻譜分析仍能捕捉週期基頻）。。</li>
</ul>

<h4>四、結論</h4>
<p>在金融資安攻防中，「封包不會說謊」。透過實體 Optical TAP 實現 100Gbps 零丟包 FPC 儲存，結合 NDR 尖端之加密流量行為分析（ETA），臺灣證券交易所即使面對全面採用 TLS 1.3 加密隱匿的境外 APT 組織，亦能從容撕開黑客面具，守護交易市場生命線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『日誌易遭抹除，封包為唯一不說謊之客觀真相 (Ground Truth)』、『拒用 SPAN 鏡像防丟包，部署無侵入 Passive Optical TAP 光纖分光』、『FPGA 硬體加速 100Gbps 零丟包寫入』、『TLS 1.3 不解密偵測：ETA (加密流量分析)』、『三大維度：JA4 握手特徵、SPLT (封包長度時間序列)、Beaconing 抵達時間間隔抖動分析』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>FPC 客觀價值（7分）</strong>：深入辨析日誌被刪除與不可篡改性差異，精準定義 FPC 之鑑識權威地位。</li>
  <li><strong>線速硬體與儲存架構（7分）</strong>：詳細說明 Optical TAP 70/30 分光、FPGA 零丟包處理與 NVMe 歷史回溯機制。</li>
  <li><strong>ETA 加密流量分析重點對比（7分）</strong>：以條列逐項剖析 JA4 指紋、SPLT 長度序列與時間間隔頻譜在不解密前提下的機器學習識別原理。</li>
  <li><strong>結論（4分）</strong>：強調「封包不會說謊」對抗高級 APT 之核心底蘊。</li>
</ul>
            """
        },

        # 13. sec-essay-61: Third-Party & Nth-Party Vendor Risk Management
        {
            "id": "sec-essay-61",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "證券期貨業委外作業資安風險管理規範與第四方（Nth-Party）供應鏈穿透式稽核實踐",
            "summary": "深入解構金管會金融作業委託他人處理規範、第四方（Nth-Party）軟體相依性滾雪球風險、委外合約法定資安條款（實地稽核權、30分鐘通報、原始碼代管）、定期穿透式資安成熟度評鑑作業。",
            "points": 25,
            "rubric": "1. 金融委外法規要求與第四方風險本質 (7分)；2. 委外合約四大核心資安法定條款 (7分)；3. 穿透式現地稽核 SOP 與評鑑指標 (7分)；4. 結論 (4分)",
            "question": "金管會發布「金融機構作業委託他人處理內部作業應注意事項」與證券期貨業委外資安規範，嚴防委外廠商成為駭客打入金融內網之跳板。請說明金融機構執行資訊委外之風險評估要項；剖析第四方供應鏈（委外廠商之再委外協力廠商）引發之「滾雪球效應」風險；並詳述合約應明訂之資安關鍵條款（實地稽核權、源碼審查、30分鐘通報、資安責任上限）與每年現地穿透式稽核標準作業程序。",
            "modelAnswer": """
<h4>一、破題：委外供應鏈資安風險與第四方（Nth-Party）滾雪球效應</h4>
<p>金融機構為加速數位轉型，大量將行動下單 App、客戶關係管理（CRM）、報表產製甚至核心系統維運委外給第三方科技廠商（Third-Party）。然而，駭客往往採取「迂迴戰術」：避開防禦森嚴的交易所主體，轉而滲透資安防護薄弱的委外廠商，利用遠端維運專線跳板直搗金融黃龍。</p>
<p>更嚴峻的是<strong>第四方供應鏈（Nth-Party / Fourth-Party）風險</strong>：委外軟體商往往又將特定模組（如圖表套件、簡訊 API、雲端主機）分包給再委外協力廠商，或大量調用開源函式庫。一旦第四方元件包含惡意後門（如 SolarWinds、Log4j、XZ Utils 事件），風險將沿著供應鏈層層傳導放大，引發災難性的<strong>滾雪球骨牌效應</strong>。</p>

<h4>二、金融委外契約法定四大關鍵資安條款</h4>
<ul>
  <li><strong>1. 實地穿透式稽核權 (Right to Audit)</strong>：標準為 <strong>金融機構及主管機關（金管會）得 隨時派員或委託獨立第三方 至廠商及再委外廠商之辦公處所、機房實施現場查核；廠商不得拒絕或拖延。</strong>；處置作為：打破「黑盒子」委外，確保監理權力延伸至供應鏈底層。。</li>
  <li><strong>2. 重大事件即時通報時效 (Incident Notification)</strong>：標準為 <strong>廠商知悉任何疑似資安受駭或機敏資料外洩事件， 必須於「知悉起 30 分鐘內」正式通報交易所 ；每 2 小時提供更新進度。</strong>；處置作為：確保交易所能於第一時間切斷維運專線，阻斷橫向擴散。。</li>
  <li><strong>3. 軟體源碼審查與代管 (Source Code Escrow)</strong>：標準為 <strong>交付前必須通過第三方 SAST/DAST 零重大漏洞檢測；交付完整 SBOM；若廠商破產或惡意終止維護， 第三方代管機構無條件釋出原始碼 。</strong>；處置作為：防止廠商倒閉引發業務中斷，防範惡意程式碼暗藏後門。。</li>
  <li><strong>4. 違約損害賠償上限排除 (Liability Carve-outs)</strong>：標準為 <strong>因廠商故意、重大過失或違反資安保密導致交易所受罰或投資人損失， 排除一般合約之「以合約總額為賠償上限」限制 。</strong>；處置作為：落實廠商實質法律責任，促使廠商董事會高度重視資安。。</li>
</ul>

<h4>三、每年委外廠商穿透式現地稽核標準作業程序（SOP）</h4>
<ol>
  <li><strong>階段一：桌上型成熟度初審（Off-Site Review）</strong>：
    審查廠商是否具備有效之 ISO 27001 / SOC 2 Type II 認證、全員社交工程釣魚演練紀錄、員工背景查核制度與資安專業人員證照（CISSP / CISM）。
  </li>
  <li><strong>階段二：實地環境穿透檢測（On-Site Technical Audit）</strong>：
    - <strong>遠距連線跳板稽核</strong>：查核維運工程師連入交易所之跳板堡壘機，是否嚴格啟用雙因子身分認證（2FA）與工作階段錄影；嚴禁廠商內部個人電腦直連交易所核心主機；<br>
    - <strong>代碼存儲與防外洩（DLP）抽查</strong>：檢查開發用筆電是否封鎖 USB、是否部署 EDR、原始碼儲存庫（GitLab）是否配置權限最小化與分支保護規則；<br>
    - <strong>再委外（Subcontractor）合規盤點</strong>：清查廠商是否未經核准擅自將模組再外包，若有再委外，強制簽署同等效力之資安保證書。
  </li>
  <li><strong>階段三：缺失矯正與限期覆核（Remediation & Closure）</strong>：
    針對稽核發現之缺失（如使用過期不安全套件），開立矯正通知書，要求高風險缺失於 14 天內修復完成並檢附佐證，未依限改善者啟動合約扣款甚至終止委外資格。
</li>
</ol>

<h4>四、結論</h4>
<p>金融安全之堅固程度取決於其供應鏈中最脆弱的環節。透過建立穿透式稽核權力、嚴苛的合約責任約束，以及定期的實地技術檢驗，臺灣證券交易所方能有效消除第四方滾雪球盲點，打造無懈可擊的金融生態系供應鏈防線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『第四方供應鏈 (Nth-Party) 滾雪球骨牌效應』、『合約四大法定條款：實地穿透式稽核權、知悉起 30 分鐘緊急通報、原始碼第三方代管 (Software Escrow)、排除賠償上限』、『實地稽核重點：遠端維運跳板 2FA 隔離、開發環境 EDR 與禁止 USB、GitLab 分支保護』、『14天缺失限期改善閉環』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>委外與第四方風險成因（7分）</strong>：深入辨析迂迴滲透戰術，精準定義第四方開源與再分包之滾雪球傳導危害。</li>
  <li><strong>四大合約條款重點條列（7分）</strong>：以條列逐項剖析實地稽核、30分鐘通報、原始碼代管與賠償上限排除之具體法律效力。</li>
  <li><strong>現地稽核 SOP（7分）</strong>：詳細條列桌上審查、現場技術查核（維運跳板、EDR、原始碼庫）及限期矯正閉環。</li>
  <li><strong>結論（4分）</strong>：總結供應鏈木桶理論之治理價值。</li>
</ul>
            """
        },

        # 14. sec-essay-62: Insider Threat Defense & DLP
        {
            "id": "sec-essay-62",
            "category": "sec",
            "chapter": "第 8 章：金融釣魚防禦、社交工程與端點深度強化",
            "title": "內部人威脅（Insider Threat）防護：DLP 資料外洩防護、隱形微點螢幕浮水印與周邊硬體管控實踐",
            "summary": "深入剖析金融交易機房內部人員威脅模型、三態 DLP（端點/儲存/網路）檢測技術、隱形微點螢幕浮水印（Forensic Watermarking）、特權終端周邊設備硬體 ID 白名單控管實務。",
            "points": 25,
            "rubric": "1. 內部人威脅模型與成因 (7分)；2. 三態 DLP 檢測技術機制對比 (7分)；3. 隱形浮水印與周邊控制實作 (7分)；4. 結論 (4分)",
            "question": "金融核心交易系統面臨內部特權員工或協力廠商工程師惡意盜取交易演算法、未公開重大財報或客戶機敏帳務之內部人威脅（Insider Threat）。請說明內部威脅三大類型（惡意洩漏、疏忽過失、憑證遭冒用）之特徵；分析資料外洩防護（DLP）在端點、儲存與網路傳輸三態之檢測技術；並詳述如何結合隱形微點螢幕數位浮水印（Forensic Watermarking）、外接儲存設備硬體識別碼（Device ID）白名單管控，建構無死角資料防洩稽核防線。",
            "modelAnswer": """
<h4>一、破題：內部人威脅（Insider Threat）三大模型剖析</h4>
<p>金融資安防線傳統多禦敵於國門之外，然而內部人員早已坐擁合法身分、熟悉網路架構且具備高存取權限。CERT Insider Threat Center 將內部人威脅歸納為三大類型：</p>
<ol>
  <li><strong>惡意洩漏者（Malicious Insider）</strong>：出於金錢利益、跳槽競爭對手或報復動機，故意利用自身特權下載交易演算法源碼、客戶明細或撮合核心架構。</li>
  <li><strong>疏忽過失者（Negligent Insider）</strong>：缺乏資安意識，將機敏原始碼誤上傳至公開 GitHub、將含客戶個資檔案寄至私人信箱，或隨意插拔未受防護之隨身碟。</li>
  <li><strong>憑證遭冒用者（Infiltrator / Compromised Credential）</strong>：員工帳號遭外部 APT 駭客透過釣魚或撞庫竊取，黑客「借殼上市」以合法內部員工身分在內網大搖大擺竊密。</li>
</ol>

<h4>二、資料外洩防護（DLP）三態防禦架構對比</h4>
<ul>
  <li><strong>1. 端點使用中 (Data-in-Use)</strong>：端點型 DLP (Endpoint DLP) 部署於維運主機與辦公筆電之 Agent；監控剪貼簿複製貼上、螢幕截圖（PrintScreen）、列印輸出、外接 USB 寫入；若偵測到機敏正則（身分證、信用卡號、金鑰特徵）立即清空剪貼簿並阻斷寫入。。</li>
  <li><strong>2. 儲存靜止中 (Data-at-Rest)</strong>：發現型 DLP (Discovery DLP) 背景排程爬網掃描器；深度巡檢內部檔案伺服器、NAS、資料庫未加密欄位與雲端共用槽；利用 精確資料比對（Exact Data Match, EDM） 與檔案數位指紋（File Hash Fingerprinting），揪出違規儲存之未遮蔽個資並強制隔離加密。。</li>
  <li><strong>3. 網路傳輸中 (Data-in-Motion)</strong>：網路型 DLP (Network DLP) 旁路鏡像或串接於邊界閘道器；結合 TLS 解密代理，全面解析 SMTP 郵件附件、HTTP/HTTPS 上傳、WebDAV 流量；一旦發現未授權外發機敏檔案，直接重置 TCP 連線或將郵件強制隔離至主管審核佇列。。</li>
</ul>

<h4>三、微點隱形浮水印與周邊硬體 ID 嚴格控管實作</h4>
<ol>
  <li><strong>隱形微點螢幕數位浮水印（Forensic Watermarking）</strong>：
    - 傳統可見浮水印（顯式文字）容易被離職員工以手機傾斜拍照、調整相片對比度或修圖抹除；<br>
    - 部署<strong>法醫級隱形微點浮水印</strong>：在螢幕顯示與匯出報表背景中，以肉眼難以察覺的微米級像素色差（黃色微點矩陣），將「員工工號 + 登入時間戳 + 終端 IP」以糾錯碼演算法編碼隱匿；<br>
    - 即使員工使用手機翻拍、局部截圖甚至列印後掃描，鑑識軟體對照片進行反色反差分析，<strong>於 3 秒內即可還原原始工號與外洩來源</strong>，形成強大的心理威懾。
  </li>
  <li><strong>周邊硬體識別碼（Device ID）白名單管控</strong>：
    - 透過作業系統 GPO 與端點防護 Agent，預設<strong>全面禁用所有 USB 大容量儲存設備（USB Mass Storage）</strong>；<br>
    - 若特定交易維運需匯出除錯日誌，強制採用「硬體白名單審批制」：僅允許具備指定硬體序號（Vendor ID、Product ID 與 Serial Number）且經全磁碟硬體加密之專用隨身碟，並限制僅能單次單向寫入，寫入內容全程錄影審計。
</li>
</ol>

<h4>四、結論</h4>
<p>內部威脅防護並非單純的不信任，而是建立客觀可稽核的免責邊界。透過三態 DLP 攔截、隱形法醫浮水印溯源與硬體級周邊鎖定，臺灣證券交易所能確保交易資產在最微細的操作端點皆能處於全生命週期受控狀態。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『內部威脅三模型：惡意洩漏、疏忽過失、憑證遭冒用』、『三態 DLP：Data-in-Use (端點剪貼/截圖)、Data-at-Rest (儲存EDM精確匹配)、Data-in-Motion (網路TLS解密審查)』、『隱形微點螢幕浮水印 (Forensic Watermarking)：黃色微點矩陣抗手機翻拍修圖，3秒還原工號』、『USB 白名單：基於 VID/PID/Serial Number + 硬體全盤加密』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>內部威脅模型（7分）</strong>：深入辨析惡意、疏忽與憑證遭冒用三者的動機與行為特徵。</li>
  <li><strong>三態 DLP 機制重點對比（7分）</strong>：以標準條列架構逐項剖析使用中、靜止中與傳輸中的技術部署模式與阻斷手法（EDM 指紋）。</li>
  <li><strong>浮水印與周邊管控實踐（7分）</strong>：詳細解析微點隱形浮水印抗翻拍解碼技術，以及 USB VID/PID 硬體級白名單。</li>
  <li><strong>結論（4分）</strong>：總結客觀稽核與內部防禦底線之價值。</li>
</ul>
            """
        },

        # 15. sec-essay-63: eBPF Tetragon & Kernel-Level Runtime Security
        {
            "id": "sec-essay-63",
            "category": "sec",
            "chapter": "第 9 章：雲端與容器安全、DevSecOps 實務",
            "title": "eBPF 核心級安全觀測與即時阻斷：Tetragon 與 Cilium Network Policy 在證券 Linux 主機之防禦實務",
            "summary": "深入剖析傳統 ptrace / auditd 性能損耗與繞過缺陷、eBPF 核心驗證器（Verifier）安全性、Tetragon 於系統呼叫層直接阻斷（kprobe/tracepoint）、Cilium 容器網路微隔離實務。",
            "points": 25,
            "rubric": "1. 傳統 Linux 監控瓶頸與 eBPF 核心理念 (7分)；2. Tetragon 核心級即時阻斷機制 (7分)；3. Cilium eBPF 網路原則相較 iptables 優勢 (7分)；4. 結論 (4分)",
            "question": "傳統 Linux 主機安全工具仰賴 ptrace、auditd 或 LD_PRELOAD，存在極大性能開銷（高 CPU/記憶體延遲）且易遭 rootkit 繞過。請說明延伸 Berkeley 封包過濾器（eBPF）之技術架構與安全機制（eBPF Verifier）；深入剖析 Tetragon 如何在核心層核心系統呼叫（System Calls, 如 sys_execve、sys_socket）實現微秒級惡意行為直接阻斷；並比較 Cilium eBPF 網路原則與傳統 iptables 在大規模微服務下之效能與安全性優勢。",
            "modelAnswer": """
<h4>一、破題：傳統 Linux 主機監控缺陷與 eBPF 革命</h4>
<p>在證券交易所低延遲撮合與行情 Linux 主機中，每微秒的延遲都至關重要。過去的安全防禦工具面臨兩難困境：</p>
<ol>
  <li><strong>極高的系統呼叫損耗</strong>：傳統 <code>auditd</code> 或 <code>ptrace</code> 會引入頻繁的用戶態（User Space）與核心態（Kernel Space）上下文切換（Context Switch），在每秒數萬筆委託併發時引發 CPU 飆高達 20%~30%，更可能造成行情封包嚴重抖動丟包。</li>
  <li><strong>容易遭受攻擊者繞過</strong>：基於 <code>LD_PRELOAD</code> 的掛鉤技術僅存在於用戶態，具備 root 權限的攻擊者可輕易卸載或透過靜態編譯繞過；核心模組（LKM）又極易引發核心當機（Kernel Panic）。</li>
  <li><strong>eBPF 核心革命</strong>：<strong>延伸 Berkeley 封包過濾器（eBPF）</strong>允許沙盒化程式直接在 Linux 核心中安全運行，<strong>無需修改核心源碼或載入外部模組</strong>；所有程式在載入前必須通過 <strong>eBPF Verifier（靜態驗證器）</strong>嚴格檢查，保證不發生死循環、無非法記憶體存取，確保系統絕對穩定。</li>
</ol>

<h4>二、Tetragon 於核心層微秒級即時阻斷機制剖析</h4>
<p>傳統主機 EDR 僅具備「事後通知告警」能力（非同步接收日誌，通知用戶態代理殺掉行程，此時勒索軟體已加密完成或反彈 Shell 已成功建立）。<strong>Tetragon</strong> 實現了真正的<strong>核心內同步即時阻斷（In-Kernel Real-Time Enforcement）</strong>：</p>
<pre><code class="language-text">[攻擊者發起 sys_execve("/bin/sh")]
               │
               ▼
┌────────────────────────────────────────────────────────┐
│ Linux Kernel 系統呼叫層 (kprobe / tracepoint)         │
│   └── eBPF Tetragon 鉤子程式                           │
│         ├── 解析行程命名空間 (Namespace) 與二進位簽章  │
│         ├── 比對 CRD 安全原則                          │
│         └── 命中非法提權規則！                          │
│               │
│               ├─> 直接回傳 sigkill (-9) 終止行程！     │
│               └─> 向用戶端非同步發送 JSON 稽核日誌     │
└────────────────────────────────────────────────────────┘
               │ 惡意 Shell 未曾離開核心態，0 微秒直接猝死！
               ▼
           (攻擊徹底失敗)</code></pre>
<ol>
  <li><strong>系統呼叫層深層過濾</strong>：掛鉤於 <code>sys_execve</code>、<code>sys_socket</code>、<code>tcp_connect</code> 等關鍵內核端點，在行程建立或網路連線<strong>尚未完成之前</strong>進行阻斷。</li>
  <li><strong>覆蓋攻擊面（Namespace Escape 逃逸防禦）</strong>：精準偵測特權容器逃逸，若容器內部行程企圖載入核心模組、讀取主機 <code>/proc</code> 或呼叫 <code>setns()</code>，Tetragon 在核心態直接強制覆寫系統呼叫返回值，令逃逸指令瞬間失效。</li>
</ol>

<h4>三、Cilium eBPF 網路原則 vs 傳統 iptables 效能與安全對比</h4>
<ul>
  <li><strong>【傳統 Linux iptables / Netfilter】</strong>：<strong>演算法複雜度</strong>：O(n) 線性循序走訪 ：規則達到數萬條時，封包遍歷所有規則引發極高延遲；<strong>服務連線轉發開銷</strong>：必須走完整個 Linux 網路堆疊（TCP/IP Stack、conntrack、NAT），多次上下文切換；<strong>微隔離安全顆粒度</strong>：僅能依賴靜態 IP / Port 進行粗糙過濾，動態容器漂移時規則頻繁刷新鎖定。</li>
  <li><strong>【Cilium eBPF 網路原生架構】</strong>：<strong>演算法複雜度</strong>：O(1) BPF Map 哈希表直查 ：無論原則數量達到數千或數十萬條，查表時間恆定；<strong>服務連線轉發開銷</strong>：Socket 層直接短路繞過（Sockops Bypass） ：同節點容器間通訊直接跨記憶體拷貝，吞吐量提升 300%；<strong>微隔離安全顆粒度</strong>：原生基於 K8s 標籤（Labels）與 L7 應用層 （如限定僅允許 HTTP GET /quote ，阻斷 POST）。</li>
</ul>

<h4>四、結論</h4>
<p>eBPF 技術為 Linux 核心安全帶來了質的飛躍。透過 Tetragon 在核心層的微秒級即時阻斷，搭配 Cilium O(1) 極致低延遲微隔離網路原則，證券交易平台在兼顧微秒級高頻極致性能的同時，構築起容器化雲原生架構下堅不可摧的核心防線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『傳統缺陷：auditd/ptrace 上下文切換消耗大，LD_PRELOAD 易遭繞過』、『eBPF Verifier 靜態驗證無死循環無野指針』、『Tetragon 核心態同步阻斷：sys_execve 直接回傳 sigkill 終止行程』、『Cilium eBPF vs iptables：O(1) 哈希表直查取代 O(n) 線性走訪』、『Sockops Socket 層直接短路繞過提升 300% 吞吐』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>傳統監控缺陷與 eBPF 理念（7分）</strong>：深入辨析性能開銷與用戶態被繞過缺陷，精準定義 eBPF Verifier 之沙盒安全本質。</li>
  <li><strong>Tetragon 核心阻斷機制（7分）</strong>：繪出核心呼叫攔截流程圖，詳述 sys_execve 掛鉤、sigkill 即時處置與容器逃逸防護。</li>
  <li><strong>Cilium vs iptables 重點對比（7分）</strong>：以條列逐項剖析 O(1) vs O(n) 複雜度、Sockops 繞過堆疊與 L7 標籤式微隔離優勢。</li>
  <li><strong>結論（4分）</strong>：總結微秒性能與核心安全兼得之成效。</li>
</ul>
            """
        },

        # 16. sec-essay-64: CIEM & Cloud Key Management (BYOK / HYOK)
        {
            "id": "sec-essay-64",
            "category": "sec",
            "chapter": "第 9 章：雲端與容器安全、DevSecOps 實務",
            "title": "雲端身分與權限權利管理（CIEM）與客戶自持金鑰（HYOK / BYOK）跨雲治理",
            "summary": "深入剖析金融多雲環境權限過度授予（Over-privileged Identities）、CIEM 權限差距量化演算法、客戶自備金鑰（BYOK）與自持金鑰（HYOK）信任邊界，以及金管會雲端委外金鑰自主控制合規實踐。",
            "points": 25,
            "rubric": "1. 雲端權限失控痛點與 CIEM 治理 (7分)；2. BYOK vs HYOK 關鍵架構對比 (7分)；3. 金融跨雲金鑰管理落地實作 (7分)；4. 結論 (4分)",
            "question": "金融機構邁向混合雲與多雲架構時，「權限過度授予（Over-permissioned Identities）」與「雲端金鑰外洩」成為重大合規隱患。請深入說明雲端身分與權限權利管理（CIEM）如何量化計算「權限差距（Permission Gap）」並落實最小特權存取；比較客戶自備金鑰（BYOK, Bring Your Own Key）與客戶自持金鑰（HYOK, Hold Your Own Key）之架構差異與法規信任邊界；並設計證交所敏感資料加密上雲之金鑰主控防護架構。",
            "modelAnswer": """
<h4>一、破題：多雲時代的身分權限爆炸與信任邊界危機</h4>
<p>金融機構採用跨公有雲（AWS, Azure, GCP）建置周邊大數據與創新應用時，面臨兩大核心資安痛點：</p>
<ol>
  <li><strong>身分權限過度授予（Permission Gap 危機）</strong>：多雲 IAM 規則極度複雜，開發者常為求便利配置萬用字元權限（如 <code>*:*</code> 或 <code>AdministratorAccess</code>），統計顯示超過 95% 的雲端角色僅使用了其被賦予權限的不到 2%，形成巨大的「休眠高危特權（Dormant Entitlements）」，黑客取得任一存取金鑰（Access Key）即可引發全雲淪陷。</li>
  <li><strong>金鑰主控權與合規疑慮</strong>：依金管會金融機構作業委外資安規範，金融機敏資料若存放於公有雲，<strong>加密金鑰之主控權必須由金融機構牢固掌握</strong>，絕不可允許雲端服務提供商（CSP）在未受授權下存取明文資料。</li>
</ol>

<h4>二、CIEM 核心治理演算法：權限差距收斂流程</h4>
<pre><code class="language-text">[授予權限 (Granted Permissions)] ──────────────────────────────┐
                                                              ├──> 權限差距 (Permission Gap) ──> 自動化收斂修剪
[實際使用權限 (Used Permissions)] <──(分析90天 CloudTrail日誌)─┘</code></pre>
<ol>
  <li><strong>權限差距量化（Permission Gap Analysis）</strong>：
    CIEM 引擎持續抓取雲端稽核日誌（如 AWS CloudTrail、Azure Activity Logs），以 90 天為滑動基準線，比對「IAM 政策所賦予之權限清單」與「運行時實際呼叫之 API 清單」。兩者之差集即為 <strong>Permission Gap</strong>。
  </li>
  <li><strong>動態最小權限政策自動生成（Least-Privilege Remediation）</strong>：
    CIEM 自動將寬鬆的 <code>Statement</code> 重構為僅包含實際呼叫 API 的細粒度最小原則，並透過 GitOps CI/CD 管線下發自動置換，徹底清除休眠特權。
</li>
</ol>

<h4>三、雲端金鑰管理模式深度對比：BYOK vs HYOK</h4>
<ul>
  <li><strong>【BYOK (Bring Your Own Key, 自備金鑰)】</strong>：<strong>金鑰生成與託管實體</strong>：金鑰由地端 HSM 生成，但 匯入並暫存於雲端服務商之 KMS / HSM 中 。；<strong>解密運算發生位置</strong>：解密運算在雲端供應商之硬體模組內部執行。；<strong>雲端服務功能相容性</strong>：極佳 ：原生無縫整合雲端原生資料庫（RDS）、容器（EKS）與 S3 物件儲存。；<strong>抗法規調取與傳票能力 (Sovereignty)</strong>：若外國政府依美國 CLOUD Act 向 CSP 發出秘密傳票，CSP 具備理論強制解密能力。。</li>
  <li><strong>【HYOK (Hold Your Own Key, 自持金鑰)】</strong>：<strong>金鑰生成與託管實體</strong>：金鑰 始終鎖定於證交所內部實體 HSM ，絕不匯入雲端！；<strong>解密運算發生位置</strong>：雲端發起解密請求時，必須 透過專線回傳至地端實體 HSM 進行運算 。；<strong>雲端服務功能相容性</strong>：受限 ：雲端原生服務無法直接透明調用，需依賴應用層自定義加密 SDK，延遲較高。；<strong>抗法規調取與傳票能力 (Sovereignty)</strong>：完全免疫 ：CSP 無私鑰，任何人均無法迫使其解密，符合金融最高機密合規。。</li>
</ul>

<h4>四、證券交易所敏感資料上雲混合金鑰架構實作</h4>
<ol>
  <li><strong>分級分類治理（Data Classification）</strong>：
    - <strong>第一級：極端機敏資料（撮合訂單、券商結算款、核心演算法）</strong>：嚴格採用 <strong>HYOK 模式</strong>，應用層地端加密完成後方才上雲；<br>
    - <strong>第二級：一般業務資料（歷史行情大數據分析、報表）</strong>：採用 <strong>BYOK 模式</strong>，地端 HSM 生成根金鑰，透過安全金鑰包裝（Key Wrapping）匯入雲端專屬 KMS，享受雲端原生彈性算力。
  </li>
  <li><strong>緊急金鑰撤銷「斷電開關（Kill Switch）」</strong>：
    一旦偵測到雲端環境發生重大未授權連線或跨國法規衝突，地端金鑰管理員按下一鍵撤銷指令，0.1 秒內刪除雲端 KMS 金鑰材料或切斷 HYOK 專線回呼通道，雲端數據瞬間變為完全不可讀之亂碼，徹底保全金融主權。
</li>
</ol>

<h4>五、結論</h4>
<p>在多雲時代，身分是新的網路邊界，而金鑰是資料的主權堡壘。透過 CIEM 精準消除權限差距，並以 BYOK/HYOK 建立牢固的密碼學主控邊界，臺灣證券交易所方能在雲端現代化浪潮中兼顧敏捷創新與合規底線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『CIEM 核心：量化 Permission Gap (授予權限 vs 實際90天使用權限) 自動收斂』、『休眠高危特權 (Dormant Entitlements) 消除』、『BYOK (金鑰進雲端KMS) vs HYOK (金鑰永在地端HSM，雲端僅能回呼解密)』、『CLOUD Act 跨國數據主權防護』、『緊急斷電開關 (Kill Switch) 0.1秒使雲端數據瞬變亂碼』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>多雲權限失控與金鑰法規痛點（7分）</strong>：深入點評萬用字元權限氾濫成因，點出金管會對金鑰自主可控之法規剛性要求。</li>
  <li><strong>CIEM 演算法與收斂流程（7分）</strong>：繪出 Permission Gap 差集計算流向，條列 CloudTrail 稽核分析與 GitOps 自動化修復。</li>
  <li><strong>BYOK vs HYOK 重點對比（7分）</strong>：以條列逐項剖析託管實體、解密位置、服務相容性與 CLOUD Act 法律抗辯能力的根本差異。</li>
  <li><strong>分級落地與結論（4分）</strong>：設計 HYOK/BYOK 分級上雲方案與緊急 Kill Switch 斷電機制。</li>
</ul>
            """
        },

        # 17. sec-essay-65: BOPLA & GraphQL Security
        {
            "id": "sec-essay-65",
            "category": "sec",
            "chapter": "第 5 章：應用程式安全、Web 攻防與安全軟體開發（SSDLC）",
            "title": "API 安全進階攻防：物件屬性級權限控制失效（BOPLA）與 GraphQL 深度遞迴 DoS 防護",
            "summary": "深入剖析 OWASP API Security Top 10:2023 新增之 BOPLA 物件屬性級授權失效、大量賦值（Mass Assignment）、過度資料暴露、GraphQL 巢狀遞迴 DoS 攻擊，以及查詢深度限制與代價計算防禦實作。",
            "points": 25,
            "rubric": "1. BOPLA 漏洞成因與金融下單危害 (7分)；2. 防禦 BOPLA 安全編碼 (DTO/白名單) (7分)；3. GraphQL 巢狀 DoS 原理與代價防禦 (7分)；4. 結論 (4分)",
            "question": "OWASP API Security Top 10:2023 將物件屬性級授權失效（BOPLA）列為核心威脅，整併了過度資料暴露與大量賦值漏洞。請分析 BOPLA 在證券交易 API（如修改個人資料時竄改帳戶餘額或交易費率）之攻擊情境與防禦代碼實踐；剖析現代行情採用 GraphQL 時面臨之「巢狀遞迴循環查詢 DoS」攻擊原理；並詳述如何透過查詢深度限制（Query Depth Limiting）、代價計算（Query Cost Analysis）與欄位層級權限控制（Field-level Authorization）全面化解風險。",
            "modelAnswer": """
<h4>一、破題：API3:2023 BOPLA 漏洞本質與金融交易危害</h4>
<p>在 OWASP API Security Top 10:2023 改版中，正式將原本分散的「過度資料暴露（Excessive Data Exposure）」與「大量賦值（Mass Assignment）」整併為 <strong>API3:2023 Broken Object Property Level Authorization（BOPLA，物件屬性級授權失效）</strong>。</p>
<p>BOPLA 專注於使用者對特定物件「特定屬性欄位」的讀取或修改權限控制缺失。在證券與行動下單系統中，危害尤為致命：</p>
<ol>
  <li><strong>寫入端大量賦值攻擊（Mass Assignment）</strong>：
    券商提供 <code>PUT /api/v1/user/profile</code> 允許投資人修改電話與地址。後端開發者若使用 ORM 框架之「自動綁定（Auto-binding）」（如 <code>User.update(request.body)</code>），黑客故意在 JSON 中注入非表單欄位 <code>{"tradeFeeDiscount": 0.001, "isVIP": true, "balance": 99999999}</code>。伺服端若未嚴格過濾屬性，該非授權欄位將直接被寫入資料庫，黑客成功篡改交易手續費率或帳戶餘額！
  </li>
  <li><strong>讀取端過度資料暴露（Excessive Data Exposure）</strong>：
    在查詢個人持股 <code>GET /api/v1/stocks</code> 時，後台直接將資料庫整張實體資料表序列化傳回，依賴前端前端過濾顯示，使得攻擊者可透過 Fiddler/Burp Suite 側錄截獲未遮蔽之身份證字號、內部銀行虛擬帳號或信用評級。
</li>
</ol>

<h4>二、BOPLA 核心防禦與安全編碼實務</h4>
<ul>
  <li><strong>【脆弱實作 (易受駭模式)】</strong>：<strong>寫入控制 (Input)</strong>：直接將 req.body 傳入 ORM 更新資料庫實體。；<strong>讀取控制 (Output)</strong>：依賴前端 React/Vue 隱藏敏感欄位。。</li>
  <li><strong>【安全架構實踐 (Gold Standard)】</strong>：<strong>寫入控制 (Input)</strong>：強制使用嚴格 DTO（資料傳輸物件）與屬性白名單 ：僅允許明確宣告之欄位（如 phone , address ）綁定，任何多餘欄位直接拒絕拋出 400 Bad Request。；<strong>讀取控制 (Output)</strong>：伺服端回應投影（Projection / View Object） ：嚴格採用 UserResponseVO ，僅序列化允許該使用者角色讀取之欄位，敏感欄位根本不出伺服器記憶體。。</li>
</ul>

<h4>三、GraphQL 巢狀遞迴 DoS 攻擊原理與立體防護</h4>
<p>現代證券行情系統漸進採用 GraphQL 提供彈性資料查詢。然而，若存在雙向關聯（如 <code>Broker -> Stocks -> Broker -> Stocks</code>），攻擊者可構造極度惡意的<strong>深層巢狀遞迴查詢 Payload</strong>：</p>
<pre><code class="language-graphql">query MaliciousQuery {
  broker(id: 101) {
    stocks {
      broker {
        stocks {
          broker {
            stocks { ... 遞迴 10,000 層 ... }
          }
        }
      }
    }
  }
}</code></pre>
<p>此類單一 HTTP 請求將引發後端資料庫指數級爆發之關聯查詢（<strong>N+1 查詢放大攻擊</strong>），只需發送 5 個請求即可瞬間耗盡伺服器 CPU 與資料庫連線池，造成全市場行情查詢中斷。</p>
<ol>
  <li><strong>查詢深度限制（Query Depth Limiting）</strong>：
    在 GraphQL 引擎（如 Apollo Server）中掛載驗證規則，解析查詢之抽象語法樹（AST）。嚴格規定<strong>最大允許深度不得超過 5 層（Max Depth = 5）</strong>，任何超過層級之請求於解析階段直接阻斷，不進入任何後端查詢。
  </li>
  <li><strong>查詢代價分析（Query Cost Analysis）</strong>：
    為每個欄位設定複雜度權重（例如純量欄位 <code>name</code> = 1 分；清單關聯欄位 <code>stocks</code> = 10 分 × 分頁數量）。單一查詢設定最大代價上限（如 Max Cost = 200），若超過上限直接拒絕。
  </li>
  <li><strong>分頁強制約束（Mandatory Pagination）</strong>：
    禁止任何無限制的清單查詢，所有陣列欄位強制要求提供 <code>first: 50</code> 或 <code>limit: 50</code> 參數，防止海量拉取資料。
</li>
</ol>

<h4>四、結論</h4>
<p>API 安全必須深入至「屬性欄位級」與「資料庫查詢複雜度」之微觀視角。透過 DTO 嚴格白名單阻斷 BOPLA，並在 GraphQL 邊界部署 AST 深度限制與代價熔斷，臺灣證券交易才能在提供靈活金融 API 服務的同時，徹底固化應用層之安全性與高可用性。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『API3:2023 BOPLA = 過度資料暴露 + 大量賦值 (Mass Assignment)』、『防禦核心：嚴格 DTO 屬性白名單 + 伺服端 View Object 投影』、『GraphQL 雙向關聯 N+1 查詢指數級爆炸 DoS』、『GraphQL 三大防線：AST 查詢深度限制 (Max Depth ≤ 5)、查詢代價分析 (Query Cost Analysis)、強制分頁約束』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>BOPLA 漏洞本質（7分）</strong>：深入辨析 2023 新版 BOPLA 整併概念，以手續費率篡改與個資外洩具體說明危害。</li>
  <li><strong>安全編碼重點對比（7分）</strong>：以條列逐項剖析寫入端 DTO 白名單與讀取端 VO 投影的防禦代碼實踐。</li>
  <li><strong>GraphQL 巢狀 DoS 與防禦（7分）</strong>：寫出惡意遞迴查詢程式碼範例，詳述 AST 深度限制、代價計分演算法與強制分頁機制。</li>
  <li><strong>結論（4分）</strong>：總結微觀屬性與查詢複雜度雙重治理之價值。</li>
</ul>
            """
        },

        # 18. sec-essay-66: CISO Governance & Three Lines Model, KRIs/KPIs
        {
            "id": "sec-essay-66",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金融資通安全長（CISO）治理架構：資安三道防線（Three Lines Model）與董事會量化 KRI/KPI 實踐",
            "summary": "深入解構金管會專責資安長（CISO）法定權責、IIA 新三道防線模型在金融資安之職責邊界、資安關鍵風險指標（KRI）與關鍵績效指標（KPI）量化體系，以及董事會定期報告與溝通實務。",
            "points": 25,
            "rubric": "1. 專責 CISO 設立法規與權責獨立性 (7分)；2. 資安三道防線職責劃分表 (7分)；3. 董事會量化 KPI/KRI 指標體系設計 (7分)；4. 結論 (4分)",
            "question": "金管會強制要求一定規模以上證券期貨業配置專責資安長（CISO）及專責部門。請說明現代內部控制「新三道防線模型（Three Lines Model）」在資安領域中各道防線（業務營運單位、資安專責部門、內部稽核部門）之明確職責與獨立性要求；設計一套能向董事會精準報告資安韌性態勢之關鍵績效指標（KPI）與關鍵風險指標（KRI，如 MTTD、MTTR、未修補高危漏洞存活天數、釣魚測試易感率）；並闡述 CISO 如何推動資安文化與合規治理。",
            "modelAnswer": """
<h4>一、破題：金管會專責資安長（CISO）設立要求與治理獨立性</h4>
<p>依金管會「金融資安行動方案 2.0」及「證券期貨商資通安全防護評估原則」，符合一定資本額或核心地位之證券期貨機構，<strong>必須設置副總經理層級以上之專責資通安全長（CISO）</strong>，且 CISO <strong>不得兼任資訊主管（CIO）或業務主管</strong>。此「職能獨立性」規定旨在打破過去「資訊為求系統快速上線而犧牲資安審查」之內在利益衝突，賦予 CISO 直接向董事會及審計委員會報告之法規權柄。</p>

<h4>二、新三道防線模型（Three Lines Model）在金融資安之權責分工</h4>
<ul>
  <li><strong>第一道防線 (First Line)</strong>：<strong>組織主體與定位</strong>：業務與 IT 維運部門 (第一線風險擁有者)；落實日常操作安全控管、安全編碼 (SSDLC)、系統補丁更新、機房實體門禁維護、初階事件通報。；<strong>獨立性與監督對象</strong>：承擔直接營運風險，接受第二道防線之政策指導與合規審查。。</li>
  <li><strong>第二道防線 (Second Line)</strong>：<strong>組織主體與定位</strong>：CISO 領導之資安專責部門 (風險監督與專業賦能)；制定全行資安政策標準（對齊 ISO 27001 / NIST CSF）、SOC 7x24 威脅監控、紅藍對抗實兵演練、第三方供應鏈稽核、主導 30 分鐘重大事件通報。；<strong>獨立性與監督對象</strong>：獨立於業務與 IT 維運，具備「資安一票否決權」；直接向總經理與董事會報告。。</li>
  <li><strong>第三道防線 (Third Line)</strong>：<strong>組織主體與定位</strong>：獨立內部稽核部門 (獨立超然保證)；獨立評估第一道及第二道防線之運作有效性，檢驗資安架構是否符合金管會法規與內部政策。；<strong>獨立性與監督對象</strong>：完全獨立於管理階層，直屬董事會審計委員會，定期提出稽核查核報告。。</li>
</ul>

<h4>三、向董事會精準量化之 KPI 與 KRI 指標體系設計</h4>
<p>董事會不關心「封鎖了幾百萬次攻擊」等技術噪音，CISO 必須將資安轉化為「可量化的營運風險與商業韌性語言」：</p>
<ol>
  <li><strong>關鍵績效指標（KPI，衡量防禦流程效能）</strong>：
    - <strong>MTTD（平均偵測時間，Mean Time to Detect）</strong>：自攻擊者滲透發生至 SOC 系統成功發出有效告警之時間（證券目標：<strong>< 15 分鐘</strong>）；<br>
    - <strong>MTTR（平均回應處置時間，Mean Time to Respond）</strong>：自告警觸發至安全小組遏止並隔離威脅之時間（證券目標：<strong>< 30 分鐘</strong>）；<br>
    - <strong>釣魚測試易感率（Phishing Prone Percentage）</strong>：無預警釣魚郵件點擊與帳密輸入比例（目標：降至 <strong>< 3%</strong>）。
  </li>
  <li><strong>關鍵風險指標（KRI，衡量潛在暴險危機）</strong>：
    - <strong>未修補重大漏洞平均存活天數（Vulnerability Dwell Time）</strong>：CVSS ≥ 9.0 或 CISA KEV 漏洞在生產環境未修補天數（監理紅線：<strong>< 7 天</strong>）；<br>
    - <strong>第三方法定資安評鑑不符合比例</strong>：供應商重大缺失未結案數量；<br>
    - <strong>特權帳號審查覆蓋率與零常設權限（ZSP）合規率</strong>：未啟用動態 JIT 提權的常態 Admin 帳號佔比（目標：<strong>0%</strong>）。
</li>
</ol>

<h4>四、結論</h4>
<p>CISO 不再只是救火的技術專家，而是企業頂層治理戰略的推動者。透過健全三道防線之權責制衡，並以量化 KRI/KPI 與董事會建立高透明度溝通，臺灣證券交易所方能將資安治理深植於企業 DNA，護航金融交易穩健前行。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『金管會規定專責 CISO 副總經理層級以上，不得兼任 CIO 確保獨立性』、『新三道防線：第一道(業務/IT 風險擁有)、第二道(CISO資安專責 風險監督+一票否決)、第三道(內部稽核 獨立保證)』、『董事會語言：拒絕技術噪音，轉化為營運韌性指標』、『KPI：MTTD (<15分)、MTTR (<30分)、釣魚易感率 (<3%)』、『KRI：高危漏洞存活天數 (<7天)、ZSP 零常設特權合規率 (100%)』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>專責 CISO 法定定位（7分）</strong>：深入辨析 CISO 與 CIO 之職責利益衝突，精準引用金管會法規強調獨立性。</li>
  <li><strong>三道防線分工重點條列（7分）</strong>：以條列逐項剖析第一道、第二道、第三道在資安落地中的邊界責任與隸屬關係。</li>
  <li><strong>董事會量化 KPI/KRI 設計（7分）</strong>：條理分明區分 KPI 效能指標（MTTD/MTTR）與 KRI 風險指標（漏洞存活天數/特權比例），具體給出金融量化目標值。</li>
  <li><strong>結論（4分）</strong>：總結頂層戰略與企業文化構建。</li>
</ul>
            """
        },

        # 19. sec-essay-67: Distributed Trading Protocol Security (FIX Security, SeqReset, Replay)
        {
            "id": "sec-essay-67",
            "category": "sec",
            "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
            "title": "分散式證券交易通訊安全：FIX 協定序號重置（SeqReset）攻擊、時戳漂移與訊息完整性防護",
            "summary": "深入剖析證券期貨標準通訊協定 FIX 4.2/4.4/5.0 Session 機制、序號重置（SeqReset/GapFill）攻擊、惡意委託重放（Replay Attack）、時鐘飄移（Timestamp Drift）與多層級訊息完整性防護架構。",
            "points": 25,
            "rubric": "1. FIX 協定狀態維護機制與安全威脅 (7分)；2. SeqReset 與 Replay 攻擊原理深入剖析 (7分)；3. 金融 FIX 通訊立體防禦架構 (7分)；4. 結論 (4分)",
            "question": "臺灣證券期貨市場各券商與交易所之間廣泛採用金融資訊交換協定（FIX Protocol）進行下單委託與撮合成交回報。請分析 FIX 協定之 Session 狀態維護機制；深入剖析黑客發動惡意序號重置（SeqReset/GapFill）以丟棄合法委託、或注入重放過期委託（Stale Order / Replay Attack）之攻擊手法；並規劃在 FIX 傳輸層、應用層及時鐘同步（PTP）三大維度落實數位簽名、嚴格時戳漂移窗口限制與完整性校驗之加固方案。",
            "modelAnswer": """
<h4>一、破題：FIX 協定在證券核心交易之地位與架構挑戰</h4>
<p><strong>FIX（Financial Information eXchange Protocol）</strong>是全球證券、期貨、選擇權市場通訊之事實標準語言（如 FIX 4.2, 4.4 與 FIXT 1.1/FIX 5.0）。FIX 協定劃分為<strong>工作階段層（Session Layer）</strong>與<strong>應用層（Application Layer）</strong>：</p>
<ol>
  <li><strong>嚴格的雙向訊息序號機制（MsgSeqNum）</strong>：
    連線雙方於每日交易開始前協商初始序號（通常為 1）。每發送一筆訊息（如 <code>35=D</code> 新單委託），序號嚴格遞增 1。若接收方發現序號跳號（Gap），會發送 <code>ResendRequest (35=2)</code> 要求重傳，以此確保交易指令<strong>零遺失、零重複且嚴格循序抵達</strong>。
  </li>
  <li><strong>安全原罪與新興威脅</strong>：
    早期 FIX 協定設計於私有封閉專線，預設採用明文傳輸（標籤 <code>Tag=Value</code> 鍵值對），未內建強認證與不可否認性機制。若內部網路或專線遭攻擊者中間人（MITM）滲透，攻擊者可透過竄改序號發動致命破壞。
</li>
</ol>

<h4>二、經典 FIX 協定攻擊技術深入剖析</h4>
<ul>
  <li><strong>1. 惡意序號重置 (Malicious SeqReset)</strong>：攻擊者注入偽造之 SequenceReset (35=4) 封包，將 NewSeqNo (Tag 36) 惡意跳躍至極大數值（如跳過 1000 號），並設定 GapFillFlag (Tag 123) = Y 。；<strong>實務落地/對策</strong>：交易所伺服器誤以為中間訊息已妥善處理而直接忽視， 導致大量合法券商下單委託被永久靜默吞沒丟棄 ，引發市場撮合重大不公與法律糾紛。。</li>
  <li><strong>2. 過期委託重放 (Stale Order Replay)</strong>：攻擊者側錄早盤特定大幅獲利之買進委託，於尾盤行情不利時重新發送；或濫用 PossDupFlag (Tag 43) = Y 假冒重傳訊息。；<strong>實務落地/對策</strong>：若伺服器未校驗原始發送時間戳（ OrigSendingTime, Tag 122 ），將引發重複扣款與重覆下單，造成投資人巨額違約交割風險。。</li>
</ul>

<h4>三、證券 FIX 通訊立體化縱深防禦加固方案</h4>
<ol>
  <li><strong>傳輸層強制 TLS 1.3 + mTLS 雙向憑證綁定</strong>：
    全面廢除未加密之明文 FIX 連線，底層強制採用 <strong>mTLS（雙向傳輸層加密）</strong>。券商伺服器與交易所閘道器皆必須出示由臺灣網路認證公司（TWCA）簽署之合格 X.509 憑證，杜絕任何第三方未授權偽造 TCP 封包或中間人篡改。
  </li>
  <li><strong>高精度 PTP 時間戳記與嚴格時鐘漂移窗口（Timestamp Window Check）</strong>：
    - 依據歐盟 MiFID II RTS 25 標準，所有 FIX 訊息必須基於 <strong>IEEE 1588v2 PTP 奈秒級時間戳</strong> 記錄 <code>SendingTime (Tag 52)</code>；<br>
    - 交易所下單閘道器實施<strong>嚴格時戳容許窗口校驗</strong>：若接收到訂單之時間戳與當前精確時間偏差超過 <strong>500 毫秒（500ms）</strong>，系統直接予以 Reject（拒絕委託）；<br>
    - 若 <code>PossDupFlag=Y</code>，強制校驗 <code>OrigSendingTime (Tag 122)</code>，一旦發現原始時間與當前差距超過容許值，直接丟棄。
  </li>
  <li><strong>應用層敏感欄位數位簽章（FIX Digital Signature）</strong>：
    針對大額委託或撤單指令，啟用 FIX 原生之 <code>RawDataLength (Tag 95)</code> 與 <code>RawData (Tag 96)</code> 欄位，將關鍵交易標籤（帳號、股號、股數、價格、時戳）利用客戶端 HSM 私鑰進行 <strong>SHA-256 + Ed25519 數位簽章</strong> 封裝，達成應用層不可篡改性與不可否認性。
</li>
</ol>

<h4>四、結論</h4>
<p>在高速高頻的證券交易環境中，通訊協定的可靠性直接牽動金融市場的公信力。透過 mTLS 傳輸加密、PTP 微秒時鐘漂移熔斷機制與應用層數位簽章，臺灣證券交易所為 FIX 交易通訊築起了防竄改、防重放與高可用的鋼鐵防線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『FIX 雙向序號 MsgSeqNum 確保零遺失零重複』、『SeqReset 攻擊：惡意偽造 Tag 36 (NewSeqNo) 與 Tag 123 (GapFill) 造成合法委託被靜默吞沒』、『Stale Order 重放攻擊：側錄重發，破解依賴 Tag 122 (OrigSendingTime) 校驗』、『底層強制 mTLS 雙向認證』、『IEEE 1588v2 PTP 奈秒同步 + 500ms 時鐘漂移嚴格窗口熔斷』、『Tag 96 封裝 Ed25519 應用層數位簽名』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>FIX Session 狀態維護機制（7分）</strong>：深入辨析 MsgSeqNum、ResendRequest 雙向保證機制，點出明文原罪之安全痛點。</li>
  <li><strong>SeqReset 與重放攻擊深入重點條列（7分）</strong>：以條列詳盡解構 Tag 36、Tag 123、Tag 43 等具體標籤的濫用步驟與對交易的實質破壞。</li>
  <li><strong>三維防禦加固方案（7分）</strong>：提出傳輸層 mTLS、時間維度 PTP 500ms 漂移窗口、應用層 Tag 96 數位簽章的立體架構。</li>
  <li><strong>結論（4分）</strong>：總結金融通訊完整性與市場公平性價值。</li>
</ul>
            """
        },

        # 20. sec-essay-68: FinTech Regulatory Sandbox Cybersecurity & Exit Strategy
        {
            "id": "sec-essay-68",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001:2022 與 ISO 27001 LA 稽核實務）",
            "title": "金融科技監理沙盒（Regulatory Sandbox）資安評估要件、隱私保護與退場機制實務",
            "summary": "深入解構《金融科技發展與創新實驗條例》監理沙盒機制、新興技術（AI/區塊鏈/Web3）資安審查六大維度、實驗數據網路實體隔離、資安事件緊急中止條款，以及實驗期滿安全退場機制（Exit Strategy）。",
            "points": 25,
            "rubric": "1. 監理沙盒制度意涵與資安審查六大維度 (7分)；2. 沙盒實驗期機敏資料與網路隔離架構 (7分)；3. 緊急中止閥與安全退場機制 (Exit Strategy) (7分)；4. 結論 (4分)",
            "question": "為鼓勵金融創新，主管機關依據《金融科技發展與創新實驗條例》推動監理沙盒機制。當證券期貨業者申請運用區塊鏈、生成式 AI 或開放 API 進行新型態業務實驗時，資安審查會議重點關注哪些核心評估維度？請詳述沙盒實驗過程中機敏資料之隱私防護與網路隔離要求；規劃資安事件發生時之緊急中止與民事補償機制；並闡述實驗期滿或失敗時之「安全退場機制（Exit Strategy）」包括資料徹底銷毀與系統復原之法規標準。",
            "modelAnswer": """
<h4>一、破題：金融科技監理沙盒之制度使命與資安底線</h4>
<p>依據臺灣《金融科技發展與創新實驗條例》，<strong>金融科技監理沙盒（Regulatory Sandbox）</strong>允許金融業者與科技創新公司在主管機關（金管會）核准之受控環境與特定期間內，豁免部分金融法規之限制，進行新型態金融服務實驗（如代幣化證券 STO、AI 演算法交易顧問、開放證券新興 API）。</p>
<p>然而，「法規豁免不等於資安放水」。創新實驗之核心前提為<strong>「風險可控、投資人權益保障無虞」</strong>。在進入沙盒前，專家審查會議針對資安實施嚴格的<strong>六大核心維度審查</strong>：</p>
<ol>
  <li><strong>系統架構成熟度與彈性</strong>：系統是否具備高可用架構與足夠的抗壓承載力；</li>
  <li><strong>身分認證與授權機制</strong>：是否採用符合 FIDO2 / MFA 之強身分認證；</li>
  <li><strong>機敏資料加密防護</strong>：靜態與傳輸中資料是否具備 AES-256 / TLS 1.3 國際標準加密；</li>
  <li><strong>軟體安全開發與相依性</strong>：第三方開源代碼是否通過嚴格 SCA/SAST 弱點掃描；</li>
  <li><strong>營運持續性與災難復原</strong>：RTO ≤ 10 分鐘、RPO 趨近於 0 之備份機制；</li>
  <li><strong>資安事件應變與補償承諾</strong>：是否配置專屬風險準備金或足額商業資安保險。</li>
</ol>

<h4>二、沙盒實驗期間機敏資料隱私防護與網路實體隔離</h4>
<ul>
  <li><strong>1. 網路實體與邏輯隔離</strong>：沙盒系統必須建置於獨立之 VPC 或實體隔離網段， 嚴禁與交易所正式撮合及帳務內網直連 ；所有跨網呼叫必須經由 API 閘道實施 mTLS 與嚴格限速。；防止實驗性代碼之漏洞成為黑客穿透至實體核心市場的跳板。。</li>
  <li><strong>2. 實驗資料去識別化</strong>：實驗初期 一律使用合成數據（Synthetic Data）或去識別化遮蔽資料 ；若必須使用參與客戶真實資料，強制取得客戶明示之沙盒獨立同意書。；杜絕因創新系統未臻成熟而導致真實投資人個資大面積外洩。。</li>
  <li><strong>3. 業務規模受限閥值</strong>：嚴格限定參與客戶總人數上限（如 1,000 人）與每人最高曝險交易金額（如單筆上限 10 萬元，總曝險不超過 1 億元）。；嚴格錨定潛在損失之最大爆炸半徑，保障系統性金融穩定。。</li>
</ul>

<h4>三、資安事件緊急中止閥與安全退場機制（Exit Strategy）</h4>
<pre><code class="language-text">[沙盒實驗運行] ──> [觸發重大資安事件 / 逾越曝險上限] ──> 【緊急中止閥 (Circuit Breaker)】
                                                               │ 立即停止新業務
                                                               │ 啟動信託賠償基金
                                                               ▼
[實驗終止或期滿] ──> 【安全退場機制 (Exit Strategy)】
                         ├── 客戶權益原路結算與資產返還
                         ├── 依據 NIST SP 800-88 執行機敏資料徹底銷毀 (Sanitization)
                         └── 撤銷所有暫時性連線憑證與網路通道</code></pre>
<ol>
  <li><strong>緊急中止閥機制（Circuit Breaker）</strong>：
    實驗期間一旦發生重大資安事件（如系統遭植入勒索軟體、大量個資外洩、帳務金額嚴重錯帳），<strong>機構必須於 30 分鐘內通報金管會，並於 1 小時內主動觸發緊急中止閥</strong>，系統強制進入唯讀狀態，暫停所有委託，由備妥之信託賠償基金或履約保證金對受損客戶啟動即時全額補償。
  </li>
  <li><strong>安全退場機制（Exit Strategy SOP）</strong>：
    實驗期滿（未獲正式商業執照）或因故提前終止時，必須執行法規嚴格規範之安全退場程序：<br>
    - <strong>客戶資產原路返還</strong>：終止當日按市價結算所有參與者部位，資金全數返還指定銀行帳戶；<br>
    - <strong>資料徹底銷毀（Cryptographic Erasure / Sanitization）</strong>：依據 <strong>NIST SP 800-88 Rev. 1</strong> 媒體清理標準，針對沙盒伺服器硬碟執行磁碟覆寫（Purge）或加密金鑰永久銷毀（Crypto Erase），由獨立資安機構出具「資料銷毀證明書」報備金管會；<br>
    - <strong>網路與權限全數回收</strong>：即時廢止所有沙盒發放之 API 金鑰、X.509 憑證與防火牆臨時放行規則，完成零殘留安全退場。
</li>
</ol>

<h4>四、結論</h4>
<p>監理沙盒是金融創新的孵化器，而資安防禦與健全的退場機制則是其最重要的安全氣囊。透過六大維度事前嚴審、事中網路隔離與數據去識別化，以及事後徹底的資料銷毀退場程序，臺灣證券期貨市場方能在擁抱金融科技創新活力的同時，堅決守護投資大眾的資產安全底線。</p>
            """,
            "examinerTips": "評分亮眼關鍵詞：『監理沙盒核心：法規豁免不等於資安放水，風險可控為唯一前提』、『事前六大資安審查維度』、『事中控制：獨立VPC網路隔離、合成數據/去識別化、人數與曝險金額閥值控制最大爆炸半徑』、『緊急中止閥 (Circuit Breaker)：30分鐘通報 + 1小時強制中止 + 信託補償金』、『安全退場機制 (Exit Strategy)：NIST SP 800-88 資料徹底銷毀 (Sanitization) 出具證明書』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>沙盒制度意涵與六維審查（7分）</strong>：深入辨析創新條例理念，明確提出六大核心資安審查構面。</li>
  <li><strong>事中隔離與防護重點條列（7分）</strong>：以條列逐項剖析網路實體/邏輯隔離、數據合成去識別化與業務規模閥值控制。</li>
  <li><strong>中止閥與安全退場流程（7分）</strong>：繪出流程圖，詳述 Circuit Breaker 觸發條件、信託補償機制與 NIST SP 800-88 媒體銷毀標準。</li>
  <li><strong>結論（4分）</strong>：以「創新孵化器與安全氣囊」生動總結。</li>
</ul>
            """
        }
    ]

def get_20_new_sec_essays():
    return get_20_brand_new_sec_essays() + get_remaining_10_sec_essays()
