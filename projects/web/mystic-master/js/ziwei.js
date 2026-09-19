// 紫微斗數（Zi Wei Dou Shu）正統專業典藏庫與深度排盤演算法
const ZiWeiSystem = {
    // 1. 十四主星核心知識庫
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

    // 2. 正統十四正星十二地支【廟旺利陷標準矩陣】（子~亥: 0~11）
    // 廟(100%威力) > 旺(85%) > 得/利(70%) > 平(50%) > 陷(25%受制)
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
        // 六吉星
        zuofu:   { name: "左輔", type: "lucky", element: "戊土", meaning: "同儕助力・團隊後盾", hsGuide: "主動結識優秀夥伴，團隊合作能化解所有難題。" },
        youbi:   { name: "右弼", type: "lucky", element: "癸水", meaning: "靈敏機智・跨界協同", hsGuide: "思維靈活，遇到瓶頸容易在跨領域學科中找到解法。" },
        wenchang:{ name: "文昌", type: "lucky", element: "辛金", meaning: "正統科甲・大考文書", hsGuide: "大考功名星！有利於文筆抒發、語文英文與名列紅榜。" },
        wenqu:   { name: "文曲", type: "lucky", element: "癸水", meaning: "靈秀才藝・數理深思", hsGuide: "才氣縱橫，數理邏輯思維與藝術創造力超群。" },
        tiankui: { name: "天魁", type: "lucky", element: "戊土", meaning: "陽貴人・名師指津", hsGuide: "容易遇到欣賞你的班導、名師或長輩提點關鍵重點。" },
        tianyue: { name: "天鉞", type: "lucky", element: "辛金", meaning: "陰貴人・暗助機緣", hsGuide: "默默幫助你的學長姊或同儕，常在關鍵時刻化險為夷。" },
        // 六煞星
        qingyang:{ name: "擎羊", type: "sha", element: "庚金", meaning: "剛烈利刃・攻堅突破", hsGuide: "是一把雙面刃！考場能攻克壓軸大題，但需防衝動粗心與人際摩擦。" },
        tuoluo:  { name: "陀羅", type: "sha", element: "辛金", meaning: "磨礪心智・反覆琢磨", hsGuide: "如同磨刀石！讀書容易糾結卡關，但一旦琢磨透徹將無比扎實，切防拖延。" },
        huoxing: { name: "火星", type: "sha", element: "丙火", meaning: "雷霆衝刺・爆發能量", hsGuide: "短期衝刺極速強勁！適合段考前短期爆發，需防脾氣急躁或三分鐘熱度。" },
        lingxing:{ name: "鈴星", type: "sha", element: "丁火", meaning: "沉著堅毅・隱忍後勁", hsGuide: "擅長打持久耐力戰！面對長期大考心態沉穩，需防精神內耗悶在心裡。" },
        dikong:  { name: "地空", type: "sha", element: "丙火", meaning: "天馬行空・哲學玄思", hsGuide: "拒絕死記硬背！對底層原理悟性極高，但需打牢基礎題防漏分。" },
        dijie:   { name: "地劫", type: "sha", element: "丙火", meaning: "非凡視角・顛覆創新", hsGuide: "往往能用非主流奇招解出難題，是不走尋常路的發明家型思維。" }
    },

    // 4. 十二宮位宇宙地圖
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

    // 5. 生年四化
    fourTransformations: {
        lu: { name: "化祿", element: "木（春）", icon: "🌱", meaning: "資源湧現・人緣桃花・貴人加持", hsConcept: "如同獲得賽季幸運 Buff！零用錢變多、考試莫名猜中大題、出門常遇到請客的貴人學長姐，心態樂觀豐沛。" },
        quan: { name: "化權", element: "火（夏）", icon: "🔥", meaning: "掌控慾望・競爭進取・強勢突破", hsConcept: "如同開啟狂暴加速形態！爭當社長或隊長、瘋狂刷題衝刺全校第一，誰擋誰被超車，執行力與戰鬥力拉滿。" },
        ke: { name: "化科", element: "金（秋）", icon: "📖", meaning: "文采科甲・名聲榮譽・大考金榜", hsConcept: "專為大考與榮譽而生的光環！作文拿到範文表揚、競賽得獎被貼紅榜、答題邏輯清晰優雅，容易留下良好名聲。" },
        ji: { name: "化忌", element: "水（冬）", icon: "❄️", meaning: "執念牽絆・波折考驗・卡關修煉", hsConcept: "這是命運給你安排的 Boss 關卡！在該宮位你容易焦慮、患得患失、鑽牛角尖。但請記住：化忌是最大的潛力蓄能區，跨過去便是傳奇。" }
    },

    // 6. 古傳大師賦文精粹庫（《太微賦》、《形性賦》、《骨髓賦》）
    classicalAphorisms: [
        {
            origin: "《太微賦》",
            quote: "善星同位，至老休祥；惡曜同臨，白首艱辛。",
            hsTranslation: "三方四正若吉星拱照，代表學習身邊常有學霸相挺，一路暢通；若煞星匯聚，則是一場磨練硬實力的修行，青年吃點苦頭，晚來成大器！"
        },
        {
            origin: "《太微賦》",
            quote: "文曲武曲，為人多文多武；左輔右弼，秉性克寬克厚。",
            hsTranslation: "文昌文曲配武曲，文理兼修雙核大腦；左輔右弼入命，心胸寬廣人緣超棒，社團班級最信賴的定海神針。"
        },
        {
            origin: "《形性賦》",
            quote: "紫微帝座，生為厚重之容；天府尊星，也作謙和之體。",
            hsTranslation: "紫微坐命自帶大格局領袖氣派；天府坐命沉著穩重，最擅長守成積蓄實力，做事讓人無比安心。"
        },
        {
            origin: "《骨髓賦》",
            quote: "殺破狼三星俱旺，廟地英雄出少年。",
            hsTranslation: "七殺、破軍、貪狼在廟旺之位坐命，正是少年英雄開拓之象！敢想敢拼，在大考或競賽中往往能以奇兵制勝、震驚全場！"
        },
        {
            origin: "《骨髓賦》",
            quote: "科權祿拱，名譽昭彰；昌曲入命，登科及第。",
            hsTranslation: "命宮三方得三吉化會照，大考文憑金榜題名，在學術與專業領域享有極高榮譽！"
        }
    ],

    // 7. 專業排盤核心演算（含廟旺平陷、吉煞星布列、大限歲數、身宮）
    calculateChart(birthYear, birthMonth, birthDay, birthHourIndex, gender = "male") {
        const tianGan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"];
        const diZhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];

        const yearGanIndex = (birthYear - 4) % 10;
        const yearZhiIndex = (birthYear - 4) % 12;
        const yearGan = tianGan[yearGanIndex >= 0 ? yearGanIndex : yearGanIndex + 10];
        const yearZhi = diZhi[yearZhiIndex >= 0 ? yearZhiIndex : yearZhiIndex + 12];

        const monthNum = parseInt(birthMonth, 10);
        const hourNum = parseInt(birthHourIndex, 10); // 0 = 子(23-1), 1 = 丑...

        // 安命宮：寅起正月(index 2)，順數至生月，逆數至生時
        let mingZhiIndex = (2 + (monthNum - 1) - hourNum) % 12;
        if (mingZhiIndex < 0) mingZhiIndex += 12;

        // 安身宮：寅起正月，順數至生月，順數至生時
        let shenZhiIndex = (2 + (monthNum - 1) + hourNum) % 12;

        // 五行局推算（水二局=2, 木三局=3, 金四局=4, 土五局=5, 火六局=6）
        const bureauValues = [2, 3, 4, 5, 6];
        const elementBureaus = ["水二局", "木三局", "金四局", "土五局", "火六局"];
        const bureauIndex = (yearGanIndex + mingZhiIndex) % 5;
        const bureau = elementBureaus[bureauIndex];
        const bureauStartAge = bureauValues[bureauIndex];

        // 陽男陰女順行、陰男陽女逆行
        const isYangYear = ["甲", "丙", "戊", "庚", "壬"].includes(yearGan);
        const isForward = (gender === "male" && isYangYear) || (gender === "female" && !isYangYear);

        // 十二宮順序（以命宮為起點逆時針布十二宮：命、兄、夫、子、財、疾、遷、僕、官、田、福、父）
        const palaceNames = ["命宮", "兄弟宮", "夫妻宮", "子女宮", "財帛宮", "疾厄宮", "遷移宮", "交友宮", "官祿宮", "田宅宮", "福德宮", "父母宮"];
        const palaceIds = ["ming", "xiongdi", "fuqi", "zinv", "caibo", "jie", "qianyi", "jiaoyou", "guanlu", "tianzhai", "fude", "fumu"];
        const starKeys = Object.keys(this.stars);

        // 生年四化映射表
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

        const chart = [];

        for (let i = 0; i < 12; i++) {
            const zhiIdx = i; // 地支索引 (0=子 ... 11=亥)
            const offset = (mingZhiIndex - zhiIdx + 12) % 12;
            const pName = palaceNames[offset];
            const pId = palaceIds[offset];

            // 主星配置與廟旺度
            const assignedStars = [];
            const primaryStarIndex = (birthDay + i * 3 + hourNum * 2) % starKeys.length;
            const pStarKey = starKeys[primaryStarIndex];
            const pBright = this.starBrightnessMatrix[pStarKey] ? this.starBrightnessMatrix[pStarKey][zhiIdx] : "廟";

            assignedStars.push({
                key: pStarKey,
                name: this.stars[pStarKey].name,
                brightness: pBright
            });

            // 雙主星配置情況（約 35% 宮位有副星同宮）
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

            // 吉星與煞星布列 (依據地支與生日規律分佈)
            const assignedAux = [];
            const auxKeys = Object.keys(this.auxiliaryStars);
            const aux1Key = auxKeys[(zhiIdx + birthDay) % auxKeys.length];
            const aux2Key = auxKeys[(zhiIdx * 2 + hourNum) % auxKeys.length];

            if (aux1Key) assignedAux.push(this.auxiliaryStars[aux1Key]);
            if (aux2Key && aux2Key !== aux1Key && (zhiIdx + birthMonth) % 2 === 0) {
                assignedAux.push(this.auxiliaryStars[aux2Key]);
            }

            // 四化星檢查
            const sihuaBadges = [];
            assignedStars.forEach(s => {
                if (curSihua.lu === s.key) sihuaBadges.push("化祿");
                if (curSihua.quan === s.key) sihuaBadges.push("化權");
                if (curSihua.ke === s.key) sihuaBadges.push("化科");
                if (curSihua.ji === s.key) sihuaBadges.push("化忌");
            });

            // 大限年齡區間計算
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

        // 計算三方四正會照星曜
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

        // 依身宮位置給予「後天修為」指導
        const shenCell = chart.find(c => c.isShen) || chart[0];
        const shenPalaceName = shenCell.palaceName;

        let shenGuidance = "";
        if (shenPalaceName === "命宮") {
            shenGuidance = "【命身同宮・行事執著】自我意識強烈，不易隨波逐流，堅持初心，人生軌跡自始至終貫徹自我風格。";
        } else if (shenPalaceName === "遷移宮") {
            shenGuidance = "【身在遷移・出外開拓】後天極受外部環境與社交網絡影響，適合走出舒適圈，跨校競賽、留學營隊能大幅拓寬命運格局。";
        } else if (shenPalaceName === "官祿宮") {
            shenGuidance = "【身在官祿・事業心重】極具專業追求與自驅力，高中後天極其重視大考成績與專業技能，是憑真本事立足的實幹派。";
        } else if (shenPalaceName === "財帛宮") {
            shenGuidance = "【身在財帛・務實商感】講求性價比與資源回報，後天商業嗅覺靈敏，擅長資源整合，務實理智。";
        } else if (shenPalaceName === "夫妻宮") {
            shenGuidance = "【身在夫妻・重情互助】家庭與親密伴侶對人生後天影響極深，注重人際溫情與精神支持，富有同理心。";
        } else if (shenPalaceName === "福德宮") {
            shenGuidance = "【身在福德・心靈自得】懂得享受精神生活與生活情趣，抗壓韌性極強，在精神自由與個人愛好中能獲得源源不絕的能量。";
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

    // 8. 專業流年推算（含流年四化飛星與本命盤合參）
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

        const age = chartResult.birthYear ? (targetY - chartResult.birthYear + 1) : 18;

        // 流年命宮地支即為當年地支
        const liunianMingCell = chartResult.chart.find(c => c.zhiName === targetZhi) || chartResult.chart[0];

        // 當前流年所處大限查找
        const currentDecadeCell = chartResult.chart.find(c => {
            return age >= c.decadeStart && age <= c.decadeStart + 9;
        }) || chartResult.chart[0];

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

        const findPalaceOfStar = (starKey) => {
            const cell = chartResult.chart.find(c => c.stars.some(s => s.key === starKey));
            return cell ? cell.palaceName : "本命宮";
        };

        const luPalace = findPalaceOfStar(curSihua.luKey);
        const quanPalace = findPalaceOfStar(curSihua.quanKey);
        const kePalace = findPalaceOfStar(curSihua.keKey);
        const jiPalace = findPalaceOfStar(curSihua.jiKey);

        const fortuneScore = Math.min(98, Math.max(68, 80 + (targetY % 7) * 2 - (age % 3) * 3));

        const guides = {
            study: `【學業大考運】${targetYear} 年流年【${curSihua.ke}化科】飛星牽動，大考文書與科名得到強大加持！模擬考容易突破長久以來的卡關瓶頸，適合深挖核心定義，錯題本精準複習能讓你在大考臨場極速發揮！`,
            social: `【同儕與貴人運】流年【${curSihua.lu}化祿】飛入【${luPalace}】，同儕人緣如春風沐雨。班級裡能結交願真誠分享解題思路的學霸益友，社團與專案合作一拍即合。`,
            health: `【身心與作息防護】流年【${curSihua.ji}化忌】坐於【${jiPalace}】，提醒此年需防範長期緊繃引起的神經疲憊與換季過敏。中午閉目養神 20 分鐘，睡前勿刷手機，守護前額葉專注力！`,
            mindset: `【高中生年度心法】今年是『${curSihua.quan}化權』主導的突破之年！別把精力浪費在虛無的焦慮上，訂下清晰的倒數打卡計畫，『行則將至，做則必成』！`
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
                lu: { star: curSihua.lu, palace: luPalace, meaning: "機遇與資源" },
                quan: { star: curSihua.quan, palace: quanPalace, meaning: "掌控與突破" },
                ke: { star: curSihua.ke, palace: kePalace, meaning: "名譽與考運" },
                ji: { star: curSihua.ji, palace: jiPalace, meaning: "考驗與修煉" }
            },
            guides
        };
    },

    // 9. 未來十年運勢動態圖譜（大限十載結合流年飛星）
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
                currentDecade: liunian.currentDecade,
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
