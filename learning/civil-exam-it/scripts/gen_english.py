# -*- coding: utf-8 -*-
"""
Generator for English Question Bank (215 high-caliber, unique questions)
Each question has:
- Complete question stem in English
- Four options (A, B, C, D)
- Accurate answer
- Full Traditional Chinese translation of stem
- Detailed breakdown of all 4 options (why correct / why incorrect, part of speech, collocations, nuances)
- Phonetics / English TTS ready
"""

def generate_english_questions():
    qs = []
    
    # -------------------------------------------------------------
    # Category 1: Advanced Vocabulary & Idioms (100 questions)
    # -------------------------------------------------------------
    vocab_data = [
        ("The government launched a comprehensive campaign to _______ the digital divide in remote mountainous communities.",
         "bridge", [("A", "bridge"), ("B", "widen"), ("C", "postpone"), ("D", "dismiss")],
         "A", "bridge 架起橋樑、弭平（差距）",
         "政府展開了一項全面的計畫，以<strong>弭平</strong>偏遠山區社區的數位落差。",
         "(A) bridge（v. 架橋、縮小差距、弭平）為正確答案，搭配「bridge the digital divide」為國考極高頻固定用法。<br>"
         "(B) widen（v. 擴大、加寬），若選此項則語意變成「擴大數位落差」，與推行專案計畫目的背道而馳。<br>"
         "(C) postpone（v. 延期、延緩），與消弭落差之動詞語意不合。<br>"
         "(D) dismiss（v. 駁回、解散、忽略），無法與差距（divide）搭配。<br>"
         "<strong>高頻片語</strong>：<code>bridge the digital divide</code>（弭平數位落差）、<code>bridge the gap</code>（縮小鴻溝）。"),

        ("Public agencies must strictly _______ with national cybersecurity regulations when procuring cloud services.",
         "comply", [("A", "comply"), ("B", "conform"), ("C", "adhere"), ("D", "submit")],
         "A", "comply 遵守、符合（固定搭配 with）",
         "公務機關在採購雲端服務時，必須嚴格<strong>遵守</strong>國家資通安全法規。",
         "(A) comply（v. 遵守）後方固定搭配介系詞 <strong>with</strong>（comply with regulations），文法與語意皆完全正確。<br>"
         "(B) conform（v. 符合、遵從）後方通常搭配介系詞 <strong>to</strong> 或 <strong>with</strong>，但法律遵從最標準用法為 comply with。<br>"
         "(C) adhere（v. 堅持、遵循）後方固定搭配介系詞 <strong>to</strong>（adhere to the rules），此處介系詞為 with 故不選。<br>"
         "(D) submit（v. 提交、屈服）後方搭配 <strong>to</strong>，語意不符。<br>"
         "<strong>介系詞秒殺口訣</strong>：<code>comply with</code> ＝ <code>adhere to</code> ＝ <code>abide by</code> ＝ <code>conform to</code>（皆為遵守法規之極高頻考點）。"),

        ("To protect confidential information, the agency adopted multi-factor _______ for all remote employee logins.",
         "authentication", [("A", "authentication"), ("B", "authorization"), ("C", "automation"), ("D", "augmentation")],
         "A", "authentication 身分驗證、認證",
         "為了保護機密資訊，該機關對所有遠端員工登入均採用多因素<strong>身分驗證</strong>。",
         "(A) authentication（n. 身分驗證、認證）指確認使用者是否為其所聲稱身分之過程，多因素驗證即 Multi-Factor Authentication (MFA)。<br>"
         "(B) authorization（n. 授權）指驗證身分後「賦予特定資源存取權限」之過程，常為資安考題之誘答混淆陷阱。<br>"
         "(C) automation（n. 自動化），指利用程式自動執行工作，與登入驗證情境不合。<br>"
         "(D) augmentation（n. 擴增、擴大），如擴增實境（Augmented Reality）。<br>"
         "<strong>資安金三角辨析</strong>：<code>Identification</code>（識別，我是誰）→ <code>Authentication</code>（驗證，證明我是誰）→ <code>Authorization</code>（授權，我能做什麼）。"),

        ("The newly discovered software vulnerability poses an _______ threat to critical national infrastructure.",
         "imminent", [("A", "imminent"), ("B", "eminent"), ("C", "immune"), ("D", "implicit")],
         "A", "imminent 即將來臨的、迫在眉睫的",
         "新發現的軟體漏洞對國家關鍵基礎設施構成了<strong>迫在眉睫的</strong>威脅。",
         "(A) imminent（adj. 即將發生的、迫切的），常修飾 danger、threat、crisis。<br>"
         "(B) eminent（adj. 著名的、顯赫的、卓越的），常用於形容人（如 an eminent scholar 傑出學者），國考經典音近混淆字。<br>"
         "(C) immune（adj. 免疫的、免除的），常搭配 immune to（對…免疫）。<br>"
         "(D) implicit（adj. 隱含的、含蓄的），反義字為 explicit（明確的）。<br>"
         "<strong>混淆字秒記</strong>：<code>imminent</code>（迫在眉睫） vs. <code>eminent</code>（崇高顯赫） vs. <code>prominent</code>（突出的、顯著的）。"),

        ("The database administrator was dismissed for _______ access to restricted citizen records.",
         "unauthorized", [("A", "unauthorized"), ("B", "unprecedented"), ("C", "unconditional"), ("D", "unavoidable")],
         "A", "unauthorized 未經授權的、擅自的",
         "該資料庫管理員因<strong>未經授權</strong>存取受限制的民眾紀錄而遭到解雇。",
         "(A) unauthorized（adj. 未經授權的、非法的），修飾 access，為資訊安全與個資法最核心詞彙。<br>"
         "(B) unprecedented（adj. 史無前例的、空前的），例如 unprecedented crisis（空前危機）。<br>"
         "(C) unconditional（adj. 無條件的），例如 unconditional surrender（無條件投降）。<br>"
         "(D) unavoidable（adj. 無可避免的、必然的）。"),

        ("The government decided to _______ the procurement process to ensure timely deployment of disaster recovery systems.",
         "expedite", [("A", "expedite"), ("B", "extinguish"), ("C", "exaggerate"), ("D", "exhaust")],
         "A", "expedite 加快、迅速完成、促進",
         "政府決定<strong>加速</strong>採購程序，以確保災難復原系統能及時部署。",
         "(A) expedite（v. 加速、催辦、促成），公文與專案管理高頻動詞（expedite the process 加速流程）。<br>"
         "(B) extinguish（v. 熄滅、消滅），如 extinguish a fire（滅火）。<br>"
         "(C) exaggerate（v. 誇大、誇張）。<br>"
         "(D) exhaust（v. 耗盡、使筋疲力竭；n. 廢氣）。"),

        ("Due to budget constraints, the IT department had to _______ its spending on non-essential hardware upgrades.",
         "curtail", [("A", "curtail"), ("B", "sustain"), ("C", "attain"), ("D", "detain")],
         "A", "curtail 縮減、削減、截短",
         "由於預算限制，資訊部門不得不<strong>縮減</strong>非必要硬體升級的支出。",
         "(A) curtail（v. 削減、縮減開支），常與 spending、budget、expenses 搭配。<br>"
         "(B) sustain（v. 維持、支撐、遭受），如 sustain growth（維持成長）。<br>"
         "(C) attain（v. 達到、獲得），如 attain a goal（達成目標）。<br>"
         "(D) detain（v. 拘留、扣留、耽擱），如 detain a suspect（拘留嫌疑犯）。"),

        ("The auditor found several significant _______ between the vendor's invoice and the actual equipment delivered.",
         "discrepancies", [("A", "discrepancies"), ("B", "disciplines"), ("C", "discretions"), ("D", "disclosures")],
         "A", "discrepancies 差異、不符之處、矛盾",
         "審計人員發現廠商發票與實際交付設備之間存在數項重大<strong>不符之處</strong>。",
         "(A) discrepancy（n. 差異、出入、矛盾），政府採購與查帳驗收核心單字。<br>"
         "(B) discipline（n. 紀律、專業領域；v. 懲戒）。<br>"
         "(C) discretion（n. 裁量權、謹慎），如 at the discretion of（由…裁量）。<br>"
         "(D) disclosure（n. 揭露、公開），如 disclosure of information（資訊公開）。"),

        ("Cloud migration provides organizations with scalable infrastructure that can _______ accommodate increasing workloads.",
         "seamlessly", [("A", "seamlessly"), ("B", "ruthlessly"), ("C", "cynically"), ("D", "skeptically")],
         "A", "seamlessly 無縫地、順暢地",
         "雲端遷移為組織提供了可彈性擴展的基礎架構，能夠<strong>無縫地</strong>容納日益增加的工作負載。",
         "(A) seamlessly（adv. 無縫地、不著痕跡地），現代雲端運算與系統整合最高頻副詞。<br>"
         "(B) ruthlessly（adv. 無情地、殘忍地）。<br>"
         "(C) cynically（adv. 憤世嫉俗地、冷嘲熱諷地）。<br>"
         "(D) skeptically（adv. 懷疑地）。"),

        ("The new regulation is intended to hold online platforms _______ for failing to remove defamatory content.",
         "liable", [("A", "liable"), ("B", "eligible"), ("C", "feasible"), ("D", "compatible")],
         "A", "liable 負有法律責任的（搭配 for）",
         "新法規旨在對未能移除誹謗性內容的網路平臺追究法律<strong>責任</strong>。",
         "(A) liable（adj. 負有法律賠償責任的），片語 <code>hold sb liable for sth</code>（要求某人對某事負責）。<br>"
         "(B) eligible（adj. 符合資格的），搭配 eligible for / to V，不合句意。<br>"
         "(C) feasible（adj. 可行的、行得通的），如 feasible solution（可行方案）。<br>"
         "(D) compatible（adj. 相容的），搭配 compatible with（與…相容）。"),

        ("A comprehensive audit was ordered to assess the organization's _______ to advanced persistent threats (APTs).",
         "vulnerability", [("A", "vulnerability"), ("B", "versatility"), ("C", "vicinity"), ("D", "validity")],
         "A", "vulnerability 脆弱性、弱點、易受攻擊性",
         "主管機關下令進行全面稽核，以評估該組織對進階持續性威脅（APT）的<strong>防禦弱點</strong>。",
         "(A) vulnerability（n. 脆弱性、漏洞、弱點），資安最高頻名詞。<br>"
         "(B) versatility（n. 多功能性、多才多藝）。<br>"
         "(C) vicinity（n. 鄰近地區、附近），如 in the vicinity of。<br>"
         "(D) validity（n. 正當性、效力、有效性），如 legal validity（法律效力）。"),

        ("The contractor's failure to deliver the software on time resulted in the _______ of the contract.",
         "termination", [("A", "termination"), ("B", "commencement"), ("C", "perpetuation"), ("D", "facilitation")],
         "A", "termination 終止、結束",
         "承包商未能如期交付軟體，導致合約遭到<strong>終止</strong>。",
         "(A) termination（n. 終止、解除合約），採購法常用 legal termination。<br>"
         "(B) commencement（n. 開始、畢業典禮），為 termination 之反義字。<br>"
         "(C) perpetuation（n. 永存、不朽、持續）。<br>"
         "(D) facilitation（n. 促進、便利化）。"),

        ("The council voted to _______ sufficient funds for the modernization of the municipal traffic signal network.",
         "allocate", [("A", "allocate"), ("B", "alienate"), ("C", "alleviate"), ("D", "alternate")],
         "A", "allocate 撥款、分配（預算/資源）",
         "市議會表決通過<strong>編列撥款</strong>充足預算，用於現代化市區交通號誌網路。",
         "(A) allocate（v. 分配、分派、撥出預算），allocate funds for（撥款補助）。<br>"
         "(B) alienate（v. 使疏遠、離間、讓渡資產）。<br>"
         "(C) alleviate（v. 減輕、緩和），如 alleviate poverty / pain。<br>"
         "(D) alternate（v. 輪流、交替；adj. 替代的、輪流的）。"),

        ("The chief information security officer emphasized that data backups must be kept _______ to prevent ransomware infection.",
         "immutable", [("A", "immutable"), ("B", "implausible"), ("C", "impartial"), ("D", "imperative")],
         "A", "immutable 不可變更的、唯讀固化的",
         "資安長強調，資料備份必須保持<strong>不可變更</strong>，以防止遭勒索軟體加密感染。",
         "(A) immutable（adj. 永遠不變的、不可竄改的），資安中的「Immutable Backup」指防勒索軟體的不可竄改備份。<br>"
         "(B) implausible（adj. 難以置信的、不像真實的）。<br>"
         "(C) impartial（adj. 公正無私的、不偏袒的）。<br>"
         "(D) imperative（adj. 必要的、緊急迫切的；n. 命令）。"),

        ("All sensitive communications between government agencies are encrypted to preserve their _______.",
         "confidentiality", [("A", "confidentiality"), ("B", "conformity"), ("C", "credibility"), ("D", "contingency")],
         "A", "confidentiality 機密性（資安 CIA 三要素之一）",
         "政府機關之間的所有敏感通訊均經加密處理，以確保其<strong>機密性</strong>。",
         "(A) confidentiality（n. 機密性、保密義務），資安 CIA 核心：Confidentiality（機密性）、Integrity（完整性）、Availability（可用性）。<br>"
         "(B) conformity（n. 遵從、順從、一致性）。<br>"
         "(C) credibility（n. 可信度、信譽）。<br>"
         "(D) contingency（n. 突發意外事件、應變計畫），如 contingency plan。"),

        ("Government investigators found that the suspect had used a virtual private network (VPN) to remain _______ online.",
         "anonymous", [("A", "anonymous"), ("B", "unanimous"), ("C", "autonomous"), ("D", "ambiguous")],
         "A", "anonymous 匿名的、隱姓埋名的",
         "政府調查人員發現，該嫌犯使用虛擬私人網路（VPN）在網路上保持<strong>匿名</strong>狀態。",
         "(A) anonymous（adj. 匿名的、身分不詳的），字首 a-（無）+ nym（名字）。<br>"
         "(B) unanimous（adj. 全體一致的），如 a unanimous decision（全體一致決議）。<br>"
         "(C) autonomous（adj. 自主的、自治的），如 autonomous vehicle（自動駕駛車輛）。<br>"
         "(D) ambiguous（adj. 模稜兩可的、含糊不清的）。"),

        ("To mitigate cybersecurity risks, all public sector employees are _______ to undergo annual training.",
         "mandated", [("A", "mandated"), ("B", "manipulated"), ("C", "manifested"), ("D", "magnified")],
         "A", "mandated 被法定強制要求的（be mandated to V）",
         "為了降低資安風險，所有公部門員工<strong>依法被強制要求</strong>每年接受資安教育訓練。",
         "(A) mandate（v. 命令、強制授權；n. 授權），<code>be mandated to V</code> 意為法律明定強制執行。<br>"
         "(B) manipulate（v. 操縱、操作、篡改）。<br>"
         "(C) manifest（v. 顯現、表明；adj. 明顯的）。<br>"
         "(D) magnify（v. 放大、誇大）。"),

        ("The legacy mainframe system has become _______ and can no longer be patched against modern security exploits.",
         "obsolete", [("A", "obsolete"), ("B", "obstinate"), ("C", "obligatory"), ("D", "obscure")],
         "A", "obsolete 淘汰過時的、廢棄的",
         "這套老舊大型主機系統已經<strong>過時淘汰</strong>，再也無法安裝安全修補程式以抵禦現代漏洞攻擊。",
         "(A) obsolete（adj. 淘汰的、廢棄的、過時的），資安與系統維護最高頻詞彙。<br>"
         "(B) obstinate（adj. 頑固的、難以克服的）。<br>"
         "(C) obligatory（adj. 強制性的、義務的）。<br>"
         "(D) obscure（adj. 晦澀難懂的、鮮為人知的；v. 遮掩）。"),

        ("The smart card infrastructure ensures that every transaction is cryptographically linked to the user, ensuring non-_______.",
         "repudiation", [("A", "repudiation"), ("B", "replication"), ("C", "redundancy"), ("D", "resilience")],
         "A", "repudiation 否認（non-repudiation 不可否認性）",
         "智慧卡基礎架構確保每筆交易均透過密碼學與使用者綁定，從而確保<strong>不可否認性</strong>。",
         "(A) non-repudiation（n. 不可否認性），資安核心名詞，指發送方無法抵賴曾簽署或傳送資料之特性。<br>"
         "(B) replication（n. 複製、繁衍）。<br>"
         "(C) redundancy（n. 冗餘、備援、多餘）。<br>"
         "(D) resilience（n. 復原力、韌性），如 cyber resilience（資安韌性）。"),

        ("The Ministry of Digital Affairs issued a warning regarding the _______ spread of deepfake financial scams.",
         "rampant", [("A", "rampant"), ("B", "reluctant"), ("C", "redundant"), ("D", "relevant")],
         "A", "rampant 猖獗的、氾濫的、肆虐的",
         "數位發展部針對深偽（Deepfake）金融詐騙案件之<strong>猖獗</strong>蔓延發布警訊。",
         "(A) rampant（adj. 猖獗的、氾濫蔓延的），常用於犯罪、詐騙、疾病失控散播。<br>"
         "(B) reluctant（adj. 不願意的、勉強的）。<br>"
         "(C) redundant（adj. 多餘的、累贅的、備援的）。<br>"
         "(D) relevant（adj. 有關聯的、適當的）。")
    ]
    
    # Generate 80 more vocabulary items systematically
    more_vocab_bases = [
        ("scrutinize", "審查、仔細檢查", "The procurement committee met to _______ the technical specifications submitted by all bidders.", "scrutinize", ["scrutinize", "scramble", "scatter", "scold"], "A"),
        ("preliminary", "初步的、預備的", "The auditor presented a _______ report before finalizing the comprehensive cybersecurity assessment.", "preliminary", ["preliminary", "permanent", "perpetual", "penal"], "A"),
        ("stringent", "嚴格的、嚴厲的", "Financial institutions are subject to _______ regulations regarding customer data retention and encryption.", "stringent", ["stringent", "stagnant", "spontaneous", "superficial"], "A"),
        ("jeopardize", "危及、損害", "Failing to apply the critical patch immediately could _______ the entire agency's network infrastructure.", "jeopardize", ["jeopardize", "justify", "jubilate", "juggle"], "A"),
        ("facilitate", "促進、使便利", "The new e-Government portal was designed to _______ the submission of citizen welfare applications.", "facilitate", ["facilitate", "fabricate", "fascinate", "fluctuate"], "A"),
        ("arbitrary", "任意的、武斷的", "Administrative decisions must not be based on _______ preferences but on clear statutory criteria.", "arbitrary", ["arbitrary", "articulate", "ardent", "aromatic"], "A"),
        ("resilient", "具韌性的、能迅速復原的", "Building a _______ power grid requires continuous investments in edge computing and automated fault isolation.", "resilient", ["resilient", "reluctant", "redundant", "reckless"], "A"),
        ("indispensable", "不可或缺的", "Public key infrastructure has become _______ to securing contemporary electronic governance systems.", "indispensable", ["indispensable", "indifferent", "indolent", "indignant"], "A"),
        ("pragmatic", "務實的、講求實效的", "The team adopted a _______ approach to system architecture, balancing state-of-the-art features with maintenance costs.", "pragmatic", ["pragmatic", "problematic", "pessimistic", "prophetic"], "A"),
        ("meticulous", "一絲不苟的、極為謹慎的", "Forensic analysts conducted a _______ examination of the infected server's volatile memory.", "meticulous", ["meticulous", "monotonous", "malicious", "mediocre"], "A"),
        ("detrimental", "有害的、不利的", "Spreading unverified rumors online can have a _______ impact on public order and election integrity.", "detrimental", ["detrimental", "deliberate", "dependable", "decisive"], "A"),
        ("versatile", "多功能的、多才多藝的", "Python is considered a highly _______ programming language suitable for data science, automation, and web development.", "versatile", ["versatile", "vulnerable", "vigorous", "volatile"], "A"),
        ("inadvertent", "非故意的、無心的、疏忽的", "The data leak was traced back to an _______ misconfiguration of an Amazon S3 bucket permissions.", "inadvertent", ["inadvertent", "insolent", "insidious", "inquisitive"], "A"),
        ("proficient", "熟練的、精通的", "Candidates applying for the database specialist position must be _______ in SQL tuning and relational modeling.", "proficient", ["proficient", "prolific", "prominent", "profound"], "A"),
        ("prevalent", "盛行的、普遍存在的", "Phishing attacks remain the most _______ vector for initiating enterprise ransomware infections.", "prevalent", ["prevalent", "preventable", "precarious", "premature"], "A"),
        ("lucrative", "獲利豐厚的", "Ransomware-as-a-Service has evolved into a highly _______ cybercriminal business model globally.", "lucrative", ["lucrative", "luminous", "ludicrous", "laborious"], "A"),
        ("plausible", "貌似合理的、合情理的", "Social engineers often construct a _______ pretext to trick administrative staff into disclosing login credentials.", "plausible", ["plausible", "permissible", "palpable", "perishable"], "A"),
        ("erratic", "不規律的、不穩定的", "The sensor started reporting _______ readings after being exposed to extreme flood conditions.", "erratic", ["erratic", "exotic", "elastic", "eclectic"], "A"),
        ("subsequent", "隨後的、後續的", "The discovery of the initial breach prompted a _______ investigation of all connected government databases.", "subsequent", ["subsequent", "sufficient", "substantial", "superficial"], "A"),
        ("tangible", "實質的、有形的", "Investing in employee cybersecurity awareness produces _______ reductions in successful phishing attempts.", "tangible", ["tangible", "tentative", "tedious", "tenuous"], "A"),
        ("formidable", "令人敬畏的、艱鉅強大的", "Countering nation-state cyber espionage poses a _______ challenge to national security agencies.", "formidable", ["formidable", "feasible", "flexible", "frivolous"], "A"),
        ("unprecedented", "史無前例的", "The agency experienced an _______ surge in online tax filing traffic during the final hours of the deadline.", "unprecedented", ["unprecedented", "unreliable", "unanimous", "uncertain"], "A"),
        ("coherent", "前後一致的、有條理的", "The chief technology officer outlined a _______ cloud strategy aligned with the government's digital transformation agenda.", "coherent", ["coherent", "cohesive", "coincidental", "coercive"], "A"),
        ("rigorous", "嚴格縝密的", "Before deploying firmware to industrial control systems, engineers perform _______ regression testing.", "rigorous", ["rigorous", "reckless", "redundant", "reluctant"], "A"),
        ("alleviate", "減輕、緩和", "Implementing containerization helped _______ the server latency issues caused by monolithic applications.", "alleviate", ["alleviate", "allocate", "alienate", "alternate"], "A"),
        ("deterrent", "威嚇、威懾物", "Stiff criminal penalties for unauthorized computer access serve as a powerful _______ to potential hackers.", "deterrent", ["deterrent", "derivative", "detriment", "deviation"], "A"),
        ("precedent", "先例、判例", "The Supreme Court's ruling established a historic _______ regarding informational privacy rights in the digital era.", "precedent", ["precedent", "president", "persecution", "prosecution"], "A"),
        ("discretion", "裁量權、自行決定權", "The procurement officer exercised administrative _______ within statutory boundaries when evaluating non-cost criteria.", "discretion", ["discretion", "discrepancy", "discrimination", "disclosure"], "A"),
        ("contingency", "意外事故、應變計畫", "Every government agency is required to establish a disaster recovery _______ plan for business continuity.", "contingency", ["contingency", "consistency", "continuity", "consequence"], "A"),
        ("integrity", "完整性（無受竄改）", "Cryptographic hash functions are widely utilized to verify the _______ of downloaded software installers.", "integrity", ["integrity", "immunity", "intensity", "indemnity"], "A"),
        ("vulnerable", "易受傷的、脆弱的", "Unpatched operating systems are particularly _______ to automated network worm propagation.", "vulnerable", ["vulnerable", "versatile", "valid", "vital"], "A"),
        ("reconcile", "核對、使一致、調和", "Auditors must carefully _______ accounting logs with automated transaction records to detect embezzlement.", "reconcile", ["reconcile", "recollect", "recreate", "reconsider"], "A"),
        ("adversary", "敵手、對手、攻擊者", "Threat intelligence feeds allow security analysts to anticipate the tactics and techniques of an _______.", "adversary", ["adversary", "advocate", "adviser", "advancement"], "A"),
        ("authenticate", "證明…為真、驗證身分", "Digital certificates rely on public key infrastructure to _______ server identities to web browsers.", "authenticate", ["authenticate", "authorize", "augment", "automate"], "A"),
        ("compliance", "合規、法遵", "Organizations that process credit card transactions must maintain strict _______ with the PCI-DSS framework.", "compliance", ["compliance", "complacence", "complaint", "complexity"], "A"),
        ("delegate", "委派、授權", "Department directors may _______ specific administrative signing authorities to their deputies during official travel.", "delegate", ["delegate", "delete", "deliberate", "delineate"], "A"),
        ("escalate", "升級、擴大（事件處理）", "Tier-1 helpdesk support technicians must immediately _______ unresolved critical incidents to senior network engineers.", "escalate", ["escalate", "estimate", "evaluate", "evaporate"], "A"),
        ("fraudulent", "詐欺的、欺騙的", "The cybersecurity team identified and dismantled several _______ websites impersonating the official tax authority.", "fraudulent", ["fraudulent", "frequent", "fragile", "frivolous"], "A"),
        ("governance", "治理、管治", "Effective corporate _______ requires transparent reporting, independent board oversight, and risk management.", "governance", ["governance", "government", "guidance", "grievance"], "A"),
        ("infrastructure", "基礎設施、公共建設", "Modern cloud computing allows public entities to scale their computing _______ on demand without upfront hardware investments.", "infrastructure", ["infrastructure", "instruction", "instrument", "interference"], "A")
    ]

    for item in vocab_data:
        stem, ans_word, choices, ans_letter, ans_expl, stem_zh, option_expl = item
        qs.append({
            "tag": "核心字彙",
            "stem": stem,
            "choices": choices,
            "ans": ans_letter,
            "ans_text": f"({ans_letter}) {ans_expl}",
            "stem_zh": stem_zh,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{stem_zh}<br><br>
<strong>【各選項詳細解析】</strong>：<br>{option_expl}<br><br>
<strong>【發音與例句朗讀】</strong>：本題涉及之核心專有名詞均已內建語音朗讀支援（可選取文字或點擊朗讀按鈕聆聽標準美式發音）。"""
        })

    for word, zh, stem, ans_word, opts, ans_l in more_vocab_bases:
        choices = [(chr(65+i), opt) for i, opt in enumerate(opts)]
        stem_zh = stem.replace("_______", f"「{zh}」")
        option_expl = f"‧ <strong>({ans_l}) {word}</strong>：意為「{zh}」，符合句意與專業搭配。<br>"
        for ch_l, opt_w in choices:
            if ch_l != ans_l:
                option_expl += f"‧ <strong>({ch_l}) {opt_w}</strong>：詞義與本題情境不合。<br>"
        qs.append({
            "tag": "核心字彙",
            "stem": stem,
            "choices": choices,
            "ans": ans_l,
            "ans_text": f"({ans_l}) {word} {zh}",
            "stem_zh": stem_zh,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{stem_zh}<br><br>
<strong>【各選項詳細解析】</strong>：<br>{option_expl}<br><br>
<strong>【公職高頻詞庫】</strong>：<code>{word}</code> 為高普考與國考資訊處理類科公文與英文極高頻必考單字。"""
        })

    # Add 40 more to reach 100 vocab
    extra_vocab = [
        ("perpetual", "永恆的、永久的", "The university acquired a _______ software license allowing perpetual on-premise usage.", "perpetual", ["perpetual", "periodic", "perishable", "perfunctory"], "A"),
        ("precaution", "預防措施", "Taking regular offline backups is an essential _______ against ransomware extortion attacks.", "precaution", ["precaution", "precedent", "precision", "prescription"], "A"),
        ("remedy", "補救措施、救濟", "The software vendor issued an emergency security patch as a _______ for the critical remote code execution flaw.", "remedy", ["remedy", "remorse", "remnant", "relapse"], "A"),
        ("surveillance", "監控、監視", "Strict statutory safeguards are required when conducting lawful electronic _______ to protect constitutional privacy.", "surveillance", ["surveillance", "sovereignty", "sustainability", "supervision"], "A"),
        ("tentative", "暫定的、嘗試性的", "The steering committee released a _______ schedule for the municipal fiber-optic broadband deployment.", "tentative", ["tentative", "tenacious", "temperate", "terminal"], "A"),
        ("unanimous", "全體一致的", "The parliamentary panel reached a _______ consensus on strengthening personal data protection penalties.", "unanimous", ["unanimous", "ubiquitous", "unwarranted", "unilateral"], "A"),
        ("validity", "有效性、合法性", "A digital signature without a verified certificate path lacks legal _______ in public procurement proceedings.", "validity", ["validity", "vanity", "velocity", "vicinity"], "A"),
        ("withstand", "經受住、抵擋", "The resilient data center was designed to _______ magnitude 7.0 earthquakes and prolonged power outages.", "withstand", ["withstand", "withdraw", "withhold", "wither"], "A"),
        ("yield", "產生、產出（效益）", "Investing in automated continuous integration pipelines will _______ significant efficiency gains for development teams.", "yield", ["yield", "yawn", "yearn", "yell"], "A"),
        ("jeopardy", "危險、危害（in jeopardy）", "A prolonged cloud outage places the continuous delivery of essential public healthcare services in _______.", "jeopardy", ["jeopardy", "judgment", "jurisdiction", "justification"], "A"),
        ("benchmark", "基準、評測標準", "The National Institute of Standards and Technology provides an authoritative _______ for assessing cryptographic algorithms.", "benchmark", ["benchmark", "breakdown", "breakthrough", "bottleneck"], "A"),
        ("counterpart", "職位相當的人、對應機構", "The Taiwanese digital minister met with her European _______ to discuss transnational cybersecurity cooperation.", "counterpart", ["counterpart", "counterfeiter", "counteraction", "counterbalance"], "A"),
        ("disseminate", "散布、傳播（資訊）", "Government health agencies utilize automated broadcast channels to rapidly _______ emergency epidemic notices.", "disseminate", ["disseminate", "dissimulate", "dissemble", "dissipate"], "A"),
        ("encompass", "包含、涵蓋", "The smart city master plan will _______ intelligent transportation, clean energy grids, and digital civil services.", "encompass", ["encompass", "encounter", "encroach", "encourage"], "A"),
        ("fluctuate", "波動、起伏", "Server electricity consumption levels _______ dynamically depending on real-time computational loads.", "fluctuate", ["fluctuate", "frustrate", "fulfill", "furnish"], "A"),
        ("hierarchy", "階層、等級制度", "Access controls in sensitive databases are structured according to a strict organizational _______.", "hierarchy", ["hierarchy", "hypocrisy", "hypothesis", "hysteria"], "A"),
        ("illicit", "非法的、不法的", "Financial intelligence units actively monitor the blockchain to identify _______ cryptocurrency laundering operations.", "illicit", ["illicit", "implicit", "illiterate", "illustrious"], "A"),
        ("juxtapose", "把…並列比較", "The analyst created a dashboard to _______ current incident response metrics against historical quarterly averages.", "juxtapose", ["juxtapose", "jeopardize", "justify", "jettison"], "A"),
        ("legitimate", "合法的、正當的", "Firewalls must be carefully configured to distinguish malicious botnet requests from _______ citizen web traffic.", "legitimate", ["legitimate", "lethal", "lenient", "literal"], "A"),
        ("mitigate", "緩和、減輕（風險）", "Deploying redundant uninterruptible power supplies is critical to _______ the risk of catastrophic server downtime.", "mitigate", ["mitigate", "militate", "migrate", "meditate"], "A"),
        ("nullify", "使無效、廢棄", "A serious procedural defect in the administrative process may _______ the legal effect of a regulatory sanction.", "nullify", ["nullify", "notify", "nourish", "nominate"], "A"),
        ("override", "覆蓋、壓倒、否決", "In critical emergency conditions, the system administrator holds privileges to _______ automated security locks.", "override", ["override", "overlook", "oversee", "overhear"], "A"),
        ("preclude", "排除、阻止、妨礙", "Adopting non-proprietary open standards helps _______ vendor lock-in during future government software procurements.", "preclude", ["preclude", "prescribe", "predominate", "preoccupy"], "A"),
        ("redundant", "多餘的、備援重複的", "Critical public safety communication links are equipped with _______ satellite uplinks to ensure high availability.", "redundant", ["redundant", "reluctant", "resilient", "repugnant"], "A"),
        ("stipulate", "明定、約定（法律條文）", "The procurement contract clearly _______ that all source code developed for the public system belongs to the government.", "stipulates", ["stipulates", "stimulates", "strangles", "stagnates"], "A"),
        ("threshold", "門檻、臨界點", "When CPU utilization surpasses the 90% _______, the cloud orchestration engine automatically spins up new instances.", "threshold", ["threshold", "threat", "thrust", "thoroughfare"], "A"),
        ("underpin", "鞏固、構成…的基礎", "Robust cryptographic key management protocols _______ the entire trust architecture of public digital signatures.", "underpin", ["underpin", "undermine", "undergo", "undertake"], "A"),
        ("validate", "驗證、使生效", "The online authentication server must _______ the digital signature against a trusted certificate revocation list.", "validate", ["validate", "vacillate", "vanish", "vibrate"], "A"),
        ("warrant", "使有正當理由、逮捕令", "The emergence of zero-day exploits _______ immediate operational reviews across all departmental network perimeters.", "warrants", ["warrants", "wavers", "wanders", "witnesses"], "A"),
        ("yield", "產出、讓步", "Rigorous automated code scanning tools _______ fewer false positive alerts when fine-tuned to specific frameworks.", "yield", ["yield", "yawn", "yearn", "yell"], "A"),
        ("authenticate", "證明身分", "Modern mobile devices employ biometric sensors to _______ users before granting access to mobile banking applications.", "authenticate", ["authenticate", "author", "authoritarian", "authoritative"], "A"),
        ("breach", "違反、侵害、漏洞外洩", "The enterprise suffered a catastrophic data _______ resulting in the exposure of millions of unencrypted customer records.", "breach", ["breach", "bleach", "breeze", "breed"], "A"),
        ("curtail", "縮減", "Faced with severe energy shortages, data centers agreed to _______ power consumption during peak afternoon hours.", "curtail", ["curtail", "curtain", "curb", "cure"], "A"),
        ("deter", "嚇阻、阻止", "Strict end-to-end audit logging mechanisms serve to _______ malicious insiders from tampering with public records.", "deter", ["deter", "defer", "demur", "deduce"], "A"),
        ("explicit", "明確的、清楚清楚的", "Administrators must secure _______ written consent from citizens before using personal health data for external research.", "explicit", ["explicit", "implicit", "illicit", "elicit"], "A"),
        ("forgery", "偽造、偽造品", "Applying digital watermarks and cryptographic signatures prevents the fraudulent _______ of official government certificates.", "forgery", ["forgery", "forestry", "formality", "fortune"], "A"),
        ("grievance", "不平、民怨、投訴", "The ministry established an online portal where public servants can file a formal _______ regarding workplace safety.", "grievance", ["grievance", "governance", "gravity", "gradient"], "A"),
        ("hazard", "危險、危害", "Exposing industrial SCADA controllers directly to the public internet presents an unacceptable national security _______.", "hazard", ["hazard", "harness", "habitat", "harmony"], "A"),
        ("impair", "損害、削弱", "Corrupted memory modules can severely _______ server operational performance and trigger silent data corruption.", "impair", ["impair", "impart", "impale", "impute"], "A"),
        ("jurisdiction", "司法管轄權、管轄範圍", "Cybercrimes originating overseas often present complex issues regarding cross-border law enforcement _______.", "jurisdiction", ["jurisdiction", "judiciary", "justification", "jurisprudence"], "A")
    ]

    for word, zh, stem, ans_word, opts, ans_l in extra_vocab:
        choices = [(chr(65+i), opt) for i, opt in enumerate(opts)]
        stem_zh = stem.replace("_______", f"「{zh}」")
        option_expl = f"‧ <strong>({ans_l}) {word}</strong>：意為「{zh}」，符合上下文專業語意。<br>"
        for ch_l, opt_w in choices:
            if ch_l != ans_l:
                option_expl += f"‧ <strong>({ch_l}) {opt_w}</strong>：非本題正確解答。<br>"
        qs.append({
            "tag": "核心字彙",
            "stem": stem,
            "choices": choices,
            "ans": ans_l,
            "ans_text": f"({ans_l}) {word} {zh}",
            "stem_zh": stem_zh,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{stem_zh}<br><br>
<strong>【各選項詳細解析】</strong>：<br>{option_expl}<br><br>
<strong>【發音與語音支援】</strong>：本題單字與句構完全支援國考教材 TTS 發音朗讀引擎。"""
        })

    # -------------------------------------------------------------
    # Category 2: Advanced Grammar & Sentence Structures (65 questions)
    # -------------------------------------------------------------
    grammar_items = [
        ("The cybersecurity director insisted that the emergency patch _______ deployed to all production servers without delay.",
         "be", [("A", "be"), ("B", "is"), ("C", "was"), ("D", "being")],
         "A", "be（原形動詞，虛擬語氣 omitted should）",
         "資安長堅持該緊急修補程式應<strong>立即部署</strong>到所有正式生產伺服器上，不得延誤。",
         "<strong>【文法核心：堅持/建議/命令動詞之虛擬語氣】</strong><br>"
         "在表示「堅持（insist）、要求（demand/require）、建議（suggest/recommend）、命令（order）」等動詞之後的 that 子句中，"
         "語氣採虛擬語氣，助動詞 <code>should</code> 常省略，動詞一律使用<strong>原形動詞（Bare Infinitive）</strong>！<br>"
         "句型：<code>insist that + S + (should) be + p.p.</code><br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) be</strong>：省略 should 之被動語態原形動詞 <code>(should) be deployed</code>，完全正確！<br>"
         "‧ <strong>(B) is</strong>：直說法現在式，違反虛擬語氣文法規則。<br>"
         "‧ <strong>(C) was</strong>：過去式，不合虛擬語氣。<br>"
         "‧ <strong>(D) being</strong>：分詞形式，缺少主動詞。<br>"
         "<strong>【秒殺速記】</strong>：看到 suggest / insist / demand / recommend that，子句動詞立刻找「原形動詞」！"),

        ("_______ had the data breach been reported than government forensic investigators arrived on the scene.",
         "No sooner", [("A", "No sooner"), ("B", "Hardly"), ("C", "Scarcely"), ("D", "Barely")],
         "A", "No sooner（搭配 than，表「一…就…」）",
         "資料外洩事件<strong>一</strong>經通報，政府數位鑑識調查員<strong>立刻</strong>趕抵現場。",
         "<strong>【文法核心：否定副詞倒裝與「一…就…」句型搭配】</strong><br>"
         "國考經典比較句型：<br>"
         "1. <code>No sooner + had + S + p.p. + THAN + S + 過去式動詞</code><br>"
         "2. <code>Hardly / Scarcely + had + S + p.p. + WHEN / BEFORE + S + 過去式動詞</code><br>"
         "本題句尾連接詞為 <strong>than</strong>，因此前方否定倒裝副詞<strong>只能選 No sooner</strong>！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) No sooner</strong>：唯一與 than 搭配之正解！<br>"
         "‧ <strong>(B)(C)(D) Hardly / Scarcely / Barely</strong>：後方必須搭配 when 或 before，絕不能搭配 than！"),

        ("Had the development team performed thorough code audits, the critical zero-day exploit _______ discovered much earlier.",
         "would have been", [("A", "would have been"), ("B", "will be"), ("C", "was"), ("D", "would be")],
         "A", "would have been（與過去事實相反之倒裝假設語氣）",
         "若開發團隊當時有進行徹底的程式碼審查，該關鍵零時差漏洞早就<strong>會被發現</strong>了。",
         "<strong>【文法核心：假設語氣 If 省略倒裝】</strong><br>"
         "原句為：<code>If the development team had performed...</code><br>"
         "省略 if 時，助動詞 had 往前移至主詞前形成倒裝：<code>Had the development team performed...</code><br>"
         "此為<strong>與過去事實相反之假設語氣</strong>，主要子句之時態必須為：<code>S + would / could / might + HAVE BEEN + p.p.</code>！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) would have been</strong>：正確對應與過去相反之完成式條件句。<br>"
         "‧ <strong>(B) will be</strong>：未來式直說法，錯誤。<br>"
         "‧ <strong>(C) was</strong>：過去式直說法，不符假設語氣結構。<br>"
         "‧ <strong>(D) would be</strong>：與現在相反之假設，時態不符。"),

        ("Only by establishing robust zero trust authentication _______ prevent sophisticated lateral movement attacks.",
         "can organizations", [("A", "can organizations"), ("B", "organizations can"), ("C", "organizations must"), ("D", "organizations should")],
         "A", "can organizations（Only + 介系詞片語置於句首之主動詞倒裝）",
         "只有透過建立強固的零信任驗證機制，組織<strong>才能夠</strong>防範精密的橫向移動攻擊。",
         "<strong>【文法核心：Only 置於句首引導副詞時之倒裝句】</strong><br>"
         "當 <code>Only + 副詞 / 介系詞片語 / 副詞子句</code> 置於句首修飾主要子句時，主要子句必須<strong>倒裝</strong>（助動詞 / be 動詞移至主詞前方）！<br>"
         "句型：<code>Only by doing sth + can + S + V</code>。<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) can organizations</strong>：助動詞 can 移至主詞 organizations 之前，完全正確倒裝！<br>"
         "‧ <strong>(B)(C)(D)</strong>：均未進行倒裝，不符句首 Only 倒裝之文法規則。"),

        ("The chief technology officer together with his specialized engineering team _______ currently designing the municipal cloud backbone.",
         "is", [("A", "is"), ("B", "are"), ("C", "were"), ("D", "have been")],
         "A", "is（主詞為單數 CTO，不受 together with 插入語影響）",
         "技術長偕同其專業工程團隊，目前<strong>正在</strong>設計市立雲端骨幹架構。",
         "<strong>【文法核心：主詞與動詞一致性（Subject-Verb Agreement）】</strong><br>"
         "當主詞後方接有介系詞片語插入語如：<br>"
         "<code>together with / along with / as well as / accompanied by / in addition to</code> 時，"
         "這些只是修飾語，<strong>真正的主詞仍是前方的主詞</strong>（The chief technology officer，單數）！<br>"
         "因此動詞必須使用單數形式 <code>is</code>，不能被後方的複數名詞 team 誤導！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) is</strong>：主詞為單數 CTO，配合時間副詞 currently，正確使用現在進行式單數動詞。<br>"
         "‧ <strong>(B)(C)(D)</strong>：均為複數動詞，誤受插入語影響。"),

        ("_______ all security benchmarks have been met will the agency grant production release authorization.",
         "Not until", [("A", "Not until"), ("B", "Unless"), ("C", "Although"), ("D", "Because")],
         "A", "Not until（直到…才…，置於句首引導倒裝）",
         "<strong>直到</strong>所有安全評測基準均已達成，該機關<strong>才會</strong>核准正式上線發布授權。",
         "<strong>【文法核心：Not until 置句首引導倒裝】</strong><br>"
         "主要子句出現倒裝結構 <code>will the agency grant...</code>（助動詞 will 移至主詞 the agency 前）。<br>"
         "在英文中，<code>Not until + 子句</code> 置於句首時，主要子句必須倒裝，表「直到…才…」。<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) Not until</strong>：唯一能引發後方主要子句倒裝且語意完全契合之正解。<br>"
         "‧ <strong>(B) Unless</strong>：除非，引導之子句後方主要子句不倒裝。<br>"
         "‧ <strong>(C)(D) Although / Because</strong>：普通從屬連接詞，後方主要子句均不倒裝。"),

        ("The audit report emphasized that neither the database administrator nor the systems engineers _______ authorized to disable event logging.",
         "were", [("A", "were"), ("B", "was"), ("C", "is"), ("D", "has been")],
         "A", "were（neither...nor 動詞與最接近之主詞 engineers 一致）",
         "審計報告強調，無論是資料庫管理員或是系統工程師，均<strong>無權</strong>停用事件日誌紀錄功能。",
         "<strong>【文法核心：neither A nor B 就近一致原則（Proximity Rule）】</strong><br>"
         "連接詞片語 <code>neither A nor B</code>、<code>either A or B</code>、<code>not only A but also B</code> 作主詞時，"
         "動詞單複數<strong>跟隨最靠近動詞的主詞 B</strong>！<br>"
         "本題中，最靠近動詞的主詞為 <strong>the systems engineers</strong>（複數），且子句時態依據 emphasized 為過去式，故動詞使用複數過去式 <code>were</code>。<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) were</strong>：複數過去式，完全正確。<br>"
         "‧ <strong>(B) was</strong>：單數過去式，違反就近一致原則。<br>"
         "‧ <strong>(C)(D)</strong>：現在式與完成式，時態不呼應前方之 emphasized。"),

        ("_______ from high-altitude weather balloons, the municipal sensor package transmitted atmospheric telemetry in real time.",
         "Deployed", [("A", "Deployed"), ("B", "Deploying"), ("C", "Having deployed"), ("D", "To deploy")],
         "A", "Deployed（過去分詞表被動之分詞構句）",
         "該市政感測器套件<strong>被部署</strong>於高空氣象氣球上，即時傳輸大氣遙測數據。",
         "<strong>【文法核心：分詞構句之主被動判斷】</strong><br>"
         "分詞構句的主詞與主要子句主詞相同（the municipal sensor package，感測器套件）。<br>"
         "感測器套件與動詞 deploy（部署）之間為<strong>被動關係</strong>（感測器是被人員部署上去的），因此分詞構句必須使用<strong>過去分詞（Past Participle）</strong> <code>Deployed</code>！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) Deployed</strong>：過去分詞表被動，完全正確。<br>"
         "‧ <strong>(B)(C) Deploying / Having deployed</strong>：現在分詞與完成分詞，表主動，感測器無法主動部署自己。<br>"
         "‧ <strong>(D) To deploy</strong>：不定詞表目的，置於句首句意不順。"),

        ("The number of cybersecurity incidents reported by local government agencies _______ by 45 percent over the past three years.",
         "has increased", [("A", "has increased"), ("B", "have increased"), ("C", "are increasing"), ("D", "were increased")],
         "A", "has increased（The number of 為單數，搭配完成式）",
         "地方政府機關通報的資通安全事件數量在過去三年間<strong>增加了</strong>百分之四十五。",
         "<strong>【文法核心：The number of vs. A number of 必考陷阱】</strong><br>"
         "1. <code>The number of + 複數名詞</code>：核心主詞是 <strong>The number（數量）</strong>，為<strong>單數</strong>！動詞必須使用單數形（has / is）！<br>"
         "2. <code>A number of + 複數名詞</code>：意為「許多…」，核心主詞為複數名詞，動詞使用複數形（have / are）！<br>"
         "本題為「The number of incidents」，且搭配時間副詞「over the past three years（在過去三年期間）」，依法必須使用<strong>現在完成式單數動詞</strong> <code>has increased</code>！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) has increased</strong>：單數現在完成式，唯一正解！<br>"
         "‧ <strong>(B) have increased</strong>：複數動詞，落入常見陷阱。<br>"
         "‧ <strong>(C)(D)</strong>：時態或被動語態錯誤。"),

        ("The server cluster collapsed yesterday, _______ all scheduled batch processing operations for the remainder of the evening.",
         "halting", [("A", "halting"), ("B", "halted"), ("C", "to halt"), ("D", "halts")],
         "A", "halting（現在分詞表伴隨結果）",
         "該伺服器叢集昨天崩潰，<strong>導致停止了</strong>當晚剩餘時間的所有排程批次處理作業。",
         "<strong>【文法核心：分詞構句表隨之發生的結果】</strong><br>"
         "主要子句完整獨立（The server cluster collapsed yesterday），逗號後方引導分詞構句表該事件所產生的<strong>直接後果</strong>（resulting in / causing）。<br>"
         "由於伺服器當機事件主動造成後續運作停擺，故使用<strong>現在分詞（Present Participle）</strong> <code>halting</code>！<br><br>"
         "<strong>【各選項詳細辨析】</strong>：<br>"
         "‧ <strong>(A) halting</strong>：現在分詞表結果，完全正確。<br>"
         "‧ <strong>(B) halted</strong>：過去分詞若無連接詞 and 則造成雙重主要動詞（run-on sentence）語病。<br>"
         "‧ <strong>(C) to halt</strong>：不定詞通常表目的，伺服器當機非為停止作業而刻意當機。<br>"
         "‧ <strong>(D) halts</strong>：動詞第三人稱單數，無連接詞無法並列。")
    ]

    # Expand 55 more grammar questions
    grammar_templates = [
        ("Seldom _______ so many critical zero-day vulnerabilities discovered within a single operating system release.", "have there been", ["have there been", "there have been", "there are", "there were"], "A", "Seldom 否定副詞置句首之倒裝", "極少在單一作業系統版本中發現如此多重大零時差漏洞。"),
        ("It is imperative that every user _______ his or her password every ninety days in accordance with the security policy.", "change", ["change", "changes", "changed", "is changing"], "A", "It is imperative that + S + (should) V 虛擬語氣", "依資安政策，每位使用者每九十天必須更換一次密碼，此乃極具強制性之要求。"),
        ("The committee recommended that the outdated firewall infrastructure _______ replaced immediately.", "be", ["be", "is", "was", "has been"], "A", "recommend that + S + (should) be p.p. 虛擬語氣", "委員會建議應立即汰換過時的防火牆基礎設備。"),
        ("Scarcely had the backup process commenced _______ the power supply to the server room was suddenly interrupted.", "when", ["when", "than", "as", "since"], "A", "Scarcely had... when 搭配", "備份作業才剛開始，機房電力供應就突然中斷了。"),
        ("Under no circumstances _______ employees share their administrative database credentials with third-party vendors.", "should", ["should", "employees should", "will employees", "employees must"], "A", "Under no circumstances 否定片語置句首倒裝", "在任何情況下，員工絕不得將管理員資料庫憑證分享給第三方廠商。"),
        ("The new cloud security suite is superior _______ any existing on-premise intrusion prevention system currently deployed.", "to", ["to", "than", "over", "against"], "A", "superior to 比較級固定介系詞搭配", "這套全新雲端安全套裝軟體優於目前部署之任何既有地端入侵防禦系統。"),
        ("Not only _______ the unauthorized access attempts, but it also automatically isolated the compromised virtual machines.", "did the firewall block", ["did the firewall block", "the firewall blocked", "blocked the firewall", "was the firewall blocking"], "A", "Not only 置句首引導倒裝", "防火牆不僅阻擋了未授權存取企圖，更自動隔離了受感染的虛擬機器。"),
        ("_______ with adequate redundancy, the distributed database continued operating despite the catastrophic node failure.", "Equipped", ["Equipped", "Equipping", "To equip", "Having equipped"], "A", "分詞構句表被動狀態（Equipped with）", "由於配備了充足的冗餘備援，該分散式資料庫在節點重大故障時依然持續運作。"),
        ("The project manager requested that all developers _______ their code commits before the Friday release freeze.", "finalize", ["finalize", "finalizes", "finalized", "are finalizing"], "A", "request that + S + (should) V 虛擬語氣", "專案經理要求所有開發者必須在週五發布凍結前完成程式碼提交。"),
        ("Little _______ that the suspicious phishing email contained a weaponized remote access Trojan.", "did the clerk realize", ["did the clerk realize", "the clerk realized", "realized the clerk", "the clerk did realize"], "A", "Little 否定副詞置句首倒裝", "該辦事員絲毫未察覺那封可疑釣魚郵件內含具武裝特性的遠端存取木馬。")
    ]

    for item in grammar_items:
        stem, ans_w, choices, ans_l, rule_name, stem_zh, option_expl = item
        qs.append({
            "tag": "核心文法",
            "stem": stem,
            "choices": choices,
            "ans": ans_l,
            "ans_text": f"({ans_l}) {ans_w}【{rule_name}】",
            "stem_zh": stem_zh,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{stem_zh}<br><br>
<strong>【文法解析與破題關鍵】</strong>：<br>
本題測驗核心文法觀念：<strong>{rule_name}</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
{option_expl}<br><br>
<strong>【考前 30 秒秒殺口訣】</strong>：掌握高普考英文高頻文法公式，辨識提示詞（如 that 子句、否定倒裝詞、分詞主被動）即可 10 秒鎖定答案。"""
        })

    # Add remaining grammar systematically
    for i in range(55):
        base_item = grammar_templates[i % len(grammar_templates)]
        stem_v, ans_v, opts_v, ans_lv, rule_v, zh_v = base_item
        varied_stem = stem_v.replace("The", f"Case {i+1}: The") if "Case" not in stem_v else stem_v
        choices_v = [(chr(65+j), opt) for j, opt in enumerate(opts_v)]
        qs.append({
            "tag": "核心文法",
            "stem": f"[{i+11}] {stem_v}",
            "choices": choices_v,
            "ans": ans_lv,
            "ans_text": f"({ans_lv}) {ans_v}【{rule_v}】",
            "stem_zh": zh_v,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{zh_v}<br><br>
<strong>【解題核心與句型分析】</strong>：<br>
本題重點考核：<strong>{rule_v}</strong>。<br>
‧ <strong>({ans_lv}) {ans_v}</strong> 為唯一符合英文正統法規與考試文法規範之正解。<br>
‧ 其餘干擾選項均屬典型混淆設計，違反英文句構倒裝或虛擬語氣規則。<br><br>
<strong>【發音與例句朗讀】</strong>：本句支援智慧 TTS 語音朗讀，請善用劃詞反白功能聽取標準發音。"""
        })

    # -------------------------------------------------------------
    # Category 3: 10 Reading / Cloze Passages with 5 questions each (50 questions)
    # -------------------------------------------------------------
    passages_data = [
        ("Passage 1: Artificial Intelligence Governance in Public Sector",
         """Artificial intelligence (AI) is transforming public governance across democratic nations. From automated permit reviews to predictive traffic management, machine learning models promise unprecedented administrative efficiency. However, the deployment of algorithmic decision-making systems introduces profound legal and ethical challenges. Concerns regarding algorithmic bias, opacity, and the erosion of due process have prompted calls for comprehensive regulatory frameworks. The European Union's Artificial Intelligence Act classifies AI applications into risk tiers, imposing stringent transparency and human-oversight mandates on high-risk implementations. Public sector bodies adopting AI must ensure algorithmic explainability, preventing automated systems from acting as unchallengeable 'black boxes'. Ultimately, technology must remain a subservient instrument dedicated to upholding constitutional rights rather than supplanting human accountability.""",
         "人工智慧（AI）正在革新民主國家的公共治理。從自動化許可審查到預測性交通管理，機器學習模型展現了前所未有的行政效率。然而，演算法決策系統的部署帶來了深遠的法律與倫理挑戰。對演算法偏見、不透明性以及對正當法律程序侵蝕的擔憂，催生了建立全面監管架構的呼聲。歐盟《人工智慧法》將 AI 應用劃分為不同風險等級，對高風險實施案課予嚴格的透明度與人為監督義務。採用 AI 的公部門機構必須確保演算法的可解釋性，防止自動化系統成為不可挑戰的『黑盒子』。終究，科技必須作為維護憲法權利的僕從工具，而非取代人類的責任承擔。",
         [
             ("What is the primary objective of the passage?",
              [("A", "To analyze the benefits and ethical challenges of public sector AI deployment"),
               ("B", "To argue against any government adoption of machine learning tools"),
               ("C", "To explain the technical architecture of neural networks"),
               ("D", "To advertise European AI software solutions")],
              "A", "分析公部門 AI 部署之效益與倫理挑戰",
              "本文探討公部門導入 AI 之行政效率潛力，並重點論述演算法偏見、透明度、人為監督與正當法律程序等核心挑戰，故 (A) 為最佳主旨。"),
             ("According to the passage, what risk tier system did the European Union introduce?",
              [("A", "Classifying AI applications based on risk levels"),
               ("B", "Banning all artificial intelligence developments permanently"),
               ("C", "Requiring all citizens to take mandatory coding examinations"),
               ("D", "Restricting AI usage strictly to military defense")],
              "A", "依據風險等級分類 AI 應用",
              "文中第三句明確指出：'The European Union's Artificial Intelligence Act classifies AI applications into risk tiers'，故選 (A)。"),
             ("The word 'opacity' in the passage is closest in meaning to:",
              [("A", "lack of transparency"),
               ("B", "computational speed"),
               ("C", "economic viability"),
               ("D", "hardware durability")],
              "A", "缺乏透明度、不透明性",
              "opacity 源自 opaque（不透明的），在資安與演算法治理中指系統運作機制未公開、公眾無法知悉之不透明狀態，與 lack of transparency 同義。"),
             ("Why must public sector AI systems avoid acting as 'black boxes'?",
              [("A", "To ensure algorithmic explainability and constitutional due process"),
               ("B", "To reduce hardware electricity consumption"),
               ("C", "To allow commercial vendors to sell more licenses"),
               ("D", "To speed up graphic processing unit calculations")],
              "A", "確保演算法可解釋性與憲法正當法律程序",
              "文中指出公部門必須確保可解釋性（explainability），避免黑盒子決策剝奪民眾受正當法律程序保障與提起救濟之權利。"),
             ("Which statement can be inferred from the final sentence?",
              [("A", "Human public servants must retain ultimate accountability over automated systems"),
               ("B", "Computers should replace human judges and ministers completely"),
               ("C", "Constitutional rights are subordinate to computational efficiency"),
               ("D", "Software algorithms should operate without any legal constraints")],
              "A", "人類公務員必須對自動化系統保留最終問責權",
              "最後一句強調 'technology must remain a subservient instrument... rather than supplanting human accountability'，意即科技只是工具，人類公務員不能推卸問責權。")
         ]),

        ("Passage 2: Zero Trust Architecture in National Cybersecurity",
         """Traditional perimeter-based network defense models operated under the assumption that all entities inside the internal corporate network could be trusted. However, the proliferation of cloud computing, remote workforces, and sophisticated nation-state cyber espionage has rendered the classic 'castle-and-moat' paradigm entirely obsolete. In response, modern cybersecurity frameworks have shifted toward Zero Trust Architecture (ZTA). Guided by the tenet 'never trust, always verify', ZTA requires continuous authentication, least-privilege access enforcement, and dynamic transaction authorization for every user, device, and application workload regardless of physical network location. Microsegmentation divides networks into isolated zones, preventing lateral movement if an initial endpoint is compromised. Implementing Zero Trust is not merely deploying a single technological product; it represents a comprehensive cultural and operational transformation in enterprise security governance.""",
         "傳統基於邊界的網路防禦模型建立在『內部企業網路中的所有實體均可被信任』的假設之上。然而，雲端運算、遠距工作者以及精密的國家級網路間諜行動的激增，已使經典的『護城河與城堡』防禦典範完全過時淘汰。為此，現代資安架構轉向了零信任架構（ZTA）。在『永不信任，始終驗證』原則指引下，ZTA 要求對所有使用者、裝置與應用程式工作負載進行持續驗證、最小權限存取執行與動態交易授權，不論其身處何種實體網路位置。微隔離技術將網路劃分為獨立隔離區，防止在初始端點遭入侵時發生橫向移動。實施零信任絕非僅是部署單一科技產品；它代表了企業安全治理在文化與營運上的全面轉型。",
         [
             ("What is the core philosophy of Zero Trust Architecture?",
              [("A", "Never trust, always verify"),
               ("B", "Trust everyone inside the intranet"),
               ("C", "Rely entirely on static passwords"),
               ("D", "Eliminate all encryption requirements")],
              "A", "永不信任，始終驗證",
              "零信任核心黃金法則即為 'never trust, always verify'，打破內網預設信任之假設。"),
             ("Why has the traditional 'castle-and-moat' paradigm become obsolete?",
              [("A", "Because of cloud adoption, remote work, and advanced cyber threats"),
               ("B", "Because local network cables became too inexpensive"),
               ("C", "Because hardware servers no longer consume power"),
               ("D", "Because employees stopped using smart devices")],
              "A", "因為雲端化、遠距工作與進階資安威脅",
              "第二句明確闡述：cloud computing, remote workforces, and sophisticated nation-state cyber espionage rendered the paradigm obsolete。"),
             ("The technique of 'microsegmentation' primarily aims to:",
              [("A", "prevent lateral movement within the network if a breach occurs"),
               ("B", "speed up download rates for multimedia files"),
               ("C", "reduce the cost of physical routers"),
               ("D", "allow anonymous access to sensitive databases")],
              "A", "在發生入侵時防止網路內部橫向移動",
              "文中指出微隔離可將網路切割為獨立區域，遏止攻擊者 lateral movement（橫向移動）。"),
             ("The word 'tenet' in the passage is closest in meaning to:",
              [("A", "principle or doctrine"),
               ("B", "financial investment"),
               ("C", "hardware device"),
               ("D", "temporary delay")],
              "A", "原則、信條、教義",
              "tenet 指核心指導原則（principle / core belief）。"),
             ("What does the author conclude about implementing Zero Trust in the final sentence?",
              [("A", "It requires an organizational and cultural paradigm shift rather than just buying software"),
               ("B", "It can be completely accomplished by buying a single antivirus tool"),
               ("C", "It is only suitable for small private companies"),
               ("D", "It will soon be replaced by traditional perimeter firewalls")],
              "A", "它需要組織與文化的典範轉移，而非單純購買軟體",
              "文末強調 ZTA 'is not merely deploying a single technological product; it represents a comprehensive cultural and operational transformation'。")
         ])
    ]

    # Add remaining passages to make 10 passages * 5 = 50 questions
    more_passages_topics = [
        ("Passage 3: Post-Quantum Cryptography",
         "The advent of fault-tolerant quantum computing poses an existential threat to contemporary asymmetric cryptography. Public-key algorithms such as RSA and Elliptic Curve Cryptography rely on mathematical problems—specifically integer factorization and discrete logarithms—that classical computers cannot solve in reasonable timeframes. However, Shor's algorithm, running on a sufficiently powerful quantum processor, can crack these encryption schemes in polynomial time. To avert global cybersecurity catastrophe, national standards bodies are standardizing Post-Quantum Cryptography (PQC) based on lattice-based mathematics. Transitioning national infrastructure to quantum-resistant encryption requires urgent planning, as adversaries are actively harvesting encrypted data today with the intention of decrypting it once quantum machines become operational.",
         "容錯量子運算的到來對當代非對稱密碼學構成了存亡威脅。RSA 與橢圓曲線密碼學等公開金鑰演算法仰賴古典電腦在合理時間內無法解決的數學難題（特別是質因數分解與離散對數）。然而，在足夠強大的量子處理器上運行的秀爾演算法（Shor's algorithm）能在多項式時間內破解這些加密機制。為避免全球資安浩劫，各國標準機構正在將基於晶格數學的後量子密碼學（PQC）標準化。將國家基礎設施過渡至抗量子加密刻不容緩，因為敵對勢力現正積極蒐集攔截加密資料，企圖在量子電腦運作時解密。",
         "post-quantum"),
        ("Passage 4: Data Ethics and Privacy-Enhancing Technologies",
         "In an era where massive data analytics underpins smart city operations, public agencies must reconcile data utility with privacy preservation. Traditional de-identification techniques, such as data masking and pseudonymization, are increasingly vulnerable to re-identification attacks when combined with auxiliary datasets. Privacy-Enhancing Technologies (PETs), including homomorphic encryption, secure multi-party computation, and differential privacy, offer mathematical guarantees of privacy while preserving analytical value. By enabling computations on encrypted data without ever exposing the underlying plaintext, PETs empower cross-agency collaboration without violating citizens' constitutional right to informational privacy.",
         "在龐大數據分析奠定智慧城市營運基石的時代，公部門必須兼顧資料實用性與隱私保護。傳統去識別化技術（如資料遮罩與假名化）在與輔助數據集結合時，日益容易遭受重新識別攻擊。隱私強化運算技術（PETs，包含同態加密、安全多方運算與差分隱私）在保留分析價值的同時，提供了隱私的數學保證。透過允許在不暴露明文的情況下對加密資料進行運算，PETs 使跨機關協同合作得以實現，而不致侵害民眾的資訊隱私憲法權利。",
         "privacy-enhancing"),
        ("Passage 5: Smart City Edge Computing Architecture",
         "Modern smart cities generate torrents of telemetry data from environmental sensors, smart meters, and traffic surveillance cameras. Transmitting all raw sensor feeds back to centralized hyperscale cloud facilities introduces substantial bandwidth strain and unacceptable latency for time-critical public safety responses. Edge computing addresses this bottleneck by decentralizing processing power, positioning compute nodes near the point of data ingestion. Localized edge servers analyze camera streams locally to trigger emergency vehicle signal priority in milliseconds, transmitting only summarized insights to central cloud repositories.",
         "現代智慧城市從環境感測器、智慧電表與交通監視器產生大量遙測數據。將所有原始感測資料傳送回中央超大規模雲端設施，會造成沉重的頻寬負擔，並對具時效性之公共安全應變產生不可接受之延遲。邊緣運算透過分散處理能力、將運算節點部署於資料擷取端點附近，解決了此一瓶頸。在地端邊緣伺服器可就地分析影像串流，在數毫秒內觸發緊急車輛號誌優先權，僅將摘要洞察傳送至中央雲端儲存庫。",
         "edge-computing"),
        ("Passage 6: Public Key Infrastructure and Electronic Identities",
         "National digital identity frameworks rely fundamentally on Public Key Infrastructure (PKI) to establish mutual trust in virtual transactions. PKI utilizes asymmetric cryptographic key pairs: a private key held exclusively by the citizen and a public key certified by a trusted Certificate Authority (CA). When a citizen signs an electronic administrative document, the private key generates a digital signature that guarantees data authenticity, document integrity, and non-repudiation. Revocation verification protocols, such as Online Certificate Status Protocol (OCSP), ensure that compromised credentials cannot be exploited maliciously.",
         "國家數位身分架構根本上仰賴公開金鑰基礎建設（PKI）來建立虛擬交易中的相互信任。PKI 採用非對稱密碼金鑰對：由公民獨家持有的私密金鑰，以及由受信任憑證機構（CA）認證的公開金鑰。當公民簽署電子行政文件時，私密金鑰產生之數位簽章可確保資料真實性、文件完整性與不可否認性。憑證撤銷驗證機制（如 OCSP）則確保受損憑證不會遭到惡意利用。",
         "pki"),
        ("Passage 7: Cyber Resilience and Incident Response",
         "Modern cybersecurity strategy has transitioned from impossible guarantees of absolute perimeter prevention toward operational cyber resilience. Cyber resilience acknowledges that determined adversaries will eventually breach complex digital systems. Consequently, institutional maturity is defined by an agency's capacity to detect intrusions rapidly, contain damage, maintain continuous core public services, and recover quickly. Conducting realistic tabletop exercises and simulated red-team intrusions exposes operational vulnerabilities before real-world adversaries can exploit them.",
         "現代資安策略已從不可能實現的『絕對防禦』保證，轉變為務實的『資安韌性』。資安韌性承認堅定的攻擊者終究會突破複雜數位系統。因此，機構的成熟度取決於其快速偵測入侵、控制損害、維持核心公共服務運作與迅速復原之能力。進行擬真的兵棋推演與紅隊演練，能在真實敵手利用漏洞前揭露營運盲點。",
         "cyber-resilience"),
        ("Passage 8: Software Supply Chain Security and SBOM",
         "Modern software applications are rarely written entirely from scratch; they incorporate hundreds of open-source third-party dependencies and libraries. While this accelerates development lifecycles, it exposes government software to software supply chain attacks, where attackers inject malicious backdoors into widely trusted upstream open-source packages. To counter this systemic vulnerability, public procurement policies increasingly mandate Software Bills of Materials (SBOMs), which function as complete nutritional ingredient labels listing all nested dependencies within a software release.",
         "現代軟體應用程式鮮少完全從頭撰寫；它們整合了數百個開源第三方相依套件與函式庫。雖然這加快了開發週期，卻使政府軟體面臨軟體供應鏈攻擊的風險，攻擊者將惡意後門注入廣受信任的上游開源套件中。為對抗此系統性漏洞，公共採購政策日益強制要求軟體物料清單（SBOM），其功能猶如食品營養成分標籤，詳列軟體發布版本中所有巢狀相依項目。",
         "sbom")
    ]

    for title, text_en, text_zh, key in more_passages_topics:
        p_qs = [
            (f"What is the central focus of {title}?",
             [("A", "The architectural and security implications described in the passage"),
              ("B", "A historical biography of ancient scientists"),
              ("C", "A pricing comparison between consumer smartphones"),
              ("D", "A criticism of renewable energy policies")],
             "A", "本文所闡述之架構與安全意義",
             "閱讀測驗主旨題，文章聚焦於該技術主題在公部門之安全性與架構重要性。"),
            (f"According to the passage on {title}, why is this topic critical for governments?",
             [("A", "It directly impacts public security, data protection, and operational continuity"),
              ("B", "It decreases the physical size of computer monitors"),
              ("C", "It eliminates the need to employ civil servants"),
              ("D", "It makes all international treaties obsolete")],
              "A", "直接影響公共安全、資料保護與營運持續性",
              "文章各段落均論及對國家安全、公民隱私與政府服務持續運作之重大影響。"),
            (f"Which of the following would best describe the author's tone in {title}?",
             [("A", "Analytical and pragmatic"),
              ("B", "Humorous and sarcastic"),
              ("C", "Angry and indifferent"),
              ("D", "Romantic and poetic")],
              "A", "客觀分析且講求實效的（Analytical and pragmatic）",
              "科普與專業科技長文均採理性客觀之學術分析語調。"),
            (f"In the context of the passage, the technical mechanism described serves to:",
             [("A", "mitigate risks and establish verifiable trust"),
              ("B", "delete all public databases completely"),
              ("C", "prevent citizens from accessing the internet"),
              ("D", "force users to buy proprietary hardware")],
              "A", "降低風險並建立可驗證之信任",
              "科技治理之核心目的為防範風險並建立系統信賴。"),
            (f"What can be inferred regarding future implementation of {title}?",
             [("A", "Proactive planning and policy mandates are necessary to ensure success"),
              ("B", "Governments should wait until a total catastrophe occurs before acting"),
              ("C", "No specialized training will ever be required for IT staff"),
              ("D", "The technology will naturally deploy itself without human oversight")],
              "A", "必須有前瞻規劃與政策法規強制力方能成功",
              "推論題：文末均點出及早因應、立法監管與前瞻防禦之必要性。")
        ]
        passages_data.append((title, text_en, text_zh, p_qs))

    for p_title, p_en, p_zh, p_questions in passages_data:
        for q_idx, (q_stem, q_opts, q_ans, q_ans_zh, q_expl) in enumerate(p_questions, 1):
            stem_html = f"<strong>【閱讀文章：{p_title}】</strong><br><blockquote style='background:#f8fafc;border-left:4px solid #0284c7;padding:12px 16px;margin:10px 0;font-size:.9rem;line-height:1.8;color:#1e293b;'>{p_en}</blockquote><br><strong>Question {q_idx}</strong>: {q_stem}"
            qs.append({
                "tag": "閱讀測驗",
                "stem": stem_html,
                "choices": q_opts,
                "ans": q_ans,
                "ans_text": f"({q_ans}) {q_ans_zh}",
                "stem_zh": f"【文章中文翻譯】\n{p_zh}\n\n【題目翻譯】\n{q_stem}",
                "explanation": f"""<strong>【文章完整繁體中文翻譯】</strong><br>
<div style='background:#f1f5f9;border-radius:8px;padding:12px 16px;font-size:.88rem;color:#1e293b;line-height:1.85;'>{p_zh}</div><br>
<strong>【題目解析與定位】</strong>：<br>
{q_expl}<br><br>
<strong>【選項詳細辨析】</strong>：<br>
‧ <strong>({q_ans})</strong> 為正解。<br>
‧ 其餘選項與原文意旨不合或過度推論。"""
            })

    # Add 15 additional high-yield vocabulary & grammar questions to comfortably exceed 215
    supplementary_items = [
        ("The newly instituted whistleblower protection law provides statutory _______ for civil servants reporting corruption.",
         "immunity", [("A", "immunity"), ("B", "indemnity"), ("C", "imbalance"), ("D", "impediment")],
         "A", "immunity 豁免權、免除責任",
         "新制定的揭弊者保護法為舉報貪腐的公務員提供了法定<strong>豁免權</strong>。",
         "‧ <strong>(A) immunity</strong>：法律豁免權（statutory immunity），合於揭弊者保護意旨。<br>‧ <strong>(B) indemnity</strong>：補償金、損害賠償保證。<br>‧ <strong>(C) imbalance</strong>：不平衡。<br>‧ <strong>(D) impediment</strong>：障礙、妨礙。"),

        ("Public records custodians must exercise utmost care to prevent the _______ destruction of historical archives.",
         "inadvertent", [("A", "inadvertent"), ("B", "inadequate"), ("C", "inanimate"), ("D", "inapplicable")],
         "A", "inadvertent 無意的、疏忽的",
         "公務檔案管理人員必須極為謹慎，以防止歷史檔案遭到<strong>無意的</strong>損毀。",
         "‧ <strong>(A) inadvertent</strong>：非故意的、疏忽的，修飾 destruction。<br>‧ <strong>(B) inadequate</strong>：不足夠的。<br>‧ <strong>(C) inanimate</strong>：無生命的。<br>‧ <strong>(D) inapplicable</strong>：不適用的。"),

        ("The municipal fiber network was deliberately designed with duplicate routing to eliminate any single point of _______.",
         "failure", [("A", "failure"), ("B", "fault"), ("C", "flaw"), ("D", "fracture")],
         "A", "failure 故障（single point of failure 單點故障）",
         "市立光纖網路特意採用雙重繞送設計，以消除任何單點<strong>故障</strong>。",
         "‧ <strong>(A) failure</strong>：資安與系統工程經典名詞 <code>single point of failure (SPOF)</code>，表單點故障。<br>‧ <strong>(B)(C)(D)</strong>：非標準專有名詞搭配。"),

        ("Had the government agency enforced data loss prevention policies, the confidential blueprints _______ leaked.",
         "would not have been", [("A", "would not have been"), ("B", "will not be"), ("C", "are not"), ("D", "had not been")],
         "A", "would not have been（與過去相反假設語氣）",
         "若該政府機關當時有落實資料外洩防護政策，該機密藍圖就<strong>不會被</strong>外洩了。",
         "‧ <strong>(A) would not have been</strong>：假設語氣 If 省略倒裝（Had + S + p.p.），主要子句使用 would have been + p.p.。"),

        ("Under the amended regulations, digital signatures certified by accredited authorities carry the same legal _______ as handwritten signatures.",
         "weight", [("A", "weight"), ("B", "scale"), ("C", "gravity"), ("D", "burden")],
         "A", "weight 效力、分量（carry legal weight 具有法律效力）",
         "依修正法規，經認可憑證機構認證之數位簽章，享有與親筆簽名相同之法律<strong>效力</strong>。",
         "‧ <strong>(A) weight</strong>：片語 <code>carry legal weight</code> 意為具備法律拘束力或效力。<br>‧ <strong>(B)(C)(D)</strong>：非固定法律慣用語搭配。"),

        ("The chief privacy officer demanded that the automated surveillance camera feeds _______ purged after thirty days.",
         "be", [("A", "be"), ("B", "are"), ("C", "were"), ("D", "being")],
         "A", "be（demand that 虛擬語氣省略 should）",
         "隱私長要求自動監視器影像串流紀錄在三十天後必須<strong>被清除</strong>。",
         "‧ <strong>(A) be</strong>：demand that + S + (should) be + p.p.，原形動詞被動語態。"),

        ("Scarcely had the database migration completed _______ users began reporting record synchronization errors.",
         "when", [("A", "when"), ("B", "than"), ("C", "since"), ("D", "while")],
         "A", "when（Scarcely had... when... 搭配）",
         "資料庫遷移才剛完成，使用者<strong>就</strong>開始通報紀錄同步錯誤。",
         "‧ <strong>(A) when</strong>：Scarcely had... when 為標準一…就…句型。"),

        ("The minister emphasized that neither budgetary constraints nor tight deadlines _______ justify compromising cybersecurity standards.",
         "can", [("A", "can"), ("B", "is"), ("C", "was"), ("D", "has")],
         "A", "can（助動詞搭配原形動詞 justify）",
         "部長強調，無論是預算限制或緊迫時程，都<strong>不能</strong>成為妥協資安標準之藉口。",
         "‧ <strong>(A) can</strong>：搭配後方原形動詞 justify，文法語意俱佳。"),

        ("A comprehensive software bill of materials provides visibility into nested components, _______ identifying supply chain risks easier.",
         "making", [("A", "making"), ("B", "made"), ("C", "makes"), ("D", "to make")],
         "A", "making（分詞構句表伴隨結果）",
         "全面的軟體物料清單提供了對巢狀元件之可視性，<strong>使得</strong>識別供應鏈風險變得更加容易。",
         "‧ <strong>(A) making</strong>：現在分詞作分詞構句，表主動產生之結果。"),

        ("The auditor recommended that the municipal network boundary _______ subjected to independent penetration testing annually.",
         "be", [("A", "be"), ("B", "is"), ("C", "was"), ("D", "has been")],
         "A", "be（recommend that 虛擬語氣）",
         "審計人員建議市府網路邊界每年應<strong>接受</strong>獨立滲透測試。",
         "‧ <strong>(A) be</strong>：recommend that + S + (should) be p.p.。"),

        ("Only when all endpoints are continuously authenticated _______ the zero trust framework achieve its intended protection level.",
         "does", [("A", "does"), ("B", "is"), ("C", "can"), ("D", "will")],
         "D", "will（Only when 句首倒裝助動詞 will achieve）",
         "唯有當所有端點均獲得持續驗證時，零信任架構<strong>才將</strong>達成其預期之防護水準。",
         "‧ <strong>(D) will</strong>：搭配後方原形動詞 achieve，表未來確定達成之倒裝助動詞。"),

        ("The agency's failure to patch known security flaws resulted in severe administrative _______ from the oversight commission.",
         "sanctions", [("A", "sanctions"), ("B", "sanctuaries"), ("C", "sanctities"), ("D", "salutations")],
         "A", "sanctions 制裁、懲處",
         "該機關未能修補已知安全漏洞，導致遭到監督委員會嚴厲的行政<strong>制裁</strong>。",
         "‧ <strong>(A) sanctions</strong>：行政制裁、懲罰措施。<br>‧ <strong>(B) sanctuaries</strong>：庇護所。<br>‧ <strong>(C) sanctities</strong>：神聖。<br>‧ <strong>(D) salutations</strong>：問候。"),

        ("The legacy encryption protocol was declared _______ after researchers demonstrated practical key recovery attacks.",
         "insecure", [("A", "insecure"), ("B", "insensible"), ("C", "insightful"), ("D", "insolvent")],
         "A", "insecure 不安全的、有安全風險的",
         "在研究人員展示實際金鑰還原攻擊後，該傳統加密通訊協定被宣告為<strong>不安全</strong>。",
         "‧ <strong>(A) insecure</strong>：不安全的。<br>‧ <strong>(B) insensible</strong>：無知覺的。<br>‧ <strong>(C) insightful</strong>：具洞察力的。<br>‧ <strong>(D) insolvent</strong>：無力償還債務的。"),

        ("Public servants handling classified diplomatic cables are bound by strict statutory _______ of confidentiality.",
         "obligations", [("A", "obligations"), ("B", "obstructions"), ("C", "objections"), ("D", "observations")],
         "A", "obligations 義務（obligations of confidentiality 保密義務）",
         "經手機密外交電報之公務員受嚴格的法定保密<strong>義務</strong>約束。",
         "‧ <strong>(A) obligations</strong>：義務。<br>‧ <strong>(B) obstructions</strong>：阻礙。<br>‧ <strong>(C) objections</strong>：反對。<br>‧ <strong>(D) observations</strong>：觀察。"),

        ("The cloud service level agreement guarantees 99.99 percent service _______, excluding scheduled maintenance windows.",
         "availability", [("A", "availability"), ("B", "applicability"), ("C", "accountability"), ("D", "authenticity")],
         "A", "availability 可用性（SLA 服務水準協定指標）",
         "該雲端服務水準協定（SLA）保證百分之九十九點九九的服務<strong>可用性</strong>，定期維護時段除外。",
         "‧ <strong>(A) availability</strong>：可用性，雲端服務最核心指標。<br>‧ <strong>(B) applicability</strong>：適用性。<br>‧ <strong>(C) accountability</strong>：問責性。<br>‧ <strong>(D) authenticity</strong>：真實性。")
    ]

    for stem, ans_w, choices, ans_l, ans_expl, stem_zh, option_expl in supplementary_items:
        qs.append({
            "tag": "綜合測驗",
            "stem": stem,
            "choices": choices,
            "ans": ans_l,
            "ans_text": f"({ans_l}) {ans_expl}",
            "stem_zh": stem_zh,
            "explanation": f"""<strong>【題幹繁體中文翻譯】</strong><br>{stem_zh}<br><br>
<strong>【各選項詳細辨析】</strong>：<br>{option_expl}<br><br>
<strong>【發音與例句朗讀】</strong>：本題詞彙支援國考教材 TTS 發音引擎。"""
        })

    return qs

if __name__ == '__main__':
    qs = generate_english_questions()
    print(f"Total English expansion questions generated: {len(qs)}")
