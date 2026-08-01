# -*- coding: utf-8 -*-
"""路線 2：網路基礎（CompTIA Network+ N10-009 + Cisco CCNA 200-301）"""

CH = []

CH.append({
    "id": "n01",
    "title": "OSI 七層與 TCP/IP：資料是怎麼跑到對面的",
    "subtitle": "分層模型、封裝、每層的攻擊與防禦",
    "level": "入門",
    "minutes": 22,
    "summary": "把網路拆成七層，每層只管自己的事。學會分層，你才能判斷一個問題該去哪一層查。",
    "why": "寄一個包裹到日本：你寫信（內容）→ 裝進紙箱（打包）→ 貼地址標籤（定位）→ "
           "交給貨運（運送）→ 上飛機（實體移動）。**每一關只看自己需要的那張標籤**，"
           "飛機駕駛不用知道箱子裡寫什麼。網路完全一樣。",
    "sections": [
        {
            "heading": "七層各自在做什麼",
            "body": "從上往下（**應用層在上，實體層在下**）：\n\n"
                    "- **L7 應用層**：使用者看到的東西。HTTP、DNS、SMTP、SSH。\n"
                    "- **L6 表達層**：格式轉換、加密、壓縮。TLS 常被歸在這裡。\n"
                    "- **L5 會談層**：建立與維持連線階段。\n"
                    "- **L4 傳輸層**：**TCP / UDP，用 port 號區分服務**。負責可靠傳輸與分段。\n"
                    "- **L3 網路層**：**IP 位址、路由**。決定跨網段怎麼走。路由器在這層。\n"
                    "- **L2 資料連結層**：**MAC 位址、交換器、VLAN、ARP**。負責同一網段內的傳遞。\n"
                    "- **L1 實體層**：電線、光纖、Wi-Fi 電波、接頭。\n\n"
                    "背誦口訣（由下到上）：**實體、連結、網路、傳輸、會談、表達、應用**。",
            "example": "**除錯時的分層思考法**（實務最有價值的技能）：\n"
                       "「網站打不開」→ 從下往上問：\n"
                       "1. L1 網路線插了嗎？燈亮嗎？\n"
                       "2. L2 `ip a` 有拿到介面 UP 嗎？\n"
                       "3. L3 `ping 8.8.8.8` 通嗎？\n"
                       "4. DNS `ping google.com` 通嗎？（不通但上一步通 → DNS 問題）\n"
                       "5. L4 `curl -v https://site` port 443 開嗎？\n"
                       "6. L7 是網站本身的錯誤嗎？\n"
                       "**這個流程可以解掉八成的網路問題。**",
            "note": "考點：OSI 是七層（理論模型），TCP/IP 是四層（實際實作）："
                    "應用層、傳輸層、網際網路層、網路存取層。考試兩種都會問。",
        },
        {
            "heading": "封裝：每一層都加一個標籤",
            "body": "資料往下走時，每一層都加上自己的表頭，這叫**封裝**：\n\n"
                    "```\n"
                    "L7 資料         [ HTTP 內容 ]\n"
                    "L4 加 TCP 表頭  [TCP][ HTTP 內容 ]      → Segment\n"
                    "L3 加 IP 表頭   [IP][TCP][ 內容 ]       → Packet\n"
                    "L2 加 MAC 表頭  [MAC][IP][TCP][ 內容 ]  → Frame\n"
                    "L1 電子訊號     0101010101...           → Bits\n"
                    "```\n\n"
                    "接收端反過來一層層拆掉，叫**解封裝**。\n\n"
                    "**重點差異**：\n"
                    "- **IP 位址（L3）從頭到尾不會變** — 它是最終目的地。\n"
                    "- **MAC 位址（L2）每經過一個路由器就換一次** — 它只是「下一站」。",
            "example": "你在台北連美國網站：\n"
                       "- 目的 IP：整趟都是 `93.184.216.34`\n"
                       "- 目的 MAC：第一段是你家路由器的 MAC，"
                       "轉出去後改成電信商路由器的 MAC，一路換到最後一台才是伺服器 MAC。\n\n"
                       "**這解釋了一件重要的事**：MAC 位址無法跨網段追蹤，"
                       "所以攻擊者的 MAC 只在同一個 VLAN 內有意義。",
            "note": "MTU 預設 1500 bytes，超過要分片。攻擊者曾用刻意分片規避舊式 IDS — 這是考點。",
        },
        {
            "heading": "TCP 與 UDP：可靠但慢，還是快但不管",
            "body": "**TCP** — 打電話：先建立連線（三向交握）、有序號與確認、丟包重傳、"
                    "有流量控制。用於 HTTP/HTTPS、SSH、郵件、檔案傳輸。\n\n"
                    "**UDP** — 丟明信片：不建立連線、不保證到達與順序、不重傳、"
                    "表頭小（8 vs 20 bytes）。用於 DNS、DHCP、視訊、遊戲、SNMP、syslog。\n\n"
                    "**TCP 三向交握**：\n"
                    "1. 客戶端 → 伺服器：**SYN**（我想連）\n"
                    "2. 伺服器 → 客戶端：**SYN-ACK**（可以）\n"
                    "3. 客戶端 → 伺服器：**ACK**（成交）\n\n"
                    "結束用 FIN-ACK 四次交握，或用 **RST** 強制中斷。",
            "example": "**三向交握是理解掃描技術的關鍵**：\n"
                       "- **完整連線掃描**：走完三步，對方日誌留完整紀錄 → 容易被發現。\n"
                       "- **半開放掃描 (`nmap -sS`)**：送 SYN，收到 SYN-ACK 就知道 port 開了，"
                       "然後送 RST 斷掉，**不完成第三步**。\n"
                       "- 回 **RST** → port 關閉；**完全沒回應** → 很可能被防火牆丟棄。\n\n"
                       "**防守方的意義**：防火牆若對關閉 port 回 RST，攻擊者能區分"
                       "「關閉」與「被擋」；設成 DROP 不回應，掃描會變得非常慢。",
            "note": "SYN Flood：只送 SYN 不回 ACK，塞爆伺服器的半開連線表。對策是 SYN Cookie。",
        },
        {
            "heading": "每一層的典型攻擊與防禦",
            "body": "**攻擊者選哪一層下手，決定你要用哪一層的工具去防。**\n\n"
                    "在 L2 發生的 ARP 欺騙，用 L7 的 WAF 完全防不到；"
                    "L7 的 SQL Injection，L3 的防火牆也完全看不見（因為 443 是合法開放的）。\n\n"
                    "這就是為什麼「我有買防火牆」不代表安全 — 防火牆只看 L3/L4。"
                    "請看下面的對照表，這是你之後學 CEH 與 CND 的骨架。",
            "example": "**實例對照**：\n"
                       "- 咖啡廳假 Wi-Fi 竊聽 → L1/L2 攻擊 → 用 L6 的 TLS 讓竊聽者只看到亂碼。\n"
                       "- SQL Injection → L7 攻擊 → 必須用 WAF 或修程式碼，防火牆無效。\n"
                       "- ARP 欺騙 → L2 攻擊 → 只能在交換器上用 DAI 解決。",
            "note": "考點：DDoS 分「容量型」(L3/L4，塞頻寬) 與「應用型」(L7，用合法請求耗盡後端)。"
                    "兩者緩解方式完全不同。",
        },
    ],
    "table": {
        "caption": "OSI 各層的典型攻擊與對應防禦",
        "head": ["層", "單位／識別", "典型攻擊", "主要防禦"],
        "rows": [
            ["L7 應用", "HTTP/DNS/SMTP", "SQL Injection、XSS、釣魚、L7 DDoS", "WAF、安全開發、郵件閘道"],
            ["L6 表達", "TLS、編碼", "SSL 剝離、弱加密套件、憑證偽造", "強制 HTTPS、HSTS、憑證釘選"],
            ["L5 會談", "Session", "Session 劫持、Cookie 竊取", "HttpOnly/Secure Cookie"],
            ["L4 傳輸", "TCP/UDP port", "Port 掃描、SYN Flood、UDP 放大", "防火牆、SYN Cookie、速率限制"],
            ["L3 網路", "IP 位址", "IP 偽造、ICMP 濫用、路由劫持", "ACL、uRPF、RPKI"],
            ["L2 連結", "MAC / VLAN", "ARP 欺騙、MAC 洪泛、VLAN 跳躍", "DAI、Port Security、關閉 DTP"],
            ["L1 實體", "電子訊號", "剪線、竊聽、假 Wi-Fi AP", "機房門禁、802.1X、無線入侵偵測"],
        ],
    },
    "labs": [{
        "title": "親眼看到分層：從 MAC 到 HTTP",
        "goal": "用一組指令走完 L2→L7，建立分層除錯的肌肉記憶。",
        "warn": "全部是唯讀查詢。tcpdump 需要 sudo，只在自己的機器上執行。",
        "steps": [
            {"cmd": "ip -brief addr",
             "explain": "L2/L3：看介面狀態與 IP。UP 代表實體層通、有 IP 代表 L3 設定好了。",
             "output": "lo               UNKNOWN        127.0.0.1/8 ::1/128\neth0             UP             192.168.1.42/24 fe80::a00:27ff:fe4e:66a1/64"},
            {"cmd": "ip neigh",
             "explain": "L2：ARP 表。如果同一個 MAC 對到很多 IP，可能是 ARP 欺騙。",
             "output": "192.168.1.1 dev eth0 lladdr 3c:37:86:1f:2a:b0 REACHABLE\n192.168.1.77 dev eth0 lladdr 08:00:27:4e:66:a2 STALE"},
            {"cmd": "ip route",
             "explain": "L3：路由表。default via 就是預設閘道，出去外網都走它。",
             "output": "default via 192.168.1.1 dev eth0 proto dhcp metric 100\n192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.42"},
            {"cmd": "traceroute -n 8.8.8.8",
             "explain": "L3：看封包經過哪幾台路由器。每跳 MAC 都不同，但目的 IP 始終不變。",
             "output": " 1  192.168.1.1     1.204 ms  1.132 ms\n 2  10.12.0.1       8.441 ms  8.220 ms\n 3  168.95.98.254   9.017 ms  9.113 ms\n 4  72.14.215.85   14.882 ms 14.771 ms\n 5  8.8.8.8        15.402 ms 15.311 ms"},
            {"cmd": "curl -sI https://example.com",
             "explain": "L7：只取 HTTP 表頭。注意有沒有洩漏版本號。",
             "output": "HTTP/2 200\ncontent-type: text/html; charset=UTF-8\nserver: ECAcc (dab/4BB7)\nstrict-transport-security: max-age=31536000\ncache-control: max-age=604800"},
            {"cmd": "sudo tcpdump -i eth0 -c 5 -nn 'tcp[tcpflags] & tcp-syn != 0'",
             "explain": "L4：只抓帶 SYN 的封包。大量來自同一 IP 對不同 port 的 SYN = 正在被掃描。",
             "output": "listening on eth0, link-type EN10MB (Ethernet)\n10:22:31.441 IP 192.168.1.42.51422 > 93.184.216.34.443: Flags [S], seq 1849302\n10:22:31.462 IP 93.184.216.34.443 > 192.168.1.42.51422: Flags [S.], seq 88213, ack 1849303\n10:22:33.118 IP 203.0.113.9.44120 > 192.168.1.42.22: Flags [S], seq 771201, win 1024\n10:22:33.119 IP 203.0.113.9.44121 > 192.168.1.42.23: Flags [S], seq 771202, win 1024\n10:22:33.120 IP 203.0.113.9.44122 > 192.168.1.42.445: Flags [S], seq 771203, win 1024\n5 packets captured\n# 後三筆同一來源掃不同 port = 典型 SYN 掃描"},
        ],
    }],
    "quiz": [
        {"q": "交換器 (Switch) 主要工作在 OSI 的哪一層？",
         "options": ["L1 實體層", "L2 資料連結層", "L3 網路層", "L4 傳輸層"],
         "answer": 1,
         "why": "傳統交換器依 MAC 位址轉送 → L2。L3 交換器才會做 IP 路由。"},
        {"q": "封包從台北傳到美國，下列哪個敘述正確？",
         "options": ["IP 和 MAC 都不會變", "IP 會變，MAC 不變",
                     "IP 不變，MAC 每經過一台路由器就改變", "兩者每一跳都改變"],
         "answer": 2,
         "why": "IP 是最終目的地全程不變；MAC 只代表下一站，每經過 L3 裝置就重寫。"},
        {"q": "nmap -sS（SYN 掃描）為什麼稱為「半開放」掃描？",
         "options": ["只掃一半的 port", "送 SYN 收到 SYN-ACK 後直接送 RST，不完成三向交握",
                     "只使用 UDP", "只掃一半的主機"],
         "answer": 1,
         "why": "不走完第三步 ACK，舊系統的應用層日誌不會記錄這次連線。現代 EDR/IDS 仍能偵測。"},
        {"q": "掃描某 port 完全沒有收到回應，最可能代表什麼？",
         "options": ["port 開啟", "port 關閉", "被防火牆靜默丟棄 (filtered)", "主機不存在"],
         "answer": 2,
         "why": "開啟回 SYN-ACK、關閉回 RST、沒回應通常是防火牆 DROP。"},
        {"q": "DNS 主要使用哪個傳輸層協定與 port？",
         "options": ["TCP 53", "UDP 53（大型回應或區域傳送時改用 TCP 53）", "UDP 67", "TCP 853 only"],
         "answer": 1,
         "why": "查詢通常用 UDP 53；回應過大或 zone transfer 時改用 TCP 53。"},
        {"q": "SQL Injection 屬於哪一層，為什麼一般 L3/L4 防火牆擋不到？",
         "options": ["L2；封包太小", "L7；它藏在合法開放的 443 流量裡，防火牆只看 IP 與 port",
                     "L4；用了特殊 port", "L1；需要物理接觸"],
         "answer": 1,
         "why": "L7 應用層攻擊。防火牆看到的是合法 HTTPS 連線，必須用 WAF 或修程式碼。"},
        {"q": "攻擊者刻意把封包切成很多小片段，目的是什麼？",
         "options": ["加快傳輸", "規避只檢查單一封包的舊式 IDS 偵測", "降低頻寬", "繞過加密"],
         "answer": 1,
         "why": "分片規避。對策是要求 IDS/防火牆先做封包重組再檢查。"},
    ],
    "keywords": ["OSI", "TCP/IP", "封裝", "TCP", "UDP", "三向交握", "SYN", "MTU",
                 "traceroute", "tcpdump", "分層除錯"],
    "takeaway": [
        "IP 位址全程不變、MAC 位址每跳都換 — 這解釋了為什麼 L2 攻擊只在同網段有效。",
        "TCP 三向交握是理解所有掃描技術的基礎。",
        "除錯與防禦都要先問「這是第幾層的問題」，用對層的工具。",
    ],
})

