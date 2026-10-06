# -*- coding: utf-8 -*-
"""
32 Brand New, High-Quality Questions for 05-common/law-bank.html
Covers:
1. 113年電子簽章法翻修 (Electronic Signatures Act)
2. 個人資料保護法與獨立監督機關 (Personal Data Protection / DPA)
3. 資通安全法責任等級與關鍵基礎設施 (Cyber Security Act / CI)
4. 刑法妨害電腦使用罪與加重處罰 (Cybercrime / Penal Code)
5. 智慧財產權與 AI 生成物 (Copyright / Trade Secrets / Intellectual Property)
6. 政府採購法資訊採購與最有利標 (Government Procurement Act)
7. 憲法法庭裁判與人權審查標準 (Constitutional Court Judgments / Strict Scrutiny)
8. 行政程序法之正當法律程序 (Due Process of Law / Administrative Procedure)
9. 民法繼承應繼分與特留分推導計算 (Civil Code Inheritance Calculation)
10. 行政罰數行為併罰與裁處時效推導 (Administrative Penalty Calculation)
"""

NEW_LAW_QUESTIONS = [
    {
        "ans": "B",
        "tag": "電子簽章法",
        "stem": "民國 113 年大幅修正公布之《電子簽章法》（Electronic Signatures Act），下列關於其修法核心重點之敘述，何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "明定「電子簽章」與「數位簽章」為包含關係，數位簽章為電子簽章之一種"),
            ("B", "明定行政機關得以行政命令實質排除特定業務適用電子簽章，無須檢討落日條款"),
            ("C", "明定具備一定憑證機構簽發之數位簽章，依法享有「推定為本人親自簽署」之法律效力"),
            ("D", "促進電子簽章之國際對等互認，放寬外國憑證機構之許可條件並導入技術中立原則")
        ],
        "ans_text": "(B) 明定行政機關得以行政命令實質排除特定業務適用電子簽章，無須檢討落日條款",
        "explanation": """<strong>【核心法理與新法變更】</strong><br>
民國 113 年修正之《電子簽章法》徹底落實「以電子為原則、紙本為例外」：<br>
(1) <strong>刪除或限制行政排除條款</strong>：過去行政機關常以公告排除電子簽章適用，修法後明定過往公告排除之適用條款設定<strong>落日條款</strong>，要求行政機關限期檢討落日，全面推動數位轉型。<br>
(2) <strong>推定本人簽署</strong>：合於特定憑證之「數位簽章（Digital Signature）」，法律直接賦予<strong>推定為本人親自簽署</strong>之法律效果。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：依新法第 2 條，電子簽章為上位概念，數位簽章（經非對稱型密碼學演算法及憑證）為其子集。<br>
‧ <strong>(B) 錯誤（本題正解）</strong>：行政機關不得再任意以行政命令長期排除，且修法後已明定既有排除公告原則上一律定期落日。<br>
‧ <strong>(C) 正確</strong>：第 5 條修正案明定符合規定之數位簽章推定為本人簽署，大幅降低民刑事舉證負擔。<br>
‧ <strong>(D) 正確</strong>：增訂促進跨國互認機制，兼顧技術中立（Technology Neutrality）原則。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Electronic Signature</code> <span class="en">Electronic Signature</span>：電子簽章（廣義，指依附於電子文件之符號或資料）。<br>
‧ <code>Digital Signature</code> <span class="en">Digital Signature</span>：數位簽章（狹義，指透過公開金鑰基礎建設 PKI 簽署）。"""
    },
    {
        "ans": "C",
        "tag": "個人資料保護法",
        "stem": "因應憲法法庭判決意旨與國際標準（如歐盟 GDPR），《個人資料保護法》（Personal Data Protection Act）近年修法之最關鍵組織變革為何？",
        "choices": [
            ("A", "將所有個資主管權責移交法務部調查局統籌管轄"),
            ("B", "改由國家安全會議直接設立個資防護專責處室"),
            ("C", "設置獨立專責機關「個人資料保護委員會」（Personal Data Protection Commission）"),
            ("D", "全面廢除行政檢查權，改採司法警察機關令狀聲請制")
        ],
        "ans_text": "(C) 設置獨立專責機關「個人資料保護委員會」（Personal Data Protection Commission）",
        "explanation": """<strong>【核心法理與憲法裁判】</strong><br>
憲法法庭 111 年憲判字第 13 號判決宣告健保資料庫二次利用等案，明確揭櫫憲法保障<strong>資訊隱私權（Right to Informational Privacy）</strong>之意旨，並要求國家應設置<strong>獨立之個人資料保護監督機制</strong>。<br>
政府據此推動個資法修法，成立「個人資料保護委員會籌備處」，未來將正式成立獨立二級機關<strong>個人資料保護委員會（PDPC）</strong>，打破過往由各目的事業主管機關分散管轄之弊病。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：法務部過去為法律解釋機關，並非專責獨立監管機關；調查局為偵查機關，不符合國際獨立監督要求。<br>
‧ <strong>(B) 錯誤</strong>：國安會為國防外交國安諮詢機關，並非主管一般民眾個資保護之獨立監管機關。<br>
‧ <strong>(C) 正確</strong>：比照歐盟 GDPR 獨立監管機構（DPA）模式，成立獨立行政機關「個人資料保護委員會」。<br>
‧ <strong>(D) 錯誤</strong>：主管機關依然享有實體行政檢查權與行政罰裁處權，且大幅提高罰鍰上限至新臺幣 1,500 萬元。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>GDPR (General Data Protection Regulation)</code> <span class="en">General Data Protection Regulation</span>：歐盟通用資料保護規則。<br>
‧ <code>Independent Supervisory Authority</code> <span class="en">Independent Supervisory Authority</span>：獨立監督機關。"""
    },
    {
        "ans": "A",
        "tag": "資通安全法",
        "stem": "依《資通安全管理法》（Cyber Security Management Act）及相關子法，下列關於公務機關與特定非公務機關資通安全防護責任之敘述，何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "公務機關若發生第四級（最嚴重）資通安全事件，應於知悉後 72 小時內完成通報"),
            ("B", "特定非公務機關包括關鍵基礎設施提供者、公營事業及政府捐助之財團法人"),
            ("C", "公務機關之資通安全責任等級由高至低劃分為 A 級、B 級、C 級、D 級與 E 級"),
            ("D", "A 級與 B 級公務機關均應配置資通安全專職人員，並定期辦理資通安全演練")
        ],
        "ans_text": "(A) 公務機關若發生第四級（最嚴重）資通安全事件，應於知悉後 72 小時內完成通報",
        "explanation": """<strong>【核心法理與通報時效】</strong><br>
依《資通安全事件通報及應變辦法》第 4 條與第 6 條規定：<br>
(1) <strong>通報時效</strong>：各級公務機關與特定非公務機關知悉資通安全事件後，<strong>均應於 1 小時內完成通報</strong>，絕非 72 小時！（72 小時通常為歐盟 GDPR 之個資外洩向主管機關通報期限，國考常故意混淆）。<br>
(2) <strong>損害控制與復原時效</strong>：第三級或第四級事件，應於知悉後 36 小時內完成損害控制或復原。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤（本題正解）</strong>：資安法規定通報時限為「知悉後 1 小時內」，72 小時是嚴重法規混淆。<br>
‧ <strong>(B) 正確</strong>：資通安全法第 2 條明定特定非公務機關之三種法定範疇。<br>
‧ <strong>(C) 正確</strong>：依資通安全責任等級分級辦法，公務機關分為 A、B、C、D、E 五個等級。<br>
‧ <strong>(D) 正確</strong>：A、B 級機關肩負關鍵核心系統維運，法定必須設置資安專職人員與專責單位。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Critical Infrastructure (CI)</code> <span class="en">Critical Infrastructure</span>：關鍵基礎設施。<br>
‧ <code>Information Security Incident</code> <span class="en">Information Security Incident</span>：資通安全事件。"""
    },
    {
        "ans": "D",
        "tag": "刑法",
        "stem": "甲為獲取不法利益，利用分散式阻斷服務攻擊（DDoS）癱瘓某公立醫院之醫療掛號與急診派工伺服器，導致病患急救調度受阻。甲之行為觸犯何種刑法罪名？",
        "choices": [
            ("A", "僅構成刑法第 358 條無故入侵電腦罪"),
            ("B", "僅構成刑法第 359 條無故取得刪除變更電磁紀錄罪"),
            ("C", "僅構成刑法第 360 條無故干擾電腦罪，無其他加重事由"),
            ("D", "構成刑法第 362 條之 1 針對公務機關或醫療關鍵基礎設施之「加重妨害電腦使用罪」")
        ],
        "ans_text": "(D) 構成刑法第 362 條之 1 針對公務機關或醫療關鍵基礎設施之「加重妨害電腦使用罪」",
        "explanation": """<strong>【核心法條與修法重點】</strong><br>
近年為強化關鍵基礎設施防護，立法院修正《刑法》第 362 條之 1（加重妨害電腦使用罪）：<br>
犯刑法第 358 條至第 360 條之罪，而有下列情形之一者，加重其刑至二分之一：<br>
一、針對<strong>公務機關之電腦或其相關設備</strong>犯之者。<br>
二、針對<strong>關鍵基礎設施（如醫療、能源、金融、交通等）之電腦或相關設備</strong>犯之者。<br>
DDoS 攻擊大量傳送封包阻塞網路，原本觸犯刑法第 360 條「無故干擾電腦罪」；但因攻擊對象為公立醫院之急診與醫療系統（關鍵基礎設施），依法應成立<strong>加重妨害電腦使用罪</strong>，處 1 年以上 7 年以下有期徒刑。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：DDoS 主要是干擾運作（第 360 條），不以破解帳密或入侵植入為要件。<br>
‧ <strong>(B) 錯誤</strong>：甲未取得或刪除電磁紀錄，非第 359 條之客觀要件。<br>
‧ <strong>(C) 錯誤</strong>：疏漏了新法針對關鍵基礎設施之法定加重刑責規定。<br>
‧ <strong>(D) 正確</strong>：該行為直接適用刑法第 362 條之 1 加重妨害電腦使用罪。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>DDoS (Distributed Denial of Service)</code> <span class="en">Distributed Denial of Service</span>：分散式阻斷服務攻擊。<br>
‧ <code>Cybercrime</code> <span class="en">Cybercrime</span>：網路犯罪、電腦犯罪。"""
    },
    {
        "ans": "C",
        "tag": "智慧財產權法",
        "stem": "生成式人工智慧（Generative AI）模型若完全無人類精神力投入，純粹由演算法程式自動演算產生之一幅數位畫作，依我國現行《著作權法》（Copyright Act）與實務見解，該畫作之法律地位為何？",
        "choices": [
            ("A", "由該 AI 軟體本身享有著作人格權，AI 開發者享有著作財產權"),
            ("B", "由下達提示詞（Prompt）之使用者自動取得完整著作權"),
            ("C", "非屬自然人之原創精神創作，不得享有著作權保護，落入公共領域"),
            ("D", "視同委聘創作，由 AI 軟體公司與使用者共有著作權")
        ],
        "ans_text": "(C) 非屬自然人之原創精神創作，不得享有著作權保護，落入公共領域",
        "explanation": """<strong>【核心法理與主管機關見解】</strong><br>
經濟部智慧財產局與法院實務穩定見解：<br>
(1) <strong>自然人創作原則</strong>：著作權法所保護之「著作」，係指「屬於文學、科學、藝術或其他學術範圍之<strong>精神上創作</strong>」（著作權法第 3 條第 1 項第 1 款），創作主體必須為<strong>自然人</strong>。<br>
(2) <strong>純 AI 生成物無著作權</strong>：若僅給予簡單指令（Prompt），由 AI 自主運算生成之內容，缺乏人類思想感情之精神創作表達，不具原創性（Originality），因此<strong>不享有著作權</strong>，直接落入公眾領域（Public Domain）。<br>
(3) <strong>例外保護</strong>：若人類在創作過程中具備重大投入與篩選、編排、後製，實質展現個人思想與原創性，僅將 AI 視為輔助創作工具者，該後續加工與獨創部分方可能享有著作權。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：AI 軟體不具自然人法律主體人格，絕無權利能力，不可能享有著作人格權。<br>
‧ <strong>(B) 錯誤</strong>：僅下達簡短 prompt，尚未達人類精神創作之原創表達門檻。<br>
‧ <strong>(C) 正確</strong>：純 AI 自動生成物依法不具著作權。<br>
‧ <strong>(D) 錯誤</strong>：委聘創作之受聘人亦需為具權利能力之人，AI 本身不得為民法上之契約受聘主體。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Originality</code> <span class="en">Originality</span>：原創性。<br>
‧ <code>Public Domain</code> <span class="en">Public Domain</span>：公共領域（公眾共有）。"""
    },
    {
        "ans": "A",
        "tag": "政府採購法",
        "stem": "公務機關辦理巨額或具高度技術性之「核心資訊系統委外建置案」，為避免不肖廠商低價搶標後品質低劣，依《政府採購法》（Government Procurement Act）規定，最適合採行之招標與決標策略為？",
        "choices": [
            ("A", "經上級機關核准後，採公開評選配合「最有利標（Most Advantageous Tender）」決標"),
            ("B", "採公開招標配合最低標決標，但要求廠商繳納百分之五十之履約保證金"),
            ("C", "逕行指定單一特定廠商採限制性招標比價，排除其餘競爭對手"),
            ("D", "採選擇性招標，並以現場抽籤方式決定得標廠商")
        ],
        "ans_text": "(A) 經上級機關核准後，採公開評選配合「最有利標（Most Advantageous Tender）」決標",
        "explanation": """<strong>【核心法條與政府採購實務】</strong><br>
依《政府採購法》第 52 條第 1 項第 3 款及第 56 條規定：<br>
(1) 資訊系統建置屬專業技術與履約能力極高之採購案，若採<strong>最低標</strong>，廠商常以超低價搶標，得標後無力履約導致爛尾。<br>
(2) 政府採購法明定具異質性之工程、財物或勞務採購，機關得報經上級機關核准，採<strong>最有利標</strong>決標，成立採購評選委員會，就廠商之技術能力、專案組織、資安防護計畫、報價等綜合評選，由總分最優之廠商得標。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：最有利標係兼顧技術品質、資安防護與合理價格之法定最佳決標機制。<br>
‧ <strong>(B) 錯誤</strong>：押標金保證金暨其他擔保作業辦法明定履約保證金上限原則為契約金額 10%，不得任意濫設 50% 阻礙投標。<br>
‧ <strong>(C) 錯誤</strong>：無正當法定事由逕行指定廠商採限制性招標，違反政府採購法公平競爭原則。<br>
‧ <strong>(D) 錯誤</strong>：政府採購法無「現場抽籤決定得標」之制度（僅於評選或抽籤同分同標價時作備位程序）。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Most Advantageous Tender (MAT)</code> <span class="en">Most Advantageous Tender</span>：最有利標。<br>
‧ <code>Evaluation Committee</code> <span class="en">Evaluation Committee</span>：採購評選委員會。"""
    },
    {
        "ans": "B",
        "tag": "憲法法庭",
        "stem": "依憲法法庭審理人權侵害案件之違憲審查架構，國家公權力限制人民憲法上之基本權利時，必須符合《憲法》第 23 條之「比例原則」（Principle of Proportionality）。比例原則包含四個子原則，其審查順序何者正確？",
        "choices": [
            ("A", "狹義比例原則 → 目的正當性 → 妥當性原則 → 必要性原則"),
            ("B", "目的正當性 → 妥當性（適合性）原則 → 必要性（最小侵害）原則 → 狹義比例原則（衡平性）"),
            ("C", "必要性原則 → 妥當性原則 → 目的正當性 → 狹義比例原則"),
            ("D", "衡平性原則 → 妥當性原則 → 必要性原則 → 法律保留原則")
        ],
        "ans_text": "(B) 目的正當性 → 妥當性（適合性）原則 → 必要性（最小侵害）原則 → 狹義比例原則（衡平性）",
        "explanation": """<strong>【核心法理與審查階層】</strong><br>
憲法法庭與公法學說建立之經典「比例原則四階審查」：<br>
<div class="step-box">
  <div class="step-title">📝 比例原則（Proportionality Principle）階層式審查順序</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge">第 1 階</span><strong>目的正當性（Legitimate Purpose）</strong>：公權力採取該措施所欲達成之公共利益目標，必須合憲正當。</li>
    <li class="step-item"><span class="step-badge">第 2 階</span><strong>適合性原則（Suitability / 妥當性）</strong>：所採行之手段必須有助於正當目的之達成（非完全無效）。</li>
    <li class="step-item"><span class="step-badge">第 3 階</span><strong>必要性原則（Necessity / 最小侵害）</strong>：在所有能達成相同效果之手段中，必須選擇對人民權利侵害最小者。</li>
    <li class="step-item"><span class="step-badge">第 4 階</span><strong>狹義比例原則（Proportionality Stricto Sensu / 衡平性）</strong>：手段造成的損害與所追求的公共利益之間，不得顯失均衡（過苛禁止）。</li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(B) 正確</strong>：嚴格依「目的正當性 → 適合性 → 必要性 → 衡平性」順序層層檢驗。<br>
‧ <strong>(A)(C)(D) 均錯誤</strong>：審查順序錯置或將非比例原則子原則混入。"""
    },
    {
        "ans": "C",
        "tag": "行政程序法",
        "stem": "行政機關於做成侵害人民權益之不利行政處分前，依《行政程序法》（Administrative Procedure Act）規定，應給予處分相對人何種正當程序保障？",
        "choices": [
            ("A", "給予該處分相對人先行聲請釋憲之權利"),
            ("B", "由上級法院召開言詞辯論庭裁定"),
            ("C", "原則上應給予該處分相對人陳述意見（Hearing / Representation）之機會"),
            ("D", "必須先獲得立法院內政委員會之審查同意")
        ],
        "ans_text": "(C) 原則上應給予該處分相對人陳述意見（Hearing / Representation）之機會",
        "explanation": """<strong>【核心法條與正當法律程序】</strong><br>
依《行政程序法》第 102 條規定：「行政機關作成限制或剝奪人民自由或權利之行政處分前，除已依第三十九條規定，通知處分相對人陳述意見，或依第一百零四條規定舉行聽證者外，<strong>應給予該處分相對人陳述意見之機會</strong>。」<br>
此即憲法上<strong>正當法律程序（Due Process of Law）</strong>在行政處分程序中最核心之具體實踐。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：行政處分做成前無從聲請憲法訴訟（須窮盡審級救濟確定後）。<br>
‧ <strong>(B) 錯誤</strong>：行政處分係行政機關單方公權力行為，做成前毋庸法院介入。<br>
‧ <strong>(C) 正確</strong>：事前陳述意見為不利處分之法定基本原則（除有第 103 條法定例外免給事由）。<br>
‧ <strong>(D) 錯誤</strong>：行政處分屬於行政權核心領域，立法院無權於事前逐案審查。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Due Process of Law</code> <span class="en">Due Process of Law</span>：正當法律程序。<br>
‧ <code>Right to be Heard</code> <span class="en">Right to be Heard</span>：受聽審權、陳述意見之權利。"""
    },
    {
        "ans": "B",
        "tag": "民法推導計算",
        "stem": "被繼承人甲死亡，遺有遺產現金新臺幣 1,200 萬元。甲無配偶，育有子女乙、丙、丁三人。甲於生前立下有效公證遺囑，表示「所有遺產 1,200 萬元全數給好友戊」。請問依我國現行《民法》（Civil Code）繼承編規定，子女乙依法得向戊主張行使扣減權之「特留分」金額為多少？",
        "choices": [
            ("A", "新臺幣 100 萬元"),
            ("B", "新臺幣 200 萬元"),
            ("C", "新臺幣 400 萬元"),
            ("D", "新臺幣 0 元（因甲之遺囑完全有效）")
        ],
        "ans_text": "(B) 新臺幣 200 萬元",
        "explanation": """<strong>【民法應繼分與特留分步進推導計算】</strong><br>
<div class="step-box">
  <div class="step-title">📝 遺產繼承與特留分（Legal Reserve）逐步計算</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge">步驟 1</span><strong>確定法定繼承人與法定應繼分（Civil Code §1138, §1141）</strong><br>
      ‧ 甲無配偶，第一順位繼承人為直系血親卑親屬（子女乙、丙、丁共三人）。<br>
      ‧ 依法按人數平均繼承，每人之<strong>法定應繼分比例為 1/3</strong>。<br>
      ‧ 乙之應繼分金額 = 1,200 萬元 × (1/3) = <strong>400 萬元</strong>。
    </li>
    <li class="step-item"><span class="step-badge">步驟 2</span><strong>計算直系血親卑親屬之特留分比例（Civil Code §1223 第 1 款）</strong><br>
      ‧ 直系血親卑親屬之特留分，為其<strong>應繼分之二分之一（1/2）</strong>。<br>
      ‧ 乙之特留分比例 = 應繼分 (1/3) × (1/2) = <strong>1/6</strong>。
    </li>
    <li class="step-item"><span class="step-badge">步驟 3</span><strong>計算特留分具體扣減金額</strong><br>
      ‧ 乙之特留分金額 = 1,200 萬元 × (1/6) = <strong>200 萬元</strong>。<br>
      ‧ 遺囑人雖得以遺囑處分財產，但不得侵害繼承人之特留分（民法第 1187 條）。遺囑侵害特留分時，乙依法享有<strong>扣減權（Right of Abatement）</strong>，得向受遺贈人戊扣減 200 萬元。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：計算比例錯誤。<br>
‧ <strong>(B) 正確</strong>：精確計算為 200 萬元。<br>
‧ <strong>(C) 錯誤</strong>：400 萬元為「法定應繼分」，非「特留分」。<br>
‧ <strong>(D) 錯誤</strong>：遺囑自由不得凌駕法定特留分之強制保障。"""
    },
    {
        "ans": "B",
        "tag": "刑法推導計算",
        "stem": "行為人甲犯竊盜罪經法院判處有期徒刑 1 年確定，入監服刑完畢出獄後第 2 年，甲又故意犯詐欺罪，依法最重本刑為有期徒刑 5 年。請問法官在對甲之詐欺罪宣告刑期時，依《刑法》（Penal Code）第 47 條「累犯」之規定及大法官釋字第 775 號解釋，下列處置何者正確？",
        "choices": [
            ("A", "甲不符合累犯要件，因為二罪罪名不同"),
            ("B", "甲符合累犯要件，但法官應依個案裁量是否加重其刑，非一律強制加重"),
            ("C", "法官依法必須強制加重本刑至三分之二"),
            ("D", "因詐欺罪本刑未達 7 年以上，法律不論以累犯")
        ],
        "ans_text": "(B) 甲符合累犯要件，但法官應依個案裁量是否加重其刑，非一律強制加重",
        "explanation": """<strong>【法條依據與司法院釋字第 775 號解釋】</strong><br>
<div class="step-box">
  <div class="step-title">📝 累犯（Recidivism）構成要件與合憲性審查推導</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge">要件 1</span><strong>前案判刑執行完畢</strong>：受徒刑之執行完畢，或一部之執行而赦免後。</li>
    <li class="step-item"><span class="step-badge">要件 2</span><strong>時效限制</strong>：於 <strong>5 年以內</strong> 故意再犯有期徒刑以上之罪者，為累犯（刑法第 47 條第 1 項）。甲於出獄後第 2 年故意再犯，符合 5 年期間限制，不問罪名是否相同。</li>
    <li class="step-item"><span class="step-badge">合憲調整</span><strong>釋字第 775 號解釋意旨</strong>：刑法第 47 條第 1 項不分情節一律強制加重最低本刑，致使罪刑不相當，違反憲法罪刑相當原則與比例原則。因此，法院審理時<strong>享有裁量權</strong>，審酌其特別惡性與再犯預防必要性，決定「是否加重其刑」，非一律強制加重！</li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：累犯不以同罪名為限，只要前後皆為故意且受徒刑執行即可。<br>
‧ <strong>(B) 正確</strong>：符合要件且落實釋字 775 號合憲解釋。<br>
‧ <strong>(C) 錯誤</strong>：累犯加重上限為二分之一，非三分之二，且非一律強制。<br>
‧ <strong>(D) 錯誤</strong>：法律無「本刑 7 年以上始成立累犯」之限制。"""
    },
    {
        "ans": "D",
        "tag": "立法院覆議門檻推導",
        "stem": "行政院對於立法院決議之法律案認為有窒礙難行時，得經總統核可移請立法院覆議。依《中華民國憲法增修條文》第 3 條規定，立法院現有立法委員共 113 席，若覆議案送達立法院後舉行表決，立法院至少需要多少位立法委員維持原案，行政院長始必須接受該決議？",
        "choices": [
            ("A", "出席委員過半數維持原案（出席 80 席時須 41 席）"),
            ("B", "全體立法委員三分之二以上維持原案（至少 76 席）"),
            ("C", "出席委員三分之二以上維持原案"),
            ("D", "全體立法委員二分之一以上維持原案（至少 57 席）")
        ],
        "ans_text": "(D) 全體立法委員二分之一以上維持原案（至少 57 席）",
        "explanation": """<strong>【憲法增修條文人數門檻逐步推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 立法院覆議維持原案之法定門檻推導</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge">步驟 1</span><strong>查閱憲法增修條文規定</strong><br>
      依《憲法增修條文》第 3 條第 2 項第 2 款規定：「覆議時，如經<strong>全體立法委員二分之一以上</strong>決議維持原案，行政院院長應即接受該決議。」
    </li>
    <li class="step-item"><span class="step-badge">步驟 2</span><strong>代入現行立法院席次計算</strong><br>
      ‧ 目前立法委員總席次法定為 <strong>113 席</strong>。<br>
      ‧ 全體立法委員之二分之一門檻：113 ÷ 2 = 56.5。<br>
      ‧ 門檻要求「二分之一以上」，故無條件進位為整數 <strong>57 席</strong>。
    </li>
    <li class="step-item"><span class="step-badge">步驟 3</span><strong>未達門檻之法律效果</strong><br>
      若贊成維持原案之立法委員未達全體二分之一（即 56 席以下），或逾期未為決議，原法律案<strong>即失其效力</strong>。
    </li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：憲法增修條文已改採「全體委員」計算，非「出席委員」。<br>
‧ <strong>(B) 錯誤</strong>：三分之二是憲法本文舊制（舊法已修廢），現行憲增非三分之二。<br>
‧ <strong>(C) 錯誤</strong>：並非出席之三分之二。<br>
‧ <strong>(D) 正確</strong>：精確門檻為全體立委二分之一以上（57 席）。"""
    },
    {
        "ans": "A",
        "tag": "行政罰法時效推導",
        "stem": "甲公司於民國 110 年 3 月 1 日違反《個人資料保護法》未落實資安防護義務，導致資料外洩。主管機關於 114 年 5 月 1 日始發現該違法情事並欲開罰。依《行政罰法》（Administrative Penalty Act）第 27 條之規定，下列關於行政罰裁處權時效之敘述，何者正確？",
        "choices": [
            ("A", "行政罰之裁處權，因三年期間之經過而消滅；本案已罹於時效，主管機關不得再為裁處"),
            ("B", "裁處權時效為五年，故主管機關仍得裁罰"),
            ("C", "時效自主管機關「知悉」時起算三年，故尚未罹於時效"),
            ("D", "行政罰之裁處時效均為十年，無消滅問題")
        ],
        "ans_text": "(A) 行政罰之裁處權，因三年期間之經過而消滅；本案已罹於時效，主管機關不得再為裁處",
        "explanation": """<strong>【核心法條與時效起算點推導】</strong><br>
<div class="step-box">
  <div class="step-title">📝 行政罰裁處權時效計算步驟</div>
  <ul class="step-list">
    <li class="step-item"><span class="step-badge">法條 1</span><strong>法定時效期間</strong>：依《行政罰法》第 27 條第 1 項：「行政罰之裁處權，因<strong>三年</strong>期間之經過而消滅。」</li>
    <li class="step-item"><span class="step-badge">法條 2</span><strong>時效起算點</strong>：同條第 2 項前段：「前項期間，自<strong>違反行政法上義務之行為為時起算</strong>。但行為有連續或繼續之狀態者，自行為終了之日起算。」——注意：是從「行為時」起算，<strong>不是從主管機關「知悉時」起算</strong>！</li>
    <li class="step-item"><span class="step-badge">計算</span><strong>案件涵攝</strong>：違規行為於 110 年 3 月 1 日發生，三年時效至 113 年 3 月 1 日即已屆滿消滅。主管機關於 114 年 5 月 1 日始欲裁罰，裁處權已確定罹於時效消滅，不得裁罰！</li>
  </ul>
</div>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：法定期限為 3 年，自行為時起算，已罹於時效。<br>
‧ <strong>(B)(D) 錯誤</strong>：行政罰裁處權原則為 3 年，非 5 年或 10 年。<br>
‧ <strong>(C) 錯誤</strong>：此為常見大陷阱！公務員懲戒法或民法侵權行為才以知悉起算，行政罰法明定自「行為時」起算。"""
    },
    {
        "ans": "C",
        "tag": "營業秘密法",
        "stem": "資訊工程師乙自甲科技公司離職，離職前將公司未公開之核心演算法原始碼秘密複製存入私人隨身碟，並意圖前往海外競爭對手處任職使用。依我國《營業秘密法》（Trade Secrets Act），下列敘述何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "營業秘密之法定三要件為：秘密性、經濟價值性、合理保密措施"),
            ("B", "若意圖在中華民國境外使用而侵害營業秘密，成立加重侵害營業秘密罪，處 1 年以上 10 年以下有期徒刑"),
            ("C", "營業秘密法僅設有民事損害賠償責任，完全不具備刑事處罰條款"),
            ("D", "侵害營業秘密所得之不法利益，法院得予以沒收或追徵")
        ],
        "ans_text": "(C) 營業秘密法僅設有民事損害賠償責任，完全不具備刑事處罰條款",
        "explanation": """<strong>【核心法條與修法要點】</strong><br>
我國為保護高科技產業命脈，早已修正《營業秘密法》增訂<strong>刑事責任</strong>：<br>
(1) <strong>境內侵權</strong>：刑法第 13 條之 1，處 5 年以下有期徒刑或拘役，得併科新臺幣 100 萬元以上 1,000 萬元以下罰金。<br>
(2) <strong>境外侵權（域外加重處罰）</strong>：刑法第 13 條之 2，意圖在大陸地區、香港、澳門或外國使用而侵害營業秘密者，處 <strong>1 年以上 10 年以下有期徒刑</strong>，得併科新臺幣 300 萬元以上 5,000 萬元以下罰金！<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：營業秘密法第 2 條所定經典三要件：秘密性（非一般周知）、經濟價值性（具商業價值）、合理保密措施（所有人已採取保密行動）。<br>
‧ <strong>(B) 正確</strong>：第 13 條之 2 境外使用加重處罰為我國國考常考法規重點。<br>
‧ <strong>(C) 錯誤（本題正解）</strong>：營業秘密法兼具嚴厲之刑事處罰條款，並非僅有民事責任。<br>
‧ <strong>(D) 正確</strong>：犯罪所得依法沒收或追徵。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Trade Secret</code> <span class="en">Trade Secret</span>：營業秘密。<br>
‧ <code>Non-Disclosure Agreement (NDA)</code> <span class="en">Non-Disclosure Agreement</span>：保密協定。"""
    },
    {
        "ans": "B",
        "tag": "公務員服務法",
        "stem": "民國 111 年新修正之《公務員服務法》（Civil Service Law），為保障公務員健康權（釋字第 785 號解釋意旨），下列關於公務員工時與輪班輪休之規定，何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "公務員每日辦公時數原則為 8 小時，每週辦公時數原則為 40 小時"),
            ("B", "公務員延長辦公時數（加班）每日完全無上限，行政首長享有絕對裁量權"),
            ("C", "輪班制公務員更換班次時，原則上應至少享有連續 11 小時之休息時間"),
            ("D", "公務員非經服務機關許可，不得兼任教學或研究工作或非營利團體職務")
        ],
        "ans_text": "(B) 公務員延長辦公時數（加班）每日完全無上限，行政首長享有絕對裁量權",
        "explanation": """<strong>【核心法條與憲法裁判】</strong><br>
司法院釋字第 785 號解釋宣告舊公務員服務法未針對業務性質特殊之輪班制公務員訂定合乎健康權保障之工時框架規範為違憲。立法院據此於民國 111 年全文修正《公務員服務法》：<br>
(1) <strong>工時上限</strong>：公務員延長辦公時數<strong>每日連同法定辦公時數不得超過 12 小時</strong>，延長辦公時數<strong>每月不得超過 60 小時</strong>（第 12 條第 3 項）。<br>
(2) <strong>輪班間隔</strong>：輪班制公務員更換班次時，至少應有<strong>連續 11 小時之休息時間</strong>（落實健康權保障）。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：每日 8 小時、每週 40 小時為法定常態工時原則。<br>
‧ <strong>(B) 錯誤（本題正解）</strong>：每日法定連同加班上限原則為 12 小時，每月上限 60 小時，絕非無上限！<br>
‧ <strong>(C) 正確</strong>：法文明定休息間隔至少連續 11 小時。<br>
‧ <strong>(D) 正確</strong>：公務員服務法第 15 條兼職規範之許可制原則。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Right to Health</code> <span class="en">Right to Health</span>：健康權。<br>
‧ <code>Overtime Work</code> <span class="en">Overtime Work</span>：加班、延長辦公時數。"""
    },
    {
        "ans": "D",
        "tag": "國家賠償法",
        "stem": "公務機關建置之即時暴雨告警智慧物聯網（IoT）系統，因機關長期疏於資通硬體維護且感測器電池耗盡未更換，導致豪雨來襲時系統完全未發出警報，造成低窪地區民眾車輛全數滅頂泡水。民眾欲向該機關請求國家賠償，其法律依據最主要是《國家賠償法》（State Compensation Law）第幾條？",
        "choices": [
            ("A", "第 2 條第 1 項公務員故意不法侵權"),
            ("B", "第 4 條受委託行使公權力團體責任"),
            ("C", "第 6 條特別法優先原則"),
            ("D", "第 3 條公有公共設施因設置或管理有欠缺致人民生命、身體、人身自由或財產受損害者")
        ],
        "ans_text": "(D) 第 3 條公有公共設施因設置或管理有欠缺致人民生命、身體、人身自由或財產受損害者",
        "explanation": """<strong>【核心法條與責任型態區辨】</strong><br>
國家賠償法區分為兩大責任型態：<br>
(1) <strong>第 2 條（人責任，過失責任）</strong>：公務員執行職務行使公權力，因故意或過失不法侵害人民自由或權利。<br>
(2) <strong>第 3 條（物責任，無過失責任）</strong>：公共設施因<strong>設置或管理有欠缺</strong>，致人民生命、身體、人身自由或財產受損害者，國家應負賠償責任。本條屬<strong>客觀無過失責任</strong>，只要設施缺乏通常應具備之安全性即成立，被害人無須證明特定公務員個人之過失。<br>
智慧暴雨告警系統、感測器、水門、排水抽水站等設備，均屬於國家提供公眾使用之「公有公共設施」，因管理疏失（電池耗盡未更換）導致功能喪失，直接該當<strong>第 3 條物之管理欠缺</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：第 2 條需證明公務員特定故意或過失，本案依第 3 條主張更具優勢且為物的客觀管理欠缺。<br>
‧ <strong>(B) 錯誤</strong>：本案為機關自建自管，非受託行使公權力團體責任。<br>
‧ <strong>(C) 錯誤</strong>：第 6 條為法規競合條款，非請求權基礎。<br>
‧ <strong>(D) 正確</strong>：公有公共設施設置或管理欠缺之國家賠償責任。"""
    },
    {
        "ans": "A",
        "tag": "行政處分廢止與撤銷",
        "stem": "甲民眾以偽造之低收入戶證明文件與虛偽所得資料，向直轄市社會局申請通過獲得每月新臺幣 15,000 元之弱勢科技補助津貼。主管機關於 6 個月後查明甲自始造假之事實。請問社會局應依《行政程序法》（Administrative Procedure Act）採取何種處置？",
        "choices": [
            ("A", "依第 117 條將該違法之授益行政處分予以「撤銷」（Revocation），且甲無信賴保護原則之適用"),
            ("B", "依第 123 條將該合法之處分予以「廢止」（Abolition），並補償甲之信賴利益"),
            ("C", "逕行以行政處分直接判處甲一年有期徒刑"),
            ("D", "因處分已生效滿六個月，依法不得再做任何變更")
        ],
        "ans_text": "(A) 依第 117 條將該違法之授益行政處分予以「撤銷」（Revocation），且甲無信賴保護原則之適用",
        "explanation": """<strong>【核心概念：撤銷 vs 廢止】</strong><br>
行政法經典觀念辨析：<br>
(1) <strong>撤銷（Revocation）</strong>：針對<strong>自始違法</strong>之行政處分，使其溯及既往失其效力（行政程序法第 117 條）。<br>
(2) <strong>廢止（Abolition / Repeal）</strong>：針對<strong>自始合法</strong>，但因嗣後情事變更或法定事由發生，由行政機關使其向將來失其效力（行政程序法第 123 條）。<br>
(3) <strong>信賴不值得保護</strong>：依行政程序法第 119 條第 1 款，受益人以<strong>詐欺、脅迫或賄賂</strong>方法，使行政機關作成行政處分者，其<strong>信賴不值得保護</strong>。甲以偽造文件詐領補助，處分自始違法，社會局應予「撤銷」，且甲無信賴保護可言，已受領之款項應依第 127 條不當得利全數追繳返還。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：自始違法處分適用「撤銷」，且造假者信賴不值得保護。<br>
‧ <strong>(B) 錯誤</strong>：廢止適用於合法處分，且甲無信賴利益補償請求權。<br>
‧ <strong>(C) 錯誤</strong>：行政機關非司法法院，無權判處徒刑刑罰。<br>
‧ <strong>(D) 錯誤</strong>：撤銷權之除斥期間為知有撤銷原因起 2 年內（第 121 條），6 個月內完全合法有權撤銷。"""
    },
    {
        "ans": "C",
        "tag": "憲法言論自由",
        "stem": "主管機關以「維護社會善良風俗」為由，要求所有民間軟體開發者在應用程式商店（App Store）上架軟體前，必須事先將程式碼與所有畫面文字提交政府審查委員會核准，否則不得上架。依我國憲法法庭歷來解釋意旨，此種管制措施侵害憲法第 11 條何種最核心之基本權利保障？",
        "choices": [
            ("A", "秘密通訊自由之事前許可"),
            ("B", "人身自由之法官保留原則"),
            ("C", "言論自由中原則上絕對禁止之「事前審查」（Prior Restraint）"),
            ("D", "集會結社自由之報備許可制")
        ],
        "ans_text": "(C) 言論自由中原則上絕對禁止之「事前審查」（Prior Restraint）",
        "explanation": """<strong>【核心法理與司法院釋字第 744 號解釋】</strong><br>
依司法院釋字第 744 號、第 364 號等多號憲法解釋意旨：<br>
(1) <strong>事前審查之嚴格禁止</strong>：事前審查（Prior Restraint）係指公權力在言論發表之前，對其內容進行審查並決定是否准許發表。事前審查會徹底扼殺言論於搖籃之中，因此在憲法言論自由之審查上，享有<strong>原則上違憲之強烈推定</strong>。<br>
(2) <strong>除極端例外不得設立事前審查</strong>：只有在極端緊急、涉及迫在眉睫之重大國家安全或不可回復之重大法益侵害時，始得例外嚴格審查，否則一律宣告違憲。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：非秘密通訊問題（通訊保障及監察法針對私人通訊之截聽）。<br>
‧ <strong>(B) 錯誤</strong>：人身自由涉及拘禁逮捕，非言論發表審查。<br>
‧ <strong>(C) 正確</strong>：事前審查為言論自由最受嚴厲非難之違憲態樣。<br>
‧ <strong>(D) 錯誤</strong>：本案非集會遊行或人民結社問題。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Prior Restraint</code> <span class="en">Prior Restraint</span>：事前審查。<br>
‧ <code>Freedom of Speech</code> <span class="en">Freedom of Speech</span>：言論自由。"""
    },
    {
        "ans": "B",
        "tag": "中央法規標準法",
        "stem": "依《中央法規標準法》（Central Regulation Standard Act）規定，下列關於法律與命令位階及生效日期之敘述，何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "法律應經立法院通過，總統公布"),
            ("B", "法規明定自公布日施行者，自公布之當日起算，至次日凌晨零時起發生效力"),
            ("C", "命令不得牴觸憲法或法律，下級機關訂定之命令不得牴觸上級機關之命令"),
            ("D", "法規定有施行期限者，期滿當然廢止，不須另行公布廢止")
        ],
        "ans_text": "(B) 法規明定自公布日施行者，自公布之當日起算，至次日凌晨零時起發生效力",
        "explanation": """<strong>【核心法條與生效日計算】</strong><br>
依《中央法規標準法》第 13 條規定：<br>
「法規明定自公布或發布日施行者，自公布或發布之日起算<strong>至第三日起發生效力</strong>。」<br>
例如：10 月 1 日公布，自公布日算起第 1 日（10/1）、第 2 日（10/2）、第 3 日（10/3）零時起發生效力！國考極常考此「第 3 日」算式，絕非「次日」或「當日」！<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：第 4 條法律成立要件。<br>
‧ <strong>(B) 錯誤（本題正解）</strong>：自公布之日起算至「第三日」發生效力，非次日。<br>
‧ <strong>(C) 正確</strong>：第 11 條法規位階原則。<br>
‧ <strong>(D) 正確</strong>：第 23 條明定定有期限者期滿當然失效。"""
    },
    {
        "ans": "D",
        "tag": "民法契約總則",
        "stem": "甲在網路拍賣平臺刊登一台二手高效能伺服器，標價新臺幣 50,000 元。乙在網站上下單點擊購買並完成信用卡刷卡授權。依《民法》（Civil Code）契約之成立規範，下列敘述何者正確？",
        "choices": [
            ("A", "甲在網站上刊登商品與標價，法律上一律視為要約之引誘，甲可隨時無條件拒絕履約"),
            ("B", "乙點擊下單僅為要約之引誘，需待甲打電話確認後契約方始成立"),
            ("C", "買賣契約必須雙方至戶政事務所公證後始發生效力"),
            ("D", "貨物標價陳列者視為要約；乙完成下單承諾時，雙方意思表示一致，買賣契約即行成立")
        ],
        "ans_text": "(D) 貨物標價陳列者視為要約；乙完成下單承諾時，雙方意思表示一致，買賣契約即行成立",
        "explanation": """<strong>【核心法條與網路買賣實務】</strong><br>
依《民法》第 154 條第 2 項規定：「<strong>貨物標價陳列者，視為要約</strong>。但價目表之寄送，不視為要約。」<br>
在電子商務中，電商平臺若明確標示商品品名、規格、單價並提供購買點擊機制，視為要約；消費者依指示下單完成付款授權（承諾），雙方<strong>意思表示合致，買賣契約即合法成立</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：民法第 154 條明定標價陳列視為要約，出賣人受該要約之拘束。<br>
‧ <strong>(B) 錯誤</strong>：下單在標價要約下屬承諾，意思表示合致契約即成立。<br>
‧ <strong>(C) 錯誤</strong>：動產買賣為諾成非要式契約，不以公證為要件。<br>
‧ <strong>(D) 正確</strong>：符合民法契約成立基本原則。"""
    },
    {
        "ans": "A",
        "tag": "憲法平權原則",
        "stem": "國家考試在特定類科中，若限定「僅限男性報考」或「男性身高須滿 165 公分、女性須滿 160 公分」，依憲法法庭 113 年憲判字第 6 號（消防警察身高限制案）及平權審查標準，該項身高限制規定因何原因被宣告違憲？",
        "choices": [
            ("A", "實質造成女性應考受大幅排除，未能證明該特定身高與執行公務有實質關聯，侵害女性服公職權與平等權"),
            ("B", "違反憲法第 8 條人身自由之保障"),
            ("C", "違反中央法規標準法關於罰則之規定"),
            ("D", "因消防警察工作完全不具任何體力門檻，不得設任何體格檢查")
        ],
        "ans_text": "(A) 實質造成女性應考受大幅排除，未能證明該特定身高與執行公務有實質關聯，侵害女性服公職權與平等權",
        "explanation": """<strong>【113 年憲判字第 6 號裁判重點】</strong><br>
憲法法庭 113 年憲判字第 6 號判決宣告公務人員特種考試警察人員考試消防警察人員類別錄取人員體格檢查「女性身高未滿 160 公分不合格」之規定違憲：<br>
(1) <strong>不利差別待遇與實質排除</strong>：該身高標準使近九成男性符合資格，卻使高達五成以上女性被排除於門檻之外，實質造成性別間之巨大不平等。<br>
(2) <strong>缺乏實質關聯性</strong>：主管機關無法提出客觀實證數據，證明身高未滿 160 公分者確實無法勝任現代消防各項專業任務與科技救災裝備。<br>
(3) <strong>違憲結論</strong>：違反憲法第 7 條<strong>平等權（Right to Equality）</strong>及第 18 條<strong>人民服公職權（Right to Take Public Service Examinations）</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：精確切中 113 年憲判字第 6 號判決意旨。<br>
‧ <strong>(B) 錯誤</strong>：非人身自由拘禁問題。<br>
‧ <strong>(C) 錯誤</strong>：體檢標準非刑罰罰則。<br>
‧ <strong>(D) 錯誤</strong>：消防工作得設合理體格規範，但必須具實質合理關聯且不得造成不合理性別實質歧視。"""
    },
    {
        "ans": "C",
        "tag": "公務員懲戒法",
        "stem": "公務員受懲戒法院判決受「免除職務」處分者，依《公務員懲戒法》（Public Functionary Disciplinary Act）規定，其法律效果為何？",
        "choices": [
            ("A", "降一級改敘，一年內不得晉敘"),
            ("B", "停止其公務員身分二年，期滿得申請復職"),
            ("C", "免除其現職，並「終身不得再任公務員」"),
            ("D", "僅罰款新臺幣 10 萬元，保留現職")
        ],
        "ans_text": "(C) 免除其現職，並「終身不得再任公務員」",
        "explanation": """<strong>【公務員懲戒處分種類與極刑】</strong><br>
依《公務員懲戒法》第 9 條所列之懲戒處分種類（由重至輕）：<br>
1. <strong>免除職務（最重懲戒處分）</strong>：依第 11 條規定，免除其現職，並<strong>終身不得再任公務員</strong>！<br>
2. 撤職：撤其現職，並於一定期間（1 年至 5 年）停止任用，期滿得再任。<br>
3. 剝奪、減少退休（職、伍）金。<br>
4. 休職：休其現職，期間 6 個月至 3 年。<br>
5. 降級。<br>
6. 減俸。<br>
7. 罰款。<br>
8. 記過。<br>
9. 申誡。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：此為「降級」之效果。<br>
‧ <strong>(B) 錯誤</strong>：此為「休職」之效果。<br>
‧ <strong>(C) 正確</strong>：「免除職務」為公務員懲戒中最嚴厲者，永久喪失公務員身分。<br>
‧ <strong>(D) 錯誤</strong>：此為單純罰款。"""
    },
    {
        "ans": "B",
        "tag": "行政訴訟法審級制度",
        "stem": "民國 112 年 8 月 15 日施行之《行政訴訟法》（Administrative Litigation Act）新制，將原本分散於各地方法院行政訴訟庭之第一審事件整合，現行我國行政法院之審級架構為何？",
        "choices": [
            ("A", "地方法院行政訴訟庭 → 高等行政法院 → 最高行政法院（三級二審）"),
            ("B", "高等行政法院「地方行政訴訟庭」→ 高等行政法院「高等行政訴訟庭」→ 最高行政法院（堅實第一審之三級二審）"),
            ("C", "憲法法庭 → 高等行政法院 → 司法院公務員懲戒委員會"),
            ("D", "各地簡易庭 → 最高法院行政民事合併庭")
        ],
        "ans_text": "(B) 高等行政法院「地方行政訴訟庭」→ 高等行政法院「高等行政訴訟庭」→ 最高行政法院（堅實第一審之三級二審）",
        "explanation": """<strong>【行政訴訟新制重大變革】</strong><br>
為強化行政審判專業性與落實「堅實第一審」，112 年 8 月正式上路之行政訴訟新制：<br>
(1) <strong>廢除地方法院行政訴訟庭</strong>：將各地方法院行政訴訟庭全數裁撤，改於臺北、臺中、高雄高等行政法院增設<strong>地方行政訴訟庭</strong>。<br>
(2) <strong>體系一元化</strong>：第一審簡易與交通事件由高等行政法院「地方行政訴訟庭」審理，上訴至高等行政法院「高等行政訴訟庭」；通常事件則由「高等行政訴訟庭」為第一審，上訴至「最高行政法院」。維持「三級二審」體系，但行政訴訟法官專責於行政法院體系內培育維運。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：舊法時代之地方法院行政訴訟庭已廢止。<br>
‧ <strong>(B) 正確</strong>：新制高等行政法院分設地方與高等行政訴訟庭之專業體制。<br>
‧ <strong>(C)(D) 均錯誤</strong>：法院體系與管轄錯誤。"""
    },
    {
        "ans": "A",
        "tag": "個人資料外洩通知義務",
        "stem": "某公立學校公務伺服器遭駭客植入後門，導致數萬名學生與家長身分證字號、戶籍地址遭洩漏並散布於暗網。依《個人資料保護法》（PDPA）第 12 條規定，該公立學校於查明後應履行何項法定通知義務？",
        "choices": [
            ("A", "應以適當方式通知當事人（Data Subjects）該外洩情事"),
            ("B", "僅須向暗網論壇寄發存證信函即可，無須通知被害人"),
            ("C", "只要資料庫完成補強重灌，得完全隱匿不通知任何當事人"),
            ("D", "必須自費為所有外洩學生投保新臺幣一億元之人壽保險")
        ],
        "ans_text": "(A) 應以適當方式通知當事人（Data Subjects）該外洩情事",
        "explanation": """<strong>【核心法條】</strong><br>
依《個人資料保護法》第 12 條規定：「公務機關或非公務機關違反本法規定，致個人資料被竊取、洩漏、竄改或其他侵害者，<strong>應查明後以適當方式通知當事人</strong>。」<br>
通知目的在於使當事人能及時採取防護措施（如更換密碼、停用帳戶、提高防詐意識等），落實資訊自主權。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：法文明定應以適當方式通知當事人。<br>
‧ <strong>(B)(C) 錯誤</strong>：刻意隱匿違反個資法法定通報與通知義務，將面臨行政懲處與民事損害賠償。<br>
‧ <strong>(D) 錯誤</strong>：法律無此項責任規範。"""
    },
    {
        "ans": "D",
        "tag": "著作權合理使用",
        "stem": "資訊系教授為課堂學術教學目的，將甲學者已公開發表之網路資安學術論文節錄其中 3 頁重要拓撲架構圖，影印發給修課的 30 名學生研討，並明確標註出處與作者。依我國《著作權法》（Copyright Act）規定，該教授之行為屬於？",
        "choices": [
            ("A", "侵害著作財產權之重製權，應處三年以下有期徒刑"),
            ("B", "侵害著作人格權之公開發表權"),
            ("C", "必須事前取得作者之書面授權，否則不論如何均屬侵權"),
            ("D", "合於著作權法第 46 條及第 65 條所定「學校教學目的之合理使用（Fair Use）」，不構成侵權")
        ],
        "ans_text": "(D) 合於著作權法第 46 條及第 65 條所定「學校教學目的之合理使用（Fair Use）」，不構成侵權",
        "explanation": """<strong>【核心法條與合理使用四要素】</strong><br>
依《著作權法》第 46 條規定，依法設立之各級學校及其擔任教學之人，為學校授課需要，在合理範圍內，得重製他人已公開發表之著作。<br>
依第 65 條第 2 項之「合理使用（Fair Use）」四項綜合判斷基準：<br>
1. <strong>利用之目的及性質</strong>：非營利、教育學術研究目的。<br>
2. <strong>著作之性質</strong>：事實性、學術性著作。<br>
3. <strong>所利用之質量及其在整個著作所佔之比例</strong>：僅節錄 3 頁，佔全篇比例極低。<br>
4. <strong>利用結果對著作潛在市場與現在價值之影響</strong>：無替代市場效果，且已註明出處。<br>
故該教授之行為完全合於著作權法合理使用，不構成侵害著作權。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A)(B)(C) 均錯誤</strong>：忽略著作權法第 46 條與第 65 條法定合理使用豁免規定。<br>
‧ <strong>(D) 正確</strong>：符合教學合理使用法定要件。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Fair Use</code> <span class="en">Fair Use</span>：合理使用。<br>
‧ <code>Copyright Infringement</code> <span class="en">Copyright Infringement</span>：著作權侵害。"""
    },
    {
        "ans": "C",
        "tag": "政府資訊公開法",
        "stem": "民眾乙依《政府資訊公開法》（Freedom of Information Act）向直轄市政府交通局申請調閱某智慧交控系統之原始採購合約、經費明細與廠商投標服務建議書。下列哪一項資訊依該法第 18 條規定，政府機關原則上「應限制公開或不予提供」？",
        "choices": [
            ("A", "政府機關之法定名稱與機關地址"),
            ("B", "該案之最終決標金額與得標廠商全名"),
            ("C", "投標廠商所提出之營業秘密或營業資訊，公開將侵害該廠商之合法權利且未涉及重大公益者"),
            ("D", "該智慧交控系統所使用之公共道路路口名稱")
        ],
        "ans_text": "(C) 投標廠商所提出之營業秘密或營業資訊，公開將侵害該廠商之合法權利且未涉及重大公益者",
        "explanation": """<strong>【核心法條與豁免公開事由】</strong><br>
依《政府資訊公開法》第 18 條第 1 項第 7 款規定：<br>
「個人、法人或團體營業上秘密或經營上之資訊，其公開或提供有侵害該個人、法人或團體之權利、競爭地位或其他正當利益者，<strong>應限制公開或不予提供</strong>。但對公益有必要或為保護人民生命、身體、健康有必要或經當事人同意者，不在此限。」<br>
廠商服務建議書內通常包含其獨家未公開之核心演算法、商業成本結構與專利技術，屬營業秘密，原則上應予遮蔽或不予公開。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A)(B)(D) 均錯誤</strong>：均屬依法應主動公開或人民申請時應透明揭露之政府資訊。<br>
‧ <strong>(C) 正確</strong>：法定營業秘密豁免條款。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Freedom of Information</code> <span class="en">Freedom of Information</span>：政府資訊公開、資訊自由。"""
    },
    {
        "ans": "A",
        "tag": "刑法偽造文書罪",
        "stem": "公務員丙明知某資訊廠商未依規格履約，竟仍在職務上掌管之公文書「驗收合格紀錄表」上填載「全數依約完成驗收，查驗合格」，並送陳主管核決付款。丙之行為構成何種刑法罪名？",
        "choices": [
            ("A", "刑法第 213 條公務員登載不實罪"),
            ("B", "刑法第 210 條偽造私文書罪"),
            ("C", "刑法第 359 條破壞電磁紀錄罪"),
            ("D", "僅違反行政程序法，不涉任何刑責")
        ],
        "ans_text": "(A) 刑法第 213 條公務員登載不實罪",
        "explanation": """<strong>【核心法條】</strong><br>
依《刑法》第 213 條規定：「公務員明知為不實之事項，而<strong>登載於職務上所掌之公文書</strong>，足以生損害於公眾或他人者，處一年以上七年以下有期徒刑。」<br>
丙身為公務員，該驗收紀錄表為其職務上製作掌管之公文書，其明知廠商未履約卻故意登載合格，已侵害公文書之公共信用與國家財政正確性，完全成立<strong>公務員登載不實罪</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：具公務員身分且登載於職務掌管公文書，為第 213 條典型態樣。<br>
‧ <strong>(B) 錯誤</strong>：驗收紀錄表為公文書，且丙有製作權限，非「無制作權而捏造」之偽造私文書。<br>
‧ <strong>(C) 錯誤</strong>：非無故變更電磁紀錄罪。<br>
‧ <strong>(D) 錯誤</strong>：嚴重觸犯刑事重大公務員犯罪。"""
    },
    {
        "ans": "B",
        "tag": "民法消滅時效",
        "stem": "甲借款新臺幣 100 萬元給乙，約定 1 年後清償。清償期屆滿後，甲因出國繁忙，長達 16 年均未向乙催討該筆借款。第 17 年甲向法院起訴請求乙返還借款。依《民法》（Civil Code）第 125 條及第 144 條規定，乙在法律上享有何種抗辯權？",
        "choices": [
            ("A", "乙之借款債務已自動合法歸於消滅，乙無須為任何主張"),
            ("B", "請求權因 15 年間不行使而消滅；乙得主張「時效消滅抗辯權」而拒絕給付"),
            ("C", "消滅時效為 20 年，故乙仍必須全額償還"),
            ("D", "乙必須向檢察官自首詐欺罪，由法院判決債務無效")
        ],
        "ans_text": "(B) 請求權因 15 年間不行使而消滅；乙得主張「時效消滅抗辯權」而拒絕給付",
        "explanation": """<strong>【核心法條與抗辯權法理】</strong><br>
依《民法》第 125 條：「請求權，因<strong>十五年間不行使而消滅</strong>。但法律所定期間較短者，依其規定。」<br>
依《民法》第 144 條第 1 項：「時效完成後，<strong>債務人得拒絕給付</strong>。」<br>
我國民法採「抗辯權發生主義」，時效完成後，債權本身不當然消滅，而是債務人取得<strong>拒絕給付之抗辯權（Defense of Limitation）</strong>。債務人乙只要在法院審理時提出時效消滅之抗辯，法官即應判決駁回原告甲之請求。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：實體債權不自動消滅（若乙自願清償仍為有法律上原因，不得依不當得利請求返還）。<br>
‧ <strong>(B) 正確</strong>：一般請求權消滅時效為 15 年，乙得行使拒絕給付抗辯權。<br>
‧ <strong>(C) 錯誤</strong>：一般消滅時效為 15 年，非 20 年。<br>
‧ <strong>(D) 錯誤</strong>：民事借貸時效與刑事詐欺自首無關。"""
    },
    {
        "ans": "C",
        "tag": "行政執行法",
        "stem": "行政機關命違規工廠限期拆除違章煙囪，該工廠負責人逾期仍不拆除。主管機關依法調派吊車與工班進場代為強制拆除，並向該負責人追繳拆除作業費用。此種行政執行手段屬於《行政執行法》（Administrative Execution Act）之何種執行方法？",
        "choices": [
            ("A", "公法上金錢給付義務之執行"),
            ("B", "怠金（連續處罰）"),
            ("C", "代履行（Execution by Substitution）"),
            ("D", "即時強制之管束")
        ],
        "ans_text": "(C) 代履行（Execution by Substitution）",
        "explanation": """<strong>【核心法條與執行方法歸類】</strong><br>
依《行政執行法》第 28 條及第 29 條：<br>
(1) <strong>代履行（第 29 條）</strong>：依法令或處分負有<strong>行為義務，此義務由他人代為履行亦能達成相同目的</strong>（可替代性行為義務），義務人逾期不履行者，由執行機關委託第三人或指定人員代為履行，其費用由義務人負擔。<br>
(2) <strong>怠金（第 30 條）</strong>：負有<strong>不可代替之行為義務或不行為義務</strong>（如親自出庭作證、不得接近某處），逾期不履行時，處新臺幣 5,000 元以上 30 萬元以下怠金，以督促其自行履行。<br>
拆除煙囪屬於他人亦能代為施作之「可替代行為義務」，故為典型的<strong>代履行</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：拆除煙囪為行為義務，非一開始之金錢給付義務。<br>
‧ <strong>(B) 錯誤</strong>：怠金適用於不可替代行為或不行為。<br>
‧ <strong>(C) 正確</strong>：代履行之典型定義。<br>
‧ <strong>(D) 錯誤</strong>：即時強制管束係針對人身自由之緊急處置。"""
    },
    {
        "ans": "D",
        "tag": "公民投票法",
        "stem": "依《中華民國憲法》及現行《公民投票法》（Referendum Act）規定，下列哪一事項<strong>不得</strong>作為全國性公民投票之提案標的？",
        "choices": [
            ("A", "法律之複決"),
            ("B", "重大政策之創制"),
            ("C", "重大政策之複決"),
            ("D", "預算案、租稅、薪俸及人事事項")
        ],
        "ans_text": "(D) 預算案、租稅、薪俸及人事事項",
        "explanation": """<strong>【核心法條與公投除外事項】</strong><br>
依《公民投票法》第 2 條第 2 項及第 3 項規定：<br>
全國性公民投票適用事項包括：<br>
一、法律之複決。<br>
二、立法原則之創制。<br>
三、重大政策之創制或複決。<br>
但明文規定：<strong>預算、租稅、薪俸及人事事項，不得作為公民投票之提案。</strong><br>
立法考量若由全民公投決定減稅或增加福利預算，將導致國家財政瞬間崩盤；若由公投罷免決定個別公務員人事，將侵害權力分立與考試任用制度。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A)(B)(C) 錯誤</strong>：均為公投法明定之合法公投適用事項。<br>
‧ <strong>(D) 正確</strong>：預算、租稅、薪俸及人事為法定絕對禁止公投事項。"""
    },
    {
        "ans": "A",
        "tag": "憲法信賴保護原則",
        "stem": "立法機關制定新法律變更既有法規時，對於過去已依舊法產生合理期待並為生活規劃之人民，應設定補救措施或過渡條款。此項合憲性審查所依據之公法原則為何？",
        "choices": [
            ("A", "信賴保護原則（Principle of Protection of Legitimate Expectations）"),
            ("B", "不當聯結禁止原則"),
            ("C", "情事變更原則"),
            ("D", "帝王條款之誠實信用原則")
        ],
        "ans_text": "(A) 信賴保護原則（Principle of Protection of Legitimate Expectations）",
        "explanation": """<strong>【核心法理與司法院釋字第 525 號解釋】</strong><br>
依司法院釋字第 525 號、第 717 號等重要憲法解釋：<br>
(1) <strong>信賴保護原則三要件</strong>：<br>
‧ <strong>信賴基礎</strong>：有國家公權力之具體行政行為或法規存在。<br>
‧ <strong>信賴表現</strong>：人民因信賴該法規而展開具體財產或生活處分安排。<br>
‧ <strong>信賴值得保護</strong>：人民無詐欺、脅迫或明知重大違法等不可歸責事由。<br>
(2) <strong>過渡條款義務</strong>：法規即使因重大公共利益需要修正或廢止，國家仍應訂定適當過渡條款（如分期實施、落日條款、補償措施），以保護人民既有之正當信賴利益。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 正確</strong>：憲法法治國原則所衍生之信賴保護原則。<br>
‧ <strong>(B) 錯誤</strong>：不當聯結禁止原則係指行政行為所追求手段與目的間不得有不相干之牽連。<br>
‧ <strong>(C) 錯誤</strong>：情事變更主要為民法契約或訴訟法上概念。<br>
‧ <strong>(D) 錯誤</strong>：誠信原則雖為公私法共通，但針對法規變動過渡保障，憲法學界均精確適用信賴保護原則。"""
    },
    {
        "ans": "B",
        "tag": "行政處分之附款",
        "stem": "直轄市環保局核發某資訊科技廠之排氣許可證，並於許可證上註明「本廠應於每年 12 月 31 日前向本局申報空氣品質連續監測數據紀錄備查」。此項註明在行政法上屬於何種行政處分之「附款」（Collateral Clause）？",
        "choices": [
            ("A", "停止條件"),
            ("B", "負擔（Burden）"),
            ("C", "解除條件"),
            ("D", "保留行政處分之廢止權")
        ],
        "ans_text": "(B) 負擔（Burden）",
        "explanation": """<strong>【核心法條與附款種類辨析】</strong><br>
依《行政程序法》第 93 條第 2 項，行政處分得附加之附款種類：<br>
1. <strong>期限</strong>：始期或終期。<br>
2. <strong>條件</strong>：將處分效力繫於將來客觀不確定之事實（停止條件成就生效；解除條件成就不生效）。<br>
3. <strong>負擔（Burden / Auflage）</strong>：附加於授益行政處分之特定行為義務（要求相對人為一定之給付、作為或不作為）。許可證<strong>立即生效</strong>，但相對人負有後續定時申報數據之作為義務，故為典型之<strong>負擔</strong>。<br>
4. <strong>保留行政處分之廢止權</strong>。<br>
5. <strong>保留負擔之事後附加或變更</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A)(C) 錯誤</strong>：該許可證核發後立即生效，不因申報與否決定許可證是否開始生效或失效。<br>
‧ <strong>(B) 正確</strong>：課予相對人額外之行政作為義務，為標準負擔。<br>
‧ <strong>(D) 錯誤</strong>：機關並未註明保留廢止字樣。"""
    },
    {
        "ans": "C",
        "tag": "行政罰責任能力",
        "stem": "13 歲國中生甲與 17 歲高中生乙，兩人共同於公共資訊導覽機觸控螢幕上塗鴉噴漆破壞外觀，違反社會秩序維護法。主管機關擬依《行政罰法》（Administrative Penalty Act）進行裁罰，下列處置何者符合法律規定？",
        "choices": [
            ("A", "甲與乙均不予處罰"),
            ("B", "甲與乙均應依成年人標準全額處罰"),
            ("C", "甲未滿十四歲，不予處罰；乙十四歲以上未滿十八歲，得減輕處罰"),
            ("D", "甲處拘留三日，乙不予處罰")
        ],
        "ans_text": "(C) 甲未滿十四歲，不予處罰；乙十四歲以上未滿十八歲，得減輕處罰",
        "explanation": """<strong>【核心法條與責任年齡推導】</strong><br>
依《行政罰法》第 9 條之年齡責任能力級距：<br>
1. <strong>第 1 項（無責任能力）</strong>：<strong>未滿十四歲人之行為，不予處罰</strong>。故 13 歲之甲依法絕對不予處罰！<br>
2. <strong>第 2 項（限制責任能力）</strong>：<strong>十四歲以上未滿十八歲人之行為，得減輕處罰</strong>。故 17 歲之乙，行政機關得審酌其情節減輕處罰。<br>
3. <strong>第 3 項（精神障礙）</strong>：行為時因精神障礙致不能辨識行為違法者，不予處罰。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A)(B)(D) 均錯誤</strong>：違反行政罰法第 9 條之責任能力規定。<br>
‧ <strong>(C) 正確</strong>：完全合於行政罰法第 9 條第 1、2 項。"""
    },
    {
        "ans": "D",
        "tag": "刑法故意責任",
        "stem": "行為人甲明知某伺服器漏洞修補程式可能含有惡意後門勒索病毒程式碼，但為了搶先發布賺取獎金，抱持著「就算真的害別人電腦中毒癱瘓也無所謂、不在乎」之心理狀態而將其上傳公開。甲之主觀心態在刑法上屬於？",
        "choices": [
            ("A", "直接故意（確定故意）"),
            ("B", "無認識之過失"),
            ("C", "有認識之過失（自信其不發生）"),
            ("D", "間接故意（不確定故意 / 容認故意）")
        ],
        "ans_text": "(D) 間接故意（不確定故意 / 容認故意）",
        "explanation": """<strong>【核心法條與責任心態辨析】</strong><br>
依《刑法》第 13 條規定故意之兩種類型：<br>
1. <strong>第 1 項（直接故意 / 確定故意）</strong>：行為人對於構成犯罪之事實，明知並<strong>有意使其發生</strong>者（明知並積極欲其發生）。<br>
2. <strong>第 2 項（間接故意 / 不確定故意）</strong>：行為人對於構成犯罪之事實，預見其發生而<strong>其發生並不違背其本意</strong>者（預見可能發生，而抱持「發生也無所謂」之容認態度）。<br>
甲預見癱瘓風險，心態為「中毒也無所謂」，合於第 13 條第 2 項之<strong>間接故意</strong>。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：甲並非以癱瘓為積極唯一目的，非直接故意。<br>
‧ <strong>(B) 錯誤</strong>：甲已有預見，非無認識過失。<br>
‧ <strong>(C) 錯誤</strong>：有認識過失（刑法第 14 條第 2 項）係「確信其不發生」，甲是「發生也無所謂（容認）」，本質截然不同。<br>
‧ <strong>(D) 正確</strong>：間接故意之經典定義。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Dolous Eventualis (Recklessness / Indirect Intent)</code> <span class="en">Indirect Intent</span>：間接故意、不確定故意。"""
    },
    {
        "ans": "A",
        "tag": "憲法法庭判決效力",
        "stem": "依《憲法訴訟法》（Constitutional Procedure Act）第 38 條規定，憲法法庭裁判之法律效力，下列敘述何者<strong>錯誤</strong>？",
        "choices": [
            ("A", "憲法法庭宣告法規違憲之判決，僅對聲請人個案有效，對其他全國各級機關無拘束力"),
            ("B", "憲法法庭裁判有拘束各級法院、各級機關之效力，各機關並應依法貫徹執行"),
            ("C", "判決宣告法規即日起立即失效者，該法規自判決公告之日起失其效力"),
            ("D", "法規經宣告定期失效者，若立法院逾期未完成修法，自該期限屆滿之日起當然失其效力")
        ],
        "ans_text": "(A) 憲法法庭宣告法規違憲之判決，僅對聲請人個案有效，對其他全國各級機關無拘束力",
        "explanation": """<strong>【憲法訴訟法之對世效力】</strong><br>
依《憲法訴訟法》第 38 條第 1 項規定：「憲法法庭裁判有<strong>拘束全國各機關及各級法院之效力</strong>；各機關並應依判決意旨實現判決內容。」<br>
憲法法庭判決具備<strong>對世效力（Erga Omnes）</strong>，非僅侷限於聲請人當事人之間！宣告法規違憲失效者，具有等同法律廢止之普遍對世拘束力。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤（本題正解）</strong>：憲法法庭判決具有拘束全國各級機關之普遍對世拘束力，絕非僅個案拘束！<br>
‧ <strong>(B)(C)(D) 正確</strong>：均為憲法訴訟法第 38 條至第 52 條之明文規範。<br><br>
<strong>【英文專有名詞與中譯】</strong>：<br>
‧ <code>Erga Omnes</code> <span class="en">Erga Omnes</span>：對世效力、拘束所有人。<br>
‧ <code>Judicial Review</code> <span class="en">Judicial Review</span>：司法審查、違憲審查。"""
    },
    {
        "ans": "C",
        "tag": "勞動基準法",
        "stem": "資訊工程師與雇主簽訂勞動契約，合約約定「因資訊專案時程緊迫，勞工同意自願無條件拋棄勞動基準法所定之特別休假與加班費請求權」。依《勞動基準法》（Labor Standards Act）第 1 條規定，該約定條款之效力為何？",
        "choices": [
            ("A", "基於契約自由原則，該約定完全合法有效"),
            ("B", "只要勞工年薪高於新臺幣 150 萬元，該約定即行有效"),
            ("C", "勞動基準法為強行法規，約定低於勞基法最低標準之一律無效，仍應依法給付"),
            ("D", "該約定效力未定，需由勞動部部長親自核定")
        ],
        "ans_text": "(C) 勞動基準法為強行法規，約定低於勞基法最低標準之一律無效，仍應依法給付",
        "explanation": """<strong>【核心法條與強行法效力】</strong><br>
依《勞動基準法》第 1 條規定：「為規定勞動條件最低標準，保障勞工權益，加強勞雇關係，促進社會與經濟發展，特制定本法。<strong>雇主與勞工所訂勞動條件，不得低於本法所定之最低標準。</strong>」<br>
勞動基準法為保障經濟弱勢勞工之<strong>公序良俗強行法規</strong>。契約自由不得牴觸強行法（民法第 71 條）。契約約定預先拋棄加班費或特休者，該違反強行法之特約<strong>依法自始、當然、確定無效</strong>，雇主仍應全額給付加班費與特休。<br><br>
<strong>【各選項詳細辨析】</strong>：<br>
‧ <strong>(A) 錯誤</strong>：契約自由受強行法規範之限制，低於勞動基準法者無效。<br>
‧ <strong>(B) 錯誤</strong>：勞動基準法保障適用對象一律受最低保障拘束。<br>
‧ <strong>(C) 正確</strong>：勞動基準法之最低基準強行法效力。<br>
‧ <strong>(D) 錯誤</strong>：依法直接無效，非效力未定。"""
    }
]

