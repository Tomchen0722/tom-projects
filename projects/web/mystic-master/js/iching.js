// ==========================================================================
// 周易大成殿：易經八卦（I Ching & Bagua）正統專業大師決策系統
// 涵蓋：二進制矩陣演化、文王金錢課六爻占筮、六十四卦正統卦象與戰略決策指南
// ==========================================================================

const IChingSystem = {
    // 八卦基本元模組（二進制演化）
    trigrams: [
        { code: "111", name: "乾", nature: "天", element: "金", symbol: "☰", virtue: "健（自強不息）", proConcept: "終極原動力、剛健中正、開闢天地的領袖意志" },
        { code: "011", name: "兌", nature: "澤", element: "金", symbol: "☱", virtue: "說（歡悅喜樂）", proConcept: "卓絕言辭說服力、和諧談判、共贏協同之情商" },
        { code: "101", name: "離", nature: "火", element: "火", symbol: "☲", virtue: "麗（光明依附）", proConcept: "文明洞察、品牌公信、如炬火般照徹迷局" },
        { code: "001", name: "震", nature: "雷", element: "木", symbol: "☳", virtue: "動（奮起突破）", proConcept: "雷霆行動力、打破舊體制之開拓殺氣" },
        { code: "110", name: "巽", nature: "風", element: "木", symbol: "☴", virtue: "入（順應滲透）", proConcept: "審時度勢、深度市場滲透、無孔不入的靈活應變" },
        { code: "010", name: "坎", nature: "水", element: "水", symbol: "☵", virtue: "陷（險阻沉潛）", proConcept: "險境中的深沉智慧、穿越週期的強大心理韌性" },
        { code: "100", name: "艮", nature: "山", element: "土", symbol: "☶", virtue: "止（篤靜守止）", proConcept: "如山般的定力風控、審慎底線思維、適時止損" },
        { code: "000", name: "坤", nature: "地", element: "土", symbol: "☷", virtue: "順（厚德載物）", proConcept: "大地般的承載包容力、基底組織支撐、長期主義" }
    ],

    // 易學二進制與現代科學橋樑
    modernBinaryConcept: {
        title: "萊布尼茲與周易：古代東方的 0 與 1 動態矩陣",
        content: "德國哲學家兼數學家萊布尼茲在創立現代計算機基礎「二進制（Binary）」時，研讀宋代邵雍六十四卦伏羲方圓圖，驚喜地發現：陰爻（⚋）即是 0，陽爻（⚊）即是 1！三爻成八卦（2³=8 位元組），六爻成六十四卦（2⁶=64 種全狀態矩陣）。古人早在三千年前，便以嚴密的數學邏輯編碼了宇宙萬物的一切動態演化法則！"
    },

    // 六十四卦正統大師戰略決策手冊
    hexagrams: {
        "111111": {
            num: 1, name: "乾為天", upper: "乾", lower: "乾",
            symbol: "䷀",
            judgement: "元亨利貞。",
            image: "天行健，君子以自強不息。",
            proStrategy: "【高階領袖自強進取指南】天道剛健運轉不息，手握至高主動權。但需恪守乾卦六爻的節奏：初期蓄勢宜「潛龍勿用」，切莫急於冒進；步入擴張期則「終日乾乾」，時刻如履薄冰；取得重大成功時更須警惕「亢龍有悔」——功高莫自傲，居安思危方能基業長青。"
        },
        "000000": {
            num: 2, name: "坤為地", upper: "坤", lower: "坤",
            symbol: "䷁",
            judgement: "元亨，利牝馬之貞。君子有攸往，先迷後得主。",
            image: "地勢坤，君子以厚德載物。",
            proStrategy: "【厚德載物與長青積累指南】像大地一樣寬廣博大。在大型組織與商業生態中，學會做賦能者與平台的堅固基石。「履霜，堅冰至」，當察覺到微小的市場異動或管理漏洞時，必須見微知著、未雨綢繆，方能厚積薄發、立於不敗之地。"
        },
        "010001": {
            num: 3, name: "水雷屯", upper: "坎", lower: "震",
            symbol: "䷂",
            judgement: "元亨利貞，勿用有攸往，利建侯。",
            image: "雲雷屯，君子以經綸。",
            proStrategy: "【草創拓荒與混亂治理指南】種子於凍土深處蓄力萌發。萬事起頭難，在全新業務立項或企業開拓初期，各方秩序尚未確立，切忌盲目急於求成。宜建構組織框架（利建侯）、梳理內部紛繁流程（君子以經綸），沉著應變，破土破局指日可待。"
        },
        "100010": {
            num: 4, name: "山水蒙", upper: "艮", lower: "坎",
            symbol: "䷃",
            judgement: "亨。匪我求童蒙，童蒙求我。初筮告，再三瀆，瀆則不告。利貞。",
            image: "山下出泉，蒙。君子以果行育德。",
            proStrategy: "【破除蒙昧與專業求真指南】面對全新未知領域或前沿賽道，最忌不懂裝懂或主觀臆斷。宜抱持求知若渴的真誠態度向行業泰斗請益。樹立標準，知錯即改，所有頂級企業皆是在不斷打破自身認知局限中走向卓越。"
        },
        "010111": {
            num: 5, name: "水天需", upper: "坎", lower: "乾",
            symbol: "䷄",
            judgement: "有孚，光亨，貞吉。利涉大川。",
            image: "雲上於天，需。君子以飲食宴樂。",
            proStrategy: "【耐力等待與週期應對指南】「需者，待也」。前有險阻，身懷實力而時機未至，切莫強行出擊。此時應做的是「飲食宴樂」般的修養生息、優化財務現金流與團隊心性。保持誠信定力，靜待政策與市場窗口成熟，屆時自可大展宏圖。"
        },
        "111010": {
            num: 6, name: "天水訟", upper: "乾", lower: "坎",
            symbol: "䷅",
            judgement: "有孚，窒惕，中吉，終凶。利見大人，不利涉大川。",
            image: "天與水違行，訟。君子以作事謀始。",
            proStrategy: "【及時止損與爭端化解指南】利益分歧、合約糾紛或商業博弈之中，「訟不可長」。即便在言辭或法務上爭得一時之利，若陷入長期纏訟亦將重創品牌與精力。行事之初當「作事謀始」，明確邊界與規則，化干戈為玉帛，專注於長遠目標。"
        },
        "000010": {
            num: 7, name: "地水師", upper: "坤", lower: "坎",
            symbol: "䷆",
            judgement: "貞，丈人吉，無咎。",
            image: "地中有水，師。君子以容民畜眾。",
            proStrategy: "【鐵血紀律與戰略出征指南】「師」者，軍隊大戰役也。無論是主持重大商業攻堅還是引領大型跨國團隊，必須仰賴鐵面無私的合規紀律與德高望重之核心主帥（丈人）。慈不掌兵，唯有紀律森嚴與賞罰分明，方能在殘酷商業競爭中克敵制勝。"
        },
        "010000": {
            num: 8, name: "水地比", upper: "坎", lower: "坤",
            symbol: "䷇",
            judgement: "吉。原筮元永貞，無咎。不寧方來，後夫凶。",
            image: "地上有水，比。先王以建萬國，親諸侯。",
            proStrategy: "【合縱連橫與戰略盟友指南】水入大地，親密無間。現代商業不是孤立零和博弈，而是構建生態聯盟。主動結交能夠賦能彼此的戰略夥伴，迅速確立合作樞紐；遲疑徘徊、坐失良機者（後夫凶）往往將被邊緣化。"
        },
        "110111": {
            num: 9, name: "風天小畜", upper: "巽", lower: "乾",
            symbol: "䷈",
            judgement: "亨。密雲不雨，自我西郊。",
            image: "風行天上，小畜。君子以懿文德。",
            proStrategy: "【細密積累與蓄力待發指南】烏雲密佈而甘霖未降，說明蓄積之力尚差最後一步。此時切忌盲目擴張或提前變現。沉下心來修練內部功力（懿文德）、打磨核心產品細節，為迎接全面爆發的市場轉折做好萬全準備。"
        },
        "111011": {
            num: 10, name: "天澤履", upper: "乾", lower: "澤",
            symbol: "䷉",
            judgement: "履虎尾，不咥人，亨。",
            image: "上天下澤，履。君子以辨上下，定民志。",
            proStrategy: "【如履薄冰與高階風控指南】身處高危博弈或直面強大監管對手，如同「踩在老虎尾巴上」。能全身而退並取得亨通，全靠極致的分寸感、對法規邊界的敬畏與冷靜周密的應對禮數。敬畏規則，方能在刀鋒起舞中取得至高勝利。"
        },
        "000111": {
            num: 11, name: "地天泰", upper: "坤", lower: "乾",
            symbol: "䷊",
            judgement: "小往大來，吉亨。",
            image: "天地交，泰。后以財成天地之道，輔相天地之宜，以左右民。",
            proStrategy: "【三陽開泰與鼎盛期擴張指南】天地陰陽相交，上下同心，各項指標皆處於最順遂的高光階段！但「泰極否來」，身處盛世更需居安思危，將眼前的溢價紅利轉化為不可動搖的固定資產與核心技術壁壘，方能打破興衰宿命。"
        },
        "111000": {
            num: 12, name: "天地否", upper: "乾", lower: "坤",
            symbol: "䷋",
            judgement: "否之匪人，不利君子貞，大往小來。",
            image: "天地不交，否。君子以儉德辟難，不可榮以祿。",
            proStrategy: "【閉關自守與穿越寒冬指南】外部環境嚴峻寒凍，上下溝通阻滯。此時切莫逆勢強行開拓或重金下注。應「儉德辟難」，嚴格收縮戰線，控制現金流消耗，保護核心骨幹與體系元氣。寒冬正是最好的沈澱期，深蹲方能高起。"
        },
        "111101": {
            num: 13, name: "天火同人", upper: "乾", lower: "離",
            symbol: "䷌",
            judgement: "同人于野，亨。利涉大川，利君子貞。",
            image: "天與火，同人。君子以類族辨物。",
            proStrategy: "【大同願景與跨國跨界協同指南】「同人于野」，打破宗派與壁壘，基於宏大共同願景招攬天下英才。求同存異，以公正無私的制度激勵夥伴，眾人拾柴火焰高，利於推動跨行業併購與大規模跨界重組。"
        },
        "101111": {
            num: 14, name: "火天大有", upper: "離", lower: "乾",
            symbol: "䷍",
            judgement: "元亨。",
            image: "火在天上，大有。君子以遏惡揚善，順天休命。",
            proStrategy: "【事業大成與財富向善指南】太陽懸掛於九天之上，光耀八荒，收穫碩果累累。當企業或個人登上財富與聲望巔峰之際，最核心的修為是「遏惡揚善，順天休命」——承擔社會責任，回饋公眾，方能使宏大財富轉化為崇高福澤。"
        },
        "000100": {
            num: 15, name: "地山謙", upper: "坤", lower: "艮",
            symbol: "䷎",
            judgement: "亨，君子有終。",
            image: "地中有山，謙。君子以裒多益寡，稱物平施。",
            proStrategy: "【周易唯一六爻皆吉之神卦】巍峨高山深藏於大地之下，實力雄渾卻內斂無比。《易經》六十四卦中唯有謙卦六爻皆吉！真正的行業泰斗與頂級智者從不需要虛張聲勢，以退為進、平衡各方利益（裒多益寡），終成不可動搖之終身基業。"
        },
        "001000": {
            num: 16, name: "雷地豫", upper: "震", lower: "坤",
            symbol: "䷏",
            judgement: "利建侯行師。",
            image: "雷出地奮，豫。先王以作樂崇德，殷薦之上帝，以配祖考。",
            proStrategy: "【熱情振奮與防止懈怠指南】驚雷破土，萬象歡欣。取得階段性大捷後，宜及時論功行賞、提振士氣；但切莫沉溺於慶祝而迷失警惕（鳴豫凶），應趁團隊士氣高昂之際，迅速將勝利果實沉澱為制度成果。"
        },
        "011001": {
            num: 17, name: "澤雷隨", upper: "兌", lower: "震",
            symbol: "䷐",
            judgement: "元亨利貞，無咎。",
            image: "澤中有雷，隨。君子以嚮晦入宴息。",
            proStrategy: "【順應週期與順勢而為指南】善於順應時代大勢與客觀規律者立大功。不要與歷史趨勢和市場週期對抗，學會跟隨最頂尖的技術浪潮與政策走向，借力使力，順勢而為，方能以最小代價取得最大戰果。"
        },
        "100110": {
            num: 18, name: "山風蠱", upper: "艮", lower: "巽",
            symbol: "䷑",
            judgement: "元亨，利涉大川。先甲三日，後甲三日。",
            image: "山下有風，蠱。君子以振民育德。",
            proStrategy: "【改革除弊與組織刮骨療毒指南】「蠱」者，器皿久置而生蟲蠹。當組織陷入體制僵化、官僚主義或流程弊端時，必須拿出壯士斷腕的刮骨勇氣推行改革！謀定而後動（先甲三日，後甲三日），破除積弊，迎來新生。"
        },
        "000011": {
            num: 19, name: "地澤臨", upper: "坤", lower: "兌",
            symbol: "䷒",
            judgement: "元亨利貞。至于八月有凶。",
            image: "地上有澤，臨。君子以教思無窮，容保民無疆。",
            proStrategy: "【居高臨下與居安思危指南】好運如春水上漲，管理成效顯著。但卦辭嚴厲提示「至于八月有凶」——繁榮的窗口期並非無限，趁當前資源充裕與地位穩固之時，迅速攻堅核心技術與短板，防止週期下行時遭遇挫敗。"
        },
        "110000": {
            num: 20, name: "風地觀", upper: "巽", lower: "坤",
            symbol: "䷓",
            judgement: "盥而不薦，有孚顒若。",
            image: "風行地上，觀。先王以省方，觀民設教。",
            proStrategy: "【宏觀審視與戰略自省指南】暫時從日常瑣碎的事務性運營中抽離出來，如同在高空俯瞰整個產業棋局。做客觀冷靜的戰略自省者，全面洞察市場底層趨勢與用戶真實訴求，以靜制動，謀定先機。"
        },
        "101001": {
            num: 21, name: "火雷噬嗑", upper: "離", lower: "震",
            symbol: "䷔",
            judgement: "亨。利用獄。",
            image: "雷電，噬嗑。先王以明罰敕法。",
            proStrategy: "【雷霆手段與破除梗阻指南】口中有阻礙物，必須狠狠咬碎方能吞嚥！面對久拖不決的重大阻礙、合約違約或腐敗弊病，不可姑息妥協。拿出雷霆般的法治手腕，明正典刑，徹底清除阻礙，暢通全局。"
        },
        "100101": {
            num: 22, name: "山火賁", upper: "艮", lower: "離",
            symbol: "䷕",
            judgement: "亨。小利有攸往。",
            image: "山下有火，賁。君子以明庶政，無敢折獄。",
            proStrategy: "【品牌包裝與返璞歸真指南】「賁」者，修飾文采也。高階品牌行銷與外在形象固然不可或缺，但若無過硬的核心產品質量與技術底蘊，終是空中樓閣。「白賁無咎」，商業競爭最終比拼的依然是本質實力，返璞歸真方為最高境界。"
        },
        "100000": {
            num: 23, name: "山地剝", upper: "艮", lower: "坤",
            symbol: "䷖",
            judgement: "不利有攸往。",
            image: "山附地上，剝。上以厚下，安宅。",
            proStrategy: "【防守固本與護持根基指南】山體剝落，外部形勢急劇惡化，小人道長、君子道消。此時不可冒險推進任何激進的擴張方案。應「厚下安宅」，保護基層核心人才與基礎資產，固守底線，等待天地氣數之重置。"
        },
        "000001": {
            num: 24, name: "地雷復", upper: "坤", lower: "震",
            symbol: "䷗",
            judgement: "亨。出入無疾，朋來無咎。反復其道，七日來復，利有攸往。",
            image: "雷在地中，復。先王以至日閉關，商旅不行，后不省方。",
            proStrategy: "【冬至一陽生與全面復甦指南】極致嚴冬的地心深處，初生陽氣重新躍動！經歷重大挫敗或行業寒冬後，生機已然破土而出。給予自己靜止蓄勢之期（至日閉關），從建立最小可行性方案（MVP）重新出發，大勢已定，前途不可限量。"
        },
        "111001": {
            num: 25, name: "天雷無妄", upper: "乾", lower: "震",
            symbol: "䷘",
            judgement: "元亨利貞。其匪正有眚，不利有攸往。",
            image: "天下雷行，物與無妄。先王以茂對時，育萬物。",
            proStrategy: "【堅守誠信與杜絕投機指南】做人立身、治企運營必須光明磊落，不可抱有任何抄捷徑、打擦邊球或虛假宣傳之僥倖心理。順應天理天時，無妄而行，方能徹底免除官非是非與致命黑天鵝。"
        },
        "100111": {
            num: 26, name: "山天大畜", upper: "艮", lower: "乾",
            symbol: "䷙",
            judgement: "利貞。不家食吉，利涉大川。",
            image: "天在山中，大畜。君子以多識前言往行，以畜其德。",
            proStrategy: "【海納百川的大資本儲備指南】崇山峻嶺將整片青天納入懷中，乃極具宏偉之蓄積格局！博採天下菁英思想，儲備充足的戰略資本、技術專利與行業威望，一旦發動，定能跨越滄海、成就跨國級霸業。"
        },
        "100001": {
            num: 27, name: "山雷頤", upper: "艮", lower: "震",
            symbol: "䷚",
            judgement: "貞吉。觀頤，自求口實。",
            image: "山下有雷，頤。君子以慎言語，節飲食。",
            proStrategy: "【慎言節用與組織生態涵養指南】「頤」者，口頰咀嚼與養生之象。審視自身的商業模式究竟以何種方式謀取利潤（觀頤，自求口實）。對外「慎言語」防範輿情危機，對內「節開支」降低非核心成本，精細涵養組織生命力。"
        },
        "011110": {
            num: 28, name: "澤風大過", upper: "兌", lower: "巽",
            symbol: "䷛",
            judgement: "棟橈，利有攸往，亨。",
            image: "澤滅木，大過。君子以獨立不懼，遁世無悶。",
            proStrategy: "【極限高壓與非常時期擔當指南】大樑受千鈞重壓而彎曲，象徵處於非同尋常的歷史十字路口或超負荷挑戰。此時唯有具備「獨立不懼」的鋼鐵意志與破釜沉舟之魄力，頂住極限壓力完成戰略重組，方能絕地逢生。"
        },
        "010010": {
            num: 29, name: "坎為水", upper: "坎", lower: "坎",
            symbol: "䷜",
            judgement: "習坎，有孚，維心亨，行有尚。",
            image: "水洊至，習坎。君子以常德行，習教事。",
            proStrategy: "【重重險阻與水性堅韌指南】一險未平，一險又至。流水奔赴向海，逢坎而盈，始終不改其初心。面臨市場接踵而至的黑天鵝衝擊，保持內心信念與契約誠信（有孚維心亨），如同水一樣順勢而變、無堅不摧！"
        },
        "101101": {
            num: 30, name: "離為火", upper: "離", lower: "離",
            symbol: "䷝",
            judgement: "利貞，亨。畜牝牛，吉。",
            image: "明兩作，離。大人以繼明照于四方。",
            proStrategy: "【光明普照與尋求正道依託指南】火焰璀璨耀眼，但必須依附薪柴方能持續發光。才華、野心與戰略必須依託於合法合規、優質平台與長青賽道之中，切莫孤身單打獨鬥，蓄養柔順溫潤之美德（畜牝牛），方能照耀四方。"
        },
        "011100": {
            num: 31, name: "澤山咸", upper: "兌", lower: "艮",
            symbol: "䷞",
            judgement: "亨，利貞，取女吉。",
            image: "山上有澤，咸。君子以虛受人。",
            proStrategy: "【真誠感通與高階共贏共鳴指南】高山頂端涵養清澈大澤，以至誠之心與各方利益主體感通。「君子以虛受人」，以虛懷若谷之胸懷傾聽用戶、合夥人與員工心聲。真誠是商業溝通與品牌凝聚力的至高法門。"
        },
        "001110": {
            num: 32, name: "雷風恆", upper: "震", lower: "巽",
            symbol: "䷟",
            judgement: "亨，無咎，利貞，利有攸往。",
            image: "雷風，恆。君子以立不易方。",
            proStrategy: "【長期主義與持之以恆指南】雷動風行，相伴不息。世界上最具威力的商業模式往往不是某一刻的靈光一閃，而是十年如一日堅持做難而正確的事。「立不易方」，恪守核心使命與戰略定力，時間的複利終將擊潰一切短期喧囂。"
        },
        "010101": {
            num: 63, name: "水火既濟", upper: "坎", lower: "離",
            symbol: "䷾",
            judgement: "亨，小利貞，初吉終亂。",
            image: "水在火上，既濟。君子以思患而預防之。",
            proStrategy: "【大功告成與終極守成指南】水火交融、六爻皆當位，近乎完美的大成之象！然而卦辭發出嚴厲警告：「初吉終亂」。在專案成功交付、企業上市或達到巔峰之時，最易因驕奢鬆懈而引發內部崩解，務必「思患而預防之」，嚴陣以待。"
        },
        "101010": {
            num: 64, name: "火水未濟", upper: "離", lower: "坎",
            symbol: "䷿",
            judgement: "亨，小狐汔濟，濡其尾，無攸利。",
            image: "火在水上，未濟。君子以慎辨物居方。",
            proStrategy: "【永不設限與二次曲線啟程指南】周易六十四卦之終卷，非圓滿終結，而是「尚未結束」！此乃東方文明至深哲思——宇宙生命永無止境，每一次巔峰皆是下一個全新週期的起點。謹慎辨析全新格局，開闢第二成長曲線，璀璨征程永不落幕！"
        }
    },

    // 擲銅錢六爻演算法（文王金錢課）
    tossCoins() {
        const coin1 = Math.random() < 0.5 ? 2 : 3;
        const coin2 = Math.random() < 0.5 ? 2 : 3;
        const coin3 = Math.random() < 0.5 ? 2 : 3;
        const sum = coin1 + coin2 + coin3;

        let type = "";
        let originalYao = 0;
        let changedYao = 0;
        let isChanging = false;
        let label = "";

        if (sum === 6) {
            type = "老陰 (極陰)";
            originalYao = 0;
            changedYao = 1;
            isChanging = true;
            label = "⚏ ✕ (動爻變陽)";
        } else if (sum === 7) {
            type = "少陽";
            originalYao = 1;
            changedYao = 1;
            isChanging = false;
            label = "⚊ (靜爻不變)";
        } else if (sum === 8) {
            type = "少陰";
            originalYao = 0;
            changedYao = 0;
            isChanging = false;
            label = "⚋ (靜爻不變)";
        } else if (sum === 9) {
            type = "老陽 (極陽)";
            originalYao = 1;
            changedYao = 0;
            isChanging = true;
            label = "⚌ 〇 (動爻變陰)";
        }

        return {
            coins: [coin1, coin2, coin3],
            sum,
            type,
            originalYao,
            changedYao,
            isChanging,
            label
        };
    },

    // 解析六爻結果得出本卦與變卦
    resolveHexagram(yaos) {
        const originalCode = yaos.map(y => y.originalYao).join("");
        const changedCode = yaos.map(y => y.changedYao).join("");

        const originalHex = this.hexagrams[originalCode] || this.getFallbackHexagram(originalCode);
        const changedHex = this.hexagrams[changedCode] || this.getFallbackHexagram(changedCode);

        // 計算互卦：二三四爻為下互，三四五爻為上互
        const interLower = `${yaos[1].originalYao}${yaos[2].originalYao}${yaos[3].originalYao}`;
        const interUpper = `${yaos[2].originalYao}${yaos[3].originalYao}${yaos[4].originalYao}`;
        const interCode = interLower + interUpper;
        const interHex = this.hexagrams[interCode] || this.getFallbackHexagram(interCode);

        const hasChanges = originalCode !== changedCode;

        // 確保相容性
        if (!originalHex.hsStrategy) originalHex.hsStrategy = originalHex.proStrategy;
        if (!changedHex.hsStrategy) changedHex.hsStrategy = changedHex.proStrategy;
        if (!interHex.hsStrategy) interHex.hsStrategy = interHex.proStrategy;

        return {
            originalHex,
            changedHex,
            interHex,
            hasChanges,
            originalCode,
            changedCode
        };
    },

    getFallbackHexagram(code) {
        const lowerCode = code.slice(0, 3);
        const upperCode = code.slice(3, 6);
        const lowerTri = this.trigrams.find(t => t.code === lowerCode) || this.trigrams[0];
        const upperTri = this.trigrams.find(t => t.code === upperCode) || this.trigrams[0];

        const strategy = `【${upperTri.name}與${lowerTri.name}的動態演化】上卦為${upperTri.name}（${upperTri.virtue}），下卦為${lowerTri.name}（${lowerTri.virtue}）。內心堅守${lowerTri.name}之戰略定力，外在展現${upperTri.name}之卓越破局力，知行合一，面對重大決策與時代浪潮定能從容破局！`;

        return {
            num: 0,
            name: `${upperTri.nature}${lowerTri.nature}（${upperTri.name}上${lowerTri.name}下）`,
            upper: upperTri.name,
            lower: lowerTri.name,
            symbol: "䷼",
            judgement: "吉亨利貞，隨時變通。",
            image: `${upperTri.nature}在${lowerTri.nature}上，君子以體察時宜，奮發自強。`,
            proStrategy: strategy,
            hsStrategy: strategy
        };
    }
};

// 相容性掛載
Object.values(IChingSystem.hexagrams).forEach(h => {
    if (!h.hsStrategy) h.hsStrategy = h.proStrategy;
});

window.IChingSystem = IChingSystem;