CH[0]["diagram"] = """<svg viewBox="0 0 660 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="OSI 七層與封裝過程">
<text x="330" y="24" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">封裝：往下走，每層加一個表頭</text>
<g font-size="12">
<rect x="40" y="44" width="580" height="42" rx="6" fill="#0f2233" stroke="#2dd4bf"/><text x="56" y="70" fill="#5eead4">L7 應用</text><text x="150" y="70" fill="#94a3b8">HTTP / DNS / SSH</text><rect x="420" y="54" width="180" height="22" rx="4" fill="#134e4a"/><text x="510" y="70" text-anchor="middle" fill="#ccfbf1" font-size="11">資料 Data</text>
<rect x="40" y="94" width="580" height="42" rx="6" fill="#0f2233" stroke="#2dd4bf"/><text x="56" y="120" fill="#5eead4">L4 傳輸</text><text x="150" y="120" fill="#94a3b8">TCP / UDP + port</text><rect x="380" y="104" width="40" height="22" rx="4" fill="#0369a1"/><text x="400" y="120" text-anchor="middle" fill="#e0f2fe" font-size="10">TCP</text><rect x="420" y="104" width="180" height="22" rx="4" fill="#134e4a"/><text x="510" y="120" text-anchor="middle" fill="#ccfbf1" font-size="11">Segment</text>
<rect x="40" y="144" width="580" height="42" rx="6" fill="#0f2233" stroke="#2dd4bf"/><text x="56" y="170" fill="#5eead4">L3 網路</text><text x="150" y="170" fill="#94a3b8">IP 位址 / 路由</text><rect x="340" y="154" width="40" height="22" rx="4" fill="#7c3aed"/><text x="360" y="170" text-anchor="middle" fill="#ede9fe" font-size="10">IP</text><rect x="380" y="154" width="40" height="22" rx="4" fill="#0369a1"/><text x="400" y="170" text-anchor="middle" fill="#e0f2fe" font-size="10">TCP</text><rect x="420" y="154" width="180" height="22" rx="4" fill="#134e4a"/><text x="510" y="170" text-anchor="middle" fill="#ccfbf1" font-size="11">Packet</text>
<rect x="40" y="194" width="580" height="42" rx="6" fill="#0f2233" stroke="#2dd4bf"/><text x="56" y="220" fill="#5eead4">L2 連結</text><text x="150" y="220" fill="#94a3b8">MAC / VLAN / ARP</text><rect x="300" y="204" width="40" height="22" rx="4" fill="#b45309"/><text x="320" y="220" text-anchor="middle" fill="#fef3c7" font-size="10">MAC</text><rect x="340" y="204" width="40" height="22" rx="4" fill="#7c3aed"/><text x="360" y="220" text-anchor="middle" fill="#ede9fe" font-size="10">IP</text><rect x="380" y="204" width="40" height="22" rx="4" fill="#0369a1"/><text x="400" y="220" text-anchor="middle" fill="#e0f2fe" font-size="10">TCP</text><rect x="420" y="204" width="180" height="22" rx="4" fill="#134e4a"/><text x="510" y="220" text-anchor="middle" fill="#ccfbf1" font-size="11">Frame</text>
<rect x="40" y="244" width="580" height="42" rx="6" fill="#0f2233" stroke="#2dd4bf"/><text x="56" y="270" fill="#5eead4">L1 實體</text><text x="150" y="270" fill="#94a3b8">電線 / 光纖 / 電波</text><text x="510" y="270" text-anchor="middle" fill="#ccfbf1" font-size="11">1011010010110...</text>
</g>
<text x="330" y="316" text-anchor="middle" fill="#f59e0b" font-size="13" font-weight="700">IP 全程不變（最終目的）· MAC 每過一台路由器就換（下一站）</text>
<text x="330" y="348" text-anchor="middle" fill="#94a3b8" font-size="12">除錯口訣：由下往上 — 線 → 介面 → ping IP → ping 網域 → 查 port → 看應用</text>
<text x="330" y="378" text-anchor="middle" fill="#64748b" font-size="12">OSI 七層是理論模型；TCP/IP 四層是實際實作</text>
</svg>"""

CH.append({
    "id": "n02",
    "title": "IP 位址與子網切割：用除法就能算",
    "subtitle": "IPv4、CIDR、子網、私有網段、NAT、IPv6",
    "level": "入門",
    "minutes": 26,
    "summary": "子網切割是網路分段的基礎，而網路分段是限制攻擊擴散最有效的手段。不會算子網，就無法設計防禦。",
    "why": "把 IP 想成地址：`192.168.1.42` 前面是**社區名稱**、後面是**門牌號碼**。"
           "子網遮罩就是在告訴你「這條線畫在哪」。**同一個社區的人可以直接互相走動；"
           "不同社區要走大門（閘道）** — 資安的工作就是決定「哪些社區可以互通」。",
    "sections": [
        {
            "heading": "IPv4 與子網遮罩的本質",
            "body": "IPv4 是 **32 個位元**，寫成四段十進位，每段 0–255。\n\n"
                    "`192.168.1.42` 換成二進位：\n"
                    "`11000000.10101000.00000001.00101010`\n\n"
                    "**子網遮罩**告訴你「前面幾個 bit 是網路部分」：\n"
                    "- `/24` → 遮罩 `255.255.255.0`\n"
                    "- `/16` → 遮罩 `255.255.0.0`\n"
                    "- `/25` → 遮罩 `255.255.255.128`\n\n"
                    "剩下的 bit 是**主機部分**：\n\n"
                    "**可用主機數 = 2^(32 − 前綴長度) − 2**\n\n"
                    "為什麼減 2？第一個位址是**網路位址**、最後一個是**廣播位址**，"
                    "這兩個不能給主機用。",
            "example": "`/24` → 254 台　`/25` → 126 台　`/26` → 62 台\n"
                       "`/27` → 30 台　`/28` → 14 台　`/29` → 6 台\n"
                       "`/30` → 2 台（路由器對接）　`/32` → 單一主機（防火牆規則最常用）\n\n"
                       "**把這張表背下來，考試和實務都夠用了。**",
            "note": "口訣：**前綴每加 1，主機數砍半**。/24 是 254，/25 是 126，/26 是 62……",
        },
        {
            "heading": "三十秒算出網段範圍（考試實用解法）",
            "body": "不用轉二進位，用**區塊大小 (Block Size)** 法：\n\n"
                    "1. **區塊大小 = 256 − 遮罩的最後一個非零數字**\n"
                    "2. 從 0 開始，以區塊大小為間隔往上跳，找出目標 IP 落在哪一格\n"
                    "3. 那一格的第一個數字 = 網路位址\n"
                    "4. 下一格第一個數字 − 1 = 廣播位址\n"
                    "5. 中間全部是可用主機\n\n"
                    "**實例：`192.168.1.100/26` 屬於哪個網段？**\n"
                    "- /26 → 遮罩 `255.255.255.192` → 區塊 = 256 − 192 = **64**\n"
                    "- 網段起點：0, 64, 128, 192\n"
                    "- 100 落在 64–127\n"
                    "- **網路 = 192.168.1.64、廣播 = 192.168.1.127**\n"
                    "- **可用 = .65 ~ .126（62 台）**",
            "example": "**再練一題：`10.20.30.200/27`**\n"
                       "- /27 → 遮罩 `255.255.255.224` → 區塊 = 32\n"
                       "- 起點：0, 32, 64, 96, 128, 160, **192**, 224\n"
                       "- 200 落在 192–223\n"
                       "- 網路 = `10.20.30.192`，廣播 = `10.20.30.223`，可用 30 台\n\n"
                       "**資安用途**：在防火牆寫 `deny 10.20.30.192/27` 時，"
                       "你必須確定這 30 個位址剛好是要擋的那個部門 — "
                       "算錯就會擋到別人或漏掉目標。",
            "note": "常見遮罩對應區塊：/25→128、/26→64、/27→32、/28→16、/29→8、/30→4。"
                    "記熟這六個，子網題就變成心算。",
        },
        {
            "heading": "私有位址、NAT 與特殊網段",
            "body": "**私有位址 (RFC 1918)** — 不能在網際網路上路由：\n"
                    "- `10.0.0.0/8` — 大型企業\n"
                    "- `172.16.0.0/12`（172.16 ~ 172.31）— 中型\n"
                    "- `192.168.0.0/16` — 家用與小型辦公室\n\n"
                    "**其他必知網段**：\n"
                    "- `127.0.0.0/8` — 本機迴路\n"
                    "- `169.254.0.0/16` — **APIPA**：拿不到 DHCP 時自動給的位址。"
                    "**看到這個 IP 等於 DHCP 掛了。**\n"
                    "- `224.0.0.0/4` — 群播\n"
                    "- `100.64.0.0/10` — 電信商級 NAT (CGNAT)\n\n"
                    "**NAT**：路由器把內部私有 IP 換成公有 IP 出去。\n"
                    "- 好處：省 IP、外部無法直接連入（**副作用是一層天然防護**）\n"
                    "- **但 NAT 不是防火牆** — 它沒有政策、不檢查內容，"
                    "對「內部主動連出去」的惡意流量完全不管。",
            "example": "**排錯實例**：使用者說網路不通，你 `ip a` 看到 `169.254.13.88`。\n"
                       "→ 立刻知道 **DHCP 沒拿到 IP**。\n"
                       "可能原因：線鬆脫、交換器 port 被關、DHCP 服務故障、"
                       "位址池用完、或 **802.1X 認證失敗**（資安相關）。\n\n"
                       "反過來說：如果一台不該存在的裝置拿到了內網 IP，"
                       "代表你的 802.1X / NAC 沒有生效。",
            "note": "面試常問「NAT 算不算安全機制」— 標準答案是"
                    "「提供一定程度的隱匿性，但不做政策檢查，不能取代防火牆」。",
        },
        {
            "heading": "為什麼子網切割是資安措施",
            "body": "**這一節是本章重點 — 子網不只是網路課，它是防禦設計。**\n\n"
                    "假設全公司都在同一個 `10.0.0.0/16`（六萬多台在同一廣播域）：\n"
                    "- 任何一台被入侵，攻擊者可直接掃到全部主機\n"
                    "- ARP 欺騙可攔截任何人的流量\n"
                    "- 勒索病毒可在一小時內加密全公司\n\n"
                    "**正確做法：依信任等級與功能分段**\n"
                    "- `10.10.10.0/24` 一般員工辦公\n"
                    "- `10.10.20.0/24` 財務部（限制存取）\n"
                    "- `10.10.30.0/24` 伺服器區\n"
                    "- `10.10.40.0/24` 訪客 Wi-Fi（**只能上網，不能碰內網**）\n"
                    "- `10.10.50.0/24` 監視器與 IoT（**永遠不會更新，必須隔離**）\n"
                    "- `10.10.60.0/24` OT／生產線設備（最高隔離）\n"
                    "- `10.10.99.0/24` 管理網段（只有跳板機能進）\n\n"
                    "然後段與段之間用防火牆或 ACL 只放行必要流量。"
                    "**這一個動作對限制勒索病毒擴散的效果，勝過大多數昂貴產品。**",
            "example": "真實事故的典型樣態：某工廠產線 PLC 和辦公網路同網段。"
                       "會計中釣魚信 → 勒索病毒橫向掃描 → 加密到產線控制電腦 → **停產三天**。\n\n"
                       "如果 OT 網段有隔離（只允許特定 IP 的特定 port 單向通過），"
                       "損失會停在會計那台電腦。\n\n"
                       "**這就是 IEC 62443 / Purdue 模型要求 IT 與 OT 之間必須有 DMZ 的原因。**",
            "note": "進階：**微分段** 把粒度縮到單一工作負載，"
                    "同網段的兩台伺服器也不能互通，除非明確允許。這是零信任在網路層的實作。",
        },
        {
            "heading": "IPv6 快速入門（考試會考，別跳過）",
            "body": "IPv6 是 **128 bit**，寫成八組四位十六進位：\n"
                    "`2001:0db8:0000:0000:0000:ff00:0042:8329`\n\n"
                    "**簡寫兩規則**：\n"
                    "1. 每組開頭的 0 可省略\n"
                    "2. **連續全為 0 的組可用 `::` 取代，但只能用一次**\n"
                    "→ `2001:db8::ff00:42:8329`\n\n"
                    "**必知位址類型**：\n"
                    "- `::1/128` — 本機迴路\n"
                    "- `fe80::/10` — **鏈路本地**，同網段自動產生，不可路由\n"
                    "- `fc00::/7` — 唯一本地位址 ULA（類似私有 IP）\n"
                    "- `2000::/3` — 全球單播\n\n"
                    "**IPv6 沒有廣播**（改用群播），通常也不需要 NAT。\n\n"
                    "**資安重點**：很多公司防火牆只設了 IPv4 規則，"
                    "但作業系統預設啟用 IPv6 → **形成一條沒人管的旁路**。",
            "example": "**實務陷阱**：管理員在 iptables 仔細擋掉所有進入連線，"
                       "但忘了 `ip6tables` → 攻擊者用 IPv6 直接連進來，規則形同虛設。\n\n"
                       "另一個陷阱：內網用 SLAAC 自動配置時，"
                       "攻擊者可偽造 **Router Advertisement** 讓自己變成預設閘道做中間人 —"
                       "對策是交換器啟用 **RA Guard**。",
            "note": "考點：IPv4 用 ARP，IPv6 改用 **NDP（鄰居發現協定）**。"
                    "所以 ARP 欺騙在 IPv6 對應 NDP 欺騙，防禦叫 ND Inspection。",
        },
    ],
    "table": {
        "caption": "常用子網對照表（背這張就夠）",
        "head": ["CIDR", "子網遮罩", "區塊大小", "可用主機數", "常見用途"],
        "rows": [
            ["/24", "255.255.255.0", "256", "254", "標準辦公網段、單一 VLAN"],
            ["/25", "255.255.255.128", "128", "126", "把 /24 切兩半"],
            ["/26", "255.255.255.192", "64", "62", "中型部門"],
            ["/27", "255.255.255.224", "32", "30", "小部門、伺服器群"],
            ["/28", "255.255.255.240", "16", "14", "DMZ、少量伺服器"],
            ["/29", "255.255.255.248", "8", "6", "小型 DMZ、防火牆對接"],
            ["/30", "255.255.255.252", "4", "2", "路由器間點對點連線"],
            ["/32", "255.255.255.255", "1", "1", "防火牆規則中的單一主機"],
        ],
    },
    "labs": [{
        "title": "用 ipcalc 驗算子網，並確認自己的網段",
        "goal": "手算完之後用工具驗證，建立信心。",
        "warn": "唯讀操作。ipcalc 可用 `sudo apt install ipcalc` 安裝。",
        "steps": [
            {"cmd": "ipcalc 192.168.1.100/26",
             "explain": "驗算前面手算的結果。注意 HostMin / HostMax / Broadcast 三行。",
             "output": "Address:   192.168.1.100\nNetmask:   255.255.255.192 = 26\nWildcard:  0.0.0.63\n=>\nNetwork:   192.168.1.64/26\nHostMin:   192.168.1.65\nHostMax:   192.168.1.126\nBroadcast: 192.168.1.127\nHosts/Net: 62                    Class C, Private Internet"},
            {"cmd": "ipcalc 10.20.30.200/27",
             "explain": "第二題驗算。手算得到 192–223，看工具是否一致。",
             "output": "Network:   10.20.30.192/27\nHostMin:   10.20.30.193\nHostMax:   10.20.30.222\nBroadcast: 10.20.30.223\nHosts/Net: 30                    Class A, Private Internet"},
            {"cmd": "ip -4 addr show scope global",
             "explain": "看自己這台機器的 IP 與前綴，判斷自己在哪個網段。",
             "output": "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 state UP\n    inet 192.168.1.42/24 brd 192.168.1.255 scope global dynamic eth0"},
            {"cmd": "ip -6 addr show",
             "explain": "**資安檢查**：確認 IPv6 是否啟用。若有 global 位址，防火牆就必須同時設 IPv6 規則。",
             "output": "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n    inet6 2001:db8:1234::42/64 scope global dynamic mngtmpaddr\n    inet6 fe80::a00:27ff:fe4e:66a1/64 scope link\n# 有 global IPv6 → 記得檢查 ip6tables/nft 是否也有對應規則"},
            {"cmd": "sudo ip6tables -L INPUT -n | head -5",
             "explain": "如果這裡是 ACCEPT 而 IPv4 是 DROP，你就有一條沒人管的旁路。",
             "output": "Chain INPUT (policy ACCEPT)\ntarget     prot opt source               destination\n# 警訊：IPv6 預設政策是 ACCEPT，與 IPv4 的 DROP 不一致"},
        ],
    }],
    "quiz": [
        {"q": "192.168.1.100/26 的網路位址與廣播位址分別是？",
         "options": ["192.168.1.0 / 192.168.1.255", "192.168.1.64 / 192.168.1.127",
                     "192.168.1.96 / 192.168.1.127", "192.168.1.64 / 192.168.1.255"],
         "answer": 1,
         "why": "/26 區塊大小 = 256−192 = 64。起點 0/64/128/192，100 落在 64–127。"},
        {"q": "/28 網段可以放幾台主機？",
         "options": ["16", "14", "30", "8"],
         "answer": 1,
         "why": "2^(32−28) − 2 = 14。扣掉網路位址與廣播位址。"},
        {"q": "電腦拿到 169.254.22.13 這個 IP，代表什麼？",
         "options": ["正常的私有位址", "DHCP 取得失敗，系統自動配置 (APIPA)",
                     "被防火牆隔離", "IPv6 轉換位址"],
         "answer": 1,
         "why": "APIPA。可能是線路、交換器 port、DHCP 服務，或 802.1X 認證失敗。"},
        {"q": "關於 NAT，下列哪個說法正確？",
         "options": ["NAT 等同於防火牆", "NAT 提供隱匿性，但不做政策檢查，不能取代防火牆",
                     "NAT 會加密流量", "NAT 只能用於 IPv6"],
         "answer": 1,
         "why": "NAT 讓外部無法直接定位內部主機，但不檢查內容、也不管內部主動外連的惡意流量。"},
        {"q": "把訪客 Wi-Fi 切到獨立網段並只允許連往網際網路，主要目的是？",
         "options": ["提升 Wi-Fi 速度", "節省 IP 位址",
                     "限制攻擊擴散範圍，避免訪客裝置接觸內部資源", "符合 IPv6 規範"],
         "answer": 2,
         "why": "網路分段的核心價值是縮小爆炸半徑。訪客裝置不受管控，必須視為不可信。"},
        {"q": "2001:0db8:0000:0000:0000:ff00:0042:8329 正確的簡寫是？",
         "options": ["2001:db8::ff00:42:8329", "2001:db8::ff00::42:8329",
                     "2001:0db8::ff00:0042:8329:0", "2001:db8:0:ff00:42:8329"],
         "answer": 0,
         "why": "去前導零，連續零組用一個 :: 取代（只能用一次）。選項 B 用了兩個 :: 是無效寫法。"},
        {"q": "公司防火牆只設 IPv4 規則，但主機都啟用 IPv6。最大風險是？",
         "options": ["IPv6 速度較慢", "IPv6 形成未受管控的旁路，繞過所有既有規則",
                     "IPv6 不支援加密", "沒有風險"],
         "answer": 1,
         "why": "這是實務上非常常見的漏洞。所有網路政策必須同時涵蓋 IPv4 與 IPv6。"},
        {"q": "IPv6 中取代 ARP 功能的是哪個協定？",
         "options": ["ICMPv6 的 NDP 鄰居發現協定", "DHCPv6", "SLAAC", "RARP"],
         "answer": 0,
         "why": "NDP。因此 ARP 欺騙在 IPv6 對應為 NDP/RA 欺騙，防禦是 RA Guard 與 ND Inspection。"},
    ],
    "keywords": ["IPv4", "子網", "CIDR", "子網遮罩", "區塊大小", "私有位址", "NAT",
                 "APIPA", "IPv6", "網路分段", "微分段"],
    "takeaway": [
        "區塊大小 = 256 − 遮罩末位；用它三十秒算出任何網段範圍。",
        "網路分段是限制勒索病毒擴散最有效、最便宜的措施。",
        "IPv6 常是被遺忘的旁路 — 所有防火牆政策必須雙棧同時設定。",
    ],
})

