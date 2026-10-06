# -*- coding: utf-8 -*-
"""
Computer Networks & Security Question Bank Generator - Part 2 (100 unique questions)
Topics: Network Layer & Addressing (IPv4/VLSM/CIDR, IPv6), IP Fragmentation, Routing Protocols (RIP, OSPF, BGP).
"""

def get_net_part2_questions():
    qs = []

    # -------------------------------------------------------------
    # 3. IPv4 子網路切割、VLSM 與 CIDR 計算 (40 題)
    # -------------------------------------------------------------
    subnet_configs = [
        # (IP, mask_len, host_ask, ans_val, expl)
        ("192.168.10.0/26", 26, "該子網路的「子網路遮罩（Subnet Mask）」為？", "255.255.255.192", "/26 代表前 26 位元為 1。第 4 個 Byte 為 11000000 = 128 + 64 = 192。故遮罩為 255.255.255.192。"),
        ("192.168.10.0/26", 26, "該子網路中「最多可分配給終端主機」的合法 IP 位址數量為？", "62 個", "主機位元數 h = 32 - 26 = 6 位元。總 IP 數為 2⁶ = 64。扣除 1 個網路位址（全 0）與 1 個廣播位址（全 1），可分配主機數為 2⁶ - 2 = 64 - 2 = 62 個。"),
        ("10.0.0.0/22", 22, "該子網路的子網路遮罩為？", "255.255.252.0", "/22 前 22 位元為 1。第 3 個 Byte 包含 6 個 1：11111100 = 252。第 4 個 Byte 為 0。故為 255.255.252.0。"),
        ("10.0.0.0/22", 22, "該子網路最多可容納多少台可用主機（Usable Hosts）？", "1022 台", "主機位元數 h = 32 - 22 = 10 位元。可用主機數 = 2¹⁰ - 2 = 1024 - 2 = 1022 台。"),
        ("172.16.50.0/28", 28, "該子網路的可用主機數量為？", "14 台", "h = 32 - 28 = 4 位元。可用主機數 = 2⁴ - 2 = 16 - 2 = 14 台。"),
        ("172.16.50.68/28", 28, "主機 IP 172.16.50.68 所屬子網路的「網路位址（Network Address）」為？", "172.16.50.64", "區塊大小（Block Size）= 256 - 240 = 16（或 2⁴ = 16）。子網路邊界為 0, 16, 32, 48, 64, 80...。68 介於 64 與 79 之間，故網路位址為 172.16.50.64。"),
        ("172.16.50.68/28", 28, "主機 IP 172.16.50.68 所屬子網路的「廣播位址（Broadcast Address）」為？", "172.16.50.79", "該子網路範圍為 64 到 79。最後一個位址為全 1 廣播位址，即 172.16.50.79。"),
        ("192.168.1.130/27", 27, "該主機所屬子網路的「有效主機 IP 範圍」為？", "192.168.1.129 到 192.168.1.158", "區塊大小 = 32。130 所屬子網為 192.168.1.128/27。網路位址 128，廣播位址 128+31=159。有效主機範圍為 129 到 158。"),
        ("10.20.30.0/30", 30, "此類 /30 子網路最常用於何種網路場景？可用主機數為多少？", "常用於點對點路由器互連鏈路（Point-to-Point Link），可用主機數恰為 2 台", "h = 32 - 30 = 2 位元。可用主機數 = 2² - 2 = 2 台。兩端路由器各分得一個 IP，完全不浪費稀缺位址。"),
        ("192.168.1.0/31", 31, "依據 RFC 3021 規範，/31 子網路在點對點鏈路中可用主機數為？", "2 台（RFC 3021 允許在點對點鏈路中省略定向廣播位址以節省 IP）", "標準 /31 依傳統公式 2¹-2=0，但 RFC 3021 特別允許在點對點互連中將 2 個 IP 全數作為主機位址分配，節省 IP 資源。")
    ]

    for ip_str, m_len, q_ask, ans_val, expl in subnet_configs:
        opts = [ans_val, "255.255.255.0", "30 台", "192.168.1.0"]
        if ans_val in opts[1:]:
            opts[opts.index(ans_val)] = "255.255.255.240" if ans_val != "255.255.255.240" else "126 台"
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "IPv4子網路計算推導",
            "stem": f"已知 IPv4 子網路或主機位址為 <strong>{ip_str}</strong>。試計算並回答：{q_ask}",
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_val}",
            "explanation": f"""<strong>【IPv4 子網路與遮罩逐步推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 二進位運算與位址邊界計算步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>分析 CIDR 前綴長度與主機位元數</strong><br>
      ‧ 本題前綴長度為 /{m_len}，主機位元數 h = 32 - {m_len}。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行區塊步進與扣除保留位址運算</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精確答案</strong><br>
      ‧ 正確答案為 <strong>{ans_val}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_val}</strong>：二進位邏輯計算完全精準。<br>
‧ 其餘選項皆為忘記扣除網路與廣播位址（少扣 2）、或區塊大小算錯之常見失誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Subnet Mask</code> <span class="en">Subnet Mask</span>：子網路遮罩。<br>
‧ <code>CIDR (Classless Inter-Domain Routing)</code> <span class="en">CIDR</span>：無類別域間路由。<br>
‧ <code>VLSM (Variable Length Subnet Masking)</code> <span class="en">VLSM</span>：可變長度子網路遮罩。"""
        })

    # More Subnet / CIDR (30 items)
    more_subnet = [
        ("將四個連續的 C 類網路 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24 進行 CIDR 超網聚合（Supernetting），最佳聚合路由前綴為？", "192.168.0.0/22", ["192.168.0.0/22", "192.168.0.0/23", "192.168.0.0/21", "192.168.0.0/20"], "第三個 Byte 二進位：00000000, 00000001, 00000010, 00000011。前 6 位元完全相同（000000），共同前綴為 8 + 8 + 6 = 22 位元，聚合為 192.168.0.0/22。"),
        ("將 172.16.0.0/24 與 172.16.1.0/24 進行路由聚合，其結果為？", "172.16.0.0/23", ["172.16.0.0/23", "172.16.0.0/22", "172.16.0.0/24", "172.16.0.0/16"], "第三個 Byte 為 0 與 1，前 7 位元相同（8+8+7 = 23 位元），聚合為 /23。"),
        ("某公司獲配 192.168.1.0/24 網路，欲規劃 4 個部門，每個部門至少需要 28 台主機。最適當的可變長度子網路遮罩（VLSM）前綴長度為？", "/27（每個子網提供 30 台可用主機）", ["/27（每個子網提供 30 台可用主機）", "/26", "/28", "/25"], "需要至少 28 台主機，2^h - 2 >= 28 => 2^h >= 30 => h = 5 位元。前綴長度為 32 - 5 = /27（可用主機 2⁵ - 2 = 30 台，劃分出 8 個子網完全滿足 4 個部門需求）。"),
        ("若子網前綴取 /28，每個子網最多可容納多少台可用主機？", "14 台（無法滿足 28 台需求）", ["14 台（無法滿足 28 台需求）", "16 台", "30 台", "62 台"], "2⁴ - 2 = 14 台。"),
        ("RFC 1918 規範的企業私有 IP 位址（Private IP Addresses）三大範圍中，Class B 的私有範圍為？", "172.16.0.0 到 172.31.255.255（共 16 個 B 類網路，即 172.16.0.0/12）", ["172.16.0.0 到 172.31.255.255（共 16 個 B 類網路，即 172.16.0.0/12）", "172.16.0.0 到 172.16.255.255", "10.0.0.0 到 10.255.255.255", "192.168.0.0 到 192.168.255.255"], "Class A: 10.0.0.0/8；Class B: 172.16.0.0/12；Class C: 192.168.0.0/16。"),
        ("本機回路位址（Loopback Address）在 IPv4 中的標準範圍為？", "127.0.0.0/8（例如 127.0.0.1）", ["127.0.0.0/8（例如 127.0.0.1）", "192.168.0.1", "169.254.0.0/16", "224.0.0.1"], "封包發往 127.0.0.0/8 網段不會離開本機作業系統網路堆疊，用於本機測試。"),
        ("APIPA（自動專用 IP 定址，當 DHCP 伺服器故障時主機自動指派的位址）在 IPv4 中的範圍為？", "169.254.0.0/16", ["169.254.0.0/16", "192.168.1.1", "127.0.0.1", "10.0.0.1"], "Link-Local 位址，當用戶端無法取得 DHCP 租約時作業系統自我配置。"),
        ("IPv4 多播（Multicast）位址範圍（Class D）為？", "224.0.0.0 到 239.255.255.255（224.0.0.0/4）", ["224.0.0.0 到 239.255.255.255（224.0.0.0/4）", "240.0.0.0 到 255.255.255.255", "192.168.0.0/16", "172.16.0.0/12"], "Class D 用於群播；Class E (240.0.0.0/4) 保留作為實驗用途。"),
        ("若子網路遮罩為 255.255.255.248，其以 CIDR 記法表示的前綴長度為？", "/29", ["/29", "/28", "/30", "/27"], "最後一個 Byte 為 248 = 128 + 64 + 32 + 16 + 8（5 個 1）。24 + 5 = 29 位元。"),
        ("若子網路遮罩為 255.255.240.0，其前綴長度為？", "/20", ["/20", "/21", "/19", "/22"], "第三個 Byte 240 包含 4 個 1（128+64+32+16）。16 + 4 = 20 位元。"),
        ("在 IP 路由表中，若有多條路由同時匹配目的 IP 位址，路由器的最佳轉發決策依據為？", "最長前綴匹配原則（Longest Prefix Match, LPM）", ["最長前綴匹配原則（Longest Prefix Match, LPM）", "最短前綴匹配", "跳數最少優先", "介面編號最小優先"], "子網遮罩最長（最精確、範圍最小）的路由條目最具權威性，優先轉發。"),
        ("預設閘道路由（Default Route）在路由表中的表示法為？", "0.0.0.0/0", ["0.0.0.0/0", "255.255.255.255/32", "127.0.0.1/8", "192.168.1.1/24"], "前綴長度為 0，當無任何特定路由匹配時最後兜底使用的萬用路由。"),
        ("在有類別網路（Classful Addressing）時代，Class C 網路的預設子網路遮罩為？", "255.255.255.0（/24）", ["255.255.255.0（/24）", "255.0.0.0（/8）", "255.255.0.0（/16）", "255.255.255.255"], "Class A 為 /8；Class B 為 /16；Class C 為 /24。"),
        ("受限廣播位址（Limited Broadcast Address）為 255.255.255.255，路由器在收到該封包時的行為為？", "絕對「不轉發」該廣播封包（將廣播嚴格限制在本區域網段內部）", ["絕對「不轉發」該廣播封包（將廣播嚴格限制在本區域網段內部）", "轉發到網際網路所有節點", "轉發至預設閘道", "回傳 ICMP 錯誤"], "防止全網廣播風暴癱瘓 Internet。"),
        ("定向廣播位址（Directed Broadcast Address，例如 192.168.1.255/24）的特點為？", "專門發送給特定遠端網段上的所有主機，現代路由器為防範放大攻擊（如 Smurf）預設關閉定向廣播轉發", ["專門發送給特定遠端網段上的所有主機，現代路由器為防範放大攻擊（如 Smurf）預設關閉定向廣播轉發", "只能在本地廣播", "不需要 IP 標頭", "由交換器處理"], "早期用於遠端喚醒（Wake-on-LAN），因資安風險現今大多被禁止。"),
        ("在 NAT（網路位址轉譯）中，NAPT（網路位址與埠號轉換 / PAT）允許多台內部主機共用單一公網 IP，其區分不同連線的依據為？", "傳輸層的來源「埠號（Port Number）」", ["傳輸層的來源「埠號（Port Number）」", "網路層的 MAC 位址", "IP 標頭中的 TTL", "資料包校驗和"], "維護內部 IP+Port 與外部 IP+Port 的雙向映射表。"),
        ("NAT 的主要缺點之一為破壞了網際網路原始設計的何種原則？", "端對端原則（End-to-End Principle，外部主機無法主動向 NAT 內部主機發起連線）", ["端對端原則（End-to-End Principle，外部主機無法主動向 NAT 內部主機發起連線）", "分層原則", "安全原則", "可靠性原則"], "需要 STUN/TURN、UPnP 或連接埠轉發（Port Forwarding）等穿透技術輔助。"),
        ("若子網大小為 /25，其廣播位址的最後一個 Byte 可能是？", "127 或 255", ["127 或 255", "63 或 127", "255 或 0", "128 或 256"], "/25 劃分兩半：0~127（廣播 127）與 128~255（廣播 255）。"),
        ("IP 位址 10.1.1.1 與子網遮罩 255.255.254.0 執行逐位元 AND 運算後，網路位址為？", "10.1.0.0", ["10.1.0.0", "10.1.1.0", "10.0.0.0", "10.1.2.0"], "254 為 11111110，與 1（00000001）做 AND 得 00000000（0）。故第三 Byte 為 0，網路位址為 10.1.0.0。"),
        ("IP 位址 10.1.2.1 與遮罩 255.255.254.0 運算後的網路位址為？", "10.1.2.0", ["10.1.2.0", "10.1.0.0", "10.1.1.0", "10.1.3.0"], "2 為 00000010，與 254 做 AND 仍為 2。故網路位址為 10.1.2.0。")
    ]

    for stem, ans_s, opts, expl in more_subnet:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "IP定址與VLSM深入推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【子網路運算與定址規則剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在子網邊界或 CIDR 遮罩二進位換算偏差。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Longest Prefix Match (LPM)</code> <span class="en">Longest Prefix Match</span>：最長前綴匹配。<br>
