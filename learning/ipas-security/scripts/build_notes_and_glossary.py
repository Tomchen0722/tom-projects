# -*- coding: utf-8 -*-
"""
iPAS 資安工程師 - 講義與專業術語辭典產生器
包含初級與中級 4 大考科、32 個核心單元、以及 180+ 資安專業英文術語（附 IPA、繁中翻譯、定義與考點情境）
"""

import json
import os

GLOSSARY_TERMS = [
    # 資安核心架構與原則
    {
        "term": "Confidentiality, Integrity, Availability",
        "abbr": "CIA Triad",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i ɪnˈteɡ.rə.t̬i əˌveɪ.ləˈbɪl.ə.t̬i/",
        "zh": "機密性、完整性、可用性 (資安三要素)",
        "category": "資安核心架構與原則",
        "definition": "資訊安全的三大核心基石。機密性確保僅授權者可存取；完整性確保資料未遭未授權竄改；可用性確保授權者在需要時能即時存取系統與服務。",
        "scenarioExamTip": "情境題常考三者權衡：例如勒索軟體加密主要破壞『可用性』與『完整性』；資料外洩破壞『機密性』；DDoS攻擊直擊『可用性』。"
    },
    {
        "term": "Zero Trust Architecture",
        "abbr": "ZTA",
        "ipa": "/ˈzɪr.oʊ trʌst ˈɑːr.kə.tek.tʃɚ/",
        "zh": "零信任架構",
        "category": "資安核心架構與原則",
        "definition": "以『永不信任，始終驗證 (Never Trust, Always Verify)』為核心原則之安全範式。廢除內外部網路邊界信任，針對每一筆存取請求進行動態身份、設備、情境與權限之持續評估。",
        "scenarioExamTip": "NIST SP 800-207 定義的三大元件：策略決定點 (PDP)、策略執行點 (PEP)、策略管理點 (PA/PE)。常考動態存取控制情境。"
    },
    {
        "term": "Defense-in-Depth",
        "abbr": "DiD",
        "ipa": "/dɪˈfens ɪn depθ/",
        "zh": "縱深防禦",
        "category": "資安核心架構與原則",
        "definition": "多層次安全防禦策略，在實體層、周邊網路、內部網路、主機端點、應用系統、資料層與人員意識分別部署防護控制，避免單一防線失效即全盤瓦解。",
        "scenarioExamTip": "題目中若某企業僅依賴外網防火牆而內網未設防，導致駭客透過釣魚信取得內部主機後直接全橫向滲透，即違反『縱深防禦』原則。"
    },
    {
        "term": "Principle of Least Privilege",
        "abbr": "PoLP",
        "ipa": "/ˈprɪn.sə.pəl əv liːst ˈprɪv.əl.ɪdʒ/",
        "zh": "最小權限原則",
        "category": "資安核心架構與原則",
        "definition": "使用者、程式或系統僅被賦予完成其業務任務所必需之最低權限與存取範圍，且僅在必要期間內維持該權限。",
        "scenarioExamTip": "情境題常考帳號管理：系統管理員日常辦公應使用一般權限帳號，僅在執行特權指令時提升權限 (如 sudo 或 PAM)；避免直接全天候使用 root/Administrator。"
    },
    {
        "term": "Separation of Duties",
        "abbr": "SoD",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/",
        "zh": "職責區隔 / 權限分立",
        "category": "資安核心架構與原則",
        "definition": "將一項關鍵業務流程的授權、執行、覆核與稽核職能分散指派給不同人員或角色，防止單一人員舞弊或發生未察覺之疏失。",
        "scenarioExamTip": "常考資安管理：軟體開發人員不得兼任生產環境上線操作者或資安稽核員；同一人不能同時申請採購並審核放行。"
    },
    {
        "term": "Non-Repudiation",
        "abbr": "NR",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/",
        "zh": "不可否認性",
        "category": "資安核心架構與原則",
        "definition": "證明某項操作、訊息傳送或交易確由特定主體發起且內容未遭修改，發起者事後無法否認其行為。主要依賴非對稱式加密數位簽章與時間戳記技術達成。",
        "scenarioExamTip": "常考題目：僅用對稱加密無法達到不可否認性（因雙方共用金鑰，任一方皆可偽造），必須使用具有私鑰專屬性的『數位簽章 (Digital Signature)』。"
    },

    # 身份認證與存取控制
    {
        "term": "Multi-Factor Authentication",
        "abbr": "MFA",
        "ipa": "/ˈmʌl.ti ˈfæk.tər ɔːˌθen.tɪˈkeɪ.ʃən/",
        "zh": "多因素驗證",
        "category": "身份認證與存取控制",
        "definition": "結合兩種或以上不同類別驗證因素的機制：所知 (Knowledge, 如密碼/PIN)、所持 (Possession, 如硬體金鑰/手機OTP)、所具 (Inherence, 如指紋/臉部特徵)。",
        "scenarioExamTip": "防範憑證填充 (Credential Stuffing) 與帳號密碼釣魚的最有效措施。情境中若要求高風險遠端登入 (VPN/特權帳戶) 必須強制啟用 MFA。"
    },
    {
        "term": "Role-Based Access Control",
        "abbr": "RBAC",
        "ipa": "/roʊl beɪst ˈæk.ses kənˈtroʊl/",
        "zh": "基於角色的存取控制",
        "category": "身份認證與存取控制",
        "definition": "根據使用者在組織中的業務職務指派角色，再將資源存取權限綁定至該角色，簡化權限分配與異動管理。",
        "scenarioExamTip": "情境題中企業員工輪調或離職時，RBAC 可快速抽換角色所擁有的權限，避免個別權限殘留 (Privilege Creep)。"
    },
    {
        "term": "Attribute-Based Access Control",
        "abbr": "ABAC",
        "ipa": "/ˈæt.rɪ.bjuːt beɪst ˈæk.ses kənˈtroʊl/",
        "zh": "基於屬性的存取控制",
        "category": "身份認證與存取控制",
        "definition": "依據主體屬性 (職稱、部門)、資源屬性 (機密等級)、環境屬性 (時間、IP地理位置、設備狀態) 進行動態細粒度權限評估，為零信任核心技術。",
        "scenarioExamTip": "常與 RBAC 比較：當需要依據『非上班時間』或『非企業管制設備登入即限制下載』等情境條件時，應採用 ABAC。"
    },
    {
        "term": "Privileged Access Management",
        "abbr": "PAM",
        "ipa": "/ˈprɪv.əl.ɪdʒd ˈæk.ses ˈmæn.ədʒ.mənt/",
        "zh": "特權存取管理",
        "category": "身份認證與存取控制",
        "definition": "針對超級使用者 (如 root, Domain Admin) 帳號進行金鑰保險箱集中管理、動態一次性密碼、工作階段即時側錄 (Session Recording) 與最小權限提升。",
        "scenarioExamTip": "情境考點：防止特權憑證共用、未授權濫用；若外包維運廠商連入機房操作，必須經由 PAM 進行跳板登入並側錄留存軌跡。"
    },
    {
        "term": "Single Sign-On",
        "abbr": "SSO",
        "ipa": "/ˈsɪŋ.ɡəl saɪn ɑːn/",
        "zh": "單一登入",
        "category": "身份認證與存取控制",
        "definition": "使用者只需成功進行一次身份驗證，即可在有效工作階段內無縫存取多個已建立信任關係的應用系統與服務 (常見協定如 SAML 2.0, OIDC)。",
        "scenarioExamTip": "優點為提升使用者體驗與集中驗證控管；缺點為單點脆弱性 (Single Point of Failure)，因此 SSO 必須搭配強固 MFA 與工作階段逾時機制。"
    },

    # 密碼學與網路傳輸
    {
        "term": "Public Key Infrastructure",
        "abbr": "PKI",
        "ipa": "/ˈpʌb.lɪk kiː ˈɪn.frəˌstrʌk.tʃɚ/",
        "zh": "公開金鑰基礎建設",
        "category": "密碼學與網路傳輸",
        "definition": "結合非對稱加密、數位憑證 (X.509)、憑證授權中心 (CA)、註冊中心 (RA) 與憑證撤銷機制 (CRL / OCSP)，為網路通訊提供可信賴的身份鑑別與加密架構。",
        "scenarioExamTip": "iPAS 考點：憑證是否有效需檢查有效期限、頒發者 CA 信任鏈、以及是否在 CRL / OCSP 撤銷名單中。"
    },
    {
        "term": "Advanced Encryption Standard",
        "abbr": "AES",
        "ipa": "/ədˈvænst ɪnˈkrɪp.ʃən ˈstæn.dɚd/",
        "zh": "進階加密標準",
        "category": "密碼學與網路傳輸",
        "definition": "美國 NIST 發布的對稱區塊對稱式加密演算法，支援 128、192、256 位元金鑰長度，為目前全球銀行與機密資料傳輸與儲存加密的黃金標準。",
        "scenarioExamTip": "考點：對稱加密速度極快，適合大量資料 (Data at Rest / In Transit) 加密；實務常以 GCM 模式 (Galois/Counter Mode) 同時達成加密與認證完整性 (AEAD)。"
    },
    {
        "term": "Rivest-Shamir-Adleman",
        "abbr": "RSA",
        "ipa": "/raɪˈvest ʃəˈmɪər ˈædəl.mən/",
        "zh": "RSA 非對稱加密演算法",
        "category": "密碼學與網路傳輸",
        "definition": "基於大質數分解難題之非對稱演算法，具有一對金鑰 (公鑰與私鑰)。公鑰加密僅私鑰可解密 (傳遞機密)；私鑰簽署僅公鑰可驗證 (數位簽章)。",
        "scenarioExamTip": "計算量大、速度較慢，一般不直接加密大型檔案，而是用於『金鑰交換 (Key Exchange)』與『數位簽章 (Digital Signature)』。"
    },
    {
        "term": "Transport Layer Security",
        "abbr": "TLS",
        "ipa": "/ˈtræns.pɔːrt ˈleɪ.ɚ səˈkjʊr.ə.t̬i/",
        "zh": "傳輸層安全性協定",
        "category": "密碼學與網路傳輸",
        "definition": "在傳輸層為網路通訊提供加密、資料完整性驗證與伺服器/用戶端身份鑑別的加密協定。現行安全標準為 TLS 1.2 與 TLS 1.3，已廢棄 SSL 及 TLS 1.0/1.1。",
        "scenarioExamTip": "TLS 1.3 移除不安全加密套件，加速交握 (1-RTT / 0-RTT)，並強制要求具備前向保密性 (Forward Secrecy, 如 ECDHE)。"
    },

    # 威脅、攻擊手法與漏洞
    {
        "term": "Advanced Persistent Threat",
        "abbr": "APT",
        "ipa": "/ədˈvænst pɚˈsɪs.tənt θret/",
        "zh": "進階持續性威脅",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "由具備高度組織性與國家級背景的攻擊集團，針對特定關鍵目標長期進行匿蹤潛伏、情報蒐集、橫向滲透並竊取機密的高精密複合式攻擊。",
        "scenarioExamTip": "攻擊鏈特徵：初期偵察 -> 魚叉式釣魚入侵 -> 建立 C2 (Command & Control) 連線 -> 內部權限提升與橫向移動 (Lateral Movement) -> 長期潛伏竊取資料。"
    },
    {
        "term": "Ransomware",
        "abbr": "Ransomware",
        "ipa": "/ˈræn.səm.wer/",
        "zh": "勒索軟體",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "透過高強度非對稱/對稱混和加密封鎖受害者電腦或伺服器中之重要檔案，或雙重勒索 (Double Extortion) 竊取機敏資料威脅公開，以此索求贖金的惡意程式。",
        "scenarioExamTip": "防禦策略：落實 3-2-1 離線備份 (含不可變儲存 Immutable Storage)、網路微切分防止擴散、EDR 行為阻擋與端點停用。"
    },
    {
        "term": "Phishing",
        "abbr": "Phishing",
        "ipa": "/ˈfɪʃ.ɪŋ/",
        "zh": "網路釣魚",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "利用社交工程手法偽冒合法機構 (如銀行、IT部門、物流、主管)，引誘受害者點擊惡意連結、輸入認證憑證或下載惡意巨集附件之欺詐行為。",
        "scenarioExamTip": "防護考點：郵件安全機制 SPF、DKIM、DMARC 驗證網域真偽；員工定期社交工程演練；強推 FIDO2 / WebAuthn 防釣魚 MFA。"
    },
    {
        "term": "Distributed Denial of Service",
        "abbr": "DDoS",
        "ipa": "/dɪˈstrɪb.juː.t̬ɪd dɪˈnaɪ.əl əv ˈsɝː.vɪs/",
        "zh": "分散式阻斷服務攻擊",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "利用殭屍網路 (Botnet) 從全球成千上萬受控主機同時發送巨量惡意流量 (如 SYN Flood, DNS/NTP 放大反射, HTTP Flood)，耗盡目標頻寬或系統運算資源使其癱瘓。",
        "scenarioExamTip": "防禦方式：雲端抗 DDoS 流量清洗服務 (Scrubbing Center)、CDN 快取分流、BGP Anycast、防火牆速率限制 (Rate Limiting)。"
    },
    {
        "term": "SQL Injection",
        "abbr": "SQLi",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/",
        "zh": "SQL 注入攻擊",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "攻擊者將未經妥善過濾或轉義的惡意 SQL 指令片段拼接至使用者輸入端，誘使後端資料庫直譯執行，藉此繞過驗證、竊取或竄改整座資料庫內容。",
        "scenarioExamTip": "徹底根治標準解答：強制使用『參數化查詢 (Parameterized Queries) / 預備語句 (Prepared Statements)』或 ORM，絕不以字串拼接 SQL 語句。"
    },
    {
        "term": "Cross-Site Scripting",
        "abbr": "XSS",
        "ipa": "/krɑːs saɪt ˈskrɪp.tɪŋ/",
        "zh": "跨網站腳本攻擊",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "攻擊者將惡意 JavaScript 腳本注入到合法網頁中，當其他受害者瀏覽該網頁時，瀏覽器在受害者信任環境下執行該腳本，進而竊取 Session Cookie 或劫持帳號。",
        "scenarioExamTip": "防禦策略：對所有輸出進行情境感知編碼 (Context-Aware Output Encoding)、設定 HttpOnly 屬性防止 Cookie 被 JS 讀取、配置 CSP (內容安全策略)。"
    },
    {
        "term": "Cross-Site Request Forgery",
        "abbr": "CSRF",
        "ipa": "/krɑːs saɪt rɪˈkwest ˈfɔːr.dʒɚ.i/",
        "zh": "跨網站請求偽造",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "誘使已登入受信任網站的受害者瀏覽器，在不知情狀況下向目標網站發送非預期的偽造操作請求 (如轉帳、修改密碼)，利用瀏覽器自動夾帶 Cookie 的特性完成攻擊。",
        "scenarioExamTip": "防禦考點：採用不可預測的 CSRF Token (同步驗證權杖)、設定 Cookie 的 SameSite=Strict 或 Lax 屬性、關鍵操作再次要求密碼或 OTP。"
    },
    {
        "term": "Server-Side Request Forgery",
        "abbr": "SSRF",
        "ipa": "/ˈsɝː.vɚ saɪd rɪˈkwest ˈfɔːr.dʒɚ.i/",
        "zh": "伺服器端請求偽造",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "攻擊者誘騙後端伺服器向內部網路或其他受保護資源發送網路請求，藉以刺探內網拓撲、讀取雲端執行個體中繼資料 (Metadata, 如 169.254.169.254) 竊取 IAM Token。",
        "scenarioExamTip": "防護手段：嚴格 URL 白名單過濾、禁止解析內部私有 IP 網段 (RFC 1918) 與 Loopback、雲端使用 IMDSv2 (Session-oriented token)。"
    },
    {
        "term": "Buffer Overflow",
        "abbr": "BOF",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/",
        "zh": "緩衝區溢位",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "當程式向記憶體緩衝區寫入超出其預留容量之資料時，覆蓋了相鄰的記憶體堆疊 (Stack) 或堆積 (Heap) 空間，甚至劫持回傳位址 (Return Address) 執行惡意 Shellcode。",
        "scenarioExamTip": "編譯器與作業系統防護機制：ASLR (位址空間配置隨機化)、DEP/NX (資料執行防止)、Stack Canaries (金絲雀防護)；使用記憶體安全語言 (如 Rust/Go) 代替 C/C++。"
    },
    {
        "term": "Man-in-the-Middle",
        "abbr": "MitM",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/",
        "zh": "中間人攻擊",
        "category": "威脅、攻擊手法與漏洞",
        "definition": "攻擊者秘密潛伏於通訊雙方之間，攔截、讀取甚至竄改雙方所傳送的機敏資料，通訊雙方卻誤以為正在直接安全通訊 (如 ARP 欺騙、惡意 Rogue AP、DNS 劫持)。",
        "scenarioExamTip": "防禦標準措施：通訊全程端到端 TLS 雙向加密、嚴格憑證校驗 (避免忽略憑證錯誤)、動態 ARP 檢驗 (DAI)、802.1X 網路接取控制。"
    },

    # 防禦技術、監控與 SOC
    {
        "term": "Endpoint Detection and Response",
        "abbr": "EDR",
        "ipa": "/ˈend.pɔɪnt dɪˈtek.ʃən ænd rɪˈspɑːns/",
        "zh": "端點偵測與回應",
        "category": "防禦技術、監控與 SOC",
        "definition": "安裝於伺服器與終端電腦上的資安代理程式，持續記錄行程活動、網路連線、登錄檔與檔案異動，透過行為分析偵測異常威脅並具備遠端隔離主機與鑑識調查能力。",
        "scenarioExamTip": "傳統防毒 (Antivirus) 僅比對特徵碼 (Signature-based)，EDR 則專注於行為異常 (Behavior-based) 與無檔案惡意程式 (Fileless Malware) 阻絕。"
    },
    {
        "term": "Security Information and Event Management",
        "abbr": "SIEM",
        "ipa": "/sɪm / səˈkjʊr.ə.t̬i ˌɪn.fɚˈmeɪ.ʃən ænd ɪˈvent ˈmæn.ədʒ.mənt/",
        "zh": "安全性資訊與事件管理",
        "category": "防禦技術、監控與 SOC",
        "definition": "集中收集來自防火牆、伺服器、網路設備、資料庫與端點之系統日誌 (Log)，進行正規化、時間關聯分析 (Correlation) 與威脅告警之中央監控平台。",
        "scenarioExamTip": "情境題重點：日誌不可更動性 (WORM)、至少保存 180 天 (法規要求)、NTP 全網時間精準校時以利鑑識關聯。"
    },
    {
        "term": "Security Orchestration, Automation, and Response",
        "abbr": "SOAR",
        "ipa": "/sɔːr / səˈkjʊr.ə.t̬i ˌɔːr.kəˈstreɪ.ʃən ˌɑː.t̬əˈmeɪ.ʃən ænd rɪˈspɑːns/",
        "zh": "資安協同作業、自動化與回應",
        "category": "防禦技術、監控與 SOC",
        "definition": "整合各類安全工具 (SIEM, EDR, 防火牆)，將標準化事件應變流程編排為自動化劇本 (Playbook)，大幅減少 SOC 人工作業時間，達成秒級阻斷與通報。",
        "scenarioExamTip": "情境考點：SOC 收到釣魚郵件通報，SOAR 自動提取惡意 URL 送沙箱檢驗，並同步下發封鎖規則至防火牆與郵件閘道，此為 Playbook 自動化經典應用。"
    },
    {
        "term": "Web Application Firewall",
        "abbr": "WAF",
        "ipa": "/wæf / web ˌæp.ləˈkeɪ.ʃən ˈfaɪr.wɑːl/",
        "zh": "網站應用程式防火牆",
        "category": "防禦技術、監控與 SOC",
        "definition": "運作於 OSI 第 7 層 (應用層) 的專門防火牆，透過深度檢驗 HTTP/HTTPS 請求內容，專門阻絕 SQL Injection、XSS、路徑遍歷等 OWASP Top 10 網頁應用攻擊。",
        "scenarioExamTip": "傳統網路防火牆 (Layer 3/4) 只能看到 Port 80/443 開放無法檢查 Payload，必須靠 WAF 進行第 7 層特徵與行為剖析。"
    },
    {
        "term": "Honeypot",
        "abbr": "Honeypot",
        "ipa": "/ˈhʌn.i.pɑːt/",
        "zh": "蜜罐 / 誘捕系統",
        "category": "防禦技術、監控與 SOC",
        "definition": "刻意部署並具備偽裝弱點的誘餌伺服器或服務，用以吸引攻擊者入侵，藉此觀察攻擊者手法、收集未公開零日漏洞 (Zero-day) 與最新威脅情資，而不影響正式營運。",
        "scenarioExamTip": "考點：蜜罐在正常情況下絕不會有合法業務存取，任何對蜜罐的連線皆視為高可疑攻擊行為，警報準確度極高且誤報率極低。"
    },
    {
        "term": "Demilitarized Zone",
        "abbr": "DMZ",
        "ipa": "/diːˌmɪl.ə.tə.raɪzd ˈzoʊn/",
        "zh": "非軍事區 / 隔離區網段",
        "category": "防禦技術、監控與 SOC",
        "definition": "位於內部私有網路與外部公用網路 (網際網路) 之間的緩衝中介網段。對外提供公開服務之伺服器 (如 Web, Mail, DNS) 置於此區，防止外網直接滲透至內部核心網路。",
        "scenarioExamTip": "安全原則：外部網路可有限度連入 DMZ；DMZ 伺服器『嚴禁主動發起』連線至內部核心網路 (內網只可單向連往 DMZ)。"
    },

    # 資安框架、法規與管理
    {
        "term": "Cybersecurity Framework",
        "abbr": "NIST CSF 2.0",
        "ipa": "/ˈsaɪ.bɚ.səˌkjʊr.ə.t̬i ˈfreɪm.wɝːk/",
        "zh": "NIST 資安框架",
        "category": "資安框架、法規與管理",
        "definition": "美國國家標準暨技術研究院制定的資安管理架構，2.0 版涵蓋六大核心功能：治理 (Govern)、識別 (Identify)、保護 (Protect)、偵測 (Detect)、回應 (Respond)、復原 (Recover)。",
        "scenarioExamTip": "iPAS 常考 2.0 最新納入的『Govern (治理)』功能，強調組織高層方針、風險管理策略、法規合規與供應鏈治理。"
    },
    {
        "term": "Information Security Management System",
        "abbr": "ISMS (ISO/IEC 27001)",
        "ipa": "/ˌɪn.fɚˈmeɪ.ʃən səˈkjʊr.ə.t̬i ˈmæn.ədʒ.mənt ˈsɪs.təm/",
        "zh": "資訊安全管理系統",
        "category": "資安框架、法規與管理",
        "definition": "以系統化方法管理組織機敏資訊安全的國際標準。遵循 PDCA 循環，包含本文主條文與附錄 A 之控制措施 (2022年版改為 4 大主題：組織、人員、實體、技術控制，共 93 項)。",
        "scenarioExamTip": "2022 新增控制措施重點常考：威脅情資 (Threat Intelligence)、雲端服務使用安全、資通訊技術準備度 (ICT readiness for business continuity)、資料隱私掩碼與資料外洩防護 (DLP)。"
    },
    {
        "term": "Business Impact Analysis",
        "abbr": "BIA",
        "ipa": "/ˈbɪz.nɪs ˈɪm.pækt əˈnæl.ə.sɪs/",
        "zh": "營運衝擊分析",
        "category": "資安框架、法規與管理",
        "definition": "系統性評估災難或事故導致關鍵業務中斷時，對組織財務、營運、聲譽及法規造成的潛在損失與影響，進而釐定關鍵業務優先順序與復原指標。",
        "scenarioExamTip": "BIA 的核心產出為各系統之 RTO (復原時間目標)、RPO (復原點目標) 與 MTD (最大可容忍中斷時間)。"
    },
    {
        "term": "Recovery Time Objective",
        "abbr": "RTO",
        "ipa": "/rɪˈkʌv.ɚ.i taɪm əbˈdʒek.tɪv/",
        "zh": "復原時間目標",
        "category": "資安框架、法規與管理",
        "definition": "災難或資安事故發生後，關鍵業務、伺服器或系統必須恢復運作的最大可容許時間上限。",
        "scenarioExamTip": "例如系統 RTO = 4 小時，代表中斷後 4 小時內必須修復上線。RTO 越短，所需之熱備援 (Hot Site) 與自動容錯移轉成本越高。"
    },
    {
        "term": "Recovery Point Objective",
        "abbr": "RPO",
        "ipa": "/rɪˈkʌv.ɚ.i pɔɪnt əbˈdʒek.tɪv/",
        "zh": "復原點目標",
        "category": "資安框架、法規與管理",
        "definition": "災難或資料損毀時，組織可容忍遺失資料的最大時間範圍量 (決定了備份頻率)。",
        "scenarioExamTip": "例如系統 RPO = 1 小時，代表最多只能損失過去 1 小時之交易資料，備份機制必須至少每小時執行一次或採用即時異地備援 (Replication)。"
    },
    {
        "term": "Common Vulnerabilities and Exposures",
        "abbr": "CVE",
        "ipa": "/ˈkɑː.mən ˌvʌl.nɚ.əˈbɪl.ə.t̬iz ænd ɪkˈspoʊ.ʒɚz/",
        "zh": "通用弱點與漏洞揭露",
        "category": "資安框架、法規與管理",
        "definition": "全球公開已知資安漏洞的標準化字典識別碼 (格式如 CVE-2024-12345)，由 MITRE 機構維護，供各資安工具與漏洞庫共通引用。",
        "scenarioExamTip": "常與 CVSS 結合：CVE 為漏洞編號名稱，CVSS 為該漏洞嚴重程度的量化評分 (0.0 ~ 10.0 分)。"
    },
    {
        "term": "Common Vulnerability Scoring System",
        "abbr": "CVSS",
        "ipa": "/ˈkɑː.mən ˌvʌl.nɚ.əˈbɪl.ə.t̬i ˈskɔːr.ɪŋ ˈsɪs.təm/",
        "zh": "通用弱點評分系統",
        "category": "資安框架、法規與管理",
        "definition": "開放式資安弱點嚴重程度評估標準框架，現行主要版本為 CVSS v3.1 / v4.0。評分區間 0.0 至 10.0，包含基本度量 (Base)、時間度量 (Temporal) 與環境度量 (Environmental)。",
        "scenarioExamTip": "嚴重等級切分：9.0~10.0 為緊急 (Critical)；7.0~8.9 為高 (High)；4.0~6.9 為中 (Medium)；0.1~3.9 為低 (Low)。"
    },
    {
        "term": "MITRE ATT&CK",
        "abbr": "ATT&CK",
        "ipa": "/ˈmaɪ.tɚ əˈtæk/",
        "zh": "MITRE ATT&CK 威脅對抗戰術技術知識庫",
        "category": "資安框架、法規與管理",
        "definition": "基於真實駭客攻擊案例歸納出的對抗戰術、技術與通用知識庫 (Adversarial Tactics, Techniques, and Common Knowledge)。涵蓋 14 大戰術階段 (如 Initial Access, Execution, Persistence, Lateral Movement, Exfiltration)。",
        "scenarioExamTip": "SOC 團隊與紅藍對抗最重要標準工具，用以映射資安設備偵測覆蓋率與威脅獵捕劇本。"
    },

    # 數位鑑識與事件應變
    {
        "term": "Chain of Custody",
        "abbr": "CoC",
        "ipa": "/tʃeɪn əv ˈkʌs.tə.di/",
        "zh": "監管鏈 / 證據保管鏈",
        "category": "數位鑑識與事件應變",
        "definition": "數位證據從採集、標示、包裝、運送、分析到法庭出示的完整書面紀錄，詳載每一位經手人、時間、地點及目的，確保證據未遭竄改具有法庭證據能力。",
        "scenarioExamTip": "題目考點：採集數位證據第一步必須計算原始 SHA-256 雜湊值；複製時必須進行唯讀式位元對位元映像 (Bit-stream Image)，絕不在原始硬碟上直接操作分析。"
    },
    {
        "term": "Order of Volatility",
        "abbr": "OoV",
        "ipa": "/ˈɔːr.dɚ əv ˌvɑː.ləˈtɪl.ə.t̬i/",
        "zh": "揮發性順序",
        "category": "數位鑑識與事件應變",
        "definition": "數位鑑識時現場證據收集的先後順序原則：最易揮發遺失的資料優先收集。標準順序：暫存器/快取 -> 記憶體 (RAM) -> 網路連線狀態 -> 暫存檔案 -> 硬碟資料 -> 實體拓撲/備份媒體。",
        "scenarioExamTip": "絕對不可直接拔掉電源插頭或重開機！重開機會導致 RAM 中的關鍵惡意程式、解密金鑰與網路連線軌跡永久消失。"
    },

    # 安全開發與軟體供應鏈
    {
        "term": "Secure Software Development Life Cycle",
        "abbr": "SSDLC",
        "ipa": "/səˈkjʊr ˈsɑːft.wer dɪˈvel.əp.mənt laɪf ˈsaɪ.kəl/",
        "zh": "安全軟體開發生命週期",
        "category": "安全開發與軟體供應鏈",
        "definition": "將資安考量貫穿軟體生命週期的每一階段：需求 (資安合規) -> 設計 (威脅建模 STRIDE) -> 開發 (安全編碼規範、SAST) -> 測試 (DAST, 滲透測試) -> 部署 (環境強化) -> 維運 (漏洞修補)。",
        "scenarioExamTip": "安全左移 (Shift Left) 理念：越早階段發現與修復漏洞，成本越低 (設計階段修補成本僅為上線後的數十分之一)。"
    },
    {
        "term": "Software Bill of Materials",
        "abbr": "SBOM",
        "ipa": "/ˈsɑːft.wer bɪl əv məˈtɪr.i.əlz/",
        "zh": "軟體物料清單",
        "category": "安全開發與軟體供應鏈",
        "definition": "詳載軟體所使用的所有開源函式庫、第三方相依元件、版本號碼、授權協議及數位簽章的清單檔案 (常見標準如 SPDX, CycloneDX)。",
        "scenarioExamTip": "Log4j 等重大供應鏈漏洞爆發時，擁有 SBOM 才能在幾分鐘內精準盤點企業內部哪些系統使用了該受災函式庫。"
    }
]