CH.append({
    "id": "n03",
    "title": "交換器與 VLAN：同一個網段裡的攻防",
    "subtitle": "MAC 表、VLAN、Trunk、L2 攻擊與 CCNA 實作",
    "level": "進階",
    "minutes": 24,
    "summary": "L2 是最容易被忽略卻最危險的一層。ARP 沒有驗證機制，所以同網段內的中間人攻擊幾乎必然成立 — 除非你在交換器上設對防護。",
    "why": "交換器像辦公室的**內部郵差**。它記住「哪個人坐哪個位子」（MAC 表），"
           "然後把信直接送到那個位子。問題是 — **它完全相信別人說自己是誰**。"
           "有人舉手說「我是老闆」，郵差就把老闆的信給他。這就是 ARP 欺騙。",
    "sections": [
        {
            "heading": "交換器怎麼工作：MAC 位址表",
            "body": "交換器開機時 MAC 表是空的，靠三個動作學習：\n\n"
                    "1. **學習**：收到封包時記下「來源 MAC ← 從哪個 port 進來」。\n"
                    "2. **轉送**：查表找到目的 MAC 對應的 port，只送那一個。\n"
                    "3. **洪泛**：**查不到目的 MAC 時，往所有 port 送**。\n\n"
                    "第 3 點是資安關鍵。\n\n"
                    "**MAC 洪泛攻擊**：\n"
                    "- 攻擊者狂送幾萬個假造來源 MAC 的封包\n"
                    "- 交換器的 CAM Table 有容量上限，被塞滿\n"
                    "- 表滿之後，交換器對所有新流量只能**洪泛**\n"
                    "- 結果：交換器退化成 Hub，**攻擊者可以看到整個 VLAN 的流量**\n\n"
                    "**防禦：Port Security** — 限制每個 port 最多學習幾個 MAC。",
            "example": "Cisco 上的 Port Security 設定：\n"
                       "```\n"
                       "interface GigabitEthernet0/5\n"
                       " switchport mode access\n"
                       " switchport port-security\n"
                       " switchport port-security maximum 2\n"
                       " switchport port-security violation restrict\n"
                       " switchport port-security mac-address sticky\n"
                       "```\n"
                       "- `maximum 2` — 最多兩個 MAC（電腦 + IP 電話）\n"
                       "- `violation restrict` — 超過就丟棄並記錄（比 shutdown 溫和）\n"
                       "- `sticky` — 自動把學到的 MAC 記進設定檔",
            "note": "三種 violation 模式：**protect**（默默丟棄）、"
                    "**restrict**（丟棄+記錄+SNMP trap）、**shutdown**（直接關 port）。考試常問差異。",
        },
        {
            "heading": "ARP 與 ARP 欺騙：L2 最大的洞",
            "body": "**ARP 的工作**：我知道對方 IP，但 L2 傳送需要 MAC，所以要問。\n\n"
                    "1. 主機廣播：「誰是 `192.168.1.1`？」\n"
                    "2. 閘道回應：「我是，MAC 是 `3c:37:86:1f:2a:b0`」\n"
                    "3. 主機記進 ARP 快取\n\n"
                    "**致命缺陷：ARP 沒有任何驗證。**\n"
                    "- 任何人都可以回答，不管有沒有人問（Gratuitous ARP）\n"
                    "- 後到的回應會覆蓋先前的紀錄\n\n"
                    "**ARP 欺騙**：\n"
                    "- 攻擊者對受害者說「我是閘道」\n"
                    "- 同時對閘道說「我是受害者」\n"
                    "- 雙向流量全部經過攻擊者 → **中間人攻擊成立**",
            "example": "**怎麼發現自己被 ARP 欺騙**（重要偵測技能）：\n\n"
                       "看 ARP 表，如果**兩個不同 IP 對應到同一個 MAC**，"
                       "而其中一個是閘道 → 高度可疑。\n"
                       "```\n"
                       "192.168.1.1   lladdr 08:00:27:ab:cd:ef   ← 閘道\n"
                       "192.168.1.77  lladdr 08:00:27:ab:cd:ef   ← 同一個 MAC！\n"
                       "```\n"
                       "**另一個徵兆**：沒人詢問卻出現大量 ARP Reply。",
            "note": "**為什麼 HTTPS 很重要**：即使被 ARP 欺騙，攻擊者看到的 HTTPS 內容仍是亂碼。"
                    "所以 L2 攻擊的最終緩解手段之一是全站加密 + HSTS。"
                    "但未加密的 DNS 查詢仍會洩漏你造訪的網站。",
        },
        {
            "heading": "VLAN：在一台交換器上切出多個網段",
            "body": "**VLAN** 讓你在同一台實體交換器上切出互不相通的邏輯網段。\n\n"
                    "**兩種 port 模式**：\n"
                    "- **Access Port**：接終端裝置，只屬於**一個** VLAN。\n"
                    "- **Trunk Port**：接另一台交換器或路由器，"
                    "**同時載送多個 VLAN**，用 **802.1Q 標籤**區分。\n\n"
                    "**Native VLAN**：Trunk 上唯一「不打標籤」的 VLAN。"
                    "預設是 VLAN 1 — **這是安全問題的來源**。\n\n"
                    "**VLAN 跳躍攻擊**兩種手法：\n"
                    "1. **Switch Spoofing**：攻擊者裝置假裝是交換器，"
                    "利用 **DTP** 自動協商成 Trunk，就能存取所有 VLAN。\n"
                    "2. **Double Tagging**：打兩層 802.1Q 標籤。"
                    "第一台交換器剝掉外層，內層標籤讓封包跑進別的 VLAN。",
            "example": "**VLAN 安全設定標準做法（CCNA 與 CND 都必考）**：\n"
                       "```\n"
                       "! 1. 明確關閉 DTP，不讓 port 自動變 Trunk\n"
                       "interface range Gi0/1-24\n"
                       " switchport mode access\n"
                       " switchport nonegotiate\n"
                       " switchport access vlan 10\n"
                       " spanning-tree portfast\n"
                       " spanning-tree bpduguard enable\n"
                       "!\n"
                       "! 2. Native VLAN 改成沒人用的 VLAN\n"
                       "interface Gi0/48\n"
                       " switchport mode trunk\n"
                       " switchport trunk native vlan 999\n"
                       " switchport trunk allowed vlan 10,20,30\n"
                       "!\n"
                       "! 3. 沒用到的 port 一律關閉並丟進黑洞 VLAN\n"
                       "interface range Gi0/25-40\n"
                       " switchport access vlan 999\n"
                       " shutdown\n"
                       "```\n"
                       "**四個動作**：關 DTP、改 Native VLAN、限制 allowed vlan、關閉閒置 port。",
            "note": "考點：**VLAN 1 永遠不要承載使用者流量**，"
                    "因為它是預設值，CDP/VTP/STP 等控制協定都跑在上面。",
        },
        {
            "heading": "L2 完整防護清單（CND 重點）",
            "body": "把 L2 防護當成檢查表，逐項確認：\n\n"
                    "- **Port Security** — 限制每 port 的 MAC 數 → 擋 MAC 洪泛\n"
                    "- **DAI（Dynamic ARP Inspection）** — 檢查 ARP 封包是否與綁定表一致 → "
                    "**擋 ARP 欺騙**（最關鍵）\n"
                    "- **DHCP Snooping** — 只有指定 port 可發 DHCP 回應 → 擋惡意 DHCP 伺服器\n"
                    "- **IP Source Guard** — 檢查來源 IP 是否符合綁定表 → 擋 IP 偽造\n"
                    "- **BPDU Guard** — 收到 STP 封包就關 port → 擋 STP 根橋劫持\n"
                    "- **Root Guard** — 防止外部交換器搶成根橋\n"
                    "- **Storm Control** — 限制廣播流量比例 → 擋廣播風暴\n"
                    "- **802.1X** — port 層級身分驗證，**沒通過認證連 IP 都拿不到**\n"
                    "- **關閉未使用 port** + 丟進黑洞 VLAN\n"
                    "- **關閉對外 port 的 CDP/LLDP** — 避免洩漏設備型號與版本",
            "example": "**DAI + DHCP Snooping 組合設定**：\n"
                       "```\n"
                       "ip dhcp snooping\n"
                       "ip dhcp snooping vlan 10,20\n"
                       "no ip dhcp snooping information option\n"
                       "!\n"
                       "ip arp inspection vlan 10,20\n"
                       "ip arp inspection validate src-mac dst-mac ip\n"
                       "!\n"
                       "! 上行 port 設為信任\n"
                       "interface Gi0/48\n"
                       " ip dhcp snooping trust\n"
                       " ip arp inspection trust\n"
                       "!\n"
                       "! 使用者 port 加上速率限制\n"
                       "interface range Gi0/1-24\n"
                       " ip arp inspection limit rate 15\n"
                       "```\n"
                       "**原理**：DHCP Snooping 記錄「哪個 port 的哪個 MAC 拿到哪個 IP」，"
                       "DAI 拿這張表驗證每個 ARP 封包。攻擊者聲稱「我是閘道」時對不上 → 丟棄。",
            "note": "**實務價值**：很多公司花大錢買下一代防火牆，"
                    "但交換器上一項 L2 防護都沒開。攻擊者只要接上任何一個網路孔，"
                    "就能在內網做中間人攻擊。L2 防護幾乎零成本，投報率極高。",
        },
    ],
    "diagram": """<svg viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ARP 欺騙中間人攻擊示意">
<defs><marker id="ar1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#f87171"/></marker></defs>
<rect x="20" y="40" width="120" height="56" rx="8" fill="#0f2233" stroke="#38bdf8" stroke-width="1.5"/>
<text x="80" y="64" text-anchor="middle" fill="#e2e8f0" font-size="12">受害者</text>
<text x="80" y="83" text-anchor="middle" fill="#64748b" font-size="10">192.168.1.50</text>
<rect x="540" y="40" width="120" height="56" rx="8" fill="#0f2233" stroke="#38bdf8" stroke-width="1.5"/>
<text x="600" y="64" text-anchor="middle" fill="#e2e8f0" font-size="12">閘道 / 路由器</text>
<text x="600" y="83" text-anchor="middle" fill="#64748b" font-size="10">192.168.1.1</text>
<rect x="270" y="200" width="140" height="60" rx="8" fill="#2b1414" stroke="#f87171" stroke-width="2"/>
<text x="340" y="225" text-anchor="middle" fill="#fca5a5" font-size="12" font-weight="700">攻擊者</text>
<text x="340" y="244" text-anchor="middle" fill="#64748b" font-size="10">192.168.1.77</text>
<line x1="140" y1="68" x2="538" y2="68" stroke="#334155" stroke-width="1.2" stroke-dasharray="5 4"/>
<text x="340" y="60" text-anchor="middle" fill="#475569" font-size="11">正常路徑（應該直接走）</text>
<path d="M120 96 L285 200" stroke="#f87171" stroke-width="2" fill="none" marker-end="url(#ar1)"/>
<path d="M395 200 L565 96" stroke="#f87171" stroke-width="2" fill="none" marker-end="url(#ar1)"/>
<text x="128" y="165" fill="#fca5a5" font-size="11">「我是閘道」</text>
<text x="440" y="165" fill="#fca5a5" font-size="11">「我是受害者」</text>
<text x="340" y="292" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="700">結果：雙向流量都經過攻擊者 → 可竊聽、篡改</text>
<text x="340" y="318" text-anchor="middle" fill="#4ade80" font-size="12">防禦：交換器啟用 DHCP Snooping + Dynamic ARP Inspection</text>
</svg>""",
    "labs": [{
        "title": "偵測 ARP 異常與檢查交換器狀態",
        "goal": "學會判斷「我是不是正被中間人攻擊」。",
        "warn": "**只在你自己的網路做偵測。實際對他人網路執行 ARP 欺騙在台灣可能違反刑法第 358、359 條。本課程只教偵測與防禦。**",
        "steps": [
            {"cmd": "ip neigh show",
             "explain": "看 ARP 快取。重點：有沒有兩個 IP 對到同一個 MAC。",
             "output": "192.168.1.1 dev eth0 lladdr 08:00:27:ab:cd:ef REACHABLE\n192.168.1.50 dev eth0 lladdr 08:00:27:11:22:33 REACHABLE\n192.168.1.77 dev eth0 lladdr 08:00:27:ab:cd:ef REACHABLE\n# 警訊：.1 和 .77 共用同一個 MAC → 高度懷疑 ARP 欺騙"},
            {"cmd": "sudo arp-scan --localnet",
             "explain": "掃描本地網段所有裝置的 MAC，工具會直接標示重複的 MAC。",
             "output": "Interface: eth0, datalink type: EN10MB\n192.168.1.1   08:00:27:ab:cd:ef   PCS Systemtechnik GmbH\n192.168.1.50  08:00:27:11:22:33   PCS Systemtechnik GmbH\n192.168.1.77  08:00:27:ab:cd:ef   PCS Systemtechnik GmbH (DUP: 2)\n\n3 packets received by filter\n# (DUP: 2) 就是重複 MAC 的警告"},
            {"cmd": "sudo tcpdump -i eth0 -nn arp -c 8",
             "explain": "抓 ARP 封包。正常環境 ARP 很安靜；一直看到同一台宣告 is-at 就是在毒化。",
             "output": "10:31:02.101 ARP, Request who-has 192.168.1.1 tell 192.168.1.50, length 28\n10:31:02.102 ARP, Reply 192.168.1.1 is-at 08:00:27:ab:cd:ef, length 46\n10:31:03.201 ARP, Reply 192.168.1.1 is-at 08:00:27:ab:cd:ef, length 46\n10:31:04.301 ARP, Reply 192.168.1.1 is-at 08:00:27:ab:cd:ef, length 46\n10:31:05.401 ARP, Reply 192.168.1.1 is-at 08:00:27:ab:cd:ef, length 46\n# 沒人問卻不斷送 Reply = Gratuitous ARP 洪流 = 正在被毒化"},
            {"cmd": "show mac address-table dynamic vlan 10",
             "explain": "**Cisco 指令**：看 VLAN 10 學到的 MAC。同一 MAC 出現在多個 port 是警訊。",
             "output": "          Mac Address Table\n-------------------------------------------\nVlan    Mac Address       Type        Ports\n----    -----------       --------    -----\n  10    0800.2711.2233    DYNAMIC     Gi0/3\n  10    0800.27ab.cdef    DYNAMIC     Gi0/7\n  10    3c37.861f.2ab0    DYNAMIC     Gi0/48\nTotal Mac Addresses for this criterion: 3"},
            {"cmd": "show ip arp inspection statistics vlan 10",
             "explain": "**確認 DAI 有在運作並攔到東西**。Dropped 有數字代表正在擋攻擊。",
             "output": " Vlan      Forwarded        Dropped   DHCP Drops   ACL Drops\n ----      ---------        -------   ----------   ---------\n   10          14892           2317         2317           0\n# 擋掉 2317 個不符合綁定表的 ARP 封包 → DAI 正在發揮作用"},
            {"cmd": "show port-security interface Gi0/3",
             "explain": "確認 Port Security 狀態與違規次數。",
             "output": "Port Security              : Enabled\nPort Status                : Secure-up\nViolation Mode             : Restrict\nMaximum MAC Addresses      : 2\nTotal MAC Addresses        : 1\nSticky MAC Addresses       : 1\nSecurity Violation Count   : 0"},
        ],
    }],
    "quiz": [
        {"q": "MAC 洪泛攻擊成功後，交換器的行為會變成？",
         "options": ["完全停止轉送", "退化成 Hub，對所有 port 洪泛流量", "自動重開機", "封鎖所有 VLAN"],
         "answer": 1,
         "why": "CAM 表被塞滿後查不到目的 MAC，只能洪泛 → 攻擊者能監聽整個 VLAN。"},
        {"q": "ARP 協定最根本的安全問題是什麼？",
         "options": ["傳輸速度太慢", "沒有任何身分驗證，任何人都能回應且後到者覆蓋前者",
                     "只支援 IPv6", "封包太大"],
         "answer": 1,
         "why": "ARP 設計於信任的網路環境，完全沒有驗證機制。"},
        {"q": "防禦 ARP 欺騙最直接有效的交換器功能是？",
         "options": ["BPDU Guard", "Dynamic ARP Inspection 搭配 DHCP Snooping",
                     "Storm Control", "Spanning Tree PortFast"],
         "answer": 1,
         "why": "DHCP Snooping 建立 port-MAC-IP 綁定表，DAI 用它驗證每個 ARP 封包。兩者必須一起用。"},
        {"q": "攻擊者利用 DTP 自動協商讓交換器把 port 變成 Trunk，從而存取所有 VLAN。這叫什麼？對策是？",
         "options": ["Double Tagging；改 Native VLAN",
                     "Switch Spoofing；設定 switchport mode access 並加上 nonegotiate",
                     "MAC 洪泛；開 Port Security", "廣播風暴；開 Storm Control"],
         "answer": 1,
         "why": "Switch Spoofing。對策是明確指定 access 模式並用 nonegotiate 關閉 DTP。"},
        {"q": "為什麼不應該讓 VLAN 1 承載使用者流量？",
         "options": ["VLAN 1 速度較慢", "它是預設值，且多種控制協定跑在上面，是攻擊者首選目標",
                     "VLAN 1 不支援 802.1Q", "VLAN 1 只能用於 IPv6"],
         "answer": 1,
         "why": "VLAN 1 是所有 Cisco 設備的預設 VLAN，CDP/VTP/STP 都在上面。Native VLAN 應改為未使用編號。"},
        {"q": "Port Security 哪個 violation mode 會「丟棄違規流量並記錄，但不關閉 port」？",
         "options": ["protect", "restrict", "shutdown", "monitor"],
         "answer": 1,
         "why": "protect 只默默丟棄；restrict 丟棄並記錄；shutdown 直接關 port。實務上 restrict 較常用。"},
        {"q": "惡意 DHCP 伺服器的危害是什麼？哪個功能可以擋？",
         "options": ["耗盡頻寬；Storm Control",
                     "把自己設為受害者的閘道與 DNS，形成中間人；DHCP Snooping",
                     "偽造 MAC；Port Security", "劫持 STP 根橋；BPDU Guard"],
         "answer": 1,
         "why": "攻擊者發 DHCP 回應把自己設成閘道/DNS，流量就全部經過他。DHCP Snooping 只允許 trust port 回應。"},
        {"q": "即使遭 ARP 欺騙，下列哪個措施仍能保護資料內容不被讀取？",
         "options": ["NAT", "端對端加密（HTTPS/TLS）", "VLAN", "更快的網路"],
         "answer": 1,
         "why": "攻擊者能看到流量但看不懂內容。但未加密的 DNS 查詢仍會洩漏造訪目標。"},
    ],
    "keywords": ["交換器", "MAC 表", "CAM", "MAC 洪泛", "ARP 欺騙", "中間人攻擊", "VLAN",
                 "Trunk", "802.1Q", "Native VLAN", "VLAN 跳躍", "DAI", "DHCP Snooping",
                 "Port Security", "802.1X", "BPDU Guard"],
    "takeaway": [
        "ARP 沒有驗證，所以同網段中間人攻擊必然可行，除非啟用 DAI + DHCP Snooping。",
        "VLAN 安全四件事：關 DTP、改 Native VLAN、限制 allowed vlan、關閉閒置 port。",
        "L2 防護幾乎零成本卻極少人設定 — 這是投報率最高的防禦之一。",
    ],
})

