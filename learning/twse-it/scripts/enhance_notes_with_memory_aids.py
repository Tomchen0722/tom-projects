# -*- coding: utf-8 -*-
"""
Enriches both notes-sec.js and notes-sysnet.js with
【🧠 3 秒核心速記骨幹 · 考試秒殺心法】
Ensures notes are deeply comprehensive yet instantaneously memorable.
"""
import os
import re
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SEC_MNEMONICS = {
    "sec-ch01": {
        "formula": "治聯監文四構面，三十通報十分斷；三道防線獨立立，一家受駭全體免。",
        "bullets_left": [
            ("治 (深化治理)", "專責 CISO 獨立資安部門 + 董事會三道防線"),
            ("聯 (強化聯防)", "F-ISAC (情資) + F-CERT (鑑識) + F-SOC (監控)"),
            ("監 (提升監韌)", "BIA 衝擊分析 + RTO ≤ 10分、RPO = 0"),
            ("文 (資安文化)", "全員社交工程郵件演練 + 國際證照考核")
        ],
        "bullets_right": [
            ("30 分鐘", "重大資安事件自「知悉」起法定初報時效"),
            ("10 分鐘", "核心交易系統中斷達 10 分鐘即判定為重大事件"),
            ("2小時 / 3天", "處置中每 2 小時更新進度，事件平息後 3 天交 RCA"),
            ("SBOM 交付", "委外軟體交付 SPDX/CycloneDX 物料清單")
        ]
    },
    "sec-ch02": {
        "formula": "四題九三新架構，組織人員實體技；五標六功治中樞，三觀證據斷缺失。",
        "bullets_left": [
            ("四大主題 93 項", "A.5 組織(37) / A.6 人員(8) / A.7 實體(14) / A.8 技術(34)"),
            ("11 項新控制項", "威脅情資、雲端安全、ICT持續整備、實體監控、資料外洩DLP"),
            ("SoA 五大標籤", "Control Types, CIA, IPDRR, Operational, Domains"),
            ("NIST CSF 2.0", "Govern(治理中樞) + Identify, Protect, Detect, Respond, Recover")
        ],
        "bullets_right": [
            ("客觀證據三要素", "書面程序 (Doc) + 執行紀錄 (Record) + 訪談驗證 (Interview)"),
            ("重大缺失 Major NC", "系統性失效、法規直接違法、影響驗證範圍，90天強制複查"),
            ("次要缺失 Minor NC", "單一偶發疏失，提交矯正預防措施 (CAPA) 書面審查"),
            ("PDCA 滾動優化", "Plan(政策風險) -> Do(落地執行) -> Check(內稽) -> Act(管審)")
        ]
    },
    "sec-ch03": {
        "formula": "雜湊摘要私鑰簽，公鑰驗章不抵賴；開殼零化保根鑰，前向保密握手快。",
        "bullets_left": [
            ("數位簽章原理", "SHA-256 摘要 + 客戶私鑰加密 = 數位簽章 (法律不可否認)"),
            ("X.509 憑證鏈", "Root CA -> Sub CA -> Entity (公鑰+主體+簽名+有效期)"),
            ("FIPS 140-3 L3", "實體防探針 + 開殼微秒零化 (Zeroization 永久抹除金鑰)"),
            ("KMIP 金鑰管理", "生成、儲存、備份、更新、銷毀全生命週期在 HSM 內部完成")
        ],
        "bullets_right": [
            ("OCSP Stapling", "由伺服器預先向 CA 取得帶簽名之狀態，消除客戶端查詢延遲"),
            ("TLS 1.3 PFS", "強制 ECDHE 臨時密鑰協商，達成完全前向保密 (抗歷史側錄)"),
            ("量子威脅破譯", "Shor 演算法瓦解 RSA/ECC，推動後量子 FIPS 203/204/205"),
            ("密鑰長度基準", "RSA ≥ 3072 bits / ECC ≥ 256 bits / AES ≥ 256 bits")
        ]
    },
    "sec-ch04": {
        "formula": "永不信任常驗證，最小特權設遭侵；PDP大腦做決策，PEP門神立馬行。",
        "bullets_left": [
            ("零信任三大原則", "Never Trust Always Verify / Least Privilege / Assume Breach"),
            ("核心控制邏輯", "原則決定點 PDP (PE引擎 + PA管理員) 下達允許/拒絕/MFA"),
            ("原則強制點 PEP", "閘道器/反向代理攔截流量，忠實執行 PDP 決策指令"),
            ("FIDO2 抗釣魚", "私鑰鎖死硬體安全晶片 (TPM 2.0)，Origin Binding 讓釣魚簽名失效")
        ],
        "bullets_right": [
            ("PAM 堡壘機治理", "消除永久特權，JIT 按需提權，雙人覆核授權 + 全程側錄"),
            ("OAuth 2.1 規範", "全面廢除隱含與密碼模式，強制 PKCE，授權碼限單次使用"),
            ("DPoP 權杖防竊", "RFC 9449 應用層公私鑰綁定，截獲 Token 無原生私鑰仍無法冒用"),
            ("連續性風險評估", "根據使用者身分、設備健康度、網路環境、存取標的動態評分")
        ]
    },
    "sec-ch05": {
        "formula": "威脅塑模左右移，白箱黑箱雙軌掃；參數查詢絕注入，組件清單查弱點。",
        "bullets_left": [
            ("SSDLC 左移安全", "Shift-Left：在需求與架構設計階段即導入安全，成本最低"),
            ("STRIDE 威脅塑模", "Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation"),
            ("三重自動化檢測", "SAST (靜態白箱原始碼) + DAST (動態黑箱掃描) + SCA (開源組件)"),
            ("防範 SQL 注入", "絕對禁止動態字串拼接 SQL，強制使用參數化查詢 (Prepared Statements)")
        ],
        "bullets_right": [
            ("SSRF 防範核心", "強制內網 IP 阻絕黑名單 (禁止存取 127.0.0.1, 169.254.169.254)"),
            ("XSS 防禦原則", "輸出強制 HTML/JS/CSS Context 敏感編碼 + 啟用嚴格 CSP 標頭"),
            ("SBOM 軟體清單", "SPDX / CycloneDX 標準格式，15 分鐘全系統定位零日漏洞"),
            ("金鑰零寫死", "程式碼庫嚴禁 Hard-coded 密碼金鑰，全面對接 HashiCorp Vault")
        ]
    },
    "sec-ch06": {
        "formula": "三四泛洪電信洗，七層慢速靠牆抵；微隔離斷橫向擴，零信任裡內外齊。",
        "bullets_left": [
            ("L3/L4 流量型 DDoS", "SYN/UDP/NTP 泛洪，依賴電信端 Clean Pipe 清洗與 BGP Anycast 分流"),
            ("L7 應用層慢速攻擊", "Slowloris, HTTP POST Flood，依賴 WAF 協同行為分析與驗證碼阻絕"),
            ("微隔離核心價值", "將資料中心細分為微安全網段，消除傳統扁平內網橫向移動風險"),
            ("Cilium eBPF 架構", "在 Linux 核心層實施 L3/L4/L7 身分感知過濾，無 iptables 效能損耗")
        ],
        "bullets_right": [
            ("速率限制策略", "滑動視窗令牌桶 (Token Bucket)，限制單一 IP 每秒最大連線頻率"),
            ("DNS 防護縱深", "部署 DNS RPZ 阻斷 C2 域名解析，啟用 DNSSEC 防範快取污染"),
            ("同城清洗機制", "證交所專屬流量清洗中心，正常業務封包回注延遲 < 1ms"),
            ("演練驗證指標", "每年辦理極端 Tbps 級無預警演練，核心撮合服務維持 100% 可用")
        ]
    },
    "sec-ch07": {
        "formula": "全網日誌匯集中，關聯分析抓黑客；SOAR劇本秒阻斷，七乘二四守夜客。",
        "bullets_left": [
            ("SOC 核心三位一體", "人員 (7x24分析師) + 流程 (SOP處置) + 技術 (SIEM/SOAR/EDR)"),
            ("SIEM 關聯分析", "統一收集 OS、網路、資料庫日誌，基於規則與 UEBA 異常行為建模"),
            ("SOAR 自動化應變", "Security Orchestration, Automation & Response，依 Playbook 秒級阻斷"),
            ("威脅情資共享", "對接 F-ISAC，自動轉換 STIX/TAXII 格式 IoC 下發防火牆封殺")
        ],
        "bullets_right": [
            ("MTTD / MTTR", "平均偵測時間壓降至 15 分鐘以內，平均處置時間壓降至 30 分鐘以內"),
            ("日誌留存法規", "核心資通系統 Audit Log 強制保存 1 年以上，防篡改 WORM 儲存"),
            ("MITRE ATT&CK", "將偵測規則完整映射至攻擊戰術與技術矩陣，找出防禦盲點"),
            ("告警降噪機制", "AI 機器學習關聯同源告警，消除告警疲勞 (Alert Fatigue)")
        ]
    },
    "sec-ch08": {
        "formula": "SPF驗發信源，DKIM防信件竄；DMARC策略阻偽冒，EDR捉無檔案。",
        "bullets_left": [
            ("SPF (寄件來源)", "DNS TXT 紀錄宣告合法寄信主機 IP 清單，接收端比對封包來源"),
            ("DKIM (防信件竄改)", "寄件伺服器私鑰為郵件 Header 簽名，接收端以 DNS 公鑰驗簽"),
            ("DMARC (政策阻斷)", "整合 SPF/DKIM，宣告 p=reject 強制退信偽冒信件，定期回傳報告"),
            ("端點 EDR 核心", "連續監控記憶體與行程行為，精準攔截 PowerShell/WMI 無檔案攻擊")
        ],
        "bullets_right": [
            ("雙因子認證 (MFA)", "郵件登入強制使用硬體 FIDO2 / 企業 Authenticator，杜絕釣魚"),
            ("社交工程演練", "每年至少 2 次全員社交工程郵件演練，開啟惡意連結者強制再培訓"),
            ("LotL 攻擊偵測", "監控「Living-off-the-Land」合法系統指令被異常叫用之行程鏈"),
            ("自動沙箱拆解", "未知郵件附件自動投遞至雲端/地端隔離沙箱執行動態行為分析")
        ]
    },
    "sec-ch09": {
        "formula": "映像簽章源頭鎖，唯讀非根不可變；命名空間嚴微隔，準入控制阻破口。",
        "bullets_left": [
            ("映像檔簽名", "Cosign / Sigstore 無金鑰簽名，未經簽名之容器禁止部署進生產環境"),
            ("最小權限執行", "強制 runAsNonRoot: true、readOnlyRootFilesystem: true，封鎖 root 容器"),
            ("準入控制門神", "OPA Gatekeeper / Kyverno 實施宣告式政策，阻絕特權容器逃逸"),
            ("核心防護加固", "移除 Linux Capabilities (drop: [ALL])，限制 seccomp 與 AppArmor")
        ],
        "bullets_right": [
            ("NetworkPolicy 隔絕", "預設 Default-Deny，跨 Namespace 僅開放必要微服務服務連接埠"),
            ("機密資訊託管", "嚴禁 ConfigMap 明文存密鑰，全面整合 HashiCorp Vault / External Secrets"),
            ("容器動態偵測", "部署 Falco eBPF 探針，即時監控容器內異常 shell 呼叫與二進制寫入"),
            ("CIS Benchmark", "定期執行 kube-bench 與 kube-hunter，確保節點組態符合金融基準")
        ]
    },
    "sec-ch10": {
        "formula": "ATT&CK對陣圖，紫隊協同補破洞；黑盒盲測真實態，優先修補高風孔。",
        "bullets_left": [
            ("紅藍紫三隊機制", "紅隊 (實兵模擬滲透) + 藍隊 (SOC防禦偵測) + 紫隊 (跨組協同除錯)"),
            ("MITRE ATT&CK 框架", "以 14 大戰術矩陣為基準，系統化盤點企業防禦偵測覆蓋率"),
            ("盲測演練 (Blind Test)", "防禦藍隊事前不知情，實戰驗證監控警報靈敏度與通報流程"),
            ("弱點生命週期", "資產識別 -> 漏洞掃描 -> CVSS 風險評級 -> 優先修補 -> 驗證覆核")
        ],
        "bullets_right": [
            ("CVSS 3.1 評級", "分數 ≥ 9.0 (Critical) 必須於 72 小時內完成修補或補償性控制"),
            ("滲透測試標準", "遵循 PTES (滲透測試執行標準)，涵蓋外網、內網與社交工程"),
            ("攻防演練合規", "金融關鍵基礎設施依規定每年至少辦理 2 次無預警實兵攻防演習"),
            ("根本原因除錯", "演練結束召開事後檢討會 (AAR)，產出技術硬化與制度改善報告")
        ]
    },
    "sec-ch11": {
        "formula": "三二一一零備份，不可篡改防勒索；RTO十分RPO零，同城雙活最可靠。",
        "bullets_left": [
            ("3-2-1-1-0 備份原則", "3份副本、2種不同媒介、1份異地、1份離線/不可篡改(WORM)、0驗證錯誤"),
            ("嚴苛金融容災指標", "核心撮合系統 RTO ≤ 10 分鐘 (快速復原)、RPO = 0 (零資料遺失)"),
            ("同城雙活資料庫", "板橋主機房與同城備援機房專線直連，同步鏡像日誌 (Sync WAL)"),
            ("防勒索氣隙 (Air-Gap)", "生產環境與離線備份完全物理/邏輯隔離，金鑰獨立保管")
        ],
        "bullets_right": [
            ("BCP 啟動門檻", "主機房遭遇大規模物理災害或核心勒索加密，30 分鐘內決定接管"),
            ("不可篡改儲存 (WORM)", "Write Once, Read Many，防範內部惡意管理者或勒索軟體直接刪除備份"),
            ("定期演練標準", "每年進行至少 2 次同城全功能實兵倒換演練，真實切斷主機房連線"),
            ("零妥協原則", "金管會嚴格禁止金融機構向勒索軟體犯罪組織支付贖金")
        ]
    },
    "sec-ch12": {
        "formula": "後量子格密碼換，提示注入設護欄；隱私脫敏人機協，模型合規長久遠。",
        "bullets_left": [
            ("後量子 PQC 遷移", "NIST FIPS 203 (ML-KEM 密鑰交換) / FIPS 204 (ML-DSA 數位簽章)"),
            ("防範提示注入", "部署雙向 AI Guardrails，輸入側消毒 (DLP/正則)，輸出側格式校驗"),
            ("金管會 AI 指引", "核心三大原則：人機協同 (Human-in-the-loop)、隱私脫敏、RAG 可解釋性"),
            ("聯邦學習 (FL)", "數據不出域，僅傳遞模型梯度參數，達成跨機構合規風控建模")
        ],
        "bullets_right": [
            ("SNDL 側錄威脅", "Store Now, Decrypt Later，推行雙模混合憑證 (Hybrid PKI) 提前抗量子"),
            ("LLM Red Teaming", "對金融 AI 系統定期進行對抗樣本測試、越獄 (Jailbreak) 與投毒演練"),
            ("加密敏捷性", "軟體架構解耦加密演算法實作，支援無痛平滑升級次世代標準"),
            ("資料外洩防禦", "禁止未去識別化之客戶個資直接作為外部 LLM Prompt 輸入")
        ]
    }
}

