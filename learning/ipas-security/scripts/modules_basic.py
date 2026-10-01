# -*- coding: utf-8 -*-
"""
iPAS 資安工程師 - 初級全 16 單元深度核心講義資料 (教科書級、技術指令、RFC/NIST標準、陷阱盲點、情境案例)
"""

BASIC_SUBJECT_1_MODULES = [
    {
        "id": "B1-M01",
        "title": "單元 1：資安核心三要素與安全架構原則",
        "keywords": ["Confidentiality", "Integrity", "Availability", "Defense-in-Depth", "Least Privilege", "Separation of Duties", "Non-Repudiation", "AAA Framework"],
        "summary": "掌握資訊安全最高指導原則：機密性 (Confidentiality)、完整性 (Integrity)、可用性 (Availability) 之工程實踐。深入解析縱深防禦 (Defense-in-Depth)、最小權限原則 (PoLP)、職責區隔 (SoD) 與不可否認性 (Non-Repudiation) 之技術落地標準。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. CIA 三要素工程定義
- **機密性 (Confidentiality)**：確保僅經授權之主體（人員、進程或系統）能夠讀取或存取受保護資料。
  - *落地控制技術*：靜態資料加密 (AES-256, BitLocker)、傳輸中資料加密 (TLS 1.3, IPsec)、動態資料遮罩 (Data Masking, 隱碼身分證號/信用卡號)、基於角色的存取控制 (RBAC)。
  - *威脅威脅*：竊聽 (Eavesdropping)、網路嗅探 (Sniffing)、資料外洩 (Data Exfiltration)、未授權讀取。
- **完整性 (Integrity)**：確保資訊與通訊系統在生命週期中未遭受未經授權的篡改、插入或刪除，保持正確性與真實性。
  - *落地控制技術*：加密雜湊函數 (SHA-256, SHA-3)、訊息鑑別碼 (HMAC)、數位簽章 (Digital Signature)、檔案完整性監控 (FIM, 如 Tripwire, OSSEC)。
  - *威脅威脅*：中間人攻擊 (MitM) 篡改封包、惡意軟體修改系統檔、未授權資料庫 UPDATE / DELETE。
- **可用性 (Availability)**：確保經授權之主體在業務需要之時，能及時、可靠地存取系統、資料與關鍵服務。
  - *落地控制技術*：伺服器高可用性叢集 (HA Cluster)、負載平衡 (Load Balancing)、DDoS 流量清洗 (Cloudflare / Akamai)、雙迴路不斷電系統 (UPS)、多重異地備援。
  - *威脅威脅*：阻斷服務攻擊 (DoS/DDoS)、勒索軟體全盤加密 (破壞可用性與完整性)、機房火災斷電。

#### 2. 經典架構原則深度解析
1. **縱深防禦 (Defense-in-Depth, DiD)**：
   - 不依賴任何單一防禦機制。建立包含「實體層、網路周邊、內部網段、端點主機、應用程式、資料層、人員意識」的七層同心圓防禦鏈。
   - 單一防線被突破時，後續防線能有效延滯、限縮並告警攻擊行為。
2. **最小權限原則 (Principle of Least Privilege, PoLP)**：
   - 主體僅被賦予執行特定業務任務所必需的最低權限集合，且維持該權限之有效時間僅限於任務執行期間 (Just-in-Time Access)。
   - 禁止日常維運常態使用 `root` 或 `Domain Admins` 特權帳號登入端點。
3. **職責區隔 (Separation of Duties, SoD)**：
   - 將關鍵交易或高風險流程之授權、執行、覆核與稽核職權分配予相異人員，防範單點弊端與單人疏失。
   - *例*：軟體開發者不得擁有生產環境 (Production) 上線發布與直接寫入資料庫之權限。
4. **不可否認性 (Non-Repudiation)**：
   - 透過「發送方專屬私鑰簽章」結合「第三方可信時間戳記 (RFC 3161 TSA)」，使行為發起者事後無法抵賴操作事實。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux 主機最小權限配置 (Sudoers 實務)
```bash
# 編輯 /etc/sudoers (務必使用 visudo 進行語法檢查)
# 嚴格限制網頁維運人員僅能重啟 nginx 服務，嚴禁取得 root shell
webadmin ALL=(ALL) /bin/systemctl restart nginx, /bin/systemctl status nginx
# 禁用通配符與 shell escape 命令
Defaults:webadmin !requiretty, secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"
```

#### 2. 檔案完整性監控 (FIM) 實務腳本
```bash
# 對關鍵系統目錄計算 SHA-256 基準雜湊清單
find /bin /sbin /usr/bin -type f -exec sha256sum {} + > /var/log/baseline_hashes.txt
# 每日排程比對校驗完整性
sha256sum -c /var/log/baseline_hashes.txt --quiet
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 觀念維度 | 考題常見陷阱選項 | 官方標準正解判定 |
| :--- | :--- | :--- |
| **勒索軟體衝擊** | 題目問勒索軟體主要破壞哪一要素，考生常誤選「機密性」 | **可用性 (Availability) 與 完整性 (Integrity)**。勒索軟體旨在鎖死檔案勒索贖金，除非伴隨雙重勒索外洩，否則核心破壞為可用性 |
| **不可否認性技術** | 宣稱「對稱式加密 (AES)」可達成不可否認性 | **錯誤！對稱金鑰由雙方共用**，任一方皆可偽造密文。必須使用「非對稱數位簽章 (Digital Signature)」方具不可否認性 |
| **縱深防禦本質** | 誤以為縱深防禦是「安裝兩套不同廠牌的防毒軟體」 | **多維度、多層次互補控管**（實體、網路、主機、應用、人員），而非單一層次之軟體重複堆疊 |

> 🔑 **防呆口訣**：
> - 機密靠加密與 ACL，完整靠雜湊與簽名，可用靠備援與清洗。
> - 對稱加密速度快但無不可否認，非對稱簽章具專屬私鑰才算數！
        """,
        "caseStudy": "【實務案例分析】某電商平台遭遇外部攻擊，駭客利用 Web 伺服器之 SQL 注入弱點突破前端。然而，該企業貫徹了「縱深防禦」與「最小權限原則」：Web 伺服器與資料庫伺服器之間存在內網次世代防火牆，嚴格僅開放 TCP 3306 且僅限指定 IP；資料庫中會員身分證字號與信用卡均採用 AES-256-GCM 密文存儲，且資料庫連線帳號僅具備 SELECT/INSERT 權限而無 DROP/ALTER 特權。駭客即便成功透過 SQL 注入取得前端部分資料，但無法提權橫向移動至內網核心網段，機敏欄位亦因密文防護無法即時破解，成功將災害控制於最低範圍。"
    },
    {
        "id": "B1-M02",
        "title": "單元 2：網路通訊協定與架構安全",
        "keywords": ["OSI 7 Layers", "TCP 3-Way Handshake", "TLS 1.3", "IPsec", "DNSSEC", "DMZ Network Architecture"],
        "summary": "全面剖析 OSI 7 層模型與 TCP/IP 協定堆疊之安全缺陷與防禦機制。深入探討 TCP 三向交握、SYN Flood 攻擊與 SYN Cookies 緩解機制、TLS 1.3 密碼套件精簡與 0-RTT 權衡、IPsec AH/ESP 模式、DNSSEC 以及企業 DMZ 隔離區規劃架構。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. OSI 7 層與常見威脅／防禦對照表
- **第 7 層 應用層 (Application)**：HTTP/HTTPS, DNS, SMTP, SSH。
  - *威脅*：SQL Injection, XSS, DNS 偽冒, HTTP Flood。
  - *防禦*：WAF (第7層檢測), DNSSEC, SPF/DKIM/DMARC。
- **第 4 層 傳輸層 (Transport)**：TCP, UDP。
  - *威脅*：TCP SYN Flood, UDP Amplification, 連線劫持。
  - *防禦*：SYN Cookies, 防火牆狀態表過濾, 流量閥值限制。
- **第 3 層 網路層 (Network)**：IP, ICMP, IPsec。
  - *威脅*：IP 偽造 (IP Spoofing), Smurf 攻擊, ICMP Flood。
  - *防禦*：IPsec (RFC 4301), 單播反向路徑轉發 (uRPF), 防火牆封鎖 ICMP。
- **第 2 層 資料鏈結層 (Data Link)**：以太網 (Ethernet), ARP, 802.1Q VLAN。
  - *威脅*：ARP 欺騙 (ARP Spoofing), MAC 氾濫, CAM 表溢位, VLAN 跳躍。
  - *防禦*：動態 ARP 檢驗 (DAI), DHCP Snooping, 連接埠安全 (Port Security)。

#### 2. TCP 三向交握 (3-Way Handshake) 與 SYN Flood
- **標準交握流程**：
  1. 客戶端發送 `SYN` (Seq = x) -> 伺服器端進入 `SYN_RCVD` 狀態，分配 TCB (傳輸控制區塊) 資源。
  2. 伺服器回覆 `SYN/ACK` (Seq = y, Ack = x + 1)。
  3. 客戶端回覆 `ACK` (Seq = x + 1, Ack = y + 1) -> 雙方進入 `ESTABLISHED`。
- **SYN Flood 阻斷服務攻擊原理**：
  - 攻擊者發送巨量偽造來源 IP 的 `SYN` 封包，伺服器發送 `SYN/ACK` 後因找不到真實客戶端而處於半開啟連線狀態 (Half-open connection)。半開連線隊列 (Backlog Queue) 迅速耗盡，導致合法使用者無法建立連線。
- **SYN Cookies 緩解原理**：
  - 伺服器在收到 SYN 時**不分配**記憶體 TCB 資源，而是利用客戶端 IP、Port、時間戳記與伺服器密鑰計算出一個加密雜湊作為 Initial Sequence Number (ISN)。只有當客戶端回覆合法 ACK 且計算驗證相符時，才分配連線資源。

#### 3. TLS 1.3 (RFC 8446) 核心技術革新
- **交握延遲降至 1-RTT** (舊版 TLS 1.2 為 2-RTT)，並支援 0-RTT 早期資料 (Early Data，注意：0-RTT 易受重送攻擊 Replay Attack)。
- **徹底廢棄不安全密碼學演算法**：移除 RSA 金鑰交換 (全面強制具備完全前向保密 PFS 之 (EC)DH)、移除 CBC 分組模式、移除 RC4、MD5、SHA-1。
- 僅保留極度精簡安全密碼套件：`TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_AES_128_GCM_SHA256`。

#### 4. DMZ (Demilitarized Zone) 拓撲原則
- **拓撲定義**：位於內部核心私有網路與外部網際網路之間的隔離緩衝網段。
- **存取控制鐵律 (Golden Rules)**：
  1. Internet 訪客僅允許連線至 DMZ 之特定公眾服務 Port (如 443, 80, 25)。
  2. DMZ 伺服器**絕對禁止主動發起**連線至內部信任網路 (Internal Trusted LAN)！
  3. 內部核心資料庫嚴禁置於 DMZ；資料庫應置於內部安全網段，由 DMZ 應用程式透過嚴格受控之代理或單向連線訪問。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux 核心啟用 SYN Cookies 防護
```bash
# 檢查當前 SYN Cookies 狀態 (1 為啟用)
sysctl net.ipv4.tcp_syncookies
# 寫入 /etc/sysctl.conf 進行永久硬化
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.tcp_synack_retries = 2
sysctl -p
```

#### 2. 交換器連接埠安全配置 (Cisco Switch Port Security)
```text
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 通訊協定 / 概念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **IPsec AH vs ESP** | 題目問哪一個協定提供「資料加密 (機密性)」 | **ESP (封裝安全酬載)** 提供加密與完整性；**AH (認證標頭)** 僅提供認證與完整性，**絕不提供加密**！ |
| **DMZ 網路規則** | 選項宣稱「DMZ 伺服器被駭後可主動連入內網排解」 | **嚴重違規！** DMZ 嚴禁主動向內網發起 TCP 握手連線 |
| **TLS 1.3 金鑰交換** | 題目問 TLS 1.3 是否仍支援靜態 RSA 加密金鑰交換 | **已全面廢除！** 強制使用具備 PFS (完全前向保密) 之 Ephemeral Diffie-Hellman (DHE/ECDHE) |

> 🔑 **防呆口訣**：
> - AH 認證無加密，ESP 封裝才加密。
> - SYN Flood 塞半開，Cookies 計算免耗台。
> - DMZ 防火牆：外入有限度，內往外可通，DMZ 往內全面封！
        """,
        "caseStudy": "【實務案例分析】某大型醫院對外掛號系統遭受巨量 TCP SYN Flood 攻擊，伺服器連線狀態表瞬間被數百萬個半開啟連線填滿，造成正常病患無法掛號。資安維運團隊緊急採取三合一措施：第一、在邊界次世代防火牆啟用 TCP SYN Proxy，阻絕偽造來源之無效交握；第二、在 Linux 伺服器核心開啟 `net.ipv4.tcp_syncookies = 1`，避免 TCB 記憶體枯竭；第三、啟用電信端清洗中心過濾非台灣境內異常網段，系統於 15 分鐘內恢復正常運作。"
    },
    {
        "id": "B1-M03",
        "title": "單元 3：作業系統與主機端點安全強化",
        "keywords": ["OS Hardening", "CIS Benchmark", "Windows GPO", "Linux Hardening", "Patch Management", "Privilege Escalation"],
        "summary": "掌握 Windows Active Directory 與 Linux 主機安全性基準強化 (Baseline Hardening)、CIS Benchmark 控制項落實、弱密碼與帳號原則、SSH 安全組態、補丁管理生命週期與提權攻擊防範。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 作業系統安全強化四大核心維度
1. **最小化受攻擊面 (Attack Surface Reduction)**：
   - 停用或移除系統非必要之服務與應用（如 Telnet, FTP, Rexec, 關閉 SMBv1 協定）。
   - 停用所有未授權之監聽連接埠 (Listening Ports)。
2. **身分鑑別與特權存取控制**：
   - 禁用預設帳號或將其更名（如停用 Guest 帳號，重命名 Administrator / root）。
   - 嚴禁空密碼，強制設定高複雜度與歷史不可重複密碼原則。
   - 設定帳戶鎖定閾值 (Account Lockout Threshold，例如 5 次失敗鎖定 30 分鐘)，阻斷暴力破解與密碼噴灑。
3. **系統日誌與稽核追蹤**：
   - 啟用成功與失敗之登入稽核 (Audit Logon Events)、權限使用稽核與特權提升追蹤。
4. **軟體補丁生命週期 (Patch Management)**：
   - 依據 CVSS 分數與在野利用情資 (CISA KEV)，在受控的測試環境驗證相容性後，以自動化工具 (WSUS, SCCM, Ansible) 於時限內發布至生產環境。

#### 2. CIS Benchmarks 國際主機基準規範
- 國際網際網路安全中心 (CIS) 為 Windows Server、RHEL、Ubuntu 等制訂之安全基準：
  - **Level 1 基準**：基礎防護等級，提供必要安全性且對系統效能與應用程式相容性影響極低。
  - **Level 2 基準**：高安全性環境（深度防禦），包含更嚴格的限制（可能限制部分相容性，適用機敏主機）。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux SSH 服務核心強化組態 (`/etc/ssh/sshd_config`)
```bash
# 禁止 root 透過 SSH 直接登入 (強制一般使用者登入後再 su/sudo)
PermitRootLogin no
# 禁用密碼認證，強制公鑰認證
PasswordAuthentication no
PubkeyAuthentication yes
# 禁用空密碼
PermitEmptyPasswords no
# 限制最大認證嘗試次數 (防暴力破解)
MaxAuthTries 3
# 停用危險的 X11 轉發
X11Forwarding no
# 重啟服務生效
systemctl restart sshd
```

#### 2. Windows 帳號與安全原則 GPO 指令檢視
```cmd
:: 匯出目前本地安全策略配置進行稽核
secedit /export /cfg C:\secpol_backup.inf
:: 查詢本機當前密碼原則
net accounts
:: 檢視當前所有監聽通訊埠與關聯進程 PID
netstat -ano | findstr "LISTENING"
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 考題情境與機制 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **更新管理流程** | 題目問「取得最新高危安全性修補程式後，第一步動作為何？」考生常誤選「立即推播更新全公司伺服器」 | **錯誤！第一步必須先在測試環境 (Test Environment) 驗證相容性**，確認無當機與服務衝突後方可排程部署上線 |
| **SMBv1 協定** | 考題問防範 WannaCry 蠕蟲最根本的端點組態 | **徹底停用 SMBv1 協定並安裝 MS17-010 補丁**。SMBv1 存在嚴重遠端代碼執行 (RCE) 漏洞 |
| **帳戶鎖定閥值** | 題目問設定帳戶鎖定是否萬無一失 | 注意「帳戶鎖定機制可能被攻擊者用作 DoS 阻斷服務攻擊（蓄意使合法使用者遭鎖定）」，需搭配鎖定時間自動解鎖與 IP 速率限制 |

> 🔑 **防呆口訣**：
> - 補丁先測再上線，空密預設全拔除。
> - SSH 禁 root 密碼，GPO 強制長與複。
> - 服務沒用立即關，SMBv1 永不再見！
        """,
        "caseStudy": "【實務案例分析】某政府機關內部一台對外 Linux 伺服器遭受攻擊者透過 SSH 字典檔攻擊入侵。事後鑑識發現，該伺服器允許 `PermitRootLogin yes` 且使用預設密碼，未受限制之 SSH 服務被嘗試了 4 萬多次成功破門。資安改善小組全面依照 CIS Benchmark 進行強化：全面改採 ED25519 金鑰認證並關閉密碼登入、安裝 `fail2ban` 自動封鎖惡意嘗試 IP、移除非必要之 FTP/Telnet 服務，並配置每週自動掃描主機合規基準，杜絕同類資安缺口。"
    },
    {
        "id": "B1-M04",
        "title": "單元 4：常見資安威脅與惡意程式防護",
        "keywords": ["Ransomware", "Computer Worm", "Trojan Horse", "Spyware", "Rootkit", "Botnet", "Social Engineering", "BEC"],
        "summary": "深入辨析各類惡意程式（Malware）之行為特徵與傳播模式：電腦蠕蟲自我複製、特洛伊木馬後門機制、勒索軟體雙重/三重勒索手腕、隱匿型 Rootkit、殭屍網路 (Botnet) 與商業電子郵件詐騙 (BEC) 社交工程防禦體系。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 惡意程式核心類別深度特徵對照
1. **電腦蠕蟲 (Worm)**：
   - *傳播特徵*：**具備高度自我複製與網路主動掃描傳播能力**。不需依附於宿主執行檔 (Host Program)，亦不需人為點擊觸發，利用作業系統或協定弱點（如 SMB, RPC）自主感染整座區網。
   - *代表案例*：WannaCry, Conficker, SQL Slammer。
2. **特洛伊木馬 (Trojan Horse)**：
   - *傳播特徵*：偽裝成合法、有用或無害之應用軟體（如修圖軟體、遊戲外掛、發票 PDF），誘騙使用者主動下載並執行。執行後於背景植入後門 (Backdoor) 或連線 C2 伺服器。**不具備自主傳染複製能力**。
3. **勒索軟體 (Ransomware)**：
   - *演進模式*：
     - *第一代 (加密勒索)*：本地高強度非對稱/對稱加密（AES + RSA），銷毀磁碟陰影複製 (Volume Shadow Copies)。
     - *第二代 (雙重勒索 Double Extortion)*：加密前先將機敏資料竊取外傳 (Exfiltration)，威脅「不付贖金即公開於暗網洩密網站」。
     - *第三代 (三重勒索 Triple Extortion)*：加密 + 外洩曝光 + 對其客戶發動 DDoS 或電話騷擾。
4. **隱匿工具 (Rootkit)**：
   - 運作於作業系統核心層 (Kernel Mode, Ring 0) 或韌體層，攔截作業系統 API，**將惡意進程、網路通訊埠與登錄檔在工作管理員與系統檢視器中完全隱形隱匿**。
5. **殭屍網路 (Botnet)**：
   - 數萬台受木馬感染的主機（殭屍節點 / Bot）受控於指令與控制伺服器 (C2 / Command and Control)，接受發起大規模 DDoS 攻擊或發送垃圾郵件。

#### 2. 商業電子郵件詐騙 (BEC) 社交工程攻擊鏈
- **攻擊模式**：攻擊者透過偽造寄件者位址 (Email Spoofing)、近音相似網域 (Typosquatting) 或盜用高層郵件帳號，精準鎖定財務主管或出納人員，下達緊急匯款至海外帳戶之指示。
- **關鍵防禦政策**：涉及金錢轉帳或變更收款帳戶者，嚴格落實「雙人核可 (Dual Authorization)」與「離線電話雙向照會 (Out-of-band Verification)」。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Windows 端點排查惡意持續潛伏 (Persistence)
```powershell
# 檢視系統所有啟動項目 (Run Keys)
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Get-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Run

# 查詢所有排程工作是否存在異常外連腳本
Get-ScheduledTask | Where-Object {$_.State -ne "Disabled"} | Select-Object TaskName, TaskPath, Actions
```

#### 2. 防範勒索軟體清空陰影複製之防護 (vssadmin 監控)
```cmd
:: 勒索軟體經典前置指令：
:: vssadmin.exe delete shadows /all /quiet
:: wmic shadowcopy delete
:: 防護措施：透過 EDR 或 GPO 限制一般與管理使用者無預警執行 vssadmin.exe
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 惡意程式類型 | 考題常見混淆陷阱 | 官方標準正解判定 |
| :--- | :--- | :--- |
| **蠕蟲 vs 木馬** | 題目問「哪種惡意程式不需要宿主程式與人為介入即可自動在網路上擴散？」考生誤選木馬 | **蠕蟲 (Worm)**。木馬需靠偽裝誘騙點擊，病毒需宿主程式，唯有蠕蟲具獨立自我複製網路傳播能力 |
| **Rootkit 偵測** | 以為一般工作管理員可以看到 Rootkit 進程 | **無法看到！** Rootkit 篡改了核心系統呼叫 (System Hooking)，必須透過乾淨離線系統 (Live CD) 進行底層映像比對 |
| **釣魚防護** | 題目問防範 BEC 詐騙最佳方法，考生誤選「購買更高等級的防火牆」 | **程序規範 (SOP) 與多重管道照會**。社交工程直擊人性與商業流程，傳統防火牆無法判定信件內容文字之真實詐欺意圖 |

> 🔑 **防呆口訣**：
> - 蠕蟲無須人介入，自主爬網全感染。
> - 木馬偽裝騙點擊，後門常開連 C2。
> - 匯款信件莫輕信，第二管道打電話！
        """,
        "caseStudy": "【實務案例分析】某高科技零組件製造商財務出納收到「董事長」從海外發來的緊急郵件，宣稱正在進行跨國併購機密談判，要求於當天下午三點前將 50 萬美元定金匯入指定香港銀行帳戶，並附上蓋有印鑑之合約影本。該出納察覺寄件者郵件網域結尾為 `.co` 而非公司正式的 `.com.tw` (近音網域欺騙)。出納秉持資安 SOP，撥打董事長隨行秘書之電話進行雙向照會，確認董事長根本未發出此信，成功攔阻了典型 BEC 商業社交工程詐騙。"
    },
    {
        "id": "B1-M05",
        "title": "單元 5：應用系統安全與 OWASP Top 10 核心漏洞",
        "keywords": ["SQL Injection", "XSS", "CSRF", "IDOR", "SSRF", "OWASP Top 10", "Prepared Statements"],
        "summary": "掌握 Web 應用程式安全防護核心：深度剖析 OWASP Top 10 核心漏洞成因與防護。重點攻克 SQL 注入 (SQLi) 參數化查詢防護、跨網站腳本 (XSS) 輸出編碼與 HttpOnly Cookie、跨網站請求偽造 (CSRF) Token、不安全直接物件參照 (IDOR) 與 SSRF 漏洞。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 注入攻擊 (SQL Injection, SQLi) 深度剖析
- **漏洞根因**：應用程式將來自外部不可信任的使用者輸入，直接以字串串接 (Concatenation) 方式拼裝至動態 SQL 語句中，導致直譯器將資料誤解析為程式指令執行。
- **經典攻擊範例**：`SELECT * FROM users WHERE user = 'admin' AND pass = '' OR '1'='1';`
- **防禦唯一解法**：**全面採用參數化查詢 (Parameterized Queries / Prepared Statements) 或 ORM**。資料與代碼在編譯期即分開解析，輸入值永遠僅被視為常數字串變數，絕不被當作語法執行。

#### 2. 跨網站腳本 (Cross-Site Scripting, XSS)
- **類別辨析**：
  1. **儲存型 XSS (Stored XSS)**：惡意腳本存入資料庫（如留言板、使用者個人暱稱），每次任何受害者瀏覽該頁面時都會觸發執行。危害最大。
  2. **反射型 XSS (Reflected XSS)**：惡意腳本包裝於 URL 查詢參數中，誘騙受害者點擊釣魚連結觸發。
  3. **DOM-based XSS**：純前端客戶端 JavaScript 解析脆弱引起。
- **縱深防護機制**：
  - 情境感知輸出編碼 (Context-aware Output Encoding，將 `<` 轉為 `&lt;`，`>` 轉為 `&gt;`)。
  - 對儲存 Session ID 的 Cookie 標記 **`HttpOnly`** 屬性（禁止 JavaScript 透過 `document.cookie` 讀取）。
  - 配置內容安全策略 (Content Security Policy, CSP)。

#### 3. 權限控制失效 (Broken Access Control)
- **IDOR (不安全直接物件參照)**：
  - 使用者存取 `GET /api/invoice?id=1001`，攻擊者直接改為 `id=1002` 即可看到其他客戶的發票。
  - *防禦*：後端伺服器在執行查詢時，必須強制比對目前登入 Session 之 UserID 與目標資源之擁有者身分。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. 安全程式碼實戰：參數化查詢 vs 脆弱代碼
```python
# ❌ 極度脆弱的代碼 (易遭 SQL Injection)
cursor.execute(f"SELECT * FROM accounts WHERE username = '{user}' AND password = '{pwd}'")

# ✅ 官方推薦標準安全寫法 (Prepared Statements)
cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (user, pwd))
```

#### 2. 關鍵 HTTP 安全回應標頭 (Security Response Headers)
```http
# 防止 XSS 竊取 Session Cookie
Set-Cookie: session_id=xyz789; Secure; HttpOnly; SameSite=Strict

# 防止點擊劫持 (Clickjacking)
X-Frame-Options: DENY

# 防止瀏覽器 MIME 混淆嗅探
X-Content-Type-Options: nosniff

# 強制 HTTPS 安全傳輸
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| Web 漏洞類型 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **SQLi 防護** | 選項宣稱「在前端用 JavaScript 過濾單引號即能徹底防範 SQL 注入」 | **極度危險且無效！** 前端驗證可輕易被 Postman 或 Burp Suite 繞過，防護必須在**後端落實參數化查詢** |
| **XSS vs CSRF** | 題目混淆兩者原理：CSRF 是竊取 Cookie 嗎？ | **不是！CSRF 是借刀殺人**（利用受害者已登入瀏覽器冒發合法請求），攻擊者**無法直接看到 Cookie**；竊取 Cookie 是 XSS |
| **Cookie 安全標記** | 題目問防止跨站腳本偷取 Cookie 該下哪個 flag | **`HttpOnly`**（阻止 JS 存取）；`Secure` 是限 HTTPS 傳輸；`SameSite` 防 CSRF |

> 🔑 **防呆口訣**：
> - SQLi 剋星參數化，字串拼接必倒下。
> - XSS 輸出要編碼，Cookie 必加 HttpOnly。
> - CSRF 靠隨機 Token，IDOR 後端查權限！
        """,
        "caseStudy": "【實務案例分析】某銀行行動網銀之繳費功能，其後端 API 原先設計為 `POST /pay { bill_id: 12345 }`，伺服器僅確認連線者已登入，未比對該 bill_id 是否屬於該登入帳號。滲透測試人員利用 IDOR 漏洞，遞增帳單編號遍歷扣繳了數十位其他顧客之帳戶款項。資安架構師隨後重新設計權限驗證中介軟體 (Middleware)：由後端 Session 取得使用者的 `account_id`，並在 SQL 查詢強制加入條件 `WHERE bill_id = ? AND owner_account_id = ?`，徹底消除了水平越權漏洞。"
    },
    {
        "id": "B1-M06",
        "title": "單元 6：密碼學基礎、對稱/非對稱與數位簽章",
        "keywords": ["Symmetric Encryption", "Asymmetric Encryption", "AES-256", "RSA", "ECC", "Hashing", "Digital Signature", "PKI"],
        "summary": "掌握密碼學核心骨架：深入比較對稱式加密 (AES/ChaCha20) 與非對稱式加密 (RSA/ECC) 之數學特性、運算效能與金鑰分發；探討密碼學單向雜湊函數 (SHA-256/SHA-3)、HMAC 訊息驗證碼、數位簽章 (Digital Signature) 運作流程與 PKI 公開金鑰基礎架構之 X.509 憑證鏈。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 對稱式 vs 非對稱式加密全方位對照

| 比較維度 | 對稱式加密 (Symmetric) | 非對稱式加密 (Asymmetric) |
| :--- | :--- | :--- |
| **金鑰機制** | 加密與解密共用同一把秘密金鑰 (Secret Key) | 成對的金鑰：公鑰 (Public Key) 公開，私鑰 (Private Key) 專屬保密 |
| **代表演算法** | **AES (Rijndael)**, ChaCha20, 3DES (已淘汰) | **RSA**, **ECC (橢圓曲線密碼)**, Diffie-Hellman |
| **運算速度** | **極快** (支援硬體 AES-NI 指令加速)，適合巨量資料 | **極慢** (牽涉大質數分解或離散對數)，約慢 1000 倍 |
| **金鑰管理難題** | $n$ 個使用者互相通訊需 $\\frac{n(n-1)}{2}$ 把金鑰，分發極難 | $n$ 個使用者僅需 $2n$ 把金鑰 (每人一對公私鑰) |
| **核心用途** | 檔案加密、資料庫欄位加密、大量資料傳輸通道加密 | 數位簽章、身分鑑別、金鑰交換 (Key Exchange) |

#### 2. 雜湊函數 (Hash Function) 特性
- **三大不可或缺特性**：
  1. **單向性 (Pre-image Resistance)**：給定雜湊值 $H(M)$，在計算上不可逆推出原始明文 $M$。
  2. **弱抗碰撞性 (Second Pre-image Resistance)**：給定特定明文 $M_1$，計算上不可能找到相異之 $M_2$ 使得 $H(M_1) = H(M_2)$。
  3. **強抗碰撞性 (Collision Resistance)**：計算上不可能找到任何兩組相異明文 $M_1 \\neq M_2$ 使得 $H(M_1) = H(M_2)$。
  4. **雪崩效應 (Avalanche Effect)**：明文哪怕只更動 1 個 bit，產出的雜湊摘要值至少有 50% 以上之位元發生劇烈改變。
- 推薦標準：**SHA-256**, **SHA-512**, **SHA-3**；MD5 與 SHA-1 均已證實存在碰撞弱點，國際嚴格禁用。

#### 3. 數位簽章 (Digital Signature) 運作流程
- **簽署流程 (發送端 Alice)**：
  1. 對原始文件計算雜湊值：$Digest = Hash(Message)$。
  2. Alice 使用自己的「**Alice 私鑰 (Alice Private Key)**」對 Digest 加密，產出「數位簽章」。
  3. 將原始文件連同數位簽章傳送給 Bob。
- **驗證流程 (接收端 Bob)**：
  1. Bob 使用「**Alice 公鑰 (Alice Public Key)**」解密該數位簽章，還原出原始 Digest A。
  2. Bob 同步對收到的原始文件自行以相同演算法計算雜湊值，獲得 Digest B。
  3. 若 Digest A == Digest B，則確認無誤！
  - **達成三大安全目標**：**身分真實性 (Authenticity)**、**資料完整性 (Integrity)**、**不可否認性 (Non-Repudiation)**。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. OpenSSL 產生高強度密鑰與數位簽章
```bash
# 產生 ECC 橢圓曲線私鑰 (使用 prime256v1 曲線)
openssl ecparam -name prime256v1 -genkey -noout -out private_key.pem
# 萃取對應之公開金鑰
openssl ec -in private_key.pem -pubout -out public_key.pem

# 使用私鑰對合約檔案進行 SHA-256 數位簽章
openssl dgst -sha256 -sign private_key.pem -out contract.sig contract.pdf

# 驗證數位簽章是否有效
openssl dgst -sha256 -verify public_key.pem -signature contract.sig contract.pdf
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 密碼學觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **金鑰使用角色** | 題目問「欲傳送機密訊息給 Bob，Alice 應使用何種金鑰加密？」考生常錯選 Alice 私鑰 | **正解：使用 Bob 的公鑰加密**。因為只有 Bob 自己的私鑰才能解開，方能保障機密性 |
| **數位簽章金鑰** | 題目問「Alice 對合約簽章，應使用哪一把金鑰？」 | **正解：使用 Alice 的私鑰加密雜湊**。因為私鑰具唯一專屬性，其他人用 Alice 公鑰解開即可證明確為 Alice 所簽 |
| **對稱金鑰長度** | 題目比較 AES-128、AES-256 與 RSA-2048 之安全強度 | **AES-128 與 RSA-2048 具備相近之安全強度 (約112~128 bits 安全等級)**；AES-256 具備抗量子前瞻安全性 |

> 🔑 **防呆口訣**：
> - 寄信保密：用「對方公鑰」加密，對方私鑰才能解！
> - 簽名作保：用「自己私鑰」簽署，全世界公鑰來驗！
> - 雜湊單向不可逆，雪崩效應防碰撞！
        """,
        "caseStudy": "【實務案例分析】某跨國外商簽署電子採購訂單，供應商事後因原物料大漲企圖毀約，宣稱該訂單從未經其執行長簽署。法庭委託數位鑑識專家進行審查：專家調閱由公證 CA 機構簽發之執行長 X.509 憑證，並利用供應商公鑰成功解密訂單之 SHA-256 數位簽章，其雜湊比對百分之百相符，且時間戳記伺服器 (TSA) 證明簽署當時該憑證完全有效未被撤銷 (CRL/OCSP 驗證通過)。法官據此認定該電子簽章具備完全之法律「不可否認性」，判決供應商敗訴履約。"
    },
    {
        "id": "B1-M07",
        "title": "單元 7：存取控制模型與使用者認證技術",
        "keywords": ["DAC", "MAC", "RBAC", "ABAC", "MFA", "FIDO2", "OAuth 2.0", "SAML 2.0"],
        "summary": "全面解析傳統與現代存取控制模型：自主存取控制 (DAC)、強制存取控制 (MAC/Bell-LaPadula)、基於角色 (RBAC) 與基於屬性 (ABAC) 存取控制。深入探討現代多因素驗證 (MFA) 三大要素、抗釣魚 FIDO2/WebAuthn 標準以及聯邦身分認證 (OAuth 2.0, OpenID Connect, SAML 2.0)。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 四大存取控制模型核心對照

| 模型名稱 | 控制機制與決策依據 | 權限授權者 | 適用情境與特性 |
| :--- | :--- | :--- | :--- |
| **DAC (自主存取控制)** | 基於主體身分與檔案權限清單 (ACL) | **資源擁有者 (Owner)** 可自行決定將讀寫權限授予他人 | 彈性最高、集中管理最難。一般個人電腦 Windows NTFS / Linux 傳統權限 |
| **MAC (強制存取控制)** | 基於安全標籤 (Security Labels) 與敏感度等級 (機密、極機密) | **系統中央安全策略**，使用者無權私自變更或轉交 | 安全等級最高。軍方、國防 (Bell-LaPadula 模型、SELinux) |
| **RBAC (基於角色的存取控制)** | 基於組織中的業務職位指派「角色」，權限綁定角色 | **系統管理員** | 企業最廣泛採用。權限異動僅需調整使用者之角色歸屬 |
| **ABAC (基於屬性的存取控制)** | 動態評估主體屬性、資源屬性與**環境情境屬性 (時間、IP、設備)** | **動態策略規則引擎 (Policy Engine)** | 零信任 (Zero Trust) 核心。可設定「非上班時間禁止下載」等細粒度條件 |

#### 2. 多因素驗證 (Multi-Factor Authentication, MFA)
- **三大獨立驗證維度（必須至少包含兩項不同類別，方稱 MFA）**：
  1. **所知 (Something you know)**：密碼、PIN碼、圖形鎖。
  2. **所持 (Something you have)**：硬體安全金鑰 (FIDO2/YubiKey)、手機 OTP Authenticator App、智慧IC卡。
  3. **所具 (Something you are)**：指紋、虹膜、臉部辨識、靜脈特徵。
- **防呆注意**：「密碼 + 提問母親生日」屬於同一類別 (所知 + 所知)，**不是 MFA**！
- **NIST SP 800-63 建議**：SMS 簡訊與語音 OTP 易受 SIM 換卡 (SIM Swapping) 與 SS7 攔截攻擊，建議逐步淘汰，全面遷移至抗釣魚的 FIDO2 / Passkeys。

#### 3. 現代聯邦身分驗證標準
- **OAuth 2.0**：**授權框架 (Authorization)**，以 Access Token 授予第三方應用有限存取權（如授權 APP 存取 Google 雲端相簿，而不提供 Google 帳密）。
- **OpenID Connect (OIDC)**：建立在 OAuth 2.0 之上的**身分認證層 (Authentication)**，回傳 ID Token (JWT 格式)。
- **SAML 2.0**：基於 XML 的單一登入 (SSO) 標準，廣泛應用於大型企業與政府內部網域跨系統身分聯合。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux SELinux (MAC 強制存取控制) 狀態管理
```bash
# 查詢當前 SELinux 運作模式 (Enforcing, Permissive, Disabled)
getenforce
# 檢視檔案的安全上下文 (Security Context)
ls -Z /var/www/html/index.html
# 修正標籤還原預設 HTTP 存取策略
restorecon -Rv /var/www/html
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 認證與授權機制 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **雙密碼是否為 MFA** | 選項宣稱「輸入登入密碼後，再輸入提款卡提款密碼即符合 MFA」 | **錯誤！兩者皆為「所知 (Something you know)」**，必須跨越不同維度 (如密碼 + 實體卡片) |
| **OAuth 2.0 本質** | 題目問「OAuth 2.0 協定的核心功能為何？」考生常誤選使用者身分認證 | **授權 (Authorization)**。OIDC 才是專職身分認證 (Authentication) |
| **Bell-LaPadula 模型** | 題目考 BLP 模型的兩大規則 | **No Read Up (NRU 不得上讀高密級), No Write Down (NWD 不得下寫低密級)**，專注維護機密性 |

> 🔑 **防呆口訣**：
> - 存取控制四兄弟：DAC 自己作主，MAC 中央規定，RBAC 職位角色，ABAC 情境多變。
> - MFA 必跨雙向：所知、所持、所具，缺一不可混為一談！
        """,
        "caseStudy": "【實務案例分析】某跨國金融顧問公司高階主管在星巴克使用公共 Wi-Fi 辦公時，遭遇連線中間人釣魚網站。該網站精確仿冒了公司登入介面，誘騙主管輸入了帳號與密碼。然而，該機構全面推行了基於 FIDO2 WebAuthn 規範的實體硬體金鑰 (YubiKey)。由於 FIDO2 協定在瀏覽器層級將驗證憑證與當前存取的真實網域名稱強行綁定 (Origin Binding)，釣魚網域無法解鎖硬體金鑰回應，攻擊者取得的帳密瞬間失效，成功挫敗了進階憑證竊取攻擊。"
    },
    {
        "id": "B1-M08",
        "title": "單元 8：台灣資通安全管理法與個資保護概論",
        "keywords": ["Cybersecurity Management Act", "PDPA", "Incident Notification", "Critical Infrastructure", "Data Breach"],
        "summary": "精準掌握我國《資通安全管理法》與《個人資料保護法》法規命令核心架構：主管機關權責、適用主體（公務機關與特定非公務機關）、責任等級劃分 (A~E 級)、資安事件 1 小時通報法定期限與 36 小時復原規範，以及個資法蒐集處理利用要件與外洩通知義務。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 我國《資通安全管理法》核心架構
- **主管機關**：數位發展部 (資通安全署)。
- **適用主體**：
  1. **公務機關**：中央與地方各級行政、立法、司法機關與公立學校/公營事業。
  2. **特定非公務機關**：
     - **關鍵基礎設施提供者 (Critical Infrastructure, CI)**：能源、水資源、通訊傳播、交通、銀行與金融、緊急救援、高科技園區、醫療等八大領域。
     - 公營事業、政府捐助之財團法人。
- **資安責任等級劃分 (A 級至 E 級)**：
  - **A 級 (最高)**：全國性機敏公務機關、八大 CI 關鍵提供者。要求：全機關導入 ISMS 並通過第三方驗證、自建或委外 SOC、每年辦理紅隊演練、專責資安主管與至少 4 名以上資安專職人員。
  - **B 級**：直轄市級公務機關。至少配置 2 名資安專職人員。
  - **C 級**：縣市公務機關。至少配置 1 名資安專職人員。
- **資安事件通報與應變時限 (必考黃金數字！)**：
  - 知悉資安事件後，**1 小時內** 必須於主管機關指定平台完成通報！
  - 第三級與第四級重大事件，必須在 **36 小時內** 完成損害控制與系統復原作業，並於一個月內提出調查改善報告。

#### 2. 我國《個人資料保護法》要點
- **個資定義**：自然人之姓名、出生年月日、身分證統一編號、護照號碼、特徵、指紋、婚姻、家庭、教育、職業、病歷、醫療、基因、性生活、健康檢查、犯罪前科、聯絡方式、財務情況等。
- **特種個人資料 (原則禁止蒐集，需符合嚴格法定事由)**：病歷、醫療、基因、性生活、健康檢查、犯罪前科。
- **當事人五大權利**：查詢或請求閱覽、請求製給複製本、請求補充或更正、請求停止蒐集/處理/利用、**請求刪除**。
- **個資外洩通知**：非公務機關發生個資被竊取、洩漏、竄改或其他侵害事故時，應查明後以適當方式「即時通知」當事人與中央目的事業主管機關。

### 二、實務技術落地與通報流程 (Incident Workflow)

```text
【資安事件法定應變流程】
[異常事件發生] 
      ↓
[技術判定確認為資安事件] 
      ↓ ⏱️ 必須在知悉後 1 小時內！
[通報至數位發展部資安通報平台 (EAP)] 
      ↓
[評定事件等級 (一級~四級)] 
      ↓ ⏱️ 三/四級重大事件需於 36 小時內完成！
[遏止控制、清除惡意程式、離線備份還原] 
      ↓
[結案確認與檢討改善報告送審]
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 法規項目 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **通報時限** | 選項出現 24 小時、72 小時、半天等時限混淆 | **資安法通報一律為「知悉後 1 小時內」完成通報**；72 小時為歐盟 GDPR 外洩通報時限，不可混淆 |
| **特種個資範疇** | 題目問哪一項不屬於特種個資：病歷、基因、犯罪前科、財務收入 | **財務收入是一般個資**；特種個資僅限：病歷、醫療、基因、性生活、健康檢查、犯罪前科六大項 |
| **關鍵基礎設施領域** | 題目問八大關鍵基礎設施領域有哪些 | 能源、水資源、通訊傳播、交通、銀行與金融、緊急救援、高科技園區、醫療 (無娛樂、一般零售) |

> 🔑 **防呆口訣**：
> - 資安通報 1 小時，三四重大 36 復！
> - 特種個資病醫基，性檢前科不可欺！
> - 八大關鍵護國家，水電交通油氣銀！
        """,
        "caseStudy": "【實務案例分析】某區域自來水公司監控系統 (SCADA) 遭勒索軟體感染，部分加壓站數值無法回傳。水廠資訊主管於上午 09:30 證實該異狀係駭客入侵造成（知悉事件）。主管立即於 10:15 (45 分鐘內) 透過數位發展部國家資通安全通報平台完成通報，並啟動緊急隔離措施。由於該水廠屬於我國「水資源關鍵基礎設施」，評定為第三級資安事件。應變團隊利用備份映像與手動水閥控制，於 22 小時內完成控制網段淨化與系統復原，符合法規知悉 1 小時通報與 36 小時復原要求。"
    }
]

BASIC_SUBJECT_2_MODULES = [
    {
        "id": "B2-M01",
        "title": "單元 1：防火牆、IDS/IPS 與次世代網路防護",
        "keywords": ["NGFW", "IDS", "IPS", "Stateful Inspection", "Packet Filtering", "WAF", "Deep Packet Inspection"],
        "summary": "掌握網路邊界縱深防禦實務：解析封包過濾防火牆、狀態檢驗防火牆 (Stateful Inspection)、次世代防火牆 (NGFW App-ID/User-ID)、入侵偵測系統 (IDS) 旁路部署與入侵防禦系統 (IPS) 串聯阻斷、以及 WAF 應用層防護差異。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 防火牆演進與檢驗技術世代

| 防火牆世代 | 運作 OSI 層次 | 檢驗核心機制 | 優缺點與防護盲點 |
| :--- | :--- | :--- | :--- |
| **傳統封包過濾 (Packet Filtering)** | 第 3/4 層 (網路/傳輸層) | 比對來源/目的 IP、Port 與 TCP Flags，無狀態紀錄 | 速度最快，但無狀態追蹤，無法防範偽造連線與高層攻擊 |
| **狀態檢驗 (Stateful Inspection)** | 第 3/4/5 層 | 維護狀態表 (State Table)，動態追蹤 TCP 三向交握連線階段 | 僅允許合法發起之回程封包，有效阻斷異常外部注入 |
| **次世代防火牆 (NGFW)** | 第 7 層 (應用層) | **深度封包檢驗 (DPI)**、**App-ID** 應用識別、**User-ID** 身分關聯 | 能辨識非標準 Port 運作之應用 (如偽裝成 443 的木馬)，可解密 SSL 檢驗 |

#### 2. IDS (入侵偵測) vs IPS (入侵防禦) 關鍵架構差異
- **IDS (Intrusion Detection System)**：
  - *部署模式*：**旁路監聽 (Out-of-band)**，透過交換器之 Port Mirroring (SPAN) 或 Network TAP 複製封包進行分析。
  - *作動機制*：被動分析。發現惡意特徵時發送警報 (Alert) 或向防火牆發送 TCP RST 封包，但**無法保證在第一時間即時丟棄 (Drop) 攻擊封包**。
  - *優點*：零延遲、故障時完全不影響現有生產網路連線 (Fail-open)。
- **IPS (Intrusion Prevention System)**：
  - *部署模式*：**線上串聯 (Inline)**，所有流量實體或邏輯穿透 IPS 設備。
  - *作動機制*：即時主動阻斷。一旦特徵或異常行為吻合，**直接在線丟棄惡意封包 (Drop Packet)** 並中斷連線。
  - *缺點*：若設備故障可能導致網路全斷 (需具備 Bypass 旁路保護機制)，且深檢可能增加網路延遲。

#### 3. WAF (網站應用程式防火牆) 專屬定位
- 傳統防火牆與 IPS 專注於 L3/L4 網路層威脅；WAF 專注於 **OSI 第 7 層 HTTP/HTTPS 酬載**。
- 專門解析 HTTP Request 中的 URI、Cookie、POST Body、Headers，專精防禦 SQL Injection、XSS、路徑遍歷與 CSRF。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux iptables 狀態檢驗防火牆規則範例
```bash
# 預設原則全部丟棄
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 允許本機回環連線
iptables -A INPUT -i lo -j ACCEPT

# 狀態檢驗核心：放行已建立 (ESTABLISHED) 與相關聯 (RELATED) 之回程連線
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 僅對特定內網網段開放 SSH Port 22
iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 22 -m conntrack --ctstate NEW -j ACCEPT
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 設備類型 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **IDS 能否即時阻斷** | 選項宣稱「IDS 可以即時在第一封包阻斷惡意攻擊」 | **錯誤！IDS 採旁路監聽只能報警**，只有串聯部署的 **IPS** 才能即時丟棄封包阻斷連線 |
| **NGFW vs WAF** | 考題問防範 Web 伺服器 SQL 注入最佳專屬設備 | **首選 WAF (網站應用程式防火牆)**，因其對 HTTP 協定與 Web Payload 具最深度之解碼防護能力 |
| **IPS 誤報 (False Positive)** | 題目問 IPS 誤報率過高會造成什麼後果 | **將合法業務流量誤判阻斷，導致正常服務不可用 (業務中斷)** |

> 🔑 **防呆口訣**：
> - IDS 旁路聽，報警不能擋；IPS 串線上，當場丟封包！
> - 傳統看 Port 號，次代深檢到第七；Web 專武找 WAF，防杜 SQL 與 XSS！
        """,
        "caseStudy": "【實務案例分析】某線上商城在週年慶促銷期間，前端 Web 伺服器遭受分散式 Slowloris 緩慢 HTTP 拒絕服務攻擊與大量偽裝成合法購物請求的 SQL 注入。企業架構師實施聯防策略：在最外層部署次世代防火牆 (NGFW) 阻絕 L3/L4 之異常連線速率；在 Web 伺服器前緣串聯部屬 WAF，啟用 OWASP Core Rule Set (CRS)，精準過濾夾帶單引號與聯集查詢之惡意 HTTP POST 參數。攻擊流量在毫秒級內被 WAF 攔截並回傳 403 Forbidden，後端資料庫完全未受干擾，保障了數億元促銷交易安全進行。"
    },
    {
        "id": "B2-M02",
        "title": "單元 2：端點防護、次世代防毒與 EDR 實務",
        "keywords": ["EDR", "NGAV", "Telemetry", "LOLBins", "Application Whitelisting", "USB Control"],
        "summary": "掌握端點安全防禦演進：傳統特徵碼防毒 (AV) 到行為分析 (NGAV) 與端點偵測回應 (EDR)；探討端點遙測資料收集、親代子進程樹 (Process Tree)、生活離地二進位檔 (LOLBins) 濫用、Windows AppLocker 白名單與周邊儲存設備管制。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 端點防護演進世代對照

| 防護維度 | 傳統防毒軟體 (Legacy AV) | 次世代防毒 (NGAV) | 端點偵測與回應 (EDR) |
| :--- | :--- | :--- | :--- |
| **偵測機制** | **靜態特徵碼比對 (Signatures)** | 啟發式 (Heuristics) + 本地/雲端機器學習行為模型 | **持續端點遙測 (Telemetry)** + 行為異常分析 + 威脅獵捕 |
| **核心防護焦點** | 已知已知 (Known-Knowns) 檔案型病毒 | 已知惡意行為、記憶體注入探測 | **未知威脅、無檔案攻擊 (Fileless)、進階持續威脅 (APT)** |
| **回應能力** | 自動刪除或隔離受感染檔案 | 阻斷惡意進程執行 | **遠端網路隔離端點、遠端終止進程、現場鑑識採證、獵捕軌跡** |

#### 2. 無檔案惡意程式 (Fileless Malware) 與 LOLBins 濫用
- **無檔案攻擊原理**：攻擊者不將實體 EXE 惡意檔案寫入受害者硬碟，而是直接將惡意 Payload 注入至合法記憶體進程（如 `explorer.exe`, `lsass.exe`），或直接利用系統內建工具執行腳本。
- **LOLBins (Living off the Land Binaries)**：
  - 攻擊者濫用作業系統合法的微軟已簽名工具進行攻擊：例如利用 `powershell.exe` 下載載具、利用 `certutil.exe -urlcache -split -f` 下載木馬、利用 `mshta.exe` 執行遠端腳本。
  - 傳統防毒因檔案具有合法微軟數位簽名而直接放行，唯有 EDR 分析「進程親緣樹異常（例如 `WINWORD.EXE` 衍生啟動 `powershell.exe`）」才能即時示警。

#### 3. 應用程式白名單 (Application Whitelisting)
- 遵循零信任與預設拒絕 (Default Deny) 理念：**除了明確列入白名單的信任程式外，其餘所有程式一律禁止執行**。
- 代表技術：Windows Defender Application Control (WDAC), AppLocker。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. PowerShell 檢視異常進程樹與出連
```powershell
# 檢視目前所有由 Office 軟體 (Word/Excel) 派生之子進程 (典型釣魚特徵)
Get-CimInstance Win32_Process | Where-Object {
    $_.ParentProcessId -in (Get-Process winword, excel -ErrorAction SilentlyContinue).Id
} | Select-Object ProcessId, Name, CommandLine

# 查詢特定 PID 之外部網路連線
Get-NetTCPConnection -OwningProcess 4088 | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

#### 2. 群組原則 (GPO) 停用抽取式磁碟存取 (USB 管制)
```text
電腦設定 -> 系統管理範本 -> 系統 -> 抽取式存放裝置存取權：
啟用【所有抽取式存放裝置類別：拒絕所有存取權】(Deny all access)
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 端點防護觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **EDR 核心價值** | 題目問「EDR 與傳統防毒最大差異為何？」 | **提供持續的端點行為遙測、可視性、調查鑑識與即時網路隔離能力**，而不僅依賴靜態特徵碼 |
| **無檔案攻擊應對** | 選項宣稱「定時執行硬體磁碟掃毒可徹底清除無檔案病毒」 | **錯誤！無檔案惡意程式常駐於 RAM 記憶體與登錄檔中**，必須透過記憶體鑑識與 EDR 行為監控處置 |
| **白名單 vs 黑名單** | 題目問何種策略對未知零日漏洞 (Zero-day) 抵抗力最高 | **應用程式白名單 (Default Deny)**。黑名單只能阻擋已知威脅 |

> 🔑 **防呆口訣**：
> - 傳統特徵比名片，次代 EDR 盯動線。
> - Word 開 PowerShell 大可疑，LOLBins 濫用無所匿。
> - 白名單預設全不准，端點隔離秒阻斷！
        """,
        "caseStudy": "【實務案例分析】某跨國製造廠一名工程師開啟一封假冒發票的電子郵件，信中附件巨集在背景神不知鬼不覺地調用 `certutil.exe` 下載加密酬載並注入至記憶體中。傳統防毒因檔案不落地完全未跳出任何警告。然而，端點 EDR 立即捕捉到遙測異常：Office 進程派生非標準子進程，且向未受信任的境外伺服器發起 TLS 握手。EDR 在 0.8 秒內自動終止可疑進程樹，並觸發「網路隔離」，使該工作站與內網其他電腦完全隔絕，成功在勒索軟體橫向擴散前掐滅危機。"
    },
    {
        "id": "B2-M03",
        "title": "單元 3：網路流量監控、封包分析與異常連線診斷",
        "keywords": ["Wireshark", "Packet Analysis", "NetFlow", "Beaconing Detection", "ARP Spoofing", "DNS Tunneling"],
        "summary": "掌握 Wireshark 抓包過濾語法、網路流量 NetFlow/IPFIX 收集、TCP 三向交握異常排查、ARP 欺騙偵測、惡意程式心跳回連 (Beaconing) 流量診斷與 DNS 穿隧 (DNS Tunneling) 外洩萃取分析。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 深度封包檢測 (PCAP) vs 網路流 (NetFlow/IPFIX)
- **完整封包擷取 (Full Packet Capture, PCAP)**：
  - *特性*：儲存完整封包標頭與有效酬載 (Payload)。
  - *用途*：微觀鑑識、惡意代碼逆向、還原傳輸檔案。缺點為儲存空間消耗極為巨大。
- **網路流 (NetFlow / IPFIX / sFlow)**：
  - *特性*：**僅記錄連線元數據 (Metadata)**：來源/目的 IP、來源/目的 Port、通訊協定、封包數量、傳輸位元組、時間戳記與 TCP Flags。
  - *用途*：巨觀流量趨勢、異常大流量外傳偵測、DDoS 監控、網路拓撲效能分析。

#### 2. 常見網路異常流量特徵模式
1. **ARP 欺騙 (ARP Spoofing / Poisoning)**：
   - *特徵*：同一個 IP 位址（如預設閘道 Gateway）在短時間內出現不同的 MAC 位址變更，或頻繁收到非請求的廣播 ARP 回應 (Gratuitous ARP Reply)。
2. **C2 惡意連線心跳 (Beaconing)**：
   - *特徵*：內部受害端點每隔固定間隔時間（如精確每 60 秒）或固定時間加上些微抖動 (Jitter)，向外部未知 IP 發起細小的 HTTP POST / DNS 請求。
3. **DNS 穿隧 (DNS Tunneling)**：
   - *特徵*：大量畸長且看似隨機編碼的子網域查詢（如 `a8f9c1b2.data.attacker.com`），TXT 紀錄回應異常龐大，利用 DNS Port 53 穿透企業防火牆外洩機密。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Wireshark 官方考試必備 Display Filters 過濾語法
```text
# 1. 尋找 TCP 三向交握的初始 SYN 封包 (連線發起)
tcp.flags.syn == 1 && tcp.flags.ack == 0

# 2. 尋找被阻斷或異常重設之連線 (RST 封包)
tcp.flags.reset == 1

# 3. 搜尋特定 IP 且排除 DNS 廣播流量
ip.addr == 192.168.1.50 && !dns

# 4. 偵測 HTTP POST 請求 (常見於登入與資料外傳)
http.request.method == "POST"

# 5. 檢視包含特定字串的 DNS 請求
dns.qry.name contains "malicious"
```

#### 2. Linux tcpdump 現場快速抓包指令
```bash
# 抓取介面 eth0 上目的地為 Port 80/443 的前 100 個封包並寫入檔案
tcpdump -i eth0 -nn "tcp port 80 or tcp port 443" -c 100 -w /tmp/traffic.pcap
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 流量異常類型 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **SYN Flood 封包特徵** | 選項出現「巨量 ACK 且無 SYN」 | **錯誤！SYN Flood 特徵是巨量 SYN 且無後續 ACK**，導致伺服器半開隊列爆滿 |
| **DNS 穿隧辨識** | 題目問為何防火牆沒擋下資料外洩？ | 因為防火牆放行內部對外之 **UDP 53 (DNS 查詢)**，攻擊者將資料 Base64 編碼藏在子網域中外傳 |
| **ARP 欺騙根因** | 考題問 ARP 協定最大安全缺陷為何？ | **無認證機制 (Stateless)**，節點無條件信任收到的 ARP Reply 並更新本機 ARP 快取表 |

> 🔑 **防呆口訣**：
> - 封包分析 Wireshark，SYN==1 握手來。
> - 定時外傳是心跳，長子網域名是穿隧。
> - IP 同一 MAC 變，定是 ARP 鬼搗亂！
        """,
        "caseStudy": "【實務案例分析】SOC 監控團隊透過 NetFlow 分析發現，研發部門一台非伺服器工作站，連續三天在每日凌晨 03:00 整準時向烏克蘭境內一處 IP 發起約 8GB 的 UDP 連線。分析師立即調閱端點 PCAP 封包進行深度檢測，發現攻擊者利用了 DNS 穿隧工具將企業晶片設計圖拆解壓縮編碼外傳。資安團隊在核心交換器與邊界防火牆立即封鎖該 C2 網域與境外 IP，並透過 EDR 溯源清除端點木馬，成功攔截了智慧財產權外流。"
    },
    {
        "id": "B2-M04",
        "title": "單元 4：弱點掃描、漏洞評估與修補排程實務",
        "keywords": ["Vulnerability Assessment", "Nessus", "CVE", "CVSS v3.1", "CISA KEV", "Patch Management"],
        "summary": "掌握企業弱點掃描 (VA) 實作流程：深入比較認證掃描 (Credentialed) 與無認證掃描 (Non-credentialed)、CVE 識別體系、CVSS v3.1 評分度量維度、CISA 已知利用漏洞清單 (KEV) 與排程修補優先級制定實務。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 弱點掃描模式深度對比

| 掃描方式 | 運作原理與權限 | 偵測深度與優點 | 限制與缺點 |
| :--- | :--- | :--- | :--- |
| **無認證掃描 (Unauthenticated Scan)** | 從外部網路對標的主機進行 Port 掃描與服務指紋識別 | 模擬外部黑客視角，無須主機密碼，適合評估邊界暴露面 | 僅能探測公開服務表面，無法深入底層系統組態，誤報率較高 |
| **認證掃描 (Credentialed Scan)** | 提供合法特權帳號 (SSH / Windows WMI) 供掃描器登入 | **深入作業系統內部**，檢視已安裝套件、註冊表設定、補丁缺失，**精確度極高** | 需管理與授權帳號憑證，對受測主機產生微量運算負載 |

#### 2. CVSS v3.1 評分系統與嚴重度劃分
- **三大評分度量衡**：
  1. **基本度量 (Base Metrics)**：漏洞本身固有的恆定特性（攻擊向量 AV、複雜度 AC、權限需求 PR、使用者互動 UI、範圍 S、機密性/完整性/可用性衝擊 C/I/A）。
  2. **時間度量 (Temporal Metrics)**：隨時間演變的特性（漏洞利用成熟度 E、修補層級 RL、確認度 RC）。
  3. **環境度量 (Environmental Metrics)**：特定組織內部之特殊環境與補償控制。
- **基本分級標準 (必背！)**：
  - **Critical (緊急)**：**9.0 ~ 10.0** (通常具備遠端無授權代碼執行 RCE 特性)。
  - **High (高)**：**7.0 ~ 8.9**。
  - **Medium (中)**：**4.0 ~ 6.9**。
  - **Low (低)**：**0.1 ~ 3.9**。
  - **None**：**0.0**。

#### 3. 修補優先級決定矩陣 (Vulnerability Prioritization)
- 切勿盲目僅依 CVSS 基本分數排程！應結合 **威脅情資 (Threat Intelligence)**：
  - 檢視 **CISA KEV (Known Exploited Vulnerabilities Catalog)**：若該漏洞已被黑客武器化並在野積極利用，即使 CVSS 僅為 7.5，修補優先級亦應提升至最高！

### 二、實務技術落地與排程規範 (Patching Policy)

```text
【企業漏洞修補標準 SLA 範本】
- Critical (CVSS 9.0~10.0 或已在野利用)：接獲通報後 24~48 小時內完成測試與上線。
- High (CVSS 7.0~8.9)：7 天至 14 天內完成修補。
- Medium (CVSS 4.0~6.9)：30 天至 60 天內隨定期維護視窗更新。
- Low (CVSS 0.1~3.9)：下一季定期維護或併同年度作業系統大版本升級。
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 弱點評估觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **弱掃 vs 滲透測試** | 題目混淆弱點掃描 (VA) 與滲透測試 (PT) | **弱掃是廣度自動化工具盤點漏洞**；**滲透測試是由人工模擬駭客思維進行深度概念驗證 (PoC) 與複合式弱點串連利用** |
| **認證掃描之優勢** | 選項宣稱「無認證掃描比認證掃描更精確」 | **完全相反！** 認證掃描能登入主機比對套件版號與註冊表，精確度遠高於無認證掃描 |
| **CVSS 嚴重性切分** | 題目問 CVSS 8.5 屬於哪一等級 | **High (高)**。9.0 以上才是 Critical (緊急) |

> 🔑 **防呆口訣**：
> - 弱掃自動盤漏洞，滲透人工串攻擊。
> - 認證掃描登入看，註冊表裡見真章。
> - 9 分以上叫緊急，在野利用搶先補！
        """,
        "caseStudy": "【實務案例分析】某大型金控進行每季全資產弱點掃描，產出報告高達 1,200 個漏洞。資訊長原要求團隊按順序修補，導致 IT 人員疲於奔命。資安長介入建立動態優先權架構：首先交叉比對 CISA KEV 與火線情資，鎖定其中 8 個已有公開武器化 Exploit 且對外公開之 Apache/OpenSSL 漏洞 (CVSS >= 9.0)，要求 48 小時內全員動員修補；其餘內部網段之中低風險漏洞排入例行月維護。成功以最少人力精準封堵最致命之破口。"
    },
    {
        "id": "B2-M05",
        "title": "單元 5：日誌收集、集中分析與基礎稽核維運",
        "keywords": ["Syslog", "Windows Event Log", "NTP Synchronization", "WORM Storage", "Log Retention", "Audit Trails"],
        "summary": "掌握資安稽核日誌 (Audit Logs) 黃金管理準則：Syslog 協定、Windows Security Event ID 關鍵事件解碼、全網 NTP 毫秒校時、單寫多讀 (WORM) 唯讀不可篡改、我國資安法法定 180 天留存與中央集中管理機制。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 日誌管理四大支柱規範
1. **即時集中轉發 (Centralized Collection)**：
   - 伺服器與網路設備本地日誌易在主機遭駭時被攻擊者抹除。必須透過 Syslog (RFC 5424) 或 Windows Event Forwarding (WEF) 即時將日誌轉發至獨立隔離的專屬日誌伺服器或 SIEM。
2. **全網時間同步 (NTP Synchronization)**：
   - 所有伺服器、防火牆、交換器與資料庫，必須強制與內部權威 NTP 時間伺服器同步。時間戳記若不一致，鑑識調查時將無法重構事件時序鏈。
3. **資料不可竄改性 (WORM & Hash Integrity)**：
   - 採用「單寫多讀 (Write Once, Read Many)」存儲媒體或具備加密簽章之雲端物件鎖 (Object Lock)。日誌寫入後，即便是網域最高管理員 (Domain Admin) 亦無權修改或刪除。
4. **法規留存期限 (Log Retention)**：
   - 我國《資通安全管理法》明文規定：關鍵資訊系統之**日誌紀錄至少必須完整保存 180 天 (半年) 以上**；金融相關法規更要求核心日誌保存 1 年至 5 年。

#### 2. Windows 必考重要安全事件識別碼 (Security Event IDs)

| Event ID | 事件名稱與意義 | 鑑識與分析核心重點 |
| :--- | :--- | :--- |
| **`4624`** | 帳戶成功登入 (An account was successfully logged on) | 檢查 **Logon Type**：<br>• Type 2：互動式本機鍵盤登入<br>• Type 3：網路連線登入 (如 SMB/共享)<br>• Type 10：遠端桌面 (RDP) 登入 |
| **`4625`** | 帳戶登入失敗 (An account failed to log on) | **暴力破解 (Brute-force) 或密碼噴灑 (Password Spraying)** 核心特徵，短時間大量出現即為警報 |
| **`4720`** | 建立新使用者帳號 (A user account was created) | 攻擊者取得權限後建立後門帳號之行為 |
| **`1102`** | 安全稽核日誌遭手動清除 (The audit log was cleared) | **極度危險指標！** 攻擊者執行 `wevtutil cl security` 企圖湮滅證據 |

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. PowerShell 快速查詢異常登入失敗與日誌清除
```powershell
# 查詢過去 24 小時內所有登入失敗 (4625) 的來源 IP 與目標帳號
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddDays(-1)} | 
    ForEach-Object {
        $xml = [xml]$_.ToXml()
        [PSCustomObject]@{
            Time = $_.TimeCreated
            User = $xml.Event.EventData.Data | Where-Object {$_.Name -eq "TargetUserName"} | Select-Object -ExpandProperty '#text'
            IP   = $xml.Event.EventData.Data | Where-Object {$_.Name -eq "IpAddress"} | Select-Object -ExpandProperty '#text'
        }
    } | Format-Table -AutoSize

