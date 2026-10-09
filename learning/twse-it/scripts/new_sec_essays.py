# -*- coding: utf-8 -*-
"""
Generate 40 new essay questions (20 for Information Security, 20 for System & Network)
and combine with original 24 questions, producing 64 comprehensive, full-mark essays
for the TWSE examination preparation platform.
"""
import os
import sys
import json

# Insert scripts dir to import existing build_essays
sys.path.insert(0, os.path.dirname(__file__))
import build_essays

def get_20_new_sec_essays():
    return [
        {
            "id": "sec-essay-13",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金管會「金融機構資通安全防護基準」主機加固、評估等級與獨立驗證實踐",
            "points": 25,
            "rubric": "1. 資通安全防護基準等級劃分原則 (6分)；2. 伺服器核心作業系統與網路加固規範 (8分)；3. 獨立資安檢測與第三方查核機制 (7分)；4. 結論 (4分)",
            "question": "依金管會與證券期貨局發布之「金融機構資通安全防護基準」，證券期貨業者必須依據業務性質及系統重要性實施分級防護。請分析該防護基準對核心交易系統之主機加固（Hardening）、帳號生命週期、密碼強度、網路通訊加密及定期獨立驗證之明確規範，並以表格對比不同防護等級之關鍵控制要求。",
            "modelAnswer": """
<h4>一、破題：金融機構資通安全防護基準之戰略定位</h4>
<p>金管會「金融機構資通安全防護基準」為我國證券期貨業建立資通安全縱深防禦體系之根本法規。其核心精神在於<strong>「風險導向、分級管理、持續驗證」</strong>，針對核心業務系統（如撮合、委託收受、行情推播）施加最高標準之防護措施。</p>

<h4>二、核心交易主機系統加固與技術控制規範</h4>
<ol>
  <li><strong>主機系統安全加固（System Hardening）</strong>：
    依據 CIS Benchmarks 關閉所有非必要服務（如 FTP、Telnet、RPC），移除未授權編譯器與工具；啟用強制存取控制（SELinux / AppArmor）；禁止使用預設帳號與弱密碼。
  </li>
  <li><strong>身分鑑別與特權存取</strong>：
    特權帳號（Root/Admin）必須落實雙人覆核或 PAM（Privileged Access Management）管控，全面啟用多因子身分鑑別（MFA），密碼長度至少 12 碼以上並強制每季變更與歷史檢核。
  </li>
  <li><strong>網路與通訊安全</strong>：
    核心主機必須置於嚴格隔離之安全網段（DMZ 或內部核心區），對外通訊一律採用 TLS 1.3 強加密通訊協定，嚴禁任何未加密之明文傳輸。
  </li>
  <li><strong>獨立安全驗證機制</strong>：
    每年至少執行一次由合格第三方機構執行之<strong>滲透測試（Penetration Testing）</strong>與<strong>弱點掃描（Vulnerability Assessment）</strong>，重大缺失限期一個月內完成修補複測。
  </li>
</ol>

<h4>三、系統防護等級關鍵控制項目橫向對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">控制構面</th>
      <th style="padding:6px 10px;">第一級（核心交易系統）</th>
      <th style="padding:6px 10px;">第二級（一般營運系統）</th>
      <th style="padding:6px 10px;">第三級（內部行政系統）</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">多因子身分鑑別 (MFA)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">全面強制要求 (FIDO2 / 硬體 Token)</td>
      <td style="padding:6px 10px;">特權帳號強制要求</td>
      <td style="padding:6px 10px;">建議特權帳號啟用</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">傳輸加密規格</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">強制 TLS 1.3 / mTLS 雙向認證</td>
      <td style="padding:6px 10px;">TLS 1.2 以上加密傳輸</td>
      <td style="padding:6px 10px;">標準 HTTPS 傳輸</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">獨立安全檢驗頻率</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">每年 1 次第三方滲透測試 + 紅隊演練</td>
      <td style="padding:6px 10px;">每兩年 1 次滲透測試</td>
      <td style="padding:6px 10px;">每年弱點掃描</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">稽核日誌保存年限</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">至少保存 5 年 (WORM 唯讀存儲)</td>
      <td style="padding:6px 10px;">至少保存 3 年</td>
      <td style="padding:6px 10px;">至少保存 1 年</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>臺灣證券交易所作為我國金融核心關鍵基礎設施，必須以「超越基準、全員防護」之高規格實踐防護基準，確保證券市場主機在遭遇複合式威脅時仍具備極致韌性。</p>
            """,
            "examinerTips": "評分重點：『金融機構資通安全防護基準第一級要求』、『CIS Benchmark 主機加固』、『第三方獨立滲透測試每年執行』、『日誌保存至少 5 年且防竄改 WORM』。",
            "detailedExplanation": "此題考驗考生對金管會法規細節之熟稔度。答題時務必區分系統分級（核心交易 vs 一般系統），切忌泛泛而談資安常識，應精確引用法規條文與控制項目。"
        },
        {
            "id": "sec-essay-14",
            "category": "sec",
            "chapter": "第 3 章：ISO 19011 管理系統稽核指引與主導稽核員實務",
            "title": "ISO 19011:2018 稽核指引：第一階段（Stage 1）與第二階段（Stage 2）稽核執行差異與現場抽樣技術",
            "points": 25,
            "rubric": "1. Stage 1 文件審查與準備度查核目的 (6分)；2. Stage 2 現場實施查核方法與客觀證據 (8分)；3. 兩階段對比分析表 (7分)；4. 抽樣偏差防範與結論 (4分)",
            "question": "臺灣證券交易所為確保資訊安全管理系統（ISMS）持續符合 ISO/IEC 27001 國際標準，定期委由外部認證機構執行轉證稽核。主導稽核員依據 ISO 19011:2018 執行評審時，何謂 Stage 1（文件審查與準備度查核）與 Stage 2（現場實施與有效性查核）？請比較兩者目標、範圍、查證手法與常見產出，並說明現場稽核時如何運用代表性抽樣避免採樣偏差？",
            "modelAnswer": """
<h4>一、破題：ISO 19011 稽核指引雙階段認證哲學</h4>
<p>依據 ISO 19011:2018 及 ISO/IEC 27006 規範，初次認證或重大重審必須嚴格區分為<strong>第一階段（Stage 1）</strong>與<strong>第二階段（Stage 2）</strong>。Stage 1 重在「設計健全度與準備度（Readiness）」，Stage 2 重在「運行有效性與落地實踐（Effectiveness）」。</p>

<h4>二、兩階段稽核執行核心重點</h4>
<ol>
  <li><strong>Stage 1 準備度評審（Readiness Review）</strong>：
    稽核員審查 ISMS 範圍界定文件（Scope）、資訊安全政策、適用性聲明書（SoA）、風險評鑑與處理報告、內部稽核與管理審查會議紀錄。目的在評估受稽單位是否已具備進入 Stage 2 現場稽核之先決條件，若發現體系缺漏可預先開立關注事項。
  </li>
  <li><strong>Stage 2 現場實施有效性評審（Implementation Review）</strong>：
    深入各營運現場（機房、監控中心、研發部門），依據 SoA 所選取之 Annex A 控制措施，透過<strong>面談（Interview）、觀察（Observation）、紀錄檢驗（Record Examination）</strong>取得客觀證據（Objective Evidence），驗證 ISMS 規範是否實際執行。
  </li>
  <li><strong>現場抽樣技術與偏差防範</strong>：
    採用<strong>條件隨機抽樣（Stratified Random Sampling）</strong>，針對高風險核心資產拉高抽樣比例；嚴格避免「受稽方主動提供挑選之樣品」，稽核員必須親自從系統總表中隨機抽樣，杜絕抽樣偏差。
  </li>
</ol>

<h4>三、Stage 1 vs Stage 2 稽核全構面對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">評審維度</th>
      <th style="padding:6px 10px;">第一階段稽核 (Stage 1)</th>
      <th style="padding:6px 10px;">第二階段稽核 (Stage 2)</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">主要目標</td>
      <td style="padding:6px 10px;">審查文管架構、確認範圍與 Stage 2 準備度</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">驗證控制措施之現場落實度與持續有效性</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">查核重點</td>
      <td style="padding:6px 10px;">SoA、風險評鑑報告、內稽與管審紀錄</td>
      <td style="padding:6px 10px;">日常維運紀錄、變更單、門禁日誌、事件處置單</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">查驗手法</td>
      <td style="padding:6px 10px;">文件審閱、高階主管溝通、流程走查</td>
      <td style="padding:6px 10px;">系統現場實機驗證、隨機抽樣日誌、人員隨機訪談</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">稽核結論產出</td>
      <td style="padding:6px 10px;">準備度報告、Stage 2 稽核計畫、改善建議</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">不符合事項報告（Major/Minor NC）、發證建議</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>主導稽核員依循 ISO 19011 原則嚴謹分流雙階段稽核，不僅保障發證公信力，更實質促使證交所 ISMS 體系自形式合規昇華至實質強固之安全文化。</p>
            """,
            "examinerTips": "評分核心：『Stage 1 準備度查核 vs Stage 2 現場有效性查核』、『客觀證據 (Objective Evidence) 三種取得法』、『條件隨機抽樣避免抽樣偏差』、『發證建議與 NC 判定』。",
            "detailedExplanation": "考生易混淆兩階段稽核之職能劃分。務必強調 Stage 1 主要是確認文件體系與管審內稽是否完備，Stage 2 才是到現場挖客觀證據。"
        },
        {
            "id": "sec-essay-15",
            "category": "sec",
            "chapter": "第 3 章：ISO 19011 管理系統稽核指引與主導稽核員實務",
            "title": "稽核不符合事項（Non-Conformity）判定原則、重大與次要缺失界定及 8D 根本原因分析（RCA）矯正措施",
            "points": 25,
            "rubric": "1. Major NC、Minor NC 與 Observation 判定基準 (7分)；2. 8D 問題解決方法架構與根本原因分析 (9分)；3. 不符合事項改善閉環對照表 (5分)；4. 結論 (4分)",
            "question": "資訊安全稽核過程中，稽核員若發現受稽單位未依作業程序執行定期特權帳號審查，應如何依據 ISO 19011 與 ISO/IEC 27001 判定其為「重大不符合事項（Major NC）」、「次要不符合事項（Minor NC）」或「觀察事項（Observation）」？請詳述其判定準則，並針對已開立之重大不符合事項，說明如何運用 8D（Eight Disciplines）問題解決方法完成根本原因分析（RCA）及後續矯正預防措施（CAPA）之有效性驗證。",
            "modelAnswer": """
<h4>一、破題：稽核發現與不符合事項本質</h4>
<p>依據 ISO 19011:2018，稽核發現（Audit Findings）乃將收集之客觀證據與稽核準則（Audit Criteria）進行比對之結果。當未滿足要求時即構成「不符合事項（NC）」。其分級攸關證書核發與管理層資源投注優先級。</p>

<h4>二、不符合事項判定準則</h4>
<ol>
  <li><strong>重大不符合事項（Major NC）</strong>：
    - 體系層面嚴重缺失，完全缺少標準強制要求之條款或關鍵控制項（如完全未實施風險評鑑或未召開管理審查）；<br>
    - 多個次要不符合事項指向同一系統性崩潰（如所有主機均無帳號審查紀錄）；<br>
    - 直接引發重大資通安全風險或違背法定監理底線。<strong>後續後果：暫緩發證或要求重大複查</strong>。
  </li>
  <li><strong>次要不符合事項（Minor NC）</strong>：
    - 單一、偶發性之作業疏失，程序書已明確定義且大部分遵循，僅抽查中發現極少數未完整執行（如 100 筆特權帳號中僅 1 筆逾期未簽核）；<br>
    - 體系維持健全，不致直接癱瘓防護效能。<strong>處理：受稽方提出改善計畫並限期關閉</strong>。
  </li>
  <li><strong>觀察事項 / 機會改善（Observation / OFI）</strong>：
    - 現行作法未違反現行標準與作業規定，但具備潛在劣化風險，稽核員提出前瞻建議。
  </li>
</ol>

<h4>三、8D（Eight Disciplines）問題分析與矯正預防實踐</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">8D 步驟</th>
      <th style="padding:6px 10px;">步驟名稱</th>
      <th style="padding:6px 10px;">特權帳號審查缺失之實務行動</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">D1 & D2</td>
      <td style="padding:6px 10px;">成立團隊 & 問題描述</td>
      <td style="padding:6px 10px;">指派資安主管、維運組長成立小組；明確定義「撮合伺服器特權帳號未落實雙月覆核」。</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">D3</td>
      <td style="padding:6px 10px;">臨時遏阻行動 (Containment)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">立即清查並凍結所有未經覆核之臨時特權帳號，限縮存取權限。</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">D4</td>
      <td style="padding:6px 10px;">根本原因分析 (RCA)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">運用 5-Whys 與魚骨圖，發現真因為「依賴人工行事曆提醒，人員輪調無交接機制」。</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">D5 & D6</td>
      <td style="padding:6px 10px;">擬定並執行永久對策</td>
      <td style="padding:6px 10px;">導入自動化 PAM 平台，自動產生存取清單並強制每 60 天鎖定逾期帳號。</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">D7 & D8</td>
      <td style="padding:6px 10px;">預防再發 & 肯定表彰</td>
      <td style="padding:6px 10px;">修訂 ISMS-P-08 程序書，並由稽核主管於 3 個月後驗證關閉。</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>稽核的終極價值不在於開單，而在於引導組織啟動閉環改善。唯有落實 8D 根本原因剖析與有效性驗證，方能杜絕資安破口死灰復燃。</p>
            """,
            "examinerTips": "踩分要點：『Major NC（系統性失效/威脅監理）vs Minor NC（單一偶發）』、『8D 架構：D3 遏阻、D4 根本原因分析 (5-Whys)、D6 永久矯正、D7 預防再發』、『有效性驗證 (Verification of Effectiveness)』。",
            "detailedExplanation": "此題為 ISO 主導稽核員（LA）實務必考題。考生必須展現對 Major NC 判定後果的清晰認識，以及 8D 閉環矯正流程的熟練應用。"
        },
        {
            "id": "sec-essay-16",
            "category": "sec",
            "chapter": "第 4 章：身分識別、存取控制與零信任架構（ZTA）",
            "title": "金融 FIDO2 / WebAuthn 無密碼強身分認證架構與防中間人（Anti-MITM）攻擊分析",
            "points": 25,
            "rubric": "1. 傳統 SMS/OTP 缺陷與反向代理釣魚威脅 (6分)；2. FIDO2 / WebAuthn 公私鑰非對稱認證機制 (8分)；3. Origin 綁定與防釣魚技術對照表 (7分)；4. 結論 (4分)",
            "question": "傳統以「帳號/密碼 + 簡訊 OTP / 軟體動態密碼」為基礎之雙因子認證（2FA），極易遭受即時反向代理（Reverse Proxy, 如 Evilginx）釣魚攻擊攔截 Session Token。請說明 FIDO Alliance 與 W3C 制定之 FIDO2 / WebAuthn 無密碼強認證標準架構，闡明用戶端設備（Client/Authenticator）如何運用晶片硬體產生金鑰對，並透過網域來源綁定（Origin Binding）徹底免疫中間人（MITM）釣魚攻擊？",
            "modelAnswer": """
<h4>一、破題：傳統多因子驗證之崩潰與反向代理釣魚危機</h4>
<p>傳統 2FA（如簡訊 SMS OTP、Email 驗證碼、TOTP Authenticator）在面對現代<strong>即時反向代理中間人攻擊（Adversary-in-the-Middle, AiTM）</strong>時存在結構性缺陷。攻擊者部署透明代理偽冒網站，用戶輸入之帳號、密碼及 OTP 均被即時截獲並轉發給正牌伺服器，奪取 Session Cookie 劫持會話。FIDO2 / WebAuthn 為當前唯一能從根本免疫 AiTM 釣魚之公鑰標準。</p>

<h4>二、FIDO2 / WebAuthn 認證核心架構與金鑰生命週期</h4>
<ol>
  <li><strong>雙層標準架構</strong>：
    包含 W3C <strong>WebAuthn（Web Authentication API）</strong>負責瀏覽器與依賴方（Relying Party, RP 伺服器）通訊；以及 FIDO <strong>CTAP2（Client to Authenticator Protocol）</strong>負責瀏覽器與硬體認證器（如 YubiKey、手機 Secure Enclave）通訊。
  </li>
  <li><strong>註冊階段（Registration）</strong>：
    用戶端產生非對稱金鑰對，私鑰<strong>牢固儲存於認證器硬體安全晶片內部（永不出境）</strong>；公鑰與憑證識別碼（Credential ID）發送並註冊至證交所 RP 伺服器。
  </li>
  <li><strong>認證階段與 Origin 綁定防釣魚機制</strong>：
    RP 伺服器發出隨機挑戰碼（Challenge）。瀏覽器將當前瀏覽器視窗之<strong>真實來源網域（Origin, 如 <code>https://trade.twse.com.tw</code>）</strong>封裝至 <code>clientDataJSON</code>，交由認證器簽章。認證器內部會比對儲存之 RP ID：
    - 若用戶誤入釣魚網域（如 <code>trade.twse-fake.com</code>），瀏覽器提交之 Origin 與認證器簽發之網域不符；<br>
    - 認證器拒絕簽發，或 RP 伺服器驗證簽名雜湊值時發現 Origin 不匹配立即阻斷！
  </li>
</ol>

<h4>三、傳統 2FA 機制 vs FIDO2 / WebAuthn 防護對比表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">比較構面</th>
      <th style="padding:6px 10px;">簡訊 SMS OTP</th>
      <th style="padding:6px 10px;">軟體 TOTP (Google Auth)</th>
      <th style="padding:6px 10px;">FIDO2 / WebAuthn (硬體/Passkey)</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">防反向代理中間人 (AiTM)</td>
      <td style="padding:6px 10px; color:#ef4444;">無防禦力 (可被轉發截獲)</td>
      <td style="padding:6px 10px; color:#ef4444;">無防禦力 (可被即時轉發)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">100% 免疫 (Origin 網域綁定)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">私鑰/秘密值保存機制</td>
      <td style="padding:6px 10px;">電信商簡訊傳遞 (SIM Swapping)</td>
      <td style="padding:6px 10px;">手機軟體記憶體共享金鑰</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">硬體安全元件 (TPM / SE) 永不導出</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">密碼洩漏風險</td>
      <td style="padding:6px 10px;">高 (仍需輸入帳號主密碼)</td>
      <td style="padding:6px 10px;">高 (仍需輸入主密碼)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">零 (真正無密碼 Passwordless)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">法遵與監理推薦</td>
      <td style="padding:6px 10px;">金管會逐步限縮核心業務使用</td>
      <td style="padding:6px 10px;">一般金融系統標準配置</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">金融資安行動方案 2.0 優先推薦標準</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>導入 FIDO2/WebAuthn 不僅達成極致無密碼便捷性，更從密碼學本質拔除釣魚憑證盜用之禍根，為證券交易下單提供無懈可擊之身分護城河。</p>
            """,
            "examinerTips": "評分亮點：『AiTM 反向代理釣魚 (如 Evilginx) 原理』、『WebAuthn + CTAP2 雙層架構』、『Origin 網域來源綁定（徹底破除釣魚中間人）』、『私鑰硬體安全晶片 (Secure Enclave) 永不出境』。",
            "detailedExplanation": "此題直指金管會『金融資安行動方案 2.0』中推動零信任與 FIDO 身分識別之核心，答題時務必寫出 Origin Binding 之防禦數學邏輯。"
        },
        {
            "id": "sec-essay-17",
            "category": "sec",
            "chapter": "第 6 章：應用系統安全、OWASP Top 10 與軟體安全生命週期",
            "title": "金融開放 API 安全防護規範（OWASP API Security Top 10）與 mTLS 雙向加密認證實踐",
            "points": 25,
            "rubric": "1. OWASP API Top 10 核心風險剖析 (7分)；2. BOLA 與 BOPLA 弱點成因與防禦架構 (8分)；3. mTLS 雙向認證與 OAuth 2.0 整合表 (6分)；4. 結論 (4分)",
            "question": "開放金融（Open Banking）與券商 API 下單時代來臨，API 成為外部威脅攻擊之首要目標。請依據 OWASP API Security Top 10 剖析「Broken Object Level Authorization (BOLA)」與「Broken Object Property Level Authorization (BOPLA)」之風險情境，並說明臺灣證券交易所在對接周邊機構與券商節點時，如何設計 API Gateway、mTLS（Mutual TLS）雙向憑證鑑別與 OAuth 2.0 MTLS Token 綁定架構以確保端對端傳輸安全？",
            "modelAnswer": """
<h4>一、破題：金融 API 暴露面之結構性安全挑戰</h4>
<p>隨著開放金融深化，傳統以 Web 頁面為主的防護思維無法阻擋針對 REST/JSON API 的攻擊。API 直接暴露業務物件與底層屬性，<strong>授權驗證疏漏（Broken Authorization）</strong>已躍居 API 安全漏洞之首。</p>

<h4>二、BOLA 與 BOPLA 弱點機制深度剖析</h4>
<ol>
  <li><strong>API1:2023 - 物件層級授權無效（BOLA, 原 IDOR）</strong>：
    攻擊者合法登入取得 Token 後，竄改 API 請求中之物件識別碼（如 <code>GET /api/v1/orders/10002</code> 改為 <code>10003</code>）。伺服器僅驗證了使用者為合法會員（驗證成功），但<strong>未校驗該使用者是否有權存取該特定 ID 物件</strong>，導致跨帳戶資料越權外洩。
  </li>
  <li><strong>API3:2023 - 物件屬性層級授權無效（BOPLA）</strong>：
    結合傳統大量指派（Mass Assignment）與過度資料暴露。API 端點接受客戶端傳入之 JSON 物件時，未嚴格白名單過濾屬性，攻擊者在委託請求中惡意夾帶 <code>"commissionRate": 0.0001</code> 或 <code>"isAdmin": true</code>，伺服器直接反射綁定並更新資料庫。
  </li>
</ol>

<h4>三、證交所金融級 API 安全閘道防護架構</h4>
<ol>
  <li><strong>雙向傳輸加密（mTLS, Mutual TLS）</strong>：
    在傳輸層不僅客戶端驗證證交所伺服器憑證，<strong>伺服器亦強制驗證券商客戶端憑證</strong>。私鑰儲存於券商 HSM 中，防範匿名呼叫與偽冒連線。
  </li>
  <li><strong>OAuth 2.0 憑證綁定（mTLS-Bound Access Tokens, RFC 8705）</strong>：
    發行之 Access Token 中注入客戶端 X.509 憑證指紋（Thumbprint）。若 Token 遭側錄，攻擊者因無法出示對應之客戶端憑證私鑰，API Gateway 將直接拒絕請求。
  </li>
</ol>

<h4>四、OWASP API 核心風險防護對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">風險類別</th>
      <th style="padding:6px 10px;">漏洞成因</th>
      <th style="padding:6px 10px;">攻擊手法示範</th>
      <th style="padding:6px 10px;">防禦與治理對策</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">API1: BOLA</td>
      <td style="padding:6px 10px;">代碼未校驗用戶與資源物件之所有權歸屬</td>
      <td style="padding:6px 10px;">遞增替換 URL 中之訂單編號 Order_ID</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">在資料庫查詢強制注入 <code>WHERE user_id = current_user</code></td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">API3: BOPLA</td>
      <td style="padding:6px 10px;">反序列化時盲目綁定用戶傳入的所有 JSON 欄位</td>
      <td style="padding:6px 10px;">在下單 JSON 額外注入 <code>is_vip: true</code></td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">嚴格使用 DTO (Data Transfer Object) 白名單過濾</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">API4: 資源耗盡</td>
      <td style="padding:6px 10px;">缺乏速率限制 (Rate Limiting) 與請求大小限制</td>
      <td style="padding:6px 10px;">高頻發送巨大批次委託查詢瘫瘓後端</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">API Gateway 實施權杖桶 (Token Bucket) 限流</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>金融 API 的防護是一場全鏈路縱深防禦，必須結合架構層之 mTLS/OAuth2 綁定與程式碼層之嚴格 DTO 驗證，杜絕任何越權存取破口。</p>
            """,
            "examinerTips": "踩分重點：『BOLA 物件層級授權失效原理』、『BOPLA 屬性大量指派風險』、『mTLS 雙向憑證認證』、『RFC 8705 mTLS-bound Access Tokens』。",
            "detailedExplanation": "API 安全近年在證券業甄試極具熱度。考生務必寫出 mTLS 與 OAuth 2.0 結合之 RFC 8705 標準，展現頂級金融通訊架構視野。"
        },
        {
            "id": "sec-essay-18",
            "category": "sec",
            "chapter": "第 10 章：雲原生與容器安全、DevSecOps 實務",
            "title": "金融軟體供應鏈安全（Software Supply Chain）：SBOM（SPDX/CycloneDX）、SLSA 框架與相依性漏洞管理",
            "points": 25,
            "rubric": "1. 軟體供應鏈攻擊途徑與危害 (6分)；2. SBOM 格式比較（SPDX vs CycloneDX）(7分)；3. SLSA (Supply-chain Levels for Software Artifacts) 四級模型 (8分)；4. 結論 (4分)",
            "question": "近年開源套件投毒（Typosquatting、Dependency Confusion）與建置管線遭竄改事件頻傳。臺灣金融監督管理委員會要求關鍵金融機構落實軟體供應鏈安全。請說明何謂軟體物料清單（SBOM, Software Bill of Materials），比較 SPDX 與 CycloneDX 之技術特點，並詳述如何導入 Google 倡議之 SLSA 框架（Supply-chain Levels for Software Artifacts）於 CI/CD 流水線中，以密碼學簽署（Cosign/Sigstore）證明建置完整性？",
            "modelAnswer": """
<h4>一、破題：軟體供應鏈威脅態勢升溫</h4>
<p>自 SolarWinds 與 Log4j 事件以來，攻擊者不再直接正面攻擊高防護之生產系統，轉而<strong>攻擊軟體開發上游、開源相依套件與 CI/CD 建置管線</strong>。一旦上游受污染，下游金融機構將在毫不知情下編譯並運行惡意後門。</p>

<h4>二、軟體物料清單（SBOM）技術實踐</h4>
<ol>
  <li><strong>SBOM 定義</strong>：
    宛如食品成分標籤，詳列軟體產品中包含之所有直接與遞移相依套件（Direct & Transitive Dependencies）、版本號、授權條款（License）與雜湊校驗碼。
  </li>
  <li><strong>兩大標準格式對照</strong>：
    - <strong>SPDX（Software Package Data Exchange）</strong>：由 Linux Foundation 主導，ISO/IEC 5962:2021 國際標準，重在開源合規與授權智財權追蹤；<br>
    - <strong>CycloneDX</strong>：由 OWASP 主導，專為<strong>資安弱點分析與威脅建模</strong>量身打造，原生支援漏洞追蹤（VEX, Vulnerability Exploitability eXchange）。
  </li>
</ol>

<h4>三、SLSA 框架（Supply-chain Levels for Software Artifacts）落地建設</h4>
<p>SLSA 提供一套防止軟體加工各階段竄改之安全評級階梯：</p>
<ol>
  <li><strong>建置環境隔離（Isolated Build）</strong>：建置任務必須在拋棄式、純淨的容器沙盒中執行，禁止建置腳本訪問外部不可信網路。</li>
  <li><strong>不可變來源追蹤（Provenance）</strong>：產生密碼學保證之建置憑證（Build Provenance），詳細記錄建置時之 Git Commit SHA、建置參數與環境雜湊。</li>
  <li><strong>成品簽章（Cosign / Sigstore）</strong>：使用無金鑰（Keyless）或 HSM 保護之金鑰對容器映像檔與產出二進位檔進行<strong>數位簽章</strong>。Kubernetes 準入控制器（Admission Controller）透過 Kyverno 驗證簽章，未經認證之映像檔一律拒絕部署！</li>
</ol>

<h4>四、SPDX vs CycloneDX 與 SLSA 等級全貌表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">比較構面</th>
      <th style="padding:6px 10px;">SPDX 格式</th>
      <th style="padding:6px 10px;">CycloneDX 格式</th>
      <th style="padding:6px 10px;">SLSA 核心對應等級</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">主導組織與標準</td>
      <td style="padding:6px 10px;">Linux Foundation (ISO/IEC 5962)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">OWASP 基金會</td>
      <td style="padding:6px 10px;">Google / OpenSSF 聯盟</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">核心應用強項</td>
      <td style="padding:6px 10px;">開源授權合規、智財權盤點</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">漏洞風險分析、VEX 漏洞狀態通報</td>
      <td style="padding:6px 10px;">CI/CD 管線防竄改與產物真偽驗證</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">防禦關鍵技術</td>
      <td style="padding:6px 10px;">套件哈希校驗、授權條款解析</td>
      <td style="padding:6px 10px;">結合 SCA 工具 (Grype/Trivy) 掃描</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">Cosign 簽名 + In-toto 證明鏈 + Kyverno 攔截</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>在金融 DevSecOps 時代，「代碼即資產、產物即合規」。導入 SBOM 與 SLSA 體系，方能確保證交所核心系統之每行代碼與每個二進位執行檔皆可溯源、無毒且不容竄改。</p>
            """,
            "examinerTips": "評分核心：『SBOM 定義與價值』、『SPDX (授權合規) vs CycloneDX (資安弱點/VEX)』、『SLSA 框架與 Build Provenance』、『Cosign/Sigstore 數位簽署防部署竄改』。",
            "detailedExplanation": "軟體供應鏈安全是近年各國政府監理（包括美國行政命令 EO 14028 及臺灣金融資安行動方案）力推的重點，務必講出 CycloneDX 與 SLSA 的實戰應用。"
        },
        {
            "id": "sec-essay-19",
            "category": "sec",
            "chapter": "第 5 章：現代密碼學、公鑰基礎設施（PKI）與硬體安全模組",
            "title": "金融實體伺服器硬體安全：TPM 2.0 晶片、安全開機（Secure Boot）信任鏈與韌體微碼加固",
            "points": 25,
            "rubric": "1. 實體信任根（Root of Trust）原理 (7分)；2. TPM 2.0 PCR 暫存器度量開機與密封機制 (8分)；3. 開機防禦技術對照表 (6分)；4. 結論 (4分)",
            "question": "高階持續性威脅（APT）日益轉向作業系統底層，利用開機磁區（Bootkit）或 UEFI 韌體漏洞繞過常規防毒軟體。請說明伺服器硬體層信任根（Root of Trust, RoT）之運作機制，闡述 TPM 2.0 晶片之平台組態暫存器（Platform Configuration Registers, PCR）度量開機（Measured Boot）與密封（Sealing）原理，並規劃證交所金融交易伺服器之 UEFI Secure Boot 信任鏈與韌體防護策略。",
            "modelAnswer": """
<h4>一、破題：作業系統以下（Below-the-OS）的致命盲區</h4>
<p>傳統端點防毒與 EDR 軟體均運行於作業系統核心（Ring 0）或使用者空間（Ring 3）。若攻擊者藉由韌體漏洞植入 <strong>UEFI Rootkit/Bootkit</strong>（運行於 Ring -2 SMM 模式），惡意程式在作業系統啟動前即已掌握控制權，導致作業系統層面的所有資安防護全數失效。</p>

<h4>二、硬體信任根與 TPM 2.0 度量防護機制</h4>
<ol>
  <li><strong>硬體信任根（Hardware Root of Trust, RoT）</strong>：
    由不可變的晶片硬體邏輯（如 CPU 熔絲或安全微控制器晶片，如 Intel Boot Guard / AMD PSB）作為開機檢驗的起點，確保第一段執行的微碼絕對可信。
  </li>
  <li><strong>UEFI 安全開機信任鏈（Secure Boot Chain of Trust）</strong>：
    依循<strong>「先驗證後執行（Verify before Execute）」</strong>原則：
    - 主機板 ROM (PK) 驗證 KEK -> KEK 驗證 db 資料庫之證書 -> db 證書驗證開機引導程式（SHIM / GRUB）之數位簽名 -> GRUB 驗證 Linux 核心內核簽名；<br>
    - 鏈條中任何環節簽章無效，硬體立即中止開機。
  </li>
  <li><strong>TPM 2.0 度量開機（Measured Boot）與金鑰密封（Sealing）</strong>：
    - <strong>PCR 暫存器度量（Hash Extension）</strong>：開機每階段組件（BIOS、Option ROM、MBR、Kernel）之雜湊值均以 <code>PCR_new = SHA256(PCR_old || Component_Hash)</code> 累積寫入 TPM PCR 暫存器（只可延伸不可竄改）；<br>
    - <strong>金鑰密封（Data Sealing）</strong>：將金融交易系統的硬碟加密金鑰（LUKS Key）密封於 TPM 晶片中，並<strong>綁定特定 PCR 期望狀態</strong>。若伺服器韌體遭竄改或硬碟被拔至他機，PCR 數值不符，TPM 拒絕釋放解密金鑰，硬碟資料保持完全加密！
  </li>
</ol>

<h4>三、傳統開機 vs Secure Boot vs Measured Boot 對比表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">機制</th>
      <th style="padding:6px 10px;">防護目標</th>
      <th style="padding:6px 10px;">核心執行動作</th>
      <th style="padding:6px 10px;">異常處理結果</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">傳統 BIOS</td>
      <td style="padding:6px 10px;">無防護</td>
      <td style="padding:6px 10px;">直接執行 MBR 第一磁區程式碼</td>
      <td style="padding:6px 10px; color:#ef4444;">無條件執行惡意 Bootkit</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">UEFI Secure Boot</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">防止未經簽章之韌體與核心引導</td>
      <td style="padding:6px 10px;">逐層驗證 X.509 數位簽名 (PK->KEK->db)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">阻斷開機流程，拒絕啟動</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">TPM 2.0 Measured Boot</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">記錄開機狀態並保護靜態硬碟加密金鑰</td>
      <td style="padding:6px 10px;">將各階段組件雜湊累積至 PCR 暫存器</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">拒絕解鎖金鑰 (Unseal)，防資料外洩</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>在證券交易所核心伺服器導入「Secure Boot + TPM 2.0 度量密封」，成功將安全邊界由作業系統向上推至晶片矽層（Silicon-level），建構不可撼動之物理級資安防禦基石。</p>
            """,
            "examinerTips": "評分亮點：『Below-the-OS 威脅危害』、『硬體信任根 (Root of Trust)』、『Secure Boot 信任鏈 (PK->KEK->db->GRUB->Kernel)』、『TPM 2.0 PCR 雜湊延伸 (Hash Extension) 與金鑰密封 (Sealing) 原理』。",
            "detailedExplanation": "硬體與韌體安全是當前高階金融主機維運的核心考科。考生能清楚推導 PCR 運算式與 LUKS 解密金鑰的關聯，即可獲得 23 分以上滿分評價。"
        },
        {
            "id": "sec-essay-20",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金融機敏交易資料去識別化（De-identification）、資料遮蔽（Masking）與差分隱私法遵實踐",
            "points": 25,
            "rubric": "1. 個資法與金融機敏資料法遵規範 (6分)；2. 去識別化技術原理（動態/靜態遮蔽/Tokenization）(8分)；3. k-匿名、l-多樣性與差分隱私（Differential Privacy）數學意涵 (7分)；4. 結論 (4分)",
            "question": "依據個人資料保護法及金管會「金融機構運用新興科技作業規範」，金融機構於進行大數據分析、模型訓練或委外開發測試時，嚴禁使用未經去識別化之客戶個人身分資訊與交易明細。請深入分析「靜態資料遮蔽（Static Data Masking）」、「動態資料遮蔽（Dynamic Data Masking）」與「權杖化（Tokenization）」之適用場景與密碼學保證，並說明 k-Anonymity 與差分隱私之數學防護意涵。",
            "modelAnswer": """
<h4>一、破題：金融資料共享與隱私合規之兩難</h4>
<p>在數位金融與 AI 時代，金融機構欲運用交易大數據進行量化分析或將系統委外維護，必須面臨《個人資料保護法》及《營業秘密法》之嚴格制約。<strong>去識別化（De-identification）技術</strong>是確保「資料可用但個人不可逆重識別」之核心科技。</p>

<h4>二、去識別化核心技術架構比較</h4>
<ol>
  <li><strong>靜態資料遮蔽（SDM, Static Data Masking）</strong>：
    在資料自正式生產庫複製至測試或分析庫時，透過批次作業執行<strong>不可逆永久替換</strong>（如加鹽雜湊、混淆置換、特定字元置換 <code>A123***789</code>）。適用於開發測試環境，徹底根除測試庫外洩風險。
  </li>
  <li><strong>動態資料遮蔽（DDM, Dynamic Data Masking）</strong>：
    生產庫中的底層資料保持明文不變，在資料庫回應客戶端查詢時，<strong>依據連線身分權限即時改寫回傳結果</strong>（如一般客服查詢顯示遮蔽身分證，受授權稽核人員顯示明文）。優點是不變動儲存，缺點是特權 DBA 仍可能看見明文。
  </li>
  <li><strong>權杖化（Tokenization）</strong>：
    將機敏資料（如信用卡卡號、身分證字號）替換為格式相容但毫無數學關聯之隨機亂數（Token）。真實資料與 Token 映射表儲存於高度隔離之「Token Vault（金鑰庫）」內。即使 Token 遭到外洩，攻擊者亦無法透過任何密碼學推算還原原始數值。
  </li>
</ol>

<h4>三、進階隱私保護理論：k-Anonymity vs 差分隱私（Differential Privacy）</h4>
<ol>
  <li><strong>k-匿名（k-Anonymity）</strong>：
    在發布之資料集中，對於任何準識別碼（Quasi-Identifier, 如年齡、性別、郵遞區號）組合，<strong>至少存在 k 筆相同記錄</strong>，使攻擊者無法以低於 <code>1/k</code> 之機率鎖定特定自然人。進階擴展包含防範屬性同質攻擊的 <strong>l-Diversity</strong>。
  </li>
  <li><strong>差分隱私（Differential Privacy, DP）</strong>：
    基於嚴謹數學機率論，在查詢結果中注入經過精準計算的<strong>拉普拉斯雜訊（Laplace Noise）</strong>。保證「在資料集中包含或剔除特定某位用戶時，輸出統計結果的分佈機率差異不超過參數 <code>e^ε</code>（隱私預算 ε）」，徹底防禦差分重構攻擊！
  </li>
</ol>

<h4>四、去識別化技術全構面對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">技術機制</th>
      <th style="padding:6px 10px;">資料可逆性</th>
      <th style="padding:6px 10px;">效能與儲存開銷</th>
      <th style="padding:6px 10px;">證交所最佳實務應用情境</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">靜態遮蔽 (SDM)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">完全不可逆</td>
      <td style="padding:6px 10px;">離線批次轉換，運行零開銷</td>
      <td style="padding:6px 10px;">下包外包商研發測試環境資料庫遮蔽</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">動態遮蔽 (DDM)</td>
      <td style="padding:6px 10px;">儲存維持明文，依角色即時隱蔽</td>
      <td style="padding:6px 10px;">增加資料庫查詢 CPU 處理開銷</td>
      <td style="padding:6px 10px;">內部臨櫃交易與客服人員權限審閱</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">權杖化 (Tokenization)</td>
      <td style="padding:6px 10px;">透過 Vault 受控單向映射可逆</td>
      <td style="padding:6px 10px;">需維護龐大 Vault 映射庫與金鑰</td>
      <td style="padding:6px 10px;">跨金融機構下單帳號與身分代碼流轉</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">差分隱私 (DP)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">群體統計輸出，完全無法還原個體</td>
      <td style="padding:6px 10px;">需計算敏感度並注入數學雜訊</td>
      <td style="padding:6px 10px;">大數據市場總交易趨勢與量化研究發布</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>金融去識別化不可一概而論，必須依業務情境動態組合 SDM、Tokenization 與差分隱私，方能達成兼顧業務前瞻發展與法遵底線之雙贏格局。</p>
            """,
            "examinerTips": "評分核心：『SDM (不可逆測試庫) vs DDM (角色動態呈現) vs Tokenization (隨機映射庫)』、『k-Anonymity (準識別碼至少 k 筆相同)』、『差分隱私 (Laplace 雜訊與隱私預算 ε)』。",
            "detailedExplanation": "此題涵蓋個資法合規與大數據安全技術，考生若能精確寫出差分隱私注入雜訊之數學意義，展現深厚理論功底，必獲高分。"
        }
    ]