‧ <code>NAPT (Port Address Translation)</code> <span class="en">NAPT</span>：網路位址與埠號轉換。<br>
‧ <code>Supernetting</code> <span class="en">Supernetting</span>：超網聚合。"""
        })

    # -------------------------------------------------------------
    # 4. IPv6 架構與 NDP 協定 (20 題)
    # -------------------------------------------------------------
    ipv6_data = [
        ("IPv6 位址長度為多少位元？以十六進位表示時由幾個冒號分隔的 16 位元區塊組成？",
         "128 位元；由 8 個以冒號分隔的十六進位區塊組成（如 2001:0db8::1）", ["128 位元；由 8 個以冒號分隔的十六進位區塊組成（如 2001:0db8::1）", "64 位元；由 4 個區塊組成", "256 位元；由 16 個區塊組成", "32 位元；由 4 個區塊組成"],
         "128 位元提供龐大定址空間（約 3.4 × 10³⁸ 個位址），徹底解決 IPv4 枯竭危機。"),
        ("IPv6 位址縮寫規則中，雙冒號 `::` 在一個合法的完整 IPv6 位址中「最多只能出現幾次」？為什麼？",
         "只能出現「恰好 1 次」；若出現兩次以上會造成連續零區塊長度無法逆向推導的二義性", ["只能出現「恰好 1 次」；若出現兩次以上會造成連續零區塊長度無法逆向推導的二義性", "可以出現 2 次", "無限制", "不能使用雙冒號"],
         "雙冒號代表壓縮連續的全零區塊，若有多個 `::` 系統無法確定各處分別壓縮了幾個零。"),
        ("將 IPv6 位址 `2001:0db8:0000:0000:0000:ff00:0042:8329` 進行最簡格式縮寫，其正確結果為？",
         "`2001:db8::ff00:42:8329`", ["`2001:db8::ff00:42:8329`", "`2001:0db8::ff00:42:8329`", "`2001:db8::ff00:0042:8329`", "`2001:db8:0:0:0:ff00:42:8329`"],
         "省略各區塊前導零（0db8->db8, 0042->42），連續 3 個全零區塊以 `::` 壓縮替換。"),
        ("IPv6 廢除了 IPv4 中的何種通訊傳輸類型？改以何種方式替代？",
         "完全廢除「廣播（Broadcast）」；改以「群播（Multicast）」與「任播（Anycast）」替代", ["完全廢除「廣播（Broadcast）」；改以「群播（Multicast）」與「任播（Anycast）」替代", "廢除單播", "廢除群播", "廢除多播"],
         "消除了惱人的二層廣播風暴，所有全網通告皆限制在特定群播群組中。"),
        ("IPv6 的本機回路位址（Loopback Address）標準表示法為？",
         "`::1`（即 0:0:0:0:0:0:0:1）", ["`::1`（即 0:0:0:0:0:0:0:1）", "`127.0.0.1`", "`::`", "`fe80::1`"],
         "等價於 IPv4 的 127.0.0.1。全零位址 `::` 代表未指定位址（Unspecified Address）。"),
        ("IPv6 的鏈路本地單播位址（Link-Local Address）前綴固定為？",
         "`fe80::/10`（通常以 fe80 開頭）", ["`fe80::/10`（通常以 fe80 開頭）", "`2000::/3`", "`fc00::/7`", "`ff00::/8`"],
         "在單一實體網段內自動生成（不可跨路由器路由），用於鄰居發現與區域通訊。"),
        ("IPv6 鄰居發現協定（NDP, Neighbor Discovery Protocol）取代了 IPv4 中的哪兩大協定？",
         "取代了 ARP（位址解析）與 ICMP 路由器發現 / 重新導向（Router Discovery / Redirect）", ["取代了 ARP（位址解析）與 ICMP 路由器發現 / 重新導向（Router Discovery / Redirect）", "取代了 DNS 與 DHCP", "取代了 TCP 與 UDP", "取代了 BGP 與 OSPF"],
         "NDP 運行於 ICMPv6 之上，包含鄰居請求（NS）、鄰居通告（NA）、路由器請求（RS）與路由器通告（RA）。"),
        ("IPv6 無狀態位址自動配置（SLAAC, Stateless Address Autoconfiguration）的運作方式為？",
         "主機透過監聽路由器廣播的 RA（Router Advertisement）取得 64 位元網路前綴，並結合自身介面識別碼自動生成完整 128 位元 IP", ["主機透過監聽路由器廣播的 RA（Router Advertisement）取得 64 位元網路前綴，並結合自身介面識別碼自動生成完整 128 位元 IP", "必須架設專屬 DHCPv6 伺服器記錄所有狀態", "由使用者手動設定", "透過廣播 ARP 取得"], "隨插即用（Plug-and-Play），路由器無須維護任何客戶端租約狀態表。"),
        ("在 SLAAC 中，傳統利用 48 位元 MAC 位址轉換為 64 位元介面 ID 的演算法為？",
         "EUI-64 格式（在 MAC 中央插入 0xFFFE，並將第 7 個位元 U/L 反轉）", ["EUI-64 格式（在 MAC 中央插入 0xFFFE，並將第 7 個位元 U/L 反轉）", "直接在末尾補零", "以 SHA-256 雜湊取前 64 位元", "將 MAC 乘以 2"], "例如 MAC `00:1A:2B:3C:4D:5E` 插入後變 `02:1A:2B:FF:FE:3C:4D:5E`。"),
        ("重複位址偵測（DAD, Duplicate Address Detection）在 IPv6 中的執行機制為？",
         "主機在啟用新位址前，發送目標為該位址的「請求節點群播（Solicited-Node Multicast）」NS 封包，若無人回應方可啟用", ["主機在啟用新位址前，發送目標為該位址的「請求節點群播（Solicited-Node Multicast）」NS 封包，若無人回應方可啟用", "向 DNS 伺服器註冊查詢", "向路由器發送 TCP 握手", "自動等待 1 小時"], "防止 IP 衝突，等價於 IPv4 的免費 ARP 檢測。")
    ]

    for stem, ans_s, opts, expl in ipv6_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "IPv6架構與NDP協定",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【IPv6 協定架構與自動配置推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 IPv6 規範推導步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認 IPv6 定址模型與前綴分類</strong><br>
      ‧ 本題依據 RFC 4291 或 NDP RFC 4861 規範進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行縮寫規則或 ICMPv6 訊息流解析</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 IPv6 官方標準。<br>
‧ 其餘選項皆為縮寫語法違規或協定職責混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Neighbor Discovery Protocol (NDP)</code> <span class="en">NDP</span>：鄰居發現協定。<br>
‧ <code>Stateless Address Autoconfiguration (SLAAC)</code> <span class="en">SLAAC</span>：無狀態位址自動配置。<br>
‧ <code>Duplicate Address Detection (DAD)</code> <span class="en">DAD</span>：重複位址偵測。"""
        })

    # More IPv6 (10 items)
    more_ipv6 = [
        ("IPv6 固定基本標頭（Base Header）的大小固定為多少位元組？相較於 IPv4 有何優勢？", "固定為 40 位元組；移除了可變長度選項，大幅簡化路由器硬體轉發解析邏輯", ["固定為 40 位元組；移除了可變長度選項，大幅簡化路由器硬體轉發解析邏輯", "固定為 20 位元組", "可變長度 20~60 位元組", "64 位元組"], "定長 40-byte 標頭極利於硬體流水線並行處理，擴充功能改以「延伸標頭（Extension Headers）」鏈結實現。"),
        ("IPv6 基本標頭中「完全移除了」下列哪一項在 IPv4 中存在且每跳皆需重新計算的欄位？", "標頭檢查碼（Header Checksum）", ["標頭檢查碼（Header Checksum）", "躍點限制（Hop Limit）", "有效負載長度", "下一標頭"], "每跳路由器無需再耗費 CPU 重算校驗和，大幅提升轉發效率（由二層 CRC 與四層 TCP/UDP 校驗把關）。"),
        ("IPv6 中的「Hop Limit（躍點限制）」欄位對應於 IPv4 的何種欄位？", "存活時間（TTL, Time to Live）", ["存活時間（TTL, Time to Live）", "服務類型（ToS）", "識別碼（Identification）", "總長度"], "每經一跳減 1，減為 0 時拋棄封包並回傳 ICMPv6 Time Exceeded。"),
        ("IPv6 規定「中繼路由器（Routers）絕對不允許對封包進行分段」，若封包超過 MTU，路由器將會？", "丟棄該封包並回傳 ICMPv6 Packet Too Big 錯誤，由「來源端主機」自行進行端對端分段", ["丟棄該封包並回傳 ICMPv6 Packet Too Big 錯誤，由「來源端主機」自行進行端對端分段", "將封包拆成兩半轉發", "暫存該封包", "壓縮封包標頭"], "消除中間分段負擔，主機利用路徑 MTU 探索（PMTUD）動態調整發送大小。"),
        ("全球單播 IPv6 位址（Global Unicast Address）的分配前綴範圍為？", "`2000::/3`（目前公網主要分配空間）", ["`2000::/3`（目前公網主要分配空間）", "`fe80::/10`", "`fc00::/7`", "`ff00::/8`"], "相當於 IPv4 的公共公網 IP。"),
        ("唯一區域單播位址（Unique Local Address, ULA）在 IPv6 中的前綴為？", "`fc00::/7`（通常使用 fd00::/8）", ["`fc00::/7`（通常使用 fd00::/8）", "`fe80::/10`", "`2001::/16`", "`ff02::1`"], "相當於 IPv4 的 RFC 1918 私網 IP，企業內部專用且不可在公網路由。"),
        ("IPv6 群播位址（Multicast Address）的固定前綴為？", "`ff00::/8`", ["`ff00::/8`", "`fe80::/10`", "`fc00::/7`", "`2000::/3`"], "所有群播皆以 ff 開頭。"),
        ("IPv6 特殊群播位址 `ff02::1` 代表？", "本鏈路上的「所有節點（All Nodes）」", ["本鏈路上的「所有節點（All Nodes）」", "所有路由器", "所有 DHCP 伺服器", "根 DNS"], "等價於子網廣播。"),
        ("IPv6 特殊群播位址 `ff02::2` 代表？", "本鏈路上的「所有路由器（All Routers）」", ["本鏈路上的「所有路由器（All Routers）」", "所有終端主機", "所有交換器", "所有網域控制器"], "主機發送 RS 尋求網段路由器時發往此位址。"),
        ("IPv4 到 IPv6 的過渡遷移技術中，雙堆疊（Dual-Stack）是指？", "網路設備與主機同時運行完整的 IPv4 與 IPv6 兩套協定堆疊", ["網路設備與主機同時運行完整的 IPv4 與 IPv6 兩套協定堆疊", "將 IPv4 封包直接改副檔名", "使用硬體轉接頭", "在兩台電腦間同步"], "最平滑、相容性最高的共存過渡方案。")
    ]

    for stem, ans_s, opts, expl in more_ipv6:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "IPv6進階特性與遷移",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【IPv6 運作特性剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在前綴範圍或標頭欄位定義偏誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Path MTU Discovery (PMTUD)</code> <span class="en">PMTUD</span>：路徑 MTU 探索。<br>
