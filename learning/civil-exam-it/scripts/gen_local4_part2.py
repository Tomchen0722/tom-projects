#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Local Civil Service Level 4 (地方特考四等) Question Bank Part 2 (80 questions).
Categories:
1. 作業系統核心架構、行程狀態、PCB 與 CPU 排程 (27 questions)
2. 行程同步、臨界區間、死結與記憶體管理 (27 questions)
3. Linux 系統管理、Shell 指令、權限與檔案系統 (26 questions)
"""

def get_local4_part2_questions():
    qs = []

    # Dataset 1: 作業系統核心架構、行程狀態、PCB 與 CPU 排程 (27 questions)
    data1 = [
        ("在作業系統核心架構分類中，比較單體核心（Monolithic Kernel，如傳統 Linux）與微核心（Microkernel，如 QNX、Minix）之特性，下列敘述何者完全正確？",
         "微核心僅將最基本之行程調度、行程間通訊（IPC）與基本記憶體管理保留於核心空間，檔案系統與設備驅動程式移至使用者空間執行，具備高度可靠性與模組化",
         ["微核心僅將最基本之行程調度、行程間通訊（IPC）與基本記憶體管理保留於核心空間，檔案系統與設備驅動程式移至使用者空間執行，具備高度可靠性與模組化",
          "單體核心所有服務皆運行於使用者空間，故效能最差",
          "微核心因所有模組皆擠在核心空間，容易因單一驅動程式錯誤導致全系統崩潰",
          "微核心無法在多核心 CPU 上運行"],
         "單體核心 vs 微核心架構：單體核心（Monolithic Kernel）將所有系統服務（虛擬記憶體、檔案系統、網路協定堆疊、驅動程式）皆放在核心空間（Ring 0）運行，彼此直接透過內部函式呼叫，效能極高但單一模組 bug 易導致系統藍屏崩潰；微核心（Microkernel）採極簡設計，僅保留核心必要服務，其餘服務作為使用者空間伺服行程（Server Processes），透過 IPC 傳訊溝通，任一伺服行程崩潰可獨立重啟不影響全域穩定。"),

        ("在作業系統中，用以完整記錄與維護單一行程（Process）生命週期所有運行狀態與硬體資訊之核心資料結構為？",
         "行程控制塊（PCB, Process Control Block）",
         ["行程控制塊（PCB, Process Control Block）",
          "檔案配置表（FAT）",
          "動態主機設定表（DHCP Table）",
          "中斷向量表（IVT）"],
         "PCB（行程控制塊）內容：PCB 是作業系統管理行程之核心資料結構。包含：1. 行程識別碼（PID）；2. 行程狀態（New, Ready, Running, Waiting, Terminated）；3. 程式計數器（PC，保存下一條指令位址）；4. CPU 暫存器內容（通用暫存器、堆疊指標）；5. CPU 排程資訊（優先權、佇列指標）；6. 記憶體管理資訊（分頁表指標）；7. 會計與審計資訊；8. I/O 狀態資訊（開啟的檔案描述元清單）。"),

        ("當一個正在 CPU 上執行中的行程（Running 狀態），因呼叫了 <code>read()</code> 系統呼叫等待硬碟讀取資料或使用者輸入時，作業系統會將該行程之狀態轉變為？",
         "等待/阻塞狀態（Waiting / Blocked 狀態）",
         ["等待/阻塞狀態（Waiting / Blocked 狀態）",
          "就緒狀態（Ready 狀態）",
          "終止狀態（Terminated 狀態）",
          "全新建立狀態（New 狀態）"],
         "行程五狀態生命週期轉換：1. New ➔ Ready：行程被建立並准許進入記憶體；2. Ready ➔ Running：排程器選中該行程分派 CPU（Dispatch）；3. Running ➔ Ready：時間配額（Time Quantum）用盡被強制搶奪（Preempt）；4. Running ➔ Waiting：行程發出 I/O 請求或等待事件（阻塞）；5. Waiting ➔ Ready：I/O 完成或事件發生，由中斷常式移回 Ready 佇列等待排程；6. Running ➔ Terminated：執行完畢退出。"),

        ("在多工處理系統中，比較「行程（Process）」與「執行緒（Thread）」之資源分配與執行特性，下列敘述何者完全正確？",
         "行程是作業系統配置資源（如獨立虛擬記憶體空間、開啟檔案）的最小單位；執行緒是 CPU 排程與分派執行的最小單位，同一個行程內的多個執行緒共享該行程的記憶體代碼段與全域資料",
         ["行程是作業系統配置資源（如獨立虛擬記憶體空間、開啟檔案）的最小單位；執行緒是 CPU 排程與分派執行的最小單位，同一個行程內的多個執行緒共享該行程的記憶體代碼段與全域資料",
          "執行緒擁有各自獨立且完全隔離的虛擬記憶體定址空間，彼此無法共享全域變數",
          "建立一個新行程的系統開銷遠小於建立一個執行緒",
          "一個執行緒崩潰絕對不會影響所屬行程中的其他執行緒"],
         "行程 vs 執行緒根本區別：Process 是資源分配的擁有者（獨立位址空間、檔案描述元表），彼此間記憶體保護隔離，通訊需透過 IPC（管線、共用記憶體）；Thread（又稱輕量級行程 LWP）是排程執行的實體，同一行程內的所有執行緒共享代碼段（Text Segment）、資料段（Data Segment）與作業系統資源，但每個執行緒各自擁有獨立的程式計數器（PC）、暫存器組與私有堆疊（Stack）。執行緒切換開銷極小，但若單一執行緒發生非法記憶體存取（Segfault）常導致整個行程崩潰。"),

        ("某區公所伺服器有四個行程 P1、P2、P3、P4 同時抵達（抵達時間皆為 0），其所需的 CPU 突發時間（Burst Time）分別為 8ms、4ms、2ms、6ms。若作業系統採用「最短工作優先（SJF, Non-preemptive Shortest Job First）」排程演算法，這四個行程之「平均等待時間（Average Waiting Time）」為？",
         "5.0 ms",
         ["5.0 ms", "4.0 ms", "6.5 ms", "8.0 ms"],
         "SJF 排程計算步驟：1. 依 Burst Time 由小到大排序執行順序：P3 (2ms) ➔ P2 (4ms) ➔ P4 (6ms) ➔ P1 (8ms)。2. 各行程完成時間：P3 於 2ms 完成；P2 於 2+4=6ms 完成；P4 於 6+6=12ms 完成；P1 於 12+8=20ms 完成。3. 各行程等待時間（抵達時間皆為 0）：P3 等待 0ms；P2 等待 2ms；P4 等待 6ms；P1 等待 12ms。4. 平均等待時間 = (0 + 2 + 6 + 12) / 4 = 20 / 4 = 5.0 ms。"),

        ("在 CPU 排程中，若採用「循環輪轉排程（Round Robin, RR）」演算法，若時間配額（Time Quantum, q）設定過大（例如趨近於無限大）或設定過小（例如接近 1 微秒），系統分別會產生何種極端不良效能影響？",
         "時間配額過大時退化為「先到先服務（FCFS）」演算法；時間配額過小時引發過度頻繁的「上下文切換（Context Switching）」，系統大部分時間耗費於排程開銷",
         ["時間配額過大時退化為「先到先服務（FCFS）」演算法；時間配額過小時引發過度頻繁的「上下文切換（Context Switching）」，系統大部分時間耗費於排程開銷",
          "時間配額過大時系統立即當機；時間配額過小時吞吐量達到理論極限",
          "時間配額大小對系統完全沒有任何影響",
          "時間配額過大時自動轉為最短工作優先（SJF）"],
         "Round Robin 時間配額權衡：RR 排程是分時系統（Time-Sharing）之核心。若 Quantum q 趨近無限大，每個行程一次就能跑完其 CPU Burst，演算法完全等同於 FCFS（護航效應，短工作需等待長工作）；若 q 極小，雖然互動響應極快，但 Context Switch 的硬體暫存器存取與快取失效開銷（Cache Pollution）將佔據巨額 CPU 運算資源。實務上通常將 q 設為 10ms~100ms，確保 80% 的 CPU Burst 均能在單一配額內完成。"),

        ("在搶奪式 CPU 排程演算法中，「最短剩餘時間優先（SRTF, Shortest Remaining Time First）」的核心排程準則為？",
         "當新行程抵達就緒佇列時，若其所需之剩餘 CPU 執行時間比「當前正在執行之行程的剩餘時間」更短，則作業系統立即搶奪 CPU 並切換給新行程執行",
         ["當新行程抵達就緒佇列時，若其所需之剩餘 CPU 執行時間比「當前正在執行之行程的剩餘時間」更短，則作業系統立即搶奪 CPU 並切換給新行程執行",
          "永遠優先執行最耗費記憶體之行程",
          "每隔 1 秒隨機強制終止一個行程",
          "優先執行最先進入系統之行程且不可搶奪"],
         "SRTF（最短剩餘時間優先）：SRTF 為 SJF 之搶奪式（Preemptive）版本。其優點為理論上能達成「最小平均等待時間」；缺點為若系統中不斷湧入微小短行程，執行時間極長的批次工作將永遠無法獲得 CPU 執行，產生嚴重的「飢餓現象（Starvation / Indefinite Blocking）」。"),

        ("為解決低優先權行程長期無法獲得 CPU 服務而產生之「飢餓現象（Starvation）」，作業系統通常導入何種機制，隨時間推移逐步調高長久等待中行程之優先權？",
         "老化機制（Aging）",
         ["老化機制（Aging）",
          "冷卻機制（Cooling）",
          "休眠機制（Sleeping）",
          "重組機制（Defragmentation）"],
         "老化機制（Aging）：排程防飢餓標準處方。例如：設定定時中斷，凡在 Ready 佇列中每等待 15 分鐘而未獲得執行的行程，其動態優先權自動加 1（優先權數值提高）。如此即使原本優先權極低的背景壓縮或批次報表行程，隨著等待時間增長，其優先權最終必然攀升至最高等級並獲得 CPU 排程執行。"),

        ("在現代作業系統中，「多層回饋佇列（MLFQ, Multilevel Feedback Queue）」排程演算法之所以被廣泛採用（如 Unix/Windows），其核心設計特性為？",
         "配置多個優先權不同之佇列，行程可在佇列間動態移動；CPU 密集型（長計算）行程逐漸降級至低優先權（大時間配額）佇列，I/O 密集型（互動型）行程保持在高優先權佇列，兼顧互動反應力與批次吞吐量",
         ["配置多個優先權不同之佇列，行程可在佇列間動態移動；CPU 密集型（長計算）行程逐漸降級至低優先權（大時間配額）佇列，I/O 密集型（互動型）行程保持在高優先權佇列，兼顧互動反應力與批次吞吐量",
          "所有佇列具有完全相同之優先權且行程嚴禁跨佇列移動",
          "僅依據行程之程式碼大小進行靜態固定分配",
          "純粹採用隨機分派完全不記錄歷史行為"],
         "MLFQ（多層回饋佇列）智慧排程哲學：新行程一律先進入最高優先權佇列 Q0（時間配額最小，如 8ms），若能在配額內主動釋出 CPU（典型互動 I/O 型），則維持高優先權；若用盡配額被搶奪（典型運算型），則被降級至 Q1（配額 16ms）甚至 Q2（FCFS）。搭配週期性的 Priority Boost（所有行程重置回最高佇列防止飢餓），無須預先得知行程 Burst Time 即可自動兼顧互動式短任務與計算密集型長任務。"),

        ("當作業系統執行「上下文切換（Context Switch）」時，CPU 硬體與核心必須執行的關鍵操作不包含下列何者？",
         "清空並格式化磁碟上所有的分頁置換檔（Swap File）",
         ["清空並格式化磁碟上所有的分頁置換檔（Swap File）",
          "保存當前執行行程之 CPU 暫存器、PC 與 PSW 數值至其 PCB 中",
          "切換記憶體分頁表指標暫存器（如 x86 的 CR3 暫存器）並可能導致 TLB 快取失效",
          "自新選定行程之 PCB 中載入其 CPU 暫存器數值與程式計數器恢復執行"],
         "Context Switch 核心開銷：上下文切換完全屬於純管理負擔（Overhead，此時 CPU 不做任何有益的應用程式運算）。其步驟包含：儲存舊行程狀態至 PCB ➔ 更新排程狀態 ➔ 載入新行程 PCB 狀態 ➔ 更新 MMU 分頁表指標（CR3 切換通常觸發 TLB 刷新，引發後續記憶體存取延遲）。格式化 Swap 檔與上下文切換完全無關。"),

        ("在即時作業系統（RTOS）之排程中，「單調速率排程（RMS, Rate Monotonic Scheduling）」演算法分配優先權的靜態準則為？",
         "任務的週期（Period）越短（發生頻率越高），其分配到的靜態優先權越高",
         ["任務的週期（Period）越短（發生頻率越高），其分配到的靜態優先權越高",
          "任務所需之運算時間越長，優先權越高",
          "任務佔用的記憶體越大，優先權越高",
          "完全隨機分配優先權"],
         "RMS（單調速率排程）演算法：即時系統中經典的靜態優先權搶奪式排程。週期 T 與頻率成反比，頻率越高的週期性任務被賦予越高的優先權。Liu 與 Layland 證明，對於 n 個獨立週期任務，若 CPU 利用率 U <= n(2^(1/n) - 1)（當 n 趨近無限大時極限為 ln 2 ≈ 69.3%），則 RMS 保證所有任務皆能於截止時間（Deadline）前完工。"),

        ("相對於 RMS 的靜態優先權，在即時系統中採用動態優先權之「最早截止時間優先（EDF, Earliest Deadline First）」演算法，其排程準則與理論 CPU 利用率上限為？",
         "距離其截止時間（Deadline）最近的任務具備最高優先權；在搶奪式理想條件下，理論 CPU 利用率上限可達到 100%",
         ["距離其截止時間（Deadline）最近的任務具備最高優先權；在搶奪式理想條件下，理論 CPU 利用率上限可達到 100%",
          "截止時間最遠的任務優先執行，利用率上限為 50%",
          "任務大小最小者優先執行，利用率上限為 70%",
          "EDF 無法保證截止時間，僅能隨機排程"],
         "EDF（最早截止時間優先）：動態優先權演算法。每次排程時動態評估就緒任務中誰的 Absolute Deadline 最迫近，最急迫者搶奪 CPU。其理論證明是最佳的（Optimal），只要系統總 CPU 利用率 U <= 1.0（100%），EDF 保證所有任務不會違背 Deadline。缺點在於若超載（U > 1），可能發生骨牌效應（Domino Effect）導致大批任務集體逾期。"),

        ("在 Unix/Linux 系統中，當一個子行程（Child Process）已經執行完畢終止，但其父行程（Parent Process）尚未呼叫 <code>wait()</code> 或 <code>waitpid()</code> 讀取其結束狀態時，該子行程在行程列表中處於何種狀態？",
         "殭屍行程（Zombie Process / Defunct）",
         ["殭屍行程（Zombie Process / Defunct）",
          "孤兒行程（Orphan Process）",
          "守護行程（Daemon Process）",
          "系統核心行程（Kernel Thread）"],
         "Zombie vs Orphan 行程：1. Zombie 行程：子行程結束時，核心釋放其絕大部分記憶體與檔案資源，但在行程表中保留 PCB 條目（記錄 PID、退出碼 Exit Status、CPU 消耗統計），等待父行程透過 wait() 讀取收屍。若父行程遲遲不收屍，殭屍行程持續佔用系統有限的 PID 數量；2. Orphan 行程：父行程在子行程前意外終止，子行程由 init（PID 1）或 systemd 收養，並由其自動呼叫 wait() 收屍。"),

        ("地方政府戶政系統在尖峰臨櫃申辦時，若伺服器因短時間內湧入數萬個並行連線，不斷大量 <code>fork()</code> 建立新行程，導致記憶體耗盡且行程數量達到作業系統上限（PID 耗盡），此種狀態稱為？",
         "Fork 炸彈（Fork Bomb）引發之資源耗竭拒絕服務",
         ["Fork 炸彈（Fork Bomb）引發之資源耗竭拒絕服務",
          "硬碟實體磁頭損毀",
          "光纖網路斷線",
          "顯示卡驅動程式逾時"],
         "Fork Bomb 與行程防護：在 Unix/Linux 中，未受控的遞迴創建行程（如經典 Bash 代碼 :(){ :|:& };:）會在幾秒內將系統 PID 耗盡、行程表與記憶體塞滿，導致管理員連下指令 kill 都無法建立新行程處理。防範措施為在 /etc/security/limits.conf 中限制單一使用者的 nproc（最大行程數上限），或利用 Linux cgroups 設定 pids.max。"),

        ("在多執行緒程式設計模型中，比較「使用者層級執行緒（ULT, User-Level Threads）」與「核心層級執行緒（KLT, Kernel-Level Threads）」之特性，下列敘述何者完全正確？",
         "ULT 之建立與切換純由使用者空間的執行緒程式庫（Thread Library）管理，切換速度極快且無需模式轉換，但若其中一個執行緒發出阻塞式系統呼叫（如 I/O），整個行程將會被全部阻塞",
         ["ULT 之建立與切換純由使用者空間的執行緒程式庫（Thread Library）管理，切換速度極快且無需模式轉換，但若其中一個執行緒發出阻塞式系統呼叫（如 I/O），整個行程將會被全部阻塞",
          "KLT 完全不需要作業系統核心支援即可執行",
          "ULT 能夠原生利用多核心 CPU 進行真正的硬體平行運算",
          "KLT 切換速度遠快於 ULT"],
         "ULT vs KLT 特性對照：1. ULT（多對一模型 M:1）：OS 核心只看得到單一行程，執行緒排程在 User Space 完成，速度快，但單一執行緒 blocking I/O 會拖垮整隊，且無法跨多核心平行；2. KLT（一對一模型 1:1，現代 Linux Pthreads 與 Windows 主流）：每個執行緒皆對應核心排程實體，能被核心分派到不同 CPU 核心平行運轉，單一執行緒阻塞不影響其他執行緒，但切換需進入核心模式代價略高。"),

        ("在 Linux 系統中，行程間通訊（IPC, Inter-Process Communication）機制多樣，下列何者屬於「單向（半雙工）、僅能在具有親緣關係（如父子行程）之行程間傳遞資料之位元組流」機制？",
         "匿名管線（Anonymous Pipe，以系統呼叫 <code>pipe()</code> 建立）",
         ["匿名管線（Anonymous Pipe，以系統呼叫 <code>pipe()</code> 建立）",
          "具名管線（Named Pipe / FIFO，以 <code>mkfifo</code> 建立）",
          "訊息佇列（Message Queue）",
          "共用記憶體（Shared Memory）"],
         "IPC 管線機制：匿名管線（Pipe）建立一組檔案描述元 fd[0]（讀取端）與 fd[1]（寫入端），資料以 FIFO 位元組流單向傳輸，存於核心緩衝區中，生命週期隨行程結束而消逝，僅能供父子或兄弟行程使用；具名管線（Named Pipe / FIFO）在檔案系統中有實體檔名節點，允許任意無關聯之獨立行程雙向或單向通訊。"),

        ("在所有行程間通訊（IPC）機制中，資料傳輸速度最快、開銷最低，因其「無需在核心空間與使用者空間之間重複複製資料」之機制為？",
         "共用記憶體（Shared Memory）",
         ["共用記憶體（Shared Memory）",
          "通訊端（Sockets）",
          "信號（Signals）",
          "匿名管線（Pipes）"],
         "共用記憶體（Shared Memory）之效能優勢：傳統 Pipe 或 Socket 傳輸資料時，資料需經歷：發送端 User 空間 ➔ 核心緩衝區 ➔ 接收端 User 空間，涉及至少兩次記憶體複製與模式切換；共用記憶體直接透過 MMU 將同一塊實體記憶體分頁映射至兩個不同行程的虛擬位址空間，行程存取資料宛如存取本地指標，達到零拷貝（Zero-Copy）極速，但必須由應用程式自行搭配號誌（Semaphore）處理同步互斥。"),

        ("在多核心作業系統中，關於「非對稱多處理（AMP, Asymmetric Multiprocessing）」與「對稱多處理（SMP, Symmetric Multiprocessing）」之架構差異，下列敘述何者完全正確？",
         "SMP 中所有 CPU 核心地位平等共享同一個實體記憶體與單一作業系統核心；AMP 採用主從架構（Master-Slave），特定主核心專門運行 OS 核心並調度任務，其餘從核心僅執行指定程式",
         ["SMP 中所有 CPU 核心地位平等共享同一個實體記憶體與單一作業系統核心；AMP 採用主從架構（Master-Slave），特定主核心專門運行 OS 核心並調度任務，其餘從核心僅執行指定程式",
          "SMP 只能由單一核心執行，其餘核心必須關閉電源",
          "AMP 核心之間完全無法共享任何資料",
          "現代伺服器已全面廢棄 SMP 僅使用 AMP"],
         "SMP vs AMP 多處理架構：SMP（Symmetric Multiprocessing）是現代多核伺服器標準，各 CPU 核心皆可運行使用者與核心代碼，共享記憶體匯流排，負載平衡度高；AMP（Asymmetric Multiprocessing）常見於異質運算晶片（如大核心搭配低功耗小核心、或主 CPU 搭配專用 DSP/AI 處理器），主核心掌控系統資源與 I/O，從核心被指派特定封閉運算，硬體邏輯較單純。"),

        ("當使用者應用程式呼叫系統呼叫（System Call，如 <code>open()</code> 或 <code>write()</code>）時，作業系統與 CPU 硬體是如何安全地從「使用者模式（User Mode）」切換至「核心模式（Kernel Mode）」？",
         "觸發「軟體中斷 / 陷阱（Software Interrupt / Trap，如 x86 的 <code>syscall</code> 或 <code>int 0x80</code> 指令）」，使 CPU 硬體切換特權等級並跳轉至預設之核心系統呼叫分派器",
         ["觸發「軟體中斷 / 陷阱（Software Interrupt / Trap，如 x86 的 <code>syscall</code> 或 <code>int 0x80</code> 指令）」，使 CPU 硬體切換特權等級並跳轉至預設之核心系統呼叫分派器",
          "由應用程式自行修改記憶體中任意位址以獲得 root 特權",
          "由工程師手動在鍵盤上輸入 root 密碼",
          "透過主機板蜂鳴器發出音頻訊號解鎖"],
         "系統呼叫與陷阱機制：應用程式若能直接調用特權指令將造成極大資安風險。Trap 是一種受控的硬體特權切換：使用者程式將系統呼叫編號放進暫存器（如 EAX）後執行 syscall 指令，硬體強行將 CPU 模式切為 Ring 0 並將 PC 導向核心預設好的中斷向量入口（System Call Table），由核心代為執行受保護的硬體存取操作後，再以 <code>sysret</code> 降級切回 User Mode。"),

        ("在作業系統行程狀態模型中，當實體記憶體嚴重不足時，中程排程器（Medium-Term Scheduler / Swapper）將某些暫時不執行的行程整份換出至磁碟交換區（Swap Space），該行程會進入何種延伸狀態？",
         "掛起就緒（Ready Suspended）或掛起阻塞（Blocked Suspended）狀態",
         ["掛起就緒（Ready Suspended）或掛起阻塞（Blocked Suspended）狀態",
          "永久終止狀態（Terminated）",
          "執行中狀態（Running）",
          "核心崩潰狀態（Kernel Panic）"],
         "七狀態行程模型（包含掛起 Suspended）：當系統實體 RAM 告急時，作業系統 Swapper 介入：1. Ready Suspended：行程已準備好運行，但其實體記憶體映像已被置換（Swapped Out）至磁碟 Swap，待記憶體充足時換回即可變回 Ready；2. Blocked Suspended：行程既在等待 I/O 事件，且實體記憶體也被換出至磁碟。中程排程器透過控制掛起行程數量，有效調解記憶體過載。"),

        ("在多核心伺服器排程中，為避免行程在不同 CPU 核心之間頻繁跳躍遷移造成 L1/L2 快取記憶體頻繁失效（Cache Invalidation），管理員可設定「處理器親和性（Processor Affinity）」，將特定市政核心服務行程綁定於指定 CPU 核心之技術稱為？",
         "硬親和性綁定（Hard Affinity / CPU Pinning，如 Linux 的 <code>taskset</code> 指令）",
         ["硬親和性綁定（Hard Affinity / CPU Pinning，如 Linux 的 <code>taskset</code> 指令）",
          "軟體超頻技術",
          "記憶體碎裂重組",
          "虛擬主機快照備份"],
         "CPU 親和性（Processor Affinity）：1. Soft Affinity：作業系統排程器盡量嘗試讓行程留在上次運行的同一個 CPU 核心上（利用快取熱度 Cache Warmth），但不做硬性保證；2. Hard Affinity（CPU Pinning）：透過系統呼叫 <code>sched_setaffinity()</code> 或 <code>taskset -c 0,1 &lt;PID&gt;</code>，強制限制該行程僅能在指定的一或多個核心上運行，常用於高吞吐量公務資料庫與低延遲網路轉發服務。"),

        ("在多處理器系統之負載平衡（Load Balancing）中，比較「推入遷移（Push Migration）」與「拉取遷移（Pull Migration）」之機制，下列敘述何者完全正確？",
         "推入遷移由特定核心背景定期檢查各核心負載，發現不平衡時主動將超載核心的任務推給閒置核心；拉取遷移由閒置核心主動向忙碌核心的就緒佇列竊取（Work Stealing）任務來執行",
         ["推入遷移由特定核心背景定期檢查各核心負載，發現不平衡時主動將超載核心的任務推給閒置核心；拉取遷移由閒置核心主動向忙碌核心的就緒佇列竊取（Work Stealing）任務來執行",
          "推入遷移只能在開機時執行一次",
          "拉取遷移會將所有行程強制移入資源回收桶",
          "兩者完全相同，僅為不同語言翻譯名詞"],
         "負載平衡遷移機制：在多佇列多處理器排程中：Push Migration 由全域監控常式定期巡邏，若核心 A 負載過重而核心 B 空閒，主動「推」任務過去；Pull Migration 由剛跑完手頭任務的空閒核心主動出擊，從其他核心「拉」任務過來（Work Stealing 機制）。現代 Linux CFS 同時結合了這兩者，確保多核心運算資源獲得最大化均衡利用。"),

        ("在評估 CPU 排程演算法效能之各項度量指標中，「周轉時間（Turnaround Time）」的精確定義為？",
         "行程從「提交進入系統（Arrival Time）」到「完全執行完畢終止（Completion Time）」所耗費的總時間長度（包含等待、執行與 I/O 時間）",
         ["行程從「提交進入系統（Arrival Time）」到「完全執行完畢終止（Completion Time）」所耗費的總時間長度（包含等待、執行與 I/O 時間）",
          "行程在就緒佇列中等待被排程的總時間",
          "行程從提交到第一次獲得 CPU 回應的時間",
          "CPU 核心風扇旋轉一圈的總時間"],
         "排程度量指標定義：1. Turnaround Time（周轉時間）= 完成時間 - 抵達時間；2. Waiting Time（等待時間）= 周轉時間 - 實際執行時間（CPU Burst + I/O Burst），即在 Ready 佇列中空等的純時間；3. Response Time（反應時間）= 從提交到第一次產生輸出回應（或首次獲得 CPU）的時間；4. Throughput（吞吐量）= 單位時間內完成的行程總數。"),

        ("在即時嵌入式與多工系統中，當一個高優先權行程因為等待低優先權行程所佔有的共享資源而被阻塞，同時中優先權行程搶佔了 CPU 導致低優先權行程無法執行並釋放資源，使得高優先權行程被無故延誤之病態現象稱為？",
         "優先權反轉（Priority Inversion），可透過「優先權繼承協定（Priority Inheritance Protocol）」解決",
         ["優先權反轉（Priority Inversion），可透過「優先權繼承協定（Priority Inheritance Protocol）」解決",
          "記憶體洩漏現象",
          "死結循環等待",
          "快取震盪現象"],
         "優先權反轉（Priority Inversion）與火星探路者號故障：情境：低優先權 L 持有 Mutex；高優先權 H 請求該 Mutex 進入等待；此時無關的中優先權 M 搶佔 CPU 狂跑，導致 L 根本沒機會執行並釋放鎖，結果變相使 H 被 M 壓制。解法為「優先權繼承（Priority Inheritance）」：當 H 阻塞於 L 持有的鎖時，L 暫時動態繼承 H 的最高優先權，迅速跑完釋放鎖後恢復原等級，防止被 M 插隊。"),

        ("在現代 Linux 作業系統之排程架構中，針對常規（非即時）行程所採用的「完全公平排程器（CFS, Completely Fair Scheduler）」之核心排程準則與內部資料結構為？",
         "記錄每個行程之「虛擬運行時間（vruntime）」，排程器永遠優先挑選 vruntime 最小的行程執行，底層使用「紅黑樹（Red-Black Tree）」維護就緒佇列",
         ["記錄每個行程之「虛擬運行時間（vruntime）」，排程器永遠優先挑選 vruntime 最小的行程執行，底層使用「紅黑樹（Red-Black Tree）」維護就緒佇列",
          "使用二元堆疊記錄程式碼大小，永遠優先執行程式碼最大的行程",
          "使用陣列隨機抽選行程執行",
          "純粹採用單純的先到先服務（FCFS）佇列"],
         "Linux CFS 完全公平排程器：Ingo Molnar 設計。取消傳統固定時間配額，改為追蹤行程的 <code>vruntime</code>（虛擬運行時間，權重越高/nice值越低的行程，vruntime 增長越慢）。所有就緒行程掛載於紅黑樹（自平衡二元搜尋樹）中，最左側節點（Leftmost Node）即為 vruntime 最小者。CPU 每次調度最左節點，確保每個行程依其 nice 權重比例獲得極致平滑的公平 CPU 時間。"),

        ("在 Linux 行程層級體系中，系統啟動時第一個被核心載入執行、作為所有其他使用者行程之曾祖父根行程（PID 為 1）的服務行程為？",
         "<code>systemd</code>（或傳統的 <code>init</code>）",
         ["<code>systemd</code>（或傳統的 <code>init</code>）", "<code>kthreadd</code>", "<code>cron</code>", "<code>bash</code>"],
         "PID 1 與 systemd 架構：核心開機引導並掛載根檔案系統後，在使用者空間啟動的第一個行程其 PID 恆等於 1（現代 Linux 發行版如 RHEL/Ubuntu 皆採用 systemd，早年為 SysV init）。systemd 負責平行啟動所有系統守護行程（Daemons）、掛載儲存設備、管理網路服務，並在背景擔任收容孤兒行程（Orphan Processes）的終極監護人角色。"),

        ("在長程排程器（Long-Term Scheduler）、中程排程器（Medium-Term Scheduler）與短程排程器（Short-Term Scheduler）之比較中，何者被觸發執行的頻率最高（通常每幾毫秒執行一次），直接決定下一個分派 CPU 之行程？",
         "短程排程器（Short-Term Scheduler / CPU Scheduler）",
         ["短程排程器（Short-Term Scheduler / CPU Scheduler）",
          "長程排程器（Long-Term Scheduler / Job Scheduler）",
          "中程排程器（Medium-Term Scheduler / Swapper）",
          "非同步備份排程器"],
         "三種排程器層級對比：1. Short-Term（短程排程器 / CPU 排程器）：毫秒級執行，從 Ready 佇列中挑選行程分配 CPU，速度必須極快；2. Medium-Term（中程排程器 / Swapper）：秒級至分鐘級，負責將行程換出/換入記憶體，調控多工併行程度（Degree of Multiprogramming）；3. Long-Term（長程排程器 / 作業排程器）：分鐘或小時級，決定哪些提交在磁碟佇列中的批次工作被准許進入記憶體轉換為行程。")
    ]

    # Dataset 2: 行程同步、臨界區間、死結與記憶體管理 (27 questions)
    data2 = [
        ("在並行程式設計中，為確保多個行程共享資源時資料之一致性，解決「臨界區間問題（Critical-Section Problem）」必須嚴格滿足的三大核心準則為？",
         "互斥（Mutual Exclusion）、進展（Progress）與有限等待（Bounded Waiting）",
         ["互斥（Mutual Exclusion）、進展（Progress）與有限等待（Bounded Waiting）",
          "原子性（Atomicity）、一致性（Consistency）與隔離性（Isolation）",
          "先到先服務、短工作優先與時間配額",
          "死結、活結與飢餓"],
         "臨界區間三大必要條件：1. 互斥（Mutual Exclusion）：若已有行程在該臨界區間內執行，其餘任何行程絕對不可進入；2. 進展（Progress）：若臨界區間為空且有行程欲進入，僅有不在剩餘區段（Remainder Section）的行程能參與下一進入者的決策，且決策不可被無限推遲；3. 有限等待（Bounded Waiting）：任一行程提出進入申請後，在獲得進入前其他行程進入臨界區間的次數必須有上限，杜絕飢餓。"),

        ("在荷蘭電腦科學家 Edsger Dijkstra 提出之「號誌（Semaphore）」機制中，原始定義之 <code>wait()</code> 操作（亦稱 <code>P()</code>）與 <code>signal()</code> 操作（亦稱 <code>V()</code>），其對整數變數 <code>S</code> 之不可分割（Atomic）操作分別為？",
         "<code>wait(S)</code>: 當 <code>S &lt;= 0</code> 時等待，一旦 <code>S &gt; 0</code> 則執行 <code>S = S - 1</code>；<code>signal(S)</code>: 執行 <code>S = S + 1</code>",
         ["<code>wait(S)</code>: 當 <code>S &lt;= 0</code> 時等待，一旦 <code>S &gt; 0</code> 則執行 <code>S = S - 1</code>；<code>signal(S)</code>: 執行 <code>S = S + 1</code>",
          "<code>wait(S)</code>: 執行 <code>S = S + 1</code>；<code>signal(S)</code>: 執行 <code>S = S - 1</code>",
          "<code>wait(S)</code>: 將 <code>S</code> 設為 0；<code>signal(S)</code>: 將 <code>S</code> 設為無限大",
          "<code>wait(S)</code> 與 <code>signal(S)</code> 皆將 <code>S</code> 數值翻倍"],
         "號誌（Semaphore）原子操作：計數號誌（Counting Semaphore）初始化為可用資源數量 N。P 操作（荷蘭語 Proberen 測試/嘗試減 1）：請求資源，若資源數不足則阻塞等待；V 操作（荷蘭語 Verhogen 增加）：釋放資源，S 遞增並喚醒等待中的行程。兩者必須以原子指令（如關閉中斷或硬體指令 Test-and-Set）保證不可中斷。若 N=1 則退化為互斥鎖（Binary Semaphore / Mutex）。"),

        ("當某行程在等待取得互斥鎖（Mutex）的過程中，採用不斷在 <code>while</code> 迴圈中檢查鎖狀態而不放棄 CPU 之「忙碌等待（Busy Waiting）」鎖，此種鎖在作業系統中被稱為？",
         "自旋鎖（Spinlock）",
         ["自旋鎖（Spinlock）",
          "條件變數（Condition Variable）",
          "讀寫鎖（Read-Write Lock）",
          "可重入鎖（Reentrant Lock）"],
         "自旋鎖（Spinlock）特性與適用場景：Spinlock 在迴圈中空轉消耗 CPU 週期，在單處理器（Single CPU）系統中是絕對的效能毒藥；但在多處理器（SMP）核心內部，若預期臨界區間極短（例如僅更新幾個指標，耗時遠低於一次 Context Switch 開銷），Spinlock 避免了行程休眠與喚醒的代價，因此常廣泛應用於作業系統核心內部極短暫之同步保護。"),

        ("在作業系統死結（Deadlock）理論中，科夫曼（Coffman）提出的「死結四大必要條件」中，若打破其中任何一個條件，死結即不可能發生。下列何者「不屬於」這四個必要條件？",
         "時間配額用盡（Time Quantum Expired）",
         ["時間配額用盡（Time Quantum Expired）",
          "互斥（Mutual Exclusion，資源非共享）",
          "持有並等待（Hold and Wait，已持有部分資源又請求新資源）",
          "不可搶奪（No Preemption，資源僅能由持有者自願釋放）"],
         "死結四大必要條件（Coffman Conditions）：1. 互斥（Mutual Exclusion）：至少有一項資源處於不可共享模式；2. 持有並等待（Hold and Wait）：行程至少持有一項資源，並等待獲取被其他行程持有的新資源；3. 不可搶奪（No Preemption）：已配置給行程的資源在未使用完畢前不可被強制剝奪；4. 循環等待（Circular Wait）：存在行程循環等待鏈（P0 等 P1，P1 等 P2，...，Pn 等 P0）。"),

        ("地方政府戶政系統在死結預防（Deadlock Prevention）策略中，若強制規定「系統中所有各類實體資源皆賦予全域唯一之整數編號，所有行程必須嚴格按照資源編號『由小到大遞增之順序』依序提出申請」，此項措施旨在徹底打破死結的哪一個必要條件？",
         "循環等待（Circular Wait）",
         ["循環等待（Circular Wait）",
          "互斥（Mutual Exclusion）",
          "不可搶奪（No Preemption）",
          "持有並等待（Hold and Wait）"],
         "破除循環等待之全域線性編序：若資源依整數定義 F(Ri)，要求申請 Rb 時必須滿足 F(Rb) > F(Ra)。在此規則下，不可能存在循環鏈 P0 ➔ P1 ➔ ... ➔ Pn ➔ P0，因為這將導致數值推導出 F(R0) < F(R1) < ... < F(R0) 之數學矛盾。此方法在嵌入式系統與資料庫防死結架構中極具工程實用性。"),

        ("在死結避免（Deadlock Avoidance）之經典「銀行家演算法（Banker's Algorithm）」中，系統在每次配置資源給請求行程之前，必須先進行何種檢驗？",
         "試驗性分配資源後，判斷系統是否仍處於「安全狀態（Safe State）」，若能找到至少一條「安全序列（Safe Sequence）」確保所有行程皆能依序執行完畢，才真正放行分配",
         ["試驗性分配資源後，判斷系統是否仍處於「安全狀態（Safe State）」，若能找到至少一條「安全序列（Safe Sequence）」確保所有行程皆能依序執行完畢，才真正放行分配",
          "檢查各投標廠商在公庫銀行的帳戶存款餘額是否充足",
          "隨機抽選一個行程直接強制殺死（Kill）",
          "直接無條件滿足所有行程的全部最大需求"],
         "銀行家演算法安全狀態檢驗：Dijkstra 提出之死結避免法。核心邏輯：令系統假裝滿足行程 Pi 的請求，計算剩餘可用資源向量 Available 與各行程尚需資源矩陣 Need。利用安全性演算法（Safety Algorithm）尋找是否存在行程順序，使得每個行程的最大需求皆能在前人釋放資源後被滿足。若安全狀態成立才正式撥付，否則行程必須等待。"),

        ("在實體記憶體連續配置策略中，當有一個大小為 15KB 的新行程需求到達時，記憶體中現有三個未配置空閒區塊（Holes）分別為 20KB、50KB 與 16KB。若採用「最佳適應（Best Fit）」策略，該行程會被配置到哪一個區塊中？",
         "16KB 的空閒區塊",
         ["16KB 的空閒區塊", "20KB 的空閒區塊", "50KB 的空閒區塊", "隨機分配至 50KB 區塊"],
         "連續動態儲存配置策略比較：1. First Fit（首次適應）：從頭掃描，配置給「第一個」夠大的區塊（20KB），速度最快；2. Best Fit（最佳適應）：遍歷全表，配置給「能容納該需求且最小」的區塊（16KB），保留大區塊，但會留下極微小難以利用的零碎小空洞；3. Worst Fit（最差適應）：配置給「最大」的空閒區塊（50KB），試圖留下較大的剩餘碎片。"),

        ("在非連續記憶體管理中，分頁（Paging）機制藉由將虛擬記憶體劃分為固定大小的 Page，實體記憶體劃分為相同大小的 Frame，徹底消除了何種碎裂問題？但仍存在何種碎裂問題？",
         "徹底消除了「外部碎裂（External Fragmentation）」，但仍可能存在「內部碎裂（Internal Fragmentation）」",
         ["徹底消除了「外部碎裂（External Fragmentation）」，但仍可能存在「內部碎裂（Internal Fragmentation）」",
          "徹底消除了內部碎裂，但仍存在外部碎裂",
          "同時徹底消除了內部碎裂與外部碎裂",
          "完全無法解決任何碎裂問題"],
         "Paging 碎裂消除原理：在連續分配中，零碎剩餘的微小空間散落於各處，總量足夠卻無法連續拼湊給新行程使用，稱為外部碎裂；分頁機制將位址空間切碎，任何空閒的實體 Frame 都可以分配給任何 Page，實體記憶體完全不需要連續，因此外部碎裂為 0。唯一損失在於行程最後一頁通常不會剛好填滿 4096 位元組，平均每行程浪費半個 Page（約 2KB），此為內部碎裂。"),

        ("某 32 位元作業系統採用單階分頁（Single-level Paging），若每個分頁大小為 4KB（2^12 Bytes），則一個行程之虛擬位址空間總共需要包含多少個分頁（Pages）？其虛擬位址中「分頁偏移量（Page Offset）」佔用多少位元？",
         "共包含 2^20（1,048,576）個分頁，偏移量佔用 12 位元",
         ["共包含 2^20（1,048,576）個分頁，偏移量佔用 12 位元",
          "共包含 2^16 個分頁，偏移量佔用 16 位元",
          "共包含 4,096 個分頁，偏移量佔用 20 位元",
          "共包含 256 個分頁，偏移量佔用 8 位元"],
         "分頁位址拆解計算：虛擬位址長度 32 位元，可定址空間為 2^32 = 4GB。分頁大小為 4KB = 4 * 1024 = 4096 = 2^12 Bytes。因此位址中「最低 12 位元（Bits 0~11）」為頁內偏移量（Offset d）；剩餘「最高 20 位元（Bits 12~31）」為虛擬分頁號碼（Page Number p）。分頁總數即為 2^(32 - 12) = 2^20 = 1,048,576 個頁面。"),

        ("在倒排分頁表（Inverted Page Table）架構中，其與傳統分頁表最大的不同與空間優勢為？",
         "整部電腦系統中僅維護一個全域分頁表，表格的條目數量由「實體記憶體框號（Frames）」決定而非由龐大的虛擬位址空間決定，大幅節省分頁表本身佔用的記憶體空間",
         ["整部電腦系統中僅維護一個全域分頁表，表格的條目數量由「實體記憶體框號（Frames）」決定而非由龐大的虛擬位址空間決定，大幅節省分頁表本身佔用的記憶體空間",
          "將所有記憶體資料倒過來由末端開始讀取",
          "完全廢除實體記憶體直接使用硬碟定址",
          "使虛擬記憶體速度達到光速運轉"],
         "倒排分頁表（Inverted Page Table）設計：在 64 位元巨型位址空間下，每個行程各自維護多層分頁表會消耗極其龐大的記憶體（數百MB）。Inverted Page Table 每個實體 Frame 在表中僅有一個條目，記錄當前是哪一個行程（PID）的哪一個虛擬 Page 佔用它。缺點在於位址查找需要遍歷搜尋（通常依賴雜湊表 Hash Table 加速），且實作虛擬記憶體共享（Shared Memory）極為困難。"),

        ("在哲學家就餐問題（Dining Philosophers Problem）中，5 位哲學家共用 5 支筷子，若每位哲學家同時拿起自己左手邊的筷子，隨後等待右手邊的筷子，系統會陷入何種僵局？最經典之防範演算法為？",
         "陷入死結（Deadlock）；解決方案可限制最多僅容許 4 位哲學家同時嘗試就餐，或奇數號哲學家先拿左邊、偶數號先拿右邊（打破循環等待）",
         ["陷入死結（Deadlock）；解決方案可限制最多僅容許 4 位哲學家同時嘗試就餐，或奇數號哲學家先拿左邊、偶數號先拿右邊（打破循環等待）",
          "系統自動將所有筷子沒收並關閉電源",
          "陷入活結且程式碼自動刪除",
          "完全不會發生任何問題，哲學家皆可順利吃麵"],
         "哲學家就餐問題本質：經典並行同步死結模型。當 5 位哲學家同時進入「拿左筷」狀態時，滿足了 Hold and Wait 且形成封閉環狀依賴，死結爆發全員餓死。破除策略：1. 使用服務生（Monitor/Mutex）將拿兩支筷子包裝成不可分割的原子動作；2. 不對稱策略：讓奇數編號先左後右、偶數編號先右後左，保證相鄰哲學家競爭同支筷子，不可能全員同時拿到一支。"),

        ("在讀者寫者問題（Readers-Writers Problem）中，若實作策略採取「讀者優先（Readers-Preference）」，多個讀者可同時讀取資料，此架構可能引發之潛在不良後果為？",
         "若連續不斷有新的讀者進入系統讀取，寫者（Writer）將長期無法取得鎖定，導致寫者陷入「飢餓（Starvation）」",
         ["若連續不斷有新的讀者進入系統讀取，寫者（Writer）將長期無法取得鎖定，導致寫者陷入「飢餓（Starvation）」",
          "資料庫實體硬碟會產生物理壞軌",
          "讀者讀取到的資料會瞬間變成空白亂碼",
          "作業系統核心行程會被自動終止"],
         "讀者寫者問題權衡：共享檔案允許多個讀者並行讀取，但寫入時必須獨佔互斥（讀寫互斥、寫寫互斥）。若讀者優先：只要還有一個讀者在讀，後續抵達的讀者皆可直接放行，寫者必須等待所有讀者離開；在讀多寫少的系統中，寫者可能無止境被插隊產生飢餓。因此實務上常採公平排程或「寫者優先（Writer-Preference）」，一旦有寫者排隊即暫停新讀者進入。"),

        ("在軟體解決臨界區間問題的經典演算法中，為兩個行程設計且嚴格滿足互斥、進展與有限等待之純軟體演算法為？",
         "彼得森演算法（Peterson's Algorithm），結合旗標陣列 <code>flag[2]</code> 與輪替變數 <code>turn</code>",
         ["彼得森演算法（Peterson's Algorithm），結合旗標陣列 <code>flag[2]</code> 與輪替變數 <code>turn</code>",
          "戴克斯特拉最短路徑演算法",
          "霍夫曼編碼演算法",
          "冒泡排序演算法"],
         "彼得森演算法（Peterson's Algorithm）：經典雙行程互斥軟體解。行程 i 欲進入臨界區時：設 <code>flag[i] = true</code>（表態有意願），再將謙讓變數設為 <code>turn = j</code>（將機會讓給對方）；進入條件為 <code>while (flag[j] &amp;&amp; turn == j);</code>。當對方無意願或對方也把機會讓給自己時，即可進入。該演算法在現代多核心弱記憶體模型（Weak Memory Order）下需搭配記憶體屏障（Memory Barrier）防止指令重排。"),

        ("現代 CPU 晶片硬體提供之原子指令（Atomic Hardware Instructions），用以實作無鎖（Lock-Free）並行演算法與高速互斥鎖之經典指令為？",
         "比較並交換指令（CAS, Compare-And-Swap）與測試並設定指令（TAS, Test-And-Set）",
         ["比較並交換指令（CAS, Compare-And-Swap）與測試並設定指令（TAS, Test-And-Set）",
          "整數加法指令（ADD）與跳躍指令（JMP）",
          "位元位移指令（SHL）與乘法指令（MUL）",
          "輸入指令（IN）與輸出指令（OUT）"],
         "硬體原子同步指令：CAS(V, A, B) 檢視記憶體位址 V 的值是否等於預期值 A，若相等則以原子操作更新為新值 B 並回傳 true，否則不做任何事回傳 false。CAS 整個過程在匯流排鎖或快取鎖保證下絕對不可分割，徹底消除了多執行緒競爭條件，是現代並行資料結構（如 Java ConcurrentHashMap、Disruptor 環形緩衝區）之基石。"),

        ("高階程式語言（如 Java）中提供之「管程 / 監視器（Monitor）」同步機制，其相對於底層號誌（Semaphore）的最大工程優勢為？",
         "管程是一種物件導向語言級封裝，保證在任何時刻「至多僅允許一個執行緒在管程內部的方法中執行」，程式設計師無需手動撰寫容易出錯的 P/V 操作",
         ["管程是一種物件導向語言級封裝，保證在任何時刻「至多僅允許一個執行緒在管程內部的方法中執行」，程式設計師無需手動撰寫容易出錯的 P/V 操作",
          "管程可以將程式執行速度提高 1,000 倍",
          "管程強制所有執行緒都在夜間執行",
          "管程能自動修復硬碟損壞磁區"],
         "Monitor（管程）高階同步結構：Hoare 與 Hansen 提出。底層 Semaphore 若工程師漏寫 V() 導致死結，漏寫 P() 導致互斥崩潰。Monitor 將共享變數及其操作函式封裝在同一個 Class 中，編譯器自動為管程方法加上互斥進入鎖（如 Java 的 <code>synchronized</code> 關鍵字），並搭配條件變數（Condition Variables，配合 <code>wait()</code> 與 <code>signal()</code>）實現精確的同步排程。"),

        ("在作業系統死結偵測之「資源配置圖（RAG, Resource Allocation Graph）」中，若系統中「每一種資源類型皆僅包含恰好一個實體（Single Instance per resource type）」，則死結存在的充分且必要條件為？",
         "資源配置圖中存在至少一個「循環等待環路（Cycle）」",
         ["資源配置圖中存在至少一個「循環等待環路（Cycle）」",
          "資源配置圖中節點數量大於 100 個",
          "所有邊皆為向外射出的箭頭",
          "系統記憶體使用率超過 90%"],
         "資源配置圖死結判準定理：1. 若每種資源只有單一實例（Single Instance）：圖中存在「循環（Cycle）」是死結發生的「充要條件」（有環路則必死結，無環路則絕無死結）；2. 若資源包含多個實例（Multiple Instances）：有環路只是死結發生的「必要條件」（有環路未必死結，若環路外的其他行程釋放了同類資源，環路即可被解開）。"),

        ("在並行處理中，「活結（Livelock）」與「死結（Deadlock）」的核心差異在於？",
         "死結中的行程皆處於阻塞等待（Blocked）睡眠狀態無法行動；活結中的行程持續處於活躍狀態並不斷改變彼此的狀態，但演算法陷入無限循環相互禮讓，整體工作永遠無法向前推進",
         ["死結中的行程皆處於阻塞等待（Blocked）睡眠狀態無法行動；活結中的行程持續處於活躍狀態並不斷改變彼此的狀態，但演算法陷入無限循環相互禮讓，整體工作永遠無限向前推進",
          "死結會導致電腦硬體爆炸，活結不會",
          "活結只會出現在單核心電腦中",
          "兩者完全相同無任何差異"],
         "Deadlock vs Livelock 形象比喻：死結如同兩輛車在窄橋上面對面互不相讓，引擎熄火僵死不動；活結如同兩位有禮貌的行人在走廊狹路相逢，A 向左避讓同時 B 也向右避讓，A 再向右 B 也再向左，兩人持續在動（CPU 100% 狂轉）但誰也過不去。解決活結常引入「隨機退避延遲（Random Backoff，如乙太網 CSMA/CD）」。"),

        ("在實體記憶體動態分區配置中，為消除「外部碎裂（External Fragmentation）」，作業系統透過將記憶體中所有現有行程搬移集中於一端，使零碎空間融合成一大塊連續空閒空間之技術稱為？",
         "記憶體壓實 / 緊縮（Compaction）",
         ["記憶體壓實 / 緊縮（Compaction）",
          "分頁替換（Paging）",
          "記憶體碎片擴散（Dispersion）",
          "快取刷新（Cache Flush）"],
         "記憶體壓實（Compaction）先決條件：壓實技術需要將正在運行的行程在記憶體中實體搬遷。只有在系統採用「動態重定位（Dynamic Relocation）」且位址繫結（Address Binding）是在「執行期（Execution Time / Run Time）」利用基底暫存器（Base Register）動態計算實體位址時，壓實才可行。若是編譯期或載入期綁定，程式內寫死絕對位址，則無法實施壓實。"),

        ("在虛擬記憶體管理中，分頁表條目（PTE, Page Table Entry）通常包含若干硬體控制旗標，其中「髒位（Dirty Bit / Modified Bit）」的核心作用為？",
         "標記該虛擬分頁在載入記憶體後「是否曾被執行過寫入修改操作」，置換換出時若 Dirty Bit = 0 則無需寫回磁碟，直接丟棄即可大幅節省 I/O 開銷",
         ["標記該虛擬分頁在載入記憶體後「是否曾被執行過寫入修改操作」，置換換出時若 Dirty Bit = 0 則無需寫回磁碟，直接丟棄即可大幅節省 I/O 開銷",
          "標記該分頁是否感染了電腦病毒",
          "記錄該分頁是由哪一位工程師編寫的",
          "標記該分頁已被永久刪除"],
         "PTE 狀態旗標功能：1. Present / Valid Bit：標記該頁是否已載入實體 RAM（0 觸發 Page Fault）；2. Dirty / Modified Bit：寫入硬體自動置 1，若被淘汰換出，Dirty=1 必須耗費磁碟寫入 I/O 刷回 Swap，Dirty=0（乾淨頁，如唯讀代碼頁）可直接覆寫回收頁框；3. Reference / Access Bit：每當被讀寫時硬體置 1，供 Clock 或 LRU 演算法評估熱度；4. Protection Bits：讀寫執行（r/w/x）權限。"),

        ("在二階分頁（Two-Level Paging）系統中，32 位元虛擬位址被拆分為 <code>P1（10 位元）、P2（10 位元）、Offset（12 位元）</code>，此架構相對於單階分頁的最大優勢在於？",
         "無需將全體分頁表一次性全部載入實體記憶體，只有被使用到的二級分頁表才動態建立，大幅減少常駐記憶體之分頁表體積",
         ["無需將全體分頁表一次性全部載入實體記憶體，只有被使用到的二級分頁表才動態建立，大幅減少常駐記憶體之分頁表體積",
          "使記憶體存取速度提高 2 倍",
          "徹底消除了 TLB 快取未命中問題",
          "不需要硬體 MMU 支援即可執行"],
         "多階分頁（Multi-Level Paging）省記憶體機制：若為單階分頁，每個行程必須連續分配 4MB 空間存放整張完整 Page Table（即使該行程只用了 100KB 記憶體）。二階分頁中，第一級外層分頁表（Outer Page Table / Page Directory）僅佔 4KB 常駐記憶體，只有當程式真正存取某虛擬位址區段時，對應的第二級分頁表才會動態配置，大幅縮小小型行程的記憶體足跡。代價是記憶體存取次數增加（需多查一次表）。"),

        ("在 Linux 行程建立中，<code>fork()</code> 系統呼叫採用「寫入時複製（COW, Copy-on-Write）」技術，其核心運作機制為？",
         "子行程建立初期與父行程「共享完全相同的實體記憶體分頁並將分頁標記為唯讀」，直到任一方試圖寫入修改時，核心才真正為該分頁複製一份實體複本",
         ["子行程建立初期與父行程「共享完全相同的實體記憶體分頁並將分頁標記為唯讀」，直到任一方試圖寫入修改時，核心才真正為該分頁複製一份實體複本",
          "在 fork 呼叫瞬間立即將父行程的所有記憶體完整複製一份給子行程",
          "禁止子行程對任何變數進行寫入操作",
          "直接將父行程終止以騰出空間給子行程"],
         "Copy-on-Write（COW 寫入時複製）：傳統 Unix fork 複製整個 1GB 行程需要拷貝 1GB 資料耗時漫長，且子行程隨後常立即呼叫 <code>exec()</code> 換裝新程式，全數拷貝淪為純粹浪費。COW 讓父子行程僅複製分頁表指標，分頁標為 Read-Only；當有行程執行寫入時，觸發 Page Fault，核心在陷阱常式中單獨複製該 4KB 分頁並改為可寫。此技術使 Linux fork() 呼叫達到微秒級極速。"),

        ("透過 <code>mmap()</code> 系統呼叫實現之「記憶體映射檔案（Memory-Mapped Files）」機制，其主要優勢為？",
         "將磁碟檔案內容直接映射至行程的虛擬位址空間，程式可直接以指標像存取陣列一樣讀寫檔案，省去 <code>read()/write()</code> 之額外核心緩衝區複製開銷",
         ["將磁碟檔案內容直接映射至行程的虛擬位址空間，程式可直接以指標像存取陣列一樣讀寫檔案，省去 <code>read()/write()</code> 之額外核心緩衝區複製開銷",
          "將磁碟上的檔案直接轉換為二進位可執行程式",
          "強制所有檔案皆不能被其他人讀取",
          "將硬碟容量擴增 10 倍"],
         "mmap（記憶體映射）原理與應用：mmap 建立虛擬位址與磁碟檔案之直接映射。初次讀取透過分頁缺失（Page Fault）由核心的分頁快取（Page Cache）載入；寫入資料時直接修改記憶體，由作業系統背景執行緒（如 pdflush/flusher）非同步刷回硬碟。除了提高大檔案讀寫效能外，多個行程映射同一個檔案亦是建構高效跨行程通訊（IPC）與資料庫（如 LMDB、SQLite）之關鍵手段。"),

        ("在分頁虛擬記憶體系統中，若實體記憶體存取時間為 100 ns，處理一次缺頁中斷（Page Fault）之磁碟服務時間為 10 毫秒（10,000,000 ns）。若系統要求「有效記憶體存取時間（EAT）」之效能降幅不得超過 10%（即 EAT <= 110 ns），則缺頁中斷率 p 最高不得超過？",
         "約百萬分之一（p <= 0.000001 即 10^-6）",
         ["約百萬分之一（p <= 0.000001 即 10^-6）",
          "約百分之一（p <= 0.01）",
          "約千分之一（p <= 0.001）",
          "約十分之一（p <= 0.1）"],
         "EAT 缺頁率極限計算：EAT 公式為 EAT = (1 - p) * 100 + p * 10,000,000 ns。要求 EAT <= 110 ns：100 - 100p + 10,000,000p <= 110 ➔ 9,999,900p <= 10 ➔ p <= 10 / 9,999,900 ≈ 10^-6（百萬分之一）。這說明由於磁碟存取比 DRAM 慢了十萬倍以上，分頁系統必須維持 99.9999% 以上的極致命中率，否則系統效能將全面崩盤。"),

        ("在銀行家演算法（Banker's Algorithm）中，已知資源矩陣關係為：各行程尚需資源矩陣 <code>Need = Max - Allocation</code>。若行程 P0 提出資源申請 <code>Request0</code>，系統受理該請求並進入安全性演算法評估之先決條件為？",
         "<code>Request0 &lt;= Need0</code>（申請量不可超過原先宣告之最大需求量）且 <code>Request0 &lt;= Available</code>（系統當前剩餘資源必須足夠支付）",
         ["<code>Request0 &lt;= Need0</code>（申請量不可超過原先宣告之最大需求量）且 <code>Request0 &lt;= Available</code>（系統當前剩餘資源必須足夠支付）",
          "<code>Request0 &gt; Max0</code>",
          "<code>Request0</code> 必須恰好等於系統所有資源之總和",
          "只要 P0 提出申請，無論資源是否足夠皆無條件放行"],
         "銀行家演算法請求步驟（Resource-Request Algorithm）：1. 若 Request_i <= Need_i，轉步驟 2；否則報錯（超出最大宣告）；2. 若 Request_i <= Available，轉步驟 3；否則 Pi 必須等待資源；3. 系統假裝配置資源：Available -= Request_i，Allocation_i += Request_i，Need_i -= Request_i；4. 執行 Safety Algorithm：若 Safe 則正式撥付，若 Unsafe 則恢復原狀，Pi 繼續等待。"),

        ("在頁面置換演算法中，「二次機會演算法（Second-Chance Algorithm / Clock 演算法）」的核心工作原理為？",
         "以環形串列維護頁面指標，檢查頁面的參考位元（Reference Bit）：若為 1 則給予第二次機會清零為 0 並移向下一個；若為 0 則選定該頁予以替換淘汰",
         ["以環形串列維護頁面指標，檢查頁面的參考位元（Reference Bit）：若為 1 則給予第二次機會清零為 0 並移向下一個；若為 0 則選定該頁予以替換淘汰",
          "每個分頁允許發生兩次硬體故障而不中斷",
          "將所有分頁備份兩份存於不同硬碟",
          "強制每個行程執行兩次後才准離開"],
         "Clock（時鐘/二次機會）演算法：LRU 演算法硬體成本高昂，Clock 演算法是 LRU 的絕佳近似。指針如同鐘錶順時針走動。當需要淘汰頁面時：若目前指針指向頁之 Reference Bit = 0，該頁最近未被使用，直接淘汰換出；若 Reference Bit = 1，將其清零為 0（給一次免死金牌）並指向下一頁繼續搜尋。最差情況指針轉一圈將所有 1 清零後，必然能找到 0 進行置換。"),

        ("在解決並行問題時，若兩個執行緒同時嘗試對同一個全域整數變數 <code>count</code> 執行 <code>count++</code> 操作（組合語言包含 <code>LOAD, ADD, STORE</code> 三條指令），若無任何同步機制保護，執行完畢後產生的錯誤現象稱為？",
         "競爭條件（Race Condition），導致更新遺失（Lost Update）且結果依執行緒交錯執行順序而隨機不一致",
         ["競爭條件（Race Condition），導致更新遺失（Lost Update）且結果依執行緒交錯執行順序而隨機不一致",
          "死結（Deadlock）",
          "記憶體位址溢位",
          "編譯器語法錯誤"],
         "Race Condition（競爭條件）：當兩個並行執行緒交錯執行時：執行緒 A 讀取 count=5；在 A 寫回前，執行緒 B 也讀取 count=5；A 執行加 1 寫回 6；B 也執行加 1 寫回 6。原本預期應為 7，最終結果卻為 6，產生更新丟失。防範之道為將 <code>count++</code> 放入臨界區間（Mutex Lock）或使用硬體原子操作（如 <code>AtomicInteger</code>）。"),

        ("當作業系統偵測到系統已經發生死結（Deadlock Detected）時，在復原策略（Recovery）中，最常採用且代價最小的解除死結方式為？",
         "依據優先權、已執行時間與剩餘時間，逐一挑選「犧牲者行程（Victim Process）」強制終止並釋放其佔有之資源，直至死結環路打破",
         ["依據優先權、已執行時間與剩餘時間，逐一挑選「犧牲者行程（Victim Process）」強制終止並釋放其佔有之資源，直至死結環路打破",
          "直接拔掉整座機房的主電源線強制斷電",
          "將資料庫所有資料表全部 DROP 刪除",
          "由工程師手動向伺服器發送電子郵件請行程自行協商"],
         "死結解除策略：1. 行程終止（Process Termination）：終止所有死結行程（暴力但代價大），或逐一終止死結行程直到死結環消除；2. 資源搶奪（Resource Preemption）：選擇犧牲者（Victim Selection）、回滾（Rollback 至安全檢查點 Checkpoint）、並防範同一行程反覆被選為犧牲者而產生飢餓（Starvation，需納入回滾次數加權考量）。")
    ]

    # Dataset 3: Linux 系統管理、Shell 指令、權限與檔案系統 (26 questions)
    data3 = [
        ("在 Linux 檔案系統權限管理中，某公務檔案的權限設定以符號表示為 <code>-rwxr-xr--</code>，轉換為八進位三位數字數值應為？",
         "<code>754</code>",
         ["<code>754</code>", "<code>751</code>", "<code>744</code>", "<code>654</code>"],
         "Linux 權限八進位換算：三位一組：1. 擁有者（User）：rwx = 4 + 2 + 1 = 7；2. 群組（Group）：r-x = 4 + 0 + 1 = 5；3. 其他人（Others）：r-- = 4 + 0 + 0 = 4。因此合併數值為 754。代表擁有者具備讀寫執行全部權限，同群組可讀取與執行，其餘使用者僅能讀取。"),

        ("某區公所資安管理員設定新建立使用者的預設權限遮罩，若系統 <code>umask</code> 設定值為 <code>027</code>，則在該環境下新建一個常規檔案（Regular File，預設基底 666）時，其最終實際取得之權限為？",
         "<code>640</code>（<code>-rw-r-----</code>）",
         ["<code>640</code>（<code>-rw-r-----</code>）", "<code>644</code>", "<code>650</code>", "<code>750</code>"],
         "umask 運算規則：在 Linux 中，新建常規檔案之最大基礎權限為 666（不可預設具備執行檔權限 x）；新建目錄最大基礎為 777。遮罩 027 代表遮蔽掉 Group 的寫入（2）與 Others 的全部權限（7 = 4+2+1）。計算：666 AND NOT 027：User=6，Group=6-2=4，Others=6-7=0（全部剝奪）。因此檔案權限為 640。"),

        ("在 Linux 系統之特殊權限位元中，為執行檔設定「SUID（Set User ID, 數值 4000）」權限位元（如 <code>chmod 4755 /usr/bin/passwd</code>）之核心功能為？",
         "當一般使用者執行該程式時，該行程在執行期間會「暫時取得該檔案擁有者（通常為 root）之特權身分」來執行",
         ["當一般使用者執行該程式時，該行程在執行期間會「暫時取得該檔案擁有者（通常為 root）之特權身分」來執行",
          "允許所有使用者隨意修改該檔案原始碼",
          "讓檔案在開機時自動執行",
          "禁止任何使用者刪除該檔案"],
         "SUID 特殊權限作用：一般使用者需要變更密碼，但密碼存放在 /etc/shadow（僅 root 可寫）。若無 SUID，一般人無法執行 passwd。設定 SUID 後，使用者執行 /usr/bin/passwd 時，行程的 Effective UID 暫時提升為 root，使其能合法更新 /etc/shadow。資安稽核中需定期盤點含 SUID 檔案，防止攻擊者利用 SUID 漏洞提權（Privilege Escalation）。"),

        ("在 Linux 公共共享目錄（如 <code>/tmp</code>，權限為 <code>drwxrwxrwt</code>，具備 Sticky Bit 1000）中，Sticky Bit（粘滯位元）的核心安全保護機制為？",
         "所有使用者皆可在該目錄下建立檔案，但「僅有檔案的擁有者（Owner）或 root 才能刪除或重新命名該檔案」，防止使用者隨意刪除他人檔案",
         ["所有使用者皆可在該目錄下建立檔案，但「僅有檔案的擁有者（Owner）或 root 才能刪除或重新命名該檔案」，防止使用者隨意刪除他人檔案",
          "目錄內部檔案會自動黏合為單一壓縮檔",
          "禁止任何人讀取該目錄內之檔案",
          "檔案儲存 24 小時後自動物理銷毀"],
         "Sticky Bit（粘滯位元 t）：若無 Sticky Bit，一般目錄只要被賦予 777 權限，任何人都可以將目錄內屬於別人的檔案任意刪除（因為刪除檔案只需對目錄具備寫入權限）。Sticky Bit（以小寫 t 標註於 others 執行位）規定：目錄內即使大家皆有寫入權，也只有檔案真正的擁有者和 root 才能刪除自己的檔案，是多使用者公用暫存目錄之必備防護。"),

        ("比較 Linux 檔案系統中的「硬連結（Hard Link）」與「符號連結（Symbolic Link / 軟連結）」之特性，下列敘述何者完全正確？",
         "硬連結直接指向相同的 Inode 編號，兩者共享相同的資料區塊且不能跨檔案系統（跨磁碟分割區）建立；符號連結是獨立的特殊檔案，內部存放目標路徑字串，可跨檔案系統建立且可連結目錄",
         ["硬連結直接指向相同的 Inode 編號，兩者共享相同的資料區塊且不能跨檔案系統（跨磁碟分割區）建立；符號連結是獨立的特殊檔案，內部存放目標路徑字串，可跨檔案系統建立且可連結目錄",
          "刪除原始檔案時，符號連結依然可以正常讀取資料，硬連結則會失效",
          "硬連結可以隨意連結不存在的檔案（Dangling Link）",
          "符號連結完全不佔用任何 Inode 與磁碟空間"],
         "Hard Link vs Symbolic Link 深度比較：1. Hard Link：目錄項目指向同一個 Inode，Inode 內引用計數器（Link Count）加 1，刪除原始檔名時僅計數減 1，只要 Link Count > 0 資料就不會消失；因 Inode 編號僅在同一檔案系統內唯一，故「不可跨檔案系統」，且為防迴圈預設「不可連結目錄」；2. Symlink：如同 Windows 捷徑，擁有獨立 Inode，記錄目標路徑，若目標被刪會變成斷鏈（Dangling Link），可跨分割區與連結目錄。"),

        ("在 Linux 系統維運中，當需要即時監控系統整體負載、CPU 各核心使用率、記憶體消耗以及依照 CPU 消耗排序的即時行程清單時，最常用之動態互動命令為？",
         "<code>top</code>（或 <code>htop</code>）",
         ["<code>top</code>（或 <code>htop</code>）", "<code>ls</code>", "<code>pwd</code>", "<code>uname</code>"],
         "Linux 效能監控指令：top 實時更新系統狀態：包含系統運行時間、Load Average（1/5/15分鐘負載）、CPU 狀態（%us 使用者、%sy 核心、%wa I/O等待、%id 閒置）、實體記憶體與 Swap 消耗，以及行程即時排名（按 P 鍵依 CPU 排序、按 M 鍵依記憶體排序）。htop 則提供彩色列印與滑鼠互動介面。"),

        ("某區公所同仁欲搜尋 <code>/var/log/</code> 目錄下，所有修改時間在「7 天以前」且副檔名為 <code>.log</code> 之歷史日誌檔案予以清理，最適宜使用之 Linux 命令為？",
         "<code>find /var/log -name \"*.log\" -mtime +7</code>",
         ["<code>find /var/log -name \"*.log\" -mtime +7</code>",
          "<code>grep -r \"*.log\" /var/log --days=7</code>",
          "<code>ls -l /var/log | filter 7d</code>",
          "<code>cat /var/log/*.log -time 7</code>"],
         "find 指令參數精析：find [路徑] [條件]。-name \"*.log\"：匹配檔名；-mtime +7：最後修改時間在 7 天以前（大於 7*24 小時）；若為 -mtime -7 則代表 7 天以內；-type f：限制為常規檔案。若搭配 -exec rm {} \\; 即可直接完成批次刪除，是公務伺服器編寫自動化清理 Shell Script 之核心指令。"),

        ("在 Linux 檔案階層標準（FHS, Filesystem Hierarchy Standard）中，系統設定檔（Configuration Files，如 <code>fstab</code>, <code>passwd</code>, <code>network/interfaces</code>）統一存放於下列哪一個目錄？",
         "<code>/etc</code>",
         ["<code>/etc</code>", "<code>/bin</code>", "<code>/var</code>", "<code>/dev</code>"],
         "Linux FHS 目錄規範：1. /etc：主機專屬之靜態系統設定檔；2. /bin 與 /sbin：基本使用者與系統管理二進位可執行指令；3. /var：動態可變資料（如 /var/log 系統日誌、/var/spool/mail 郵件佇列、網頁根目錄）；4. /dev：實體硬體設備節點（如 /dev/sda 硬碟、/dev/tty 終端機）；5. /proc 與 /sys：核心虛擬檔案系統，反映記憶體與硬體執行期狀態。"),

        ("在 Linux 排程管理中，若欲設定於「每週一至週五的凌晨 2 點 30 分」自動執行備份腳本 <code>/backup/daily.sh</code>，在 <code>crontab</code> 中的排程時間設定表達式應為？",
         "<code>30 2 * * 1-5 /backup/daily.sh</code>",
         ["<code>30 2 * * 1-5 /backup/daily.sh</code>",
          "<code>2 30 * * 1-5 /backup/daily.sh</code>",
          "<code>* 2 30 * 1-5 /backup/daily.sh</code>",
          "<code>30 2 1-5 * * /backup/daily.sh</code>"],
         "Crontab 五欄位格式標準：格式順序為：[分 0-59] [時 0-23] [日 1-31] [月 1-12] [星期 0-6，0或7為週日]。本題：分=30，時=2，日=*，月=*，星期=1-5（週一至週五）。因此組合為 30 2 * * 1-5。公務機關定期異地備份、資安日誌輪替、稽核報表產出皆仰賴 cron 背景服務（crond）穩定執行。"),

        ("在虛擬化與雲原生技術中，比較傳統虛擬機器（Virtual Machines, 如 VMware, KVM）與容器技術（Containers, 如 Docker）之根本架構差異，下列敘述何者完全正確？",
         "虛擬機器透過 Hypervisor 虛擬化整套硬體並各自運行完整的客戶端作業系統（Guest OS）；容器技術直接共享宿主機作業系統核心（Host Kernel），透過 Linux 核心的 Namespaces 與 cgroups 實現隔離，啟動更快速且資源開銷極低",
         ["虛擬機器透過 Hypervisor 虛擬化整套硬體並各自運行完整的客戶端作業系統（Guest OS）；容器技術直接共享宿主機作業系統核心（Host Kernel），透過 Linux 核心的 Namespaces 與 cgroups 實現隔離，啟動更快速且資源開銷極低",
          "容器技術必須為每個容器各自安裝一套完整的微軟 Windows 核心",
          "虛擬機器不需要 Hypervisor 即可直接在硬體上多開 OS",
          "容器技術隔離性絕對優於虛擬機器且能模擬不同 CPU 架構"],
         "VM vs Container 深度解析：1. 虛擬機（Hypervisor Type 1/2）：抽象層在硬體，包含 Guest OS 核心，隔離性極高（硬體級隔離），但體積臃腫（數GB起跳）、開機需數十秒、記憶體浪費嚴重；2. 容器（Container）：抽象層在 OS 核心，利用 Namespaces（PID/Mount/Net 視圖隔離）與 cgroups（CPU/記憶體資源配額），直接作為宿主機上的一個隔離進程群執行，啟動僅需毫秒級、鏡像僅數十MB，是現代微服務部署主流。"),

        ("在 Linux 磁碟與檔案系統管理中，用以檢視「硬碟分割區總空間、已使用空間、剩餘可用空間與掛載點（以人類可讀易懂的 GB/MB 格式呈現）」之標準指令為？",
         "<code>df -h</code>",
         ["<code>df -h</code>", "<code>du -sh</code>", "<code>free -m</code>", "<code>fdisk -l</code>"],
         "df 與 du 指令辨析：1. df -h（Disk Free）：報告整個檔案系統/磁碟分割區之容量空間（-h 代表 human-readable，以 K/M/G 顯示）；2. du -sh [路徑]（Disk Usage）：計算指定目錄或檔案所消耗的實際磁碟空間總和；3. free -m：檢查實體記憶體 RAM 與 Swap 之使用量。公務主機磁碟空間警報時，常先用 df -h 查出哪個分割區爆滿，再用 du -sh * 追查大檔案。"),

        ("在 Linux 終端機命令列中，若欲強制終止一個已經失去回應且無法正常關閉的背景行程（PID 為 1234），應發送何種信號（Signal）？",
         "<code>kill -9 1234</code>（發送 <code>SIGKILL</code> 信號，核心強制終止，行程無法捕捉或忽略）",
         ["<code>kill -9 1234</code>（發送 <code>SIGKILL</code> 信號，核心強制終止，行程無法捕捉或忽略）",
          "<code>kill -15 1234</code>（僅禮貌請求關閉）",
          "<code>kill -1 1234</code>（重新載入設定檔）",
          "<code>kill -0 1234</code>（僅測試行程是否存在）"],
         "Linux 常用 Signal 代碼辨析：1. SIGTERM (15)：預設終止訊號，禮貌請求程式釋放資源並自行正常結束，行程可攔截處理；2. SIGKILL (9)：強制擊殺，信號由核心直接執行銷毀 PCB，行程「無法捕捉、無法忽略、無法阻塞」，用於處決殭死失控行程；3. SIGHUP (1)：掛斷訊號，常促使 Daemon 重新讀取設定檔；4. SIGINT (2)：鍵盤中斷 Ctrl+C。"),

        ("在 Linux 命令列管道與重導向中，若欲將指令執行時產生的「標準輸出（stdout）」與「標準錯誤（stderr）」同時合併重導向輸出至同一個檔案 <code>output.log</code> 中，標準 Shell 語法為？",
         "<code>./program &gt; output.log 2&gt;&amp;1</code>（或 Bash 簡化語法 <code>&amp;&gt; output.log</code>）",
         ["<code>./program &gt; output.log 2&gt;&amp;1</code>（或 Bash 簡化語法 <code>&amp;&gt; output.log</code>）",
          "<code>./program &gt;&gt; 2 output.log</code>",
          "<code>./program &lt; output.log</code>",
          "<code>./program | output.log</code>"],
         "Shell I/O 重導向描述元：檔案描述元 0 代表標準輸入（stdin）；1 代表標準輸出（stdout）；2 代表標準錯誤（stderr）。語法 <code>&gt; output.log</code> 將 stdout 導向檔案；<code>2&gt;&amp;1</code> 將 stderr 導向至目前 stdout 所指向的位置（即檔案）。若寫成 <code>2&gt;1</code> 則會被誤認為輸出至名為 1 的普通檔案。"),

        ("在 Linux 文本處理三劍客中，若需要自 <code>/etc/passwd</code> 帳號清冊中，僅提取出「每行的第一個欄位（帳號名稱，欄位間以冒號 <code>:</code> 分隔）」，最簡潔之文字處理指令為？",
         "<code>cut -d':' -f1 /etc/passwd</code>（或 <code>awk -F':' '{print $1}' /etc/passwd</code>）",
         ["<code>cut -d':' -f1 /etc/passwd</code>（或 <code>awk -F':' '{print $1}' /etc/passwd</code>）",
          "<code>grep -f1 /etc/passwd</code>",
          "<code>sed -c 1 /etc/passwd</code>",
          "<code>cat -first /etc/passwd</code>"],
         "文字欄位切割指令：<code>cut -d [分隔符號] -f [欄位編號]</code>。例如 <code>cut -d: -f1</code> 取第 1 欄（使用者名），<code>-f7</code> 取第 7 欄（預設 Shell 如 /bin/bash）。強大的文字處理語言 <code>awk</code> 則支援 <code>awk -F: '{print $1}'</code>。"),

        ("在 Linux 歸檔與壓縮指令中，將 <code>/home/data</code> 目錄打包並以 gzip 演算法壓縮為 <code>backup.tar.gz</code> 檔案之標準指令為？",
         "<code>tar -czvf backup.tar.gz /home/data</code>",
         ["<code>tar -czvf backup.tar.gz /home/data</code>",
          "<code>tar -xzvf backup.tar.gz /home/data</code>",
          "<code>zip -compress backup.tar.gz /home/data</code>",
          "<code>gzip -tar /home/data backup.tar.gz</code>"],
         "tar 指令常用參數組合：<code>-c</code>：建立新的歸檔檔（Create）；<code>-x</code>：解開歸檔檔（Extract）；<code>-z</code>：調用 gzip 壓縮/解壓縮（副檔名 .tar.gz）；<code>-j</code>：調用 bzip2 壓縮（.tar.bz2）；<code>-v</code>：顯示詳細處理進度（Verbose）；<code>-f</code>：指定歸檔檔名（File，後接檔名）。打包壓縮用 <code>-czvf</code>，解開解壓縮用 <code>-xzvf</code>。"),

        ("在 Linux 系統服務管理（systemd）中，若欲設定將網頁伺服器 Nginx 服務「開機時自動啟用啟動」，應執行之 systemctl 指令為？",
         "<code>systemctl enable nginx</code>",
         ["<code>systemctl enable nginx</code>",
          "<code>systemctl start nginx</code>",
          "<code>systemctl reload nginx</code>",
          "<code>systemctl status nginx</code>"],
         "systemctl 核心子命令：1. <code>start</code>：立即啟動服務（但重開機後不會自動啟動）；2. <code>stop</code>：立即停止；3. <code>restart</code>：重啟；4. <code>enable</code>：建立符號連結至 systemd 開機目標目錄，設定開機自動啟動；5. <code>disable</code>：取消開機自啟動；6. <code>status</code>：檢查服務運行健康度與最新日誌。"),

        ("在 Linux 網路狀態檢查與通訊埠監控中，用以查詢伺服器本機目前正在「監聽中（Listening）的所有 TCP 與 UDP 網路通訊埠號（以純數字顯示）」之現代標準命令為？",
         "<code>ss -tuln</code>（或 <code>netstat -tuln</code>）",
         ["<code>ss -tuln</code>（或 <code>netstat -tuln</code>）",
          "<code>ping -a</code>",
          "<code>ip route show</code>",
          "<code>ifconfig -all</code>"],
         "ss 與 netstat 通訊埠檢查：<code>ss</code>（Socket Statistics）參數意義：<code>-t</code>（TCP 連線）、<code>-u</code>（UDP 連線）、<code>-l</code>（僅列出 Listening 監聽中之服務埠）、<code>-n</code>（數值化呈現，顯示 Port 80 而非翻譯為 http，速度更快）。<code>ss</code> 直接自核心 netlink 提取資訊，效能遠勝於傳統已遭棄用的 <code>netstat</code>。"),

        ("在 Linux 磁碟分割與檔案系統掛載中，若希望某個新的磁碟分割區（如 <code>/dev/sdb1</code>）在每次主機重新開機時皆能「自動掛載至 <code>/data</code> 目錄」，管理員必須編輯下列哪一個系統設定檔？",
         "<code>/etc/fstab</code>",
         ["<code>/etc/fstab</code>", "<code>/etc/hosts</code>", "<code>/etc/resolv.conf</code>", "<code>/etc/sudoers</code>"],
         "<code>/etc/fstab</code>（File Systems Table）設定：系統開機自動掛載清單。包含 6 個欄位：<code>[設備UUID或路徑] [掛載點如 /data] [檔案系統類型如 ext4/xfs] [掛載參數如 defaults] [dump備份標記 0/1] [fsck開機檢查順序 0/1/2]</code>。若語法錯誤可能導致系統開機進入緊急修復模式（Emergency Mode）。"),

        ("在 Linux 帳號管理中，存放所有使用者「加密後之密碼雜湊值（Password Hash）」且權限嚴格限制僅有 root 能夠讀取的系統關鍵設定檔為？",
         "<code>/etc/shadow</code>",
         ["<code>/etc/shadow</code>", "<code>/etc/passwd</code>", "<code>/etc/group</code>", "<code>/etc/login.defs</code>"],
         "<code>/etc/passwd</code> vs <code>/etc/shadow</code>：早年 Unix 密碼放在 <code>/etc/passwd</code>，但所有使用者與程式皆需讀取該檔以解析 UID/GID，駭客可輕易複製雜湊值離線暴力破解；現代架構將 <code>/etc/passwd</code> 第二欄標記為 <code>x</code>，真正以 SHA-512/yescrypt 加密之雜湊與密碼過期策略抽離至 <code>/etc/shadow</code>，權限設為 <code>000</code> 或 <code>640 (root:shadow)</code>，極大化資安防護。"),

        ("在 Linux SSH 伺服器安全性強化（Hardening）中，為防止外部暴力破解攻擊，最關鍵之 <code>/etc/ssh/sshd_config</code> 設定組合為？",
         "停用 root 遠端直接登入（<code>PermitRootLogin no</code>）並停用密碼驗證強制僅限金鑰認證（<code>PasswordAuthentication no</code>）",
         ["停用 root 遠端直接登入（<code>PermitRootLogin no</code>）並停用密碼驗證強制僅限金鑰認證（<code>PasswordAuthentication no</code>）",
          "將 SSH 埠號開放給全世界且無密碼直接登入",
          "將所有使用者之密碼皆改為 123456",
          "關閉 SSH 防火牆規則並允許匿名 FTP"],
         "SSH 伺服器安全加固準則：公務伺服器上線必備：1. <code>PermitRootLogin no</code>：禁止外部直接登入最高特權 root，強迫以一般帳號登入再 <code>sudo</code>，留下審計軌跡；2. <code>PasswordAuthentication no</code>：禁用弱密碼，改採 4096-bit RSA 或 Ed25519 非對稱公私鑰認證（Public Key Authentication）；3. 變更預設 Port 22；4. 搭配 Fail2ban 阻斷暴力嘗試。"),

        ("在 Docker 容器操作中，若欲自終端機進入一個正在背景運行的容器 <code>web-server</code> 內部，並開啟互動式 Bash Shell 進行除錯，標準命令為？",
         "<code>docker exec -it web-server /bin/bash</code>",
         ["<code>docker exec -it web-server /bin/bash</code>",
          "<code>docker run -d web-server</code>",
          "<code>docker start web-server</code>",
          "<code>docker build -t web-server .</code>"],
         "Docker exec 互動命令：<code>docker exec [參數] [容器名稱/ID] [指令]</code>。參數 <code>-i</code>（Interactive，保持標準輸入開放）、<code>-t</code>（TTY，分配虛擬終端終端），組合 <code>-it</code> 即可讓管理員獲得該容器內部隔離命名空間中的互動式 Shell，且退出時容器依然持續在背景運行不中斷。"),

        ("在虛擬化技術分類中，Hypervisor（虛擬機器監視器）分為 Type 1 與 Type 2。下列何者屬於「直接安裝運行於實體裸機硬體之上，無中介宿主作業系統」之 Type 1（Bare-Metal）虛擬化平台？",
         "VMware ESXi（或 Proxmox VE、KVM）",
         ["VMware ESXi（或 Proxmox VE、KVM）",
          "VirtualBox（運行於 Windows 桌面）",
          "VMware Workstation（運行於 macOS 或 Linux 桌面）",
          "瀏覽器外掛擴充程式"],
         "Hypervisor 分類辨析：1. Type 1（裸機型 Bare-Metal）：Hypervisor 本身就是微型作業系統，直接掌控實體 CPU、記憶體與硬體虛擬化指令（Intel VT-x/AMD-V），效能開銷極小（&lt; 2%），如 VMware ESXi、Proxmox VE、Xen；2. Type 2（代管型 Hosted）：運行於傳統主機 OS（如 Windows/macOS）之上作為應用程式，虛擬化請求需經過 Host OS 轉發，效能開銷較大，如 VirtualBox、VMware Workstation。"),

        ("在 Linux 日誌稽核中，由 systemd 集中管理的系統二進位日誌，應使用下列何種命令進行即時串流追蹤與錯誤篩選？",
         "<code>journalctl -xeu [服務名稱]</code>",
         ["<code>journalctl -xeu [服務名稱]</code>",
          "<code>syslog -read</code>",
          "<code>tail /etc/log.txt</code>",
          "<code>cat /proc/log</code>"],
         "journalctl 日誌查詢利器：systemd-journald 服務統一接管所有系統與服務日誌。參數 <code>-u [服務名]</code>（篩選特定 systemd 單元）、<code>-e</code>（跳轉至日誌末端）、<code>-x</code>（附加詳細解釋訊息）、<code>-f</code>（Follow 即時串流監控）、<code>-p err</code>（僅顯示錯誤等級以上日誌）。"),

        ("在 Linux 檔案屬性中，用以防止即使是最高特權的 <code>root</code> 使用者也「絕對無法修改、刪除、覆寫或重新命名」某關鍵公務設定檔（如 <code>/etc/resolv.conf</code>）之底層擴充屬性指令為？",
         "<code>chattr +i /etc/resolv.conf</code>（設定 Immutable 不可變屬性）",
         ["<code>chattr +i /etc/resolv.conf</code>（設定 Immutable 不可變屬性）",
          "<code>chmod 000 /etc/resolv.conf</code>",
          "<code>chown nobody /etc/resolv.conf</code>",
          "<code>rm -f /etc/resolv.conf</code>"],
         "Linux 擴充檔案屬性 chattr +i：傳統 Linux 權限中 root 擁有絕對特權（即使 chmod 000，root 也能強制寫入）。<code>chattr +i</code>（Immutable）在 ext4/xfs 檔案系統層面加鎖，任何使用者（包含 root）皆無法修改、刪除、建立連結。需先執行 <code>chattr -i</code> 解鎖後始得變更，是防範勒索軟體與木馬竄改系統設定檔之高階防禦技巧。"),

        ("在 Linux 中，用以檢視本機各網路介面之 IP 位址、MAC 位址與鏈路狀態之現代標準命令為？",
         "<code>ip addr show</code>（或簡寫 <code>ip a</code>）",
         ["<code>ip addr show</code>（或簡寫 <code>ip a</code>）",
          "<code>route -all</code>",
          "<code>arp -who</code>",
          "<code>hostname -ip</code>"],
         "iproute2 工具集：現代 Linux 發行版全面以 <code>ip</code> 指令取代傳統已過時之 <code>net-tools</code>（ifconfig/route）。<code>ip addr show</code> 查詢 IP 與 MAC；<code>ip link set eth0 up/down</code> 啟用/停用網卡；<code>ip route show</code> 查詢路由表。")
,

        ("在 Ubuntu/Debian 體系之 Linux 公務伺服器維護中，用以「更新本地套件清單索引快取，並將系統中所有已知過期套件全數升級至最新安全版本」之標準 APT 指令組合為？",
         "<code>sudo apt update && sudo apt upgrade -y</code>",
         ["<code>sudo apt update && sudo apt upgrade -y</code>",
          "<code>sudo apt remove --all</code>",
          "<code>sudo apt install windows-update</code>",
          "<code>sudo apt clean --force-delete</code>"],
         "APT 套件管理雙核心指令：<code>apt update</code> 負責向軟體來源伺服器（Repository）下載最新的套件清單索引檔案（存於 /var/lib/apt/lists/），但不實際安裝或升級套件；隨後執行的 <code>apt upgrade -y</code> 才會真正比對本機已安裝版本，下載並安裝各套件與核心之最新安全性更新修補檔。")
    ]

    all_datasets = [
        ("作業系統核心架構、行程狀態、PCB 與 CPU 排程", data1),
        ("行程同步、臨界區間、死結與記憶體管理", data2),
        ("Linux 系統管理、Shell 指令、權限與檔案系統", data3)
    ]

    for tag, dataset in all_datasets:
        for stem, ans_s, opts, expl in dataset:
            choices = [("A", opts[0]), ("B", opts[1]), ("C", opts[2]), ("D", opts[3])]
            qs.append({
                "tag": "計算機概要",
                "stem": stem,
                "choices": choices,
                "ans": "A",
                "ans_text": f"(A) {ans_s}",
                "explanation": f"""<strong>【地方特考四等公務實務情境深度解析】</strong><br>