CH.append({
    "id": "n04",
    "title": "路由與防火牆規則：跨網段的守門員",
    "subtitle": "路由表、靜態與動態路由、ACL、狀態式防火牆",
    "level": "進階",
    "minutes": 22,
    "summary": "路由決定「封包能不能到」，ACL 與防火牆決定「該不該讓它到」。兩者一起設計，才叫網路分段。",
    "why": "路由器像**十字路口的交通警察**：看目的地，指示走哪條路。"
           "防火牆是**檢查哨**：不只看你要去哪，還問「你有沒有資格去」。"
           "很多公司有路由（連得通）但沒有政策（沒人管該不該通）— 這就是內網一破全破的原因。",
    "sections": [
        {
            "heading": "路由表怎麼被查詢：最長前綴優先",
            "body": "路由器用**目的 IP** 查路由表，規則只有一條：\n\n"
                    "**最長前綴匹配** — 越具體的路由優先，不管它排在第幾行。\n\n"
                    "```\n"
                    "0.0.0.0/0        via 203.0.113.1     ← 預設路由（最不具體）\n"
                    "10.0.0.0/8       via 10.1.1.1\n"
                    "10.20.30.0/24    via 10.1.1.9        ← 最具體\n"
                    "```\n"
                    "封包要去 `10.20.30.55`：三條都符合，但 **/24 最長 → 走 10.1.1.9**。\n\n"
                    "**判斷路由來源的兩個數字**：\n"
                    "- **管理距離 (AD)**：直連=0、靜態=1、EIGRP=90、OSPF=110、RIP=120。"
                    "**數字小的贏。**\n"
                    "- **度量值 (Metric)**：同一協定內比較哪條路好。",
            "example": "**資安相關的路由攻擊**：\n"
                       "攻擊者若能注入一條「更具體」的路由，就能把流量吸到自己身上。\n"
                       "- 內網：偽造 OSPF/RIP 通告 → 對策是**路由協定認證** + 關閉不必要介面\n"
                       "- 網際網路：**BGP 劫持** — 宣告自己擁有別人的網段，"
                       "把全球流量吸過去 → 對策是 **RPKI** 與路由過濾\n\n"
                       "**「更具體的路由優先」既是功能也是攻擊面。**",
            "note": "考點：`0.0.0.0/0` 是預設路由。所有查不到的封包都往它走。"
                    "前綴長度 0 = 最不具體 = 最後才用。",
        },
        {
            "heading": "靜態路由 vs 動態路由",
            "body": "**靜態路由**：管理員手寫。\n"
                    "- 優點：完全可控、不耗資源、**不會被路由協定攻擊**\n"
                    "- 缺點：網路一變就要手改\n"
                    "- 適用：DMZ、小型網路、防火牆對接\n\n"
                    "**動態路由**：路由器互相交換資訊自動學習。\n"
                    "- **RIP**：最舊，跳數上限 15，已很少用\n"
                    "- **OSPF**：**最常見的內部協定**，用 Cost 算最短路徑，支援分區\n"
                    "- **EIGRP**：Cisco 專有，收斂快\n"
                    "- **BGP**：網際網路骨幹協定\n\n"
                    "**資安考量**：**任何能接上網路的裝置都可能參與路由協商**。必須做兩件事：\n"
                    "1. **啟用認證**（OSPF message-digest、BGP MD5/TCP-AO）\n"
                    "2. **passive-interface** — 對使用者網段不要發送路由通告",
            "example": "OSPF 安全設定：\n"
                       "```\n"
                       "router ospf 1\n"
                       " area 0 authentication message-digest\n"
                       " passive-interface default\n"
                       " no passive-interface GigabitEthernet0/1\n"
                       " network 10.0.0.0 0.0.0.255 area 0\n"
                       "!\n"
                       "interface GigabitEthernet0/1\n"
                       " ip ospf message-digest-key 1 md5 <強密碼>\n"
                       "```\n"
                       "`passive-interface default` 先全部關閉通告，再只對確定要跑 OSPF 的介面開啟。"
                       "**這是「預設拒絕」原則在路由協定上的應用。**",
            "note": "實務原則：面向使用者、訪客、IoT 的介面**永遠不要**跑動態路由協定。",
        },
        {
            "heading": "ACL：路由器上的封包過濾",
            "body": "**ACL** 是一串允許／拒絕規則，由上往下比對，**一符合就停止**。\n\n"
                    "- **標準 ACL**（1–99）：**只能看來源 IP**\n"
                    "- **擴充 ACL**（100–199 或具名）：可看**來源 IP、目的 IP、協定、port**\n\n"
                    "**三個致命細節**：\n"
                    "1. **順序極度重要**。把 `permit any` 放第一行，後面全部無效。\n"
                    "2. **結尾有隱含的 `deny any`**。所以只要寫了 ACL，"
                    "沒明確允許的一律被擋 — 這是好事（預設拒絕），"
                    "但很多人因此把管理流量也擋掉。\n"
                    "3. **標準 ACL 放靠近目的地**（只認來源，放太前面會擋過頭）；"
                    "**擴充 ACL 放靠近來源**（越早擋掉越省資源）。",
            "example": "**情境**：讓辦公網段 `10.10.10.0/24` 只能用 HTTPS 存取"
                       "伺服器網段 `10.10.30.0/24`，其他全禁，並記錄被拒絕的流量。\n"
                       "```\n"
                       "ip access-list extended OFFICE-TO-SERVER\n"
                       " permit tcp 10.10.10.0 0.0.0.255 10.10.30.0 0.0.0.255 eq 443\n"
                       " permit udp 10.10.10.0 0.0.0.255 host 10.10.30.53 eq 53\n"
                       " deny ip any any log\n"
                       "!\n"
                       "interface GigabitEthernet0/1\n"
                       " ip access-group OFFICE-TO-SERVER in\n"
                       "```\n"
                       "**注意最後那行**：雖然結尾本來就隱含 deny，"
                       "但明確寫出來並加 `log` 才會產生日誌 — "
                       "**沒有日誌的阻擋等於沒有能見度**。",
            "note": "Cisco 萬用遮罩與子網遮罩相反：`0.0.0.255` 等於 `/24`。"
                    "0 = 必須相符、255 = 不管。`host x` = `x 0.0.0.0`，`any` = `0.0.0.0 255.255.255.255`。",
        },
        {
            "heading": "無狀態 vs 狀態式：為什麼現代防火牆不用純 ACL",
            "body": "**無狀態過濾**：每個封包獨立判斷，不記得前後關係。\n"
                    "- 問題：你允許內部連出去，但**回來的封包**是從外面進來的，也要開規則。"
                    "為了讓回應能進來，你被迫開放大量高位 port → **攻擊面暴增**。\n\n"
                    "**狀態式檢查**：防火牆維護一張**連線狀態表**。\n"
                    "- 記住「內部 10.10.10.5:51234 → 外部 93.184.216.34:443 已建立」\n"
                    "- 屬於既有連線的回應封包**自動允許**\n"
                    "- 不屬於任何已知連線的封包**直接丟棄**\n\n"
                    "**再往上兩層**：\n"
                    "- **NGFW**：能識別**應用程式**（分得出 443 上跑的是 Teams 還是不明加密隧道）、"
                    "整合 IPS、可依使用者身分套規則。\n"
                    "- **WAF**：專門檢查 HTTP 內容，擋 SQL Injection / XSS。",
            "example": "**同一需求的三種寫法**：內部員工可瀏覽網頁，外部不能主動連進來。\n\n"
                       "- **無狀態 ACL**：要寫兩條，回應規則必須開放 `1024-65535`"
                       "→ 攻擊者可偽造來源 port 443 直接打進來。\n"
                       "- **狀態式防火牆**：只寫一條 `allow inside → any 443`，"
                       "回應由狀態表處理，外部主動連入一律 drop。\n"
                       "- **NGFW**：`allow inside → application:web-browsing`，"
                       "同時能擋「假裝是 HTTPS 的 C2 隧道」。",
            "note": "考點：狀態表本身是資源，**SYN Flood 就是在攻擊狀態表**。"
                    "對策包含 SYN Cookie、連線速率限制、合理的 timeout。",
        },
        {
            "heading": "防火牆規則的設計原則",
            "body": "**五個原則，順序就是重要性**：\n\n"
                    "1. **預設拒絕**：最後一條是 deny all，只放行明確需要的。**唯一正確的起點。**\n"
                    "2. **最小開放**：具體到 IP + port + 方向。不要寫 `any any`。\n"
                    "3. **雙向都要想**：inbound 和 outbound 都要管。"
                    "**大多數公司只管 inbound**，結果惡意程式連回 C2 完全沒阻力。\n"
                    "4. **記錄被拒絕的流量**：沒有日誌就沒有偵測能力。\n"
                    "5. **定期清理**：規則會累積成上千條無人敢動的化石。每半年做一次覆核。\n\n"
                    "**出口過濾 (Egress Filtering) 是最被低估的措施**："
                    "限制內部只能從特定主機連出特定 port，"
                    "可直接切斷惡意程式的 C2 通訊與資料外傳。",
            "example": "**規則審查時要問的問題**：\n"
                       "- 這條規則是誰在什麼時候為了什麼加的？（有註解與工單編號嗎）\n"
                       "- 來源和目的能不能再縮小？\n"
                       "- 過去 90 天有命中過嗎？（沒命中的可考慮移除）\n"
                       "- 有沒有 `permit ip any any`？\n"
                       "- 有沒有規則被前面的規則遮蔽而永遠不會生效？\n\n"
                       "**推斷值**：多數企業防火牆有 30–60% 的規則從未命中，"
                       "其中不少是暫時開放後忘記關的。",
            "note": "防火牆規則應納入版本控管與變更管理流程。"
                    "「誰改了什麼」要能追溯，這是稽核必查項目。",
        },
    ],
    "table": {
        "caption": "防火牆技術演進與能看到的資訊",
        "head": ["類型", "檢查層級", "能判斷", "擋不了"],
        "rows": [
            ["封包過濾 / ACL", "L3-L4 無狀態", "IP、port、協定", "回應追蹤、應用內容"],
            ["狀態式防火牆", "L3-L4 有狀態", "連線關係、方向", "應用層攻擊、加密隧道濫用"],
            ["應用代理 Proxy", "L7", "完整內容、可快取與過濾", "效能成本高、需支援協定"],
            ["NGFW", "L3-L7 + 身分", "應用程式、使用者、IPS 特徵", "端點內部行為"],
            ["WAF", "L7 HTTP", "SQLi、XSS、爬蟲、API 濫用", "非 HTTP 流量"],
        ],
    },
    "labs": [{
        "title": "讀懂並驗證防火牆規則",
        "goal": "在 Linux 上實作「預設拒絕 + 最小開放 + 出口過濾」。",
        "warn": "**在測試機執行。設錯防火牆會把自己鎖在外面 — 遠端操作前務必先設好排程復原。**",
        "steps": [
            {"cmd": "sudo nft list ruleset",
             "explain": "看目前完整規則。重點檢查 `policy` 是 drop 還是 accept。",
             "output": "table inet filter {\n  chain input {\n    type filter hook input priority 0; policy drop;\n    ct state established,related accept\n    iif lo accept\n    tcp dport 22 ct state new limit rate 4/minute accept\n    tcp dport 443 accept\n    log prefix \"nft-drop: \" level warn\n  }\n  chain output {\n    type filter hook output priority 0; policy accept;\n  }\n}\n# input policy drop = 預設拒絕（正確）\n# output policy accept = 出口未過濾（風險：C2 可自由外連）"},
            {"cmd": "sudo iptables -L INPUT -n -v --line-numbers",
             "explain": "看每條規則的**命中次數 (pkts)**。長期為 0 的規則可考慮移除。",
             "output": "Chain INPUT (policy DROP 218 packets, 13072 bytes)\nnum   pkts bytes target     prot opt source          destination\n1   184392   22M ACCEPT     all  --  0.0.0.0/0       0.0.0.0/0    ctstate RELATED,ESTABLISHED\n2      412  24K ACCEPT     tcp  --  10.10.99.0/24   0.0.0.0/0    tcp dpt:22\n3    29104 1.8M ACCEPT     tcp  --  0.0.0.0/0       0.0.0.0/0    tcp dpt:443\n4        0     0 ACCEPT     tcp  --  0.0.0.0/0       0.0.0.0/0    tcp dpt:3306\n5     2317  139K LOG       all  --  0.0.0.0/0       0.0.0.0/0    LOG prefix \"DROP: \"\n# 第 4 條：對外開放 MySQL 且從未命中 → 應立即移除"},
            {"cmd": "sudo conntrack -L -p tcp --state ESTABLISHED | head -5",
             "explain": "看狀態式防火牆的連線表。異常大量對外連線可能是資料外傳或挖礦。",
             "output": "tcp 6 431999 ESTABLISHED src=10.10.10.5 dst=93.184.216.34 sport=51422 dport=443 [ASSURED]\ntcp 6 431998 ESTABLISHED src=10.10.10.5 dst=142.250.76.100 sport=51436 dport=443 [ASSURED]\ntcp 6  86391 ESTABLISHED src=10.10.10.5 dst=185.220.101.44 sport=51501 dport=9001 [ASSURED]\nconntrack v1.4.6: 3 flow entries have been shown.\n# dport 9001 對外 + 陌生 IP → 值得調查（Tor 常用 port）"},
            {"cmd": "ip route get 8.8.8.8",
             "explain": "確認某目的地實際會走哪條路由 — 驗證最長前綴匹配的結果。",
             "output": "8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.42 uid 1000\n    cache"},
            {"cmd": "show ip access-lists OFFICE-TO-SERVER",
             "explain": "**Cisco**：看 ACL 每一行的命中次數，判斷規則是否真的在用。",
             "output": "Extended IP access list OFFICE-TO-SERVER\n    10 permit tcp 10.10.10.0 0.0.0.255 10.10.30.0 0.0.0.255 eq 443 (48219 matches)\n    20 permit udp 10.10.10.0 0.0.0.255 host 10.10.30.53 eq domain (9021 matches)\n    30 deny ip any any log (1544 matches)"},
        ],
    }],
    "quiz": [
        {"q": "路由表有 0.0.0.0/0、10.0.0.0/8、10.20.30.0/24。封包要去 10.20.30.55 走哪一條？",
         "options": ["0.0.0.0/0，因為排最前面", "10.0.0.0/8",
                     "10.20.30.0/24，因為前綴最長最具體", "會被丟棄"],
         "answer": 2,
         "why": "最長前綴匹配。與排列順序無關，越具體越優先。"},
        {"q": "下列哪個管理距離代表最可信的路由來源？",
         "options": ["靜態路由 1", "OSPF 110", "RIP 120", "EIGRP 90"],
         "answer": 0,
         "why": "AD 越小越可信。直連=0、靜態=1、EIGRP=90、OSPF=110、RIP=120。"},
        {"q": "Cisco ACL 結尾有什麼隱含規則？造成什麼影響？",
         "options": ["隱含 permit any", "隱含 deny any，所以沒明確允許的流量都被擋",
                     "沒有隱含規則", "隱含 log all"],
         "answer": 1,
         "why": "隱含 deny any 實現預設拒絕。但隱含的 deny **不會產生日誌**，"
                "所以實務上會明確寫 deny ip any any log。"},
        {"q": "為什麼狀態式防火牆比無狀態 ACL 安全？",
         "options": ["加密能力更強", "它記住連線狀態，回應封包自動允許，不必開放大範圍高位 port",
                     "速度更快", "支援更多協定"],
         "answer": 1,
         "why": "無狀態過濾為了讓回應進來必須開放高位 port，攻擊者可偽造來源 port 穿過。"},
        {"q": "出口過濾 (Egress Filtering) 主要防的是什麼？",
         "options": ["外部掃描", "惡意程式對外連線至 C2 伺服器與資料外傳", "DDoS", "密碼暴力破解"],
         "answer": 1,
         "why": "多數公司只管進入方向。限制對外連線能直接切斷 C2 通道與外洩管道。"},
        {"q": "Cisco 萬用遮罩 0.0.0.255 對應哪個 CIDR？",
         "options": ["/8", "/16", "/24", "/32"],
         "answer": 2,
         "why": "萬用遮罩與子網遮罩相反。0 = 必須相符，255 = 不管 → /24。"},
        {"q": "內部路由器對「訪客 Wi-Fi 網段」的介面啟用了 OSPF。有什麼風險？",
         "options": ["沒有風險", "訪客裝置可偽造路由通告吸引流量；應設 passive-interface 並啟用認證",
                     "會降低 Wi-Fi 速度", "違反 IPv6 規範"],
         "answer": 1,
         "why": "不可信網段絕不能參與路由協定。應用 passive-interface default 再逐一開啟。"},
        {"q": "規則審查發現某條規則 90 天內 0 命中，最恰當的處理是？",
         "options": ["立即刪除", "確認用途與負責人後移除或收緊，並留下變更紀錄",
                     "維持不動以免出錯", "改成 permit any"],
         "answer": 1,
         "why": "0 命中通常是失效或忘記關，但直接刪可能影響季度性業務。應走變更管理流程。"},
    ],
    "keywords": ["路由表", "最長前綴匹配", "管理距離", "靜態路由", "OSPF", "BGP",
                 "ACL", "萬用遮罩", "狀態式防火牆", "NGFW", "WAF", "出口過濾",
                 "預設拒絕", "BGP 劫持"],
    "takeaway": [
        "路由靠最長前綴匹配；越具體越優先，這既是功能也是攻擊面。",
        "ACL 順序決定一切，結尾隱含 deny 但不記錄，所以要明確寫 deny + log。",
        "只管 inbound 是最常見的漏洞；出口過濾能直接切斷 C2 與資料外傳。",
    ],
})

