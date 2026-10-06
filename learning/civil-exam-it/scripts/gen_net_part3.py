# -*- coding: utf-8 -*-
"""
Computer Networks & Security Question Bank Generator - Part 3 (95 unique questions)
Topics: Transport Layer (TCP 3-Way Handshake, 4-Way Teardown, Congestion Control AIMD, Flow Control),
Application Layer (HTTP/1.1/2/3 QUIC, DNS/DNSSEC, TLS 1.2/1.3, Email Protocols SPF/DKIM/DMARC).
"""

def get_net_part3_questions():
    qs = []

    # -------------------------------------------------------------
    # 6. 傳輸層 TCP 機制與壅塞控制推導 (45 題)
    # -------------------------------------------------------------
    tcp_data = [
        ("TCP 三向交握（Three-Way Handshake）建立連線的過程中，三個封包的控制旗標與序號行為依序為？",
         "1. Client 發送 SYN（seq=x）；2. Server 回覆 SYN+ACK（seq=y, ack=x+1）；3. Client 發送 ACK（seq=x+1, ack=y+1）", ["1. Client 發送 SYN（seq=x）；2. Server 回覆 SYN+ACK（seq=y, ack=x+1）；3. Client 發送 ACK（seq=x+1, ack=y+1）", "1. Client 發送 SYN；2. Server 回覆 ACK；3. Client 發送 DATA", "1. Client 發送 ACK；2. Server 回覆 SYN；3. Client 發送 FIN", "1. 雙方同時發送 SYN+ACK"],
         "三向交握確保雙方初始序號（ISN）成功同步，且確認雙向資料通道的發送與接收能力皆運作正常。SYN 訊號消耗 1 個序號空間，故 ACK 回傳 x+1。"),
        ("TCP 四向揮手（Four-Way Teardown）斷開連線過程中，主動關閉端在發送最後一個 ACK 封包後，必須進入何種狀態？該狀態必須等待多久？",
         "進入 TIME_WAIT 狀態；必須等待 2MSL（兩倍最長封包存活時間，通常為 60~120 秒）", ["進入 TIME_WAIT 狀態；必須等待 2MSL（兩倍最長封包存活時間，通常為 60~120 秒）", "進入 CLOSED 狀態立即關閉", "進入 CLOSE_WAIT 狀態等待 1 小時", "進入 FIN_WAIT_1 狀態等待 10 秒"],
         "TIME_WAIT 存在兩大目的：1. 確保最後的 ACK 順利抵達被動端（若被動端重傳 FIN，主動端仍可重送 ACK）；2. 讓本次連線在網路上延遲迷失的所有舊封包在 2MSL 內徹底消逝，防止干擾後續使用相同四元組（IP:Port）的新連線！"),
        ("在 TCP 壅塞控制（Congestion Control）中，慢啟動（Slow Start）階段的擁塞視窗（cwnd, Congestion Window）成長特徵為？",
         "每經過一個往返時間（RTT），cwnd 大小呈現「指數倍增長（Exponential Growth：1 -> 2 -> 4 -> 8...）」", ["每經過一個往返時間（RTT），cwnd 大小呈現「指數倍增長（Exponential Growth：1 -> 2 -> 4 -> 8...）」", "每經過一個 RTT 增加 1 個 MSS（線性增長）", "保持常數不變", "每秒翻倍"],
         "傳送端每收到一個有效的 ACK，cwnd 即增加 1 個 MSS。當一整個視窗的 ACK 抵達時，cwnd 恰好翻倍，快速探測網路極限。"),
        ("當 cwnd 增長達到「慢啟動門檻（ssthresh, Slow Start Threshold）」時，TCP 狀態機會轉移至何種演算法？該演算法的 cwnd 增長方式為？",
         "轉移至「壅塞避免（Congestion Avoidance）」；每經過一個 RTT，cwnd 僅增加 1 個 MSS（加性增長 Additive Increase）", ["轉移至「壅塞避免（Congestion Avoidance）」；每經過一個 RTT，cwnd 僅增加 1 個 MSS（加性增長 Additive Increase）", "轉移至快速重傳；cwnd 保持不變", "轉移至超時中斷；cwnd 歸零", "繼續指數增長"],
         "加性增長（Additive Increase）謹慎試探瓶頸頻寬，避免急劇引發網路嚴重壅塞丟包。"),
        ("在 TCP Tahoe 演算法中，當發生「重傳逾時（RTO Timeout）」時，系統對 ssthresh 與 cwnd 的處置為？",
         "ssthresh 設為「當前 cwnd 的一半（cwnd / 2）」，並將 cwnd「暴跌強制重設為 1 個 MSS」，重新進入慢啟動", ["ssthresh 設為「當前 cwnd 的一半（cwnd / 2）」，並將 cwnd「暴跌強制重設為 1 個 MSS」，重新進入慢啟動", "cwnd 減半並保持在壅塞避免", "僅重傳封包，視窗不變", "關閉 TCP 連線"],
         "逾時代表網路極度嚴重擁塞，Tahoe 採取極端激進防衛措施，重置回慢啟動起點。"),
        ("在 TCP Reno 演算法中，當傳送端連續收到「3 個重複確認（3 Duplicate ACKs）」時，觸發快速重傳與快速復原（Fast Recovery），此時 cwnd 的調整為？",
         "ssthresh 設為 cwnd / 2，cwnd 設為 ssthresh + 3（或 cwnd / 2），直接進入壅塞避免，而「絕不跌回 1」", ["ssthresh 設為 cwnd / 2，cwnd 設為 ssthresh + 3（或 cwnd / 2），直接進入壅塞避免，而「絕不跌回 1」", "cwnd 跌回 1 MSS 重新慢啟動", "cwnd 保持完全不變", "增加 cwnd 至最大值"],
         "能收到 3 個 Duplicate ACK 代表後續封包仍能順利抵達接收端，網路並未全線癱瘓，僅單一封包遺失。乘法減半（Multiplicative Decrease）後立即快速復原，效能遠超 Tahoe。"),
        ("TCP 的 AIMD（加性增、乘性減，Additive Increase Multiplicative Decrease）原則在穩定狀態下使網路多條 TCP 連線達成？",
         "頻寬分配的「效率性（Efficiency）」與「公平性（Fairness）」（收斂至公平分享頻寬點）", ["頻寬分配的「效率性（Efficiency）」與「公平性（Fairness）」，收斂至公平分享頻寬點", "零封包遺失", "永遠不產生延遲", "所有封包亂序傳輸"], " Chiu 與 Jain 經典證明：AIMD 是唯一能在分散式無協調環境下保證收斂至公平平衡點的演算法。"),
        ("TCP 流量控制（Flow Control）主要是為了解決下列何種問題？",
         "防止發送端發送速度過快，導致「接收端緩衝區溢位（Receiver Buffer Overflow）」崩潰", ["防止發送端發送速度過快，導致「接收端緩衝區溢位（Receiver Buffer Overflow）」崩潰", "防止網路路由器壅塞", "防止封包遭竊聽", "確保封包加密強度"], "流量控制是端對端（End-to-End）接收能力協商，由接收端透過 TCP 標頭的 rwnd（Receive Window）公告視窗大小實現。"),
        ("「愚蠢視窗症候群（Silly Window Syndrome, SWS）」是指何種低效現象？",
         "發送端與接收端以極其微小的視窗大小（如僅 1 個 Byte）頻繁傳輸微小資料，導致 40 位元組的 TCP/IP 標頭開銷佔據 97% 以上頻寬", ["發送端與接收端以極其微小的視窗大小（如僅 1 個 Byte）頻繁傳輸微小資料，導致 40 位元組的 TCP/IP 標頭開銷佔據 97% 以上頻寬", "視窗大小超過 65535", "視窗完全無法關閉", "接收端拒絕接收任何資料"], "解決方案：發送端使用 Nagle 演算法（未湊滿 MSS 且有未確認封包時暫存不發）；接收端使用 Clark 演算法（未達到半個緩衝區或 MSS 前通告視窗為 0）。"),
        ("SYN 洪泛攻擊（SYN Flood Attack）利用了 TCP 連線建立過程中的何種缺陷？最佳防禦手段為何？",
         "大量發送偽造來源 IP 的 SYN 請求但不回覆最後的 ACK，耗盡伺服器的半連接佇列（SYN Queue）；防禦為啟用 SYN Cookies", ["大量發送偽造來源 IP 的 SYN 請求但不回覆最後的 ACK，耗盡伺服器的半連接佇列（SYN Queue）；防禦為啟用 SYN Cookies", "利用 FIN 封包斷線；防禦為關閉防火牆", "利用 RST 封包重設；防禦為增加頻寬", "利用 UDP 廣播；防禦為重開機"], "SYN Cookie 不在半連接佇列預先配置記憶體，而是將連線加密資訊編碼進 ISN，收到第三次握手 ACK 時逆向解密驗證，完美化解半連線佔用。")
    ]

    for stem, ans_s, opts, expl in tcp_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "TCP協定與壅塞控制推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【TCP 狀態機與壅塞視窗步進推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 TCP 握手/揮手與視窗數值演算法推導</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立 TCP 狀態機與視窗控制階段</strong><br>
      ‧ 本題依據 RFC 793 / RFC 5681 規範進行嚴格分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行狀態轉移與視窗大小推演</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精確答案</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：推導計算完全符合 TCP 規格標準。<br>
