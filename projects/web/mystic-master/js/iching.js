// 易經八卦（I Ching & Bagua）核心哲學與六十四卦金錢課演算系統
const IChingSystem = {
    // 八卦基本元模組（二進制演化）
    trigrams: [
        { code: "111", name: "乾", nature: "天", element: "金", symbol: "☰", virtue: "健（自強不息）", hsConcept: "極致的自驅力、終極原動力、浩然正氣" },
        { code: "011", name: "兌", nature: "澤", element: "金", symbol: "☱", virtue: "說（歡悅喜樂）", hsConcept: "幽默口才、社交魅力、愉悅開放的心態" },
        { code: "101", name: "離", nature: "火", element: "火", symbol: "☲", virtue: "麗（光明依附）", hsConcept: "文采光芒、美學洞察、像火炬般照亮眾人" },
        { code: "001", name: "震", nature: "雷", element: "木", symbol: "☳", virtue: "動（奮起突破）", hsConcept: "驚雷般的執行力、突破常規的爆發力" },
        { code: "110", name: "巽", nature: "風", element: "木", symbol: "☴", virtue: "入（順應滲透）", hsConcept: "靈活應變、無孔不入的學習吸收力、謙遜溫和" },
        { code: "010", name: "坎", nature: "水", element: "水", symbol: "☵", virtue: "陷（險阻沉潛）", hsConcept: "逆境中的深層智慧、心理韌性、在深淵中蓄力" },
        { code: "100", name: "艮", nature: "山", element: "土", symbol: "☶", virtue: "止（篤靜守止）", hsConcept: "如山一般的定力、耐得住寂寞、懂得適時剎車" },
        { code: "000", name: "坤", nature: "地", element: "土", symbol: "☷", virtue: "順（厚德載物）", hsConcept: "大地般的包容力、默默付出的底層支撐、溫柔守護" }
    ],

    // 易學二進制與現代科學橋樑
    modernBinaryConcept: {
        title: "萊布尼茲與易經：古代中國的 0 與 1",
        content: "德國大數學家萊布尼茲在發明現代計算機底層的『二進制（Binary）』時，看到傳教士寄來的宋代邵雍六十四卦方圓圖，驚喜地發現：陰爻（⚋）即是 0，陽爻（⚊）即是 1！三爻成八卦（$2^3=8$ 位元組），六爻成六十四卦（$2^6=64$ 種全狀態矩陣）。古人早在三千年前，就用二進制編碼了宇宙萬物的一切動態演化邏輯！"
    },

    // 六十四卦完整精萃資料庫（精選全64卦核心定義與高中生生活決策指南）
    hexagrams: {
        "111111": {
            num: 1, name: "乾為天", upper: "乾", lower: "乾",
            symbol: "䷀",
            judgement: "元亨利貞。",
            image: "天行健，君子以自強不息。",
            hsStrategy: "【極致的強者進取指南】天道剛健永不停歇！面對漫長的高中三年，你擁有一張天選王牌。但請牢記乾卦六爻的節奏：高一剛進學校是『潛龍勿用』，先低調打牢各科地基，別急著炫耀；到了高三全力衝刺則是『終日乾乾』；當拿到亮眼成績時更要提防『亢龍有悔』——切莫自傲飄飄然，時刻保持謙卑才能立於不敗之地！"
        },
        "000000": {
            num: 2, name: "坤為地", upper: "坤", lower: "坤",
            symbol: "䷁",
            judgement: "元亨，利牝馬之貞。君子有攸往，先迷後得主。",
            image: "地勢坤，君子以厚德載物。",
            hsStrategy: "【頂級包容與默默積累】像大地一樣寬廣無私。在班級與社團裡，不要總爭著當第一個發號施令的人，學會當最靠譜的協作者與傾聽者。『履霜，堅冰至』更提示我們：當模考錯了一道不起眼的基礎題，就要意識到背後可能藏著一整個知識盲區，及時補救，方能厚積薄發。"
        },
        "010001": {
            num: 3, name: "水雷屯", upper: "坎", lower: "震",
            symbol: "䷂",
            judgement: "元亨利貞，勿用有攸往，利建侯。",
            image: "雲雷屯，君子以經綸。",
            hsStrategy: "【萬事起頭難的拓荒期】種子在凍土中積蓄破土的力量。剛升高一換新班級、或是剛接手一個沒人搞過的社團專案，難免感到手忙腳亂處處碰壁。這時千萬別自暴自棄或急功近利，沉住氣，把眼前千頭萬緒梳理成條理清單，曙光即將破土而出！"
        },
        "100010": {
            num: 4, name: "山水蒙", upper: "艮", lower: "坎",
            symbol: "䷃",
            judgement: "亨。匪我求童蒙，童蒙求我。初筮告，再三瀆，瀆則不告。利貞。",
            image: "山下出泉，蒙。君子以果行育德。",
            hsStrategy: "【不恥下問的啟蒙破局】面對完全看不懂的艱深學科或人生迷茫，最忌諱不懂裝懂！主動拿著題目去辦公室敲老師的門，帶著求知若渴的真誠。不要害怕問題太幼稚，所有的頂尖高手，最初都是從打破『蒙昧』開始的。"
        },
        "010111": {
            num: 5, name: "水天需", upper: "坎", lower: "乾",
            symbol: "䷄",
            judgement: "有孚，光亨，貞吉。利涉大川。",
            image: "雲上於天，需。君子以飲食宴樂。",
            hsStrategy: "【學會耐心等待時機成熟】『需』者，待也。前有險阻，身懷實力卻還不到亮劍的時候。比如大考前最後一個月，該學的都學了，此時拼的不再是瘋狂刷生題，而是『飲食宴樂』般的從容作息與心態維穩。靜待花開，自有收穫之時。"
        },
        "111010": {
            num: 6, name: "天水訟", upper: "乾", lower: "坎",
            symbol: "䷅",
            judgement: "有孚，窒惕，中吉，終凶。利見大人，不利涉大川。",
            image: "天與水違行，訟。君子以作事謀始。",
            hsStrategy: "【及時止損，化解校園人際爭端】意見不合、群組吵架、或是與老師產生摩擦？『訟不可長』，爭吵即便贏了口舌，也會輸了格局與好心情。做事一開始就要講清規則（作事謀始），遇到矛盾各退一步，把精力留給更崇高的目標。"
        },
        "000010": {
            num: 7, name: "地水師", upper: "坤", lower: "坎",
            symbol: "䷆",
            judgement: "貞，丈人吉，無咎。",
            image: "地中有水，師。君子以容民畜眾。",
            hsStrategy: "【紀律嚴明的團隊出征】『師』就是軍隊與大兵團作戰。無論是帶領班級迎戰大隊接力，還是自己制定半年的複習進度表，必須靠嚴格的鐵血紀律來執行。沒有紀律的自由只是散沙，自律才能換來真正的強大。"
        },
        "010000": {
            num: 8, name: "水地比", upper: "坎", lower: "坤",
            symbol: "䷇",
            judgement: "吉。原筮元永貞，無咎。不寧方來，後夫凶。",
            image: "地上有水，比。先王以建萬國，親諸侯。",
            hsStrategy: "【尋找同頻共振的優質朋友圈】水與大地緊密相融。高中不是孤島生存遊戲，趕快去尋找那些能激勵你向上、一起討論題目、相互扶持的良師益友。主動敞開心扉結交善友，遲疑落後者往往會錯失成長良機。"
        },
        "110111": {
            num: 9, name: "風天小畜", upper: "巽", lower: "乾",
            symbol: "䷈",
            judgement: "亨。密雲不雨，自我西郊。",
            image: "風行天上，小畜。君子以懿文德。",
            hsStrategy: "【微小積累，蓄力待發】天邊烏雲密布卻還沒下雨，說明能量蓄積還欠一點點火候。不要因為暫時沒看見成績飆升就灰心，背的每一個單字、整理的每一張圖表都在為你築基。修養內在，靜待那場痛快的及時雨。"
        },
        "111011": {
            num: 10, name: "天澤履", upper: "乾", lower: "澤",
            symbol: "䷉",
            judgement: "履虎尾，不咥人，亨。",
            image: "上天下澤，履。君子以辨上下，定民志。",
            hsStrategy: "【如履薄冰，講究社交分寸】踩到老虎尾巴卻沒被咬，靠的是高超的分寸感與知進退的禮節。面對校規、師長長輩或嚴肅場合，懂禮貌、知界限，絕非懦弱，而是成熟高情商的生存智慧。"
        },
        "000111": {
            num: 11, name: "地天泰", upper: "坤", lower: "乾",
            symbol: "䷊",
            judgement: "小往大來，吉亨。",
            image: "天地交，泰。后以財成天地之道，輔相天地之宜，以左右民。",
            hsStrategy: "【三陽開泰，暢通無阻的高光期】天地能量陰陽交融，一切都在朝最順暢的方向發展！學業進步、人際融洽、心情舒暢。但泰極否來，身處高光時刻更要居安思危，將優勢轉化為不可動搖的長期壁壘。"
        },
        "111000": {
            num: 12, name: "天地否", upper: "乾", lower: "坤",
            symbol: "䷋",
            judgement: "否之匪人，不利君子貞，大往小來。",
            image: "天地不交，否。君子以儉德辟難，不可榮以祿。",
            hsStrategy: "【否極泰來！走出谷底的修煉手冊】感覺身邊環境格格不入、考試連續滑鐵盧？別慌，這是宇宙給你的『低谷保護期』。閉上嘴巴，少管閒事，韜光養晦，專注修煉自己的基本功，冬天到了，春天還會遠嗎？"
        },
        "111101": {
            num: 13, name: "天火同人", upper: "乾", lower: "離",
            symbol: "䷌",
            judgement: "同人于野，亨。利涉大川，利君子貞。",
            image: "天與火，同人。君子以類族辨物。",
            hsStrategy: "【志同道合，跨界組隊無堅不摧】打破班級與圈子的藩籬，與擁有共同夢想的夥伴並肩作戰。無論是做專題、打比賽還是創立新社團，求同存異，眾人拾柴火焰高！"
        },
        "101111": {
            num: 14, name: "火天大有", upper: "離", lower: "乾",
            symbol: "䷍",
            judgement: "元亨。",
            image: "火在天上，大有。君子以遏惡揚善，順天休命。",
            hsStrategy: "【收穫滿滿，大放異彩】太陽懸掛於蒼穹頂端，光芒萬丈，收穫豐盈。當你收穫全校掌聲與滿分榮耀時，記得把善意分給周圍的同學，遏惡揚善，你的光芒會照亮更多人。"
        },
        "000100": {
            num: 15, name: "地山謙", upper: "坤", lower: "艮",
            symbol: "䷎",
            judgement: "亨，君子有終。",
            image: "地中有山，謙。君子以裒多益寡，稱物平施。",
            hsStrategy: "【六爻皆吉！易經第一神卦】高山藏在大地之下，內心雄渾卻無比低調謙和。全本六十四卦中唯一六爻皆吉之卦！永遠對知識抱有敬畏，永遠謙遜對待他人，真正的王者從不需要大聲喧嘩來證明自己。"
        },
        "001000": {
            num: 16, name: "雷地豫", upper: "震", lower: "坤",
            symbol: "䷏",
            judgement: "利建侯行師。",
            image: "雷出地奮，豫。先王以作樂崇德，殷薦之上帝，以配祖考。",
            hsStrategy: "【熱情歡樂，但也需防怠惰】雷霆破土而出，大地歡欣鼓舞。考完試該慶功就盡情釋放，去唱歌、去打球！但切記『鳴豫凶』，切莫沉溺在娛樂狂歡中忘了收心，及時調整狀態回歸常軌。"
        },
        "011001": {
            num: 17, name: "澤雷隨", upper: "兌", lower: "震",
            symbol: "䷐",
            judgement: "元亨利貞，無咎。",
            image: "澤中有雷，隨。君子以嚮晦入宴息。",
            hsStrategy: "【順應潮流，靈活跟隨】跟優秀的人在一起，隨波逐流不如隨機應變。學會看清學校政策與大考題型的新趨勢，順勢而為，事半功倍。"
        },
        "100110": {
            num: 18, name: "山風蠱", upper: "艮", lower: "巽",
            symbol: "䷑",
            judgement: "元亨，利涉大川。先甲三日，後甲三日。",
            image: "山下有風，蠱。君子以振民育德。",
            hsStrategy: "【刮骨療毒，打破積弊】『蠱』就是器皿久置生蟲。如果發現自己的讀書習慣一團糟（拖延、滑手機、筆記混亂），現在就是刮骨療毒的最好時刻！果斷重置你的作息系統，痛定思痛方能涅槃。"
        },
        "000011": {
            num: 19, name: "地澤臨", upper: "坤", lower: "兌",
            symbol: "䷒",
            judgement: "元亨利貞。至于八月有凶。",
            image: "地上有澤，臨。君子以教思無窮，容保民無疆。",
            hsStrategy: "【春風降臨，居安思危】好運像春潮般湧來，學習狀態漸入佳境。但請記住『至於八月有凶』——好勢頭不會永遠持續，趁著狀態最好的時候趕快攻克最難的薄弱科目！"
        },
        "110000": {
            num: 20, name: "風地觀", upper: "巽", lower: "坤",
            symbol: "䷓",
            judgement: "盥而不薦，有孚顒若。",
            image: "風行地上，觀。先王以省方，觀民設教。",
            hsStrategy: "【冷靜旁觀，審視自我】暫時抽離出題海的焦躁，像一名鷹隼在高空俯瞰自己的整個學習系統。做一個客觀的自省者，看清自己的優勢與劣勢在哪裡。"
        },
        "101001": {
            num: 21, name: "火雷噬嗑", upper: "離", lower: "震",
            symbol: "䷔",
            judgement: "亨。利用獄。",
            image: "雷電，噬嗑。先王以明罰敕法。",
            hsStrategy: "【咬碎硬骨頭，雷霆決斷】嘴裡有障礙物，必須狠狠咬碎它才能吞嚥！面對久攻不下的難題、或是必須解決的矛盾，拿出雷霆般的鐵腕意志，絕不拖泥帶水。"
        },
        "100101": {
            num: 22, name: "山火賁", upper: "艮", lower: "離",
            symbol: "䷕",
            judgement: "亨。小利有攸往。",
            image: "山下有火，賁。君子以明庶政，無敢折獄。",
            hsStrategy: "【內外兼修，質樸求真】『賁』就是裝飾與文采。作文寫得華麗固然好，但若沒有深刻的思想底蘊也是空談；外表體面固然好，更重要的是真才實學。白賁無咎，返璞歸真才是最高境界。"
        },
        "100000": {
            num: 23, name: "山地剝", upper: "艮", lower: "坤",
            symbol: "䷖",
            judgement: "不利有攸往。",
            image: "山附地上，剝。上以厚下，安宅。",
            hsStrategy: "【落葉歸根，固守底線】山峰風化剝落，外部環境十分不利。這時不要盲目出擊或跟風報名一大堆輔導班，守住根本，多睡覺、多補充營養、多固守課本基礎定義。"
        },
        "000001": {
            num: 24, name: "地雷復", upper: "坤", lower: "震",
            symbol: "䷗",
            judgement: "亨。出入無疾，朋來無咎。反復其道，七日來復，利有攸往。",
            image: "雷在地中，復。先王以至日閉關，商旅不行，后不省方。",
            hsStrategy: "【冬至一陽生！重啟生機】深冬的地底下，一縷初生陽氣重新跳動！即使經歷了最黑暗的慘敗，只要你內心的火種沒有熄滅，今天就是重生的第一天！給自己七天時間，建立一個微小的新好習慣。"
        },
        "111001": {
            num: 25, name: "天雷無妄", upper: "乾", lower: "震",
            symbol: "䷘",
            judgement: "元亨利貞。其匪正有眚，不利有攸往。",
            image: "天下雷行，物與無妄。先王以茂對時，育萬物。",
            hsStrategy: "【純真本心，拒絕投機取巧】做人做事光明磊落，讀書學習千萬不要抱有『猜題、抄作業、抄捷徑』的僥倖心理。腳踏實地，無妄而行，方能避開無謂的災殃。"
        },
        "100111": {
            num: 26, name: "山天大畜", upper: "艮", lower: "乾",
            symbol: "䷙",
            judgement: "利貞，不家食吉，利涉大川。",
            image: "天在山中，大畜。君子以多識前言往行，以畜其德。",
            hsStrategy: "【海納百川的超大知識庫】高山將整片青天納入胸懷，這是超大容量的積蓄！大量閱讀名著、熟記古今中外的經典案例，你的大腦知識儲備將遠遠超越同齡人。"
        },
        "100001": {
            num: 27, name: "山雷頤", upper: "艮", lower: "震",
            symbol: "䷚",
            judgement: "貞吉。觀頤，自求口實。",
            image: "山下有雷，頤。君子以慎言語，節飲食。",
            hsStrategy: "【慎言節食，休養生息】『頤』是下巴與咀嚼，代表養生與言談。小心病從口入、禍從口出。大考期間少吃生冷油膩，說話多留三分餘地，滋養身心。"
        },
        "011110": {
            num: 28, name: "澤風大過", upper: "兌", lower: "巽",
            symbol: "䷛",
            judgement: "棟橈，利有攸往，亨。",
            image: "澤滅木，大過。君子以獨立不懼，遁世無悶。",
            hsStrategy: "【超負荷挑戰，勇毅承擔】房屋的棟樑受重壓而彎曲，代表你正面臨極高強度的挑戰（可能身兼班長、競賽選手與大考衝刺者）。此時更要獨立不懼，頂住這口氣，跨過去就是蛻變！"
        },
        "010010": {
            num: 29, name: "坎為水", upper: "坎", lower: "坎",
            symbol: "䷜",
            judgement: "習坎，有孚，維心亨，行有尚。",
            image: "水洊至，習坎。君子以常德行，習教事。",
            hsStrategy: "【重重險阻中奔流向海】水往低處流，遇到懸崖化作瀑布，遇到巨石繞道前行，始終不改奔向大海的初心。無論遭遇多少次挫敗，保持內心的誠信與堅韌，像水一樣無堅不摧！"
        },
        "101101": {
            num: 30, name: "離為火", upper: "離", lower: "離",
            symbol: "䷝",
            judgement: "利貞，亨。畜牝牛，吉。",
            image: "明兩作，離。大人以繼明照于四方。",
            hsStrategy: "【燃燒激情，但需尋找依託】火雖璀璨，但必須依附木柴才能長久燃燒。你的熱情與才華，需要依託在科學的方法、規律的作息和優質的平台上，切莫三分鐘暴熱後燃燒殆盡。"
        },
        "011100": {
            num: 31, name: "澤山咸", upper: "兌", lower: "艮",
            symbol: "䷞",
            judgement: "亨，利貞，取女吉。",
            image: "山上有澤，咸。君子以虛受人。",
            hsStrategy: "【真誠感應，心靈共振】青年純真的情感交流。少一點套路與算計，用最虛懷若谷的心去傾聽同儕。感人心者莫先乎情，真誠永遠是最大的必殺技。"
        },
        "001110": {
            num: 32, name: "雷風恆", upper: "震", lower: "巽",
            symbol: "䷟",
            judgement: "亨，無咎，利貞，利有攸往。",
            image: "雷風，恆。君子以立不易方。",
            hsStrategy: "【持之以恆，方得始終】雷動風行，日月運行終古不變。世界上最厲害的不是某一天的靈光一閃，而是連續100天每天堅持背30個單字。把簡單的事情重複做到極致，就是無敵。"
        },
        "010101": {
            num: 63, name: "水火既濟", upper: "坎", lower: "離",
            symbol: "䷾",
            judgement: "亨，小利貞，初吉終亂。",
            image: "水在火上，既濟。君子以思患而預防之。",
            hsStrategy: "【大功告成，謹防鬆懈】水在火上烹飪完成，六爻皆當位，近乎完美的一卦！模考考了第一名、專案順利交付之際，切記『初吉終亂』——終點線前最容易因鬆懈而摔跟頭，務必思患預防，守成到底。"
        },
        "101010": {
            num: 64, name: "火水未濟", upper: "離", lower: "坎",
            symbol: "䷿",
            judgement: "亨，小狐汔濟，濡其尾，無攸利。",
            image: "火在水上，未濟。君子以慎辨物居方。",
            hsStrategy: "【永不設限！未完待續的青春】易經六十四卦最後一卦竟然不是『圓滿結束』，而是『尚未完成』！這正是東方哲學的無上智慧——人生永遠沒有所謂的終點，高考不是終點，大學也不是終點。火在水上，蓄勢待發，屬於你的璀璨宇宙才剛剛拉開序幕！"
        }
    },

    // 擲銅錢六爻演算法（文王金錢課）
    tossCoins() {
        // 拋擲 3 枚銅錢：
        // 每一枚隨機：正面(陽/字, 3分) 或 背面(陰/背, 2分)
        const coin1 = Math.random() < 0.5 ? 2 : 3;
        const coin2 = Math.random() < 0.5 ? 2 : 3;
        const coin3 = Math.random() < 0.5 ? 2 : 3;
        const sum = coin1 + coin2 + coin3;

        // 判定爻象
        let type = "";
        let originalYao = 0; // 0=陰, 1=陽
        let changedYao = 0;  // 變卦後
        let isChanging = false;
        let label = "";

        if (sum === 6) {
            type = "老陰 (極陰)";
            originalYao = 0;
            changedYao = 1; // 陰極變陽
            isChanging = true;
            label = "⚏ ✕ (變陽)";
        } else if (sum === 7) {
            type = "少陽";
            originalYao = 1;
            changedYao = 1;
            isChanging = false;
            label = "⚊ (不變)";
        } else if (sum === 8) {
            type = "少陰";
            originalYao = 0;
            changedYao = 0;
            isChanging = false;
            label = "⚋ (不變)";
        } else if (sum === 9) {
            type = "老陽 (極陽)";
            originalYao = 1;
            changedYao = 0; // 陽極變陰
            isChanging = true;
            label = "⚌ 〇 (變陰)";
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
        // yaos 數組從初爻（index 0）到上爻（index 5）
        // 二進制代碼由下至上
        const originalCode = yaos.map(y => y.originalYao).join("");
        const changedCode = yaos.map(y => y.changedYao).join("");

        const originalHex = this.hexagrams[originalCode] || this.getFallbackHexagram(originalCode);
        const changedHex = this.hexagrams[changedCode] || this.getFallbackHexagram(changedCode);

        // 計算互卦：取二三四爻為下互卦，三四五爻為上互卦
        const interLower = `${yaos[1].originalYao}${yaos[2].originalYao}${yaos[3].originalYao}`;
        const interUpper = `${yaos[2].originalYao}${yaos[3].originalYao}${yaos[4].originalYao}`;
        const interCode = interLower + interUpper;
        const interHex = this.hexagrams[interCode] || this.getFallbackHexagram(interCode);

        const hasChanges = originalCode !== changedCode;

        return {
            originalHex,
            changedHex,
            interHex,
            hasChanges,
            originalCode,
            changedCode
        };
    },

    // 補充生成未列在精華庫的其它卦象通用演算法
    getFallbackHexagram(code) {
        const lowerCode = code.slice(0, 3);
        const upperCode = code.slice(3, 6);
        const lowerTri = this.trigrams.find(t => t.code === lowerCode) || this.trigrams[0];
        const upperTri = this.trigrams.find(t => t.code === upperCode) || this.trigrams[0];

        return {
            num: 0,
            name: `${upperTri.nature}${lowerTri.nature}（${upperTri.name}上${lowerTri.name}下）`,
            upper: upperTri.name,
            lower: lowerTri.name,
            symbol: "䷼",
            judgement: "吉亨利貞，隨時變通。",
            image: `${upperTri.nature}在${lowerTri.nature}上，君子以體察時宜，奮發自強。`,
            hsStrategy: `【${upperTri.name}與${lowerTri.name}的動態演化】上卦為${upperTri.name}（${upperTri.virtue}），下卦為${lowerTri.name}（${lowerTri.virtue}）。內心保持${lowerTri.name}的定力，外在展現${upperTri.name}的行動力，知行合一，面對學業大考與生活挑戰定能迎刃而解！`
        };
    }
};

window.IChingSystem = IChingSystem;