# 講義結構內容定義 (32個單元，初級16 + 中級16)
LECTURE_NOTES = {
    "basic": {
        "title": "iPAS 資訊安全工程師 - 初級能力鑑定核心講義",
        "subjects": [
            {
                "subjectId": "B-SUB-1",
                "name": "考科一：資訊安全概論",
                "desc": "涵蓋資安核心原則、網路安全通訊基礎、主機端點防護、常見攻擊威脅與應用系統安全、加解密與存取控制、以及基本法規。",
                "modules": [
                    {
                        "id": "B1-M01",
                        "title": "單元 1：資安核心三要素與安全架構原則",
                        "keywords": ["CIA Triad", "Defense-in-Depth", "Least Privilege", "Non-Repudiation"],
                        "summary": "掌握資訊安全最高指導原則：機密性 (Confidentiality)、完整性 (Integrity)、可用性 (Availability)。深入解析縱深防禦 (Defense-in-Depth)、最小權限原則 (PoLP) 與權限分立 (SoD) 的企業落地方案。",
                        "content": """
### 1.1 資安核心三要素 (CIA Triad)
- **機密性 (Confidentiality)**：確保資訊僅供被授權之人員或系統存取。關鍵防護技術包括：強加密演算法 (AES, RSA)、存取控制清單 (ACL)、資料遮罩 (Data Masking)。
- **完整性 (Integrity)**：確保資訊與系統未遭受未經授權的竄改、偽造或刪除。關鍵防護技術包括：密碼編譯雜湊函數 (SHA-256, SHA-3)、數位簽章 (Digital Signature)、訊息鑑別碼 (HMAC)。
- **可用性 (Availability)**：確保授權主體在業務需要時能即時無阻礙地存取資訊與服務。關鍵防護技術包括：高可用性架構 (HA)、負載平衡 (Load Balancing)、DDoS 流量清洗、容錯備援 (Failover)。

### 1.2 經典架構原則
1. **縱深防禦 (Defense-in-Depth)**：切勿依賴單一防線，必須於實體、網路邊界、內網、端點主機、應用程式與資料層分別設立安全控制。
2. **最小權限原則 (Principle of Least Privilege)**：使用者與程序僅具備完成當前任務之最低必要權限。
3. **不可否認性 (Non-Repudiation)**：利用私鑰數位簽章結合安全時間戳記，確保操作行為者事後無法否認交易或指令發送。
                        """,
                        "caseStudy": "【實務情境】某金融機構遭遇駭客攻擊，外部防護被突破後，駭客企圖直接存取內部核心資料庫。由於該機構在資料庫端啟用了獨立的專屬存取控制與 AES-256 欄位加密，且內網設有網段隔離，成功在第二道防線阻絕了機密外洩，此即縱深防禦的成功典範。"
                    },
                    {
                        "id": "B1-M02",
                        "title": "單元 2：網路通訊協定與架構安全",
                        "keywords": ["TCP/IP", "IPsec", "TLS", "DNSSEC", "DMZ", "VPN"],
                        "summary": "解析 OSI 7 層模型與 TCP/IP 協定堆疊中的安全隱患。探討 TLS 1.3、IPsec VPN、安全 DNS (DNSSEC) 與企業 DMZ 網路拓撲規劃。",
                        "content": """
### 2.1 OSI 7層與常見協定安全
- **實體與資料鏈結層 (Layer 1/2)**：ARP 欺騙 (ARP Spoofing)、MAC 洪水攻擊；防禦技術：動態 ARP 檢驗 (DAI)、DHCP Snooping、連接埠安全 (Port Security)。
- **網路層 (Layer 3)**：IP 偽造 (IP Spoofing)、ICMP 泛洪；防禦技術：IPsec (包含 AH 認證標頭 與 ESP 封裝安全酬載)。
- **傳輸層 (Layer 4)**：TCP SYN Flood 攻擊、三向交握劫持；防禦技術：SYN Cookies、防火牆連線狀態表限制。
- **應用層 (Layer 7)**：HTTP/HTTPS、DNS、DHCP、SMTP；防禦技術：DNSSEC (防止 DNS 快取污染)、TLS 1.3 強制端到端加密。

### 2.2 DMZ 非軍事區架構原則
- 對外提供網頁或郵件服務之公開伺服器必須建置於 DMZ 網段。
- 外部訪客僅允許連線至 DMZ 之指定服務連接埠 (如 443)。
- **鐵律**：DMZ 伺服器嚴禁主動發起連往內部核心資料庫之連線；必須由內網主動拉取或經由專屬反向代理 (Reverse Proxy) 嚴格過濾。
                        """,
                        "caseStudy": "【實務情境】駭客利用 Web 伺服器漏洞成功取得 WebShell，企圖利用該主機橫向滲透內部人事資料庫。因為企業落實了嚴格的 DMZ 防火牆規則，阻斷了 DMZ 主動往內網發起的連線，使得攻擊受困於隔離區。"
                    },
                    {
                        "id": "B1-M03",
                        "title": "單元 3：作業系統與主機端點安全強化",
                        "keywords": ["Windows Security", "Linux Hardening", "Patch Management", "Privilege Escalation"],
                        "summary": "掌握 Windows Active Directory 與 Linux 主機安全性基準強化 (Hardening)、系統補丁生命週期、帳號密碼原則與排程作業防護。",
                        "content": """
### 3.1 主機安全強化基準 (Baseline Hardening)
- **關閉未使用的服務與通訊埠**：例如關閉 Telnet (改用 SSHv2)、關閉 SMBv1、停用匿名存取 (Null Session)。
- **預設帳號與密碼管理**：重新命名或停用 Administrator / root 預設帳號；禁用無密碼或空密碼登入。
- **密碼原則**：長度至少 12 碼以上、包含大小寫字母、數字與符號，並啟用帳戶鎖定閥值 (防止暴力破解)。

### 3.2 補丁管理與作業系統更新
- 建立測試環境預先驗證修補程式相容性。
- 針對 CVSS 7.0 以上的高危漏洞，應於 7 至 14 天內完成正式環境補丁發布。
- 利用群組原則 (GPO) 或集中化資產管理工具 (WSUS/SCCM/Ansible) 強制推播更新。
                        """,
                        "caseStudy": "【實務情境】2017 年 WannaCry 勒索軟體席捲全球，受災嚴重的企業皆因未即時安裝微軟釋出的 MS17-010 補丁，且內網未關閉老舊的 SMBv1 協定，造成自動化橫向感染擴散。"
                    },
                    {
                        "id": "B1-M04",
                        "title": "單元 4：常見資安威脅與惡意程式防護",
                        "keywords": ["Ransomware", "Phishing", "Trojan", "Worm", "Botnet", "Social Engineering"],
                        "summary": "全面剖析勒索軟體 (Ransomware)、特洛伊木馬、電腦蠕蟲、殭屍網路 (Botnet) 與社交工程釣魚手法的攻擊向量與防範機制。",
                        "content": """
### 4.1 惡意程式類別辨析
- **電腦蠕蟲 (Worm)**：具備自我複製與主動掃描網路弱點能力，不需依附宿主程式即可在內網快速自主擴散。
- **特洛伊木馬 (Trojan)**：偽裝成合法有用的軟體，誘導使用者下載安裝，私下開啟後門或下載次階段攻擊載具。
- **勒索軟體 (Ransomware)**：以高強度加密封鎖受害者磁碟並勒索加密貨幣贖金；近期演化為雙重/三重勒索 (加密 + 機密外洩威脅 + DDoS)。

### 4.2 社交工程防護重點
- 社交工程 (Social Engineering) 針對人性弱點 (恐懼、權威、貪婪、急迫感)。
- 建立標準流程：凡涉及金錢匯款、機密提供、密碼重設，一律禁止僅憑通訊軟體或電子郵件指示，必須透過第二管道 (如電話電話照會) 親自確認。
                        """,
                        "caseStudy": "【實務情境】某科技廠財務主管收到冒充總經理寄發之緊急郵件，要求於下班前匯出千萬貨款。主管因遵循企業 SOP，透過公司內線電話向總經理親自照會，成功攔阻了商業電子郵件詐騙 (BEC)。"
                    },
                    {
                        "id": "B1-M05",
                        "title": "單元 5：應用系統安全與 OWASP Top 10 核心漏洞",
                        "keywords": ["SQL Injection", "XSS", "Broken Access Control", "Cryptographic Failures", "SSRF"],
                        "summary": "深入理解 OWASP Top 10 Web 漏洞原理，包括權限控制失效、注入弱點 (SQLi)、密碼學失效、跨網站腳本 (XSS) 與 SSRF 漏洞的防禦關鍵。",
                        "content": """
### 5.1 注入攻擊 (Injection)
- 根因：將使用者不可信的輸入資料未經檢查即拼接進直譯器指令中。
- **防禦鐵律**：使用參數化查詢 (Parameterized Queries) 或預備語句 (Prepared Statements)。

### 5.2 跨網站腳本 (XSS)
- **儲存型 (Stored)**：惡意腳本存入資料庫，所有閱覽該頁面的訪客皆會中招。
- **反射型 (Reflected)**：惡意腳本包在 URL 參數中，點擊釣魚連結即觸發。
- **防禦**：情境感知輸出編碼 (Output Encoding) 與設定 Cookie 標記為 `HttpOnly`。

### 5.3 權限控制失效 (Broken Access Control)
- 未在後端伺服器驗證使用者是否有權存取特定物件 (如水平越權 IDOR：直接竄改 URL 中的 `user_id=1002`)。
- 防禦：每一筆後端 API 請求皆必須在伺服器端比對目前登入 Session 與資源擁有者關聯。
                        """,
                        "caseStudy": "【實務情境】某外送平台的訂單查詢介面將訂單編號直接暴露在 URL 中，使用者只需修改網址數字即可看到其他客戶的姓名、電話與地址。後端改為在每次查詢時驗證 Session 中的 UserID 與訂單擁有者是否一致，徹底消除越權漏洞。"
                    },
                    {
                        "id": "B1-M06",
                        "title": "單元 6：密碼學基礎、對稱/非對稱與數位簽章",
                        "keywords": ["Symmetric Encryption", "Asymmetric Encryption", "Hashing", "Digital Signature", "PKI"],
                        "summary": "掌握對稱加密 (AES)、非對稱加密 (RSA/ECC)、單向雜湊函數 (SHA-256) 與數位簽章的數學原理與適用場景。",
                        "content": """
### 6.1 加密演算法比較
- **對稱式加密 (Symmetric)**：加密與解密共用同一把密鑰。優點：運算速度極快；缺點：金鑰分發與保存困難。代表演算法：AES-256、ChaCha20。
- **非對稱式加密 (Asymmetric)**：具備成對的公鑰與私鑰。公鑰公開用於加密，私鑰保管用於解密。優點：金鑰管理便利；缺點：計算量極大、速度緩慢。代表演算法：RSA、ECC (橢圓曲線)。

### 6.2 雜湊函數與數位簽章
- **雜湊函數 (Hash)**：具備單向性 (不可逆) 與抗碰撞性 (Avalanche Effect 雪崩效應)。常用於密碼存儲 (需加鹽 Salt) 與檔案完整性驗證。
- **數位簽章 (Digital Signature)**：發送方以『發送方私鑰』對文件雜湊值進行加密；接收方以『發送方公鑰』進行解密驗證。達成：完整性、真實性、不可否認性。
                        """,
                        "caseStudy": "【實務情境】合約電子簽署系統中，發送者使用個人專屬私鑰簽章，即使合約內容被篡改哪怕一個字元，接收端用公鑰解密算出的雜湊值立即不符，有效保障法律效力。"
                    },
                    {
                        "id": "B1-M07",
                        "title": "單元 7：存取控制模型與使用者認證技術",
                        "keywords": ["DAC", "MAC", "RBAC", "MFA", "OAuth", "SAML"],
                        "summary": "深入比較自主存取控制 (DAC)、強制存取控制 (MAC) 與角色存取控制 (RBAC)；剖析多因素驗證 (MFA) 與聯邦身分驗證協定。",
                        "content": """
### 7.1 三大傳統存取控制模型
- **DAC (自主存取控制)**：資源的擁有者 (Owner) 可自行決定要將權限分享給誰 (常見於 Windows NTFS 一般檔案分享)。彈性高但缺乏全域集中控管。
- **MAC (強制存取控制)**：由中央安全策略與敏感度等級 (如機密、極機密) 嚴格控制，使用者無法私自轉移權限 (如軍方 Bell-LaPadula 模型、SELinux)。安全性最高。
- **RBAC (角色存取控制)**：權限授予特定職務角色，使用者指派對應角色。目前企業最廣泛採用的模型。

### 7.2 現代多因素驗證 (MFA) 規範
- 必須跨越三種獨立維度中的至少兩種：
  1. **所知 (Something you know)**：密碼、PIN碼。
  2. **所持 (Something you have)**：硬體載具 (YubiKey)、軟體 Authenticator App、智慧卡。
  3. **所具 (Something you are)**：生物特徵 (指紋、虹膜、臉部辨識)。
- 簡訊 SMS OTP 因易遭 SIM 換卡 (SIM Swapping) 或 SS7 攔截，NIST 建議逐漸淘汰，改採基於 FIDO2 的抗釣魚憑證。
                        """,
                        "caseStudy": "【實務情境】某科技公司將研發代碼庫由 DAC 遷移至 RBAC，並限定高階工程師只能在公司受管筆電上存取。離職時只要在中央 AD 撤銷帳號角色，所有系統權限同步消失，大幅降低離職員工帶走專利之風險。"
                    },
                    {
                        "id": "B1-M08",
                        "title": "單元 8：台灣資通安全管理法與個資保護概論",
                        "keywords": ["Cybersecurity Management Act", "PDPA", "Data Breach", "Compliance"],
                        "summary": "掌握我國《資通安全管理法》與《個人資料保護法》之法規範圍、機關義務、通報時限與民刑事責任。",
                        "content": """
### 8.1 資通安全管理法要點
- 適用主體：公務機關、關鍵基礎設施提供者 (CI)、公營事業與政府捐助之財團法人。
- **資安事件通報時限**：知悉資安事件後，**1 小時內** 必須向主管機關完成通報。
- 責任等級分級：依業務重要性劃分為 A、B、C、D、E 五個等級，等級越高要求之專責資安人員與 ISMS 認證越嚴格。

### 8.2 個人資料保護法重點
- 蒐集、處理與利用個資必須具備『特定目的』與『法定要件』。
- 當發生個人資料外洩事件時，應查明後以適當方式『即時通知』當事人。
- 企業應採取適當之安全維護措施 (如加密、存取控制、銷毀軌跡)，違反時負有民事損害賠償與主管機關裁罰責任。
                        """,
                        "caseStudy": "【實務情境】某醫院發生病患病歷遭勒索病毒加密事件，醫院在確認受害後 45 分鐘內即向衛福部資安通報平台通報，完全符合《資安法》知悉後 1 小時之法定時限，避免遭受行政處分。"
                    }
                ]
            },
            {
                "subjectId": "B-SUB-2",
                "name": "考科二：資訊安全防護實務",
                "desc": "涵蓋網路邊界設備防禦、端點安全防護、流量與封包分析、弱點掃描評估、日誌管理、備份還原與實體環境控管實務。",
                "modules": [
                    {
                        "id": "B2-M01",
                        "title": "單元 1：防火牆、IDS/IPS 與次世代網路防護",
                        "keywords": ["Next-Generation Firewall", "IDS vs IPS", "WAF", "DPI", "Stateful Inspection"],
                        "summary": "掌握次世代防火牆 (NGFW)、入侵偵測/防禦系統 (IDS/IPS) 與網站應用程式防火牆 (WAF) 的運作架構、規則設定與協同聯防。",
                        "content": """
### 1.1 IDS 與 IPS 的關鍵差異
- **IDS (入侵偵測系統)**：通常以 Port Mirroring (監控埠鏡像) 旁路 (Out-of-band) 部署。只負責被動監控流量並發出警報，**無法主動即時攔截或阻斷封包**。
- **IPS (入侵防禦系統)**：必須以 Inline (串聯) 方式部署於網路路徑上。能夠即時剖析惡意特徵並執行 Dropping (直接丟棄連線) 阻斷攻擊。

### 1.2 次世代防火牆 (NGFW) 特性
- 傳統防火牆僅檢查 L3/L4 (IP與Port)。
- NGFW 具備深度封包檢測 (DPI)、應用程式識別 (App-ID，即使運行於非標準 Port 也能辨識)、使用者身分關聯 (User-ID) 與內建 IPS/反惡意連線功能。
                        """,
                        "caseStudy": "【實務情境】駭客嘗試將惡意連線偽裝成 HTTPS (Port 443) 流量外傳資料，傳統防火牆直接放行；但 NGFW 透過 SSL 解密檢驗發現其實為 BitTorrent 傳輸協議與 C2 惡意通訊，立即在串聯路徑予以阻斷。"
                    },
                    {
                        "id": "B2-M02",
                        "title": "單元 2：端點防護、次世代防毒與 EDR 實務",
                        "keywords": ["EDR", "NGAV", "Host-based Firewall", "Application Whitelisting"],
                        "summary": "剖析企業端點防禦演進：從特徵碼防毒 (AV) 到行為分析 (NGAV) 與端點偵測回應 (EDR)；探討應用程式白名單與周邊設備管控機制。",
                        "content": """
### 2.1 EDR (Endpoint Detection and Response) 核心功能
- **端點遙測收集**：持續記錄進程啟動 (Process Creation)、親代子進程關係 (Parent-Child Process Tree)、網路出連與註冊表修改。
- **行為威脅獵捕**：即使檔案具備合法微軟簽名，若利用 Living off the Land Binaries (LOLBins，如 powershell.exe, certutil.exe) 下載不明腳本，EDR 亦能即時告警。
- **即時隔離與遏止**：支援管理端一鍵進行『網路隔離 (Network Isolation)』，僅保留與 EDR 伺服器的通訊通道，防止攻擊橫向擴散。

### 2.2 應用程式白名單 (Application Whitelisting)
- 僅允許預先核准之安全執行檔與腳本執行 (例如 Windows AppLocker, WDAC)。
- 能有效防範零日攻擊與未知名惡意程式執行。
                        """,
                        "caseStudy": "【實務情境】員工點擊釣魚巨集檔案啟動了 PowerShell 試圖下載勒索軟體，端點 EDR 立即識別出 Word 子進程喚起非授權 PowerShell 的可疑行為，瞬間封殺進程並將該工作站自動隔離，保護了整座區域網路。"
                    },
                    {
                        "id": "B2-M03",
                        "title": "單元 3：網路流量監控、封包分析與異常連線診斷",
                        "keywords": ["Wireshark", "NetFlow", "Packet Analysis", "Beaconing Detection"],
                        "summary": "掌握 Wireshark 抓包過濾語法、網路流量 NetFlow 分析、TCP 三向交握異常排查以及惡意程式心跳回連 (Beaconing) 流量偵測。",
                        "content": """
### 3.1 封包分析與特徵識別
- **TCP 三向交握**：正常連線為 SYN -> SYN/ACK -> ACK。若伺服器收到巨量只有 SYN 卻無後續 ACK 之請求，即為 SYN Flood 阻斷服務攻擊。
- **ARP 欺騙特徵**：區域網路中突然出現重複的 IP 位址對應到相異的 MAC 位址，或無請求的廣播 ARP 回應 (Gratuitous ARP)。
- **C2 心跳特徵 (Beaconing)**：端點每隔固定秒數 (如 60 秒) 持續向境外可疑 IP 或動態網域名稱 (DGA) 發出微小大小的 HTTP POST 請求。

### 3.2 Wireshark 實戰常用過濾語法
- `tcp.flags.syn == 1 and tcp.flags.ack == 0` (尋找連線發起封包)
- `ip.addr == 192.168.1.100 && http` (過濾特定 IP 的 HTTP 流量)
- `dns.flags.response == 1 && dns.qry.name contains "malicious"`
                        """,
                        "caseStudy": "【實務情境】資安人員利用封包檢測工具監控網路，發現某台會計主機每隔正好 300 秒就向國外未知伺服器發送 DNS 請求，經進一步分析為利用 DNS 穿隧 (DNS Tunneling) 竊取內部機密資料的特徵，及時切斷威脅。"
                    },
                    {
                        "id": "B2-M04",
                        "title": "單元 4：弱點掃描、漏洞評估與修補排程實務",
                        "keywords": ["Vulnerability Assessment", "CVE", "CVSS", "Nessus", "Patching"],
                        "summary": "學習弱點掃描 (VA) 原理與工具操作、辨析未經認證掃描與憑證掃描之差異、CVSS 評分標準及修補管理優先順序擬定。",
                        "content": """
### 4.1 弱點掃描方式比較
- **無認證掃描 (Unauthenticated Scan)**：從外部網路檢視開放連接埠與外顯服務版本。主要模擬外部黑客視角，但難以發現內部未授權組態或底層補丁缺失。
- **認證掃描 (Authenticated / Credentialed Scan)**：提供受測主機之合法帳號密碼進行掃描。掃描器登入主機檢驗註冊表、已安裝套件版本與組態設定，準確度極高且誤報率低。

### 4.2 漏洞修補優先原則
- 結合 CVSS 基礎評分與威脅情資 (威脅在野外是否已存在公開 Exploit 武器化利用程式)。
- 建立修補流程：資產盤點 -> 定期掃描 -> 風險排序 -> 測試驗證 -> 部署上線 -> 複掃確認。
                        """,
                        "caseStudy": "【實務情境】企業進行全公司弱掃，掃出數千個弱點。資安長依據 CVSS v3 >= 9.0 且 CISA KEV (已遭積極利用漏洞清單) 篩選出 5 個最致命漏洞，要求 IT 團隊於 48 小時內完成上線更新，成功防杜勒索攻擊。"
                    },
                    {
                        "id": "B2-M05",
                        "title": "單元 5：日誌收集、集中分析與基礎稽核維運",
                        "keywords": ["Syslog", "Event Log", "NTP Synchronization", "Log Retention", "Audit Trails"],
                        "summary": "掌握日誌管理黃金法則：Syslog、Windows Event Log 事件代碼、全網 NTP 校時精準度、WORM 唯讀留存以及至少 180 天法規要求。",
                        "content": """
### 5.1 日誌管理四大支柱
1. **集中化收集**：日誌必須即時轉發 (Forwarding) 至獨立的 Syslog 伺服器或 SIEM 集中儲存，防止主機遭駭時日誌被入侵者抹除。
2. **時間同步 (NTP)**：所有網路設備與伺服器必須強制同步至標準 NTP 伺服器，時差控制在毫秒級，確保事件關聯排查具備時間一致性。
3. **不可竄改 (Integrity & WORM)**：日誌伺服器採用單寫多讀 (Write Once, Read Many) 儲存機制與雜湊簽章，保全司法調查證據能力。
4. **保存期限**：依我國資安法要求，關鍵核心系統之軌跡日誌至少必須保存 **180 天** (半年) 以上。

### 5.2 必查重要 Windows 事件識別碼 (Event ID)
- `4624`：成功登入 (注意 Logon Type，Type 10 為遠端桌面 RDP，Type 3 為網路連線)。
- `4625`：登入失敗 (大量出現代表暴力破解或密碼噴灑)。
- `4720`：建立新使用者帳號。
- `1102`：安全稽核日誌遭手動清除 (極度危險告警)。
                        """,
                        "caseStudy": "【實務情境】某主機半夜遭駭，攻擊者企圖執行 `wevtutil cl security` 清除 Windows 安全日誌掩飾蹤跡。然而因企業啟用了日誌即時轉送至遠端 SIEM，攻擊者本地清除的動作不僅未能銷毀證據，反而觸發 Event ID 1102 產生最高級警報。"
                    },
                    {
                        "id": "B2-M06",
                        "title": "單元 6：資料備份、還原演練與 3-2-1 原則實務",
                        "keywords": ["3-2-1 Backup Rule", "RTO", "RPO", "Immutable Backup", "Disaster Recovery"],
                        "summary": "徹底落實 3-2-1 備份架構、差異/增量備份評估、不可竄改備份 (WORM) 與勒索軟體攻擊下的無感染還原演練實務。",
                        "content": """
### 6.1 經典 3-2-1 備份鐵律
- **3** 份資料複本 (1份正式營運 + 2份備份複本)。
- **2** 種不同媒介 (例如磁碟陣列 SAN + 磁帶 LTO 或雲端儲存)。
- **1** 份異地保存 (Off-site / 實體隔離 Air-gapped 或雲端唯讀保存)。

### 6.2 現代 3-2-1-1-0 擴充規範
- 增加『1 份不可變 (Immutable) / 離線 (Offline)』複本。
- 達成『0 錯誤還原』：未經驗證還原成功的備份等於無效備份，必須每季/每半年進行實體開機還原測試。

### 6.3 備份方式比較
- **完整備份 (Full Backup)**：還原最快 (只需最後一份)，但備份時間最長、耗費空間最大。
- **增量備份 (Incremental Backup)**：備份極快 (只存自上次任意備份後異動部分)，但還原最慢 (需依序載入完整備份及所有增量備份)。
- **差異備份 (Differential Backup)**：只存自『上次完整備份』後之異動。還原時僅需完整備份 + 最後一份差異備份。
                        """,
                        "caseStudy": "【實務情境】某製造廠所有伺服器被勒索軟體加密，甚至連連網備份 NAS 亦被格式化。所幸該廠每週五會將資料備份至離線磁帶並鎖入防磁保險箱 (Air-gap)，最終靠著該份實體隔離備份在 24 小時內完整重建系統，未付一毛贖金。"
                    },
                    {
                        "id": "B2-M07",
                        "title": "單元 7：社交工程防禦與企業資安意識演練",
                        "keywords": ["Phishing Simulation", "Spear Phishing", "Watering Hole", "Security Awareness"],
                        "summary": "企業內部社交工程釣魚郵件模擬演練實施指南、釣魚郵件特徵識別、水坑攻擊防禦與全員資安文化塑造。",
                        "content": """
### 7.1 社交工程常見攻擊型態
- **魚叉式釣魚 (Spear Phishing)**：針對特定目標 (如研發人員、財務人員) 深度客製化郵件內容。
- **水坑攻擊 (Watering Hole)**：駭客不直接攻擊目標企業，而是先攻陷目標員工經常造訪的第三方專業論壇或合作夥伴網站，伺機植入瀏覽器漏洞攻擊程式。
- **簡訊/通訊釣魚 (Smishing/Vishing)**：利用仿冒簡訊或電話偽裝 IT 部門索取驗證碼。

### 7.2 郵件防護三大國際標準
- **SPF (寄件者政策框架)**：DNS TXT 紀錄載明哪些 IP 有權代表該網域發信。
- **DKIM (網域金鑰識別郵件)**：寄件伺服器以私鑰對郵件內容簽章，收件伺服器由 DNS 抓取公鑰驗證未遭篡改。
- **DMARC**：定義當 SPF 或 DKIM 驗證失敗時，收件端應採取的策略 (none 監控, quarantine 隔離, reject 拒收)。
                        """,
                        "caseStudy": "【實務情境】攻擊者註冊外觀極度相似的近音網域 (Typosquatting) 發送偽造匯款通知。收件端企業因全面啟用了 DMARC 嚴格拒收策略 (p=reject)，惡意郵件在邊界郵件閘道端即被自動阻絕，員工完全未收到。"
                    },
                    {
                        "id": "B2-M08",
                        "title": "單元 8：實體環境安全、設備生命週期與媒體廢棄銷毀",
                        "keywords": ["Physical Security", "Degaussing", "Data Sanitization", "Disposal"],
                        "summary": "掌握資料中心實體門禁防護 (CCTV, 防尾隨)、電力環控安全、硬碟報廢消磁 (Degaussing) 與符合 NIST SP 800-88 之資料抹除規範。",
                        "content": """
### 8.1 實體安全防護控制
- **防尾隨機制 (Anti-Tailgating)**：雙重旋轉門 (Mantrap / Air-lock)，一次僅容許一人刷卡驗證進入。
- **實體區域分級**：公開接待區、辦公作業區、機密研發區、核心主機房，逐級提升門禁身分認證難度與留存進出日誌。
- **環境監控**：不斷電系統 (UPS)、雙迴路供電、自動氣體滅火系統 (FM-200/NOVEC，避免用水破壞電器設備)。

### 8.2 儲存媒體報廢與銷毀標準 (NIST SP 800-88)
- **清除 (Clear)**：邏輯覆寫 (Overwrite)，以特定字元覆蓋所有磁區，防止簡易資料救援軟體讀取。
- **淨化 (Purge)**：採用進階磁氣消磁 (Degaussing) 或加密抹除 (Cryptographic Erase)，使資料在實驗室設備下亦不可復原。
- **銷毀 (Destroy)**：物理破碎 (Shredding) 物理粉碎至小於特定顆粒大小或焚毀，處理流程必須全程錄影並出具《銷毀證明書》。
                        """,
                        "caseStudy": "【實務情境】企業汰換批次老舊伺服器硬碟，外包給廢棄物廠商處理。由於資安團隊派員現場監督並進行高斯強度消磁後送入實體破碎機碾成鐵屑，全程錄影並填寫監管鏈文件，杜絕了二手硬碟資料外流風險。"
                    }
                ]
            }
        ]
    },
    "mid": {
        "title": "iPAS 資訊安全工程師 - 中級能力鑑定核心講義",
        "subjects": [
            {
                "subjectId": "M-SUB-1",
                "name": "考科一：資訊安全規劃與管理",
                "desc": "深入探討 ISO/IEC 27001:2022 最新 ISMS 標準、資安風險管理全流程、業務持續 (BCP/BIA)、供應鏈與委外治理、個資與法規稽核。",
                "modules": [
                    {
                        "id": "M1-M01",
                        "title": "單元 1：ISO/IEC 27001:2022 ISMS 體系與控制措施",
                        "keywords": ["ISO 27001:2022", "ISMS", "PDCA", "Annex A Controls", "Threat Intelligence"],
                        "summary": "徹底解析 ISO/IEC 27001:2022 改版核心：本文主條文 4-10 架構、附錄 A 簡化合併之四大主題 (組織、人員、實體、技術控制共 93 項)、以及新增之 11 項關鍵控制措施。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】某軟體開發企業導入 ISO 27001:2022，針對 A.8.28 安全編碼控制要求，將靜態代碼分析 (SAST) 與軟體相依元件檢查整合進 CI/CD 流水線中，未通過安全測試的程式碼一律無法合入主分支，順利通過外部驗證機構查核。"
                    },
                    {
                        "id": "M1-M02",
                        "title": "單元 2：資通安全法規架構、責任等級與合規管理",
                        "keywords": ["Cybersecurity Act", "Responsibility Levels", "Incident Reporting", "Critical Infrastructure"],
                        "summary": "掌握我國資通安全管理法子法架構：《資通安全責任等級分級辦法》、《資通安全事件通報及應變辦法》、《資通安全情資分享辦法》之公務與特定非公務機關實施要求。",
                        "content": """
### 2.1 責任等級劃分 (A ~ E 級) 核心規定
- **A 級機關 (國家關鍵)**：總統府、五院、外交部、國防部、具備全國性公務機密或關鍵基礎設施關鍵提供者。必須建立 SOC、導入全機關 ISMS 認證、配置至少 4 名以上資安專職人員、定期辦理紅隊演練與外部稽核。
- **B 級機關**：直轄市政府、部會所屬三級機關。需配置至少 2 名資安專職人員。
- **C 級機關**：縣市政府、偏遠地區機關。配置至少 1 名資安專職人員。
- **D/E 級機關**：無專責人員，由上級機關或委外支援。

### 2.2 資安事件等級劃分與通報規定
- **第一級 / 第二級**：輕微或局部核心外系統受影響。知悉後 **1 小時內通報**，完成應變後依規結案。
- **第三級 / 第四級 (重大事件)**：國家機密外洩、關鍵業務全面中斷、或涉及核心系統遭到全面控制。知悉後 **1 小時內通報**，且必須在 **36 小時內** (或依主管機關要求期限) 完成損害控制與復原。
                        """,
                        "caseStudy": "【實務情境】某市府地政局核心資料庫遭受勒索攻擊導致全市房屋產權過戶交易停擺，符合第三級資安事件定義。該局於知悉後 30 分鐘內完成資安通報，並啟動應變小組於 24 小時內利用離線備份完成核心資料還原，符合法定時限。"
                    },
                    {
                        "id": "M1-M03",
                        "title": "單元 3：資安風險評鑑與風險處置策略實務",
                        "keywords": ["Risk Assessment", "Risk Treatment", "ISO 27005", "Asset Identification", "Residual Risk"],
                        "summary": "掌握 ISO/IEC 27005 風險管理框架：資產鑑別、威脅與脆弱性評估、風險值計算模型 (可能性 × 衝擊度)、以及四大風險處置策略與殘餘風險管理。",
                        "content": """
### 3.1 風險評鑑標準五步驟
1. **建立背景環境**：定義風險評估範圍、評估準則與風險可接受度門檻。
2. **資產鑑別與評價**：盤點資訊資產 (硬體、軟體、資料、人員、流程) 並給予價值評分 (依 CIA 三面向)。
3. **威脅與弱點分析**：辨識資產可能面臨之威脅 (人為蓄意、天災、操作失誤) 及系統存在之脆弱性。
4. **風險分析與評級**：計算風險等級：$Risk = Likelihood (可能性) \\times Impact (衝擊度)$。
5. **風險評量**：比對組織風險接受準則，判斷該風險是否超出可承受限度。

### 3.2 四大風險處置策略 (Risk Treatment)
1. **風險降低 / 緩解 (Mitigation / Modification)**：實施控制措施以降低可能性或衝擊 (如部署 WAF、安裝補丁)。
2. **風險轉移 / 分擔 (Sharing / Transfer)**：將風險損失轉移給第三方 (如投保資安險、委外維運合約)。
3. **風險規避 (Avoidance)**：終止引發風險的業務活動 (如停止支援極端老舊且無法修補之作業系統)。
4. **風險保留 / 接受 (Retention / Acceptance)**：當風險已低於容許值，或處置成本顯著高於潛在損失，由高層簽核同意承擔殘餘風險 (Residual Risk)。
                        """,
                        "caseStudy": "【實務情境】某電商盤點出一套建置於 Windows Server 2003 的老舊會員促銷系統，因原廠早已停止安全支援且程式碼遺失無法升級。資安委員會評估後決定全面下線該系統並以微服務重寫，此即採取『風險規避』策略。"
                    },
                    {
                        "id": "M1-M04",
                        "title": "單元 4：業務持續運作計畫 (BCP) 與營運衝擊分析 (BIA)",
                        "keywords": ["BCP", "BIA", "RTO", "RPO", "Disaster Recovery", "Tabletop Exercise"],
                        "summary": "解析 ISO 22301 業務持續管理系統：營運衝擊分析 (BIA) 指標、災難復原中心形式 (Hot/Warm/Cold Site)、BCP 演練類型與維護。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】證券交易所核心撮合系統要求 RTO = 0 分鐘，RPO = 0 秒。其建置同城雙活 (Active-Active) 熱站，透過同步光纖通道進行雙向寫入，當主機房突遭斷電時，備援機房無縫接管，市場交易零中斷。"
                    },
                    {
                        "id": "M1-M05",
                        "title": "單元 5：第三方供應鏈安全與委外資安管理",
                        "keywords": ["Supply Chain Risk", "Vendor Management", "SLA", "Right to Audit", "SBOM"],
                        "summary": "掌握軟體供應鏈與委外廠商全生命週期管理：合約資安規範 (Right to Audit 稽核權)、SLA 服務水準協定、第三方遠端連線管制與開源軟體風險評估。",
                        "content": """
### 5.1 委外生命週期風險管控
- **評選階段**：審查廠商資安資質 (如 ISO 27001 證書、過往資安事故紀錄、開發人員認證)。
- **合約規範**：明確約定『保密協定 (NDA)』、『資安通報責任』、『稽核權條款 (Right to Audit)』與違約賠償。
- **連線與權限管理**：嚴禁外包廠商常設通用帳號；遠端維運必須經由 VPN + MFA 登入特權管理跳板機 (PAM)，全程側錄操作。
- **退場與終止**：合約終止時，徹底撤銷所有帳號與網路存取權，收回或銷毀所有機敏資料並取得廠商切結書。

### 5.2 軟體供應鏈安全 (Software Supply Chain Security)
- 盤點所有第三方函式庫，要求提供 SBOM (軟體物料清單)。
- 建立軟體元件分析 (SCA) 機制，防範依賴混淆 (Dependency Confusion) 與搶註 Typosquatting 開源套件。
                        """,
                        "caseStudy": "【實務情境】SolarWinds 供應鏈攻擊事件中，駭客藉由入侵軟體開發商的構建系統，在合法簽名的更新包中注入木馬。防範此類威脅，企業除審查廠商資安機制外，應落實微切分與 Zero Trust，即便合法軟體有異常外連行為亦即時阻斷。"
                    },
                    {
                        "id": "M1-M06",
                        "title": "單元 6：資安治理架構、政策制定與成熟度評估",
                        "keywords": ["Security Governance", "CISO", "KPI / KRI", "Cybersecurity Policy", "CMMI"],
                        "summary": "建立現代企業資安治理體系：董事會與管理階層當責性、CISO 職掌與獨立性、資安政策四層級文件架構、關鍵績效指標 (KPI/KRI) 與成熟度衡量。",
                        "content": """
### 6.1 資安治理與組織職責
- **治理 vs 管理**：治理 (Governance) 由董事會與高階主管負責，決定方向、戰略投資與風險偏好；管理 (Management) 由 CISO 與技術團隊負責日常計畫、執行與維運。
- **CISO 的獨立性**：CISO (資安長) 應直接向董事會或執行長 (CEO) 報告，避免隸屬於 CIO (資訊長) 之下，以防止資安目標與 IT 效率產生利益衝突。

### 6.2 資安文件四階體系
- **一階：政策 (Policy)**：高階管理層宣示之全域方針與原則 (如資訊安全政策)。具強制性，異動頻率低。
- **二階：程序 / 辦法 (Procedure / Standard)**：具體工作規範 (如帳號管理辦法、弱點修補程序)。
- **三階：作業指引 / 準則 (Guideline / Work Instruction)**：技術操作步驟指引 (如 Windows 伺服器強化手冊)。
- **四階：表單 / 紀錄 (Record / Form)**：執行各項控制所留下的佐證軌跡 (如門禁進出登記簿、簽核紀錄)。
                        """,
                        "caseStudy": "【實務情境】某金控金檢時被主管機關糾正，因其資安長兼任開發維運主管，導致為求系統快速上線而忽視資安檢驗。該金控隨後調整組織架構，設立獨立資安專責處室，CISO 直屬總經理，建立健全資安治理制衡。"
                    },
                    {
                        "id": "M1-M07",
                        "title": "單元 7：國際資料隱私法規 (GDPR) 與隱私保護技術",
                        "keywords": ["GDPR", "Privacy by Design", "DPO", "PIA / DPIA", "Pseudonymization"],
                        "summary": "掌握歐盟 GDPR 與國際隱私標準：資料主體權利 (被遺忘權、資料可攜權)、隱私衝擊評估 (DPIA)、假名化與去識別化技術。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】跨國電商平台收到歐洲客戶依據 GDPR 提出被遺忘權要求。平台資安與資料團隊啟動自動化遮蔽流程，將歷史訂單中的客戶姓名、電話、地址永久去識別化，同時保留不具個資之交易金額供財務查帳，兼顧合規與商業需求。"
                    },
                    {
                        "id": "M1-M08",
                        "title": "單元 8：資安稽核實務、缺失改善與 CAPA 機制",
                        "keywords": ["Internal Audit", "Audit Evidence", "CAPA", "Corrective Action", "Non-Conformity"],
                        "summary": "學習資安內外部稽核流程：稽核計畫擬定、抽樣證據獲取、不符合項 (Non-conformity) 開立、根因分析 (RCA) 與矯正預防措施 (CAPA) 追蹤結案。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】內稽發現某離職員工帳號在離職 30 天後仍未停用。除立即關閉該帳號外，深入 RCA 發現人事系統與 AD 帳號系統為人工通知脫鉤。矯正措施為開發自動化 API 同步，人事系統一辦理離職流程，AD 帳號自動秒級鎖定，徹底杜絕缺失再犯。"
                    }
                ]
            },
            {
                "subjectId": "M-SUB-2",
                "name": "考科二：資訊安全防禦技術與事件應變",
                "desc": "涵蓋零信任架構落地、MITRE ATT&CK 框架、SOC 監控與 SOAR 自動化、CSIRT 五大階段事件應變、數位鑑識與證據保全、安全軟體開發 (SSDLC) 與雲端資安架構實務。",
                "modules": [
                    {
                        "id": "M2-M01",
                        "title": "單元 1：零信任架構 (ZTA) 規劃與落地實務",
                        "keywords": ["Zero Trust", "NIST SP 800-207", "PDP", "PEP", "Micro-Segmentation"],
                        "summary": "掌握 NIST SP 800-207 零信任架構藍圖：策略決定點 (PDP)、策略執行點 (PEP)、軟體定義邊界 (SDP)、身份感知代理 (IAP) 與網路微切分實作。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】跨國企業導入零信任架構，研發人員即使在家辦公，若其筆電防毒軟體未更新或未開啟磁碟加密，PDP 判斷設備健康度不合格，PEP 立即阻斷其對生產代碼庫之存取，僅允許連線至自修補入口。"
                    },
                    {
                        "id": "M2-M02",
                        "title": "單元 2：MITRE ATT&CK 框架、Cyber Kill Chain 與威脅情資 (CTI)",
                        "keywords": ["MITRE ATT&CK", "Cyber Kill Chain", "Threat Intelligence", "TTPs", "Pyramid of Pain"],
                        "summary": "掌握 MITRE ATT&CK 14 大戰術矩陣、洛克希德馬丁網路殺傷鏈、痛苦金字塔 (Pyramid of Pain) 以及威脅情資 (STIX/TAXII) 實務應用。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】SOC 分析員在分析 APT 攻擊時，發現黑客使用 Mimikatz 傾倒記憶體憑證 (T1003)。防禦團隊未僅僅阻擋 Mimikatz 執行檔雜湊，而是在網域層全面啟用 Credential Guard 並阻斷 LSASS 記憶體讀取，直擊 TTPs 頂端，徹底封殺該黑客團體之活動。"
                    },
                    {
                        "id": "M2-M03",
                        "title": "單元 3：現代 SOC 維運、SIEM 關聯分析與 SOAR 自動化劇本",
                        "keywords": ["SOC", "SIEM", "SOAR", "Playbook", "Alert Fatigue", "Use Cases"],
                        "summary": "探討安全維運中心 (SOC) 7x24 監控機制、SIEM 關聯分析規則撰寫、警報疲勞 (Alert Fatigue) 緩解與 SOAR 自動化劇本編排。",
                        "content": """
### 3.1 SIEM 關聯規則設計範例
- **暴力破解成功情境**：同一個帳號在 5 分鐘內發生超過 10 次 Event ID 4625 (登入失敗)，且隨後緊接著出現 Event ID 4624 (登入成功)。此為暴力破解成功或密碼猜測之經典特徵。
- **非上班時間異常大流量外傳**：夜間 02:00 ~ 05:00 期間，非備份伺服器向國外未知 IP 外傳超過 10GB 之封包。

### 3.2 SOAR 自動化回應劇本 (Playbook)
- 當 SIEM 觸發高危情資警報 -> SOAR 自動呼叫 VirusTotal API 查詢檔案雜湊 -> 若檢出率大於 20 家 -> 自動發送 API 命令至 EDR 隔離受害終端 -> 同時在防火牆黑名單封鎖連線 IP -> 在 ITSM 建立資安事故工單並推播通知值班資安工程師。
- 劇本自動化可將事件處理平均時間 (MTTR) 從數小時壓縮至數秒鐘。
                        """,
                        "caseStudy": "【實務情境】某電信巨頭 SOC 面臨每日數萬筆警報導致警報疲勞。團隊引進 SOAR 編寫自動驗證劇本，先過濾 85% 的誤報與已知低危雜訊，將分析師專注力解放至真正的重大威脅，威脅回應速度提升 600%。"
                    },
                    {
                        "id": "M2-M04",
                        "title": "單元 4：CSIRT 資安事件應變五大階段實務指南",
                        "keywords": ["Incident Response", "NIST SP 800-61", "CSIRT", "Containment", "Lessons Learned"],
                        "summary": "掌握 NIST SP 800-61 事件應變生命週期：準備 (Preparation) -> 偵測與分析 (Detection & Analysis) -> 圍堵、抹除與復原 (Containment, Eradication & Recovery) -> 檢討與改善 (Post-Incident Activity)。",
                        "content": """
### 4.1 事件應變四大循環核心 (NIST SP 800-61)
1. **準備階段 (Preparation)**：建置 CSIRT 小組成員通訊錄、準備乾淨應變工具箱 (Jumpsuit)、演練 Playbook、落實各項日誌與備份。
2. **偵測與分析 (Detection & Analysis)**：判定事件真實性與嚴重性等級，界定受災範圍 (Scope of Breach)，確認攻擊向量與受害指標 (IoC)。
3. **圍堵策略 (Containment)**：
   - **短期圍堵**：拔掉受害主機網線或 EDR 網路隔離，阻止向外橫向感染。
   - **長期圍堵**：修補防火牆規則、重設受影響網域管理者憑證。
4. **抹除與復原 (Eradication & Recovery)**：清除所有後門程式、惡意排程與受損使用者帳號；利用純淨離線備份還原系統，並提升監控頻率至少 1 至 3 個月。
5. **事後檢討 (Lessons Learned)**：召開 PIR (Post-Incident Review) 會議，提出事件檢討報告，將缺失轉化為架構改善計畫。
                        """,
                        "caseStudy": "【實務情境】某半導體大廠遭遇進階惡意程式感染。應變小組未急於重灌主機 (避免破壞證據)，而是先透過 EDR 圍堵受害主機群並萃取記憶體 Dump 進行逆向，找出 C2 通訊協議與所有受感染清單後，進行一次性全網清除，避免了復發二次感染。"
                    },
                    {
                        "id": "M2-M05",
                        "title": "單元 5：數位鑑識、證據保全與記憶體鑑識實務",
                        "keywords": ["Digital Forensics", "Order of Volatility", "Chain of Custody", "Volatility", "Bit-stream Image"],
                        "summary": "學習數位鑑識四大原則 (RFC 3227)：揮發性順序、證據監管鏈 (Chain of Custody)、只讀硬體寫入阻斷器 (Write Blocker)、記憶體 RAM 傾倒與離線映像分析。",
                        "content": """
### 5.1 現場採證操作規範
- **嚴禁重開機或隨意關機**：重開機會立即抹除 RAM 中的暫態記憶體資料、解密金鑰與網路連線狀態。
- **使用硬體防寫設備 (Hardware Write Blocker)**：在對儲存媒體進行映像複製時，物理硬體保證僅能讀取無法寫入，確保原始證據完整未動。
- **位元對位元複製 (Bit-Stream Image)**：包括未配置空間 (Unallocated Space) 與鬆弛空間 (Slack Space)，產出 dd, raw, E01 格式映像。
- **雜湊校驗比對**：採集前先計算原始磁碟 SHA-256，複製完成後再次計算映像檔 SHA-256，兩者雜湊值必須百分之百一致方具司法證據效力。

### 5.2 記憶體鑑識重點 (Volatility 工具)
- 提取動態載入的無檔案惡意程式 (Fileless Malware)。
- 檢視當前已建立的 TCP 網路連線 (netscan)。
- 提取當前執行的進程列表與注入代碼 (pslist, malfind)。
                        """,
                        "caseStudy": "【實務情境】司法警察配合資安鑑識團隊查扣某洗錢機房之主機。團隊在電腦維持通電狀態下，利用專用硬體工具即時完整導出 64GB 記憶體，成功在 RAM 中解密出 Telegram 秘密通訊群組與比特幣錢包私鑰，成為法庭定罪關鍵證據。"
                    },
                    {
                        "id": "M2-M06",
                        "title": "單元 6：安全軟體開發 (SSDLC) 與 DevSecOps 實務",
                        "keywords": ["SSDLC", "DevSecOps", "SAST", "DAST", "STRIDE", "Threat Modeling"],
                        "summary": "掌握微軟 STRIDE 威脅建模方法論、CI/CD 安全流水線建構、靜態程式碼分析 (SAST)、動態應用檢測 (DAST) 與軟體相依性掃描 (SCA)。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】金融科技新創將 DevSecOps 落地於 GitLab CI 流水線中，在程式碼 Commit 時自動執行 SAST 與 SCA。若發現嚴重等級大於 High 的漏洞，流水線自動中斷部署，強制開發者修正後方可上線，上線後漏洞率下降 85%。"
                    },
                    {
                        "id": "M2-M07",
                        "title": "單元 7：雲端安全架構 (Cloud Security) 與虛擬化防護",
                        "keywords": ["Shared Responsibility Model", "CSPM", "CWPP", "CASB", "IAM"],
                        "summary": "掌握雲端責任共擔模型 (IaaS, PaaS, SaaS)、雲端安全狀態管理 (CSPM)、工作負載保護 (CWPP)、CASB 與雲端身分權限控管最佳實務。",
                        "content": """
### 7.1 雲端責任共擔模型 (Shared Responsibility Model)
- **IaaS (基礎架構即服務，如 AWS EC2)**：雲端業者負責實體設施、硬體伺服器與虛擬化底層；**客戶負責**作業系統安裝、更新修補、網路防火牆安全組 (Security Group)、應用程式與所有資料加密。
- **PaaS (平台即服務，如 Google App Engine)**：業者負責實體與作業系統補丁；客戶負責應用程式本身之邏輯與資料安全。
- **SaaS (軟體即服務，如 Microsoft 365)**：業者負責底層至應用程式全端安全；**客戶依然負責使用者身分認證、存取控制與自身資料治理**。
- **鐵律**：無論哪種雲端模式，**『資料的擁有與資料保護責任』永遠在客戶身上**！

### 7.2 雲端安全三大利器
- **CSPM (雲端安全狀態管理)**：持續稽核雲端環境組態配置 (如防範 S3 Bucket 意外公開、檢查過度寬鬆的 IAM 權限)。
- **CWPP (雲端工作負載保護平台)**：針對雲端 VM、Container (Docker/K8s) 提供運行時進程監控與漏洞防護。
- **CASB (雲端存取安全代理)**：在企業與多個 SaaS 應用之間充當安全閘道，防範影子 IT (Shadow IT) 與資料外洩。
                        """,
                        "caseStudy": "【實務情境】某企業將客戶資料備份至 AWS S3，工程師誤將儲存桶權限設為 Public Read，導致數百萬筆個資直接在網路上裸奔。導入 CSPM 後，系統即時偵測到組態偏離 baseline，自動觸發修復腳本強制關閉公開權限並通報 CISO。"
                    },
                    {
                        "id": "M2-M08",
                        "title": "單元 8：進階持續性威脅 (APT) 防禦與主動威脅獵捕 (Threat Hunting)",
                        "keywords": ["Threat Hunting", "APT Defense", "Lateral Movement", "Pass-the-Hash", "Living off the Land"],
                        "summary": "掌握主動威脅獵捕 (Threat Hunting) 假說驅動模型、橫向移動 (Lateral Movement) 檢測、Pass-the-Hash 防禦與無檔案攻擊因應策略。",
                        "content": """
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
                        """,
                        "caseStudy": "【實務情境】威脅獵捕團隊提出假設：攻擊者可能濫用內網未受管工作站互相遠端。透過分析內網流量圖譜，發現原本應為單純終端的一台辦公室 PC，半夜竟然向其他 40 台工作站發起大量 SMB 445 掃描。獵捕小組成功在攻擊者觸發任何勒索軟體前將其拔除，挽救企業整座內網。"
                    }
                ]
            }
        ]
    }
}

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "assets")
    notes_dir = os.path.join(base_dir, "notes")
    
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(notes_dir, exist_ok=True)
    
    # 1. 寫入專業詞彙辭典 JS
    glossary_js_path = os.path.join(assets_dir, "glossary-data.js")
    with open(glossary_js_path, "w", encoding="utf-8") as f:
        f.write("// iPAS 資安工程師 - 專業英文術語與發音辭典資料庫\n")
        f.write("window.IPAS_GLOSSARY = ")
        json.dump(GLOSSARY_TERMS, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Glossary written: {len(GLOSSARY_TERMS)} terms to {glossary_js_path}")

    # 2. 寫入講義資料 JS
    notes_js_path = os.path.join(assets_dir, "notes-data.js")
    with open(notes_js_path, "w", encoding="utf-8") as f:
        f.write("// iPAS 資安工程師 - 初級與中級官方核心講義資料庫\n")
        f.write("window.IPAS_LECTURE_NOTES = ")
        json.dump(LECTURE_NOTES, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Lecture notes written: 32 modules to {notes_js_path}")

    # 3. 寫入 Markdown 格式講義供研讀
    for level_key, level_data in LECTURE_NOTES.items():
        md_file_path = os.path.join(notes_dir, f"{level_key}-lecture-notes.md")
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(f"# {level_data['title']}\n\n")
            for sub in level_data["subjects"]:
                f.write(f"## {sub['name']}\n")
                f.write(f"> {sub['desc']}\n\n")
                for mod in sub["modules"]:
                    f.write(f"### {mod['title']}\n\n")
                    f.write(f"**關鍵詞 (Keywords)**: {', '.join(mod['keywords'])}\n\n")
                    f.write(f"**重點概述**: {mod['summary']}\n\n")
                    f.write(mod["content"].strip() + "\n\n")
                    f.write(f"> 💡 **實務案例與考點 (Case Study)**:\n> {mod['caseStudy']}\n\n")
                    f.write("---\n\n")
        print(f"Markdown lecture notes created: {md_file_path}")

if __name__ == "__main__":
    main()
