# -*- coding: utf-8 -*-
"""
10 Core TWSE Facility, Physical Security & Supply Chain Simulation Essays (sec-essay-80 ~ sec-essay-89)
Designed according to the pattern of sec-essay-77 ~ sec-essay-79:
- Concise, bullet-pointed structure hitting 80%+ marks
- High real-world engineering fidelity for TWSE CI Data Center
- ISO/IEC 27001:2022 physical, environmental, supplier & technical controls

Essays:
1. sec-essay-80: 雙門互鎖安全艙（Mantrap Airlock）與活體雙生物辨識防尾隨
2. sec-essay-81: 精密空調冷卻（CRAC）、冷熱通道封閉與機房溫濕度防禦
3. sec-essay-82: 金融硬體安全模組（HSM）機房實體防拆、零化與 M-of-N 保管
4. sec-essay-83: 廢棄儲存媒體（HDD/SSD）實體銷毀、消磁與鏈式監管（Chain of Custody）
5. sec-essay-84: 實體網路佈線安全（Cabling Security）、暗纖維防竊聽與智慧配線架
6. sec-essay-85: 外包維護人員攜帶自攜設備（BYOD）與實體工具無塵隔離檢測區（Kiosk）
7. sec-essay-86: 頻外管理（OOB）實體氣隙隔離、IPMI/iLO 防護與防硬體木馬植入
8. sec-essay-87: 機房電磁脈衝防護（HEMP / TEMPEST）與高耐震剪力隔震工程架構
9. sec-essay-88: 廠務自動化（BMS/SCADA）與工控物聯網 Purdue 模型隔離與防竄改
10. sec-essay-89: 機房全時閉路電視（CCTV）、智慧 AI 視覺行為分析與即時聯防
"""