SYSNET_MNEMONICS = {
    "sn-ch01": {
        "formula": "核心旁路跳排程，零拷貝池無鎖環；親和綁核消抖動，微秒撮合極致快。",
        "bullets_left": [
            ("核心旁路 Kernel Bypass", "Solarflare Onload / DPDK，封包直達用戶空間，跳過 Linux 核心堆疊"),
            ("無鎖環形佇列", "LMAX Disruptor 架構，以原子 CAS 操作消除鎖競爭 (Zero Lock)"),
            ("快取行對齊 (alignas 64)", "消除 False Sharing 偽共享，防止多核心快取無效化與匯流排鎖定"),
            ("單執行緒核心綁定", "Single-Threaded Pinned Model，單執行緒專注撮合，鎖競爭直接歸零")
        ],
        "bullets_right": [
            ("SO_BUSY_POLL 輪詢", "通訊端忙輪詢技術，消除中斷喚醒延遲，代價是 CPU 佔用 100%"),
            ("TCP_NODELAY 停用 Nagle", "小封包立即送出，配合 TCP_QUICKACK 消除 40ms 假死鎖延遲"),
            ("快取行預取 __builtin_prefetch", "在計算期間提前載入下一筆委託至 CPU 快取，隱藏記憶體延遲"),
            ("尾端延遲 P99.9 控制", "消除作業系統背景抖動 (Jitter)，撮合延遲方差壓降至奈秒級")
        ]
    },
    "sn-ch02": {
        "formula": "脊葉雙層固定跳，線速直通不排隊；IGMPv3指定源，行情多播百萬隨。",
        "bullets_left": [
            ("Spine-Leaf 脊葉拓撲", "任意兩台撮合主機間固定雙跳 (Two-hop)，延遲嚴格對稱確定"),
            ("Cut-Through 直通交換", "ASIC 僅讀取前 64 bytes 目的 MAC 即開始轉發，交換延遲壓降至 200ns"),
            ("PIM-SSM 多播協定", "指定來源多點廣播 (S,G)，免去 RP 匯聚點瓶頸，行情直線路徑分發"),
            ("IGMPv3 來源過濾", "券商端精確訂閱 (INCLUDE 模式) 特定交易所發布主機，免收干擾雜訊")
        ],
        "bullets_right": [
            ("ECMP 等價多路徑", "基於 5-Tuple 雜湊在多條上行鏈路平衡流量，無單點瓶頸"),
            ("硬體封包複製", "交換機 ASIC 硬體線速複製多播封包，向千家券商廣播零延遲累加"),
            ("網卡多佇列 RSS", "Receive Side Scaling，將封包依雜湊分散至多顆 CPU 核心處理"),
            ("光纖直連優化", "板橋與各大券商機房採用低折射率單模光纖，光速延遲 5μs/km 精算")
        ]
    },
    "sn-ch03": {
        "formula": "納秒齊步靠硬體，主從時間雙向傳；IEEE 1588時鐘樹，交易時戳無誤差。",
        "bullets_left": [
            ("PTP (IEEE 1588v2)", "微秒/奈秒級精準時鐘協定，遠超傳統 NTP (毫秒級) 之精度"),
            ("硬體 PHY 時間戳", "網卡物理層收發封包當下即刻打上記號，徹底排除 OS 軟體延遲"),
            ("時鐘階層樹狀結構", "Grandmaster (GPS/北斗銫原子鐘) -> Boundary Clock (邊界) -> Slave (伺服器)"),
            ("透明時鐘 (TC) 修正", "交換機動態計算內部轉發駐留時間 (Residence Time) 並補償校正")
        ],
        "bullets_right": [
            ("雙向延遲計算公式", "Offset = [(t2-t1) - (t4-t3)] / 2；Delay = [(t2-t1) + (t4-t3)] / 2"),
            ("逐筆撮合公平性", "確保每筆委託抵達時戳不可被作弊竄改，保障撮合順序絕對公允"),
            ("MiFID II 法規遵循", "對標歐盟高頻交易法規，時鐘同步偏差要求 ≤ 100 微秒，解析度 1 微秒"),
            ("時鐘源雙備援", "衛星天線雙路部署，失鎖時靠原子鐘晶振 (OCXO/Rubidium) 高精度守時")
        ]
    },
    "sn-ch04": {
        "formula": "隔離核心停滴答，親和綁定抗排程；大頁鎖定防換出，消除長尾穩如山。",
        "bullets_left": [
            ("isolcpus 核心隔離", "將撮合專用 CPU 自 Linux CFS 排程器完全剔除，杜絕背景行程干擾"),
            ("nohz_full (Tickless)", "當隔離核心僅運行單一執行緒時，停用定時器中斷 (Timer Tick)"),
            ("mlockall 記憶體鎖定", "將交易程式碼與資料完全鎖定於實體 RAM，防範 Major Page Fault"),
            ("1GB 巨型分頁 HugePages", "分頁大小由 4KB 暴增至 1GB，大幅提高 CPU TLB 轉譯緩衝區命中率")
        ],
        "bullets_right": [
            ("SCHED_FIFO 即時排程", "先進先出即時排程，優先級設為 99，非即時行程完全無法搶佔"),
            ("關閉 CPU C-States", "BIOS 鎖定 C0 最高效能狀態，停用節能降頻與 Turbo Boost 抖動"),
            ("中斷親和性 (smp_affinity)", "將網卡中斷綁定至獨立輔助核心，避免中斷打擾核心撮合執行緒"),
            ("髒頁回寫參數調校", "降低 dirty_background_ratio，防止撮合期間遭遇核心大區塊 I/O 停頓")
        ]
    },
    "sn-ch05": {
        "formula": "FIX下單規範嚴，ITCH行情廣播宣；OUCH簡潔速度快，Kafka分區順序傳。",
        "bullets_left": [
            ("FIX 4.2 / 4.4 協定", "金融資訊交換標準 (Tag=Value 格式)，語意豐富，廣泛用於委託下單"),
            ("NASDAQ ITCH 5.0", "定長二進制超低延遲行情廣播，直觀解析，解析速度較 FIX 快十倍"),
            ("OUCH 極致下單協定", "極度精簡的定長二進制委託協定，針對極致撮合最佳化"),
            ("FIX Engine 設計", "無動態記憶體分配 (Zero-Allocation)，預分配封包池以消除 GC/Malloc 開銷")
        ],
        "bullets_right": [
            ("Kafka 分區循序寫入", "以 Partition 為單位保證單一股票委託單絕對時間順序不可逆"),
            ("訊息冪等性 (Idempotence)", "下單系統透過 ClOrdID (委託編號) 達成去重複，防止重複扣款"),
            ("零拷貝傳輸 (sendfile)", "Kafka 透過 Linux sendfile 系統呼叫，資料直通網卡，不經使用者空間"),
            ("落盤策略 (flush.messages)", "金融核心設定嚴格 acks=all，保證多節點副本寫入成功才回覆")
        ]
    },
    "sn-ch06": {
        "formula": "兩階段提交保一致，預寫日誌抗崩潰；同城同步零損失，腦裂隔離定生死。",
        "bullets_left": [
            ("ACID 原則嚴格恪守", "Atomicity, Consistency, Isolation (序列化隔離), Durability"),
            ("WAL 預寫日誌機制", "Write-Ahead Logging，資料變更必須先順序寫入磁碟日誌才修改記憶體"),
            ("同城雙活同步複製", "主資料庫與備援資料庫同步傳輸日誌，保證 RPO = 0 (零資料遺失)"),
            ("兩階段提交 (2PC)", "協調者發起 Prepare 投票，全員同意方可 Commit，任一失敗即 Rollback")
        ],
        "bullets_right": [
            ("半同步複製 (Semi-Sync)", "至少一個備援節點 ACK 接收日誌後才回覆客戶端，兼顧延遲與安全"),
            ("分散式 MVCC", "多版本並行控制，讀取不阻塞寫入，寫入不阻塞讀取，提供極致吞吐"),
            ("Raft 共識演算法", "Leader 選舉 + 日誌複製多數決 (Quorum)，杜絕單點故障與分裂"),
            ("秒級故障自動倒換", "主節點故障時，哨兵/叢集控制器 5 秒內將備援節點提升為新主")
        ]
    },
    "sn-ch07": {
        "formula": "快取偽共享對齊，NUMA本地記憶取；分支預測指令緊，流水線衝最高速。",
        "bullets_left": [
            ("CPU 快取階層 (L1/L2/L3)", "L1 (1ns) -> L2 (4ns) -> L3 (12ns) -> RAM (60ns)，命中率決定一切"),
            ("快取偽共享 (False Sharing)", "不同核心變數共處同一 64-byte Cache Line，互斥無效化癱瘓效能"),
            ("NUMA 親和性存取", "綁定行程於特定 Socket 與本地記憶體節點，避開 QPI/UPI 跨晶片延遲"),
            ("分支預測優化", "使用 __builtin_expect 提示 likely/unlikely，保持 CPU 流水線滿載")
        ],
        "bullets_right": [
            ("循環展開 (Loop Unrolling)", "減少分支跳轉指令，增加指令級並行度 (ILP)"),
            ("靜態鏈結與 LTO", "Link-Time Optimization 跨模組最佳化與函式內聯，指令緊湊化"),
            ("RDTSC 高精準計數器", "直接讀取 CPU 週期暫存器，奈秒級量測撮合函數各階段耗時"),
            ("記憶體對齊 (Memory Alignment)", "資料結構按 8/16/64 bytes 對齊，防止跨 Cache Line 雙重存取")
        ]
    },
    "sn-ch08": {
        "formula": "全閃陣列NVMe，緩存溢位預防先；令牌桶限微突發，隊列監控穩優先。",
        "bullets_left": [
            ("全快閃陣列 (AFA)", "全面採用 NVMe SSD，消除傳統機械硬碟尋道延遲，IOPS 突破百萬"),
            ("NVMe-oF (RoCEv2)", "透過 RDMA 遠端直接記憶體存取存儲陣列，儲存延遲降至微秒級"),
            ("微突發 (Microburst) 衝擊", "開盤 9:00 百倍委託瞬間灌入，導致交換機與網卡環形緩衝區溢位丟包"),
            ("環形緩衝區擴大", "ethtool -G rx 4096，拉大網卡佇列深度，吸收突發封包衝擊")
        ],
        "bullets_right": [
            ("滑動視窗令牌桶", "在下單閘道器實施平滑限流，超量委託排隊微延遲而不直接中斷"),
            ("無失真乙太網 (PFC/ECN)", "Priority-based Flow Control + ECN 顯式壅塞通知，防止佇列丟包"),
            ("記憶體池預分配", "交易啟動時一次性 Malloc 大塊記憶體池，運行期絕不動態釋放/配置"),
            ("非同步落盤架構", "撮合主執行緒僅寫入記憶體 WAL 環形佇列，由獨立 I/O 執行緒負責寫入陣列")
        ]
    },
    "sn-ch09": {
        "formula": "拓撲分佈防單點，親和調度低延遲；無失真網卡直通，水平擴展秒級支。",
        "bullets_left": [
            ("Pod 拓撲分佈約束", "PodTopologySpreadConstraint 確保微服務均勻分散在不同機櫃與節點"),
            ("節點親和性 NodeAffinity", "將撮合周邊模組強制排程至具備 NVMe 與高頻 CPU 之特定實體機"),
            ("SR-IOV / Host-device", "繞過 CNI 軟體虛擬網橋，直接將實體網卡 VF 直通容器，逼近裸機延遲"),
            ("容器資源硬限制 (Guaranteed)", "requests 與 limits 數值完全一致，提升 QoS 等級，防止 OOM 優先被殺")
        ],
        "bullets_right": [
            ("唯讀根檔案系統", "readOnlyRootFilesystem: true，提高容器安全性與不可變性"),
            ("HPA + KEDA 自動擴展", "基於 Kafka 佇列延遲與 CPU 負載，在盤中秒級橫向擴展後端結算 Pod"),
            ("Cilium eBPF CNI", "取代傳統 iptables/kube-proxy，以 eBPF 實現高效能 Pod 路由與轉發"),
            ("平滑終止 (Graceful Shutdown)", "配置 preStop 鉤子與 terminationGracePeriodSeconds，確保交易處理完才退出")
        ]
    },
    "sn-ch10": {
        "formula": "奇數法定防分歧，心跳遺失切電源；隔離故障保資料，高可用性永不倒。",
        "bullets_left": [
            ("叢集腦裂 (Split-Brain)", "心跳中斷導致雙節點皆自認是主節點，同時寫入儲存造成資料毀滅性破壞"),
            ("奇數節點 Quorum", "建立 2N+1 仲裁機制，必須獲得 (N/2 + 1) 以上多數票才能維持運作"),
            ("STONITH 防護機制", "Shoot The Other Node In The Head，確認心跳遺失立刻透過 IPMI 切斷對方電源"),
            ("硬體 Fencing 設備", "網路受控 PDU 電源分配器、SAN Switch 光纖埠遮蔽，徹底隔離死機節點")
        ],
        "bullets_right": [
            ("雙路獨立心跳網路", "一組實體直連心跳線 + 一組管理網路心跳，消除單一交換機誤判"),
            ("Corosync / Pacemaker", "成熟高可用叢集架構，嚴格監控撮合服務虛擬 IP (VIP) 與儲存資源"),
            ("VIP 漂移與 ARP 更新", "主節點切換時發送 Gratuitous ARP，促使全網交換機立即更新 MAC 轉發"),
            ("SDR 共享磁碟鎖定", "使用 SCSI-3 Persistent Reservation (PR) 保證同一時間僅單一節點能掛載寫入")
        ]
    },
    "sn-ch11": {
        "formula": "循序寫入零拷貝，分區平行吞吐高；冪等消費去重複，消息持久不可銷。",
        "bullets_left": [
            ("循序寫入 (Sequential I/O)", "利用作業系統 PageCache 與磁碟循序追加寫入，效能逼近記憶體速度"),
            ("Zero-Copy 零拷貝技術", "利用 sendfile() 系統呼叫，資料直接從 PageCache 拷貝至網卡 Buffer"),
            ("分區 (Partition) 並行架構", "以 Partition 為擴展單元，多消費者群組並行讀取，吞吐破百萬 TPS"),
            ("長輪詢機制 (Long Polling)", "消費者端發起長輪詢拉取 (Pull)，無新訊息時掛起，杜絕空轉輪詢浪費")
        ],
        "bullets_right": [
            ("Exactly-Once (精確一次)", "結合冪等性 Producer 與事務 API，確保網路抖動重傳時絕無重複扣帳"),
            ("ISR (同步副本集合)", "In-Sync Replicas，僅在所有 ISR 節點皆確認收到日誌後方視為寫入成功"),
            ("Compaction 日誌壓縮", "保留特定 Key 的最新狀態值，精簡磁碟容量，支援快速重放復原"),
            ("背壓機制 (Backpressure)", "當下游撮合主機負載過高時，通知上游減速，防止記憶體溢出崩潰")
        ]
    },
    "sn-ch12": {
        "formula": "四個黃金指標看，錯誤預算量化衡；基礎設施即代碼，自動自癒最從容。",
        "bullets_left": [
            ("四大黃金指標 (Four Golden Signals)", "延遲 (Latency)、流量 (Traffic)、錯誤率 (Errors)、飽和度 (Saturation)"),
            ("SLI / SLO / SLA 體系", "服務水準指標 (真實數據) -> 服務水準目標 (內部指標 99.999%) -> 協議 (法律賠付)"),
            ("錯誤預算 (Error Budget)", "衡量系統未達標之容許額度，預算耗盡時全面凍結新功能發布，專注除錯"),
            ("基礎設施即代碼 (IaC)", "使用 Terraform / Ansible 宣告式管理所有伺服器與網路，杜絕雪花機器 (Snowflake)")
        ],
        "bullets_right": [
            ("無指責檢討會 (Blameless Post-mortem)", "聚焦系統設計漏洞與自動化防護缺失，嚴禁個人歸咎文化"),
            ("Prometheus + Alertmanager", "以微秒精度收集節點遙測指標，配置智慧靜音與告警合併策略"),
            ("混沌工程 (Chaos Engineering)", "盤中在預備環境隨機關閉節點或注入網路延遲，驗證自動容災自癒能力"),
            ("自動自癒 (Auto-remediation)", "偵測到程序卡死或記憶體洩漏時，自動執行預設劇本重啟或流量切換")
        ]
    }
}