<div class="step-box">
  <div class="step-title">🐧 地方政府作業系統運作、並行排程與 Linux 主機管理實務</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge formula">步驟 1</span><strong>釐清核心架構概念/公式演算法與公務機關實務環境</strong><br>
      ‧ 本題依據國家考試地方特考四等《計算機概要》考綱，緊扣作業系統核心、行程生命週期、同步死結防護及 Linux 維運指令嚴謹命題。
    </li>
    <li class="step-item"><span class="step-badge check">步驟 2</span><strong>詳細計算推導與技術原理對照</strong><br>
      ‧ {expl}
    </li>
  </ul>
</div>
<br><strong>【各選項詳細對錯解析】</strong><br>
‧ <strong>(A) 正確</strong>：{opts[0]}。<br>
‧ <strong>(B) 錯誤</strong>：{opts[1]}（觀念混淆、排程算法計算錯誤或系統機制不合）。<br>
‧ <strong>(C) 錯誤</strong>：{opts[2]}（極端荒謬之技術處置或錯誤之名詞定義）。<br>
‧ <strong>(D) 錯誤</strong>：{opts[3]}（非業界規範或違背作業系統基礎運作原理）。<br><br>
<strong>地特加分角度</strong>：地方特考四等在作業系統考點中，<strong>CPU 排程演算法等待時間計算</strong>、<strong>死結四條件與銀行家演算法</strong>、<strong>Linux 權限換算（chmod/umask）</strong>與<strong>行程 vs 執行緒資源模型</strong>為命題核心。作答時清楚呈現<strong>核心機制運作步驟</strong>，可穩拿最高分。"""
            })

    return qs

if __name__ == '__main__':
    qs = get_local4_part2_questions()
    print(f"Total Part 2 questions generated: {len(qs)}")
