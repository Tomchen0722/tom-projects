# -*- coding: utf-8 -*-
"""
14 Unique, Deep, High-Scoring System & Network Management Essays for TWSE IT Exam
IDs: sn-essay-33 to sn-essay-46
Replaces previous generic template loops with comprehensive, domain-grounded model answers.
"""

def get_sysnet_essays_33_to_46():
    return [
        # sn-essay-33: io_uring vs epoll
        {
            "id": "sn-essay-33",
            "category": "sysnet",
            "chapter": "第 1 章：撮合核心與超低延遲系統架構（Kernel Bypass 與記憶體優化）",
            "title": "超低延遲撮合：Linux 6.x io_uring 與傳統 epoll/select 在下單閘道器（Gateway）之效能評估與架構設計",
            "summary": "深入解構 Linux 6.x io_uring 提交佇列（SQ）與完成佇列（CQ）無鎖環形緩衝區架構、IORING_SETUP_SQPOLL 核心執行緒輪詢、Registered Buffers 零拷貝機制，以及在下單閘道器消除 Syscall 開銷之實務規劃。",
            "points": 25,
            "rubric": "1. 傳統 epoll/select 在百萬級 IOPS 下 Syscall 與上下文切換瓶頸 (6分)；2. io_uring 雙環形佇列（SQ/CQ）共享記憶體運作原理 (7分)；3. IORING_SETUP_SQPOLL 與 Registered Buffers 零系統呼叫架構 (7分)；4. 證券下單閘道器效能延遲（P99/P99.99）實務結論 (5分)",
            "question": "證券下單閘道器（Order Gateway）必須每秒處理數萬筆來自券商之 FIX / 二進位下單報文。傳統基於 Linux epoll 之事件驅動架構在百萬級 IOPS 下面臨頻繁系統呼叫（Syscall）帶來的 CPU 上下文切換與快取抖動。試申論：(1) 傳統 `epoll_wait` + `read`/`write` 模型之系統呼叫開銷與 Spectre/Meltdown 緩解措施帶來的額外延遲懲罰；(2) Linux 6.x `io_uring` 架構原理：Submission Queue（SQ）與 Completion Queue（CQ）共享記憶體環形緩衝區無鎖運作；(3) 啟用 `IORING_SETUP_SQPOLL`（核心輪詢執行緒）與 Registered Buffers 達成「完全零系統呼叫（Zero-Syscall）」與「零拷貝」之極致下單閘道器架構；(4) 生產環境下 epoll 與 io_uring 在延遲分佈（P99 / P99.99）與 CPU 資源耗用之基準對比。",
            "modelAnswer": r"""
<h4>一、破題：下單閘道器 I/O 吞吐瓶頸與系統呼叫代價</h4>
<p>在逐筆撮合與高頻交易環境中，下單閘道器（Order Gateway）是券商訂單進入交易所核心之第一站。傳統 Linux 高效能網路程式設計長達二十年以 <code>epoll</code> 為標準。然而，每次處理網路 I/O，程式必須在使用者空間（User Space）與核心空間（Kernel Space）之間來回切換。在百萬級 IOPS 下，<strong>CPU 上下文切換（Context Switch）、TLB 刷新以及 Spectre/Meltdown 核心頁表隔離（KPTI）</strong>帶來高達數百奈秒之額外懲罰。<strong>Linux 6.x io_uring</strong> 之問世，徹底改寫了非同步 I/O 之遊戲規則。</p>

<h4>二、傳統 epoll 模型於微秒撮合之物理極限</h4>
<ol>
  <li><strong>雙重 Syscall 開銷</strong>：epoll 模型中，主迴圈先呼叫 <code>epoll_wait()</code> 捕獲就緒事件，隨後對每個 Socket 呼叫 <code>read()</code> 或 <code>write()</code> 進行資料搬移。單一請求至少經歷 2 次系統呼叫。每次 Syscall 在現代 x86 CPU 上因 KPTI 增加 100~300ns 開銷。</li>
  <li><strong>快取污染（Cache Trashing）</strong>：頻繁陷入核心導致 CPU L1/L2 快取行被核心代碼覆蓋，使用者空間解析訂單報文時頻繁遭遇 Cache Miss。</li>
  <li><strong>無法處理磁碟 I/O</strong>：Linux AIO 僅支援 `O_DIRECT` 磁碟檔案，無法統一下單網路 Socket 與磁碟持久化 WAL 日誌。</li>
</ol>

<h4>三、io_uring 核心機制：SQ/CQ 雙環形緩衝區架構</h4>
<pre><code class="language-text">  [使用者空間 (User Space)]
       │ (透過 mmap 共享記憶體無鎖寫入)
       ├──> [Submission Queue (SQ) 環形佇列] ──> [SQE 提交項目]
       │                                             │
       │                                             ▼ (核心直接消費)
  ═════╪═══════════════════════════════════════════════════════════════
       │                                    [Linux 6.x 核心處理引擎]
       │                                             │
       │ (透過 mmap 共享記憶體無鎖讀取)               ▼ (完成事件回填)
       └──< [Completion Queue (CQ) 環形佇列] <── [CQE 完成項目]
  [使用者空間 (User Space)]</code></pre>
<ul>
  <li><strong>mmap 共享記憶體零拷貝佇列</strong>：核心與使用者空間共享兩組無鎖環形緩衝區——<strong>提交佇列（Submission Queue, SQ）</strong>與<strong>完成佇列（Completion Queue, CQ）</strong>。使用者程式填充 SQE，核心完成 I/O 後回填 CQE，雙方皆以原子記憶體指標操作，徹底免除資料跨空間複製。</li>
  <li><strong>批量提交（Batching）</strong>：單次 <code>io_uring_enter()</code> 可同時提交數十筆下單 Socket 讀寫請求，大幅均攤 Syscall 成本。</li>
</ul>

<h4>四、極致優化：SQPOLL 與 Registered Buffers 零 Syscall 落地</h4>
<p>針對證交所關鍵下單通道之終極配置：</p>
<ol>
  <li><strong>啟用 `IORING_SETUP_SQPOLL`（核心輪詢執行緒）</strong>：
    <ul>
      <li>核心在底層專門啟動一個核心執行緒（Kernel Polling Thread），持續輪詢 SQ 佇列。</li>
      <li>使用者空間下單程式只需將委託單放入 SQ，核心執行緒立刻在背景取走執行，<strong>下單傳輸全程「0 次 Syscall」</strong>，達到真正的純記憶體無感通訊。</li>
    </ul>
  </li>
  <li><strong>註冊固定緩衝區（Registered Buffers, `IORING_REGISTER_BUFFERS`）</strong>：
    <ul>
      <li>在系統啟動時，預先將下單接收緩衝區固定並鎖定於實體記憶體（`mlock`）。核心預先完成虛擬位址至實體位址（page pinning）映射，後續 I/O 操作直接進行 DMA，免除每次 I/O 之分頁映射開銷。</li>
    </ul>
  </li>
  <li><strong>註冊固定檔案描述子（Fixed Files, `IORING_REGISTER_FILES`）</strong>：
    <ul>
      <li>預先將長期連線之券商 Socket 註冊至核心陣列，消除核心在 `fget()` / `fput()` 檔案描述子原子計數鎖之爭用。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：延遲分佈對比與 SRE 最佳實務</h4>
<p>在生產基準測試中，面對 200,000 IOPS 之高頻壓力，<strong>io_uring 相較於傳統 epoll 可降低 CPU 使用率 30% 以上，並將 P99.99 長尾延遲由 45 微秒大幅壓降至 8 微秒以內</strong>。證交所下單閘道器全面導入 io_uring，結合 CPU 核心隔離（`isolcpus`），成功為我國資本市場建構具備確定性延遲保證之超高效能網路基石。</p>
            """,
            "examinerTips": "得分關鍵詞：『epoll Syscall 開銷與 KPTI 緩解措施』、『io_uring SQ/CQ 雙環形共享記憶體佇列』、『mmap 零拷貝通訊』、『IORING_SETUP_SQPOLL 達成零系統呼叫 Zero-Syscall』、『Registered Buffers 與 Fixed Files 消除鎖爭用』、『P99.99 尾端延遲由 45μs 降至 8μs』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>epoll 瓶頸剖析（6分）</strong>：深入辨析系統呼叫陷入、KPTI 延遲懲罰及快取污染之物理根因。</li>
  <li><strong>io_uring 核心架構（7分）</strong>：繪製清晰 ASCII 共享記憶體架構圖，闡明 SQ/CQ 環形無鎖運作。</li>
  <li><strong>SQPOLL 與註冊優化（7分）</strong>：精準說明核心輪詢執行緒、固定緩衝區與免除 page pinning 原理。</li>
  <li><strong>延遲對比與結論（5分）</strong>：提出 P99.99 延遲由 45μs 降至 8μs 之量化指標與 SRE 實踐。</li>
</ul>
            """
        },

        # sn-essay-34: SR-IOV + DPDK
        {
            "id": "sn-essay-34",
            "category": "sysnet",
            "chapter": "第 1 章：撮合核心與超低延遲系統架構（Kernel Bypass 與記憶體優化）",
            "title": "網路虛擬化硬體加速：SR-IOV 與 DPDK 結合在證券期貨下單與多播行情主機之優化策略",
            "summary": "剖析 PCIe 單根 I/O 虛擬化（SR-IOV）之實體功能（PF）與虛擬功能（VF）硬體切分、結合 DPDK Poll Mode Driver（PMD）旁路 Linux 核心網路堆疊，消除中斷與上下文切換之極致延遲架構。",
            "points": 25,
            "rubric": "1. 虛擬交換機（vSwitch/Linux Bridge）在金融低延遲環境之缺陷 (6分)；2. PCIe SR-IOV 實體功能（PF）與虛擬功能（VF）硬體直通技術 (7分)；3. DPDK PMD 輪詢驅動、巨頁（HugePages）與 Kernel Bypass 整合 (7分)；4. 多播行情接收零丟包與 NUMA 親和調校實務結論 (5分)",
            "question": "證券交易所於現代私有雲或容器環境部署服務時，傳統虛擬交換機（如 Linux Bridge, OVS）因封包複製與軟體轉發產生數十微秒之延遲抖動。試申論：(1) PCIe 單根 I/O 虛擬化（SR-IOV）技術原理：實體功能（Physical Function, PF）與虛擬功能（Virtual Function, VF）之硬體虛擬化切分；(2) DPDK（Data Plane Development Kit）PMD（Poll Mode Driver）如何直接接管 SR-IOV VF 網卡，繞過 Linux 核心網路堆疊（Kernel Bypass）；(3) 結合 HugePages（1GB 巨頁）鎖定實體記憶體消除 TLB Miss 與 NUMA 本地化配置之微秒級通訊設計；(4) 行情多播（Multicast UDP）接收主機在開盤微突發下，如何透過 SR-IOV + DPDK 消除封包丟失（Zero-Packet-Drop）。",
            "modelAnswer": r"""
<h4>一、破題：虛擬化便利性與微秒延遲之物理矛盾</h4>
<p>金融機構積極推動基礎設施私有雲化與容器化以增進維運彈性。然而，傳統虛擬化網路（如 VMware vSwitch、Linux Bridge、Open vSwitch）依賴 Hypervisor 軟體轉發封包，封包需經歷虛擬化層中斷轉發、記憶體多次拷貝（Memory Copy），帶來高達 20~50 微秒的延遲與嚴重抖動。要讓虛擬化環境達到<strong>「媲美裸機（Bare-metal）之次微秒級效能」</strong>，必須將<strong>「SR-IOV 硬體直通」</strong>與<strong>「DPDK 核心旁路」</strong>強強聯手。</p>

<h4>二、PCIe SR-IOV 硬體虛擬化切分技術</h4>
<ol>
  <li><strong>SR-IOV 核心概念（Single Root I/O Virtualization）</strong>：PCI-SIG 制定的硬體標準，允許單一實體 PCIe 網卡在硬體層級模擬出多個獨立的虛擬網卡。</li>
  <li><strong>PF 與 VF 職責劃分</strong>：
    <ul>
      <li><strong>實體功能（Physical Function, PF）</strong>：具備完整 PCIe 配置空間之主通道，由宿主機（Host OS）管理，負責實體網卡全局鏈路狀態、巨型影格（Jumbo Frame）與韌體配置。</li>
      <li><strong>虛擬功能（Virtual Function, VF）</strong>：輕量化之虛擬 PCIe 裝置，硬體直接提供獨立的 TX/RX 環形佇列、DMA 引擎與中斷信號。宿主機可將 VF 透過 <code>VFIO / PCI-Passthrough</code> 繞過 Hypervisor，直接直通分配給單一虛擬機或容器。</li>
    </ul>
  </li>
  <li><strong>消除軟體轉發開銷</strong>：封包進出網卡由網卡硬體 ASIC 晶片內建之 L2 轉發引擎直接分派給目標 VF，<strong>完全不消耗 Host CPU</strong>，消除 vSwitch 之延遲。</li>
</ol>

<h4>三、DPDK PMD 輪詢與核心旁路（Kernel Bypass）整合</h4>
<pre><code class="language-text">  [實體 100GbE 網卡] ── (PCIe 硬體直通) ──> [SR-IOV 虛擬功能 VF]
                                                    │ (DMA 直接寫入)
                                                    ▼
  ┌────────────────────────────────────────────────────────┐
  │ 使用者空間 (User Space)                                │
  │   ├── DPDK PMD (Poll Mode Driver) ── 100% 核心死循環輪詢  │
  │   ├── HugePages (1GB 巨頁) ───────── 鎖定記憶體消除 TLB Miss │
  │   └── NUMA 綁定 ──────────────────── 本地節點記憶體零匯流排延遲 │
  └────────────────────────┬───────────────────────────────┘
                           │ (解析 FIX / ITCH 行情)
                           ▼
                  [證交所撮合 / 行情引擎]</code></pre>
<ul>
  <li><strong>PMD 輪詢模式驅動（Poll Mode Driver）</strong>：
    <ul>
      <li>Linux 預設採用「硬體中斷驅動」，每次中斷皆導致 CPU 暫停當前工作並進行上下文切換。</li>
      <li>DPDK 專用 CPU 核心以 `while(1)` 死循環 100% 輪詢網卡 RX 環形緩衝區，封包抵達瞬間即在微秒內完成抓取，<strong>中斷開銷徹底降為 0</strong>。</li>
    </ul>
  </li>
  <li><strong>1GB HugePages 記憶體鎖定</strong>：
    <ul>
      <li>預設 4KB 分頁在海量封包緩衝下會產生龐大的分頁表，引發頻繁的 CPU TLB Miss。</li>
      <li>DPDK 配置 <strong>1GB 巨型分頁（HugePages）</strong>，並透過 `mlockall()` 鎖定實體記憶體，將 TLB 快取命中率提升至接近 100%。</li>
    </ul>
  </li>
  <li><strong>NUMA 親和性綁定（NUMA Affinity）</strong>：
    <ul>
      <li>網卡 PCIe 插槽綁定之 CPU Socket（如 NUMA Node 0），與執行 DPDK 程式之 CPU 核心、HugePages 實體記憶體完全限制在同一 NUMA 節點內，消除跨 QPI/UPI 匯流排存取之 150ns 延遲。</li>
    </ul>
  </li>
</ul>

<h4>四、行情多播（UDP Multicast）開盤微突發防護實務</h4>
<ol>
  <li><strong>微突發丟包痛點</strong>：上午 9:00 開盤瞬間，巨量成交行情多播（Multicast ITCH）封包湧入。傳統 Linux Socket 緩衝區受限於排程延遲，極易發生網卡 RX Ring Buffer 溢位丟包。</li>
  <li><strong>硬體佇列放大與多佇列分離（RSS）</strong>：
    <ul>
      <li>透過 SR-IOV 為行情專用 VF 分配最大硬體環形佇列（`rx_ring_size = 4096`）。</li>
      <li>啟用網卡硬體接收端調節（RSS, Receive Side Scaling），依據多播群組 IP 雜湊分流至多個專用 DPDK PMD 輪詢執行緒。</li>
    </ul>
  </li>
  <li><strong>達成絕對零丟包（Zero-Packet-Drop）</strong>：DPDK 無拷貝環形佇列與納秒級處理循環，即使在線速 100Gbps 開盤海量行情衝擊下，亦能確保行情封包一筆不漏直達撮合引擎。</li>
</ol>

<h4>五、結論：構建雲原生金融超高速公路</h4>
<p>藉由 <strong>SR-IOV 硬體切分 ＋ DPDK 核心旁路</strong>，證交所成功在虛擬化與雲原生容器環境中實現了<strong>封包延遲 < 1.5 微秒、抖動 < 200 奈秒</strong>之極致指標。既保有了虛擬化架構之靈活動態調度能力，又完全兼顧了國家金融關鍵基礎設施對超低延遲之極限苛求。</p>
            """,
            "examinerTips": "得分關鍵詞：『vSwitch 軟體轉發與上下文切換延遲』、『SR-IOV 實體功能 PF 與虛擬功能 VF 硬體切分』、『VFIO 直通繞過 Hypervisor』、『DPDK PMD 輪詢消除中斷』、『1GB HugePages 消除 TLB Miss』、『NUMA 本地化親和綁定』、『開盤多播 Zero-Packet-Drop』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>虛擬化網路痛點（6分）</strong>：深入解構 vSwitch、記憶體多次複製與 Hypervisor 排程抖動根因。</li>
  <li><strong>SR-IOV 原理（7分）</strong>：辨析 PF 與 VF 職責，闡明硬體 L2 ASIC 轉發與直通優勢。</li>
  <li><strong>DPDK 核心旁路整合（7分）</strong>：條理清晰闡釋 PMD 輪詢、1GB 巨頁與 NUMA 親和性優化機制。</li>
  <li><strong>多播行情防護結論（5分）</strong>：結合 9:00 開盤微突發，提出 RSS 分流、RX 佇列放大與零丟包落地實務。</li>
</ul>
            """
        },

        # sn-essay-35: BGP Anycast and ECMP
        {
            "id": "sn-essay-35",
            "category": "sysnet",
            "chapter": "第 2 章：金融專屬網路拓撲與行情多點廣播（Multicast）",
            "title": "跨資料中心 BGP Anycast 與等價多路徑（ECMP）在證交所多機房負載均衡與秒級容災接管",
            "summary": "剖析 IP Anycast 原理、BGP 路由屬性（MED, AS-Path Prepending）、五元組雜湊負載均衡、健康檢查連動 BGP 撤銷（BGP Route Withdrawal）達成秒級自動流量轉移之架構實務。",
            "points": 25,
            "rubric": "1. IP Anycast 原理與證券單一固定 VIP 連線架構 (6分)；2. BGP 路由控制（AS-Path, MED）與交換機 ECMP 多路徑負載均衡 (7分)；3. TCP 有狀態連線防漂移與五元組一致性雜湊 (7分)；4. BGP 路由撤銷（Route Withdrawal）秒級容災切換結論 (5分)",
            "question": "臺灣證交所具備板橋主資料中心、台北第一備援機房及異地第二備援機房。為提供券商單一固定連線 IP 並達成秒級自動故障轉移，試申論：(1) IP Anycast 核心原理：跨不同物理機房之邊界路由器宣告相同 IP 位址（VIP）；(2) BGP 路由協議屬性（AS-Path, MED, Community）與交換機等價多路徑（ECMP）在多機房負載均衡之運作機制；(3) Anycast 面臨 TCP 連線狀態漂移（State Flapping）之技術挑戰，與五元組雜湊（Consistent Hashing）保持連線黏性之解法；(4) 當單一機房遭遇火警或網路中斷時，透過 BGP Route Withdrawal（路由撤銷）與 BGP Fast Reroute（FRR）實現秒級流量無感切換之架構設計。",
            "modelAnswer": r"""
<h4>一、破題：跨機房高可用負載均衡之戰略挑戰</h4>
<p>臺灣證券交易所為維繫交易連續性，建置了<strong>板橋主資料中心（IDC）、台北第一備援機房與異地第二備援機房</strong>。傳統 DNS 輪詢（DNS Round-Robin）或主備切換受制於客戶端 DNS 快取（TTL），切換往往耗時數分鐘甚至數小時，無法滿足金融級 RTO ≤ 10 分鐘之嚴格要求。透過<strong>「BGP Anycast（任播）」結合「ECMP（等價多路徑）」</strong>，可讓多個實體機房共享相同的服務 IP（VIP），達成路徑最短化、負載均衡與秒級自動容災。</p>

<h4>二、BGP Anycast 原理與單一 VIP 連線架構</h4>
<ol>
  <li><strong>Anycast 本質</strong>：在網路層（L3），將同一個單播 IP 位址（如 `203.75.100.1`）同時配置於板橋與台北多個不同實體機房之負載均衡器（LB）。</li>
  <li><strong>BGP 路由廣播</strong>：各機房之邊界路由器向各電信業者（中華電信、遠傳、台灣大哥大）及券商骨幹發布相同 VIP 之 BGP 路由條目。</li>
  <li><strong>拓撲最短路徑路由</strong>：券商下單系統發起連線時，網際網路路由器依據 BGP 最短 AS-Path 與 IGP Metric，自動將封包引導至<strong>物理距離最近、網路跳數最少</strong>之證交所機房，顯著壓降下單傳輸時延。</li>
</ol>

<h4>三、BGP 路由屬性控制與交換機 ECMP 機制</h4>
<pre><code class="language-text">                     [證券商下單主機 / 券商專線]
                                  │
                                  ▼
                     [電信骨幹 / 邊界路由器]
                                  │
         ┌────────────────────────┴────────────────────────┐
         │ (ECMP / BGP 最短路徑)                           │ (BGP 備援路徑)
         ▼                                                 ▼
  [板橋主機房 (VIP: 203.75.100.1)]              [台北備援機房 (VIP: 203.75.100.1)]
  BGP 正常宣告 (AS-Path: 65001)                 BGP Prepend (AS-Path: 65001 65001)
         │                                                 │
  [主撮合閘道器叢集 (Active)]                    [備援撮合閘道器叢集 (Standby)]</code></pre>
<ul>
  <li><strong>主備流量引流工程（BGP Traffic Engineering）</strong>：
    <ul>
      <li><strong>AS-Path Prepending</strong>：板橋主機房宣告原始 AS-Path；台北備援機房額外填充 2~3 個自身 AS 號（Prepending），使全球路由器優先將流量導向板橋。</li>
      <li><strong>Multi-Exit Discriminator（MED）</strong>：在跨機房同屬單一 ISP 專線時，設定較低的 MED 值（如 10 vs 100）指定主機房優先級。</li>
    </ul>
  </li>
  <li><strong>ECMP（Equal-Cost Multi-Path）</strong>：在資料中心內部 Spine-Leaf 架構中，交換機遇到開銷相同之多條路徑時，依據封包<strong>五元組（來源 IP、來源 Port、目的 IP、目的 Port、協定）</strong>進行雜湊分流，達成線速橫向擴展負載均衡。</li>
</ul>

<h4>四、TCP 有狀態連線防漂移與一致性雜湊</h4>
<p>Anycast 最大挑戰在於 TCP 為「有狀態（Stateful）」，若網際網路路由發生震盪（Flapping），後續 TCP ACK 封包可能被轉發至另一個機房，導致連線中斷（RST）：</p>
<ol>
  <li><strong>邊界穩定化配置（Route Dampening）</strong>：在上游 ISP 側設定適當的路由衰減閥值，防止微小網路抖動觸發全網路由重收斂。</li>
  <li><strong>L4 負載均衡一致性雜湊（Consistent Hashing）</strong>：各機房內部部署採用 <strong>Maglev 演算法</strong> 之四層負載均衡器（L4LB），即使節點故障或擴展，相同 TCP 連線仍固定轉發至同一下單伺服器。</li>
  <li><strong>跨機房連線狀態同步（State Mirroring）</strong>：透過板橋與台北之間的低延遲專線，關鍵下單連線狀態即時雙向鏡像。一旦發生極端連線漂移，台北機房仍可接續維持 TCP 工作階段，避免重新握手。</li>
</ol>

<h4>五、結論：BGP 路由撤銷（Withdrawal）秒級容災實務</h4>
<p>各機房內部運行高精度健康檢查守護行程（Health-check Agent）。一旦板橋機房遭遇嚴重水火警、核心交換機癱瘓或所有下單閘道器斷線，<strong>健康守護進程於 1 秒內強制中斷與邊界路由器之 BGP Peering，向全網發送 BGP Route Withdrawal（路由撤銷）</strong>。全網 BGP 路由器在 <strong>2~3 秒內自動完成收斂</strong>，所有後續下單委託瞬間平滑引流至台北備援機房，達成 RTO 趨近於零的極致高可用金融韌性。</p>
            """,
            "examinerTips": "得分關鍵詞：『BGP Anycast 多機房單一 VIP』、『AS-Path Prepending 與 MED 流量工程』、『交換機五元組 ECMP 負載均衡』、『TCP 狀態漂移防護與 Maglev 一致性雜湊』、『連線狀態專線鏡像』、『BGP Route Withdrawal 秒級自動撤銷容災』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>Anycast 原理（6分）</strong>：深入辨析 L3 任播技術、單一 VIP 與最優跳數路由優勢。</li>
  <li><strong>BGP 與 ECMP 工程（7分）</strong>：精確指出 AS-Path Prepend、MED 控制主備流量及交換機五元組雜湊。</li>
  <li><strong>TCP 狀態漂移解法（7分）</strong>：直擊 Anycast 致命弱點，提出 Maglev 演算法與跨機房專線狀態同步。</li>
  <li><strong>秒級容災結論（5分）</strong>：闡述主動健康檢查連動 BGP 撤銷，實現 2~3 秒無感故障轉移。</li>
</ul>
            """
        },

        # sn-essay-36: NVMe-oF RoCEv2
        {
            "id": "sn-essay-36",
            "category": "sysnet",
            "chapter": "第 6 章：分散式交易、雙活資料庫與高可用叢集",
            "title": "全快閃儲存 NVMe-oF（Over Fabrics）RoCEv2 在證券撮合日誌持久化與資料庫儲存之架構設計",
            "summary": "分析 RDMA over Converged Ethernet（RoCEv2）無失真網路架構、PFC 優先級流量控制、ECN 壅塞通知，以及 NVMe-oF 將遠端儲存存取延遲由毫秒壓降至微秒之撮合 WAL 落地設計。",
            "points": 25,
            "rubric": "1. 傳統 FC-SAN/iSCSI SCSI 協定佇列鎖瓶頸 vs NVMe 本質優勢 (6分)；2. NVMe-oF 結合 RoCEv2 RDMA 核心旁路與零拷貝技術 (7分)；3. 無失真乙太網（Lossless Ethernet）：PFC（802.1Qbb）與 ECN 機制 (7分)；4. 撮合 WAL 交易日誌微秒級同步寫入實踐結論 (5分)",
            "question": "逐筆撮合系統每完成一筆訂單成交，必須強制將預寫交易日誌（WAL）同步寫入持久化儲存方可回報成交。傳統 FC-SAN / iSCSI 存取延遲在數百微秒至毫秒級，成為系統每秒十萬筆撮合之物理天花板。試申論：(1) 傳統 SCSI 協定棧與單一佇列鎖限制，對比 NVMe 具備 64,000 個深度佇列（Queue Depth 64k）之本質差異；(2) NVMe-oF（NVMe over Fabrics）結合 RoCEv2（RDMA over Converged Ethernet v2）之遠端直接記憶體存取架構；(3) 無失真乙太網（Lossless Ethernet）底層關鍵機制：優先級流量控制（PFC, 802.1Qbb）與顯式壅塞通知（ECN, RFC 3168）消除封包遺失；(4) 撮合主機透過 NVMe-oF 將日誌同步鏡像至同城全快閃儲存陣列（AFA），將遠端寫入延遲壓降至 10 微秒以內之生產實務架構。",
            "modelAnswer": r"""
<h4>一、破題：逐筆撮合交易之持久化（WAL）物理天花板</h4>
<p>在證券集中市場之逐筆撮合機制中，金融交易之 ACID 特性要求每一筆委託成交必須落實 <strong>預寫式日誌（Write-Ahead Logging, WAL）</strong> 同步落盤，方能向券商回報成交，確保系統崩潰時具備 <strong>RPO = 0（零資料遺失）</strong>。傳統企業儲存（FC-SAN、iSCSI）之存取延遲高達數百微秒（μs）至數毫秒（ms），直接鎖死撮合吞吐量。<strong>NVMe-oF 結合 RoCEv2</strong> 之全快閃儲存架構，將遠端儲存延遲壓降至<strong>微秒級（< 10μs）</strong>，打破了集中市場性能之硬體桎梏。</p>

<h4>二、SCSI 協定瓶頸 vs. NVMe 佇列革命</h4>
<ol>
  <li><strong>傳統 SCSI 協定棧缺陷</strong>：
    <ul>
      <li>SCSI 誕生於機械硬碟時代，設計僅具備<strong>單一指令佇列（Single Queue）</strong>，佇列深度僅 32~256。</li>
      <li>在現代多核心 CPU（如 64 核心）環境下，所有核心存取儲存必須爭搶全域自旋鎖（Global Spinlock），導致嚴重的 CPU 核心間互斥鎖爭用與等待延遲。</li>
    </ul>
  </li>
  <li><strong>NVMe 原生硬體革命</strong>：
    <ul>
      <li>支援多達 <strong>64,000 個獨立 I/O 佇列</strong>，每個佇列深度可達 <strong>64,000 個指令</strong>。</li>
      <li>每個 CPU 核心可分配專屬的獨立佇列，完全消除跨核心鎖爭用，將 NVMe SSD 之微秒級讀寫潛力徹底釋放。</li>
    </ul>
  </li>
</ol>

<h4>三、NVMe-oF 結合 RoCEv2 遠端直通架構</h4>
<pre><code class="language-text">  [證交所撮合主機 CPU 記憶體]
             │ (RDMA 零拷貝寫入請求)
             ▼
  ┌────────────────────────────────────────────────────────┐
  │ 100GbE 智慧網卡 (SmartNIC / RNIC)                      │
  │   └── 封裝 NVMe 指令至 RDMA RoCEv2 UDP 封包 (Port 4791) │
  └──────────────────────────┬─────────────────────────────┘
                             │ (無失真乙太網直連，延遲 < 8μs)
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ 遠端全快閃儲存陣列 (NVMe-oF Target / AFA)               │
  │   └── 硬體 DMA 直接寫入遠端 Enterprise NVMe SSD WAL 日誌 │
  └────────────────────────────────────────────────────────┘</code></pre>
<ul>
  <li><strong>NVMe-oF（NVMe over Fabrics）技術原理</strong>：打破原本 PCIe 匯流排之物理長度限制，將 NVMe 封包封裝於高速網路結構中傳輸。</li>
  <li><strong>RoCEv2（RDMA over Converged Ethernet v2）</strong>：
    <ul>
      <li>利用標準 UDP/IP 網路（封包目的 Port 4791）進行路由，傳輸全程由硬體 RNIC 網卡負責處理。</li>
      <li><strong>零拷貝（Zero-Copy）與核心旁路（Kernel Bypass）</strong>：資料直接自撮合主機記憶體 DMA 拷貝至遠端全快閃儲存記憶體，完全不需經過 Host OS 核心堆疊，單向網路傳輸僅需 1~2 微秒。</li>
    </ul>
  </li>
</ul>

<h4>四、無失真乙太網（Lossless Ethernet）：PFC 與 ECN 協同</h4>
<p>RDMA 設計預設底層網路為「零封包丟失（Lossless）」。若發生丟包觸發重傳，延遲將瞬間飆升數千倍：</p>
<ol>
  <li><strong>優先級流量控制（PFC, IEEE 802.1Qbb）</strong>：
    <ul>
      <li>在單一實體網路上將流量切分為 8 個優先級（CoS 0~7）。將 NVMe-oF WAL 日誌綁定於高優先級隊列（如 CoS 3）。</li>
      <li>當交換機佇列水線達到高水位閾值時，交換機向上游發送 <strong>PFC PAUSE 暫停幀</strong>，僅暫停 CoS 3 流量，絕不丟失任何日誌封包，亦不影響其他業務流量。</li>
    </ul>
  </li>
  <li><strong>顯式壅塞通知（ECN, RFC 3168）</strong>：
    <ul>
      <li>交換機在佇列即將壅塞但尚未溢位前，在 IP 標頭標記 ECN 位元（CE 狀態）。</li>
      <li>接收端發現標記後回傳 CNP（Congestion Notification Packet），促使傳送端智慧網卡適應性調降發送速率，從源頭化解壅塞，避免頻繁觸發 PFC 引發「PFC 死鎖（PFC Deadlock）」。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：撮合交易日誌同城微秒級同步落地</h4>
<p>證交所透過 <strong>NVMe-oF RoCEv2</strong>，將撮合主機與板橋同城災備全快閃陣列直連。撮合引擎完成委託撮合後，<strong>同步寫入雙節點 WAL 日誌之整體耗時（Round-Trip Time）穩定壓降於 8~12 微秒以內</strong>。在保證金融級 <strong>RPO = 0、強一致性 ACID</strong> 的前提下，撮合系統吞吐量提升達 5 倍以上，奠定世界頂尖撮合效能基石。</p>
            """,
            "examinerTips": "得分關鍵詞：『SCSI 單佇列鎖瓶頸 vs NVMe 64k 佇列革命』、『NVMe-oF RoCEv2 UDP 4791』、『RDMA 核心旁路與零拷貝 DMA』、『無失真乙太網 Lossless Ethernet』、『PFC 802.1Qbb 優先級流量控制』、『ECN 顯式壅塞通知與 CNP 防死鎖』、『WAL 雙寫延遲壓降至 10 微秒以內』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>儲存架構瓶頸（6分）</strong>：深入解構 SCSI 鎖爭用、佇列深度極限與撮合 WAL 同步延遲之矛盾。</li>
  <li><strong>NVMe-oF 與 RoCEv2（7分）</strong>：繪製清晰資料流向圖，精準闡明 RDMA DMA 直通與次微秒通訊機制。</li>
  <li><strong>無失真網路技術（7分）</strong>：條列清晰指出 PFC 802.1Qbb 優先級隊列與 ECN 壅塞通知之防死鎖配合。</li>
  <li><strong>撮合 WAL 落地結論（5分）</strong>：提出板橋同城雙寫、RPO = 0 與 8~12 微秒 RTT 之卓越工程指標。</li>
</ul>
            """
        },

        # sn-essay-37: Linux Kernel Tuning (dirty_ratio, nohz_full, isolcpus)
        {
            "id": "sn-essay-37",
            "category": "sysnet",
            "chapter": "第 4 章：作業系統核心調校與即時排程（Linux Kernel Tuning）",
            "title": "Linux 核心參數深度調校：消除記憶體分頁回寫（Dirty Ratio）與定時器中斷對極致撮合之抖動",
            "summary": "解構 Linux 記憶體回寫參數（vm.dirty_background_ratio, vm.dirty_ratio）、定時器無滴答核心（nohz_full）、RCU 核心綁定（rcu_nocbs）消除撮合主機 CPU 抖動（Jitter）之最佳實務調校。",
            "points": 25,
            "rubric": "1. 記憶體分頁髒污回寫與定時中斷引發長尾延遲抖動（Jitter）成因 (6分)；2. vm.dirty 參數群（background_ratio, ratio, expire）平滑回寫機制 (7分)；3. Linux 啟動引數：nohz_full, isolcpus 與 rcu_nocbs 隔離配置 (7分)；4. 停用 THP 與 NUMA 自動平衡防凍結實務結論 (5分)",
            "question": "證交所極致低延遲撮合伺服器對 99.99 百分位（P99.99）長尾延遲要求極端苛刻（不允許超過 50 微秒）。然而 Linux 預設排程與記憶體子系統常因背景回寫與定時中斷引發高達數毫秒之延遲毛刺（Jitter）。試申論：(1) Linux 記憶體分頁回寫機制（Page Dirtying）與 `flush/kworker` 執行緒突發搶佔導致 I/O 阻塞之成因；(2) 核心參數調校策略：`vm.dirty_background_ratio=3`, `vm.dirty_ratio=5`, `vm.dirty_expire_centisecs=500` 平滑寫入之原理；(3) Linux 啟動參數：`nohz_full`（無滴答核心 Tickless）、`isolcpus`（核心隔離）與 `rcu_nocbs` 消除撮合專用核心之中斷干擾；(4) 停用透明大頁（Transparent Huge Pages, THP = never）與 NUMA 自動平衡（`numa_balancing = 0`）以避免記憶體隨機凍結（Stall）之調校依據。",
            "modelAnswer": r"""
<h4>一、破題：延遲確定性與 Linux 通用排程之矛盾</h4>
<p>在通用作業系統中，Linux 核心預設之設計哲學是「吞吐量優先（Throughput-oriented）」與「公平共享（CFS Scheduler）」。然而，在證券交易所逐筆撮合伺服器上，衡量系統優劣的關鍵不在於平均延遲（Average Latency），而在於<strong>「長尾延遲（Tail Latency, P99.99）」之確定性</strong>。若系統每數萬筆交易隨機出現一次高達數毫秒的延遲毛刺（Jitter），即可能導致撮合順序錯亂或高頻策略嚴重虧損。必須對 Linux 記憶體、中斷與排程進行手術刀級別的極致硬化調校。</p>

<h4>二、記憶體分頁回寫（Page Cache）引發之 I/O 凍結成因</h4>
<ol>
  <li><strong>Linux 預設回寫機制缺陷</strong>：
    <ul>
      <li>預設配置下，`vm.dirty_ratio` 常高達 20%~30%。當伺服器記憶體為 512GB 時，髒頁（Dirty Pages）可堆積至 100GB 以上。</li>
      <li>一旦髒頁超過上限，Linux 核心會<strong>強制將正在產生寫入的應用程式執行緒掛起（Throttle / Blocking）</strong>，強迫其同步參與磁碟回寫，導致撮合執行緒瞬間凍結長達數秒。</li>
    </ul>
  </li>
  <li><strong>kworker 執行緒 CPU 爭用</strong>：背景核心執行緒 `kworker/kswapd` 突發被喚醒大量消耗記憶體匯流排頻寬，排擠撮合核心。</li>
</ol>

<h4>三、虛擬記憶體參數平滑調校策略</h4>
<p>在 `/etc/sysctl.conf` 中實施「早回寫、平滑寫、小步慢跑」原則：</p>
<pre><code class="language-ini"># 當髒頁達到系統記憶體 3% 時，背景啟動回寫，完全不阻塞應用層
vm.dirty_background_ratio = 3

# 嚴格限制最大髒頁上限為 5%，杜絕巨量髒頁積累引發強制同步鎖定
vm.dirty_ratio = 5

# 縮減髒頁過期時間至 5 秒（預設為 30 秒），促使核心持續平滑寫入
vm.dirty_expire_centisecs = 500
vm.dirty_writeback_centisecs = 100

# 降低 Swap 交換傾向，極致環境中建議徹底禁用 Swap
vm.swappiness = 0</code></pre>
<ul>
  <li><strong>原理效益</strong>：透過極小化比例，將累積大量寫入的「海嘯式突發」轉化為「涓涓細流」的平穩背景 I/O，徹底消除撮合執行緒被核心強制凍結的風險。</li>
</ul>

<h4>四、啟動參數隔離：打造純淨零中斷核心（Tickless Kernel）</h4>
<p>在 GRUB 核心啟動參數（`/etc/default/grub`）中，將撮合專用 CPU 核心（如 Core 8~15）完全自 Linux 排程體系中剝離：</p>
<pre><code class="language-text">GRUB_CMDLINE_LINUX="... isolcpus=8-15 nohz_full=8-15 rcu_nocbs=8-15 processor.max_cstate=0 intel_idle.max_cstate=0"</code></pre>
<ol>
  <li><strong>`isolcpus=8-15`（CPU 核心隔離）</strong>：
    <ul>
      <li>告知 Linux CFS 排程器嚴禁將任何一般使用者進程或系統 Daemon 自動排程至 Core 8~15。</li>
      <li>僅由撮合主程式在啟動時，透過 <code>sched_setaffinity()</code> 顯式手動綁定專用核心。</li>
    </ul>
  </li>
  <li><strong>`nohz_full=8-15`（全無滴答核心 Full Tickless）</strong>：
    <ul>
      <li>Linux 核心傳統每秒產生 100~1000 次定時器排程中斷（Timer Tick）。</li>
      <li>當隔離核心上僅運行單一撮合執行緒時，`nohz_full` <strong>直接關閉定時器中斷</strong>，消除定時中斷造成的每秒數十次微秒級上下文抖動。</li>
    </ul>
  </li>
  <li><strong>`rcu_nocbs=8-15`（卸載 RCU 回呼）</strong>：
    <ul>
      <li>將核心內部 RCU（Read-Copy Update）回呼處置責任移交給非隔離核心（Core 0~7），隔離核心完全不受核心簿記工作打擾。</li>
    </ul>
  </li>
  <li><strong>關閉 C-states 節能（`intel_idle.max_cstate=0`）</strong>：強制 CPU 永遠鎖定在最高 P-state 頻率，消除 CPU 自睡眠低頻狀態喚醒帶來的 10~50 微秒喚醒延遲。</li>
</ol>

<h4>五、結論：停用 THP 與 NUMA 自動平衡防隨機凍結</h4>
<ul>
  <li><strong>停用透明大頁（THP = never）</strong>：Linux `khugepaged` 背景壓縮整理 2MB 大頁面時會持有全域記憶體鎖（Memory Compaction），導致隨機 10~100ms 停頓。撮合系統全面採用<strong>預先分配之靜態 HugePages（1GB 巨頁）</strong>並永久停用 THP。</li>
  <li><strong>停用 NUMA 自動平衡（`kernel.numa_balancing = 0`）</strong>：防止核心在背景隨意將記憶體頁跨 CPU Socket 搬移產生缺頁中斷。</li>
</ul>
<p>透過上述極致調校，證交所撮合伺服器達成了<strong>「零計時中斷、零強制回寫、零隨機鎖定」</strong>，將 P99.99 延遲牢牢錨定在 15 微秒以內，實現世界級延遲確定性。</p>
            """,
            "examinerTips": "得分關鍵詞：『P99.99 長尾延遲確定性』、『vm.dirty_background_ratio=3 平滑回寫消除 Throttle』、『isolcpus 隔離專用撮合核心』、『nohz_full 關閉定時器排程中斷 Full Tickless』、『rcu_nocbs 卸載 RCU 回呼』、『intel_idle.max_cstate=0 關閉節能省電』、『THP=never 停用透明大頁防 Compaction 凍結』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>Jitter 成因剖析（6分）</strong>：直擊記憶體髒頁超標引發核心 Throttle 與定時器中斷之抖動根因。</li>
  <li><strong>vm.dirty 調校策略（7分）</strong>：精確給出 background=3, ratio=5 參數，闡明「小步慢跑」平滑寫入原理。</li>
  <li><strong>啟動引數隔離（7分）</strong>：條列清晰深入 nohz_full、isolcpus、rcu_nocbs 與關閉 C-states 機制。</li>
  <li><strong>THP 與 NUMA 結論（5分）</strong>：指出 khugepaged 整理鎖定風險，提出靜態巨頁與停用自動平衡之標竿實踐。</li>
</ul>
            """
        },

        # sn-essay-38: Raft Consensus in Ledger
        {
            "id": "sn-essay-38",
            "category": "sysnet",
            "chapter": "第 6 章：分散式交易、雙活資料庫與高可用叢集",
            "title": "分散式高可用撮合叢集：Raft 共識演算法與 Paxos 在金流簿記（Ledger）狀態機複製之應用",
            "summary": "深入剖析 Raft 演算法 Leader 選舉、日誌複製（Log Replication）、安全性保證與腦裂（Split-Brain）多數決（Quorum）機制，設計金融交易帳本狀態機強一致性複製架構。",
            "points": 25,
            "rubric": "1. 狀態機複製（State Machine Replication, SMR）架構與金融強一致性 (6分)；2. Raft 核心子問題剖析：Leader 選舉、Term 租期與日誌複製 Quorum (7分)；3. 網路分區防腦裂（Split-Brain）與安全性不變量（Safety Invariants） (7分)；4. 高頻流水線（Pipelining）與批量提交效能優化結論 (5分)",
            "question": "證券集中市場之成交簿記（Trade Ledger）要求絕對不可遺失（RPO = 0）與最高一致性（Linearizability）。試申論：(1) 狀態機複製（State Machine Replication, SMR）架構原理；(2) Raft 共識演算法三大核心子問題剖析：Leader 選舉（Heartbeat, Randomized Election Timeout）、日誌複製（AppendEntries, Quorum 多數決）與安全性保證（Leader Completeness）；(3) 面對跨機房網路分區（Network Partition）時，Raft 奇數節點（2N+1）如何徹底防範「腦裂（Split-Brain）」；(4) 針對證券超高頻交易場景，如何透過批量日誌提交（Batching）、流水線複製（Pipelining）與非阻塞持久化（Asynchronous Disk Flush）進行 Raft 效能極限優化。",
            "modelAnswer": r"""
<h4>一、破題：分散式交易帳本一致性與可用性之基石</h4>
<p>在證券集中市場中，成交簿記（Trade Ledger）是投資人資產轉移與交割結算的終極憑證。任何單點故障皆不可導致帳本分歧或歷史紀錄遺失（必須保證 <strong>RPO = 0</strong> 與<strong>可線性化（Linearizability）強一致性</strong>）。傳統主從非同步複製存在資料遺失盲區，而硬體共享磁碟又受限於物理距離。<strong>狀態機複製（SMR, State Machine Replication）</strong> 結合現代分散式共識演算法（如 <strong>Raft</strong>），已成為構建金融級分散式撮合帳本叢集之核心範式。</p>

<h4>二、狀態機複製（SMR）核心架構原理</h4>
<p>狀態機複製建立於確定性原理：<strong>「多個相同的確定性狀態機（Deterministic State Machine），只要從相同的初始狀態出發，依據完全相同的順序執行相同的日誌指令序列（Input Log），最終必定產出完全一致的狀態。」</strong></p>
<ol>
  <li><strong>共識層（Consensus Module）</strong>：負責保證所有節點上的日誌序列（Log Entries）在順序與內容上達成絕對一致。</li>
  <li><strong>狀態機層（State Machine）</strong>：由撮合引擎與帳本簿記邏輯構成，僅依循共識層確認提交（Committed）之日誌順序依序套用（Apply），更新記憶體買賣委託簿與帳戶餘額。</li>
</ol>

<h4>三、Raft 演算法三大子問題運作剖析</h4>
<pre><code class="language-text">  [用戶端券商委託] ──> [Leader 節點] ── (AppendEntries RPC) ──> [Follower 節點 1] (ACK)
                             │
                             ├── (AppendEntries RPC) ──> [Follower 節點 2] (ACK)
                             │
                             ▼ (過半數 Quorum 2/3 同意)
                  [標記 Committed 並套用至狀態機]
                             │
                             └──> [回傳撮合成交回報]</code></pre>
<ul>
  <li><strong>Leader 選舉（Leader Election）</strong>：
    <ul>
      <li>叢集包含三種角色：Leader、Follower、Candidate。Leader 週期向 Follower 發送心跳（Heartbeat）。</li>
      <li><strong>隨機化選舉超時（Randomized Election Timeout, 如 150~300ms）</strong>：若 Follower 在超時內未收到心跳，轉為 Candidate 並增加任期號（Term），發起投票。隨機化機制有效避免多個節點同時參選導致選票瓜分（Split Vote）。</li>
    </ul>
  </li>
  <li><strong>日誌複製（Log Replication）與 Quorum</strong>：
    <ul>
      <li>所有交易指令僅能由 Leader 接收。Leader 將指令附加至自身日誌後，透過 `AppendEntries` RPC 平行分發給全體 Follower。</li>
      <li>一旦收到<strong>嚴格多數節點（Quorum, $\lfloor N/2 \rfloor + 1$）</strong> 之成功回覆，該日誌即被判定為 <strong>Committed（已提交）</strong>，Leader 隨後將指令套用至狀態機，並通知客戶端成交。</li>
    </ul>
  </li>
  <li><strong>安全性保證（Leader Completeness）</strong>：
    <ul>
      <li>Raft 保證：<strong>任何新當選的 Leader 必定包含所有在之前任期中已經 Committed 的全部日誌</strong>。投票規則明定：若 Candidate 的日誌最後條目在「Term 號」或「日誌索引（Index）」落後於 Voter，Voter 直接拒絕投票，從數學上杜絕歷史日誌被覆蓋。</li>
    </ul>
  </li>
</ul>

<h4>四、網路分區與防腦裂（Split-Brain）設計</h4>
<p>在跨板橋、台北、台中三機房部署 5 節點叢集（Quorum = 3）：</p>
<ol>
  <li><strong>網路分區情境</strong>：假設板橋機房（2 節點）與台北/台中機房（3 節點）之間專線完全中斷。
    <ul>
      <li><strong>少數派分區（板橋，2 節點）</strong>：舊 Leader 無法取得過半數（2 < 3）確認，所有新的下單交易無法 Commit，自動被掛起或拒絕，<strong>絕對無法產生腦裂雙寫</strong>。</li>
      <li><strong>多數派分區（台北/台中，3 節點）</strong>：成功選出新 Leader，3 節點滿足 Quorum（3 ≥ 3），持續安全處理撮合交易。</li>
    </ul>
  </li>
  <li><strong>網路復原收斂</strong>：當分區修復後，舊 Leader 收到新 Leader 之高 Term 號心跳，自動降級為 Follower，並以新 Leader 之日誌覆蓋未提交之懸掛日誌，叢集瞬時恢復全域一致。</li>
</ol>

<h4>五、結論：證券高頻場景之極致效能調校</h4>
<p>標準 Raft 每筆交易等待磁碟 fsync 與網路往返，吞吐量難破萬。針對證交所每秒十萬筆逐筆撮合：</p>
<ul>
  <li><strong>批量提交（Batching）</strong>：撮合前置將微秒內湧入之數十筆委託封裝為單一 Raft Log Entry，分攤共識開銷。</li>
  <li><strong>流水線複製（Pipelining）</strong>：Leader 無需等待上一筆 RPC 回傳即可持續發送下一筆日誌，大幅消除網路 RTT 等待。</li>
  <li><strong>記憶體日誌與非同步快照（In-Memory Raft + Async Snapshot）</strong>：利用 NVMe-oF 遠端鏡像日誌，並非同步生成帳本快照，將狀態機複製之端到端延遲壓降至 100 微秒以內，實現極致可靠之分散式金融核心。</li>
</ul>
            """,
            "examinerTips": "得分關鍵詞：『狀態機複製 SMR 確定性原理』、『隨機選舉超時 Randomized Election Timeout 防 Split Vote』、『Quorum 過半數多數決 (N/2 + 1)』、『Leader Completeness 安全性保證』、『網路分區防腦裂：少數派無法 Commit』、『批量提交 Batching 與流水線 Pipelining 優化』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>SMR 狀態機複製原理（6分）</strong>：深入辨析確定性狀態機、日誌序列輸入與強一致性。</li>
  <li><strong>Raft 核心機制（7分）</strong>：精確剖析 Leader 選舉、Term 租期、AppendEntries 與安全性保證。</li>
  <li><strong>網路分區防腦裂（7分）</strong>：以 5 節點跨機房為例，透徹說明少數派與多數派之數學分割與自癒。</li>
  <li><strong>高頻撮合優化結論（5分）</strong>：提出 Batching、Pipelining 與非同步快照之實務吞吐調校架構。</li>
</ul>
            """
        },

        # sn-essay-39: OpenTelemetry Distributed Tracing
        {
            "id": "sn-essay-39",
            "category": "sysnet",
            "chapter": "第 12 章：維運自動化（IaC）、SRE 網站可靠性工程與監控體系",
            "title": "分散式可觀測性：OpenTelemetry 結合微秒級分散式追蹤（Distributed Tracing）在下單全鏈路之診斷",
            "summary": "探討 W3C TraceContext 標準、Span 傳遞、eBPF 自動無侵入式探針、全鏈路延遲瓶頸分析（券商網關-風控-撮合主機-行情推播）與動態採樣策略。",
            "points": 25,
            "rubric": "1. 證券交易全鏈路微突發延遲定位痛點與 OpenTelemetry 三大支柱 (6分)；2. W3C TraceContext（traceparent/tracestate）標準與跨程序傳播機制 (7分)；3. eBPF 核心級無侵入式探針技術 (7分)；4. 尾端特徵智慧採樣（Tail-based Sampling）與 SRE 實踐結論 (5分)",
            "question": "證券交易鏈路跨越多個系統環節（券商網路網關 -> 預風控引擎 -> 撮合主機 -> 成交回報 -> 多播行情廣播）。當某筆交易發生異常延遲時，如何快速定位瓶頸節點至關重要。試申論：(1) OpenTelemetry（OTel）統一標準架構：Metrics、Logs、Traces 三大支柱之關聯性；(2) W3C TraceContext（`traceparent` 與 `tracestate`）標頭規範與全鏈路 Span 上下文穿透傳遞；(3) 傳統 APM 探針插樁帶來的納秒級延遲損耗，如何結合 eBPF 核心級自動無侵入探針解決；(4) 面對開盤每秒數十萬筆交易之巨量遙測數據，如何實施基於尾端特徵（Tail-based Sampling）之智慧動態採樣（100% 捕獲延遲 > 500μs 之慢交易）。",
            "modelAnswer": r"""
<h4>一、破題：全鏈路微秒延遲之可觀測性黑洞</h4>
<p>在現代證券交易架構中，單筆下單委託自外部券商發起，依序穿越：<strong>【邊界防火牆】 ➔ 【下單網關（Order Gateway）】 ➔ 【事前風控引擎（Pre-trade Risk）】 ➔ 【記憶體撮合主機（Matching Engine）】 ➔ 【成交回報庫（Trade DB）】 ➔ 【多播行情發布（Market Data）】</strong>。過去各子系統僅記錄各自的文字日誌（Log），時鐘不同步且缺乏全域串接標籤。當客戶投訴某筆委託延遲高達 10 毫秒時，維運團隊常陷入互相推諉之困境。<strong>OpenTelemetry（OTel）結合分散式追蹤（Distributed Tracing）</strong>，正是打破系統黑盒之終極武器。</p>

<h4>二、OpenTelemetry 三大支柱關聯模型</h4>
<ol>
  <li><strong>Traces（追蹤鏈路）</strong>：記錄單筆委託穿越全鏈路之因果關係圖與時間戳記。單一追蹤稱為一個 Trace，由多個子環節的 <strong>Span</strong> 組成樹狀結構。</li>
  <li><strong>Metrics（度量指標）</strong>：宏觀統計系統吞吐量（IOPS）、網卡隊列水線、CPU 使用率與 P99 延遲分佈。</li>
  <li><strong>Logs（日誌事件）</strong>：微觀詳細記錄特定業務錯誤碼或委託明文。</li>
  <li><strong>三位一體融合</strong>：Span 內部內嵌日誌事件（Span Events），並關聯指標維度（Exemplars），使 SRE 工程師在 Grafana 看板看到 P99 抖動峰值時，<strong>點擊圖表單一數據點即可秒級跳轉至該筆異常委託之完整 Trace 呼叫鏈</strong>。</li>
</ol>

<h4>三、W3C TraceContext 標準與上下文穿透傳播</h4>
<pre><code class="language-text">  [外部券商 FIX 報文]
           │
           ▼
  [下單閘道器 (Gateway)] ──> 生成 W3C traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
           │                 (Version - TraceID - ParentSpanID - TraceFlags)
           ▼
  [事前風控引擎] ──────────> 承接 TraceID，生成專屬 SpanID 記錄風控耗時
           │
           ▼
  [逐筆撮合核心] ──────────> 承接 TraceID，生成撮合 Span，計算微秒級排隊時延</code></pre>
<ul>
  <li><strong>`traceparent` 規範格式</strong>：包含四大欄位：
    <ul>
      <li>`version`（2 字符，目前為 `00`）。</li>
      <li>`trace-id`（32 字符十六進制，全鏈路唯一識別碼）。</li>
      <li>`parent-id / span-id`（16 字符十六進制，代表父調用節點）。</li>
      <li>`trace-flags`（8 位元旗標，標註是否強制採樣）。</li>
    </ul>
  </li>
  <li><strong>協定穿透實務</strong>：在 HTTP/gRPC 環境直接透過標頭傳遞；在二進位下單協定（如 NASDAQ OUCH 或客製 FIX 協定）中，於自訂擴充標頭（User-defined Tag，如 Tag 9999）封裝二進位 Trace ID，確保跨行程上下文不中斷。</li>
</ul>

<h4>四、eBPF 核心級無侵入式探針（Zero-Overhead Probing）</h4>
<ol>
  <li><strong>傳統 APM 痛點</strong>：傳統 Java/C++ APM Agent 依賴字節碼改寫（Bytecode Instrumentation）或代碼侵入插樁，每次函數調用增加微秒級開銷，並可能引發垃圾回收（GC）停頓，嚴禁部署於撮合引擎。</li>
  <li><strong>eBPF 核心旁路自動擷取</strong>：
    <ul>
      <li>利用 Linux eBPF 探針（kprobe/uprobe 或 Tracepoints）在核心層 <code>sys_enter_writev</code> 與 <code>tcp_sendmsg</code> 處掛載輕量級代碼。</li>
      <li>核心自動解析網路封包中的交易流水號與時間戳記，<strong>完全不需要修改任何撮合主機原始碼</strong>，在核心層非同步推播遙測數據至外置 OTel Collector，延遲干擾小於 50 奈秒。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：尾端特徵智慧採樣（Tail-based Sampling）與 SRE 實務</h4>
<p>在開盤高峰，每秒數十萬筆交易若 100% 全量保存 Tracing 數據，將耗盡網路頻寬與儲存容量：</p>
<ul>
  <li><strong>傳統前端採樣（Head-based Sampling）缺陷</strong>：在請求發起時隨機決定是否採樣（如 1%）。若某筆交易在後端撮合時突發卡頓 20 毫秒，卻因一開始未被抽中而痛失關鍵故障日誌。</li>
  <li><strong>尾端智慧採樣（Tail-based Sampling）架構</strong>：所有 Span 先暫存於 OTel Collector 之記憶體環形緩衝區（保留 5 秒）。等到單筆交易全鏈路結束時進行評估：<strong>「凡是全鏈路耗時 > 500 微秒、HTTP Status != 200 或風控異常拒絕者，100% 強制保留落盤；正常 20 微秒以內完成者僅保留 0.01%」</strong>。</li>
</ul>
<p>透過此機制，證交所維運中心在節省 99% 儲存開銷的同時，確保每一筆微秒長尾抖動交易皆能原形畢現，達成金融級可觀測性最高境界。</p>
            """,
            "examinerTips": "得分關鍵詞：『OpenTelemetry Traces/Metrics/Logs 三位一體』、『Exemplars 指標秒跳 Trace』、『W3C TraceContext traceparent 結構』、『二進位協定自訂 Tag 傳播 TraceID』、『eBPF 核心級無侵入探針納秒開銷』、『Tail-based Sampling 尾端採樣：慢交易 100% 捕獲』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>全鏈路痛點與 OTel 支柱（6分）</strong>：深入解構交易全鏈路拓撲、黑盒排查難題及三大支柱融合機制。</li>
  <li><strong>W3C TraceContext（7分）</strong>：給出清晰 traceparent 格式定義與二進位協定擴充傳遞實務。</li>
  <li><strong>eBPF 核心探針優勢（7分）</strong>：對比傳統插樁代價，詳述 eBPF kprobe/uprobe 納秒級無侵入捕獲。</li>
  <li><strong>尾端採樣與 SRE 結論（5分）</strong>：辨析 Head vs Tail 採樣，闡明 >500μs 慢交易 100% 保留之精準策略。</li>
</ul>
            """
        },

        # sn-essay-40: Kubernetes Multi-Cluster Multi-Active DR
        {
            "id": "sn-essay-40",
            "category": "sysnet",
            "chapter": "第 7 章：微服務、容器編排與 Kubernetes 金融實務",
            "title": "Kubernetes 容器平台容災：多叢集多活架構（Multi-Cluster Multi-Active）與 GitOps 持續交付實務",
            "summary": "規劃板橋主機房與備援機房之跨叢集服務網格（Cilium Cluster Mesh）、ArgoCD 宣告式 GitOps 部署、不可變基礎設施與秒級流量調度架構。",
            "points": 25,
            "rubric": "1. 單一跨機房 K8s 叢集 etcd 延遲腦裂風險 vs 多叢集獨立架構 (6分)；2. Cilium Cluster Mesh 扁平化網路互連與跨叢集 Global Services (7分)；3. ArgoCD 宣告式 GitOps 持續交付與自動漂移偵測（Drift Detection） (7分)；4. 金融合規 Sealed Secrets 與變更軌跡不可否認性審計結論 (5分)",
            "question": "臺灣證交所推進金融周邊服務與行情發布容器化，要求容器平台具備跨資料中心容災與自動化部署合規能力。試申論：(1) 單一大型 K8s 叢集跨機房部署之控制平面（etcd）腦裂風險，與「多叢集獨立多活架構（Multi-Cluster Architecture）」之設計優勢；(2) 透過 Cilium Cluster Mesh 或 Submariner 達成跨叢集扁平網路互連與跨機房微服務動態容災發現（Global Service）；(3) 宣告式 GitOps 持續交付（如 ArgoCD）：以 Git 為單一真實來源（Single Source of Truth）、自動漂移偵測（Drift Detection）與不可變組態部署；(4) 金融業嚴格法遵之 GitOps 安全控制：雙人代碼審查（Code Review）、機密資料加密儲存（Sealed Secrets / HashiCorp Vault）與變更軌跡不可否認性審計。",
            "modelAnswer": r"""
<h4>一、破題：金融容器化演進與高可用容災架構抉擇</h4>
<p>在推動金融應用雲原生容器化過程中，許多企業初期傾向於建立「單一跨機房延伸 Kubernetes 叢集（Stretched Cluster）」。然而，跨機房網路延遲與抖動極易破壞 K8s 控制平面核心——<strong>etcd 分散式共識（Raft）</strong>，造成整個叢集癱瘓。因此，針對板橋主機房與台北備援機房，建構<strong>「多叢集獨立多活架構（Multi-Cluster Multi-Active）」結合「GitOps 宣告式自動化交付」</strong>，是兼顧極限容災與金融合規之最佳解法。</p>

<h4>二、跨機房 Stretched 叢集風險 vs. 多叢集獨立架構對比</h4>
<ol>
  <li><strong>跨機房延伸叢集（Stretched Cluster）之致命隱患</strong>：
    <ul>
      <li><strong>etcd 敏感度過高</strong>：etcd 要求節點間 RTT 小於 10ms，且磁碟寫入延遲極低。一旦跨機房專線發生短暫抖動或封包遺失，etcd 頻繁觸發 Leader 選舉，導致整個 K8s API Server 凍結。</li>
      <li><strong>故障爆炸半徑（Blast Radius）過大</strong>：若某機房遭遇配置錯誤或軟體 Bug，整個跨機房叢集同步崩潰，徹底喪失災備意義。</li>
    </ul>
  </li>
  <li><strong>多叢集獨立架構優勢</strong>：
    <ul>
      <li>板橋與台北各自擁有完全獨立的控制平面（Control Plane）與 etcd 叢集，兩者在架構上完全解耦，故障爆炸半徑嚴格限制在單一機房內。</li>
    </ul>
  </li>
</ol>

<h4>三、Cilium Cluster Mesh 跨叢集扁平網路與 Global Services</h4>
<pre><code class="language-text">  [板橋主機房 K8s 叢集] ── (專線 WireGuard 加密通道) ── [台北備援機房 K8s 叢集]
  Pod 網段: 10.244.0.0/16                                 Pod 網段: 10.245.0.0/16
         │                                                       │
         ├── Cilium Cluster Mesh 控制面 (etcd/API 同步) ────────┤
         │                                                       │
  [服務 Pod A (Active)] <── Global Service 自動負載與容災 ──> [服務 Pod A (Standby)]</code></pre>
<ul>
  <li><strong>扁平化 Pod 互連（Pod-to-Pod Routing）</strong>：各叢集規劃非重疊之 Pod CIDR（如板橋 `10.244.0.0/16`、台北 `10.245.0.0/16`）。Cilium 利用 eBPF 在核心層建立跨機房隧道，兩地 Pod 可直接透過原生 IP 相互通訊，<strong>無需經過 Ingress / Egress 閘道器進行多次 NAT 轉換</strong>。</li>
  <li><strong>跨叢集全域服務（Global Services）</strong>：
    <ul>
      <li>透過在 K8s Service 加上標註（Annotation）`io.cilium/global-service: "true"`。</li>
      <li>板橋的客戶端 Pod 存取 `order-service` 時，預設優先調用板橋本機房 Pod；一旦板橋 Pod 全數掛起，Cilium 於 <strong>1 秒內自動將請求透明轉發至台北機房之健康 Pod</strong>，達成零程式碼修改之跨機房微服務自動容災。</li>
    </ul>
  </li>
</ul>

<h4>四、ArgoCD 宣告式 GitOps 持續交付實務</h4>
<p>在多叢集環境中，嚴禁任何維運人員使用 `kubectl` 手動修改生產配置。全面推行 <strong>GitOps</strong>：</p>
<ol>
  <li><strong>Git 單一真實來源（Single Source of Truth）</strong>：所有 K8s Deployment、ConfigMap、網路策略（CNP）均以宣告式 YAML/Helm/Kustomize 形式存放於 GitLab 倉庫。</li>
  <li><strong>自動漂移偵測與自癒（Drift Detection & Self-Healing）</strong>：
    <ul>
      <li>ArgoCD 控制器以每 3 分鐘為週期（或藉由 Git Webhook 即時觸發）比對 Git 倉庫與板橋、台北兩地叢集之實際運行狀態。</li>
      <li>一旦有人在叢集內部私自修改配置，ArgoCD 立即偵測到「OutOfSync（組態漂移）」，並自動下發修復覆蓋（Auto-Sync / Self-Heal），保證兩地機房配置 100% 精準對齊。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：金融合規安全防護與稽核軌跡</h4>
<p>金融監管對自動化發布有著最嚴格之合規要求：</p>
<ul>
  <li><strong>機密資訊密封管理（Sealed Secrets / HashiCorp Vault）</strong>：資料庫密碼與 TLS 憑證嚴禁明文存放於 Git。透過非對稱加密封裝為 `SealedSecret` CRD，僅目標叢集控制器持有私鑰可解密。</li>
  <li><strong>不可逆變更審計鏈</strong>：所有生產變更必須透過 Git Pull Request 發起，強制要求<strong>主管＋資安雙人數位簽署（GPG Signed Commits）審批</strong>方可合流（Merge）。變更歷程永久留存於 Git 提交歷史中，完全契合金管會雙軸稽核對不可否認性（Non-repudiation）之法規要求。</li>
</ul>
            """,
            "examinerTips": "得分關鍵詞：『Stretched Cluster 之 etcd Raft 崩潰風險』、『多叢集獨立多活架構限制爆炸半徑』、『Cilium Cluster Mesh 扁平化網路』、『Global Services io.cilium/global-service 跨機房透明容災』、『GitOps 單一真實來源 Single Source of Truth』、『ArgoCD 自動漂移偵測 Drift Detection』、『Sealed Secrets 與 GPG 簽署雙人審批合規』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>架構對比剖析（6分）</strong>：深入辨析延伸叢集 etcd 延遲敏感性痛點與多叢集隔離之優勢。</li>
  <li><strong>Cluster Mesh 網路（7分）</strong>：繪製清晰拓撲圖，闡述 eBPF Pod 扁平路由與 Global Service 秒級容災機制。</li>
  <li><strong>GitOps 與 ArgoCD（7分）</strong>：精確指出宣告式組態、Git Webhook 即時同步與 Self-Healing 漂移修復。</li>
  <li><strong>金融合規結論（5分）</strong>：提出 Sealed Secrets、GPG 數位簽署與雙人審批之金融監管落實方案。</li>
</ul>
            """
        },

        # sn-essay-41: QUIC HTTP/3 for Mobile Trading
        {
            "id": "sn-essay-41",
            "category": "sysnet",
            "chapter": "第 5 章：金融通訊協定（FIX/ITCH/OUCH）與低延遲訊息佇列",
            "title": "次世代傳輸協定 QUIC（HTTP/3）於行動證券看盤與行情下單高丟包環境之應用評估",
            "summary": "對比 TCP 與 QUIC（UDP 基礎）機制，剖析單一封包遺失不影響其他 Stream 之消除隊頭阻塞（Head-of-Line Blocking）原理、0-RTT 連線建立與 5G 移動網路連線遷移（Connection Migration）在證券下單之優勢。",
            "points": 25,
            "rubric": "1. 傳統 TCP 傳輸協定於行動弱網環境三大致命缺陷 (6分)；2. QUIC（RFC 9000）架構原理：UDP 封裝、多路複用與消除隊頭阻塞 (7分)；3. 0-RTT 極速交握與 TLS 1.3 深度整合機制 (7分)；4. 連線識別碼（Connection ID）無感連線遷移實務結論 (5分)",
            "question": "廣大行動投資人透過 4G/5G 或公共 Wi-Fi 進行手機下單看盤時，常因無線網路封包遺失或信號切換導致看盤畫面卡頓、下單逾時。試申論：(1) 傳統 TCP 傳輸協定在弱網環境之致命缺陷：傳輸層隊頭阻塞（Head-of-Line Blocking）與 3-Way Handshake / TLS 握手之多次 RTT 延遲；(2) QUIC（RFC 9000，基於 UDP）架構原理：多路複用獨立資料流（Independent Streams）如何徹底根絕隊頭阻塞；(3) QUIC 內建 TLS 1.3 之 0-RTT / 1-RTT 極速連線建立機制；(4) 連線識別碼（Connection ID）技術在行動裝置由 Wi-Fi 切換至 5G 基站時實現「無縫連線遷移（Connection Migration）」，維持證券看盤即時性之實務評估。",
            "modelAnswer": r"""
<h4>一、破題：行動交易時代之弱網傳輸挑戰</h4>
<p>隨著智慧型手機成為投資人看盤下單的主要載體，行動網路環境（4G/5G、公共 Wi-Fi、捷運地下道）具備<strong>高隨機丟包率、頻寬劇烈抖動與基地台切換頻繁</strong>之物理特性。傳統網際網路通訊協定（TCP ＋ TLS 1.2/1.3 ＋ HTTP/1.1 或 HTTP/2）建立於有線網路穩定假設之上。在行動弱網環境下，TCP 之協定缺陷常導致看盤畫面凍結、下單點擊逾時。<strong>IETF 官方標準 QUIC（RFC 9000，HTTP/3 底層傳輸協定）</strong>以顛覆性設計重構傳輸層，成為次世代金融行動通訊之救星。</p>

<h4>二、傳統 TCP 在行動環境之三大致命缺陷</h4>
<ol>
  <li><strong>傳輸層隊頭阻塞（Head-of-Line Blocking, HoL Blocking）</strong>：
    <ul>
      <li>HTTP/2 雖支援多路複用，但在單一 TCP 連線上，所有資料流共用同一個滑動視窗。</li>
      <li>若網路發生 1% 隨機丟包，即便遺失的只是背景非關鍵圖形封包，<strong>TCP 必須暫停整條連線的所有後續封包遞交</strong>，等待超時重傳（ACK），導致前端即時報價與急迫下單委託同步卡死。</li>
    </ul>
  </li>
  <li><strong>高握手延遲（High Handshake Latency）</strong>：
    <ul>
      <li>建立全新安全連線需歷經：TCP 三向交握（1 RTT）＋ TLS 1.3 握手（1 RTT），合計至少 <strong>2 個往返時間（2 RTT）</strong>。在跨區或行動弱網下，延遲常高達 200~500 毫秒。</li>
    </ul>
  </li>
  <li><strong>連線中斷重連（Connection Severance）</strong>：
    <ul>
      <li>TCP 以<strong>「四元組（來源 IP、來源 Port、目的 IP、目的 Port）」</strong>標識連線。投資人離開家門由 Wi-Fi 切換為 5G 時，手機 IP 改變，TCP 連線瞬間強制中斷（RST），必須重新握手並重新認證下單工作階段。</li>
    </ul>
  </li>
</ol>

<h4>三、QUIC 架構原理：UDP 封裝與獨立資料流</h4>
<pre><code class="language-text">  傳統 HTTP/2 over TCP:
  [Stream A (下單)] [Stream B (行情)] [Stream C (走勢圖)]
  ───────────┬────────────────────────────────────────
             │ (單一封包遺失 ──> 整體 TCP 連線全部凍結停頓！)
             ▼
  QUIC / HTTP/3 over UDP:
  [Stream A (下單)] ───> 獨立滑動視窗 (單獨遞交，零延遲)
  [Stream B (行情)] ───> 獨立滑動視窗 (單獨遞交，零延遲)
  [Stream C (走勢圖)] ──> (封包遺失 ──> 僅 Stream C 重傳，完全不影響 A 與 B！)</code></pre>
<ul>
  <li><strong>基於 UDP 打造之現代傳輸層</strong>：QUIC 於使用者空間實現可靠傳輸、擁塞控制與排序機制，避免受限於 Linux 核心升級週期緩慢之問題。</li>
  <li><strong>消除傳輸層隊頭阻塞</strong>：QUIC 在單一連線內劃分多個邏輯上<strong>彼此完全獨立的資料流（Stream）</strong>。若 Stream C 的走勢圖封包遺失，僅 Stream C 進行重傳；核心交易下單（Stream A）與即時最佳五檔報價（Stream B）之封包由作業系統即刻正常遞交處理，達成完全解耦。</li>
</ul>

<h4>四、0-RTT 極速建連與深度安全整合</h4>
<p>QUIC 將傳輸層握手與 TLS 1.3 密碼學握手<strong>合併為單一階段</strong>：</p>
<ol>
  <li><strong>1-RTT 初次連線</strong>：首次連線時，QUIC 在單一往返（1 RTT）內同時完成傳輸參數協商與 TLS 1.3 金鑰交換，連線速度較傳統 TCP 提升一倍。</li>
  <li><strong>0-RTT 再次連線（Zero Round-Trip Time）</strong>：
    <ul>
      <li>投資人在 App 再次連線時，利用前次會話快取之預共享金鑰（PSK, Pre-Shared Key）。</li>
      <li><strong>客戶端發送的第一個 UDP 封包中，即可直接夾帶加密後的委託下單請求（0-RTT Data）</strong>，下單延遲直降為純物理傳播時間，大幅提高搶單成功率。</li>
      <li><strong>防範重放攻擊（Anti-Replay）</strong>：針對 0-RTT 金融下單請求，伺服器端必須在應用層嚴格落實 Nonce 與單調遞增委託序號校驗，防止封包被黑客側錄重播。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：Connection ID 無感連線遷移與落地評估</h4>
<ul>
  <li><strong>連線遷移（Connection Migration）</strong>：QUIC 改以 64 位元之<strong>「連線識別碼（Connection ID）」</strong>標記連線。當行動裝置在 Wi-Fi 與 5G 之間跳轉時，即便 IP 與 Port 變動，只要 Connection ID 相同，<strong>連線絕不斷開，無需重新握手</strong>，下單看盤平滑如絲。</li>
  <li><strong>證交所落地實務評估</strong>：建議證交所將 QUIC/HTTP/3 部署於行動下單 API 閘道器與 Web 行情推播前端。針對內部撮合主機間仍維持固定專線 TCP/Kernel Bypass，達成「外網行動端走 QUIC 抗弱網、內網骨幹走 Kernel Bypass 追極限」之最優架構。</li>
</ul>
            """,
            "examinerTips": "得分關鍵詞：『TCP 傳輸層隊頭阻塞 HoL Blocking』、『QUIC RFC 9000 基於 UDP 使用者空間協定』、『獨立資料流 Streams 徹底消除隊頭阻塞』、『0-RTT 極速交握與 PSK 防重放』、『Connection ID 達成 Wi-Fi/5G 無感連線遷移』、『外網 QUIC 抗弱網＋內網 Kernel Bypass 追極限』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>TCP 行動痛點（6分）</strong>：深入解構隊頭阻塞、2 RTT 握手延遲及四元組切換斷線之根因。</li>
  <li><strong>QUIC 多路複用原理（7分）</strong>：繪製清晰对比圖，闡釋基於 UDP 之獨立資料流滑動視窗機制。</li>
  <li><strong>0-RTT 與安全整合（7分）</strong>：精確指出 TLS 1.3 深度合併、PSK 原理及金融防重放機制。</li>
  <li><strong>連線遷移與落地結論（5分）</strong>：闡述 Connection ID 物理優勢，並給出內外網分層架構建議。</li>
</ul>
            """
        },

        # sn-essay-42: DWDM Optical Fiber
        {
            "id": "sn-essay-42",
            "category": "sysnet",
            "chapter": "第 2 章：金融專屬網路拓撲與行情多點廣播（Multicast）",
            "title": "證交所骨幹網路光纖 DWDM（波分複用）與板橋-台北主備機房超低延遲直連架構規劃",
            "summary": "計算光纖每公里約 5 微秒物理傳播延遲、DWDM 多波長傳輸、光保護倒換（APS）50 毫秒內自癒切換，以及最小化色散補償與放大器跳數之雙活專線設計。",
            "points": 25,
            "rubric": "1. 光纖傳播物理極限推導與延遲計算公式 (6分)；2. 密集波分複用（DWDM）技術原理與頻寬架構 (7分)；3. 幾何最短光纜路徑規劃與消除光電轉換（O-E-O）延遲 (7分)；4. 光保護倒換（APS < 50ms）與雙活機房高可用結論 (5分)",
            "question": "證交所板橋核心主機房與台北第一備援機房之間需進行資料庫即時雙活同步與微秒級委託鏡像。試申論：(1) 光纖物理傳播延遲之物理極限推導（光在真空速率約 300,000 km/s，在玻璃纖維折射率 n≈1.468 下之傳播速度約 204,000 km/s，每公里延遲約 4.9 微秒）；(2) 密集波分複用（DWDM）技術原理：單一光纖對同時傳輸多個波長（C-band / L-band）達成 Tbps 級骨幹傳輸；(3) 超低延遲直連光纖路由之幾何路徑最佳化與減少光電轉換（O-E-O）次數；(4) 光保護倒換系統（APS, Optical Protection Switching）在 50 毫秒內完成斷纖自癒切換之高可用設計。",
            "modelAnswer": r"""
<h4>一、破題：跨機房金融雙活之物理極限考驗</h4>
<p>在證交所規劃「板橋主資料中心」與「台北第一備援機房」之雙活（Active-Active）或同步熱備（Hot Standby）架構中，資料庫交易日誌（WAL）鏡像與分散式共識（Raft）受限於<strong>物理光速定律</strong>。任憑軟體演算法如何極致調校，資料跨機房傳輸之延遲下限完全由光在玻璃纖維中的傳播速率決定。建構<strong>「超低延遲裸光纖（Dark Fiber）＋ 密集波分複用（DWDM）」</strong>骨幹直連通道，是突破機房空間束縛之基石工程。</p>

<h4>二、光纖傳播物理極限與延遲嚴格推導</h4>
<ol>
  <li><strong>光在介質中的傳播速率</strong>：
    <ul>
      <li>真空中的光速為 $c \approx 300,000\text{ km/s}$。</li>
      <li>標準單模石英光纖（如 ITU-T G.652D）之纖芯玻璃折射率為 $n \approx 1.468$。</li>
      <li>光在光纖中的真實傳播速度為：
        $$v = \frac{c}{n} = \frac{300,000}{1.468} \approx 204,360\text{ km/s}$$
      </li>
    </ul>
  </li>
  <li><strong>每公里傳播時延計算</strong>：
    <ul>
      <li>每公里單向傳播時延為：
        $$t = \frac{1\text{ km}}{204,360\text{ km/s}} \approx 4.893\text{ 微秒/公里}\ (\approx 4.9\ \mu\text{s/km})$$
      </li>
      <li><strong>往返延遲（RTT）</strong>：每公里雙向 RTT 約為 <strong>$9.8\ \mu\text{s}$</strong>。</li>
    </ul>
  </li>
  <li><strong>板橋至台北實務測算</strong>：若板橋至台北之道路光纜佈線距離為 25 公里，則光在光纖內的純物理往返時間即為：$25 \times 9.8\ \mu\text{s} \approx 245\ \mu\text{s}$。</li>
</ol>

<h4>三、密集波分複用（DWDM）技術原理與容量擴展</h4>
<pre><code class="language-text">  [板橋主機房]                                                   [台北備援機房]
  ├── 業務系統 A (100GbE) ──> [λ1: 1550.12nm] ┐             ┌──> [λ1] ──> 業務系統 A
  ├── 撮合日誌 WAL (100GbE) ─> [λ2: 1550.92nm] ┼─ (單一光纖對) ─┼──> [λ2] ──> 撮合鏡像
  └── 儲存同步 SAN (32G FC) ─> [λ3: 1551.72nm] ┘  DWDM 光鏈路 └──> [λ3] ──> 儲存鏡像</code></pre>
<ul>
  <li><strong>波長分割多工原理</strong>：利用光學合波器（Multiplexer, Mux），在 C-band（約 1530~1565nm）視窗內，以極窄之頻道間隔（如 50GHz / 100GHz 柵格，約 0.8nm）同時將 40~96 個不同波長（$\lambda_1 \sim \lambda_{96}$）之獨立光信號注入同一對玻璃光纖中傳輸。</li>
  <li><strong>協議透明與超高頻寬</strong>：DWDM 屬於物理層純光學傳輸，對上層協定完全透明。單一光纖對可同時混載 100GbE 乙太網、Fibre Channel（FC-32G/64G）儲存網路與 InfiniBand，總骨幹頻寬輕鬆突破數十 Tbps。</li>
</ul>

<h4>四、超低延遲直連光纖路由工程規劃</h4>
<ol>
  <li><strong>幾何最短路徑選擇（Physical Route Optimization）</strong>：
    <ul>
      <li>嚴禁租用繞經多個電信局端（CO）之傳統環狀迴路。證交所應向電信業者專屬包租<strong>點對點直達暗光纖（Point-to-Point Dark Fiber）</strong>，依據鐵道、捷運或主幹道路沿線鋪設，將實體光纖長度壓縮至物理幾何極限。</li>
    </ul>
  </li>
  <li><strong>消除光電光（O-E-O）轉換開銷</strong>：
    <ul>
      <li>中間節點全面採用<strong>可重構光加減多工器（ROADM, Reconfigurable Optical Add-Drop Multiplexer）</strong>進行全光學交換（All-Optical Switch），避免在中間局端進行「光轉電、電轉光」之數位再生處理，將中間節點延遲由微秒級壓降至納秒級。</li>
    </ul>
  </li>
  <li><strong>最小化色散補償延遲</strong>：淘汰傳統色散補償光纖（DCF，其額外增加數公里傳播時延），改採<strong>同調數位訊號處理器（Coherent DSP）</strong>進行電子色散補償（EDC），零延遲消除色散效應。</li>
</ol>

<h4>五、結論：光保護倒換（APS < 50ms）與金融雙活</h4>
<p>在板橋與台北之間鋪設<strong>「實體完全相異路由（Physically Diverse Dual-Route）」</strong>之雙路暗光纖（主路沿新北環快、備路沿台鐵地下隧道）。部署<strong>光保護倒換系統（APS, Optical Protection Switching）</strong>：</p>
<ul>
  <li><strong>雙發選收機制（1+1 Optical Protection）</strong>：發送端將光信號複製至主備兩條光纜同時傳送，接收端即時監測光功率。</li>
  <li><strong>< 50ms 無感自癒</strong>：一旦主路光纜因道路施工遭挖斷，接收端硬體光學開關在 <strong>20~50 毫秒內自動切換至備用光纖</strong>，上層 TCP 與資料庫連線完全不中斷，建構國家級金融骨幹最高可靠神盾。</li>
</ul>
            """,
            "examinerTips": "得分關鍵詞：『光在光纖速度 204,000 km/s，每公里單向延遲 4.9 微秒』、『雙向 RTT 約 9.8 微秒/公里計算公式』、『DWDM C-band 50GHz 窄通道間隔多工』、『點對點直連暗光纖 Dark Fiber』、『ROADM 全光交換消除 O-E-O 光電轉換』、『1+1 APS 光保護倒換 < 50ms 自動自癒』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>物理延遲嚴格推導（6分）</strong>：以折射率 n=1.468 推導出 204,000 km/s 及 4.9μs/km，展現扎實科學素養。</li>
  <li><strong>DWDM 技術原理（7分）</strong>：深入解構光波長多工、C-band 頻譜及協議透明性。</li>
  <li><strong>超低延遲路由工程（7分）</strong>：條列清晰指出最短幾何路徑、ROADM 全光傳輸與 DSP 電子色散補償。</li>
  <li><strong>APS 容災結論（5分）</strong>：提出 1+1 雙發選收與 < 50ms 自癒切換，支撐金融雙活高可用。</li>
</ul>
            """
        },

        # sn-essay-43: Saga vs TCC Distributed Transactions
        {
            "id": "sn-essay-43",
            "category": "sysnet",
            "chapter": "第 6 章：分散式交易、雙活資料庫與高可用叢集",
            "title": "資料庫分散式交易：Saga 模式與 TCC（Try-Confirm-Cancel）在跨證券交割服務之最終一致性實踐",
            "summary": "對比 2PC 兩階段提交之效能瓶頸，深入闡述 TCC 模式預留資源與 Saga 補償機制在跨結算機構金融交易之狀態機設計與冪等性（Idempotence）保證。",
            "points": 25,
            "rubric": "1. 傳統 2PC 兩階段提交於微服務高併發架構之致命瓶頸 (6分)；2. TCC（Try-Confirm-Cancel）三階段資源隔離與原子性運作機制 (7分)；3. Saga 模式（正向執行 ＋ 補償交易）與協調器狀態機設計 (7分)；4. 冪等性（Idempotency）、空補償與防懸掛實務結論 (5分)",
            "question": "證券交易涉及集保結算、交割結算銀行、經紀商與交易所多個異質分散式系統。傳統 2PC（兩階段提交）由於長期鎖定全域資源，在微服務高併發架構下極易造成系統阻塞。試申論：(1) 傳統 2PC 兩階段提交之效能瓶頸（同步鎖定資源、協調者單點故障、資料不一致盲區）；(2) TCC（Try-Confirm-Cancel）模式之三階段運作原理：業務層資源預留、確認提交與補償釋放；(3) Saga 模式（正向交易鏈 + 反向補償鏈）在跨機構非同步長事務（Long-running Transaction）之狀態機編排（Orchestration vs Choreography）；(4) 分散式交易面對網路重試之「冪等性（Idempotence）」、「防懸掛（Anti-hanging）」與「空補償處理」之工程實踐。",
            "modelAnswer": r"""
<h4>一、破題：分散式微服務架構與金融資料一致性困境</h4>
<p>在傳統單體（Monolithic）架構中，金融交易依賴關聯式資料庫之本地事務（Local ACID）即可保證一致性。然而，現代證券交割與清算體系跨越<strong>【證交所撮合系統】 ➔ 【臺灣集中保管結算所（TDCC）股票劃撥】 ➔ 【交割結算銀行金流扣款】</strong>等多個獨立異質系統。在分散式網路下，CAP 定理表明無法同時達成強一致性與高可用性。如何在放棄全域強鎖定的前提下，確保跨系統資產之<strong>「最終一致性（Eventual Consistency）」</strong>，是金融架構師之核心考驗。</p>

<h4>二、傳統 2PC（兩階段提交）之死穴解構</h4>
<ol>
  <li><strong>全域資源同步鎖定（Lock Contention）</strong>：在 Phase 1（Prepare）至 Phase 2（Commit）期間，所有參與者資料庫必須持有行級鎖（Row Lock）。在高頻交割時，鎖定等待導致資料庫連線池瞬間枯竭。</li>
  <li><strong>協調者單點故障（Single Point of Failure）</strong>：若協調者（Coordinator）在發出 Prepare 成功後崩潰，所有參與者將無限期掛起（Blocking），資源無法釋放。</li>
  <li><strong>網路分區盲區</strong>：若 Phase 2 時部分節點網路斷線，導致部分 Commit、部分超時，破壞資料一致性。</li>
</ol>

<h4>三、TCC 模式：業務層資源預留與強隔離</h4>
<p>TCC 不依賴資料庫底層 XA 鎖，而是在<strong>「業務應用層」</strong>實現兩階段控制：</p>
<pre><code class="language-text">  [交割客戶帳戶]
        │
        ├── 1. Try 階段 (預留資源) ──> 可用餘額 -100萬，凍結金額 +100萬 (餘額充足即可成功)
        │
        ├── 2. Confirm 階段 (確認) ──> 凍結金額 -100萬，完成實質款項劃撥 (不再做業務檢核)
        │
        └── 3. Cancel 階段 (取消) ───> 凍結金額 -100萬，可用餘額 +100萬 (釋放預留款項)</code></pre>
<ul>
  <li><strong>Try 階段（檢查與預留）</strong>：完成所有業務檢查（一致性檢查），並<strong>「預留（Reserve）」</strong>業務資源。例如：證券帳戶先將股票狀態改為「待交割凍結」，而非直接扣除。此時其他交易仍可正常併發，不產生全域鎖阻塞。</li>
  <li><strong>Confirm 階段（確認執行）</strong>：若所有微服務的 Try 皆成功，協調者發起 Confirm。Confirm 只使用 Try 預留的資源，不做任何業務檢查，業務上保證必定成功。</li>
  <li><strong>Cancel 階段（取消與釋放）</strong>：若任一微服務 Try 失敗，協調者發起 Cancel，釋放 Try 階段預留的資源，恢復原狀。</li>
</ul>

<h4>四、Saga 模式：長事務補償狀態機</h4>
<p>針對跨機構（交易所、銀行、集保）耗時數秒至數分鐘之<strong>長事務（Long-running Transaction）</strong>，TCC 長期凍結資源成本過高，宜採用 <strong>Saga 模式</strong>：</p>
<ol>
  <li><strong>正向事務鏈與補償事務鏈</strong>：
    <ul>
      <li>將分散式大事務拆解為 $N$ 個循序執行的子事務：$T_1, T_2, \dots, T_n$。</li>
      <li>每個子事務皆對應一個反向的<strong>補償事務（Compensating Transaction）</strong>：$C_1, C_2, \dots, C_n$。</li>
      <li>若執行至 $T_3$ 失敗，Saga 協調器自動依序倒序觸發 $C_2, C_1$ 進行衝銷（如已扣除銀行款項則發起退款入帳），達成業務最終一致。</li>
    </ul>
  </li>
  <li><strong>編排器模式（Orchestration）</strong>：金融系統首選集中式狀態機編排器（如 Temporal 或 AWS Step Functions 架構）。編排器精準維護狀態持久化日誌，便於審計與異常人工介入。</li>
</ol>

<h4>五、結論：分散式交易三大工程防禦鐵律</h4>
<p>在不可靠網路環境中，分散式交易框架必須在程式碼層面落實三大鐵律：</p>
<ul>
  <li><strong>冪等性（Idempotence）</strong>：網路超時重試極為普遍。Confirm 與 Cancel 介面必須依據<strong>「全域唯一交易流水號（Global TxID）」</strong>進行去重校驗，保證「相同指令重複調用一次或十次，業務結果完全一致」。</li>
  <li><strong>防懸掛（Anti-hanging）</strong>：因網路延遲，Cancel 請求可能比 Try 請求更早抵達目標伺服器。若 Cancel 發現事務尚未 Try，必須先寫入一筆「已取消標記」，後續延遲抵達的 Try 看到標記必須直接拒絕執行，嚴防資源遭永久懸掛。</li>
  <li><strong>空補償處理（Empty Compensation）</strong>：若 Try 請求根本未抵達或直接超時失敗，此時發起的 Cancel 必須識別為空補償，平滑回傳成功，不得拋出異常。</li>
</ul>
<p>透過 TCC 處理極致微秒撮合內存資源、Saga 處置跨銀行盤後交割清算，證交所構築了固若金湯之分散式金融帳本體系。</p>
            """,
            "examinerTips": "得分關鍵詞：『2PC 全域鎖阻塞與協調者單點故障』、『TCC 業務層資源預留 Try-Confirm-Cancel』、『Saga 正向交易鏈與反向補償事務 (T1~Tn / C1~Cn)』、『Orchestration 狀態機集中編排』、『分散式三大防禦鐵律：冪等性 Idempotence』、『防懸掛 Anti-hanging』、『空補償 Empty Compensation 處理』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>2PC 缺陷剖析（6分）</strong>：深入解構行級鎖鎖定、連線枯竭及協調者崩潰之架構死穴。</li>
  <li><strong>TCC 運作機制（7分）</strong>：條列清晰闡述 Try 預留、Confirm 放行與 Cancel 回滾之無鎖隔離設計。</li>
  <li><strong>Saga 長事務架構（7分）</strong>：精確推導正向與反向補償鏈，對比 Orchestration 編排器之金融優勢。</li>
  <li><strong>三大工程鐵律結論（5分）</strong>：深入辨析冪等性、防懸掛與空補償，展現頂級金融工程落地深度。</li>
</ul>
            """
        },

        # sn-essay-44: Redis Cluster Caching
        {
            "id": "sn-essay-44",
            "category": "sysnet",
            "chapter": "第 1 章：撮合核心與超低延遲系統架構（Kernel Bypass 與記憶體優化）",
            "title": "高效能記憶體資料庫 Redis Cluster 在逐筆撮合委託單快顯緩存與防崩潰（雪崩/穿透/擊穿）之架構",
            "summary": "剖析 16384 個 Hash Slot 分片、Sentinel 哨兵機制、布隆過濾器（Bloom Filter）防穿透、互斥鎖（Mutex）防擊穿與雙活快顯預熱之金融實務部署。",
            "points": 25,
            "rubric": "1. Redis Cluster 16,384 虛擬槽（Hash Slot）與 CRC16 分片分佈機制 (6分)；2. 快取穿透（Cache Penetration）成因與布隆過濾器（Bloom Filter）防護 (7分)；3. 快取擊穿（Breakdown）互斥鎖 vs 快取雪崩（Avalanche）隨機 TTL 抖動 (7分)；4. 跨機房雙活快顯預熱與高可用 Sentinel 容災實務結論 (5分)",
            "question": "證交所前置系統採用分散式記憶體快取（如 Redis Cluster）儲存證券行情快照、委託單查詢快取與靜態證券主檔。試申論：(1) Redis Cluster 虛擬槽（16,384 Hash Slots）分片架構、Gossip 協議節點通訊與 Master-Slave 自動故障轉移（Failover）機制；(2) 快取穿透（Cache Penetration）成因及布隆過濾器（Bloom Filter）在下單前端之攔截防護；(3) 快取擊穿（Cache Breakdown）成因及互斥鎖（Mutex Key）與熱點資料邏輯過期永不過期預熱機制；(4) 快取雪崩（Cache Avalanche）成因及隨機 TTL 抖動（TTL Jitter）與多副本跨機房部署防護實務。",
            "modelAnswer": r"""
<h4>一、破題：記憶體快取在金融高頻查詢之核心價值</h4>
<p>在證交所極致交易環境中，後端關聯式資料庫（RDBMS）的磁碟 I/O 吞吐量有限。盤中數百萬投資人每秒高頻刷新「最佳五檔行情」、「個股即時委託量」與「帳戶下單權限」，高達 95% 以上之查詢請求由記憶體資料庫（如 <strong>Redis Cluster</strong>）直接吸收。然而，快取一旦設計不良遭遇崩潰，海量查詢流量將瞬間如水壩決堤般灌入後端資料庫，造成骨牌效應引發金融交易停擺。建構具備<strong>「自適應防崩潰防禦」之 Redis 叢集</strong>至關重要。</p>

<h4>二、Redis Cluster 虛擬槽分片與高可用機制</h4>
<ol>
  <li><strong>16,384 虛擬槽（Hash Slots）分片演算法</strong>：
    <ul>
      <li>Redis 將整個鍵空間劃分為固定的 <strong>16,384 個 Slot</strong>。</li>
      <li>儲存或查詢鍵時，計算公式為：
        $$\text{Slot} = \text{CRC16}(\text{Key}) \pmod{16384}$$
      </li>
      <li>若業務要求多個相關鍵必須分配在同一節點（如同一檔股票之行情與委託簿），可使用 <strong>Hash Tag</strong>，如 `{2330}.quote` 與 `{2330}.order`，系統僅對大括號內之字串計算雜湊，保證落在同一節點以支援微秒級管線批量操作。</li>
    </ul>
  </li>
  <li><strong>Gossip 協定與自動故障轉移（Failover）</strong>：
    <ul>
      <li>節點間透過 Gossip 協定定時交換 PING/PONG 心跳資訊。</li>
      <li>當某個 Master 節點失聯超過 `cluster-node-timeout`（如 1 秒），過半數 Master 標記其為 `FAIL`。其對應之 Slave 節點自動發起選舉，在 <strong>1~2 秒內平滑晉升為新 Master</strong>，全自動恢復槽位對外服務。</li>
    </ul>
  </li>
</ol>

<h4>三、快取穿透（Cache Penetration）與布隆過濾器防禦</h4>
<pre><code class="language-text">  [查詢請求 (證券代號)] ──> [布隆過濾器 (Bloom Filter)]
                                     │
                 ┌───────────────────┴───────────────────┐
                 │ (未命中：代表代號 100% 絕對不存在)     │ (命中：可能存在)
                 ▼                                       ▼
          [直接返回 404 錯誤]                    [查詢 Redis 快取]
          (完全不查 Redis/DB)                            │ (快取未命中 Miss)
                                                         ▼
                                                [查詢後端核心資料庫]</code></pre>
<ul>
  <li><strong>穿透成因</strong>：黑客或惡意爬蟲故意大量發送<strong>「系統中根本不存在的代碼」</strong>（如查詢不存在之股票代號 `99999` 或惡意隨機 UUID）。快取無此資料，請求每次皆直接穿透快取擊打後端資料庫，引發資料庫 CPU 100% 癱瘓。</li>
  <li><strong>布隆過濾器（Bloom Filter）硬核防護</strong>：
    <ul>
      <li>在 API 閘道器或 Redis 前端部署布隆過濾器，利用多個雜湊函數將全市場所有合法的千檔股票代號映射至 Bit Array（位元陣列）。</li>
      <li><strong>特性</strong>：若布隆過濾器判定不存在，則該代號<strong>「必定 100% 不存在」</strong>，直接在前端阻斷返回錯誤，請求完全不進入 Redis 與資料庫；僅極少數誤判（False Positive）放行查詢。</li>
    </ul>
  </li>
  <li><strong>空值快取（Cache Null Object）</strong>：對極少數穿透但確認不存在的資料，將空值 `null` 寫入 Redis 並設定極短過期時間（如 30 秒），防止相同無效查詢持續穿透。</li>
</ul>

<h4>四、快取擊穿（Breakdown）與快取雪崩（Avalanche）立體防禦</h4>
<ol>
  <li><strong>快取擊穿（熱點 Key 瞬間過期）防護</strong>：
    <ul>
      <li><strong>成因</strong>：某檔超熱門權值股（如台積電 2330）為全市場關注焦點，併發查詢達數萬 QPS。當其快取 TTL 到期失效之瞬間，數萬個並發查詢同時撲向資料庫。</li>
      <li><strong>互斥鎖（Mutex Key）機制</strong>：快取未命中時，僅允許第一個獲得分散式互斥鎖（`SET key value NX PX 1000`）的執行緒前往資料庫重載資料並回填 Redis；其餘執行緒原地短暫等待（Sleep 20ms）後重試，將資料庫負載嚴格壓降為 1。</li>
      <li><strong>邏輯過期（永不過期）架構</strong>：熱點資料實體上不設 TTL，而是在 JSON Value 內嵌入邏輯時間戳記。背景執行緒非同步定期檢查並提前預熱更新快取，達成前台讀取永遠命中。</li>
    </ul>
  </li>
  <li><strong>快取雪崩（巨量 Key 同時集體失效）防護</strong>：
    <ul>
      <li><strong>成因</strong>：系統若在開盤前批量預熱全市場資料，並統一設定相同的過期時間（如 1 小時）。開盤後 1 小時整，數萬筆資料同時失效，造成後端瞬間崩潰。</li>
      <li><strong>TTL 隨機抖動（TTL Jitter）</strong>：在基礎過期時間上加上一個隨機偏移行（例如：原本 3600 秒，隨機調整為 `3600 + rand(0, 300)` 秒），讓快取資料在時間軸上均勻散開失效。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：跨機房雙活預熱與高可用結論</h4>
<p>在證交所生產維運規範中，每日 8:00 盤前啟動<strong>「自動化快取預熱流水線」</strong>，將全體證券代碼、前日收盤價、漲跌停限制等靜態主檔提前注入板橋與台北兩地 Redis 叢集。透過主從雙活、記憶體預分配（`maxmemory` + `volatile-lru`）與嚴格的防崩潰四道防線，構築堅不可摧的金融低延遲快取基石。</p>
            """,
            "examinerTips": "得分關鍵詞：『Redis Cluster 16384 Hash Slots 與 CRC16 演算法』、『Hash Tag {tag} 綁定同一節點』、『布隆過濾器 Bloom Filter 阻斷快取穿透』、『互斥鎖 Mutex NX PX 解決熱點擊穿』、『邏輯過期永不過期預熱』、『TTL Jitter 隨機抖動化解快取雪崩』、『盤前自動化快取預熱流水線』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>分片與高可用原理（6分）</strong>：深入辨析 16384 槽位計算、Hash Tag 聚合及 Gossip 容災機制。</li>
  <li><strong>快取穿透防禦（7分）</strong>：繪製清晰流程圖，詳述布隆過濾器位元陣列與空值短效快取之雙重保險。</li>
  <li><strong>擊穿 vs 雪崩對比（7分）</strong>：清楚辨析擊穿（單一熱點）與雪崩（集體失效）本質，提出 Mutex 與 TTL Jitter 解決方案。</li>
  <li><strong>金融實務結論（5分）</strong>：結合 8:00 盤前預熱與 LRU 淘汰策略，展現證交所生產落地規範。</li>
</ul>
            """
        },

        # sn-essay-45: Microservice Adaptive Rate Limiting
        {
            "id": "sn-essay-45",
            "category": "sysnet",
            "chapter": "第 8 章：雲原生儲存、高可用叢集與微突發流量防禦",
            "title": "微服務架構流量治理：自適應限流（Adaptive Rate Limiting）與熔斷降級（Circuit Breaker）在開盤微突發之防護",
            "summary": "分析開盤 9:00 之極端百倍微突發流量，規劃滑動視窗令牌桶（Token Bucket）、Sentinel 自適應動態過載保護、熔斷降級狀態機（Closed/Open/Half-Open）與柔性降級策略。",
            "points": 25,
            "rubric": "1. 臺股開盤 9:00:00 微突發（Microburst）流量特徵與靜態限流之盲區 (6分)；2. 自適應限流（Adaptive Limiting）借鑑 BBR 演算法之容量動態推導 (7分)；3. 熔斷器（Circuit Breaker）三態狀態機轉換與慢呼叫比例阻斷 (7分)；4. 核心撮合優先保障與非核心柔性降級實務結論 (5分)",
            "question": "每日上午 8:30~9:00 臺股盤前試撮與 9:00 開盤瞬間，大量量化交易程式與散戶委託湧入，瞬間流量常達到平時數十至百倍（微突發 Microburst）。試申論：(1) 傳統漏桶（Leaky Bucket）與令牌桶（Token Bucket）靜態限流在極端突發流量下之侷限性；(2) 借鑑 TCP BBR 演算法之「自適應限流（Adaptive Rate Limiting）」架構原理（依據 CPU 核心負載、記憶體排隊延遲與即時 inflight 請求動態調整系統通行窗口）；(3) 熔斷器（Circuit Breaker）三種狀態（Closed, Open, Half-Open）轉換機制與對下游故障依賴服務之快速失敗保護；(4) 盤中非核心業務（如歷史報表匯出、靜態新聞查詢）之柔性降級策略，確保核心下單撮合專用頻寬與計算資源。",
            "modelAnswer": r"""
<h4>一、破題：開盤瞬間「微突發（Microburst）」對交易系統之衝擊</h4>
<p>臺灣證券市場每日上午 <strong>9:00:00.000 開盤瞬間</strong>，全臺數十萬投資人與量化高頻演算法搶先掛單，瞬間湧入之委託流量常達到日常平均之 <strong>50 至 100 倍</strong>。這種持續時間僅數百毫秒至數秒之極端流量衝擊被稱為<strong>「微突發（Microburst）」</strong>。若系統缺乏靈活流量治理，後端交易微服務將因佇列溢位、線程池耗盡而陷入雪崩。必須構建<strong>「自適應動態限流」＋「熔斷降級」</strong>之立體防護網。</p>

<h4>二、傳統靜態限流模型之盲區與瓶頸</h4>
<ol>
  <li><strong>靜態閥值之兩難</strong>：
    <ul>
      <li>傳統<strong>令牌桶（Token Bucket）</strong>或<strong>漏桶（Leaky Bucket）</strong>演算法要求工程師預先設定靜態 QPS 上限（如 `rate = 10,000/s`）。</li>
      <li><strong>閥值設太高</strong>：當伺服器因硬體異常或 GC 停頓導致處理能力驟降時，靜態限流無法感知，過量流量仍灌入系統導致崩潰。</li>
      <li><strong>閥值設太低</strong>：在伺服器硬體處於低負載、尚有大量算力餘裕時，合法委託卻被粗暴拒絕，損害市場交易公平性。</li>
    </ul>
  </li>
  <li><strong>無法應對波動性</strong>：靜態規則無法依據「目前每筆交易處理耗時之長短」即時動態調整。</li>
</ol>

<h4>三、自適應限流（Adaptive Limiting）核心演算法原理</h4>
<pre><code class="language-text">  [系統執行期遙測中樞]
     ├── CPU 核心負載 (System Load / CPU Usage)
     ├── 請求平均反應時間 (Average Response Time, RT)
     └── 即時通行請求數 (Inflight Requests)
           │
           ▼ (借鑑利特爾法則 Little's Law 與 BBR 演算法動態計算)
  ┌────────────────────────────────────────────────────────┐
  │ 自適應通行容量上限 = MaxQPS * MinRT * SystemStatusCoeff │
  └────────────────────────┬───────────────────────────────┘
                           │ (動態裁決)
                           ├── 正常安全水位 ──> 平滑全速放行
                           └── 負載超標臨界 ──> 拋棄多餘請求 (快速失敗 Fast-Fail)</code></pre>
<ul>
  <li><strong>借鑑 TCP BBR 演算法與利特爾法則（Little's Law）</strong>：
    <ul>
      <li>系統依據在線統計之歷史最佳表現，動態推導當前主機能夠承載的最大在線併發數：
        $$\text{MaxInflight} = \text{MaxQPS} \times \text{MinRT}$$
      </li>
      <li>$\text{MaxQPS}$ 為過去一段時間內系統測得之最大處理能力，$\text{MinRT}$ 為系統最低平穩反應時間。</li>
    </ul>
  </li>
  <li><strong>CPU 負載水線聯動（如 Sentinel 動態保護）</strong>：
    <ul>
      <li>即時監控作業系統 Load 與 CPU 使用率。當 CPU 負載超過 <strong>80% 安全警戒線</strong> 時，系統自動切換為防護模式，僅允許 $\text{Inflight} \le \text{MaxInflight}$ 之請求通過，其餘流量在入口處立刻快速失敗（Fast-Fail），保護核心不被壓垮。</li>
    </ul>
  </li>
</ul>

<h4>四、熔斷器（Circuit Breaker）狀態機運作機制</h4>
<p>針對分散式架構中下游依賴服務（如徵信風控服務、第三方行情源）發生逾時或崩潰：</p>
<ol>
  <li><strong>關閉狀態（Closed，正常通行）</strong>：所有請求正常轉發下游。熔斷器持續統計慢呼叫比例（Slow Call Rate）與異常比例。</li>
  <li><strong>開啟狀態（Open，熔斷阻斷）</strong>：
    <ul>
      <li>當特定時間視窗內，下游服務呼叫耗時超過閾值（如 RT > 100ms）之比例超過 50%，熔斷器<strong>瞬間跳脫為 Open 狀態</strong>。</li>
      <li>所有後續請求<strong>「不再打向下游，直接在本地快速失敗或執行預設降級邏輯」</strong>，避免執行緒無限期阻塞於逾時等待，杜絕連鎖崩潰。</li>
    </ul>
  </li>
  <li><strong>半開狀態（Half-Open，探測復原）</strong>：
    <ul>
      <li>熔斷開啟維持一段冷卻時間（如 5 秒）後，自動切換至 Half-Open 狀態。</li>
      <li>試探性放行少數請求（如 5 筆）轉發至下游。若全數成功且延遲恢復正常，熔斷器自動切換回 <strong>Closed</strong> 恢復全量通訊；若仍失敗則重新退回 <strong>Open</strong> 狀態。</li>
    </ul>
  </li>
</ol>

<h4>五、結論：分級保障與非核心柔性降級實務</h4>
<p>證交所微服務體系劃分四級業務優先級：<strong>【L0 核心撮合】 > 【L1 委託接收與回報】 > 【L2 最佳五檔即時行情】 > 【L3 歷史報表、官網靜態查詢】</strong>。開盤微突發期間：</p>
<ul>
  <li><strong>柔性降級策略</strong>：API 閘道器自動啟動 L3/L2 柔性降級，將歷史帳冊查詢直接回傳「盤中暫停查詢，請盤後再試」，或拉長快取時間；</li>
  <li><strong>算力全力保全</strong>：將釋放出的全體網路頻寬、CPU 與資料庫連線池，<strong>100% 優先傾注於 L0 撮合與 L1 下單核心</strong>，確保資本市場開盤撮合絲滑順暢，維持國家金融市場秩序。</li>
</ul>
            """,
            "examinerTips": "得分關鍵詞：『開盤 9:00:00 百倍微突發 Microburst』、『靜態限流盲區 vs 自適應限流』、『利特爾法則 Inflight = MaxQPS * MinRT』、『Sentinel CPU 80% 動態過載保護』、『熔斷器三態狀態機：Closed、Open、Half-Open 探測』、『慢呼叫比例跳脫』、『四級優先級 (L0~L3) 柔性降級保撮合』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>微突發與靜態限制痛點（6分）</strong>：深入解構 9:00 開盤百倍流量衝擊與靜態閥值之死穴。</li>
  <li><strong>自適應限流演算法（7分）</strong>：給出利特爾法則與 CPU 80% 水線聯動之動態容量推導原理。</li>
  <li><strong>熔斷狀態機轉換（7分）</strong>：條列清晰闡述 Closed -> Open -> Half-Open 之狀態遷移與慢呼叫快速失敗。</li>
  <li><strong>業務分級降級結論（5分）</strong>：劃分 L0~L3 優先級，展現金融級以退為進之系統保全智慧。</li>
</ul>
            """
        },

        # sn-essay-46: In-band Network Telemetry (INT)
        {
            "id": "sn-essay-46",
            "category": "sysnet",
            "chapter": "第 2 章：金融專屬網路拓撲與行情多點廣播（Multicast）",
            "title": "網路微突發監控：In-band Network Telemetry（INT）與高頻緩衝區佇列監控在行情網路微突發之防護",
            "summary": "剖析行情多播微突發造成交換機晶片緩衝區溢位丟包成因，詳述帶內網路遙測（INT）利用 P4 可程式化交換機在封包標頭插入排隊延遲與佇列深度、gNMI 毫秒級遙測與動態緩衝區調校防禦。",
            "points": 25,
            "rubric": "1. 網路微突發（Microburst）物理成因與傳統 SNMP 週期監控失明 (6分)；2. 帶內網路遙測（INT）技術原理：P4 可程式化交換機資料平面遙測 (7分)；3. gNMI / Streaming Telemetry 高頻串流與佇列水線預警架構 (7分)；4. 交換機動態緩衝區分配（Dynamic Buffer Allocation）實務結論 (5分)",
            "question": "在證券行情多播推播與委託下單網路中，微突發（Microburst）常於數百微秒內填滿交換機之封包共享緩衝區（Packet Buffer），導致無預警丟包，而傳統 SNMP 週期輪詢（1~5 分鐘）對此完全失明。試申論：(1) 微突發之物理成因：多埠對單埠（Incast）瞬間突發匯聚與交換機晶片緩衝區溢位；(2) 帶內網路遙測（INT, In-band Network Telemetry）技術原理：利用 P4 可程式化交換機在數據封包頭部動態插入交換機 ID、輸入/輸出埠、佇列延遲與緩衝區佔用深度；(3) 高頻硬體串流遙測（Streaming Telemetry / gNMI）以毫秒級週期主動推送交換機佇列水線之監控架構；(4) 結合動態緩衝區分配（Dynamic Buffer Allocation）與微秒級早期丟包告警之高可靠網路實戰配置。",
            "modelAnswer": r"""
<h4>一、破題：網路封包緩衝區（Packet Buffer）之微秒級風暴</h4>
<p>在證券交易所網路架構中，多播行情發布（Multicast Market Data）與逐筆委託下單流量高度聚集。傳統網路維運團隊經常遭遇一種離奇現象：<strong>「SNMP 監控顯示交換機平均頻寬利用率僅 20%~30%，但交易端點卻頻繁回報 UDP 多播行情丟包與 TCP 逾時重傳」</strong>。此現象背後之元兇即是<strong>「網路微突發（Microburst）」</strong>。傳統以分鐘計之網路監控工具對此毫無知覺，唯有導入<strong>帶內網路遙測（INT）與高頻串流遙測（Streaming Telemetry）</strong>，方能揭開微突發之神秘面紗。</p>

<h4>二、微突發之物理成因：Incast 匯聚與緩衝區耗盡</h4>
<ol>
  <li><strong>多對一瞬間匯聚（Incast Traffic）</strong>：當多個下單節點（例如 48 個 10GbE 輸入埠）同時向單一撮合主機所在之輸出埠（40GbE 或 100GbE 輸出埠）瞬間發送數據時，總瞬時頻寬需求瞬間超過輸出埠實體線速。</li>
  <li><strong>晶片封包快取（Packet Buffer）溢位</strong>：
    <ul>
      <li>交換機晶片（ASIC，如 Broadcom Trident/Tomahawk）內部之共享封包快取容量非常有限（通常僅 16MB~32MB）。</li>
      <li>微突發持續時間通常僅 <strong>50 微秒至 2 毫秒</strong>，在極短瞬間將交換機輸出佇列緩衝區填滿，後續抵達之行情與委託封包直接被<strong>尾端丟棄（Tail-Drop）</strong>。</li>
    </ul>
  </li>
  <li><strong>SNMP 監控之致命盲區</strong>：SNMP 採樣週期通常為 1 分鐘至 5 分鐘。在數分鐘之平均值計算下，數百微秒之暴衝峰值被徹底平滑稀釋，呈現出「看似風平浪靜、實則暗潮洶湧」之假象。</li>
</ol>

<h4>三、帶內網路遙測（INT, In-band Network Telemetry）技術原理</h4>
<pre><code class="language-text">  [原始交易封包 (Payload)] ──> [進網交換機 (Ingress Switch)]
                                        │
                                        ▼ (P4 晶片線速插入 INT 標頭)
  ┌────────────────────────────────────────────────────────┐
  │ IP 標頭 │ INT 標頭：Hop1 ID | In/Out Port | Queue Depth | Hop1 Egress Latency │ Payload │
  └─────────────────────────────┬──────────────────────────┘
                                │ (穿越中間交換機，逐跳追加 INT 遙測中繼資料)
                                ▼
  ┌────────────────────────────────────────────────────────┐
  │ IP 標頭 │ Hop1 INT Metadata │ Hop2 INT Metadata │ Payload                      │
  └─────────────────────────────┬──────────────────────────┘
                                │ (出網交換機剝離標頭並推送遙測分析集線器)
                                ▼
  [出網交換機 (Egress Switch)] ──> [遙測數據鏡像至 Kafka / 時序資料庫]</code></pre>
<ul>
  <li><strong>P4 可程式化資料平面</strong>：INT 基於 P4 語言定義之可程式化交換機晶片（如 Intel Tofino）。在封包以線速（Terabits/sec）穿越交換機晶片內部流水線（Pipeline）時，<strong>硬體直接在封包頭部與 Payload 之間插入微秒級遙測中繼資料（Metadata）</strong>。</li>
  <li><strong>逐跳記錄之遙測指標（Hop-by-Hop Telemetry）</strong>：
    <ul>
      <li><strong>Switch ID & Port ID</strong>：明確記錄封包路徑拓撲。</li>
      <li><strong>佇列佔用深度（Queue Occupancy）</strong>：記錄封包穿越當下，該交換機輸出佇列已佔用之位元組數。</li>
      <li><strong>排隊時延（Queue Egress Latency）</strong>：記錄封包在交換機快取中等待轉發之奈秒級時延。</li>
    </ul>
  </li>
  <li><strong>邊界剝離與零開銷</strong>：在封包離開證交所核心網路抵達終端主機前，邊界交換機自動將 INT 標頭剝離，將真實封包交付伺服器，同時將遙測數據鏡像旁路推播至分析中樞，終端應用完全無感。</li>
</ul>

<h4>四、gNMI 串流遙測與動態緩衝區調校（Dynamic Buffer）</h4>
<ol>
  <li><strong>Streaming Telemetry（gNMI / gRPC）</strong>：
    <ul>
      <li>揚棄舊時代輪詢模式，交換機硬體每 <strong>10 毫秒（甚至亞毫秒級）</strong>主動以 Protocol Buffers 格式將佇列水線數據向外推送至時序資料庫（Prometheus / InfluxDB）。</li>
    </ul>
  </li>
  <li><strong>動態緩衝區分配（Dynamic Buffer Allocation / Alpha Tuning）</strong>：
    <ul>
      <li>設定交換機動態共享緩衝區係數 $\alpha$：
        $$\text{Queue Threshold} = \alpha \times (\text{Remaining Shared Buffer})$$
      </li>
      <li>當特定行情佇列突發擁塞時，交換機能動態向全域共享池借調更多快取空間，吸收持續數百微秒之 Incast 衝擊，將丟包率降至最低。</li>
    </ul>
  </li>
  <li><strong>早熟預警與微突發熱區定位</strong>：當佇列水線超過 60% 時，INT 自動產生告警事件，SRE 團隊可精確定位是哪一家券商、哪一條光纖鏈路在開盤瞬間引發了微突發。</li>
</ol>

<h4>五、結論：構建確定性金融微秒級網路空間</h4>
<p>透過<strong>帶內網路遙測（INT）與高頻串流遙測</strong>，證交所徹底打破了傳統網路黑盒，將網路監控之時間分辨率由「分鐘級」一口氣拉升至<strong>「微秒級」</strong>。結合動態緩衝區調校與 ECN 壅塞通知，為我國逐筆撮合與海量多播行情構築了具備自適應緩衝與透明可觀測之極致金融網路神盾。</p>
            """,
            "examinerTips": "得分關鍵詞：『Incast 匯聚與交換機晶片 Packet Buffer 溢位』、『SNMP 分鐘級輪詢嚴重失明』、『INT 帶內網路遙測基於 P4 可程式化晶片』、『逐跳線速插入 Queue Occupancy 與 Egress Latency』、『gNMI 毫秒級主動串流遙測』、『Dynamic Buffer Allocation 動態緩衝區 Alpha 調校』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>微突發物理成因（6分）</strong>：直擊 Incast 瞬時匯聚、晶片快取耗盡及 SNMP 分鐘級平滑失明之痛點。</li>
  <li><strong>INT 技術原理（7分）</strong>：繪製清晰資料封包結構圖，深入 P4 晶片線速注入與逐跳遙測機制。</li>
  <li><strong>gNMI 串流與動態緩衝（7分）</strong>：條理分明闡釋高頻推送與動態 Alpha 閾值借調緩衝區之實務防護。</li>
  <li><strong>可觀測性結論（5分）</strong>：總結微秒級時間分辨率對金融高頻交易網路之革命性戰略價值。</li>
</ul>
            """
        }
    ]

if __name__ == "__main__":
    essays = get_sysnet_essays_33_to_46()
    print(f"Loaded {len(essays)} unique Sysnet essays (sn-essay-33 to sn-essay-46).")
    for e in essays:
        print(f"  [{e['id']}] {e['title']} ({len(e['modelAnswer'])} chars)")
