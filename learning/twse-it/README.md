# 臺灣證券交易所 (TWSE) 資訊人員招募備考神盾

> 臺灣證券交易所新進人員招募甄試（資訊人員）專屬自學備考系統。純靜態 HTML5/CSS/JavaScript 架構，無需安裝任何後端依賴，以手機或電腦瀏覽器開啟 `index.html` 即可展開極致研鑽。

---

## 系統核心特色與亮點

**雙考科分軌準備**，專為**「資通安全人員」**（主考科）與**「系統與網路管理人員」**（實務考科）量身打造，涵蓋：
- **114 題全真標竿滿分申論題庫**（資通安全 68 題 ＋ 系統網路 46 題，含 **50 題最新預測猜題**、嚴格採點給分規範、閱卷委員得分秘笈、滿分五段式標竿範本與延伸深度解析）。
- **24 大深入核心速記講義**（雙科各 12 章，每章皆內建【🧠 3 秒核心速記骨幹 · 考試秒殺心法】口訣、記憶拆解表格、實務參數與 AAA 級高對比度代碼閱讀）。
- **雙語金融資訊術語辭典**（收錄國際金融高頻核心詞彙、國際音標 IPA、繁體中文精解、證交所實務情境與 Web Speech API 真人語音發音）。
- **全真計時申論模擬考引擎**（支援 2 題/4 題隨機抽題、50/100 分鐘全真倒數、線上即時擬答草稿存檔、字數即時統計與交卷對比檢討）。
- **極致手機響應式設計（Mobile-First Adaptive UI）**：支援 iOS / Android 手機無障礙直覺研鑽，導覽列橫向平滑滑動、章節標籤流暢切換、代碼與表格防溢位滑動、觸控友善大按鈕與輸入防縮放。

---

## 考科涵蓋範圍與模組架構

### 一、資通安全人員 (資訊安全概論 / 資通安全) — 68 題標竿申論 ＋ 12 章速記講義
1. **第 1 章：金融資安法規治理與證券期貨業聯防體系** (金融資安行動方案 2.0、30 分鐘重大資安通報、F-ISAC/CERT/SOC、資通安全管理法 A 級機關、CISO 設置、第三方供應鏈 SBOM 治理)
2. **第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）** (ISO 27001:2022 四大主題 93 項控制措施、SoA 適用性聲明、NIST CSF 2.0 六大功能、BIA 營運衝擊分析、ISO 19011 主導稽核實務)
3. **第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證** (AES-256-GCM、ECC/RSA、SHA-256、HMAC、金融 HSM FIPS 140-3 零化防護、數位簽章法、X.509 憑證鏈、OCSP Stapling、TLS 1.3/PFS、後量子 PQC)
4. **第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理** (NIST SP 800-207、PDP/PEP 決策強制、MFA/FIDO2 來源網域綁定抗釣魚、OAuth 2.1/DPoP、PAM 堡壘機、雙人授權、微隔離)
5. **第 5 章：安全軟體開發生命週期（SSDLC）與 OWASP Top 10** (OWASP Top 10:2021 A01~A10、SQLi/XSS/CSRF/SSRF 防禦、SAST/DAST/SCA、Shift-Left 左移安全、CSP 標頭、Cosign 簽章、Sigstore)
6. **第 6 章：分散式阻斷服務（DDoS）攻擊防禦與網路微隔離** (電信端 Clean Pipe 清洗、SYN Cookie、BGP Anycast、WAF、Cilium eBPF 微隔離、DNSSEC/RPZ 防快取污染)
7. **第 7 章：資安監控中心（SOC）、SIEM 與威脅情資聯防** (7x24 SOC 三層架構、SIEM/UEBA、SOAR 自動化 Playbook、EDR/XDR、MITRE ATT&CK 映射、IoC/IoA、WORM 審計日誌)
8. **第 8 章：郵件伺服器資安與進階端點防禦（EDR/XDR）** (SPF 發信驗證、DKIM 簽章、DMARC 阻斷策略、EDR 攔截 PowerShell/WMI 無檔案攻擊、防社交工程演練)
9. **第 9 章：容器安全、DevSecOps 與 Kubernetes 叢集防禦** (CIS Kubernetes Benchmark、Non-root 與唯讀檔案系統、OPA Gatekeeper / Kyverno 準入控制器、Falco eBPF 動態偵測)
10. **第 10 章：滲透測試、弱點管理與紅藍攻防演練** (PTES 滲透測試、CVSS 3.1 評級、紅藍紫三隊協同、盲測演練、攻擊鏈 Kill Chain 阻斷)
11. **第 11 章：業務營運持續（BCP）、高可用性與災難復原演練** (3-2-1-1-0 備份原則、WORM 不可篡改儲存、RTO ≤ 10 分鐘、RPO = 0、同城雙活資料庫、零贖金原則)
12. **第 12 章：新興金融科技安全（GenAI 防禦、聯邦學習與量子密碼）** (金管會 AI 指引三大原則、OWASP Top 10 for LLM、AI Guardrails 護欄、FIPS 203/204/205 PQC 遷移、聯邦學習)

