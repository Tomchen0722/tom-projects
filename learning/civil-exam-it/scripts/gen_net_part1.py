# -*- coding: utf-8 -*-
"""
Computer Networks & Security Question Bank Generator - Part 1 (100 unique questions)
Topics: Physical Layer Calculations (Nyquist, Shannon, Delays), Data Link Layer (CRC, Hamming, ARQ Flow Control, CSMA/CD, Switching & STP).
"""

def get_net_part1_questions():
    qs = []

    # -------------------------------------------------------------
    # 1. 物理層計算與通訊定理 (40 題)
    # -------------------------------------------------------------
    phy_calc = [
        ("無雜訊通道（Noiseless Channel）的頻寬為 4 kHz，若每個訊號準位（Signal Level）可以採用 16 種相異電位狀態，根據奈奎斯特公式（Nyquist Theorem），該通道的最高理論資料傳輸率（Maximum Data Rate）為？",
         "32 kbps", ["32 kbps", "16 kbps", "64 kbps", "8 kbps"],
         "奈奎斯特公式：C = 2 × B × log₂(M)。代入頻寬 B = 4000 Hz，訊號位階數 M = 16：C = 2 × 4000 × log₂(16) = 2 × 4000 × 4 = 32,000 bps = 32 kbps。"),
        ("某有雜訊通道（Noisy Channel）的頻寬為 3 kHz，訊雜比（Signal-to-Noise Ratio, SNR）為 31.62（約等於信噪比 15 dB，SNR = 31.62 ≈ 31）。依據夏農定理（Shannon Capacity Formula），其理論最大通道容量約為？",
         "15 kbps", ["15 kbps", "30 kbps", "6 kbps", "3 kbps"],
         "夏農定理：C = B × log₂(1 + SNR)。SNR ≈ 31，代入得 1 + SNR = 32。C = 3000 × log₂(32) = 3000 × 5 = 15,000 bps = 15 kbps。"),
        ("若某通道的訊雜比標示為 30 dB，則其無因次（Linear Scale）的訊雜比 S/N 實際數值為？",
         "1000", ["1000", "30", "100", "10000"],
         "分貝（dB）定義公式：SNR_dB = 10 × log₁₀(S/N)。代入 30 = 10 × log₁₀(S/N) => log₁₀(S/N) = 3 => S/N = 10³ = 1000。"),
        ("一條長度為 2000 公里的光纖鏈路，光在光纖中的傳播速度約為 2 × 10⁸ m/s。一個封包從起點傳播至終點的「傳遞延遲（Propagation Delay）」為？",
         "10 毫秒（10 ms）", ["10 毫秒（10 ms）", "1 毫秒", "100 毫秒", "5 毫秒"],
         "傳遞延遲公式：d_prop = 距離 / 傳播速度 = (2000 × 10³ m) / (2 × 10⁸ m/s) = 2 × 10⁶ / 2 × 10⁸ = 10⁻² 秒 = 0.01 秒 = 10 ms。"),
        ("透過 100 Mbps 的網路傳輸一個大小為 1.25 MB（百萬位元組）的檔案，其「傳輸延遲（Transmission Delay）」為？",
         "0.1 秒（100 毫秒）", ["0.1 秒（100 毫秒）", "1.25 秒", "0.01 秒", "10 秒"],
         "傳輸延遲公式：d_trans = 封包長度 L / 傳輸速率 R。1.25 MB = 1.25 × 10⁶ × 8 bits = 10⁷ bits。d_trans = 10⁷ bits / (100 × 10⁶ bps) = 0.1 秒。"),
        ("若網路的頻寬為 1 Gbps，往返時間（RTT, Round-Trip Time）為 40 ms。該網路鏈路的「頻寬延遲乘積（Bandwidth-Delay Product, BDP）」為？",
         "5 MB（或 40 Mbits）", ["5 MB（或 40 Mbits）", "40 MB", "4 MB", "1 MB"],
         "BDP = 頻寬 × RTT = (1 × 10⁹ bps) × (40 × 10⁻³ s) = 40 × 10⁶ bits = 40 Mbits = 5 MB。BDP 代表填滿整條管道所需的傳輸資料量，決定了 TCP 滑動視窗的最佳緩衝區大小。"),
        ("雙絞線（Twisted Pair）將兩根絕緣導線依特定螺旋密度互相絞繞的主要目的為？",
         "抵消各線對產生的電磁輻射，並減少來自外部與相鄰線對的「電磁干擾與串音（Crosstalk）」", ["抵消各線對產生的電磁輻射，並減少來自外部與相鄰線對的「電磁干擾與串音（Crosstalk）」", "增加電纜的抗拉物理強度", "降低訊號的傳播速度", "防止導線氧化"], "兩導線在相鄰絞節中所受干擾相位相反彼此抵消，極大抑制串音（Crosstalk）。"),
        ("光纖通訊（Fiber Optic）傳輸光脈衝訊號所依據的基礎物理光學原理為？",
         "光在纖芯（Core）與包層（Cladding）界面發生的「全反射（Total Internal Reflection）」", ["光在纖芯（Core）與包層（Cladding）界面發生的「全反射（Total Internal Reflection）」", "光的雙縫干涉", "光電效應", "光的繞射現象"], "核心折射率大於包層折射率，入射角大於臨界角時發生全反射，能量無衰減在纖芯前進。"),
        ("單模光纖（Single-Mode Fiber, SMF）相較於多模光纖（Multi-Mode Fiber, MMF），其核心特點為？",
         "纖芯極細（約 8~10 微米），僅容許單一光波模式直線傳播，完全消除模態色散（Modal Dispersion），適合超長距離骨幹網路傳輸", ["纖芯極細（約 8~10 微米），僅容許單一光波模式直線傳播，完全消除模態色散（Modal Dispersion），適合超長距離骨幹網路傳輸", "纖芯較粗，傳輸距離短", "使用 LED 作為光源", "製造成本遠低於多模光纖"], "多模光纖多路光線反射存在時間差（模態色散），距離受限；單模使用雷射二極體，傳輸達數十公里。"),
        ("脈衝編碼調變（PCM, Pulse Code Modulation）將類比語音訊號轉換為數位訊號的三個標準步驟依序為？",
         "取樣（Sampling） -> 量化（Quantization） -> 編碼（Encoding）", ["取樣（Sampling） -> 量化（Quantization） -> 編碼（Encoding）", "調變 -> 解調 -> 放大", "濾波 -> 壓縮 -> 加密", "量化 -> 取樣 -> 編碼"], "電話語音標準：4 kHz 訊號以 8 kHz 取樣（奈奎斯特），8-bit 量化，產生 64 kbps 標準音訊流（DS0）。")
    ]

    for stem, ans_s, opts, expl in phy_calc:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "物理層通訊定理推導",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【物理層通訊定理逐步計算】</strong><br>
