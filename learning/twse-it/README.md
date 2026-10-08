# 臺灣證券交易所 (TWSE) 資訊人員招募備考神盾

> 臺灣證券交易所新進人員招募甄試（資訊人員）全方位備考自學系統。純靜態 HTML5/CSS/JavaScript 架構，無需安裝任何後端依賴，以瀏覽器開啟 `index.html` 即可展開極致研鑽。

---

## 一句話說明

**雙考科分軌準備**，專為**「系統與網路管理人員」**（計算機概論）與**「資通安全人員」**（資訊安全概論）量身打造，涵蓋：
- **1,400 題四選一選擇題庫**（雙科各 700 題，題題具備英文專有名詞、Web Speech TTS 真人語音發音、雙向翻譯與四選項逐項深度剖析）。
- **24 大深入核心講義**（雙科各 12 章推導、呼叫盒、呼應實戰的代碼與拓撲圖示，AAA 級超高對比度代碼閱讀）。
- **20 題標竿滿分申論範本**（雙科各 10 題，嚴格遵循國家考試與證交所招募評分標準，提供明確採點給分規範與精準得分字）。
- **雙語金融資訊術語辭典**（收錄國際金融高頻核心詞彙、國際音標 IPA、繁體中文精解與臺灣證交所實務情境）。
- **全真計時模擬考引擎**（支援 50 題 / 100 題隨機抽題、60 / 120 分鐘倒數、70 分及格檢核與錯題一鍵複習）。

---

## 考科涵蓋範圍與模組架構

### 一、系統與網路管理人員 (計算機概論 / 系統與網路管理) — 700 題 ＋ 12 章講義 ＋ 10 題申論
1. **第 1 章：臺灣證交所撮合架構與低延遲計算** (逐筆撮合、Kernel Bypass、DPDK、Solarflare Onload、NUMA、Linux isolcpus/nohz_full、LMAX Disruptor、mlockall、1GB HugePages)
2. **第 2 章：金融高可靠網路拓撲與行情推播** (UDP Multicast、PIM-SSM、IGMPv3、Spine-Leaf、ECMP、Cut-Through、Microburst、Feed A/B 雙路冗餘、BGP EVPN/VXLAN、RoCEv2/PFC)
3. **第 3 章：金融高精度時間同步與時序工程** (PTP IEEE 1588v2、硬體時間戳記、Grandmaster Clock、邊界時鐘 BC、透明時鐘 TC、MiFID II 100µs 合規、NTP vs PTP)
4. **第 4 章：Linux 系統底層調校與性能工程** (Linux 核心啟動參數、CFS 排程、SCHED_FIFO、TCP_NODELAY、TCP_QUICKACK、SO_BUSY_POLL、epoll ET、Perf 分析、eBPF 觀測)
5. **第 5 章：金融關聯式資料庫與高可用架構** (ACID、WAL 預寫日誌、MVCC、B+ Tree、2PC 兩階段提交、同城雙活雙寫、CDC、分庫分表 Sharding、分散式事務)
6. **第 6 章：儲存架構、快照備份與災難復原** (NVMe-oF、全快閃儲存陣列、SAN 光纖交換、同步遠端鏡像 SRDF、RTO/RPO 指標、WORM 防竄改、無預警災難切換演練)
7. **第 7 章：虛擬化、容器平台與維運監控** (Kubernetes 金融私有雲、CRI-O/Containerd、SR-IOV 直通、Prometheus/Grafana、OpenTelemetry 分散式追蹤、SRE SLI/SLO)

### 二、資通安全人員 (資訊安全概論 / 資通安全) — 700 題 ＋ 12 章講義 ＋ 10 題申論
1. **第 1 章：金融資安法規治理與證券期貨業聯防體系** (金融資安行動方案 2.0、30 分鐘重大資安通報、F-ISAC/CERT/SOC、資通安全管理法、CISO 設置、第三方供應鏈管理、SBOM)
2. **第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）** (ISO 27001:2022 四大主題 93 項控制措施、SoA 適用性聲明、NIST CSF 2.0 六大功能、BIA 營運衝擊分析、CIS Controls v8)
3. **第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證** (AES-256-GCM、ECC/RSA、SHA-256、HMAC、金融 HSM FIPS 140-3、KMIP、數位簽章法、X.509 憑證鏈、OCSP Stapling、TLS 1.3/PFS)
4. **第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理** (NIST SP 800-207、PDP/PEP、MFA/FIDO2、OAuth 2.0/OIDC、SAML 2.0、PAM 堡壘機、雙人授權、微隔離、AD Tier 防護)
5. **第 5 章：應用程式安全、OWASP Top 10 與 DevSecOps** (OWASP Top 10:2021 A01~A10、SQLi/XSS/CSRF/SSRF 防禦、SAST/DAST/SCA、Shift-Left、CSP 標頭、API Security、Cosign 簽章)
6. **第 6 章：網路邊界防禦、DDoS 防護與微隔離架構** (次世代防火牆 NGFW、IDS/IPS、金融流量清洗中心 Clean Pipe、SYN Cookie、BGP Anycast、WAF、IPsec VPN、SASE、DNSSEC/RPZ)
7. **第 7 章：SOC 威脅監控、SIEM/SOAR、EDR 與事件應變** (7x24 SOC 三層架構、SIEM/UEBA、SOAR 自動化 Playbook、EDR/XDR、MITRE ATT&CK、IoC/IoA、YARA/SIGMA、記憶體鑑識 Volatility、WORM 冷備份)

---

## 視覺與互動亮點

- **和風極簡美學（Warm Japanese Minimalist）**：精選和紙暖白（`#FAF7F2`）、淡木亞麻（`#F3ECE2`）、濃墨色（`#2C2825`）與弁柄紅（`#C2593F`）溫潤配色，徹底消除傳統冷白反光眩光。
- **高對比度代碼視窗（AAA High Contrast Compliance）**：終結代碼區塊文字泛白淡灰問題，代碼背景採用濃墨夜色（`#1C1917`）搭配耀眼柔白字體，對比度大於 15:1。
- **雙語專利語音整合（Web Speech API TTS）**：所有金融資訊英文術語均具備一鍵真人英語發音與中文釋義，邊看題目邊聽正確讀音。
- **深淺模式無縫切換**：內建晝夜和風雙模式，偏好設定自動持久化於瀏覽器 LocalStorage。
- **作答進度全自動記憶**：做過的題目、錯題本、星號收藏夾、模擬考最佳戰績自動本地儲存，無需連線後端資料庫。

---

## 快速啟動

直接雙擊點擊 `index.html`，以 Chrome / Edge / Firefox / Safari 開啟即可使用。
亦可透過專案根目錄的 `啟動Hub.bat` 於本機入口台啟動。