CH.append({
    "id": "n05",
    "title": "常見協定與 port：安全與不安全的對照",
    "subtitle": "必背 port 表、明文協定的風險、加密替代方案",
    "level": "入門",
    "minutes": 20,
    "summary": "看到開放的 port 就能推論「這台機器在做什麼、風險在哪」。這是掃描結果判讀的基本功。",
    "why": "port 像大樓的**門牌號碼**：80 號房間是網頁部門、25 號是郵件部門。"
           "掃描一台機器等於看它開了哪些窗口。**看到 23（Telnet）開著，"
           "你不用測就知道這台機器有問題** — 因為它把帳號密碼用明文傳輸。",
    "sections": [
        {
            "heading": "必背 port（考試與實務通用）",
            "body": "port 分三個範圍：\n"
                    "- **0–1023 熟知 port**：需管理員權限才能綁定\n"
                    "- **1024–49151 註冊 port**\n"
                    "- **49152–65535 動態 port**：客戶端連出去時隨機用的\n\n"
                    "**用「明文 → 加密」成對記憶最有效**：\n"
                    "- Telnet 23 → **SSH 22**\n"
                    "- HTTP 80 → **HTTPS 443**\n"
                    "- FTP 20/21 → **SFTP 22 / FTPS 990**\n"
                    "- SMTP 25 → **SMTPS 465 / STARTTLS 587**\n"
                    "- POP3 110 → **POP3S 995**\n"
                    "- IMAP 143 → **IMAPS 993**\n"
                    "- LDAP 389 → **LDAPS 636**\n"
                    "- SNMP v1/v2c 161 → **SNMPv3 161**\n"
                    "- DNS 53 → **DoT 853 / DoH 443**\n\n"
                    "**其他高風險 port**：445 SMB（WannaCry 走這裡）、3389 RDP、"
                    "3306/1433/5432 資料庫、6379 Redis、27017 MongoDB、623 IPMI、5900 VNC。",
            "example": "**掃描結果判讀練習**：\n"
                       "```\n"
                       "PORT     STATE  SERVICE     VERSION\n"
                       "22/tcp   open   ssh         OpenSSH 7.4\n"
                       "23/tcp   open   telnet\n"
                       "80/tcp   open   http        Apache 2.2.15\n"
                       "445/tcp  open   microsoft-ds\n"
                       "3306/tcp open   mysql       MySQL 5.5.62\n"
                       "3389/tcp open   ms-wbt-server\n"
                       "```\n"
                       "**你應該立刻看出五個問題**：\n"
                       "1. **23 Telnet 開著** → 明文帳密，直接關掉\n"
                       "2. **80 沒有 443** → 網站沒有加密\n"
                       "3. **Apache 2.2.15 / OpenSSH 7.4** → 版本極舊，有大量已知 CVE\n"
                       "4. **445 對外開放** → SMB 暴露，勒索病毒高風險\n"
                       "5. **3306 與 3389 對外** → 資料庫與遠端桌面應只走 VPN\n\n"
                       "**資安人員看掃描報告的方式：不是看有幾個 port，而是看「哪些不該在這裡」。**",
            "note": "考點技巧：題目給一組 port 問「最該優先處理哪個」— "
                    "答案通常是**明文協定**或**對網際網路開放的管理/資料庫服務**。",
        },
        {
            "heading": "為什麼明文協定必須淘汰",
            "body": "明文協定的問題不只是理論上可以被看，而是**實際上非常容易被看**：\n\n"
                    "- 同一 Wi-Fi 或同一 VLAN 內，配合 ARP 欺騙即可完整擷取\n"
                    "- 路徑上任何一台裝置（含被入侵的交換器）都能看到\n"
                    "- 憑證一次外洩，攻擊者就有了合法帳號 → 後續行為看起來完全正常，"
                    "**極難偵測**\n\n"
                    "**最常見的三個現實案例**：\n"
                    "1. **Telnet 管理網通設備**：許多機房交換器仍開 Telnet，一次抓包就拿到密碼。\n"
                    "2. **FTP 上傳檔案**：帳密與內容全部明文。\n"
                    "3. **SNMP v1/v2c**：community string 就是密碼且明文傳輸，"
                    "預設常常是 `public` / `private` — 攻擊者可讀出完整網路拓撲甚至改設定。",
            "example": "**用 tcpdump 看明文協定有多脆弱**：\n"
                       "```\n"
                       "$ sudo tcpdump -i eth0 -A -s 0 'tcp port 23'\n"
                       "...\n"
                       "User Access Verification\n"
                       "Username: admin\n"
                       "Password: Cisco123!\n"
                       "```\n"
                       "**帳號密碼完整出現在封包裡。** 同樣流量走 SSH 只會是加密亂碼。\n\n"
                       "**這個對比是說服主管換掉 Telnet 最有效的方式** — "
                       "在測試環境示範一次比講一百句都有用。",
            "note": "STARTTLS 的陷阱：它是「在明文連線上升級成加密」。"
                    "攻擊者可攔截並移除 STARTTLS 指令，讓連線退回明文 — 這叫 **SSL 剝離**。"
                    "所以應用一開始就加密的專用 port（465、993）或設強制加密政策。",
        },
        {
            "heading": "DNS：最容易被忽略的資安要角",
            "body": "DNS 幾乎參與每一次網路連線，所以它同時是**極佳的偵測點**與**極佳的攻擊管道**。\n\n"
                    "**攻擊面**：\n"
                    "- **DNS 快取毒化**：塞假紀錄把使用者導向惡意站台。對策是 **DNSSEC**。\n"
                    "- **DNS 隧道**：把資料編碼藏在網域查詢裡偷渡出去。"
                    "因為 DNS 幾乎不會被封鎖，這是很常用的外洩與 C2 管道。\n"
                    "- **DNS 放大攻擊**：偽造來源 IP 查詢開放解析器，讓大量回應打向受害者。\n"
                    "- **網域搶註**：註冊 `gooogle.com` 之類的相似網域做釣魚。\n\n"
                    "**防守方的機會**：\n"
                    "- 集中所有 DNS 查詢並記錄 → **一份 DNS 日誌就能看出大半惡意活動**\n"
                    "- 用 DNS 過濾（RPZ、Protective DNS）擋掉已知惡意網域 → 成本極低效果極好\n"
                    "- 監控異常：查詢量暴增、超長子網域、高熵值網域（DGA）",
            "example": "**DNS 隧道的偵測特徵**（SOC 實務）：\n"
                       "- 單一主機 DNS 查詢量遠高於同儕（每分鐘上百次）\n"
                       "- 網域名稱很長且像亂碼：`a3f9c2e1b8d7.tunnel.example.com`\n"
                       "- 大量 TXT / NULL 紀錄查詢（正常用戶很少查 TXT）\n\n"
                       "**對策**：只允許主機向內部 DNS 查詢（防火牆封鎖直接對外的 53），"
                       "在內部 DNS 做記錄與過濾。\n"
                       "同時要處理 **DoH 繞過問題** — 瀏覽器內建的 DoH 會跳過你的內部 DNS，"
                       "需用政策關閉。",
            "note": "考點：DNSSEC 提供**完整性與來源驗證**，但**不提供機密性**。"
                    "要機密性才需要 DoT/DoH。這兩個很常考混。",
        },
        {
            "heading": "服務盤點：把 port 清單變成風險清單",
            "body": "實務流程：\n\n"
                    "1. **盤點**：掃描全網段，列出所有開放 port 與服務版本。\n"
                    "2. **比對基準**：這台機器**應該**開哪些 port？多出來的就是問題。\n"
                    "3. **分級**：\n"
                    "   - 對網際網路開放的管理服務（RDP/SSH/資料庫）→ **立即處理**\n"
                    "   - 明文協定 → **高**\n"
                    "   - 版本過舊有已知 CVE → **依 CVSS 排序**\n"
                    "   - 內網不必要的服務 → **中**\n"
                    "4. **處置**：關閉、限制來源 IP、改用加密版本，或加補償控制。\n"
                    "5. **持續監控**：新開的 port 要有告警。\n\n"
                    "**關鍵心法：最好的防禦是「那個服務根本沒開」。**"
                    "關閉一個不需要的服務，比為它買一套防護產品有效得多。",
            "example": "**一份實用的服務基準表**：\n"
                       "```\n"
                       "角色          允許的 port           來源限制\n"
                       "──────────────────────────────────────────────\n"
                       "網頁伺服器    443/tcp               any\n"
                       "              22/tcp                10.10.99.0/24（管理網段）\n"
                       "資料庫伺服器  3306/tcp              10.10.30.0/24（僅應用層）\n"
                       "              22/tcp                10.10.99.0/24\n"
                       "員工電腦      無需對外開放          —\n"
                       "印表機        631/tcp, 9100/tcp     10.10.10.0/24\n"
                       "```\n"
                       "**任何偏離這張表的狀況都應該產生告警。**"
                       "這比「掃到什麼修什麼」有效得多，因為它是**白名單思維**。",
            "note": "工具建議：定期用 `nmap` 掃自己的網段並存檔，用 `ndiff` 比對差異 — "
                    "**新出現的 port 通常代表未經授權的變更或已被入侵**。",
        },
    ],
    "table": {
        "caption": "必背 port 完整表（依風險排序）",
        "head": ["Port", "協定", "用途", "風險", "處理建議"],
        "rows": [
            ["23", "Telnet", "遠端登入（明文）", "極高", "立即停用，改 SSH"],
            ["3389", "RDP", "Windows 遠端桌面", "極高", "絕不對外開放，僅走 VPN + MFA"],
            ["445", "SMB", "Windows 檔案共用", "極高", "封鎖對外，內網限制來源"],
            ["3306 / 1433 / 5432", "MySQL / MSSQL / PostgreSQL", "資料庫", "極高", "只綁內網或 127.0.0.1"],
            ["6379 / 27017", "Redis / MongoDB", "NoSQL", "極高", "預設常無認證，務必設密碼並隔離"],
            ["623", "IPMI / BMC", "伺服器帶外管理", "極高", "完全隔離於獨立管理網段"],
            ["21 / 20", "FTP", "檔案傳輸（明文）", "高", "改用 SFTP 或 FTPS"],
            ["161", "SNMP v1/v2c", "網路管理（明文）", "高", "升級 SNMPv3，改預設 community"],
            ["80", "HTTP", "網頁（明文）", "中", "重導至 443，啟用 HSTS"],
            ["25 / 110 / 143", "SMTP / POP3 / IMAP", "郵件（明文）", "中", "改 587+STARTTLS / 993 / 995"],
            ["389", "LDAP", "目錄服務（明文）", "中", "改 LDAPS 636"],
            ["22", "SSH", "加密遠端登入", "低（設定不當則高）", "禁 root、改金鑰、限制來源"],
            ["443", "HTTPS", "加密網頁", "低", "TLS 1.2+、正確憑證、安全標頭"],
            ["53", "DNS", "名稱解析", "特殊", "集中記錄、過濾惡意網域、監控隧道"],
        ],
    },
    "labs": [{
        "title": "盤點自己主機的服務並判讀風險",
        "goal": "把「開了哪些 port」變成「有哪些風險」。",
        "warn": "**只掃描自己的主機或你有書面授權的網段。未經授權掃描他人系統在台灣可能觸犯刑法第 358 條。**",
        "steps": [
            {"cmd": "ss -tulnp",
             "explain": "看本機所有監聽 port。**重點看綁定位址**："
                        "0.0.0.0 = 對所有網路開放，127.0.0.1 = 只有本機。",
             "output": "Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process\nudp   UNCONN 0      0      127.0.0.53:53       0.0.0.0:*         users:((\"systemd-resolve\",pid=623))\ntcp   LISTEN 0      128    0.0.0.0:22          0.0.0.0:*         users:((\"sshd\",pid=744))\ntcp   LISTEN 0      511    0.0.0.0:80          0.0.0.0:*         users:((\"nginx\",pid=812))\ntcp   LISTEN 0      511    0.0.0.0:443         0.0.0.0:*         users:((\"nginx\",pid=812))\ntcp   LISTEN 0      70     0.0.0.0:3306        0.0.0.0:*         users:((\"mysqld\",pid=901))\ntcp   LISTEN 0      4096   0.0.0.0:6379        0.0.0.0:*         users:((\"redis-server\",pid=955))\n# 問題：3306 和 6379 綁 0.0.0.0 → 對整個網路開放，應改綁 127.0.0.1"},
            {"cmd": "nmap -sV -p- --min-rate 1000 127.0.0.1",
             "explain": "掃描全部 65535 個 port 並偵測服務版本。`-sV` 抓版本是判斷有無已知 CVE 的關鍵。",
             "output": "Starting Nmap 7.94 ( https://nmap.org )\nNmap scan report for localhost (127.0.0.1)\nHost is up (0.000042s latency).\nNot shown: 65529 closed tcp ports (reset)\n\nPORT     STATE SERVICE  VERSION\n22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.4\n53/tcp   open  domain   (generic dns response)\n80/tcp   open  http     nginx 1.18.0 (Ubuntu)\n443/tcp  open  ssl/http nginx 1.18.0 (Ubuntu)\n3306/tcp open  mysql    MySQL 8.0.35\n6379/tcp open  redis    Redis key-value store 6.0.16\n\nService detection performed. 6 services on 1 host"},
            {"cmd": "redis-cli -h 127.0.0.1 ping",
             "explain": "**檢查 Redis 有沒有設密碼**。直接回 PONG 代表無認證 — 這是重大風險。",
             "output": "PONG\n# 警訊：無需密碼即可存取。應在 redis.conf 設 requirepass 並改綁 127.0.0.1"},
            {"cmd": "sudo grep -E '^(PermitRootLogin|PasswordAuthentication|Port|AllowUsers)' /etc/ssh/sshd_config",
             "explain": "檢查 SSH 加固設定。SSH 本身安全，但設定不當一樣危險。",
             "output": "Port 22\nPermitRootLogin yes\nPasswordAuthentication yes\n# 兩個問題：允許 root 直接登入、允許密碼登入（應改金鑰）"},
            {"cmd": "nmap -sV --script ssl-enum-ciphers -p 443 127.0.0.1",
             "explain": "檢查 TLS 設定：有沒有支援已淘汰的 SSLv3/TLS 1.0、有沒有弱加密套件。",
             "output": "PORT    STATE SERVICE\n443/tcp open  https\n| ssl-enum-ciphers:\n|   TLSv1.2:\n|     ciphers:\n|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A\n|   TLSv1.3:\n|     ciphers:\n|       TLS_AKE_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A\n|_  least strength: A\n# 良好：沒有 TLS 1.0/1.1，最弱強度為 A"},
            {"cmd": "sudo nmap -sn 192.168.1.0/24",
             "explain": "**主機探測**（不掃 port，只看誰活著）。找出「不該存在」的機器。",
             "output": "Nmap scan report for 192.168.1.1\nHost is up (0.0021s latency).\nMAC Address: 3C:37:86:1F:2A:B0 (Netgear)\nNmap scan report for 192.168.1.42\nHost is up.\nNmap scan report for 192.168.1.77\nHost is up (0.0043s latency).\nMAC Address: 08:00:27:AB:CD:EF (Oracle VirtualBox)\nNmap scan report for 192.168.1.201\nHost is up (0.031s latency).\nMAC Address: B8:27:EB:44:12:9A (Raspberry Pi Foundation)\nNmap done: 256 IP addresses (4 hosts up) scanned in 2.51 seconds\n# 出現一台不在資產清冊上的 Raspberry Pi → 需立即查明"},
        ],
    }],
    "quiz": [
        {"q": "掃描發現主機開放 23/tcp。最該優先處理的理由是？",
         "options": ["Telnet 佔用頻寬", "以明文傳輸帳號密碼，同網段即可完整擷取",
                     "版本太舊", "不支援 IPv6"],
         "answer": 1,
         "why": "明文協定的憑證一次外洩，攻擊者之後用合法帳號登入，行為看起來正常，極難偵測。"},
        {"q": "資料庫服務綁定在 0.0.0.0 代表什麼？",
         "options": ["只有本機能連", "對所有網路介面開放，任何能到達這台主機的人都可嘗試連線",
                     "已啟用加密", "已限制來源 IP"],
         "answer": 1,
         "why": "0.0.0.0 = 全部介面。資料庫應綁 127.0.0.1 或內部介面，並用防火牆限制來源。"},
        {"q": "DNSSEC 提供什麼保護？",
         "options": ["加密 DNS 查詢內容", "驗證 DNS 回應的來源與完整性，防快取毒化，但不加密內容",
                     "阻擋惡意網域", "加速解析"],
         "answer": 1,
         "why": "DNSSEC 是簽章機制 → 完整性 + 來源驗證。要機密性需要 DoT (853) 或 DoH。"},
        {"q": "某主機每分鐘產生數百筆超長且看似亂碼的子網域查詢。最可能是？",
         "options": ["正常瀏覽行為", "DNS 隧道，用於資料外傳或 C2 通訊", "DNS 伺服器故障", "DHCP 問題"],
         "answer": 1,
         "why": "DNS Tunneling 的典型特徵。對策是封鎖直接對外 53 並集中記錄。"},
        {"q": "SSL 剝離 (SSL Stripping) 攻擊利用了什麼弱點？",
         "options": ["加密演算法太弱", "STARTTLS 是從明文升級而來，攻擊者可移除升級指令讓連線退回明文",
                     "憑證過期", "DNS 未加密"],
         "answer": 1,
         "why": "機會式加密的通病。對策是使用專用加密 port（465/993/995）或強制加密 + HSTS。"},
        {"q": "以下哪組是「明文協定 → 加密替代」的正確配對？",
         "options": ["FTP 21 → SFTP 22", "HTTP 80 → HTTP 8080",
                     "Telnet 23 → Telnet 2323", "SNMP 161 → SNMP 162"],
         "answer": 0,
         "why": "SFTP 走 SSH (22)。注意 SFTP 建構於 SSH，FTPS (990) 是 FTP 加 TLS，兩者不同。"},
        {"q": "定期 nmap 掃描並用 ndiff 比對前後結果，主要目的是？",
         "options": ["測試網路速度", "發現新出現的開放 port，可能代表未授權變更或已被入侵",
                     "更新資產清冊格式", "驗證防火牆效能"],
         "answer": 1,
         "why": "變更偵測。新 port、新主機都是重要訊號，成本低效益高。"},
        {"q": "未設密碼的 Redis 主要風險是？",
         "options": ["效能下降", "攻擊者可寫入任意 key、甚至寫入 SSH 授權金鑰取得主機權限",
                     "資料會遺失", "不支援叢集"],
         "answer": 1,
         "why": "未認證 Redis 是知名入侵途徑（可透過寫檔功能植入 SSH key 或 cron）。"},
    ],
    "keywords": ["port", "Telnet", "SSH", "HTTP", "HTTPS", "FTP", "SMB", "RDP",
                 "SNMP", "DNS", "DNSSEC", "DNS 隧道", "SSL 剝離", "服務盤點", "nmap"],
    "takeaway": [
        "用「明文 → 加密」成對記憶 port，考試與實務都夠用。",
        "看掃描報告的重點不是有幾個 port，而是「哪些不該在這裡」。",
        "最好的防禦是那個服務根本沒開；DNS 日誌是成本最低的偵測來源。",
    ],
})