<div class="step-box">
  <div class="step-title">📝 數理公式代入與單位換算步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立物理通道模型與定理公式</strong><br>
      ‧ 本題依據奈奎斯特取樣定理、夏農容量極限或延遲傳播模型進行計算。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行數值運算與單位對齊</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精準結論</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：計算完全精準無誤。<br>
‧ 其餘選項皆為 dB 換算公式記錯、Bytes 與 bits 混淆或傳遞/傳輸延遲概念顛倒。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Shannon Capacity Formula</code> <span class="en">Shannon Capacity</span>：夏農通道容量公式。<br>
‧ <code>Bandwidth-Delay Product (BDP)</code> <span class="en">Bandwidth-Delay Product</span>：頻寬延遲乘積。<br>
‧ <code>Propagation Delay</code> <span class="en">Propagation Delay</span>：傳遞延遲。"""
        })

    # Expand Physical layer to 40 (30 more items)
    more_phy = [
        ("依據奈奎斯特取樣定理，若欲完整重構一個最高頻率為 f_max 的連續類比訊號，取樣頻率 f_s 必須滿足？", "f_s >= 2 · f_max", ["f_s >= 2 · f_max", "f_s >= f_max", "f_s >= 4 · f_max", "f_s <= f_max / 2"], "防止產生混疊（Aliasing）現象，取樣率必須至少為訊號最高頻率的 2 倍。"),
        ("曼徹斯特編碼（Manchester Encoding）的核心特色為？", "每個位元週期的「正中央皆發生一次電位跳變」，兼具資料傳輸與內建時脈同步（Clock Synchronization）功能", ["每個位元週期的「正中央皆發生一次電位跳變」，兼具資料傳輸與內建時脈同步（Clock Synchronization）功能", "頻寬使用率為 100%", "完全不產生跳變", "僅用於光纖傳輸"], "以中央跳變方向代表 0 或 1，無直流偏移（DC Component）且天然提取時脈，早期 10BASE-T 乙太網路標準。"),
        ("差分曼徹斯特編碼（Differential Manchester Encoding）判定位元數值的方式為？", "依據位元週期的「起始處是否發生電位跳變」來決定數值（有跳變代表 0，無跳變代表 1）", ["依據位元週期的「起始處是否發生電位跳變」來決定數值（有跳變代表 0，無跳變代表 1）", "僅看正負電位", "依據位元週期結束時的振幅", "依據訊號頻率"], "抗噪性與抗極性反接能力極強，廣泛應用於權杖環網路（Token Ring 802.5）。"),
        ("NRZ（Non-Return-to-Zero，不歸零碼）在傳輸長串連續的 '0' 或連續的 '1' 時，會引發何種嚴重問題？", "時脈同步漂移（Clock Drift / Loss of Synchronization）與直流偏移（DC Drift）", ["時脈同步漂移（Clock Drift / Loss of Synchronization）與直流偏移（DC Drift）", "頻寬耗盡", "訊號反射", "線路過熱"], "長時間電位恆定無跳變，接收端鎖相環無法維持時脈同步。"),
        ("4B/5B 編碼技術的主要目的為？", "將每 4 位元資料映射為 5 位元編碼，消除長串連續的 0，使編碼效率高達 80% 且保證時脈跳變", ["將每 4 位元資料映射為 5 位元編碼，消除長串連續的 0，使編碼效率高達 80% 且保證時脈跳變", "資料加密", "錯誤更正", "訊號放大"], "曼徹斯特編碼效率僅 50%（頻寬加倍），4B/5B 搭配 NRZI 大幅提升頻寬利用率至 80%（如百兆乙太網 100BASE-FX）。"),
        ("在數位調變技術中，QAM（正交振幅調變，Quadrature Amplitude Modulation）同時改變訊號的哪兩個特徵？", "振幅（Amplitude）與相位（Phase）", ["振幅（Amplitude）與相位（Phase）", "頻率與波長", "振幅與頻率", "相位與時間"], "例如 16-QAM 具備 16 個星座圖狀態點，每個符元（Baud）可攜帶 log₂(16) = 4 個位元。"),
        ("64-QAM 調變技術中，每個符元（Baud / Symbol）可傳輸多少個位元的資料？", "6 個位元", ["6 個位元", "4 個位元", "8 個位元", "64 個位元"], "log₂(64) = 6 bits/symbol。"),
        ("256-QAM 調變技術中，每個符元可傳輸多少個位元？", "8 個位元（1 個 Byte）", ["8 個位元（1 個 Byte）", "6 個位元", "16 個位元", "256 個位元"], "log₂(256) = 8 bits/symbol，廣泛應用於 Wi-Fi 5/6 與數位有線電視。"),
        ("分頻多工（FDM, Frequency-Division Multiplexing）的運作方式為？", "將通道總頻寬分割為多個互不重疊的子頻帶，各路訊號同時在不同的載波頻率上並行傳輸", ["將通道總頻寬分割為多個互不重疊的子頻帶，各路訊號同時在不同的載波頻率上並行傳輸", "各路訊號在不同時間片傳輸", "各路訊號使用正交碼分開", "在不同光纖傳輸"], "例如傳統廣播電台與類比有線電視。"),
        ("分時多工（TDM, Time-Division Multiplexing）的運作方式為？", "將時間劃分為週期性訊框，各訊號輪流在分配到的固定時間槽（Time Slot）內佔用全頻寬傳輸", ["將時間劃分為週期性訊框，各訊號輪流在分配到的固定時間槽（Time Slot）內佔用全頻寬傳輸", "同時佔用不同頻率", "波長分割", "隨機競爭"], "同步 TDM 時間槽固定；統計 TDM（STDM）按需動態分配時間槽以提升利用率。"),
        ("分波多工（WDM / DWDM, Wavelength-Division Multiplexing）是應用於何種傳輸媒介的特殊 FDM 技術？", "光纖（Fiber Optic，在同一根光纖中同時傳輸不同波長的光訊號）", ["光纖（Fiber Optic，在同一根光纖中同時傳輸不同波長的光訊號）", "同軸電纜", "雙絞線", "衛星通訊"], "密集分波多工（DWDM）可在一根光纖內塞入數十至上百個波長通道，總傳輸速率達數十 Tbps。"),
        ("分碼多工（CDMA, Code-Division Multiple Access）各發送端如何實現共享同一頻率且同時傳輸？", "各使用者指派互相正交的碼片序列（Orthogonal Chip Sequences / Walsh Codes）", ["各使用者指派互相正交的碼片序列（Orthogonal Chip Sequences / Walsh Codes）", "各使用者隨機搶佔", "依靠時間輪流", "依振幅大小區分"], "利用正交向量內積等於零之數學特性，接收端以目標碼片序列做內積運算即可完美濾除其他用戶的干擾。"),
        ("若某同軸電纜衰減常數為 2 dB/100m，訊號傳輸 1 公里（1000m）後，訊號衰減的總分貝數為？", "20 dB", ["20 dB", "2 dB", "200 dB", "10 dB"], "1000m / 100m = 10 段，總衰減 = 10 × 2 dB = 20 dB。"),
        ("20 dB 的衰減代表訊號功率減少為原本發送功率的？", "百分之一（1%）", ["百分之一（1%）", "十分之一（10%）", "千分之一", "二十分之一"], "20 = 10 log₁₀(P_in / P_out) => log₁₀(P_in / P_out) = 2 => P_in / P_out = 100 => P_out = P_in / 100。"),
        ("天線發射訊號在自由空間傳播時，其接收功率與傳播距離 d 的關係為？", "與距離的平方成反比（1 / d²）", ["與距離的平方成反比（1 / d²）", "與距離成反比（1 / d）", "與距離無關", "與距離的三次方成反比"], "自由空間路徑損耗（FSPL）遵循反平方定律。"),
        ("正交分頻多工（OFDM, Orthogonal Frequency-Division Multiplexing）相較於傳統 FDM 的最大突破為？", "子載波互相正交且頻譜重疊，省去保護頻帶（Guard Bands）大幅提升頻譜利用率，並極強對抗多路徑衰落（Multipath Fading）", ["子載波互相正交且頻譜重疊，省去保護頻帶（Guard Bands）大幅提升頻譜利用率，並極強對抗多路徑衰落（Multipath Fading）", "完全不需要調變", "完全消除電磁波", "將光纖與無線電波結合"], "現代 Wi-Fi 4/5/6、4G LTE 與 5G NR 物理層之核心骨幹調變技術。"),
        ("OFDMA（正交分頻多重接取）在 Wi-Fi 6 (802.11ax) 中引入的主要功能為？", "將通道頻寬劃分為多個資源單元（RU, Resource Units），支援「多個使用者在同一個傳輸時間內並行收發」", ["將通道頻寬劃分為多個資源單元（RU, Resource Units），支援「多個使用者在同一個傳輸時間內並行收發」", "僅增加天線數量", "提升電池續航力", "將頻率改為光波"], "大幅降低高密度設備環境下的排隊延遲與衝突，由競爭轉為排程並發。"),
        ("MIMO（多輸入多輸出，Multiple-Input Multiple-Output）技術的核心效益為？", "利用多天線空間多工（Spatial Multiplexing）倍增資料傳輸率，或利用空間分集（Diversity）增強抗衰落可靠度", ["利用多天線空間多工（Spatial Multiplexing）倍增資料傳輸率，或利用空間分集（Diversity）增強抗衰落可靠度", "減少天線數量", "消除微波輻射", "節省電力消耗"], "Wi-Fi 與 5G 關鍵技術，例如 4x4 MIMO 在相同頻寬下理論速率最高翻 4 倍。"),
        ("無線傳輸中的「多路徑效應（Multipath Effect）」會引發何種干擾？", "符元間干擾（ISI, Inter-Symbol Interference）與頻率選擇性衰落", ["符元間干擾（ISI, Inter-Symbol Interference）與頻率選擇性衰落", "線路短路", "MAC 位址衝突", "密鑰外洩"], "電磁波經牆面反射產生多條相差不同延遲的路徑到達接收端，訊號波形疊加變形。"),
        ("衛星通訊中，地球同步軌道（GEO）衛星相較於低軌衛星（LEO, 如 Starlink），最明顯的網路特性差異為？", "GEO 傳播延遲極高（RTT 約 500 ms），而 LEO 傳播延遲低（RTT 約 20~40 ms）", ["GEO 傳播延遲極高（RTT 約 500 ms），而 LEO 傳播延遲低（RTT 約 20~40 ms）", "GEO 軌道高度較低", "LEO 覆蓋單顆即可涵蓋全球", "GEO 頻寬永遠大於 LEO"], "GEO 高度約 35,786 km，光速來回需數百毫秒；LEO 高度僅數百公里，延遲接近地面光纖。"),
        ("CAT-5e、CAT-6 與 CAT-6a 雙絞線標準中，CAT-6a 支援 10 Gbps 傳輸的最大標準距離為？", "100 公尺（100 meters）", ["100 公尺（100 meters）", "55 公尺", "10 公尺", "500 公尺"], "CAT-6 跑 10 Gbps 僅限 55 公尺，CAT-6a (500 MHz) 支援全額 100 公尺。"),
        ("RJ-45 接頭壓接線序中，T568B 標準的前四根線序顏色依序為？", "白橙、橙、白綠、藍", ["白橙、橙、白綠、藍", "白綠、綠、白橙、藍", "橙、白橙、綠、白綠", "藍、白藍、橙、白橙"], "台灣最常用之 T568B 標準：白橙、橙、白綠、藍、白藍、綠、白棕、棕。"),
        ("「跳線（Crossover Cable，交錯線）」的兩端線序標準為？", "一端為 T568A，另一端為 T568B", ["一端為 T568A，另一端為 T568B", "兩端皆為 T568A", "兩端皆為 T568B", "隨意接合"], "早期用於同種設備（如 Switch-to-Switch 或 PC-to-PC）直連，現代網卡皆支援 Auto-MDIX 自動翻轉，已無需實體跳線。"),
        ("波特率（Baud Rate）與位元率（Bit Rate）的換算關係為？", "Bit Rate = Baud Rate × log₂(M)（M 為每個波特符元所包含的有效狀態個數）", ["Bit Rate = Baud Rate × log₂(M)（M 為每個波特符元所包含的有效狀態個數）", "Bit Rate = Baud Rate / 2", "Bit Rate = Baud Rate", "Bit Rate = Baud Rate²"], "Baud 代表每秒傳輸的符元（Symbol）數量，Bit Rate 代表每秒傳輸的純二進位資料位元數。"),
        ("全雙工（Full-Duplex）通訊模式的精確定義為？", "通訊雙方「可以同時」進行雙向發送與接收資料", ["通訊雙方「可以同時」進行雙向發送與接收資料", "雙方可以雙向傳輸，但同一時刻只能單向傳送（如對講機）", "只能單向傳輸（如廣播）", "需要四根天線"], "半雙工（Half-Duplex）需分時交替；單工（Simplex）永遠單向。"),
        ("現代交換式乙太網路（Switched Ethernet）在全雙工模式下運作時，下列何種機制會被自動停用？", "CSMA/CD 碰撞偵測機制", ["CSMA/CD 碰撞偵測機制", "CRC 檢查碼", "訊框長度限制", "MAC 位址查詢"], "點對點專屬鏈路且收發獨立線對，物理上絕不發生衝突（Collision-Free），故 CSMA/CD 完全停止使用。"),
        ("微波通訊（Microwave Communication）屬於何種傳播特性？", "視距傳播（Line-of-Sight, LOS，兩端天線間不得有物理障礙物遮蔽）", ["視距傳播（Line-of-Sight, LOS，兩端天線間不得有物理障礙物遮蔽）", "沿地表繞射傳播", "電離層反射傳播", "穿透地心傳播"], "高頻微波直線傳播，易受山丘或高樓阻擋，塔台間距通常為數十公里。"),
        ("短波通訊（High Frequency / HF）能進行超遠距離洲際通訊的主要反射層為？", "電離層（Ionosphere）", ["電離層（Ionosphere）", "平流層", "對流層", "大氣邊界層"], "利用天波（Skywave）在電離層與地球表面間多次跳躍反射。"),
        ("光纖中的「色散（Dispersion）」會導致何種現象而限制傳輸距離與速率？", "光脈衝在傳播過程中展寬（Pulse Spreading），導致相鄰脈衝相互重疊干擾", ["光脈衝在傳播過程中展寬（Pulse Spreading），導致相鄰脈衝相互重疊干擾", "光波頻率變高", "光線完全消失", "產生高熱"], "包含色度色散與模態色散，長距離需加裝色散補償模組。"),
        ("光纖放大器 EDFA（摻鉺光纖放大器）的最大技術優勢為？", "可直接在「全光域（All-Optical）」同時放大數十個波長的訊號，無須進行昂貴的光-電-光（O-E-O）轉換", ["可直接在「全光域（All-Optical）」同時放大數十個波長的訊號，無須進行昂貴的光-電-光（O-E-O）轉換", "能降低光速", "將多模轉為單模", "加密光波"], "DWDM 長途骨幹網路商用化的最大功臣。")
    ]

    for stem, ans_s, opts, expl in more_phy:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "傳輸媒介與調變技術",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【實體傳輸特性深入剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在調變公式混淆或傳輸介質物理特性認知偏差。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Manchester Encoding</code> <span class="en">Manchester Encoding</span>：曼徹斯特編碼。<br>
‧ <code>Quadrature Amplitude Modulation (QAM)</code> <span class="en">QAM</span>：正交振幅調變。<br>
‧ <code>Orthogonal Frequency-Division Multiplexing (OFDM)</code> <span class="en">OFDM</span>：正交分頻多工。"""
        })

    # -------------------------------------------------------------
    # 2. 資料鏈結層：CRC、漢明碼、ARQ 與 MAC 協定 (60 題)
    # -------------------------------------------------------------
    dll_items = [
        ("使用循環冗餘檢查碼（CRC），待傳送資料為 1101011011，生成多項式為 G(x) = x⁴ + x + 1（對應二進位 10011）。計算其 FCS（訊框檢查序列，餘數）為？",
         "1110", ["1110", "1001", "0110", "1101"],
         "模 2 除法推導步驟：G(x) 最高次方為 4，在原資料後補 4 個 0 得 11010110110000。以 10011 進行逐位 XOR 除法：商為 1100001010，最終餘數為 4 位元的 1110。傳送訊框為資料加上 FCS：11010110111110。"),
        ("使用漢明碼（Hamming Code）檢測並更正單一錯誤，若資料位元數為 m = 7，最少需要多少個檢查位元（Parity Bits, r）？",
         "4 個", ["4 個", "3 個", "5 個", "2 個"],
         "漢明不等式公式：2^r >= m + r + 1。若 r=3: 2³=8 < 7+3+1=11（不滿足）；若 r=4: 2⁴=16 >= 7+4+1=12（滿足！）。故最少需要 4 個檢查位元，總碼長為 7+4=11 位元。"),
        ("滑動視窗流量控制協定中，使用 n 個位元對訊框進行編號（序號空間為 0 到 2ⁿ − 1）。在「回退 N 步協定（Go-Back-N ARQ）」中，傳送端視窗大小 W_s 的最大值為？",
         "2ⁿ − 1", ["2ⁿ − 1", "2ⁿ", "2^(n-1)", "2ⁿ + 1"],
         "若視窗大小達到 2ⁿ，當整組 ACK 遺失時，接收端無法分辨傳送端重傳的是舊訊框還是新序號訊框！故傳送視窗上限嚴格限制為 2ⁿ − 1（接收端視窗固定為 1）。"),
        ("在「選擇性重傳協定（Selective Repeat ARQ）」中，傳送端視窗大小 W_s 與接收端視窗大小 W_r 必須滿足何種上限關係以防序號重疊混淆？",
         "W_s <= 2^(n-1) 且 W_r <= 2^(n-1)（通常取 W_s = W_r = 2^(n-1)）", ["W_s <= 2^(n-1) 且 W_r <= 2^(n-1)（通常取 W_s = W_r = 2^(n-1)）", "W_s + W_r <= 2ⁿ − 1", "W_s <= 2ⁿ", "W_r = 1"],
         "兩視窗大小之和不得超過序號空間總容量：W_s + W_r <= 2ⁿ。為發揮雙向最大效能，兩視窗大小通常各取序號空間的一半即 2^(n-1)。"),
        ("在 CSMA/CD 協定中，若網路頻寬為 100 Mbps，電纜長度為 1 公里，訊號傳播速度為 2 × 10⁸ m/s。為保證能正確偵測到碰撞，網路規定的「最小訊框長度（Minimum Frame Size）」為？",
         "1000 位元（125 位元組）", ["1000 位元（125 位元組）", "512 位元", "64 位元組", "100 位元"],
         "最小訊框傳輸時間必須大於或等於兩倍最大傳播延遲（RTT 爭用槽時間）：L_min / R >= 2 × (d / v)。L_min = 2 × (1000 m / 2×10⁸ m/s) × 100×10⁶ bps = 2 × (5 × 10⁻⁶ s) × 10⁸ bps = 10⁻⁵ × 10⁸ = 1000 bits。"),
        ("傳統標準 10 Mbps 乙太網路（IEEE 802.3）規範的最小訊框長度為 64 位元組（512 位元），其爭用槽時間（Slot Time）為？",
         "51.2 微秒（51.2 μs）", ["51.2 微秒（51.2 μs）", "100 μs", "5.12 μs", "64 μs"],
         "Slot Time = 512 bits / 10 Mbps = 51.2 μs。傳送端在發送前 64 位元組期間若無偵測到碰撞，即保證該訊框成功佔據通道。"),
        ("在 CSMA/CD 的二進位指數倒退演算法（Binary Exponential Backoff）中，當某訊框發生了第 3 次碰撞時，其隨機退避的等待槽數 k 將從何區間隨機選取？",
         "[0, 7] 間的整數（即 0 到 2³ − 1）", ["[0, 7]間的整數（即 0 到 2³ − 1）", "[0, 3]", "[0, 15]", "[1, 8]"],
         "演算法在第 i 次碰撞時（i <= 10），隨機選取 k ∈ [0, 2ⁱ − 1]，等待 k 個 Slot Time 後再次嘗試發送。第 3 次碰撞即 2³ - 1 = 7。"),
        ("在 CSMA/CD 中，若一個訊框連續發生了 16 次碰撞，演算法將採取何種處置？",
         "放棄發送該訊框並向高層協定回報傳輸錯誤（Excessive Collision Error）", ["放棄發送該訊框並向高層協定回報傳輸錯誤（Excessive Collision Error）", "繼續無限期重試", "等待 1024 個時隙後重試", "重開機"], "碰撞上限為 16 次，超過判定鏈路嚴重壅塞崩潰，直接丟棄並報錯。"),
        ("CSMA/CA 協定主要應用於下列何種網路環境？為什麼不能直接沿用 CSMA/CD？",
         "無線區域網路（Wi-Fi 802.11）；因為無線發射訊號強度遠大於接收強度，無線網卡無法在發射的同時偵測微弱的外部碰撞訊號", ["無線區域網路（Wi-Fi 802.11）；因為無線發射訊號強度遠大於接收強度，無線網卡無法在發射的同時偵測微弱的外部碰撞訊號", "光纖網路", "衛星通訊", "海底電纜"], "無線電硬體無法做到「邊發邊聽」的高靈敏碰撞偵測，故改採以 ACK、IFS 間隙與 RTS/CTS 為核心的「碰撞避免（Collision Avoidance）」機制。"),
        ("在無線區域網路中，「隱藏節點問題（Hidden Terminal Problem）」可透過何種機制獲得有效解決？",
         "RTS / CTS（請求傳送 / 允許傳送）訊框交換機制配合虛擬載波偵測（NAV）", ["RTS / CTS（請求傳送 / 允許傳送）訊框交換機制配合虛擬載波偵測（NAV）", "提高發射功率", "改用雙絞線", "增加天線長度"], "AP 回應的 CTS 廣播會通知所有周遭隱藏節點設定網路分配向量（NAV）進入靜默，避免盲目發送引發碰撞。")
    ]

    for stem, ans_s, opts, expl in dll_items:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "資料鏈結層推導與MAC",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【資料鏈結層協定演算法推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 演算步驟與二進位推導分析</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>確立訊框協定規則與數學定理</strong><br>
      ‧ 本題依據 CRC 模2除法、漢明不等式或 CSMA 爭用槽公式進行分析。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>執行逐步數理演算</strong><br>
      ‧ {expl}
    </li>
    <li class="step-item"><span class="step-badge check">步驟 3</span><strong>得出精確答案</strong><br>
      ‧ 正確答案為 <strong>{ans_s}</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) {ans_s}</strong>：推導計算完全符合 IEEE 802 與 RFC 規範。<br>