# 檢測安全日誌是否被惡意清空 (Event ID 1102)
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102} -ErrorAction SilentlyContinue
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 日誌維運觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **法定保存期限** | 題目問資通安全管理法要求系統軌跡紀錄至少保存幾天？ | **至少 180 天 (約半年)**。常以 30 天、90 天作為干擾誘答項 |
| **NTP 時間誤差** | 題目問為何不同設備日誌無法進行事件關聯分析 | **未落實 NTP 時間校時**，導致各設備時間偏差數分鐘甚至數小時，時序被打亂 |
| **4624 登入類型** | 題目問遠端桌面 (RDP) 登入在 Event ID 4624 中標示為哪種類型？ | **Logon Type 10 (RemoteInteractive)**；Type 2 為本地 Console；Type 3 為網路連線 |

> 🔑 **防呆口訣**：
> - 4624 成功進，4625 失敗停。
> - 4720 偷建號，1102 抹日誌（最危險！）。
> - 集中轉發防毀證，NTP 校時保一致，法規保存 180！
        """,
        "caseStudy": "【實務案例分析】某政府機關半夜遭 APT 攻擊者滲透，攻擊者提權至本機 Administrator 後，立即在命令提示字元執行 `wevtutil cl Security` 指令清除所有本機安全日誌，企圖令鑑識小組無跡可尋。所幸該機關遵照規範落實了「集中日誌轉發」：本地日誌在生成的幾毫秒內已透過 Syslog TLS 即時轉發至獨立的 SIEM 儲存庫。本地記錄雖被清空，但在 SIEM 端立即觸發了「Event ID 1102 日誌清除警報」與完整的攻擊溯源軌跡，值班資安人員在 5 分鐘內完成受害主機隔離。"
    },
    {
        "id": "B2-M06",
        "title": "單元 6：資料備份、還原演練與 3-2-1 原則實務",
        "keywords": ["3-2-1 Backup Rule", "Immutable Backup", "RTO", "RPO", "Full Backup", "Incremental Backup", "Differential Backup"],
        "summary": "徹底落實資料備份與災難復原架構：經典 3-2-1 鐵律與現代 3-2-1-1-0 擴充規範、完整備份 (Full)、增量備份 (Incremental) 與差異備份 (Differential) 差異對決、不可竄改快照 (WORM/Air-gap) 與定期實體還原演練驗證。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 經典 3-2-1 備份鐵律與現代擴充
- **經典 3-2-1 原則**：
  - **3 份資料複本**：1 份原始生產資料 + 2 份獨立備份複本。
  - **2 種不同存儲媒介**：避免單一媒介共通硬體瑕疵（如磁碟陣列 SAN + 磁帶 LTO 或雲端儲存）。
  - **1 份異地保存 (Off-site)**：遠離本地災區（防範火災、水災、地震）。
- **現代 3-2-1-1-0 擴充規範 (專門對抗勒索軟體)**：
  - 額外增加 **1 份離線 (Offline) 或不可變 (Immutable / Air-gapped)** 備份：採用實體隔離或 WORM 物件鎖定，防範連網備份磁碟被勒索軟體同時加密。
  - 達成 **0 錯誤還原 (Zero recovery errors)**：定期進行開機還原測試演練，未經驗證還原的備份視為無效備份。

#### 2. 三大備份模式全方位深度對照

| 備份模式 | 備份資料範圍定義 | 備份耗時與空間 | 災難還原所需步驟與耗時 |
| :--- | :--- | :--- | :--- |
| **完整備份 (Full Backup)** | 備份目標系統的所有選定資料 | 耗時**最長**，佔用空間**最大** | **最快最簡單**。僅需最後一份完整備份即可直接還原 |
| **差異備份 (Differential)** | 僅備份自「**上一次完整備份**」後所有異動的資料 | 耗時與空間適中 (隨時間累積增大) | 還原快速。需：**最後一次完整備份 + 最後一次差異備份** (共2份) |
| **增量備份 (Incremental)** | 僅備份自「**上一次任意備份** (完整或增量)」後異動的資料 | 耗時**最短**，佔用空間**最小** | **還原最慢且繁瑣**。需：最後完整備份 + 其後所有增量備份依序還原，任一增量損毀即可能中斷 |

#### 3. 業務復原核心指標：RTO vs RPO
- **RTO (復原時間目標, Recovery Time Objective)**：中斷事件發生後，系統**必須恢復上線服務之最大容許時間**（重視復原速度）。
- **RPO (復原點目標, Recovery Point Objective)**：組織**可容許損失資料的最大時間跨度**（重視資料新鮮度，決定備份頻率）。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. Linux rsync 異地增量鏡像備份指令
```bash
# 使用 rsync 進行異地增量同步 (保持屬性、排除暫存目錄、刪除來源已不存在檔案)
rsync -avz --delete --exclude='*.tmp' /var/www/data/ backupuser@192.168.20.100:/backup/data/
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 備份觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **還原差異 vs 增量** | 題目問「週日做完整備份，週一至週四做增量備份，週五毀損需拿幾份還原？」 | **正解：需拿週日完整 + 週一、週二、週三、週四共 5 份**！若為差異備份則僅需週日完整 + 週四差異共 2 份 |
| **不可篡改性 (Air-gap)** | 題目問「為何 NAS 本地定期備份在勒索攻擊中常全軍覆沒？」 | 因為備份主機仍**連網且共用網域憑證**，駭客提權後直接將連網備份一併格式化；必須有**實體離線 (Air-gapped) 或 Immutable** 複本 |
| **RPO 概念** | 題目問「某系統每 4 小時備份一次，其 RPO 為何？」 | **RPO 為 4 小時**（最壞情況下損失過去 4 小時之交易資料） |

> 🔑 **防呆口訣**：
> - 3-2-1 鐵律記：3 複本、2 媒介、1 異地、加 1 離線 0 差錯！
> - 完整備份還原快，增量省位還原慢，差異適中拿兩塊。
> - RTO 看修復時間，RPO 看資料遺失容許線！
        """,
        "caseStudy": "【實務案例分析】某高科技封測廠產線資料庫半夜遭遇勒索軟體全盤加密，連同連網備份伺服器亦遭攻擊者以管理員權限格式化。此時 IT 團隊啟動終極 BCP 計畫：該廠落實了「3-2-1-1-0」原則，每逢週五均將資料寫入實體磁帶 (LTO Tape) 並由專人運送至遠端銀行保險庫實體離線保存 (Air-gap)。團隊自保險庫取出磁帶，配合乾淨新主機在 18 小時內完成全廠系統重建，成功於 RTO 時限內復原，未支付巨額贖金。"
    },
    {
        "id": "B2-M07",
        "title": "單元 7：社交工程防禦與企業資安意識演練",
        "keywords": ["Phishing Simulation", "Spear Phishing", "Watering Hole Attack", "SPF", "DKIM", "DMARC", "Security Awareness"],
        "summary": "掌握企業社交工程防護全貌：魚叉式釣魚 (Spear Phishing)、鯨釣 (Whaling)、水坑攻擊 (Watering Hole)、商業電子郵件詐騙 (BEC)；深入解析郵件網域身分鑑別三巨頭 SPF、DKIM、DMARC 協定原理與 DNS 配置實務，以及企業社交工程演練標準程序。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 社交工程進階攻擊型態對照
1. **魚叉式釣魚 (Spear Phishing)**：
   - 針對特定人員或部門（如人資、財務、研發），事先蒐集社交媒體與公開資訊，量身訂製高度逼真之郵件內容與誘餌檔案。
2. **水坑攻擊 (Watering Hole Attack)**：
   - 駭客不直接攻擊防禦森嚴之目標企業，而是先調查該企業員工經常造訪的第三方合法網站（如產業技術論壇、供應商入口），將其攻陷並植入瀏覽器零日漏洞攻擊程式，等候目標員工連線造訪時中招。
3. **商業電子郵件詐騙 (BEC / CEO Fraud)**：
   - 偽裝高階主管或合作廠商，利用急迫性與權威心理，繞過正式簽核流程騙取財務人員匯款。

#### 2. 電子郵件防偽三巨頭協定深度解析
1. **SPF (寄件者政策框架, Sender Policy Framework)**：
   - 網域擁有者在 DNS 發布 TXT 紀錄，**列明哪些伺服器 IP 位址有權代表該網域發送郵件**。收件伺服器比對發信來源 IP 是否列於清單中。
2. **DKIM (網域金鑰識別郵件, DomainKeys Identified Mail)**：
   - 發信伺服器以「私鑰」對郵件標頭與內容計算數位簽章 (DKIM-Signature Header)；收信端向寄信網域的 DNS 查詢「公鑰」驗證簽章，**確保郵件在傳輸過程中未遭竄改**。
3. **DMARC (網域型訊息鑑別、報告與一致性)**：
   - 整合 SPF 與 DKIM。網域擁有者定義當 SPF 或 DKIM 驗證失敗時，收件方應採取的處置策略：
     - `p=none`：僅監控回報，不攔截。
     - `p=quarantine`：隔離至垃圾郵件箱。
     - **`p=reject`**：**最嚴格防護，直接拒收並丟棄偽冒郵件**。

### 二、實務技術落地與指令配置 (Technical Implementation & CLI)

#### 1. DNS 電子郵件安全防偽 TXT 紀錄配置範例
```text
# 1. SPF 紀錄：僅允許自身 MX 紀錄與特定 IP 代表發信，其餘嚴格拒絕 (-all)
example.com.   IN TXT "v=spf1 mx ip4:203.0.113.10 -all"

# 2. DMARC 紀錄：強制要求嚴格拒收偽冒郵件，並將聚合報告寄至資安郵箱
_dmarc.example.com. IN TXT "v=DMARC1; p=reject; pct=100; rua=mailto:dmarc-reports@example.com"
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 郵件防護協定 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **SPF 盲點** | 選項宣稱「設定 SPF 即可防止郵件內容被篡改」 | **錯誤！SPF 只能驗證寄件 IP**，無法驗證內容是否被竄改；驗證內容完整性必須靠 **DKIM 數位簽章** |
| **DMARC 策略選項** | 題目問哪一個 DMARC 策略最能有效保護企業網域不被冒名發送釣魚信給大眾？ | **`p=reject` (直接拒收)**。`p=none` 只能監控 |
| **水坑攻擊概念** | 題目描述駭客入侵知名同業論壇以感染訪問該論壇之目標企業員工 | **水坑攻擊 (Watering Hole Attack)** |

> 🔑 **防呆口訣**：
> - SPF 查 IP 名單，DKIM 簽章防篡改，DMARC 下令全拒收 (reject)！
> - 鎖定目標叫魚叉，埋伏論壇是水坑。
> - 急切匯款莫著急，電話照會解百惑！
        """,
        "caseStudy": "【實務案例分析】某國際半導體公司屢遭駭客註冊相似網域偽造採購單。資安團隊全面推行防護工程：第一、在企業所有公網網域啟用 DNSSEC 結合嚴格的 SPF 與 DKIM 簽名；第二、在 DMARC 策略中配置 `p=reject`，強制全世界收件郵件伺服器凡收到未通過 SPF/DKIM 檢驗的偽冒信件一律直接拒收丟棄；第三、每季對全體員工無預警實施釣魚郵件模擬演練，點擊率超過 5% 的部門全員強制接受加強型實體資安培訓，成功使企業外部偽冒事件下降 99%。"
    },
    {
        "id": "B2-M08",
        "title": "單元 8：實體環境安全、設備生命週期與媒體廢棄銷毀",
        "keywords": ["Physical Security", "Mantrap", "Data Sanitization", "NIST SP 800-88", "Degaussing", "Physical Destruction"],
        "summary": "掌握資料中心實體門禁縱深控制 (防尾隨雙重旋轉門 Mantrap/Air-lock)、供電環控與 FM-200 氣體滅火安全、儲存媒體生命週期報廢、符合 NIST SP 800-88 標準之資料清除 (Clear)、淨化 (Purge) 與銷毀 (Destroy) 規範實務。",
        "content": """
### 一、核心架構與國際標準對照 (Architecture & Standards)

#### 1. 實體門禁與環境安全控制
- **防尾隨機制 (Anti-Tailgating / Piggybacking)**：
  - **雙重安全旋轉門 (Mantrap / Air-lock)**：兩道門互鎖（Interlocking Doors），第一道門關閉並完成第二身分驗證（如刷卡 + 指紋）後，第二道門方可開啟，物理上限制一次僅容許單人通過。
- **資料中心環控與消防**：
  - **電力備援**：不斷電系統 (UPS) 提供初期過渡電力，發電機 (Generator) 提供長時間自主發電，配電盤雙迴路 (Dual-cord Power)。
  - **消防滅火系統**：機房嚴禁使用自動灑水系統（水會造成高壓設備短路與永久毀損）；必須使用**潔淨氣體滅火系統 (Clean Agent Fire Suppression，如 FM-200, Novec 1230, 惰性氣體 IG-541)**，透過中斷燃燒鏈滅火且不留殘留物。

#### 2. NIST SP 800-88 媒體資料清除與淨化三大等級

| 處置等級 (Level) | 技術手段與實作方式 | 資料復原可能性 | 適用情境與安全等級 |
| :--- | :--- | :--- | :--- |
| **1. 清除 (Clear)** | 邏輯性覆寫 (Overwriting)，以固定模式字元 (如全 0 或亂數) 覆蓋所有可定址磁區 | 一般簡易資料救援軟體無法讀取，但實驗室微探針仍有極微小機率復原 | 設備於組織內部不同部門間移交或降階重用 |
| **2. 淨化 (Purge)** | **高斯消磁 (Degaussing)** (針對傳統磁帶/HDD) 或 **加密抹除 (Cryptographic Erase, CE)** | 即使在尖端實驗室設備下亦**完全不可復原** | 設備即將釋出組織外部、轉售或報廢 |
| **3. 銷毀 (Destroy)** | **物理破碎 (Shredding)** 碾碎至規定顆粒大小、焚毀 (Incineration)、融熔 | 物理結構完全摧毀，絕無復原可能 | 處理極機密、國防或高度機敏資料媒體 |

### 二、實務技術落地與監管作業 (Chain of Custody)

```text
【機敏硬碟報廢標準作業程序 (SOP)】
1. 盤點登記：比對硬碟序號 (Serial Number) 與資產清冊。
2. 淨化消磁：使用通過認證之消磁機 (強度大於 8,000 高斯) 破壞磁區結構。
3. 實體物理粉碎：送入工業破碎機碾壓成直徑小於 2mm 之碎屑。
4. 全程監管記錄：資安與稽核人員現場雙人監控並全程錄影。
5. 出具文件：廠商與監管主管共同簽署《報廢銷毀證明書》並歸檔稽核。
```

### 三、iPAS 官方考點盲點與防呆破題口訣 (Exam Traps & Distractors)

| 實體與銷毀觀念 | 考題常見混淆陷阱 | 官方標準解答認定 |
| :--- | :--- | :--- |
| **SSD 固態硬碟消磁** | 題目問「使用強力消磁機 (Degausser) 能否銷毀 SSD 固態硬碟之資料？」考生常誤選可以 | **無效！SSD 採用閃存快閃記憶體 (NAND Flash)，非磁性媒體**，消磁對 SSD 完全無效！SSD 必須使用「加密抹除 (CE)」或「實體晶片破碎 (Shredding)」 |
| **防尾隨最佳機制** | 題目問防止未授權訪客尾隨員工進入機房最佳設施 | **雙重防尾隨門 (Mantrap / Air-lock)** |
| **機房滅火氣體** | 考題出現 CO2、水霧、FM-200，問有人機房優先選擇 | **FM-200 或 Novec 1230** (高濃度二氧化碳 CO2 會使人員窒息，僅用於無人機房) |

> 🔑 **防呆口訣**：
> - 傳統硬碟可消磁，SSD 快閃必粉碎！
> - 門禁防尾用 Mantrap，機房滅火 FM-200。
> - Clear 覆寫內部換，Purge 淨化外流安，Destroy 碎裂無牽掛！
        """,
        "caseStudy": "【實務案例分析】某大型金控進行資料中心伺服器汰舊換新，共有 500 顆退役 SAS 磁碟與 200 顆 NVMe SSD。資安長嚴格遵循 NIST SP 800-88 標準作業：SAS 傳統磁碟先經由 10,000 高斯消磁機完成磁性消除，確認馬達與磁軌完全失效；針對消磁無效的 200 顆 SSD，則直接送入工業雙軸物理破碎機進行現場刀刃切割，將快閃記憶體晶片碾碎成小於 5mm 顆粒。資安稽核員全程錄影並核對序號產出報廢證書，徹底杜絕了退役二手硬碟資料外流風險。"
    }
]
