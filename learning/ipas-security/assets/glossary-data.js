// iPAS 資安工程師 - 專業英文術語與發音辭典資料庫
window.IPAS_GLOSSARY = [
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
];
