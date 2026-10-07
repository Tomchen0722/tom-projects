#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Local Civil Service Level 4 (地方特考四等) Question Bank Part 3 (80 questions).
Categories:
1. 網路模型、實體層與鏈結層 (OSI/TCP-IP, 乙太網, VLAN, STP) (27 questions)
2. 網路層與傳輸層協定 (IPv4/IPv6, CIDR, ARP, ICMP, TCP/UDP) (27 questions)
3. 網路服務、路由協定、無線網路與 VPN 遠端辦公 (NAT, DNS, DHCP, Wi-Fi, VPN) (26 questions)
"""

def get_local4_part3_questions():
    qs = []

    # Dataset 1: 網路模型、實體層與鏈結層 (27 questions)
    data1 = [
        ("在 OSI 七層網路架構模型中，當應用程式資料由頂層向下逐層封裝傳輸時，各層所處理之通訊協定資料單元（PDU）名稱，下列對應何者完全正確？",
         "傳輸層（Transport）➔ 區段（Segment）；網路層（Network）➔ 封包（Packet）；資料鏈結層（Data Link）➔ 訊框（Frame）",
         ["傳輸層（Transport）➔ 區段（Segment）；網路層（Network）➔ 封包（Packet）；資料鏈結層（Data Link）➔ 訊框（Frame）",
          "傳輸層 ➔ 訊框；網路層 ➔ 位元；資料鏈結層 ➔ 封包",
          "傳輸層 ➔ 封包；網路層 ➔ 區段；資料鏈結層 ➔ 檔案",
          "所有層級之 PDU 一律統稱為位元組（Byte）"],
         "OSI 七層模型 PDU 名稱規範：1. 應用層/展示層/會議層：資料（Data / Message）；2. 傳輸層（Layer 4）：區段（Segment，TCP）或資料包（Datagram，UDP）；3. 網路層（Layer 3）：封包（Packet）；4. 資料鏈結層（Layer 2）：訊框（Frame）；5. 實體層（Layer 1）：位元流（Bits）。向下傳輸時每層加上該層表頭（Header），解封裝時逆向拆除。"),

        ("在乙太網路（Ethernet）實體線路規格中，某區公所新建機房佈設 Cat.6 雙絞線（Twisted Pair），若在標準 10GBASE-T 規格下傳輸 10Gbps 高速頻寬，其無中繼之最大有效傳輸距離限制約為？",
         "約 55 公尺（若改採 Cat.6A 則可達到標準的 100 公尺）",
         ["約 55 公尺（若改採 Cat.6A 則可達到標準的 100 公尺）",
          "約 1,000 公尺",
          "約 10 公尺",
          "無距離限制，可跨縣市傳輸"],
         "雙絞線規格與傳輸距離：乙太網路標準最大通道長度通常為 100 公尺（90m 水平纜線 + 10m 跳線）。在 10Gbps（10GBASE-T）高速傳輸下，Cat.6 由於內部串音干擾較大，在未經加強隔離下僅能保證傳輸 37~55 公尺；若需在 10Gbps 下達到完整 100 公尺長度，必須採購具備更嚴格防外來串音（Alien Crosstalk）之 Cat.6A（Augmented）或 Cat.7 遮蔽雙絞線。"),

        ("在 RJ-45 網路線接頭壓接標準中，若線路兩端一端採用 T568A 接線順序，另一端採用 T568B 接線順序，此條網路線被稱為？",
         "跳線 / 交叉線（Crossover Cable）",
         ["跳線 /交叉線（Crossover Cable）",
          "直通線（Straight-through Cable）",
          "反轉線（Rollover Console Cable）",
          "同軸電纜線"],
         "T568A vs T568B 與線材類型：T568A 顏色順序為：白綠、綠、白橙、藍、白藍、橙、白棕、棕；T568B 為：白橙、橙、白綠、藍、白藍、綠、白棕、棕。若兩端同為 T568B 稱為「直通線」（連接異質設備如 PC 連 Switch）；若一端 A 一端 B 稱為「跳線」（連接同質設備如 Switch 連 Switch、PC 連 PC）。現代網路設備普遍具備 Auto-MDIX 功能，可自動辨識線路類型。"),

        ("標準乙太網路媒體存取控制位址（MAC Address）之長度為多少個位元組？其中前半段 24 位元代表之意義為？",
         "長度為 6 個位元組（48 位元）；前半段 24 位元為 IEEE 分配給網卡製造商的「組織唯一識別碼（OUI, Organizationally Unique Identifier）」",
         ["長度為 6 個位元組（48 位元）；前半段 24 位元為 IEEE 分配給網卡製造商的「組織唯一識別碼（OUI, Organizationally Unique Identifier）」",
          "長度為 4 個位元組（32 位元）；前半段 16 位元為國家代碼",
          "長度為 16 個位元組（128 位元）；前半段 64 位元為路由器 IP",
          "長度為 8 個位元組（64 位元）；前半段為使用者身分證字號"],
         "MAC 位址結構解析：MAC 位址為 Layer 2 實體燒錄位址（BIA）。共 48 位元（6 Bytes），通常以 12 位十六進位表示（如 <code>00:1A:2B:3C:4D:5E</code>）。前 24 位元（3 Bytes）為 OUI（由 IEEE 統一核發給 Intel、Realtek、Cisco 等晶片廠商）；後 24 位元由廠商自行流水編號配置給每張網卡，理論上全球唯一。"),

        ("在半雙工傳統乙太網路中，為解決多台主機共享同一條傳輸媒介時可能發生的訊號碰撞問題，資料鏈結層採用之通訊協定為？",
         "CSMA/CD（載波感測多重存取/碰撞偵測，Carrier Sense Multiple Access with Collision Detection）",
         ["CSMA/CD（載波感測多重存取/碰撞偵測，Carrier Sense Multiple Access with Collision Detection）",
          "CSMA/CA（載波感測多重存取/碰撞避免）",
          "權標環（Token Ring）",
          "純 ALOHA 隨機廣播協定"],
         "CSMA/CD 運作口訣：1. 先聽後送（Carrier Sense）：發送前先監聽通道，若有訊號則等待；2. 邊送邊聽（Collision Detection）：發送資料時持續監聽電壓變化；3. 碰撞停送：一旦偵測到電壓異常代表發生碰撞，立即停止發送並發送壅塞信號（Jam Signal）強化碰撞讓所有人知曉；4. 隨機重送：採用「二元指數退避演算法（Binary Exponential Backoff）」隨機延遲後重試。全雙工交換式網路已無此需求。"),

        ("比較網路設備「集線器（Hub）」與「第二層交換器（Layer 2 Switch）」在網域劃分上之根本差異，下列敘述何者完全正確？",
         "集線器上所有連接埠共享同一個碰撞網域（Collision Domain）；交換器之每個獨立連接埠各自形成一個獨立的碰撞網域，大幅消除封包碰撞",
         ["集線器上所有連接埠共享同一個碰撞網域（Collision Domain）；交換器之每個獨立連接埠各自形成一個獨立的碰撞網域，大幅消除封包碰撞",
          "集線器能隔離廣播網域，交換器不行",
          "集線器具備 MAC 位址學習表，交換器僅盲目廣播",
          "兩者完全相同，僅為不同廠牌稱呼"],
         "Hub vs Switch 網域隔離：1. Hub（實體層 Layer 1）：純訊號中繼器，任一埠輸入之訊號無條件廣播複製至所有其餘連接埠，所有連接埠共用頻寬且處於同一個「碰撞網域」與同一個「廣播網域」；2. Switch（資料鏈結層 Layer 2）：基於 ASIC 硬體查表轉發，每個埠各自獨立，全雙工運作且互不干擾（隔絕碰撞網域），但預設情況下所有連接埠仍處於同一個「廣播網域」。"),

        ("當 Layer 2 交換器剛開機、其內部 MAC 位址表（CAM Table）尚為全空狀態時，若自 Port 1 收到一個「目的 MAC 位址為未知單播（Unknown Unicast）」之訊框，交換器之標準轉發動作為？",
         "學習（Learning）來源 MAC 與 Port 1 的對應關係，並將該訊框自「除了 Port 1 以外的所有其他連接埠全數泛洪廣播出去（Flooding）」",
         ["學習（Learning）來源 MAC 與 Port 1 的對應關係，並將該訊框自「除了 Port 1 以外的所有其他連接埠全數泛洪廣播出去（Flooding）」",
          "直接丟棄（Drop）該訊框並發送報警簡訊",
          "將該訊框原封不動自 Port 1 彈回發送端",
          "暫停交換器運作 10 分鐘等待管理員手動設定"],
         "交換器三大轉發行為：1. 學習（Learning）：檢查進來訊框的「來源 MAC」，若表中無該筆紀錄則記入 CAM 表；2. 轉發/過濾（Forwarding/Filtering）：若「目的 MAC」已在表中且在不同埠，精確單播轉發；若目的 MAC 就在同一個輸入埠則過濾丟棄；3. 泛洪（Flooding）：若目的 MAC 為未知的單播（Unknown Unicast）或廣播訊框（<code>FF:FF:FF:FF:FF:FF</code>），則向所有其他連接埠氾濫廣播。"),

        ("地方政府行政大樓內部將民政局、財政局與社會局連接至同一台實體交換器，為防止業務廣播風暴互相干擾並落實網路安全隔離，應在交換器上配置何種技術？",
         "虛擬區域網路（VLAN, Virtual Local Area Network, IEEE 802.1Q）",
         ["虛擬區域網路（VLAN, Virtual Local Area Network, IEEE 802.1Q）",
          "超執行緒技術（Hyper-Threading）",
          "網路時鐘同步協定（NTP）",
          "動態網域名稱解析（DDNS）"],
         "VLAN（虛擬區域網路）核心效益：VLAN 在 Layer 2 交換器內部將實體交換器邏輯切割為多個獨立的虛擬交換器。1. 隔離廣播網域（Broadcast Domain）：單一局處的廣播封包（如 ARP 請求）被限制在該 VLAN 內部，不會泛洪干擾其他局處；2. 強化橫向安全：不同 VLAN 之間的電腦在二層完全不通，若需跨 VLAN 互通必須經過 Layer 3 路由器或防火牆實施安全檢驗與存取控制。"),

        ("在 IEEE 802.1Q VLAN 訊框標籤（VLAN Tag）標準中，標籤內部用以標識 VLAN 編號之「VLAN ID（VID）」欄位長度為多少位元？理論上最多可劃分多少個 VLAN？",
         "長度為 12 位元，最多可劃分 4,096（$2^{12}$）個 VLAN（VID 範圍 0~4095）",
         ["長度為 12 位元，最多可劃分 4,096（$2^{12}$）個 VLAN（VID 範圍 0~4095）",
          "長度為 8 位元，最多可劃分 256 個 VLAN",
          "長度為 16 位元，最多可劃分 65,536 個 VLAN",
          "長度為 4 位元，最多可劃分 16 個 VLAN"],
         "802.1Q Tag 欄位結構：在原始乙太網訊框的來源 MAC 與 Type 欄位之間插入 4 個位元組的 802.1Q Tag。包含：1. TPID（2 Bytes，固定為 <code>0x8100</code> 標明為 Tagged 訊框）；2. TCI（2 Bytes）：包含 3-bit PCP（802.1p QoS 優先權）、1-bit DEI/CFI（丟棄合格指示）以及 12-bit VID（VLAN ID）。12 位元可表示 4096 個數值，其中 0 與 4095 為保留值，有效可用 VLAN 範圍為 1 至 4094。"),

        ("在跨交換器傳輸多個 VLAN 流量之骨幹網路鏈路（Trunk Link）中，交換器連接埠之型態應設定為？",
         "Trunk 埠（幹線埠），負責在封包上添加或識別 802.1Q 標籤並承載多個 VLAN 之流量",
         ["Trunk 埠（幹線埠），負責在封包上添加或識別 802.1Q 標籤並承載多個 VLAN 之流量",
          "Access 埠（存取埠），僅能連接單一電腦且封包不帶標籤",
          "Console 埠",
          "AUX 輔助埠"],
         "Access 埠 vs Trunk 埠：1. Access Port：連接一般終端電腦、印表機。該埠僅屬於單一特定 VLAN，終端設備發送的原生訊框進入時被打上該 VLAN 標籤，發送給終端電腦前標籤被剝除（Untagged）；2. Trunk Port：連接交換器與交換器、或交換器與路由器。允許多個不同 VLAN 的訊框通過，封包在線路上攜帶 802.1Q Tag（Tagged），對端交換器藉由標籤辨識該訊框應歸屬於哪一個 VLAN。"),

        ("在地方政府複雜的區域網路佈線中，若管理員不慎將兩台交換器之間以多條實體網路線交叉迴路連接，在缺乏防護下會引發交換器 CAM 表震盪並癱瘓全網之嚴重災難，該災難稱為？",
         "廣播風暴（Broadcast Storm）",
         ["廣播風暴（Broadcast Storm）",
          "太陽黑子干擾",
          "光纖熔接不良",
          "作業系統記憶體碎片"],
         "廣播風暴成因：Layer 2 訊框之表頭中「沒有 TTL（存活時間計數器）」。當網路拓撲存在環路（Loop）時，一個 ARP 廣播封包進入交換器會被泛洪至所有埠；對端交換器收到後又泛洪回來，在環路中無休止地倍增循環複製。幾秒鐘內鏈路頻寬被垃圾廣播封包 100% 塞爆，交換器 CPU 衝上 100%，整個機關所有電腦完全無法上網。"),

        ("為防止上述第二層網路環路並自動修剪無迴圈之樹狀拓撲，交換器必須啟用的標準生成樹協定為？",
         "STP（生成樹協定，IEEE 802.1D / 快速生成樹 RSTP IEEE 802.1w）",
         ["STP（生成樹協定，IEEE 802.1D / 快速生成樹 RSTP IEEE 802.1w）",
          "BGP（邊界閘道協定）",
          "OSPF（開放最短路徑優先）",
          "SNMP（簡單網路管理協定）"],
         "STP（生成樹協定）運作原理：Radia Perlman 發明。所有交換器定期互傳 BPDU（橋接器協定資料單元），依據最小 Bridge ID 選出「根橋接器（Root Bridge）」；隨後各交換器計算至 Root 的最短路徑開銷，選定 Root Port 與 Designated Port，將多餘形成環路的備援鏈路連接埠置於「阻塞狀態（Blocking / Discarding）」。當主要鏈路斷線時，阻塞埠自動啟用復原，兼顧防迴圈與冗餘備援。"),

        ("在區域網路骨幹中，地方政府為將兩台核心交換器之間的 2 條 1Gbps 實體線路綑綁合併為一條邏輯鏈路，達成 2Gbps 頻寬倍增與斷線負載切換，應設定何種鏈路聚合協定？",
         "LACP（鏈路聚合控制協定，IEEE 802.3ad / IEEE 802.1AX）",
         ["LACP（鏈路聚合控制協定，IEEE 802.3ad / IEEE 802.1AX）",
          "HDLC 協定",
          "PPP 協定",
          "SLIP 協定"],
         "LACP（鏈路聚合）：將多條實體乙太網鏈路綑綁為單一邏輯通道（Port Channel / Link Aggregation Group, LAG）。核心優勢：1. 頻寬累加（如 4 條 1G 形成 4G 邏輯頻寬）；2. 負載平衡（基於來源/目的 IP 或 MAC 雜湊分流）；3. 容錯備援（任一條實體線路斷裂，流量毫秒級自動由其餘線路承載，業務不中斷且 STP 不會將其視為環路阻斷）。"),

        ("在 OSI 七層網路模型中，負責資料格式轉換（如 EBCDIC 與 ASCII 碼互換）、圖形影像編碼解碼（JPEG/PNG）以及資料加解密與資料壓縮之層級為？",
         "展示層（Presentation Layer, 第 6 層）",
         ["展示層（Presentation Layer, 第 6 層）",
          "應用層（Application Layer, 第 7 層）",
          "會議層（Session Layer, 第 5 層）",
          "傳輸層（Transport Layer, 第 4 層）"],
         "OSI 展示層功能：展示層處理資料的語法（Syntax）與語意（Semantics）。核心職責：1. 資料格式轉譯（如不同作業系統字元集編碼轉換）；2. 資料加密與解密（如早期的加密展示標準）；3. 資料壓縮與解壓縮（降低傳輸所需位元數）。"),

        ("在 OSI 模型之會議層（Session Layer, 第 5 層）中，其核心管理功能為？",
         "建立、管理、維護與終止不同主機應用程式之間的對話連線（Session），並在資料流中插入檢查點（Checkpoints）以支援斷線後的同步復原",
         ["建立、管理、維護與終止不同主機應用程式之間的對話連線（Session），並在資料流中插入檢查點（Checkpoints）以支援斷線後的同步復原",
          "負責光纖線路中光脈衝的調變與解調變",
          "為每個資料封包計算 CRC-32 校驗碼",
          "在路由器之間計算最佳傳輸路徑"],
         "會議層對話管理：會議層負責對話控制（半雙工或全雙工交替）。其最著名的機制為「同步檢查點（Synchronization / Checkpoints）」。例如在傳輸一個 100MB 的大型檔案時，每 10MB 插入一個檢查點；若傳輸至 55MB 時網路中斷，連線重建後只需自第 50MB 檢查點接續傳輸，無需從頭重傳。"),

        ("在光纖網路佈線規格中，比較「單模光纖（SMF）」與「多模光纖（MMF）」之物理特性，下列敘述何者完全正確？",
         "單模光纖纖芯極細（約 9μm），使用雷射作為光源，無模態色散，傳輸距離遠（可達數十公里）；多模光纖纖芯較粗（50/62.5μm），使用 LED 作為光源，模態色散大，傳輸距離較短（數百公尺）",
         ["單模光纖纖芯極細（約 9μm），使用雷射作為光源，無模態色散，傳輸距離遠（可達數十公里）；多模光纖纖芯較粗（50/62.5μm），使用 LED 作為光源，模態色散大，傳輸距離較短（數百公尺）",
          "多模光纖傳輸距離遠大於單模光纖，常跨海纜使用",
          "單模光纖只能傳送黑白訊號，多模光纖可傳送彩色訊號",
          "多模光纖內部為實體銅線，單模光纖內部為石英玻璃"],
         "單模 vs 多模光纖辨析：1. 單模光纖（Single Mode Fiber, SMF）：芯徑 9μm，光信號以單一角度直線傳播，消除模態色散（Modal Dispersion），搭配高功率半導體雷射（LD），衰減極小，用於跨縣市、跨機房骨幹（黃色外被）；2. 多模光纖（Multi-Mode Fiber, MMF）：芯徑 50μm 或 62.5μm，多種光路模式全反射傳播，色散大，距離限於機房內部數百公尺（橘色或水藍色外被）。"),

        ("網路管理員使用 Wireshark 進行網路封包側錄與排錯時，必須將網路介面卡設定為下列何種運作模式，方能接收「區域網路上非發送給本機的所有廣播、群播與單播訊框」？",
         "混雜模式 / 混雜監聽模式（Promiscuous Mode）",
         ["混雜模式 / 混雜監聽模式（Promiscuous Mode）",
          "安全隱形模式（Stealth Mode）",
          "省電睡眠模式（Power Saving Mode）",
          "單播專用模式（Unicast-Only Mode）"],
         "網卡混雜模式（Promiscuous Mode）：正常狀態下，網卡硬體僅接收目的 MAC 為「本機 MAC」或「廣播 MAC」的訊框，其餘訊框在硬體晶片層直接過濾丟棄；開啟 Promiscuous 模式後，網卡硬體關閉 MAC 過濾器，將實體線上監聽到的「所有」訊框通通無條件接收並向上提交給作業系統核心與嗅探程式（如 Wireshark、Snort IDS）。"),

        ("標準乙太網路（IEEE 802.3）訊框規範中，其「最小訊框長度（Minimum Frame Size）」規定為 64 位元組，其核心物理設計目的為？",
         "確保在最長網路傳輸距離與中繼器限制下，發送端在「訊框發送完畢之前」必然能夠及時偵測到遠端發生的碰撞（滿足爭用期 Slot Time 要求）",
         ["確保在最長網路傳輸距離與中繼器限制下，發送端在「訊框發送完畢之前」必然能夠及時偵測到遠端發生的碰撞（滿足爭用期 Slot Time 要求）",
          "防止封包在硬碟儲存時佔用過少空間",
          "使網路線內部電流維持恆定不變",
          "強制所有公務文件必須湊滿 64 個字元才能傳輸"],
         "乙太網 64 位元組最小訊框之物理意義：CSMA/CD 要求「邊送邊聽」。若訊框長度太短（例如只有 10 Bytes），發送端在幾微秒內即已全數發送完畢並關閉發射器；此時若在網路最遠端發生碰撞，反射回來的碰撞信號抵達發送端時，發送端已無從知曉，誤以為傳輸成功。64 Bytes（512 位元時間，Slot Time）恰為信號在最長 2.5 公里同軸網路來回走一趟（RTT）所需的最短發送時間。"),

        ("在進階交換器功能中，為防止未授權之外來筆記型電腦隨意插入辦公室網路孔，管理員可啟用「連接埠安全性（Port Security）」，下列何種安全設定能在交換器重開機後依然自動永久保留已學習到的合法 MAC 位址？",
         "粘滯 MAC 位址學習（Sticky MAC Addresses）",
         ["粘滯 MAC 位址學習（Sticky MAC Addresses）",
          "動態 MAC 位址學習（隨時間老化清除）",
          "匿名訪客模式",
          "隨機 MAC 輪替模式"],
         "Port Security 之 Sticky MAC：Port Security 限制連接埠可學習的 MAC 數量與合法清單。1. 動態 MAC：重開機後遺失需重新學習；2. 靜態 MAC：手動打指令輸入 48 位元 MAC 極度繁瑣；3. Sticky MAC（<code>switchport port-security mac-address sticky</code>）：交換器動態將當前插入的第一台電腦 MAC 自動轉錄並寫入 <code>running-config</code> 永久保存，兼具動態便利性與重開機持續保護。"),

        ("當交換器連接埠遭遇違反 Port Security 規範（如未授權 MAC 插入）時，若違規動作設定為「Shutdown」，交換器標準處置動作為？",
         "立即產生 SNMP Trap 告警並強制將該連接埠關閉，使其進入 <code>err-disabled</code> 狀態，直到管理員手動修復",
         ["立即產生 SNMP Trap 告警並強制將該連接埠關閉，使其進入 <code>err-disabled</code> 狀態，直到管理員手動修復",
          "繼續放行封包，僅在螢幕上閃爍黃燈",
          "將違規電腦之作業系統強制重灌",
          "拔掉交換器的總電源線"],
         "Port Security 三種違規模式：1. Protect：丟棄未授權 MAC 的封包，不發警報、不記錄日誌、不關埠；2. Restrict：丟棄違規封包，發送 SNMP Trap 告警並使違規計數器（Violation Counter）遞增；3. Shutdown（預設最嚴格）：丟棄封包，發送告警，並直接將該實體連接埠關閉（進入 err-disabled），必須由網管手動 <code>shutdown / no shutdown</code> 解鎖。"),

        ("比較交換器內部轉發技術：儲存轉發（Store-and-Forward）與直通轉發（Cut-Through）之特性，下列敘述何者完全正確？",
         "儲存轉發會完整接收整個訊框並進行 CRC 校驗確認無誤後才轉發，能過濾錯誤訊框但延遲略高；直通轉發僅讀取前 6 位元組的目的 MAC 即刻開始轉發，延遲最低但會轉發損壞訊框",
         ["儲存轉發會完整接收整個訊框並進行 CRC 校驗確認無誤後才轉發，能過濾錯誤訊框但延遲略高；直通轉發僅讀取前 6 位元組的目的 MAC 即刻開始轉發，延遲最低但會轉發損壞訊框",
          "直通轉發能在轉發前修復損壞的位元",
          "儲存轉發只適用於半雙工集線器",
          "兩者轉發延遲完全一模一樣"],
         "交換器轉發模式對決：1. Store-and-Forward：必須將整個訊框存入 Buffer，計算 FCS（CRC-32），若校驗錯誤或長度小於 64 Bytes（Runt）則直接丟棄，防止垃圾訊框在網路蔓延，是現代企業交換器預設模式；2. Cut-Through：讀完目的 MAC（前 6 Bytes）即刻觸發交叉矩陣轉發，延遲達奈秒級（常用於高頻金融交易或資料中心）；3. Fragment-Free：折衷方案，讀完前 64 Bytes（過濾碰撞碎片）後轉發。"),

        ("在快速生成樹協定（RSTP, IEEE 802.1w）中，相較於傳統 STP（802.1D）需要 30 至 50 秒的漫長收斂時間，RSTP 能在 1 秒以內迅速收斂，其連接埠狀態被簡化為哪三種狀態？",
         "丟棄狀態（Discarding）、學習狀態（Learning）與轉發狀態（Forwarding）",
         ["丟棄狀態（Discarding）、學習狀態（Learning）與轉發狀態（Forwarding）",
          "阻塞、監聽、學習、轉發與停用五種狀態",
          "開機、待機與關機狀態",
          "單播、廣播與群播狀態"],
         "RSTP 802.1w 狀態簡化與機制：傳統 STP 包含 Blocking、Listening、Learning、Forwarding、Disabled 五種狀態，仰賴定時器（Forward Delay 15s + Max Age 20s）收斂極慢。RSTP 將 Blocking、Listening 與 Disabled 統一合併為「Discarding（丟棄）」，僅保留 Discarding、Learning、Forwarding 三種狀態，並引進 Proposal/Agreement 交握機制與 Edge Port（邊界埠直通 Forwarding），使拓撲在幾百毫秒內迅速收斂。"),

        ("在地方政府機關佈設網路時，若希望透過同一條乙太網路雙絞線同時傳輸「網路資料」與提供「終端設備電源（如 IP 網路電話、PoE 網路監視器、無線基地台 AP）」，所使用的標準技術為？",
         "乙太網路供電技術（PoE, Power over Ethernet, IEEE 802.3af / 802.3at PoE+）",
         ["乙太網路供電技術（PoE, Power over Ethernet, IEEE 802.3af / 802.3at PoE+）",
          "電力線網路技術（PLC）",
          "無線微波供電技術",
          "光纖太陽能發電技術"],
         "PoE（乙太網路供電）標準演進：1. IEEE 802.3af（PoE）：供電端最高 15.4W，受電端可用約 12.95W，適用於一般 IP Phone；2. IEEE 802.3at（PoE+）：最高 30W（可用 25.5W），適用於 PTZ 旋轉監視器與雙頻 Wi-Fi 5 AP；3. IEEE 802.3bt（4PPoE / PoE++）：利用四對線全部供電，最高可達 60W~90W，可驅動視訊會議終端與大功率 LED 照明。"),

        ("在區域網路備援架構中，為防止核心閘道路由器發生單點故障（SPOF）導致全機關斷網，管理員配置兩台實體路由器共享同一個「虛擬 IP（VIP）與虛擬 MAC」，該高可用性協定為？",
         "虛擬路由器備援協定（VRRP, Virtual Router Redundancy Protocol / HSRP）",
         ["虛擬路由器備援協定（VRRP, Virtual Router Redundancy Protocol / HSRP）",
          "RIP 協定",
          "ICMP 重導向協定",
          "SNMP 網管協定"],
         "VRRP / HSRP 第一跳備援（FHRP）：終端電腦通常只能設定單一「預設閘道器（Default Gateway）」。若實體路由器當機，電腦無法自動切換。VRRP（RFC 5798 標準）或 HSRP（Cisco 私有）讓主（Master/Active）與備（Backup/Standby）路由器對外呈現單一虛擬 IP（如 <code>192.168.1.254</code>）。平時由主路由器轉發流量；主機斷線時，備援機毫秒級接管該 VIP，終端使用者完全無感知。"),

        ("在乙太網路標準中，傳統標準訊框之 MTU（最大傳輸單元）為 1500 位元組，若在資料中心或高效能儲存網路（如 iSCSI SAN）中啟用「巨型訊框（Jumbo Frames）」，其單一訊框大小通常擴充至？",
         "約 9,000 位元組（減少訊框數量與 CPU 中斷開銷，顯著提升大檔案吞吐量）",
         ["約 9,000 位元組（減少訊框數量與 CPU 中斷開銷，顯著提升大檔案吞吐量）",
          "約 64 位元組",
          "約 1,000,000 位元組",
          "約 16 位元組"],
         "Jumbo Frames（巨型訊框）：標準 MTU 1500 Bytes 傳輸 9000 Bytes 資料需拆成 6 個訊框，產生 6 次表頭開銷與 6 次網卡中斷（Interrupts）。啟用 Jumbo Frame 9000 後，單一訊框即可容納，中斷次數減少 80% 以上，伺服器 CPU 使用率劇降且儲存傳輸速率顯著提升。先決條件：傳輸路徑上所有交換器與網卡必須全部支援並開啟 Jumbo Frames，否則會發生封包截斷丟棄。"),

        ("在區域網路中，若網卡與交換器連接埠之「雙工模式（Duplex）」設定不匹配（一端設為強制全雙工 Full-Duplex，另一端設為半雙工 Half-Duplex），線路上最容易引發的特徵錯誤為？",
         "雙工不匹配（Duplex Mismatch），在半雙工端產生大量「晚期碰撞（Late Collisions）」與 CRC 訊框校驗錯誤，導致傳輸速率急遽暴跌",
         ["雙工不匹配（Duplex Mismatch），在半雙工端產生大量「晚期碰撞（Late Collisions）」與 CRC 訊框校驗錯誤，導致傳輸速率急遽暴跌",
          "線路瞬間燒毀中斷",
          "電腦自動重灌為最新作業系統",
          "網路完全正常且頻寬提高兩倍"],
         "Duplex Mismatch（雙工不匹配）：極具迷惑性的公務網路常見隱疾。全雙工端認為通道絕不會有碰撞，隨時發送資料；半雙工端在發送資料途中突然收到對端發送過來的資料，判定為「碰撞」。由於全雙工端根本不聽碰撞，半雙工端在發送了超過 64 Bytes 之後才偵測到碰撞（此即 Late Collision，晚期碰撞），導致大量重傳與封包丟棄，表面上能 ping 通但傳大檔案慢如撥接。"),

        ("在網路交換器中，由硬體專用積體電路實現之「CAM 表（Content Addressable Memory）」與「TCAM 表（Ternary CAM）」之主要用途分別為？",
         "CAM 表以極速進行精確比對，專門用於 Layer 2 MAC 位址轉發；TCAM 表支援「0, 1 與 Wildcard（Don't care）」三態比對，專門用於 Layer 3 路由最長前綴匹配與 ACL 防火牆規則硬體過濾",
         ["CAM 表以極速進行精確比對，專門用於 Layer 2 MAC 位址轉發；TCAM 表支援「0, 1 與 Wildcard（Don't care）」三態比對，專門用於 Layer 3 路由最長前綴匹配與 ACL 防火牆規則硬體過濾",
          "CAM 表用於儲存使用者密碼，TCAM 用於儲存電子郵件",
          "CAM 表用於顯示卡 3D 渲染，TCAM 用於播放音訊",
          "兩者皆為一般機械式硬碟磁軌名稱"],
         "CAM vs TCAM 硬體轉發：1. CAM（內容可定址記憶體）：輸入資料本身直接輸出位址（反向查詢），單一時鐘週期完成 MAC 表精確匹配（Binary 0/1）；2. TCAM（三態 CAM）：支援第三種狀態「X / Wildcard（通配符/任意值）」，能同時並行比對數萬條長度不一的路由遮罩（最長前綴匹配 LPM）與複雜的 ACL 存取控制清單，是 Layer 3 高階交換器實現線速（Wire-Speed）轉發的核心硬體大腦。")
    ]

    # Dataset 2: 網路層與傳輸層協定 (27 questions)
    data2 = [
        ("在 IPv4 位址規劃中，依據 RFC 1918 規範之「私人私有 IP 位址（Private IP Addresses）」範圍，下列何者「不屬於」法定之私有 IP 區段？",
         "<code>172.33.0.0/16</code>",
         ["<code>172.33.0.0/16</code>",
          "<code>10.0.0.0/8</code>（10.0.0.0 ～ 10.255.255.255）",
          "<code>172.16.0.0/12</code>（172.16.0.0 ～ 172.31.255.255）",
          "<code>192.168.0.0/16</code>（192.168.0.0 ～ 192.168.255.255）"],
         "RFC 1918 私有 IP 範圍三大區段：1. Class A：<code>10.0.0.0/8</code>（共 1 個 A 級網段）；2. Class B：<code>172.16.0.0/12</code>（涵蓋 <code>172.16.x.x</code> 至 <code>172.31.x.x</code>，共 16 個 B 級網段，因此 172.32 以上為公開 Public IP）；3. Class C：<code>192.168.0.0/16</code>（涵蓋 <code>192.168.0.x</code> 至 <code>192.168.255.x</code>，共 256 個 C 級網段）。私有 IP 無法在 Internet 公網直接路由。"),

        ("某區公所獲配一個 IPv4 子網路區段 <code>192.168.10.0/26</code>，該子網路之「子網路遮罩（Subnet Mask）」以及「理論上最多可分配給終端公務電腦之可用主機 IP 數量」分別為？",
         "遮罩為 <code>255.255.255.192</code>，可用主機數量為 62 台",
         ["遮罩為 <code>255.255.255.192</code>，可用主機數量為 62 台",
          "遮罩為 <code>255.255.255.128</code>，可用主機數量為 126 台",
          "遮罩為 <code>255.255.255.224</code>，可用主機數量為 30 台",
          "遮罩為 <code>255.255.255.0</code>，可用主機數量為 254 台"],
         "CIDR /26 子網路計算：/26 代表網路位元為 26，主機位元 $h = 32 - 26 = 6$。1. 遮罩最後一位元組：前兩位為 1（$128 + 64 = 192$），故遮罩為 <code>255.255.255.192</code>；2. 區塊大小為 $2^6 = 64$；3. 扣除 1 個 Network ID（.0）與 1 個 Directed Broadcast IP（.63），可用主機數公式為 $2^h - 2 = 2^6 - 2 = 64 - 2 = 62$ 台。"),

        ("某台公務主機 IP 位址為 <code>10.20.30.75</code>，子網路遮罩為 <code>255.255.255.240</code>（/28），該主機所屬子網路之「網路位址（Network ID）」與「定向廣播位址（Broadcast IP）」分別為？",
         "網路位址為 <code>10.20.30.64</code>，廣播位址為 <code>10.20.30.79</code>",
         ["網路位址為 <code>10.20.30.64</code>，廣播位址為 <code>10.20.30.79</code>",
          "網路位址為 <code>10.20.30.0</code>，廣播位址為 <code>10.20.30.255</code>",
          "網路位址為 <code>10.20.30.70</code>，廣播位址為 <code>10.20.30.85</code>",
          "網路位址為 <code>10.20.30.48</code>，廣播位址為 <code>10.20.30.63</code>"],
         "子網網段精確拆解：遮罩 <code>240</code> 代表主機位元數為 4（$32 - 28 = 4$），子網區塊間距（Magic Number）為 $256 - 240 = 16$。子網劃分如下：0~15, 16~31, 32~47, 48~63, 64~79, 80~95...。IP <code>75</code> 落在 64 至 79 區間。因此：該網段第一個位址 <code>.64</code> 為 Network ID，最後一個位址 <code>.79</code> 為 Broadcast ID，主機可用範圍為 <code>.65</code> 至 <code>.78</code>。"),

        ("在 IPv6 位址表示法中，依據 RFC 5952 縮寫規則，IPv6 位址 <code>2001:0db8:0000:0000:0000:0000:1428:57ab</code> 最精簡且唯一標準之縮寫格式為？",
         "<code>2001:db8::1428:57ab</code>",
         ["<code>2001:db8::1428:57ab</code>",
          "<code>2001:db8:0:0:0:0:1428:57ab</code>",
          "<code>2001:0db8::1428:57ab</code>",
          "<code>2001:db8::0::1428:57ab</code>"],
         "IPv6 位址縮寫雙準則：1. 每組 16 位元區段中「前導零（Leading Zeros）必須省略」，例如 <code>0db8</code> 寫為 <code>db8</code>；2. 連續全為 0 的區段可用雙冒號 <code>::</code> 取代，但「整串位址中 <code>::</code> 只能出現恰好一次」，以避免長度歧義。因此連續 4 組 0000 壓成 <code>::</code>，結果即為 <code>2001:db8::1428:57ab</code>。"),

        ("在 TCP/IP 通訊協定中，當本機電腦已知目標伺服器的「IP 位址」，但需要得知其「MAC 實體位址」以封裝 Layer 2 訊框時，所使用的核心協定為？",
         "位址解析協定（ARP, Address Resolution Protocol）",
         ["位址解析協定（ARP, Address Resolution Protocol）",
          "網際網路控制訊息協定（ICMP）",
          "動態主機設定協定（DHCP）",
          "網域名稱系統（DNS）"],
         "ARP 協定運作流程：主機查詢本地 ARP 快取，若無紀錄則向區域網路發送「ARP Request」廣播訊框（目的 MAC 為 <code>FF:FF:FF:FF:FF:FF</code>，內容詢問：誰擁有此 IP？請告訴我你的 MAC）；同網段內擁有該 IP 的主機收到後，以單播（Unicast）發送「ARP Reply」回應其 MAC 位址。請求主機隨後更新其 ARP 表。"),

        ("駭客在區公所區域網路內發動中間人攻擊（MITM），透過偽造虛假之 ARP 回應封包，欺騙公務電腦與預設閘道器（Gateway），使其 ARP 表中閘道器的 MAC 被竄改為駭客主機之 MAC，此種攻擊稱為？",
         "ARP 欺騙 / ARP 快取毒化（ARP Spoofing / Poisoning），可透過交換器的動態 ARP 檢驗（DAI）防禦",
         ["ARP 欺騙 / ARP 快取毒化（ARP Spoofing / Poisoning），可透過交換器的動態 ARP 檢驗（DAI）防禦",
          "DDoS 阻斷服務攻擊",
          "SQL 資料隱碼攻擊",
          "跨站腳本攻擊（XSS）"],
         "ARP 欺騙防護機制：ARP 協定設計初期缺乏認證機制，任何主機皆可隨時發送偽造的 ARP Reply（即使對方未曾發出 Request），受害主機會直接覆寫其 ARP 快取。防禦手段為在交換器上啟用 DAI（Dynamic ARP Inspection），交換器比對 DHCP 監聽綁定表（DHCP Snooping Binding Table），將不合法的偽造 ARP 封包在交換器硬體層直接丟棄。"),

        ("網路管理員使用 <code>ping 8.8.8.8</code> 測試對外連線時，背後主要使用的網路層通訊協定與訊息類型為？",
         "ICMP 協定（發送 Type 8 的 Echo Request，並等待回傳 Type 0 的 Echo Reply）",
         ["ICMP 協定（發送 Type 8 的 Echo Request，並等待回傳 Type 0 的 Echo Reply）",
          "TCP 協定發送 SYN 封包",
          "UDP 協定發送廣播封包",
          "IGMP 群播協定"],
         "ICMP 訊息代碼解析：ICMP（Internet Control Message Protocol）為 IP 協定的伴生除錯回報協定。1. Type 8（Echo Request）與 Type 0（Echo Reply）用於 <code>ping</code> 測試連通性；2. Type 3（Destination Unreachable）用於目標不可達；3. Type 11（Time Exceeded / TTL 歸零）為 <code>traceroute</code> 追蹤路徑路由節點之基礎；4. Type 5（Redirect）通知主機最佳路由。"),

        ("在 TCP 協定之連線建立過程中，雙方必須完成著名的「三向交握（Three-Way Handshake）」，其標準旗標（Flags）交換程序為？",
         "客戶端發送 <code>SYN</code> ➔ 伺服器回傳 <code>SYN + ACK</code> ➔ 客戶端回傳 <code>ACK</code>",
         ["客戶端發送 <code>SYN</code> ➔ 伺服器回傳 <code>SYN + ACK</code> ➔ 客戶端回傳 <code>ACK</code>",
          "客戶端發送 <code>ACK</code> ➔ 伺服器回傳 <code>SYN</code> ➔ 客戶端回傳 <code>FIN</code>",
          "客戶端發送 <code>FIN</code> ➔ 伺服器回傳 <code>ACK</code> ➔ 客戶端回傳 <code>RST</code>",
          "伺服器發送 <code>HELLO</code> ➔ 客戶端回傳 <code>OK</code>"],
         "TCP 三向交握流程與序號同步：1. Client 隨機生成初始序號（ISN）$x$，發送 <code>SYN, seq=x</code>；2. Server 收到後分配緩衝區，隨機生成自己的 ISN $y$，回傳 <code>SYN+ACK, seq=y, ack=x+1</code>；3. Client 收到後回傳 <code>ACK, seq=x+1, ack=y+1</code>。至此雙向虛擬電路正式建立，雙方確認彼此具備雙向收發能力。若駭客大量發送第一步的 SYN 且永不發送最後一步 ACK，即形成「SYN Flood 阻斷服務攻擊」。"),

        ("在 TCP 連線正常關閉時，主動發起關閉連線之一方在送出最後一個 ACK 封包後，通常必須停留在「TIME_WAIT」狀態等待 <code>2MSL</code>（兩倍最大區段存活時間）之久，其核心目的為？",
         "確保最後一個 ACK 封包確實抵達被動關閉方（若遺失可重傳 ACK），並讓本次連線在網路中殘留的迷航舊封包在網路上徹底自然消逝，避免干擾後續新連線",
         ["確保最後一個 ACK 封包確實抵達被動關閉方（若遺失可重傳 ACK），並讓本次連線在網路中殘留的迷航舊封包在網路上徹底自然消逝，避免干擾後續新連線",
          "等待硬碟磁頭歸位以節省電力",
          "強迫作業系統重新開機",
          "由工程師手動確認檔案無病毒後手動放行"],
         "TIME_WAIT 狀態之雙重保險：MSL（Maximum Segment Lifetime，通常為 30 秒至 2 分鐘）。停留在 TIME_WAIT 達 2MSL 的原因：1. 可靠終止連線：若主動方的最後一個 ACK 在網路上掉包，被動方會重傳 <code>FIN</code>，主動方處於 TIME_WAIT 才能重新發送 ACK；2. 避免舊封包混淆：若立即重用相同的四元組（來源IP/Port、目的IP/Port）建立新連線，上次連線延遲抵達的舊封包會被新連線誤收造成資料錯亂。"),

        ("比較傳輸層兩大主流協定 TCP 與 UDP 之特性差異，下列敘述何者完全正確？",
         "TCP 是連線導向、提供可靠傳輸、具備順序保證與流量擁塞控制；UDP 是非連線導向、傳輸速度快且表頭開銷小（僅 8 位元組），但不保證封包一定抵達",
         ["TCP 是連線導向、提供可靠傳輸、具備順序保證與流量擁塞控制；UDP 是非連線導向、傳輸速度快且表頭開銷小（僅 8 位元組），但不保證封包一定抵達",
          "UDP 提供嚴格的滑動視窗流量控制，TCP 則無任何控制",
          "DNS 查詢與 VoIP 視訊串流主要依賴 TCP 進行高速傳輸",
          "TCP 表頭長度固定為 8 位元組，UDP 表頭至少 20 位元組"],
         "TCP vs UDP 深度對照：1. TCP：連線導向（需三次交握），提供確認（ACK）、超時重傳、累積確認、滑動視窗（流量控制）與擁塞控制，表頭至少 20 Bytes，適用於不允許任何資料遺失的網頁（HTTP）、郵件（SMTP）、檔案傳輸（FTP）；2. UDP：非連線、Best-Effort 盡力而為傳輸，表頭僅 8 Bytes，適用於對延遲敏感但容忍微量掉包的語音（VoIP）、串流直播、DNS 查詢與 DHCP。"),

        ("在 TCP 流量控制（Flow Control）機制中，接收端是透過 TCP 表頭中的哪一個欄位動態告知傳送端「本機目前緩衝區尚能接收之位元組空間」，以防止接收端緩衝區被灌爆溢位？",
         "接收視窗（Receive Window, rwnd / Window Size 欄位）",
         ["接收視窗（Receive Window, rwnd / Window Size 欄位）",
          "急迫指標（Urgent Pointer）",
          "檢查碼（Checksum）",
          "生存時間（TTL）"],
         "滑動視窗流量控制：TCP 採用 End-to-End 的 Sliding Window 機制。接收端在每次回傳的 ACK 封包中填入當前剩餘可用 Buffer 大小（rwnd）。傳送端發送但未確認的資料量絕對不可超過 rwnd。若接收端處理太慢，rwnd 降為 0，傳送端必須暫停發送（僅定期發送 Window Probe 探測封包），達成端點間的精確流量配速。"),

        ("在 TCP 擁塞控制（Congestion Control）機制中，當連線剛建立時，擁塞視窗（cwnd, Congestion Window）從 1 個 MSS 開始，在未發生掉包且未達到慢啟動門檻（ssthresh）之前，cwnd 的增長規律呈現何種趨勢？",
         "慢啟動階段（Slow Start），每個往返時間（RTT）內 cwnd 呈「指數級增長（每收到一個有效 ACK 增加 1，即翻倍增長）」",
         ["慢啟動階段（Slow Start），每個往返時間（RTT）內 cwnd 呈「指數級增長（每收到一個有效 ACK 增加 1，即翻倍增長）」",
          "線性增長（每個 RTT 僅固定增加 1 個 MSS）",
          "對數級遞減",
          "完全保持恆定不變"],
         "TCP 擁塞控制四階段：1. 慢啟動（Slow Start）：cwnd 從 1 MSS 開始，每經過一個 RTT，cwnd 翻倍（1➔2➔4➔8...，實質是指數級暴增！）；2. 擁塞避免（Congestion Avoidance）：當 cwnd 達到門檻值 ssthresh，轉為加法增大（Additive Increase，每個 RTT 僅增加 1 MSS 線性攀升）；3. 快重傳（Fast Retransmit）：收到 3 個重複 ACK（Triple Duplicate ACKs）時不等超時立即重傳；4. 快復原（Fast Recovery）。"),

        ("在 IPv4 封包表頭中，用以防止封包在網路路由器之間因路由迴路（Routing Loop）無限循環轉發而塞爆頻寬之欄位為？",
         "存活時間（TTL, Time to Live），封包每經過一台路由器時數值自動減 1，歸零時封包被丟棄",
         ["存活時間（TTL, Time to Live），封包每經過一台路由器時數值自動減 1，歸零時封包被丟棄",
          "服務類型（ToS）",
          "封包總長度（Total Length）",
          "識別碼（Identification）"],
         "TTL 防迴路機制：TTL 欄位長度為 8 位元（最大值 255）。封包每經過一個 L3 Hop（路由器），路由器將 TTL 減 1 並重新計算表頭 Checksum。若減至 0，路由器立即將該封包拋棄，並向來源端回傳 ICMP Type 11（Time to Live exceeded in transit）錯誤訊息。<code>traceroute</code> 即是故意發送 TTL=1, 2, 3... 的封包，藉由誘發各節點的 ICMP 逾時回應繪製出路徑拓撲。"),

        ("在 Linux/Windows 網路工具中，用以解析特定主機名稱（如 <code>www.gov.tw</code>）對應之 IP 位址或查詢 DNS 紀錄（MX, NS, TXT）之標準命令為？",
         "<code>nslookup</code>（或 <code>dig</code>, <code>host</code>）",
         ["<code>nslookup</code>（或 <code>dig</code>, <code>host</code>）", "<code>ipconfig /flushdns</code>", "<code>telnet</code>", "<code>ftp</code>"],
         "DNS 診斷命令：<code>nslookup</code> 是跨平台的 DNS 查詢工具，支援互動模式；<code>dig</code>（Domain Information Groper）是 Linux 專業網管利器，提供極其詳盡的解析耗時、權威應答標記（AA Flag）與 SOA 序號；<code>host</code> 則輸出簡潔明瞭的解析結果。"),

        ("在 IPv4 位址體系中，位址 <code>127.0.0.1</code> 屬於何種特殊用途位址？當對該位址發送 ping 測試時，其封包的真實傳輸路徑為？",
         "回呼位址（Loopback Address），封包直接在本地作業系統核心的 TCP/IP 協定堆疊內部迴環處理，完全不會發送到實體網路線上",
         ["回呼位址（Loopback Address），封包直接在本地作業系統核心的 TCP/IP 協定堆疊內部迴環處理，完全不會發送到實體網路線上",
          "廣播位址，封包會發送至全區公所的所有電腦",
          "預設閘道位址，封包會直接送往中華電信機房",
          "無效位址，系統會立即回報硬體中斷錯誤"],
         "Loopback（回呼位址）特性：整段 <code>127.0.0.0/8</code> 皆為迴環位址（最常用 127.0.0.1，對應主機名 localhost）。當應用程式連線 127.0.0.1 時，核心在網路層直接將封包導回接收佇列，無需經過實體網卡晶片或對外線路。執行 <code>ping 127.0.0.1</code> 是驗證本機作業系統 TCP/IP 協定堆疊安裝是否健全之第一道檢測命令。"),

        ("當某公務電腦設定為透過 DHCP 自動取得 IP，但機房 DHCP 伺服器因故障無法連線時，Windows 電腦通常會自動為自己指派一個 <code>169.254.x.x</code> 之 IP 位址，此機制稱為？",
         "自動私人 IP 定址（APIPA, Automatic Private IP Addressing / Link-Local RFC 3927）",
         ["自動私人 IP 定址（APIPA, Automatic Private IP Addressing / Link-Local RFC 3927）",
          "靜態公共 IP 配置",
          "DNS 動態更新",
          "NAT 虛擬映射"],
         "APIPA 機制：當主機發送 DHCP Discover 多次未獲回應時，作業系統自動從保留網段 <code>169.254.0.0/16</code> 中隨機挑選一個位址，並發送免費 ARP 確認無人使用後自我配置。此位址僅能在同一個 Layer 2 區域網路內臨時通訊，因無預設閘道器（Gateway）與 DNS，電腦無法連上 Internet。看到 169.254.x.x 即代表「DHCP 租約獲取失敗」。"),

        ("在早期的 IPv4 類別定址（Classful Addressing）中，IP 位址之第一個位元組（First Octet）數值範圍落在 <code>192 至 223</code> 之間者，屬於哪一等級之網路？其預設子網路遮罩為？",
         "Class C 網路，預設子網路遮罩為 <code>255.255.255.0</code>（/24）",
         ["Class C 網路，預設子網路遮罩為 <code>255.255.255.0</code>（/24）",
          "Class A 網路，預設遮罩為 255.0.0.0",
          "Class B 網路，預設遮罩為 255.255.0.0",
          "Class D 網路（群播專用）"],
         "IPv4 傳統類別劃分：1. Class A：0~127（最高位為 0），預設 /8；2. Class B：128~191（最高兩位 10），預設 /16；3. Class C：192~223（最高三位 110），預設 /24，每個網路容納 254 台主機；4. Class D：224~239（最高四位 1110），多點傳送（Multicast）專用；5. Class E：240~255，實驗保留。現代網路已全面改採無類別網域間路由（CIDR）。"),

        ("當一個長度為 4,000 位元組的 IPv4 封包需要通過一個最大傳輸單元（MTU）為 1,500 位元組的網路鏈路時，路由器必須對其進行「IP 分段（Fragmentation）」，重組這些分段封包所需之三個關鍵表頭欄位為？",
         "識別碼（Identification）、旗標（Flags, 如 DF/MF 位元）與分段偏移量（Fragment Offset）",
         ["識別碼（Identification）、旗標（Flags, 如 DF/MF 位元）與分段偏移量（Fragment Offset）",
          "TTL、通訊協定與檢查碼",
          "來源 IP、目的 IP 與服務類型",
          "視窗大小、確認號碼與緊急指標"],
         "IP 分段三大欄位解析：1. Identification（16-bit）：同一個大封包切出的所有分段具有完全相同的 ID；2. Flags（3-bit）：DF（Don't Fragment，若為 1 且超過 MTU 則丟棄回傳 ICMP）、MF（More Fragments，1 表後面還有分段，0 表這是最後一片）；3. Fragment Offset（13-bit）：記錄該分段相對於原資料起始點的偏移量（以 8 位元組為計數單位）。重組工作一律在最終目的端主機進行。"),

        ("在 IPv6 通訊協定中，徹底取代傳統 IPv4 之 ARP 廣播協定，負責在同網段解析鄰居 MAC 位址、路由器發現與重複位址檢測（DAD）之核心協定為？",
         "鄰居發現協定（NDP, Neighbor Discovery Protocol，基於 ICMPv6 協定）",
         ["鄰居發現協定（NDP, Neighbor Discovery Protocol，基於 ICMPv6 協定）",
          "RARP 逆向位址解析協定",
          "BOOTP 引導通訊協定",
          "IGMP 網際網路群組管理協定"],
         "IPv6 NDP 機制革新：IPv6 全面廢除了容易引發廣播風暴的「廣播（Broadcast）」，改採精確的「群播（Multicast）」。NDP 運行於 ICMPv6 之上，包含：1. 鄰居請求（NS）與鄰居通告（NA）：取代 ARP 查詢 MAC；2. 路由器請求（RS）與路由器通告（RA）：實現無狀態自動設定（SLAAC）；3. 重複位址檢測（DAD）：啟用 IP 前先問有沒有人用，確保全網唯一。"),

        ("IPv6 之「鏈路本地位址（Link-Local Address）」僅能在同一個實體鏈路（同一子網路）內部通訊且不可被路由器轉發，其標準前綴格式為？",
         "<code>fe80::/10</code>",
         ["<code>fe80::/10</code>", "<code>fc00::/7</code>", "<code>ff00::/8</code>", "<code>2001::/16</code>"],
         "IPv6 特殊前綴分類：1. <code>fe80::/10</code>：Link-Local 位址，每張啟用 IPv6 的網卡自動產生，用於鄰居通訊與內部路由協定（如 OSPFv3），絕不跨路由器路由；2. <code>fc00::/7</code>：唯一本地位址（ULA），相當於 IPv4 的私有 IP；3. <code>ff00::/8</code>：群播位址（Multicast）；4. <code>::1/128</code>：迴環位址（相當於 127.0.0.1）；5. <code>::/128</code>：未指定位址（相當於 0.0.0.0）；6. <code>2000::/3</code>：全球單播位址（GUA，公網 IP）。"),

        ("公務電腦在剛開機連接網路取得 IP 時，會主動向區域網路發送一個來源 IP 與目的 IP 皆為本機剛分配 IP 之「免費 ARP（Gratuitous ARP）」廣播封包，其最核心的兩大目的為？",
         "檢查區域網路內是否存在「IP 位址衝突（IP Conflict）」，並主動通知全網交換器與其他主機即刻更新其 ARP 快取與 MAC 對應表",
         ["檢查區域網路內是否存在「IP 位址衝突（IP Conflict）」，並主動通知全網交換器與其他主機即刻更新其 ARP 快取與 MAC 對應表",
          "向中華電信申請升級寬頻頻寬",
          "清除作業系統所有的瀏覽器歷史紀錄",
          "向全世界發布本機使用者的電子郵件帳號"],
         "免費 ARP（Gratuitous ARP）兩大價值：1. IP 衝突檢測：主機剛拿到 IP（如靜態設定或 DHCP），廣播詢問「誰有我的 IP？」。若收到任何 Reply 回應，代表網段內已有他人佔用該 IP，系統立即跳出「IP 位址發生衝突」警告並停用該 IP；2. 刷新全網快取：當主機更換網卡（MAC 改變）或伺服器做 HA 切換時，發送 Gratuitous ARP 能瞬間強制刷新全網交換器的 CAM 表與其他主機的 ARP 表。"),

        ("在極高速（如 10Gbps）長延遲網路傳輸中，標準 TCP 表頭中的視窗大小（Window Size）欄位僅有 16 位元（最大僅能表示 65,535 位元組，即 64KB），容易成為吞吐量瓶頸。RFC 1323 定義了何種 TCP 選項來突破此限制？",
         "視窗縮放選項（Window Scale Option），最大可將視窗大小擴展至 1GB",
         ["視窗縮放選項（Window Scale Option），最大可將視窗大小擴展至 1GB",
          "訊框壓縮選項",
          "巨型封包截斷選項",
          "非同步重傳選項"],
         "TCP Window Scale（RFC 1323 高效能擴充）：依據頻寬延遲積（BDP = Bandwidth * RTT），在高速長距離鏈路（如 10G 光纖）中，64KB 視窗只要幾毫秒就被塞滿，傳送端被迫停下來等待 ACK，頻寬利用率低於 1%。Window Scale 在三向交握時協商一個位移倍率（Shift Count 0~14），將 16-bit 視窗值左移，等同於乘以 $2^S$（最大 $2^{14} = 16384$），使有效視窗達到 $65535 	imes 16384 pprox 1$GB。"),

        ("在傳統 TCP 累積確認（Cumulative ACK）中，若發送端連續傳送封包 1 至 5，僅有封包 2 在途中遺失，接收端僅能持續回傳 ACK 2，導致傳送端必須將封包 2、3、4、5 全部重傳。為避免重傳未遺失之封包，現代 TCP 引入之擴充選項為？",
         "選擇性確認（SACK, Selective Acknowledgment, RFC 2018）",
         ["選擇性確認（SACK, Selective Acknowledgment, RFC 2018）",
          "快速跳躍確認",
          "盲目重送選項",
          "非對稱交握選項"],
         "SACK（選擇性確認）之精準重傳：SACK 允許接收端在回傳的 ACK 表頭中，利用 TCP Options 區塊明確條列「目前已成功收到的非連續資料區間區塊（Blocks）」（例如告訴發送端：我已收到 3、4、5，僅缺 2）。發送端讀取 SACK 後，精確只重傳遺失的封包 2，而不會愚蠢地重複重傳 3、4、5，極大化提升高丟包率或高延遲網路下的傳輸效能。"),

        ("在計算機網路中，TCP 最大區段大小（MSS, Maximum Segment Size）通常等於乙太網之 MTU（1500 位元組）扣除標準 IPv4 表頭與標準 TCP 表頭長度，其典型標準數值為？",
         "1,460 位元組（1500 - 20 Bytes IP 表頭 - 20 Bytes TCP 表頭）",
         ["1,460 位元組（1500 - 20 Bytes IP 表頭 - 20 Bytes TCP 表頭）",
          "1,500 位元組",
          "1,480 位元組",
          "1,024 位元組"],
         "MSS（最大區段大小）計算推導：MSS 指的是單一 TCP Segment 中所能承載的「純應用層有效資料（Payload）」上限，不包含 TCP 表頭與 IP 表頭。標準乙太網 MTU = 1500 Bytes；標準無選項之 IPv4 Header 長度為 20 Bytes；標準無選項之 TCP Header 長度為 20 Bytes。因此 $	ext{MSS} = 1500 - 20 - 20 = 1460$ Bytes。（若為 IPv6，因 IPv6 固定表頭為 40 Bytes，其典型 MSS 為 1440 Bytes）。"),

        ("在 TCP 逾時重傳時間（RTO, Retransmission TimeOut）之動態估算中，最著名之 Jacobson/Karels 演算法計算 RTO 之公式模型為？",
         "<code>RTO = SRTT + 4 * RTTVAR</code>（平滑往返時間加上 4 倍往返時間變異數）",
         ["<code>RTO = SRTT + 4 * RTTVAR</code>（平滑往返時間加上 4 倍往返時間變異數）",
          "RTO = 固定 1.0 秒永遠不變",
          "RTO = SRTT / 2",
          "RTO = RTT * 100"],
         "TCP RTO 動態計算原理：若 RTO 設太小，網路稍有波動即引發虛假重傳（Spurious Retransmission）；若 RTO 設太大，真正掉包時需等待漫長時間才重傳，吞吐量暴跌。RFC 6298 採用 Jacobson 演算法：1. 計算平滑 RTT：$	ext{SRTT} = (1 - lpha)	ext{SRTT} + lpha 	ext{RTT}$；2. 計算偏差量（Jitter）：$	ext{RTTVAR} = (1 - eta)	ext{RTTVAR} + eta |	ext{SRTT} - 	ext{RTT}|$；3. 最終 $	ext{RTO} = 	ext{SRTT} + 4 	imes 	ext{RTTVAR}$（至少保證大於 1 秒）。"),

        ("網路通訊傳輸方式分為單播（Unicast）、廣播（Broadcast）與群播（Multicast），在地方政府智慧交控視訊監控串流傳輸中，「由單一攝影機發送影像，僅允許加入特定多播群組的主機接收，其餘無關主機不收亦不受干擾」之傳輸模式為？",
         "群播 / 多點傳送（Multicast，搭配 IGMP 協定管理成員關係）",
         ["群播 / 多點傳送（Multicast，搭配 IGMP 協定管理成員關係）",
          "單播（Unicast，對每台主機複製一份獨立傳輸）",
          "廣播（Broadcast，強迫全網所有設備一律接收處理）",
          "隨機漫播"],
         "Multicast（群播）在影音串流之優勢：若採用 Unicast，1,000 位使用者觀看監視器需發送 1,000 份重複串流，伺服器與骨幹頻寬瞬間癱瘓；若採 Broadcast，連不看視訊的辦公電腦也會被垃圾視訊封包淹沒。Multicast 採用 Class D 群播位址（224.0.0.0/4），終端透過 IGMP 協定向交換器/路由器登記加入，路由器僅在有成員的分支鏈路上複製轉發一份串流，頻寬效益極致最佳化。"),

        ("在網路層封包路由決策中，路由器在路由表（Routing Table）中比對封包目的 IP 位址時，必須遵循的最核心原則為？",
         "最長前綴匹配原則（LPM, Longest Prefix Match，遮罩長度最長者優先匹配）",
         ["最長前綴匹配原則（LPM, Longest Prefix Match，遮罩長度最長者優先匹配）",
          "最短前綴匹配原則（/0 預設路由永遠最優先）",
          "字母順序排列優先原則",
          "路由器隨機挑選一條介面轉發"],
         "最長前綴匹配（LPM 原則）：當路由表中有數條路由皆能涵蓋目標 IP 時，路由器永遠挑選「子網路遮罩最長（Prefix 長度最大、劃分範圍最精確）」之路由規則。例如：目標 IP 為 <code>10.1.1.5</code>，表中同時存在 <code>10.0.0.0/8</code>、<code>10.1.1.0/24</code> 與 <code>0.0.0.0/0</code>（預設路由），路由器毫不猶豫選擇前綴最長的 <code>/24</code> 路由。預設路由（/0）遮罩最短，僅在完全無任何匹配時作為最後墊底。")
    ]

    # Dataset 3: 網路服務、路由協定、無線網路與 VPN 遠端辦公 (26 questions)
    data3 = [
        ("在地方政府機關區域網路出口閘道器上，最常用以將機關內部數百台私有 IP 電腦「映射為少數幾個（甚至單一）公有 Public IP 的不同連接埠號連上網際網路」之 NAT 技術為？",
         "網路位址埠號轉譯（NAPT / PAT, Port Address Translation）",
         ["網路位址埠號轉譯（NAPT / PAT, Port Address Translation）",
          "靜態 NAT（一對一固定映射）",
          "動態 NAT（無埠號轉換之一對一池化）",
          "DNS 負載平衡"],
         "NAT/NAPT 核心運作：1. 靜態 NAT：一個內部私有 IP 一對一固定映射一個公有 IP，無法節省公有 IP；2. NAPT / PAT（最普遍）：多對一或多對多轉換，利用傳輸層的「TCP/UDP 來源通訊埠號（Port）」作為多工依據，在連線追蹤表（Conntrack Table）中記錄 <code>私有IP:Port &lt;=&gt; 公網IP:動態Port</code>，使整座公所數百名同仁僅需 1 個公有 IP 即可同時上網，徹底緩解 IPv4 枯竭危機。"),

        ("在動態主機設定協定（DHCP）之標準租約取得流程中，客戶端電腦初次開機取得 IP 必須經過的「四部曲封包互動順序」為？",
         "DHCP Discover（廣播）➔ DHCP Offer（單播/廣播）➔ DHCP Request（廣播）➔ DHCP Ack（確認）",
         ["DHCP Discover（廣播）➔ DHCP Offer（單播/廣播）➔ DHCP Request（廣播）➔ DHCP Ack（確認）",
          "DHCP Request ➔ DHCP Offer ➔ DHCP Discover ➔ DHCP Ack",
          "DHCP Hello ➔ DHCP Welcome ➔ DHCP Accept ➔ DHCP Bye",
          "DHCP Start ➔ DHCP Wait ➔ DHCP Stop ➔ DHCP Finish"],
         "DHCP 四步驟口訣（DORA）：1. Discover：客戶端無 IP，發送 UDP 廣播（Port 67/68，來源 <code>0.0.0.0</code> 目的 <code>255.255.255.255</code>）搜尋 DHCP 伺服器；2. Offer：伺服器提供可用 IP、遮罩、閘道與 DNS；3. Request：客戶端廣播告知全網「我決定採用某伺服器之報價」（同時婉拒其他伺服器）；4. Ack：伺服器正式確認租約（Lease Time）生效。"),

        ("若地方政府各局處電腦位於不同的 VLAN（不同子網路）中，而全機關僅在資訊中心集中建置了一台 DHCP 伺服器，欲使跨網段電腦皆能順利取得 IP，必須在各 VLAN 閘道器上配置何種代理機制？",
         "DHCP 中繼代理（DHCP Relay Agent，將 Layer 2 廣播轉換為 Layer 3 單播轉發）",
         ["DHCP 中繼代理（DHCP Relay Agent，將 Layer 2 廣播轉換為 Layer 3 單播轉發）",
          "全面關閉各交換器的防火牆",
          "在每部終端電腦上安裝 DHCP 伺服器軟體",
          "將所有電腦的網線拔掉重新插上"],
         "DHCP Relay Agent 運作本質：DHCP Discover 是 Layer 2 廣播封包，依照網路標準路由器絕不轉發廣播，因此不同 VLAN 的主機無法直接接觸遠端集中式 DHCP 伺服器。在三層交換器或路由器介面上設定 DHCP 中繼（如 Cisco 的 <code>ip helper-address</code>），閘道器攔截 Discover 廣播後，將其封裝為 Layer 3 單播封包轉發給跨網段的 DHCP 伺服器，大幅節省在各局處重複架設伺服器的成本。"),

        ("在 DNS 網域名稱解析查詢過程中，「遞迴查詢（Recursive Query）」與「反覆/疊代查詢（Iterative Query）」的核心差異在於？",
         "遞迴查詢要求受查詢的 DNS 伺服器「必須負責到底並回傳最終解析結果（若自己不知道需代為向外部詢問）」；疊代查詢則是「若伺服器不知道具體答案，僅回傳下一層應去詢問之 DNS 伺服器參考位址」",
         ["遞迴查詢要求受查詢的 DNS 伺服器「必須負責到底並回傳最終解析結果（若自己不知道需代為向外部詢問）」；疊代查詢則是「若伺服器不知道具體答案，僅回傳下一層應去詢問之 DNS 伺服器參考位址」",
          "遞迴查詢只能查英文網址，疊代查詢只能查中文網址",
          "遞迴查詢使用 TCP 協定，疊代查詢使用 UDP 協定",
          "兩者完全相同無任何差異"],
         "DNS 遞迴 vs 疊代解析機制：終端 PC 向機關內部 Local DNS（如 168.95.1.1）發出的是「遞迴查詢」（用戶端只等最終答案，不做跑腿差事）；Local DNS 伺服器在快取未命中時，以「疊代查詢」依序向全球 13 組根網域名稱伺服器（Root ➔ 回應 .tw 伺服器）➔ 頂級網域伺服器（TLD ➔ 回應 .gov.tw 伺服器）➔ 權威 DNS 伺服器（Authoritative Name Server ➔ 回應最終 IP），最後將結果回傳給終端電腦。"),

        ("在 DNS 資源紀錄（Resource Records）類型中，用以建立網域名稱之「別名（Alias）」，將某一主機名稱指向另一個正規主機名稱（Canonical Name）之紀錄類型為？",
         "CNAME 紀錄",
         ["CNAME 紀錄", "A 紀錄", "MX 紀錄", "PTR 紀錄"],
         "DNS 核心紀錄類型對照：1. A 紀錄：IPv4 位址對應（Host ➔ IPv4）；2. AAAA 紀錄：IPv6 位址對應；3. CNAME（Canonical Name）：別名紀錄（如將 <code>mail.city.gov.tw</code> 指向 <code>webmail.service.city.gov.tw</code>）；4. MX（Mail Exchanger）：電子郵件伺服器路由紀錄；5. PTR（Pointer）：反向解析（IP ➔ 網域名稱）；6. NS（Name Server）：指定該網域之權威 DNS 伺服器。"),

        ("在內部閘道路由協定（IGP）中，比較「RIP 協定」與「OSPF 協定」之特性，下列敘述何者完全正確？",
         "RIP 採用距離向量演算法（Distance Vector），以跳數（Hop Count）為度量且上限為 15 跳；OSPF 採用鏈路狀態演算法（Link-State），以頻寬開銷（Cost）為度量，支援階層化區域（Area 0 骨幹）且收斂速度極快",
         ["RIP 採用距離向量演算法（Distance Vector），以跳數（Hop Count）為度量且上限為 15 跳；OSPF 採用鏈路狀態演算法（Link-State），以頻寬開銷（Cost）為度量，支援階層化區域（Area 0 骨幹）且收斂速度極快",
          "RIP 適用於跨國超大型電信網路，OSPF 僅能用於兩台電腦互連",
          "OSPF 以跳數為度量，上限為 16 跳",
          "RIP 採用戴克斯特拉（Dijkstra）最短路徑演算法"],
         "RIP vs OSPF 路由協定對決：1. RIP（Routing Information Protocol）：Bellman-Ford 演算法，每 30 秒向鄰居廣播全表，僅計算跳數（無視頻寬高低），Hop=16 即判定不可達，易產生路由迴圈且收斂慢；2. OSPF（Open Shortest Path First）：各路由器泛洪 LSA（鏈路狀態通告）建立全網拓撲圖，由 Dijkstra 演算法計算 SPF 樹，基於頻寬計算 Metric（Cost = $10^8 / \\text{Bandwidth}$），支援 VLSM 與階層分區，是大中型公務機關標準協定。"),

        ("在最新 Wi-Fi 6（IEEE 802.11ax）無線通訊標準中，相較於前代 Wi-Fi 5，其能大幅改善多裝置並行連線擁塞、提高頻譜利用率之核心劃分技術為？",
         "正交分頻多重存取（OFDMA, Orthogonal Frequency Division Multiple Access）",
         ["正交分頻多重存取（OFDMA, Orthogonal Frequency Division Multiple Access）",
          "直接序列展頻（DSSS）",
          "跳頻展頻技術（FHSS）",
          "頻率調變廣播（FM）"],
         "Wi-Fi 6 OFDMA 革命：傳統 Wi-Fi 採用 OFDM，每個時槽（Timeslot）整條頻寬通道只能傳給單一使用者（類似一輛大卡車只載一位乘客的包裹）；Wi-Fi 6 引進源自 4G/5G 的 OFDMA 技術，將無線頻道細分為數十個微小的子載波資源單元（RU, Resource Units），單一傳輸週期內可同時並行向數十個不同設備收發資料，徹底終結多設備排隊搶頻道的延遲痛點。"),

        ("在無線區域網路（WLAN）安全防護中，相較於 WPA2 容易遭受離線字典檔暴力破解攻擊（Offline Dictionary Attack），WPA3 引入何種握手認證機制大幅強化密碼防禦力？",
         "同時對等認證機制（SAE, Simultaneous Authentication of Equals / Dragonfly 握手協定）",
         ["同時對等認證機制（SAE, Simultaneous Authentication of Equals / Dragonfly 握手協定）",
          "WEP 40 位元靜態金鑰驗證",
          "純明文無密碼開放連線",
          "簡單對稱式 XOR 移位演算法"],
         "WPA3 SAE（同時對等認證）防護原理：WPA2-PSK 採用傳統 4-Way Handshake，駭客在公共場合側錄到交握封包後，可帶回家使用 GPU 進行無限次離線密碼字典爆破；WPA3 採用基於零知識證明的 SAE（蜻蜓交握協定），每次握手使用動態密碼學金鑰交換，攻擊者無法進行離線推導，每次猜測密碼皆必須連線與 AP 實時互動，搭配防爆破次數限制，從根本上杜絕了弱密碼外洩風險。"),

        ("地方政府公務同仁在疫情或外勤期間進行遠距居家辦公，透過網際網路安全連回府內核心公文與戶政系統，最常建置之加密通道技術為？",
         "虛擬私有網路（VPN, Virtual Private Network，如 IPsec VPN 或 SSL/TLS VPN）",
         ["虛擬私有網路（VPN, Virtual Private Network，如 IPsec VPN 或 SSL/TLS VPN）",
          "Telnet 明文遠端登入連線",
          "無加密之 FTP 檔案傳輸",
          "HTTP 明文網頁直接暴露"],
         "VPN（虛擬私有網路）遠端安全通道：在不可信的公共 Internet 上建立加密穿隧通道（Tunneling）。1. IPsec VPN（網路層 Layer 3）：包含 ESP（加密與認證）與 AH（僅認證），支援通道模式（Site-to-Site 機關對機關）與傳輸模式；2. SSL/TLS VPN（應用層/傳輸層）：透過 HTTPS 或專屬用戶端（如 OpenVPN、WireGuard），使用者僅需身分認證（通常搭配雙因素認證 2FA）即可建立虛擬網卡安全存取內網。"),

        ("在 IPsec 協定套件中，提供「資料機密性（加密封裝）」、「資料完整性驗證」與「防重送攻擊（Anti-Replay）」之核心協定為？",
         "封裝安全負載協定（ESP, Encapsulating Security Payload）",
         ["封裝安全負載協定（ESP, Encapsulating Security Payload）",
          "認證表頭協定（AH，Authentication Header，不提供加密功能）",
          "網際網路金鑰交換協定（IKE）",
          "簡單網路管理協定（SNMP）"],
         "IPsec AH vs ESP 核心差異：1. AH（Authentication Header，協定號 51）：提供資料完整性認證與來源身分驗證，但「完全不提供加密服務」（Payload 資料為明文！），且因保護外層 IP 表頭，與 NAT 不相容；2. ESP（協定號 50）：利用對稱加密演算法（如 AES-GCM）提供高強度「機密性加密」，同時提供數位簽章認證與防重送，是現代 VPN 穿隧之標準核心。"),

        ("在公務機關伺服器負載均衡中，DNS 伺服器設定同一個網域名稱（如 <code>www.city.gov.tw</code>）對應多筆不同伺服器實體 IP，依序輪流回應給不同發送請求之查詢者，此種最簡單的負載平衡機制稱為？",
         "DNS 輪詢機制（DNS Round Robin）",
         ["DNS 輪詢機制（DNS Round Robin）",
          "DNS 區域轉移（Zone Transfer）",
          "Anycast 任意播路由",
          "動態路由收斂"],
         "DNS Round Robin（輪詢負載平衡）：在 DNS 區域檔中為同一主機名稱配置多筆 A 紀錄（如 IP-A, IP-B, IP-C）。DNS 伺服器在收到查詢時，輪流將 IP 清單順序調整（A➔B➔C，下次 B➔C➔A），使客戶端連線平均分散至不同伺服器。缺點在於 DNS 無法感知後端伺服器的健康狀態（若某台當機仍會繼續分派請求），且受限於各級 DNS 快取（TTL）導致流量切換延遲。"),

        ("在無線網路 802.11 媒體存取控制中，為徹底避免多台無線設備因「隱藏節點問題（Hidden Terminal Problem）」互相聽不到對方而同時向無線基地台發射引發嚴重碰撞，最常用之握手協定為？",
         "RTS / CTS 機制（請求傳送 Request to Send / 允許傳送 Clear to Send）",
         ["RTS / CTS 機制（請求傳送 Request to Send / 允許傳送 Clear to Send）",
          "CSMA/CD 碰撞偵測",
          "三向交握機制",
          "Token 權標傳遞機制"],
         "隱藏節點與 RTS/CTS 機制：節點 A 與節點 B 皆在 AP 的覆蓋範圍內，但 A 與 B 之間因距離過遠或障礙物阻隔而聽不到彼此。若 A 與 B 同時偵測空中無訊號並向 AP 發射，會在 AP 端造成訊號嚴重碰撞。啟用 RTS/CTS：A 先向 AP 發送微小的 RTS；AP 回覆廣播 CTS（告知所有人保留通道一段時間）；B 聽到 CTS 隨即保持靜默退避，A 順利傳送資料，完美解決隱藏節點干擾。"),

        ("在地方政府對外便民服務架構中，資訊局欲將內部機房私有 IP 伺服器（<code>192.168.1.100:80</code>）發布至網際網路，讓民眾能透過防火牆之公網實體 IP（<code>210.69.1.5:80</code>）造訪，在防火牆上應設定之 NAT 類型為？",
         "目的端網路位址轉譯（DNAT / Port Forwarding 連接埠轉發）",
         ["目的端網路位址轉譯（DNAT / Port Forwarding 連接埠轉發）",
          "來源端網路位址轉譯（SNAT）",
          "靜態 MAC 轉譯",
          "動態路由震盪"],
         "SNAT vs DNAT 核心區辨：1. SNAT（Source NAT）：用於內部私有 IP「主動連線出網際網路」，將連線封包的「來源 IP」替換為公網 IP；2. DNAT（Destination NAT / 虛擬伺服器 Virtual Server / Port Forwarding）：用於外部公網使用者「主動連入內部伺服器」，防火牆攔截抵達公網 IP:Port 的請求，將封包的「目的 IP:Port」重寫為內部伺服器的私有 IP:Port 並轉發。"),

        ("在大型寬頻電信網路中，由於 IPv4 公有位址嚴重不足，電信業者在核心網普遍導入「電信級 NAT（CGNAT / Carrier-Grade NAT）」，依據 RFC 6598 規範，專屬分配給 CGNAT 之特殊保留 IP 位址區段為？",
         "<code>100.64.0.0/10</code>（範圍 100.64.0.0 至 100.127.255.255）",
         ["<code>100.64.0.0/10</code>（範圍 100.64.0.0 至 100.127.255.255）",
          "<code>192.168.0.0/16</code>",
          "<code>10.0.0.0/8</code>",
          "<code>127.0.0.0/8</code>"],
         "CGNAT（RFC 6598 Shared Address Space）：寬頻用戶家中分享器拿到的 WAN IP 很多時候並非真實 Public IP，而是 <code>100.64.0.0/10</code>。這是 IANA 專門給 ISP 業者做二次 NAT（NAT444 架構）使用的共享位址空間，防止與企業用戶內部常用的 RFC 1918 私有 IP（10.x 或 192.168.x）產生 IP 位址衝突。缺點為用戶端難以自建伺服器對外直連。"),

        ("某區公所公務印表機需要維持固定不變的 IP 位址（如 <code>192.168.1.200</code>），但網管人員希望統一由 DHCP 伺服器集中管理設定而不手動在印表機面板上寫死靜態 IP，最佳設定作法為？",
         "在 DHCP 伺服器中建立「靜態保留 / 靜態預留（DHCP Reservation / MAC-IP 綁定）」",
         ["在 DHCP 伺服器中建立「靜態保留 / 靜態預留（DHCP Reservation / MAC-IP 綁定）」",
          "縮短 DHCP 租約時間至 1 秒鐘",
          "關閉印表機電源",
          "每次列印前重新拔插網路線"],
         "DHCP 靜態保留（Reservation）：在 DHCP 伺服器設定檔中，將印表機的實體 MAC 位址與指定 IP 永久綁定。當印表機發送 DHCP Discover 時，DHCP 伺服器永遠只分配該特定 IP 給它，同時自動下發閘道器與 DNS。既享有固定 IP 的服務穩定性，又享有集中管理的彈性（日後更換 DNS 或 Gateway 無需逐台設備手動改機）。"),

        ("客戶端電腦在取得 DHCP 租約後，當租約有效時間進行至「50%（T1 時間）」時，客戶端依標準程序應當採取的租約更新動作為？",
         "向原先發放該租約之 DHCP 伺服器發送單播（Unicast）「DHCP Request」請求延長租約",
         ["向原先發放該租約之 DHCP 伺服器發送單播（Unicast）「DHCP Request」請求延長租約",
          "向全區域網路發送廣播 DHCP Discover 重新要求全新 IP",
          "立即停止連線並將 IP 釋放歸還",
          "關閉電腦作業系統網路卡"],
         "DHCP 租約更新兩大時間點：1. T1（租約 50%）：客戶端以單播直接詢問原發證的 DHCP 伺服器「請求續約」，若伺服器在線回覆 DHCP Ack，租約計時器重置為 100%；2. T2（租約 87.5%）：若 T1 續約失敗（原伺服器重開機或故障），在 87.5% 時間點客戶端轉為「全網廣播 DHCP Request」，嘗試向區域網路內任何其他可用的 DHCP 伺服器請求續約。若租約 100% 屆滿仍無回應，才釋放 IP 重新從 Discover 開始。"),

        ("在 DNS 網域名稱階層體系中，我國政府機關網域名稱（如 <code>www.moi.gov.tw</code>），其中的「<code>.tw</code>」與「<code>.gov.tw</code>」在階層架構中分別屬於？",
         "<code>.tw</code> 為國家代碼頂級網域（ccTLD）；<code>.gov.tw</code> 為二級專用屬性網域（Second-Level Domain）",
         ["<code>.tw</code> 為國家代碼頂級網域（ccTLD）；<code>.gov.tw</code> 為二級專用屬性網域（Second-Level Domain）",
          "<code>.tw</code> 為根網域，<code>.gov.tw</code> 為主機名稱",
          "兩者皆為通用頂級網域（gTLD）",
          "兩者皆為本地交換器專用名稱"],
         "DNS 階層樹狀架構：1. Root Domain：以「.」代表，全球 13 組根伺服器節點（A~M）；2. TLD（頂級網域）：包含通用 gTLD（.com, .org, .edu）與國家代碼 ccTLD（.tw, .jp, .uk）；3. SLD（二級網域）：如台灣由 TWNIC 管理之屬性型網域 <code>.gov.tw</code>（政府專用）、<code>.edu.tw</code>（教育）、<code>.com.tw</code>（商業）；4. 子網域（Subdomain）：如 <code>moi</code>（內政部）；5. 主機名稱：如 <code>www</code>。"),

        ("為防止中間人攻擊者偽造 DNS 應答以進行「DNS 快取毒化（Cache Poisoning）」將民眾導向釣魚網站，數位發展部推動政府機關導入之 DNS 密碼學安全防禦標準為？",
         "DNSSEC（網域名稱系統安全擴充協定，DNS Security Extensions）",
         ["DNSSEC（網域名稱系統安全擴充協定，DNS Security Extensions）",
          "DNS Round Robin",
          "Dynamic DNS",
          "DNS Zone Transfer"],
         "DNSSEC 防毒化機制：傳統 DNS 查詢採明文 UDP，任何人皆可搶先偽造回應欺騙快取。DNSSEC 採用非對稱密碼學技術，權威伺服器利用私鑰對資源紀錄進行數位簽章（生成 RRSIG 紀錄），並在母網域與子網域之間建立「信任鏈（Chain of Trust，透過 DS 紀錄與 DNSKEY 驗證）」。遞迴 DNS 收到解析結果時驗證其公鑰數位簽章，若簽章不符立即拋棄，確保資料來源真實性與內容完整性。"),

        ("在跨網際網路（Internet）之各大自治系統（AS, Autonomous System）之間，用以交換路由資訊之唯一核心外部閘道路由協定（EGP）為？",
         "BGP（邊界閘道協定，Border Gateway Protocol，目前主要版本為 BGP-4）",
         ["BGP（邊界閘道協定，Border Gateway Protocol，目前主要版本為 BGP-4）",
          "RIP 協定",
          "OSPF 協定",
          "IS-IS 協定"],
         "BGP（邊界閘道協定）特性：BGP 是驅動全球 Internet 運作的動態路由骨幹。屬於「路徑向量協定（Path-Vector Protocol）」。特點：1. 運行於 TCP 179 埠之上，連線高度可靠；2. 度量指標不是簡單的頻寬或跳數，而是豐富的 BGP 屬性（如 AS-Path、Local Preference、MED），能支援複雜的商業政策路由（Policy Routing）；3. 藉由記錄完整的 AS-Path 列表，徹底消除跨跨國路由迴路。"),

        ("在路由器路由表中，若同時透過不同管道學到抵達同一個目的網段的路由，路由器依據「管理距離（AD, Administrative Distance）」決定優先採納何者。下列路由來源依 AD 值「由小到大（優先級由最高至最低）」之排列順序何者完全正確？",
         "直連介面（Connected, AD=0） ➔ 靜態路由（Static, AD=1） ➔ OSPF（AD=110） ➔ RIP（AD=120）",
         ["直連介面（Connected, AD=0） ➔ 靜態路由（Static, AD=1） ➔ OSPF（AD=110） ➔ RIP（AD=120）",
          "RIP（AD=0） ➔ OSPF（AD=1） ➔ 靜態路由（AD=110） ➔ 直連介面（AD=120）",
          "靜態路由 ➔ 直連介面 ➔ RIP ➔ OSPF",
          "所有路由來源之 AD 值完全相同皆為 100"],
         "管理距離（Administrative Distance, AD）權重：AD 代表路由協定的「可信度（Believability）」，數值越小代表越可信越優先採納入 RIB：1. 直連網路（Directly Connected）：AD = 0；2. 靜態路由（Static Route）：AD = 1；3. eBGP（外部 BGP）：AD = 20；4. EIGRP 內部：AD = 90；5. OSPF：AD = 110；6. IS-IS：AD = 115；7. RIP：AD = 120；8. iBGP：AD = 200；9. 不可達：AD = 255。"),

        ("在商用與公務環境佈設 2.4GHz 無線區域網路（Wi-Fi）時，為避免相鄰無線基地台（AP）之間頻率重疊相互干擾，最常規劃採用之「三個完全互不重疊之頻道組合」為？",
         "頻道 1、頻道 6、頻道 11",
         ["頻道 1、頻道 6、頻道 11",
          "頻道 1、頻道 2、頻道 3",
          "頻道 2、頻道 4、頻道 6",
          "頻道 10、頻道 11、頻道 12"],
         "2.4GHz 頻率規劃原則：2.4GHz 頻段（802.11b/g/n）共劃分 14 個頻道，每個頻道中心頻率僅相隔 5MHz，但單一頻道訊號頻寬佔用約 20~22MHz。因此相鄰頻道訊號嚴重重疊干擾。全球公認唯一的 3 個互不重疊乾淨頻道為 Channel 1（2412MHz）、Channel 6（2437MHz）與 Channel 11（2462MHz）。大型機房與辦公大樓佈設多台 AP 時，必須採蜂巢狀交錯配置 1/6/11。"),

        ("在企業級無線區域網路架構中，相較於每台 AP 需個別手動設定的「胖 AP（Fat AP / 自治型 AP）」，地方政府行政大樓多採用「瘦 AP（Fit AP / 集中控管型 AP）」架構，其核心優勢為？",
         "瘦 AP 僅負責純無線射頻收發，所有身分認證、頻道功率調適、漫遊切換與安全策略皆由後端的「無線網路控制器（AC, Wireless Access Controller）」集中管理",
         ["瘦 AP 僅負責純無線射頻收發，所有身分認證、頻道功率調適、漫遊切換與安全策略皆由後端的「無線網路控制器（AC, Wireless Access Controller）」集中管理",
          "瘦 AP 外殼體積只有一般 AP 的百分之一且完全無須供電",
          "瘦 AP 只能連接一台筆記型電腦",
          "瘦 AP 必須使用手動轉盤調整頻道"],
         "Fat AP vs Fit AP 集中管理：1. Fat AP（自治型）：每台 AP 擁有完整的作業系統、路由與安全設定，若機關有 200 台 AP，更改 Wi-Fi 密碼或升級韌體需登入 200 次，難以維護；2. Fit AP + AC 架構：AP 透過 CAPWAP 通道（RFC 5415）自動向集中式 AC 控制器註冊，AC 一鍵下發 SSID、VLAN 與射頻優化，並支援 AP 間快速無縫漫遊（802.11r/k/v）與非法 AP 偵測（WIPS），是現代智慧政府標準規範。"),

        ("在無線網路 802.11 安全架構中，公務機關同仁在辦公室連接 Wi-Fi 時，不使用共用固定密碼，而是輸入個人公務帳號與密碼，由後端 RADIUS 伺服器進行身分驗證，此架構屬於？",
         "WPA2/WPA3 企業級認證（Enterprise Mode，基於 IEEE 802.1X / EAP 架構）",
         ["WPA2/WPA3 企業級認證（Enterprise Mode，基於 IEEE 802.1X / EAP 架構）",
          "WPA-Personal（預先共享金鑰 PSK 模式）",
          "WPS 一鍵按鈕連線模式",
          "開放式無密碼認證"],
         "802.1X 企業認證架構：Personal 模式所有人共用同一組密碼，同仁離職必須全機關改密碼；802.1X Enterprise 模式包含三大角色：1. 請求者（Supplicant / 終端裝置）；2. 認證者（Authenticator / 無線 AP 或交換器）；3. 認證伺服器（Authentication Server / 通常為 RADIUS 結合機關 Active Directory / LDAP）。每位同仁使用個人獨立公務帳號，支援多因素驗證（MFA）與動態派發獨立傳輸金鑰，離職只需停用帳號即可。"),

        ("現代瀏覽器與網頁伺服器建立安全加密連線時採用 HTTPS（TCP 埠 443），其底層採用之 TLS 1.3 協定相較於舊版 TLS 1.2，在連線交握延遲上取得之重大突破為？",
         "將完整的加密交握往返時間由 2-RTT 縮減至 1-RTT，並支援 0-RTT 早期資料快速恢復連線",
         ["將完整的加密交握往返時間由 2-RTT 縮減至 1-RTT，並支援 0-RTT 早期資料快速恢復連線",
          "將資料傳輸速度限制為 56 Kbps",
          "完全放棄非對稱金鑰交換改用明文傳輸",
          "要求伺服器必須重新啟動方可連線"],
         "TLS 1.3 革命性升級（RFC 8446）：1. 效能倍增：TLS 1.2 需要 2 個往返（2-RTT）完成交握；TLS 1.3 將金鑰協商（Diffie-Hellman）直接整合入 Client Hello 與 Server Hello 中，初次交握僅需 1-RTT；若之前連線過，更支援 0-RTT（無需交握直接在第一包送出請求）；2. 資安提升：徹底廢除不安全的舊加密演算法（如 RC4、3DES、MD5、SHA-1 以及靜態 RSA 金鑰交換），全面強制具備完全前向保密性（PFS）。"),

        ("比較遠端連線終端工具「Telnet」與「SSH（Secure Shell）」之安全性，下列敘述何者完全正確？",
         "Telnet（TCP 埠 23）所有傳輸內容（包含帳號密碼與終端指令）皆為明文傳輸，極易在網路上遭監聽竊取；SSH（TCP 埠 22）全流程經過高強度對稱/非對稱密碼學加密與完整性驗證",
         ["Telnet（TCP 埠 23）所有傳輸內容（包含帳號密碼與終端指令）皆為明文傳輸，極易在網路上遭監聽竊取；SSH（TCP 埠 22）全流程經過高強度對稱/非對稱密碼學加密與完整性驗證",
          "Telnet 安全性遠高於 SSH",
          "SSH 是微軟 Windows 專用私有協定，Linux 無法使用",
          "兩者完全相同，僅為通訊埠號不同"],
         "Telnet vs SSH 安全分野：早期 Unix 伺服器廣泛使用 Telnet，但在 Hub 或未加密 Wi-Fi 環境中，攻擊者只需開啟 Wireshark 即可一字不漏看到管理員輸入的 root 密碼與機敏指令。SSH 採用強大非對稱金鑰交換、AES 對稱加密與 HMAC/SHA-2 完整性防篡改校驗，並支援 SFTP 加密傳檔與 X11/連接埠安全轉發（SSH Tunneling），公務機關資安法規嚴禁任何 Telnet 明文通訊。"),

        ("網路管理員在排除網路故障時，使用 <code>traceroute</code>（Windows 為 <code>tracert</code>）追蹤封包自本地到達目的主機所行經之所有路由器節點，其能依序獲取沿途各跳躍點 IP 之核心原理為？",
         "依序發送 TTL 數值由 1, 2, 3... 逐次遞增的探測封包，利用各路由器在 TTL 歸零時回傳之「ICMP Time Exceeded（Type 11）」訊息解析路由器 IP",
         ["依序發送 TTL 數值由 1, 2, 3... 逐次遞增的探測封包，利用各路由器在 TTL 歸零時回傳之「ICMP Time Exceeded（Type 11）」訊息解析路由器 IP",
          "直接向中華電信機房發送電子郵件索取路徑圖",
          "在每個封包中強制寫入 GPS 衛星定位座標",
          "要求路由器主動關閉所有防火牆介面"],
         "traceroute 實作原理：1. 發送第 1 個封包，TTL = 1。第一台路由器收到後將 TTL 減 1 變為 0，丟棄封包並回傳 ICMP Type 11，發送端由此得知第 1 個 Hop 的 IP 與 RTT；2. 發送第 2 個封包，TTL = 2，第一台路由器放行（TTL變1），第二台路由器將其歸零並回傳 ICMP，得知第 2 跳 IP；3. 依此類推不斷遞增，直到封包抵達目標主機回傳 ICMP Port Unreachable（UDP模式）或 Echo Reply（Windows ICMP模式）結束。")
    ]

    all_datasets = [
        ("網路模型、實體層與鏈結層 (OSI/TCP-IP, 乙太網, VLAN, STP)", data1),
        ("網路層與傳輸層協定 (IPv4/IPv6, CIDR, ARP, ICMP, TCP/UDP)", data2),
        ("網路服務、路由協定、無線網路與 VPN 遠端辦公", data3)
    ]

    for tag, dataset in all_datasets:
        for stem, ans_s, opts, expl in dataset:
            choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
            qs.append({
                "tag": "資通網路與安全概要",
                "stem": stem,
                "choices": choices,
                "ans": "A",
                "ans_text": f"(A) {ans_s}",
                "explanation": f"""<strong>【地方特考四等公務實務情境深度解析】</strong><br>
