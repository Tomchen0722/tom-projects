# -*- coding: utf-8 -*-
"""課程內容總索引。

每一條「學習路線」(track) 是一個 Python 檔案，
裡面是一個 dict，結構如下：

TRACK = {
  "id":        路線代號，例如 "t2-network"
  "title":     路線名稱
  "code":      對應的證照代號
  "stage":     1=打底 / 2=核心 / 3=攻防 / 4=企業
  "stageName": 階段名稱
  "color":     主色調 token 名稱
  "tagline":   一句話介紹
  "goal":      學完可以做到什麼
  "chapters":  章節清單
}

每一章 (chapter) 的結構：

{
  "id":       章節代號（全站唯一）
  "title":    章節標題
  "subtitle": 副標
  "level":    入門 / 進階 / 企業
  "minutes":  預估閱讀分鐘
  "summary":  一句話總結
  "why":      為什麼要學（用生活比喻）
  "sections": [{"heading":..., "body":..., "example":..., "note":...}]
  "diagram":  SVG 圖解字串（可省略）
  "table":    {"caption":..., "head":[...], "rows":[[...]]}（可省略）
  "labs":     [{"title":..., "goal":..., "warn":...,
                "steps":[{"cmd":..., "explain":..., "output":...}]}]
  "quiz":     [{"q":..., "options":[...], "answer": 索引, "why":...}]
  "keywords": [搜尋關鍵字]
  "takeaway": 帶走這三句
}
"""

from .t1_foundations import TRACK as T1
from .t2_network import TRACK as T2
from .t3_linux import TRACK as T3
from .t4_security_plus import TRACK as T4
from .t5_cnd import TRACK as T5
from .t6_ceh import TRACK as T6
from .t7_cysa import TRACK as T7
from .t8_enterprise import TRACK as T8

TRACKS = [T1, T2, T3, T4, T5, T6, T7, T8]

# ---------------------------------------------------------------------------
# 名詞小辭典：模擬終端機的 man 指令、以及「術語表」頁面都會用到
# ---------------------------------------------------------------------------
GLOSSARY = {
    "cia": "資安三本柱：Confidentiality 機密性（不該看的人看不到）、"
           "Integrity 完整性（資料沒被偷改）、Availability 可用性（該用的時候用得到）。",
    "aaa": "Authentication 你是誰、Authorization 你能做什麼、"
           "Accounting 你做了什麼（留紀錄）。企業權限設計的骨架。",
    "0day": "零日漏洞：廠商還沒出修補程式就被拿去攻擊的漏洞。防不了「補丁」，"
            "只能靠分層防禦與偵測。",
    "apt": "Advanced Persistent Threat 進階持續威脅：有組織、有資源、"
           "長期潛伏在你網路裡的攻擊者，通常是國家級或犯罪集團。",
    "arp": "Address Resolution Protocol：在同一個區網裡用 IP 問出 MAC 位址的協定。"
           "沒有驗證機制，所以會被 ARP 欺騙。",
    "chmod": "change mode：改檔案權限。chmod 640 file 代表擁有者可讀寫、"
             "群組唯讀、其他人不能看。",
    "cve": "Common Vulnerabilities and Exposures：全世界公開漏洞的統一編號，"
           "例如 CVE-2021-44228（Log4Shell）。",
    "cvss": "漏洞嚴重度評分 0.0–10.0。9.0 以上是 Critical，要優先修。",
    "dmz": "非軍事區：放對外服務（網站、郵件）的隔離網段。就算被攻破，"
           "也進不了內部核心網路。",
    "dns": "把網域名稱翻成 IP 的電話簿服務。UDP/TCP port 53。",
    "edr": "Endpoint Detection and Response：端點偵測與回應。比防毒更進一步，"
           "會記錄行為、可以遠端隔離主機。",
    "iptables": "Linux 傳統封包過濾防火牆指令。新系統多改用 nftables 或 firewalld。",
    "journalctl": "systemd 的日誌查詢工具。journalctl -u sshd 只看 sshd 的日誌。",
    "kerberos": "Windows 網域的預設認證協定，用「票證」代替反覆傳密碼。",
    "mfa": "多因子驗證：知道的（密碼）＋擁有的（手機/金鑰）＋本身的（指紋）"
           "至少兩種。擋掉絕大多數帳密外洩攻擊。",
    "mitre": "MITRE ATT&CK：把真實攻擊者的手法整理成矩陣（戰術 × 技術）的知識庫，"
             "藍隊用它盤點偵測涵蓋率。",
    "nmap": "網路掃描工具，用來確認「哪些主機活著、開了哪些 port、跑什麼服務」。"
            "只能掃自己有權限的目標。",
    "siem": "Security Information and Event Management：把全公司日誌集中、"
            "關聯分析、產生告警的平台。",
    "soar": "Security Orchestration, Automation and Response："
            "把重複的處理流程自動化（自動封 IP、自動隔離主機）。",
    "soc": "Security Operations Center 資安維運中心，24 小時盯告警的團隊。",
    "ss": "socket statistics：看目前連線與監聽 port。ss -tulnp 是最常用的組合。",
    "ssh": "Secure Shell，加密的遠端登入協定，TCP port 22。",
    "tcpdump": "命令列封包擷取工具。tcpdump -i eth0 port 53 只抓 DNS 流量。",
    "tls": "傳輸層加密，https 底下那一層。現在應該用 TLS 1.2 以上。",
    "vlan": "虛擬區網：在同一台交換器上切出互不相通的邏輯網段，用來做網路分段。",
    "vpn": "虛擬私人網路：在不安全的網路上建一條加密隧道。",
    "waf": "Web Application Firewall：專門檔 SQL Injection、XSS 等網站攻擊的防火牆。",
    "xss": "Cross-Site Scripting：攻擊者把 JavaScript 塞進網頁，讓其他使用者的"
           "瀏覽器去執行。防法是輸出編碼。",
    "zero trust": "零信任：不因為「你在內網」就信任你。每一次存取都要重新驗證"
                  "身分、裝置、權限。",
}
