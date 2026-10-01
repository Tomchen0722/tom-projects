// iPAS 資訊安全工程師 - 初級與中級官方核心講義資料庫
window.IPAS_LECTURE_NOTES = {
  "basic": {
    "title": "iPAS 資訊安全工程師 - 初級能力鑑定核心講義",
    "subjects": [
      {
        "subjectId": "B-SUB-1",
        "name": "考科一：資訊安全概論",
        "desc": "涵蓋資安核心三要素 (CIA)、網路通訊安全架構、作業系統強化、惡意程式分類防護、OWASP Top 10 核心弱點、密碼學應用與資安法規概要。",
        "modules": [
          {
            "id": "B1-M01",
            "title": "單元 1：資安核心三要素與安全架構原則",
            "keywords": [
              "Confidentiality",
              "Integrity",
              "Availability",
              "Defense-in-Depth",
              "Least Privilege",
              "Separation of Duties",
              "Non-Repudiation",
              "AAA Framework"
            ],
            "summary": "掌握資訊安全最高指導原則：機密性 (Confidentiality)、完整性 (Integrity)、可用性 (Availability) 之工程實踐。深入解析縱深防禦 (Defense-in-Depth)、最小權限原則 (PoLP)、職責區隔 (SoD) 與不可否認性 (Non-Repudiation) 之技術落地標準。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. CIA 三要素工程定義\n- **機密性 (Confidentiality)**：確保僅經授權之主體（人員、進程或系統）能夠讀取或存取受保護資料。\n  - *落地控制技術*：靜態資料加密 (AES-256, BitLocker)、傳輸中資料加密 (TLS 1.3, IPsec)、動態資料遮罩 (Data Masking, 隱碼身分證號/信用卡號)、基於角色的存取控制 (RBAC)。\n  - *威脅威脅*：竊聽 (Eavesdropping)、網路嗅探 (Sniffing)、資料外洩 (Data Exfiltration)、未授權讀取。\n- **完整性 (Integrity)**：確保資訊與通訊系統在生命週期中未遭受未經授權的篡改、插入或刪除，保持正確性與真實性。\n  - *落地控制技術*：加密雜湊函數 (SHA-256, SHA-3)、訊息鑑別碼 (HMAC)、數位簽章 (Digital Signature)、檔案完整性監控 (FIM, 如 Tripwire, OSSEC)。\n  - *威脅威脅*：中間人攻擊 (MitM) 篡改封包、惡意軟體修改系統檔、未授權資料庫 UPDATE / DELETE。\n- **可用性 (Availability)**：確保經授權之主體在業務需要之時，能及時、可靠地存取系統、資料與關鍵服務。\n  - *落地控制技術*：伺服器高可用性叢集 (HA Cluster)、負載平衡 (Load Balancing)、DDoS 流量清洗 (Cloudflare / Akamai)、雙迴路不斷電系統 (UPS)、多重異地備援。\n  - *威脅威脅*：阻斷服務攻擊 (DoS/DDoS)、勒索軟體全盤加密 (破壞可用性與完整性)、機房火災斷電。\n\n#### 2. 經典架構原則深度解析\n1. **縱深防禦 (Defense-in-Depth, DiD)**：\n   - 不依賴任何單一防禦機制。建立包含「實體層、網路周邊、內部網段、端點主機、應用程式、資料層、人員意識」的七層同心圓防禦鏈。\n   - 單一防線被突破時，後續防線能有效延滯、限縮並告警攻擊行為。\n2. **最小權限原則 (Principle of Least Privilege, PoLP)**：\n   - 主體僅被賦予執行特定業務任務所必需的最低權限集合，且維持該權限之有效時間僅限於任務執行期間 (Just-in-Time Access)。\n   - 禁止日常維運常態使用 `root` 或 `Domain Admins` 特權帳號登入端點。\n3. **職責區隔 (Separation of Duties, SoD)**：\n   - 將關鍵交易或高風險流程之授權、執行、覆核與稽核職權分配予相異人員，防範單點弊端與單人疏失。\n   - *例*：軟體開發者不得擁有生產環境 (Production) 上線發布與直接寫入資料庫之權限。\n4. **不可否認性 (Non-Repudiation)**：\n   - 透過「發送方專屬私鑰簽章」結合「第三方可信時間戳記 (RFC 3161 TSA)」，使行為發起者事後無法抵賴操作事實。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux 主機最小權限配置 (Sudoers 實務)\n```bash\n# 編輯 /etc/sudoers (務必使用 visudo 進行語法檢查)\n# 嚴格限制網頁維運人員僅能重啟 nginx 服務，嚴禁取得 root shell\nwebadmin ALL=(ALL) /bin/systemctl restart nginx, /bin/systemctl status nginx\n# 禁用通配符與 shell escape 命令\nDefaults:webadmin !requiretty, secure_path=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin\"\n```\n\n#### 2. 檔案完整性監控 (FIM) 實務腳本\n```bash\n# 對關鍵系統目錄計算 SHA-256 基準雜湊清單\nfind /bin /sbin /usr/bin -type f -exec sha256sum {} + > /var/log/baseline_hashes.txt\n# 每日排程比對校驗完整性\nsha256sum -c /var/log/baseline_hashes.txt --quiet\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 觀念維度 | 考題常見陷阱選項 | 官方標準正解判定 |\n| :--- | :--- | :--- |\n| **勒索軟體衝擊** | 題目問勒索軟體主要破壞哪一要素，考生常誤選「機密性」 | **可用性 (Availability) 與 完整性 (Integrity)**。勒索軟體旨在鎖死檔案勒索贖金，除非伴隨雙重勒索外洩，否則核心破壞為可用性 |\n| **不可否認性技術** | 宣稱「對稱式加密 (AES)」可達成不可否認性 | **錯誤！對稱金鑰由雙方共用**，任一方皆可偽造密文。必須使用「非對稱數位簽章 (Digital Signature)」方具不可否認性 |\n| **縱深防禦本質** | 誤以為縱深防禦是「安裝兩套不同廠牌的防毒軟體」 | **多維度、多層次互補控管**（實體、網路、主機、應用、人員），而非單一層次之軟體重複堆疊 |\n\n> 🔑 **防呆口訣**：\n> - 機密靠加密與 ACL，完整靠雜湊與簽名，可用靠備援與清洗。\n> - 對稱加密速度快但無不可否認，非對稱簽章具專屬私鑰才算數！\n        ",
            "caseStudy": "【實務案例分析】某電商平台遭遇外部攻擊，駭客利用 Web 伺服器之 SQL 注入弱點突破前端。然而，該企業貫徹了「縱深防禦」與「最小權限原則」：Web 伺服器與資料庫伺服器之間存在內網次世代防火牆，嚴格僅開放 TCP 3306 且僅限指定 IP；資料庫中會員身分證字號與信用卡均採用 AES-256-GCM 密文存儲，且資料庫連線帳號僅具備 SELECT/INSERT 權限而無 DROP/ALTER 特權。駭客即便成功透過 SQL 注入取得前端部分資料，但無法提權橫向移動至內網核心網段，機敏欄位亦因密文防護無法即時破解，成功將災害控制於最低範圍。"
          },
          {
            "id": "B1-M02",
            "title": "單元 2：網路通訊協定與架構安全",
            "keywords": [
              "OSI 7 Layers",
              "TCP 3-Way Handshake",
              "TLS 1.3",
              "IPsec",
              "DNSSEC",
              "DMZ Network Architecture"
            ],
            "summary": "全面剖析 OSI 7 層模型與 TCP/IP 協定堆疊之安全缺陷與防禦機制。深入探討 TCP 三向交握、SYN Flood 攻擊與 SYN Cookies 緩解機制、TLS 1.3 密碼套件精簡與 0-RTT 權衡、IPsec AH/ESP 模式、DNSSEC 以及企業 DMZ 隔離區規劃架構。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. OSI 7 層與常見威脅／防禦對照表\n- **第 7 層 應用層 (Application)**：HTTP/HTTPS, DNS, SMTP, SSH。\n  - *威脅*：SQL Injection, XSS, DNS 偽冒, HTTP Flood。\n  - *防禦*：WAF (第7層檢測), DNSSEC, SPF/DKIM/DMARC。\n- **第 4 層 傳輸層 (Transport)**：TCP, UDP。\n  - *威脅*：TCP SYN Flood, UDP Amplification, 連線劫持。\n  - *防禦*：SYN Cookies, 防火牆狀態表過濾, 流量閥值限制。\n- **第 3 層 網路層 (Network)**：IP, ICMP, IPsec。\n  - *威脅*：IP 偽造 (IP Spoofing), Smurf 攻擊, ICMP Flood。\n  - *防禦*：IPsec (RFC 4301), 單播反向路徑轉發 (uRPF), 防火牆封鎖 ICMP。\n- **第 2 層 資料鏈結層 (Data Link)**：以太網 (Ethernet), ARP, 802.1Q VLAN。\n  - *威脅*：ARP 欺騙 (ARP Spoofing), MAC 氾濫, CAM 表溢位, VLAN 跳躍。\n  - *防禦*：動態 ARP 檢驗 (DAI), DHCP Snooping, 連接埠安全 (Port Security)。\n\n#### 2. TCP 三向交握 (3-Way Handshake) 與 SYN Flood\n- **標準交握流程**：\n  1. 客戶端發送 `SYN` (Seq = x) -> 伺服器端進入 `SYN_RCVD` 狀態，分配 TCB (傳輸控制區塊) 資源。\n  2. 伺服器回覆 `SYN/ACK` (Seq = y, Ack = x + 1)。\n  3. 客戶端回覆 `ACK` (Seq = x + 1, Ack = y + 1) -> 雙方進入 `ESTABLISHED`。\n- **SYN Flood 阻斷服務攻擊原理**：\n  - 攻擊者發送巨量偽造來源 IP 的 `SYN` 封包，伺服器發送 `SYN/ACK` 後因找不到真實客戶端而處於半開啟連線狀態 (Half-open connection)。半開連線隊列 (Backlog Queue) 迅速耗盡，導致合法使用者無法建立連線。\n- **SYN Cookies 緩解原理**：\n  - 伺服器在收到 SYN 時**不分配**記憶體 TCB 資源，而是利用客戶端 IP、Port、時間戳記與伺服器密鑰計算出一個加密雜湊作為 Initial Sequence Number (ISN)。只有當客戶端回覆合法 ACK 且計算驗證相符時，才分配連線資源。\n\n#### 3. TLS 1.3 (RFC 8446) 核心技術革新\n- **交握延遲降至 1-RTT** (舊版 TLS 1.2 為 2-RTT)，並支援 0-RTT 早期資料 (Early Data，注意：0-RTT 易受重送攻擊 Replay Attack)。\n- **徹底廢棄不安全密碼學演算法**：移除 RSA 金鑰交換 (全面強制具備完全前向保密 PFS 之 (EC)DH)、移除 CBC 分組模式、移除 RC4、MD5、SHA-1。\n- 僅保留極度精簡安全密碼套件：`TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_AES_128_GCM_SHA256`。\n\n#### 4. DMZ (Demilitarized Zone) 拓撲原則\n- **拓撲定義**：位於內部核心私有網路與外部網際網路之間的隔離緩衝網段。\n- **存取控制鐵律 (Golden Rules)**：\n  1. Internet 訪客僅允許連線至 DMZ 之特定公眾服務 Port (如 443, 80, 25)。\n  2. DMZ 伺服器**絕對禁止主動發起**連線至內部信任網路 (Internal Trusted LAN)！\n  3. 內部核心資料庫嚴禁置於 DMZ；資料庫應置於內部安全網段，由 DMZ 應用程式透過嚴格受控之代理或單向連線訪問。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux 核心啟用 SYN Cookies 防護\n```bash\n# 檢查當前 SYN Cookies 狀態 (1 為啟用)\nsysctl net.ipv4.tcp_syncookies\n# 寫入 /etc/sysctl.conf 進行永久硬化\nnet.ipv4.tcp_syncookies = 1\nnet.ipv4.tcp_max_syn_backlog = 4096\nnet.ipv4.tcp_synack_retries = 2\nsysctl -p\n```\n\n#### 2. 交換器連接埠安全配置 (Cisco Switch Port Security)\n```text\nSwitch(config-if)# switchport mode access\nSwitch(config-if)# switchport port-security\nSwitch(config-if)# switchport port-security maximum 2\nSwitch(config-if)# switchport port-security mac-address sticky\nSwitch(config-if)# switchport port-security violation shutdown\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 通訊協定 / 概念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **IPsec AH vs ESP** | 題目問哪一個協定提供「資料加密 (機密性)」 | **ESP (封裝安全酬載)** 提供加密與完整性；**AH (認證標頭)** 僅提供認證與完整性，**絕不提供加密**！ |\n| **DMZ 網路規則** | 選項宣稱「DMZ 伺服器被駭後可主動連入內網排解」 | **嚴重違規！** DMZ 嚴禁主動向內網發起 TCP 握手連線 |\n| **TLS 1.3 金鑰交換** | 題目問 TLS 1.3 是否仍支援靜態 RSA 加密金鑰交換 | **已全面廢除！** 強制使用具備 PFS (完全前向保密) 之 Ephemeral Diffie-Hellman (DHE/ECDHE) |\n\n> 🔑 **防呆口訣**：\n> - AH 認證無加密，ESP 封裝才加密。\n> - SYN Flood 塞半開，Cookies 計算免耗台。\n> - DMZ 防火牆：外入有限度，內往外可通，DMZ 往內全面封！\n        ",
            "caseStudy": "【實務案例分析】某大型醫院對外掛號系統遭受巨量 TCP SYN Flood 攻擊，伺服器連線狀態表瞬間被數百萬個半開啟連線填滿，造成正常病患無法掛號。資安維運團隊緊急採取三合一措施：第一、在邊界次世代防火牆啟用 TCP SYN Proxy，阻絕偽造來源之無效交握；第二、在 Linux 伺服器核心開啟 `net.ipv4.tcp_syncookies = 1`，避免 TCB 記憶體枯竭；第三、啟用電信端清洗中心過濾非台灣境內異常網段，系統於 15 分鐘內恢復正常運作。"
          },
          {
            "id": "B1-M03",
            "title": "單元 3：作業系統與主機端點安全強化",
            "keywords": [
              "OS Hardening",
              "CIS Benchmark",
              "Windows GPO",
              "Linux Hardening",
              "Patch Management",
              "Privilege Escalation"
            ],
            "summary": "掌握 Windows Active Directory 與 Linux 主機安全性基準強化 (Baseline Hardening)、CIS Benchmark 控制項落實、弱密碼與帳號原則、SSH 安全組態、補丁管理生命週期與提權攻擊防範。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 作業系統安全強化四大核心維度\n1. **最小化受攻擊面 (Attack Surface Reduction)**：\n   - 停用或移除系統非必要之服務與應用（如 Telnet, FTP, Rexec, 關閉 SMBv1 協定）。\n   - 停用所有未授權之監聽連接埠 (Listening Ports)。\n2. **身分鑑別與特權存取控制**：\n   - 禁用預設帳號或將其更名（如停用 Guest 帳號，重命名 Administrator / root）。\n   - 嚴禁空密碼，強制設定高複雜度與歷史不可重複密碼原則。\n   - 設定帳戶鎖定閾值 (Account Lockout Threshold，例如 5 次失敗鎖定 30 分鐘)，阻斷暴力破解與密碼噴灑。\n3. **系統日誌與稽核追蹤**：\n   - 啟用成功與失敗之登入稽核 (Audit Logon Events)、權限使用稽核與特權提升追蹤。\n4. **軟體補丁生命週期 (Patch Management)**：\n   - 依據 CVSS 分數與在野利用情資 (CISA KEV)，在受控的測試環境驗證相容性後，以自動化工具 (WSUS, SCCM, Ansible) 於時限內發布至生產環境。\n\n#### 2. CIS Benchmarks 國際主機基準規範\n- 國際網際網路安全中心 (CIS) 為 Windows Server、RHEL、Ubuntu 等制訂之安全基準：\n  - **Level 1 基準**：基礎防護等級，提供必要安全性且對系統效能與應用程式相容性影響極低。\n  - **Level 2 基準**：高安全性環境（深度防禦），包含更嚴格的限制（可能限制部分相容性，適用機敏主機）。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux SSH 服務核心強化組態 (`/etc/ssh/sshd_config`)\n```bash\n# 禁止 root 透過 SSH 直接登入 (強制一般使用者登入後再 su/sudo)\nPermitRootLogin no\n# 禁用密碼認證，強制公鑰認證\nPasswordAuthentication no\nPubkeyAuthentication yes\n# 禁用空密碼\nPermitEmptyPasswords no\n# 限制最大認證嘗試次數 (防暴力破解)\nMaxAuthTries 3\n# 停用危險的 X11 轉發\nX11Forwarding no\n# 重啟服務生效\nsystemctl restart sshd\n```\n\n#### 2. Windows 帳號與安全原則 GPO 指令檢視\n```cmd\n:: 匯出目前本地安全策略配置進行稽核\nsecedit /export /cfg C:\\secpol_backup.inf\n:: 查詢本機當前密碼原則\nnet accounts\n:: 檢視當前所有監聽通訊埠與關聯進程 PID\nnetstat -ano | findstr \"LISTENING\"\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 考題情境與機制 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **更新管理流程** | 題目問「取得最新高危安全性修補程式後，第一步動作為何？」考生常誤選「立即推播更新全公司伺服器」 | **錯誤！第一步必須先在測試環境 (Test Environment) 驗證相容性**，確認無當機與服務衝突後方可排程部署上線 |\n| **SMBv1 協定** | 考題問防範 WannaCry 蠕蟲最根本的端點組態 | **徹底停用 SMBv1 協定並安裝 MS17-010 補丁**。SMBv1 存在嚴重遠端代碼執行 (RCE) 漏洞 |\n| **帳戶鎖定閥值** | 題目問設定帳戶鎖定是否萬無一失 | 注意「帳戶鎖定機制可能被攻擊者用作 DoS 阻斷服務攻擊（蓄意使合法使用者遭鎖定）」，需搭配鎖定時間自動解鎖與 IP 速率限制 |\n\n> 🔑 **防呆口訣**：\n> - 補丁先測再上線，空密預設全拔除。\n> - SSH 禁 root 密碼，GPO 強制長與複。\n> - 服務沒用立即關，SMBv1 永不再見！\n        ",
            "caseStudy": "【實務案例分析】某政府機關內部一台對外 Linux 伺服器遭受攻擊者透過 SSH 字典檔攻擊入侵。事後鑑識發現，該伺服器允許 `PermitRootLogin yes` 且使用預設密碼，未受限制之 SSH 服務被嘗試了 4 萬多次成功破門。資安改善小組全面依照 CIS Benchmark 進行強化：全面改採 ED25519 金鑰認證並關閉密碼登入、安裝 `fail2ban` 自動封鎖惡意嘗試 IP、移除非必要之 FTP/Telnet 服務，並配置每週自動掃描主機合規基準，杜絕同類資安缺口。"
          },
          {
            "id": "B1-M04",
            "title": "單元 4：常見資安威脅與惡意程式防護",
            "keywords": [
              "Ransomware",
              "Computer Worm",
              "Trojan Horse",
              "Spyware",
              "Rootkit",
              "Botnet",
              "Social Engineering",
              "BEC"
            ],
            "summary": "深入辨析各類惡意程式（Malware）之行為特徵與傳播模式：電腦蠕蟲自我複製、特洛伊木馬後門機制、勒索軟體雙重/三重勒索手腕、隱匿型 Rootkit、殭屍網路 (Botnet) 與商業電子郵件詐騙 (BEC) 社交工程防禦體系。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 惡意程式核心類別深度特徵對照\n1. **電腦蠕蟲 (Worm)**：\n   - *傳播特徵*：**具備高度自我複製與網路主動掃描傳播能力**。不需依附於宿主執行檔 (Host Program)，亦不需人為點擊觸發，利用作業系統或協定弱點（如 SMB, RPC）自主感染整座區網。\n   - *代表案例*：WannaCry, Conficker, SQL Slammer。\n2. **特洛伊木馬 (Trojan Horse)**：\n   - *傳播特徵*：偽裝成合法、有用或無害之應用軟體（如修圖軟體、遊戲外掛、發票 PDF），誘騙使用者主動下載並執行。執行後於背景植入後門 (Backdoor) 或連線 C2 伺服器。**不具備自主傳染複製能力**。\n3. **勒索軟體 (Ransomware)**：\n   - *演進模式*：\n     - *第一代 (加密勒索)*：本地高強度非對稱/對稱加密（AES + RSA），銷毀磁碟陰影複製 (Volume Shadow Copies)。\n     - *第二代 (雙重勒索 Double Extortion)*：加密前先將機敏資料竊取外傳 (Exfiltration)，威脅「不付贖金即公開於暗網洩密網站」。\n     - *第三代 (三重勒索 Triple Extortion)*：加密 + 外洩曝光 + 對其客戶發動 DDoS 或電話騷擾。\n4. **隱匿工具 (Rootkit)**：\n   - 運作於作業系統核心層 (Kernel Mode, Ring 0) 或韌體層，攔截作業系統 API，**將惡意進程、網路通訊埠與登錄檔在工作管理員與系統檢視器中完全隱形隱匿**。\n5. **殭屍網路 (Botnet)**：\n   - 數萬台受木馬感染的主機（殭屍節點 / Bot）受控於指令與控制伺服器 (C2 / Command and Control)，接受發起大規模 DDoS 攻擊或發送垃圾郵件。\n\n#### 2. 商業電子郵件詐騙 (BEC) 社交工程攻擊鏈\n- **攻擊模式**：攻擊者透過偽造寄件者位址 (Email Spoofing)、近音相似網域 (Typosquatting) 或盜用高層郵件帳號，精準鎖定財務主管或出納人員，下達緊急匯款至海外帳戶之指示。\n- **關鍵防禦政策**：涉及金錢轉帳或變更收款帳戶者，嚴格落實「雙人核可 (Dual Authorization)」與「離線電話雙向照會 (Out-of-band Verification)」。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Windows 端點排查惡意持續潛伏 (Persistence)\n```powershell\n# 檢視系統所有啟動項目 (Run Keys)\nGet-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\nGet-ItemProperty HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\n\n# 查詢所有排程工作是否存在異常外連腳本\nGet-ScheduledTask | Where-Object {$_.State -ne \"Disabled\"} | Select-Object TaskName, TaskPath, Actions\n```\n\n#### 2. 防範勒索軟體清空陰影複製之防護 (vssadmin 監控)\n```cmd\n:: 勒索軟體經典前置指令：\n:: vssadmin.exe delete shadows /all /quiet\n:: wmic shadowcopy delete\n:: 防護措施：透過 EDR 或 GPO 限制一般與管理使用者無預警執行 vssadmin.exe\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 惡意程式類型 | 考題常見混淆陷阱 | 官方標準正解判定 |\n| :--- | :--- | :--- |\n| **蠕蟲 vs 木馬** | 題目問「哪種惡意程式不需要宿主程式與人為介入即可自動在網路上擴散？」考生誤選木馬 | **蠕蟲 (Worm)**。木馬需靠偽裝誘騙點擊，病毒需宿主程式，唯有蠕蟲具獨立自我複製網路傳播能力 |\n| **Rootkit 偵測** | 以為一般工作管理員可以看到 Rootkit 進程 | **無法看到！** Rootkit 篡改了核心系統呼叫 (System Hooking)，必須透過乾淨離線系統 (Live CD) 進行底層映像比對 |\n| **釣魚防護** | 題目問防範 BEC 詐騙最佳方法，考生誤選「購買更高等級的防火牆」 | **程序規範 (SOP) 與多重管道照會**。社交工程直擊人性與商業流程，傳統防火牆無法判定信件內容文字之真實詐欺意圖 |\n\n> 🔑 **防呆口訣**：\n> - 蠕蟲無須人介入，自主爬網全感染。\n> - 木馬偽裝騙點擊，後門常開連 C2。\n> - 匯款信件莫輕信，第二管道打電話！\n        ",
            "caseStudy": "【實務案例分析】某高科技零組件製造商財務出納收到「董事長」從海外發來的緊急郵件，宣稱正在進行跨國併購機密談判，要求於當天下午三點前將 50 萬美元定金匯入指定香港銀行帳戶，並附上蓋有印鑑之合約影本。該出納察覺寄件者郵件網域結尾為 `.co` 而非公司正式的 `.com.tw` (近音網域欺騙)。出納秉持資安 SOP，撥打董事長隨行秘書之電話進行雙向照會，確認董事長根本未發出此信，成功攔阻了典型 BEC 商業社交工程詐騙。"
          },
          {
            "id": "B1-M05",
            "title": "單元 5：應用系統安全與 OWASP Top 10 核心漏洞",
            "keywords": [
              "SQL Injection",
              "XSS",
              "CSRF",
              "IDOR",
              "SSRF",
              "OWASP Top 10",
              "Prepared Statements"
            ],
            "summary": "掌握 Web 應用程式安全防護核心：深度剖析 OWASP Top 10 核心漏洞成因與防護。重點攻克 SQL 注入 (SQLi) 參數化查詢防護、跨網站腳本 (XSS) 輸出編碼與 HttpOnly Cookie、跨網站請求偽造 (CSRF) Token、不安全直接物件參照 (IDOR) 與 SSRF 漏洞。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 注入攻擊 (SQL Injection, SQLi) 深度剖析\n- **漏洞根因**：應用程式將來自外部不可信任的使用者輸入，直接以字串串接 (Concatenation) 方式拼裝至動態 SQL 語句中，導致直譯器將資料誤解析為程式指令執行。\n- **經典攻擊範例**：`SELECT * FROM users WHERE user = 'admin' AND pass = '' OR '1'='1';`\n- **防禦唯一解法**：**全面採用參數化查詢 (Parameterized Queries / Prepared Statements) 或 ORM**。資料與代碼在編譯期即分開解析，輸入值永遠僅被視為常數字串變數，絕不被當作語法執行。\n\n#### 2. 跨網站腳本 (Cross-Site Scripting, XSS)\n- **類別辨析**：\n  1. **儲存型 XSS (Stored XSS)**：惡意腳本存入資料庫（如留言板、使用者個人暱稱），每次任何受害者瀏覽該頁面時都會觸發執行。危害最大。\n  2. **反射型 XSS (Reflected XSS)**：惡意腳本包裝於 URL 查詢參數中，誘騙受害者點擊釣魚連結觸發。\n  3. **DOM-based XSS**：純前端客戶端 JavaScript 解析脆弱引起。\n- **縱深防護機制**：\n  - 情境感知輸出編碼 (Context-aware Output Encoding，將 `<` 轉為 `&lt;`，`>` 轉為 `&gt;`)。\n  - 對儲存 Session ID 的 Cookie 標記 **`HttpOnly`** 屬性（禁止 JavaScript 透過 `document.cookie` 讀取）。\n  - 配置內容安全策略 (Content Security Policy, CSP)。\n\n#### 3. 權限控制失效 (Broken Access Control)\n- **IDOR (不安全直接物件參照)**：\n  - 使用者存取 `GET /api/invoice?id=1001`，攻擊者直接改為 `id=1002` 即可看到其他客戶的發票。\n  - *防禦*：後端伺服器在執行查詢時，必須強制比對目前登入 Session 之 UserID 與目標資源之擁有者身分。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. 安全程式碼實戰：參數化查詢 vs 脆弱代碼\n```python\n# ❌ 極度脆弱的代碼 (易遭 SQL Injection)\ncursor.execute(f\"SELECT * FROM accounts WHERE username = '{user}' AND password = '{pwd}'\")\n\n# ✅ 官方推薦標準安全寫法 (Prepared Statements)\ncursor.execute(\"SELECT * FROM accounts WHERE username = %s AND password = %s\", (user, pwd))\n```\n\n#### 2. 關鍵 HTTP 安全回應標頭 (Security Response Headers)\n```http\n# 防止 XSS 竊取 Session Cookie\nSet-Cookie: session_id=xyz789; Secure; HttpOnly; SameSite=Strict\n\n# 防止點擊劫持 (Clickjacking)\nX-Frame-Options: DENY\n\n# 防止瀏覽器 MIME 混淆嗅探\nX-Content-Type-Options: nosniff\n\n# 強制 HTTPS 安全傳輸\nStrict-Transport-Security: max-age=31536000; includeSubDomains; preload\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| Web 漏洞類型 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **SQLi 防護** | 選項宣稱「在前端用 JavaScript 過濾單引號即能徹底防範 SQL 注入」 | **極度危險且無效！** 前端驗證可輕易被 Postman 或 Burp Suite 繞過，防護必須在**後端落實參數化查詢** |\n| **XSS vs CSRF** | 題目混淆兩者原理：CSRF 是竊取 Cookie 嗎？ | **不是！CSRF 是借刀殺人**（利用受害者已登入瀏覽器冒發合法請求），攻擊者**無法直接看到 Cookie**；竊取 Cookie 是 XSS |\n| **Cookie 安全標記** | 題目問防止跨站腳本偷取 Cookie 該下哪個 flag | **`HttpOnly`**（阻止 JS 存取）；`Secure` 是限 HTTPS 傳輸；`SameSite` 防 CSRF |\n\n> 🔑 **防呆口訣**：\n> - SQLi 剋星參數化，字串拼接必倒下。\n> - XSS 輸出要編碼，Cookie 必加 HttpOnly。\n> - CSRF 靠隨機 Token，IDOR 後端查權限！\n        ",
            "caseStudy": "【實務案例分析】某銀行行動網銀之繳費功能，其後端 API 原先設計為 `POST /pay { bill_id: 12345 }`，伺服器僅確認連線者已登入，未比對該 bill_id 是否屬於該登入帳號。滲透測試人員利用 IDOR 漏洞，遞增帳單編號遍歷扣繳了數十位其他顧客之帳戶款項。資安架構師隨後重新設計權限驗證中介軟體 (Middleware)：由後端 Session 取得使用者的 `account_id`，並在 SQL 查詢強制加入條件 `WHERE bill_id = ? AND owner_account_id = ?`，徹底消除了水平越權漏洞。"
          },
          {
            "id": "B1-M06",
            "title": "單元 6：密碼學基礎、對稱/非對稱與數位簽章",
            "keywords": [
              "Symmetric Encryption",
              "Asymmetric Encryption",
              "AES-256",
              "RSA",
              "ECC",
              "Hashing",
              "Digital Signature",
              "PKI"
            ],
            "summary": "掌握密碼學核心骨架：深入比較對稱式加密 (AES/ChaCha20) 與非對稱式加密 (RSA/ECC) 之數學特性、運算效能與金鑰分發；探討密碼學單向雜湊函數 (SHA-256/SHA-3)、HMAC 訊息驗證碼、數位簽章 (Digital Signature) 運作流程與 PKI 公開金鑰基礎架構之 X.509 憑證鏈。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 對稱式 vs 非對稱式加密全方位對照\n\n| 比較維度 | 對稱式加密 (Symmetric) | 非對稱式加密 (Asymmetric) |\n| :--- | :--- | :--- |\n| **金鑰機制** | 加密與解密共用同一把秘密金鑰 (Secret Key) | 成對的金鑰：公鑰 (Public Key) 公開，私鑰 (Private Key) 專屬保密 |\n| **代表演算法** | **AES (Rijndael)**, ChaCha20, 3DES (已淘汰) | **RSA**, **ECC (橢圓曲線密碼)**, Diffie-Hellman |\n| **運算速度** | **極快** (支援硬體 AES-NI 指令加速)，適合巨量資料 | **極慢** (牽涉大質數分解或離散對數)，約慢 1000 倍 |\n| **金鑰管理難題** | $n$ 個使用者互相通訊需 $\\frac{n(n-1)}{2}$ 把金鑰，分發極難 | $n$ 個使用者僅需 $2n$ 把金鑰 (每人一對公私鑰) |\n| **核心用途** | 檔案加密、資料庫欄位加密、大量資料傳輸通道加密 | 數位簽章、身分鑑別、金鑰交換 (Key Exchange) |\n\n#### 2. 雜湊函數 (Hash Function) 特性\n- **三大不可或缺特性**：\n  1. **單向性 (Pre-image Resistance)**：給定雜湊值 $H(M)$，在計算上不可逆推出原始明文 $M$。\n  2. **弱抗碰撞性 (Second Pre-image Resistance)**：給定特定明文 $M_1$，計算上不可能找到相異之 $M_2$ 使得 $H(M_1) = H(M_2)$。\n  3. **強抗碰撞性 (Collision Resistance)**：計算上不可能找到任何兩組相異明文 $M_1 \\neq M_2$ 使得 $H(M_1) = H(M_2)$。\n  4. **雪崩效應 (Avalanche Effect)**：明文哪怕只更動 1 個 bit，產出的雜湊摘要值至少有 50% 以上之位元發生劇烈改變。\n- 推薦標準：**SHA-256**, **SHA-512**, **SHA-3**；MD5 與 SHA-1 均已證實存在碰撞弱點，國際嚴格禁用。\n\n#### 3. 數位簽章 (Digital Signature) 運作流程\n- **簽署流程 (發送端 Alice)**：\n  1. 對原始文件計算雜湊值：$Digest = Hash(Message)$。\n  2. Alice 使用自己的「**Alice 私鑰 (Alice Private Key)**」對 Digest 加密，產出「數位簽章」。\n  3. 將原始文件連同數位簽章傳送給 Bob。\n- **驗證流程 (接收端 Bob)**：\n  1. Bob 使用「**Alice 公鑰 (Alice Public Key)**」解密該數位簽章，還原出原始 Digest A。\n  2. Bob 同步對收到的原始文件自行以相同演算法計算雜湊值，獲得 Digest B。\n  3. 若 Digest A == Digest B，則確認無誤！\n  - **達成三大安全目標**：**身分真實性 (Authenticity)**、**資料完整性 (Integrity)**、**不可否認性 (Non-Repudiation)**。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. OpenSSL 產生高強度密鑰與數位簽章\n```bash\n# 產生 ECC 橢圓曲線私鑰 (使用 prime256v1 曲線)\nopenssl ecparam -name prime256v1 -genkey -noout -out private_key.pem\n# 萃取對應之公開金鑰\nopenssl ec -in private_key.pem -pubout -out public_key.pem\n\n# 使用私鑰對合約檔案進行 SHA-256 數位簽章\nopenssl dgst -sha256 -sign private_key.pem -out contract.sig contract.pdf\n\n# 驗證數位簽章是否有效\nopenssl dgst -sha256 -verify public_key.pem -signature contract.sig contract.pdf\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 密碼學觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **金鑰使用角色** | 題目問「欲傳送機密訊息給 Bob，Alice 應使用何種金鑰加密？」考生常錯選 Alice 私鑰 | **正解：使用 Bob 的公鑰加密**。因為只有 Bob 自己的私鑰才能解開，方能保障機密性 |\n| **數位簽章金鑰** | 題目問「Alice 對合約簽章，應使用哪一把金鑰？」 | **正解：使用 Alice 的私鑰加密雜湊**。因為私鑰具唯一專屬性，其他人用 Alice 公鑰解開即可證明確為 Alice 所簽 |\n| **對稱金鑰長度** | 題目比較 AES-128、AES-256 與 RSA-2048 之安全強度 | **AES-128 與 RSA-2048 具備相近之安全強度 (約112~128 bits 安全等級)**；AES-256 具備抗量子前瞻安全性 |\n\n> 🔑 **防呆口訣**：\n> - 寄信保密：用「對方公鑰」加密，對方私鑰才能解！\n> - 簽名作保：用「自己私鑰」簽署，全世界公鑰來驗！\n> - 雜湊單向不可逆，雪崩效應防碰撞！\n        ",
            "caseStudy": "【實務案例分析】某跨國外商簽署電子採購訂單，供應商事後因原物料大漲企圖毀約，宣稱該訂單從未經其執行長簽署。法庭委託數位鑑識專家進行審查：專家調閱由公證 CA 機構簽發之執行長 X.509 憑證，並利用供應商公鑰成功解密訂單之 SHA-256 數位簽章，其雜湊比對百分之百相符，且時間戳記伺服器 (TSA) 證明簽署當時該憑證完全有效未被撤銷 (CRL/OCSP 驗證通過)。法官據此認定該電子簽章具備完全之法律「不可否認性」，判決供應商敗訴履約。"
          },
          {
            "id": "B1-M07",
            "title": "單元 7：存取控制模型與使用者認證技術",
            "keywords": [
              "DAC",
              "MAC",
              "RBAC",
              "ABAC",
              "MFA",
              "FIDO2",
              "OAuth 2.0",
              "SAML 2.0"
            ],
            "summary": "全面解析傳統與現代存取控制模型：自主存取控制 (DAC)、強制存取控制 (MAC/Bell-LaPadula)、基於角色 (RBAC) 與基於屬性 (ABAC) 存取控制。深入探討現代多因素驗證 (MFA) 三大要素、抗釣魚 FIDO2/WebAuthn 標準以及聯邦身分認證 (OAuth 2.0, OpenID Connect, SAML 2.0)。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 四大存取控制模型核心對照\n\n| 模型名稱 | 控制機制與決策依據 | 權限授權者 | 適用情境與特性 |\n| :--- | :--- | :--- | :--- |\n| **DAC (自主存取控制)** | 基於主體身分與檔案權限清單 (ACL) | **資源擁有者 (Owner)** 可自行決定將讀寫權限授予他人 | 彈性最高、集中管理最難。一般個人電腦 Windows NTFS / Linux 傳統權限 |\n| **MAC (強制存取控制)** | 基於安全標籤 (Security Labels) 與敏感度等級 (機密、極機密) | **系統中央安全策略**，使用者無權私自變更或轉交 | 安全等級最高。軍方、國防 (Bell-LaPadula 模型、SELinux) |\n| **RBAC (基於角色的存取控制)** | 基於組織中的業務職位指派「角色」，權限綁定角色 | **系統管理員** | 企業最廣泛採用。權限異動僅需調整使用者之角色歸屬 |\n| **ABAC (基於屬性的存取控制)** | 動態評估主體屬性、資源屬性與**環境情境屬性 (時間、IP、設備)** | **動態策略規則引擎 (Policy Engine)** | 零信任 (Zero Trust) 核心。可設定「非上班時間禁止下載」等細粒度條件 |\n\n#### 2. 多因素驗證 (Multi-Factor Authentication, MFA)\n- **三大獨立驗證維度（必須至少包含兩項不同類別，方稱 MFA）**：\n  1. **所知 (Something you know)**：密碼、PIN碼、圖形鎖。\n  2. **所持 (Something you have)**：硬體安全金鑰 (FIDO2/YubiKey)、手機 OTP Authenticator App、智慧IC卡。\n  3. **所具 (Something you are)**：指紋、虹膜、臉部辨識、靜脈特徵。\n- **防呆注意**：「密碼 + 提問母親生日」屬於同一類別 (所知 + 所知)，**不是 MFA**！\n- **NIST SP 800-63 建議**：SMS 簡訊與語音 OTP 易受 SIM 換卡 (SIM Swapping) 與 SS7 攔截攻擊，建議逐步淘汰，全面遷移至抗釣魚的 FIDO2 / Passkeys。\n\n#### 3. 現代聯邦身分驗證標準\n- **OAuth 2.0**：**授權框架 (Authorization)**，以 Access Token 授予第三方應用有限存取權（如授權 APP 存取 Google 雲端相簿，而不提供 Google 帳密）。\n- **OpenID Connect (OIDC)**：建立在 OAuth 2.0 之上的**身分認證層 (Authentication)**，回傳 ID Token (JWT 格式)。\n- **SAML 2.0**：基於 XML 的單一登入 (SSO) 標準，廣泛應用於大型企業與政府內部網域跨系統身分聯合。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux SELinux (MAC 強制存取控制) 狀態管理\n```bash\n# 查詢當前 SELinux 運作模式 (Enforcing, Permissive, Disabled)\ngetenforce\n# 檢視檔案的安全上下文 (Security Context)\nls -Z /var/www/html/index.html\n# 修正標籤還原預設 HTTP 存取策略\nrestorecon -Rv /var/www/html\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 認證與授權機制 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **雙密碼是否為 MFA** | 選項宣稱「輸入登入密碼後，再輸入提款卡提款密碼即符合 MFA」 | **錯誤！兩者皆為「所知 (Something you know)」**，必須跨越不同維度 (如密碼 + 實體卡片) |\n| **OAuth 2.0 本質** | 題目問「OAuth 2.0 協定的核心功能為何？」考生常誤選使用者身分認證 | **授權 (Authorization)**。OIDC 才是專職身分認證 (Authentication) |\n| **Bell-LaPadula 模型** | 題目考 BLP 模型的兩大規則 | **No Read Up (NRU 不得上讀高密級), No Write Down (NWD 不得下寫低密級)**，專注維護機密性 |\n\n> 🔑 **防呆口訣**：\n> - 存取控制四兄弟：DAC 自己作主，MAC 中央規定，RBAC 職位角色，ABAC 情境多變。\n> - MFA 必跨雙向：所知、所持、所具，缺一不可混為一談！\n        ",
            "caseStudy": "【實務案例分析】某跨國金融顧問公司高階主管在星巴克使用公共 Wi-Fi 辦公時，遭遇連線中間人釣魚網站。該網站精確仿冒了公司登入介面，誘騙主管輸入了帳號與密碼。然而，該機構全面推行了基於 FIDO2 WebAuthn 規範的實體硬體金鑰 (YubiKey)。由於 FIDO2 協定在瀏覽器層級將驗證憑證與當前存取的真實網域名稱強行綁定 (Origin Binding)，釣魚網域無法解鎖硬體金鑰回應，攻擊者取得的帳密瞬間失效，成功挫敗了進階憑證竊取攻擊。"
          },
          {
            "id": "B1-M08",
            "title": "單元 8：台灣資通安全管理法與個資保護概論",
            "keywords": [
              "Cybersecurity Management Act",
              "PDPA",
              "Incident Notification",
              "Critical Infrastructure",
              "Data Breach"
            ],
            "summary": "精準掌握我國《資通安全管理法》與《個人資料保護法》法規命令核心架構：主管機關權責、適用主體（公務機關與特定非公務機關）、責任等級劃分 (A~E 級)、資安事件 1 小時通報法定期限與 36 小時復原規範，以及個資法蒐集處理利用要件與外洩通知義務。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 我國《資通安全管理法》核心架構\n- **主管機關**：數位發展部 (資通安全署)。\n- **適用主體**：\n  1. **公務機關**：中央與地方各級行政、立法、司法機關與公立學校/公營事業。\n  2. **特定非公務機關**：\n     - **關鍵基礎設施提供者 (Critical Infrastructure, CI)**：能源、水資源、通訊傳播、交通、銀行與金融、緊急救援、高科技園區、醫療等八大領域。\n     - 公營事業、政府捐助之財團法人。\n- **資安責任等級劃分 (A 級至 E 級)**：\n  - **A 級 (最高)**：全國性機敏公務機關、八大 CI 關鍵提供者。要求：全機關導入 ISMS 並通過第三方驗證、自建或委外 SOC、每年辦理紅隊演練、專責資安主管與至少 4 名以上資安專職人員。\n  - **B 級**：直轄市級公務機關。至少配置 2 名資安專職人員。\n  - **C 級**：縣市公務機關。至少配置 1 名資安專職人員。\n- **資安事件通報與應變時限 (必考黃金數字！)**：\n  - 知悉資安事件後，**1 小時內** 必須於主管機關指定平台完成通報！\n  - 第三級與第四級重大事件，必須在 **36 小時內** 完成損害控制與系統復原作業，並於一個月內提出調查改善報告。\n\n#### 2. 我國《個人資料保護法》要點\n- **個資定義**：自然人之姓名、出生年月日、身分證統一編號、護照號碼、特徵、指紋、婚姻、家庭、教育、職業、病歷、醫療、基因、性生活、健康檢查、犯罪前科、聯絡方式、財務情況等。\n- **特種個人資料 (原則禁止蒐集，需符合嚴格法定事由)**：病歷、醫療、基因、性生活、健康檢查、犯罪前科。\n- **當事人五大權利**：查詢或請求閱覽、請求製給複製本、請求補充或更正、請求停止蒐集/處理/利用、**請求刪除**。\n- **個資外洩通知**：非公務機關發生個資被竊取、洩漏、竄改或其他侵害事故時，應查明後以適當方式「即時通知」當事人與中央目的事業主管機關。\n\n### 二、實務技術落地與通報流程 (Incident Workflow)\n\n```text\n【資安事件法定應變流程】\n[異常事件發生] \n      ↓\n[技術判定確認為資安事件] \n      ↓ ⏱️ 必須在知悉後 1 小時內！\n[通報至數位發展部資安通報平台 (EAP)] \n      ↓\n[評定事件等級 (一級~四級)] \n      ↓ ⏱️ 三/四級重大事件需於 36 小時內完成！\n[遏止控制、清除惡意程式、離線備份還原] \n      ↓\n[結案確認與檢討改善報告送審]\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 法規項目 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **通報時限** | 選項出現 24 小時、72 小時、半天等時限混淆 | **資安法通報一律為「知悉後 1 小時內」完成通報**；72 小時為歐盟 GDPR 外洩通報時限，不可混淆 |\n| **特種個資範疇** | 題目問哪一項不屬於特種個資：病歷、基因、犯罪前科、財務收入 | **財務收入是一般個資**；特種個資僅限：病歷、醫療、基因、性生活、健康檢查、犯罪前科六大項 |\n| **關鍵基礎設施領域** | 題目問八大關鍵基礎設施領域有哪些 | 能源、水資源、通訊傳播、交通、銀行與金融、緊急救援、高科技園區、醫療 (無娛樂、一般零售) |\n\n> 🔑 **防呆口訣**：\n> - 資安通報 1 小時，三四重大 36 復！\n> - 特種個資病醫基，性檢前科不可欺！\n> - 八大關鍵護國家，水電交通油氣銀！\n        ",
            "caseStudy": "【實務案例分析】某區域自來水公司監控系統 (SCADA) 遭勒索軟體感染，部分加壓站數值無法回傳。水廠資訊主管於上午 09:30 證實該異狀係駭客入侵造成（知悉事件）。主管立即於 10:15 (45 分鐘內) 透過數位發展部國家資通安全通報平台完成通報，並啟動緊急隔離措施。由於該水廠屬於我國「水資源關鍵基礎設施」，評定為第三級資安事件。應變團隊利用備份映像與手動水閥控制，於 22 小時內完成控制網段淨化與系統復原，符合法規知悉 1 小時通報與 36 小時復原要求。"
          }
        ]
      },
      {
        "subjectId": "B-SUB-2",
        "name": "考科二：資訊安全防護實務",
        "desc": "深入防火牆與次世代防護、端點偵測與回應 (EDR)、封包分析與異常流量診斷、弱點掃描評估、Syslog/Windows 事件日誌維運與 3-2-1 備份還原實務。",
        "modules": [
          {
            "id": "B2-M01",
            "title": "單元 1：防火牆、IDS/IPS 與次世代網路防護",
            "keywords": [
              "NGFW",
              "IDS",
              "IPS",
              "Stateful Inspection",
              "Packet Filtering",
              "WAF",
              "Deep Packet Inspection"
            ],
            "summary": "掌握網路邊界縱深防禦實務：解析封包過濾防火牆、狀態檢驗防火牆 (Stateful Inspection)、次世代防火牆 (NGFW App-ID/User-ID)、入侵偵測系統 (IDS) 旁路部署與入侵防禦系統 (IPS) 串聯阻斷、以及 WAF 應用層防護差異。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 防火牆演進與檢驗技術世代\n\n| 防火牆世代 | 運作 OSI 層次 | 檢驗核心機制 | 優缺點與防護盲點 |\n| :--- | :--- | :--- | :--- |\n| **傳統封包過濾 (Packet Filtering)** | 第 3/4 層 (網路/傳輸層) | 比對來源/目的 IP、Port 與 TCP Flags，無狀態紀錄 | 速度最快，但無狀態追蹤，無法防範偽造連線與高層攻擊 |\n| **狀態檢驗 (Stateful Inspection)** | 第 3/4/5 層 | 維護狀態表 (State Table)，動態追蹤 TCP 三向交握連線階段 | 僅允許合法發起之回程封包，有效阻斷異常外部注入 |\n| **次世代防火牆 (NGFW)** | 第 7 層 (應用層) | **深度封包檢驗 (DPI)**、**App-ID** 應用識別、**User-ID** 身分關聯 | 能辨識非標準 Port 運作之應用 (如偽裝成 443 的木馬)，可解密 SSL 檢驗 |\n\n#### 2. IDS (入侵偵測) vs IPS (入侵防禦) 關鍵架構差異\n- **IDS (Intrusion Detection System)**：\n  - *部署模式*：**旁路監聽 (Out-of-band)**，透過交換器之 Port Mirroring (SPAN) 或 Network TAP 複製封包進行分析。\n  - *作動機制*：被動分析。發現惡意特徵時發送警報 (Alert) 或向防火牆發送 TCP RST 封包，但**無法保證在第一時間即時丟棄 (Drop) 攻擊封包**。\n  - *優點*：零延遲、故障時完全不影響現有生產網路連線 (Fail-open)。\n- **IPS (Intrusion Prevention System)**：\n  - *部署模式*：**線上串聯 (Inline)**，所有流量實體或邏輯穿透 IPS 設備。\n  - *作動機制*：即時主動阻斷。一旦特徵或異常行為吻合，**直接在線丟棄惡意封包 (Drop Packet)** 並中斷連線。\n  - *缺點*：若設備故障可能導致網路全斷 (需具備 Bypass 旁路保護機制)，且深檢可能增加網路延遲。\n\n#### 3. WAF (網站應用程式防火牆) 專屬定位\n- 傳統防火牆與 IPS 專注於 L3/L4 網路層威脅；WAF 專注於 **OSI 第 7 層 HTTP/HTTPS 酬載**。\n- 專門解析 HTTP Request 中的 URI、Cookie、POST Body、Headers，專精防禦 SQL Injection、XSS、路徑遍歷與 CSRF。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux iptables 狀態檢驗防火牆規則範例\n```bash\n# 預設原則全部丟棄\niptables -P INPUT DROP\niptables -P FORWARD DROP\niptables -P OUTPUT ACCEPT\n\n# 允許本機回環連線\niptables -A INPUT -i lo -j ACCEPT\n\n# 狀態檢驗核心：放行已建立 (ESTABLISHED) 與相關聯 (RELATED) 之回程連線\niptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT\n\n# 僅對特定內網網段開放 SSH Port 22\niptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 22 -m conntrack --ctstate NEW -j ACCEPT\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 設備類型 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **IDS 能否即時阻斷** | 選項宣稱「IDS 可以即時在第一封包阻斷惡意攻擊」 | **錯誤！IDS 採旁路監聽只能報警**，只有串聯部署的 **IPS** 才能即時丟棄封包阻斷連線 |\n| **NGFW vs WAF** | 考題問防範 Web 伺服器 SQL 注入最佳專屬設備 | **首選 WAF (網站應用程式防火牆)**，因其對 HTTP 協定與 Web Payload 具最深度之解碼防護能力 |\n| **IPS 誤報 (False Positive)** | 題目問 IPS 誤報率過高會造成什麼後果 | **將合法業務流量誤判阻斷，導致正常服務不可用 (業務中斷)** |\n\n> 🔑 **防呆口訣**：\n> - IDS 旁路聽，報警不能擋；IPS 串線上，當場丟封包！\n> - 傳統看 Port 號，次代深檢到第七；Web 專武找 WAF，防杜 SQL 與 XSS！\n        ",
            "caseStudy": "【實務案例分析】某線上商城在週年慶促銷期間，前端 Web 伺服器遭受分散式 Slowloris 緩慢 HTTP 拒絕服務攻擊與大量偽裝成合法購物請求的 SQL 注入。企業架構師實施聯防策略：在最外層部署次世代防火牆 (NGFW) 阻絕 L3/L4 之異常連線速率；在 Web 伺服器前緣串聯部屬 WAF，啟用 OWASP Core Rule Set (CRS)，精準過濾夾帶單引號與聯集查詢之惡意 HTTP POST 參數。攻擊流量在毫秒級內被 WAF 攔截並回傳 403 Forbidden，後端資料庫完全未受干擾，保障了數億元促銷交易安全進行。"
          },
          {
            "id": "B2-M02",
            "title": "單元 2：端點防護、次世代防毒與 EDR 實務",
            "keywords": [
              "EDR",
              "NGAV",
              "Telemetry",
              "LOLBins",
              "Application Whitelisting",
              "USB Control"
            ],
            "summary": "掌握端點安全防禦演進：傳統特徵碼防毒 (AV) 到行為分析 (NGAV) 與端點偵測回應 (EDR)；探討端點遙測資料收集、親代子進程樹 (Process Tree)、生活離地二進位檔 (LOLBins) 濫用、Windows AppLocker 白名單與周邊儲存設備管制。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 端點防護演進世代對照\n\n| 防護維度 | 傳統防毒軟體 (Legacy AV) | 次世代防毒 (NGAV) | 端點偵測與回應 (EDR) |\n| :--- | :--- | :--- | :--- |\n| **偵測機制** | **靜態特徵碼比對 (Signatures)** | 啟發式 (Heuristics) + 本地/雲端機器學習行為模型 | **持續端點遙測 (Telemetry)** + 行為異常分析 + 威脅獵捕 |\n| **核心防護焦點** | 已知已知 (Known-Knowns) 檔案型病毒 | 已知惡意行為、記憶體注入探測 | **未知威脅、無檔案攻擊 (Fileless)、進階持續威脅 (APT)** |\n| **回應能力** | 自動刪除或隔離受感染檔案 | 阻斷惡意進程執行 | **遠端網路隔離端點、遠端終止進程、現場鑑識採證、獵捕軌跡** |\n\n#### 2. 無檔案惡意程式 (Fileless Malware) 與 LOLBins 濫用\n- **無檔案攻擊原理**：攻擊者不將實體 EXE 惡意檔案寫入受害者硬碟，而是直接將惡意 Payload 注入至合法記憶體進程（如 `explorer.exe`, `lsass.exe`），或直接利用系統內建工具執行腳本。\n- **LOLBins (Living off the Land Binaries)**：\n  - 攻擊者濫用作業系統合法的微軟已簽名工具進行攻擊：例如利用 `powershell.exe` 下載載具、利用 `certutil.exe -urlcache -split -f` 下載木馬、利用 `mshta.exe` 執行遠端腳本。\n  - 傳統防毒因檔案具有合法微軟數位簽名而直接放行，唯有 EDR 分析「進程親緣樹異常（例如 `WINWORD.EXE` 衍生啟動 `powershell.exe`）」才能即時示警。\n\n#### 3. 應用程式白名單 (Application Whitelisting)\n- 遵循零信任與預設拒絕 (Default Deny) 理念：**除了明確列入白名單的信任程式外，其餘所有程式一律禁止執行**。\n- 代表技術：Windows Defender Application Control (WDAC), AppLocker。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. PowerShell 檢視異常進程樹與出連\n```powershell\n# 檢視目前所有由 Office 軟體 (Word/Excel) 派生之子進程 (典型釣魚特徵)\nGet-CimInstance Win32_Process | Where-Object {\n    $_.ParentProcessId -in (Get-Process winword, excel -ErrorAction SilentlyContinue).Id\n} | Select-Object ProcessId, Name, CommandLine\n\n# 查詢特定 PID 之外部網路連線\nGet-NetTCPConnection -OwningProcess 4088 | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State\n```\n\n#### 2. 群組原則 (GPO) 停用抽取式磁碟存取 (USB 管制)\n```text\n電腦設定 -> 系統管理範本 -> 系統 -> 抽取式存放裝置存取權：\n啟用【所有抽取式存放裝置類別：拒絕所有存取權】(Deny all access)\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 端點防護觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **EDR 核心價值** | 題目問「EDR 與傳統防毒最大差異為何？」 | **提供持續的端點行為遙測、可視性、調查鑑識與即時網路隔離能力**，而不僅依賴靜態特徵碼 |\n| **無檔案攻擊應對** | 選項宣稱「定時執行硬體磁碟掃毒可徹底清除無檔案病毒」 | **錯誤！無檔案惡意程式常駐於 RAM 記憶體與登錄檔中**，必須透過記憶體鑑識與 EDR 行為監控處置 |\n| **白名單 vs 黑名單** | 題目問何種策略對未知零日漏洞 (Zero-day) 抵抗力最高 | **應用程式白名單 (Default Deny)**。黑名單只能阻擋已知威脅 |\n\n> 🔑 **防呆口訣**：\n> - 傳統特徵比名片，次代 EDR 盯動線。\n> - Word 開 PowerShell 大可疑，LOLBins 濫用無所匿。\n> - 白名單預設全不准，端點隔離秒阻斷！\n        ",
            "caseStudy": "【實務案例分析】某跨國製造廠一名工程師開啟一封假冒發票的電子郵件，信中附件巨集在背景神不知鬼不覺地調用 `certutil.exe` 下載加密酬載並注入至記憶體中。傳統防毒因檔案不落地完全未跳出任何警告。然而，端點 EDR 立即捕捉到遙測異常：Office 進程派生非標準子進程，且向未受信任的境外伺服器發起 TLS 握手。EDR 在 0.8 秒內自動終止可疑進程樹，並觸發「網路隔離」，使該工作站與內網其他電腦完全隔絕，成功在勒索軟體橫向擴散前掐滅危機。"
          },
          {
            "id": "B2-M03",
            "title": "單元 3：網路流量監控、封包分析與異常連線診斷",
            "keywords": [
              "Wireshark",
              "Packet Analysis",
              "NetFlow",
              "Beaconing Detection",
              "ARP Spoofing",
              "DNS Tunneling"
            ],
            "summary": "掌握 Wireshark 抓包過濾語法、網路流量 NetFlow/IPFIX 收集、TCP 三向交握異常排查、ARP 欺騙偵測、惡意程式心跳回連 (Beaconing) 流量診斷與 DNS 穿隧 (DNS Tunneling) 外洩萃取分析。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 深度封包檢測 (PCAP) vs 網路流 (NetFlow/IPFIX)\n- **完整封包擷取 (Full Packet Capture, PCAP)**：\n  - *特性*：儲存完整封包標頭與有效酬載 (Payload)。\n  - *用途*：微觀鑑識、惡意代碼逆向、還原傳輸檔案。缺點為儲存空間消耗極為巨大。\n- **網路流 (NetFlow / IPFIX / sFlow)**：\n  - *特性*：**僅記錄連線元數據 (Metadata)**：來源/目的 IP、來源/目的 Port、通訊協定、封包數量、傳輸位元組、時間戳記與 TCP Flags。\n  - *用途*：巨觀流量趨勢、異常大流量外傳偵測、DDoS 監控、網路拓撲效能分析。\n\n#### 2. 常見網路異常流量特徵模式\n1. **ARP 欺騙 (ARP Spoofing / Poisoning)**：\n   - *特徵*：同一個 IP 位址（如預設閘道 Gateway）在短時間內出現不同的 MAC 位址變更，或頻繁收到非請求的廣播 ARP 回應 (Gratuitous ARP Reply)。\n2. **C2 惡意連線心跳 (Beaconing)**：\n   - *特徵*：內部受害端點每隔固定間隔時間（如精確每 60 秒）或固定時間加上些微抖動 (Jitter)，向外部未知 IP 發起細小的 HTTP POST / DNS 請求。\n3. **DNS 穿隧 (DNS Tunneling)**：\n   - *特徵*：大量畸長且看似隨機編碼的子網域查詢（如 `a8f9c1b2.data.attacker.com`），TXT 紀錄回應異常龐大，利用 DNS Port 53 穿透企業防火牆外洩機密。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Wireshark 官方考試必備 Display Filters 過濾語法\n```text\n# 1. 尋找 TCP 三向交握的初始 SYN 封包 (連線發起)\ntcp.flags.syn == 1 && tcp.flags.ack == 0\n\n# 2. 尋找被阻斷或異常重設之連線 (RST 封包)\ntcp.flags.reset == 1\n\n# 3. 搜尋特定 IP 且排除 DNS 廣播流量\nip.addr == 192.168.1.50 && !dns\n\n# 4. 偵測 HTTP POST 請求 (常見於登入與資料外傳)\nhttp.request.method == \"POST\"\n\n# 5. 檢視包含特定字串的 DNS 請求\ndns.qry.name contains \"malicious\"\n```\n\n#### 2. Linux tcpdump 現場快速抓包指令\n```bash\n# 抓取介面 eth0 上目的地為 Port 80/443 的前 100 個封包並寫入檔案\ntcpdump -i eth0 -nn \"tcp port 80 or tcp port 443\" -c 100 -w /tmp/traffic.pcap\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 流量異常類型 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **SYN Flood 封包特徵** | 選項出現「巨量 ACK 且無 SYN」 | **錯誤！SYN Flood 特徵是巨量 SYN 且無後續 ACK**，導致伺服器半開隊列爆滿 |\n| **DNS 穿隧辨識** | 題目問為何防火牆沒擋下資料外洩？ | 因為防火牆放行內部對外之 **UDP 53 (DNS 查詢)**，攻擊者將資料 Base64 編碼藏在子網域中外傳 |\n| **ARP 欺騙根因** | 考題問 ARP 協定最大安全缺陷為何？ | **無認證機制 (Stateless)**，節點無條件信任收到的 ARP Reply 並更新本機 ARP 快取表 |\n\n> 🔑 **防呆口訣**：\n> - 封包分析 Wireshark，SYN==1 握手來。\n> - 定時外傳是心跳，長子網域名是穿隧。\n> - IP 同一 MAC 變，定是 ARP 鬼搗亂！\n        ",
            "caseStudy": "【實務案例分析】SOC 監控團隊透過 NetFlow 分析發現，研發部門一台非伺服器工作站，連續三天在每日凌晨 03:00 整準時向烏克蘭境內一處 IP 發起約 8GB 的 UDP 連線。分析師立即調閱端點 PCAP 封包進行深度檢測，發現攻擊者利用了 DNS 穿隧工具將企業晶片設計圖拆解壓縮編碼外傳。資安團隊在核心交換器與邊界防火牆立即封鎖該 C2 網域與境外 IP，並透過 EDR 溯源清除端點木馬，成功攔截了智慧財產權外流。"
          },
          {
            "id": "B2-M04",
            "title": "單元 4：弱點掃描、漏洞評估與修補排程實務",
            "keywords": [
              "Vulnerability Assessment",
              "Nessus",
              "CVE",
              "CVSS v3.1",
              "CISA KEV",
              "Patch Management"
            ],
            "summary": "掌握企業弱點掃描 (VA) 實作流程：深入比較認證掃描 (Credentialed) 與無認證掃描 (Non-credentialed)、CVE 識別體系、CVSS v3.1 評分度量維度、CISA 已知利用漏洞清單 (KEV) 與排程修補優先級制定實務。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 弱點掃描模式深度對比\n\n| 掃描方式 | 運作原理與權限 | 偵測深度與優點 | 限制與缺點 |\n| :--- | :--- | :--- | :--- |\n| **無認證掃描 (Unauthenticated Scan)** | 從外部網路對標的主機進行 Port 掃描與服務指紋識別 | 模擬外部黑客視角，無須主機密碼，適合評估邊界暴露面 | 僅能探測公開服務表面，無法深入底層系統組態，誤報率較高 |\n| **認證掃描 (Credentialed Scan)** | 提供合法特權帳號 (SSH / Windows WMI) 供掃描器登入 | **深入作業系統內部**，檢視已安裝套件、註冊表設定、補丁缺失，**精確度極高** | 需管理與授權帳號憑證，對受測主機產生微量運算負載 |\n\n#### 2. CVSS v3.1 評分系統與嚴重度劃分\n- **三大評分度量衡**：\n  1. **基本度量 (Base Metrics)**：漏洞本身固有的恆定特性（攻擊向量 AV、複雜度 AC、權限需求 PR、使用者互動 UI、範圍 S、機密性/完整性/可用性衝擊 C/I/A）。\n  2. **時間度量 (Temporal Metrics)**：隨時間演變的特性（漏洞利用成熟度 E、修補層級 RL、確認度 RC）。\n  3. **環境度量 (Environmental Metrics)**：特定組織內部之特殊環境與補償控制。\n- **基本分級標準 (必背！)**：\n  - **Critical (緊急)**：**9.0 ~ 10.0** (通常具備遠端無授權代碼執行 RCE 特性)。\n  - **High (高)**：**7.0 ~ 8.9**。\n  - **Medium (中)**：**4.0 ~ 6.9**。\n  - **Low (低)**：**0.1 ~ 3.9**。\n  - **None**：**0.0**。\n\n#### 3. 修補優先級決定矩陣 (Vulnerability Prioritization)\n- 切勿盲目僅依 CVSS 基本分數排程！應結合 **威脅情資 (Threat Intelligence)**：\n  - 檢視 **CISA KEV (Known Exploited Vulnerabilities Catalog)**：若該漏洞已被黑客武器化並在野積極利用，即使 CVSS 僅為 7.5，修補優先級亦應提升至最高！\n\n### 二、實務技術落地與排程規範 (Patching Policy)\n\n```text\n【企業漏洞修補標準 SLA 範本】\n- Critical (CVSS 9.0~10.0 或已在野利用)：接獲通報後 24~48 小時內完成測試與上線。\n- High (CVSS 7.0~8.9)：7 天至 14 天內完成修補。\n- Medium (CVSS 4.0~6.9)：30 天至 60 天內隨定期維護視窗更新。\n- Low (CVSS 0.1~3.9)：下一季定期維護或併同年度作業系統大版本升級。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 弱點評估觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **弱掃 vs 滲透測試** | 題目混淆弱點掃描 (VA) 與滲透測試 (PT) | **弱掃是廣度自動化工具盤點漏洞**；**滲透測試是由人工模擬駭客思維進行深度概念驗證 (PoC) 與複合式弱點串連利用** |\n| **認證掃描之優勢** | 選項宣稱「無認證掃描比認證掃描更精確」 | **完全相反！** 認證掃描能登入主機比對套件版號與註冊表，精確度遠高於無認證掃描 |\n| **CVSS 嚴重性切分** | 題目問 CVSS 8.5 屬於哪一等級 | **High (高)**。9.0 以上才是 Critical (緊急) |\n\n> 🔑 **防呆口訣**：\n> - 弱掃自動盤漏洞，滲透人工串攻擊。\n> - 認證掃描登入看，註冊表裡見真章。\n> - 9 分以上叫緊急，在野利用搶先補！\n        ",
            "caseStudy": "【實務案例分析】某大型金控進行每季全資產弱點掃描，產出報告高達 1,200 個漏洞。資訊長原要求團隊按順序修補，導致 IT 人員疲於奔命。資安長介入建立動態優先權架構：首先交叉比對 CISA KEV 與火線情資，鎖定其中 8 個已有公開武器化 Exploit 且對外公開之 Apache/OpenSSL 漏洞 (CVSS >= 9.0)，要求 48 小時內全員動員修補；其餘內部網段之中低風險漏洞排入例行月維護。成功以最少人力精準封堵最致命之破口。"
          },
          {
            "id": "B2-M05",
            "title": "單元 5：日誌收集、集中分析與基礎稽核維運",
            "keywords": [
              "Syslog",
              "Windows Event Log",
              "NTP Synchronization",
              "WORM Storage",
              "Log Retention",
              "Audit Trails"
            ],
            "summary": "掌握資安稽核日誌 (Audit Logs) 黃金管理準則：Syslog 協定、Windows Security Event ID 關鍵事件解碼、全網 NTP 毫秒校時、單寫多讀 (WORM) 唯讀不可篡改、我國資安法法定 180 天留存與中央集中管理機制。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 日誌管理四大支柱規範\n1. **即時集中轉發 (Centralized Collection)**：\n   - 伺服器與網路設備本地日誌易在主機遭駭時被攻擊者抹除。必須透過 Syslog (RFC 5424) 或 Windows Event Forwarding (WEF) 即時將日誌轉發至獨立隔離的專屬日誌伺服器或 SIEM。\n2. **全網時間同步 (NTP Synchronization)**：\n   - 所有伺服器、防火牆、交換器與資料庫，必須強制與內部權威 NTP 時間伺服器同步。時間戳記若不一致，鑑識調查時將無法重構事件時序鏈。\n3. **資料不可竄改性 (WORM & Hash Integrity)**：\n   - 採用「單寫多讀 (Write Once, Read Many)」存儲媒體或具備加密簽章之雲端物件鎖 (Object Lock)。日誌寫入後，即便是網域最高管理員 (Domain Admin) 亦無權修改或刪除。\n4. **法規留存期限 (Log Retention)**：\n   - 我國《資通安全管理法》明文規定：關鍵資訊系統之**日誌紀錄至少必須完整保存 180 天 (半年) 以上**；金融相關法規更要求核心日誌保存 1 年至 5 年。\n\n#### 2. Windows 必考重要安全事件識別碼 (Security Event IDs)\n\n| Event ID | 事件名稱與意義 | 鑑識與分析核心重點 |\n| :--- | :--- | :--- |\n| **`4624`** | 帳戶成功登入 (An account was successfully logged on) | 檢查 **Logon Type**：<br>• Type 2：互動式本機鍵盤登入<br>• Type 3：網路連線登入 (如 SMB/共享)<br>• Type 10：遠端桌面 (RDP) 登入 |\n| **`4625`** | 帳戶登入失敗 (An account failed to log on) | **暴力破解 (Brute-force) 或密碼噴灑 (Password Spraying)** 核心特徵，短時間大量出現即為警報 |\n| **`4720`** | 建立新使用者帳號 (A user account was created) | 攻擊者取得權限後建立後門帳號之行為 |\n| **`1102`** | 安全稽核日誌遭手動清除 (The audit log was cleared) | **極度危險指標！** 攻擊者執行 `wevtutil cl security` 企圖湮滅證據 |\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. PowerShell 快速查詢異常登入失敗與日誌清除\n```powershell\n# 查詢過去 24 小時內所有登入失敗 (4625) 的來源 IP 與目標帳號\nGet-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddDays(-1)} | \n    ForEach-Object {\n        $xml = [xml]$_.ToXml()\n        [PSCustomObject]@{\n            Time = $_.TimeCreated\n            User = $xml.Event.EventData.Data | Where-Object {$_.Name -eq \"TargetUserName\"} | Select-Object -ExpandProperty '#text'\n            IP   = $xml.Event.EventData.Data | Where-Object {$_.Name -eq \"IpAddress\"} | Select-Object -ExpandProperty '#text'\n        }\n    } | Format-Table -AutoSize\n\n# 檢測安全日誌是否被惡意清空 (Event ID 1102)\nGet-WinEvent -FilterHashtable @{LogName='Security'; Id=1102} -ErrorAction SilentlyContinue\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 日誌維運觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **法定保存期限** | 題目問資通安全管理法要求系統軌跡紀錄至少保存幾天？ | **至少 180 天 (約半年)**。常以 30 天、90 天作為干擾誘答項 |\n| **NTP 時間誤差** | 題目問為何不同設備日誌無法進行事件關聯分析 | **未落實 NTP 時間校時**，導致各設備時間偏差數分鐘甚至數小時，時序被打亂 |\n| **4624 登入類型** | 題目問遠端桌面 (RDP) 登入在 Event ID 4624 中標示為哪種類型？ | **Logon Type 10 (RemoteInteractive)**；Type 2 為本地 Console；Type 3 為網路連線 |\n\n> 🔑 **防呆口訣**：\n> - 4624 成功進，4625 失敗停。\n> - 4720 偷建號，1102 抹日誌（最危險！）。\n> - 集中轉發防毀證，NTP 校時保一致，法規保存 180！\n        ",
            "caseStudy": "【實務案例分析】某政府機關半夜遭 APT 攻擊者滲透，攻擊者提權至本機 Administrator 後，立即在命令提示字元執行 `wevtutil cl Security` 指令清除所有本機安全日誌，企圖令鑑識小組無跡可尋。所幸該機關遵照規範落實了「集中日誌轉發」：本地日誌在生成的幾毫秒內已透過 Syslog TLS 即時轉發至獨立的 SIEM 儲存庫。本地記錄雖被清空，但在 SIEM 端立即觸發了「Event ID 1102 日誌清除警報」與完整的攻擊溯源軌跡，值班資安人員在 5 分鐘內完成受害主機隔離。"
          },
          {
            "id": "B2-M06",
            "title": "單元 6：資料備份、還原演練與 3-2-1 原則實務",
            "keywords": [
              "3-2-1 Backup Rule",
              "Immutable Backup",
              "RTO",
              "RPO",
              "Full Backup",
              "Incremental Backup",
              "Differential Backup"
            ],
            "summary": "徹底落實資料備份與災難復原架構：經典 3-2-1 鐵律與現代 3-2-1-1-0 擴充規範、完整備份 (Full)、增量備份 (Incremental) 與差異備份 (Differential) 差異對決、不可竄改快照 (WORM/Air-gap) 與定期實體還原演練驗證。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 經典 3-2-1 備份鐵律與現代擴充\n- **經典 3-2-1 原則**：\n  - **3 份資料複本**：1 份原始生產資料 + 2 份獨立備份複本。\n  - **2 種不同存儲媒介**：避免單一媒介共通硬體瑕疵（如磁碟陣列 SAN + 磁帶 LTO 或雲端儲存）。\n  - **1 份異地保存 (Off-site)**：遠離本地災區（防範火災、水災、地震）。\n- **現代 3-2-1-1-0 擴充規範 (專門對抗勒索軟體)**：\n  - 額外增加 **1 份離線 (Offline) 或不可變 (Immutable / Air-gapped)** 備份：採用實體隔離或 WORM 物件鎖定，防範連網備份磁碟被勒索軟體同時加密。\n  - 達成 **0 錯誤還原 (Zero recovery errors)**：定期進行開機還原測試演練，未經驗證還原的備份視為無效備份。\n\n#### 2. 三大備份模式全方位深度對照\n\n| 備份模式 | 備份資料範圍定義 | 備份耗時與空間 | 災難還原所需步驟與耗時 |\n| :--- | :--- | :--- | :--- |\n| **完整備份 (Full Backup)** | 備份目標系統的所有選定資料 | 耗時**最長**，佔用空間**最大** | **最快最簡單**。僅需最後一份完整備份即可直接還原 |\n| **差異備份 (Differential)** | 僅備份自「**上一次完整備份**」後所有異動的資料 | 耗時與空間適中 (隨時間累積增大) | 還原快速。需：**最後一次完整備份 + 最後一次差異備份** (共2份) |\n| **增量備份 (Incremental)** | 僅備份自「**上一次任意備份** (完整或增量)」後異動的資料 | 耗時**最短**，佔用空間**最小** | **還原最慢且繁瑣**。需：最後完整備份 + 其後所有增量備份依序還原，任一增量損毀即可能中斷 |\n\n#### 3. 業務復原核心指標：RTO vs RPO\n- **RTO (復原時間目標, Recovery Time Objective)**：中斷事件發生後，系統**必須恢復上線服務之最大容許時間**（重視復原速度）。\n- **RPO (復原點目標, Recovery Point Objective)**：組織**可容許損失資料的最大時間跨度**（重視資料新鮮度，決定備份頻率）。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux rsync 異地增量鏡像備份指令\n```bash\n# 使用 rsync 進行異地增量同步 (保持屬性、排除暫存目錄、刪除來源已不存在檔案)\nrsync -avz --delete --exclude='*.tmp' /var/www/data/ backupuser@192.168.20.100:/backup/data/\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 備份觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **還原差異 vs 增量** | 題目問「週日做完整備份，週一至週四做增量備份，週五毀損需拿幾份還原？」 | **正解：需拿週日完整 + 週一、週二、週三、週四共 5 份**！若為差異備份則僅需週日完整 + 週四差異共 2 份 |\n| **不可篡改性 (Air-gap)** | 題目問「為何 NAS 本地定期備份在勒索攻擊中常全軍覆沒？」 | 因為備份主機仍**連網且共用網域憑證**，駭客提權後直接將連網備份一併格式化；必須有**實體離線 (Air-gapped) 或 Immutable** 複本 |\n| **RPO 概念** | 題目問「某系統每 4 小時備份一次，其 RPO 為何？」 | **RPO 為 4 小時**（最壞情況下損失過去 4 小時之交易資料） |\n\n> 🔑 **防呆口訣**：\n> - 3-2-1 鐵律記：3 複本、2 媒介、1 異地、加 1 離線 0 差錯！\n> - 完整備份還原快，增量省位還原慢，差異適中拿兩塊。\n> - RTO 看修復時間，RPO 看資料遺失容許線！\n        ",
            "caseStudy": "【實務案例分析】某高科技封測廠產線資料庫半夜遭遇勒索軟體全盤加密，連同連網備份伺服器亦遭攻擊者以管理員權限格式化。此時 IT 團隊啟動終極 BCP 計畫：該廠落實了「3-2-1-1-0」原則，每逢週五均將資料寫入實體磁帶 (LTO Tape) 並由專人運送至遠端銀行保險庫實體離線保存 (Air-gap)。團隊自保險庫取出磁帶，配合乾淨新主機在 18 小時內完成全廠系統重建，成功於 RTO 時限內復原，未支付巨額贖金。"
          },
          {
            "id": "B2-M07",
            "title": "單元 7：社交工程防禦與企業資安意識演練",
            "keywords": [
              "Phishing Simulation",
              "Spear Phishing",
              "Watering Hole Attack",
              "SPF",
              "DKIM",
              "DMARC",
              "Security Awareness"
            ],
            "summary": "掌握企業社交工程防護全貌：魚叉式釣魚 (Spear Phishing)、鯨釣 (Whaling)、水坑攻擊 (Watering Hole)、商業電子郵件詐騙 (BEC)；深入解析郵件網域身分鑑別三巨頭 SPF、DKIM、DMARC 協定原理與 DNS 配置實務，以及企業社交工程演練標準程序。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 社交工程進階攻擊型態對照\n1. **魚叉式釣魚 (Spear Phishing)**：\n   - 針對特定人員或部門（如人資、財務、研發），事先蒐集社交媒體與公開資訊，量身訂製高度逼真之郵件內容與誘餌檔案。\n2. **水坑攻擊 (Watering Hole Attack)**：\n   - 駭客不直接攻擊防禦森嚴之目標企業，而是先調查該企業員工經常造訪的第三方合法網站（如產業技術論壇、供應商入口），將其攻陷並植入瀏覽器零日漏洞攻擊程式，等候目標員工連線造訪時中招。\n3. **商業電子郵件詐騙 (BEC / CEO Fraud)**：\n   - 偽裝高階主管或合作廠商，利用急迫性與權威心理，繞過正式簽核流程騙取財務人員匯款。\n\n#### 2. 電子郵件防偽三巨頭協定深度解析\n1. **SPF (寄件者政策框架, Sender Policy Framework)**：\n   - 網域擁有者在 DNS 發布 TXT 紀錄，**列明哪些伺服器 IP 位址有權代表該網域發送郵件**。收件伺服器比對發信來源 IP 是否列於清單中。\n2. **DKIM (網域金鑰識別郵件, DomainKeys Identified Mail)**：\n   - 發信伺服器以「私鑰」對郵件標頭與內容計算數位簽章 (DKIM-Signature Header)；收信端向寄信網域的 DNS 查詢「公鑰」驗證簽章，**確保郵件在傳輸過程中未遭竄改**。\n3. **DMARC (網域型訊息鑑別、報告與一致性)**：\n   - 整合 SPF 與 DKIM。網域擁有者定義當 SPF 或 DKIM 驗證失敗時，收件方應採取的處置策略：\n     - `p=none`：僅監控回報，不攔截。\n     - `p=quarantine`：隔離至垃圾郵件箱。\n     - **`p=reject`**：**最嚴格防護，直接拒收並丟棄偽冒郵件**。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. DNS 電子郵件安全防偽 TXT 紀錄配置範例\n```text\n# 1. SPF 紀錄：僅允許自身 MX 紀錄與特定 IP 代表發信，其餘嚴格拒絕 (-all)\nexample.com.   IN TXT \"v=spf1 mx ip4:203.0.113.10 -all\"\n\n# 2. DMARC 紀錄：強制要求嚴格拒收偽冒郵件，並將聚合報告寄至資安郵箱\n_dmarc.example.com. IN TXT \"v=DMARC1; p=reject; pct=100; rua=mailto:dmarc-reports@example.com\"\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 郵件防護協定 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **SPF 盲點** | 選項宣稱「設定 SPF 即可防止郵件內容被篡改」 | **錯誤！SPF 只能驗證寄件 IP**，無法驗證內容是否被竄改；驗證內容完整性必須靠 **DKIM 數位簽章** |\n| **DMARC 策略選項** | 題目問哪一個 DMARC 策略最能有效保護企業網域不被冒名發送釣魚信給大眾？ | **`p=reject` (直接拒收)**。`p=none` 只能監控 |\n| **水坑攻擊概念** | 題目描述駭客入侵知名同業論壇以感染訪問該論壇之目標企業員工 | **水坑攻擊 (Watering Hole Attack)** |\n\n> 🔑 **防呆口訣**：\n> - SPF 查 IP 名單，DKIM 簽章防篡改，DMARC 下令全拒收 (reject)！\n> - 鎖定目標叫魚叉，埋伏論壇是水坑。\n> - 急切匯款莫著急，電話照會解百惑！\n        ",
            "caseStudy": "【實務案例分析】某國際半導體公司屢遭駭客註冊相似網域偽造採購單。資安團隊全面推行防護工程：第一、在企業所有公網網域啟用 DNSSEC 結合嚴格的 SPF 與 DKIM 簽名；第二、在 DMARC 策略中配置 `p=reject`，強制全世界收件郵件伺服器凡收到未通過 SPF/DKIM 檢驗的偽冒信件一律直接拒收丟棄；第三、每季對全體員工無預警實施釣魚郵件模擬演練，點擊率超過 5% 的部門全員強制接受加強型實體資安培訓，成功使企業外部偽冒事件下降 99%。"
          },
          {
            "id": "B2-M08",
            "title": "單元 8：實體環境安全、設備生命週期與媒體廢棄銷毀",
            "keywords": [
              "Physical Security",
              "Mantrap",
              "Data Sanitization",
              "NIST SP 800-88",
              "Degaussing",
              "Physical Destruction"
            ],
            "summary": "掌握資料中心實體門禁縱深控制 (防尾隨雙重旋轉門 Mantrap/Air-lock)、供電環控與 FM-200 氣體滅火安全、儲存媒體生命週期報廢、符合 NIST SP 800-88 標準之資料清除 (Clear)、淨化 (Purge) 與銷毀 (Destroy) 規範實務。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 實體門禁與環境安全控制\n- **防尾隨機制 (Anti-Tailgating / Piggybacking)**：\n  - **雙重安全旋轉門 (Mantrap / Air-lock)**：兩道門互鎖（Interlocking Doors），第一道門關閉並完成第二身分驗證（如刷卡 + 指紋）後，第二道門方可開啟，物理上限制一次僅容許單人通過。\n- **資料中心環控與消防**：\n  - **電力備援**：不斷電系統 (UPS) 提供初期過渡電力，發電機 (Generator) 提供長時間自主發電，配電盤雙迴路 (Dual-cord Power)。\n  - **消防滅火系統**：機房嚴禁使用自動灑水系統（水會造成高壓設備短路與永久毀損）；必須使用**潔淨氣體滅火系統 (Clean Agent Fire Suppression，如 FM-200, Novec 1230, 惰性氣體 IG-541)**，透過中斷燃燒鏈滅火且不留殘留物。\n\n#### 2. NIST SP 800-88 媒體資料清除與淨化三大等級\n\n| 處置等級 (Level) | 技術手段與實作方式 | 資料復原可能性 | 適用情境與安全等級 |\n| :--- | :--- | :--- | :--- |\n| **1. 清除 (Clear)** | 邏輯性覆寫 (Overwriting)，以固定模式字元 (如全 0 或亂數) 覆蓋所有可定址磁區 | 一般簡易資料救援軟體無法讀取，但實驗室微探針仍有極微小機率復原 | 設備於組織內部不同部門間移交或降階重用 |\n| **2. 淨化 (Purge)** | **高斯消磁 (Degaussing)** (針對傳統磁帶/HDD) 或 **加密抹除 (Cryptographic Erase, CE)** | 即使在尖端實驗室設備下亦**完全不可復原** | 設備即將釋出組織外部、轉售或報廢 |\n| **3. 銷毀 (Destroy)** | **物理破碎 (Shredding)** 碾碎至規定顆粒大小、焚毀 (Incineration)、融熔 | 物理結構完全摧毀，絕無復原可能 | 處理極機密、國防或高度機敏資料媒體 |\n\n### 二、實務技術落地與監管作業 (Chain of Custody)\n\n```text\n【機敏硬碟報廢標準作業程序 (SOP)】\n1. 盤點登記：比對硬碟序號 (Serial Number) 與資產清冊。\n2. 淨化消磁：使用通過認證之消磁機 (強度大於 8,000 高斯) 破壞磁區結構。\n3. 實體物理粉碎：送入工業破碎機碾壓成直徑小於 2mm 之碎屑。\n4. 全程監管記錄：資安與稽核人員現場雙人監控並全程錄影。\n5. 出具文件：廠商與監管主管共同簽署《報廢銷毀證明書》並歸檔稽核。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 實體與銷毀觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **SSD 固態硬碟消磁** | 題目問「使用強力消磁機 (Degausser) 能否銷毀 SSD 固態硬碟之資料？」考生常誤選可以 | **無效！SSD 採用閃存快閃記憶體 (NAND Flash)，非磁性媒體**，消磁對 SSD 完全無效！SSD 必須使用「加密抹除 (CE)」或「實體晶片破碎 (Shredding)」 |\n| **防尾隨最佳機制** | 題目問防止未授權訪客尾隨員工進入機房最佳設施 | **雙重防尾隨門 (Mantrap / Air-lock)** |\n| **機房滅火氣體** | 考題出現 CO2、水霧、FM-200，問有人機房優先選擇 | **FM-200 或 Novec 1230** (高濃度二氧化碳 CO2 會使人員窒息，僅用於無人機房) |\n\n> 🔑 **防呆口訣**：\n> - 傳統硬碟可消磁，SSD 快閃必粉碎！\n> - 門禁防尾用 Mantrap，機房滅火 FM-200。\n> - Clear 覆寫內部換，Purge 淨化外流安，Destroy 碎裂無牽掛！\n        ",
            "caseStudy": "【實務案例分析】某大型金控進行資料中心伺服器汰舊換新，共有 500 顆退役 SAS 磁碟與 200 顆 NVMe SSD。資安長嚴格遵循 NIST SP 800-88 標準作業：SAS 傳統磁碟先經由 10,000 高斯消磁機完成磁性消除，確認馬達與磁軌完全失效；針對消磁無效的 200 顆 SSD，則直接送入工業雙軸物理破碎機進行現場刀刃切割，將快閃記憶體晶片碾碎成小於 5mm 顆粒。資安稽核員全程錄影並核對序號產出報廢證書，徹底杜絕了退役二手硬碟資料外流風險。"
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
            "keywords": [
              "ISO 27001:2022",
              "ISMS",
              "Annex A Controls",
              "Threat Intelligence",
              "Data Masking",
              "ICT Readiness"
            ],
            "summary": "徹底解析 ISO/IEC 27001:2022 改版核心：本文主條文 4-10 架構、附錄 A 整合之四大主題 (組織、人員、實體、技術共 93 項控制)、以及 11 項全新增列之關鍵控制措施（威脅情資、雲端服務資安、組態管理、資料外洩防護 DLP 與安全編碼）。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. ISO/IEC 27001:2022 核心架構改版深度剖析\n- **本文主條文 (Clauses 4-10)**：遵循 ISO 高階架構 (Harmonized Structure)：\n  - 第 4 節：組織背景 (Context of the organization，界定內外部議題與利害關係人需求)。\n  - 第 5 節：領導力 (Leadership，高階管理階層承諾、資安政策發布與角色責任指派)。\n  - 第 6 節：規劃 (Planning，風險評鑑處置與資安目標及達成規劃)。\n  - 第 7 節：支援 (Support，資源、能力、意識、通訊與文件化資訊)。\n  - 第 8 節：運作 (Operation，落實風險評鑑與控制措施執行)。\n  - 第 9 節：績效評估 (Performance evaluation，監控度量、內部稽核與管理審查)。\n  - 第 10 節：改善 (Improvement，不符合事項與矯正措施 CAPA)。\n- **附錄 A 控制措施結構重大變革**：\n  - 由 2013 版的 14 個網域 114 項控制，大幅整編為 **4 大主題 (Themes) 共 93 項控制措施**：\n    1. **組織控制 (Organizational controls)**：37 項 (如 A.5.1 政策、A.5.7 威脅情資、A.5.23 雲端資安)。\n    2. **人員控制 (People controls)**：8 項 (如 A.6.1 到職背景審查、A.6.3 資安意識培訓、A.6.5 離職後責任)。\n    3. **實體控制 (Physical controls)**：14 項 (如 A.7.1 實體安全邊界、A.7.4 實體安全監控、A.7.7 清晰桌面與螢幕)。\n    4. **技術控制 (Technological controls)**：34 項 (如 A.8.9 組態管理、A.8.11 資料遮罩、A.8.12 DLP、A.8.28 安全編碼)。\n\n#### 2. 2022 版全新增列之 11 項關鍵控制措施 (iPAS 中級必考重點！)\n1. **A.5.7 威脅情資 (Threat intelligence)**：組織應建立威脅情資收集、分析與產生機制，以因應新興威脅。\n2. **A.5.23 雲端服務使用資安 (Information security for use of cloud services)**：依據雲端責任共擔模型建立選商與使用準則。\n3. **A.5.30 業務持續之 ICT 準備度 (ICT readiness for business continuity)**：確保資通訊系統在突發災難時具備足夠韌性與備援能力。\n4. **A.7.4 實體安全監控 (Physical security monitoring)**：運用監控攝影機 (CCTV)、入侵警報系統監控實體敏感區域。\n5. **A.8.9 組態管理 (Configuration management)**：建立並維護硬體、軟體與網路設備之安全 Baseline 組態。\n6. **A.8.10 資訊刪除 (Information deletion)**：依據法令與資料生命週期，安全刪除過期儲存之機敏資料。\n7. **A.8.11 資料遮罩 (Data masking)**：根據存取控制原則，採用動態或靜態遮罩技術隱碼機敏個資。\n8. **A.8.12 資料外洩防護 (Data leakage prevention, DLP)**：在網路閘道、端點及雲端即時監控阻斷機敏資料未授權傳輸。\n9. **A.8.16 監控活動 (Monitoring activities)**：建立異常行為基準線 (Baseline) 並進行網路與主機異常持續監控。\n10. **A.8.23 網站過濾 (Web filtering)**：阻斷使用者瀏覽已確認之釣魚、惡意或違規網站。\n11. **A.8.28 安全編碼 (Secure coding)**：將軟體安全開發原則 (SSDLC) 納入程式開發生命週期。\n\n### 二、實務技術落地與控制矩陣 (Implementation Matrix)\n\n```text\n【ISO 27001:2022 控制屬性五大標籤 (Attributes)】\n每個控制措施均標記 5 個屬性值，以利資安工具自動映射：\n1. 控制類型 (Control type)：預防性 (Preventive)、偵測性 (Detective)、矯正性 (Corrective)。\n2. 資安屬性 (Information security properties)：機密性 (C)、完整性 (I)、可用性 (A)。\n3. 網路安全概念 (Cybersecurity concepts)：識別 (Identify)、保護 (Protect)、偵測 (Detect)、回應 (Respond)、復原 (Recover)。\n4. 操作能力 (Operational capabilities)：治理、資產管理、身分鑑別、應用安全、事件管理...等。\n5. 安全網域 (Security domains)：治理與生態系統、保護、防禦、韌性。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 改版細節 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **控制數量與主題** | 選項出現「14個網域 114項控制」 | **那是 2013 舊版！2022 最新版為「4 大主題 93 項控制措施」** |\n| **新增控制識別** | 題目問「下列何者不是 ISO 27001:2022 新增控制措施？」 | 記住 11 項新控制（威脅情資、雲端安全、ICT準備度、實體監控、組態管理、資訊刪除、資料遮罩、DLP、活動監控、網站過濾、安全編碼）。未在其中的為原有控制 |\n| **SOA 適用性聲明** | 考題問 SOA 是否只能包含 ISO 27001 附錄 A 內的項目？ | **錯誤！SOA 可納入附錄 A 以外之自訂控制措施**，附錄 A 僅為基準檢核清單 |\n\n> 🔑 **防呆口訣**：\n> - 27001 換新裝：四主題、九三條。\n> - 十一新兵記心頭：情資、雲端、DLP，遮罩、編碼、控組態！\n        ",
            "caseStudy": "【實務案例分析】某金融科技公司欲將其核心微服務架構由地端遷移至 AWS 公有雲，同時面臨 ISO/IEC 27001:2022 改版查核。資安架構師依據新增之 A.5.23 (雲端服務資安) 與 A.8.9 (組態管理)，制定了雲端安全 Baseline：使用 Terraform 進行基礎架構即代碼 (IaC) 的安全檢測，全面封鎖 S3 Bucket 公開存取；針對 A.8.11 (資料遮罩)，在 API 輸出端部署動態資料遮罩中介軟體，遮蔽客戶帳號中間 6 碼；針對 A.5.7 (威脅情資)，串接 MISP 威脅情資平台自動阻斷惡意 C2 IP。在外部驗證機構稽核中，稽核員對其完整落實 2022 新增控制項之工程落地給予零不符合項之高度評價。"
          },
          {
            "id": "M1-M02",
            "title": "單元 2：資通安全法規架構、責任等級與合規管理",
            "keywords": [
              "Cybersecurity Act",
              "Responsibility Levels A-E",
              "SOC Requirement",
              "Red Team Exercise",
              "Incident Classification 1-4"
            ],
            "summary": "深入掌握我國資通安全管理法母法及子法實施全貌：《資通安全責任等級分級辦法》A~E 級公務與特定非公務機關實施要求、SOC 7x24 監控規範、第三方紅隊演練、資安事件一至四級嚴重度判定標準、知悉後 1 小時通報與 36 小時重大事件復原規範。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 我國《資通安全責任等級分級辦法》維度全覽\n\n| 責任等級 | 劃分標的機關與特性 | 組織與專責人力要求 | 技術防護與稽核要求 |\n| :--- | :--- | :--- | :--- |\n| **A 級 (最高)** | 總統府、五院、國防、外交、重大民生關鍵基礎設施 (CI) 核心提供者 | • 設置專職資安長 (CISO)<br>• 配置**專職資安人員至少 4 名**以上 | • 全機關導入 ISMS 並通過第三方外部驗證<br>• **自建或委外 7x24 SOC**<br>• 每 2 年辦理 1 次全機關紅隊演練<br>• 每年辦理 1 次滲透測試與弱點掃描 |\n| **B 級** | 直轄市政府、部會二/三級核心機關、非核心 CI 提供者 | • 配置**專職資安人員至少 2 名**以上 | • 核心系統通過 ISMS 驗證<br>• 導入 SOC 日誌收集監控<br>• 每年辦理 1 次滲透測試 |\n| **C 級** | 縣市政府、公立大專院校、偏遠機關 | • 配置**專職資安人員至少 1 名**以上 | • 核心系統落實 ISMS<br>• 定期辦理弱點掃描 |\n| **D 級 / E 級** | 鄉鎮市區公所、公立中小學 | 無須專責人員，由上級機關統一統籌 | 落實基本端點防毒與資安意識培訓 |\n\n#### 2. 資通安全事件分級判定標準 (一級至四級)\n- **第一級資安事件**：非核心業務系統受影響，未造成業務中斷，無機密洩漏，可自行於短時間排除。\n- **第二級資安事件**：非核心業務中斷，或核心業務短暫局部受影響，或一般非公務機密遭洩漏。\n- **第三級資安事件 (重大)**：\n  - **核心業務系統中斷運作，無法於可容忍時間內復原**。\n  - **關鍵基礎設施核心運作停擺**。\n  - **國家機密保護法核定之機密資訊外洩**。\n  - **大量個人資料外洩 (如超過數萬筆個資外洩)**。\n- **第四級資安事件 (國安級重大)**：\n  - 國家關鍵基礎設施全面崩潰停擺。\n  - 國家安全情報嚴重洩漏，對國家生存利益造成立即危害。\n\n#### 3. 法定時限與行政義務 (1-36 鐵律)\n- **通報時限**：所有等級資安事件，**知悉後 1 小時內** 必須於「國家資通安全通報應變平台 (EAP)」完成通報。\n- **復原與損害控制**：第三級與第四級重大資安事件，必須在 **36 小時內** 完成遏止與復原，並於 1 個月內提出完整事件調查與改善報告。\n\n### 二、實務技術落地與合規稽核 (Compliance Checklist)\n\n```text\n【公務機關資安合規必查清單】\n[ ] 核心系統是否完成政府組態基準 (GCB) 套用率 >= 90%？\n[ ] 對外網站是否已全面封鎖老舊 TLS 1.0 / 1.1，強制 TLS 1.2 / 1.3？\n[ ] 特權帳號是否禁用通用密碼，並全面啟用硬體多因素驗證 (MFA)？\n[ ] 委外開發合約是否已明定「原始碼安全檢測 (SAST)」與「稽核權條款」？\n[ ] 本機安全性記錄檔是否設定即時集中轉發至 SOC/SIEM，並留存 >= 180 天？\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 法規項目 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **A 級機關專責人員** | 選項出現 1 名、2 名、3 名、4 名 | **A 級機關必須配置至少 4 名專職資安人員**；B 級為 2 名，C 級為 1 名 |\n| **重大事件判定** | 題目問核心產線全面被勒索加密停擺屬於第幾級事件？ | **至少屬於第三級 (重大事件)**；重大事件復原時限為 **36 小時** |\n| **紅隊演練頻率** | 考題問 A 級機關紅隊演練 (Red Teaming) 辦理週期 | **每 2 年至少辦理 1 次**；滲透測試與弱掃為每年至少 1 次 |\n\n> 🔑 **防呆口訣**：\n> - 責任等級算人頭：A 四、B 二、C 出一！\n> - A 級 SOC 全天候，兩年紅隊打一次。\n> - 知悉一小時必通報，三四重大三六復！\n        ",
            "caseStudy": "【實務案例分析】某屬於「高科技園區」關鍵基礎設施之 A 級特定非公務機關，其核心供電監控系統於週六清晨遭 APT 勒索攻擊，造成廠區局部電壓不穩。資安監控小組於 06:15 判定為外部惡意攻擊（知悉時點）。CISO 立即於 06:50 (35 分鐘內) 登入國家通報平台登錄為「第三級資安事件」，並成立緊急 CSIRT 小組。團隊利用備份映像重新刷新 PLC 控制器，於週日 14:00 (歷時 31 小時) 恢復全廠系統，完全符合法定 1 小時通報與 36 小時復原要求，事後一個月內向數發部提交 RCA 根因報告與加強版微切分計畫。"
          },
          {
            "id": "M1-M03",
            "title": "單元 3：資安風險評鑑與風險處置策略實務",
            "keywords": [
              "ISO 27005",
              "Risk Assessment",
              "Risk Treatment",
              "Risk Matrix",
              "Residual Risk",
              "Asset Valuation"
            ],
            "summary": "精熟 ISO/IEC 27005 資訊安全風險管理標準：資產識別與 CIA 價值評估、威脅與脆弱性交叉比對、定性 (Qualitative) 與定量 (Quantitative) 風險計算矩陣、四大風險處置策略（降低、轉移、規避、接受）以及殘餘風險 (Residual Risk) 審查機制。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. ISO/IEC 27005 風險評鑑標準五大核心步驟\n1. **建立背景環境 (Context Establishment)**：定義風險評估範疇、組織邊界、風險準則與「風險可接受度門檻 (Risk Acceptance Criteria)」。\n2. **風險識別 (Risk Identification)**：\n   - *資產鑑別 (Asset Identification)*：盤點硬體、軟體、資料、人員與服務資產。\n   - *資產評價*：依據機密性 (C)、完整性 (I)、可用性 (A) 衝擊度分別給予 1~5 分評級，取最高者或加權值作為資產價值 (Asset Value)。\n   - *威脅識別 (Threat Identification)*：人為蓄意、環境天災、硬體故障、人員疏失。\n   - *弱點識別 (Vulnerability Identification)*：系統漏洞、組態缺失、流程瑕疵。\n3. **風險分析 (Risk Analysis)**：\n   - 評估威脅利用弱點發生的**可能性 (Likelihood / Probability)** 與造成之**衝擊度 (Impact / Consequence)**。\n4. **風險評量 (Risk Evaluation)**：\n   - 計算風險值：$Risk = Likelihood \\times Impact$。\n   - 將計算結果與風險胃納量 (Risk Appetite) 比較，判定風險優先等級。\n5. **風險處置 (Risk Treatment)**：挑選合適之控制措施將風險降至可接受水準。\n\n#### 2. 四大風險處置策略 (Risk Treatment Strategies)\n1. **風險降低 / 修改 (Risk Mitigation / Modification)**：\n   - 實施技術或管理控制措施，降低威脅發生的可能性或減輕潛在衝擊（例如：為防止 SQL 注入而引入參數化查詢並部署 WAF）。最常採用的策略。\n2. **風險轉移 / 分擔 (Risk Sharing / Transfer)**：\n   - 將風險帶來的財務或法律損失轉移給第三方承擔（例如：購買「網路安全保險 (Cyber Insurance)」；將伺服器維運外包並於合約明訂 SLA 與賠償條款）。\n   - *注意：責任 (Accountability) 永遠無法轉移，僅有財務或部分作業風險被分擔！*\n3. **風險規避 (Risk Avoidance)**：\n   - 徹底終止或退出導致該風險的業務活動（例如：企業全面停止使用並下線已終止支援 (EOL) 的 Windows Server 2003 系統，或停止收集特定高風險個資）。\n4. **風險保留 / 接受 (Risk Retention / Acceptance)**：\n   - 經客觀評估，處置該風險所需之成本遠超過潛在損失，或該風險已低於容許門檻。**必須由組織高階管理層 (CISO/董事會) 正式書面簽核核准**，並列入追蹤清冊。\n\n#### 3. 殘餘風險 (Residual Risk) 審查\n- 實施安全控制措施後所剩餘的風險稱為「殘餘風險」。\n- **鐵律**：殘餘風險**必須小於或等於組織之風險可接受水準**；若仍高於門檻，必須重新進行控制措施規劃或由最高管理層專案核決。\n\n### 二、實務技術落地與風險矩陣 (Risk Matrix)\n\n```text\n【5x5 風險等級判定矩陣】\n       衝擊度 (Impact) →\n可能   1(極低)  2(低)   3(中)   4(高)   5(災難)\n↓\n5(極高)   5      10      15      20      25 (極高風險)\n4(高)     4       8      12      16      20 (高風險)\n3(中)     3       6       9      12      15 (中風險)\n2(低)     2       4       6       8      10 (低風險)\n1(極低)   1       2       3       4       5 (可接受)\n[處置準則]：>=15 分必須於 1 個月內完成處置；9~12 分列入季改善；<=8 分可由部門主管接受。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 風險管理觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **投保資安險之策略** | 題目問「企業購買 5,000 萬元資安險屬於哪種處置策略？」考生常誤選風險降低 | **風險轉移 / 分擔 (Risk Transfer/Sharing)**。保險不能降低被駭機率，只能轉移財務損失 |\n| **全面下線老舊系統** | 題目問因無法修補而決定停止該項業務 | **風險規避 (Risk Avoidance)** |\n| **風險接受的權責** | 選項宣稱「第一線工程師因沒時間修補，可自行勾選接受風險」 | **嚴重違規！風險接受必須由高階主管 (Management) 書面核准**，不得由技術操作者擅自決定 |\n\n> 🔑 **防呆口訣**：\n> - 買保險叫「轉移」，裝防火牆叫「降低」。\n> - 不幹下線叫「規避」，高層簽字才「接受」！\n> - 殘餘風險要受控，超過門檻不可留。\n        ",
            "caseStudy": "【實務案例分析】某電商在年度 ISO 27005 風險評鑑中，識別出運行 15 年的顧客積分舊系統架構於早已 EOL 的 PHP 5.2 伺服器上，存在數十個已知高危 RCE 漏洞。資訊部門評估修補需修改數萬行原始碼，成本高達 800 萬元，但該系統每年營收僅 50 萬元。資安長召開風險處置審查會議，否決了「風險降低」（成本不符效益）與「風險接受」（漏洞過大），最終決策採取「風險規避」策略：將積分系統功能整合進新版雲端微服務，於 60 天內全面停用並徹底下線該老舊伺服器，將該資產所衍生的安全風險降為零。"
          },
          {
            "id": "M1-M04",
            "title": "單元 4：業務持續運作計畫 (BCP) 與營運衝擊分析 (BIA)",
            "keywords": [
              "ISO 22301",
              "BCP",
              "BIA",
              "RTO",
              "RPO",
              "MTD",
              "Hot Site",
              "Warm Site",
              "Cold Site"
            ],
            "summary": "掌握 ISO 22301 業務持續管理體系 (BCMS)：深入理解營運衝擊分析 (BIA) 流程、MTD/RTO/RPO 數理關係與預算權衡、三種災難復原站台 (Hot/Warm/Cold Site) 架構評估、以及四種持續演練模式（桌面兵推、結構走查、模擬測試至全面切換）。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 營運衝擊分析 (BIA) 關鍵時間指標關係\n- **最大可容忍中斷時間 (Maximum Tolerable Downtime, MTD / MAO)**：\n  - 當業務功能或關鍵系統中斷時間超過此極限值，組織將面臨**無法承受之倒閉、重大法律吊照或永久性品牌商譽毀滅**。\n- **復原時間目標 (Recovery Time Objective, RTO)**：\n  - 災難發生後，系統必須完成修復並重新上線對外服務的目標時限。\n  - **核心限制公式**：**$RTO < MTD$**（RTO 必須嚴格小於 MTD，預留緩衝空間）。\n- **復原點目標 (Recovery Point Objective, RPO)**：\n  - 災難發生時，組織**可容許遺失資料的最大時間跨度**。\n  - RPO 決定了資料庫同步或備份之頻率（例如 RPO = 0 要求即時同步寫入；RPO = 24 小時代表每日備份一次即可）。\n- **工作復原時間 (Work Recovery Time, WRT)**：\n  - 系統硬體復原後，將歷史備份資料還原、跑完整性校驗與手動對帳並恢復正常業務運作所需之時間。$RTO + WRT \\le MTD$。\n\n#### 2. 三大異地災難備援中心 (Disaster Recovery Sites) 評估\n\n| 站台類型 | 硬體與網路設備就緒度 | 資料同步狀態 | 復原時間 (RTO) | 成本建置投入 |\n| :--- | :--- | :--- | :--- | :--- |\n| **熱站 (Hot Site)** | **完全鏡像配置**，伺服器與連線全時運作 (Active) | **即時同步複製 (Real-time Mirroring)** | **數秒至數分鐘** (全自動容錯移轉 Failover) | **最高** (相當於維持兩套完全獨立的資料中心) |\n| **溫站 (Warm Site)** | 硬體與作業系統已安裝就緒，但無即時資料 | 週期性非同步傳輸 (非即時) | **數小時至數天** (需手動掛載最後備份並校驗) | **中等** |\n| **冷站 (Cold Site)** | 僅具備機房建築空間、電力配電、高架地板與空調，**無現成運算主機** | **無現成資料** (需臨時搬遷或採購硬體) | **數天至數週** (需採購、安裝 OS、還原資料) | **最低** |\n\n#### 3. BCP 四大演練層次演進\n1. **桌面兵棋推演 (Tabletop Exercise)**：各部門主管圍坐會議室，針對假想災難情境口頭討論應變職責。成本最低、衝擊最小。\n2. **結構化走查 (Structured Walk-through)**：團隊依照 BCP 文件逐條檢核步驟，確認人員聯絡電話、備用鑰匙與文件是否完備。\n3. **模擬情境測試 (Simulation Test)**：模擬部分非核心系統中斷，並將部分流量切換至備援環境，檢視技術人員實際操作能力。\n4. **全中斷切換演練 (Full Interruption Test)**：**強制關閉生產環境真實主機房電力**，驗證異地熱站是否能全自動接管整體營運。衝擊最高、最逼真，若失敗可能造成真實業務損失，需最高管理層特准。\n\n### 二、實務技術落地與指標關係圖 (Visual Logic)\n\n```text\n[正常營運] ────(災難發生)─────────────────────────────────── [業務完全復原]\n                    │                                             │\n   ←─── RPO ────→   │  ←─────── RTO ────────→  ←──── WRT ────→    │\n  [最後成功備份點]  │  [系統硬體與服務上線]    [資料校驗與業務接手]\n                    │                                             │\n                    └─────────────── MTD (最大容忍極限) ──────────┘\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| BCP / BIA 觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **RTO 與 MTD 關係** | 選項宣稱「RTO 可以等於或大於 MTD」 | **嚴重錯誤！RTO 必須小於 MTD**，否則超過 MTD 組織已宣告瓦解 |\n| **RPO 核心意涵** | 題目問「RPO 主要是用來衡量什麼指標？」考生誤選系統復原速度 | **衡量「資料遺失量 (Data Loss)」或備份頻率**；衡量復原速度的是 **RTO** |\n| **冷站特性** | 題目問冷站 (Cold Site) 包含哪些設施 | **包含水電、空調、機房建築與網路線路，但「不包含運算伺服器與即時資料」** |\n\n> 🔑 **防呆口訣**：\n> - MTD 是死亡線，RTO 必須比它快。\n> - RPO 看資料丟多少，頻繁備份保如新。\n> - 熱站秒切成本昂，溫站手動需半天，冷站空房等主機！\n        ",
            "caseStudy": "【實務案例分析】某證券交易期貨中心依據 BIA 分析，確定核心交易撮合系統之 MTD 為 15 分鐘，RTO 必須 <= 5 分鐘，RPO 必須為 0 秒（絕對不能遺失任何一筆交易委託）。架構師採用了同城雙活 (Active-Active) 熱站 (Hot Site) 部署：兩座機房相距 25 公里，鋪設專屬雙迴路低延遲光纖通道，資料庫採用同步多主複製架構。在年度全中斷切換演練中，工程師人為切斷第一機房總電源，第二機房在 42 秒內全自動接管所有撮合請求，客戶端連線無感知切換，資料零遺失，成功達成 BCP 指標。"
          },
          {
            "id": "M1-M05",
            "title": "單元 5：第三方供應鏈安全與委外資安管理",
            "keywords": [
              "Supply Chain Risk",
              "SBOM",
              "Right to Audit",
              "Vendor Lifecycle",
              "PAM",
              "Dependency Confusion"
            ],
            "summary": "掌握第三方軟體供應鏈與委外廠商全生命週期管理：委外評選階段之資安資質審查、合約規範（稽核權條款 Right to Audit、事故通報責任、NDA）、特權跳板機 (PAM) 操作側錄、軟體物料清單 (SBOM SPDX/CycloneDX) 與開源軟體依賴混淆防禦。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 委外服務全生命週期風險管控\n1. **評選與採購階段 (Vendor Selection)**：\n   - 審查委外廠商之資安資質（如是否取得 ISO 27001, ISO 27701 認證、開發人員是否有資安證照）。\n   - 評估廠商歷史資安事故紀錄與財務健全度。\n2. **合約締結階段 (Contracting & SLA)**：\n   - **保密協定 (NDA)**：約定商業機密與個資保密責任，效力通常及於合約終止後數年。\n   - **稽核權條款 (Right to Audit)**：**企業有權指派內部或委託第三方獨立稽核員，無須受阻即可進入廠商現場查核合約履行狀況與資安控制**。\n   - **資安事件通報時限**：明訂廠商在知悉其系統或受託業務遭遇安全事故時，必須於特定時限內（如 2~24 小時內）正式通報委任企業。\n   - 智財權歸屬、安全開發義務 (SSDLC)、罰則與賠償上限。\n3. **維運階段 (Operations & Access Control)**：\n   - 嚴禁常設開放外部遠端連線或提供通用管理員密碼。\n   - 廠商遠端維護必須採用「VPN + 雙因素認證 (MFA)」，登入專屬特權存取管理系統 (PAM 跳板機)，連線具備時效性 (Just-in-Time)，且全程進行畫面錄影與鍵盤指令側錄。\n4. **終止與退場階段 (Termination & Exit)**：\n   - 立即全面停用並撤銷所有專案相關帳號、API Keys、憑證與網路訪問權限。\n   - 要求廠商交還或徹底銷毀所有機敏資料與原始碼，並出具具法律效力之《銷毀切結書》。\n\n#### 2. 軟體供應鏈安全與 SBOM (軟體物料清單)\n- **軟體供應鏈威脅 (如 SolarWinds 攻擊)**：駭客不直接攻擊企業，而是攻陷上游軟體供應商的 CI/CD 構建伺服器，將後門注入合法簽名的更新包中分發給數萬家企業。\n- **SBOM (Software Bill of Materials)**：\n  - 詳列軟體產品內所包含之所有相依元件、開源函式庫、版本號碼、授權協議與數位雜湊的標準化清單。\n  - 主流國際格式：**SPDX** (Linux 基金會推動)、**CycloneDX** (OWASP 推動)。\n  - *效益*：當 Log4Shell (CVE-2021-44228) 等零日漏洞爆發時，安全團隊可在幾秒內藉由 SBOM 查詢企業內部哪些系統使用了該受災套件，無須逐一拆解掃描代碼。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. 使用 Syft 自動化產出軟體容器之 CycloneDX SBOM\n```bash\n# 對發布之 Docker 映像檔掃描並生成 CycloneDX JSON 格式之 SBOM 清單\nsyft packages alpine:latest -o cyclonedx-json > sbom.json\n# 檢查清單中所有開源依賴項\njq '.components[] | {name: .name, version: .version}' sbom.json\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 供應鏈資安觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **稽核權條款 (Right to Audit)** | 廠商拒絕企業入廠查核，宣稱「我們是獨立法人你無權管」 | 企業若在合約中預先載明 **「稽核權條款 (Right to Audit)」**，即可依法要求查核，保障委外監督權 |\n| **廠商遠端存取** | 選項宣稱「為加速除錯，提供 AnyDesk 讓廠商 24 小時隨時連入」 | **嚴重違規！必須透過 PAM 跳板機連線、強制啟用 MFA 並全程操作錄影** |\n| **SBOM 價值** | 題目問企業要求軟體商提供 SBOM 主要目的為何？ | **精準掌握第三方元件依賴性，以利在爆發開源漏洞時迅速盤點受災面** |\n\n> 🔑 **防呆口訣**：\n> - 委外合約三件寶：保密 (NDA)、通報、稽核權 (Right to Audit)！\n> - 廠商連入走 PAM，MFA 驗證加側錄。\n> - 軟體成分看 SBOM，SPDX/CycloneDX 漏洞秒盤點！\n        ",
            "caseStudy": "【實務案例分析】某金控委託軟體開發商建置核心網路銀行 APP。在專案交付驗收時，金控資安長要求廠商提供完整之 CycloneDX 格式 SBOM，並執行第三方開源元件弱點掃描 (SCA)。掃描發現廠商引入了一款已終止維護且存在已知高危 RCE 漏洞的開源 XML 解析庫。得益於合約中明訂的 SSDLC 安全編碼義務與驗收條款，金控依約要求廠商免費抽換該函式庫並完成回歸測試後方准放行驗收，成功阻斷了軟體供應鏈安全破口。"
          },
          {
            "id": "M1-M06",
            "title": "單元 6：資安治理架構、政策制定與成熟度評估",
            "keywords": [
              "Security Governance",
              "CISO Independence",
              "Policy Hierarchy",
              "KPI and KRI",
              "CMMI Maturity Model"
            ],
            "summary": "建立現代企業資安治理體系：董事會與高階主管當責性、CISO (資安長) 職責獨立性與匯報路線、資安政策四階文件架構（政策、辦法/標準、作業指引、紀錄表單）、關鍵績效指標 (KPI) 與關鍵風險指標 (KRI) 設計以及 CMMI/NIST CSF 成熟度衡量。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 資安治理 (Governance) vs 資安管理 (Management)\n- **資安治理 (Governance)**：\n  - *主導者*：**董事會 (Board of Directors) 與最高管理階層**。\n  - *核心目標*：定義組織安全願景、設定風險胃納量、提供資源、監督指導戰略投資與合規監督。\n  - *原則*：當責性 (Accountability) 始終屬於董事會與 CEO。\n- **資安管理 (Management)**：\n  - *主導者*：**CISO (資訊安全長) 與專責管理團隊**。\n  - *核心目標*：日常規劃、建置、執行、維運各項安全控制措施以落實治理方針。\n- **CISO 的組織獨立性 (關鍵考點！)**：\n  - CISO 應**直接向執行長 (CEO) 或董事會審計委員會獨立匯報**。\n  - **嚴禁將 CISO 隸屬於 CIO (資訊長) 之下**！因為 CIO 重視「系統上線速度與營運效率」，CISO 重視「風險控管與安全防禦」，兩者存在天然之職責利益衝突。\n\n#### 2. 資安四階文件階層體系 (Documentation Hierarchy)\n1. **第一階：政策 (Policy)**：\n   - 高階主管宣示之最高指導綱領（如全域《資訊安全政策》）。陳述「要做什麼 (What)」，具有全公司強制性，變動頻率最低（通常一年審查一次）。\n2. **第二階：辦法 / 程序 / 標準 (Procedure / Standard)**：\n   - 規範跨部門或特定領域之具體管理規則（如《存取控制管理辦法》、《備份作業程序》）。陳述「由誰在何時做 (Who, When)」。\n3. **第三階：作業指引 / 規範 (Guideline / Work Instruction)**：\n   - 技術人員執行的具體操作手冊（如《Windows Server 2022 安全強化設定指引》）。陳述「如何一步一步操作 (How)」。\n4. **第四階：表單 / 紀錄 (Form / Record)**：\n   - 執行流程所留下之具體佐證與客觀稽核軌跡（如機房進出簽名簿、帳號異動申請單）。證明「確實執行過 (Evidence)」。\n\n#### 3. 關鍵量化指標：KPI vs KRI\n- **KPI (關鍵績效指標)**：衡量過去與當前安全活動之執行效率與成果（如：弱點平均修補時間 MTTR、高危漏洞修補完成率、釣魚演練未點擊率）。\n- **KRI (關鍵風險指標)**：**前瞻性指標 (Leading Indicator)**，預警未來風險升高的信號（如：離職員工未封鎖帳號數量、過期特權帳號數量、未修補重大漏洞積壓趨勢）。\n\n### 二、實務技術落地與成熟度評估 (Maturity Model)\n\n```text\n【CMMI / NIST 資安成熟度五大層次】\n• Level 1 初始級 (Initial)：未定型、混亂、臨時應對 (Ad-hoc)，依賴個人英雄主義。\n• Level 2 可重複級 (Repeatable)：具備基本直覺專案流程，但缺乏正式文件。\n• Level 3 已定義級 (Defined)：建立全公司標準作業程序 (SOP) 與正式四階文件。\n• Level 4 已管理級 (Managed)：引進量化度量 (KPI/KRI) 進行數據化監控與管理。\n• Level 5 持續最佳化級 (Optimizing)：持續主動創新、自動化與主動威脅防禦。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 資安治理觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **CISO 報告體系** | 選項宣稱「CISO 應向 CIO 報告以統一 IT 指揮權」 | **嚴重違規！CISO 應獨立於 CIO**，直接向 CEO 或董事會報告，避免利益衝突 |\n| **政策 vs 指引** | 題目問哪一階文件規定具體的技術指令操作？ | **第三階：作業指引 (Work Instruction)**；第一階政策絕不包含具體命令細節 |\n| **KRI 的前瞻性** | 題目問用來預警未來潛在資安風險爆發的指標為何？ | **KRI (關鍵風險指標)**；KPI 衡量過去執行成效 |\n\n> 🔑 **防呆口訣**：\n> - 治理在董事，管理在 CISO，獨立向 CEO 不受 CIO 制。\n> - 一階政策定方向，二階辦法定規範，三階指引教操作，四階表單留軌跡。\n> - KPI 算過去功績，KRI 測未來危機！\n        ",
            "caseStudy": "【實務案例分析】某金控金檢時被金融監督管理委員會糾正：該公司資安長長期兼任資訊處長 (CIO)，為確保各項新業務系統如期上線，屢次特許系統在尚未修補高危漏洞的情況下上線運作，違反資安治理制衡原則。董事會接獲糾正後立即啟動治理整頓：成立獨立於資訊處的「資訊安全專責處」，任命專任 CISO 直屬總經理並向董事會審計委員會每季報告；同時建立四階資安文件審查機制與 KRI 風險儀表板，將未修補漏洞指標與 IT 部門績效直接連動，成功建立健全之資安治理架構。"
          },
          {
            "id": "M1-M07",
            "title": "單元 7：國際資料隱私法規 (GDPR) 與隱私保護技術",
            "keywords": [
              "GDPR",
              "Data Subject Rights",
              "DPO",
              "DPIA",
              "Pseudonymization",
              "Anonymization",
              "72-Hour Breach Notification"
            ],
            "summary": "全面掌握歐盟一般資料保護規則 (GDPR) 與國際隱私工程：資料控制者 (Controller) 與處理者 (Processor) 權責、DPO 設立要件、當事人權利（被遺忘權、資料可攜權）、高額罰款機制（全球營收 4%）、72 小時外洩法定通報、隱私衝擊評估 (DPIA) 以及假名化 (Pseudonymization) 與匿名化 (Anonymization) 之技術差異。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 歐盟 GDPR 核心法規範圍與罰則\n- **域外管轄權 (Extra-territorial Applicability)**：\n  - 即使企業設立於歐盟境外（如台灣企業），只要其**向歐盟境內之個人提供商品/服務**，或**監控歐盟境內個人的行為**，均完全受 GDPR 管轄。\n- **高額行政罰款雙軌制 (必考數字！)**：\n  1. *較輕違規*：最高 **1,000 萬歐元** 或 企業全球年營業額 **2%** (取其高者)。\n  2. *重大違規 (侵犯當事人核心權利、非法跨境傳輸)*：最高 **2,000 萬歐元** (約合新台幣 7 億元) 或 企業全球年營業額 **4%** (取其高者)！\n- **72 小時資安外洩通報 (Breach Notification)**：\n  - 資料控制者在知悉個人資料侵害事件後，必須在 **72 小時內** 向歐盟主管機關通報；若外洩可能對當事人權利自由產生高度風險，亦須**即時通知受害當事人**。\n\n#### 2. 當事人核心權利 (Data Subject Rights)\n- **被遺忘權 / 刪除權 (Right to be Forgotten / Erasure, Article 17)**：\n  - 當事人撤回同意或資料已無當初蒐集之業務目的時，有權要求控制者徹底刪除其所有個人資料。\n- **資料可攜權 (Right to Data Portability, Article 20)**：\n  - 當事人有權取得結構化、通用且機器可讀格式 (如 JSON/CSV) 之個人資料，並有權將其無阻礙地移轉至另一家競爭平台。\n- **限制處理權**、**反對權**、**存取查閱權**。\n\n#### 3. 隱私工程保護技術：假名化 vs 匿名化\n- **假名化 (Pseudonymization)**：\n  - 將個資中的識別欄位（如姓名、身分證號）替換為人工假名或隨機雜湊代碼。\n  - *關鍵特徵*：只要取得分開獨立加密保存之「金鑰/對照表」，**仍可重新反查識別出特定個人**。\n  - *法律地位*：在 GDPR 下**依然屬於個人資料**，但被視為一項優秀的安全補償控制措施。\n- **匿名化 (Anonymization)**：\n  - 經過不可逆技術（如 k-匿名化、差分隱私、泛化擾動），使任何技術手段在合理範圍內均**永久無法重新識別出特定個人**。\n  - *法律地位*：處理完成後**不再屬於個人資料**，完全脫離 GDPR 之監管範疇。\n\n### 二、實務技術落地與 DPIA 流程 (Data Protection Impact Assessment)\n\n```text\n【何時必須執行隱私衝擊評估 (DPIA)】\n依據 GDPR 第 35 條，遇下列情境必須於開發上線前執行 DPIA：\n1. 大規模系統性評估個人特徵 (如利用 AI 自動化分析信用評分或求職者篩選)。\n2. 大規模處理特殊類別資料 (特種個資：醫療病歷、基因、生物辨識特徵)。\n3. 大規模公開場所系統性監控 (如公共場所裝設智慧人臉辨識 CCTV)。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| GDPR 觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **外洩通報時限** | 題目混淆台灣資安法與 GDPR 通報時限 | **GDPR 個資外洩通報時限為「72 小時內」**；台灣資通安全管理法為「1 小時內」 |\n| **假名化是否受管轄** | 選項宣稱「資料一經假名化 (Pseudonymized)，即不再受 GDPR 規範」 | **嚴重錯誤！假名化仍屬個資，受 GDPR 管轄**；只有不可逆的「匿名化 (Anonymization)」才脫離 GDPR |\n| **最高罰款上限** | 題目問 GDPR 最嚴重違規之行政罰款上限 | **2,000 萬歐元 或 全球年營業額 4% (取其高者)** |\n\n> 🔑 **防呆口訣**：\n> - 歐盟 GDPR 罰天價：全球營業百分四 (4%)！\n> - 外洩通知七二 (72) 時，當事人擁被遺忘。\n> - 假名可逆仍算個資，匿名不可逆才脫鉤！\n        ",
            "caseStudy": "【實務案例分析】某台灣跨國機票代訂平台拓展歐洲航線業務，向歐盟旅客提供機票比價與訂購服務。該平台資料庫遭遇勒索攻擊，部分歐盟公民護照號碼與信用卡資料洩漏。法務與資安團隊立即啟動 GDPR 應變程序：在知悉事件後 48 小時內（符合 72 小時限）向法國國家資訊自由委員會 (CNIL) 提交詳細事故通報與影響範圍評估。由於該平台事先對所有儲存之護照號碼實施了強加密與「假名化」處理，外洩之密文在缺乏金鑰下無法直接還原識別，且平台積極通知受影響旅客，最終監管機構認定其善盡安全維護責任，免除了高達全球營收 4% 的毀滅性重罰。"
          },
          {
            "id": "M1-M08",
            "title": "單元 8：資安稽核實務、缺失改善與 CAPA 機制",
            "keywords": [
              "Internal Audit",
              "Audit Evidence",
              "Non-Conformity",
              "Root Cause Analysis",
              "5-Whys",
              "CAPA Process"
            ],
            "summary": "深入掌握資訊安全內部與外部稽核實務：第一/二/三方稽核角色定義、客觀稽核證據 (Objective Evidence) 抽樣原則、主要不符合 (Major) 與次要不符合 (Minor) 判定、根本原因分析 (RCA / 5-Whys / 魚骨圖) 與矯正預防措施 (CAPA) 閉環管理流程。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 稽核三大類型深度對照\n\n| 稽核類別 | 執行主體與角色 | 稽核目的與特性 | 獨立性要求 |\n| :--- | :--- | :--- | :--- |\n| **第一方稽核 (內部稽核)** | 組織內部指派之稽核人員 | 自我檢查 ISMS 運作有效性，尋找改進空間 | 稽核員不得稽核自己所屬部門或自身業務 (迴避原則) |\n| **第二方稽核 (外部/供應商稽核)** | 組織指派人員對其**供應商或外包廠商**查核 | 確認委外廠商是否符合採購合約與資安規範 | 具備客戶與廠商間之監督獨立性 |\n| **第三方稽核 (驗證稽核)** | 獨立、具認證資格之外部認證機構 (如 BSI, SGS, DNV) | 正式審查是否符合國際標準並**核發 ISO 證書** | 最高等級獨立性與客觀性 |\n\n#### 2. 稽核發現等級判定標準\n- **符合項 (Conformity)**：完全遵循標準與作業規範並具備佐證。\n- **觀察事項 (Observation / Opportunity for Improvement, OFI)**：尚符合標準，但流程存在微小潛在風險，建議持續精進。\n- **次要不符合項 (Minor Non-Conformity)**：\n  - 局部、偶發性或單一文件的疏漏（如 100 筆帳號抽查中發現 1 筆離職表單未經主管補簽，但帳號已停用）。未對整個 ISMS 系統運作造成根本性瓦解。\n- **主要不符合項 (Major Non-Conformity - 最嚴重！)**：\n  - **根本性系統失效**：標準中某一核心條文或控制措施完全未被落實（如完全沒有做過風險評鑑、整個機關完全沒有備份記錄）。\n  - 多個次要不符合項累積指向同一系統性失控。\n  - **後果：驗證機構將直接拒絕發證或暫停/撤銷現有 ISO 27001 證書！**\n\n#### 3. 矯正預防措施 (CAPA) 閉環管理五大步驟\n1. **問題定義與短期遏止 (Containment)**：立即修正眼前表面錯誤（如立即手動鎖定該遺漏之帳號）。\n2. **根本原因分析 (Root Cause Analysis, RCA)**：\n   - 探究背後流程缺失，運用 **5-Whys (連續追問五個為什麼)** 或 **石川魚骨圖**。\n   - *例*：為什麼帳號沒關？因為人資沒通知。為什麼人資沒通知？因為人資表單沒連線。為什麼沒連線？因為缺乏跨系統整合 API。\n3. **擬定長期矯正措施 (Corrective Action Plan)**：從制度或技術架構消除根本原因（如開發 HR 與 AD 自動同步 API）。\n4. **措施落實執行 (Implementation)**：排程上線並保存紀錄。\n5. **有效性驗證 (Effectiveness Review)**：在下一次稽核週期回查該缺失是否不再復發，確認有效方可正式「結案 (Closure)」。\n\n### 二、實務技術落地與稽核查檢 (Audit Trail Evidence)\n\n```text\n【稽核證據三角驗證法 (Triangulation)】\n專業稽核員判定一項控制措施是否有效落實，絕不輕信單一口述，必須包含：\n1. 面談詢問 (Interview)：向作業人員確認日常標準流程與認知。\n2. 文件規範 (Document)：查核二階辦法是否有明確作業準則。\n3. 實體佐證 (Records / Log)：調閱系統 Log、簽核單據、截圖進行交叉比對。\n若口述與紀錄不符，即刻開立不符合項。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 稽核實務觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **內稽獨立性原則** | 題目問「資訊處資安組長能否擔任資訊處伺服器主機備份的內部稽核員？」 | **不行！違反獨立性與迴避原則**。不得稽核自身所屬部門之業務 |\n| **主要不符合之後果** | 題目問稽核員發現主要不符合項 (Major NC) 時會發生何種結果？ | **無法通過驗證發證 (或暫停證書)**，必須限期完成矯正並實施複查 |\n| **CAPA 核心思維** | 選項宣稱「把那筆漏掉的資料補齊即算完成 CAPA 結案」 | **錯誤！那只是短期遏止 (Containment)**；CAPA 核心必須進行 **RCA 消除根本原因** 並驗證不再復發 |\n\n> 🔑 **防呆口訣**：\n> - 內稽迴避不查己，外稽驗證才發照。\n> - 主要缺失證書扣，次要缺失限期收。\n> - 遏止治標、RCA 治本，有效回查才結案！\n        ",
            "caseStudy": "【實務案例分析】在 ISO 27001 外部複審稽核中，第三方主導稽核員抽查 50 筆近期離職員工名單，發現其中 3 名工程師在離職超過 14 天後，其 VPN 帳號依然處於啟用狀態。稽核員判定為「主要不符合項 (Major Non-Conformity)」，限期 30 天內完成改善否則暫停證書。CISO 召集專案會議，運用 5-Whys 進行 RCA：根本原因在於人資離職系統與 IT 網域完全為人工紙本傳遞，偶遇休假即發生公文延誤。矯正措施為開發自動化中介服務，由 HR 系統結算日離職時間一到自動觸發 Webhook，即時透過 API 鎖定 AD 與 VPN 權限。30 天後複查驗證有效，成功解除 Major NC 並順利換證。"
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
            "keywords": [
              "Zero Trust",
              "NIST SP 800-207",
              "PDP",
              "PEP",
              "Policy Engine",
              "SDP",
              "Micro-Segmentation"
            ],
            "summary": "掌握零信任安全最高標準 NIST SP 800-207：核心設計原則「永不信任，始終驗證 (Never Trust, Always Verify)」、策略決定點 (PDP) 之策略引擎 (PE) 與管理點 (PA) 大腦架構、策略執行點 (PEP) 守門員元件、軟體定義邊界 (SDP)、身分感知代理 (IAP) 與網路微切分實作。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. NIST SP 800-207 零信任架構 (ZTA) 七大核心原則\n1. **所有資料來源與運算服務皆視為資源**。\n2. **無論網路位置位於內部或外部，所有通訊均受到保護與加密**（徹底打破內網即安全之傳統迷思）。\n3. **對個別企業資源的存取授權，必須以「每個獨立工作階段 (Per-session)」為基礎動態評估**。\n4. **資源存取權限由動態策略決定**：綜合評估主體身分、設備健康度、應用軟體安全狀態、地理環境屬性等多維度特徵。\n5. **企業應持續監控並量測所有關聯資產的安全性與健康狀態**（例如防毒未更新或未開啟磁碟加密之端點直接降階或拒絕連線）。\n6. **所有資源的存取在授予前必須經過動態身分鑑別與授權**（強大多因素認證 MFA）。\n7. **企業應持續收集資產、網路與通訊之狀態資訊，並將其回饋至策略決策引擎中滾動最佳化**。\n\n#### 2. 零信任三大核心元件邏輯模型\n\n```text\n[主體 (Subject) + 端點裝置] \n            │ \n            ▼ (發起存取請求)\n    ┌───────────────────────────┐\n    │ 策略執行點 (PEP)           │ ──(轉發決策請求)──> ┌──────────────────────────────┐\n    │ Policy Enforcement Point  │                      │ 策略決定點 (PDP)             │\n    │ (閘道端、API Gateway、代理)│ <──(下發授權/拒絕)─  │ ┌──────────────────────────┐ │\n    └─────────────┬─────────────┘                      │ │ 策略引擎 (Policy Engine) │ │\n                  │                                    │ └────────────┬─────────────┘ │\n                  ▼ (通過驗證放行連線)                  │ ┌────────────▼─────────────┐ │\n    ┌───────────────────────────┐                      │ │ 策略管理點 (Policy Admin) │ │\n    │ 企業受保護資源 (Resource)  │                      │ └──────────────────────────┘ │\n    └───────────────────────────┘                      └──────────────────────────────┘\n```\n- **策略引擎 (Policy Engine, PE)**：**大腦**。負責比對安全策略規則與環境情資，做出「允許 (Allow)」或「拒絕 (Deny)」存取的終極決定。\n- **策略管理點 (Policy Administrator, PA)**：**神經系統**。接收 PE 決策，負責向 PEP 發布工作階段憑證或金鑰以建立或關閉通訊通道。\n  - *(PE 與 PA 邏輯上共同構成策略決定點 PDP)*。\n- **策略執行點 (Policy Enforcement Point, PEP)**：**守門員**。直接攔截、啟用、監控並最終中斷主體與資源之間的連線。\n\n#### 3. 軟體定義邊界 (SDP) 與微切分 (Micro-Segmentation)\n- **SDP (Software Defined Perimeter)**：遵循「先驗證後連線 (Authenticate-Before-Connect)」理念，使未經授權之主機在網路上完全呈現「不可見 (Black Cloud)」，杜絕通訊埠掃描。\n- **微切分**：將資料中心與雲端網路切分為極細小的工作負載隔離單元，嚴禁伺服器與工作站橫向直連 (East-West Traffic Isolation)。\n\n### 二、實務技術落地與動態策略 (Conditional Access Logic)\n\n```json\n// 零信任動態條件式存取原則範例 (JSON 邏輯)\n{\n  \"policy_name\": \"ZeroTrust_Core_Database_Access\",\n  \"conditions\": {\n    \"user_role\": \"DBA_Senior\",\n    \"mfa_status\": \"FIDO2_Hardware_Verified\",\n    \"device_compliance\": {\n      \"edr_active\": true,\n      \"os_patch_level\": \"within_14_days\",\n      \"disk_encrypted\": true\n    },\n    \"location\": \"Taiwan_IP_Range\",\n    \"time_window\": \"Working_Hours_Only\"\n  },\n  \"action\": \"ALLOW_SESSION_WITH_PAM_RECORDING\"\n}\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 零信任觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **PDP 與 PEP 職責** | 題目問「直接負責攔截與放行網路連線的元件是哪一個？」考生常錯選 PDP | **策略執行點 (PEP)**。PDP 只負責「做決策」，真正站在第一線攔截封包的是「PEP」 |\n| **零信任核心假設** | 選項宣稱「零信任是將所有外部攻擊者徹底阻絕在外」 | **零信任核心思維是「假設已被滲透 (Assume Breach)」**，即使進入內網亦永不信任，始終動態驗證 |\n| **傳統 VPN vs ZTA** | 題目問為何現代架構建議淘汰傳統 VPN？ | 傳統 VPN 採「邊界信任」，一旦撥入即獲得整個內網的存取權限，易遭橫向滲透；ZTA 採 Per-session 最小權限 |\n\n> 🔑 **防呆口訣**：\n> - 零信任理念：永不信任、始終驗證、假設被駭。\n> - 大腦做決定叫 PDP，門房來攔截叫 PEP。\n> - 傳統 VPN 進門隨便走，微切分零信任每步都要查！\n        ",
            "caseStudy": "【實務案例分析】某跨國 IC 設計龍頭在疫情期間全員遠端辦公。一名資深工程師的家用電腦不慎感染木馬，黑客取得其 VPN 帳號密碼企圖連線企業內網竊取晶片光罩原始碼。由於該公司已全面落地 NIST SP 800-207 零信任架構：當連線發起時，PEP 攔截請求送交 PDP 評估；策略引擎 (PE) 判定該連線裝置未安裝企業受管 EDR 代理程式且硬碟未加密，設備健康度評分不及格。PEP 當場拒絕建立通訊通道並觸發 SOC 高危告警，成功防堵了一場災難性的專利外洩事故。"
          },
          {
            "id": "M2-M02",
            "title": "單元 2：MITRE ATT&CK 框架、Cyber Kill Chain 與威脅情資 (CTI)",
            "keywords": [
              "MITRE ATT&CK",
              "Cyber Kill Chain",
              "Pyramid of Pain",
              "Threat Intelligence",
              "STIX/TAXII",
              "TTPs"
            ],
            "summary": "精準運用高階威脅對抗框架：洛克希德馬丁網路殺傷鏈 (Cyber Kill Chain) 七大階段、MITRE ATT&CK 14 大戰術矩陣 (Tactics) 與百項技術 (Techniques)、畢安可痛苦金字塔 (Pyramid of Pain) 威脅對抗層次、以及威脅情資 (CTI) 格式標準 STIX/TAXII 實務應用。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 痛苦金字塔 (The Pyramid of Pain) 深度解析\n- 由 David Bianco 提出，描述防禦者封鎖各類指標時，**帶給黑客對手的痛苦程度由底層至頂層**：\n  1. **雜湊值 (Hash Values - 最底層)**：對黑客極容易更換。只需修改檔案中任一 byte 或重新編譯，雜湊值全變。\n  2. **IP 位址 (IP Addresses)**：容易更換。攻擊者可透過 Proxy、Tor、租用大量雲端 VPS 任意切換。\n  3. **網域名稱 (Domain Names)**：稍具難度。更換需重新註冊網域，或依賴 DGA 動態生成。\n  4. **網路與主機產出物 (Network/Host Artifacts)**：中等難度。如惡意通訊特徵碼、特定 URI 模式、特定登錄檔鍵值。\n  5. **攻擊工具 (Tools)**：困難。黑客必須尋找、逆向或重新編寫新的利用工具。\n  6. **手法戰術與技術 (TTPs - 最頂層！最痛苦！)**：**直擊黑客核心能力！** 若防禦者從技術手法維度（如阻止記憶體傾倒、封鎖特定橫向移動技術）防禦，黑客必須重新受訓或徹底推翻攻擊思維，往往直接放棄目標！\n\n#### 2. MITRE ATT&CK 14 大戰術階段 (Tactics) 脈絡\n- **戰術 (Tactics，攻擊者的目標「Why」)** -> **技術 (Techniques，攻擊者達成目標的手法「How」)**：\n  1. `TA0043` 偵察 (Reconnaissance)\n  2. `TA0042` 資源開發 (Resource Development)\n  3. `TA0001` 初始存取 (Initial Access)：魚叉釣魚 (T1566)、利用對外應用漏洞 (T1190)。\n  4. `TA0002` 執行 (Execution)：命令列執行 (T1059)、PowerShell 腳本。\n  5. `TA0003` 持續潛伏 (Persistence)：排程工作 (T1053)、啟動註冊表 (T1547)。\n  6. `TA0004` 權限提升 (Privilege Escalation)：利用核心漏洞、存取權杖操縱 (T1134)。\n  7. `TA0005` 防禦規避 (Defense Evasion)：偽裝、清除日誌 (T1070)、進程注入 (T1055)。\n  8. `TA0006` 憑證存取 (Credential Access)：LSASS 記憶體傾倒 (T1003)、暴力破解。\n  9. `TA0007` 發現探勘 (Discovery)：內網資產掃描、網域信任探索。\n  10. `TA0008` 橫向移動 (Lateral Movement)：Pass the Hash (T1550)、RDP 連線、SMB/PsExec。\n  11. `TA0009` 收集 (Collection)：螢幕截圖、擊鍵側錄、敏感資料歸檔。\n  12. `TA0011` 命令與控制 (Command and Control, C2)：加密通道連線、非標準通訊協定。\n  13. `TA0010` 資料外洩 (Exfiltration)：資料壓縮後透過 C2 或雲端外傳。\n  14. `TA0040` 衝擊破壞 (Impact)：資料加密勒索 (T1486)、磁碟抹除破壞。\n\n#### 3. 威脅情資 (CTI) 交換國際標準\n- **STIX (結構化威脅資訊表達)**：基於 JSON 的標準化語言，用於描述威脅指標 (IoC)、TTPs、攻擊動機與行動者。\n- **TAXII (情資資訊受信任自動交換)**：傳輸協定，利用 HTTPS RESTful API 自動化交換 STIX 格式情資。\n\n### 二、實務技術落地與 MITRE 對齊實作 (Threat Hunting)\n\n#### 1. 偵測 T1003 (OS Credential Dumping: LSASS Memory)\n```text\n【Sigma 規則定義：偵測非法讀取 LSASS 記憶體憑證】\nlogsource:\n    category: process_access\n    product: windows\ndetection:\n    selection:\n        TargetImage|endswith: '\\lsass.exe'\n        GrantedAccess|contains: '0x1010' # PROCESS_VM_READ\n    filter:\n        SourceImage|endswith: \n            - '\\svchost.exe'\n            - '\\csrss.exe'\n    condition: selection and not filter\nlevel: critical\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| ATT&CK 與 CTI 觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **痛苦金字塔頂層** | 題目問「哪一項指標能帶給攻擊者最大的痛苦與挫敗感？」考生常誤選 IP 或雜湊 | **TTPs (戰術、技術與程序)**。雜湊與 IP 最底層最無效 |\n| **STIX vs TAXII** | 題目混淆資料格式與傳輸通訊協定 | **STIX 是表達語言與資料格式 (JSON)**；**TAXII 是傳輸協定 (API/Transport)** |\n| **Kill Chain vs ATT&CK** | 考題問兩者差異 | **Kill Chain 呈單向線性七階段**；**ATT&CK 呈非線性矩陣**，涵蓋更詳盡的行為技術與對抗矩陣 |\n\n> 🔑 **防呆口訣**：\n> - 痛苦金字塔倒著記：雜湊 IP 隨便換，工具 TTP 痛斷魂！\n> - STIX 寫語言格式，TAXII 跑傳輸通道。\n> - ATT&CK 十四戰術陣，橫向移動抓 PtH，憑證存取盯 LSASS！\n        ",
            "caseStudy": "【實務案例分析】SOC 分析師在監控日誌中發現多個境外 IP 對外網進行連接埠掃描。初階分析師提議將該批 IP 加入防火牆黑名單封鎖。資安架構師依據「痛苦金字塔」原則指出：單純封鎖 IP 位於底層，黑客能在 3 分鐘內切換數百個新 IP。團隊進而依據 MITRE ATT&CK 框架展開深層分析：比對其 Payload 發現攻擊者正在利用 T1059.001 (PowerShell) 與 T1003 (LSASS 憑證傾倒)。防禦團隊直接於網域 GPO 全面啟用 Windows Defender Credential Guard，以硬體虛擬化技術隔離 LSASS，並啟用 PowerShell 限制語言模式。攻擊者因無法執行 TTPs 關鍵技術，橫向移動全面受挫，被迫放棄攻擊。"
          },
          {
            "id": "M2-M03",
            "title": "單元 3：現代 SOC 維運、SIEM 關聯分析與 SOAR 自動化劇本",
            "keywords": [
              "SOC",
              "SIEM",
              "SOAR",
              "Playbook",
              "Correlation Rules",
              "Alert Fatigue",
              "MTTR"
            ],
            "summary": "掌握安全維運中心 (SOC) 現代運作體系：Tier 1~3 分析師階層職責、SIEM 跨日誌即時關聯分析規則撰寫、警報疲勞 (Alert Fatigue) 消除機制、SOAR 安全協同與自動化回應劇本 (Playbook) 編排、以及平均偵測與應變時間 (MTTD / MTTR) 指標最佳化。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 現代 SOC 三層級階層職能\n- **Tier 1 (初階監控分析師 - Triage)**：7x24 輪班監控 SIEM/EDR 警報，進行初步真偽判定 (True Positive vs False Positive)，過濾低危雜訊，將確認事件升級至 Tier 2。\n- **Tier 2 (資深應變分析師 - Incident Responder)**：深入調查確認受災範圍，分析惡意載具行為，執行短期圍堵（如網路隔離）與清除。\n- **Tier 3 (高階威脅獵捕與鑑識專家 - Threat Hunter)**：主動假說獵捕內部潛伏威脅、逆向工程分析、自研關聯分析規則、指導 SOAR 自動化編排。\n\n#### 2. SIEM 關聯分析 (Correlation Analysis) 實務模型\n- 單一事件通常無害，**多源時間關聯**方能顯現真實攻擊鏈：\n  - *案例：暴力破解成功攻擊鏈*：\n    1. 條件 A：端點在 5 分鐘內累積發生超過 10 次 Event ID 4625 (登入失敗)。\n    2. 條件 B：緊接著在第 6 分鐘出現同一帳號之 Event ID 4624 (登入成功)。\n    3. 條件 C：該帳號在登入成功後 1 分鐘內，發起向非授權外部 IP 之異常連線。\n    4. *動作*：觸發「緊急重大威脅警報 (Critical Alert)」。\n\n#### 3. SOAR (自動化編排與回應) 劇本 (Playbook)\n- **警報疲勞 (Alert Fatigue)**：SOC 每天收到數萬筆警報，分析師因過載產生麻痺，導致重大威脅被漏失。\n- **SOAR 價值**：將高度重複、標準化之調查應變流程自動化編排：\n  - *釣魚郵件自動處置劇本 (Phishing Playbook)*：\n    1. 員工通報可疑郵件 -> 2. SOAR 自動解析 EML 標頭與附件 -> 3. 提取 URL 與檔案雜湊呼叫情資 API (VirusTotal) 查詢 -> 4. 判定為惡意 -> 5. 自動自郵件伺服器全面刪除該郵件 -> 6. 下發惡意網址至邊界防火牆黑名單 -> 7. 自動關閉工單並回信感謝員工。\n  - 將平均應變時間 (**MTTR**) 從數小時壓縮至 **數秒鐘**！\n\n### 二、實務技術落地與規則語法 (SIEM / YARA-L Logic)\n\n```text\n// Google Chronicle / SIEM 關聯規則範例：密碼噴灑與異常外連\nrule Password_Spray_And_Exfil {\n  meta:\n    description = \"偵測短時間多帳號登入失敗後單一成功並向外連線\"\n    severity = \"CRITICAL\"\n  events:\n    // 收集同一來源 IP 之多次失敗\n    $fail.metadata.event_type = \"USER_LOGIN\"\n    $fail.security_result.action = \"BLOCK\"\n    $source_ip = $fail.principal.ip\n\n    // 後續成功登入\n    $success.metadata.event_type = \"USER_LOGIN\"\n    $success.security_result.action = \"ALLOW\"\n    $success.principal.ip = $source_ip\n\n  match:\n    $source_ip over 5m\n  condition:\n    #fail >= 10 and #success >= 1\n}\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| SOC 維運觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **SIEM vs SOAR** | 題目問「負責自動化調用 API 隔離受害端點並封鎖 IP 的系統是？」考生誤選 SIEM | **SOAR (安全性協同作業、自動化與回應)**。SIEM 專職「收集與關聯分析」，SOAR 專職「自動化回應與編排」 |\n| **警報疲勞解決手段** | 選項宣稱「調高告警閥值或關閉警報即可解決警報疲勞」 | **嚴重錯誤！應透過 SOAR 自動化過濾雜訊、情資富化與微調關聯規則** |\n| **MTTR 指標** | 題目問 MTTR 代表什麼意涵？ | **平均復原時間 (Mean Time to Respond / Recover)**，數值越低代表應變效率越高 |\n\n> 🔑 **防呆口訣**：\n> - SIEM 集中算關聯，SOAR 編排自動阻。\n> - 警報疲勞靠劇本，秒級處置降 MTTR！\n        ",
            "caseStudy": "【實務案例分析】某金控 SOC 團隊每天面臨超過 15,000 筆安全警報，一線分析師疲於奔命導致離職率居高不下。新任 CISO 引進 SOAR 平台建置自動化回應劇本：針對佔比 70% 的外部暴力破解與釣魚郵件通報，由 SOAR 機器人自動提取 IP 與附件，調用威脅情資自動判定。若為誤報自動結案並反饋調整規則，若確認為真實惡意則由機器人直接呼叫防火牆 API 阻斷並在 EDR 隔離受害機器。導入後，人工作業警報量驟減 85%，平均威脅應變時間 (MTTR) 由 180 分鐘大幅縮減至 45 秒。"
          },
          {
            "id": "M2-M04",
            "title": "單元 4：CSIRT 資安事件應變五大階段實務指南",
            "keywords": [
              "CSIRT",
              "Incident Response",
              "NIST SP 800-61 Rev.2",
              "Containment",
              "Eradication",
              "Lessons Learned"
            ],
            "summary": "掌握國際標準 NIST SP 800-61 Rev.2 電腦安全性事件處理生命週期：準備 (Preparation)、偵測與分析 (Detection & Analysis)、圍堵/抹除與復原 (Containment, Eradication & Recovery)、事後檢討 (Lessons Learned)；深入掌握攻擊指標 (IoC) 萃取、短期 vs 長期圍堵策略與 PIR 會議召開實務。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. NIST SP 800-61 Rev.2 事件應變四大循環維度\n1. **準備階段 (Preparation)**：\n   - 建立 CSIRT (電腦安全事件應變小組) 組織架構與緊急通訊錄（包含法務、公關、外部專家與執法機關）。\n   - 準備經安全校驗之鑑識工具箱 (Jump Kit / Forensic Workstation)。\n   - 建立應變作業手冊 (Playbooks)、啟用足夠深度之系統日誌與離線備份。\n2. **偵測與分析 (Detection & Analysis)**：\n   - 確認事件真偽 (Verification)，排除誤報。\n   - 界定攻擊範圍 (Scope Assessment)：哪些伺服器、帳號與網段受害？\n   - 萃取「受害指標 (Indicators of Compromise, IoC)」：惡意檔案 SHA-256、C2 IP、惡意網域、異常排程。\n   - 評定嚴重等級並依法規時限通報 (如台灣資安法 1 小時內通報)。\n3. **圍堵、抹除與復原 (Containment, Eradication, and Recovery)**：\n   - **短期圍堵 (Short-term Containment)**：迅速限制災害擴散（拔掉實體網線、EDR 網路隔離受害主機、停用受害帳號）。\n   - **長期圍堵 (Long-term Containment)**：封鎖外部惡意 C2 IP、在邊界防火牆下發規則、重設網域所有特權密碼。\n   - **抹除 (Eradication)**：全面清除受害系統上之所有後門、木馬、惡意排程與受損帳號。\n   - **復原 (Recovery)**：利用乾淨無染的離線備份還原生產系統，上線後提高監控頻率至少 1~3 個月，防範復發。\n4. **事後活動與檢討 (Post-Incident Activity / Lessons Learned)**：\n   - 於事件平息後兩週內召開「事後檢討會議 (Post-Incident Review, PIR)」。\n   - 回答核心問題：到底發生了什麼？應變團隊表現如何？流程存在哪些破綻？未來如何防範？產出《事件調查總結報告》以持續改進防禦。\n\n### 二、實務技術落地與應變處置 (IR Playbook Steps)\n\n```text\n【勒索軟體爆發之標準遏止處置清單】\n[步驟 1]：嚴禁將受害主機直接強制關機或拔電源！(避免 RAM 鑑識證據與解密金鑰遺失)。\n[步驟 2]：立即實體拔除受害主機網路線，或透過 EDR 發出「網路隔離 (Network Isolation)」。\n[步驟 3]：立即停用遭入侵之網域帳號，並強制撤銷所有作用中 Kerberos TGT 票證 (重設 krbtgt 帳號密碼兩次)。\n[步驟 4]：離線採集記憶體 RAM 傾倒映像。\n[步驟 5]：在核心交換器切斷受害網段與備份網段之路由，保護離線備份。\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 事件應變觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **發現中毒第一動作** | 題目問發現端點正在連線黑客 C2，第一步動作為何？考生誤選「立即重灌作業系統」 | **錯誤！重灌會破壞所有鑑識證據**。第一步應為「**實施圍堵 (如隔離網路)**」，保全證據後再調查分析 |\n| **關機是否正確** | 選項宣稱「發現駭客入侵應立刻拔掉電源插頭關機」 | **嚴重錯誤！拔電源會導致揮發性極高的記憶體 (RAM) 資料永久蒸發**，應進行網路隔離而非斷電 |\n| **事後檢討目的** | 題目問 Lessons Learned 會議主要目的為何？ | **檢討應變流程缺失以改進防禦體系**，絕非「追究懲處個別員工責任」 |\n\n> 🔑 **防呆口訣**：\n> - 應變四部曲：準備、偵測、圍堵抹除、事後檢討。\n> - 拔網線莫拔電源，先圍堵莫急重灌。\n> - 檢討會議抓漏破，改進架構防再犯！\n        ",
            "caseStudy": "【實務案例分析】某大型醫療體系檢驗科伺服器突遭勒索病毒加密。CSIRT 應變小組迅速啟動標準流程：第一線人員嚴格遵循規範，未直接拔掉電源，而是立即拔除網路線並使用 EDR 進行邏輯隔離，成功將病毒封鎖於單一檢驗主機；隨後鑑識人員進入現場，在通電狀態下完整提取 32GB 記憶體與磁碟映像；團隊透過分析記憶體鎖定惡意 C2 連線特徵與注入之 PowerShell 指令，進而於全院邊界全面阻斷該 IP；最後調取離線冷備份完成無毒還原，病患檢驗業務於 6 小時內恢復，並於兩週後召開 PIR 會議更新全院防火牆防禦規則。"
          },
          {
            "id": "M2-M05",
            "title": "單元 5：數位鑑識、證據保全與記憶體鑑識實務",
            "keywords": [
              "Digital Forensics",
              "Order of Volatility",
              "Chain of Custody",
              "Hardware Write Blocker",
              "Bit-stream Image",
              "Volatility 3"
            ],
            "summary": "掌握司法級數位鑑識核心規範 (RFC 3227)：揮發性順序 (Order of Volatility)、證據監管鏈 (Chain of Custody)、只讀硬體防寫阻斷器 (Hardware Write Blocker)、位元對位元磁碟映像 (Bit-stream Image E01/RAW)、雜湊完整性比對、以及利用 Volatility 3 實施記憶體 (RAM) 鑑識萃取無檔案木馬。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 證據揮發性順序 (Order of Volatility - RFC 3227 必考！)\n現場採證時，必須**按照資料隨時間蒸發消失的速度，由最易揮發者依序優先採集**：\n1. **暫存器 (Registers) 與 快取記憶體 (Cache)** (數十奈秒內即消失)。\n2. **隨機存取記憶體 (RAM / Physical Memory)** (包含動態進程、解密金鑰、未存檔文件、網路連線)。\n3. **網路狀態與連線 (Network State)** (現存 TCP/UDP 連線表、ARP 快取、路由表)。\n4. **執行中進程狀態 (Running Processes)**。\n5. **硬碟實體儲存媒體 (Disk / Internal Storage)**。\n6. **遠端記錄日誌與監控數據 (Remote Logging & Monitoring Data)**。\n7. **實體網路拓撲配置與備份媒體 (Physical Topology & Archival Media)** (最不易揮發)。\n\n#### 2. 證據監管鏈 (Chain of Custody, CoC)\n- 確保數位證據在進入法庭審理時具備「證據能力 (Admissibility)」的法定紀錄文件。\n- **詳載項目**：證據採集時間、確切地理位置、原始雜湊值 (SHA-256)、採集人姓名職稱、每次移交保管之經手人簽名、移交目的、儲存環境。\n- 若監管鏈出現斷點（例如證物在未記錄的情況下被非授權人員移轉數小時），證據將因存在「遭篡改之合理懷疑」而**被法官裁定無效**！\n\n#### 3. 磁碟採證黃金法則\n- **嚴禁在原始硬碟上直接操作分析**！\n- 採集時必須串接「**硬體防寫設備 (Hardware Write Blocker)**」，物理硬體層級徹底阻絕任何寫入訊號。\n- 製作 **位元對位元映像 (Bit-stream Image / Forensic Duplicate)**（包含未配置空間 Unallocated Space 與檔案鬆弛空間 Slack Space，非一般邏輯檔案複製）。\n- 採集前後必須立即計算原始硬碟與映像檔之 **SHA-256 雜湊值**，兩者雜湊值必須百分之百一致。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. Linux dd 製作司法映像與雜湊校驗\n```bash\n# 使用 dd 進行位元對位元複製 (來源為 /dev/sdb，輸出為 forensic.raw)\ndd if=/dev/sdb of=/evidence/forensic.raw bs=4096 status=progress conv=noerror,sync\n\n# 計算原始設備與映像檔之 SHA-256 進行雙向校驗\nsha256sum /dev/sdb\nsha256sum /evidence/forensic.raw\n```\n\n#### 2. Volatility 3 實體記憶體鑑識實戰指令\n```bash\n# 1. 檢視採集記憶體中當時所有執行之進程樹 (尋找可疑衍生關係)\nvol -f memdump.raw windows.pstree\n\n# 2. 檢視當時建立的現存網路連線 (比對惡意外部 C2 IP)\nvol -f memdump.raw windows.netscan\n\n# 3. 掃描記憶體中注入的未命名可執行代碼 (偵測無檔案注入)\nvol -f memdump.raw windows.malfind\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 數位鑑識觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **揮發性順序首位** | 題目問現場第一優先採集之資料為何？ | **記憶體 (RAM / Registers)** 優先於硬碟檔案與備份磁帶 |\n| **複製檔案 vs 映像** | 選項宣稱「用隨身碟將受害主機 C 槽檔案複製出來即可分析」 | **嚴重錯誤！那只是邏輯複製 (Logical Copy)**，無法擷取已刪除檔案與未配置空間；必須做 **Bit-stream Image** |\n| **雜湊不符之後果** | 題目問若映像檔 SHA-256 與採集前原始磁碟雜湊不相符時代表何意？ | **證據已被篡改或損壞，喪失法庭證據能力** |\n\n> 🔑 **防呆口訣**：\n> - 鑑識首重揮發性：快取、RAM、網路先，硬碟、磁帶最後延。\n> - 硬體防寫串在前，位元映像不可偏。\n> - 雜湊前後相吻合，監管鏈全上法庭！\n        ",
            "caseStudy": "【實務案例分析】執法單位配合資安鑑識專家查抄某跨國勒索軟體集團之洗錢跳板機房。工程師抵達現場時，主機螢幕仍處於登入狀態。鑑識專家阻止了員警拔插頭的動作，嚴格按照 RFC 3227 揮發性順序：第一時間使用專用硬體記憶體擷取器導出 64GB 實體 RAM；隨後將硬碟卸下串接硬體防寫阻斷器，產出 raw 位元映像並校驗 SHA-256。團隊在 Volatility 記憶體分析中，成功提取出尚未被釋放的加密通訊金鑰與記憶體注入木馬，並在法庭出示無懈可擊的監管鏈文件，最終使嫌犯無從抵賴俯首認罪。"
          },
          {
            "id": "M2-M06",
            "title": "單元 6：安全軟體開發 (SSDLC) 與 DevSecOps 實務",
            "keywords": [
              "SSDLC",
              "DevSecOps",
              "STRIDE Threat Modeling",
              "SAST",
              "DAST",
              "IAST",
              "SCA",
              "Shift Left"
            ],
            "summary": "掌握安全軟體開發生命週期 (SSDLC) 與 DevSecOps 落地：安全左移 (Shift Left) 理念、微軟 STRIDE 威脅建模方法論、CI/CD 安全流水線自動化整合、靜態代碼分析 (SAST)、動態應用檢測 (DAST)、互動式測試 (IAST) 與開源軟體成分分析 (SCA) 實戰評估。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 安全左移 (Shift Left) 經濟學原理\n- **軟體生命週期漏洞修復成本**：\n  - 設計/架構階段發現漏洞並修復：成本約 **$1x**（只需修改設計圖與規格書）。\n  - 編碼階段修復：成本約 **$5x**。\n  - 測試階段修復：成本約 **$15x**。\n  - **正式上線 (Production) 後才發現漏洞**：成本高達 **$30x ~ $100x**！（面臨緊急停機、重新編譯發布、商譽損失、個資外洩訴訟與監管罰款）。\n- **核心理念**：資安考量必須「向左延伸至需求與架構初期」，而非在最後上線前夕才做一次掃描。\n\n#### 2. 微軟 STRIDE 威脅建模模型 (必考對照！)\n\n| 威脅字母與名稱 | 攻擊者企圖手法 | 違反之資安屬性 | 標準技術防禦對策 |\n| :--- | :--- | :--- | :--- |\n| **S - 偽冒身分 (Spoofing)** | 偽裝成其他合法使用者或伺服器 | **身分鑑別 (Authentication)** | 多因素驗證 (MFA)、數位憑證、FIDO2 |\n| **T - 竄改資料 (Tampering)** | 惡意修改傳輸中或存儲中的資料代碼 | **完整性 (Integrity)** | 數位簽章、SHA-256 雜湊、ACL 權限鎖定 |\n| **R - 否認行為 (Repudiation)** | 否認發起過某筆交易或操作 | **不可否認性 (Non-Repudiation)** | 專屬私鑰簽名、稽核日誌記錄、時間戳記 |\n| **I - 資訊洩漏 (Information Disclosure)** | 竊聽或讀取未經授權之機敏機密資料 | **機密性 (Confidentiality)** | AES-256 加密、TLS 傳輸加密、資料遮罩 |\n| **D - 阻斷服務 (Denial of Service)** | 耗盡運算或網路資源使合法服務癱瘓 | **可用性 (Availability)** | 流量清洗、頻寬限制、資源配額、HA 叢集 |\n| **E - 特權提升 (Elevation of Privilege)** | 一般低權限使用者越權取得 Admin/root | **授權控制 (Authorization)** | 最小權限原則、輸入過濾、避免 SUID/提權弱點 |\n\n#### 3. 現代 DevSecOps 安全檢測工具光譜\n\n| 工具類型 | 運作模式與測試視角 | 優點與價值 | 限制與缺點 |\n| :--- | :--- | :--- | :--- |\n| **SAST (靜態分析)** | **白箱測試 (White-box)**。在編譯期掃描原始程式碼或位元組碼 (如 SonarQube) | 涵蓋率高，能精確定位到原始碼第幾行，可在編譯前執行 | 無法發現運行時 (Runtime) 環境與組態錯誤，誤報率偏高 |\n| **DAST (動態分析)** | **黑箱測試 (Black-box)**。對運行中系統發送 HTTP 攻擊 Payload (如 OWASP ZAP) | 能發現伺服器組態與綜合脆弱性，誤報率較低 | 無法定位原始碼行數，無法掃描未公開之內部後端 API |\n| **SCA (軟體成分分析)** | 掃描相依之第三方與開源套件 (如 Snyk) | 迅速識別具已知 CVE 的老舊元件與授權風險 | 無法檢測自行編寫的客製業務邏輯漏洞 |\n\n### 二、實務技術落地與 CI/CD 流水線配置 (GitLab CI / GitHub Actions)\n\n```yaml\n# GitHub Actions DevSecOps 流水線範例\nname: DevSecOps_Pipeline\non: [push, pull_request]\n\njobs:\n  security_gate:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n\n      # 步驟 1：執行 SCA 開源依賴項檢測\n      - name: Dependency Vulnerability Check (SCA)\n        uses: snyk/actions/node@master\n        env:\n          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}\n\n      # 步驟 2：執行 SAST 靜態程式碼安全掃描\n      - name: Static Code Analysis (SAST)\n        uses: github/codeql-action/analyze@v2\n\n      # 步驟 3：安全門檻檢查 (Gate)\n      - name: Break Build if Critical Vulnerabilities Exist\n        run: |\n          if [ \"$CRITICAL_COUNT\" -gt 0 ]; then\n            echo \"❌ 發現致命漏洞，終止自動上線流程！\"\n            exit 1\n          fi\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 安全開發觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **STRIDE 屬性對照** | 題目問 STRIDE 中的 Repudiation 違反哪項屬性？考生誤選機密性 | **不可否認性 (Non-Repudiation)** |\n| **SAST vs DAST** | 題目問「哪種工具能在不執行程式的情況下精確定位原始碼漏洞行數？」 | **SAST (靜態分析 / 白箱)**；DAST 必須在程式跑起來時從外部測試 |\n| **安全左移本質** | 選項宣稱「安全左移是把所有安全測試移給軟體測試員 (QA) 負責」 | **錯誤！安全左移是指在軟體開發最早期的需求與架構階段即融入資安** |\n\n> 🔑 **防呆口訣**：\n> - 安全左移成本低，拖到上線百倍賠。\n> - STRIDE 威脅六字訣：冒(S)、改(T)、賴(R)、洩(I)、癱(D)、篡(E)。\n> - SAST 看源碼定行數，DAST 打黑箱測運行，SCA 專查開源病！\n        ",
            "caseStudy": "【實務案例分析】某網路銀行開發新一代信用卡繳費系統。團隊在需求階段即導入 STRIDE 威脅建模，辨識出「使用者可能篡改 HTTP 請求中的帳單編號越權繳費 (IDOR)」之風險 (對應 Tampering 與 Elevation of Privilege)。開發團隊隨即在架構層制定伺服器端強校驗規範；並將 SAST 與 SCA 工具無縫整合至 GitLab CI 流水線中，設定「只要存在 High 或 Critical 漏洞，自動拒絕 Merge Request 並中斷部屬」。該系統上線前委託第三方紅隊進行黑箱滲透測試，創下零高危漏洞的完美記錄。"
          },
          {
            "id": "M2-M07",
            "title": "單元 7：雲端安全架構 (Cloud Security) 與虛擬化防護",
            "keywords": [
              "Cloud Security",
              "Shared Responsibility Model",
              "CSPM",
              "CWPP",
              "CASB",
              "IAM Least Privilege"
            ],
            "summary": "掌握公有雲安全架構與合規防護：AWS/Azure/GCP 責任共擔模型 (Shared Responsibility Model - IaaS, PaaS, SaaS 責任劃分)、雲端安全狀態管理 (CSPM)、雲端工作負載保護平台 (CWPP)、雲端存取安全代理 (CASB)、影子 IT (Shadow IT) 控管以及雲端 IAM 最小權限落地實務。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 雲端責任共擔模型 (Shared Responsibility Model - 必考核心！)\n\n| 雲端服務模式 | 雲端服務業者 (CSP) 負責安全範疇 | 企業客戶 (Customer) 負責安全範疇 |\n| :--- | :--- | :--- |\n| **IaaS (基礎架構即服務)**<br>*例：AWS EC2, Azure VM* | • 實體資料中心設施、供電空調<br>• 硬體伺服器與儲存設備<br>• 虛擬化 Hypervisor 層架構 | • **作業系統 (OS) 安裝、更新修補與加固**<br>• **網路防火牆安全組 (Security Group)**<br>• 應用系統程式與運行環境<br>• **所有存儲資料之加密與備份** |\n| **PaaS (平台即服務)**<br>*例：Google App Engine, RDS* | • 包含 IaaS 所有項目<br>• **作業系統補丁與硬體維護**<br>• 資料庫引擎與執行環境更新 | • 應用程式本身邏輯與安全代碼<br>• **自身資料庫資料與存取控制權限** |\n| **SaaS (軟體即服務)**<br>*例：Microsoft 365, Salesforce* | • 幾乎全端包辦：從實體設施、底層主機、作業系統至應用程式全部安全維護 | • **使用者身分驗證與帳號生命週期**<br>• **存取授權 (誰能看什麼資料)**<br>• **資料本身的分類、保護與合規治理** |\n\n> ⚠️ **雲端安全唯一不變鐵律**：\n> **不管哪一種雲端模式 (IaaS, PaaS, SaaS)，「資料的擁有權與資料保護責任」永遠百分之百在客戶身上！** 雲端業者絕不代為承擔資料遺失或外洩之最終責任！\n\n#### 2. 現代雲端安全三大利器 (CSPM, CWPP, CASB)\n1. **CSPM (雲端安全狀態管理, Cloud Security Posture Management)**：\n   - 專注於「雲端組態與合規」。自動持續掃描雲端基礎架構，抓出錯誤組態（如：S3 Bucket 被誤設為 Public Read、未開啟 MFA 的 Root 帳號、未加密的 EBS 磁碟）。\n2. **CWPP (雲端工作負載保護平台, Cloud Workload Protection Platform)**：\n   - 專注於「運行時保護」。針對虛擬機器 (VM)、容器 (Docker/Kubernetes) 與無伺服器架構 (Serverless)，提供進程行為監控、漏洞防護與異常入侵偵測。\n3. **CASB (雲端存取安全代理, Cloud Access Security Broker)**：\n   - 位於企業內部網路與多個外部 SaaS 雲端應用之間的安全關卡。提供「影子 IT (Shadow IT)」可視性、防範員工擅自將機敏代碼上傳至個人 Dropbox，並落實雲端 DLP。\n\n### 二、實務技術落地與指令配置 (Technical Implementation & CLI)\n\n#### 1. AWS CLI 稽核意外公開之 S3 儲存桶\n```bash\n# 查詢所有公開讀取的 S3 Bucket 權限 (排查資料外洩缺口)\naws s3api get-public-access-block --bucket my-company-secret-data\n# 強制開啟全域公開存取封鎖 (Block Public Access)\naws s3api put-public-access-block --bucket my-company-secret-data     --public-access-block-configuration \"BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true\"\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| 雲端安全觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **IaaS 作業系統補丁** | 題目問「在 AWS EC2 上的 Windows Server 補丁該由誰負責？」考生常誤選 AWS | **客戶自己負責！** IaaS 模式下作業系統屬於客戶管理範疇 |\n| **SaaS 的客戶責任** | 選項宣稱「導入 SaaS 後企業不必負擔任何資安責任」 | **完全錯誤！客戶依然負責使用者身分認證、存取權限與資料治理** |\n| **CSPM vs CWPP** | 題目問防止 S3 存儲桶設定錯誤導致個資外洩首選工具 | **CSPM (雲端安全狀態管理)**；CWPP 是保護運算節點進程 |\n\n> 🔑 **防呆口訣**：\n> - 責任共擔分層看：IaaS 主機自己顧，PaaS 只要顧代碼，SaaS 帳號自己管。\n> - 資料責任永在己，雲端業者不背鍋！\n> - CSPM 查組態防洩密，CWPP 保工作負載，CASB 攔截影子 IT！\n        ",
            "caseStudy": "【實務案例分析】某數位媒體公司將數百萬會員身分證影本備份於 AWS S3 儲存桶中。維運工程師為圖除錯方便，將該 Bucket 存取權限設置為 `AllUsers: Read`，導致全量資料在網路上裸奔數月。資安團隊介入全面重整：首先導入 CSPM 工具，設定自動化安全基準線，一旦偵測到儲存桶公開即刻自動觸發 Lambda 腳本強制加鎖並通知告警；其次重新設計 IAM 策略，嚴格落實最小權限原則，所有存取必須透過暫時性 STS 憑證並綁定 VPC Endpoint，徹底杜絕公網存取與錯誤組態再犯。"
          },
          {
            "id": "M2-M08",
            "title": "單元 8：進階持續性威脅 (APT) 防禦與主動威脅獵捕 (Threat Hunting)",
            "keywords": [
              "APT Defense",
              "Threat Hunting",
              "Assume Breach",
              "Pass-the-Hash",
              "Kerberoasting",
              "Credential Guard"
            ],
            "summary": "掌握國家級進階持續性威脅 (APT) 攻防與主動獵捕：擺脫被動防禦的「假設已被滲透 (Assume Breach)」思維、假說驅動威脅獵捕 (Hypothesis-driven Hunting) 四步循環、Windows 橫向移動內網核心手法（Pass-the-Hash, Kerberoasting）原理與 Credential Guard 阻絕防禦落地。",
            "content": "\n### 一、核心架構與國際標準對照 (Architecture & Standards)\n\n#### 1. 主動威脅獵捕 (Threat Hunting) 哲學與架構\n- **假設已被滲透 (Assume Breach)**：\n  - 傳統防禦依賴「安全設備被動跳警報」。但 APT 國家級黑客平均潛伏期 (Dwell Time) 長達數百天，黑客使用合法帳密與內建工具，設備完全不跳警報。\n  - 威脅獵捕是指：**主動假設攻擊者已經繞過所有防火牆並潛伏於內網中**，分析師以人為假說主動穿透遙測大數據尋找異常軌跡。\n- **假說驅動獵捕 (Hypothesis-Driven Hunting) 四大步驟**：\n  1. **提出假說 (Hypothesis Generation)**：依據最新威脅情資、同行被駭案例或 ATT&CK 技術提出具體推論（例如：「*我們內網中可能有攻擊者正在濫用 WMI 建立排程以維持開機潛伏*」）。\n  2. **收集指標與遙測分析 (Evidence Collection & Analysis)**：透過 EDR 與 SIEM 撈取全網端點中過去 30 天所有 WMI Event Consumer 的建立紀錄。\n  3. **識別與排查 (Uncover TTPs)**：過濾合法軟體，找出隱匿的未知惡意代碼與受害端點。\n  4. **回饋與自動化固化 (Automation & Hardening)**：將獵捕成功的新特徵轉化為 SIEM 的永久自動偵測規則，並修補系統弱點。\n\n#### 2. Windows 網域橫向移動與憑證竊取三大致命手法\n1. **Pass-the-Hash (PtH，雜湊傳遞攻擊 - T1550.002)**：\n   - 攻擊者不需破解 NTLM 密碼明文，直接自記憶體或 SAM 資料庫傾倒出 NTLM Hash，將該 Hash 作為身分憑證向內網其他主機發起 SMB/RDP 驗證，迅速橫向移動。\n2. **Kerberoasting (T1558.003)**：\n   - 攻擊者身為合法一般網域使用者，向網域控制站 (DC) 請求針對特定服務帳號 (SPN) 的 Kerberos TGS 服務票據。攻擊者將票據導出至本地進行離線暴力破解，還原出高權限服務帳號的明文密碼。\n3. **防禦黃金機制**：\n   - 啟用 **Windows Defender Credential Guard**：利用硬體虛擬化安全 (VBS) 與 Hyper-V 隔離 LSA 機密，黑客即使擁有本機 Administrator 權限亦無法自 LSASS 讀取 NTLM 雜湊或 Kerberos 票證！\n   - 停用 NTLMv1，限制 NTLM 網路驗證，強制使用 Kerberos AES 加密。\n   - 實施主機防火牆嚴禁工作站之間互連 (Workstation-to-Workstation Isolation)。\n\n### 二、實務技術落地與獵捕查詢 (Hunting Queries)\n\n#### 1. PowerShell 獵捕可疑 WMI 持續性潛伏後門\n```powershell\n# 查詢全機所有註冊之 WMI 事件消費者 (常見 APT 潛伏後門)\nGet-CimInstance -Namespace root\\subscription -ClassName __EventConsumer | Select-Object Name, CommandLineTemplate\nGet-CimInstance -Namespace root\\subscription -ClassName __EventFilter | Select-Object Name, Query\n```\n\n#### 2. 檢測全網端點是否已啟用 Credential Guard\n```powershell\n# 檢視本機虛擬化安全隔離保護狀態 (SecurityServicesRunning 包含 1 代表 Credential Guard 已生效)\n(Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\\Microsoft\\Windows\\DeviceGuard).SecurityServicesRunning\n```\n\n### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)\n\n| APT 獵捕觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |\n| :--- | :--- | :--- |\n| **Pass-the-Hash 原理** | 題目問攻擊者發起 PtH 是否必須將 NTLM 雜湊解密為明文？ | **完全不需要！** 攻擊者直接使用雜湊值即可完成 NTLM 挑戰回應驗證 |\n| **威脅獵捕思維** | 選項宣稱「威脅獵捕是等 SIEM 跳出告警後再開始調查」 | **那是被動事件應變！威脅獵捕是「主動出擊」**，在無告警狀態下主動搜尋未知威脅 |\n| **防範 LSASS 竊密** | 考題問防範 Mimikatz 傾倒記憶體最根本之微軟防護技術 | **Windows Defender Credential Guard (基於 VBS 虛擬化安全隔離)** |\n\n> 🔑 **防呆口訣**：\n> - 威脅獵捕假設被駭，主動出擊不等人。\n> - PtH 拿雜湊直接衝，內網防禦切隔離。\n> - Credential Guard 開隔離，Mimikatz 伸手也撲空！\n        ",
            "caseStudy": "【實務案例分析】某國防承包商之威脅獵捕小組基於最新 APT 威脅情資，建立獵捕假說：「黑客可能利用 PsExec 配合竊取之管理員雜湊在內網主機間橫向擴散」。小組分析全網端點日誌，發現一台位於人資部門之普通 PC，在凌晨 02:00 突向財務與研發網段之 50 台伺服器發起大量 TCP 445 連線，並執行 `psexec -u Administrator`。獵捕小組立即確認攻擊者正以 Pass-the-Hash 手法進行內網踩點。安全團隊在攻擊者觸發勒索軟體前，直接隔離該 PC，重設網域密碼，並於全網推播強制啟用 Credential Guard 與工作站互聯阻斷規則，在無任何業務損失下成功殲滅潛伏威脅。"
          }
        ]
      }
    ]
  }
};
