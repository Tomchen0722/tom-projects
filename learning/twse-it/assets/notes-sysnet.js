/**
 * 臺灣證券交易所 (TWSE) 招募備考講義 - 系統與網路管理人員 (計算機概論)
 * 涵蓋金融核心架構、超低延遲運算、網路拓撲、Linux Kernel 調校、資料庫雙活等 12 大深入單元
 */

const NOTES_SYSNET = [
  {
    id: "sn-ch01",
    chapter: "第 1 章：臺灣證交所撮合架構與超低延遲運算",
    title: "逐筆撮合核心機制、微秒級低延遲與 Kernel Bypass 技術",
    summary: "剖析臺灣證券市場逐筆撮合（Continuous Trading）引擎架構，涵蓋 DPDK、Solarflare Onload 核心旁路技術、NUMA 記憶體隔離及 CPU 綁定實務。",
    content: `
<h2>1. 逐筆撮合（Continuous Trading）架構解析</h2>
<p>臺灣證券交易所於 2020 年正式全面推行『逐筆撮合』機制。與早期 5 秒集合競價不同，逐筆撮合隨到隨撮，以<strong>「價格優先、時間優先」</strong>為撮合核心原則。下單委託類型更擴充為限價（Limit Order）、市價（Market Order），搭配立即成交否則取消（IOC, Immediate-or-Cancel）與全部成交否則取消（FOK, Fill-or-Kill），對系統每秒交易量（TPS）與往返延遲（Round-Trip Latency）提出極限考驗。</p>

<div class="callout-box">
  <div class="callout-title">📌 金融撮合熱路徑（Hot Path）三大延遲殺手</div>
  <p>1. <strong>作業系統 Context Switch（環境切換）</strong>：傳統 Socket API 每次讀寫封包皆引發 User Space 與 Kernel Space 之保護模式切換。<br>
  2. <strong>CPU 硬體與軟中斷（Hardware & Software IRQ）</strong>：網卡產生中斷會打斷撮合行程管線，造成尾端延遲（Tail Latency）飆升。<br>
  3. <strong>CPU 快取失效（Cache Miss）與記憶體換頁（Paging/TLB Miss）</strong>：跨 Socket 記憶體存取將延遲自 10ns 放大至 100ns 以上。</p>
</div>

<h2>2. 核心旁路技術：DPDK 與 Solarflare Onload</h2>
<p>為達成微秒（µs）級甚至次微秒之極致撮合速度，金融交易熱路徑普遍揚棄標準 Linux 網路堆疊，採用 <code>Kernel Bypass</code>（核心旁路）架構：</p>
<ul>
  <li><strong>DPDK（Data Plane Development Kit，資料平面開發套件）</strong>：利用 <strong>PMD（Poll Mode Driver，輪詢模式驅動）</strong> 繞過中斷機制，直接在使用者空間輪詢網卡環形緩衝區（Ring Buffer），零拷貝（Zero-Copy）處理封包。</li>
  <li><strong>Solarflare Onload（OpenOnload）</strong>：針對證券業標準 TCP/UDP 應用程式提供無縫加速。其在使用者空間實現完整的 TCP/IP 堆疊，應用程式不需修改 Socket 原始碼，即可達成 1.2µs 內之極致單向網路延遲。</li>
</ul>

<pre><code>// DPDK 核心輪詢無鎖封包處理模型範例 (C 語言擬真)
while (likely(!force_quit)) {
    // 透過輪詢模式驅動 PMD 從網卡 RX Ring 批量取得封包，全無中斷開銷
    const uint16_t nb_rx = rte_eth_rx_burst(port_id, queue_id, pkts_burst, BURST_SIZE);
    if (unlikely(nb_rx == 0)) continue;

    for (int i = 0; i < nb_rx; i++) {
        struct rte_mbuf *m = pkts_burst[i];
        // 進入撮合引擎熱路徑：訂單委託解碼 (FIX / TWSE 二進位通訊協定)
        process_twse_order(rte_pktmbuf_mtod(m, void *));
        rte_pktmbuf_free(m);
    }
}</code></pre>

<h2>3. 記憶體管理與 CPU 深度調校實務</h2>
<p>在生產環境部署證券撮合伺服器時，必須進行深層 Linux 系統調校：</p>
<ul>
  <li><strong>CPU Pinning（核心綁定）與隔離（isolcpus）</strong>：在開機參數加入 <code>isolcpus=2-15 nohz_full=2-15 rcu_nocbs=2-15</code>，確保撮合執行緒獨佔特定實體核心，不受 Linux CFS 排程器打擾。</li>
  <li><strong>NUMA（非均勻記憶體存取）親和性綁定</strong>：使用 <code>numactl --cpunodebind=0 --membind=0</code>，確保執行緒存取的記憶體與處理該網卡中斷的 PCIe 總線位於同一 NUMA 節點，徹底消除 QPI/UPI 跨匯流排懲罰。</li>
  <li><strong>記憶體鎖定與大頁（HugePages）</strong>：呼叫 <code>mlockall(MCL_CURRENT | MCL_FUTURE)</code> 鎖定進程虛擬記憶體於實體 RAM 中，嚴禁發生 Swap Page Fault；啟用 1GB HugePages 消除 TLB（轉譯後備緩衝區）失誤。</li>
</ul>
`
  },
  {
    id: "sn-ch02",
    chapter: "第 2 章：金融高可靠網路拓撲與行情推播",
    title: "多點廣播（Multicast）、Spine-Leaf 架構與微突發（Microburst）防禦",
    summary: "深度解析證交所行情傳輸（PIM-SM/SSM、IGMPv3）、金融資料中心 Spine-Leaf 現代網路拓撲、BGP EVPN / VXLAN 與交換器緩衝區調校。",
    content: `
<h2>1. 證券行情多點廣播（Multicast Market Data）傳輸原理</h2>
<p>證交所行情（Market Data）包括揭示五檔價格、委託筆數、逐筆成交資訊。若採傳統 TCP 單播（Unicast），每多一家證券商就必須複製一份封包發送，伺服器出口頻寬將成倍爆炸。因此全球交易所一致採用 <strong>IP Multicast（多點廣播）</strong>：</p>
<ul>
  <li><strong>傳輸協定</strong>：基於 UDP，發送端僅需在網路中注入單一封包，由網路交換器與路由器硬體複製封包並分送給所有訂閱者。</li>
  <li><strong>群播協定架構</strong>：
    <ul>
      <li><strong>IGMPv3（網際網路群組管理協定第三版）</strong>：主機與區域交換器間的群組註冊協定，支援 Source-Specific Multicast（指定來源群播）。</li>
      <li><strong>PIM-SSM（Protocol Independent Multicast - Source-Specific Multicast）</strong>：省去複雜的 RP（集合點 Rendezvous Point），訂閱端直接指定 (S, G)（來源 IP S 與群播群組 G），建立最優群播樹（Shortest Path Tree），大幅降低路由建立時間與收斂延遲。</li>
    </ul>
  </li>
</ul>

<h2>2. 金融資料中心 Spine-Leaf（脊葉式）架構與 ECMP</h2>
<p>傳統三層式網路（Core-Aggregation-Access）存在 STP（生成樹協定）阻塞鏈路與東-西向流量延遲不可預測之致命缺點。證券現代機房全面改採 <strong>Spine-Leaf 雙層拓撲</strong>：</p>
<ul>
  <li><strong>全網雙跳直連</strong>：任何兩台伺服器之間的通訊，皆維持精準的 2 次轉發（Leaf → Spine → Leaf），延遲固定且可預測（通常低於 1 微秒）。</li>
  <li><strong>ECMP（Equal-Cost Multi-Path）等價多路徑</strong>：所有上行鏈路全部處於主動轉發狀態，無多餘閒置頻寬，利用 5-tuple 雜湊達到完美的負載均衡。</li>
  <li><strong>BGP EVPN / VXLAN</strong>：以標準 BGP 為控制平面，VXLAN 為資料平面，在三層底層實體網路（Underlay）上建立靈活的二層虛擬化大二層覆蓋網路（Overlay），支援伺服器集群無縫遷移。</li>
</ul>

<h2>3. 金融微突發（Microburst）與交換器低延遲直通（Cut-Through）</h2>
<div class="callout-box">
  <div class="callout-title">⚠️ Microburst（微突發）對撮合系統的威脅</div>
  <p>當開盤瞬時或重大財經事件公布時，數萬筆下單封包在短短數十微秒內湧入特定交換器埠，儘管平均頻寬利用率僅 20%，但瞬時 Buffer 瞬間被填滿，引發<strong>尾端丟包（Tail Drop）與封包重傳（TCP Retransmission）</strong>，導致撮合嚴重卡頓。</p>
</div>

<p><strong>防禦與調校策略：</strong></p>
<ol>
  <li><strong>Cut-Through Switching（直通式交換）</strong>：交換器讀取完封包標頭前 64 Bytes 目的 MAC 即開始轉發，無須等待整包接收完畢，將轉發延遲由 Store-and-Forward 的 5~10µs 降至 200~350ns。</li>
  <li><strong>動態共用緩衝區（Dynamic Shared Buffering）</strong>：採用 Broadcom Trident/Tomahawk 或 Cisco Cloud Scale 晶片之動態緩衝技術，允許突發流量臨時借用共享緩衝區，抑制丟包。</li>
  <li><strong>PTP（IEEE 1588v2 精度時間同步）</strong>：採用 Boundary Clock 或 Transparent Clock 硬體時間標記，監控交換器內部微秒級排隊延遲（Queue Depth Telemetry）。</li>
</ol>
`
  },
  {
    id: "sn-ch03",
    chapter: "第 3 章：作業系統核心機制、程序調度與並行通訊",
    title: "Linux CFS 排程器、即時排程 SCHED_FIFO、記憶體分頁與 IPC",
    summary: "探討 Linux 核心排程原理、POSIX 實時優先權、虛擬記憶體管理、三級分頁機制、無鎖環形佇列（Disruptor）與行程間通訊（IPC）。",
    content: `
<h2>1. Linux 排程器原理：CFS vs. 即時排程（SCHED_FIFO / SCHED_RR）</h2>
<p>Linux 預設採用 <strong>CFS（Completely Fair Scheduler，完全公平排程器）</strong>，透過紅黑樹（Red-Black Tree）維護各進程之虛擬執行時間 <code>vruntime</code>。然而 CFS 追求整體公平性，會在時間片耗盡時強制剝奪 CPU，引發金融交易之嚴重抖動。</p>
<p>在證券撮合伺服器中，關鍵撮合執行緒必須切換為 POSIX 即時排程策略：</p>
<ul>
  <li><strong>SCHED_FIFO（先進先出即時排程）</strong>：靜態優先權範圍 1~99（高於普通進程）。除非該執行緒主動呼叫 <code>sched_yield()</code> 或發生阻塞，否則將<strong>永久獨佔 CPU</strong>，絕不被任何普通 CFS 行程搶佔。</li>
  <li><strong>SCHED_RR（時間輪轉即時排程）</strong>：同優先權執行緒依據固定時間片輪轉執行。</li>
</ul>

<h2>2. 虛擬記憶體機制與分頁中斷（Page Fault）深度防範</h2>
<p>現代 x86-64 處理器採用 4 級分頁架構（PML4 → PDPT → PD → PT），將虛擬位址轉換為實體位址。若發生分頁失誤（Major Page Fault），作業系統必須自磁碟讀取數據，引發高達數毫秒（ms）之嚴重延遲，這在證交所系統中是絕對無法容忍的災難。</p>

<p><strong>極致效能架構防護關鍵：</strong></p>
<ul>
  <li><strong>Transparent Huge Pages (THP) 關閉</strong>：Linux 核心的 THP 背景碎片重組（khugepaged）常造成不可預測的幾十毫秒凍結（Latency Spike）。金融低延遲伺服器必須執行 <code>echo never > /sys/kernel/mm/transparent_hugepage/enabled</code>，改以手動配置靜態 HugePages。</li>
  <li><strong>無鎖設計：LMAX Disruptor 與 Lock-free Ring Buffer</strong>：傳統 Mutex（互斥鎖）會引發 <code>futex</code> 系統呼叫與核心空間睡眠喚醒開銷。金融高頻系統全面採用基於記憶體屏障（Memory Barrier）與 CAS（Compare-And-Swap）的無鎖佇列，透過 Cache Line 填充（Padding）消滅<strong>偽共享（False Sharing）</strong>。</li>
</ul>
`
  },
  {
    id: "sn-ch04",
    chapter: "第 4 章：電腦硬體結構、CPU 體系架構與快取階層",
    title: "指令管線化、MESI 快取一致性協定、NVMe-oF 與 SAN 儲存架構",
    summary: "從硬體底層剖析現代 CPU 超純量管線、快取行（Cache Line）設計、MESI 協定、記憶體偽共享、光纖通道（FC SAN）與新一代 NVMe-oF 金融儲存網。",
    content: `
<h2>1. CPU 運算體系：管線化、分支預測與超純量</h2>
<p>現代伺服器 CPU 透過多級指令管線化（Instruction Pipelining，例如 14~19 級管線）實現並行指令解碼與執行：</p>
<ul>
  <li><strong>分支預測（Branch Prediction）</strong>：若條件跳轉預測失敗，CPU 必須沖刷管線（Pipeline Flush），代價約為 15~20 個時脈週期。在撮合邏輯代碼中，應大量使用 <code>__builtin_expect(!!(x), 1)</code>（即 <code>likely() / unlikely()</code> 巨集）引導編譯器生成最優分支指令順序。</li>
  <li><strong>亂序執行（Out-of-Order Execution）與記憶體屏障</strong>：為防止編譯器與 CPU 重排記憶體存取指令導致多執行緒狀態不一致，必須精準運用 <code>std::atomic_thread_fence(std::memory_order_acquire/release)</code>。</li>
</ul>

<h2>2. 快取階層架構與 MESI 協定</h2>
<p>CPU 快取以 <strong>Cache Line（通常為 64 Bytes）</strong> 為基本傳輸單位。多核心共享快取時，透過硬體匯流排監聽（Bus Snooping）維持一致性，最經典即為 <strong>MESI 協定</strong>：</p>
<table style="width:100%; border-collapse:collapse; margin:1rem 0;">
  <thead>
    <tr style="background:var(--bg-secondary); border-bottom:2px solid var(--border-color);">
      <th style="padding:0.5rem; text-align:left;">狀態代號</th>
      <th style="padding:0.5rem; text-align:left;">狀態名稱</th>
      <th style="padding:0.5rem; text-align:left;">定義與行為說明</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);"><strong>M (Modified)</strong></td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">已修改</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">該快取行已被修改，與記憶體不一致，且僅存在於當前核心快取中。</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);"><strong>E (Exclusive)</strong></td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">獨佔</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">該快取行與記憶體一致，且僅存在於當前核心快取中。</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);"><strong>S (Shared)</strong></td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">共享</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">該快取行與記憶體一致，可能同時存在於多個核心的快取中。</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);"><strong>I (Invalid)</strong></td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">無效</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">該快取行資料已過期無效，讀取時必須觸發 Cache Miss 重新載入。</td></tr>
  </tbody>
</table>

<div class="callout-box">
  <div class="callout-title">⚠️ 偽共享（False Sharing）效能陷阱</div>
  <p>若兩個獨立的執行緒分別頻繁更新同一個 64-Byte Cache Line 內的相鄰變數（如 Core 1 更新 <code>order_count_A</code>，Core 2 更新 <code>order_count_B</code>），MESI 協定將使兩核心快取行反覆在 M 與 I 狀態間劇烈震盪（Cache Ping-Pong），造成 CPU 吞吐量暴跌 90%！解決方法是使用 <code>alignas(64)</code> 進行記憶體對齊填充。</p>
</div>

<h2>3. 金融企業級儲存：FC-SAN 與 NVMe-oF</h2>
<ul>
  <li><strong>FC-SAN（Fibre Channel Storage Area Network）</strong>：證券業核心資料庫長期採用 32G/64G 光纖通道儲存網路，透過專屬光纖交換器與 Host Bus Adapter（HBA）卡傳輸 SCSI 塊級協議，具備無損（Lossless）與高可用雙迴路（Multipath I/O）特性。</li>
  <li><strong>NVMe-oF（NVMe over Fabrics）</strong>：新一代全閃存儲存互連架構。透過 RoCEv2（RDMA over Converged Ethernet）將 PCIe NVMe 傳輸協定直接延伸至高速乙太網，將儲存網路端到端延遲壓低至 10µs 以內，完美支撐交易資料庫毫秒級大量寫入。</li>
</ul>
`
  },
  {
    id: "sn-ch05",
    chapter: "第 5 章：TCP/IP 通訊協定棧調校與高精準度時序同步",
    title: "TCP 核心參數最佳化、PTP (IEEE 1588) 奈秒時間戳與金融監理",
    summary: "詳解 TCP 三向交握、四向揮手、TCP_NODELAY、SO_BUSY_POLL 核心調校，以及歐盟 MiFID II / 證期法要求之 PTP 亞微秒時間同步實作。",
    content: `
<h2>1. 金融交易 TCP 參數極致調優</h2>
<p>標準作業系統的 TCP 堆疊預設為了大吞吐量與省頻寬而設計，存在多種延遲機制，必須在金融撮合熱路徑中徹底停用：</p>
<ul>
  <li><strong>停用 Nagle 演算法（TCP_NODELAY）</strong>：Nagle 演算法會將小封包緩衝合併直到收到前一個封包的 ACK 為止。在證券即時下單中，每一微秒都攸關成交優先權，必須透過 <code>setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &val, sizeof(val))</code> 徹底關閉，保證委託即時噴出。</li>
  <li><strong>停用 Delayed ACK（TCP 延遲確認）</strong>：接收端延遲發送 ACK 往往與 Nagle 演算法形成惡意死鎖（Deadlock），導致 40ms~200ms 之巨大延遲，需設置 <code>TCP_QUICKACK</code>。</li>
  <li><strong>SO_BUSY_POLL 忙輪詢</strong>：透過 <code>setsockopt(fd, SOL_SOCKET, SO_BUSY_POLL, &usecs, sizeof(usecs))</code> 允許 Socket 讀取呼叫在使用者層主動輪詢網卡佇列指定的微秒數，免除中斷喚醒開銷。</li>
</ul>

<h2>2. 高精準度時鐘同步：PTP（IEEE 1588v2）與金融監理法規</h2>
<p>在逐筆撮合與高頻交易爭議仲裁中，撮合時間戳記（Timestamp）精準度具備嚴格法律效力（如 MiFID II RTS 25 規定交易時間戳記最大偏差不得超過 100 微秒，解析度須達 1 微秒）：</p>
<ul>
  <li><strong>傳統 NTP（網路時間協定）</strong>：精度僅在毫秒（ms）等級，且易受作業系統中斷與網路延遲抖動影響，無法滿足撮合爭議仲裁要求。</li>
  <li><strong>PTP（Precision Time Protocol，IEEE 1588v2）</strong>：
    <ul>
      <li>利用<strong>網卡實體層（PHY）晶片之硬體時間戳記（Hardware Timestamping）</strong>，在封包剛抵達網卡物理引腳之瞬間即打印時間戳。</li>
      <li>消除所有作業系統核心、中斷、驅動程式之軟體延遲誤差，在專屬 Grandmaster Clock（GPS 衛星銣原子鐘）同步下，實現<strong>小於 100 奈秒（ns）</strong>之超高精度時間一致性。</li>
    </ul>
  </li>
</ul>
`
  },
  {
    id: "sn-ch06",
    chapter: "第 6 章：關聯式資料庫交易、WAL 與金融雙活容災架構",
    title: "交易 ACID、隔離層級、MVCC、RTO/RPO 與雙活（Active-Active）機房",
    summary: "解析關聯式資料庫交易底層原理、WAL 預寫日誌、MVCC 多版本併發控制、證券雙活機房同步複寫、容災切換與分散式一致性協定。",
    content: `
<h2>1. 資料庫交易 ACID 與 WAL 內部運作機制</h2>
<p>金融核心帳務與交易歷史資料庫必須百分之百滿足 <strong>ACID（原子性 Atomicity、一致性 Consistency、隔離性 Isolation、持久性 Durability）</strong>：</p>
<ul>
  <li><strong>WAL（Write-Ahead Logging，預寫日誌）</strong>：為了避免隨機磁碟寫入（Random I/O）瓶頸，資料庫所有交易修改在真正刷入磁碟資料頁（Buffer Pool Dirty Page Flushing）前，必須先<strong>循序追加（Sequential Append）</strong>寫入 WAL 日誌檔，並呼叫 <code>fsync()</code> 確認落盤。</li>
  <li><strong>Crash Recovery（崩潰復原機制）</strong>：利用 ARIES 演算法包含三大階段：
    <ol>
      <li><strong>分析階段（Analysis）</strong>：找出故障時 Buffer Pool 髒頁與活躍交易。</li>
      <li><strong>重做階段（REDO）</strong>：重現所有已提交交易之變更，恢復至崩潰前最新狀態。</li>
      <li><strong>復原階段（UNDO）</strong>：回滾所有在崩潰發生時尚未提交之活躍交易，維護資料一致性。</li>
    </ol>
  </li>
</ul>

<h2>2. 併發控制：交易隔離層級與 MVCC</h2>
<table style="width:100%; border-collapse:collapse; margin:1rem 0;">
  <thead>
    <tr style="background:var(--bg-secondary); border-bottom:2px solid var(--border-color);">
      <th style="padding:0.5rem; text-align:left;">隔離層級 (ANSI SQL)</th>
      <th style="padding:0.5rem; text-align:left;">髒讀 (Dirty Read)</th>
      <th style="padding:0.5rem; text-align:left;">不可重複讀 (Non-Repeatable)</th>
      <th style="padding:0.5rem; text-align:left;">幻讀 (Phantom Read)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">Read Uncommitted</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">可能發生</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">可能發生</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">可能發生</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">Read Committed (多數預設)</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">可能發生</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">可能發生</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">Repeatable Read</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">InnoDB 藉 Next-Key Lock 解決</td></tr>
    <tr><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">Serializable</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td><td style="padding:0.5rem; border-bottom:1px solid var(--border-subtle);">徹底杜絕</td></tr>
  </tbody>
</table>

<h2>3. 證券金融雙活（Active-Active）機房容災標準</h2>
<div class="callout-box">
  <div class="callout-title">📌 金融關鍵容災指標（DR Metric）</div>
  <p><strong>RTO（Recovery Time Objective，復原時間目標）</strong>：系統從災難中斷到完全恢復對外提供服務的最大允許時長。證交所核心系統要求 <strong>RTO ≈ 0（秒級切換）</strong>。<br>
  <strong>RPO（Recovery Point Objective，復原點目標）</strong>：系統從災難中斷所能容忍之最大交易資料遺失量。證券核心帳務要求 <strong>RPO = 0（零資料遺失）</strong>。</p>
</div>

<p><strong>雙活機房建設關鍵要點：</strong></p>
<ol>
  <li><strong>同城雙活（Metro Active-Active）</strong>：兩機房相距 30 公里以內，透過裸光纖直連傳輸延遲小於 1ms，採用<strong>同步鏡像（Synchronous Replication）</strong>與分散式多主庫架構，雙中心同時對券商開放下單。</li>
  <li><strong>異地備援（Remote Disaster Recovery）</strong>：相距 100 公里以上（如新北機房對龍潭/台中備援），採用<strong>非同步複寫（Asynchronous Replication）</strong>，避免光速傳輸實體延遲拖垮本地撮合 TPS。</li>
  <li><strong>裂腦（Split-Brain）仲裁機制</strong>：部署獨立第三方仲裁站點（Quorum Witness），防止跨機房心跳中斷時兩邊同時爭搶 Master 導致資料撕裂。</li>
</ol>
`
  },
  {
    id: "sn-ch07",
    chapter: "第 7 章：容器化、Kubernetes 與雲原生基礎設施維運",
    title: "Docker cgroups/namespaces 隔離、K8s 排程演算法與 SRE 維運實務",
    summary: "探討容器底層 Linux 核心隔離原理、Kubernetes Pod 生命週期、CNI 網路插件、Prometheus+Grafana 監控指標與 SRE 穩定性工程。",
    content: `
<h2>1. 容器底層技術：Linux Namespaces 與 cgroups</h2>
<p>Docker 與容器並非真正的硬體虛擬化，而是利用 Linux 核心的兩大原生機制建構之進程隔離沙盒：</p>
<ul>
  <li><strong>Namespaces（命名空間 - 實現檢視隔離）</strong>：
    <ul>
      <li><code>pid</code>：進程 ID 樹隔離（容器內可見 PID 1）。</li>
      <li><code>net</code>：獨立網路設備、路由表、防火牆規則、Socket。</li>
      <li><code>mnt</code>：獨立掛載點檔案系統（配合 OverlayFS）。</li>
      <li><code>ipc</code>：System V IPC 與 POSIX 訊息佇列隔離。</li>
      <li><code>uts</code>：獨立主機名稱與網域名稱。</li>
      <li><code>user</code>：使用者與群組 ID 映射（容器內 root 可映射為宿主機非 root）。</li>
    </ul>
  </li>
  <li><strong>cgroups（Control Groups 控制群組 - 實現資源上限限制）</strong>：嚴格限制容器之 CPU Quota、記憶體硬限制（OOM Killer 觸發點）、磁碟 I/O 權重與網路流量。</li>
</ul>

<h2>2. Kubernetes 金融雲架構與網路插件（CNI）</h2>
<p>在證券周邊交易輔助平台中，K8s 承載微服務與查詢 API：</p>
<ul>
  <li><strong>K8s 排程器（kube-scheduler）</strong>：依據 NodeAffinity（節點親和性）、PodAntiAffinity（Pod 反親和性，確保同一微服務的多個副本絕不排程在同一實體主機）、Taints & Tolerations（污點與容忍）執行精準排程。</li>
  <li><strong>高效能 CNI 插件</strong>：金融生產環境揚棄慢速的 Overlay 封裝（Flannel VXLAN），全面採用 <strong>Calico BGP 路由模式</strong> 或 <strong>Cilium（基於 eBPF）</strong>，使 Pod IP 直接在實體網路交換器上路由轉發，消除二次封包封裝損耗。</li>
</ul>

<h2>3. SRE（網站可靠性工程）金融營運指標體系</h2>
<ul>
  <li><strong>SLI（Service Level Indicator，服務水準指標）</strong>：量化測量的即時數據，如「撮合查詢延遲低於 5ms 之成功請求比例」。</li>
  <li><strong>SLO（Service Level Objective，服務水準目標）</strong>：團隊內部設定之高標準可靠性目標，例如「每季度可用性達到 99.999%（五個九，相當於每季度允許停機時間小於 1.3 分鐘）」。</li>
  <li><strong>Error Budget（錯誤預算）</strong>：100% - SLO。當錯誤預算消耗殆盡時，強制凍結所有新功能發布，所有工程量能全力投入系統穩定性與性能優化。</li>
</ul>
`
  }
];

window.NOTES_SYSNET = NOTES_SYSNET;