def get_more_sec_essays_21_to_32():
    return [
        {
            "id": "sec-essay-21",
            "category": "sec",
            "chapter": "第 11 章：紅藍隊演練、滲透測試與漏洞管理",
            "title": "內網橫向移動（Lateral Movement）偵測：Pass-the-Hash / Kerberoasting 原理與 HoneyToken 蜜罐誘捕防禦",
            "points": 25,
            "rubric": "1. 內網認證協定弱點（NTLM / Kerberos）(7分)；2. Pass-the-Hash 與 Kerberoasting 攻擊路徑 (8分)；3. AD 分級防護與 HoneyToken 誘捕表 (6分)；4. 結論 (4分)",
            "question": "在金融機構內部網路環境中，一旦邊界端點遭受滲透，攻擊者常利用 Windows Active Directory（AD）網域之協定特性進行橫向移動與特權提升。請分析 Pass-the-Hash（PtH）與 Kerberoasting 攻擊技術之底層原理與封包行為，並說明防禦方如何透過 Active Directory 階層式管理（Tiering Model）、gMSA（群組受信任服務帳號）以及部署 HoneyToken（誘餌帳號/密鑰）實現高保真度之早期預警與主動誘捕？",
            "modelAnswer": """
<h4>一、破題：內網特權邊界失守的骨牌效應</h4>
<p>在成熟的企業內網中，攻擊者很少需要使用昂貴的零日漏洞（Zero-Day），而是利用<strong>身分憑證濫用（Living off the Land）</strong>，在記憶體中撈取憑證快取，藉由合法協定在網域內伺服器間橫向擴散，直指網域控制站（Domain Controller）。</p>

<h4>二、Pass-the-Hash 與 Kerberoasting 攻擊原理剖析</h4>
<ol>
  <li><strong>Pass-the-Hash（PtH，雜湊傳遞攻擊）</strong>：
    - <strong>底層原理</strong>：Windows NTLM 認證協定在計算驗證回應時，僅需<strong>使用者密碼的 NTLM Hash</strong>，而無需明文密碼；<br>
    - <strong>攻擊手法</strong>：攻擊者以 Mimikatz 從受害端點之 LSASS 記憶體中轉儲出 NTLM Hash，直接將該雜湊注入自己的連線 Session 中呼叫 SMB/WMI/RPC，冒充網域管理員登入其他主機。
  </li>
  <li><strong>Kerberoasting（服務票證離線破解）</strong>：
    - <strong>底層原理</strong>：網域中任何普通合法用戶均可向金鑰發行中心（KDC）請求針對特定服務主要名稱（SPN）的票證授權服務票據（TGS Ticket）；<br>
    - <strong>致命缺陷</strong>：該 TGS 票據是使用<strong>目標服務帳號的 NTLM 密碼雜湊</strong>進行 RC4/AES 加密的。攻擊者取得 TGS 後，直接匯出至離線 GPU 叢集使用 Hashcat 進行無限制暴力字典破解，一旦破解即可取得服務帳號密碼！
  </li>
</ol>

<h4>三、防禦實踐：AD 階層模型與 HoneyToken 主動誘捕</h4>
<ol>
  <li><strong>Active Directory 階層式管理（Tiering Model）</strong>：
    嚴格劃分 <strong>Tier 0（網域控制器、PKI）</strong>、<strong>Tier 1（企業核心伺服器、交易庫）</strong>與 <strong>Tier 2（終端使用者電腦）</strong>。明文規定高層級憑證嚴禁登入低層級設備（使用 Protected Users 組與憑證防衛 Credential Guard），杜絕 LSASS 雜湊洩漏。
  </li>
  <li><strong>群組受管理服務帳號（gMSA）</strong>：
    全面替換傳統 SPN 弱密碼服務帳號，改用 gMSA，密碼長度由 AD 自動生成為 120 碼隨機字元並定期自動更換，徹底無效化 Kerberoasting 離線破解。
  </li>
  <li><strong>HoneyToken（誘餌帳號與誘餌金鑰）主動防禦</strong>：
    在端點記憶體或設定檔中植入偽造的「誘餌網域管理員帳號（如 <code>svc-twse-admin</code>）」。此帳號無任何真實業務功能，一旦 SIEM/SOC 偵測到有任何伺服器發起該誘餌帳號的 Kerberos 請求，即可<strong>100% 判定內網存在橫向移動攻擊</strong>，達成零誤報即時阻斷！
  </li>
</ol>

<h4>四、PtH vs Kerberoasting 攻防對比表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">攻擊手法</th>
      <th style="padding:6px 10px;">攻擊協定</th>
      <th style="padding:6px 10px;">利用之底層弱點</th>
      <th style="padding:6px 10px;">防禦與誘捕最佳對策</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">Pass-the-Hash (PtH)</td>
      <td style="padding:6px 10px;">NTLM / SMB / RPC</td>
      <td style="padding:6px 10px;">LSASS 殘留 NTLM 雜湊直接作為認證憑據</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">啟用 Credential Guard、停用 NTLM、AD 階層隔離</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">Kerberoasting</td>
      <td style="padding:6px 10px;">Kerberos TGS</td>
      <td style="padding:6px 10px;">任何普通用戶皆可申請 SPN TGS 並離線破解</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">強制採用 gMSA、設定 25 字元以上強密碼、AES 強加密</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">HoneyToken 誘捕</td>
      <td style="padding:6px 10px;">全協定偵測</td>
      <td style="padding:6px 10px;">攻擊者無差別掃描並嘗試利用高權限帳號</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">佈建虛假高權限 SPN 帳號，觸發即連鎖 SOAR 隔離</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>在面對內網進階威脅時，防禦思維必須自被動圍堵進化為「假定已遭滲透（Assume Breach）」，透過嚴密之身分階層架構與主動誘捕蜜罐，在橫向擴散早期精準殲滅威脅。</p>
            """,
            "examinerTips": "評分重點：『Pass-the-Hash 免密碼利用 NTLM Hash 登入原理』、『Kerberoasting 利用 SPN TGS 離線暴力破解』、『AD Tiering Model (Tier 0/1/2) 憑證隔離』、『HoneyToken 誘餌零誤報警報機制』。",
            "detailedExplanation": "橫向移動為金融紅隊演練與實戰中最具殺傷力的環節。此答案完整闡述攻擊協定弱點與主動誘捕對策，展現頂級藍隊防禦工程能力。"
        },
        {
            "id": "sec-essay-22",
            "category": "sec",
            "chapter": "第 7 章：網路防禦、三層式 DDoS 緩解與金融級邊界防護",
            "title": "金融網路微隔離（Micro-Segmentation）架構規劃：以軟體定義與標籤策略落實東西向流量零信任",
            "points": 25,
            "rubric": "1. 傳統南北向防護之東西向盲點分析 (6分)；2. 微隔離技術架構與標籤策略 (8分)；3. 微隔離技術方案比較表 (7分)；4. 結論 (4分)",
            "question": "傳統金融資料中心主要依賴實體邊界防火牆管制南北向（North-South）進出流量，一旦內部受害節點遭植入後門，東西向（East-West）伺服器間橫向擴散將難以防堵。請規劃一套基於「微隔離（Micro-Segmentation）」之金融網路防護架構，說明以工作負載身分標籤（Workload Identity & Tags）取代傳統靜態 IP/VLAN 規則之優勢，並分析其在撮合、結算、資料庫不同信任層級間之部署實務。",
            "modelAnswer": """
<h4>一、破題：資料中心「雞蛋殼模型」的終結</h4>
<p>傳統資料中心安全架構宛如「堅硬外殼、鬆軟內部（Hard Perimeter, Soft Interior）」。南北向防火牆守住邊界，但同一 VLAN 內成百上千台主機互通無阻。現代零信任架構要求推動<strong>微隔離（Micro-Segmentation）</strong>，將網路安全防界線細化收縮至<strong>每一台虛擬機器或容器之虛擬網卡（vNIC）層級</strong>。</p>

<h4>二、微隔離技術架構與標籤化存取控制</h4>
<ol>
  <li><strong>擺脫靜態 IP/VLAN 之動態標籤模型</strong>：
    傳統 ACL 依賴靜態 IP，當伺服器因彈性擴容或漂移改變 IP 時，防護規則極易脫節出錯。微隔離採用多維度<strong>工作負載身分標籤（Tags / Metadata）</strong>，例如：<br>
    - <code>Role = Matching-Engine</code>（撮合引擎）；<br>
    - <code>Env = Production</code>（生產環境）；<br>
    - <code>DataClassification = Confidential</code>（機密資料）。<br>
    安全原則定義為：「僅允許 <code>Role = Order-Gateway</code> 透過 TCP/9000 存取 <code>Role = Matching-Engine</code>」，無論主機 IP 為何，規則動態即時生效。
  </li>
  <li><strong>分層控制實踐（撮合 vs 結算 vs 數據庫）</strong>：
    - <strong>撮合核心區</strong>：實施白名單完全隔離，除下單閘道器之撮合連線外，禁止所有外部直接存取（包含阻斷任何連往網際網路之連線）；<br>
    - <strong>資料庫區</strong>：僅開放應用中台伺服器特定連接埠，跨主機間禁止任何平級 SSH/RDP/SMB 連通；<br>
    - <strong>管理平面隔離</strong>：僅允許由指定 PAM 跳板機發起經認證之管理連線，徹底防堵蠕蟲式橫向傳播。
  </li>
</ol>

<h4>三、微隔離主流實作架構對比表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">架構型態</th>
      <th style="padding:6px 10px;">實現技術核心</th>
      <th style="padding:6px 10px;">優點</th>
      <th style="padding:6px 10px;">挑戰與限制</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">主機代理型 (Host-Agent)</td>
      <td style="padding:6px 10px;">於各主機核心安裝 Agent 調控 iptables/Windows WFP</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">跨多雲/實體機/虛擬機統一治理，支援行程級識別</td>
      <td style="padding:6px 10px;">需在每台主機安裝 Agent，極限超低延遲撮合需精細調校</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">虛擬化管理層 (Hypervisor)</td>
      <td style="padding:6px 10px;">VMware NSX 分散式防火牆 (DFW) 於 vSwitch 攔截</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">無侵入主機 (Agentless)，在虛擬網卡硬性攔截</td>
      <td style="padding:6px 10px;">受限於單一虛擬化平台，無法直接控管裸金屬實體機</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">雲原生 CNI (eBPF)</td>
      <td style="padding:6px 10px;">Cilium 於 Linux Kernel 透過 eBPF 攔截封包</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">K8s 原生標籤匹配，效能極高無 iptables 鏈開銷</td>
      <td style="padding:6px 10px;">僅適用於 Linux 容器化叢集環境</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>落實微隔離為金融零信任架構中不可或缺的網路支柱。透過身分標籤與預設拒絕（Default Deny）白名單策略，能將單點滲透的爆炸半徑（Blast Radius）嚴格限縮在最小單元內。</p>
            """,
            "examinerTips": "評分亮點：『傳統南北向防護缺陷 vs 東西向微隔離』、『標籤化 (Tags/Identity) 取代靜態 IP/VLAN 規則』、『白名單預設拒絕 (Default Deny) 限制爆炸半徑』、『Agent vs Hypervisor vs eBPF CNI 選型對照』。",
            "detailedExplanation": "微隔離是現代金融資料中心防勒索軟體橫向擴散的最佳解法。答題時展現對標籤化規則維護與不同實現方式的理解即可穩拿滿分。"
        },
        {
            "id": "sec-essay-23",
            "category": "sec",
            "chapter": "第 8 章：資安監控維運（SOC）、SIEM/SOAR 與威脅獵捕",
            "title": "金融資安監控之使用者與實體設備行為分析（UEBA）與機器學習異常偵測模型落地",
            "points": 25,
            "rubric": "1. 傳統規則比對（Rule-based）瓶頸 (6分)；2. UEBA 基準線建立與特徵工程 (8分)；3. UEBA 偵測情境矩陣表 (7分)；4. 結論 (4分)",
            "question": "傳統 SIEM 依賴靜態相關規則（Correlation Rules），難以偵測低慢速（Low and Slow）攻擊、合法憑證遭竊取（Living off the Land）或內部人員（Insider Threat）異常盜拷行為。請闡述使用者與實體設備行為分析（UEBA, User and Entity Behavior Analytics）之運作架構，說明其如何透過同儕群組分析（Peer Group Analysis）、時間序列異常（Time-Series Anomaly）與風險評分（Risk Scoring），於金融核心系統精準捕捉未授權行為？",
            "modelAnswer": """
<h4>一、破題：傳統 SIEM 的告警疲勞與偵測盲區</h4>
<p>傳統 SIEM 依賴靜態閾值規則（如「5 分鐘內失敗登入大於 10 次」），攻擊者只需以低慢速頻率（每 10 分鐘嘗試 1 次）或直接使用竊得之合法管理員帳號，即可輕易規避規則。<strong>UEBA（使用者與實體設備行為分析）</strong>運用機器學習演算法，將焦點由「已知攻擊特徵」轉向<strong>「正常行為基準線（Baseline）之異常偏離」</strong>。</p>

<h4>二、UEBA 核心分析引擎與偵測技術架構</h4>
<ol>
  <li><strong>行為特徵工程與基準線建立</strong>：
    收集身分認證日誌、VPN 連線、端點行程執行及資料庫存取歷史，運用非監督式機器學習建立個別帳號與設備的長期行為畫像（Profile）：包含常用登入時段、登入地點、常存取的主機及傳輸資料量平均值。
  </li>
  <li><strong>同儕群組分析（Peer Group Analysis）</strong>：
    單看個人歷史可能不足，UEBA 自動將職能相近者歸為同儕（如「一般櫃員組」、「撮合主機維運組」）。若某位櫃員突發存取高階資料庫匯出指令，雖然其個人可能首次執行，但系統比對其所屬同儕群組從未有人執行此動作，立即判定為嚴重異常。
  </li>
  <li><strong>動態風險評分（Risk Scoring Engine）</strong>：
    避免單一異常引發大量誤報，UEBA 採用<strong>風險評分聚合模型</strong>：<br>
    - 「非典型時段自異常 IP 登入」：風險分數 +30；<br>
    - 「查詢非日常業務範圍之交易資料表」：風險分數 +40；<br>
    - 「單次匯出超過 50,000 筆客戶資料」：風險分數 +50。<br>
    當帳號總風險分數在 24 小時內累積突破閾值（如 100 分），系統自動觸發高優先級重大事件，並聯動 SOAR 自動吊銷該帳號 Session！
  </li>
</ol>

<h4>三、靜態 SIEM 規則 vs 機器學習 UEBA 分析能力矩陣表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">比較構面</th>
      <th style="padding:6px 10px;">傳統 SIEM 靜態規則</th>
      <th style="padding:6px 10px;">UEBA 行為分析引擎</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">偵測核心邏輯</td>
      <td style="padding:6px 10px;">已知特徵、布林邏輯、固定時間窗口閾值</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">動態行為基準線、統計偏差、機器學習模型</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">合法帳號遭竊防禦</td>
      <td style="padding:6px 10px; color:#ef4444;">無效 (合法憑證視為正常交易)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">強大 (精準識別不合常理的時空與操作偏離)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">內部威脅與內鬼偵測</td>
      <td style="padding:6px 10px; color:#ef4444;">難以發現緩慢漸進竊密</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">透過同儕比對與資料外傳異常敏銳捕捉</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">誤報率 (False Positive)</td>
      <td style="padding:6px 10px;">高 (易引發資安人員告警疲勞)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">低 (多維度風險評分聚合驗證)</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>在資安戰場上，攻擊者使用合法帳號登入系統已成常態。透過 UEBA 動態行為基準線與同儕分析，證交所 SOC 監控中心得以突破傳統特徵比對極限，有效抵禦最隱蔽的特權盜用威脅。</p>
            """,
            "examinerTips": "踩分重點：『靜態規則 (Correlation) 面對合法憑證竊取與慢速攻擊之失效』、『UEBA 動態基準線 (Baseline)』、『同儕群組分析 (Peer Group Analysis)』、『動態累積風險評分 (Risk Scoring) 聯動 SOAR』。",
            "detailedExplanation": "UEBA 代表現代金融次世代 SOC (Next-Gen SOC) 的頂尖戰力。答題時結合具體金融場景（如特權 DBA 異常匯出）能使論述極具說服力。"
        },
        {
            "id": "sec-essay-24",
            "category": "sec",
            "chapter": "第 10 章：雲原生與容器安全、DevSecOps 實務",
            "title": "雲端資安態勢管理（CSPM）與雲端工作負載保護平台（CWPP）在金融混合雲之建置實務",
            "points": 25,
            "rubric": "1. 金融混合雲資安治理挑戰 (6分)；2. CSPM 靜態組態漂移稽核架構 (7分)；3. CWPP 運行時行為防護與比較表 (8分)；4. 結論 (4分)",
            "question": "證券期貨業漸進邁向混合雲（Hybrid Cloud）架構，但因多雲管理介面異質性與組態錯誤（Misconfiguration）頻繁，容易引發雲端資料外洩。請深入剖析「雲端資安態勢管理（CSPM）」與「雲端工作負載保護平台（CWPP）」之核心功能差異，並針對證交所關鍵系統在雲端執行環境中，說明如何落實雲端資產發現、組態合規自動修復及運行時惡意行為阻斷？",
            "modelAnswer": """
<h4>一、破題：雲端安全責任共擔模型與多雲治理挑戰</h4>
<p>依據 Gartner 統計，高達 99% 的雲端資安事故源於<strong>客戶端之組態設定錯誤（Misconfiguration）與權限過大</strong>，而非雲端服務商底層漏洞。金融機構導入混合雲時，必須在管理平面與運行平面分別部署 <strong>CSPM（雲端資安態勢管理）</strong>與 <strong>CWPP（雲端工作負載保護平台）</strong>。</p>

<h4>二、CSPM 與 CWPP 雙軌防護體系深度剖析</h4>
<ol>
  <li><strong>CSPM（Cloud Security Posture Management，態勢管理層）</strong>：
    - <strong>運作機制</strong>：透過雲端 API 以無代理（Agentless）方式對多雲控制平面進行靜態掃描與分析；<br>
    - <strong>核心功能</strong>：即時盤點雲端資產清單、比對法規合規基準（如 CIS Benchmarks、ISO 27001、金管會規範）、偵測公開暴露的儲存桶（如 S3/Blob 桶權限公開）、寬鬆安全群組（SG 0.0.0.0/0 開放 SSH/RDP）；<br>
    - <strong>自動修復（Auto-Remediation）</strong>：發現組態漂移（Drift）時，自動觸發 Lambda/Function 關閉公開權限。
  </li>
  <li><strong>CWPP（Cloud Workload Protection Platform，運行時防護層）</strong>：
    - <strong>運作機制</strong>：在虛擬主機、容器（Pod）或無伺服器環境中安裝輕量 Agent 或透過 eBPF 深入作業系統核心；<br>
    - <strong>核心功能</strong>：專注於<strong>工作負載內部之運行時保護（Runtime Protection）</strong>。防禦記憶體無檔案攻擊、反向 Shell（Reverse Shell）、非法行程生成、CVE 漏洞入侵與特權逃逸（Privilege Escalation）。
  </li>
</ol>

<h4>三、CSPM vs CWPP vs CIEM 多雲安全三劍客對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">平台類別</th>
      <th style="padding:6px 10px;">防護焦點與維度</th>
      <th style="padding:6px 10px;">部署與收集手法</th>
      <th style="padding:6px 10px;">典型阻斷威脅場景</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">CSPM (態勢管理)</td>
      <td style="padding:6px 10px;">雲端控制平面之靜態架構與組態設定</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">API 連接無代理 (Agentless)，每小時巡檢</td>
      <td style="padding:6px 10px;">儲存桶未加密、管理埠公開暴露、未啟用日誌</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">CWPP (負載保護)</td>
      <td style="padding:6px 10px;">運算實體內部之動態運行時 (Runtime) 行為</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">主機 Agent、eBPF 核心感應探針</td>
      <td style="padding:6px 10px;">容器被植入挖礦木馬、WebShell 反連、權限逃逸</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">CIEM (身分管理)</td>
      <td style="padding:6px 10px;">雲端 IAM 身分、角色與過度授權 (Over-privileged)</td>
      <td style="padding:6px 10px;">IAM 授權日誌與存取分析</td>
      <td style="padding:6px 10px;">閒置特權角色遭濫用、跨帳戶未授權躍遷</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>在金融混合雲建設中，CSPM 提供宏觀架構之合規導航，CWPP 則提供微觀執行之近身肉搏防護，兩者深度整合（CNAPP）方能構築兼顧敏捷與安全的現代雲端堡壘。</p>
            """,
            "examinerTips": "評分核心：『多雲組態錯誤 (Misconfiguration) 為主要風險』、『CSPM 控管平面 API Agentless 靜態合規與漂移修復』、『CWPP 工作負載內部 Runtime 行為監控與容器防護』、『兩者融合成 CNAPP』。",
            "detailedExplanation": "混合雲安全是證券周邊單位數位轉型的熱門主題。答題時精準點出 CSPM 與 CWPP 的防護邊界與分工，展現成熟架構規劃能力。"
        },
        {
            "id": "sec-essay-25",
            "category": "sec",
            "chapter": "第 1 章：金融資安法規治理與證券期貨業聯防體系",
            "title": "金融實兵無預警社交工程郵件釣魚演練方案設計與員工資安意識量化評估",
            "points": 25,
            "rubric": "1. 社交工程演練法規依據與執行原則 (6分)；2. 釣魚情境設計（Quishing 二維碼釣魚等）(8分)；3. 演練指標（點閱率/填表率/通報率）與改善表 (7分)；4. 結論 (4分)",
            "question": "社交工程（Social Engineering）電子郵件釣魚始終是 APT 駭客組織攻破金融機構外圍防線的最常用途徑。金管會規定金融機構每年必須定期舉辦無預警社交工程演練。請規劃一份完整之證券交易所年度社交工程實兵演練專案計畫，說明演練情境主題之設計技巧（如 Quishing 二維碼釣魚、假冒人資考績與外包供應商緊急通知），並定義關鍵量化評估指標（KPI）與後續補強教育訓練機制。",
            "modelAnswer": """
<h4>一、破題：人性的弱點是資安防禦鏈最脆弱的環節</h4>
<p>無論邊界防火牆多麼強固，只要有一名員工點擊釣魚郵件並輸入網域密碼，攻擊者即可輕易越過所有邊界防禦。金管會規範金融機構每年至少辦理<strong>兩次以上無預警社交工程實兵演練</strong>，目的在將員工自「資安受害者」淬鍊為「人體第一道感測防火牆（Human Sensor）」</p>

<h4>二、實兵演練專案方案規劃與情境設計技巧</h4>
<ol>
  <li><strong>演練原則與倫理審查</strong>：
    演練前成立機密籌備小組（僅高階主管與 CISO 知情），確保演練完全無預警；演練伺服器收集憑證時必須以雜湊遮蔽，嚴禁記錄員工真實密碼明文。
  </li>
  <li><strong>高擬真演練情境主題設計</strong>：
    - <strong>權威與急迫性（Authority & Urgency）</strong>：假冒「金管會緊急稽核回覆通知」或「證交所總經理室重大資安通報」；<br>
    - <strong>利益與切身相關（Greed & Curiosity）</strong>：假冒「人資部年度調薪與績效獎金核發明細查詢」；<br>
    - <strong>新興技術攻擊（Quishing, QR Code Phishing）</strong>：郵件內文不含任何超連結文字以繞過郵件過濾引擎，改嵌入圖片 QR Code 要求員工使用手機掃描登入，測試行動端跨界防範意識。
  </li>
  <li><strong>量化指標評估（KPI）</strong>：
    - <strong>郵件開啟率（Open Rate）</strong>：衡量郵件主題誘因；<br>
    - <strong>惡意連結點擊率（Click Rate）</strong>：金管會基準要求嚴格壓制於 <strong>10% 以下</strong>；<br>
    - <strong>敏感資訊填寫率（Submit Rate）</strong>：於偽造釣魚頁輸入帳密之比率，目標壓制於 <strong>3% 以下</strong>；<br>
    - <strong>主動通報率（Report Rate）</strong>：收到釣魚信於 10 分鐘內點擊通報按鈕通報 SOC 之比率，作為衡量正向資安文化的關鍵指標（目標 <strong>40% 以上</strong>）。
  </li>
</ol>

<h4>三、社交工程演練情境分級與後續輔導改善對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">情境難度</th>
      <th style="padding:6px 10px;">釣魚手法特徵</th>
      <th style="padding:6px 10px;">測驗目標構面</th>
      <th style="padding:6px 10px;">受測失敗之處置輔導措施</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">基礎級 (Level 1)</td>
      <td style="padding:6px 10px;">明顯錯別字、通用寄件者、中獎假消息</td>
      <td style="padding:6px 10px;">基本防範警覺、寄件者網域辨別</td>
      <td style="padding:6px 10px;">線上完成 1 小時基礎防釣魚教學與測驗</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">進階級 (Level 2)</td>
      <td style="padding:6px 10px;">相似網域 (Typosquatting)、假冒人資通知</td>
      <td style="padding:6px 10px;">超連結懸停預覽檢視、內部公告求證</td>
      <td style="padding:6px 10px;">面談輔導、由資安主管重新審查權限</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">精準標靶 (Level 3)</td>
      <td style="padding:6px 10px;">Quishing 二維碼、供應商真實業務主題偽冒</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">跨載具攻擊警覺、雙管道確認機制</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">強制參加實體工作坊，次季納入重點複測</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>社交工程演練絕非懲處員工之手段，而是強化組織防禦彈性的訓練工具。結合主動通報獎勵與高擬真演練，方能建立「人人皆哨兵」的堅韌金融資安文化。</p>
            """,
            "examinerTips": "評分核心：『金管會每年至少兩次無預警演練法規』、『Quishing (二維碼釣魚) 等新興情境』、『四大量化指標：開啟率、點閱率、填表率與通報率 (Report Rate)』、『正向輔導與補強培訓』。",
            "detailedExplanation": "此題貼近金融日常資安治理實務。考生若能提出強調『主動通報率』作為量化資安文化成熟度之指標，將讓評卷委員眼前一亮。"
        },
        {
            "id": "sec-essay-26",
            "category": "sec",
            "chapter": "第 5 章：現代密碼學、公鑰基礎設施（PKI）與硬體安全模組",
            "title": "交易防竄改：SHA-3、HMAC、數位簽章（Ed25519）在金融委託回報傳輸之防重放（Anti-Replay）防護",
            "points": 25,
            "rubric": "1. 金融訊息安全威脅模型 (6分)；2. SHA-3、HMAC 與 Ed25519 密碼特性 (8分)；3. 防重放協定設計與對照表 (7分)；4. 結論 (4分)",
            "question": "證券期貨電子交易系統中，委託下單（Order Placement）與成交回報（Trade Execution Report）必須嚴格具備機密性、不可否認性（Non-Repudiation）、訊息完整性與即時有效性。請詳述現代密碼學中 SHA-3（Keccak 海綿結構）、HMAC 與橢圓曲線數位簽章 Ed25519 之安全優勢，並設計一套結合時間戳記（Timestamp）、一次性隨機數（Nonce）與遞增序列號（Sequence Number）之高抗重放交易通訊框架。",
            "modelAnswer": """
<h4>一、破題：金融委託傳輸的威脅模型</h4>
<p>在高速證券交易網路中，未受嚴密保護之報文可能面臨三重致命威脅：<strong>訊息竄改（Tampering）</strong>更改股票代碼與委託數量；<strong>身分偽冒（Spoofing）</strong>假冒客戶下單事後否認；以及<strong>重放攻擊（Replay Attack）</strong>側錄合法下單封包並惡意重複發送，導致投資人重大財務損失。</p>

<h4>二、現代密碼演算法技術優勢解析</h4>
<ol>
  <li><strong>SHA-3（Keccak 海綿結構, Sponge Construction）</strong>：
    不同於 SHA-2 基於 Merkle-Damgård 結構（易受長度擴展攻擊 Length Extension Attack），SHA-3 採用「吸收（Absorb）與擠出（Squeeze）」海綿運算機制，具有極高的密碼學代數複雜度，能天然抵禦長度擴展與特定差分分析。
  </li>
  <li><strong>HMAC（金鑰雜湊訊息鑑別碼）</strong>：
    在點對點超低延遲行情推播中，若非對稱簽章運算開銷過大，可採用 <code>HMAC-SHA256</code>。透過共用金鑰與雙重雜湊運算，兼具超高計算效能（奈秒級）與完整性鑑別保證。
  </li>
  <li><strong>Ed25519（愛德華曲線數位簽章）</strong>：
    相較於傳統 RSA-2048 及 ECDSA P-256，Ed25519 具備：<br>
    - <strong>極致簽驗速度</strong>：單核每秒可驗證數萬次簽章，完全契合高頻交易需求；<br>
    - <strong>抗側信道攻擊（Side-Channel Resistant）</strong>：演算法執行時間完全恆定，杜絕計時攻擊（Timing Attack）；<br>
    - <strong>決定性簽章（Deterministic）</strong>：不依賴系統不良隨機數產生器，避免 ECDSA 因隨機數重複洩漏私鑰之歷史悲劇（如 Sony PS3 破解事件）。
  </li>
</ol>

<h4>三、防重放（Anti-Replay）高可用交易協定設計</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">防重放機制</th>
      <th style="padding:6px 10px;">控制技術與參數</th>
      <th style="padding:6px 10px;">防護原理與驗證邏輯</th>
      <th style="padding:6px 10px;">邊界防禦效果</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">時間戳記 (Timestamp)</td>
      <td style="padding:6px 10px;">PTP 奈秒級伺服器時間，設定時間窗口 Δt = 500ms</td>
      <td style="padding:6px 10px;">伺服器比對 <code>|T_server - T_msg| > Δt</code> 立即判定逾時丟棄</td>
      <td style="padding:6px 10px;">防禦跨日或長時間延遲之離線重放</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">一次性隨機數 (Nonce)</td>
      <td style="padding:6px 10px;">客戶端每次產生 128-bit 密碼學安全隨機數</td>
      <td style="padding:6px 10px;">伺服器將 Nonce 存入高速記憶體快取 (Redis/BloomFilter) 查重</td>
      <td style="padding:6px 10px;">保證相同時間窗口內完全無重複報文</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">嚴格單調遞增序號 (SeqNum)</td>
      <td style="padding:6px 10px;">每個 Session 連線維持 64-bit 嚴格遞增序號</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">伺服器強制要求 <code>Seq_recv == Seq_expected</code>，否則中斷連線</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">徹底杜絕封包調序（Out-of-Order）與任何注入攻擊</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">不可否認數位簽章</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">Ed25519(OrderData || Timestamp || Nonce || Seq)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">使用客戶端私鑰對上述所有防重放欄位一同簽署</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">提供法律效力之不可否認性與完整性保證</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>金融下單安全必須同時兼顧「密碼學數學確定性」與「微秒級吞吐效能」。結合 Ed25519 決定性簽章與三合一防重放機制，為證券交易構建起高抗攻擊、無法竄改與無從反悔的信任基石。</p>
            """,
            "examinerTips": "評分核心：『SHA-3 海綿結構抗長度擴展』、『Ed25519 恆定時間與高吞吐性能優勢』、『三合一防重放：Timestamp (防超時)、Nonce (防同窗口重複)、SeqNum (防跳序與重放)』、『整包數位簽章賦予不可否認性』。",
            "detailedExplanation": "此題展示了將密碼學理論（Ed25519）完美結合金融交易工程（防重放協定設計）的高水準答題架構，實用性極高。"
        },
        {
            "id": "sec-essay-27",
            "category": "sec",
            "chapter": "第 7 章：網路防禦、三層式 DDoS 緩解與金融級邊界防護",
            "title": "金融阻斷服務攻擊演練（DDoS Drill）規劃：三層流量清洗驗證、BGP Flowspec 動態引流與演練指標",
            "points": 25,
            "rubric": "1. 金融 DDoS 實兵演練目的與邊界控制 (6分)；2. 三層流量清洗協防與 BGP Flowspec (8分)；3. 攻擊向量驗證表 (7分)；4. 結論 (4分)",
            "question": "為因應地緣政治與國際駭客針對臺灣金融關鍵基礎設施發動之大規模多向量 DDoS 攻擊，證券交易所必須定期執行實兵 DDoS 攻防演練。請規劃一套符合主管機關標準之金融 DDoS 實兵演練作業方案，詳述在不影響日間線上實盤撮合之前提下，如何驗證 CDN WAF、電信級 Clean Pipe 與 BGP Flowspec 核心路由黑洞之連鎖協防機制，並列出應衡量之量化演練驗收指標。",
            "modelAnswer": """
<h4>一、破題：關鍵金融基礎設施之韌性試金石</h4>
<p>DDoS 攻擊已由單純的大流量洪水演化為<strong>「Tbps 級容量型洪泛 + 應用層 L7 慢速穿透 + 核心路由耗盡」之多向量複合式攻擊</strong>。金融資安行動方案 2.0 強制要求每年執行無預警或全真 DDoS 演練，驗證極限承載力與連鎖清洗反應時間。</p>

<h4>二、演練環境設計與三層清洗聯防驗證</h4>
<ol>
  <li><strong>演練安全邊界與時間窗口</strong>：
    演練嚴格安排於<strong>非交易營業日（週末或夜間維護窗口）</strong>；在模擬演練網段或隔離演練 IP 進行實彈壓測，嚴禁影響日間正式委託撮合資料庫。
  </li>
  <li><strong>三層立體流量清洗協防流程</strong>：
    - <strong>第一層：邊緣 Anycast CDN / WAF</strong>：率先承接並吸收 70% 外部流量，過濾 HTTP CC 攻擊、畸形標頭與爬蟲穿透；<br>
    - <strong>第二層：電信級雲端流量清洗中心（ISP Clean Pipe）</strong>：當攻擊流量超過證交所實體專線頻寬閾值時，自動/手動透過 BGP 宣告切換引流，將流量牽引至電信商清洗中心進行特徵過濾，將乾淨流量（Clean Traffic）回注（Re-injection）；<br>
    - <strong>第三層：BGP Flowspec（RFC 5575）細粒度路由控制</strong>：當遭遇高強度 UDP/NTP 反射放大攻擊時，邊界路由器自動下發 Flowspec 規則至上游 ISP 核心交換節點，直接依據特定封包長度、來源埠 drop 丟棄，<strong>避免傳統黑洞路由（Blackholing）將正常業務流量一併犧牲之自殘缺陷</strong>。
  </li>
</ol>

<h4>三、多向量 DDoS 攻擊演練場景與驗收標準表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">攻擊向量類別</th>
      <th style="padding:6px 10px;">模擬攻擊技術指標</th>
      <th style="padding:6px 10px;">預期防禦觸發動作</th>
      <th style="padding:6px 10px;">量化驗收成功指標 (KPI)</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">L3/L4 巨量頻寬洪水</td>
      <td style="padding:6px 10px;">NTP / DNS 反射放大、SYN Flood (50 Gbps)</td>
      <td style="padding:6px 10px;">觸發電信級 Clean Pipe 引流與 SYN Cookie</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">3 分鐘內完成引流，主線頻寬佔用率 < 70%</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">L7 應用層連線耗盡</td>
      <td style="padding:6px 10px;">Slowloris / HTTP Post 慢速連線攻擊 (10 萬連線)</td>
      <td style="padding:6px 10px;">邊界防禦設備逾時強制中斷、動態 IP 封鎖</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">Web 伺服器連線池佔用 < 50%，正常查詢無逾時</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">BGP 路由層級防禦</td>
      <td style="padding:6px 10px;">針對特定下單 Gateway IP 之精準阻斷</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">自動下發 BGP Flowspec 丟棄惡意來源特徵封包</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">合法券商下單連線封包遺失率 (Packet Loss) < 0.1%</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>DDoS 演練是一場對電信基礎設施、清洗平台與內部維運團隊之全面大考驗。透過 BGP Flowspec 精準引流與指標化驗證，證交所得以確保在面臨國家級網路戰威脅時，交易通道永不中斷。</p>
            """,
            "examinerTips": "評分重點：『演練安全邊界（非營業日+隔離網段避免影響實盤）』、『三層清洗聯防（CDN WAF -> Clean Pipe -> BGP Flowspec）』、『BGP Flowspec 相較於傳統 Blackholing 黑洞路由之精準優勢』、『關鍵量化指標：引流啟動時間、封包遺失率 < 0.1%』。",
            "detailedExplanation": "實兵 DDoS 演練為證交所資安年度重大工作。此答案具備極高工程實用性，寫出 BGP Flowspec 解決傳統黑洞自殘缺陷是奪取頂標分數的關鍵。"
        },
        {
            "id": "sec-essay-28",
            "category": "sec",
            "chapter": "第 12 章：新興金融資安威脅、AI 安全與後量子密碼學",
            "title": "金融數位資產資安：冷熱錢包實體隔離、多重簽章（Multi-Sig）與多方安全計算（MPC/TSS）防護架構",
            "points": 25,
            "rubric": "1. 數位資產私鑰安全生命週期 (6分)；2. 冷/溫/熱錢包分級與實體保全 (7分)；3. Multi-Sig 與 MPC-TSS 門檻式簽章對照表 (8分)；4. 結論 (4分)",
            "question": "隨著金融市場發展與證券期貨業跨足數位資產託管（Digital Asset Custody）與代幣化證券（Security Token Offering, STO）業務，私鑰（Private Key）安全即為資產安全之命脈。請分析冷錢包（Cold Wallet）、溫錢包（Warm Wallet）與熱錢包（Hot Wallet）之實體與網路隔離要求，並深入比較「智慧合約多重簽章（Multi-Sig）」與「門檻式簽章方案（MPC-TSS, Threshold Signature Scheme）」在金鑰分散產生、授權簽署與跨鏈相容性之優劣。",
            "modelAnswer": """
<h4>一、破題：Not Your Keys, Not Your Assets 的金融監理考驗</h4>
<p>在數位資產與虛擬資產領域，「私鑰即資產，簽署即不可逆」。傳統金融帳戶交易若出錯可由後台撤銷沖正，但在區塊鏈分散式帳本上，一旦私鑰被竊，鏈上資產將在數秒內被轉移洗劫一空。建立金融級<strong>託管金鑰保全與多方簽章治理</strong>是推展 STO 業務之第一要務。</p>

<h4>二、冷、溫、熱三層錢包分級安全架構</h4>
<ol>
  <li><strong>冷錢包（Cold Wallet，佔比 90% 以上資產）</strong>：
    - <strong>實體隔離（Air-Gapped）</strong>：金鑰永不接觸任何網路，儲存於保險庫之 FIPS 140-3 Level 4 HSM 或氣隙專用硬體載具中；<br>
    - <strong>簽章流程</strong>：透過無網路之實體 QR Code 或專用單向光偶合設備傳輸未簽署交易資料，線下簽名後再導出廣播；需三位以上高階主管於不同監控監視下實體多方認證。
  </li>
  <li><strong>溫錢包（Warm Wallet，佔比約 5~8%）</strong>：
    半離線狀態，用於調度熱錢包之儲備流動性，需經 PAM 跳板機與雙人線上即時審核方可簽名。
  </li>
  <li><strong>熱錢包（Hot Wallet，佔比小於 2%）</strong>：
    連接網際網路，專門處理即時小額自動劃撥提存。設有嚴格單筆交易限額、單日總額上限及風控異常自動中斷融斷機制。
  </li>
</ol>

<h4>三、多重簽章（Multi-Sig）vs 門檻式簽章（MPC-TSS）技術剖析</h4>
<ol>
  <li><strong>鏈上多重簽章（On-Chain Multi-Sig，如 Gnosis Safe）</strong>：
    - <strong>原理</strong>：藉由區塊鏈智慧合約實施 <code>m-of-n</code> 授權（例如 3 個人中需 2 個人完成交易簽署）；<br>
    - <strong>限制</strong>：每次簽名均需送出多次獨立交易，手續費（Gas Fee）高昂；簽署者結構直接暴露於區塊鏈公開帳本上，缺乏隱私；且無法跨鏈通用於不支持智能合約之公鏈。
  </li>
  <li><strong>鏈下門檻簽章方案（Off-Chain MPC-TSS）</strong>：
    - <strong>原理</strong>：基於安全多方計算（Secure Multi-Party Computation），<strong>完整的私鑰從未在任何單一設備上完整生成過</strong>！金鑰在初始化時即以數學多項式分割為多個「金鑰碎片（Key Shares）」；<br>
    - <strong>簽章過程</strong>：多方在不互相洩漏金鑰碎片之前提下，透過密碼學協同運算共同產出<strong>標準的單一簽章（如 ECDSA / Ed25519 簽名）</strong>；<br>
    - <strong>優勢</strong>：在鏈上視角完全是一筆普通的單簽交易，Gas 費最低，支援所有公鏈，且外部攻擊者永遠無法在單一節點尋獲私鑰。
  </li>
</ol>

<h4>四、Multi-Sig vs MPC-TSS 全維度對比表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">比較構面</th>
      <th style="padding:6px 10px;">智慧合約 Multi-Sig</th>
      <th style="padding:6px 10px;">門檻簽章 MPC-TSS</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">私鑰存在形態</td>
      <td style="padding:6px 10px;">各自維護獨立的完整私鑰，由合約彙整</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">私鑰自始至終不存在，僅有分散的數學碎片</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">跨鏈相容性</td>
      <td style="padding:6px 10px; color:#ef4444;">差 (受限於該鏈之智能合約能力)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">極高 (通用於所有支援 ECDSA/Ed25519 區塊鏈)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">鏈上交易成本 (Gas)</td>
      <td style="padding:6px 10px;">高 (需驗證多次合約呼叫與狀態)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">低 (鏈上等同普通單簽交易)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">金鑰更換與動態管理</td>
      <td style="padding:6px 10px;">需發起鏈上合約呼叫變更所有者</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">支援 Resharing，動態更換碎片且鏈上地址不變</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>金融機構涉足數位資產託管，必須採納「90% 冷錢包 Air-Gapped + 核心金鑰 MPC-TSS 門檻治理」的黃金架構，徹底根除單點金鑰洩漏風險，樹立機構級資產託管新標竿。</p>
            """,
            "examinerTips": "評分核心：『冷/溫/熱錢包資產比例與 Air-Gapped 氣隙隔離』、『Multi-Sig (鏈上智慧合約驗證) 限制與高成本』、『MPC-TSS (鏈下多方計算無完整私鑰生成) 之跨鏈與隱私優勢』、『Key Resharing 動態金鑰輪換』。",
            "detailedExplanation": "隨著證券業推進 STO 與虛擬資產託管業務，數位資產密碼學題目為近年命題黑馬。清晰推演 MPC-TSS 的數學特質能展現前沿科技實力。"
        },
        {
            "id": "sec-essay-29",
            "category": "sec",
            "chapter": "第 9 章：資安事件通報、應變處理與數位鑑識實務",
            "title": "金融資安事件應變團隊（CSIRT）權責劃分、沙盒動態分析與 YARA 規則威脅獵捕",
            "points": 25,
            "rubric": "1. CSIRT 組織架構與緊急升級程序 (6分)；2. 沙盒動態行為監控與特徵提取 (8分)；3. YARA 規則語法與全網獵捕實作表 (7分)；4. 結論 (4分)",
            "question": "當證券交易所內部端點主機觸發 EDR 告警，疑似遭植入新型未知金融木馬時，資安事件應變團隊（CSIRT）應如何啟動應變標準作業程序？請詳述指揮官、鑑識工程師與系統維運人員之角色分工，說明如何於隔離的沙盒環境中對惡意程式進行動態行為分析（API Monitoring / Process Injection 監控），並示範如何提取特徵撰寫 YARA 規則進行全內網主機之威脅獵捕（Threat Hunting）。",
            "modelAnswer": """
<h4>一、破題：面對未知威脅之 CSIRT 協同應變機制</h4>
<p>當常規特徵庫無法辨識未知惡意二進位檔案時，金融機構不能單純仰賴端點阻斷，必須由<strong>資安事件應變小組（CSIRT）</strong>啟動完整之事件處理生命週期：<strong>準備 -> 偵測 -> 遏阻 -> 根除 -> 復原 -> 事後檢討（PIR）</strong>。</p>

<h4>二、CSIRT 關鍵角色職能分工</h4>
<ol>
  <li><strong>應變指揮官（Incident Commander）</strong>：負責全局決策、資源調度、向 CISO 與金管會回報，評估通報等級（30 分鐘通報機制）。</li>
  <li><strong>鑑識工程師（Forensic Investigator）</strong>：執行 RFC 3227 揮發性記憶體採集、磁碟取證、沙盒行為逆向分析與撰寫威脅情報（IoC）。</li>
  <li><strong>系統維運工程師（Infrastructure Engineer）</strong>：執行網路端點實體/邏輯隔離、防火牆黑名單封鎖、備份映像檔復原與系統加固。</li>
</ol>

<h4>三、隔離沙盒動態行為分析與 YARA 獵捕實戰</h4>
<ol>
  <li><strong>沙盒動態行為剖析（Dynamic Sandbox Analysis）</strong>：
    在隔離的虛擬化沙盒（如 Cuckoo Sandbox / Any.Run）中引爆樣本，監控：<br>
    - <strong>處理程序注入（Process Injection）</strong>：監控 <code>VirtualAllocEx</code>, <code>WriteProcessMemory</code>, <code>CreateRemoteThread</code> 是否將惡意代碼注入正常的 <code>explorer.exe</code>；<br>
    - <strong>網路外連（C2 Beaconing）</strong>：攔截其 DNS 請求、HTTP POST 心跳包格式與回傳指令；<br>
    - <strong>持久化存留（Persistence）</strong>：監控 Registry Run Keys 或排程工作（Scheduled Tasks）變更。
  </li>
  <li><strong>YARA 規則撰寫與全網威脅獵捕</strong>：
    從惡意二進位檔案中提取獨特的字串（Strings）、代碼片段與 PE 檔頭結構特徵，編寫 YARA 規則下發至 EDR 進行全網排查：
  </li>
</ol>

<pre style="background:#0f172a; color:#f8fafc; padding:12px; border-radius:6px; font-family:monospace; font-size:0.85rem; overflow-x:auto;">
rule TWSE_Targeted_Trojan_Hunting {
    meta:
        description = "Detects in-memory targeted financial trojan variant"
        author = "TWSE CSIRT Team"
        severity = "Critical"
    strings:
        $c2_uri = "/api/v2/telemetry/sync" ascii
        $inject_api = "WriteProcessMemory" ascii
        $mutex = "Global\\TWSE_MUTEX_9981" wide
        $shellcode_pattern = { 6A 00 68 00 00 00 00 50 FF 15 ?? ?? ?? ?? }
    condition:
        uint16(0) == 0x5A4D and // MZ header
        filesize < 2MB and
        ($c2_uri and ($mutex or $shellcode_pattern))
}
</pre>

<h4>四、CSIRT 事件應變流程與處置對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">應變階段</th>
      <th style="padding:6px 10px;">核心執行任務</th>
      <th style="padding:6px 10px;">產出與客觀證據</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">遏阻 (Containment)</td>
      <td style="padding:6px 10px;">EDR 網路隔離受害端點，保留記憶體通電狀態</td>
      <td style="padding:6px 10px;">LiME / WinPmem 記憶體映像檔、受控連線中斷</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">分析 (Analysis)</td>
      <td style="padding:6px 10px;">沙盒引爆監控 Process Injection，萃取 C2 與檔案特徵</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">動態行為分析報告、IoC 清單、YARA 獵捕規則</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">獵捕與根除 (Eradication)</td>
      <td style="padding:6px 10px;">下發 YARA 規則全內網伺服器磁碟與記憶體掃描</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">清除潛伏後門、重置受影響帳號、撤銷舊金鑰</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">復原與檢討 (Recovery)</td>
      <td style="padding:6px 10px;">乾淨備份重建主機、強化防火牆、召開 PIR 會議</td>
      <td style="padding:6px 10px;">根本原因分析報告 (RCA)、內部控制漏洞修補單</td>
    </tr>
  </table>
</div>

<h4>五、結論</h4>
<p>資安防禦是一場與時間賽跑的戰役。建立敏捷運作的 CSIRT，結合高擬真沙盒逆向與精準 YARA 威脅獵捕，能將未知惡意攻擊的平均圍堵時間（MTTR）壓縮至最短，保衛金融交易核心秩序。</p>
            """,
            "examinerTips": "評分重點：『CSIRT 權責分工與 30 分鐘通報』、『動態沙盒監控 Process Injection (VirtualAllocEx/WriteProcessMemory)』、『YARA 規則完整結構 (meta / strings / condition)』、『全內網獵捕與閉環根除』。",
            "detailedExplanation": "事件應變與數位鑑識是證交所資安人員招募考試的命題大宗。給出標準格式的 YARA 規則示範，能極大程度展現應試者的實務技術深度。"
        },
        {
            "id": "sec-essay-30",
            "category": "sec",
            "chapter": "第 4 章：身分識別、存取控制與零信任架構（ZTA）",
            "title": "金融機構特權帳號管理（PAM）：雙人控管、一次性憑證（OTP）、跳板機堡壘與全時側錄稽核架構",
            "points": 25,
            "rubric": "1. 特權帳號風險威脅分析 (6分)；2. 現代 PAM 核心模組架構 (8分)；3. 雙人覆核與側錄稽核對照表 (7分)；4. 結論 (4分)",
            "question": "內外部重大資安事件多數源自特權帳號（Privileged Accounts，如 AD Domain Admins、Linux Root、資料庫 DBA）遭濫用或竊取。請針對臺灣證券交易所關鍵交易主機環境，規劃一套端對端「特權帳號管理（PAM, Privileged Access Management）」系統架構，詳述密碼保險箱（Credential Vault）、及時授權（Just-In-Time / Ephemeral Credentials）、雙人覆核機制與終端連線全時錄影側錄之技術實作。",
            "modelAnswer": """
<h4>一、破題：王國鑰匙的危機與管理痛點</h4>
<p>在金融 IT 架構中，特權帳號（Root / Administrator / SA）擁有至高無上的系統控制權。傳統維運常面臨「多人共用單一帳號密碼」、「帳號密碼寫死於腳本設定檔中（Hardcoded）」以及「操作軌跡無法歸屬到具體自然人」之致命合規盲點。<strong>PAM（特權存取管理）</strong>是守護特權王冠之關鍵堡壘。</p>

<h4>二、證交所金融級 PAM 端對端架構規劃</h4>
<ol>
  <li><strong>密碼保險箱與密碼輪換（Enterprise Password Vault）</strong>：
    所有生產主機之 Root/Admin 密碼一律由 PAM 集中代管，維運人員<strong>完全不知曉真實主機密碼</strong>。密碼長度由系統自動設定為 32 碼隨機字元，並在每次連線結束後（Check-in）或每隔 24 小時強制由 PAM 自動輪換變更。
  </li>
  <li><strong>動態及時授權（Just-In-Time, JIT & 最小特權）</strong>：
    維運人員平時僅具備普通無權限帳號。遇到維運變更時，透過工單系統申請「及時暫時提權」，系統簽發限時 2 小時之一次性短效憑證（Ephemeral Certificate），時間屆滿憑證自動作廢，消除常駐特權（Zero Standing Privileges, ZSP）。
  </li>
  <li><strong>雙人授權覆核機制（Dual Authorization / Four-Eyes Principle）</strong>：
    針對高風險操作（如修改撮合設定、生產資料庫 DDL 變更、重啟伺服器），PAM 要求維運人員發起請求後，必須由<strong>另一位合格主管於管理 App 上完成生物辨識即時審批</strong>，方能開啟連線通道，杜絕單人蓄意破壞。
  </li>
  <li><strong>安全堡壘機與全時操作錄影側錄（Session Recording & Keystroke Logging）</strong>：
    連線強制透過 PAM 代理中繼跳板機（不允許直連目標主機）。連線過程對 SSH 命令、RDP 畫面實施<strong>每秒影格錄影與鍵盤字元即時紀錄</strong>。若偵測到黑名單指令（如 <code>rm -rf /</code> 或 <code>DROP TABLE</code>），PAM 具備即時阻斷連線（Session Termination）之主動防禦能量。
  </li>
</ol>

<h4>三、傳統跳板機 vs 現代零信任 PAM 平台能力對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">評估指標</th>
      <th style="padding:6px 10px;">傳統跳板機 (Bastion Host)</th>
      <th style="padding:6px 10px;">現代零信任 PAM 平台</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">密碼透明度</td>
      <td style="padding:6px 10px; color:#ef4444;">人員知曉主機密碼，容易私下備份抄寫</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">人員完全盲打，密碼託管於 Vault 每次輪換</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">授權模型</td>
      <td style="padding:6px 10px;">靜態長效帳號 (Standing Privileges)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">動態及時授權 (JIT) 與零常駐特權 (ZSP)</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">雙人覆核機制</td>
      <td style="padding:6px 10px;">依賴線下紙本或電子郵件，無法系統硬性攔截</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">四眼原則 (Four-Eyes) 線上即時審批始解鎖通道</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">稽核追溯能力</td>
      <td style="padding:6px 10px;">僅有文字 Log，難以追查 GUI 點擊行徑</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">全螢幕視訊錄影 + 擊鍵索引 + 高危指令即時中斷</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>在金融資安治理中，「信任是好事，但驗證更重要」。透過 PAM 架構的落地，將特權帳號的申請、使用、監控與回收全面自動化與閉環化，為證券交易核心主機打造最可靠的特權防線。</p>
            """,
            "examinerTips": "評分核心：『密碼保險箱 (Vault) 與 Check-in 自動輪換』、『零常駐特權 (Zero Standing Privileges, ZSP) 與 JIT 授權』、『雙人覆核四眼原則 (Four-Eyes Principle)』、『全時錄影側錄與高危指令中斷』。",
            "detailedExplanation": "特權帳號管理是金融資安評鑑與金管會專案金檢的必查重點。此題答題結構層次分明，切中監理痛點，極具競爭力。"
        },
        {
            "id": "sec-essay-31",
            "category": "sec",
            "chapter": "第 6 章：應用系統安全、OWASP Top 10 與軟體安全生命週期",
            "title": "金融行動應用程式（Mobile App）資安防護：防逆向工程、動態防篡改、安全金鑰儲存與法規檢測基準",
            "points": 25,
            "rubric": "1. 金管會「行動應用 App 基本資安檢測基準」核心規範 (6分)；2. 防逆向工程與動態反除錯技術 (8分)；3. 安全儲存與 SSL Pinning 實踐表 (7分)；4. 結論 (4分)",
            "question": "現代投資人高度仰賴手機 App 進行行動下單與帳務查詢，使得行動下單 App 成為駭客攻擊與偽冒重組的首要對象。請依據金管會發布之「行動應用 App 基本資安檢測基準」，說明開發券商下單 App 時應實施之安全架構，包括原始碼混淆（Obfuscation）、動態反竄改反除錯（Anti-Root/Anti-Jailbreak/Anti-Frida）、硬體金鑰庫安全儲存及 SSL Pinning 憑證綁定機制。",
            "modelAnswer": """
<h4>一、破題：非受控端點上的金融交易戰場</h4>
<p>行動手機屬於完全開放、難以被金融機構掌控之端點設備。攻擊者可在越獄或 Root 的手機環境中，運用反組譯工具（如 IDA Pro、Ghidra）還原 App 業務邏輯，甚至透過 Frida 等動態 Hook 框架竄改下單金額或記憶體驗證邏輯。金管會頒布之<strong>「行動應用 App 基本資安檢測基準（MAS）」</strong>為保障金融 App 安全之法定標竿。</p>

<h4>二、金融行動 App 四大防禦維度實踐</h4>
<ol>
  <li><strong>靜態原始碼防護（Source Code Obfuscation）</strong>：
    採用進階加固工具（如 ProGuard / DexGuard）實施控制流程平坦化（Control Flow Flattening）、字串加密、類別與函式名稱混淆；將敏感交易運算邏輯沉降至 C/C++ Native Library（JNI/NDK），大幅拔高逆向破解門檻。
  </li>
  <li><strong>動態環境偵測與反竄改（Anti-Tampering & Anti-Hook）</strong>：
    - <strong>環境檢測</strong>：啟動時檢查 <code>/system/bin/su</code>、Cydia Substrate、Magisk 檔案，偵測到 Root/Jailbreak 立即終止執行；<br>
    - <strong>反除錯與反動態注入</strong>：檢測 <code>ptrace</code> 掛載狀態與 Frida/Xposed 典型通訊連接埠（如 27042）及記憶體特徵，偵測到 Hook 行為即刻自我銷毀退出；<br>
    - <strong>二進位完整性校驗</strong>：在執行階段比對自身 APK/IPA 簽名證書雜湊，防止重打包二次發布（Repackaging）。
  </li>
  <li><strong>金鑰與敏感資料安全儲存</strong>：
    嚴禁將帳號密碼或憑證私鑰明文寫入 <code>SharedPreferences</code> 或 <code>UserDefaults</code>。必須強制調用硬體級安全儲存介面：<strong>Android Keystore（TEE/StrongBox）</strong>與 <strong>iOS Keychain（Secure Enclave）</strong>，私鑰以硬體隔離儲存並綁定生物辨識解鎖。
  </li>
  <li><strong>通訊層 SSL/TLS 憑證綁定（Certificate Pinning）</strong>：
    在 App 內部預先固化證交所伺服器憑證之公鑰雜湊（SPKI Pinning）。即使攻擊者在手機內強行安裝偽造的根憑證（如 Charles Proxy 抓包），App 網路層比對公鑰雜湊失敗即拒絕連線，徹底防堵中間人封包側錄。
  </li>
</ol>

<h4>三、金融行動 App 資安檢測項目與防禦對照表</h4>
<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">檢測維度</th>
      <th style="padding:6px 10px;">法規合規要求</th>
      <th style="padding:6px 10px;">核心技術防禦實施對策</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">原始碼加固</td>
      <td style="padding:6px 10px;">防止靜態逆向工程、文字字串暴露</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">控制流程平坦化、字串加密、Native C/C++ 封裝</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">動態運行安全</td>
      <td style="padding:6px 10px;">防止記憶體除錯、動態 Hook 注入與二度打包</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">Anti-Frida 偵測、ptrace 反除錯、簽章雜湊自校驗</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">敏感資料儲存</td>
      <td style="padding:6px 10px;">身分憑證與交易金鑰不得明文落地</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">調用 Android KeyStore (StrongBox) / iOS Keychain</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">傳輸通訊安全</td>
      <td style="padding:6px 10px;">防止傳輸竊聽、攔截與中間人偽造</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">TLS 1.3 + HPKP / 靜態公鑰綁定 (SSL Pinning)</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>在「行動優先」的金融下單時代，唯有建構從靜態加固、動態自衛到硬體金鑰庫防護之端到端縱深防禦，方能保護廣大投資人之交易資產安全。</p>
            """,
            "examinerTips": "評分核心：『金管會行動應用 App 基本資安檢測基準 (MAS)』、『防動態注入 (Anti-Frida / Anti-Root / ptrace)』、『硬體金鑰庫 (Keystore StrongBox / Keychain Secure Enclave)』、『SSL Pinning 免疫中間人抓包』。",
            "detailedExplanation": "行動下單 App 安全是證券交易前端防護的最前線。答案全面覆蓋靜態、動態、儲存與通訊四大維度，展現高度專業性。"
        },
        {
            "id": "sec-essay-32",
            "category": "sec",
            "chapter": "第 12 章：新興金融資安威脅、AI 安全與後量子密碼學",
            "title": "量子破譯危機下之金融根憑證（Root CA）遷移策略、NIST PQC 演算法實裝與混合模式（Hybrid Mode）測試",
            "points": 25,
            "rubric": "1. 量子破譯衝擊剖析 (6分)；2. 根憑證遷移五大階段規劃 (8分)；3. 經典與後量子演算法效能對照表 (7分)；4. 結論 (4分)",
            "question": "面對量子電腦於十年內破解 RSA 及 ECC 非對稱加密之潛在危機，全球金融基礎設施正積極啟動「後量子密碼遷移專案（PQC Migration）」。請針對臺灣證券交易所之公鑰基礎設施（PKI）與金融根憑證機構（Root CA），規劃一套完整的後量子轉型策略，詳述如何設計「經典演算法與 PQC 混合模式（Hybrid X.509 Certificate）」以兼顧舊版交易系統之向後相容性，並分析 PQC 龐大簽章體積（Signature Overhead）對金融網路傳輸效能之影響與調校對策。",
            "modelAnswer": """
<h4>一、破題：Y2Q（Years to Quantum）與金融密碼末日危機</h4>
<p>當擁有數千邏輯量子位元之量子電腦成熟時，Shor 演算法將在數秒內攻破目前全球金融體系所依賴的 RSA-2048 及 ECDSA 橢圓曲線非對稱加密。攻擊者現已發動<strong>「先截獲，後解密（SNDL, Store Now, Decrypt Later）」</strong>。證交所作為核心金融中樞，必須超前啟動 <strong>PQC（後量子密碼學）遷移戰略</strong>。</p>

<h4>二、金融根憑證（Root CA）PQC 遷移五大階段規劃</h4>
<ol>
  <li><strong>第 1 階段：密碼資產盤點（Crypto Inventory）</strong>：
    全面盤查所有證券下單通道、FIX 閘道、TLS 憑證、資料庫加密金鑰與簽章演算法，標註依賴 RSA/ECC 之資產，產出加密物料清單（CBOM, Cryptographic Bill of Materials）。
  </li>
  <li><strong>第 2 階段：加密敏捷性（Crypto-Agility）重構</strong>：
    改造 PKI 軟體與通訊通訊協定，將底層密碼呼叫模組化抽象（如 OpenSSL 3.x 提供者架構），使系統具備「在不重新編譯業務代碼前提下熱切換演算法」之敏捷性。
  </li>
  <li><strong>第 3 階段：混合過渡模式測試（Hybrid Mode X.509）</strong>：
    為保障現有數百家券商終端不斷線，採用 <strong>IETF 混合憑證架構</strong>（如 <code>Draft-ietf-lamps-cert-binding-for-multi-auth</code>）。在單張 X.509 憑證中同時嵌入：<br>
    - <strong>經典簽章（Classic）</strong>：ECDSA P-256（供舊版用戶端驗證）；<br>
    - <strong>後量子簽章（PQC）</strong>：<strong>ML-DSA-65 (CRYSTALS-Dilithium3)</strong>。<br>
    支援 PQC 的現代閘道校驗 ML-DSA，舊版系統則自動降級驗證 ECDSA，達成無縫向後相容！
  </li>
  <li><strong>第 4 階段：正式啟用後量子根憑證（Native PQC Root CA）</strong>：
    建立純 PQC CA 階層，簽發基於 ML-KEM（金鑰封裝）之 TLS 憑證與 ML-DSA 之數位簽章憑證。
  </li>
  <li><strong>第 5 階段：除役與歷史資料重新封裝（Decommission & Re-encryption）</strong>：
    對歷史長期保存之交易資料與數位合約，採用 PQC 演算法進行二次加封簽名，防止未來遭量子解密。
  </li>
</ol>

<h4>三、PQC 演算法體積對網路傳輸之衝擊與性能評估表</h4>
<p>PQC 演算法雖然具備抗量子數學強度，但其金鑰與簽章體積遠大於傳統演算法，容易導致 <strong>TCP 封包分段（Fragmentation）</strong>與延遲上升：</p>

<div class="table-wrap">
  <table style="width:100%; border-collapse:collapse; margin:10px 0;">
    <tr style="background:#1e3a8a; color:#fff;">
      <th style="padding:6px 10px;">演算法規格</th>
      <th style="padding:6px 10px;">演算法類型與標準</th>
      <th style="padding:6px 10px;">公鑰長度</th>
      <th style="padding:6px 10px;">密文/簽章長度</th>
      <th style="padding:6px 10px;">高頻撮合網路影響評估</th>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">ECDSA (P-256)</td>
      <td style="padding:6px 10px;">傳統橢圓曲線 (非抗量子)</td>
      <td style="padding:6px 10px;">64 Bytes</td>
      <td style="padding:6px 10px;">64 Bytes</td>
      <td style="padding:6px 10px;">單一 MTU 內可容納，微秒級</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">ML-DSA-65 (Dilithium)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">NIST PQC 晶格數位簽章標準</td>
      <td style="padding:6px 10px;">1,952 Bytes</td>
      <td style="padding:6px 10px; color:#ef4444; font-weight:700;">3,309 Bytes</td>
      <td style="padding:6px 10px;">需跨越 3 個 TCP 封包 (MTU 1500)，需調校 Jumbo Frame</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">ML-KEM-768 (Kyber)</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">NIST PQC 晶格金鑰封裝標準</td>
      <td style="padding:6px 10px;">1,184 Bytes</td>
      <td style="padding:6px 10px;">1,088 Bytes</td>
      <td style="padding:6px 10px;">TLS 1.3 協商首包稍微膨脹，但運算速度極快</td>
    </tr>
    <tr>
      <td style="padding:6px 10px; font-weight:700;">Falcon-512</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">NIST PQC 緊湊型數位簽章</td>
      <td style="padding:6px 10px;">897 Bytes</td>
      <td style="padding:6px 10px; color:#16a34a; font-weight:700;">666 Bytes</td>
      <td style="padding:6px 10px;">簽章最小，單包傳輸，極契合低延遲金融交易</td>
    </tr>
  </table>
</div>

<h4>四、結論</h4>
<p>後量子密碼遷移不是單純的演算法替換，而是一項跨越十年的金融基礎設施升級大工程。藉由「加密敏捷性、雙軌混合憑證、巨型訊框 Jumbo Frame 調校」之三維推進，臺灣證券交易所將引領我國資本市場從容邁入抗量子的全新安全紀元。</p>
            """,
            "examinerTips": "評分核心：『SNDL 先截獲後解密威脅』、『PQC 遷移五大階段：盤點 -> 敏捷化 -> 混合模式 -> 原生切換 -> 重新封裝』、『混合憑證 (Hybrid Mode: ECDSA + ML-DSA) 平滑相容』、『PQC 簽章體積膨脹 (Dilithium 3.3KB) 與 Jumbo Frame 網路調校』。",
            "detailedExplanation": "此題聚焦 NIST 剛公佈正式標準之 PQC 核心演算法（FIPS 203 ML-KEM、FIPS 204 ML-DSA）。寫出真實封包體積與 Jumbo Frame 調校，將展现登峰造極的金融架構功力。"
        }
    ]