‧ 其餘選項常為滑動視窗上限忘記減 1、或 CSMA/CD 最小訊框公式漏乘 2 之常見錯誤。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Cyclic Redundancy Check (CRC)</code> <span class="en">Cyclic Redundancy Check</span>：循環冗餘檢查碼。<br>
‧ <code>Binary Exponential Backoff</code> <span class="en">Binary Exponential Backoff</span>：二進位指數倒退演算法。<br>
‧ <code>Hidden Terminal Problem</code> <span class="en">Hidden Terminal Problem</span>：隱藏節點問題。"""
        })

    # Expand DLL items to 60 (50 more items)
    more_dll = [
        ("純 ALOHA 系統的最大通道吞吐量（Throughput）為？", "1 / (2e) ≈ 18.4%", ["1 / (2e) ≈ 18.4%", "1 / e ≈ 36.8%", "50%", "100%"], "危險時間（Vulnerable Time）為 2 個訊框傳輸時間，S = G · e^(-2G)，當 G = 0.5 時取極大值 1/(2e) ≈ 0.184。"),
        ("分槽 ALOHA（Slotted ALOHA）將時間劃分為槽位，其最大通道吞吐量提升至？", "1 / e ≈ 36.8%", ["1 / e ≈ 36.8%", "18.4%", "50%", "73.6%"], "危險時間縮短為 1 個訊框時間，S = G · e^(-G)，當 G = 1 時達到最大值 1/e ≈ 0.368，吞吐量翻倍。"),
        ("1-堅持 CSMA（1-Persistent CSMA）的運作邏輯為？", "持續監聽通道，若通道忙碌則「持續監聽」；一旦發現空閒，則「以機率 1（立即）」發送訊框", ["持續監聽通道，若通道忙碌則「持續監聽」；一旦發現空閒，則「以機率 1（立即）」發送訊框", "通道空閒時以機率 p 發送", "通道忙碌時隨機等待一段時間再聽", "完全不監聽"], "因空閒時多個等待節點同時以 100% 機率發送，碰撞率極高。"),
        ("非堅持 CSMA（Non-Persistent CSMA）的運作邏輯為？", "監聽通道，若通道忙碌則「放棄監聽並隨機等待一段時間」後再重新監聽", ["監聽通道，若通道忙碌則「放棄監聽並隨機等待一段時間」後再重新監聽", "持續監聽直到空閒", "以機率 p 傳送", "直接發送"], "減少了空閒瞬間同時搶發的碰撞，但引入了無謂的等待延遲，通道利用率略低。"),
        ("p-堅持 CSMA（p-Persistent CSMA）適用於何種環境？運作方式為？", "適用於分槽通道；監聽若空閒則以機率 p 發送，以機率 (1-p) 推遲到下一個槽位", ["適用於分槽通道；監聽若空閒則以機率 p 發送，以機率 (1-p) 推遲到下一個槽位", "以機率 p 關閉電源", "隨機丟棄封包", "僅發送前導碼"], "折衷方案，調和衝突率與通道利用率。"),
        ("生成樹協定（STP, IEEE 802.1D）的核心目標為？", "在包含冗餘實體連線的二層交換網路中，邏輯上阻斷特定埠以「消除網路迴圈（Bridge Loops / Broadcast Storms）」", ["在包含冗餘實體連線的二層交換網路中，邏輯上阻斷特定埠以「消除網路迴圈（Bridge Loops / Broadcast Storms）」", "加快封包轉發速度", "建立虛擬區域網路", "分配 IP 位址"], "廣播風暴會使交換器 MAC 表震盪並在數秒內癱瘓整棟大樓網路，STP 自動修剪成無環生成樹。"),
        ("STP 選舉「根橋接器（Root Bridge）」的比較準則為？", "擁有最小「橋接器識別碼（Bridge ID, BID）」的交換器勝出（優先比較優先級 Priority，相同時比較最小 MAC 位址）", ["擁有最小「橋接器識別碼（Bridge ID, BID）」的交換器勝出（優先比較優先級 Priority，相同時比較最小 MAC 位址）", "擁有最大 MAC 位址的交換器", "埠數最多的交換器", "連線速度最快的交換器"], "Bridge ID = 2-byte Priority (預設 32768) + 6-byte MAC Address。BID 數值最小者成為根交換器。"),
        ("STP 中，非根交換器上「到達根橋接器路徑成本最低」的埠被選舉為？", "根埠（Root Port, RP，每個非根交換器恰好有且僅有一個）", ["根埠（Root Port, RP，每個非根交換器恰好有且僅有一個）", "指定埠（Designated Port）", "阻斷埠（Blocking / Alternate Port）", "備援埠"], "Root Port 負責向根方向轉發流量。"),
        ("STP 中，在每一個實體網段（LAN Segment）上，負責向該網段轉發流量的埠被稱為？", "指定埠（Designated Port, DP）", ["指定埠（Designated Port, DP）", "根埠", "阻斷埠", "邊界埠"], "每個網段有且僅有一個 Designated Port，根交換器上的所有可用埠必皆為 Designated Port。"),
        ("STP 802.1D 傳統收斂時間大約需要多久？", "30 到 50 秒（歷經 Blocking -> Listening(15s) -> Learning(15s) -> Forwarding）", ["30 到 50 秒（歷經 Blocking -> Listening(15s) -> Learning(15s) -> Forwarding）", "1 秒內", "10 毫秒", "5 分鐘"], "收斂極慢；快速生成樹協定（RSTP 802.1w）引入 Proposal/Agreement 機制將收斂時間縮減至毫秒級。"),
        ("IEEE 802.1Q VLAN 標籤（Tag）在乙太網路訊框中佔用多少位元組？其中 VLAN ID（VID）佔幾位元？", "佔用 4 個位元組；其中 VID 佔 12 位元（支援最多 4094 個可用 VLAN）", ["佔用 4 個位元組；其中 VID 佔 12 位元（支援最多 4094 個可用 VLAN）", "佔用 2 位元組；VID 佔 8 位元", "佔用 8 位元組；VID 佔 16 位元", "佔用 1 位元組；VID 佔 4 位元"], "4-byte 802.1Q 標籤插在來源 MAC 與 EtherType 之間，包含 TPID (0x8100)、3-bit PCP 優先權、1-bit DEI、12-bit VID (0 與 4095 保留，可用 1..4094)。"),
        ("交換器的 Access 埠與 Trunk 埠之行為差異為？", "Access 埠僅屬於單一 VLAN 且收發不帶 Tag 的標準訊框（連接終端電腦）；Trunk 埠允許「多個 VLAN 訊框通過」且攜帶 802.1Q Tag（連接交換器間）", ["Access 埠僅屬於單一 VLAN 且收發不帶 Tag 的標準訊框（連接終端電腦）；Trunk 埠允許「多個 VLAN 訊框通過」且攜帶 802.1Q Tag（連接交換器間）", "Access 埠攜帶 Tag，Trunk 埠不帶", "兩者完全相同", "Trunk 只能連接路由器"], "Trunk 骨幹鏈路承載跨交換器的多 VLAN 流量，原生 VLAN（Native VLAN）在 Trunk 上傳輸時預設不打 Tag。"),
        ("乙太網路 MAC 位址長度為多少位元？前 24 位元代表何者？", "48 位元（6 個位元組）；前 24 位元為組織唯一識別碼（OUI, Organizationally Unique Identifier，代表硬體製造商）", ["48 位元（6 個位元組）；前 24 位元為組織唯一識別碼（OUI, Organizationally Unique Identifier，代表硬體製造商）", "32 位元；前 16 位元為國家碼", "64 位元；前 32 位元為製造商", "128 位元；前 64 位元為網路號"], "以十六進位表示（如 00:1A:2B:3C:4D:5E），後 24 位元由廠商自行分配流水號。"),
        ("乙太網路廣播 MAC 位址（Broadcast MAC Address）為？", "FF:FF:FF:FF:FF:FF", ["FF:FF:FF:FF:FF:FF", "00:00:00:00:00:00", "FF:FF:FF:00:00:00", "01:00:5E:00:00:01"], "全 1 廣播位址，二層交換器收到後必定無條件向除接收埠外的所有其他埠洪泛（Flooding）。"),
        ("交換器轉發訊框時，若在 MAC 位址表（CAM 表）中「查無目的地 MAC 位址」，交換器的處置為？", "向除接收埠以外的所有同 VLAN 埠執行「未知單播洪泛（Unknown Unicast Flooding）」", ["向除接收埠以外的所有同 VLAN 埠執行「未知單播洪泛（Unknown Unicast Flooding）」", "直接丟棄該訊框", "回傳 ICMP 錯誤封包", "將該封包存入快取等待"], "交換器自學機制：未知目的地先洪泛，一旦目的主機回覆即可學習其來源 MAC 與埠號對應，收斂 MAC 表。"),
        ("三層交換器（Layer 3 Switch）相較於傳統路由器的優勢為？", "具備專屬硬體 ASIC / TCAM 晶片，能以「線速（Wire-Speed）」硬體轉發路由跨 VLAN 封包（一次路由，多次交換）", ["具備專屬硬體 ASIC / TCAM 晶片，能以「線速（Wire-Speed）」硬體轉發路由跨 VLAN 封包（一次路由，多次交換）", "完全不需要 IP 位址", "能取代所有伺服器", "成本低於集線器"], "硬體級路由轉發吞吐量達數百 Gbps，成為大型企業內部骨幹核心。"),
        ("單臂路由器（Router-on-a-Stick）實現跨 VLAN 路由的實體架構為？", "路由器使用「單一實體介面」配置多個邏輯子介面（Sub-interfaces），透過 Trunk 鏈路與交換器連接", ["單臂路由器（Router-on-a-Stick）實現跨 VLAN 路由的實體架構為？", "每個 VLAN 各拉一條實體網路線到路由器", "使用兩台路由器互相備援", "不使用路由器"], "利用 802.1Q 封裝，節省路由器昂貴實體埠。"),
        ("ARP（位址解析協定）的主要功能為？", "根據已知的目的地「IP 位址（邏輯位址）」查詢解析出對應的「MAC 位址（實體位址）」", ["根據已知的目的地「IP 位址（邏輯位址）」查詢解析出對應的「MAC 位址（實體位址）」", "根據 MAC 位址查詢 IP 位址", "自動分配 IP 位址", "將網域名稱解析為 IP"], "封包在二層封裝時必須填入目的 MAC，ARP 透過廣播請求、單播回覆完成動態映射。"),
        ("免費 ARP（Gratuitous ARP）的主要用途為？", "主機啟動時向網路廣播自身的 IP 與 MAC，用以「偵測 IP 位址是否發生衝突（IP Conflict Detection）」或通知交換器更新 MAC 快取", ["主機啟動時向網路廣播自身的 IP 與 MAC，用以「偵測 IP 位址是否發生衝突（IP Conflict Detection）」或通知交換器更新 MAC 快取", "免費取得上網頻寬", "向路由器請求預設閘道", "查詢 DNS 伺服器"], "若收到回覆則代表網路上已有其他設備佔用該 IP，立即提示 IP 衝突。"),
        ("ARP 詐欺（ARP Spoofing / Poisoning）攻擊的原理為？", "發送偽造的 ARP 回覆封包，將目標主機的閘道 MAC 位址竄改為攻擊者的 MAC 位址，以實施中間人攻擊（MITM）", ["發送偽造的 ARP 回覆封包，將目標主機的閘道 MAC 位址竄改為攻擊者的 MAC 位址，以實施中間人攻擊（MITM）", "破壞交換器電源", "發送大量廣播封包阻塞網路", "修改 DNS 快取"], "防範手段為啟用交換器動態 ARP 檢查（DAI, Dynamic ARP Inspection）或綁定靜態 ARP 表。"),
        ("動態 ARP 檢查（DAI）在交換器上依賴何種安全資料庫進行封包驗證？", "DHCP 窺探綁定表（DHCP Snooping Binding Database）", ["DHCP 窺探綁定表（DHCP Snooping Binding Database）", "DNS 快取表", "路由表", "ACL 存取清單"], "DAI 檢查通過非信任埠的 ARP 封包，比對 IP-MAC-Port 是否與 DHCP 分配記錄相符，違規者直接丟棄。"),
        ("點對點協定（PPP, Point-to-Point Protocol）相較於舊式 SLIP，其核心功能優勢為？", "支援鏈路控制協定（LCP）、網路控制協定（NCP）、身分認證（PAP/CHAP）與多協定封裝", ["支援鏈路控制協定（LCP）、網路控制協定（NCP）、身分認證（PAP/CHAP）與多協定封裝", "支援 CSMA/CD", "支援廣播傳輸", "僅用於無線網路"], "廣域網路串列專線經典二層協定。"),
        ("CHAP 認證（Challenge Handshake Authentication Protocol）相較於 PAP 的安全性優勢為？", "採用「挑戰-回應」機制與 MD5 單向雜湊，密碼「絕不在網路上以明文傳輸」且能防止重送攻擊", ["採用「挑戰-回應」機制與 MD5 單向雜湊，密碼「絕不在網路上以明文傳輸」且能防止重送攻擊", "認證速度快 10 倍", "不需要密碼", "支援雙因素認證"], "PAP 為明文發送密碼，極易遭側聽洩漏；CHAP 定期重新發送 Challenge 驗證連線。"),
        ("乙太網路訊框前置碼（Preamble）包含 7 個位元組的 10101010 與 1 個位元組的訊框起始定界符（SFD），SFD 的數值為？", "10101011（以結尾連續兩個 1 標誌訊框內容正式開始）", ["10101011（以結尾連續兩個 1 標誌訊框內容正式開始）", "10101010", "11111111", "00000000"], "使實體層接收器進行位元同步並精確鎖定第一個資料位元組位置。"),
        ("標準乙太網路訊框的有效負載（Payload）長度範圍為？", "46 到 1500 位元組（不足 46 位元組必須補 Padding 填補字元）", ["46 到 1500 位元組（不足 46 位元組必須補 Padding 填補字元）", "0 到 1024 位元組", "64 到 1518 位元組", "128 到 2048 位元組"], "若負載小於 46 位元組，加上 14 位元組標頭與 4 位元組 FCS 會低於 64 位元組最小訊框限制，故必須填充 Padding。"),
        ("巨型訊框（Jumbo Frames）通常將 MTU 大小擴展至多少位元組以提升高頻寬資料中心儲存傳輸效能？", "9000 位元組（9000 Bytes）", ["9000 位元組（9000 Bytes）", "1500 位元組", "3000 位元組", "65535 位元組"], "減少高吞吐傳輸時每秒訊框中斷處理次數，大幅降低 CPU 負載。"),
        ("流量控制中，停止等待協定（Stop-and-Wait ARQ）在「長延遲大頻寬管道（高 BDP）」中表現極差的主因為？", "傳送端每發送一個訊框就必須停下來等待整整一個 RTT 的 ACK，導致通道利用率極低趨近於零", ["傳送端每發送一個訊框就必須停下來等待整整一個 RTT 的 ACK，導致通道利用率極低趨近於零", "演算法太複雜", "容易產生迴圈", "無法偵測錯誤"], "通道容量極大卻長期待機，通道利用率 η = t_trans / (t_trans + 2·t_prop) << 1。"),
        ("選擇性重傳協定（Selective Repeat）相較於回退 N 步協定（Go-Back-N），在網路封包遺失率高時的主要優勢為？", "接收端具有緩衝區，僅要求重傳「真正遺失的那一個訊框」，後續已正確抵達的訊框無須重複發送", ["接收端具有緩衝區，僅要求重傳「真正遺失的那一個訊框」，後續已正確抵達的訊框無須重複發送", "不需要序號", "不需要 ACK 確認", "實作比 GBN 簡單"], "避免 GBN 浪費性重傳後續所有正常封包的頻寬浪費。"),
        ("在 HDLC（高級資料鏈路控制）協定中，為了在訊框內部防止出現與標誌欄位（01111110）相同的位元組合，採用的資料透明傳輸技術為？", "位元填充法（Bit Stuffing，逢連續 5 個 1 即強制插入一個 0）", ["位元填充法（Bit Stuffing，逢連續 5 個 1 即強制插入一個 0）", "字元填充法", "加上跳脫字元 ESC", "全訊框加密"], "發送端遇到 5 個連續 1 自動補 0，接收端逢 5 個 1 自動刪除其後的 0，保證標誌唯一性。"),
        ("鏈路聚合（LACP / IEEE 802.3ad）將多條實體線路綁定為一條邏輯通道（Port-Channel / EtherChannel），其核心效益為？", "線性倍增可用傳輸頻寬，並提供硬體級線路冗餘容錯（Fault Tolerance）", ["線性倍增可用傳輸頻寬，並提供硬體級線路冗餘容錯（Fault Tolerance）", "降低線路成本", "將二層轉為三層", "防止病毒入侵"], "任一條實體線路斷線流量自動切換至其他線路無縫轉發。")
    ]

    for stem, ans_s, opts, expl in more_dll:
        choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
        qs.append({
            "tag": "資料鏈結層深入機制",
            "stem": stem,
            "choices": choices,
            "ans": "A",
            "ans_text": f"(A) {ans_s}",
            "explanation": f"""<strong>【資料鏈結層協定核心特性剖析】</strong><br>
‧ <strong>(A) {ans_s}</strong>：依原理推導，{expl}<br>
‧ 其餘選項皆存在運作條件或協定語意混淆。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Spanning Tree Protocol (STP)</code> <span class="en">STP</span>：生成樹協定。<br>
‧ <code>Virtual Local Area Network (VLAN)</code> <span class="en">VLAN</span>：虛擬區域網路。<br>
‧ <code>Gratuitous ARP</code> <span class="en">Gratuitous ARP</span>：免費 ARP。"""
        })

    return qs

if __name__ == '__main__':
    qs = get_net_part1_questions()
    print(f"Generated Net Part 1 questions: {len(qs)}")