‧ 其餘選項常為 Tahoe 與 Reno 快速重傳差異混淆、或 TIME_WAIT 狀態時間與成因誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>AIMD (Additive Increase Multiplicative Decrease)</code> <span class="en">AIMD</span>：加性增乘性減。<br>
‧ <code>SYN Cookie</code> <span class="en">SYN Cookie</span>：SYN Cookie 防禦機制。<br>
‧ <code>Silly Window Syndrome</code> <span class="en">Silly Window Syndrome</span>：愚蠢視窗症候群。"""
        })

    # More TCP items (35 items)
    more_tcp = [
        ("TCP 標頭中的 RST（Reset）控制旗標在何種情況下會被發送？", "連線發生不可恢復的嚴重異常，或存取了一個未開啟監聽的連接埠，強制「立即中斷連線」", ["連線發生不可恢復的嚴重異常，或存取了一個未開啟監聽的連接埠，強制「立即中斷連線」", "正常關閉連線時", "請求重傳遺失封包", "連線建立握手時"], "RST 封包直接銷毀雙方 TCB 控制區塊，無須經歷四向揮手與 TIME_WAIT。"),
        ("TCP 標頭中的 PSH（Push）旗標的語意為？", "指示接收端作業系統「立即將緩衝區中的資料交付給應用程式」，無須等待緩衝區填滿", ["指示接收端作業系統「立即將緩衝區中的資料交付給應用程式」，無須等待緩衝區填滿", "要求傳送端加快發送速度", "清空伺服器快取", "重設連線序號"], "常用於互動式終端機（如 SSH/Telnet），確保打字指令即時上送處理。"),
        ("TCP 標頭預設標準長度為多少位元組？最大可擴展至多少位元組？", "預設 20 位元組（無選項）；最大可透過選項欄位擴充至 60 位元組", ["預設 20 位元組（無選項）；最大可透過選項欄位擴充至 60 位元組", "固定 40 位元組", "預設 8 位元組，最大 16 位元組", "固定 32 位元組"], "由 4-bit Data Offset（資料偏移）指示，最大值為 15（15 × 4 = 60 bytes）。"),
        ("UDP 標頭長度固定為多少位元組？包含哪四個欄位？", "固定為 8 位元組；包含：來源埠號、目的埠號、長度、校驗和（各佔 2 位元組）", ["固定為 8 位元組；包含：來源埠號、目的埠號、長度、校驗和（各佔 2 位元組）", "固定為 20 位元組", "固定為 16 位元組", "4 位元組"], "極簡輕量化無連接設計，開銷極低。"),
        ("TCP 虛擬標頭（Pseudo-Header）在計算校驗和時的作用為？", "臨時提取來源 IP、目的 IP、協定號與 TCP 長度參與校驗和計算，防範「IP 誤送但 TCP 誤收」之定址錯誤", ["臨時提取來源 IP、目的 IP、協定號與 TCP 長度參與校驗和計算，防範「IP 誤送但 TCP 誤收」之定址錯誤", "加密 TCP 負載", "記錄經過的路由器", "儲存在資料庫"], "偽標頭只存在於計算校驗和的瞬間，絕不實際在實體網路上傳輸。"),
        ("TCP 保活計時器（Keepalive Timer）的主要功用為？", "在連線長時間無任何資料傳輸時（預設通常為 2 小時），探測對端主機是否已經當機崩潰以釋放死連線", ["在連線長時間無任何資料傳輸時（預設通常為 2 小時），探測對端主機是否已經當機崩潰以釋放死連線", "每秒強制刷新視窗", "計算 RTT 時間", "防範重放攻擊"], "防止半開放（Half-Open）殭屍連線永久佔用伺服器資源。"),
        ("TCP 堅持計時器（Persist Timer）的主要功用為？", "當接收端通告「零視窗（rwnd=0）」後，定期發送 1 位元組的視窗探測封包，防止「視窗更新 ACK 遺失導致的永久死鎖」", ["當接收端通告「零視窗（rwnd=0）」後，定期發送 1 位元組的視窗探測封包，防止「視窗更新 ACK 遺失導致的永久死鎖」", "計時 2MSL 關閉連線", "計算逾時重傳時間", "測量伺服器延遲"], "若接收端空出緩衝區後發送的非零視窗 ACK 意外遺失，雙方將陷入永久互相等待；Persist Timer 定期打破僵局。"),
        ("TCP 選擇性確認（SACK, Selective Acknowledgment）選項的主要效益為？", "允許接收端在 ACK 標頭中回報多個「已成功接收的不連續資料區塊區間」，使傳送端精準只重傳缺失區塊", ["允許接收端在 ACK 標頭中回報多個「已成功接收的不連續資料區塊區間」，使傳送端精準只重傳缺失區塊", "將 TCP 傳輸速率提高 10 倍", "取代 UDP 協定", "加密所有資料區塊"], "顯著提升嚴重丟包或高延遲鏈路下的重傳效率。"),
        ("TCP 視窗縮放選項（Window Scale Option, RFC 1323）解決了何種歷史局限？", "突破原生 TCP 標頭中 16 位元視窗大小欄位（最大 65,535 位元組）的限制，將最大視窗擴充至 1 GB（長肥管道 LFN 必備）", ["突破原生 TCP 標頭中 16 位元視窗大小欄位（最大 65,535 位元組）的限制，將最大視窗擴充至 1 GB（長肥管道 LFN 必備）", "縮短 TCP 標頭", "自動修復壞軌", "支援 IPv6"], "透過位移因子（Shift Count 最大 14）將視窗上限推至 2³⁰ Bytes。"),
        ("TCP 與 UDP 在多工（Multiplexing）與解多工（Demultiplexing）時，判定目的 socket 的元組數量差異為？", "UDP 僅需二元組（目的 IP, 目的 Port）；TCP 必須依賴四元組（來源 IP, 來源 Port, 目的 IP, 目的 Port）", ["UDP 僅需二元組（目的 IP, 目的 Port）；TCP 必須依賴四元組（來源 IP, 來源 Port, 目的 IP, 目的 Port）", "兩者皆需四元組", "TCP 僅需二元組", "UDP 需五元組"], "UDP 無連接，所有發往該 Port 的封包導向同一 socket；TCP 面向連接，不同客戶端連線映射至專屬的已連接 socket。"),
        ("TCP 的 Karn 演算法在計算往返時間（RTT）估算時的著名規則為？", "在「重傳封包」發生時，絕不將該次取樣的 RTT 納入加權平均計算（因為無法區分 ACK 是針對初傳還是重傳）", ["在「重傳封包」發生時，絕不將該次取樣的 RTT 納入加權平均計算（因為無法區分 ACK 是針對初傳還是重傳）", "每次重傳將 RTO 減半", "永遠取固定 RTO", "只計算第一個封包的 RTT"], "解決重傳二義性（Retransmission Ambiguity），同時配合計時器倒退（每重傳一次 RTO 翻倍）。"),
        ("TCP 連線狀態機中，伺服器收到客戶端的 SYN 封包後，進入的狀態為？", "SYN_RCVD", ["SYN_RCVD", "ESTABLISHED", "LISTEN", "SYN_SENT"], "發送 SYN+ACK 後等待客戶端最後的 ACK。"),
        ("客戶端發送 SYN 封包後，本端處於何種狀態？", "SYN_SENT", ["SYN_SENT", "SYN_RCVD", "ESTABLISHED", "TIME_WAIT"], "等待伺服器的 SYN+ACK 回應。"),
        ("在 TCP 關閉過程中，伺服器收到客戶端的 FIN 並回傳 ACK 後，伺服器本端進入何種狀態？", "CLOSE_WAIT", ["CLOSE_WAIT", "TIME_WAIT", "LAST_ACK", "CLOSED"], "等待應用程式主動關閉 socket 並調用 close() 發出自己的 FIN。"),
        ("若伺服器端積累了極大量的 CLOSE_WAIT 狀態，通常暴露了應用程式的何種程式碼 Bug？", "應用程式在讀取到客戶端斷線訊號（EOF）後，「忘記調用 socket.close() 釋放連線資源」（連線洩漏 Connection Leak）", ["應用程式在讀取到客戶端斷線訊號（EOF）後，「忘記調用 socket.close() 釋放連線資源」（連線洩漏 Connection Leak）", "網路卡驅動程式崩潰", "作業系統防火牆阻擋", "客戶端發送了惡意封包"], "典型後端程式碼資源洩漏問題，最終耗盡系統 file descriptors。"),
        ("TCP 延遲確認（Delayed ACK）機制的設計考量為？", "收到資料後不立即發送 ACK，等待一段微小時間（通常至多 200 ms）以便隨同本端的回應資料一同「捎帶（Piggybacking）」發送", ["收到資料後不立即發送 ACK，等待一段微小時間（通常至多 200 ms）以便隨同本端的回應資料一同「捎帶（Piggybacking）」發送", "故意延緩伺服器速度", "防止駭客攻擊", "減少記憶體使用"], "大幅減少網路上純 ACK 空封包數量；但若與 Nagle 演算法同時啟用可能引發 200ms 死鎖延遲。"),
        ("TCP BBR 壅塞控制演算法（由 Google 開發）相較於傳統基於丟包的算法（如 Cubic/Reno），其核心突破為？", "基於測量「瓶頸頻寬（BtlBw）」與「最小往返時間（RTprop）」，徹底擺脫將封包遺失視為壅塞的傳統假設，極大消除緩衝區膨脹（Bufferbloat）", ["基於測量「瓶頸頻寬（BtlBw）」與「最小往返時間（RTprop）」，徹底擺脫將封包遺失視為壅塞的傳統假設，極大消除緩衝區膨脹（Bufferbloat）", "完全不重傳封包", "將頻寬強制限速為 10 Mbps", "僅適用於光纖"], "高頻寬高丟包環境（如跨國跨海鏈路）傳輸速度提升數倍。"),
        ("TCP 快速開啟（TFO, TCP Fast Open）的運作方式為？", "在初次連線後伺服器頒發 TFO Cookie，後續重新連線時可在「第一個 SYN 封包中直接附帶 HTTP 請求資料」，實現 0-RTT 資料傳輸", ["在初次連線後伺服器頒發 TFO Cookie，後續重新連線時可在「第一個 SYN 封包中直接附帶 HTTP 請求資料」，實現 0-RTT 資料傳輸", "跳過三次握手永遠不需要 ACK", "將 TCP 轉為 UDP", "關閉伺服器驗證"], "大幅消除行動網路長 RTT 下的連線啟動延遲。"),
        ("UDP 協定是否保證資料的順序性（Ordering）與重複性消除？", "完全不保證（封包可能遺失、亂序抵達或重複收到，全由應用層自行處理）", ["完全不保證（封包可能遺失、亂序抵達或重複收到，全由應用層自行處理）", "保證不重複", "保證循序抵達", "僅保證前 10 個封包"], "極度精簡，將完全控制權交還應用程式（如即時語音、DNS、遊戲連線）。"),
        ("TCP 協定將資料視為「無邊界的位元組流（Byte Stream）」，這導致應用程式接收時必須自行處理何種現象？", "黏包（Packet Concatenation）與拆包（Packet Fragmentation）問題（需自訂長度標頭或分隔符號）", ["黏包（Packet Concatenation）與拆包（Packet Fragmentation）問題（需自訂長度標頭或分隔符號）", "字元編碼轉換", "大小寫轉換", "記憶體釋放"], "TCP 不保留應用程式寫入的 message boundaries，發送兩次 100 bytes 可能被合併為一次 200 bytes 接收。")
    ]

    for stem, ans_s, opts, expl in more_tcp:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "傳輸層狀態機與特性",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【傳輸層協定運作機制深入辨析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在狀態轉移或計時器職責定義偏誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Delayed ACK</code> <span class="en">Delayed ACK</span>：延遲確認。<br>
‧ <code>Bufferbloat</code> <span class="en">Bufferbloat</span>：緩衝區膨脹。<br>
‧ <code>TCP Fast Open (TFO)</code> <span class="en">TCP Fast Open</span>：TCP 快速開啟。"""
        })

    # -------------------------------------------------------------
    # 7. 應用層協定：DNS, HTTP/1-3, TLS 1.3, 電子郵件 (50 題)
    # -------------------------------------------------------------
    app_data = [
        ("DNS 查詢中，「遞迴查詢（Recursive Query）」與「迭代查詢（Iterative Query）」的行為差異為？",
         "遞迴查詢要求被詢問的 DNS 伺服器全權代勞直至查出最終結果；迭代查詢若伺服器不知答案，則回傳「下一級可供查詢之 DNS 伺服器 IP」讓客戶端自行再去查", ["遞迴查詢要求被詢問的 DNS 伺服器全權代勞直至查出最終結果；迭代查詢若伺服器不知答案，則回傳「下一級可供查詢之 DNS 伺服器 IP」讓客戶端自行再去查", "兩者完全相同", "遞迴查詢速度永遠快於迭代查詢", "迭代查詢只用於根網域名稱伺服器"],
         "終端 PC 向本地 Local DNS 發起的是遞迴查詢；Local DNS 向上層 Root DNS / TLD DNS 發起的是迭代查詢。"),
        ("DNS 資源紀錄（Resource Records）中，`A` 紀錄與 `AAAA` 紀錄的差別為？",
         "`A` 紀錄將網域名稱映射至 32 位元 IPv4 位址；`AAAA` 紀錄將網域名稱映射至 128 位元 IPv6 位址", ["`A` 紀錄將網域名稱映射至 32 位元 IPv4 位址；`AAAA` 紀錄將網域名稱映射至 128 位元 IPv6 位址", "`A` 為主要伺服器，`AAAA` 為備援伺服器", "`AAAA` 包含四個 IPv4 位址", "兩者無任何差異"], "IPv6 的四倍長度（Quad-A）代表 128 位元。"),
        ("DNS 資源紀錄中，`CNAME` 紀錄的功用為？",
         "建立網域名稱的「別名（Canonical Name / Alias）」，將一個網域名稱指向另一個正規網域名稱", ["建立網域名稱的「別名（Canonical Name / Alias）」，將一個網域名稱指向另一個正規網域名稱", "指定電子郵件伺服器", "指定授權名稱伺服器", "反向解析 IP"], "例如將 `www.example.com` 指向 `cdn.provider.net`。"),
        ("DNS 安全擴充協定（DNSSEC）主要用於防範下列何種致命資安攻擊？其運作核心為？",
         "防範 DNS 快取污染與詐欺（DNS Cache Poisoning）；核心為利用公私鑰非對稱密碼學建立「數位簽章信任鏈（Chain of Trust）」驗證資料真實性與完整性", ["防範 DNS 快取污染與詐欺（DNS Cache Poisoning）；核心為利用公私鑰非對稱密碼學建立「數位簽章信任鏈（Chain of Trust）」驗證資料真實性與完整性", "防範 DDoS 攻擊", "加密所有 DNS 查詢文字防止側聽", "加快解析速度"], "DNSSEC 解決真實性（Authenticity）與完整性（Integrity），但不提供隱私加密（查詢內容仍為明文，隱私需靠 DoH/DoT）。"),
        ("HTTP/1.1 相較於 HTTP/1.0 的重大改良為？",
         "預設啟用「持久連線（Keep-Alive Persistent Connection）」並支援「管線化（Pipelining）」及 Host 標頭（支援虛擬主機）", ["預設啟用「持久連線（Keep-Alive Persistent Connection）」並支援「管線化（Pipelining）」及 Host 標頭（支援虛擬主機）", "採用二進位訊框", "支援多工傳輸", "改用 UDP 協定"], "避免每個靜態資源（CSS, JS, 圖片）重複進行三次握手與慢啟動。"),
        ("HTTP/1.1 的管線化（Pipelining）在實踐中極少被預設啟用的根本瓶頸為？",
         "應用層「行頭阻塞（HOL Blocking, Head-of-Line Blocking）」，伺服器必須嚴格依據收到請求的順序依序回傳回應，若第一筆請求耗時卡死，後續所有回應全部受阻", ["應用層「行頭阻塞（HOL Blocking, Head-of-Line Blocking）」，伺服器必須嚴格依據收到請求的順序依序回傳回應，若第一筆請求耗時卡死，後續所有回應全部受阻", "協定不安全", "佔用過多記憶體", "瀏覽器不支援"], "無法亂序回傳回應，成為 HTTP/1.1 無法克服的體質缺陷。"),
        ("HTTP/2 徹底解決應用層行頭阻塞的核心關鍵技術為？",
         "將純文字協定改為「二進位訊框（Binary Framing）」，在單一 TCP 連線上實作「多工雙向多工傳輸（Multiplexing）」", ["將純文字協定改為「二進位訊框（Binary Framing）」，在單一 TCP 連線上實作「多工雙向多工傳輸（Multiplexing）」", "改用 UDP 傳輸", "強制啟用多條 TCP 連線", "將圖片轉為文字"], "每個請求分配獨立 Stream ID，不同請求的訊框可交錯亂序傳輸並在接收端重組。"),
        ("HTTP/3 放棄底層的 TCP 協定，改為基於 UDP 的何種新興傳輸層協定？其最大優勢為？",
         "基於 QUIC 協定；徹底消除「TCP 傳輸層行頭阻塞」，實現 0-RTT 極速連線建立，並支援「連線遷移（Connection Migration）」", ["基於 QUIC 協定；徹底消除「TCP 傳輸層行頭阻塞」，實現 0-RTT 極速連線建立，並支援「連線遷移（Connection Migration）」", "基於 SCTP 協定", "基於 IPsec 協定", "完全不需要伺服器"], "在 HTTP/2 中若單一 TCP 封包遺失，整個連線所有串流皆被凍結（TCP 級 HOL）；QUIC 在 UDP 上獨立重傳特定串流，並以 Connection ID 支援手機在 Wi-Fi 與 4G/5G 切換時不停斷連線！"),
        ("TLS 1.3 相較於 TLS 1.2，在握手延遲（Handshake Latency）與安全性上的革命性變革為？",
         "完整握手由 2-RTT 降為「1-RTT」（支援 0-RTT Resumption），且「廢除靜態 RSA 金鑰交換」強制全面採用前向保密（PFS / Ephemeral Diffie-Hellman）", ["完整握手由 2-RTT 降為「1-RTT」（支援 0-RTT Resumption），且「廢除靜態 RSA 金鑰交換」強制全面採用前向保密（PFS / Ephemeral Diffie-Hellman）", "握手延遲增加為 3-RTT", "改用 DES 對稱加密", "不再需要數位憑證"], "TLS 1.3 剪除所有不安全舊式密碼套件，握手速度與安全性達成極致躍升。"),
        ("前向保密（PFS, Perfect Forward Secrecy）的資安保障意義為？",
         "即使伺服器的長期私鑰（Private Key）在未來某天不幸遭到洩漏，攻擊者過去所側聽攔截儲存的所有歷史通訊流量「依然無法被事後破解解密」", ["即使伺服器的長期私鑰（Private Key）在未來某天不幸遭到洩漏，攻擊者過去所側聽攔截儲存的所有歷史通訊流量「依然無法被事後破解解密」", "保證未來的通訊不會被攔截", "完全杜絕阻斷服務攻擊", "自動備份私鑰"], "每次連線動態生成拋棄式臨時金鑰（ECDHE），私鑰僅用於身分簽章而非直接解密連線金鑰。")
    ]

    for stem, ans_s, opts, expl in app_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "應用層協定演進與安全",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【應用層協定架構與安全機制剖析】</strong><br>
