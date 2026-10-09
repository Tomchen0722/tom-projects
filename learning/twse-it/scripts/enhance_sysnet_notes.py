# -*- coding: utf-8 -*-
"""
Enhance TWSE SysNet Notes with:
- Chapter vocabulary bars with pronunciation pills
- High-probability TWSE Exam Predictions for each chapter (以系統網路管理為輔)
- Export to window.NOTES_SYSNET
"""
import os
import json
import importlib.util

spec = importlib.util.spec_from_file_location('bsn', 'learning/twse-it/scripts/build_sysnet_notes.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
notes = mod.get_sysnet_notes()

sysnet_meta = {
    "sn-ch01": {
        "vocab": [
            ("Continuous Trading", "逐筆撮合機制"),
            ("Kernel Bypass", "核心旁路技術"),
            ("Data Plane Development Kit", "DPDK 封包加速套件"),
            ("Solarflare Onload", "Onload 網路加速堆疊"),
            ("Poll Mode Driver", "輪詢模式驅動 (PMD)"),
            ("NUMA Affinity", "非均勻記憶體親和性"),
            ("HugePages", "巨型分頁機制")
        ],
        "prediction_title": "【系統網路核心題】金融極致超低延遲逐筆撮合架構規劃與 Linux 核心最佳化",
        "question": "臺灣證券交易所（TWSE）全面推動逐筆撮合（Continuous Trading），對於訂單處理往返延遲（Round-Trip Latency）之要求已進入微秒（µs）級別。請分析傳統 Linux 作業系統網路通訊架構之主要延遲瓶頸，並詳述如何運用 Kernel Bypass 技術與作業系統底層調校策略，建構高吞吐、微秒級之撮合引擎執行環境？（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>傳統 Linux 網路瓶頸（7分）</strong>：環境切換（Context Switch）、網卡硬體/軟體中斷（IRQ）打斷管線、多次記憶體拷貝。<br>2. <strong>Kernel Bypass 核心旁路（9分）</strong>：DPDK PMD 使用者空間純輪詢網卡 RX 環、Solarflare Onload 相容 BSD Socket 免改代碼、零拷貝（Zero-Copy）將延遲壓制至 1.2µs 內。<br>3. <strong>OS 底層深度調校（9分）</strong>：CPU 隔離（isolcpus、nohz_full）、NUMA 節點親和性綁定消除 QPI 總線延遲、1GB 靜態 HugePages 消除 TLB Miss、alignas(64) 消除快取偽共享。"
    },
    "sn-ch02": {
        "vocab": [
            ("Multicast Market Data", "多點廣播行情推播"),
            ("Source-Specific Multicast", "指定來源群播 (PIM-SSM)"),
            ("Spine-Leaf Architecture", "脊葉網路架構"),
            ("Microburst", "瞬時流量微突發"),
            ("Equal-Cost Multi-Path", "等價多路徑路由 (ECMP)"),
            ("Cut-Through Switching", "直通轉發模式")
        ],
        "prediction_title": "【系統網路核心題】UDP 群播行情推播、Spine-Leaf CLOS 拓撲與交換器微突發防禦",
        "question": "臺灣證券交易所每日產出海量逐筆成交與五檔委託行情資訊，必須即時、公平且低延遲地推播至全臺數百家證券商。請說明證交所為何採用 UDP Multicast 作為行情推播協定？試述 PIM-SSM 與 IGMPv3 在此架構下的運作原理，並針對開盤瞬時流量微突發（Microburst）提出交換器端之防禦與調校對策。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>UDP Multicast 優勢（8分）</strong>：出口負載恆定（交換器線速複製）、微秒級絕對公平性、Feed A/B 雙路廣播與券商端 Arbiter 雙收仲裁。<br>2. <strong>PIM-SSM 與 IGMPv3 原理（8分）</strong>：券商以 IGMPv3 報告指定 (S, G)，建立最優最短路徑樹（SPT），摒棄單點故障之 RP 集合點。<br>3. <strong>微突發交換器調校（9分）</strong>：動態共用緩衝區（Dynamic Shared Buffer Alpha Tuning）、Cut-Through 直通轉發模式降低延遲至 300ns、ECN 顯式擁塞通知平滑發送速率。"
    },
    "sn-ch03": {
        "vocab": [
            ("Precision Time Protocol", "精確時間協定 (PTP)"),
            ("Grandmaster Clock", "主時鐘源 (GM)"),
            ("Boundary Clock", "邊界時鐘 (BC)"),
            ("Transparent Clock", "透明時鐘 (TC)"),
            ("Hardware Timestamping", "硬體時間戳記"),
            ("MiFID II RTS 25", "金融時序監理規範")
        ],
        "prediction_title": "【系統網路核心題】IEEE 1588v2 PTP 奈秒同步原理、時鐘架構與 MiFID II 監理規範",
        "question": "在逐筆撮合與高頻交易環境中，時間戳記精度攸關撮合成交之絕對公平性。試比較 NTP 與 IEEE 1588v2 PTP 協定之精度差異與打標機制；推導 PTP 雙向時間偏移計算公式；並依據國際金融 MiFID II (RTS 25) 規範，說明對高頻交易系統時間同步與最大偏差之嚴苛要求。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>NTP vs PTP 對照（8分）</strong>：NTP 為軟體層打標毫秒級 (1~50ms)；PTP 為網卡 PHY/MAC 硬體打標奈秒級 (10~100ns)。<br>2. <strong>PTP 四時間戳記推導（9分）</strong>：寫出 Sync 與 Delay_Req 封包之 t1, t2, t3, t4，單向延遲 Delay = [(t4-t1)-(t3-t2)]/2，時間偏差 Offset = [(t2-t1)-(t4-t3)]/2。<br>3. <strong>MiFID II RTS 25 規範與架構（8分）</strong>：時間戳記精度達 100µs 內、與 UTC 最大允許偏差不得超過 1µs；機房建置 Grandmaster 原子鐘/GPS、交換器啟用 Boundary Clock (BC) 防止抖動。"
    },
    "sn-ch04": {
        "vocab": [
            ("Completely Fair Scheduler", "完全公平排程器 (CFS)"),
            ("Real-Time Scheduling", "即時排程 (SCHED_FIFO)"),
            ("Translation Lookaside Buffer", "轉譯後備緩衝區 (TLB)"),
            ("Shared Memory", "POSIX 共享記憶體"),
            ("Unix Domain Socket", "Unix 域通訊端"),
            ("Inter-Process Communication", "行程間通訊 (IPC)")
        ],
        "prediction_title": "【系統網路核心題】Linux CFS 排程機制、SCHED_FIFO 即時調度與 IPC 延遲剖析",
        "question": "請分析 Linux 預設 CFS（完全公平排程器）之紅黑樹底層調度原理及其在金融微秒級撮合情境下產生之延遲抖動瓶頸；說明為何撮合引擎需切換至 SCHED_FIFO 即時排程；並比較 POSIX 共享記憶體、Unix Domain Socket 與 TCP Loopback 在 IPC 傳輸延遲與記憶體拷貝次數之差異。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>CFS 紅黑樹原理與抖動（8分）</strong>：以 vruntime 排隊，休眠喚醒仍需計算排程樹節點，帶來 20~50µs 長尾延遲。<br>2. <strong>SCHED_FIFO 即時排程（8分）</strong>：靜態優先權 99，撮合行程獨佔 CPU，永不被核心排程器主動中斷搶占，徹底消除排程抖動。<br>3. <strong>IPC 評比表（9分）</strong>：POSIX 共享記憶體（零拷貝、<0.1µs 納秒級）最適合撮合與行情通信；Unix Domain Socket 1 次拷貝 1.5~3.5µs；TCP Loopback 經網路堆疊 2 次拷貝 8~20µs 嚴禁於熱路徑使用。"
    },
    "sn-ch05": {
        "vocab": [
            ("Nagle Algorithm", "Nagle 緩衝演算法"),
            ("Busy Polling", "核心忙輪詢 (SO_BUSY_POLL)"),
            ("I/O Multiplexing", "I/O 多工模型"),
            ("Edge-Triggered", "邊緣觸發模式 (epoll ET)"),
            ("Extended BPF", "延伸式封包過濾 (eBPF)"),
            ("Delayed ACK", "延遲確認機制")
        ],
        "prediction_title": "【系統網路核心題】TCP 延遲參數最佳化、Linux epoll ET 多工與 eBPF 性能觀測",
        "question": "在券商下單通訊閘道（Gateway）架構中，請說明 TCP_NODELAY 為何能避免 Nagle 演算法與 Delayed ACK 產生之 40ms 延遲死鎖；闡明 Linux epoll 紅黑樹與就緒佇列架構及其在 ET（邊緣觸發）模式下配合非阻塞 I/O 之實作要點；並說明如何運用 eBPF 工具鏈進行微秒級核心延遲排查。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>Nagle 與 Delayed ACK 延遲死鎖（8分）</strong>：Nagle 緩存小封包湊滿 MSS，遇接收端延遲確認導致 40ms~200ms 等待；TCP_NODELAY 立即發送。<br>2. <strong>epoll ET 邊緣觸發實作（9分）</strong>：紅黑樹管理 fd、雙向就緒鏈表 O(1) 返回；ET 僅狀態改變通知一次，配合非阻塞 I/O 迴圈讀取至 EAGAIN/EWOULDBLOCK。<br>3. <strong>eBPF 核心觀測（8分）</strong>：kprobe/kretprobe 動態掛載 tcp_v4_rcv，使用 bpftrace tcprtt 測量往返耗時，零侵入性替代高開銷之 strace。"
    },
    "sn-ch06": {
        "vocab": [
            ("Write-Ahead Logging", "預寫日誌 (WAL)"),
            ("Multi-Version Concurrency Control", "多版本並行控制 (MVCC)"),
            ("Active-Active Replication", "同城雙活容災架構"),
            ("Two-Phase Commit", "兩階段提交 (2PC)"),
            ("Quorum Consensus", "多數決共識演算法"),
            ("InnoDB Locking", "記錄鎖與間隙鎖")
        ],
        "prediction_title": "【系統網路核心題】資料庫 ACID 保證、WAL/MVCC 底層機制與同城雙活容災架構",
        "question": "證券帳務與結算系統要求資料庫具備絕對的 ACID 交易保證與零資料遺失能力。試從資料庫核心原理說明 WAL（Write-Ahead Logging）與 MVCC 如何協同保障交易之原子性、隔離性與持久性；並針對臺灣證券交易所之容災要求，規劃一套具備 RPO=0、RTO≤10分鐘之同城雙活（Active-Active）資料庫容災架構。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>ACID 與 WAL/MVCC 實現（9分）</strong>：Undo Log 保障原子性與回滾；WAL ARIES 保障持久性（Redo Log 先循序 fsync 方可回寫髒頁）；MVCC ReadView 消除讀寫阻塞。<br>2. <strong>同城雙活物理傳輸（8分）</strong>：主備機房鋪設專用實體暗光纖（Dark Fiber），單向延遲 < 1ms（距離 < 30km）。<br>3. <strong>共識與分散式事務（8分）</strong>：採用 Raft / Paxos 多副本 Quorum 多數決，日誌同步寫入過半節點即可提交，單機房全毀自動無感選主；跨庫交易採 2PC 兩階段提交。"
    },
    "sn-ch07": {
        "vocab": [
            ("Instruction Pipelining", "指令管線化"),
            ("Branch Prediction", "分支預測器"),
            ("Cache Coherence", "快取一致性協定 (MESI)"),
            ("False Sharing", "快取偽共享"),
            ("Memory Barrier", "記憶體屏障"),
            ("NVMe over Fabrics", "NVMe 光纖網路 (NVMe-oF)")
        ],
        "prediction_title": "【系統網路核心題】伺服器 CPU 超純量架構、MESI 快取一致性與快取偽共享消除",
        "question": "試分析現代 x86_64 CPU 之指令管線化與分支預測失敗對金融撮合熱路徑延遲之衝擊；詳述 MESI 快取一致性協定之四種狀態；並說明多執行緒並行時「快取偽共享（False Sharing）」之成因與 C/C++ 核心資料結構之 64-byte 對齊防護手法。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>管線化與分支預測（8分）</strong>：分支預測失敗引發 Pipeline Flush 清空管線，浪費 15~20 週期；撮合代碼採用 likely()/unlikely() 優化編譯路徑。<br>2. <strong>MESI 協定四狀態（8分）</strong>：Modified（已修改未回寫）、Exclusive（獨佔且與內存一致）、Shared（共享）、Invalid（無效）。<br>3. <strong>False Sharing 消除（9分）</strong>：多核寫入位於同一個 64-byte Cache Line 的不同變數引發總線無效化風暴；使用 alignas(64) 或 padding 填充實體對齊。"
    },
    "sn-ch08": {
        "vocab": [
            ("All-Flash Array", "全快閃儲存陣列 (AFA)"),
            ("Symmetrix Remote Data Facility", "同步遠端鏡像 (SRDF)"),
            ("Fibre Channel SAN", "光纖通道儲存網路"),
            ("Deduplication and Compression", "重複資料刪除與壓縮"),
            ("Immutable Storage", "不可變 WORM 存儲"),
            ("Multipath I/O", "多路徑 I/O")
        ],
        "prediction_title": "【系統網路核心題】金融級全快閃陣列 AFA、同步遠端鏡像 SRDF 與 WORM 存儲",
        "question": "金融核心帳務對儲存子系統要求微秒級穩態 I/O 與零資料遺失。試說明全快閃儲存陣列（AFA）架構特性；比較同步遠端鏡像（SRDF/S）與非同步鏡像（SRDF/A）在 RPO、RTO 及網路延遲之取捨；並闡述如何結合 WORM 儲存防範勒索軟體破壞。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>AFA 企業儲存架構（8分）</strong>：NVMe 固態磁碟、雙主控制器主動主動（Active-Active）、在線去重與壓縮、FC SAN 雙光纖交換器多路徑。<br>2. <strong>SRDF/S vs SRDF/A 對比（9分）</strong>：SRDF/S 寫入等待遠端 ACK 保證 RPO=0，受光纖延遲限制（同城 < 30km）；SRDF/A 異步傳輸無延遲懲罰但有微小 RPO 差距，適用異地防天災。<br>3. <strong>WORM 不可竄改機制（8分）</strong>：Write Once Read Many，磁碟底層微碼鎖死檔案，任何特權帳號均無法在保留期內修改或刪除，防範勒索軟體惡意破壞。"
    },
    "sn-ch09": {
        "vocab": [
            ("Control Groups", "控制群組 (cgroups)"),
            ("Linux Namespaces", "名稱空間隔離"),
            ("Container Network Interface", "容器網路介面 (CNI)"),
            ("Single Root I/O Virtualization", "單根虛擬化 (SR-IOV)"),
            ("Kubernetes Scheduler", "K8s 排程器"),
            ("Site Reliability Engineering", "網站可靠性工程 (SRE)")
        ],
        "prediction_title": "【系統網路核心題】Linux 容器核心隔離機制、K8s 排程演算法與 SR-IOV 高性能網路",
        "question": "試從 Linux 核心機制說明 cgroups 與 Namespaces 如何實現容器之資源限制與環境隔離；分析在金融超低延遲撮合情境下，傳統 K8s Overlay 網路（如 Flannel/VXLAN）之性能瓶頸，並說明 SR-IOV 與 Host-Network 如何達成接近裸機之網路效能。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>cgroups 與 Namespaces 原理（8分）</strong>：cgroups 限制 CPU、RAM、Block I/O 配額；Namespaces 隔離 pid、net、ipc、mnt、uts、user 檢視。<br>2. <strong>Overlay 網路封裝延遲（8分）</strong>：VXLAN 封裝增加 50-byte 標頭、CPU 額外加解密負載、MTU 碎片化引入數十微秒延遲。<br>3. <strong>SR-IOV 硬體直通（9分）</strong>：將物理網卡切分為數十個 Virtual Function (VF) 直通容器 Pod，繞過虛擬網橋與主機核心網路棧，達成裸機級次微秒傳輸。"
    },
    "sn-ch10": {
        "vocab": [
            ("Virtual Router Redundancy Protocol", "虛擬路由器備援協定 (VRRP)"),
            ("Cluster Resource Manager", "叢集資源管理器 (Pacemaker)"),
            ("Split-Brain Syndrome", "叢集腦裂症候群"),
            ("STONITH", "爆頭強制斷電機制 (STONITH)"),
            ("Direct Routing Mode", "直接路由模式 (LVS-DR)"),
            ("BGP Anycast Routing", "任播路由負載平衡")
        ],
        "prediction_title": "【系統網路核心題】高可用叢集架構、腦裂成因與 STONITH 爆頭機制防禦",
        "question": "在證交所關鍵高可用系統中，試說明 Keepalived VRRP 與 Pacemaker/Corosync 之架構差異；詳細分析高可用叢集發生「腦裂（Split-Brain）」之成因與危害，並闡明 STONITH 機制如何透過 IPMI/iDRAC 帶外硬體控制徹底防範資料覆蓋損毀。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>VRRP vs Pacemaker 對比（8分）</strong>：Keepalived 專注 VIP 漂移（適合無狀態服務）；Pacemaker+Corosync 提供 Totem 令牌環心跳、Quorum 多數決與複雜資源狀態調度。<br>2. <strong>腦裂危害（8分）</strong>：心跳中斷但節點皆存活，雙方皆誤認對方死亡同時掛載共享磁碟或爭搶寫入，引發嚴重的資料覆蓋損壞。<br>3. <strong>STONITH 物理斷電（9分）</strong>：Shoot The Other Node In The Head，合法獲得 Quorum 節點透過 IPMI 帶外管理強制切斷失聯節點電源，確定對方死透後方接管業務。"
    },
    "sn-ch11": {
        "vocab": [
            ("Financial Information eXchange", "金融資訊交換協定 (FIX)"),
            ("Message Sequence Number", "訊息序號 (MsgSeqNum)"),
            ("Append-Only Log", "順序追加日誌"),
            ("Zero-Copy Sendfile", "零拷貝發送機制"),
            ("In-Sync Replicas", "同步副本集合 (ISR)"),
            ("Idempotent Producer", "冪等生產者")
        ],
        "prediction_title": "【系統網路核心題】FIX 協定會話管理、Kafka 零拷貝循序日誌與 Exactly-Once 保證",
        "question": "證券期貨下單廣泛採用 FIX 協定，後台日誌管線則依賴 Kafka。試說明 FIX 協定 Session 層如何運用 MsgSeqNum 與 ResendRequest 保證訊息不脫序與不遺失；闡述 Kafka 如何利用 Linux 零拷貝（sendfile）與順序追加寫入達成百萬級吞吐；並說明 Exactly-Once 交付語意之實現架構。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>FIX 協定會話層保證（8分）</strong>：雙向連續 MsgSeqNum，心跳（Heartbeat）維持連線，偵測序號斷層（Gap）立即發出 35=2 ResendRequest 重傳。<br>2. <strong>Kafka 循序日誌與零拷貝（9分）</strong>：Append-only 循序寫入磁碟逼近 RAM 速度；Linux sendfile() 系統呼叫資料直接自 Page Cache 經 DMA 送至網卡，繞過 JVM 使用者空間。<br>3. <strong>Exactly-Once 實現（8分）</strong>：生產端分配 PID 與 Sequence Number（冪等生產者）；消費端搭配資料庫唯一事務鍵（Idempotency Key），防範重試重複記帳。"
    },
    "sn-ch12": {
        "vocab": [
            ("Infrastructure as Code", "基礎設施即代碼 (IaC)"),
            ("Idempotency", "冪等性原理"),
            ("Chaos Engineering", "混沌工程"),
            ("Core Dump", "核心轉儲映像"),
            ("Post-Mortem Debugging", "事後故障診斷"),
            ("Service Level Objective", "服務水準目標 (SLO)")
        ],
        "prediction_title": "【系統網路核心題】Ansible 自動化冪等維運、混沌工程演練與 GDB Core Dump 故障診斷",
        "question": "金融生產環境要求 99.999% 高可用。請說明 Ansible 自動化維運之「冪等性（Idempotency）」原理與 GitOps 雙人審核實踐；闡述混沌工程（Chaos Engineering）在離峰演練時如何主動注入故障以驗證容災韌性；並展示當 Linux 生產撮合進程崩潰時，如何運用 Core Dump 與 GDB 進行事後堆疊追蹤排查。（配分：25分）",
        "tips": "<strong>🎯 評分踩點與核心要點</strong>：<br>1. <strong>Ansible 冪等性與 GitOps（8分）</strong>：反覆執行 Playbook 保證目標狀態恆定；配置變更託管於 Git 庫，PR 雙人審查審計軌跡。<br>2. <strong>混沌工程故障注入（8分）</strong>：主動注入網卡隨機丟包/延遲、隨機 kill 資料庫進程、模擬 CPU 100% 飽和，驗證 VIP 漂移與熔斷降級機制。<br>3. <strong>Core Dump 與 GDB 診斷（9分）</strong>：配置 ulimit -c unlimited 與 core_pattern；使用 gdb ./binary core.dump 執行 bt full 印出崩潰呼叫堆疊，thread apply all bt 偵測死鎖狀態。"
    }
}

new_notes = []
for n in notes:
    nid = n["id"]
    meta = sysnet_meta.get(nid)
    if not meta:
        new_notes.append(n)
        continue
    
    # Build vocabulary bar
    vocab_html = '<div class="chapter-vocab-bar">\n  <div class="vocab-bar-title">🎧 本章高頻英文術語發音（點擊即可聆聽真人語音）：</div>\n  <div class="vocab-items">\n'
    for term, zh in meta["vocab"]:
        vocab_html += f'    <button type="button" class="vocab-pill" onclick="speakEn(\'{term}\', this)">{term} 🔊</button>\n'
    vocab_html += '  </div>\n</div>\n\n'
    
    # Build prediction box
    pred_html = f"""
<div class="exam-prediction-box">
  <span class="prediction-badge">🎯 臺灣證交所年度核心猜題與考點剖析（系統網路管理為輔）</span>
  <h4 style="margin:0.5rem 0; color:var(--accent-primary);">{meta['prediction_title']}</h4>
  <p><strong>題目</strong>：{meta['question']}</p>
  <div class="essay-examiner-tips">
    {meta['tips']}
  </div>
</div>
"""
    # Combine content
    orig_content = n["content"]
    combined_content = vocab_html + orig_content.strip() + "\n" + pred_html
    
    new_n = {
        "id": n["id"],
        "chapter": n["chapter"],
        "title": n["title"],
        "summary": n["summary"],
        "content": combined_content
    }
    new_notes.append(new_n)

# Write to assets/notes-sysnet.js
output_path = 'learning/twse-it/assets/notes-sysnet.js'
js_content = """/**
 * 臺灣證券交易所 (TWSE) 招募備考講義 - 系統與網路管理人員 (計算機概論)
 * 完整涵蓋 12 大深入核心單元（超低延遲、網路拓撲、PTP、Linux 核心、資料庫雙活、儲存架構、K8s、叢集高可用、FIX/Kafka、SRE）
 * 每一章節均深度收錄：核心底層原理、實務配置要點、技術對照矩陣、雙語術語發音、以及【🎯 臺灣證交所年度核心猜題與考點剖析（系統網路為輔）】
 */

const NOTES_SYSNET = """ + json.dumps(new_notes, ensure_ascii=False, indent=2) + """;

// 關鍵導出：確保附掛於全局 window 物件以利跨腳本存取
window.NOTES_SYSNET = NOTES_SYSNET;
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {output_path} with {len(new_notes)} chapters!")
