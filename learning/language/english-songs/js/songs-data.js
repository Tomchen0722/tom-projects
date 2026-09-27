/**
 * 英文歌學習英語 - 預載歌曲資料庫 (Songs Database)
 * 包含：精準時間戳記 (LRC)、原文歌詞、繁體中文翻譯、重點單字、片語語法解析
 */

const SONGS_DATA = [
  {
    id: "count-on-me",
    title: "Count On Me",
    artist: "Bruno Mars",
    genre: "Pop / Acoustic",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "🎵",
    color: "linear-gradient(135deg, #f59e0b, #d97706)",
    audioNotes: "純淨吉他彈唱與流行旋律，歌詞發音極其清晰，包含大量情態助詞、條件句與友情片語。",
    // 音符配置 (用於內建 Web Audio 播放高品質原創吉他/鋼琴和弦伴奏)
    synthPattern: "acoustic-guitar-ballad",
    bpm: 88,
    grammarFocus: [
      { rule: "Conditional Sentences (條件句)", example: "If you ever find yourself stuck in the middle of the sea, I'll sail the world to find you." },
      { rule: "Phrasal Verbs (動詞片語)", example: "Count on (依靠、指望), Find out (查明、發現), Remind of (提醒)" },
      { rule: "Time Clauses (時間副詞子句)", example: "When you are tossed in darkness, I'll be the light to guide you." }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 5.5,
        en: "If you ever find yourself stuck in the middle of the sea",
        zh: "如果你發現自己被困在汪洋大海之中",
        phonetic: "ɪf juː ˈɛvər faɪnd jʊərˈsɛlf stʌk ɪn ðə ˈmɪdəl əv ðə siː",
        notes: "【重點】stuck (困住，stick 的過去分詞)；in the middle of (在...中間/當中)",
        keyWords: ["stuck", "middle", "sea"]
      },
      {
        start: 5.5,
        end: 10.2,
        en: "I'll sail the world to find you",
        zh: "我會揚帆航遍全世界找到你",
        phonetic: "aɪl seɪl ðə wɜːrld tuː faɪnd juː",
        notes: "【語法】I'll = I will (表達承諾與決心)；sail the world (航行環遊世界)",
        keyWords: ["sail", "world", "find"]
      },
      {
        start: 10.2,
        end: 15.6,
        en: "If you ever find yourself lost in the dark and you can't see",
        zh: "如果你發現自己迷失在黑暗中，伸手不見五指",
        phonetic: "ɪf juː ˈɛvər faɪnd jʊərˈsɛlf lɔːst ɪn ðə dɑːrk ænd juː kænt siː",
        notes: "【連音】and you 常弱化讀作 /ən juː/；lost in the dark (在黑暗中迷失)",
        keyWords: ["lost", "dark"]
      },
      {
        start: 15.6,
        end: 20.8,
        en: "I'll be the light to guide you",
        zh: "我會成為引導你的那道光芒",
        phonetic: "aɪl biː ðə laɪt tuː ɡaɪd juː",
        notes: "【重點】guide (動詞：指引、導引；名詞：導遊、指南)",
        keyWords: ["light", "guide"]
      },
      {
        start: 20.8,
        end: 26.2,
        en: "We find out what we're made of",
        zh: "我們終於明白自己有多堅強、由什麼特質鑄成",
        phonetic: "wiː faɪnd aʊt wʌt wɪr meɪd ʌv",
        notes: "【片語】find out (搞清楚、發現)；be made of (由...組成，這裡引申為人的品格骨氣)",
        keyWords: ["find out", "made of"]
      },
      {
        start: 26.2,
        end: 31.8,
        en: "When we are called to help our friends in need",
        zh: "當我們被召喚去幫助身處患難的朋友時",
        phonetic: "wɛn wiː ɑːr kɔːld tuː hɛlp ˈaʊər frɛndz ɪn niːd",
        notes: "【名句】friends in need 來自名言 'A friend in need is a friend indeed' (患難見真情)",
        keyWords: ["called", "friends", "in need"]
      },
      {
        start: 31.8,
        end: 37.0,
        en: "You can count on me like one, two, three",
        zh: "你可以像數一、二、三一樣依靠我",
        phonetic: "juː kæn kaʊnt ɒn miː laɪk wʌn tuː θriː",
        notes: "【核心片語】count on someone (依賴/信任某人)；like one, two, three (比喻輕而易舉、隨傳隨到)",
        keyWords: ["count on", "one", "two", "three"]
      },
      {
        start: 37.0,
        end: 41.5,
        en: "I'll be there",
        zh: "我立刻就會趕到你身邊",
        phonetic: "aɪl biː ðɛər",
        notes: "【口語】I'll be there (我會在那裡/支持你/在身旁守護)",
        keyWords: ["there"]
      },
      {
        start: 41.5,
        end: 47.0,
        en: "And I know when I need it, I can count on you like four, three, two",
        zh: "我也深知當我需要時，也能如倒數四、三、二般依賴你",
        phonetic: "ænd aɪ noʊ wɛn aɪ niːd ɪt, aɪ kæn kaʊnt ɒn juː laɪk fɔːr θriː tuː",
        notes: "【連音】need it 讀作 /niː dɪt/",
        keyWords: ["need", "count on"]
      },
      {
        start: 47.0,
        end: 51.5,
        en: "And you'll be there",
        zh: "而你也一定會在我身邊",
        phonetic: "ænd juːl biː ðɛər",
        notes: "【縮寫】you'll = you will",
        keyWords: ["there"]
      },
      {
        start: 51.5,
        end: 56.5,
        en: "'Cause that's what friends are supposed to do, oh yeah",
        zh: "因為這正是身為好朋友所應該做的，沒錯",
        phonetic: "kəz ðæts wʌt frɛndz ɑːr səˈpoʊzd tuː duː, oʊ jɛə",
        notes: "【重點句型】be supposed to (應當、本該)；'Cause = Because (口語縮讀)",
        keyWords: ["supposed to", "friends"]
      },
      {
        start: 56.5,
        end: 62.0,
        en: "Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh, yeah, yeah",
        zh: "噢～噢～噢～噢～ 耶～",
        phonetic: "uː uː uː uː, jɛə jɛə",
        notes: "【哼唱段落】放鬆心情跟隨節奏哼唱，感受發聲共鳴",
        keyWords: []
      },
      {
        start: 62.0,
        end: 67.5,
        en: "If you toss and you turn and you just can't fall asleep",
        zh: "如果你輾轉難眠，怎麼翻來覆去都睡不著",
        phonetic: "ɪf juː tɒs ænd juː tɜːrn ænd juː ʤʌst kænt fɔːl əˈsliːp",
        notes: "【生活片語】toss and turn (輾轉難眠、翻來覆去)；fall asleep (入睡)",
        keyWords: ["toss", "turn", "asleep"]
      },
      {
        start: 67.5,
        end: 72.8,
        en: "I'll sing a song beside you",
        zh: "我會在你的身旁為你唱一首歌",
        phonetic: "aɪl sɪŋ ə sɔːŋ bɪˈsaɪd juː",
        notes: "【介系詞】beside (在...旁邊；注意不要跟 besides「而且/此外」搞混)",
        keyWords: ["sing", "beside"]
      },
      {
        start: 72.8,
        end: 78.5,
        en: "And if you ever forget how much you really mean to me",
        zh: "如果你哪天忘記了，你對我而言有多麼無可取代",
        phonetic: "ænd ɪf juː ˈɛvər fərˈɡɛt haʊ mʌʧ juː ˈrɪəli miːn tuː miː",
        notes: "【必背句型】mean something to someone (對某人有深遠意義/重要性)",
        keyWords: ["forget", "really", "mean"]
      },
      {
        start: 78.5,
        end: 84.0,
        en: "Every day I will remind you",
        zh: "每一天，我都一定會提醒你",
        phonetic: "ˈɛvri deɪ aɪ wɪl rɪˈmaɪnd juː",
        notes: "【重點動詞】remind (提醒)；remind someone of something (使某人想起某事)",
        keyWords: ["remind", "every day"]
      },
      {
        start: 84.0,
        end: 90.0,
        en: "You'll always have my shoulder when you cry",
        zh: "當你哭泣時，我的肩膀永遠為你依靠",
        phonetic: "juːl ˈɔːlweɪz hæv maɪ ˈʃoʊldər wɛn juː kraɪ",
        notes: "【美語慣用語】a shoulder to cry on (可以哭訴依靠的肩膀/傾聽者)",
        keyWords: ["shoulder", "cry", "always"]
      },
      {
        start: 90.0,
        end: 96.0,
        en: "I'll never let go, never say goodbye",
        zh: "我絕不放手，也絕不道別離去",
        phonetic: "aɪl ˈnɛvər lɛt ɡoʊ, ˈnɛvər seɪ ˌɡʊdˈbaɪ",
        notes: "【片語】let go (放手、釋懷)；say goodbye (道別)",
        keyWords: ["never", "let go", "goodbye"]
      },
      {
        start: 96.0,
        end: 102.0,
        en: "You can count on me like one, two, three, I'll be there",
        zh: "你可以隨時依靠我，如數一二三般我即刻就到",
        phonetic: "juː kæn kaʊnt ɒn miː laɪk wʌn tuː θriː, aɪl biː ðɛər",
        notes: "【副歌複習】加深印象，練習用自然語速流利跟讀",
        keyWords: ["count on"]
      }
    ]
  },
  {
    id: "a-whole-new-world",
    title: "A Whole New World",
    artist: "Aladdin Soundtrack",
    genre: "Disney Classic / Musical",
    level: "中級 (B1-B2)",
    cover: "✨",
    color: "linear-gradient(135deg, #6366f1, #8b5cf6)",
    audioNotes: "迪士尼經典男女對唱，詞彙華麗且富含比喻修辭，是學習高雅形容詞與感官動詞的極品教材。",
    synthPattern: "disney-orchestral-ballad",
    bpm: 76,
    grammarFocus: [
      { rule: "Sensory & Perception Verbs (感官動詞)", example: "I can show you the world, Tell me when did you last let your heart decide." },
      { rule: "Inverted & Poetic Sentences (詩意倒裝與修辭)", example: "A whole new world, A new fantastic point of view." }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 6.2,
        en: "I can show you the world, shining, shimmering, splendid",
        zh: "我能為你展現整個世界：閃耀奪目、波光粼粼、燦爛壯麗",
        phonetic: "aɪ kæn ʃoʊ juː ðə wɜːrld, ˈʃaɪnɪŋ, ˈʃɪmərɪŋ, ˈsplɛndɪd",
        notes: "【頭韻修辭】shining (閃耀), shimmering (微光閃爍), splendid (極為華麗壯觀) 形成華美押韻",
        keyWords: ["shining", "shimmering", "splendid"]
      },
      {
        start: 6.2,
        end: 12.8,
        en: "Tell me, princess, now when did you last let your heart decide?",
        zh: "告訴我，公主，你上一次聽從自己心聲做決定是什麼時候？",
        phonetic: "tɛl miː, ˈprɪnsɛs, naʊ wɛn dɪd juː læst lɛt jʊər hɑːrt dɪˈsaɪd",
        notes: "【使役動詞】let + 受詞 + 原形動詞 (let your heart decide)",
        keyWords: ["princess", "heart", "decide"]
      },
      {
        start: 12.8,
        end: 18.5,
        en: "I can open your eyes, take you wonder by wonder",
        zh: "我能為你開啟全新視野，帶你閱覽一個又一個不可思議的奇蹟",
        phonetic: "aɪ kæn ˈoʊpən jʊər aɪz, teɪk juː ˈwʌndər baɪ ˈwʌndər",
        notes: "【片語】wonder by wonder (一處又一處的奇觀奇蹟)",
        keyWords: ["open", "wonder"]
      },
      {
        start: 18.5,
        end: 25.0,
        en: "Over, sideways and under on a magic carpet ride",
        zh: "乘著魔毯翱翔，穿越高空、側身盤旋、俯衝低掠",
        phonetic: "ˈoʊvər, ˈsaɪdweɪz ænd ˈʌndər ɒn ə ˈmæʤɪk ˈkɑːrpɪt raɪd",
        notes: "【空間副詞】over (越過), sideways (橫向/側邊), under (下方)",
        keyWords: ["sideways", "magic", "carpet"]
      },
      {
        start: 25.0,
        end: 30.5,
        en: "A whole new world, a new fantastic point of view",
        zh: "一個嶄新的世界，一種令人驚嘆的全新視角與天地",
        phonetic: "ə hoʊl nuː wɜːrld, ə nuː fænˈtæstɪk pɔɪnt əv vjuː",
        notes: "【片語】point of view (觀點、視角；縮寫常為 POV)",
        keyWords: ["whole", "fantastic", "point of view"]
      },
      {
        start: 30.5,
        end: 37.0,
        en: "No one to tell us no, or where to go, or say we're only dreaming",
        zh: "沒有人能拒絕我們、指指點點，或是譏諷我們只是在作夢",
        phonetic: "noʊ wʌn tuː tɛl ʌs noʊ, ɔːr wɛər tuː ɡoʊ, ɔːr seɪ wɪr ˈoʊnli ˈdriːmɪŋ",
        notes: "【語意】表達自由無拘無束的心境",
        keyWords: ["dreaming"]
      },
      {
        start: 37.0,
        end: 43.5,
        en: "A whole new world, a dazzling place I never knew",
        zh: "一個嶄新的世界，一片我從未見識過、耀眼迷人的天地",
        phonetic: "ə hoʊl nuː wɜːrld, ə ˈdæzlɪŋ pleɪs aɪ ˈnɛvər nuː",
        notes: "【重點形容詞】dazzling (令人眼花繚亂的、燦爛奪目的)",
        keyWords: ["dazzling", "knew"]
      },
      {
        start: 43.5,
        end: 51.0,
        en: "But when I'm way up here, it's crystal clear",
        zh: "但是當我置身如此高空之上，一切都無比清澈明朗",
        phonetic: "bʌt wɛn aɪm weɪ ʌp hɪər, ɪts ˈkrɪstl klɪər",
        notes: "【成語】crystal clear (像水晶般剔透／顯而易見、清清楚楚)",
        keyWords: ["crystal clear"]
      },
      {
        start: 51.0,
        end: 58.0,
        en: "That now I'm in a whole new world with you",
        zh: "我終於體會，此刻我正與你共享這嶄新的大千世界",
        phonetic: "ðæt naʊ aɪm ɪn ə hoʊl nuː wɜːrld wɪð juː",
        notes: "【總結句】表達同在的幸福感",
        keyWords: ["world"]
      }
    ]
  },
  {
    id: "stand-by-me",
    title: "Stand By Me",
    artist: "Ben E. King",
    genre: "Classic Soul / R&B",
    level: "基礎入門 (A1-A2)",
    cover: "🤝",
    color: "linear-gradient(135deg, #10b981, #059669)",
    audioNotes: "歷史最偉大經典之一，旋律節奏鮮明，句型平實真摯，極度適合初學者練習口說連音與肯定句語氣。",
    synthPattern: "motown-bass-groove",
    bpm: 118,
    grammarFocus: [
      { rule: "Zero / First Conditionals (條件句)", example: "When the night has come, and the land is dark..." },
      { rule: "Concession & Determination (讓步與堅定語法)", example: "No I won't be afraid, just as long as you stand by me." }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 6.8,
        en: "When the night has come, and the land is dark",
        zh: "當黑夜降臨，大地陷入一片漆黑",
        phonetic: "wɛn ðə naɪt hæz kʌm, ænd ðə lænd ɪz dɑːrk",
        notes: "【時態】has come (現在完成式，表示夜晚已經來臨)",
        keyWords: ["night", "land", "dark"]
      },
      {
        start: 6.8,
        end: 13.5,
        en: "And the moon is the only light we'll see",
        zh: "而皎潔的明月，是我們唯一能看見的光芒",
        phonetic: "ænd ðə muːn ɪz ði ˈoʊnli laɪt wiːl siː",
        notes: "【冠詞與發音】the only 這裡的 the 需讀作 /ði/，因為 only 是母音開頭",
        keyWords: ["moon", "only", "light"]
      },
      {
        start: 13.5,
        end: 20.0,
        en: "No, I won't be afraid, oh, I won't be afraid",
        zh: "不，我絕不會畏懼，噢，我絲毫不會害怕",
        phonetic: "noʊ, aɪ woʊnt biː əˈfreɪd, oʊ, aɪ woʊnt biː əˈfreɪd",
        notes: "【形容詞】be afraid (害怕、恐懼)；won't = will not",
        keyWords: ["afraid", "won't"]
      },
      {
        start: 20.0,
        end: 26.5,
        en: "Just as long as you stand, stand by me",
        zh: "只要你能佇立在我身邊，支持陪伴著我",
        phonetic: "ʤʌst æz lɔːŋ æz juː stænd, stænd baɪ miː",
        notes: "【連接詞片語】as long as (只要...)；stand by someone (支持/陪伴某人)",
        keyWords: ["as long as", "stand by"]
      },
      {
        start: 26.5,
        end: 33.2,
        en: "So darling, darling, stand by me, oh stand by me",
        zh: "所以親愛的，請陪伴在我身旁，守護著我",
        phonetic: "soʊ ˈdɑːrlɪŋ, ˈdɑːrlɪŋ, stænd baɪ miː, oʊ stænd baɪ miː",
        notes: "【稱謂】darling (親愛的、寶貝)",
        keyWords: ["darling", "stand by"]
      },
      {
        start: 33.2,
        end: 40.0,
        en: "Oh stand, stand by me, stand by me",
        zh: "噢，請陪伴著我，守護在我身邊",
        phonetic: "oʊ stænd, stænd baɪ miː, stænd baɪ miː",
        notes: "【祈使句】重複以加強情感懇求",
        keyWords: ["stand by"]
      },
      {
        start: 40.0,
        end: 46.8,
        en: "If the sky that we look upon should tumble and fall",
        zh: "即使我們仰望的蒼穹崩塌傾頹、墜落大地",
        phonetic: "ɪf ðə skaɪ ðæt wiː lʊk əˈpɒn ʃʊd ˈtʌmbəl ænd fɔːl",
        notes: "【動詞片語】look upon (仰望、看待)；tumble and fall (翻滾跌落、坍塌崩解)",
        keyWords: ["sky", "tumble", "fall"]
      },
      {
        start: 46.8,
        end: 53.5,
        en: "Or the mountain should crumble to the sea",
        zh: "抑或是高山巍峨盡皆崩解、沉入汪洋之中",
        phonetic: "ɔːr ðə ˈmaʊntən ʃʊd ˈkrʌmbəl tuː ðə siː",
        notes: "【生動動詞】crumble (粉碎、崩解、碎裂成塊)",
        keyWords: ["mountain", "crumble", "sea"]
      },
      {
        start: 53.5,
        end: 60.0,
        en: "I won't cry, I won't cry, no I won't shed a tear",
        zh: "我也不會痛哭，我絕不啜泣，連一滴眼淚都不會掉下",
        phonetic: "aɪ woʊnt kraɪ, aɪ woʊnt kraɪ, noʊ aɪ woʊnt ʃɛd ə tɪər",
        notes: "【優雅片語】shed a tear (流下一滴淚；shed 流出/脫落)",
        keyWords: ["shed", "tear", "cry"]
      },
      {
        start: 60.0,
        end: 67.0,
        en: "Just as long as you stand, stand by me",
        zh: "只要有你在身邊支持著我",
        phonetic: "ʤʌst æz lɔːŋ æz juː stænd, stænd baɪ miː",
        notes: "【主旨複誦】深情堅定",
        keyWords: ["stand by"]
      }
    ]
  },
  {
    id: "country-roads",
    title: "Take Me Home, Country Roads",
    artist: "John Denver",
    genre: "American Folk / Country",
    level: "中級 (B1)",
    cover: "🏞️",
    color: "linear-gradient(135deg, #0ea5e9, #0284c7)",
    audioNotes: "全美最經典鄉村民謠，地名與自然風光詞彙豐富，副歌旋律極易朗朗上口，是訓練鄉村連音與節奏感的最佳曲目。",
    synthPattern: "folk-guitar-strum",
    bpm: 82,
    grammarFocus: [
      { rule: "Comparative Forms & Metaphor (比較級與比喻)", example: "Older than the trees, younger than the mountains, growin' like a breeze." },
      { rule: "Present Participle Reduction (現在分詞縮讀)", example: "Growin' = growing, blowing = blowin' (流行鄉村口音縮省略 g)" }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 6.5,
        en: "Almost heaven, West Virginia",
        zh: "幾乎有如人間天堂，西維吉尼亞州",
        phonetic: "ˈɔːlmoʊst ˈhɛvən, wɛst vərˈʤɪnjə",
        notes: "【文化背景】West Virginia (美國東南部以阿帕拉契山脈著名的山地州)",
        keyWords: ["almost", "heaven"]
      },
      {
        start: 6.5,
        end: 12.8,
        en: "Blue Ridge Mountains, Shenandoah River",
        zh: "藍嶺山脈綿延，雪蘭多河水潺潺",
        phonetic: "bluː rɪʤ ˈmaʊntənz, ˌʃɛnənˈdoʊə ˈrɪvər",
        notes: "【專有名詞】Blue Ridge (藍嶺山脈)；Shenandoah (雪蘭多河，美洲原住民語意為星辰之女)",
        keyWords: ["mountains", "river"]
      },
      {
        start: 12.8,
        end: 19.0,
        en: "Life is old there, older than the trees",
        zh: "那裡的歲月悠久沉靜，比古木森林還要滄桑",
        phonetic: "laɪf ɪz oʊld ðɛər, ˈoʊldər ðæn ðə triːz",
        notes: "【比較級】older than (比...更古老)",
        keyWords: ["trees", "older"]
      },
      {
        start: 19.0,
        end: 25.5,
        en: "Younger than the mountains, growin' like a breeze",
        zh: "卻又比巍峨群山年輕，如清風般自在生長、吹拂大地",
        phonetic: "ˈjʌŋɡər ðæn ðə ˈmaʊntənz, ˈɡroʊɪn laɪk ə briːz",
        notes: "【片語】breeze (微風)；growin' = growing (鄉村歌曲常將 -ing 簡略為 -in')",
        keyWords: ["younger", "breeze"]
      },
      {
        start: 25.5,
        end: 32.0,
        en: "Country roads, take me home to the place I belong",
        zh: "鄉村小路，請引領我回家，回到那屬於我的歸屬之地",
        phonetic: "ˈkʌntri roʊdz, teɪk miː hoʊm tuː ðə pleɪs aɪ bɪˈlɔːŋ",
        notes: "【核心片語】belong to (屬於)；the place I belong (我所歸屬的地方)",
        keyWords: ["country roads", "belong"]
      },
      {
        start: 32.0,
        end: 38.5,
        en: "West Virginia, mountain mama, take me home, country roads",
        zh: "西維吉尼亞，宛如群山母親，帶我回家吧，蜿蜒的鄉村路",
        phonetic: "wɛst vərˈʤɪnjə, ˈmaʊntən ˈmɑːmə, teɪk miː hoʊm, ˈkʌntri roʊdz",
        notes: "【修辭】mountain mama (把山脈擬人化為孕育一切的母親)",
        keyWords: ["mama", "country roads"]
      },
      {
        start: 38.5,
        end: 45.0,
        en: "All my memories gather 'round her, miner's lady, stranger to blue water",
        zh: "所有的回憶都圍繞著她，她是礦工之妻，未曾見過碧藍大洋",
        phonetic: "ɔːl maɪ ˈmɛməriz ˈɡæðər raʊnd hɜːr, ˈmaɪnərz ˈleɪdi, ˈstreɪnʤər tuː bluː ˈwɔːtər",
        notes: "【片語】stranger to (對...感到陌生；未曾經歷過...)",
        keyWords: ["memories", "gather", "stranger"]
      },
      {
        start: 45.0,
        end: 52.0,
        en: "Dark and dusty, painted on the sky, misty taste of moonshine, teardrop in my eye",
        zh: "昏暗揚塵染遍蒼穹，自釀烈酒散發著迷濛香氣，眼角滑落思鄉淚滴",
        phonetic: "dɑːrk ænd ˈdʌsti, ˈpeɪntɪd ɒn ðə skaɪ, ˈmɪsti teɪst əv ˈmuːnˌʃaɪn, ˈtɪrˌdrɒp ɪn maɪ aɪ",
        notes: "【文化俚語】moonshine (原本指私釀玉米烈酒，也是鄉村特產)；teardrop (淚珠)",
        keyWords: ["dusty", "misty", "moonshine", "teardrop"]
      }
    ]
  },
  {
    id: "fly-me-to-the-moon",
    title: "Fly Me to the Moon",
    artist: "Frank Sinatra",
    genre: "Jazz / Standard",
    level: "進階文雅 (B2)",
    cover: "🌙",
    color: "linear-gradient(135deg, #a855f7, #ec4899)",
    audioNotes: "經典爵士搖擺名曲，句式精緻優雅，押韻節奏典雅，是學習英文浪漫修辭與詩意表達的代表作。",
    synthPattern: "jazz-swing-piano",
    bpm: 110,
    grammarFocus: [
      { rule: "Imperative Mood for Wishes (祈使與願望語氣)", example: "Fly me to the moon, let me play among the stars." },
      { rule: "Idiomatic Paraphrasing (同義置換)", example: "In other words, hold my hand. In other words, baby, kiss me." }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 5.5,
        en: "Fly me to the moon, let me play among the stars",
        zh: "帶我飛向明月，讓我在璀璨群星之間恣意徜徉",
        phonetic: "flaɪ miː tuː ðə muːn, lɛt miː pleɪ əˈmʌŋ ðə stɑːrz",
        notes: "【介系詞】among (在...群體之中，三者以上；兩者之間用 between)",
        keyWords: ["moon", "stars", "among"]
      },
      {
        start: 5.5,
        end: 11.0,
        en: "Let me see what spring is like on Jupiter and Mars",
        zh: "讓我一睹木星與火星上的春日究竟是何種光景",
        phonetic: "lɛt miː siː wʌt sprɪŋ ɪz laɪk ɒn ˈʤuːpɪtər ænd mɑːrz",
        notes: "【疑問句轉名詞子句】what spring is like (春天是長什麼模樣)",
        keyWords: ["spring", "Jupiter", "Mars"]
      },
      {
        start: 11.0,
        end: 16.5,
        en: "In other words, hold my hand",
        zh: "換句話說，請牽緊我的雙手",
        phonetic: "ɪn ˈʌðər wɜːrdz, hoʊld maɪ hænd",
        notes: "【轉折片語】in other words (換句話說、也就是說)",
        keyWords: ["in other words", "hold"]
      },
      {
        start: 16.5,
        end: 22.0,
        en: "In other words, baby, kiss me",
        zh: "也就是說，親愛的，請吻我吧",
        phonetic: "ɪn ˈʌðər wɜːrdz, ˈbeɪbi, kɪs miː",
        notes: "【真情告白】直率真誠的爵士魅力",
        keyWords: ["kiss"]
      },
      {
        start: 22.0,
        end: 27.5,
        en: "Fill my heart with song, and let me sing forevermore",
        zh: "讓歌聲填滿我的心靈，讓我直到永遠都為你歌唱",
        phonetic: "fɪl maɪ hɑːrt wɪð sɔːŋ, ænd lɛt miː sɪŋ fərˈɛvərˌmɔːr",
        notes: "【古雅字詞】forevermore (永遠、長長久久，比 forever 更具詩意)",
        keyWords: ["fill", "forevermore"]
      },
      {
        start: 27.5,
        end: 33.0,
        en: "You are all I long for, all I worship and adore",
        zh: "你是我心中唯一的渴望，是我全心崇敬與摯愛的一切",
        phonetic: "juː ɑːr ɔːl aɪ lɔːŋ fɔːr, ɔːl aɪ ˈwɜːrʃɪp ænd əˈdɔːr",
        notes: "【動詞片語】long for (深切渴望)；adore (深愛、愛慕)",
        keyWords: ["long for", "worship", "adore"]
      },
      {
        start: 33.0,
        end: 38.5,
        en: "In other words, please be true",
        zh: "換言之，請對我堅貞不渝",
        phonetic: "ɪn ˈʌðər wɜːrdz, pliːz biː truː",
        notes: "【片語】be true (忠誠、真摯、不變心)",
        keyWords: ["true"]
      },
      {
        start: 38.5,
        end: 45.0,
        en: "In other words, I love you",
        zh: "簡單說，我深深愛著你",
        phonetic: "ɪn ˈʌðər wɜːrdz, aɪ lʌv juː",
        notes: "【經典結尾】化繁為簡的真情終句",
        keyWords: ["love"]
      }
    ]
  },
  {
    id: "you-are-my-sunshine",
    title: "You Are My Sunshine",
    artist: "Traditional / Folk",
    genre: "Acoustic Folk",
    level: "基礎入門 (A1)",
    cover: "☀️",
    color: "linear-gradient(135deg, #eab308, #ca8a04)",
    audioNotes: "傳唱近百年的世界名曲，韻律優美自然，發音圓潤，是練習母音長短音與基礎英語時態對比的極佳曲目。",
    synthPattern: "warm-music-box",
    bpm: 96,
    grammarFocus: [
      { rule: "Simple Present & Past Contrasts (現在式與過去式對照)", example: "The other night, dear, as I lay sleeping, I dreamed I held you in my arms." },
      { rule: "Colloquial Expressions (日常暖心口語)", example: "You make me happy when skies are gray." }
    ],
    lyrics: [
      {
        start: 0.0,
        end: 6.0,
        en: "You are my sunshine, my only sunshine",
        zh: "你是我的陽光，我唯一璀璨的陽光",
        phonetic: "juː ɑːr maɪ ˈsʌnˌʃaɪn, maɪ ˈoʊnli ˈsʌnˌʃaɪn",
        notes: "【隱喻】sunshine (喻指帶來歡樂與溫暖的摯愛之人)",
        keyWords: ["sunshine", "only"]
      },
      {
        start: 6.0,
        end: 12.0,
        en: "You make me happy when skies are gray",
        zh: "即使天空烏雲籠罩，你也能使我笑容綻放",
        phonetic: "juː meɪk miː ˈhæpi wɛn skaɪz ɑːr ɡreɪ",
        notes: "【使役動詞用法】make + 受詞 + 形容詞 (make me happy)；gray skies 比喻心情陰沉",
        keyWords: ["happy", "skies", "gray"]
      },
      {
        start: 12.0,
        end: 18.0,
        en: "You'll never know, dear, how much I love you",
        zh: "親愛的，你永遠不會知道我對你的愛有多深",
        phonetic: "juːl ˈnɛvər noʊ, dɪər, haʊ mʌʧ aɪ lʌv juː",
        notes: "【程度感嘆】how much I love you (我有多愛你)",
        keyWords: ["never", "dear", "love"]
      },
      {
        start: 18.0,
        end: 25.0,
        en: "Please don't take my sunshine away",
        zh: "所以請不要帶走我那珍貴的陽光",
        phonetic: "pliːz doʊnt teɪk maɪ ˈsʌnˌʃaɪn əˈweɪ",
        notes: "【片語】take away (拿走、帶走、奪去)",
        keyWords: ["take away", "sunshine"]
      },
      {
        start: 25.0,
        end: 31.0,
        en: "The other night, dear, as I lay sleeping",
        zh: "前些天夜裡，親愛的，當我沉沉入睡之時",
        phonetic: "ði ˈʌðər naɪt, dɪər, æz aɪ leɪ ˈsliːpɪŋ",
        notes: "【時間片語】the other night (前幾天的某個夜晚)；lay (lie 的過去式，躺臥)",
        keyWords: ["night", "sleeping", "lay"]
      },
      {
        start: 31.0,
        end: 37.0,
        en: "I dreamed I held you in my arms",
        zh: "我夢見我曾將你緊緊擁入我的懷中",
        phonetic: "aɪ driːmd aɪ hɛld juː ɪn maɪ ɑːrmz",
        notes: "【時態】held 為 hold (擁抱) 的過去式；in someone's arms (在某人懷抱中)",
        keyWords: ["dreamed", "held", "arms"]
      },
      {
        start: 37.0,
        end: 43.0,
        en: "When I awoke, dear, I was mistaken",
        zh: "但當我驚醒時，親愛的，才發現只是一場誤會與幻夢",
        phonetic: "wɛn aɪ əˈwoʊk, dɪər, aɪ wʌz mɪsˈteɪkən",
        notes: "【片語】be mistaken (弄錯了、誤會了)；awoke 是 awake 的過去式",
        keyWords: ["awoke", "mistaken"]
      },
      {
        start: 43.0,
        end: 50.0,
        en: "So I hung my head and I cried",
        zh: "於是我垂下了頭，止不住地流下眼淚",
        phonetic: "soʊ aɪ hʌŋ maɪ hɛd ænd aɪ kraɪd",
        notes: "【肢體語言片語】hang one's head (垂頭喪氣、低頭難過)",
        keyWords: ["hung", "head", "cried"]
      }
    ]
  }
];

