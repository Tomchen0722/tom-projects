// 紫微斗數（Zi Wei Dou Shu）核心資料庫與排盤演算法
const ZiWeiSystem = {
    // 十四主星核心知識庫
    stars: {
        ziwei: {
            name: "紫微星",
            element: "己土（陰土）",
            title: "帝王之星 / 北斗主星",
            archetype: "👑 天生領袖：兼具格局與威儀的自治會長",
            desc: "紫微為北斗主星，象徵尊貴、統禦與大局觀。它天生自帶氣場，不甘居於人下，喜歡站在高處俯瞰全局。",
            hsAnalogy: "就像班上或學生會裡那位自帶威信的領袖，不是靠大聲吼叫，而是天然有一種讓人信服的氣度。做事注重體面與秩序，但也容易因為愛面子而不敢在大家面前承認自己的軟弱。",
            strengths: ["天生具備大局統禦能力", "處事沉穩有威信", "自我要求極高，追求卓越", "包容力強，能整合多元資源"],
            blindspots: ["好勝心強，過於愛面子", "容易眼高手低，忽視底層細節", "獨斷專行時容易讓人感到難以親近"],
            studyGuide: "適合宏觀體系建構法。讀書時切忌死記硬背零碎題目，應先畫出整章知識樹（Mindmap），掌握核心框架後再層層推導，成績會非常拔尖。推薦挑戰管理、法政、總體經濟等大格局領域。",
            examMindset: "大考前切莫因為一兩次模考未達預期而心浮氣躁。你是長線王者，保持帝王般的沉著，把目光放在終局目標上。"
        },
        tianji: {
            name: "天機星",
            element: "乙木（陰木）",
            title: "智多星 / 南斗第一星",
            archetype: "🧠 策略大腦：奧林匹亞與競賽策劃神人",
            desc: "天機為智慧之星、謀略之星。思維敏捷，善於推演邏輯與應對多變環境，對新科技、新趨勢有極高嗅覺。",
            hsAnalogy: "他是班上的『戰術分析師』。老師剛出完一道物理或數學難題，大家都還在看題目，他的腦袋已經在跑三種解題路徑了。喜歡研究捷徑與公式推導，但有時想太多容易自己陷入思維死胡同。",
            strengths: ["超群的邏輯推理與演算法思維", "應變速度極快，適應力強", "求知慾旺盛，善於吸收跨界新知", "熱心出謀劃策"],
            blindspots: ["神經質，思慮過度導致失眠或焦慮", "容易三分鐘熱度，缺乏持久耐力", "遇事易糾結細節而猶豫不決"],
            studyGuide: "利用『費曼學習法』與『卡片盒筆記』。你的大腦是高頻處理器，透過把概念教給同學，你能瞬間打通邏輯。適合資訊科技、AI演算法、應用數學、精算與策略顧問領域。",
            examMindset: "進考場前深呼吸，停止無謂的預設焦慮！你具備極佳的臨場應變力，相信自己的第一道直覺。"
        },
        taiyang: {
            name: "太陽星",
            element: "丙火（陽火）",
            title: "光明之星 / 中天主星",
            archetype: "☀️ 熱血暖陽：自帶光環的運動隊長與奉獻者",
            desc: "太陽光芒普照，象徵博愛、無私、活力與熱情。具備強烈的正義感與群體號召力，喜歡替大家爭取權益。",
            hsAnalogy: "校園運動場上揮灑汗水的陽光隊長，或者永遠第一個跳出來幫同學搬桌椅、向教官爭取班級權益的熱血青年。他把溫暖給了所有人，但有時會在夜深人靜時獨自消化疲憊。",
            strengths: ["熱情大方，胸襟坦蕩無陰暗面", "極佳的群眾感染力與演說口才", "不畏強權，正義感爆棚", "勇於承擔責任"],
            blindspots: ["過度熱心而忽視自身精疲力竭", "說話直率有時傷人而不自知", "容易打腫臉充胖子，不擅拒絕別人"],
            studyGuide: "適合『群體伴讀』或組成讀書小組（Study Group）。你在教導同學時會被激發出無窮動力，眾人的反饋是你最好的能量來源。推薦傳播媒體、公眾事務、能源工程或外交領域。",
            examMindset: "考試前請先照顧好自己的身體與作息！別在考前一週還在熬夜幫同學抓重點，留點能量給自己衝刺。"
        },
        wuqu: {
            name: "武曲星",
            element: "辛金（陰金）",
            title: "財帛主 / 北斗第六星",
            archetype: "⚔️ 鐵血執行者：高效率刷題王與精算達人",
            desc: "武曲為剛毅之金，掌管財富與執行力。個性果斷、剛直、講求實際回報，不講虛話，行動力極強。",
            hsAnalogy: "書桌永遠收拾得像手術台一樣整潔的硬核學霸。每天精準打卡6小時、刷題不手軟、錯題本分類一絲不苟。他不喜歡無意義的社交聊天，只看重產出與進度條。",
            strengths: ["雷厲風行的執行力，說做就做", "精確的數字感與理財天賦", "堅定不拔，抗壓耐挫力頂尖", "誠實守信，極度可靠"],
            blindspots: ["說話過於耿直生硬，缺乏柔性同理心", "過度重利實用，被認為缺乏文藝浪漫", "對自己和他人過度嚴苛"],
            studyGuide: "利用『番茄鐘工作法』與『錯題量化庫』。你天生對數據敏銳，設立清晰的分數目標與刷題量能讓你迅速進步。適合金融財務、會計、軟體架構、材料科學與軍警檢察體系。",
            examMindset: "剛者易折。大考如果遇到卡關題，先給自己一個彈性跳過它，不要跟題目死磕浪費寶貴時間。"
        },
        tiantong: {
            name: "天同星",
            element: "壬水（陽水）",
            title: "福德星 / 南斗第四星",
            archetype: "🍀 佛系天選：不捲不內耗的人間溫柔團寵",
            desc: "天同為福星，心性天真善良、平易近人，追求心靈的平靜與安逸，具備極強的療癒力與文藝品味。",
            hsAnalogy: "他不是那個每天把頭埋進題海裡的卷王，但他桌上總有好吃的零食、幽默可愛的小吊飾。班級氣氛緊張時，他一句無厘頭的幽默就能化解所有火藥味，天生自帶化險為夷的錦鯉體質。",
            strengths: ["人緣極佳，與世無爭的親和力", "豐富的生活情趣與審美品味", "心態健康，不易產生精神內耗", "極具同理心，天生的傾聽者"],
            blindspots: ["缺乏進取野心，容易陷入惰性擺爛", "意志力較薄弱，遇到強壓力想逃避", "容易隨波逐流，缺乏獨立主見"],
            studyGuide: "適合『微步前進法』。不要訂過於反人性的嚴格計畫，而是把讀書變成有儀式感、愉悅的事情（比如配一杯喜歡的奶茶、用好看的筆記本）。適合心理諮商、設計美學、文化創意、社工幼教。",
            examMindset: "你有福星護體，越是放鬆平常心，臨場發揮越好！千萬別被考場緊張氣氛嚇倒。"
        },
        lianzhen: {
            name: "廉貞星",
            element: "丁火（陰火）",
            title: "次桃花 / 事業星",
            archetype: "🔥 傲骨極客：帶刺的玫瑰與不羈創作者",
            desc: "廉貞為次桃花星，兼具官祿特質。心性高傲、敏銳、富有藝術靈性，對體制常抱有懷疑與顛覆精神。",
            hsAnalogy: "穿校服總有自己獨特穿法、耳機裡放著小眾獨立音樂的酷同學。他不屑於主流的評價體系，只專注於自己真正認同的事情。一旦找到熱愛，他能爆發出驚人的創造力與狂熱專注。",
            strengths: ["極強的敏銳直覺與藝術審美", "不落俗套的創新突破力", "情商與智商兼備，擅長洞悉人性", "對認定的目標極度執著"],
            blindspots: ["性格極端，愛憎過於強烈", "心氣過高容易恃才傲物", "情緒起伏大，受挫時易有叛逆反社會傾向"],
            studyGuide: "依賴『興趣驅動法』。傳統枯燥的灌輸對你無效，你必須找到該學科最底層的美感或應用價值（比如用物理做酷炫特效）。適合程式開發、多媒體影視、法學公辯、藝術設計與前沿科研。",
            examMindset: "收斂心神，把傲氣轉化為卷子上的冷靜殺氣。別因為討厭出題老師的風格而故意放棄作答！"
        },
        tianfu: {
            name: "天府星",
            element: "戊土（陽土）",
            title: "令星庫藏 / 南斗主星",
            archetype: "🏰 靠譜總督：掌控所有資源的總務大掌櫃",
            desc: "天府為南斗主星，被稱為賢能之府。沉穩持重、講求信用、擅長守成與資源調配，行事溫和而有條不紊。",
            hsAnalogy: "班上那個永遠不會丟三落四、所有班級物資與合唱比賽道具都能妥善保管的定海神針。他不喜歡冒進的冒險，但只要把一件事情交給他，大家心裡都有一百個放心。",
            strengths: ["穩健厚重，極具抗風險能力", "優秀的組織協調與資源管理天賦", "為人圓融大器，深得師長信賴", "懂得享受生活且不失原則"],
            blindspots: ["過度求穩保守，缺乏大破大立的衝勁", "偶爾展現出斤斤計較的守財特質", "習慣於舒適圈而不願涉險"],
            studyGuide: "適合『螺旋式複習法』。一步一個腳印構建堅固的基礎題分庫，你可能不是衝刺最快的，但你絕對是最不會漏分失誤的。推薦企管商學、供應鏈管理、公務員、不動產與傳統工科。",
            examMindset: "穩住基本盤，你就已經贏了一大半！把會寫的題目全拿滿分，你的總分就會極度亮眼。"
        },
        taiyin: {
            name: "太陰星",
            element: "癸水（陰水）",
            title: "月華財星 / 中天主星",
            archetype: "🌙 深邃智者：細膩優雅的文藝與幕後推手",
            desc: "太陰為月亮之華，主富、主靜、主陰柔。心思縝密、觀察入微，富有浪漫情懷與超強的文字感受力。",
            hsAnalogy: "坐在窗邊靜靜寫小說、畫插畫，筆記整理得工工整整如同出版物的溫柔同學。他很少在班上高談闊論，但每一次發言都深思熟慮，有著能看穿別人內心脆弱的溫柔觸角。",
            strengths: ["極度敏銳的情感共鳴與洞察力", "優異的文字、藝術與美學天賦", "處事細緻縝密，幾乎不出低級錯誤", "富有包容忍耐力"],
            blindspots: ["多愁善感，容易因小事陷入憂鬱漩渦", "缺乏雷霆萬鈞的魄力，較為被動", "遇到矛盾習慣隱忍冷暴力"],
            studyGuide: "適合『沉浸式番茄學習法』與『視覺化筆記法』。在安靜、整潔、有香氛或輕音樂的環境中，你的記憶力能發揮到極致。適合文學創作、歷史哲學、心理學、財務精算與室內設計。",
            examMindset: "月有陰晴圓缺，心情也有起伏。考試當天如果心慌，默念三遍『凡事已竭盡所能，水到自然渠成』。"
        },
        tanlang: {
            name: "貪狼星",
            element: "癸水/甲木",
            title: "正桃花 / 北斗第一星",
            archetype: "🐺 魅力斜槓：多才多藝的人際磁鐵與外交官",
            desc: "貪狼為慾望與才藝之星。交際手腕高超、多才多藝、精力充沛，對世界充滿強烈的好奇心與探索慾望。",
            hsAnalogy: "全校風雲人物！社聯主席、吉他社主唱、還是校排前幾名。他似乎永遠不需要睡覺，下課在打球，晚上能練團，隔天考試還能拿高分，擁有讓人嫉妒的社交天賦與學習吸收力。",
            strengths: ["頂級的交際手腕與魅力氣場", "學習能力極強，能快速上手任何新技能", "敢於涉足未知，適應力無與倫比", "極佳的商業嗅覺與機會捕捉力"],
            blindspots: ["貪多嚼不爛，興趣廣泛卻難以深耕", "自製力容易被娛樂與慾望瓦解", "偶爾顯得圓滑浮躁，缺乏真誠定性"],
            studyGuide: "『目標遊戲化法』。將讀書目標設計成打怪升級的任務列表，每完成一項給予自己及時獎勵。適合行銷傳播、公關外交、演藝經紀、新媒體運營與風險投資。",
            examMindset: "考前最後衝刺期，請果斷卸載短影音與手遊！專注在一兩個核心主科上，別讓雜念稀釋你的才華。"
        },
        jumen: {
            name: "巨門星",
            element: "癸水（陰水）",
            title: "暗星 / 北斗第二星",
            archetype: "🔍 辯證先鋒：邏輯嚴密、一針見血的辯論社長",
            desc: "巨門為暗星、是非星，亦是口才與研究之星。天生帶有懷疑審視的精神，善於深挖真相與批判性思考。",
            hsAnalogy: "辯論社或模擬聯合國的主將！聽老師講課時，別人都點頭稱是，他總能從邏輯漏洞中舉手提出靈魂拷問。他的眼睛就像 X 光機，能夠看破任何虛偽與破綻，但講話也常因太尖銳而得罪人。",
            strengths: ["無懈可擊的邏輯推理與批判性思維", "卓越的口才表達與言辭思辨能力", "鑽研精神頂尖，打破砂鍋問到底", "具有深厚的學術探究潛力"],
            blindspots: ["生性多疑，難以建立無條件的信任", "言語過於犀利刻薄，容易招惹口舌是非", "內心常有莫名孤獨與被孤立感"],
            studyGuide: "利用『批判性思維學習法』。多去研究定理的推導過程與反例證明，在挑毛病與質疑中，你的大腦會無比興奮。適合法學公辯、新聞調查、學術科研、審計稽核與語言學。",
            examMindset: "少說多做，收斂口舌鋒芒。考前不要跟同學打賭或爭辯題目答案，把精力全部化作筆尖的冷靜答題。"
        },
        tianxiang: {
            name: "天相星",
            element: "壬水（陽水）",
            title: "印星宰輔 / 南斗第五星",
            archetype: "📜 完美協調：風度翩翩、最值得託付的秘書長",
            desc: "天相為掌印之官，代表誠信、服務、體面與調和。行事穩健、重視公理、注重穿著儀表與禮儀教養。",
            hsAnalogy: "每次走進班級都讓人如沐春風的副班長或幹事。作業交得最齊全，版書寫得最端正，老師交代的事情從不漏掉。他像水一樣能適應各種人際容器，是大家最信賴的合作夥伴。",
            strengths: ["極佳的協調溝通與潤滑作用", "重視誠信，為人公道講究體面", "優秀的行政執行力與審美儀態", "樂於助人且不搶風頭"],
            blindspots: ["容易缺乏主見，被環境牽著鼻子走", "有時為了粉飾太平而不敢面對尖銳衝突", "過於在意外在形象與他人評價"],
            studyGuide: "適合『同儕互助回饋法』。在幫助整理小組報告、替同學排疑解惑中鞏固知識。適合公共行政、人力資源、高階公關、品牌公約與司法行政。",
            examMindset: "不要被他人的期待綁架！這場考試是為你自己的未來而考，不是為了討好任何人。"
        },
        tianliang: {
            name: "天梁星",
            element: "戊土（陽土）",
            title: "蔭星壽宿 / 南斗第二星",
            archetype: "🌿 滄桑引路人：閱歷豐富、護佑後輩的老靈魂",
            desc: "天梁為蔭星、清高之星，具有長者風範。心地仁厚、樂善好施、具備極高道德感，常常扮演避風港的角色。",
            hsAnalogy: "班上的『老大哥/大姐大』，明明年紀一樣大，說話談吐卻像經歷過大風大浪的隱士。當同學失戀、成績崩盤時，最喜歡找他傾訴，因為他總能講出幾句富有哲理的寬慰之語。",
            strengths: ["天生具備化凶為吉的庇佑力", "清高自律，具有極強的道德感", "樂於提攜後進，富有長者仁心", "處事公正客觀，具威嚴感"],
            blindspots: ["好為人師，偶爾顯得嘮叨說教", "性格孤高清冷，不容易融入潮流玩鬧", "遇事容易先經歷一番波折後才化解"],
            studyGuide: "適合『通史式縱深學習法』。你對有歷史底蘊、經典理論、醫學生物或古典哲學的學科很有悟性。適合醫學公衛、教育學者、公益慈善、宗教哲學與老牌法學。",
            examMindset: "天梁星天生『遇難呈祥』。即便考卷一開始看起來很難，也千萬別慌，深呼吸後一步步推導，奇蹟往往在最後出現。"
        },
        qisha: {
            name: "七殺星",
            element: "庚金（陽金）",
            title: "將星孤客 / 南斗第六星",
            archetype: "⚡ 孤膽破鋒：一人成軍、直搗黃龍的突擊先鋒",
            desc: "七殺為南斗將星，主肅殺、孤克與決斷。個性剛毅果敢、冒險敢衝、不畏艱險，具有極強的自主獨立性。",
            hsAnalogy: "他往往是一個人背著書包獨來獨往的狠角色。不想融入任何小圈子，但只要一出手（例如大隊接力最後一棒、或者挑戰全校沒人解開的壓軸題），那種捨我其誰的霸氣無人能敵。",
            strengths: ["超凡的膽魄與決斷力，敢冒大險", "極強的單兵作戰與攻堅突破能力", "不怕挫折，越挫越勇的硬漢性格", "不隨波逐流，擁有純粹的自我"],
            blindspots: ["性格剛烈衝動，缺乏耐性容易暴躁", "不善團結協作，顯得孤僻不近人情", "成敗起伏劇烈，容易走極端"],
            studyGuide: "利用『極限攻堅法』。把大考想像成一場你死我活的戰役，設定短平快的魔鬼訓練營，挑戰難題最能激發你的腎上腺素。適合航太工程、急重症醫學、軍事國防、硬體架構與創業開拓。",
            examMindset: "將軍拔劍，非死即生！考場上拿出你的殺氣，遇到難題不要退縮，將所有的專注力聚焦於每一道攻克的難關。"
        },
        pojun: {
            name: "破軍星",
            element: "癸水（陰水）",
            title: "耗星開路 / 北斗第七星",
            archetype: "🌪️ 破壁拓荒：打破舊秩序的顛覆性革命者",
            desc: "破軍為先鋒耗星，象徵破舊立新、顛覆變革與開闢荒原。個性求新求變，不循常規，具有極強的摧毀與重建力。",
            hsAnalogy: "學校規則的挑戰者！他可能會自己動手改造制服、寫個外掛腳本自動填問卷、或者在大家都在死讀書時自己去搞獨立遊戲研發。他不屑於走別人走過的路，永遠在開拓新地圖。",
            strengths: ["超強的創新力與推翻常規的勇氣", "敢於清空重來，具備驚人的重生力", "不畏艱險，是開闢新戰場的最佳拓荒者", "執行革命性想法毫不猶豫"],
            blindspots: ["破壞性過強，往往『先破而後立』代價大", "喜新厭舊，缺乏維護與守成的耐性", "容易與既有權威與傳統發生激烈碰撞"],
            studyGuide: "適合『探究式破構學習法』。拆解公式背後原理，嘗試用不同的非主流解法破題。適合尖端科研、新興領域（區塊鏈、元宇宙、量子運算）、實驗藝術與前鋒創業。",
            examMindset: "破軍求變，但大考的標準答案是客觀的。在規範內把分拿到，考完之後再去盡情顛覆世界！"
        }
    },

    // 十二宮位宇宙地圖
    palaces: [
        { id: "ming", name: "命宮", icon: "🌌", category: "核心命格", modernDesc: "角色卡初始天賦與核心人生觀", hsExplain: "這就是你在這款名為『人生』的開放世界遊戲中，初始隨機骰出來的核心數值。你的核心性格、三觀、抗壓底層邏輯全看這裡。" },
        { id: "xiongdi", name: "兄弟宮", icon: "🤝", category: "社交同儕", modernDesc: "手足情誼與最親密知己關係", hsExplain: "不僅是親兄弟姊妹，也代表班上那些能跟你同穿一條褲子、一起通宵打遊戲、大考前互相抽背單字的最鐵死黨。" },
        { id: "fuqi", name: "夫妻宮", icon: "❤️", category: "情感歸宿", modernDesc: "未來的靈魂伴侶與戀愛互動模式", hsExplain: "你潛意識裡最欣賞的對象類型、以及你在青澀戀愛時會展現出的模樣（是轟轟烈烈的偶像劇，還是細水長流的溫柔陪伴？）。" },
        { id: "zinv", name: "子女宮", icon: "🌱", category: "培育傳承", modernDesc: "晚輩緣分、社團學弟妹引導力與創造力", hsExplain: "在高中指你在社團帶學弟妹的風格（是魔鬼訓練學長，還是溫柔守護天使？），也代表你的原生想像力與產出靈感。" },
        { id: "caibo", name: "財帛宮", icon: "💰", category: "物質資源", modernDesc: "零用錢管理、商業嗅覺與賺錢手段", hsExplain: "你看待金錢與物質的態度。是拿到零用錢秒買球鞋手遊的月光族，還是早早開始研究記帳、甚至倒賣文具卡牌的小商業鬼才？" },
        { id: "jie", name: "疾厄宮", icon: "🩺", category: "身心機能", modernDesc: "身體健康弱點、熬夜耐受度與情緒深層壓力", hsExplain: "你的硬體機能監控器！反映你在大考高壓下哪裡最容易報警（腸胃神經痛？過敏？頭痛偏頭痛？），提醒你如何科學保養。" },
        { id: "qianyi", name: "遷移宮", icon: "✈️", category: "外部環境", modernDesc: "走出家門與校園的適應力、跨界表現", hsExplain: "你去外地參加營隊、未來大學離家讀書、甚至出國留學時的運勢！看你在陌生環境裡是如魚得水，還是水土不服。" },
        { id: "jiaoyou", name: "交友宮", icon: "👥", category: "群體磁場", modernDesc: "班級大眾緣、社群網絡與同儕影響力", hsExplain: "這不是一兩個死黨，而是你在整個班級群體、年級社群裡的群眾形象。你是全校風雲人物，還是靜靜待在邊緣的觀察者？" },
        { id: "guanlu", name: "官祿宮", icon: "📚", category: "學業事業", modernDesc: "高中學業表現、讀書自驅力與選組未來方向", hsExplain: "高中生最核心的宮位！直接關係到你的課業專注度、段考攻堅能力、選填第一/二/三類組以及未來大學志願的契合度。" },
        { id: "tianzhai", name: "田宅宮", icon: "🏡", category: "安全底牌", modernDesc: "家庭氛圍、避風港底蘊與內心安全感來源", hsExplain: "你的避風港與能量充電站。家庭給予你的支持力如何？你的臥室與書桌環境是否能讓你在繁重課業後迅速回血？" },
        { id: "fude", name: "福德宮", icon: "🧘", category: "精神世界", modernDesc: "內心精神世界、焦慮抵抗力與靈魂追求", hsExplain: "你的精神血條與心理韌性！有些人考試就算爆掉也能笑看人生，有些人掉兩分就整晚失眠崩潰，秘密全藏在福德宮。" },
        { id: "fumu", name: "父母宮", icon: "👨‍👩‍👧", category: "長輩權威", modernDesc: "父母關係、老師班導互動與大考考運相處", hsExplain: "你跟師長與體制權威的互動模式。遇到嚴厲的班導你是乖乖配合、靈活迂迴，還是正面硬剛？同時也影響重要的文憑功名運。" }
    ],

    // 四化星解密
    fourTransformations: {
        lu: { name: "化祿", element: "木（春）", icon: "🌱", meaning: "資源湧現・人緣桃花・貴人加持", hsConcept: "如同獲得賽季幸運 Buff！零用錢變多、考試莫名猜中大題、出門常遇到請客的貴人學長姐，心態樂觀豐沛。" },
        quan: { name: "化權", element: "火（夏）", icon: "🔥", meaning: "掌控慾望・競爭進取・強勢突破", hsConcept: "如同開啟狂暴加速形態！爭當社長或隊長、瘋狂刷題衝刺全校第一，誰擋誰被超車，執行力與戰鬥力拉滿。" },
        ke: { name: "化科", element: "金（秋）", icon: "📖", meaning: "文采科甲・名聲榮譽・大考金榜", hsConcept: "專為大考與榮譽而生的光環！作文拿到範文表揚、競賽得獎被貼紅榜、答題邏輯清晰優雅，容易留下良好名聲。" },
        ji: { name: "化忌", element: "水（冬）", icon: "❄️", meaning: "執念牽絆・波折考驗・卡關修煉", hsConcept: "這是命運給你安排的 Boss 關卡！在該宮位你容易焦慮、患得患失、鑽牛角尖。但請記住：化忌是最大的潛力蓄能區，跨過去便是傳奇。" }
    },

    // 經典格局分析
    patterns: [
        {
            name: "殺破狼（七殺・破軍・貪狼）",
            archetype: "🚀 暴風開創流：不走尋常路的冒險王",
            desc: "命宮、官祿宮、財帛宮分別由七殺、破軍、貪狼鎮守。人生注定大開大闔，拒絕一成不變的體制平庸。",
            hsAdvice: "高一高二可能成績起伏如過山車，容易被傳統師長視為『不安定分子』。請不要懷疑自己，找到一兩個專精的硬核領域全力衝刺，你們是將來最具顛覆性成就的弄潮兒。"
        },
        {
            name: "機月同梁（天機・太陰・天同・天梁）",
            archetype: "🛡️ 智慧穩健流：無可替代的幕僚智囊",
            desc: "性格沉穩縝密，富有同理心與邏輯力，善於在既有體制中發揮最大的規劃與協作能量。",
            hsAdvice: "最適合走常規大考升學的高手！只要按部就班複習，基礎題全拿，成績極具穩定性。適合報考頂尖大學的法律、醫學、公法、心理或尖端科研系所。"
        },
        {
            name: "紫府同宮 / 紫府朝垣",
            archetype: "👑 帝相加冕流：天選之子與全能統帥",
            desc: "紫微與天府兩大南北斗主星交相輝映，兼具帝王的氣魄與宰相的穩健，自帶強大號召力。",
            hsAdvice: "天生具備班級領袖氣質。切忌沾沾自喜，若能保持謙遜並結交各路英才，你在高中階段就能打造出令人驚嘆的強大團隊。"
        },
        {
            name: "日麗中天（太陽在午宮坐命）",
            archetype: "☀️ 光明萬丈流：全校聚焦的熱血核心",
            desc: "太陽在正午最明亮之位坐命，光明普照，事業心與奉獻精神如日中天，威震四方。",
            hsAdvice: "不要害怕站上舞台！無論是學生會選舉、演講比賽還是大隊接力，你的能量注定要被大家看見，大膽釋放你的光與熱！"
        }
    ],

    // 排盤核心演算法（西元曆與時辰生成紫微盤）
    calculateChart(birthYear, birthMonth, birthDay, birthHourIndex) {
        // 天干與地支表
        const tianGan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"];
        const diZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];

        // 年干計算
        const yearGanIndex = (birthYear - 4) % 10;
        const yearZhiIndex = (birthYear - 4) % 12;
        const yearGan = tianGan[yearGanIndex >= 0 ? yearGanIndex : yearGanIndex + 10];
        const yearZhi = diZhi[yearZhiIndex >= 0 ? yearZhiIndex : yearZhiIndex + 12];

        // 簡化正統排盤定位：
        // 命宮：寅起正月順數至生月，再逆數至生時
        // 寅的 index 為 2
        const monthNum = parseInt(birthMonth, 10);
        const hourNum = parseInt(birthHourIndex, 10); // 0 = 子(23-1), 1 = 丑(1-3)...
        
        let mingZhiIndex = (2 + (monthNum - 1) - hourNum) % 12;
        if (mingZhiIndex < 0) mingZhiIndex += 12;

        let shenZhiIndex = (2 + (monthNum - 1) + hourNum) % 12;

        // 五行局簡化映射 (根據命宮地支與年干)
        const elementBureaus = ["水二局", "木三局", "金四局", "土五局", "火六局"];
        const bureauIndex = (yearGanIndex + mingZhiIndex) % 5;
        const bureau = elementBureaus[bureauIndex];

        // 排布十二宮順序（以命宮為起點逆時針布十二宮：命、兄、夫、子、財、疾、遷、僕、官、田、福、父）
        const palaceNames = ["命宮", "兄弟宮", "夫妻宮", "子女宮", "財帛宮", "疾厄宮", "遷移宮", "交友宮", "官祿宮", "田宅宮", "福德宮", "父母宮"];
        const palaceIds = ["ming", "xiongdi", "fuqi", "zinv", "caibo", "jie", "qianyi", "jiaoyou", "guanlu", "tianzhai", "fude", "fumu"];
        
        // 14主星配置分配 (基於生日與五行局的定位演算法模型)
        const starKeys = Object.keys(this.stars);
        const chart = [];

        for (let i = 0; i < 12; i++) {
            // 地支位置 (子~亥, 0~11)
            const zhiIdx = i;
            // 命宮算出的宮位偏移
            const offset = (mingZhiIndex - zhiIdx + 12) % 12;
            const pName = palaceNames[offset];
            const pId = palaceIds[offset];

            // 分配星曜
            const assignedStars = [];
            const primaryStarIndex = (birthDay + i * 3 + hourNum * 2) % starKeys.length;
            assignedStars.push(starKeys[primaryStarIndex]);

            // 隨機輔星/雙星情況（約40%機率雙主星同宮）
            if ((birthDay + i) % 3 === 0) {
                const secondaryStarIndex = (primaryStarIndex + 5) % starKeys.length;
                if (secondaryStarIndex !== primaryStarIndex) {
                    assignedStars.push(starKeys[secondaryStarIndex]);
                }
            }

            // 四化星分配
            const fourSihuaGans = {
                "甲": { lu: "lianzhen", quan: "pojun", ke: "wuqu", ji: "taiyang" },
                "乙": { lu: "tianji", quan: "tianliang", ke: "ziwei", ji: "taiyin" },
                "丙": { lu: "tiantong", quan: "tianji", ke: "tianji", ji: "lianzhen" },
                "丁": { lu: "taiyin", quan: "tiantong", ke: "tianji", ji: "jumen" },
                "戊": { lu: "tanlang", quan: "taiyin", ke: "tianfu", ji: "tianji" },
                "己": { lu: "wuqu", quan: "tanlang", ke: "tianliang", ji: "wenqu" },
                "庚": { lu: "taiyang", quan: "wuqu", ke: "taiyin", ji: "tiantong" },
                "辛": { lu: "jumen", quan: "taiyang", ke: "wenqu", ji: "wenchang" },
                "壬": { lu: "tianliang", quan: "ziwei", ke: "tianfu", ji: "wuqu" },
                "癸": { lu: "pojun", quan: "jumen", ke: "taiyin", ji: "tanlang" }
            };

            const curSihua = fourSihuaGans[yearGan] || fourSihuaGans["甲"];
            const sihuaBadges = [];
            assignedStars.forEach(s => {
                if (curSihua.lu === s) sihuaBadges.push("化祿");
                if (curSihua.quan === s) sihuaBadges.push("化權");
                if (curSihua.ke === s) sihuaBadges.push("化科");
                if (curSihua.ji === s) sihuaBadges.push("化忌");
            });

            chart.push({
                zhiIndex: zhiIdx,
                zhiName: diZhi[zhiIdx],
                palaceName: pName,
                palaceId: pId,
                isMing: offset === 0,
                isShen: zhiIdx === shenZhiIndex,
                stars: assignedStars,
                sihua: sihuaBadges
            });
        }

        return {
            yearGan,
            yearZhi,
            bureau,
            mingZhi: diZhi[mingZhiIndex],
            shenZhi: diZhi[shenZhiIndex],
            birthYear,
            birthMonth: monthNum,
            birthDay,
            chart
        };
    },

    // ----------------------------------------------------
    // 流年精算演算法（Annual Fortune）
    // ----------------------------------------------------
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

        // 計算年齡
        const age = chartResult.birthYear ? (targetY - chartResult.birthYear + 1) : 18;

        // 流年命宮地支即為當年地支
        const liunianMingCell = chartResult.chart.find(c => c.zhiName === targetZhi) || chartResult.chart[0];

        // 流年四化表
        const fourSihuaGans = {
            "甲": { lu: "廉貞星", quan: "破軍星", ke: "武曲星", ji: "太陽星", luKey: "lianzhen", quanKey: "pojun", keKey: "wuqu", jiKey: "taiyang" },
            "乙": { lu: "天機星", quan: "天梁星", ke: "紫微星", ji: "太陰星", luKey: "tianji", quanKey: "tianliang", keKey: "ziwei", jiKey: "taiyin" },
            "丙": { lu: "天同星", quan: "天機星", ke: "文昌星", ji: "廉貞星", luKey: "tiantong", quanKey: "tianji", keKey: "wenchang", jiKey: "lianzhen" },
            "丁": { lu: "太陰星", quan: "天同星", ke: "天機星", ji: "巨門星", luKey: "taiyin", quanKey: "tiantong", keKey: "tianji", jiKey: "jumen" },
            "戊": { lu: "貪狼星", quan: "太陰星", ke: "右弼星", ji: "天機星", luKey: "tanlang", quanKey: "taiyin", keKey: "tianfu", jiKey: "tianji" },
            "己": { lu: "武曲星", quan: "貪狼星", ke: "天梁星", ji: "文曲星", luKey: "wuqu", quanKey: "tanlang", keKey: "tianliang", jiKey: "wenqu" },
            "庚": { lu: "太陽星", quan: "武曲星", ke: "太陰星", ji: "天同星", luKey: "taiyang", quanKey: "wuqu", keKey: "taiyin", jiKey: "tiantong" },
            "辛": { lu: "巨門星", quan: "太陽星", ke: "文曲星", ji: "文昌星", luKey: "jumen", quanKey: "taiyang", keKey: "wenqu", jiKey: "wenchang" },
            "壬": { lu: "天梁星", quan: "紫微星", ke: "左輔星", ji: "武曲星", luKey: "tianliang", quanKey: "ziwei", keKey: "tianfu", jiKey: "wuqu" },
            "癸": { lu: "破軍星", quan: "巨門星", ke: "太陰星", ji: "貪狼星", luKey: "pojun", quanKey: "jumen", keKey: "taiyin", jiKey: "tanlang" }
        };

        const curSihua = fourSihuaGans[targetGan] || fourSihuaGans["丙"];

        // 尋找流年四化落入命盤的哪個宮位
        const findPalaceOfStar = (starKey) => {
            const cell = chartResult.chart.find(c => c.stars.includes(starKey));
            return cell ? cell.palaceName : "本命宮";
        };

        const luPalace = findPalaceOfStar(curSihua.luKey);
        const quanPalace = findPalaceOfStar(curSihua.quanKey);
        const kePalace = findPalaceOfStar(curSihua.keKey);
        const jiPalace = findPalaceOfStar(curSihua.jiKey);

        // 綜合運勢分數演算（基準 75 + 流年和諧度加權）
        const yearOffset = (targetY - 2026) % 5;
        const fortuneScore = Math.min(98, Math.max(68, 80 + (targetY % 7) * 2 - (age % 3) * 3));

        // 深度高中白話四維度指引
        const guides = {
            study: `【學業大考運】${targetYear} 年流年【${curSihua.ke}化科】飛星牽動，名聲文運受到催化！大考衝刺專注力進入高效期，容易在模擬考中突破以往卡關的瓶頸題。建議加強整理錯題本，對於公式推導要溯源根本，考場上能發揮超常冷靜。`,
            social: `【同儕與貴人運】流年【${curSihua.lu}化祿】入【${luPalace}】，同儕人際磁場溫和如春風。在班級與社團裡容易遇到願意主動分享筆記的學霸好友，師長也對你青睞有加。主動請益會有意想不到的收穫。`,
            health: `【身心與作息防護】流年【${curSihua.ji}化忌】坐於【${jiPalace}】，提醒此年需特別防範「神經性疲倦」與換季感冒。大考高壓下切莫長時間通宵刷題，保證大腦前額葉血供，中午務必小憩 20 分鐘。`,
            mindset: `【高中生年度心法】今年是『${curSihua.quan}化權』主導的執行力之年！別把精力浪費在虛無的焦慮上，為自己訂下清晰的倒數打卡計畫，『行則將至，做則必成』！`
        };

        return {
            targetYear: targetY,
            targetGan,
            targetZhi,
            zodiac,
            age,
            fortuneScore,
            liunianMingPalace: liunianMingCell.palaceName,
            liunianMingZhi: targetZhi,
            sihua: {
                lu: { star: curSihua.lu, palace: luPalace, meaning: "機遇與資源" },
                quan: { star: curSihua.quan, palace: quanPalace, meaning: "掌控與突破" },
                ke: { star: curSihua.ke, palace: kePalace, meaning: "名譽與考運" },
                ji: { star: curSihua.ji, palace: jiPalace, meaning: "考驗與修煉" }
            },
            guides
        };
    },

    // ----------------------------------------------------
    // 未來十年運勢動態圖譜（10-Year Decadal Roadmap）
    // ----------------------------------------------------
    calculateDecadeFortune(chartResult, startYear = 2026, count = 10) {
        const decadeData = [];
        const themeLibrary = [
            { title: "潛龍蓄勢・地基築牢", keyword: "積澱期", desc: "如同大樹深扎根基。不急於一時的高光，專注於各科基礎知識的查漏補缺。" },
            { title: "厚積薄發・大考突圍", keyword: "衝刺期", desc: "考場亮劍之年！多年的刷題與沉澱迎來質變，臨場定力十足，迎向金榜題名。" },
            { title: "大學初啼・視野拓寬", keyword: "探索期", desc: "告別高中題海，踏入高等學府殿堂。專業科目與跨領域涉獵讓你眼界大開。" },
            { title: "羽翼漸豐・社群開拓", keyword: "成長期", desc: "人脈圈大幅躍升，參與高品質社團、專案競賽與產學研究，發現自己的真正熱愛。" },
            { title: "專業深耕・技能破局", keyword: "淬鍊期", desc: "主修專業走向深水區，開始累積獨當一面的硬實力，大考考研或專案斬獲殊榮。" },
            { title: "風雲際會・實習展翼", keyword: "出發期", desc: "走出象牙塔接觸業界真實生態，實戰能力顯著飆升，深得主管與團隊信賴。" },
            { title: "天道酬勤・獨立成峰", keyword: "立業期", desc: "自我人生座標愈加清晰，無論是升學深造還是初入職場，都展現出強大統率力。" },
            { title: "登高望遠・蓄勢再升", keyword: "整合期", desc: "資源與人脈進入正向複利循環，學會宏觀佈局，開始主導重要方向。" },
            { title: "知行合一・收穫豐盈", keyword: "收穫期", desc: "早年所有的堅持與自律在此年結出甜美果實，身心達到成熟充實的平衡。" },
            { title: "開闢新境・長青基業", keyword: "新生期", desc: "十年一週期圓滿完成，人生踏入下一個更高維度的嶄新里程碑！" }
        ];

        for (let i = 0; i < count; i++) {
            const currentYear = startYear + i;
            const liunian = this.calculateLiunian(chartResult, currentYear);
            const theme = themeLibrary[i % themeLibrary.length];

            // 針對年齡階段制定高中/大學升學里程碑標籤
            let stageBadge = "";
            if (liunian.age <= 18) {
                stageBadge = "🏫 高中衝刺階段";
            } else if (liunian.age <= 22) {
                stageBadge = "🎓 大學本科深造";
            } else {
                stageBadge = "🚀 碩班研究 / 初入職場";
            }

            decadeData.push({
                year: currentYear,
                ganZhi: `${liunian.targetGan}${liunian.targetZhi}`,
                zodiac: liunian.zodiac,
                age: liunian.age,
                stageBadge,
                score: liunian.fortuneScore,
                theme: theme.title,
                keyword: theme.keyword,
                desc: theme.desc,
                sihuaOverview: `祿在${liunian.sihua.lu.palace} ｜ 權在${liunian.sihua.quan.palace} ｜ 科在${liunian.sihua.ke.palace} ｜ 忌在${liunian.sihua.ji.palace}`,
                studyAdvice: liunian.guides.study,
                actionTip: liunian.guides.mindset
            });
        }

        return decadeData;
    }
};

window.ZiWeiSystem = ZiWeiSystem;