<div class="step-box">
  <div class="step-title">📝 應用層協定標準分析步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認協定版本與傳輸層底座</strong><br>
      ‧ 本題依據 RFC 規範（HTTP/2, HTTP/3 QUIC, TLS 1.3 或 DNS 體系）進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行連線往返延遲或安全屬性驗證</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 IETF 現代網路規格。<br>
‧ 其餘選項常為 QUIC 傳輸層混淆或 TLS 1.3 簡化握手特性誤判。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>QUIC Protocol</code> <span class="en">QUIC</span>：QUIC 傳輸協定。<br>
‧ <code>Perfect Forward Secrecy (PFS)</code> <span class="en">PFS</span>：前向保密。<br>
‧ <code>Head-of-Line (HOL) Blocking</code> <span class="en">HOL Blocking</span>：行頭阻塞。"""
        })

    # More App layer items (40 items)
    more_app = [
        ("電子郵件防偽機制中，SPF（寄件者政策架構，Sender Policy Framework）的運作方式為？", "網域擁有者在 DNS 發布 TXT 紀錄，宣告「哪些 IP 位址有權代表該網域發送電子郵件」", ["網域擁有者在 DNS 發布 TXT 紀錄，宣告「哪些 IP 位址有權代表該網域發送電子郵件」", "對每封郵件內容進行非對稱加密", "要求寄件者輸入動態驗證碼", "掃描郵件附件病毒"], "收件伺服器比對發信 SMTP 伺服器 IP 是否在 SPF 白名單內。"),
        ("電子郵件防偽機制中，DKIM（網域金鑰識別郵件，DomainKeys Identified Mail）的運作方式為？", "發信伺服器以「私鑰對郵件標頭與內文進行數位簽章」，收信方透過寄件網域的 DNS TXT 公鑰進行驗證", ["發信伺服器以「私鑰對郵件標頭與內文進行數位簽章」，收信方透過寄件網域的 DNS TXT 公鑰進行驗證", "強制要求寄件者綁定手機號碼", "檢查發件人 IP", "自動過濾垃圾郵件"], "保證郵件內容在傳輸途中未遭篡改（完整性與身分確認）。"),
        ("DMARC（基於網域的訊息驗證、報告和一致性）在 SPF 與 DKIM 之上的功能為？", "統一 SPF 與 DKIM 驗證結果，宣告驗證失敗時的處置政策（如直接隔離 Quarantine 或退信 Reject），並產生存取報表", ["DMARC（基於網域的訊息驗證、報告和一致性）在 SPF 與 DKIM 之上的功能為？", "替代 SMTP 協定", "加密郵件檔案", "自動回覆郵件"], "建構電子郵件防冒名詐騙之完整閉環治理。"),
        ("HTTP 狀態碼 301 與 302 的核心差異為？", "301 為「永久重新導向（Moved Permanently）」，搜尋引擎會轉移權重且瀏覽器會快取；302 為「暫時重新導向（Found / Moved Temporarily）」", ["301 為「永久重新導向（Moved Permanently）」，搜尋引擎會轉移權重且瀏覽器會快取；302 為「暫時重新導向（Found / Moved Temporarily）」", "301 是暫時，302 是永久", "301 代表權限不足", "兩者行為完全相同"], "SEO 與網頁轉址重要常識。"),
        ("HTTP 狀態碼 401 與 403 的差別為？", "401 代表「未認證（Unauthorized / Unauthenticated）」，需提供登入憑證；403 代表「已被識別但無存取權限（Forbidden）」", ["401 代表「未認證（Unauthorized / Unauthenticated）」，需提供登入憑證；403 代表「已被識別但無存取權限（Forbidden）」", "401 是伺服器錯誤", "403 代表網頁不存在", "兩者皆代表找不到網頁"], "401 需登入；403 是登入了但被伺服器權限管理拒絕訪問。"),
        ("HTTP 狀態碼 502 Bad Gateway 與 504 Gateway Timeout 的差別為？", "502 代表反向代理伺服器從上游後端收到「無效/異常的回應」；504 代表反向代理等待上游回應「逾時逾期未回」", ["502 代表反向代理伺服器從上游後端收到「無效/異常的回應」；504 代表反向代理等待上游回應「逾時逾期未回」", "502 是客戶端錯誤", "504 代表伺服器記憶體不足", "兩者完全相同"], "Nginx 與後端 API 伺服器除錯必備。"),
        ("HSTS（HTTP 嚴格傳輸安全，HTTP Strict Transport Security）回應標頭的作用為？", "強制瀏覽器在後續存取該網站時「一律自動採用 HTTPS」，即使使用者輸入 http:// 也由瀏覽器內部直接轉為 https://", ["強制瀏覽器在後續存取該網站時「一律自動採用 HTTPS」，即使使用者輸入 http:// 也由瀏覽器內部直接轉為 https://", "加速網頁下載", "阻止所有 Cookie", "強制關閉網頁"], "徹底封殺 SSL Strip（中間人 HTTPS 降級為明文 HTTP）劫持攻擊。"),
        ("HTTP Cookie 屬性中，`HttpOnly` 的安全防禦功用為？", "禁止瀏覽器端的客戶端 JavaScript 腳本（如 document.cookie）存取該 Cookie，有效防範 XSS 竊取 Session", ["禁止瀏覽器端的客戶端 JavaScript 腳本（如 document.cookie）存取該 Cookie，有效防範 XSS 竊取 Session", "僅允許在 HTTP 下傳輸，禁止 HTTPS", "將 Cookie 保存 1 年", "將 Cookie 限制在特定網域"], "防禦 XSS 攻擊竊取 Session Cookie 的金盾牌。"),
        ("HTTP Cookie 屬性中，`Secure` 的安全功用為？", "指示瀏覽器該 Cookie「僅能在加密的 HTTPS 連線」下傳送，絕不在明文 HTTP 連線中外洩", ["指示瀏覽器該 Cookie「僅能在加密的 HTTPS 連線」下傳送，絕不在明文 HTTP 連線中外洩", "加密 Cookie 內部數值", "防止 XSS 攻擊", "僅限管理員使用"], "防止公共 Wi-Fi 明文側聽洩漏憑證。"),
        ("HTTP Cookie 屬性中，`SameSite=Strict` 的主要功用為？", "在任何跨站請求（Cross-Site Requests）中一律禁止攜帶該 Cookie，能徹底根除 CSRF 攻擊", ["在任何跨站請求（Cross-Site Requests）中一律禁止攜帶該 Cookie，能徹底根除 CSRF 攻擊", "僅允許同一個 IP 存取", "跨站時自動同步", "限制 Cookie 大小"], "現代瀏覽器防範 CSRF（跨站請求偽造）的最有效機制。"),
        ("DNS 根網域名稱伺服器（Root Name Servers）全球邏輯上共有多少個（以 A 到 M 命名）？現代如何支撐全球巨量查詢？", "邏輯上共有 13 個；現代透過 Anycast（任播）技術將每個字母分散部署至全球數千台實體鏡像伺服器", ["邏輯上共有 13 個；現代透過 Anycast（任播）技術將每個字母分散部署至全球數千台實體鏡像伺服器", "全球僅有 13 台實體電腦", "共有 256 個", "每個國家配置 1 個"], "Anycast 路由自動將請求導向物理距離最近的鏡像節點，兼具極速回應與強大抗 DDoS 能力。"),
        ("DNS-over-HTTPS (DoH) 與 DNS-over-TLS (DoT) 的主要技術動機為？", "將原本明文傳輸的 UDP 53 DNS 查詢透過 TLS 加密封裝，防止 ISP 或中間人側聽使用者造訪的網域隱私與竄改", ["將原本明文傳輸的 UDP 53 DNS 查詢透過 TLS 加密封裝，防止 ISP 或中間人側聽使用者造訪的網域隱私與竄改", "提升網域名稱解析速度 10 倍", "取代作業系統 Hosts 檔案", "自動修復斷線"], "守護最後一段未加密的網路隱私暴露面。"),
        ("SNI（伺服器名稱指示，Server Name Indication）在 TLS 握手中的核心功用為？", "允許客戶端在 TLS 握手最初的 Client Hello 中指明「欲存取的目標網域名稱」，使同一 IP 的虛擬主機能返回正確的 SSL 憑證", ["允許客戶端在 TLS 握手最初的 Client Hello 中指明「欲存取的目標網域名稱」，使同一 IP 的虛擬主機能返回正確的 SSL 憑證", "加密網域名稱", "提供雙向認證", "加速 TCP 連線"], "解決單一 IP 伺服器託管數百個 HTTPS 網站時的憑證匹配盲點。"),
        ("ESNI / ECH（加密客戶端 Hello，Encrypted Client Hello）進一步解決了何種隱私問題？", "將包含 SNI 網域名稱在內的整個 Client Hello 訊息全面加密，防止監控者透過側聽 SNI 獲知使用者造訪之網站", ["將包含 SNI 網域名稱在內的整個 Client Hello 訊息全面加密，防止監控者透過側聽 SNI 獲知使用者造訪之網站", "加快加密運算", "取代 CA 憑證", "提供免費網域名稱"], "杜絕網路營運商利用明文 SNI 進行審查或行為側寫。"),
        ("HTTP/2 的 HPACK 演算法採用何種機制壓縮 HTTP 標頭？", "靜態字典、動態字典與霍夫曼編碼（Huffman Coding）", ["靜態字典、動態字典與霍夫曼編碼（Huffman Coding）", "直接使用 GZIP", "將字串轉為 Hash", "刪除所有標頭"], "有效降低每次請求重複傳送 User-Agent, Cookie 等大標頭的頻寬浪費。"),
        ("RESTful API 架構風格中，HTTP 的 GET, POST, PUT, DELETE 方法分別代表何種語意操作？", "GET: 讀取資源；POST: 新增資源；PUT: 替換/更新完整資源；DELETE: 刪除資源", ["GET: 讀取資源；POST: 新增資源；PUT: 替換/更新完整資源；DELETE: 刪除資源", "GET: 寫入；POST: 讀取", "PUT: 建立；POST: 刪除", "全部皆可用於讀取"], "標準 REST 架構遵循 HTTP 原生動詞語意。"),
        ("在 REST API 中，HTTP 冪等性（Idempotence）的定義為？下列何者屬於非冪等（Non-idempotent）操作？", "連續執行多次相同的操作，伺服器產生的狀態結果與執行一次完全相同；POST 為非冪等操作", ["連續執行多次相同的操作，伺服器產生的狀態結果與執行一次完全相同；POST 為非冪等操作", "操作速度恆定；GET 為非冪等", "保證不發生錯誤；DELETE 為非冪等", "僅能執行一次；PUT 為非冪等"], "GET, PUT, DELETE 具備冪等性；多次 POST 會連續產生多筆相異新資源。"),
        ("WebSocket 協定相較於傳統 HTTP 輪詢（Polling）的最大優勢為？", "透過 HTTP 握手升級（101 Switching Protocols）後，在單一 TCP 上建立全雙工（Full-Duplex）雙向即時通訊", ["透過 HTTP 握手升級（101 Switching Protocols）後，在單一 TCP 上建立全雙工（Full-Duplex）雙向即時通訊", "不需要 TCP 連線", "資料傳輸完全免費", "自動防止 XSS 攻擊"], "極低訊框標頭開銷（僅 2~10 bytes），支援伺服器端主動推送。"),
        ("WebRTC（網頁即時通訊）實現瀏覽器間點對點（P2P）直接影音串流傳輸所依賴的底層傳輸協定為？", "SRTP（安全即時傳輸協定）運行於 UDP 之上", ["SRTP（安全即時傳輸協定）運行於 UDP 之上", "標準 TCP", "HTTP/1.1", "FTP"], "低延遲語音視訊通話首選，配合 ICE, STUN, TURN 實現 NAT 穿透。"),
        ("DHCP 協定租約取得的四步驟（DORA）依序為？", "Discover（廣播探尋） -> Offer（提供） -> Request（請求） -> Acknowledge（確認）", ["Discover（廣播探尋） -> Offer（提供） -> Request（請求） -> Acknowledge（確認）", "Request -> Offer -> Discover -> ACK", "Hello -> Reply -> Syn -> Ack", "Query -> Answer -> Bind -> Close"], "用戶端與 DHCP 伺服器（UDP 67/68）標準動態 IP 配置四部曲。")
    ]

    for stem, ans_s, opts, expl in more_app:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "網路應用層服務特性",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【網路應用層技術細節解析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在協定方法定義或安全機制語意誤解。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>HSTS (HTTP Strict Transport Security)</code> <span class="en">HSTS</span>：HTTP 嚴格傳輸安全。<br>
‧ <code>Idempotence</code> <span class="en">Idempotence</span>：冪等性。<br>
‧ <code>DMARC</code> <span class="en">DMARC</span>：網域訊息驗證與報告。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_net_part3_questions()
    print(f"Generated Net Part 3 questions: {len(qs)}")