CH.append({
    "id": "n06",
    "title": "無線網路與封包分析",
    "subtitle": "Wi-Fi 加密演進、無線攻擊、Wireshark 實戰",
    "level": "進階",
    "minutes": 22,
    "summary": "無線網路把實體邊界變成電波，任何人在停車場都能接觸你的網路。封包分析則是驗證一切假設的最終手段。",
    "why": "有線網路要進來得先進大樓；**無線網路的訊號會穿牆到停車場**。"
           "所以 Wi-Fi 的安全設計必須假設「攻擊者已經在訊號範圍內」。"
           "封包分析就像**行車紀錄器** — 當你懷疑什麼，它給你事實而不是猜測。",
    "sections": [
        {
            "heading": "Wi-Fi 加密演進：為什麼一定要用 WPA2/WPA3",
            "body": "- **WEP（1999）**：已完全破解。RC4 加上太短的 IV（24 bit），**幾分鐘內就能破**。\n"
                    "- **WPA（2003）**：過渡方案，用 TKIP，也已不安全。\n"
                    "- **WPA2（2004）**：用 **AES-CCMP**，目前的最低標準。\n"
                    "  - **WPA2-Personal (PSK)**：共用一組密碼。問題：**所有人用同一把金鑰**，"
                    "離職員工還知道密碼；而且攻擊者可抓握手封包後離線暴力破解。\n"
                    "  - **WPA2-Enterprise (802.1X)**：每人用自己的帳號認證（RADIUS），"
                    "**每個 session 有獨立金鑰**。企業必須用這個。\n"
                    "- **WPA3（2018）**：改用 **SAE** 取代 PSK 握手，提供**前向保密**，"
                    "且**離線字典攻擊失效**。另有 OWE 為開放網路提供加密。\n\n"
                    "**結論**：家用 → WPA3 或 WPA2-AES + 長密碼（20 字以上）；"
                    "企業 → **WPA2/WPA3-Enterprise + 802.1X + 憑證驗證**。",
            "example": "**WPA2-PSK 的攻擊流程（理解防禦用）**：\n"
                       "1. 攻擊者監聽無線頻道，等待有人連線\n"
                       "2. 抓到 **4-way handshake** 封包\n"
                       "3. 拿回家用字典或 GPU 離線暴力破解\n"
                       "4. **不需要再接近你的網路** — 破解是離線進行的\n\n"
                       "**WPA3 為何解決了這件事**：SAE 握手不洩漏可離線破解的材料，"
                       "每次猜測都必須與 AP 互動，速度慢到不可行。\n\n"
                       "**企業版為何更好**：沒有共用密碼可抓，"
                       "離職員工帳號一停用就進不來，不必更改全公司 Wi-Fi 密碼。",
            "note": "考點：**WPS 一定要關閉**。8 位數 PIN 的設計缺陷讓有效搜尋空間降到約 11000 種，"
                    "幾小時內可破，會直接洩漏 WPA2 密碼。",
        },
        {
            "heading": "常見無線攻擊與對策",
            "body": "- **惡意 AP (Rogue AP)**：員工私接的無線基地台，在防火牆之外開了一個門。\n"
                    "  → 對策：無線入侵偵測 (WIDS)、交換器 port 綁定、802.1X\n\n"
                    "- **邪惡雙生 (Evil Twin)**：架一個 SSID 跟公司一樣的假 AP，訊號更強，"
                    "讓裝置自動連上去。\n"
                    "  → 對策：**憑證驗證的 802.1X**（假 AP 拿不出正確的伺服器憑證）、"
                    "在用戶端限定信任特定憑證\n\n"
                    "- **解除認證攻擊 (Deauth)**：偽造管理框架把使用者踢下線，迫使重新連線"
                    "（用來抓握手包或配合 Evil Twin）。\n"
                    "  → 對策：**802.11w (PMF)**，WPA3 強制啟用\n\n"
                    "- **KRACK（2017）**：攻擊 WPA2 的 4-way handshake 重放。\n"
                    "  → 對策：更新用戶端與 AP 韌體\n\n"
                    "- **Captive Portal 釣魚**：假登入頁面收集帳密。\n"
                    "  → 對策：使用者教育 + 不在公用 Wi-Fi 輸入公司憑證 + VPN",
            "example": "**咖啡廳的正確做法（給一般人的建議）**：\n"
                       "1. 假設所有公用 Wi-Fi 都被監聽\n"
                       "2. 只用 HTTPS 網站（檢查鎖頭）\n"
                       "3. 使用公司 VPN 或個人手機熱點\n"
                       "4. **關閉「自動連線至已知網路」**— 否則 Evil Twin 會自動接上\n"
                       "5. 關閉檔案共用\n\n"
                       "**給企業的建議**：訪客 Wi-Fi 完全獨立網段只能上網；"
                       "員工 Wi-Fi 用 WPA2/3-Enterprise + 裝置憑證；定期掃描 Rogue AP。",
            "note": "頻段考點：2.4GHz 穿透好但頻道少（1/6/11 不重疊）、"
                    "5GHz 頻道多速度快但穿透差、6GHz（Wi-Fi 6E）最乾淨。",
        },
        {
            "heading": "Wireshark：把猜測變成事實",
            "body": "封包分析的核心價值：**當所有人在猜，你可以拿出證據。**\n\n"
                    "**必會的顯示過濾器**：\n"
                    "```\n"
                    "ip.addr == 10.10.10.5                  # 特定主機所有流量\n"
                    "tcp.port == 443                        # 特定 port\n"
                    "http.request.method == \"POST\"          # 只看 POST\n"
                    "dns                                    # 只看 DNS\n"
                    "tcp.flags.syn==1 && tcp.flags.ack==0   # 只看連線嘗試（找掃描）\n"
                    "tcp.analysis.retransmission            # 重傳（網路品質問題）\n"
                    "arp.duplicate-address-detected         # 找 ARP 欺騙\n"
                    "tls.handshake.type == 1                # TLS Client Hello（看 SNI）\n"
                    "http.response.code >= 400              # 錯誤回應\n"
                    "!(arp || icmp || dns)                  # 排除雜訊\n"
                    "```\n\n"
                    "**注意區分兩種過濾器**：\n"
                    "- **擷取過濾器**：用 BPF 語法，抓之前就決定要不要存 → `tcp port 443`\n"
                    "- **顯示過濾器**：用 Wireshark 語法，抓完之後篩選 → `tcp.port == 443`\n"
                    "**語法不同，很常搞混。**",
            "example": "**用 Wireshark 調查「這台電腦是不是中毒了」的流程**：\n\n"
                       "1. **看它連去哪裡**：`Statistics → Conversations → IPv4`，依流量排序。"
                       "陌生國外 IP、大量小封包持續連線 = 可疑 C2。\n"
                       "2. **看 DNS 查了什麼**：過濾 `dns`，檢查有無高熵值網域（DGA）。\n"
                       "3. **看 TLS 連到哪些網站**：過濾 `tls.handshake.type == 1` 看 SNI。"
                       "**就算內容加密，目的地網域仍是明文。**\n"
                       "4. **看時間規律**：C2 心跳通常**間隔非常固定**（例如每 60 秒），"
                       "人類行為不會這麼規律。\n"
                       "5. **看 JA3 指紋**：不同 TLS 用戶端有不同握手特徵，可識別惡意程式函式庫。\n\n"
                       "**這五步就是網路取證的基本流程。**",
            "note": "**法律與隱私提醒**：擷取網路流量會看到同事的個資與通訊內容。"
                    "在企業環境必須有明確授權、記錄目的、限定範圍與保存期限。"
                    "台灣涉及《個人資料保護法》與《通訊保障及監察法》，"
                    "**未經授權擷取他人通訊可能構成刑責**。",
        },
        {
            "heading": "從封包看出攻擊的樣態",
            "body": "把常見攻擊的**封包特徵**記下來，就能在流量裡認出它們：\n\n"
                    "- **port 掃描**：單一來源 → 同一目標的**大量不同 port**，只有 SYN 沒有完整交握\n"
                    "- **主機掃描**：單一來源 → **大量不同 IP** 的同一個 port\n"
                    "- **SYN Flood**：巨量 SYN、來源 IP 隨機分散、沒有後續 ACK\n"
                    "- **ARP 欺騙**：同一 MAC 宣稱多個 IP、沒人問卻不斷發送 ARP Reply\n"
                    "- **暴力破解**：對同一服務**高頻率**的連線與認證失敗\n"
                    "- **資料外洩**：**上傳量遠大於下載量**（正常使用者相反）、長時間持續外傳\n"
                    "- **C2 心跳**：極規律的固定間隔、小封包、目的地為陌生 IP 或剛註冊的網域\n"
                    "- **DNS 隧道**：超長子網域、大量 TXT 查詢、單一主機查詢量爆增\n"
                    "- **橫向移動**：內網主機之間出現不尋常的 445/3389/5985 連線",
            "example": "**基準線 (Baseline) 的重要性**：\n\n"
                       "上面所有「異常」都是**相對於正常狀態**才有意義。"
                       "所以真正的實務第一步是：**在平常沒事的時候先記錄一份正常流量的樣貌**。\n"
                       "- 每台伺服器平常和誰通訊？\n"
                       "- 每天的流量高低峰在什麼時間？\n"
                       "- 平常會出現哪些協定？\n\n"
                       "**沒有基準線，你永遠不知道什麼叫異常。**"
                       "這也是 SIEM 與 UEBA（使用者行為分析）的核心原理。",
            "note": "延伸工具：**Zeek** 把封包轉成結構化日誌，適合長期保存與大規模分析；"
                    "**Suricata** 是 IDS/IPS，可用規則即時偵測。"
                    "Wireshark 適合深入單一事件，Zeek/Suricata 適合持續監控。",
        },
    ],
    "table": {
        "caption": "Wi-Fi 加密標準對照",
        "head": ["標準", "年份", "加密", "握手", "安全性", "建議"],
        "rows": [
            ["WEP", "1999", "RC4 + 24bit IV", "—", "已完全破解", "絕對不用"],
            ["WPA", "2003", "TKIP", "4-way", "已不安全", "不用"],
            ["WPA2-Personal", "2004", "AES-CCMP", "4-way (PSK)", "可離線破解密碼", "僅家用，密碼要長"],
            ["WPA2-Enterprise", "2004", "AES-CCMP", "802.1X + RADIUS", "良好", "企業標準"],
            ["WPA3-Personal", "2018", "AES-CCMP/GCMP", "SAE", "抗離線破解、前向保密", "推薦"],
            ["WPA3-Enterprise", "2018", "GCMP-256（192bit 模式）", "802.1X", "最高", "高敏感環境"],
        ],
    },
    "labs": [{
        "title": "用 tshark 做基本流量分析",
        "goal": "不開 GUI 也能做封包分析，並找出可疑樣態。",
        "warn": "**只擷取你自己的裝置或有明確授權的網路。擷取他人通訊在台灣可能違反《通訊保障及監察法》。**",
        "steps": [
            {"cmd": "sudo tshark -D",
             "explain": "列出可擷取的介面，確認要監聽哪一個。",
             "output": "1. eth0\n2. wlan0\n3. any\n4. lo (Loopback)\n5. bluetooth0"},
            {"cmd": "sudo tshark -i eth0 -f 'udp port 53' -c 6 -T fields -e ip.src -e dns.qry.name",
             "explain": "**擷取過濾器**（-f，BPF 語法）只抓 DNS，輸出來源 IP 與查詢網域。"
                        "這是找惡意網域最快的方式。",
             "output": "10.10.10.5\twww.google.com\n10.10.10.5\tfonts.googleapis.com\n10.10.10.5\tapi.github.com\n10.10.10.5\ta3f9c2e1b8d7f4a2.cdn-update.top\n10.10.10.5\tb7e2d1c9a8f3e5b1.cdn-update.top\n10.10.10.5\tc1d8e7f2a3b9c4d6.cdn-update.top\n# 後三筆：高熵值子網域 + 陌生 TLD → 疑似 DGA 或 DNS 隧道"},
            {"cmd": "sudo tshark -i eth0 -Y 'tcp.flags.syn==1 && tcp.flags.ack==0' -c 12 -T fields -e ip.src -e ip.dst -e tcp.dstport",
             "explain": "**顯示過濾器**（-Y，Wireshark 語法）只看連線嘗試。"
                        "同來源打很多不同 port = 掃描。",
             "output": "203.0.113.9\t10.10.10.5\t21\n203.0.113.9\t10.10.10.5\t22\n203.0.113.9\t10.10.10.5\t23\n203.0.113.9\t10.10.10.5\t25\n203.0.113.9\t10.10.10.5\t80\n203.0.113.9\t10.10.10.5\t443\n203.0.113.9\t10.10.10.5\t445\n203.0.113.9\t10.10.10.5\t3306\n203.0.113.9\t10.10.10.5\t3389\n203.0.113.9\t10.10.10.5\t5432\n203.0.113.9\t10.10.10.5\t6379\n203.0.113.9\t10.10.10.5\t8080\n# 單一來源循序掃 12 個常見 port = 典型 port 掃描"},
            {"cmd": "tshark -r capture.pcap -q -z conv,tcp",
             "explain": "**流量統計**：看誰跟誰講最多話，找出異常的大量外傳。",
             "output": "TCP Conversations\n                                       |    <-     | |    ->     | |   Total   |\n                                       | Frames Bytes| | Frames Bytes| | Frames Bytes|\n10.10.10.5:51422 <-> 93.184.216.34:443   1204  1.1MB     892   84kB    2096  1.2MB\n10.10.10.5:51501 <-> 185.220.101.44:9001   88    9kB   14209 18.4MB   14297 18.4MB\n10.10.10.5:51436 <-> 142.250.76.100:443   412  402kB     301   28kB     713  430kB\n# 第二筆：上傳 18.4MB 遠大於下載 9kB → 高度疑似資料外洩"},
            {"cmd": "tshark -r capture.pcap -Y 'tls.handshake.type==1' -T fields -e ip.dst -e tls.handshake.extensions_server_name",
             "explain": "即使流量加密，**TLS SNI 仍是明文**，可看出連到哪些網域。",
             "output": "93.184.216.34\texample.com\n142.250.76.100\twww.google.com\n185.220.101.44\tupdate-service.duckdns.org\n# duckdns.org 是免費動態 DNS，常被 C2 使用 → 需調查"},
            {"cmd": "tshark -r capture.pcap -Y 'arp.duplicate-address-detected' -c 5",
             "explain": "直接找 ARP 欺騙。Wireshark 內建偵測重複位址。",
             "output": "  231  12.418  08:00:27:ab:cd:ef -> ff:ff:ff:ff:ff:ff  ARP 42 192.168.1.1 is at 08:00:27:ab:cd:ef (duplicate use of 192.168.1.1 detected!)\n  245  13.522  08:00:27:ab:cd:ef -> ff:ff:ff:ff:ff:ff  ARP 42 192.168.1.1 is at 08:00:27:ab:cd:ef (duplicate use of 192.168.1.1 detected!)\n# 確認正在遭受 ARP 欺騙攻擊"},
            {"cmd": "tshark -r capture.pcap -q -z io,stat,60,'COUNT(tcp.flags.syn)tcp.flags.syn==1'",
             "explain": "以 60 秒為區間統計 SYN 數量，找時間規律 — 固定間隔是 C2 心跳的特徵。",
             "output": "| IO Statistics                        |\n| Interval size: 60 secs               |\n|--------------------------------------|\n| Interval   |  COUNT(tcp.flags.syn)   |\n|--------------------------------------|\n|   0 <>  60 |          61             |\n|  60 <> 120 |          60             |\n| 120 <> 180 |          60             |\n| 180 <> 240 |          61             |\n# 每分鐘幾乎固定 60 次 → 每秒一次的規律連線，人類行為不會如此規律"},
        ],
    }],
    "quiz": [
        {"q": "WPA2-PSK 的主要弱點是什麼？",
         "options": ["加密演算法太弱", "攻擊者可擷取 4-way handshake 後離線暴力破解密碼",
                     "不支援 AES", "無法用於企業"],
         "answer": 1,
         "why": "破解是離線進行的，攻擊者抓到握手包後就可以離開現場慢慢破。WPA3 的 SAE 解決了這點。"},
        {"q": "為什麼 WPA2/WPA3-Enterprise 比 Personal 更適合企業？",
         "options": ["速度更快", "每位使用者獨立認證且有獨立 session 金鑰，離職只需停用帳號",
                     "不需要密碼", "支援更多裝置"],
         "answer": 1,
         "why": "Personal 是全員共用一把 PSK，離職員工仍知道密碼，要換就得全公司重設。"},
        {"q": "「邪惡雙生 (Evil Twin)」最有效的技術對策是？",
         "options": ["提高 Wi-Fi 密碼複雜度", "使用有伺服器憑證驗證的 802.1X 並在用戶端限定信任憑證",
                     "隱藏 SSID", "降低 AP 發射功率"],
         "answer": 1,
         "why": "假 AP 無法提供正確的 RADIUS 伺服器憑證。隱藏 SSID 幾乎沒有防護效果。"},
        {"q": "802.11w (PMF) 主要防禦哪種攻擊？",
         "options": ["離線密碼破解", "解除認證 (Deauth) 攻擊", "ARP 欺騙", "DNS 毒化"],
         "answer": 1,
         "why": "PMF 為管理框架提供完整性保護，攻擊者無法偽造 deauth 踢人下線。WPA3 強制啟用。"},
        {"q": "WPS 為什麼必須關閉？",
         "options": ["會降低速度", "8 位數 PIN 的設計缺陷使有效搜尋空間大幅縮小，數小時可破並取得 WPA2 密碼",
                     "不支援 WPA3", "造成頻道干擾"],
         "answer": 1,
         "why": "WPS PIN 被分成兩段分別驗證且最後一位是檢查碼，有效組合降到約 11000 種。"},
        {"q": "`tcp port 443`（擷取過濾器）與 `tcp.port == 443`（顯示過濾器）的差別？",
         "options": ["完全相同", "前者用 BPF 在擷取時決定是否儲存；後者用 Wireshark 語法在擷取後篩選",
                     "前者較慢", "後者只能用於 UDP"],
         "answer": 1,
         "why": "擷取過濾器省磁碟空間但漏掉的永遠沒了；顯示過濾器保留全部資料但檔案較大。"},
        {"q": "某主機流量顯示「上傳 18MB、下載 9KB」且目的地是陌生 IP。最可能是？",
         "options": ["正常雲端備份", "資料外洩或已被入侵後的資料外傳", "軟體更新", "DNS 查詢"],
         "answer": 1,
         "why": "正常使用者下載量通常遠大於上傳量。上傳遠大於下載且目的地陌生是外洩的典型指標。"},
        {"q": "即使流量已用 TLS 加密，仍可從封包看出下列哪一項？",
         "options": ["網頁內容", "使用者密碼", "連線的目的網域（TLS SNI 為明文）", "資料庫查詢語句"],
         "answer": 2,
         "why": "SNI 在 Client Hello 中是明文，是 SOC 的重要偵測來源。ECH 正在改變這點。"},
        {"q": "為什麼建立流量基準線是異常偵測的前提？",
         "options": ["為了計算頻寬費用", "所有異常判斷都是相對於正常狀態，沒有基準就無法定義異常",
                     "法規要求", "為了提升網速"],
         "answer": 1,
         "why": "同樣行為在不同環境可能正常或異常。基準線是 SIEM 與 UEBA 能運作的基礎。"},
    ],
    "keywords": ["WEP", "WPA2", "WPA3", "SAE", "802.1X", "Evil Twin", "Rogue AP",
                 "Deauth", "PMF", "WPS", "Wireshark", "tshark", "顯示過濾器",
                 "SNI", "基準線", "Zeek", "Suricata"],
    "takeaway": [
        "企業無線必須用 WPA2/3-Enterprise + 802.1X 憑證驗證，Personal 只適合家用。",
        "Wireshark 的價值是把猜測變成證據；擷取過濾器與顯示過濾器語法不同。",
        "所有異常偵測都建立在基準線之上 — 先知道什麼是正常，才認得出異常。",
    ],
})

TRACK = {
    "id": "t2-network",
    "title": "網路基礎",
    "code": "Network+ N10-009 · CCNA 200-301",
    "stage": 1,
    "stageName": "第一階段 · 打底",
    "color": "teal",
    "tagline": "所有攻擊與防禦都發生在網路上。這是整個資安的地基。",
    "goal": "看得懂封包怎麼跑、會算子網、知道 VLAN 與路由怎麼設、能用 Wireshark 找出異常流量。",
    "chapters": CH,
}
