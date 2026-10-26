# -*- coding: utf-8 -*-
"""
3 Core TWSE Facility & Physical Security Simulation Essays (sec-essay-77 ~ sec-essay-79)
Covering:
1. 機房預防性維護（PM）、2N 不間斷電力設施與 VESDA 極早期火災預警 (sec-essay-77)
2. 外包駐點代打卡出勤舞弊之 ISO 27001 漏洞剖析、PAM 特權控管與實體閘門連動防禦 (sec-essay-78)
3. 關鍵基礎設施資料中心設備維護「營運不中斷（Availability）」與「廠務實體安全（Physical Security）」協同防禦架構 (sec-essay-79)
"""

def get_3_new_facility_essays():
    return [
        # 1. sec-essay-77: PM, UPS & VESDA in Data Center Physical Security
        {
            "id": "sec-essay-77",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "關鍵基礎設施資料中心預防性維護（PM）、UPS 電力和 VESDA 極早期火警之 ISO 27001 實體安全防護",
            "summary": "針對臺灣證券交易所國家核心關鍵基礎設施資料中心，依 ISO/IEC 27001:2022 實體控制項規範，深入解構預防性維護（PM）、2N 不間斷電力基礎設施（UPS/發電機/STS）與 VESDA 極早期煙霧感測火警之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO/IEC 27001:2022 實體控制項對應 (5分)；2. 預防性維護 (PM) 之變更管理與主動預警 (7分)；3. 2N 不間斷電力 (UPS/發電機/STS) 容錯架構 (7分)；4. 極早期火災預警 (VESDA) 四段警報與滅火聯防 (6分)",
            "question": "台灣證券交易所作為國家核心關鍵基礎設施，其資料中心（Data Center）必須符合 ISO/IEC 27001 之實體與環境安全規範。請依您的工程實務，說明如何針對機房建置「預防性維護（PM）」、「不間斷電力基礎設施」與「極早期火災預警系統（VESDA）」之資安防禦架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 實體安全標準</h4>
<p>臺灣證券交易所作為國家關鍵基礎設施（CI）與資安 A 級機關，核心交易系統可用性要求高達 99.999%（年停機時間小於 5.26 分鐘）。機房實體與環境安全是確保交易不中斷的第一道防線，嚴格對應 <strong>ISO/IEC 27001:2022 附錄 A 主題 7「實體控制項」</strong>：</p>
<ul>
  <li><strong>A.7.5 防範實體與環境威脅</strong>：保護機房免受火災、水患、地震與供電異常等物理破壞。</li>
  <li><strong>A.7.11 設備公用設施</strong>：確保電力、空調等支援設施具備冗餘，免於中斷威脅。</li>
  <li><strong>A.7.13 設備維護</strong>：落實定期維護，防止設備劣化引發無預警停擺。</li>
</ul>

<h4>二、三大核心基礎設施資安防衛架構重點剖析</h4>
<ul>
  <li><strong>1. 預防性維護 (PM, Preventive Maintenance)</strong>：
    <ul>
      <li><strong>制度基線與變更管理（A.7.13）</strong>：訂定嚴格年度、季、月 PM 維護計畫；任何維護皆須開立工單並通過變更審核（Change Management），一律限制於非交易時段（平日夜間或週末假日）執行。</li>
      <li><strong>實體與網路隔離</strong>：維護工程師禁用自攜隨身碟或筆電直連核心網路；專用維修筆電採實體唯讀/離線模式，USB 連接埠硬體封死，防範供應鏈木馬跳板植入。</li>
      <li><strong>預測性健康監測</strong>：導入 DCIM 智慧環控，針對伺服器風扇轉速、電容紋波、硬碟 S.M.A.R.T. 數值進行劣化趨勢分析，於平均故障間隔（MTBF）前主動預防性置換，杜絕突發斷線。</li>
    </ul>
  </li>
  <li><strong>2. 不間斷電力基礎設施 (UPS & Power Infrastructure)</strong>：
    <ul>
      <li><strong>2N 雙迴路全冗餘拓撲（A.7.11）</strong>：遵循 ANSI/TIA-942 Tier IV 容錯標準，建立 A/B 兩路完全實體隔離之供電路徑。引進台電雙不同變電所饋線，杜絕單點電網失效（SPOF）。</li>
      <li><strong>在線式雙轉換 UPS（Online Double Conversion）</strong>：零中斷切換時間（Transfer Time = 0ms）；電池組配置 BMS（電池管理系統）實時監控內阻與溫度；滿載續航 15~30 分鐘，支撐至柴油發電機順利併聯。</li>
      <li><strong>緊急柴油發電機與 ATS 自動切換</strong>：配置 N+1 或 2N 柴油發電機組，搭配 ATS（自動切換開關）於市電中斷後 10~15 秒內完成併聯發電；地下油槽常備 72 小時以上滿載連續運轉燃料，並簽訂緊急加油供油合約。</li>
      <li><strong>機櫃雙 PDU 與靜態轉換開關（STS）</strong>：伺服器全面採用雙電源供應器（Dual PSU）分接 A/B PDU；單電源網路設備則配置 STS（切換時間小於 4ms，無相位衝擊），保障端點永不瞬斷。</li>
    </ul>
  </li>
  <li><strong>3. 極早期火災預警系統 (VESDA, Very Early Smoke Detection Apparatus)</strong>：
    <ul>
      <li><strong>主動式微粒雷射偵測原理（A.7.5）</strong>：採主動抽氣式採樣管路（Air Sampling），利用高敏度雷射感測空氣中過熱物質裂解出的不可見微粒子，較傳統光電/離子煙霧探測器提早 2~4 小時發現電路板過熱異常。</li>
      <li><strong>四段式階梯告警機制</strong>：
        <ol>
          <li><strong>Alert（微粒初現）</strong>：機房 DCIM 儀表板提示，廠務人員攜帶熱像儀巡檢特定機櫃；</li>
          <li><strong>Action（濃度累積）</strong>：連動攝影機聚焦機櫃，降低空調送風擾流，廠務工程師現場警戒；</li>
          <li><strong>Fire 1（火警確認）</strong>：發出蜂鳴警報，連動 7x24 SOC 與機房主管手機；</li>
          <li><strong>Fire 2（火勢形成）</strong>：採雙迴路交叉確認（Cross-zone），啟動 30 秒倒數計時並釋放潔淨無毒氣體滅火劑（如 Novec 1230 / FM-200），不導電且不破壞伺服器硬碟磁頭，同時自動關閉防火風門。</li>
        </ol>
      </li>
    </ul>
  </li>
</ul>

<h4>三、實務整合運作：DCIM 與 SOC 智慧聯防閉環</h4>
<ol>
  <li><strong>DCIM 集中監控</strong>：全機房電力負載（PUE）、冷熱通道溫濕度矩陣、漏水檢測繩與 VESDA 煙霧濃度統合於單一儀表板，即時偵測異常。</li>
  <li><strong>資安監控中心（SOC）連動</strong>：實體環境告警與 SIEM/SOC 平台串接，將「電力異常、溫升超標、VESDA 警報」列為重大資安事件等級，確保廠務與 IT 團隊於 3 分鐘內啟動現場聯防應變。</li>
</ol>

<h4>四、結論</h4>
<p>關鍵基礎設施的資安防護不可偏廢實體環境。透過「PM 預測性維護固化設備生命週期」、「2N UPS 與柴油發電機確保零瞬斷供電」，以及「VESDA 早慧雷射偵測遏止電氣火災」，三者緊密構築 ISO 27001 實體與環境安全防線，為證交所撮合與行情系統提供固若金湯的運行環境。</p>
            """,
            "examinerTips": "評分採點關鍵字：『ISO/IEC 27001:2022 A.7.5 實體威脅、A.7.11 設備公用設施、A.7.13 設備維護』、『Tier IV 2N 雙迴路獨立供電、雙變電所饋線、在線式雙轉換 UPS (零切換0ms)、ATS 10~15秒柴油發電機 (72小時滿載儲油)、機櫃雙 PDU 與 STS (<4ms)』、『VESDA 主動抽氣式採樣、高敏雷射偵測提早2~4小時、Alert/Action/Fire1/Fire2 四段階梯告警、Cross-zone 雙迴路釋放 Novec 1230 / FM-200 潔淨氣體』、『PM 維護變更工單管理、離線維護終端防木馬、DCIM S.M.A.R.T./電容壽命趨勢分析』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>破題與 ISO 27001 控制項對照（5分）</strong>：精準引用 A.7.5、A.7.11、A.7.13，確立關鍵基礎設施實體防護標準與 99.999% 高可用要求。</li>
  <li><strong>預防性維護 PM 架構（7分）</strong>：涵蓋維護窗口、雙人覆核工單變更、離線專用設備防木馬跳板，以及 DCIM 預測性維護。</li>
  <li><strong>不間斷電力設施（7分）</strong>：完整回答 2N 雙迴路、在線式雙轉換 UPS、ATS 柴油發電機（72小時）、雙 PDU 與 STS 等工業級參數。</li>
  <li><strong>VESDA 極早期預警（6分）</strong>：條列主動微粒抽樣原理、Alert/Action/Fire1/Fire2 四段告警、雙迴路交會防誤噴與 Novec 1230 潔淨氣體聯動。</li>
</ul>
            """
        },

        # 2. sec-essay-78: Contractor Attendance Fraud, ISO 27001 Vulnerabilities & PAM / Gate Interlock
        {
            "id": "sec-essay-78",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "外包駐點代打卡出勤舞弊之 ISO 27001 漏洞剖析、PAM 特權控管與實體閘門連動防禦",
            "summary": "針對關鍵基礎設施外包駐點人員集體代打卡與偽造紙本簽名之資安危機，深入對照 ISO/IEC 27001:2022 控制項漏洞，並提出整合 PAM 特權帳號動態提權與防尾隨/反潛回實體閘門之雙向互鎖工程落地架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO/IEC 27001:2022 控制項漏洞剖析 (7分)；2. 出勤舞弊之本質資安風險分析 (4分)；3. 特權帳號管理 (PAM) 導入與 JIT 授權機制 (7分)；4. 實體進出閘門與 PAM 動態連動改善方案 (7分)",
            "question": "派駐於重要機關之外包駐點廠商（如廠務、IT維護人員），若發生集體使用個人代碼代打卡、或於紙本簽到表上偽造主管姓名以規避出勤稽核等情事，請依 ISO 27001 控制項說明該系統存在何種安全漏洞？應如何導入「特權帳號管理（PAM）」與「實體進出閘門連動機制」進行改善？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 控制項漏洞對照剖析</h4>
<p>外包駐點人員集體代打卡與紙本偽造簽名，表面為行政出勤舞弊，實質暴露出重大<strong>組織、人員、實體與系統存取控制潰敗</strong>。直接違反 ISO/IEC 27001:2022 以下控制項：</p>
<ul>
  <li><strong>A.5.19 供應商關係之資訊安全</strong>：缺乏對委外廠商駐點作業之履約稽核與現場實質監督機制。</li>
  <li><strong>A.6.2 僱用條款與條件</strong>：外包合約與駐點合約未落實資安違規懲戒條款，人員缺乏資安守法自律與法律拘束力。</li>
  <li><strong>A.7.2 實體進入控制</strong>：門禁系統僅採個人代碼或無防偽磁卡，缺乏身分唯一性驗證，無法防範代刷與冒用。</li>
  <li><strong>A.8.2 特權存取權限</strong>：未將外包人員特權帳號納管，導致「人未到場或未經授權者」仍能取得高階系統特權。</li>
  <li><strong>A.8.15 記錄保存（Logging）與 A.5.33 證據保護</strong>：紙本簽到簿易於塗改偽造，門禁日誌未受保護，喪失事後不可否認性（Non-repudiation）與鑑識稽核力。</li>
</ul>

<h4>二、出勤漏洞引發之核心資安威脅</h4>
<ul>
  <li><strong>1. 幽靈人員與責任空窗（Accountability Void）</strong>：虛假出勤導致重大故障或資安事件發生時，無法確認實際在場操作者，責任歸屬徹底失真。</li>
  <li><strong>2. 實體在場與邏輯特權脫鉤</strong>：外包工程師不在現場卻能在遠端私自登入伺服器，或未經核准之未授權人員隨意進出高敏感機房。</li>
  <li><strong>3. 內部人威脅與跳板攻擊</strong>：外包代碼共用造成權限擴散，極易被植入硬體側錄器或植入後門程式，演變為 APT 供應鏈跳板攻擊。</li>
</ul>

<h4>三、導入「特權帳號管理（PAM）」防護改善方案</h4>
<ol>
  <li><strong>全面收回常設特權（Zero Standing Privileges, ZSP）</strong>：
    全面收繳外包工程師之 Root、Administrator 與資料庫管理密碼，統一託管於 <strong>PAM 密碼保險箱（Credential Vault）</strong>；啟用每次使用後自動隨機輪替高強度密碼。
  </li>
  <li><strong>JIT（Just-In-Time）動態按需授權與工單綁定</strong>：
    外包人員操作前必須提出包含工單號碼（ITSM Ticket）之申請；PAM 僅於審批核准時段（如 14:00~16:00）派發短暫效期權杖（Ephemeral Token），工單逾時自動註銷連線。
  </li>
  <li><strong>四眼原則（Four-Eyes Principle）與連線即時側錄</strong>：
    外包人員登入特權作業必須經機關專責主管「即時線上覆核（Dual Control / Session Approval）」；連線過程全程進行指令記錄與螢幕錄影（OCR 檢索），遇到高危指令（如 <code>rm -rf</code>、<code>shutdown</code>）系統即時阻斷連線。
  </li>
</ol>

<h4>四、導入「實體進出閘門與 PAM 動態連動機制」</h4>
<ol>
  <li><strong>多因子生物辨識與防尾隨閘門（A.7.2）</strong>：
    全面淘汰單純鍵盤代碼或磁卡，進出機房升級為<strong>「高防偽人臉辨識（具活體檢測，防照片/影片）＋ 掌靜脈/指紋」</strong>；設置<strong>雙向互鎖防尾隨旋轉閘門（Speed Gate / Mantrap）</strong>，確保一人一刷，徹底杜絕代打卡。
  </li>
  <li><strong>強制啟用反潛回（Anti-Passback, APB）</strong>：
    門禁控制器啟用硬體嚴格反潛回機制：未刷入者嚴禁刷出，未刷出者無法再次刷入，完全防絕「代刷」與「卡片隔空傳遞」。
  </li>
  <li><strong>「人在權在、人走權銷」之實體與 PAM 智慧連動</strong>：
    <ul>
      <li><strong>實體驗證前置鎖</strong>：外包人員於 PAM 發起連線時，PAM 系統透過安全 API 即時檢驗實體門禁控制器。若該人員<strong>「過去 15 分鐘內無實體通過生物辨識閘門進入該機房之紀錄」</strong>，PAM 嚴格阻斷登入請求！</li>
      <li><strong>離場即時熔斷機制</strong>：外包人員於實體閘門刷卡離開機房時，門禁控制器立即發送事件至 PAM 系統，PAM <strong>瞬間強制中斷其作用中特權工作階段（Terminate Session）</strong>並鎖定帳號。</li>
    </ul>
  </li>
  <li><strong>全面廢除紙本簽到與日誌 WORM 固化</strong>：
    出勤與門禁數據全自動加密寫入 WORM（單寫多讀）不可篡改儲存設備並拋轉 SIEM；系統每日自動交叉比對「工單核准時段、門禁出入記錄、PAM 操作日誌」，一旦發現偏差自動告警並啟動違約重罰。
  </li>
</ol>

<h4>五、結論</h4>
<p>透過淘汰偽造紙本與弱代碼，導入「生物辨識防尾隨閘門」與「PAM 即時動態授權」，並達成「實體在場即特權生效、實體離場即特權收回」的軟硬雙向互鎖，從根源根絕代打卡舞弊，全面修復 ISO 27001 供應商與特權存取漏洞。</p>
            """,
            "examinerTips": "評分採點關鍵字：『ISO/IEC 27001:2022 控制項：A.5.19 供應商安全、A.6.2 僱用合約懲處、A.7.2 實體門禁、A.8.2 特權管理、A.8.15 記錄保存/不可否認性』、『出勤舞弊本質：幽靈人員/責任空窗、實體與邏輯存取脫鉤、內部人跳板威脅』、『PAM 方案：收繳常設密碼、Credential Vault 密碼保險箱、JIT 按需授權綁定 ITSM 工單、四眼原則雙人線上即時覆核、全工作階段螢幕錄影與高危指令阻斷』、『實體閘門連動：人臉活體辨識+掌靜脈、防尾隨旋轉閘門 (Mantrap)、硬體反潛回 (Anti-Passback)、人在權在 (門禁刷入方可解鎖 PAM)、人走權銷 (閘門刷出即強制中斷 Session)、廢除紙本導入 WORM 不可篡改稽核』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>ISO 27001 控制項漏洞剖析（7分）</strong>：精準指出 A.5.19（供應商關係）、A.6.2（合約條款）、A.7.2（實體門禁）、A.8.2（特權存取）、A.8.15（日誌與不可否認性）。</li>
  <li><strong>資安風險本質分析（4分）</strong>：點出幽靈人員責任真空、實體與邏輯脫鉤、內部人橫向滲透威脅。</li>
  <li><strong>特權帳號管理 PAM（7分）</strong>：詳述密碼保險箱、零常設特權（ZSP）、JIT 工單綁定、雙人即時覆核與會話錄影阻斷。</li>
  <li><strong>實體閘門與 PAM 連動機制（7分）</strong>：核心得分亮點在於「活體人臉+反潛回」與「實體在場前置校驗 + 離場即時中斷連線」雙向連動，徹底取代紙本偽造。</li>
</ul>
            """
        },

        # 3. sec-essay-79: Availability vs Physical Security in Core Trading Data Center
        {
            "id": "sec-essay-79",
            "category": "sec",
            "chapter": "第 11 章：業務營運持續（BCP）、高可用性與災難復原演練",
            "title": "關鍵基礎設施資料中心設備維護「營運不中斷（Availability）」與「廠務實體安全（Physical Security）」協同防禦架構",
            "summary": "針對臺灣證券交易所核心交易系統與資料中心機房，深入剖析如何依循 ISO/IEC 27001 規範，兼顧 7x24 設備維護「營運不中斷（Availability 99.999%）」與「廠務實體與環境安全（Physical Security）」之立體化協同架構。",
            "points": 25,
            "rubric": "1. 破題：可用性與實體安全之矛盾與法規要求 (5分)；2. 營運不中斷 (Availability) 高可用架構與並行維護實務 (7分)；3. 廠務實體與環境安全 (Physical Security) 分區與覆核管制 (7分)；4. DCIM 智慧環控連動與 BCP 全真演練驗證 (6分)",
            "question": "台灣證券交易所作為國家核心關鍵基礎設施，其資料中心（Data Center）之核心交易系統與實體機房，必須同時確保「設備維護之營運不中斷（Availability）」與「廠務實體與環境安全（Physical Security）」。請依據 ISO/IEC 27001 與關鍵基礎設施工程實務，說明應如何規劃整體防護架構，以在執行硬體變更與廠務維護時兼顧高可用性（HA）與實體資安管控？（25分）",
            "modelAnswer": """
<h4>一、破題：可用性（Availability）與實體安全（Physical Security）之矛盾與協同</h4>
<p>臺灣證券交易所肩負全市場撮合結算重責，核心系統服務中斷達 10 分鐘即屬法定重大資安事件，SLA 可用性承諾高達 99.999%（Five Nines，全年非預期停機小於 5.26 分鐘），RTO ≤ 10 分鐘，RPO = 0。</p>
<p>在工程實務上，<strong>「維護不中斷（Availability）」</strong>要求硬體故障更換、廠務水電檢修時系統必須無縫運轉；<strong>「實體安全（Physical Security）」</strong>則要求嚴密管制人員進入與硬體接觸，防範人為拔錯線路、惡意植入木馬或誤觸跳電。兩者常面臨「緊急修復搶修 vs 嚴格審核管制」之張力。唯有透過 <strong>ISO/IEC 27001:2022 控制項 A.7（實體）與 A.8（技術/冗餘維護）</strong>之結構化解耦，方能兼顧雙贏。</p>

<h4>二、確保設備維護「營運不中斷（Availability）」之工程架構</h4>
<ul>
  <li><strong>1. 廠務在線並行維護性（Concurrent Maintainability）</strong>：
    依據 Tier IV 容錯標準，機房電力與空調公用設施採 <strong>2N 雙迴路獨立拓撲（A.7.11）</strong>。配置雙變電所饋線、雙在線式 UPS、雙配電盤、雙冰水主機與 CRAC 空調管道。各迴路均具備實體旁路隔離閥，<strong>任一機組、管路或開關維修抽換時，皆無需中斷運算設備供電與冷卻</strong>。
  </li>
  <li><strong>2. 核心交易系統同城雙活與熱容錯（Active-Active HA, A.8.14）</strong>：
    <ul>
      <li>伺服器標配雙電源（Dual PSU）、雙網卡多路徑聚合（LACP/SR-IOV）與雙光纖 SAN 網狀通道（Dual Fabric），消滅單點故障。</li>
      <li>建置第一資料中心（1DC）與同城第二資料中心（2DC）雙活架構，透過專用 DWDM 光纖以微秒級延遲同步複製交易日誌（WAL Sync, RPO=0）。當任一伺服器或機櫃需下線維修時，透過<strong>無感平滑切換（Graceful Switchover）</strong>將撮合流量引導至備援節點，使用者下單零中斷。</li>
    </ul>
  </li>
  <li><strong>3. 分級維護變更窗口與自動回滾（Rollback Plan）</strong>：
    硬體更換與核心網路變更嚴格遵循變更管理程序（A.8.32），一律限定於「非交易時段（每日 15:30 後或週末盤後）」；變更工單必須內建回滾腳本，一旦驗證超時 15 分鐘未達基線，強制啟動倒退復原。
  </li>
</ul>

<h4>三、確保「廠務實體與環境安全（Physical Security）」之管制架構</h4>
<ul>
  <li><strong>1. 縱深防禦實體四層安全分區（Physical Security Perimeters, A.7.1）</strong>：
    <ol>
      <li><strong>外圍周界區</strong>：阻車柱、防衝撞圍籬、紅外線侵入感測器、車牌辨識；</li>
      <li><strong>建物進出區</strong>：警衛崗哨、訪客生物登記、X 光行李機與金屬探測門（防夾帶未授權儲存媒介）；</li>
      <li><strong>廠務動力區</strong>：發電機房、變電站、冷卻水塔專區，獨立雙因子進出查驗；</li>
      <li><strong>核心撮合機房與 HSM 密鑰室</strong>：高防偽人臉辨識+掌靜脈雙重鑑別、防尾隨艙（Mantrap）、無窗電磁屏蔽（TEMPEST 防護）。</li>
    </ol>
  </li>
  <li><strong>2. 廠務維護「雙人覆核同行」與智慧電子機櫃鎖（A.7.2 / A.7.13）</strong>：
    <ul>
      <li>外包工程師或廠務技師進入機房，必須全程由<strong>「證交所正職資安/系統人員 1 對 1 陪同（Dual Custody / Escort）」</strong>。</li>
      <li>機房所有伺服器機櫃全面安裝<strong>智慧電子鎖（Smart Rack Lock）</strong>，工單僅授權開啟特定編號機櫃，相鄰無關機櫃維持鎖定，徹底杜絕「拔錯光纖、誤觸電源」等人為維護災難。</li>
    </ul>
  </li>
</ul>

<h4>四、DCIM 智慧環控預警與 BCP 全真演練整合</h4>
<ol>
  <li><strong>DCIM 數位孿生與主動預警（A.7.5）</strong>：
    全機房冷熱通道溫濕度矩陣、漏水檢測繩、微差壓正壓防塵感測與 VESDA 極早期煙霧感測全面連動 DCIM 平台。當局部機櫃熱點升溫或微粒異動，系統於事故前 2 小時主動發出預警，自動調配備援風機降溫，變被動滅火為主動預防。
  </li>
  <li><strong>業務持續性（BCP）全真容錯演練（A.5.29 / A.5.30）</strong>：
    每季強制辦理無預警「市電斷電切換發電機實兵演練」，每年辦理「同城雙活資料中心全系統切換演習」，實測確認核心撮合 RTO ≤ 10 分鐘、RPO = 0，驗證在遭遇重大實體事故時仍能達成營運不中斷。
  </li>
</ol>

<h4>五、結論</h4>
<p>在國家核心關鍵基礎設施中，高可用性（Availability）必須建立在堅不可摧的實體與環境安全（Physical Security）基礎之上。藉由「Tier IV 2N 在線並行維護消除單點故障」、「四層實體分區與雙人機櫃電子鎖杜絕人為誤觸」，輔以「DCIM 智慧預警與同城雙活容錯」，證交所完美達成維護不停機與實體零漏洞之雙重使命。</p>
            """,
            "examinerTips": "評分採點關鍵字：『SLA 99.999% Five Nines (年停機<5.26分)、RTO≤10分、RPO=0、10分鐘中斷即屬重大資安事件』、『Tier IV 2N 並行維護性 (Concurrent Maintainability)、雙變電所饋線/雙在線式UPS/雙CRAC空調隔離閥、維護作業不中斷IT供電冷卻』、『系統雙活：雙電源/雙網卡聚合/雙Fabric、1DC與2DC同城雙活、DWDM微秒同步WAL日誌、平滑熱切換 (Graceful Switchover)』、『實體四層縱深分區：周界防撞柱、安檢X光機、廠務動力區、核心撮合與HSM無窗TEMPEST屏蔽』、『維護雙人覆核同行 (Dual Custody/Escort)、智慧機櫃電子鎖 (Smart Rack Lock 限開工單機櫃防拔錯線)』、『DCIM 智慧預警 + BCP 季市電斷電與年同城雙活災難切換實兵演練』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>破題與可用性/實體安全矛盾剖析（5分）</strong>：定義 99.999%、RTO ≤ 10分、RPO = 0 與 10 分鐘法定重大事件門檻，指出並行維護與實體接觸管制的平衡點。</li>
  <li><strong>營運不中斷 Availability 工程架構（7分）</strong>：詳述 Tier IV 2N 並行維護性（Bypass 閥門）、雙活資料庫微秒同步、雙網卡雙 Fabric 消除 SPOF 與離峰變更回滾機制。</li>
  <li><strong>廠務實體與環境安全 Physical Security（7分）</strong>：四層安全分區、TEMPEST 屏蔽、外包 1 對 1 陪同監護、智慧機櫃電子鎖（防止拔錯光纖/電源）。</li>
  <li><strong>DCIM 智慧預警與 BCP 演練（6分）</strong>：DCIM 主動預防、季度市電斷電切換發電機實兵演練與年度雙活切換驗證。</li>
</ul>
            """
        }
    ]
