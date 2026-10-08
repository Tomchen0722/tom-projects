/**
 * 臺灣證券交易所 (TWSE) 招募備考系統 - 雙語金融資訊術語辭典
 * 包含英文、音標讀音、繁體中文釋義、證交所實務應用場景與發音綁定
 */

const TWSE_GLOSSARY = [
  {
    en: "Continuous Trading",
    phonetic: "/kənˈtɪnjuəs ˈtreɪdɪŋ/",
    zh: "逐筆撮合機制",
    category: "sysnet",
    desc: "臺灣證券交易所自 2020 年全面實施之撮合架構。委託隨到隨撮，以價格優先、時間優先為原則，大幅提升市場流動性與撮合效率，撮合延遲進入微秒等級。"
  },
  {
    en: "Kernel Bypass",
    phonetic: "/ˈkɜːrnl ˈbaɪpæs/",
    zh: "核心旁路技術",
    category: "sysnet",
    desc: "繞過作業系統 Linux Kernel 的網路堆疊與中斷機制，直接在使用者空間（User Space）讀寫網卡環形緩衝區，如 DPDK 與 Solarflare Onload，消除環境切換開銷。"
  },
  {
    en: "Multicast Market Data",
    phonetic: "/ˈmʌltikæst ˈmɑːrkɪt ˈdeɪtə/",
    zh: "行情多點廣播推播",
    category: "sysnet",
    desc: "證交所向各券商專線伺服器分送即時五檔與逐筆成交行情的核心網路技術。基於 UDP Multicast (PIM-SSM/IGMPv3)，發送端僅需廣播一次即可觸達所有訂閱節點。"
  },
  {
    en: "Spine-Leaf Topology",
    phonetic: "/spaɪn liːf təˈpɑːlədʒi/",
    zh: "脊葉式資料中心拓撲",
    category: "sysnet",
    desc: "現代金融機房核心網路架構。任兩台伺服器間傳輸均維持一致的跳數（Hop Count）與可預測的超低延遲，並具備 ECMP 等價多路徑負載平衡與無阻塞橫向擴展特性。"
  },
  {
    en: "Precision Time Protocol (PTP)",
    phonetic: "/prɪˈsɪʒn taɪm ˈproʊtəkɔːl/",
    zh: "高精準度時間同步協定 (IEEE 1588)",
    category: "sysnet",
    desc: "金融監理與證券高頻交易必備之時間同步標準。透過硬體時間戳記（Hardware Timestamping）實現亞微秒（Sub-microsecond）乃至奈秒級同步，滿足 MiFID II 與證期法嚴格稽核要求。"
  },
  {
    en: "Non-Uniform Memory Access (NUMA)",
    phonetic: "/nɑːn ˈjuːnɪfɔːrm ˈmɛməri ˈæksɛs/",
    zh: "非均勻記憶體存取架構",
    category: "sysnet",
    desc: "多 CPU 插槽伺服器中各 CPU 存取本地記憶體速度遠快於跨匯流排存取遠端記憶體。撮合系統須透過 numa node binding 與 cpu pinning 避免跨節點記憶體延遲。"
  },
  {
    en: "Write-Ahead Logging (WAL)",
    phonetic: "/raɪt əˈhɛd ˈlɔːɡɪŋ/",
    zh: "預寫式日誌",
    category: "sysnet",
    desc: "關聯式資料庫保證交易 ACID 耐久性（Durability）之核心機制。所有交易變更在寫入磁碟資料頁前，必須先順序追加寫入 WAL 日誌，支援崩潰後即時重做（REDO）。"
  },
  {
    en: "Dual-Active Data Center",
    phonetic: "/ˈduːəl ˈæktɪv ˈdeɪtə ˈsɛntər/",
    zh: "雙活資料中心",
    category: "sysnet",
    desc: "兩處地理機房同時在線承載即時撮合與查詢流量，資料透過同步鏡像傳輸，達成本地 RTO ≈ 0、RPO ≈ 0 之最高容災等級，確保證券市場永不中斷。"
  },
  {
    en: "Zero Trust Architecture (ZTA)",
    phonetic: "/ˈzɪroʊ trʌst ˈɑːrkɪtɛktʃər/",
    zh: "零信任架構",
    category: "sec",
    desc: "『永不信任，始終驗證』（Never Trust, Always Verify）。基於 NIST SP 800-207 標準，摒棄傳統周界防禦，對身分、設備、網路微隔離與存取政策進行持續動態驗證。"
  },
  {
    en: "Hardware Security Module (HSM)",
    phonetic: "/ˈhɑːrdwer sɪˈkjʊrəti ˈmɑːdʒuːl/",
    zh: "硬體安全模組",
    category: "sec",
    desc: "專門用於管理金融交易憑證私鑰、數位簽章與敏感金鑰運算之防篡改硬體設備（具備 FIPS 140-2 Level 3/4 認證），任何未授權物理探針拆解皆會觸發主動銷毀機制。"
  },
  {
    en: "Financial ISAC (F-ISAC)",
    phonetic: "/faɪˈnænʃl ˈaɪsæk/",
    zh: "金融資安資訊分享與分析中心",
    category: "sec",
    desc: "金管會主導之金融聯防樞紐。推動證券期貨業情資分享、惡意指標（IoC）即時通報、金融 APT 威脅早期預警與跨機構資安應變協同作戰。"
  },
  {
    en: "DDoS Traffic Scrubbing",
    phonetic: "/diː dɒs ˈtræfɪk ˈskrʌbɪŋ/",
    zh: "分散式阻斷服務流量清洗",
    category: "sec",
    desc: "運用 Anycast BGP 路由將海量攻擊流量引流至電信級清洗中心，透過深度封包檢測（DPI）、挑戰應答（Challenge-Response）與行為特徵過濾，確保正常下單流量順暢。"
  },
  {
    en: "Extended Detection and Response (XDR)",
    phonetic: "/ɪkˈstɛndɪd dɪˈtɛkʃn ənd rɪˈspɑːns/",
    zh: "延伸偵測及回應",
    category: "sec",
    desc: "整合端點（EDR）、網路（NDR）、雲端與身分驗證日誌之資安監控平台。利用跨維度關聯分析精準揪出進階持續性滲透（APT）與勒索軟體橫向移動跡象。"
  },
  {
    en: "Software Bill of Materials (SBOM)",
    phonetic: "/ˈsɔːftwer bɪl əv məˈtɪriəlz/",
    zh: "軟體物料清單",
    category: "sec",
    desc: "詳列應用系統所採用之所有開源套件、第三方函式庫與依賴版本之清單結構（如 SPDX 或 CycloneDX），為軟體供應鏈安全與 Log4j 等重大漏洞應變之基石。"
  },
  {
    en: "Post-Quantum Cryptography (PQC)",
    phonetic: "/poʊst ˈkwɑːntəm krɪpˈtɑːɡrəfi/",
    zh: "後量子密碼學",
    category: "sec",
    desc: "抵抗量子電腦 Shor 演算法破解之新一代密碼標準（NIST 評選之晶格密碼如 ML-KEM、ML-DSA），用於替換既有 RSA/ECC，守護金融長期交易存檔與通訊機密。"
  },
  {
    en: "Remote Direct Memory Access (RDMA)",
    phonetic: "/rɪˈmoʊt daɪˈrɛkt ˈmɛməri ˈæksɛs/",
    zh: "遠端直接記憶體存取",
    category: "sysnet",
    desc: "允許伺服器透過網路直接讀取另一台主機之記憶體，完全不需經過雙方 CPU 與作業系統核心堆疊參與，於 RoCEv2 架構下提供微秒級資料庫同步傳輸。"
  },
  {
    en: "Microburst",
    phonetic: "/ˈmaɪkroʊbɜːrst/",
    zh: "網路微突發流量",
    category: "sysnet",
    desc: "金融市場行情劇烈波動時，極短時間（數十微秒內）湧入的大量行情或下單封包，極易瞬間填滿交換器 Buffer 造成丟包與延遲抖動，需透過專屬 Buffer 佇列管理技術緩解。"
  },
  {
    en: "Role-Based Access Control (RBAC)",
    phonetic: "/roʊl beɪst ˈæksɛs kənˈtroʊl/",
    zh: "角色型存取控制",
    category: "sec",
    desc: "依據使用者在組織內的職責角色配置最小權限之權限管理模型。證券業落實職能分工（Segregation of Duties, SoD）與雙人覆核管制之基本準則。"
  },
  {
    en: "Security Operations Center (SOC)",
    phonetic: "/sɪˈkjʊrəti ˌɑːpəˈreɪʃnz ˈsɛntər/",
    zh: "資安監控維運中心",
    category: "sec",
    desc: "7x24 不間斷監控金融基礎設施之安全團隊與技術體系。整合 SIEM 與 SOAR 平台，對異常日誌警報進行分級評估與自動化腳本封鎖應變。"
  },
  {
    en: "MITRE ATT&CK Framework",
    phonetic: "/ˈmaɪtər əˈtæk ˈfreɪmwɜːrk/",
    zh: "MITRE 攻擊戰術與技術知識庫",
    category: "sec",
    desc: "全球資安防護與威脅獵捕通用之威脅矩陣，系統化歸納駭客攻擊生命週期中各階段（如 Initial Access、Execution、Persistence、Lateral Movement）之具體技術與防禦策略。"
  },
  {
    en: "Lead Auditor (LA)",
    phonetic: "/liːd ˈɔːdɪtər/",
    zh: "主導稽核員",
    category: "sec",
    desc: "取得國際認可證照（如 IRCA/CQI）具備領導稽核團隊、規劃稽核計畫、主持開幕與閉幕會議、判定不符合事項（NC）並審核矯正措施有效性之資深稽核專家。"
  },
  {
    en: "Objective Evidence",
    phonetic: "/əbˈdʒɛktɪv ˈɛvɪdəns/",
    zh: "客觀證據",
    category: "sec",
    desc: "ISO 19011 稽核之核心靈魂。透過訪談（Interviews）、文件審閱（Records Review）及現場實作觀察（Observation）取得可被重複驗證的事實數據，作為稽核發現判定之唯一依據。"
  },
  {
    en: "Statement of Applicability (SoA)",
    phonetic: "/ˈsteɪtmənt əv ˌæplɪkəˈbɪləti/",
    zh: "適用性聲明書",
    category: "sec",
    desc: "ISO/IEC 27001 Clause 6.1.3 核心文件。詳列 Annex A 93 項控制措施之採納或排除理由、實施現況及對應控制目標，為 Stage 1 文件審查與合規查核之關鍵樞紐。"
  },
  {
    en: "Major Non-conformity",
    phonetic: "/ˈmeɪdʒər nɑːnkənˈfɔːrməti/",
    zh: "重大不符合事項",
    category: "sec",
    desc: "ISO 19011 稽核中最嚴重等級之發現。代表核心條款未滿足、控制措施系統性崩潰或對資安產生直接重大危害。直接阻擋證書簽發，受稽方需於 90 天內完成 RCA 並接受實地複查。"
  },
  {
    en: "Minor Non-conformity",
    phonetic: "/ˈmaɪnər nɑːnkənˈfɔːrməti/",
    zh: "次要不符合事項",
    category: "sec",
    desc: "單一或偶發性之作業疏漏，未對整體 ISMS 有效性構成系統性衝擊。不阻擋證書發放，但需於限期內提出矯正措施計畫（CAP）及佐證資料送書面複審。"
  },
  {
    en: "Opportunity for Improvement (OFI)",
    phonetic: "/ˌɑːpərˈtuːnəti fər ɪmˈpruːvmənt/",
    zh: "改善機會 / 觀察事項",
    category: "sec",
    desc: "現行作業符合標準要求，但依稽核員專業判斷存在潛在惡化風險或具備更佳業界做法之建議，不需開立矯正措施單，供受稽組織持續精進參考。"
  },
  {
    en: "Root Cause Analysis (RCA)",
    phonetic: "/ruːt kɔːz əˈnæləsɪs/",
    zh: "根本原因分析",
    category: "sec",
    desc: "ISO 27001 Clause 10.1 要求之問題根因深究方法（如 5-Why 分析法或魚骨圖）。旨在挖掘制度架構、流程自動化與技術機制的根本成因，杜絕問題再度復發。"
  },
  {
    en: "Corrective Action",
    phonetic: "/kəˈrɛktɪv ˈækʃn/",
    zh: "矯正措施",
    category: "sec",
    desc: "消除已發生之不符合事項根本原因並防止其再次發生的閉環行動。包含：即刻遏阻、根本原因分析、預防措施擬定與執行，以及後續有效性驗證（Verification）。"
  },
  {
    en: "Order of Volatility",
    phonetic: "/ˈɔːrdər əv ˌvɑːləˈtɪləti/",
    zh: "數位鑑識揮發性順序",
    category: "sec",
    desc: "RFC 3227 現場數位鑑識證據採集鐵律。依揮發性由高至低採集：CPU 暫存器 -> 實體記憶體 RAM -> 網路連線狀態 -> 磁碟儲存媒體 -> 備份媒體，嚴禁第一時間拔除電源。"
  },
  {
    en: "Financial Action Plan 2.0",
    phonetic: "/faɪˈnænʃl ˈækʃn plæn/",
    zh: "金融資安行動方案 2.0",
    category: "sec",
    desc: "金管會深化金融營運韌性之核心綱領。涵蓋深化治理（專責 CISO）、強化聯防（F-ISAC/SOC）、提升監韌（BIA/RTO/RPO 與防勒索演練）、建構文化四大構面。"
  }
];

window.TWSE_GLOSSARY = TWSE_GLOSSARY;