def inject_memorization_cards(notes_list, mnemonics_dict):
    for item in notes_list:
        nid = item["id"]
        if nid not in mnemonics_dict:
            continue
        m = mnemonics_dict[nid]

        left_html = "".join([f"<li><strong>{k}</strong>：{v}</li>" for k, v in m["bullets_left"]])
        right_html = "".join([f"<li><strong>{k}</strong>：{v}</li>" for k, v in m["bullets_right"]])

        card_html = f"""
<!-- 🧠 核心速記骨幹 · 考試秒殺心法 -->
<div class="quick-memorization-card">
  <div class="memorization-badge">🧠 3 秒核心速記骨幹 · 考試秒殺心法</div>
  <div class="mnemonic-quote">
    「{m["formula"]}」
  </div>
  <div class="mnemonic-breakdown">
    <div class="mnemonic-col">
      <div class="mnemonic-col-title">【⚡ 7秒破題核心拆解】</div>
      <ul>
        {left_html}
      </ul>
    </div>
    <div class="mnemonic-col">
      <div class="mnemonic-col-title">【🎯 關鍵得分指標與參數】</div>
      <ul>
        {right_html}
      </ul>
    </div>
  </div>
</div>
"""
        # If card already present, replace it; else insert after vocab bar or at top
        old_content = item["content"]
        if "quick-memorization-card" in old_content:
            old_content = re.sub(r'<!-- 🧠 核心速記骨幹.*?</div>\s*</div>\s*</div>', '', old_content, flags=re.DOTALL)

        if "</div>\n</div>\n\n<h2>" in old_content:
            new_content = old_content.replace("</div>\n</div>\n\n<h2>", "</div>\n</div>\n" + card_html + "\n<h2>", 1)
        elif "</div>\n</div>" in old_content:
            new_content = old_content.replace("</div>\n</div>", "</div>\n</div>\n" + card_html, 1)
        else:
            new_content = card_html + "\n" + old_content

        item["content"] = new_content

def process_file(file_path, var_name, mnemonics_dict):
    full_path = os.path.normpath(os.path.join(CURRENT_DIR, "..", "assets", file_path))
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract JSON array by bracket indices
    start = content.find('[')
    end = content.rfind(']') + 1
    if start == -1 or end == 0:
        print(f"Failed to find bracket range in {file_path}")
        return

    data = json.loads(content[start:end])
    inject_memorization_cards(data, mnemonics_dict)

    header = f"/**\n * 臺灣證券交易所 (TWSE) 招募備考講義 - {var_name}\n * 內建【🧠 3 秒核心速記骨幹 · 考試秒殺心法】快速記憶卡\n */\n\nconst {var_name} = "
    footer = f";\n\nwindow.{var_name} = {var_name};\n"

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(header + json.dumps(data, ensure_ascii=False, indent=2) + footer)

    print(f"Successfully enriched {file_path} with rapid memorization blueprints!")

if __name__ == "__main__":
    process_file("notes-sec.js", "NOTES_SEC", SEC_MNEMONICS)
    process_file("notes-sysnet.js", "NOTES_SYSNET", SYSNET_MNEMONICS)
