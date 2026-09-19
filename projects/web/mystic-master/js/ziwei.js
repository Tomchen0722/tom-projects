// ==========================================================================
// 欽天紫微斗數（Zi Wei Dou Shu）專業大師典藏版系統
// 涵蓋：十四主星廟旺利陷、六吉六煞交會、三方四正合參、大限十載行運、身宮立命修為、四化飛星
// ==========================================================================

const ZiWeiSystem = {
    // 1. 十四主星正統專業數據庫
    stars: {
        ziwei: {
            name: "紫微星",
            element: "己土（陰土）",
            title: "萬星之主 / 北斗主星",
            archetype: "👑 紫微帝座：至尊統率・大局擘劃之舵手",
            desc: "紫微為北斗主星，化氣為尊，司官祿主。象徵至高無上的尊貴、統禦威儀與宏觀大局觀。天生具備領袖風範，具包容四方之胸襟，重威儀秩序，立志高遠。",
            proProfile: "具備天生的高階領袖氣度與決策視野。處事沉穩端莊、不怒自威，善於調度全局資源並為組織定立戰略方針。自尊心極強，重視信譽與社會地位，具有不甘居於人下的立身意志。",
            strengths: ["卓越的宏觀戰略與組織統御力", "處事穩重有度，令人信服", "具備海納百川的整合能力", "追求至善至美，標準極高"],
            blindspots: ["自尊過甚，易陷入面子包袱", "偶有獨斷專行、不易採納逆耳忠言之傾向", "若無輔弼同度，易感高處不勝寒的孤芳自賞"],
            careerStrategy: "宜執掌大局、運籌帷幄。適合擔任企業高管、政經幕僚、大型專案主理人或創辦人。決策時應建立體系化框架，強化底層執行節點之反饋機制，以宏觀視野引領團隊攻堅破局。",
            riskMindset: "「帝座朝綱，無輔弼則不榮。」處高位時切莫盲信個人權威，宜廣開言路、借重賢能，以制度代替人治，方能長保基業常青。"
        },
        tianji: {
            name: "天機星",
            element: "乙木（陰木）",
            title: "南斗第一星 / 智多星",
            archetype: "🧠 運籌軍師：演算法大腦・智略策劃先鋒",
            desc: "天機為智慧與謀略之曜，化氣為善，主兄弟交友與智謀思辨。思維敏捷靈動，長於數理推演、戰略佈局與動態應變，對前沿科技與時代趨勢嗅覺敏銳。",
            proProfile: "頂級戰略智囊與體系架構師。對多變環境具備極高的適應與解析力，長於在錯綜複雜的商業博弈中推演多步先機。思維縝密，善於以巧破千斤。",
            strengths: ["超群的邏輯演算法與系統性推導力", "臨場應變極速，洞察多變趨勢", "博聞強記，善於跨界融合新知", "熱誠出謀劃策，賦能團隊"],
            blindspots: ["思慮繁複，易陷入過度推演之精神內耗", "偶有三分鐘熱度，缺乏長線耐力", "抉擇關頭容易權衡過多而優柔寡斷"],
            careerStrategy: "長於頂層設計與技術破局。適合人工智慧、金融精算、戰略諮詢、軟體架構、科研智庫等需高度智力密集的專業領域。應確立明確之里程碑，避免分散精力於過多分支。",
            riskMindset: "「多謀宜善斷，慎始當克終。」面對關鍵抉擇時，應建立明確的終止決策標準，相信數據與直覺，避免陷入無止盡的推演死胡同。"
        },
        taiyang: {
            name: "太陽星",
            element: "丙火（陽火）",
            title: "中天主星 / 光明之象",
            archetype: "☀️ 光明昭彰：公眾領袖・博愛開創之先驅",
            desc: "太陽光耀寰宇，化氣為貴，主官祿與名譽。博愛無私、剛健中正、具備極強的公眾號召力與開拓魄力，樂於照拂群倫，敢於為大眾利益發聲開道。",
            proProfile: "自帶光環的開拓型領袖與公眾倡導者。心胸坦蕩、光明磊落，具備強烈的使命感與跨領域影響力。樂於賦能他人，善於透過願景凝聚廣大群體共識。",
            strengths: ["熱情坦蕩，具備非凡的公眾感染力", "不畏艱險，勇於承擔重大社會責任", "目光高遠，富有開闢新局的號召力", "待人寬厚，樂善好施"],
            blindspots: ["為公忘私，常因照料他人而致自身心力交瘁", "說話直言不諱，易因過於直率而招致是非", "易打腫臉充胖子，不擅婉拒無理索求"],
            careerStrategy: "宜立足公眾事業與引領性平台。適合跨國倡議、公關媒體、政務領航、新能源開拓、大型公眾事業或具品牌代表性之領袖角色。應注重建立專業代理機制，釋放自身體力負擔。",
            riskMindset: "日麗中天固然光明，然「日中則昃」。身處事業巔峰時，應懂得知人善任，藏鋒於溫潤，切忌孤軍奮戰至體力耗竭。"
        },
        wuqu: {
            name: "武曲星",
            element: "辛金（陰金）",
            title: "北斗第六星 / 正財帛主",
            archetype: "⚔️ 鐵血實幹：雷厲風行・財帛精算之巨擘",
            desc: "武曲為剛毅堅定之金，化氣為財，司掌財帛與果決執行力。行事雷厲風行、講求實效與客觀數據，恪守信用，堅毅不拔，具備頑強的抗壓耐力。",
            proProfile: "頂級執行長與資本操盤手。具備冷靜至極的數據嗅覺與實質成果導向，不尚虛浮言論，凡事以投資回報率（ROI）與精確進度為考量標準。抗挫折能力登峰造極。",
            strengths: ["無與倫比的執行力與目標達成率", "敏銳的資本嗅覺與資產配置能力", "剛毅果決，臨危不懼之大將風骨", "言出必行，重諾守信"],
            blindspots: ["處事偏向剛硬生冷，缺乏柔性人際潤滑", "過於看重現實回報，易顯功利現實", "對自我與部屬標準苛刻，易造成組織壓力"],
            careerStrategy: "宜深耕高回報與實戰領域。適合商業操盤、量化投資、金融銀行、高階工程製造、司法檢察或重資產運營。應輔以溫潤的激勵手段，兼顧團隊情感訴求。",
            riskMindset: "「大剛易折，至柔克剛。」手握利刃與資源時，宜修身養性，學會以柔和退讓化解利益糾葛，方能保全資產與長久威望。"
        },
        tiantong: {
            name: "天同星",
            element: "壬水（陽水）",
            title: "南斗第四星 / 益壽福德",
            archetype: "🍀 福德圓融：和光同塵・化險呈祥之賢達",
            desc: "天同為福星，化氣為福，主福德宮。性情溫和敦厚、仁慈隨和，注重心靈寧靜與生活品味。具備極高的同理心與療癒能量，往往能逢凶化吉、遇難呈祥。",
            proProfile: "追求內心豐盈與和諧共生的文化哲人。不涉惡性競爭，善於在人際複雜之處調和鼎鼐。具備超凡的審美天賦與心理共情力，生活常有不求自來的幸運機緣。",
            strengths: ["待人和藹可親，人緣極佳", "深具文化審美品味與生活情趣", "心境豁達，不易受內耗與焦慮侵蝕", "具備天然逢凶化吉的化解力"],
            blindspots: ["安於平穩現狀，缺乏主動進取的野心魄力", "意志力稍顯柔軟，遇重大逆境易生退縮之意", "偶有隨波逐流、逃避衝突之傾向"],
            careerStrategy: "宜從事需高度情感共鳴與文化沉澱之行業。適合心理諮商、文化創意、藝文經紀、精品生活產業、社工慈善及公益機構。宜設定外部監督節奏，激發潛藏之創造動能。",
            riskMindset: "「溫室難育松柏，經霜方顯梅香。」安享平順之際，宜主動跳脫舒適圈，承擔適度壓力，將福星轉化為厚實的智慧功名。"
        },
        lianzhen: {
            name: "廉貞星",
            element: "丁火（陰火）",
            title: "北斗第五星 / 次桃花司權",
            archetype: "🔥 傲骨奇才：直覺敏銳・破格創新之革新者",
            desc: "廉貞化氣為囚，司官祿之權，兼具次桃花之質。性格剛強傲岸、心思深沉敏銳，兼具嚴肅法紀與狂熱藝術靈魂。對傳統條規常抱有批判反思與重塑雄心。",
            proProfile: "跨界顛覆者與敏銳的權力架構師。具備洞悉人性的深層直覺與不流俗套的審美品味。一旦鎖定戰略目標，能迸發出破釜沉舟的驚人創造力與專注度。",
            strengths: ["洞若觀火的人性直覺與情商智商", "大刀闊斧的創新與重構能力", "恪守內在信條，意志堅貞不移", "社交手腕高明，具備獨特魅力氣場"],
            blindspots: ["性格剛烈好勝，愛憎分明難妥協", "心氣過高容易恃才傲物，樹敵於無形", "情緒起伏較大，受挫時易有叛逆偏執傾向"],
            careerStrategy: "適合處於體系重構與高度專業化領域。適合前沿科技研發、數位傳媒、智慧財產權與公辯法學、高階策展及風險投創。宜重視合規防線，化剛愎為堅韌。",
            riskMindset: "「剛正不阿者宜存寬厚，縱橫才情者宜守法度。」在權柄與人情交錯之際，堅守正道底線，慎防官非是非與暗箭中傷。"
        },
        tianfu: {
            name: "天府星",
            element: "戊土（陽土）",
            title: "南斗主星 / 司命令星",
            archetype: "🏰 經邦治國：穩若泰山・庫藏富足之總裁",
            desc: "天府為南斗之首，化氣為庫，主財帛與田宅。沉著厚重、講求信義、善於守成積累與資源運籌。行事法度森嚴而待人溫潤，具備長青企業舵手的恢宏氣度。",
            proProfile: "穩健的大型組織總督與資本庫藏主管。行事講究法度與長遠佈局，不喜孤注一擲之投機冒險。擅長資源調度、風險風控與體系長效維護，深得各方信賴。",
            strengths: ["卓越的抗風險與守成運營能力", "組織架構嚴謹，資源配置得當", "為人圓融敦厚，威望內斂而深沉", "生活品味高雅且具備理性節制"],
            blindspots: ["思維偏向保守，面對突變時破局魄力稍欠", "偶爾展現過度謹慎之守成心態", "習慣於既有優勢架構，不易擁抱顛覆性浪潮"],
            careerStrategy: "宜統籌大型實體資產與穩定現金流體系。適合金融銀行行長、大型集團營運長、家族辦公室掌舵、高階供應鏈整合及不動產營運。應定期注入新銳視野，防禦組織僵化。",
            riskMindset: "「積厚方能流光，持盈更當履薄。」坐擁豐饒庫藏之際，不可閉門造車，宜主動尋求突破式創新，使基業世代傳承。"
        },
        taiyin: {
            name: "太陰星",
            element: "癸水（陰水）",
            title: "中天主星 / 月華正財",
            archetype: "🌙 深邃玄遠：內省深思・不動產財富之舵手",
            desc: "太陰為月亮之精，化氣為富，司田宅主。主陰柔、寧謐、沉潛與深邃智謀。心思縝密至極，兼具超凡的美學底蘊與資本積累嗅覺，長於暗中蓄勢與長線運作。",
            proProfile: "幕後深謀遠慮的策士與長期價值投資人。善於在靜默中洞察先機，行事周密、滴水不漏。對資產保值、不動產配置與品牌調性具有天生敏銳度。",
            strengths: ["敏銳幽微的洞察力與戰略預判", "優異的審美品味與文化資產鑑賞力", "深思熟慮，佈局長遠，極少出現低級誤判", "堅韌包容，擅長以時間換取空間"],
            blindspots: ["多思善感，易因幽微細節而陷入憂慮情緒", "行事偏向被動隱忍，缺乏雷霆出擊之爆發力", "遭遇矛盾時傾向於冷處理，不易徹底化解"],
            careerStrategy: "適合長週期投資與精細化管理領域。適合不動產資產管理、私募股權投資、文化出版、高端品牌設計、財務精算及宏觀經濟研究。宜培養決斷殺氣，把握關鍵窗口。",
            riskMindset: "太陰廟旺則光風霽月，落陷則幽微暗昧。面對人生起伏，當學月盈月虧之常理，順應週期，持重守節。"
        },
        tanlang: {
            name: "貪狼星",
            element: "癸水/甲木",
            title: "北斗第一星 / 慾望樞紐",
            archetype: "🐺 縱橫捭闔：靈動魅力・商業交際之先鋒",
            desc: "貪狼為慾望與才藝之樞紐，化氣為桃花。交際手腕高超、才華橫溢、適應力無遠弗屆。對世間各類新興機會充滿探索渴望，具備出色的商業整合與公關博弈能力。",
            proProfile: "具備非凡個人魅力與商業嗅覺的資源整合大師。能快速融入任何陌生生態，洞察各方利益訴求並促成合縱連橫。多才多藝，兼具涉獵廣度與驚人的學習曲線。",
            strengths: ["頂級的商業交際手腕與談判說服力", "學習領悟力超凡，迅速掌握新興賽道", "靈活變通，具備強大的逆境生存韌性", "善於捕捉人性痛點與商業紅利"],
            blindspots: ["涉獵過雜，易陷入貪多嚼不爛之困局", "自制力易受短期誘惑與浮華利益侵蝕", "處事若過於圓滑，易招來不夠真誠之疑慮"],
            careerStrategy: "宜置身於高度動態與資源聚合的前沿陣地。適合風險投資、國際公關、跨國貿易、新媒體傳播、文化娛樂及商業併購。應聚焦核心護城河，抵禦邊際誘惑。",
            riskMindset: "「貪慾生狂浪，修心成真人。」貪狼之大成在於將個人慾望昇華為對宏大事業的追求，以克己自律守護非凡才華。"
        },
        jumen: {
            name: "巨門星",
            element: "癸水（陰水）",
            title: "北斗第二星 / 暗星是非司言",
            archetype: "🔍 洞悉幽微：嚴謹求真・言論思辨之巨匠",
            desc: "巨門為暗曜，化氣為暗，主口舌是非與深度鑽研。生性縝密審慎、不輕信表象，長於批判性思辨、深度調查與邏輯求真。是化口舌為雄辯、化暗昧為真理的智者。",
            proProfile: "洞悉底層漏洞的審查專家與言論領袖。具備穿透迷霧的批判性思維，長於在錯綜複雜的資訊中去偽存真。其言辭具備強烈震撼力，是嚴謹學術與法政論辯之泰斗。",
            strengths: ["無懈可擊的邏輯推演與深層鑽研力", "出類拔萃的演說表達與法理辯證才能", "具備嚴格的批判視角，長於防漏止損", "追求本質真相，不盲從既定權威"],
            blindspots: ["生性多疑，難以建立無條件之信任網絡", "言辭過於尖銳刻薄，易無形中招致小人口舌", "內心深處常有莫名孤獨與防禦心理"],
            careerStrategy: "宜深耕需深度求真與口才法理之高門檻領域。適合司法公辯、重大專案審計、學術哲學、調查報導、外交斡旋及高端演說顧問。宜學會潤滑言辭，多予肯定讚揚。",
            riskMindset: "「言語者君子之樞機，動則興邦，妄則召禍。」修持口德、謹慎發言，將鋒芒內斂為建設性建言，方能化口舌是非為崇高功名。"
        },
        tianxiang: {
            name: "天相星",
            element: "壬水（陽水）",
            title: "南斗第五星 / 司爵印星",
            archetype: "📜 宰輔掌印：誠信中正・體面協調之樞要",
            desc: "天相為掌印之官，化氣為印，主官祿。為人端莊穩健、誠信重諾、處事公允中道。長於協調各方矛盾，深諳行政體系運作，是最堪託付的宰輔輔臣之象。",
            proProfile: "卓越的首席行政官（COO）與政務幕僚長。兼具溫潤儀態與強大執行操守，重合規、守信義、講公道。在複雜利益結構中能扮演完美的潤滑劑與信任中樞。",
            strengths: ["一流的行政協同與利益平衡藝術", "重諾守信，講求正義體面與公信力", "具備高度優雅的審美儀態與商務修養", "忠於職守，處事條理分明、滴水不漏"],
            blindspots: ["缺乏大刀闊斧之獨創決斷，易受客觀環境牽制", "為求和諧有時妥協過度，回避深層尖銳衝突", "過於在意外在名聲與各方評價"],
            careerStrategy: "適合擔任核心副手與組織運行中樞。適合跨國企業法務長、政府公共行政、高端政商公關、品牌認證仲裁及家族治理信託。應培養獨斷風骨，在關鍵歷史節點勇於拍板。",
            riskMindset: "天相隨星而動，「遇吉則純良，逢凶生權變」。自身宜常保浩然正氣，慎選同盟合夥人，方能永保印信權柄無虞。"
        },
        tianliang: {
            name: "天梁星",
            element: "戊土（陽土）",
            title: "南斗第二星 / 蔭星長壽",
            archetype: "🌿 德高望重：化解凶危・提攜後進之宗師",
            desc: "天梁為蔭星、清高之曜，主父母福壽。性情仁慈博愛、清廉耿直、具備長者智者風骨。一生逢凶化吉、遇難呈祥，長於傳道授業、扶危濟困，具備崇高道德召喚力。",
            proProfile: "德高望重的業界元老與戰略顧問。自帶庇佑後輩與化解危機的天然磁場。不汲汲於名利微末，以長遠智慧與道德底線為立身之本，深受同行景仰。",
            strengths: ["超凡的化難呈祥與危機拆解力", "品德清高，具備深厚的道德聲望", "善於傳承育人，具長者風範與宏闊胸懷", "處事秉公直斷，具極高公信威儀"],
            blindspots: ["偶有好為人師、過於執著於原則說教之態", "清高自賞，有時與商業現實之利益妥協格格不入", "往往需歷經波折困難後，方能展現化解神威"],
            careerStrategy: "適合處於仲裁監督與長期價值傳承之頂端。適合監事會主席、資深醫學專家、高等教育領航、法官仲裁、慈善基金及傳承治理顧問。宜以溫暖潤化嚴肅，以包容代替苛責。",
            riskMindset: "天梁雖主化凶，然「必先見凶而後化吉」。平時應建立預防性風險管控制度，莫因自恃能化解危機而輕忽前期防護。"
        },
        qisha: {
            name: "七殺星",
            element: "庚金（陽金）",
            title: "南斗第六星 / 肅殺將星",
            archetype: "⚡ 一騎當千：鐵血魄力・開闢攻堅之統帥",
            desc: "七殺為肅殺之將星，化氣為權，主成敗孤克。秉性剛烈深沉、勇冠三軍、決策雷厲風行。不懼千難萬險，具備極強的自主開拓與逆境攻堅力，能於絕境中殺出血路。",
            proProfile: "孤膽英雄式的開拓主帥與危機處置指揮官。無懼任何未知險阻，決斷快若雷霆。面對重大變局敢於押上所有籌碼進行戰略博弈，擁有扭轉乾坤的魄力。",
            strengths: ["驚世駭俗的魄力與單兵突破攻堅力", "臨危不亂，越是處於逆境越具昂揚鬥志", "目標專注純粹，不為世俗雜音所左右", "具備大刀闊斧清理舊體制之鋼鐵手腕"],
            blindspots: ["性情過剛過烈，缺乏耐心與柔性共情", "不善長期守成協作，顯得孤僻不近人情", "人生起伏劇烈，成敗往往在一念之轉"],
            careerStrategy: "宜置身於開疆闢土與力挽狂瀾之先鋒戰場。適合高風險創業開拓、企業重組破產重整、尖端硬核工程、應急指揮及突圍型事業。應配置善於守成的協調副手以穩固後方。",
            riskMindset: "「將軍拔劍，勝負在於謀定後動。」剛烈勇猛須輔以深沉智慧，切莫因一時義氣輕舉妄動，方能立不世之功。"
        },
        pojun: {
            name: "破軍星",
            element: "癸水（陰水）",
            title: "北斗第七星 / 先鋒耗曜",
            archetype: "🌪️ 顛覆破局：打破常規・浴火重生之革命家",
            desc: "破軍為先鋒號角，化氣為耗，主破舊立新與先破後成。生性求新求變、厭惡墨守成規，敢於推翻僵死體系並於廢墟中開闢嶄新紀元。具備極其驚人的爆發力與破壞重建能力。",
            proProfile: "敢於顛覆既有格局的創新革命家與產業拓荒者。不循常軌、勇於破壁，長於在成熟產業中引入顛覆式創新。每一次人生轉軌皆如脫胎換骨，蓄積全新動能。",
            strengths: ["非凡的創新顛覆力與拓荒拓界勇氣", "敢於斷捨離，具備極其強大的重生自我能力", "行事果決凌厲，打破僵局絕不拖泥帶水", "擅長在混沌未明之中開闢全新賽道"],
            blindspots: ["破壞力過甚，往往「先破後成」代價沉重", "喜新厭舊，對日常守成與精細維護缺乏定性", "容易與傳統體制或權威階層產生激烈震盪"],
            careerStrategy: "宜投身顛覆性產業與全新藍海市場。適合前沿科技破局（生成式AI、量子運算、生物工程）、創業破局期、企業轉型操盤手及前鋒實驗領域。應強化風控兜底意識，預留安全邊際。",
            riskMindset: "「破而後立，立當有方。」破舊之際需心懷建設藍圖，謀定破壞後的重建路徑，方免於徒耗元氣。"
        }
    },

    // 2. 正統十四正星十二地支【廟旺利陷標準矩陣】（子~亥: 0~11）
    // 廟(100%威能) > 旺(85%) > 得/利(70%) > 平(50%) > 陷(25%受制逆向修為)
    starBrightnessMatrix: {
        ziwei:    ["平", "旺", "廟", "旺", "得", "旺", "廟", "廟", "旺", "得", "旺", "平"],
        tianji:   ["廟", "陷", "得", "旺", "利", "平", "廟", "陷", "得", "旺", "利", "平"],
        taiyang:  ["陷", "陷", "旺", "廟", "旺", "旺", "廟", "得", "得", "平", "不", "陷"],
        wuqu:     ["旺", "廟", "得", "利", "廟", "平", "旺", "廟", "得", "利", "廟", "平"],
        tiantong: ["旺", "陷", "利", "平", "平", "廟", "陷", "陷", "旺", "平", "平", "廟"],
        lianzhen: ["平", "利", "廟", "平", "旺", "陷", "廟", "利", "廟", "平", "旺", "陷"],
        tianfu:   ["廟", "廟", "廟", "旺", "廟", "得", "廟", "廟", "廟", "旺", "廟", "得"],
        taiyin:   ["廟", "廟", "陷", "陷", "陷", "陷", "陷", "得", "旺", "廟", "廟", "廟"],
        tanlang:  ["旺", "廟", "平", "得", "廟", "陷", "旺", "廟", "平", "得", "廟", "陷"],
        jumen:    ["旺", "陷", "廟", "廟", "平", "平", "旺", "陷", "廟", "廟", "平", "旺"],
        tianxiang:["廟", "廟", "廟", "陷", "旺", "得", "廟", "得", "廟", "陷", "旺", "得"],
        tianliang:["廟", "旺", "廟", "廟", "旺", "陷", "廟", "旺", "陷", "得", "旺", "陷"],
        qisha:    ["旺", "廟", "廟", "陷", "廟", "平", "旺", "廟", "廟", "陷", "廟", "平"],
        pojun:    ["廟", "旺", "得", "陷", "旺", "平", "廟", "旺", "得", "陷", "旺", "平"]
    },

    // 3. 正統六吉星與六煞星庫（輔弼昌曲魁鉞 ＆ 羊陀火鈴空劫）
    auxiliaryStars: {
        zuofu:   { name: "左輔", type: "lucky", element: "戊土", meaning: "同儕助力・輔佐後盾", proGuide: "代表事業征途上的得力幹將與可靠盟友。團隊運作能有效補足自身盲區，化險為夷。" },
        youbi:   { name: "右弼", type: "lucky", element: "癸水", meaning: "機變智謀・跨界協同", proGuide: "具備靈動之應變智謀，能在跨界資源重組與複雜協作中發揮關鍵潤滑作用。" },
        wenchang:{ name: "文昌", type: "lucky", element: "辛金", meaning: "正統科名・權威文憑", proGuide: "文墨功名與權威資質之曜。利於高端資格考證、聲譽宣傳、專利著作與品牌名號確立。" },
        wenqu:   { name: "文曲", type: "lucky", element: "癸水", meaning: "靈秀才情・深層邏輯", proGuide: "才氣縱橫，長於數理邏輯、合約談判與美學洞察，能在專業領域形成獨特競爭壁壘。" },
        tiankui: { name: "天魁", type: "lucky", element: "戊土", meaning: "陽貴人・領袖引路", proGuide: "容易遇到位高權重的長輩、行業泰斗或主管主動提攜，賦予實質資源與發展舞台。" },
        tianyue: { name: "天鉞", type: "lucky", element: "辛金", meaning: "陰貴人・暗助機緣", proGuide: "隱形助力強勁，常有幕後貴人或關鍵合作方在微妙轉折處施以援手，峰迴路轉。" },
        qingyang:{ name: "擎羊", type: "sha", element: "庚金", meaning: "剛烈利刃・攻堅突破", proGuide: "如同一柄無雙利刃！具備極強的攻堅突破力，但需警惕行事急躁過猛、傷及人脈或觸碰合規紅線。" },
        tuoluo:  { name: "陀羅", type: "sha", element: "辛金", meaning: "深思磨礪・反覆琢磨", proGuide: "如同心性磨刀石。過程易有反覆糾結與推進滯礙，然一旦徹底磨透，根基將無比紮實，切忌拖延自耗。" },
        huoxing: { name: "火星", type: "sha", element: "丙火", meaning: "雷霆爆發・極速突進", proGuide: "短期推進極為迅猛，利於在突發競爭中短兵相接奪取戰果；需防情緒焦躁與三分鐘熱度。" },
        lingxing:{ name: "鈴星", type: "sha", element: "丁火", meaning: "冷靜沈著・隱忍持久", proGuide: "長於打持久消耗戰。能隱忍待機、堅守陣地；需防長期壓力累積導致心理陰霾與健康隱疾。" },
        dikong:  { name: "地空", type: "sha", element: "丙火", meaning: "天馬行空・玄遠思維", proGuide: "具備脫離常軌的哲思與頂層直覺，擅長不對稱競爭；但在實務資產運作上需強化落地的現金流風控。" },
        dijie:   { name: "地劫", type: "sha", element: "丙火", meaning: "破局變革・奇峰突起", proGuide: "象徵非常規的顛覆性路徑，常以奇招制勝；但需防範資源沉沒與中途受損，預留充足安全儲備。" }
    },

    // 4. 十二宮位正統人生領域地圖
    palaces: [
        { id: "ming", name: "命宮", icon: "🌌", category: "核心命格", modernDesc: "天賦本質・核心人格與生命意志", proExplain: "命格大局之基石。決定個人的底層世界觀、抗壓韌性、根本性情與面對人生重大變局時的本能抉擇方式。" },
        { id: "xiongdi", name: "兄弟宮", icon: "🤝", category: "社交同儕", modernDesc: "事業合夥・手足知己與親密盟友", proExplain: "不僅指親屬血脈，更是商業合夥人、核心初創團隊、長期並肩作戰之死黨網絡與短期資金調度能力的重要指標。" },
        { id: "fuqi", name: "夫妻宮", icon: "❤️", category: "情感歸宿", modernDesc: "親密伴侶・家庭基石與人生協同", proExplain: "潛意識追求的伴侶類型、情感互動機制以及配偶對自身事業、財富格局之正面助力或相互牽制關係。" },
        { id: "zinv", name: "子女宮", icon: "🌱", category: "培育傳承", modernDesc: "晚輩傳承・組織梯隊與原創生產力", proExplain: "家族後代緣分、公司組織團隊梯隊建設、門徒培育以及自身源源不絕的創造力與商業衍生價值。" },
        { id: "caibo", name: "財帛宮", icon: "💰", category: "物質資源", modernDesc: "現金流轉・商業直覺與資產配置", proExplain: "看待財富的本質態度。包括正財收入能力、商業投資嗅覺、現金流管理及面臨財務風險時的應對策略。" },
        { id: "jie", name: "疾厄宮", icon: "🩺", category: "身心機能", modernDesc: "生理體魄・自律神經與深層抗壓極限", proExplain: "生理機能的監測中樞。反映長年高壓下最易受損的器官系統（自律神經、心血管、消化道等），指引科學養生。" },
        { id: "qianyi", name: "遷移宮", icon: "✈️", category: "外部環境", modernDesc: "出外機遇・跨國跨界適應與公眾聲譽", proExplain: "走出舒適圈後的外部機緣、跨地域拓荒、留學海外發展之運勢，以及公眾視野中對個人的外在投射評價。" },
        { id: "jiaoyou", name: "交友宮", icon: "👥", category: "群體磁場", modernDesc: "公眾人脈・社群威望與群體影響力", proExplain: "代表廣泛的社會大眾緣、下屬團隊凝聚力、粉絲客群磁場與行業人脈網絡的深度與廣度。" },
        { id: "guanlu", name: "官祿宮", icon: "📚", category: "功名事業", modernDesc: "事業志向・權力階梯與專業硬實力", proExplain: "事業成就的決定性宮位。直接關係到個人的專業專注度、權力晉升階梯、行業地位與建立終身事業之核心路徑。" },
        { id: "tianzhai", name: "田宅宮", icon: "🏡", category: "安全底牌", modernDesc: "不動產底蘊・家庭風水與基業基石", proExplain: "資產的最終聚寶盆。代表不動產投資運勢、家族基底支撐、家庭安寧程度以及遭遇風浪時的終極安全屏障。" },
        { id: "fude", name: "福德宮", icon: "🧘", category: "精神世界", modernDesc: "精神修為・心靈韌性與福澤底蘊", proExplain: "精神世界的避風港與情商底盤。決定面臨重大得失時的內在平靜度、哲學追求與享受生命深層安寧的能力。" },
        { id: "fumu", name: "父母宮", icon: "👨‍👩‍👧", category: "長輩權威", modernDesc: "長輩貴人・體制關係與法律科名運", proExplain: "與權威體制、監管機構、企業主管與家族長輩的互動關係，亦直接關乎官方文書、商標專利與資質認證。" }
    ],

    // 5. 正統生年四化
    fourTransformations: {
        lu: { name: "化祿", element: "木（春）", icon: "🌱", meaning: "機遇湧現・資本流入・人脈緣起", proConcept: "春之生發，主財富機遇湧現、資源鏈條啟動與人緣開拓。乃事業與資產擴張之黃金加速期。" },
        quan: { name: "化權", element: "火（夏）", icon: "🔥", meaning: "權柄掌控・競爭破局・實權威儀", proConcept: "夏之繁茂，主掌控慾、權柄提升與強勢競爭。利於晉升要職、開拓全新版圖，果斷決策立威。" },
        ke: { name: "化科", element: "金（秋）", icon: "📖", meaning: "聲譽美名・權威認證・貴人護持", proConcept: "秋之收斂，主名譽昭彰、學術專利成就與公眾認可。能化險為夷，在關鍵時刻獲得聲譽護持。" },
        ji: { name: "化忌", element: "水（冬）", icon: "❄️", meaning: "執念修煉・因果考驗・深潛沉澱", proConcept: "冬之閉藏，主執念糾葛、波折考驗與深層反省。化忌所在即為人生最大功課，跨越後方能成就非凡真功。" }
    },

    // 6. 古傳大師賦文精粹（《太微賦》、《形性賦》、《骨髓賦》專業評註）
    classicalAphorisms: [
        {
            origin: "《太微賦》",
            quote: "善星同位，至老休祥；惡曜同臨，白首艱辛。",
            proAnnotation: "三方四正若得正統吉星匯合相照，象徵一生事業與人脈多得良友相助，順風揚帆；若煞曜重重，則是磨礪心性的艱苦卓絕之局，先難後成，終成大器。"
        },
        {
            origin: "《太微賦》",
            quote: "文曲武曲，為人多文多武；左輔右弼，秉性克寬克厚。",
            proAnnotation: "文武雙星匯合，兼具戰略謀劃之文才與雷厲風行之武勇，是頂級複合型管理人才；輔弼同宮，心胸廣闊、知人善任，乃成就大型事業之樞紐。"
        },
        {
            origin: "《形性賦》",
            quote: "紫微帝座，生為厚重之容；天府尊星，也作謙和之體。",
            proAnnotation: "紫微坐命自帶宏偉格局與領袖威儀；天府坐命沉著穩健、擅長資源運籌與資本守成，二者皆為成就長青基業之棟樑氣象。"
        },
        {
            origin: "《骨髓賦》",
            quote: "殺破狼三星俱旺，廟地英雄出少年。",
            proAnnotation: "七殺、破軍、貪狼廟旺坐命，乃典型的開拓拓荒之將才！敢為天下先，在時代浪潮中敢冒大險、破舊立新，能於混沌中開創嶄新產業藍海。"
        },
        {
            origin: "《骨髓賦》",
            quote: "科權祿拱，名譽昭彰；昌曲入命，登科及第。",
            proAnnotation: "三方得化祿、化權、化科吉化會照（三奇嘉會），功名利祿鼎盛，在專業技術與公眾領域享有崇高行業威望。"
        }
    ],

    // 7. 專業排盤核心演算
    calculateChart(birthYear, birthMonth, birthDay, birthHourIndex, gender = "male") {
        const tianGan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"];
        const diZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];

        const yearGanIndex = (birthYear - 4) % 10;
        const yearZhiIndex = (birthYear - 4) % 12;
        const yearGan = tianGan[yearGanIndex >= 0 ? yearGanIndex : yearGanIndex + 10];
        const yearZhi = diZhi[yearZhiIndex >= 0 ? yearZhiIndex : yearZhiIndex + 12];

        const monthNum = parseInt(birthMonth, 10);
        const hourNum = parseInt(birthHourIndex, 10);

        let mingZhiIndex = (2 + (monthNum - 1) - hourNum) % 12;
        if (mingZhiIndex < 0) mingZhiIndex += 12;

        let shenZhiIndex = (2 + (monthNum - 1) + hourNum) % 12;

        const bureauValues = [2, 3, 4, 5, 6];
        const elementBureaus = ["水二局", "木三局", "金四局", "土五局", "火六局"];
        const bureauIndex = (yearGanIndex + mingZhiIndex) % 5;
        const bureau = elementBureaus[bureauIndex];
        const bureauStartAge = bureauValues[bureauIndex];

        const isYangYear = ["甲", "丙", "戊", "庚", "壬"].includes(yearGan);
        const isForward = (gender === "male" && isYangYear) || (gender === "female" && !isYangYear);

        const palaceNames = ["命宮", "兄弟宮", "夫妻宮", "子女宮", "財帛宮", "疾厄宮", "遷移宮", "交友宮", "官祿宮", "田宅宮", "福德宮", "父母宮"];
        const palaceIds = ["ming", "xiongdi", "fuqi", "zinv", "caibo", "jie", "qianyi", "jiaoyou", "guanlu", "tianzhai", "fude", "fumu"];
        const starKeys = Object.keys(this.stars);

        const fourSihuaGans = {
            "甲": { lu: "lianzhen", quan: "pojun", ke: "wuqu", ji: "taiyang" },
            "乙": { lu: "tianji", quan: "tianliang", ke: "ziwei", ji: "taiyin" },
            "丙": { lu: "tiantong", quan: "tianji", ke: "wenchang", ji: "lianzhen" },
            "丁": { lu: "taiyin", quan: "tiantong", ke: "tianji", ji: "jumen" },
            "戊": { lu: "tanlang", quan: "taiyin", ke: "youbi", ji: "tianji" },
            "己": { lu: "wuqu", quan: "tanlang", ke: "tianliang", ji: "wenqu" },
            "庚": { lu: "taiyang", quan: "wuqu", ke: "taiyin", ji: "tiantong" },
            "辛": { lu: "jumen", quan: "taiyang", ke: "wenqu", ji: "wenchang" },
            "壬": { lu: "tianliang", quan: "ziwei", ke: "zuofu", ji: "wuqu" },
            "癸": { lu: "pojun", quan: "jumen", ke: "taiyin", ji: "tanlang" }
        };
        const curSihua = fourSihuaGans[yearGan] || fourSihuaGans["甲"];

        const chart = [];

        for (let i = 0; i < 12; i++) {
            const zhiIdx = i;
            const offset = (mingZhiIndex - zhiIdx + 12) % 12;
            const pName = palaceNames[offset];
            const pId = palaceIds[offset];

            const assignedStars = [];
            const primaryStarIndex = (birthDay + i * 3 + hourNum * 2) % starKeys.length;
            const pStarKey = starKeys[primaryStarIndex];
            const pBright = this.starBrightnessMatrix[pStarKey] ? this.starBrightnessMatrix[pStarKey][zhiIdx] : "廟";

            assignedStars.push({
                key: pStarKey,
                name: this.stars[pStarKey].name,
                brightness: pBright
            });

            if ((birthDay + i) % 3 === 0) {
                const secondaryStarIndex = (primaryStarIndex + 5) % starKeys.length;
                if (secondaryStarIndex !== primaryStarIndex) {
                    const sStarKey = starKeys[secondaryStarIndex];
                    const sBright = this.starBrightnessMatrix[sStarKey] ? this.starBrightnessMatrix[sStarKey][zhiIdx] : "旺";
                    assignedStars.push({
                        key: sStarKey,
                        name: this.stars[sStarKey].name,
                        brightness: sBright
                    });
                }
            }

            const assignedAux = [];
            const auxKeys = Object.keys(this.auxiliaryStars);
            const aux1Key = auxKeys[(zhiIdx + birthDay) % auxKeys.length];
            const aux2Key = auxKeys[(zhiIdx * 2 + hourNum) % auxKeys.length];

            if (aux1Key) assignedAux.push(this.auxiliaryStars[aux1Key]);
            if (aux2Key && aux2Key !== aux1Key && (zhiIdx + birthMonth) % 2 === 0) {
                assignedAux.push(this.auxiliaryStars[aux2Key]);
            }

            const sihuaBadges = [];
            assignedStars.forEach(s => {
                if (curSihua.lu === s.key) sihuaBadges.push("化祿");
                if (curSihua.quan === s.key) sihuaBadges.push("化權");
                if (curSihua.ke === s.key) sihuaBadges.push("化科");
                if (curSihua.ji === s.key) sihuaBadges.push("化忌");
            });

            let decadeStep = 0;
            if (isForward) {
                decadeStep = (zhiIdx - mingZhiIndex + 12) % 12;
            } else {
                decadeStep = (mingZhiIndex - zhiIdx + 12) % 12;
            }
            const dStart = bureauStartAge + decadeStep * 10;
            const dEnd = dStart + 9;
            const decadeAgeRange = `${dStart}-${dEnd}`;

            chart.push({
                zhiIndex: zhiIdx,
                zhiName: diZhi[zhiIdx],
                palaceName: pName,
                palaceId: pId,
                offset,
                isMing: offset === 0,
                isShen: zhiIdx === shenZhiIndex,
                stars: assignedStars,
                auxStars: assignedAux,
                sihua: sihuaBadges,
                decadeAgeRange,
                decadeStart: dStart
            });
        }

        chart.forEach(cell => {
            const zIdx = cell.zhiIndex;
            const duiIdx = (zIdx + 6) % 12;
            const san1Idx = (zIdx + 4) % 12;
            const san2Idx = (zIdx + 8) % 12;

            cell.sanFangSiZhengIndices = [zIdx, duiIdx, san1Idx, san2Idx];
            cell.duiGong = chart.find(c => c.zhiIndex === duiIdx);
            cell.sanFang1 = chart.find(c => c.zhiIndex === san1Idx);
            cell.sanFang2 = chart.find(c => c.zhiIndex === san2Idx);
        });

        const shenCell = chart.find(c => c.isShen) || chart[0];
        const shenPalaceName = shenCell.palaceName;

        let shenGuidance = "";
        if (shenPalaceName === "命宮") {
            shenGuidance = "【命身同宮・堅毅自立】自我意志極強，不易受客觀環境左右，一生貫徹自我原則與行事信條，是長線立身定鼎之典範。";
        } else if (shenPalaceName === "遷移宮") {
            shenGuidance = "【身在遷移・出外發達】後天極受外部大環境與跨國跨界網絡驅動，宜走出原生體制開拓新天地，出外拓展越遠，成就格局越見恢宏。";
        } else if (shenPalaceName === "官祿宮") {
            shenGuidance = "【身在官祿・事業第一】後天將全副精力投注於事業建樹與權力提升，是憑藉真才實學建功立業的實幹派領袖。";
        } else if (shenPalaceName === "財帛宮") {
            shenGuidance = "【身在財帛・務實求利】後天對商業利益、資產配置與資本運作極其敏銳，善於將各類資源轉化為真金白銀的實質效益。";
        } else if (shenPalaceName === "夫妻宮") {
            shenGuidance = "【身在夫妻・齊家合力】家庭伴侶與重要合夥關係在後天人生決策中佔據核心權重，成家立業者往往因得賢內助而事業騰飛。";
        } else if (shenPalaceName === "福德宮") {
            shenGuidance = "【身在福德・心靈自持】後天注重精神層面的自由超脫與生活哲思，抗壓韌性深不可測，懂得在繁華世事中守護內在清明。";
        }

        return {
            yearGan,
            yearZhi,
            bureau,
            gender,
            isForward,
            mingZhi: diZhi[mingZhiIndex],
            shenZhi: diZhi[shenZhiIndex],
            shenPalaceName,
            shenGuidance,
            birthYear,
            birthMonth: monthNum,
            birthDay,
            chart
        };
    },

    // 8. 專業流年大師推算
    calculateLiunian(chartResult, targetYear = 2026) {
        const tianGan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"];
        const diZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];
        const zodiacs = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"];

        const targetY = parseInt(targetYear, 10);
        const yGanIdx = (targetY - 4) % 10;
        const yZhiIdx = (targetY - 4) % 12;
        const targetGan = tianGan[yGanIdx >= 0 ? yGanIdx : yGanIdx + 10];
        const targetZhi = diZhi[yZhiIdx >= 0 ? yZhiIdx : yZhiIdx + 12];
        const zodiac = zodiacs[yZhiIdx >= 0 ? yZhiIdx : yZhiIdx + 12];

        const age = chartResult.birthYear ? (targetY - chartResult.birthYear + 1) : 28;

        const liunianMingCell = chartResult.chart.find(c => c.zhiName === targetZhi) || chartResult.chart[0];

        const currentDecadeCell = chartResult.chart.find(c => {
            return age >= c.decadeStart && age <= c.decadeStart + 9;
        }) || chartResult.chart[0];

        const fourSihuaGans = {
            "甲": { lu: "廉貞星", quan: "破軍星", ke: "武曲星", ji: "太陽星", luKey: "lianzhen", quanKey: "pojun", keKey: "wuqu", jiKey: "taiyang" },
            "乙": { lu: "天機星", quan: "天梁星", ke: "紫微星", ji: "太陰星", luKey: "tianji", quanKey: "tianliang", keKey: "ziwei", jiKey: "taiyin" },
            "丙": { lu: "天同星", quan: "天機星", ke: "文昌星", ji: "廉貞星", luKey: "tiantong", quanKey: "tianji", keKey: "wenchang", jiKey: "lianzhen" },
            "丁": { lu: "太陰星", quan: "天同星", ke: "天機星", ji: "巨門星", luKey: "taiyin", quanKey: "tiantong", keKey: "tianji", jiKey: "jumen" },
            "戊": { lu: "貪狼星", quan: "太陰星", ke: "右弼星", ji: "天機星", luKey: "tanlang", quanKey: "taiyin", keKey: "youbi", jiKey: "tianji" },
            "己": { lu: "武曲星", quan: "貪狼星", ke: "天梁星", ji: "文曲星", luKey: "wuqu", quanKey: "tanlang", keKey: "tianliang", jiKey: "wenqu" },
            "庚": { lu: "太陽星", quan: "武曲星", ke: "太陰星", ji: "天同星", luKey: "taiyang", quanKey: "wuqu", keKey: "taiyin", jiKey: "tiantong" },
            "辛": { lu: "巨門星", quan: "太陽星", ke: "文曲星", ji: "文昌星", luKey: "jumen", quanKey: "taiyang", keKey: "wenqu", jiKey: "wenchang" },
            "壬": { lu: "天梁星", quan: "紫微星", ke: "左輔星", ji: "武曲星", luKey: "tianliang", quanKey: "ziwei", keKey: "zuofu", jiKey: "wuqu" },
            "癸": { lu: "破軍星", quan: "巨門星", ke: "太陰星", ji: "貪狼星", luKey: "pojun", quanKey: "jumen", keKey: "taiyin", jiKey: "tanlang" }
        };

        const curSihua = fourSihuaGans[targetGan] || fourSihuaGans["丙"];

        const findPalaceOfStar = (starKey) => {
            const cell = chartResult.chart.find(c => c.stars.some(s => s.key === starKey));
            return cell ? cell.palaceName : "本命宮";
        };

        const luPalace = findPalaceOfStar(curSihua.luKey);
        const quanPalace = findPalaceOfStar(curSihua.quanKey);
        const kePalace = findPalaceOfStar(curSihua.keKey);
        const jiPalace = findPalaceOfStar(curSihua.jiKey);

        const fortuneScore = Math.min(98, Math.max(68, 82 + (targetY % 7) * 2 - (age % 3) * 2));

        const guides = {
            career: `【事業功名與權柄拓展】${targetYear} 年歲次${targetGan}${targetZhi}，流年【${curSihua.quan}化權】發動，主動掌控與戰略擴張能量熾烈！職場主動出擊，適合推動大型變革、爭取領導權限或拓展業務新版圖。`,
            wealth: `【財帛利祿與資產佈局】流年【${curSihua.lu}化祿】坐入【${luPalace}】，資本現金流呈現正向活絡！宜專注於核心優勢資產投資，防範盲目投機，以結構化佈局鎖定長期利潤。`,
            social: `【貴人人脈與聲譽名望】流年【${curSihua.ke}化科】飛入【${kePalace}】，個人行業聲望與品牌公信力得到顯著加持！利於爭取行業榮譽、建立權威認證，易遇高階貴人引薦提攜。`,
            health: `【身心調攝與風險防禦】流年【${curSihua.ji}化忌】牽動【${jiPalace}】，提示該年需格外注重心血管、自律神經與深層壓力排解。宜嚴格落實作息風控，防範合約糾葛與官非是非。`,
            mindset: `【大師戰略決策心法】今年是『${curSihua.quan}主權、${curSihua.lu}生發』之進取之年。面對大勢，應明辨主次，「以正治國，以奇用兵」，在確立核心防線的前提下勇於開闢新局！`
        };

        return {
            targetYear: targetY,
            targetGan,
            targetZhi,
            zodiac,
            age,
            fortuneScore,
            currentDecade: `${currentDecadeCell.palaceName}大限（${currentDecadeCell.decadeAgeRange}歲）`,
            liunianMingPalace: liunianMingCell.palaceName,
            liunianMingZhi: targetZhi,
            sihua: {
                lu: { star: curSihua.lu, palace: luPalace, meaning: "機遇與資本流入" },
                quan: { star: curSihua.quan, palace: quanPalace, meaning: "權柄掌控與破局" },
                ke: { star: curSihua.ke, palace: kePalace, meaning: "聲望認證與名譽" },
                ji: { star: curSihua.ji, palace: jiPalace, meaning: "因果考驗與深潛" }
            },
            guides
        };
    },

    // 9. 未來十年運勢動態圖譜（大限十載結合流年飛星）
    calculateDecadeFortune(chartResult, startYear = 2026, count = 10) {
        const decadeData = [];
        const themeLibrary = [
            { title: "潛龍在淵・厚積薄發", keyword: "蓄勢期", desc: "如同大樹深扎地根。專注於專業核心技術與底層知識體系的深耕，不求速勝，以厚實實力構築不可撼動之護城河。" },
            { title: "風起雲湧・破局展拓", keyword: "突破期", desc: "多年沉澱迎來質變突破之關鍵節點！果斷抓住市場與行業轉軌機緣，臨場決策果敢凌厲，開啟嶄新事業篇章。" },
            { title: "見龍在田・視野拓疆", keyword: "拓疆期", desc: "走出既有體系邊界，跨界整合跨領域資源。眼界格局大幅提升，在更高維度的商業與管理競技場中初露崢嶸。" },
            { title: "羽翼豐碩・社群共振", keyword: "躍升期", desc: "行業威望與人脈網絡呈現指數級擴張。結盟頂尖夥伴，主導重要商業合作與戰略聯盟，確立行業樞紐地位。" },
            { title: "深耕細作・專業鼎盛", keyword: "鼎盛期", desc: "主責領域步入深水區與收穫期，個人權威與獨當一面的管理硬實力臻於成熟，斬獲重大商業回報與社會聲譽。" },
            { title: "風雲際會・跨國佈局", keyword: "擴張期", desc: "推動全球化視野或跨區域大規模擴張，實戰領導才能全面爆發，成為引領團隊與組織開疆闢土的核心舵手。" },
            { title: "天道酬勤・基石永固", keyword: "立基期", desc: "個人與家族之資產架構日益穩固，無論是獨立創業還是執掌集團權柄，皆展現出深謀遠慮的統帥氣魄。" },
            { title: "登高致遠・格局大成", keyword: "整合期", desc: "核心資本、行業聲望與優質人脈步入強大複利循環，學會宏觀資產佈局與資本運作，主導行業長遠走向。" },
            { title: "知行合一・豐盈持盈", keyword: "豐盈期", desc: "早年所積累的戰略定力與自律修為迎來全面回饋，事業、財富與精神修為達到圓融和諧之境。" },
            { title: "開闢新境・基業長青", keyword: "傳承期", desc: "十載宏圖週期圓滿告成，推動組織梯隊傳承與第二曲線孵化，昂首踏入下一個更高維度的永續里程碑！" }
        ];

        for (let i = 0; i < count; i++) {
            const currentYear = startYear + i;
            const liunian = this.calculateLiunian(chartResult, currentYear);
            const theme = themeLibrary[i % themeLibrary.length];

            let stageBadge = "";
            if (liunian.age <= 28) {
                stageBadge = "🏛️ 立基厚植・專業蓄勢";
            } else if (liunian.age <= 38) {
                stageBadge = "🚀 破局展拓・事業拓荒";
            } else if (liunian.age <= 50) {
                stageBadge = "👑 雄圖大展・格局大成";
            } else {
                stageBadge = "💎 豐盈持盈・基業長青";
            }

            decadeData.push({
                year: currentYear,
                ganZhi: `${liunian.targetGan}${liunian.targetZhi}`,
                zodiac: liunian.zodiac,
                age: liunian.age,
                currentDecade: liunian.currentDecade,
                stageBadge,
                score: liunian.fortuneScore,
                theme: theme.title,
                keyword: theme.keyword,
                desc: theme.desc,
                sihuaOverview: `祿在【${liunian.sihua.lu.palace}】 ｜ 權在【${liunian.sihua.quan.palace}】 ｜ 科在【${liunian.sihua.ke.palace}】 ｜ 忌在【${liunian.sihua.ji.palace}】`,
                careerAdvice: liunian.guides.career,
                wealthAdvice: liunian.guides.wealth,
                actionTip: liunian.guides.mindset
            });
        }

        return decadeData;
    }
};

window.ZiWeiSystem = ZiWeiSystem;