def get_10_new_facility_essays():
    return [
        # 1. sec-essay-80: Mantrap Airlock & Anti-Spoofing Biometrics
        {
            "id": "sec-essay-80",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "機房實體分區管制、防尾隨雙門互鎖安全艙（Mantrap）與活體雙生物辨識防禦架構",
            "summary": "針對國家核心關鍵基礎設施核心機房實體進入防護，依 ISO/IEC 27001:2022 A.7.1 與 A.7.2 規範，深度解構雙門互鎖安全艙（Mantrap）、重量感測地板、3D 結構光/紅外活體人臉與掌靜脈辨識之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001:2022 實體進入控制項對照 (5分)；2. 雙門互鎖安全艙 (Mantrap) 與重量感測機制 (7分)；3. 3D 活體人臉 + 掌靜脈雙生物辨識防偽架構 (7分)；4. 異常尾隨報警連動與稽核審計 (6分)",
            "question": "臺灣證券交易所核心交易機房實施實體周界防護，外來廠商常以「雙人跟隨（Tailgating/Piggybacking）」或以高畫質人臉相片、3D面具企圖規避查驗。請依 ISO/IEC 27001 之 A.7.1 實體安全邊界與 A.7.2 實體進入控制項，說明如何建置「雙門互鎖安全艙（Mantrap Airlock）」、「重量感測地板」與「活體雙生物辨識」之實體防禦架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 實體控制項對應</h4>
<p>臺灣證券交易所核心撮合與帳務機房為國家關鍵基礎設施（CI）核心禁區。人員實體滲透將直接威脅交易主機實體完整性。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.1（實體安全邊界）與 A.7.2（實體進入控制）</strong>，機房必須建構具備身分唯一性鑑別與防尾隨之實體縱深屏障。</p>

<h4>二、雙門互鎖安全艙（Mantrap Airlock）與防尾隨機制</h4>
<ul>
  <li><strong>雙門互鎖邏輯（Interlocking Door System）</strong>：
    安全艙設置外門（Door A）與內門（Door B），受微處理器硬體互鎖控制。平時雙門緊閉鎖死；外門刷卡驗證開啟後，人員進入艙體，外門完全關閉且磁吸鎖上鎖後，內門方能解鎖；<strong>任一時刻雙門嚴禁同時開啟</strong>，徹底阻斷氣流與尾隨者直通。
  </li>
  <li><strong>重量感測地板（Weight Sensing Floor）</strong>：
    安全艙地板內嵌高精度荷重感測器矩陣，<strong>設定單人體重容許公差區間（如 40kg~120kg，誤差 ±5kg）</strong>。若感測到總重量超標（如兩人同時擠入）或零負重異常，系統即刻發出警報並鎖死內門，啟動廣播要求非授權者退出。
  </li>
</ul>

<h4>三、活體雙生物辨識防偽鑑別架構</h4>
<ul>
  <li><strong>3D 結構光人臉辨識（防偽活體檢測）</strong>：
    捨棄傳統 2D 平面鏡頭，採用紅外線 3D 結構光鏡頭發射數萬個不可見光點，精確構建臉部深度三維模型；<strong>結合活體微表情與微血管紅外吸收光譜分析</strong>，徹底防禦高解析照片、動態平板影片與高仿真矽膠 3D 面具攻擊。
  </li>
  <li><strong>非接觸式掌靜脈辨識（Palm Vein Verification）</strong>：
    利用近紅外線（Near-Infrared）照射手掌，擷取皮下還原血紅素之獨特靜脈血管分佈紋理。掌靜脈為隱藏於人體內部之生物特徵，<strong>無殘留印痕且具備活體血流流動特徵</strong>，偽造機率近乎於零（FAR 錯誤接受率小於 0.00001%）。
  </li>
  <li><strong>人卡脈三因子動態綁定</strong>：
    外包人員進入安全艙時，必須同時出示「晶片身分工單卡」＋「3D 活體人臉」＋「掌靜脈」，三者特徵即時比對無誤，內門方予解鎖。
  </li>
</ul>

<h4>四、異常事件即時連動與稽核審計</h4>
<ol>
  <li><strong>安全艙逾時與強行破壞告警</strong>：人員於艙內停留超過設定時限（如 30 秒）或偵測到劇烈衝撞，門禁控制器立即觸發艙內警報並通報中控室警衛。</li>
  <li><strong>高畫質 CCTV 俯視抓拍</strong>：艙頂安裝魚眼俯視攝影機與前後視角攝影機，刷卡時自動連動錄影抓拍，影像加蓋時間戳記與 SHA-256 數位簽章存入 WORM 儲存設備，保留至少 180 天以供稽核。</li>
</ol>

<h4>五、結論</h4>
<p>結合雙門互鎖物理安全艙、單人重量感測地板與活體雙生物辨識技術，能於實體第一線徹底消滅代打卡、尾隨進場與冒用身分之安全死角，奠定關鍵基礎設施無懈可擊之實體進入防禦。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.1 實體邊界、A.7.2 實體進入控制』、『雙門互鎖安全艙 (Mantrap / Air-lock) 雙門永不同時開啟』、『單人重量感測地板 (40~120kg) 防雙人擠入』、『3D 結構光紅外活體人臉 (防照片/3D面具) + 掌靜脈辨識 (皮下還原血紅素/FAR<0.00001%)』、『人+卡+脈三因子綁定』、『逾時滯留警報、俯視攝影機抓拍與 WORM 180天稽核』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>ISO 27001 控制項對照（5分）</strong>：精準指出 A.7.1 與 A.7.2，確立核心機房邊界保護標準。</li>
  <li><strong>Mantrap 互鎖與重量感測（7分）</strong>：條列雙門互鎖硬體邏輯、重量公差與雙人擠入攔截機制。</li>
  <li><strong>活體雙生物辨識防偽（7分）</strong>：深入對比 3D 結構光防偽與掌靜脈血流特徵，說明三因子綁定。</li>
  <li><strong>告警連動與審計（6分）</strong>：逾時強制告警、CCTV 抓拍與不可篡改存儲閉環。</li>
</ul>
            """
        },

        # 2. sec-essay-81: Precision Cooling (CRAC), Hot/Cold Aisle Containment & Environmental Defense
        {
            "id": "sec-essay-81",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "資料中心精密空調（CRAC）、冷熱通道氣流封閉與機房溫濕度極限資安防禦架構",
            "summary": "針對臺灣證券交易所高密度刀鋒伺服器與低延遲撮合叢集，依 ISO/IEC 27001:2022 A.7.5 與 A.7.11 規範，深入解析 N+1/2N 精密空調（CRAC）、冷熱通道完全封閉、ASHRAE 溫濕度基線與自動降載熱熔斷之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 實體與環境威脅對應 (5分)；2. N+1/2N 精密空調 (CRAC) 雙迴路冗餘架構 (7分)；3. 冷熱通道實體封閉 (HAC/CAC) 與 ASHRAE 環境參數 (7分)；4. 散熱失效時系統分級降載與熱熔斷 (Thermal Throttling) (6分)",
            "question": "臺灣證券交易所高密度刀鋒伺服器與運算叢集散熱負載龐大，環境高溫或極度乾燥將直接引發晶片過熱降頻或靜電（ESD）硬體燒毀。請依 ISO/IEC 27001 之 A.7.5 防範實體與環境威脅及 A.7.11 設備公用設施，說明如何建置「N+1 / 2N 精密空調（CRAC）」、「冷熱通道氣流封閉」與「溫濕度資安監控暨自動降載熱熔斷」架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 實體與環境威脅對照</h4>
<p>高密度金融交易伺服器晶片功耗極高，散熱中斷數分鐘即可導致機櫃溫度飆破 50°C，引發伺服器熱當機或硬體永久損毀；極度乾燥則誘發靜電放電（ESD）擊穿精密晶片。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.5（實體與環境威脅防禦）與 A.7.11（設備公用設施）</strong>，機房必須將冷卻系統視為核心資安基礎設施。</p>

<h4>二、N+1 / 2N 精密空調（CRAC/CRAH）雙迴路冗餘架構</h4>
<ul>
  <li><strong>雙管路冰水主機與 2N 精密空調配置</strong>：
    採用雙獨立冰水管路（Dual Chilled Water Loop）與環狀配管，任何單一冰水主機或水泵故障維修時，具備自動切換隔離閥（Automatic Isolation Valves）；機房內部配置 N+1 或 2N 列間空調（In-Row Cooling）與下吹式電腦機房空調（CRAC）。
  </li>
  <li><strong>無瞬斷供電連動（UPS 支撐風機）</strong>：
    精密空調之送風機與電控系統全面接入在線式雙轉換 UPS，市電中斷時風機持續旋轉（維持氣流循環零中斷），水泵與冰水主機於 10~15 秒內由緊急柴油發電機順利接手供電。
  </li>
</ul>

<h4>三、冷熱通道實體封閉（Containment）與 ASHRAE 標準參數</h4>
<ul>
  <li><strong>冷通道封閉（Cold Aisle Containment, CAC）</strong>：
    機櫃面對面排列，於冷通道上方安裝阻燃防爆天花板，兩端裝設自動關閉推拉門，將低溫冷氣完全鎖定於冷通道；<strong>徹底杜絕冷熱氣流混風（Mixing）與氣流短路</strong>，使 PUE（電力使用效率）降至 1.3 以下。
  </li>
  <li><strong>嚴格落實 ASHRAE TC 9.9 環境控制基線</strong>：
    <ul>
      <li><strong>伺服器進氣溫度</strong>：維持在 <strong>18°C ~ 27°C</strong>（建議值 22°C ± 1°C）。</li>
      <li><strong>相對濕度（RH）</strong>：維持在 <strong>40% ~ 60% RH</strong>（露點溫度 5.5°C ~ 15°C）；濕度過低引發靜電（ESD），過高引發金屬針腳凝結水氣短路與離子遷移腐蝕。</li>
      <li><strong>微正壓防塵控制</strong>：機房室內維持 <strong>10 ~ 15 Pa 微正壓</strong>，防範室外粉塵與腐蝕性氣體（如硫化物）經縫隙滲入。</li>
    </ul>
  </li>
</ul>

<h4>四、散熱失效時系統分級降載與熱熔斷（Thermal Throttling）</h4>
<ol>
  <li><strong>冷熱通道溫濕度矩陣監控（DCIM 連動）</strong>：每個機櫃配置上、中、下三層溫度感測器，結合熱成像攝影機實時建構 3D 溫度場。</li>
  <li><strong>三階段自動防禦應變機制</strong>：
    <ul>
      <li><strong>第一階段（局部超溫 28°C）</strong>：自動將備援空調風機轉速拉升至 100%，並由 DCIM 推播預警至廠務工程師；</li>
      <li><strong>第二階段（警示高溫 32°C）</strong>：自動啟動虛擬化與容器動態遷移（vMotion / K8s Drain），將運算負載調度至冷卻充裕之同城雙活機房節點；</li>
      <li><strong>第三階段（致命高溫 38°C 熱熔斷）</strong>：觸發預警性關機（Graceful Shutdown），依序終止次要報表系統、降載非核心節點，保全核心撮合主機晶片免於物理燒毀。</li>
    </ul>
  </li>
</ol>

<h4>五、結論</h4>
<p>精密冷卻不僅是廠務工程，更是守護系統可用性（Availability）的核心防線。透過 2N 空調冗餘、冷通道實體氣流封閉與熱熔斷分級調度，證交所能自硬體物理底層杜絕過熱中斷，確保核心撮合交易全天候磐石運轉。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.5 實體環境威脅、A.7.11 公用設施』、『2N 雙迴路冰水管路 + N+1 列間空調 (In-Row/CRAC)』、『冷通道封閉 (Cold Aisle Containment, CAC) 防混風、PUE < 1.3』、『ASHRAE TC 9.9 基線：進氣 18~27°C、濕度 40~60% RH (防靜電 ESD 與凝結短路)、機房微正壓 10~15 Pa』、『散熱失效熱熔斷 (Thermal Throttling)：28°C風機全開、32°C負載跨機房遷移、38°C分級關機保全』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準控制項對照（5分）</strong>：引用 A.7.5 與 A.7.11，闡明高密度機房散熱與靜電防禦重要性。</li>
  <li><strong>CRAC 雙迴路冗餘（7分）</strong>：冰水環網、隔離閥、UPS 支撐風機持續轉動等高可用參數。</li>
  <li><strong>氣流封閉與 ASHRAE 指標（7分）</strong>：冷通道封閉原理、溫濕度數值、微正壓防塵防硫化。</li>
  <li><strong>自動降載與熱熔斷機制（6分）</strong>：三階段梯度降載遷移與晶片防燒毀保護。</li>
</ul>
            """
        },

        # 3. sec-essay-82: HSM Physical Security, FIPS 140-3 Zeroization & M-of-N Key Custody
        {
            "id": "sec-essay-82",
            "category": "sec",
            "chapter": "第 3 章：密碼學原理、硬體安全模組（HSM）與 PKI 憑證",
            "title": "金融硬體安全模組（HSM）機房實體防拆、FIPS 140-3 零化與 M-of-N 實體金鑰保管架構",
            "summary": "針對臺灣證券交易所核心交易憑證簽章與密鑰保全，依 ISO/IEC 27001:2022 A.7.3、A.7.4 與 A.8.24 規範，深度解構 FIPS 140-3 Level 3/4 實體防拆阻抗、主動零化（Zeroization）及 M-of-N 雙人實體金鑰保險箱保管之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 實體密鑰安全控制項對應 (5分)；2. FIPS 140-3 Level 3/4 實體防篡改與封裝防禦 (7分)；3. 實體入侵偵測與主動式零化 (Active Zeroization) (7分)；4. M-of-N 秘密分享實體智慧卡雙人保全與異地保險箱制度 (6分)",
            "question": "臺灣證券交易所核心交易憑證簽章與金融結算高度仰賴硬體安全模組（HSM）。若遭未授權人員實體拆卸、鑽孔探測或側信道攻擊，將導致根金鑰外洩之滅頂之災。請依 ISO/IEC 27001 規範，申論金融 HSM 實體防護規範、FIPS 140-3 實體防拆阻抗與主動零化（Zeroization）原理，以及如何落實實體金鑰智慧卡之 M-of-N 雙人控管與異地保管？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 控制項對照</h4>
<p>金融硬體安全模組（HSM）儲存證交所最高等級之根簽章金鑰（Root CA）與下單驗章私鑰，是金融密碼學信任錨點。一旦實體遭接觸入侵，所有軟體防護將蕩然無存。遵循 <strong>ISO/IEC 27001:2022 控制項 A.7.3（保護機敏區域安全）、A.7.4（實體安全監控）與 A.8.24（密碼技術的使用）</strong>，HSM 必須實施極致實體防護。</p>

<h4>二、FIPS 140-3 Level 3/4 實體防拆阻抗與封裝架構</h4>
<ul>
  <li><strong>實體防拆外殼與環氧樹脂灌封（Potting）</strong>：
    HSM 核心加密處理器與易失性 RAM 被完全封裝於<strong>高硬度不透明環氧樹脂（Epoxy Resin）</strong>中。內部嵌有精密導電柵網（Conductive Mesh Matrix），任何試圖透過化學溶劑溶解、機械銑削、雷射切割或探針微鑽孔的行為，皆會改變導電柵網阻抗或截斷電路。
  </li>
  <li><strong>防開蓋微動開關與防篡改封條（Tamper-Evident Seals）</strong>：
    外殼接縫處配置防破壞微動開關（Microswitches）與光敏電晶體（Photo-sensors）；機殼外部黏貼具備全像攝影與撕毀即浮現「VOID」字樣之防偽安全封條，任何未經授權之外殼開啟皆留下不可逆物理痕跡。
  </li>
</ul>

<h4>三、實體環境異常感測與主動式零化（Active Zeroization）</h4>
<ul>
  <li><strong>全方位物理環境感測器</strong>：
    HSM 內建高精度感測矩陣，全時監控：
    <ol>
      <li><strong>溫度感測</strong>：防範液態氮極低溫冷凍攻擊（Cold Boot Attack）或高溫破壞；</li>
      <li><strong>電壓與時脈頻率感測</strong>：防範電壓突波注入故障攻擊（Fault Injection）；</li>
      <li><strong>光線感測器</strong>：外殼一旦破裂透光瞬間觸發。</li>
    </ol>
  </li>
  <li><strong>主動零化機制（Active Zeroization Circuit）</strong>：
    內部配備獨立專用備用電池與快速放電電容。一旦偵測到實體入侵、外殼被開或環境異常，<strong>系統在微秒級（µs）時間內切斷主金鑰 RAM 供電並強制反向接地放電</strong>，徹底清除金鑰位元，保證金鑰化為虛無，杜絕任何實體逆向還原。
  </li>
</ul>

<h4>四、M-of-N 秘密分享實體智慧卡雙人保全與保管架構</h4>
<ol>
  <li><strong>Shamir 門檻秘密分享（Threshold Secret Sharing）</strong>：
    HSM 管理與金鑰復原權限拆分為 <strong>N 張高安全性接觸式智慧卡（Smart Cards），設定門檻值為 M（如 3-of-5）</strong>；任何單一管理員持有之卡片不含任何完整金鑰資訊，必須至少 M 位授權人同時在場插入卡片並輸入個人 PIN 碼方能解鎖 HSM 管理權限。
  </li>
  <li><strong>雙人四眼原則與專屬籠式屏蔽機櫃（Cage）</strong>：
    HSM 伺服器獨立置於機房內部之<strong>「雙鎖金屬籠式機櫃（Caged Rack）」</strong>內，外層金屬門與機櫃門皆需兩位不同正職主管各自持有之實體鑰匙與門禁卡同時刷卡方能開啟；作業全程由雙人相互監督並受高清特寫鏡頭 360 度錄影。
  </li>
  <li><strong>異地防磁防火防核保險箱保管</strong>：
    智慧卡分裝於特製防靜電、防磁、防輻射之金屬封籤袋內，分別存放於第一資料中心與異地第二資料中心之<strong>頂級防盜防火保險箱（符合 UL 687 標準）</strong>，每季強制啟動實體封條盤點覆核。
  </li>
</ol>

<h4>五、結論</h4>
<p>結合 FIPS 140-3 物理防拆灌封、主動零化熔斷機制與 M-of-N 雙人實體金鑰分散保管，證交所為核心交易密鑰築起了物理與數學雙重護城河，確保金融信任核心不受任何實體攻破。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.3 機敏區域、A.7.4 實體監控、A.8.24 密碼控制』、『FIPS 140-3 Level 3/4 不透明環氧樹脂灌封 + 導電柵網 (Conductive Mesh)』、『防開蓋微動開關 + Tamper-evident VOID 防偽封條』、『全方位感測器：冷凍溫度/電壓故障注入/光敏』、『微秒級主動零化 (Active Zeroization) 電容放電徹底清除密鑰』、『M-of-N (如 3-of-5) 智慧卡門檻秘密分享』、『雙人雙鎖金屬籠式機櫃 (Caged Rack) + 異地防磁防火保險箱』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>控制項標準對照（5分）</strong>：引用 A.7.3、A.7.4、A.8.24 與 FIPS 140-3，確立密碼模組實體防禦位階。</li>
  <li><strong>FIPS 140-3 實體封裝防拆（7分）</strong>：環氧樹脂灌封、內部導電網、防開蓋微開關與實體封條。</li>
  <li><strong>感測器與主動零化（7分）</strong>：溫度/電壓/光敏防側信道故障注入，微秒級主動放電零化原理。</li>
  <li><strong>M-of-N 與保險箱雙人保管（6分）</strong>：門檻秘密分享、籠式雙鎖機櫃與異地防火保險箱管理。</li>
</ul>
            """
        },

        # 4. sec-essay-83: Storage Media Disposal, Degaussing & Chain of Custody
        {
            "id": "sec-essay-83",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "機房退役硬碟實體銷毀、消磁清除非密碼化與全流程鏈式監管（Chain of Custody）",
            "summary": "針對臺灣證券交易所除役儲存媒體（HDD/SSD）之報廢除役，依 ISO/IEC 27001:2022 A.7.10 與 NIST SP 800-88 R1 規範，深入剖析消磁（Degaussing）、物理粉碎（Shredding）與全程錄影監銷之鏈式監管（Chain of Custody）80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 媒體處置控制項對照 (5分)；2. NIST SP 800-88 媒體清除等級與 HDD/SSD 銷毀技術 (7分)；3. 實體銷毀作業鏈式監管 (Chain of Custody) 全流程 (7分)；4. 銷毀證明防偽、資產下線除籍與審計閉環 (6分)",
            "question": "證交所伺服器淘汰或退役之硬碟（HDD/SSD）可能殘留大量機敏委託記錄與投資人個資。外包廠商清運時若發生抽換掉包或未徹底銷毀，將引發嚴重資料外洩。請依 ISO/IEC 27001 之 A.7.10 儲存媒體之處置與 NIST SP 800-88 媒體清除指引，說明如何建立儲存硬碟實體銷毀機制，並規劃全程「鏈式監管（Chain of Custody）」防禦體系？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 儲存媒體處置標準</h4>
<p>金融伺服器與全快閃陣列（AFA）退役之硬碟含有海量撮合記錄、證券帳號與交易日誌。若僅使用邏輯格式化（Format），資料極易透過專業鑑識工具還原。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.10（儲存媒體之處置）</strong>，媒體報廢處置必須確保資料達<strong>不可逆之永久毀滅</strong>。</p>

<h4>二、NIST SP 800-88 R1 媒體清除等級與銷毀技術規範</h4>
<p>依據 NIST SP 800-88 Rev. 1 指引，清除層級分為 Clear（清除）、Purge（淨化）與 <strong>Destroy（銷毀，最高層級）</strong>。證交所機敏硬碟一律採「Purge + Destroy」雙重程序：</p>
<ul>
  <li><strong>1. 磁性硬碟（HDD）：高強度消磁（Degaussing）＋ 物理粉碎</strong>：
    <ul>
      <li><strong>強力脈衝消磁</strong>：使用通過 NSA/CSS 認證之消磁機，產生高達 <strong>10,000 高斯（Gauss / 1 Tesla 以上）</strong>之強烈瞬態磁場，破壞磁軌伺服標記（Servo Tracks）與磁疇方向，使其物理性無法再定址。</li>
      <li><strong>機械物理破碎</strong>：消磁後直接送入工業碎裂機，<strong>將碟片粉碎成顆粒小於 2mm 之金屬碎屑</strong>，徹底根除磁力顯微鏡（MFM）實驗室讀取可能。</li>
    </ul>
  </li>
  <li><strong>2. 固態硬碟（SSD / NVMe）：加密清除（Crypto Erase）＋ 顆粒物理穿刺破碎</strong>：
    SSD 快閃記憶體（NAND Flash）不具磁性，消磁完全無效！必須執行：
    <ul>
      <li><strong>ATA Secure Erase / NVMe Format（Crypto Erase）</strong>：覆寫並銷毀 SSD 控制器內部之 AES-256 媒體加密金鑰（MEK）；</li>
      <li><strong>微針多點多重穿刺或專用快閃晶片粉碎機</strong>：將 SSD 電路板上所有 NAND Flash 快閃記憶體顆粒進行<strong>物理折斷、多孔衝壓穿刺並粉碎至小於 2mm 碎塊</strong>。</li>
    </ul>
  </li>
</ul>

<h4>三、實體銷毀「鏈式監管（Chain of Custody）」全流程管控</h4>
<ol>
  <li><strong>步驟一：機櫃拆卸與序號一維/二維條碼登記（A.5.9 盤點）</strong>：
    硬碟自機櫃拔除前，雙人覆核掃描硬碟序號（Serial Number）、WWN 與機櫃槽位，系統即刻將資產狀態標註為「待銷毀」，貼上防撕毀追蹤條碼。
  </li>
  <li><strong>步驟二：防撬保密防護箱暫存（Dual Custody）</strong>：
    拆下之硬碟置入特製金屬防撬運送箱，箱體加封<strong>具備獨立編號之一次性鋼絲封條（Tamper-Evident Cable Seal）</strong>；暫存於機房獨立受控防盜保險室內。
  </li>
  <li><strong>步驟三：廠內現地銷毀（On-Site Destruction 原則）</strong>：
    <strong>嚴禁硬碟運出證交所建築體外銷毀！</strong>由外包合格銷毀廠商將專業移動式消磁粉碎車開抵證交所安全管制區，於機關內部現地執行。
  </li>
  <li><strong>步驟四：證交所專責人員全時監銷與 360 度錄影</strong>：
    銷毀全程由證交所資安人員與政風/稽核人員<strong>「全程在場監銷（Witness）」</strong>；專用攝影機全程特寫錄影記錄「掃描序號 → 投入消磁機 → 進入粉碎機出料」連續畫面，影像無中斷剪接。
  </li>
</ol>

<h4>四、銷毀證明防偽、資產除籍與審計閉環</h4>
<ul>
  <li><strong>不可篡改銷毀憑證（Certificate of Destruction）</strong>：外包廠商交付之銷毀清冊必須逐一載明硬碟廠牌、型號、出廠序號、消磁高斯讀數、粉碎時間與監銷主管簽章，並將清單哈希值（SHA-256）與錄影封裝存檔。</li>
  <li><strong>ITAM 資產系統自動下線除籍</strong>：CMDB 系統將該批序號狀態自動變更為「已實體銷毀」，稽核軌跡寫入 WORM 儲存設備，終身可追溯。</li>
</ul>

<h4>五、結論</h4>
<p>儲存媒體報廢是資訊生命週期的終局戰場。透過「HDD消磁+物理粉碎」、「SSD顆粒穿刺破壞」與「嚴格現地鏈式監管（Chain of Custody）」，徹底根絕硬碟外流掉包風險，圓滿達成 ISO 27001 媒體處置合規要求。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.10 媒體處置、NIST SP 800-88 R1 Destroy 級別』、『HDD：>10,000 高斯脈衝消磁 (Degaussing) 破壞 Servo Track + 碎屑 < 2mm 物理粉碎』、『SSD：消磁無效！需 ATA Crypto Erase 銷毀 MEK 金鑰 + NAND 顆粒多點穿刺粉碎至 < 2mm』、『鏈式監管 (Chain of Custody)：雙人序號條碼登記、鋼絲封條防撬箱、嚴格現地銷毀 (On-Site，禁運出廠外)』、『正職雙人全程在場監銷 + 360度錄影無剪接 + 防偽 Certificate of Destruction + WORM 存檔』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準依據（5分）</strong>：引用 ISO 27001 A.7.10 與 NIST SP 800-88 R1 Destroy 最高規範。</li>
  <li><strong>HDD vs SSD 銷毀技術差異（7分）</strong>：精準點出 HDD 消磁參數（10,000高斯）與 SSD 消磁無效需顆粒穿刺粉碎之技術核心。</li>
  <li><strong>鏈式監管全流程（7分）</strong>：序號掃描、防撬箱、嚴格現地銷毀、雙人現場監銷錄影。</li>
  <li><strong>證明憑證與資產除籍（6分）</strong>：銷毀證明書載明序號、CMDB 自動除籍與 WORM 留存。</li>
</ul>
            """
        },

        # 5. sec-essay-84: Cabling Security, Dark Fiber Anti-Tapping & Smart Patch Panels
        {
            "id": "sec-essay-84", # correct ID
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "實體網路佈線安全（Cabling Security）、暗纖維防竊聽與智慧配線架（AIM）防禦架構",
            "summary": "針對證券撮合機房內外大量光纖與雙絞線之實體竊聽威脅，依 ISO/IEC 27001:2022 A.7.12 規範，深度解構封閉金屬導管、光時域反射儀（OTDR）微光衰告警、MACsec 線路加密與智慧配線架（AIM）之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 佈線安全控制項對應 (5分)；2. 光纖實體竊聽 (Optical Tapping) 原理與防護 (7分)；3. 機房內實體線槽、暗管與智慧配線架 (AIM) 規範 (7分)；4. OTDR 即時監控與底層線路加密 (MACsec) 整合 (6分)",
            "question": "高頻交易與撮合機房內外佈建海量萬兆光纖。若外包維護人員或攻擊者於線槽私接分流器（Network TAP）或利用光纖彎曲微漏光技術（Optical Fiber Tapping）暗中竊聽交易封包，軟體防火牆將完全無法察覺。請依 ISO/IEC 27001 之 A.7.12 佈線安全規範，說明如何針對「主幹暗纖（Dark Fiber）」與「機房配線架」建置防實體竊聽、OTDR 即時預警與智慧配線管理架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 佈線安全控制項對照</h4>
<p>在超低延遲證券交易環境中，光纖通訊直接傳遞 FIX 交易委託單與即時行情。攻擊者可利用極微小的物理介入側錄明文數據。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.12（佈線安全）</strong>，傳輸電力或資料之電信線路必須施加防範攔截、竄改或損壞之實體與技術保護。</p>

<h4>二、光纖實體竊聽（Optical Fiber Tapping）攻擊原理與威脅</h4>
<ul>
  <li><strong>微彎曲漏光竊聽（Macro-bending Tapping）</strong>：
    攻擊者將光纖保護套剝除，使裸纖產生特定微小曲率彎曲，使內部傳導的光訊號部分自纖芯折射洩漏至外層包層；再利用高靈敏度光電感測夾頭（Clip-on Coupler）擷取洩漏光子，<strong>在「不斷纖、不中斷通訊」情況下竊取交易封包</strong>。
  </li>
  <li><strong>未授權分光器（Optical Splitter / TAP）接入</strong>：
    外包人員假借維護名義，於配線架（Patch Panel）背後偷接 99:1 或 90:10 實體分光鏡，將主幹線路流量靜默複製鏡像至旁路側錄設備。
  </li>
</ul>

<h4>三、機房內部實體管線與智慧配線架（AIM）防禦架構</h4>
<ul>
  <li><strong>封閉金屬導管與開放式高架線槽（A.7.12）</strong>：
    <ul>
      <li><strong>廢除隱蔽暗線</strong>：全面揚棄高架地板下方盲目走線，改採<strong>「天花板懸吊式開放金屬網狀橋架（Wire Mesh Tray）」</strong>，所有線纜走向一覽無遺，任何外掛掛載設備（如偽造 TAP）立即可見。</li>
      <li><strong>實體金屬防護管（Rigid Steel Conduit）</strong>：跨機房、穿越公共區域或引進外線之主幹光纜，強制穿入厚鋼管（RMC）並灌膠封裝，任何電鑽破壞即刻發出警報。</li>
    </ul>
  </li>
  <li><strong>智慧自動化基礎設施管理配線架（AIM / Smart Patch Panel）</strong>：
    採用符合 ISO/IEC 18598 標準之智慧配線架。<strong>RJ45 與 LC 光纖接頭內建微感應接觸針腳與 RFID 標籤</strong>。一旦有人拔出跳線、私插跳線或跨接非核准連接埠，系統於 1 秒內自動觸發實體告警，連動攝影機變焦錄影。
  </li>
</ul>

<h4>四、OTDR 即時在線監測與線路層 MACsec 硬體加密</h4>
<ol>
  <li><strong>光時域反射儀（OTDR）在線即時監控</strong>：
    於主幹暗纖維（Dark Fiber）部署<strong>在線式 OTDR 監測系統</strong>（利用非工作波長如 1625nm/1650nm 在線發送偵測脈衝）。當光纖遭受微彎曲竊聽導致<strong>光功率微幅衰減超過閾值（如 ΔLoss ≥ 0.1 ~ 0.2 dB）</strong>或反射波形異常時，系統於數秒內發出入侵警報並精確定位至「公尺級（±1m）」實體座標。
  </li>
  <li><strong>底層線路硬體加密（IEEE 802.1AE MACsec / DWDM 物理加密）</strong>：
    即便光纖遭竊聽，為確保資料機密性，於交換機間全面啟用 <strong>MACsec（AES-256-GCM 硬體線速加密）</strong>；在 DWDM 光傳輸設備端啟用光層加密（OTN Layer 1 Encryption）。攻擊者即使成功截獲洩漏光子，亦僅能取得毫無意義之密文亂碼。
  </li>
</ol>

<h4>五、結論</h4>
<p>佈線安全是網路拓撲的物理神經。結合「開放可視線槽與封閉鋼管」、「智慧配線架即時防插拔」、「OTDR 微光衰公尺級定位」與「底層 MACsec 硬體加密」，構建從物理層至鏈結層之銅牆鐵壁，徹底封死光纖竊聽漏洞。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.12 佈線安全』、『光纖微彎漏光竊聽 (Macro-bending Tapping / Clip-on Coupler) 與惡意分光器 (Splitter/TAP)』、『天花板開放式金屬網狀橋架 (可視化防私接) + 跨區厚鋼管 (Rigid Steel Conduit)』、『智慧配線架 (AIM, ISO/IEC 18598) 感應接腳/RFID 實時防私插拔』、『在線式 OTDR (1625nm) 微光衰感測 (ΔLoss ≥ 0.1~0.2 dB 觸發公尺級定位)』、『底層線速加密：IEEE 802.1AE MACsec (AES-256-GCM) + DWDM L1 加密』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準控制項依據（5分）</strong>：引用 A.7.12，指出物理竊聽非軟體防火牆可防之嚴峻性。</li>
  <li><strong>光纖竊聽攻擊原理（7分）</strong>：條列微彎曲漏光與旁路分光器偷接之技術機制。</li>
  <li><strong>機房線槽與智慧配線架（7分）</strong>：開放式網狀線槽消除盲區、智慧 AIM 瞬態偵測拔線插線。</li>
  <li><strong>OTDR 與底層加密聯防（6分）</strong>：在線 OTDR 監測 0.1dB 光衰精準定位，以及 MACsec 線速加密確保截獲無效。</li>
</ul>
            """
        },

        # 6. sec-essay-85: Quarantine Kiosk for Contractor BYOD & Maintenance Tools
        {
            "id": "sec-essay-85",
            "category": "sec",
            "chapter": "第 4 章：零信任架構（ZTA）、身分鑑別與特權存取管理",
            "title": "外包維護自攜設備（BYOD）與維護隨身碟之「無塵隔離檢測區（Quarantine Kiosk）」防禦架構",
            "summary": "針對維護廠商筆電、隨身碟攜入核心機房引發之 Stuxnet 式氣隙感染威脅，依 ISO/IEC 27001:2022 A.7.9 與 A.8.19 規範，深度解構實體隔離安檢亭（Security Kiosk）、CDR 內容重組、單向資料光閘與雷射易碎封條管制之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 攜離與自攜設備控制項對照 (5分)；2. 隨身碟與外來維護筆電之物理跳板威脅剖析 (4分)；3. 無塵隔離安檢亭 (Security Kiosk) 與 CDR 資料清洗機制 (8分)；4. 攜入設備實體白名單資產管制與硬體封緘 (8分)",
            "question": "駐點廠務與設備維護外包人員常需攜帶除錯筆電、韌體更新隨身碟或網路測試儀進入核心機房。若工具中潛藏震網（Stuxnet）式電磁/實體跳板惡意程式，將直接感染氣隙隔絕（Air-Gapped）之核心交易與廠務環控主機。請依 ISO/IEC 27001 規範，說明如何建置「機房實體隔離安檢站（Security Kiosk）」、「資料清洗轉換」與「外來設備實體封緘管制」防線？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 控制項對照</h4>
<p>關鍵基礎設施核心交易系統常採實體氣隙（Air-Gap）隔離。然而，外包工程師攜帶維護隨身碟、調試筆電或專用刷機工具，往往成為突破氣隙防線的<strong>「特洛伊木馬（Physical Vector）」</strong>。遵循 <strong>ISO/IEC 27001:2022 控制項 A.7.9（離場資產之安全性）與 A.8.19（安裝軟體之操作系統）</strong>，攜入機房之設備必須實施嚴苛檢驗與清洗。</p>

<h4>二、外來維護工具之實體跳板威脅剖析</h4>
<ul>
  <li><strong>BadUSB 韌體級攻擊</strong>：隨身碟微控制器晶片被刷入惡意韌體，插入時偽裝為人機介面設備（HID 鍵盤），微秒內自動敲入 PowerShell/Bash 惡意腳本。</li>
  <li><strong>封裝夾帶木馬之安裝檔/韌體</strong>：廠商提供之驅動程式或 Patch 安裝包暗藏供應鏈後門，感染氣隙內網主機。</li>
  <li><strong>維護筆電雙網卡跳板</strong>：筆電私下插上 4G/5G 網卡，另一端接上核心交換機 Console 埠，直接鑿穿機房實體隔離邊界。</li>
</ul>

<h4>三、無塵隔離安檢亭（Security Kiosk）與資料清洗機制</h4>
<p>於核心機房安檢外側建置獨立之<strong>「資安隔離檢測亭（Security Kiosk）」</strong>，所有攜入媒介一律執行標準清洗程序：</p>
<ol>
  <li><strong>多防毒引擎並行深度掃描（Multi-Engine Scanning）</strong>：
    安檢亭配置 10 組以上國際主流反病毒引擎（如 Kaspersky, Bitdefender, CrowdStrike），以非對稱特徵庫離線深度比對檔案。
  </li>
  <li><strong>內容結構消除與重組技術（CDR, Content Disarm and Reconstruction）</strong>：
    凡更新文件、說明手冊或組態設定檔，嚴格執行 CDR 清洗：<strong>剝除所有巨集代碼、嵌入式腳本（VBA/JS）、可疑超連結與非標準二進位物件</strong>，僅重構乾淨安全的明文字元。
  </li>
  <li><strong>單向光閘轉載（Data Diode Transfer）</strong>：
    外部隨身碟資料通過審查後，透過<strong>硬體單向光閘（只能發送、無法接收）</strong>單向傳輸至證交所專用之加密維護隨身碟（硬體加密晶片，附防寫實體開關）；<strong>外包廠商之原始隨身碟絕對嚴禁帶入機房！</strong>
  </li>
</ol>

<h4>四、外來筆電資產管制、實體封緘與全程側錄</h4>
<ul>
  <li><strong>設備攜入實體工單白名單（Asset Whitelisting）</strong>：
    外包筆電必須於 3 天前申請工單，詳列廠牌、型號、MAC 位址與序號；進入機房前由資安人員現場查核，比對無誤核發臨時條碼。
  </li>
  <li><strong>實體連接埠封緘（Physical Port Blocking）</strong>：
    <ul>
      <li>外包筆電所有<strong>攝影鏡頭、麥克風、無線網卡天線與未核准之 USB/Type-C 接口</strong>，現場貼上<strong>「雷射防偽易碎防篡改封籤（Tamper-Evident Tape）」</strong>；</li>
      <li>一旦撕開即浮現「OPENED」字樣且無法復原；出機房時由警衛逐項驗封，封條受損立即扣留設備進行數位鑑識。</li>
    </ul>
  </li>
  <li><strong>工作站本機離線稽核 Agent</strong>：
    攜入設備強制執行由證交所提供之暫時性離線稽核工具，關閉本機 Wi-Fi、藍牙與熱點分享，僅允許透過受控 Console 線路連接目標設備。
  </li>
</ul>

<h4>五、結論</h4>
<p>透過建立「無塵隔離安檢亭」、「CDR 資料清洗轉換」、「單向光閘專用儲存媒介」與「外來設備實體雷射封緘」，從源頭切斷惡意代碼隨人攜入之管道，為實體氣隙隔離提供堅不可摧的技術保障。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.9 攜離/自攜資產、A.8.19 操作軟體安裝』、『BadUSB (偽裝 HID 鍵盤) 與筆電 4G/5G 雙網卡跳板威脅』、『資安隔離檢測亭 (Security Kiosk) + 10組 Multi-Engine 多引擎掃描』、『CDR (內容結構消除與重組) 剝除巨集與惡意腳本』、『硬體單向光閘 (Data Diode) 轉載至專用防寫加密隨身碟 (廠商私碟嚴禁入內)』、『攜入筆電管制：鏡頭/網卡/USB 實體黏貼雷射易碎防篡改封籤 (Tamper-evident Tape) 出場驗封』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準控制項依據（5分）</strong>：引用 A.7.9 與 A.8.19，點出維護工具破壞實體氣隙之致命風險。</li>
  <li><strong>工具跳板威脅剖析（4分）</strong>：BadUSB 韌體攻擊、封裝後門與雙網卡鑿穿隔離邊界。</li>
  <li><strong>Security Kiosk 與 CDR 機制（8分）</strong>：多引擎離線掃描、CDR 剝除巨集與硬體單向光閘轉載。</li>
  <li><strong>設備封緘與資產白名單（8分）</strong>：白名單工單、雷射易碎封條封死鏡頭/USB、出場驗封機制。</li>
</ul>
            """
        },

        # 7. sec-essay-86: Out-of-Band (OOB) Physical Isolation, IPMI/iLO & Hardware Trojan Prevention
        {
            "id": "sec-essay-86",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "伺服器頻外管理（OOB / IPMI）實體獨立隔離、韌體防篡改與實體硬體木馬防護",
            "summary": "針對資料中心伺服器底層 BMC（IPMI/iLO/iDRAC）最高特權風險與硬體供應鏈植入威脅，依 ISO/IEC 27001:2022 A.8.20 與 A.7.13 規範，深度解構 OOB 實體氣隙專網、安全啟動 Root-of-Trust、高解析 X 光驗收與防硬體木馬之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 網路隔離與設備維護控制項對應 (5分)；2. 基板管理控制器 (BMC/IPMI) 之架構特權與致命破口 (4分)；3. OOB 頻外管理網路實體氣隙隔離與 PAM 存取加固 (8分)；4. 伺服器硬體交付驗收之硬體木馬 (Hardware Trojan) 防檢機制 (8分)",
            "question": "為確保核心伺服器於作業系統當機時仍能遠端開機與維護，伺服器皆搭載 IPMI/iLO/iDRAC 等基板管理控制器（BMC）。BMC 具備繞過作業系統直通硬體的最高特權，若遭入侵或供應鏈預先植入實體硬體木馬（Hardware Trojan），後果不堪設想。請依 ISO/IEC 27001 規範，申論如何規劃「頻外管理（OOB）實體隔離」、「BMC 韌體根信任防護」與「伺服器硬體防篡改驗收」架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 控制項對照</h4>
<p>基板管理控制器（BMC，如 HPE iLO、Dell iDRAC、Supermicro IPMI）為獨立於 CPU 與作業系統之外的微型電腦（SoC），具備冷啟動主機、虛擬光碟掛載與記憶體直接存取（DMA）之神級特權。依據 <strong>ISO/IEC 27001:2022 控制項 A.8.20（網路安全）與 A.7.13（設備維護）</strong>，必須對 BMC 與頻外維護網路建立極致防禦。</p>

<h4>二、BMC / IPMI 架構特權與資安致命弱點</h4>
<ul>
  <li><strong>環形零（Ring -1 / Ring -2）絕對特權</strong>：BMC 獨立運作於主板，即使伺服器 OS 關機、崩潰或遭重灌，BMC 依然全時通電運行；能遠端截獲螢幕鍵盤（KVM over IP）、重寫 BIOS 韌體。</li>
  <li><strong>常態性共用網卡（Shared LOM）漏洞</strong>：早期機房常將 BMC 與一般業務網卡共用實體連接埠（Sideband 通訊），攻擊者一旦打穿業務系統，即可橫向滲透進 BMC 掌控硬體。</li>
</ul>

<h4>三、頻外管理（OOB）實體氣隙隔離與存取治理架構</h4>
<ul>
  <li><strong>1. 實體獨立專網（Air-Gapped OOB Physical Network）</strong>：
    <ul>
      <li><strong>徹底禁用共用網卡模式（Dedicated Mode Only）</strong>：硬體配置強制鎖定專屬獨立網孔（Dedicated Management Port），物理性切斷與主機生產業務網路之任何連通；</li>
      <li><strong>獨立實體交換機與佈線</strong>：OOB 網路採用專屬獨立交換機、專用線槽與專屬 IP 網段，絕不與業務交換機共用 VLAN，達成真正的實體氣隙隔離。</li>
    </ul>
  </li>
  <li><strong>2. 存取收斂與 PAM 雙因子授權</strong>：
    <ul>
      <li>嚴禁工程師電腦直連 OOB 交換機；連線一律經由 <strong>OOB 專用 PAM 堡壘機</strong> 轉接；</li>
      <li>停用未加密之 IPMI 1.5/2.0 協定（防範 RAKP 密碼雜湊離線碰撞攻擊），強制採用 HTTPS / TLS 1.3 與 SSH 密鑰認證，並全面啟用 FIDO2 硬體 MFA。</li>
    </ul>
  </li>
  <li><strong>3. 韌體硬體根信任（Hardware Root of Trust, RoT）</strong>：
    選用具備硬體信任根晶片之伺服器（如 Silicon Root of Trust / Titan 晶片）；啟動時由不可篡改之唯讀硬體驗證 BMC 韌體之 ECDSA 數位簽章，若簽章毀損或版本降級（Anti-rollback），主機強制拒絕通電啟動。
  </li>
</ul>

<h4>四、伺服器硬體交付驗收之防硬體木馬（Hardware Trojan）實務</h4>
<ol>
  <li><strong>雙重防偽包裝驗證與資產溯源</strong>：
    新伺服器進場驗收時，檢驗原廠防撕毀雷射防偽易碎封條與出廠雜湊憑證，追蹤原廠安全供應鏈出貨溯源日誌。
  </li>
  <li><strong>高解析 X 光射線透視檢測（X-Ray Inspection）</strong>：
    針對批量進場之核心撮合伺服器主板進行抽樣 X-Ray 光學檢測：<strong>將主板內部多層 PCB 佈線與晶片腳位，與原廠標準設計金樣（Golden Image）進行自動化逐像素比對</strong>，精準察覺是否被惡意偷焊微型間諜晶片（如偷接於 I2C/SPI 匯流排之寄生硬體木馬）。
  </li>
  <li><strong>韌體指紋比對與外接設備實體防護</strong>：
    開機前導出 BIOS、BMC、RAID 卡與網卡 Option ROM 之二進位韌體，比對原廠官方 SHA-256 簽名；伺服器機箱內部 USB 連接埠與 PCIe 插槽加裝防破壞實體物理卡扣。
  </li>
</ol>

<h4>五、結論</h4>
<p>頻外管理是機房維運的最後底牌，亦是敵手夢寐以求的攻擊跳板。透過「OOB 獨立實體交換機氣隙隔離」、「硬體根信任韌體簽名」與「X-Ray 透視防硬體木馬檢驗」，證交所自矽晶圓與物理電路板底層築起金城湯池。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.8.20 網路安全、A.7.13 設備維護』、『BMC/iLO/iDRAC 特權 (Ring -2 / KVM over IP / DMA 記憶體穿透)』、『OOB 實體專網：強制專屬獨立網孔 (禁用 Shared LOM)、獨立實體交換機與線路 (禁共用 VLAN)』、『停用 IPMI 2.0 (防 RAKP 雜湊碰撞)，強制 HTTPS TLS 1.3 + PAM 堡壘機 + FIDO2 MFA』、『硬體根信任 (Silicon Root of Trust) 數位簽名校驗 + 防韌體降級』、『硬體木馬防護：原廠防偽封條、X-Ray 射線透視比對原廠 Golden Image (查核 I2C/SPI 偷焊寄生晶片)』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準依據（5分）</strong>：引用 A.8.20 與 A.7.13，闡釋 BMC 頻外管理之底層神級特權風險。</li>
  <li><strong>BMC 特權與共用網卡漏洞（4分）</strong>：KVM 穿透、DMA 存取與 Shared LOM 側信道破口。</li>
  <li><strong>OOB 實體氣隙與 PAM（8分）</strong>：獨立實體交換機、停用 IPMI 2.0、PAM 轉接與 Silicon RoT 韌體簽名。</li>
  <li><strong>硬體木馬檢測實務（8分）</strong>：原廠溯源、X-Ray 透視比對 Golden Image 與韌體指紋比對。</li>
</ul>
            """
        },

        # 8. sec-essay-87: HEMP/TEMPEST Shielding & Seismic Base Isolation
        {
            "id": "sec-essay-87",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "機房電磁脈衝防護（HEMP / TEMPEST）與極限抗震剪力隔震工程防禦架構",
            "summary": "針對地緣政治衝突高空核爆電磁脈衝（HEMP）、非核電磁脈衝武器（IEMI）與強烈地震，依 ISO/IEC 27001:2022 A.7.5 與 MIL-STD-188-125 標準，深度解構法拉第籠（Faraday Cage）電磁屏蔽、蜂窩導波管與抗震雙向隔震墊之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 實體與環境極端威脅對照 (5分)；2. 電磁脈衝 (HEMP/IEMI) 與電磁洩漏 (TEMPEST) 物理破壞原理 (4分)；3. 法拉第籠 (Faraday Cage) 屏蔽室與管線濾波工程 (8分)；4. 伺服器機架雙向水平抗震隔震墊 (Seismic Base Isolation) (8分)",
            "question": "證券交易所作為國家政經中樞，面臨高空核爆電磁脈衝（HEMP）、非核電磁脈衝武器（IEMI）定向能攻擊、電磁洩漏（TEMPEST）監聽以及強烈地震等極端威脅。請依 ISO/IEC 27001 之 A.7.5 規範，說明如何針對核心撮合機房規劃「法拉第籠（Faraday Cage）電磁屏蔽」、「濾波波導系統」與「機架抗震隔震（Seismic Isolation）」架構？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 極端實體威脅對應</h4>
<p>臺灣證券交易所為國家關鍵基礎設施一級防護目標，在現代不對稱作戰與極端天災情境下，必須防範超越傳統火水災的實體極限打擊。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.5（防範實體與環境威脅）</strong>，核心機房必須具備抵禦強烈地震、電磁脈衝摧毀與電磁輻射洩漏的工程強化防線。</p>

<h4>二、電磁脈衝（HEMP/IEMI）摧毀原理與 TEMPEST 洩漏威脅</h4>
<ul>
  <li><strong>高空核爆電磁脈衝（HEMP / MIL-STD-188-125）</strong>：
    產生 E1（奈秒級超快上升沿，場強數萬伏特/米，擊穿微電子半導體）、E2（微秒級雷電特性）與 E3（百秒級地磁感應電流，燒毀變壓器與電網電力設施）。
  </li>
  <li><strong>非核高功率電磁武器（IEMI）與 TEMPEST 洩漏</strong>：
    恐怖分子利用微波定向能武器自建築外發射電磁波燒毀伺服器；或利用高靈敏接收天線截獲伺服器螢幕與匯流排洩漏之微弱高頻電磁輻射，遠端還原交易畫面與金鑰。
  </li>
</ul>

<h4>三、法拉第籠（Faraday Cage）屏蔽室與管線濾波工程</h4>
<ul>
  <li><strong>1. 六面連續焊接式金屬屏蔽室（Faraday Cage）</strong>：
    核心撮合與密鑰機房天花板、地板、四面牆壁採用<strong>雙層鍍鋅鋼板（厚度 ≥ 2mm）或純銅板全連續縫隙氣密焊接</strong>，形成封閉式法拉第等電位籠體；於 10kHz 至 10GHz 寬頻帶範圍內，提供 <strong>大於 80dB ~ 100dB 的電磁屏蔽衰減效能</strong>。
  </li>
  <li><strong>2. 進出管線與開口之電磁防禦</strong>：
    <ul>
      <li><strong>蜂窩狀導波通風窗（Honeycomb Waveguide Vents）</strong>：機房空調進回風口安裝截面呈六角形之蜂窩銅質導波管，利用「截止波導管（Waveguide Below Cutoff）」物理原理，使空氣暢通流通，但電磁波完全被反射衰減；</li>
      <li><strong>電源 HEMP 濾波器（HEMP Power Line Filters）</strong>：所有引進機房之電力線路，於屏蔽外壁安裝通過 MIL-STD-188-125-1 認證之大容量突波抑制器（MOV）與低通電感電容濾波器，將瞬態感應突波於奈秒內導引至大地；</li>
      <li><strong>光纖進線專用介質穿牆波導管</strong>：資料通訊全面採用光纖，金屬外皮於屏蔽壁外剝除接地，純玻璃纖維經由金屬波導管穿入，阻絕任何金屬導線引入感應電流。</li>
    </ul>
  </li>
</ul>

<h4>四、伺服器機櫃雙向抗震隔震墊（Seismic Base Isolation）</h4>
<ol>
  <li><strong>耐震防護目標（符合耐震 7 級，地表加速度 PGA > 0.4g）</strong>：
    台灣地處環太平洋地震帶，劇烈震動會導致伺服器硬碟磁頭撞擊碟片（Head Crash）、光纖接頭脫落與機櫃傾倒短路。
  </li>
  <li><strong>雙向滾珠/摩擦擺隔震台（Ball Bearing / Friction Pendulum Isolator）</strong>：
    核心機櫃基座與建築地板間安裝<strong>「三維雙向滾動隔震台」</strong>。在強烈地震發生時，底座鋼珠於曲面滑道內滾動滑移，<strong>將傳導至機櫃之水平加速度消能衰減 70%~85% 以上</strong>，將劇烈劇震轉化為平緩低頻晃動。
  </li>
  <li><strong>柔性管線與抗震彈簧懸吊</strong>：
    空調冰水管路與電源匯流排排管採用耐震可撓性軟管（Flexible Joints），天花板懸吊線槽配備抗震斜撐支架，杜絕管線拉扯斷裂漏水漏電。
  </li>
</ol>

<h4>五、結論</h4>
<p>面對極端地緣威脅與強震挑戰，透過「法拉第籠全面電磁屏蔽阻斷 HEMP 燒毀與 TEMPEST 側錄」、「蜂窩導波管與濾波器消滅進線突波」結合「雙向隔震墊守護硬體機械結構」，證交所達成最高等級實體韌性，立於不敗之地。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.5 實體環境威脅、MIL-STD-188-125 標準』、『HEMP 威脅：E1 奈秒超快沿半導體擊穿、E2、E3 地磁感應燒毀變壓器』、『TEMPEST 電磁洩漏監聽防護』、『法拉第籠 (Faraday Cage) 雙層鍍鋅鋼板連續氣密焊接，屏蔽衰減 > 80~100dB』、『管線防護：蜂窩狀導波通風窗 (Honeycomb Waveguide)、電源 HEMP 突波濾波器、非金屬光纖波導進線』、『機架耐震 7 級 (PGA > 0.4g)：三維雙向滾珠摩擦擺隔震台 (消能衰減 70~85%)、可撓性軟管防止拉扯斷裂』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準與極端威脅背景（5分）</strong>：引用 A.7.5 與 MIL-STD-188-125，界定 HEMP、IEMI 與強震威脅情境。</li>
  <li><strong>HEMP 與 TEMPEST 機制（4分）</strong>：深入點出 E1 脈衝擊穿半導體與高頻電磁輻射洩密。</li>
  <li><strong>法拉第籠與波導管工程（8分）</strong>：雙層鋼板連續焊接、蜂窩導波通風窗、電源突波濾波器與光纖穿牆波導。</li>
  <li><strong>耐震 7 級雙向隔震台（8分）</strong>：滾珠摩擦擺隔震消能 70%~85%、保護硬碟磁頭與抗震可撓管線。</li>
</ul>
            """
        },

        # 9. sec-essay-88: OT Facility Systems (BMS/SCADA), Purdue Model & Anti-Tampering
        {
            "id": "sec-essay-88",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "機房廠務工控（BMS/SCADA）物聯網 Purdue 模型隔離與防惡意篡改架構",
            "summary": "針對資料中心樓宇管理（BMS）、可程式邏輯控制器（PLC）調控空調冰水與發電機之工控資安風險，依 ISO/IEC 27001:2022 A.8.20 與 IEC 62443 規範，深度解構 Purdue 五層模型、單向資料光閘、Modbus/BACnet 協定深度封包檢測之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 網路隔離及工控標準對應 (5分)；2. 廠務工控協定 (Modbus/BACnet) 缺乏身分鑑別之致命漏洞 (4分)；3. Purdue 五層模型與 OT/IT 實體/邏輯深度隔離 (8分)；4. 工業級單向光閘與深度封包檢測 (DPI) 異常指令阻斷 (8分)",
            "question": "資料中心依賴樓宇管理系統（BMS/BAS）與可程式邏輯控制器（PLC）調控冰水主機、UPS 電源分配與消防排氣。若工控通訊協定（如 Modbus、BACnet）遭外包或內網駭客滲透竄改，可能蓄意關閉冷卻或中斷電源導致交易主機過熱燒毀。請依 ISO/IEC 27001 規範，說明如何運用 Purdue 工控模型將「廠務 OT 網路」與「IT 交易網路」隔離，並建立防指令篡改防線？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 工控網路防護對照</h4>
<p>資料中心實體營運完全依賴廠務營運技術（OT）與樓宇管理系統（BMS）。攻擊者若能控制機房空調 PLC 或發電機控制器，即可進行實體破壞（Cyber-Physical Attack），引發無預警全廠跳電或火災。依據 <strong>ISO/IEC 27001:2022 控制項 A.8.20（網路安全）與 ISA/IEC 62443 工控資安標準</strong>，廠務 OT 必須實施嚴格區域分段。</p>

<h4>二、傳統廠務工控通訊協定之脆弱性破口</h4>
<ul>
  <li><strong>明文無認證原罪</strong>：Modbus/TCP、BACnet/IP、LonWorks 等工控協定設計於封閉環境，<strong>缺乏身分鑑別（No Authentication）、資料加密與抗重放機制</strong>；任何能連入網路之終端，皆可偽造 Function Code（如 Modbus <code>Write Single Coil (0x05)</code>）向 PLC 發送強制關閉冰水泵指令。</li>
  <li><strong>外包遠端維護後門</strong>：空調或發電機原廠常於控制器旁私自外掛 4G 數據機或 TeamViewer，繞過企業防火牆形成隱蔽邊界穿透。</li>
</ul>

<h4>三、Purdue 工控模型分層與 OT/IT 深度隔離架構</h4>
<p>全面導入 <strong>Purdue 五層模型（ISA-95 / IEC 62443）</strong>，實施縱深防禦與微隔離：</p>
<ul>
  <li><strong>Level 0 / Level 1（現場儀表與控制器層）</strong>：
    溫濕度感測器、水流計、變頻器與 PLC（可程式邏輯控制器）。建立獨立專用硬體匯流排（RS-485 / CAN bus），完全不接入乙太網。
  </li>
  <li><strong>Level 2（廠務操作監控層）</strong>：
    BMS HMI 人機介面工作站與 SCADA 伺服器。限制於封閉 OT 區域，停用外部網際網路存取，所有 USB 埠硬體鎖死。
  </li>
  <li><strong>Level 3（廠務運營管理層）</strong>：
    DCIM 資料庫與廠務記錄伺服器。設置於專用廠務機房，與辦公網完全實體解耦。
  </li>
  <li><strong>Level 3.5（工業隔離區 IDMZ, Industrial Demilitarized Zone）</strong>：
    <strong>IT 與 OT 唯一的受控橋樑！</strong>部署雙重異質防火牆（Dual Heterogeneous Firewalls）；任何 IT 業務系統（如 SIEM / 報表）嚴禁直連 OT 主機，所有跨區資料傳輸必須於 IDMZ 之中繼跳板伺服器（Proxy/Bastion）進行資料交換。
  </li>
</ul>

<h4>四、工業級單向光閘（Data Diode）與 DPI 深度封包檢測</h4>
<ol>
  <li><strong>硬體單向光閘傳輸（Unidirectional Data Diode）</strong>：
    廠務 DCIM 需將冷熱通道溫濕度、發電機狀態數據即時同步至上層 IT 資安監控中心（SOC）。<strong>全面採用物理單向光閘：光發射端（LED）位於 OT 側，光接收端（Photodiode）位於 IT 側</strong>；數據只能單向由 OT 拋出至 IT，IT 側物理上絕不可能發送任何指令或封包反向進入 OT，根絕勒索軟體橫向擴散。
  </li>
  <li><strong>工控協定深度封包檢測（DPI Industrial Firewall）</strong>：
    於 BMS HMI 與 PLC 間佈設工控專用防火牆，啟用 <strong>DPI 深度封包檢測與指令白名單</strong>：
    <ul>
      <li>僅允許讀取指令（如 Modbus <code>Read Holding Registers (0x03)</code>），一律阻斷所有寫入與停機指令；</li>
      <li>若需在維護時段下達變更指令，必須透過 PAM 堡壘機取得具時效的工單金鑰，並由廠務專責正職人員現場執行「實體切換鑰匙（Hardware Key Switch）」將 PLC 解鎖，防範純軟體未授權覆寫。</li>
    </ul>
  </li>
</ol>

<h4>五、結論</h4>
<p>廠務工控是支撐交易核心的命脈。透過 Purdue 模型嚴格分層、IDMZ 雙異質防線、物理單向光閘阻斷橫向反動，以及工控 DPI 指令白名單管制，證交所徹底消滅網路武器由廠務破門而入之實體攻擊路徑。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.8.20 網路安全、ISA/IEC 62443 工控標準』、『Modbus/BACnet 缺乏認證與明文漏洞 (偽造 Write Coil 0x05 關閉冰水泵)』、『Purdue 五層模型分段：L0/L1現場儀表、L2 HMI監控、L3 廠務運營、L3.5 工業隔離區 (IDMZ 雙異質防火牆)』、『物理單向光閘 (Data Diode)：OT 狀態拋轉 IT，物理絕無可能反向傳入指令』、『工控 DPI 深度封包檢測 + 指令白名單 (僅放行 Read，封鎖 Write)』、『PLC 實體鑰匙鎖 (Hardware Key Switch) 雙人現場變更』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準與工控安全依據（5分）</strong>：引用 A.8.20 與 IEC 62443，指出網路攻擊引發實體毀滅之重大風險。</li>
  <li><strong>工控協定脆弱性剖析（4分）</strong>：Modbus/BACnet 缺乏驗證、明文通訊與外包私掛 4G 後門。</li>
  <li><strong>Purdue 五層分層與 IDMZ（8分）</strong>：L0~L3 封閉分層，L3.5 工業 DMZ 雙異質防火牆中繼。</li>
  <li><strong>單向光閘與 DPI 指令白名單（8分）</strong>：物理單向光纖隔離橫向攻擊、DPI 封鎖寫入指令與 PLC 實體鑰匙開關。</li>
</ul>
            """
        },

        # 10. sec-essay-89: 24/7 CCTV, Intelligent AI Video Content Analytics (VCA) & SOC Interlocking
        {
            "id": "sec-essay-89",
            "category": "sec",
            "chapter": "第 2 章：資安標準與控制框架（ISO 27001 與 NIST CSF）",
            "title": "機房全時全景閉路電視（CCTV）、智慧 AI 視覺分析（VCA）與 SOC 即時動態聯防",
            "summary": "針對傳統機房監視器事後調閱被動盲點與現場違規防範，依 ISO/IEC 27001:2022 A.7.4 實體安全監視規範，深度解構 4K 全景無死角覆蓋、邊緣 AI 異常行為視覺分析（VCA）、影像 SHA-256 數位水印與 SOC 3分鐘現場阻斷之 80% 核心得分架構。",
            "points": 25,
            "rubric": "1. 破題與 ISO 27001 實體安全監控控制項對照 (5分)；2. 機房立體化 CCTV 佈設與抗剪接影像保全 (4分)；3. 智慧邊緣 AI 視覺分析 (VCA) 異常行為偵測模型 (8分)；4. 門禁工單即時勾稽、SOC 聲光連動與事中阻斷閉環 (8分)",
            "question": "傳統機房閉路監視器（CCTV）多僅作事後調閱錄影，無法在外部人員代打卡、未依工單擅自觸碰隔壁機櫃、或非法拿出手機偷拍螢幕時即時攔截。請依 ISO/IEC 27001 之 A.7.4 實體安全監視規範，說明如何規劃機房立體化 CCTV 影像覆蓋，並結合「AI 視覺分析（VCA）」與「門禁/SOC 即時聯防」以達成事前預警與事中即時阻斷？（25分）",
            "modelAnswer": """
<h4>一、破題與 ISO/IEC 27001:2022 實體安全監控標準</h4>
<p>實體安全監視不可停留於「事後調閱責任追究」之被動模式。在微秒決勝的金融關鍵基礎設施中，未經授權的物理碰觸可能於數秒內癱瘓撮合主機。依據 <strong>ISO/IEC 27001:2022 控制項 A.7.4（實體安全監控）</strong>，監控設施必須能即時偵測非授權實體進入與異常活動，並引導安全人員立即應變處置。</p>

<h4>二、機房立體化 CCTV 佈設與防篡改影像保全架構</h4>
<ul>
  <li><strong>全方位立體無死角影像覆蓋</strong>：
    <ul>
      <li><strong>機房主要出入口與安全艙</strong>：配置 4K 星光級臉部特寫攝影機（支援 WDR 寬動態，防強光背光影響辨識）；</li>
      <li><strong>冷熱通道與走道</strong>：配置 180° / 360° 全景魚眼攝影機（高密度覆蓋）；</li>
      <li><strong>伺服器機櫃內部與正反面</strong>：機櫃上方配置交叉對射鏡頭，<strong>精準拍攝工程師手指操作、線路插拔與機櫃門開關之細節</strong>，徹底消滅盲區。</li>
    </ul>
  </li>
  <li><strong>影像真實性與防剪接數位水印（Anti-Tamper Video）</strong>：
    影像編碼晶片硬體即時注入<strong>高精度 PTP（IEEE 1588v2）奈秒時間戳記與專屬晶片私鑰簽章之 SHA-256 數位水印</strong>；錄影資料經獨立專網傳輸，全量寫入 <strong>WORM（單寫多讀）不可篡改光碟/雲儲存庫，保留至少 180 天至 1 年</strong>，杜絕內部人消磁或抽換錄影。
  </li>
</ul>

<h4>三、邊緣 AI 智慧視覺分析（VCA, Video Content Analytics）模型</h4>
<p>攝影機邊緣（Edge AI）內建深度學習神經網路模型，毫秒級實時分析以下異常行為：</p>
<ol>
  <li><strong>防尾隨與反向逆行偵測</strong>：辨識閘門區域在一次授權刷卡動作下，是否有第二人緊貼尾隨進入，或自出口方向逆向闖入。</li>
  <li><strong>越界攀爬與非法逗留（Loitering）偵測</strong>：設定虛擬電子圍籬（Virtual Tripwire）；當人員滯留於高敏感區域（如 HSM 密鑰區、主配電盤前）超過設定時限（如 2 分鐘）且無操作行為，即刻發出警報。</li>
  <li><strong>違規持用手機與偷拍姿勢識別（Object & Pose Detection）</strong>：利用骨骼姿態演算法（Pose Estimation）與物件偵測，<strong>一旦識別出人員拿出智慧型手機、相機或做出舉起設備對準螢幕/機架之拍照手勢</strong>，系統於 0.5 秒內警報。</li>
  <li><strong>未授權觸碰機櫃偵測（Unscheduled Rack Touching）</strong>：在非工單核准之相鄰機櫃周遭畫設偵測框，一旦有人員手臂伸入或嘗試開啟非授權機櫃門，系統即刻發送告警。</li>
</ol>

<h4>四、門禁工單即時勾稽、SOC 連動與事中阻斷閉環</h4>
<ul>
  <li><strong>門禁工單與影像即時連動勾稽</strong>：
    VCA 系統透過安全 API 串接 ITSM 工單系統與實體門禁。當某個機櫃門被開啟時，系統即時驗證：<strong>「此時此刻該位置是否有對應之有效維護工單？」</strong>；若屬無工單強行開啟，判定為重大入侵事件。
  </li>
  <li><strong>7x24 SOC 儀表板彈窗與現場聲光震撼</strong>：
    異常觸發時，機房現場對應分區頂部之<strong>紅色旋轉警示燈立即閃爍並啟動定向定向廣播警告</strong>；同時，7x24 SOC 監控電視牆瞬間自動彈出「多視角現場即時 4K 畫面」與「工單資訊」，SOC 值班主管按下按鈕，3 分鐘內駐點機動警衛抵達現場阻斷違規。
  </li>
</ul>

<h4>五、結論</h4>
<p>結合立體全景 4K 監控、WORM 數位水印防偽、邊緣 AI 異常姿態行為辨識，以及與門禁工單/SOC 毫秒級聲光連動，證交所將 CCTV 由傳統「事後鑑識調閱」轉變為「事中主動攔截」，構築起 AI 賦能之實體安全智慧天網。</p>
            """,
            "examinerTips": "評分關鍵字：『ISO 27001:2022 A.7.4 實體安全監控』、『全景立體無死角：4K 臉部特寫 (WDR)、冷熱通道 360° 魚眼、機櫃對射鏡頭拍攝插拔細節』、『影像防偽：PTP 奈秒時戳、硬體晶片簽章 SHA-256 數位水印、WORM 存儲 180天至1年』、『邊緣 AI 視覺分析 (VCA)：防尾隨/逆行、虛擬圍籬滯留、手機偷拍姿態 (Pose Estimation) 識別、未授權機櫃觸碰』、『工單即時勾稽：開機櫃門對照 ITSM 工單有效性』、『SOC 閉環：現場分區紅光閃爍+定向廣播，SOC 電視牆彈窗，3分鐘警衛抵達現場攔截』。",
            "detailedExplanation": """
<h5>🎯 評分踩點邏輯剖析</h5>
<ul>
  <li><strong>標準控制項依據（5分）</strong>：引用 A.7.4，界定主動防禦相對於事後調閱的革命性優勢。</li>
  <li><strong>立體監控佈設與防篡改（4分）</strong>：4K/魚眼/機櫃對射覆蓋，奈秒時戳與 WORM 不可篡改保存。</li>
  <li><strong>AI 視覺分析 VCA 四大模型（8分）</strong>：尾隨逆行、區域滯留、手機偷拍姿態與非工單機櫃觸碰識別。</li>
  <li><strong>工單勾稽與 SOC 事中阻斷（8分）</strong>：自動比對工單、現場聲光警告、SOC 電視牆聯動與 3 分鐘警衛攔截閉環。</li>
</ul>
            """
        }
    ]