### 二、系統與網路管理人員 (計算機概論 / 系統與網路管理) — 46 題標竿申論 ＋ 12 章速記講義
1. **第 1 章：臺灣證交所撮合架構與超低延遲運算** (逐筆撮合、Kernel Bypass、DPDK、Solarflare Onload、NUMA、Linux isolcpus/nohz_full、LMAX Disruptor、mlockall、1GB HugePages、io_uring)
2. **第 2 章：金融高可靠網路拓撲與行情推播** (UDP Multicast、PIM-SSM、IGMPv3、Spine-Leaf、ECMP、Cut-Through、Microburst 微突發防禦、Feed A/B 雙路冗餘、DWDM 光纖直連)
3. **第 3 章：金融高精度時間同步與時序工程** (PTP IEEE 1588v2、硬體時間戳記、Grandmaster Clock、邊界時鐘 BC、透明時鐘 TC、MiFID II 100µs 合規、NTP vs PTP)
4. **第 4 章：作業系統核心調校與即時排程（Linux Kernel Tuning）** (Linux 核心啟動參數、CFS 排程、SCHED_FIFO、TCP_NODELAY、TCP_QUICKACK、SO_BUSY_POLL、epoll ET、Perf 分析、eBPF 觀測)
5. **第 5 章：金融通訊協定（FIX/ITCH/OUCH）與低延遲訊息佇列** (FIX 4.2/4.4、NASDAQ ITCH 5.0 二進制行情、OUCH 極致下單、Kafka 分區循序寫入、訊息冪等性、sendfile 零拷貝)
6. **第 6 章：分散式交易、雙活資料庫與高可用叢集** (ACID、WAL 預寫日誌、MVCC、2PC 兩階段提交、TCC/Saga 最終一致性、同城雙活、Raft 共識演算法)
7. **第 7 章：現代伺服器硬體架構、快取階層與多核心優化** (L1/L2/L3 快取階層、False Sharing 偽共享消除、alignas(64)、NUMA 親和性、__builtin_expect 分支提示、LTO)
8. **第 8 章：雲原生儲存、高可用叢集與微突發流量防禦** (全快閃儲存 AFA、NVMe-oF RoCEv2、環形緩衝區擴大、滑動視窗令牌桶限流、無失真乙太網 PFC/ECN)
9. **第 9 章：微服務、容器編排與 Kubernetes 金融實務** (PodTopologySpreadConstraint 拓撲分佈、NodeAffinity 親和調度、SR-IOV 網卡直通、HPA/KEDA 自動擴展、Cilium eBPF CNI)
10. **第 10 章：叢集腦裂防範、分散式共識與 STONITH 防護** (Split-Brain 腦裂成因、奇數節點 Quorum 2N+1、STONITH 電源擊殺、Corosync/Pacemaker、SCSI-3 PR 磁碟鎖)
11. **第 11 章：分散式訊息中介、事件驅動架構與串流運算** (Kafka 順序寫入、Zero-Copy 零拷貝、Exactly-Once 語義、ISR 同步副本、日誌 Compaction、背壓機制)
12. **第 12 章：維運自動化（IaC）、SRE 網站可靠性工程與監控體系** (四大黃金指標、SLI/SLO/SLA 錯誤預算、Terraform/Ansible IaC、Prometheus 告警、綠色算力 PUE 與液冷機櫃)

---

## 視覺與互動亮點

- **和風極簡美學（Warm Japanese Minimalist）**：精選和紙暖白（`#FAF7F2`）、淡木亞麻（`#F3ECE2`）、濃墨色（`#2C2825`）與弁柄紅（`#C2593F`）溫潤配色，舒適不刺眼。
- **高對比度代碼視窗（AAA High Contrast Compliance）**：代碼背景採用濃墨夜色（`#1C1917`）搭配耀眼柔白字體，對比度大於 15:1。
- **雙語專利語音整合（Web Speech API TTS）**：所有金融資訊英文術語均具備一鍵真人英語發音與中文釋義，邊看講義邊聽正確讀音。
- **深淺模式無縫切換**：內建晝夜和風雙模式，偏好設定自動持久化於瀏覽器 LocalStorage。
- **線上擬答自動暫存**：每一題申論的練習草稿、字數統計與收藏狀態全自動本地儲存，無懼頁面刷新。

---

## 快速啟動

直接雙擊點擊 `index.html`，以手機或電腦 Chrome / Edge / Safari 開啟即可使用。
亦可透過專案根目錄的 `啟動Hub.bat` 於本機入口台啟動。