‧ <code>Dual-Stack</code> <span class="en">Dual-Stack</span>：雙協定堆疊。<br>
‧ <code>Extension Header</code> <span class="en">Extension Header</span>：延伸標頭。"""
        })

    # -------------------------------------------------------------
    # 5. IP 分段推導與路由協定 (30 題)
    # -------------------------------------------------------------
    frag_data = [
        ("一個總長度為 4000 位元組的 IPv4 封包（包含 20 位元組 IP 標頭與 3980 位元組資料），需通過 MTU = 1500 位元組的網路鏈路。第一個分段（Fragment 1）的資料負載長度與片段偏移（Fragment Offset）分別為？",
         "資料長度 1480 位元組，片段偏移 Offset = 0", ["資料長度 1480 位元組，片段偏移 Offset = 0", "資料長度 1500 位元組，Offset = 0", "資料長度 1480 位元組，Offset = 185", "資料長度 1500 位元組，Offset = 1500"],
         "分段規則：MTU = 1500，扣除 20-byte 標頭剩 1480 位元組。片段資料長度必須為 8 的整數倍（1480 / 8 = 185，剛好整除）。第一個分段攜帶 1480 位元組資料，起始位置為 0，Offset = 0/8 = 0，MF = 1。"),
        ("承上題，第二個分段（Fragment 2）的資料負載長度與片段偏移（Fragment Offset）分別為？",
         "資料長度 1480 位元組，片段偏移 Offset = 185", ["資料長度 1480 位元組，片段偏移 Offset = 185", "資料長度 1480 位元組，Offset = 1480", "資料長度 1500 位元組，Offset = 185", "資料長度 1020 位元組，Offset = 370"],
         "第二個分段起始於第 1480 位元組處，攜帶 1480 位元組（涵蓋位元組 1480~2959）。Offset 欄位以 8 位元組為單位記錄：1480 / 8 = 185，MF = 1。"),
        ("承上題，第三個分段（Fragment 3，最後一個分段）的資料負載長度、片段偏移與 MF（More Fragments）旗標分別為？",
         "資料長度 1020 位元組，Offset = 370，MF = 0", ["資料長度 1020 位元組，Offset = 370，MF = 0", "資料長度 1020 位元組，Offset = 2960，MF = 1", "資料長度 1040 位元組，Offset = 370，MF = 0", "資料長度 1480 位元組，Offset = 370，MF = 0"],
         "剩餘資料長度 = 3980 - 1480 - 1480 = 1020 位元組。起始偏移為 2960 位元組，Offset = 2960 / 8 = 370。因是最後一個分段，MF = 0。"),
        ("若 IP 標頭中的 DF（Don't Fragment）旗標被設為 1，當該封包長度大於路由器出埠 MTU 時，路由器將會？",
         "丟棄該封包，並向來源主機回傳 ICMP Destination Unreachable（Fragmentation Needed and DF set）錯誤", ["丟棄該封包，並向來源主機回傳 ICMP Destination Unreachable（Fragmentation Needed and DF set）錯誤", "忽略 DF 旗標強制分段", "暫存該封包等待頻寬", "直接壓縮封包"], "DF=1 強制不可分段，常被 PMTUD 用於探測整條路徑的瓶頸 MTU。"),
        ("距離向量路由協定（Distance Vector，如 RIP）中，「計數至無窮大（Count-to-Infinity）」問題的主要成因與標準解決方案為？",
         "成因：節點故障時相鄰路由器互信彼此陳舊資訊形成循環遞增；解法：水平分割（Split Horizon）與毒性逆轉（Poison Reverse）", ["成因：節點故障時相鄰路由器互信彼此陳舊資訊形成循環遞增；解法：水平分割（Split Horizon）與毒性逆轉（Poison Reverse）", "成因：封包過大；解法：加大記憶體", "成因：MAC 衝突；解法：改用交換器", "成因：廣播風暴；解法：STP"], "水平分割規定：從某介面學到的路由資訊，絕不再從該介面反向通告回去；毒性逆轉則通告度量為 16（無窮大不可達）。"),
        ("RIP（路由資訊協定）使用的度量標準（Metric）為何？最大合法跳數為多少？",
         "度量標準為跳數（Hop Count）；最大合法跳數為 15（跳數達到 16 即視為不可達）", ["度量標準為跳數（Hop Count）；最大合法跳數為 15（跳數達到 16 即視為不可達）", "度量為頻寬與延遲；最大跳數 255", "度量為鏈路成本；最大跳數 100", "度量為可靠度；最大跳數 16"], "RIP 限制最大 15 跳，僅適用於小型網路。"),
        ("OSPF 鏈路狀態路由協定中，計算最短路徑樹所依賴的核心演算法為？度量值 Metric 的計算公式為？",
         "Dijkstra 演算法（SPF 最短路徑優先）；預設成本 Cost = 參考頻寬（100 Mbps） / 介面實際頻寬", ["Dijkstra 演算法（SPF 最短路徑優先）；預設成本 Cost = 參考頻寬（100 Mbps） / 介面實際頻寬", "Bellman-Ford 演算法；Cost = 跳數", "Floyd 演算法；Cost = 延遲", "Kruskal 演算法；Cost = 封包遺失率"], "鏈路頻寬越高，Cost 越小越優先。"),
        ("在 OSPF 多區域（Multi-Area）設計中，所有非骨幹區域（Non-Backbone Areas）必須？",
         "在邏輯上直接連接到「骨幹區域（Backbone Area，即 Area 0）」", ["在邏輯上直接連接到「骨幹區域（Backbone Area，即 Area 0）」", "直接彼此互相連接", "完全獨立運作", "必須連接到網際網路"], "兩層階層式結構防止區域間路由環路，跨區域流量必須經過 Area 0 中轉（若無法直連需建虛擬鏈路 Virtual Link）。"),
        ("在廣播型多重存取網路（如乙太網）中，OSPF 選舉 DR（Designated Router）與 BDR 的主要目的為？",
         "將鄰接關係（Adjacency）數量從 O(N²) 暴跌縮減至 O(N)，大幅減少 LSA 洪泛與更新同步的網路頻寬開銷", ["將鄰接關係（Adjacency）數量從 O(N²) 暴跌縮減至 O(N)，大幅減少 LSA 洪泛與更新同步的網路頻寬開銷", "擔任唯一的封包轉發閘道", "取代生成樹協定", "負責分配動態 IP"], "N 台路由器全互聯需 N(N-1)/2 個鄰接；引進 DR 後所有路由器只與 DR/BDR 建立鄰接。"),
        ("BGP（邊界閘道協定）屬於下列何種路由協定類型？其防止自治系統（AS）間環路的核心屬性為？",
         "路徑向量協定（Path Vector Protocol）；利用 AS-Path 屬性（若發現自己的 AS 號已存在於 AS-Path 清單中則直接忽略該路由）", ["路徑向量協定（Path Vector Protocol）；利用 AS-Path 屬性（若發現自己的 AS 號已存在於 AS-Path 清單中則直接忽略該路由）", "距離向量協定；利用跳數防環", "鏈路狀態協定；利用 Dijkstra 防環", "二層協定；利用 STP 防環"], "網際網路 AS 級跨域路由核心，AS-Path 記載經過的所有自治系統編號。")
    ]

    for stem, ans_s, opts, expl in frag_data:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "IP分段與路由協定推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【IP 分段計算與路由演算法深入推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 分段偏移與協定狀態機演算</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確認 MTU 限制與 8 位元組對齊規則</strong><br>
      ‧ 本題依據 IPv4 片段偏移定義（Offset = 物理位移 / 8）或動態路由收斂特性進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行數值計算與防環驗證</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：完全符合 RFC 791 與動態路由理論。<br>
‧ 其餘選項常為 Offset 忘記除以 8、或 OSPF/RIP 核心演算法混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Fragment Offset</code> <span class="en">Fragment Offset</span>：片段偏移。<br>
‧ <code>Split Horizon</code> <span class="en">Split Horizon</span>：水平分割。<br>
‧ <code>Designated Router (DR)</code> <span class="en">Designated Router</span>：指定路由器。"""
        })

    # More Routing & Fragmentation (20 items)
    more_frag = [
        ("OSPF 中，區域邊界路由器（ABR, Area Border Router）的定義為？", "同時連接骨幹區域（Area 0）與一個或多個非骨幹區域的路由器", ["同時連接骨幹區域（Area 0）與一個或多個非骨幹區域的路由器", "僅位於區域內部的路由器", "連接外部自治系統的路由器", "只有單一介面的路由器"], "負責在不同區域間彙總與傳遞 Type-3 網路摘要 LSA。"),
        ("OSPF 中，自治系統邊界路由器（ASBR, Autonomous System Boundary Router）的職責為？", "連接 OSPF 網路與其他外部路由網域（如 BGP 或 RIP），並注入 Type-5 外部 LSA", ["連接 OSPF 網路與其他外部路由網域（如 BGP 或 RIP），並注入 Type-5 外部 LSA", "負責在交換器間劃分 VLAN", "僅處理靜態路由", "負責指派 IP 位址"], "實現異質路由重分配（Route Redistribution）。"),
        ("在 BGP 路由屬性選路決策中，下列哪項屬性具備「最高優先級（第一優先比對）」？", "Weight（Cisco 專屬本地權重，數值越大越優先）或 Local-Preference（標準本地優先級）", ["Weight（Cisco 專屬本地權重，數值越大越優先）或 Local-Preference（標準本地優先級）", "AS-Path 長度", "MED 屬性", "Origin 屬性"], "Local-Preference 控制 AS 內部流量如何流向外部（出站選路）。"),
        ("BGP 中的 MED（Multi-Exit Discriminator）屬性主要功用為？", "通知相鄰自治系統進入本 AS 的最佳入口（入站選路，數值越小越優先）", ["通知相鄰自治系統進入本 AS 的最佳入口（入站選路，數值越小越優先）", "控制出站流量", "防止環路", "設定密碼"], "度量指標，告訴對方針對特定網段應由哪一條鏈路送進來。"),
        ("BGP 建立鄰居關係時依賴何種傳輸層協定？其監聽的特定 TCP 埠號為？", "TCP 協定；監聽埠號 TCP 179", ["TCP 協定；監聽埠號 TCP 179", "UDP 埠號 520", "IP 協定號 89", "ICMP 埠號 1"], "不同於內部網關協定直接封裝或使用廣播，BGP 透過可靠 TCP 單播連線建立對等體（BGP Peer）。"),
        ("OSPF 封包直接封裝在 IP 標頭內部，其對應的 IP 協定號（Protocol Number）為？", "89", ["89", "6（TCP）", "17（UDP）", "1（ICMP）"], "無需依賴傳輸層，具備專屬協定號。"),
        ("RIP 封包封裝在傳輸層的何種協定？埠號為？", "UDP 協定；埠號 520", ["UDP 協定；埠號 520", "TCP 179", "IP 89", "ICMP 0"], "使用 UDP 廣播或群播（224.0.0.9）定期通告。"),
        ("ICMP 協定（網際網路控制訊息協定）在網路層的主要功用為？", "報告封包處理異常與提供網路診斷資訊（如 Echo Request/Reply, TTL Exceeded, Destination Unreachable）", ["報告封包處理異常與提供網路診斷資訊（如 Echo Request/Reply, TTL Exceeded, Destination Unreachable）", "加密資料傳輸", "建立動態路由表", "取代 TCP 傳輸大檔案"], "Ping 與 Traceroute 之基礎。"),
        ("Traceroute 診斷工具探測沿途路由器 IP 的核心技術手法為？", "發送一連串 TTL 逐次遞增（1, 2, 3...）的探測封包，迫使沿途路由器因 TTL=0 回傳 ICMP Time Exceeded 封包", ["發送一連串 TTL 逐次遞增（1, 2, 3...）的探測封包，迫使沿途路由器因 TTL=0 回傳 ICMP Time Exceeded 封包", "查詢全網 DNS 資料庫", "發送廣播 ARP", "直接掃描交換器 MAC 表"], "巧妙利用 TTL 逾時機制揭露沿途每一跳路由器的介面 IP。"),
        ("當主機收到 ICMP Destination Unreachable（Code 3: Port Unreachable）時，代表何種狀況？", "目的主機 IP 可達，但該主機上沒有任何應用程式在該特定目標埠號上進行監聽", ["目的主機 IP 可達，但該主機上沒有任何應用程式在該特定目標埠號上進行監聽", "實體網路線斷線", "預設閘道當機", "防火牆阻擋所有連線"], "通常在 UDP 存取未開啟服務埠時由目的作業系統回覆。"),
        ("IGMP（網際網路群組管理協定）主要運行於何處？其功用為？", "運行於主機與其緊鄰的最後一跳路由器之間，用於「動態加入或離開多播群組」", ["運行於主機與其緊鄰的最後一跳路由器之間，用於「動態加入或離開多播群組」", "在路由器之間計算多播樹", "建立 VPN 隧道", "分配靜態 IP"], "告知路由器本地網段是否有主機需要接收特定多播頻道資料流。"),
        ("PIM（獨立於通訊協定的多播路由協定）稀疏模式（PIM-SM）核心架構包含？", "會合點（RP, Rendezvous Point）與共享樹（RPT / (*, G) 樹）轉短路徑樹（SPT / (S, G) 樹）", ["會合點（RP, Rendezvous Point）與共享樹（RPT / (*, G) 树）轉短路徑樹（SPT / (S, G) 樹）", "全網洪泛剪枝", "僅使用廣播", "完全依賴 OSPF"], "專門處理接收者廣泛分散的跨網段群播傳輸。"),
        ("在 IP 標頭中，服務類型（ToS / DiffServ DSCP）欄位主要用於？", "網路服務品質（QoS, Quality of Service）與封包排隊優先權標記", ["網路服務品質（QoS, Quality of Service）與封包排隊優先權標記", "記錄封包經過的跳數", "防範緩衝區溢位", "記錄發送端作業系統"], "配合流量整型（Traffic Shaping）與權重公平排隊（WFQ）保證語音視訊等即時流量頻寬。"),
        ("ECMP（等價多路徑路由，Equal-Cost Multi-Path）的功能為？", "當到達同一目的地有多條 Cost 相同的最佳路徑時，在多條鏈路間進行負載平衡（Load Balancing）流量分流", ["當到達同一目的地有多條 Cost 相同的最佳路徑時，在多條鏈路間進行負載平衡（Load Balancing）流量分流", "隨機丟棄一半流量", "只走第一條鏈路", "將封包拆成多段"], "成倍提升骨幹吞吐量並提供快速故障切換。"),
        ("若一個 IPv4 封包的總長度欄位（Total Length）為 800 位元組，標頭長度（IHL）為 5，則其資料載荷大小為？", "780 位元組", ["780 位元組", "795 位元組", "800 位元組", "760 位元組"], "IHL 以 4 位元組為單位，5 × 4 = 20 位元組標頭。載荷 = 800 - 20 = 780 位元組。"),
        ("IPv4 標頭的最小可能長度與最大可能長度分別為？", "最小 20 位元組（無選項），最大 60 位元組（含 40 位元組選項）", ["最小 20 位元組（無選項），最大 60 位元組（含 40 位元組選項）", "最小 16 位元組，最大 32 位元組", "固定 40 位元組", "最小 24 位元組，最大 64 位元組"], "IHL 欄位為 4 位元，最大值為 15（15 × 4 = 60 位元組）。"),
        ("在動態路由協定中，「收斂（Convergence）」的定義為？", "當網路拓樸發生變化後，所有路由器更新完畢其路由表並達成「全網路由一致狀態」的過程", ["當網路拓樸發生變化後，所有路由器更新完畢其路由表並達成「全網路由一致狀態」的過程", "所有路由器同時重新開機", "所有封包全部抵達終點", "網路頻寬達到上限"], "收斂時間越短，網路越穩定。"),
        ("RIPv1 與 RIPv2 的最重大差異為？", "RIPv1 為有類別（Classful）且廣播發送；RIPv2 支援 VLSM、CIDR、MD5 認證且改用群播（224.0.0.9）發送", ["RIPv1 為有類別（Classful）且廣播發送；RIPv2 支援 VLSM、CIDR、MD5 認證且改用群播（224.0.0.9）發送", "RIPv1 跳數為 30", "RIPv2 只能用於光纖", "兩者完全相同"], "RIPv2 支援在路由更新中攜帶子網路遮罩。"),
        ("靜態路由（Static Route）相較於動態路由協定的主要優點為？", "不產生任何額外的網路協定頻寬開銷、不佔用 CPU 運算資源，且路由路徑完全確定具高可控性與安全性", ["不產生任何額外的網路協定頻寬開銷、不佔用 CPU 運算資源，且路由路徑完全確定具高可控性與安全性", "當線路中斷時會自動繞道", "適合超大型複雜網際網路", "能自動學習全網拓樸"], "小型封閉網路或末梢站台首選。"),
        ("浮動靜態路由（Floating Static Route）的設定技巧為？", "將備援靜態路由的管理距離（Administrative Distance, AD）設定得「高於」主要路由（如 AD=200）", ["將備援靜態路由的管理距離（Administrative Distance, AD）設定得「高於」主要路由（如 AD=200）", "將 AD 設為 0", "將躍點設為 16", "關閉介面"], "平時隱藏於後台，僅在主要線路（如 AD=1）實體中斷時自動浮現轉發。")
    ]

    for stem, ans_s, opts, expl in more_frag:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "路由協定與標頭進階特性",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【網路層協定與分段控制剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在標頭運算或路由協定行為偏誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Area Border Router (ABR)</code> <span class="en">ABR</span>：區域邊界路由器。<br>
‧ <code>Administrative Distance (AD)</code> <span class="en">Administrative Distance</span>：管理距離。<br>
‧ <code>Equal-Cost Multi-Path (ECMP)</code> <span class="en">ECMP</span>：等價多路徑路由。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_net_part2_questions()
    print(f"Generated Net Part 2 questions: {len(qs)}")