<div class="step-box">
  <div class="step-title">🌐 地方政府資通網路架構、協定分析與連線實務剖析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>釐清網路協定階層、硬體規格與機關實務環境</strong><br>
      ‧ 本題依據國家考試地方特考四等《資通網路與安全概要》考綱，緊扣 OSI 網路模型、TCP/IP 通訊協定、子網劃分計算與無線/VPN 架構嚴謹命題。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>詳細計算推導與通訊協定邏輯對照</strong><br>
      ‧ {expl}
    </li>
  </ul>
</div>
<br><strong>【各選項詳細對錯解析】</strong><br>
‧ <strong>(A) 正確</strong>：{opts[0]}。<br>
‧ <strong>(B) 錯誤</strong>：{opts[1]}（協定層級認知錯誤、子網計算偏差或架構觀念混淆）。<br>
‧ <strong>(C) 錯誤</strong>：{opts[2]}（極端荒謬之技術處置或錯誤之名詞定義）。<br>
‧ <strong>(D) 錯誤</strong>：{opts[3]}（非業界規範或違背網際網路標準 RFC 規範）。<br><br>
<strong>地特加分角度</strong>：地方特考四等在網路考科中，<strong>CIDR 子網路遮罩與可用主機計算</strong>、<strong>TCP 三向交握與滑動視窗</strong>、<strong>VLAN / STP 運作機制</strong>與<strong>DNS/DHCP 解析流程</strong>為高頻必考命題。作答時清楚掌握<strong>協定封裝細節</strong>，可穩拿最高分。"""
            })

    return qs

if __name__ == '__main__':
    qs = get_local4_part3_questions()
    print(f"Total Part 3 questions generated: {len(qs)}")