// 常用單字字典庫 (支援點擊單字即時查詢、音標與詳細中文釋義)
const SONG_DICTIONARY = {
  "stuck": { kk: "/stʌk/", pos: "adj.", zh: "卡住的、動彈不得的、陷入困境的", desc: "動詞 stick 的過去式與過去分詞，常用於 be stuck in traffic (塞車) 或 feel stuck (感覺迷惘)。" },
  "middle": { kk: "/ˈmɪdl/", pos: "n.", zh: "中間、中央", desc: "in the middle of 即在...中間或忙於某事之時。" },
  "sea": { kk: "/si/", pos: "n.", zh: "海洋、汪洋", desc: "at sea 常有引申義「茫然失措、困惑不知所措」。" },
  "sail": { kk: "/sel/", pos: "v.", zh: "航行、揚帆行駛", desc: "sail through something 意為「輕易順利通過考驗」。" },
  "world": { kk: "/wɝld/", pos: "n.", zh: "世界、天下", desc: "mean the world to someone 意為「對某人極其珍貴重要」。" },
  "find": { kk: "/faɪnd/", pos: "v.", zh: "發現、找到、查覺", desc: "find out 意為「查出真相、得知消息」。" },
  "lost": { kk: "/lɔst/", pos: "adj.", zh: "迷失的、遺失的", desc: "lose 的過去分詞；get lost 也有口語「走開、滾開」之意。" },
  "dark": { kk: "/dɑrk/", pos: "n./adj.", zh: "黑暗、昏暗的", desc: "in the dark 常指「被蒙在鼓裡、不知情」。" },
  "light": { kk: "/laɪt/", pos: "n./adj.", zh: "光芒、燈光、輕巧的", desc: "see the light 意為「恍然大悟」。" },
  "guide": { kk: "/ɡaɪd/", pos: "v./n.", zh: "引導、指引；導遊、指南", desc: "guiding principle 指「指導原則」。" },
  "count": { kk: "/kaʊnt/", pos: "v.", zh: "計數、數數；有重要性", desc: "count on 表示「指望、信賴」；Every second counts (分秒必爭)。" },
  "supposed": { kk: "/səˈpozd/", pos: "adj.", zh: "應當的、被期望的", desc: "be supposed to do something 是日常口語高頻用法「理應做某事」。" },
  "toss": { kk: "/tɔs/", pos: "v.", zh: "翻轉、投擲", desc: "toss and turn 指「翻來覆去睡不著」。" },
  "turn": { kk: "/tɝn/", pos: "v.", zh: "轉身、轉向、轉動", desc: "turn into (變成)；turn down (拒絕或轉小聲)。" },
  "asleep": { kk: "/əˈslip/", pos: "adj.", zh: "睡著的、入睡的", desc: "fall asleep 進入夢鄉；fast asleep 熟睡。" },
  "beside": { kk: "/bɪˈsaɪd/", pos: "prep.", zh: "在...旁邊", desc: "注意不要跟 besides (而且/此外) 混淆。" },
  "forget": { kk: "/fɚˈɡɛt/", pos: "v.", zh: "忘記、遺忘", desc: "forget to do (忘記要去做) vs forget doing (忘記曾做過)。" },
  "really": { kk: "/ˈriəli/", pos: "adv.", zh: "真正地、實在地", desc: "用於修飾形容詞或強調真實情感。" },
  "mean": { kk: "/min/", pos: "v.", zh: "意味著、意欲；對...重要", desc: "What do you mean? (你是什麼意思？)" },
  "remind": { kk: "/rɪˈmaɪnd/", pos: "v.", zh: "提醒、使想起", desc: "remind me to call mom (提醒我打給媽媽)。" },
  "shoulder": { kk: "/ˈʃoldɚ/", pos: "n.", zh: "肩膀", desc: "shoulder the responsibility (擔負起責任)。" },
  "cry": { kk: "/kraɪ/", pos: "v.", zh: "哭泣、呼喊", desc: "cry out (大聲呼喊)；a far cry from (大相逕庭)。" },
  "never": { kk: "/ˈnɛvɚ/", pos: "adv.", zh: "永不、絕不", desc: "強烈否定副詞。" },
  "goodbye": { kk: "/ˌɡʊdˈbaɪ/", pos: "int./n.", zh: "再見、道別", desc: "源自 God be with you (願上帝與你同在)。" },
  "shining": { kk: "/ˈʃaɪnɪŋ/", pos: "adj.", zh: "閃耀的、光亮的", desc: "a shining example 卓越的典範。" },
  "shimmering": { kk: "/ˈʃɪmərɪŋ/", pos: "adj.", zh: "微光閃爍的、波光粼粼的", desc: "常形容月光下的水面或寶石光澤。" },
  "splendid": { kk: "/ˈsplɛndɪd/", pos: "adj.", zh: "極佳的、壯麗輝煌的", desc: "英式英語常用來表示「太棒了、太精彩了」。" },
  "princess": { kk: "/ˈprɪnsɛs/", pos: "n.", zh: "公主", desc: "prince 是王子。" },
  "heart": { kk: "/hɑrt/", pos: "n.", zh: "心臟、心靈、核心", desc: "by heart (牢記、默背)。" },
  "decide": { kk: "/dɪˈsaɪd/", pos: "v.", zh: "決定、裁決", desc: "decision 為名詞形。" },
  "wonder": { kk: "/ˈwʌndɚ/", pos: "n./v.", zh: "奇蹟、驚奇；想知道", desc: "No wonder (難怪)；Seven wonders (七大奇景)。" },
  "sideways": { kk: "/ˈsaɪdˌwez/", pos: "adv.", zh: "向側邊、橫向地", desc: "look sideways 斜眼看。" },
  "magic": { kk: "/ˈmæʤɪk/", pos: "adj./n.", zh: "神奇的、魔法的；魔術", desc: "work like magic (靈驗無比)。" },
  "carpet": { kk: "/ˈkɑrpɪt/", pos: "n.", zh: "地毯", desc: "red carpet (紅地毯)。" },
  "fantastic": { kk: "/fænˈtæstɪk/", pos: "adj.", zh: "極好的、幻想奇妙的", desc: "日常生活極高頻讚美詞彙。" },
  "dreaming": { kk: "/ˈdrimɪŋ/", pos: "v./adj.", zh: "作夢、有夢想的", desc: "dream big (敢於做大夢)。" },
  "dazzling": { kk: "/ˈdæzlɪŋ/", pos: "adj.", zh: "耀眼的、光彩奪目的", desc: "dazzle (使眼花繚亂)。" },
  "crystal": { kk: "/ˈkrɪstl/", pos: "n./adj.", zh: "水晶、晶瑩剔透的", desc: "crystal clear (顯而易見、十分明瞭)。" },
  "afraid": { kk: "/əˈfred/", pos: "adj.", zh: "害怕的、恐懼的", desc: "I'm afraid so/not (恐怕是/恐怕不行，委婉語法)。" },
  "stand": { kk: "/stænd/", pos: "v.", zh: "站立、忍受、支持", desc: "I can't stand it (我受不了了)；stand for (代表)。" },
  "darling": { kk: "/ˈdɑrlɪŋ/", pos: "n.", zh: "親愛的、心愛的人", desc: "溫馨親暱稱呼。" },
  "tumble": { kk: "/ˈtʌmbl/", pos: "v.", zh: "跌倒、翻滾、墜落", desc: "tumble down (摔落)。" },
  "fall": { kk: "/fɔl/", pos: "v./n.", zh: "落下、跌倒；秋天", desc: "fall in love with (愛上某人)。" },
  "mountain": { kk: "/ˈmaʊntn/", pos: "n.", zh: "山脈、高山", desc: "mountain of tasks (堆積如山的工作)。" },
  "crumble": { kk: "/ˈkrʌmbl/", pos: "v.", zh: "粉碎、崩潰、碎裂", desc: "cookie crumbles (人生常態無可奈何)。" },
  "shed": { kk: "/ʃɛd/", pos: "v.", zh: "流出、脫落、蛻皮", desc: "shed light on (闡明、揭露事實)。" },
  "tear": { kk: "/tɪr/", pos: "n.", zh: "眼淚、淚滴", desc: "注意發 /tɪr/ 為眼淚；發 /tɛr/ 則為撕裂。" },
  "heaven": { kk: "/ˈhɛvn/", pos: "n.", zh: "天堂、樂土", desc: "in seventh heaven (欣喜若狂)。" },
  "river": { kk: "/ˈrɪvɚ/", pos: "n.", zh: "河流、溪流", desc: "cross the river (渡河)。" },
  "trees": { kk: "/triz/", pos: "n.", zh: "樹木、森林", desc: "can't see the wood for the trees (見樹不見林)。" },
  "breeze": { kk: "/briz/", pos: "n.", zh: "微風、輕而易舉的事", desc: "It's a breeze (小菜一碟、非常輕鬆)。" },
  "belong": { kk: "/bɪˈlɔŋ/", pos: "v.", zh: "屬於、適得其所", desc: "sense of belonging (歸屬感)。" },
  "memories": { kk: "/ˈmɛməriz/", pos: "n.", zh: "記憶、回憶", desc: "memory (單數)；fond memories (美好回憶)。" },
  "gather": { kk: "/ˈɡæðɚ/", pos: "v.", zh: "聚集、收集", desc: "gather around (圍聚在一起)。" },
  "stranger": { kk: "/ˈstrenʤɚ/", pos: "n.", zh: "陌生人", desc: "stranger to (對...不熟悉)。" },
  "dusty": { kk: "/ˈdʌsti/", pos: "adj.", zh: "布滿灰塵的", desc: "dust (名詞：灰塵；動詞：撢除灰塵)。" },
  "misty": { kk: "/ˈmɪsti/", pos: "adj.", zh: "有霧的、模糊迷濛的", desc: "mist (薄霧)。" },
  "moonshine": { kk: "/ˈmunˌʃaɪn/", pos: "n.", zh: "私釀酒、月光", desc: "美國傳統文化中秘密蒸餾的玉米酒。" },
  "teardrop": { kk: "/ˈtɪrˌdrɑp/", pos: "n.", zh: "淚珠、眼淚滴", desc: "teardrop-shaped (水滴形的)。" },
  "stars": { kk: "/stɑrz/", pos: "n.", zh: "星星、明星", desc: "reach for the stars (胸懷大志)。" },
  "among": { kk: "/əˈmʌŋ/", pos: "prep.", zh: "在...之中 (三者以上)", desc: "among friends (在朋友群中)。" },
  "spring": { kk: "/sprɪŋ/", pos: "n.", zh: "春天、泉水、彈簧", desc: "spring forward (彈起、向前跳躍)。" },
  "kiss": { kk: "/kɪs/", pos: "v./n.", zh: "親吻、吻", desc: "blow a kiss (送飛吻)。" },
  "fill": { kk: "/fɪl/", pos: "v.", zh: "填滿、充滿", desc: "fill out a form (填寫表格)。" },
  "forevermore": { kk: "/fəˌrɛvərˈmɔr/", pos: "adv.", zh: "永遠、長久", desc: "詩意與文雅的長久表達。" },
  "worship": { kk: "/ˈwɝʃɪp/", pos: "v./n.", zh: "崇敬、敬奉、熱愛", desc: "hero worship (盲目崇拜)。" },
  "adore": { kk: "/əˈdɔr/", pos: "v.", zh: "深愛、愛慕、極其喜歡", desc: "adorable (可愛惹人愛的)。" },
  "sunshine": { kk: "/ˈsʌnˌʃaɪn/", pos: "n.", zh: "陽光、朝氣、心愛之人", desc: "Bring a little sunshine into someone's life (帶給人溫暖)。" },
  "happy": { kk: "/ˈhæpi/", pos: "adj.", zh: "快樂的、幸福的", desc: "happy-go-lucky (樂天隨性的)。" },
  "gray": { kk: "/ɡre/", pos: "adj./n.", zh: "灰色的、陰暗憂鬱的", desc: "美式拼寫為 gray，英式多為 grey。" },
  "sleeping": { kk: "/ˈslipɪŋ/", pos: "adj./v.", zh: "沉睡的、入睡中", desc: "sleeping beauty (睡美人)。" },
  "held": { kk: "/hɛld/", pos: "v.", zh: "擁抱、握住 (hold 過去式)", desc: "hold one's hand (握住某人的手)。" },
  "arms": { kk: "/ɑrmz/", pos: "n.", zh: "手臂、懷抱、武器", desc: "open arms (熱情張開雙臂)。" },
  "awoke": { kk: "/əˈwok/", pos: "v.", zh: "醒來 (awake 過去式)", desc: "awoke to the sound of rain (在雨聲中醒來)。" },
  "mistaken": { kk: "/mɪˈstekən/", pos: "adj.", zh: "犯錯的、誤會的", desc: "Unless I am mistaken (除非我弄錯了)。" },
  "hung": { kk: "/hʌŋ/", pos: "v.", zh: "懸掛、垂下 (hang 過去式)", desc: "hang out (閒晃、消磨時間)。" }
};
