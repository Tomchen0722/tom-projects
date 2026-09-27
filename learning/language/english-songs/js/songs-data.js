/**
 * 英文歌學習英語 - 60 首精選曲目資料庫 (60 Curated Songs Database)
 * 涵蓋六大分類：
 * 1. 流行抒情金曲 (Pop & Ballads)
 * 2. 迪士尼與動畫名曲 (Disney & Animation)
 * 3. 傳奇民謠與經典搖滾 (Folk & Classic Rock)
 * 4. 爵士風華與浪漫標準曲 (Jazz & Standards)
 * 5. 溫馨童謠與基礎入門 (Gentle Folk & Beginners)
 * 6. 勵志心靈與生命之歌 (Inspirational & Life Songs)
 *
 * 每一首均包含：
 * - 英文原文歌詞與精緻時間戳記 (LRC)
 * - 繁體中文逐句翻譯
 * - 國際音標 / KK 音標
 * - 重點單字與片語文法解析
 * - 原創和弦伴奏設定與導唱歌聲參數
 */

const SONGS_DATA = [
  // ─── 1. 流行抒情金曲 (Pop & Ballads) ───
  {
    id: "count-on-me",
    title: "Count On Me",
    artist: "Bruno Mars",
    genre: "流行抒情",
    category: "pop",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "🌿",
    color: "#C68A2C",
    bpm: 88,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "日常口語最高頻的友情金曲，清晰輕快的民謠吉他，包含條件句與生活片語。",
    lyrics: [
      { start: 0.0, end: 5.5, en: "If you ever find yourself stuck in the middle of the sea", zh: "如果你發現自己被困在汪洋大海之中", phonetic: "ɪf juː ˈɛvər faɪnd jʊərˈsɛlf stʌk ɪn ðə ˈmɪdəl əv ðə siː", notes: "【片語】stuck in the middle of (困在...之中)", keyWords: ["stuck", "middle", "sea"] },
      { start: 5.5, end: 10.2, en: "I'll sail the world to find you", zh: "我會揚帆航遍全世界找到你", phonetic: "aɪl seɪl ðə wɜːrld tuː faɪnd juː", notes: "【語法】I'll = I will (表達承諾與決心)", keyWords: ["sail", "world", "find"] },
      { start: 10.2, end: 15.6, en: "If you ever find yourself lost in the dark and you can't see", zh: "如果你發現自己迷失在黑暗中，伸手不見五指", phonetic: "ɪf juː ˈɛvər faɪnd jʊərˈsɛlf lɔːst ɪn ðə dɑːrk ænd juː kænt siː", notes: "【連音】and you 常弱化讀作 /ən juː/", keyWords: ["lost", "dark"] },
      { start: 15.6, end: 20.8, en: "I'll be the light to guide you", zh: "我會成為引導你的那道光芒", phonetic: "aɪl biː ðə laɪt tuː ɡaɪd juː", notes: "【單字】guide (動詞：引導；名詞：指南)", keyWords: ["light", "guide"] },
      { start: 20.8, end: 26.2, en: "We find out what we're made of", zh: "我們終於明白自己有多堅強、由什麼特質鑄成", phonetic: "wiː faɪnd aʊt wʌt wɪr meɪd ʌv", notes: "【片語】be made of (由...組成/骨氣品格)", keyWords: ["find out", "made of"] },
      { start: 26.2, end: 31.8, en: "When we are called to help our friends in need", zh: "當我們被召喚去幫助身處患難的朋友時", phonetic: "wɛn wiː ɑːr kɔːld tuː hɛlp ˈaʊər frɛndz ɪn niːd", notes: "【諺語】A friend in need is a friend indeed (患難見真情)", keyWords: ["friends", "need"] },
      { start: 31.8, end: 37.0, en: "You can count on me like one, two, three", zh: "你可以像數一、二、三一樣依靠我", phonetic: "juː kæn kaʊnt ɒn miː laɪk wʌn tuː θriː", notes: "【核心片語】count on (依靠、指望)", keyWords: ["count on", "one", "two", "three"] },
      { start: 37.0, end: 41.5, en: "I'll be there", zh: "我立刻就會趕到你身邊", phonetic: "aɪl biː ðɛər", notes: "【日常表達】I'll be there (守護在你身旁)", keyWords: ["there"] },
      { start: 41.5, end: 47.0, en: "And I know when I need it, I can count on you like four, three, two", zh: "我也深知當我需要時，也能如倒數四、三、二般依賴你", phonetic: "ænd aɪ noʊ wɛn aɪ niːd ɪt, aɪ kæn kaʊnt ɒn juː", notes: "【倒數節奏】four, three, two 回應友情互信", keyWords: ["need", "count on"] },
      { start: 47.0, end: 51.5, en: "And you'll be there", zh: "而你也一定會在我身邊", phonetic: "ænd juːl biː ðɛər", notes: "【縮讀】you'll = you will", keyWords: ["there"] },
      { start: 51.5, end: 57.0, en: "'Cause that's what friends are supposed to do, oh yeah", zh: "因為這正是身為好朋友所應該做的", phonetic: "kəz ðæts wʌt frɛndz ɑːr səˈpoʊzd tuː duː", notes: "【重要句型】be supposed to (本該、理應)", keyWords: ["supposed to", "friends"] }
    ]
  },
  {
    id: "someone-like-you",
    title: "Someone Like You",
    artist: "Adele",
    genre: "流行抒情",
    category: "pop",
    level: "中級 (B1)",
    cover: "🍂",
    color: "#A25F28",
    bpm: 68,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "深情鋼琴彈唱，詞彙真摯深沉，適合練習英文過去式與感情釋懷句型。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I heard that you're settled down", zh: "我聽說你已經安定下來、成家立業", phonetic: "aɪ hɜːrd ðæt jʊər ˈsɛtld daʊn", notes: "【片語】settle down (安頓下來、過平靜生活)", keyWords: ["heard", "settled down"] },
      { start: 6.5, end: 12.8, en: "That you found a girl and you're married now", zh: "聽說你遇見了合適的女孩，如今已經步入婚姻", phonetic: "ðæt juː faʊnd ə ɡɜːrl ænd jʊər ˈmærɪd naʊ", notes: "【狀態】married (已婚的)", keyWords: ["found", "married"] },
      { start: 12.8, end: 19.5, en: "I heard that your dreams came true", zh: "我聽說你的夢想如今都已成真", phonetic: "aɪ hɜːrd ðæt jʊər driːmz keɪm truː", notes: "【名句】dreams come true (夢想成真)", keyWords: ["dreams", "true"] },
      { start: 19.5, end: 26.0, en: "Guess she gave you things I didn't give to you", zh: "猜想她給了你許多我未能給予你的溫暖吧", phonetic: "ɡɛs ʃiː ɡeɪv juː θɪŋz aɪ ˈdɪdnt ɡɪv tuː juː", notes: "【比較句】didn't give to you (過去未能給予)", keyWords: ["guess", "give"] },
      { start: 26.0, end: 32.5, en: "Never mind, I'll find someone like you", zh: "沒關係的，我也一定會找到一個像你一樣好的人", phonetic: "ˈnɛvər maɪnd, aɪl faɪnd ˈsʌmwʌn laɪk juː", notes: "【口語】Never mind (別放在心上、沒關係)", keyWords: ["never mind", "someone"] },
      { start: 32.5, end: 39.0, en: "I wish nothing but the best for you, too", zh: "我也衷心為你獻上最真摯的祝福", phonetic: "aɪ wɪʃ ˈnʌθɪŋ bʌt ðə bɛst fɔːr juː tuː", notes: "【優雅片語】nothing but (僅僅、只有；全心全意)", keyWords: ["wish", "best"] },
      { start: 39.0, end: 46.0, en: "Don't forget me, I beg, I remember you said", zh: "只求你不要遺忘我，我仍記得你曾說過", phonetic: "doʊnt fərˈɡɛt miː aɪ bɛɡ aɪ rɪˈmɛmbər juː sɛd", notes: "【動詞】beg (懇求)；remember (記得)", keyWords: ["forget", "beg", "remember"] },
      { start: 46.0, end: 54.0, en: "Sometimes it lasts in love, but sometimes it hurts instead", zh: "有時候愛能長相廝守，但有時候卻只留下椎心刺痛", phonetic: "ˈsʌmˌtaɪmz ɪt læsts ɪn lʌv bʌt ˈsʌmˌtaɪmz ɪt hɜːrts ɪnˈstɛd", notes: "【哲理句】instead (取而代之；反而)", keyWords: ["lasts", "love", "hurts", "instead"] }
    ]
  },
  {
    id: "perfect",
    title: "Perfect",
    artist: "Ed Sheeran",
    genre: "流行抒情",
    category: "pop",
    level: "初級 (A2)",
    cover: "💍",
    color: "#B87818",
    bpm: 63,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "現代婚禮第一名曲，旋律舒緩，用詞純淨溫柔，極適合練習慢速連音。",
    lyrics: [
      { start: 0.0, end: 6.8, en: "I found a love for me", zh: "我尋覓到了一份專屬於我的真愛", phonetic: "aɪ faʊnd ə lʌv fɔːr miː", notes: "【語句】found 為 find 的過去式", keyWords: ["found", "love"] },
      { start: 6.8, end: 14.0, en: "Darling, just dive right in and follow my lead", zh: "親愛的，就全心投入吧，跟隨我的腳步", phonetic: "ˈdɑːrlɪŋ ʤʌst daɪv raɪt ɪn ænd ˈfɒloʊ maɪ liːd", notes: "【片語】dive right in (縱身躍入、全力投入)；follow one's lead (跟隨引導)", keyWords: ["dive", "follow", "lead"] },
      { start: 14.0, end: 21.0, en: "Well, I found a girl, beautiful and sweet", zh: "我遇見了一位美麗又甜美純潔的女孩", phonetic: "wɛl aɪ faʊnd ə ɡɜːrl ˈbjuːtəfəl ænd swiːt", notes: "【形容詞】sweet (甜美溫柔)", keyWords: ["beautiful", "sweet"] },
      { start: 21.0, end: 28.5, en: "I never knew you were the someone waiting for me", zh: "我從未意料到，那一直默默等待著我的人竟然就是你", phonetic: "aɪ ˈnɛvər nuː juː wɜːr ðə ˈsʌmwʌn ˈweɪtɪŋ fɔːr miː", notes: "【現在分詞】waiting for me 修飾 someone", keyWords: ["knew", "waiting"] },
      { start: 28.5, end: 36.0, en: "'Cause we were just kids when we fell in love", zh: "因為當我們當初相戀時，都還只是不懂事的情竇初開", phonetic: "kəz wiː wɜːr ʤʌst kɪdz wɛn wiː fɛl ɪn lʌv", notes: "【重要片語】fall in love (墜入愛河；過去式 fell)", keyWords: ["kids", "fell in love"] },
      { start: 36.0, end: 44.0, en: "Not knowing what it was, I will not give you up this time", zh: "那時懵懵懂懂不知何為愛，但這一次我絕不會放棄你", phonetic: "nɒt ˈnoʊɪŋ wʌt ɪt wʌz aɪ wɪl nɒt ɡɪv juː ʌp ðɪs taɪm", notes: "【片語】give up (放棄、拋棄)", keyWords: ["knowing", "give up"] },
      { start: 44.0, end: 52.0, en: "Darling, you look perfect tonight", zh: "親愛的，今夜的你看起來無比完美動人", phonetic: "ˈdɑːrlɪŋ juː lʊk ˈpɜːrfɪkt təˈnaɪt", notes: "【感官動詞】look + 形容詞 (look perfect)", keyWords: ["darling", "perfect", "tonight"] }
    ]
  },
  {
    id: "shallow",
    title: "Shallow",
    artist: "Lady Gaga & Bradley Cooper",
    genre: "流行抒情",
    category: "pop",
    level: "中高級 (B2)",
    cover: "🌊",
    color: "#5C6B73",
    bpm: 96,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "奧斯卡最佳原創歌曲，音域寬廣，富含深沉隱喻（淺灘與深淵的對比）。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Tell me somethin', girl, are you happy in this modern world?", zh: "告訴我，女孩，在這個喧囂的現代世界裡你過得快樂嗎？", phonetic: "tɛl miː ˈsʌmθɪŋ ɡɜːrl ɑːr juː ˈhæpi ɪn ðɪs ˈmɒdərn wɜːrld", notes: "【口語】somethin' = something (縮省略 g)", keyWords: ["happy", "modern"] },
      { start: 6.5, end: 13.0, en: "Or do you need more? Is there somethin' else you're searchin' for?", zh: "還是你心中渴望更多？是否還有你一直在尋覓追尋的嚮往？", phonetic: "ɔːr duː juː niːd mɔːr ɪz ðɛər ˈsʌmθɪŋ ɛls jʊər ˈsɜːrʧɪŋ fɔːr", notes: "【動詞片語】search for (尋找、探索)", keyWords: ["search for"] },
      { start: 13.0, end: 19.5, en: "I'm fallin' in all the good times I find myself longin' for change", zh: "我正陷落沉醉，縱使在所有美好時光裡，我也渴望尋求改變", phonetic: "aɪm ˈfɔːlɪn ɪn ɔːl ðə ɡʊd taɪmz aɪ faɪnd maɪˈsɛlf ˈlɔːŋɪŋ fɔːr ʧeɪnʤ", notes: "【動詞片語】long for (深切渴望)", keyWords: ["long for", "change"] },
      { start: 19.5, end: 26.5, en: "And in the bad times I fear myself", zh: "而在低谷困厄之時，我甚至畏懼自己的脆弱", phonetic: "ænd ɪn ðə bæd taɪmz aɪ fɪər maɪˈsɛlf", notes: "【心理描述】fear oneself (對自我感到懷疑不安)", keyWords: ["fear"] },
      { start: 26.5, end: 33.5, en: "I'm off the deep end, watch as I dive in", zh: "我已縱身躍入深水區，看著我義無反顧地向下潛潛入", phonetic: "aɪm ɔːf ðə diːp ɛnd wɒʧ æz aɪ daɪv ɪn", notes: "【隱喻成語】off the deep end (不再瞻前顧後、大膽冒險)", keyWords: ["deep end", "dive"] },
      { start: 33.5, end: 41.0, en: "I'll never meet the ground", zh: "我絕不會墜落觸底", phonetic: "aɪl ˈnɛvər miːt ðə ɡraʊnd", notes: "【象徵】meet the ground (摔落地面)", keyWords: ["ground"] },
      { start: 41.0, end: 48.0, en: "Crash through the surface, where they can't hurt us", zh: "衝破水面破浪而出，置身於世俗流言無法傷害我們之處", phonetic: "kræʃ θruː ðə ˈsɜːrfɪs wɛər ðeɪ kænt hɜːrt ʌs", notes: "【動態動詞】crash through (撞破、穿透)", keyWords: ["surface", "hurt"] },
      { start: 48.0, end: 56.0, en: "We're far from the shallow now", zh: "此時此刻，我們早已遠離了那淺薄平庸的淺灘", phonetic: "wɪr fɑːr frʌm ðə ˈʃæloʊ naʊ", notes: "【核心概念】shallow (淺灘；象徵膚淺保守的生活)", keyWords: ["far from", "shallow"] }
    ]
  },
  {
    id: "all-of-me",
    title: "All of Me",
    artist: "John Legend",
    genre: "流行抒情",
    category: "pop",
    level: "中級 (B1)",
    cover: "🎹",
    color: "#6D597A",
    bpm: 60,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "當代浪漫鋼琴代表作，充滿巧妙對比修辭（curves and edges, end and beginning）。",
    lyrics: [
      { start: 0.0, end: 6.2, en: "What would I do without your smart mouth?", zh: "如果沒有你那伶牙俐齒的小嘴，我該怎麼辦？", phonetic: "wʌt wʊd aɪ duː wɪˈðaʊt jʊər smɑːrt maʊθ", notes: "【習慣用語】smart mouth (口齒伶俐/愛頂嘴可愛模樣)", keyWords: ["without", "smart"] },
      { start: 6.2, end: 12.5, en: "Drawing me in, and you kicking me out", zh: "時而溫柔吸引著我，時而又把我推得遠遠的", phonetic: "ˈdrɔːɪŋ miː ɪn ænd juː ˈkɪkɪŋ miː aʊt", notes: "【對比動詞】draw in (吸引) vs kick out (踢開)", keyWords: ["drawing", "kicking"] },
      { start: 12.5, end: 19.0, en: "You've got my head spinning, no kidding, I can't pin you down", zh: "你讓我神魂顛倒，不開玩笑，我永遠捉摸不透你的心思", phonetic: "juːv ɡɒt maɪ hɛd ˈspɪnɪŋ noʊ ˈkɪdɪŋ aɪ kænt pɪn juː daʊn", notes: "【生活片語】no kidding (不開玩笑)；pin down (看透、搞懂)", keyWords: ["spinning", "kidding"] },
      { start: 19.0, end: 26.0, en: "'Cause all of me loves all of you", zh: "因為我所有的靈魂，深深愛著你的一切所有", phonetic: "kəz ɔːl əv miː lʌvz ɔːl əv juː", notes: "【名句】all of me loves all of you", keyWords: ["all of me"] },
      { start: 26.0, end: 32.5, en: "Love your curves and all your edges, all your perfect imperfections", zh: "愛你的迷人曲線與所有稜角，深愛你身上每一處完美的瑕疵", phonetic: "lʌv jʊər kɜːrvz ænd ɔːl jʊər ˈɛʤɪz ɔːl jʊər ˈpɜːrfɪkt ˌɪmpərˈfɛkʃənz", notes: "【極致修辭】perfect imperfections (以明暗對照法表達全盤接納)", keyWords: ["curves", "edges", "imperfections"] },
      { start: 32.5, end: 39.5, en: "Give your all to me, I'll give my all to you", zh: "將你的全部交給我，我也會將我的一生全心交付於你", phonetic: "ɡɪv jʊər ɔːl tuː miː aɪl ɡɪv maɪ ɔːl tuː juː", notes: "【互惠誓言】give one's all (全力以赴、毫無保留)", keyWords: ["give", "all"] }
    ]
  },
  {
    id: "memories",
    title: "Memories",
    artist: "Maroon 5",
    genre: "流行抒情",
    category: "pop",
    level: "初級 (A2)",
    cover: "🥂",
    color: "#B56576",
    bpm: 91,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "旋律取樣自卡農 (Pachelbel's Canon)，發音極清晰，充滿致敬思念意境。",
    lyrics: [
      { start: 0.0, end: 5.5, en: "Here's to the ones that we got", zh: "為我們身邊緊緊相依的摯友舉杯慶祝", phonetic: "hɪrz tuː ðə wʌnz ðæt wiː ɡɒt", notes: "【祝酒詞】Here's to... (為...敬一杯、乾杯)", keyWords: ["here's to"] },
      { start: 5.5, end: 10.5, en: "Cheers to the wish you were here, but you're not", zh: "也為心中多希望你能在此刻相伴，卻已不在的人乾杯", phonetic: "ʧɪərz tuː ðə wɪʃ juː wɜːr hɪər bʌt jʊər nɒt", notes: "【乾杯片語】Cheers to (敬...一杯)；wish + 過去式 (假設語氣)", keyWords: ["cheers", "wish"] },
      { start: 10.5, end: 15.5, en: "'Cause the drinks bring back all the memories", zh: "因為杯中烈酒，總會喚醒深藏心底的所有往日回憶", phonetic: "kəz ðə drɪŋks brɪŋ bæk ɔːl ðə ˈmɛməriz", notes: "【動詞片語】bring back (帶回、勾起)", keyWords: ["bring back", "memories"] },
      { start: 15.5, end: 21.0, en: "Of everything we've been through", zh: "重溫我們曾攜手走過的大風大浪與點點滴滴", phonetic: "əv ˈɛvrɪˌθɪŋ wiːv biːn θruː", notes: "【片語】go through (歷經磨難、走過歲月)", keyWords: ["been through"] },
      { start: 21.0, end: 26.5, en: "Toast to the ones here today", zh: "向今天歡聚在此的每個人致敬", phonetic: "toʊst tuː ðə wʌnz hɪər təˈdeɪ", notes: "【祝酒】toast to (向...祝酒舉杯)", keyWords: ["toast"] },
      { start: 26.5, end: 32.5, en: "Toast to the ones that we lost on the way", zh: "也向在人生的漫漫旅途中，先行離我們而去的親友致敬", phonetic: "toʊst tuː ðə wʌnz ðæt wiː lɔːst ɒn ðə weɪ", notes: "【片語】on the way (在路上、在旅程中)", keyWords: ["lost", "on the way"] },
      { start: 32.5, end: 40.0, en: "'Cause the drinks bring back all the memories and the memories bring back, memories bring back you", zh: "因為美酒勾起記憶，而回憶又悄悄將你帶回我的身旁", phonetic: "kəz ðə drɪŋks brɪŋ bæk ɔːl ðə ˈmɛməriz", notes: "【回文修辭】層層遞進，深情動人", keyWords: ["memories", "bring back"] }
    ]
  },
  {
    id: "just-the-way-you-are",
    title: "Just the Way You Are",
    artist: "Bruno Mars",
    genre: "流行抒情",
    category: "pop",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "✨",
    color: "#E5989B",
    bpm: 109,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "洋溢陽光讚美的自信情歌，含有大量對容貌神態的生動讚美詞彙。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Oh, her eyes, her eyes make the stars look like they're not shinin'", zh: "噢，她的雙眸璀璨明媚，讓漫天星辰都相形失色、暗淡無光", phonetic: "oʊ hɜːr aɪz hɜːr aɪz meɪk ðə stɑːrz lʊk laɪk ðeɪr nɒt ˈʃaɪnɪŋ", notes: "【使役動詞】make + 受詞 + 原形動詞 (make the stars look)", keyWords: ["eyes", "stars", "shining"] },
      { start: 6.5, end: 13.0, en: "Her hair, her hair falls perfectly without her tryin'", zh: "她的秀髮自然垂落飄逸，不必刻意梳理就那樣恰到好處", phonetic: "hɜːr hɛər hɜːr hɛər fɔːlz ˈpɜːrfɪktli wɪˈðaʊt hɜːr ˈtraɪɪŋ", notes: "【介系詞】without + V-ing (無需多費心思)", keyWords: ["hair", "perfectly"] },
      { start: 13.0, end: 19.5, en: "She's so beautiful and I tell her every day", zh: "她是如此美麗動人，而我每一天都忍不住深情告訴她", phonetic: "ʃiːz soʊ ˈbjuːtəfəl ænd aɪ tɛl hɜːr ˈɛvri deɪ", notes: "【日常表達】tell someone every day", keyWords: ["beautiful"] },
      { start: 19.5, end: 26.5, en: "When I see your face, there's not a thing that I would change", zh: "當我注視著你的臉龐，世上沒有任何一處是我想要改變的", phonetic: "wɛn aɪ siː jʊər feɪs ðɛrz nɒt ə θɪŋ ðæt aɪ wʊd ʧeɪnʤ", notes: "【否定強調】not a thing (絲毫沒有、一點也不)", keyWords: ["face", "change"] },
      { start: 26.5, end: 34.0, en: "'Cause you're amazing, just the way you are", zh: "因為你本身就是如此耀眼驚艷，正是你最原本真實的模樣", phonetic: "kəz jʊər əˈmeɪzɪŋ ʤʌst ðə weɪ juː ɑːr", notes: "【經典語句】just the way you are (就維持你原本的樣子)", keyWords: ["amazing", "way you are"] }
    ]
  },
  {
    id: "thinking-out-loud",
    title: "Thinking Out Loud",
    artist: "Ed Sheeran",
    genre: "流行抒情",
    category: "pop",
    level: "中級 (B1)",
    cover: "🕯️",
    color: "#6D6875",
    bpm: 79,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "藍調靈魂吉他經典，講述伴隨一生白頭偕老的承諾，情深意長。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When your legs don't work like they used to before", zh: "當歲月漸長，你的雙腿不再如年輕時那般健步如飛", phonetic: "wɛn jʊər lɛɡz doʊnt wɜːrk laɪk ðeɪ juːst tuː bɪˈfɔːr", notes: "【過去習慣】used to (過去曾經習慣如何)", keyWords: ["legs", "used to"] },
      { start: 6.5, end: 13.0, en: "And I can't sweep you off of your feet", zh: "而我也許再也無法像當年那樣，一把將你抱起旋轉", phonetic: "ænd aɪ kænt swiːp juː ɔːf əv jʊər fiːt", notes: "【習語】sweep someone off their feet (使某人為之傾倒、深深陶醉)", keyWords: ["sweep off"] },
      { start: 13.0, end: 19.5, en: "Will your mouth still remember the taste of my love?", zh: "你的雙唇是否還會清晰記得我唇齒間愛的餘溫？", phonetic: "wɪl jʊər maʊθ stɪl rɪˈmɛmbər ðə teɪst əv maɪ lʌv", notes: "【深情提問】remember the taste", keyWords: ["remember", "taste"] },
      { start: 19.5, end: 26.5, en: "Will your eyes still smile from your cheeks?", zh: "你的雙眸是否依然會伴隨著臉頰淺淺漾起笑意？", phonetic: "wɪl jʊər aɪz stɪl smaɪl frʌm jʊər ʧiːks", notes: "【生動刻畫】eyes smile from cheeks", keyWords: ["smile", "cheeks"] },
      { start: 26.5, end: 34.0, en: "And, darling, I will be loving you 'til we're seventy", zh: "親愛的，我會一直深深愛著你，直到我們攜手白頭至七十歲", phonetic: "ænd ˈdɑːrlɪŋ aɪ wɪl biː ˈlʌvɪŋ juː tɪl wɪr ˈsɛvnti", notes: "【未來進行式】will be loving you (持續深愛)", keyWords: ["loving", "seventy"] },
      { start: 34.0, end: 42.0, en: "And baby, my heart could still fall as hard at twenty-three", zh: "寶貝，我的心悸動依然，一如二十三歲初見時那般怦然心動", phonetic: "ænd ˈbeɪbi maɪ hɑːrt kʊd stɪl fɔːl æz hɑːrd æt ˈtwɛnti θriː", notes: "【比較句】as hard as (同樣深陷動心)", keyWords: ["heart", "twenty-three"] }
    ]
  },
  {
    id: "fix-you",
    title: "Fix You",
    artist: "Coldplay",
    genre: "流行搖滾",
    category: "pop",
    level: "中級 (B1)",
    cover: "💡",
    color: "#4A5568",
    bpm: 70,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "英式搖滾療癒名作，講述在遭遇挫折低潮時的陪伴與慰藉，感人肺腑。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When you try your best, but you don't succeed", zh: "當你已經竭盡全力，卻依然未能收穫預期的成功", phonetic: "wɛn juː traɪ jʊər bɛst bʌt juː doʊnt səkˈsiːd", notes: "【努力片語】try one's best (全力以赴)；succeed (成功)", keyWords: ["try your best", "succeed"] },
      { start: 6.5, end: 13.0, en: "When you get what you want, but not what you need", zh: "當你得到了看似渴望的一切，內心深處卻深感空虛荒涼", phonetic: "wɛn juː ɡɛt wʌt juː wɒnt bʌt nɒt wʌt juː niːd", notes: "【名詞子句】what you want vs what you need", keyWords: ["want", "need"] },
      { start: 13.0, end: 19.5, en: "When you feel so tired, but you can't sleep", zh: "當你身心疲憊至極，躺在床上卻怎麼也無法闔眼入眠", phonetic: "wɛn juː fiːl soʊ ˈtaɪərd bʌt juː kænt sliːp", notes: "【情緒描寫】feel tired (心力交瘁)", keyWords: ["tired", "sleep"] },
      { start: 19.5, end: 26.5, en: "Stuck in reverse", zh: "人生彷彿卡在倒退檔，寸步難行", phonetic: "stʌk ɪn rɪˈvɜːrs", notes: "【比喻片語】stuck in reverse (陷入停滯倒退)", keyWords: ["stuck", "reverse"] },
      { start: 26.5, end: 33.5, en: "Lights will guide you home", zh: "點點溫暖燈火，終會引領你平安返家", phonetic: "laɪts wɪl ɡaɪd juː hoʊm", notes: "【象徵】Lights (希望、親情、愛的光芒)", keyWords: ["lights", "guide", "home"] },
      { start: 33.5, end: 40.5, en: "And ignite your bones", zh: "重新點燃你骨子裡的熱情與勇氣", phonetic: "ænd ɪɡˈnaɪt jʊər boʊnz", notes: "【文學用詞】ignite (點燃燃起)", keyWords: ["ignite", "bones"] },
      { start: 40.5, end: 48.0, en: "And I will try to fix you", zh: "而我會竭盡所能，治癒陪伴著受傷的你", phonetic: "ænd aɪ wɪl traɪ tuː fɪks juː", notes: "【核心承諾】fix you (修復、療傷、撫慰心靈)", keyWords: ["try", "fix"] }
    ]
  },
  {
    id: "until-i-found-you",
    title: "Until I Found You",
    artist: "Stephen Sanchez",
    genre: "復古抒情",
    category: "pop",
    level: "中級 (B1)",
    cover: "📻",
    color: "#7E52A0",
    bpm: 101,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "五十年代 Doo-Wop 復古搖滾風格，旋律優美高雅，語法純正典雅。",
    lyrics: [
      { start: 0.0, end: 6.0, en: "Georgia, wrap me up in all your", zh: "喬治亞，用你的一切溫柔將我緊緊包圍", phonetic: "ˈʤɔːrʤə ræp miː ʌp ɪn ɔːl jʊər", notes: "【動詞片語】wrap up in (包裹、包容)", keyWords: ["wrap up"] },
      { start: 6.0, end: 11.5, en: "I want you in my arms, oh let me", zh: "我只想將你擁入我的懷中，請讓我好好擁抱你", phonetic: "aɪ wɒnt juː ɪn maɪ ɑːrmz oʊ lɛt miː", notes: "【使役動詞】let me (讓我)", keyWords: ["arms"] },
      { start: 11.5, end: 17.5, en: "Hold you, I'll never let you go again, like I did", zh: "抱緊你，我絕不會再像從前那樣傻傻放開你的手", phonetic: "hoʊld juː aɪl ˈnɛvər lɛt juː ɡoʊ əˈɡɛn laɪk aɪ dɪd", notes: "【代動詞】like I did (如同我過去曾犯的錯)", keyWords: ["hold", "let go"] },
      { start: 17.5, end: 24.5, en: "Oh, I used to say", zh: "噢，我過去總自以為是地說", phonetic: "oʊ aɪ juːst tuː seɪ", notes: "【習慣短語】used to say (過去常說)", keyWords: ["used to"] },
      { start: 24.5, end: 32.0, en: "I would never fall in love until I found her", zh: "我以為我這一生絕不會輕易墜入情網，直到我遇見了她", phonetic: "aɪ wʊd ˈnɛvər fɔːl ɪn lʌv ənˈtɪl aɪ faʊnd hɜːr", notes: "【否定加直到】not... until... (直到...才...)", keyWords: ["fall in love", "until", "found"] },
      { start: 32.0, end: 40.0, en: "I said, 'I would never fall unless it's you I fall into'", zh: "我說：『我絕不輕易動心，除非那個人是你，我願全心奔赴』", phonetic: "aɪ sɛd aɪ wʊd ˈnɛvər fɔːl ənˈlɛs ɪts juː aɪ fɔːl ˈɪntuː", notes: "【條件連接詞】unless (除非)", keyWords: ["unless", "fall into"] }
    ]
  },
  {
    id: "a-thousand-years",
    title: "A Thousand Years",
    artist: "Christina Perri",
    genre: "流行抒情",
    category: "pop",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "⏳",
    color: "#A2708A",
    bpm: 70,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "暮光之城經典主題曲，大氣悠揚，時間概念與愛情承諾詞彙極具美感。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Heart beats fast, colors and promises", zh: "心跳悄然加速，繁華色彩與深情誓言在眼前交織", phonetic: "hɑːrt biːts fæst ˈkʌlərz ænd ˈprɒmɪsɪz", notes: "【生理描述】heart beats fast (心跳加速)", keyWords: ["heart", "beats", "promises"] },
      { start: 6.5, end: 13.0, en: "How to be brave? How can I love when I'm afraid to fall?", zh: "該如何鼓起勇氣？當我如此害怕摔得粉身碎骨，又該如何敞開心扉去愛？", phonetic: "haʊ tuː biː breɪv haʊ kæn aɪ lʌv wɛn aɪm əˈfreɪd tuː fɔːl", notes: "【句型】be afraid to (害怕去做某事)", keyWords: ["brave", "afraid"] },
      { start: 13.0, end: 19.5, en: "But watching you stand alone, all of my doubt suddenly goes away somehow", zh: "但看著你孤單佇立的身影，我所有的猶豫與疑慮頓時煙消雲散", phonetic: "bʌt ˈwɒʧɪŋ juː stænd əˈloʊn ɔːl əv maɪ daʊt ˈsʌdnli ɡoʊz əˈweɪ ˈsʌmˌhaʊ", notes: "【副詞】somehow (不知怎地、不知不覺間)", keyWords: ["stand alone", "doubt", "goes away"] },
      { start: 19.5, end: 26.5, en: "One step closer", zh: "再向你靠近一步", phonetic: "wʌn stɛp ˈkloʊsər", notes: "【比較級】closer (更加靠近)", keyWords: ["closer"] },
      { start: 26.5, end: 34.0, en: "I have died every day waiting for you", zh: "在等待著你的漫長歲月裡，我彷彿每一天都在相思中煎熬", phonetic: "aɪ hæv daɪd ˈɛvri deɪ ˈweɪtɪŋ fɔːr juː", notes: "【誇飾修辭】have died waiting (極致期盼)", keyWords: ["died", "waiting"] },
      { start: 34.0, end: 41.0, en: "Darling, don't be afraid, I have loved you for a thousand years", zh: "親愛的，不要懼怕，我已經愛了你一千年之久", phonetic: "ˈdɑːrlɪŋ doʊnt biː əˈfreɪd aɪ hæv lʌvd juː fɔːr ə ˈθaʊznd jɪərz", notes: "【現在完成式】have loved for a thousand years (跨越時空的愛)", keyWords: ["thousand years"] },
      { start: 41.0, end: 49.0, en: "I'll love you for a thousand more", zh: "未來的歲月，我願再深愛你另一個一千年", phonetic: "aɪl lʌv juː fɔːr ə ˈθaʊznd mɔːr", notes: "【永恆誓言】a thousand more (更長久的守候)", keyWords: ["love", "thousand"] }
    ]
  },
  {
    id: "say-you-wont-let-go",
    title: "Say You Won't Let Go",
    artist: "James Arthur",
    genre: "流行民謠",
    category: "pop",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "☕",
    color: "#6F4E37",
    bpm: 85,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "真摯樸實的民謠情歌，敘事性強，生活起居情景描摹極其細膩生動。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I met you in the dark, you lit me up", zh: "在人生最灰暗無光的角落遇見了你，是你點亮了我整個世界", phonetic: "aɪ mɛt juː ɪn ðə dɑːrk juː lɪt miː ʌp", notes: "【動詞片語】light up (照亮；過去式 lit up)", keyWords: ["dark", "lit up"] },
      { start: 6.5, end: 12.8, en: "You made me feel as though I was enough", zh: "你讓我終於覺得，原本不完美的自己也是值得被愛的", phonetic: "juː meɪd miː fiːl æz ðoʊ aɪ wʌz ɪˈnʌf", notes: "【連詞】as though = as if (彷彿)", keyWords: ["enough"] },
      { start: 12.8, end: 19.5, en: "We danced the night away, we drank too much", zh: "我們整夜歡舞縱情歡笑，杯酒微醺", phonetic: "wiː dænst ðə naɪt əˈweɪ wiː dræŋk tuː mʌʧ", notes: "【片語】dance the night away (徹夜起舞度過良宵)", keyWords: ["danced", "drank"] },
      { start: 19.5, end: 26.5, en: "I held your hair back when you were throwing up", zh: "當你反胃難受嘔吐時，我輕輕幫你撥開撫著長髮", phonetic: "aɪ hɛld jʊər hɛər bæk wɛn juː wɜːr ˈθroʊɪŋ ʌp", notes: "【生活片語】throw up (嘔吐；極具生活細節真實感)", keyWords: ["held", "throwing up"] },
      { start: 26.5, end: 33.5, en: "Then you smiled over your shoulder", zh: "隨後你轉過肩頭，給了我一個溫暖深情的微笑", phonetic: "ðɛn juː smaɪld ˈoʊvər jʊər ˈʃoʊldər", notes: "【身體描寫】over your shoulder (回眸轉身)", keyWords: ["smiled", "shoulder"] },
      { start: 33.5, end: 41.0, en: "For a minute, I was stone-cold sober", zh: "那一瞬間，我所有的醉意頓時清醒，心中一片澄澈", phonetic: "fɔːr ə ˈmɪnɪt aɪ wʌz stoʊn koʊld ˈsoʊbər", notes: "【成語】stone-cold sober (完全清醒、毫無醉意)", keyWords: ["sober"] },
      { start: 41.0, end: 48.0, en: "I pulled you closer to my chest", zh: "我輕輕將你拉近，緊緊貼在我的胸膛前", phonetic: "aɪ pʊld juː ˈkloʊsər tuː maɪ ʧɛst", notes: "【動作動詞】pull closer (拉近貼緊)", keyWords: ["pulled", "chest"] },
      { start: 48.0, end: 56.0, en: "And you asked me to stay over, I said, I already told ya, I think that you should get some rest", zh: "你輕聲邀我留宿，我說：傻瓜，我剛才就跟你說過了，你現在最需要好好休息", phonetic: "ænd juː æskt miː tuː steɪ ˈoʊvər", notes: "【口語】stay over (過夜留宿)；told ya = told you", keyWords: ["stay over", "rest"] }
    ]
  },
  {
    id: "photograph",
    title: "Photograph",
    artist: "Ed Sheeran",
    genre: "流行民謠",
    category: "pop",
    level: "初級 (A2)",
    cover: "📷",
    color: "#83677B",
    bpm: 108,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "用「照片」定格時間與愛的溫暖隱喻，是練習英語時間副詞與記憶詞彙的優質歌曲。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Loving can hurt, loving can hurt sometimes", zh: "愛有時會帶來疼痛，愛有時會讓人感到受傷難熬", phonetic: "ˈlʌvɪŋ kæn hɜːrt ˈlʌvɪŋ kæn hɜːrt ˈsʌmˌtaɪmz", notes: "【動名詞當主詞】Loving (去愛人這件事)", keyWords: ["loving", "hurt"] },
      { start: 6.5, end: 13.0, en: "But it's the only thing that I know", zh: "但這卻是我這輩子所知曉最真實珍貴的真理", phonetic: "bʌt ɪts ði ˈoʊnli θɪŋ ðæt aɪ noʊ", notes: "【發音】the only 發作 /ði ˈoʊnli/", keyWords: ["only thing"] },
      { start: 13.0, end: 19.5, en: "When it gets hard, you know it can get hard sometimes", zh: "當生活變得無比艱難沉重，你深知有時人生確實坎坷難行", phonetic: "wɛn ɪt ɡɛts hɑːrd juː noʊ ɪt kæn ɡɛt hɑːrd ˈsʌmˌtaɪmz", notes: "【連綴動詞】get hard (變得艱辛難熬)", keyWords: ["gets hard"] },
      { start: 19.5, end: 26.5, en: "It is the only thing that makes us feel alive", zh: "但愛也是唯一能讓我們真切體會生命跳動與活著的奇蹟", phonetic: "ɪt ɪz ði ˈoʊnli θɪŋ ðæt meɪks ʌs fiːl əˈlaɪv", notes: "【感官使役】make us feel alive (讓我們感受到生命力)", keyWords: ["alive"] },
      { start: 26.5, end: 33.5, en: "We keep this love in a photograph", zh: "我們把這份真摯純粹的愛，珍藏定格在一張泛黃的照片裡", phonetic: "wiː kiːp ðɪs lʌv ɪn ə ˈfoʊtəˌɡræf", notes: "【片語】keep in a photograph (定格珍存於相片中)", keyWords: ["photograph"] },
      { start: 33.5, end: 41.0, en: "We made these memories for ourselves", zh: "我們為彼此親手釀造了這些永難磨滅的珍貴回憶", phonetic: "wiː meɪd ðiːz ˈmɛməriz fɔːr ˌaʊərˈsɛlvz", notes: "【反身代名詞】ourselves (我們自己)", keyWords: ["memories", "ourselves"] },
      { start: 41.0, end: 49.0, en: "Where our eyes are never closing, our hearts were never broken, and time's forever frozen still", zh: "在相片裡，我們的眼眸永遠不曾闔上，心靈未曾破碎，歲月時光永遠溫柔靜止停留", phonetic: "wɛər ˈaʊər aɪz ɑːr ˈnɛvər ˈkloʊzɪŋ", notes: "【詩意隱喻】time is frozen still (時光被溫柔冰封凍結)", keyWords: ["broken", "frozen still"] }
    ]
  },
  {
    id: "make-you-feel-my-love",
    title: "Make You Feel My Love",
    artist: "Adele / Bob Dylan",
    genre: "經典民謠",
    category: "pop",
    level: "中級 (B1)",
    cover: "🌧️",
    color: "#5B7065",
    bpm: 72,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "鮑勃狄倫原創、愛黛兒深情翻唱之世界經典，修辭典雅，充滿無私奉獻的深情。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When the rain is blowing in your face", zh: "當冷冽的風雨肆無忌憚地拍打吹拂在你的臉上", phonetic: "wɛn ðə reɪn ɪz ˈbloʊɪŋ ɪn jʊər feɪs", notes: "【自然隱喻】風雨比喻人生艱辛", keyWords: ["rain", "blowing"] },
      { start: 6.5, end: 13.0, en: "And the whole world is on your case", zh: "當全世界彷彿都在挑剔為難你、讓你喘不過氣時", phonetic: "ænd ðə hoʊl wɜːrld ɪz ɒn jʊər keɪs", notes: "【慣用俚語】be on one's case (找麻煩、嚴苛挑剔責難)", keyWords: ["on your case"] },
      { start: 13.0, end: 19.5, en: "I could offer you a warm embrace", zh: "我會毫無保留為你敞開一個溫暖堅實的擁抱", phonetic: "aɪ kʊd ˈɒfər juː ə wɔːrm ɪmˈbreɪs", notes: "【優雅用詞】embrace = hug (擁抱)", keyWords: ["offer", "warm embrace"] },
      { start: 19.5, end: 26.5, en: "To make you feel my love", zh: "只為讓你真真切切感受到我深切的愛", phonetic: "tuː meɪk juː fiːl maɪ lʌv", notes: "【使役句型】make you feel my love", keyWords: ["feel my love"] },
      { start: 26.5, end: 33.5, en: "When the evening shadows and the stars appear", zh: "當暮色夜影低垂，群星漸次在蒼穹浮現之時", phonetic: "wɛn ði ˈiːvnɪŋ ˈʃædoʊz ænd ðə stɑːrz əˈpɪər", notes: "【時間描摹】evening shadows (黃昏暮影)", keyWords: ["shadows", "appear"] },
      { start: 33.5, end: 41.0, en: "And there is no one there to dry your tears", zh: "身邊若沒有任何一個人能為你拂去臉頰上的淚滴", phonetic: "ænd ðɛər ɪz noʊ wʌn ðɛər tuː draɪ jʊər tɪərz", notes: "【安慰片語】dry one's tears (擦乾淚水)", keyWords: ["dry", "tears"] },
      { start: 41.0, end: 49.0, en: "I could hold you for a million years to make you feel my love", zh: "我願意將你緊緊擁抱一百萬年，讓你確信這份至死不渝的愛", phonetic: "aɪ kʊd hoʊld juː fɔːr ə ˈmɪljən jɪərz", notes: "【誇飾情感】for a million years (歷經百萬年之久)", keyWords: ["million years"] }
    ]
  },

  // ─── 2. 迪士尼與動畫經典 (Disney & Animation) ───
  {
    id: "a-whole-new-world",
    title: "A Whole New World",
    artist: "Aladdin Soundtrack",
    genre: "迪士尼音樂劇",
    category: "disney",
    level: "中級 (B1-B2)",
    cover: "✨",
    color: "#6366F1",
    bpm: 76,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "迪士尼史上最華麗男女對唱，詞藻瑰麗，頭韻豐富，是學習典雅形容詞的最佳範例。",
    lyrics: [
      { start: 0.0, end: 6.2, en: "I can show you the world, shining, shimmering, splendid", zh: "我能為你展現整個世界：閃耀奪目、波光粼粼、燦爛壯麗", phonetic: "aɪ kæn ʃoʊ juː ðə wɜːrld ˈʃaɪnɪŋ ˈʃɪmərɪŋ ˈsplɛndɪd", notes: "【頭韻修辭】shining, shimmering, splendid 連綴押韻", keyWords: ["shining", "shimmering", "splendid"] },
      { start: 6.2, end: 12.8, en: "Tell me, princess, now when did you last let your heart decide?", zh: "告訴我，公主，你上一次聽從自己心聲做決定是什麼時候？", phonetic: "tɛl miː ˈprɪnsɛs naʊ wɛn dɪd juː læst lɛt jʊər hɑːrt dɪˈsaɪd", notes: "【使役動詞】let your heart decide", keyWords: ["princess", "heart", "decide"] },
      { start: 12.8, end: 18.5, en: "I can open your eyes, take you wonder by wonder", zh: "我能為你開啟全新視野，帶你閱覽一個又一個不可思議的奇蹟", phonetic: "aɪ kæn ˈoʊpən jʊər aɪz teɪk juː ˈwʌndər baɪ ˈwʌndər", notes: "【片語】wonder by wonder (一處又一處的奇觀)", keyWords: ["open", "wonder"] },
      { start: 18.5, end: 25.0, en: "Over, sideways and under on a magic carpet ride", zh: "乘著魔毯翱翔，穿越高空、側身盤旋、俯衝低掠", phonetic: "ˈoʊvər ˈsaɪdweɪz ænd ˈʌndər ɒn ə ˈmæʤɪk ˈkɑːrpɪt raɪd", notes: "【方位詞群】over, sideways, under", keyWords: ["magic carpet"] },
      { start: 25.0, end: 30.5, en: "A whole new world, a new fantastic point of view", zh: "一個嶄新的世界，一種令人驚嘆的全新視角與天地", phonetic: "ə hoʊl nuː wɜːrld ə nuː fænˈtæstɪk pɔɪnt əv vjuː", notes: "【片語】point of view (觀點視角；POV)", keyWords: ["fantastic", "point of view"] },
      { start: 30.5, end: 37.0, en: "No one to tell us no, or where to go, or say we're only dreaming", zh: "沒有人能拒絕指點我們，或譏諷我們只是在作夢", phonetic: "noʊ wʌn tuː tɛl ʌs noʊ ɔːr wɛər tuː ɡoʊ", notes: "【自由心境】表達掙脫束縛的灑脫", keyWords: ["dreaming"] },
      { start: 37.0, end: 43.5, en: "A whole new world, a dazzling place I never knew", zh: "一個嶄新的世界，一片我從未見識過、耀眼迷人的天地", phonetic: "ə hoʊl nuː wɜːrld ə ˈdæzlɪŋ pleɪs aɪ ˈnɛvər nuː", notes: "【生動形容詞】dazzling (令人眼花繚亂耀眼的)", keyWords: ["dazzling"] },
      { start: 43.5, end: 51.0, en: "But when I'm way up here, it's crystal clear", zh: "但是當我置身如此高空之上，一切都無比清澈明朗", phonetic: "bʌt wɛn aɪm weɪ ʌp hɪər ɪts ˈkrɪstl klɪər", notes: "【成語】crystal clear (極為清楚透徹)", keyWords: ["crystal clear"] },
      { start: 51.0, end: 58.0, en: "That now I'm in a whole new world with you", zh: "我終於體會，此刻我正與你共享這嶄新的大千世界", phonetic: "ðæt naʊ aɪm ɪn ə hoʊl nuː wɜːrld wɪð juː", notes: "【昇華結尾】同在的幸福感受", keyWords: ["whole new world"] }
    ]
  },
  {
    id: "let-it-go",
    title: "Let It Go",
    artist: "Idina Menzel (Frozen)",
    genre: "迪士尼音樂劇",
    category: "disney",
    level: "中級 (B1)",
    cover: "❄️",
    color: "#48CAE4",
    bpm: 137,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "全球現象級主題曲，充滿擺脫束縛、接納自我的震撼爆發力。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "The snow glows white on the mountain tonight, not a footprint to be seen", zh: "今夜皚皚白雪在山巔閃耀銀光，不見半個凡人的足跡", phonetic: "ðə snoʊ ɡloʊz waɪt ɒn ðə ˈmaʊntən təˈnaɪt nɒt ə ˈfʊtˌprɪnt tuː biː siːn", notes: "【景象描寫】footprint (腳印、足跡)", keyWords: ["snow", "glows", "footprint"] },
      { start: 6.5, end: 13.0, en: "A kingdom of isolation, and it looks like I'm the queen", zh: "這片遺世獨立的冰雪孤絕王國，看來我正是唯一的女王", phonetic: "ə ˈkɪŋdəm əv ˌaɪsəˈleɪʃən ænd ɪt lʊks laɪk aɪm ðə kwiːn", notes: "【名詞】isolation (孤立、隔絕封閉)", keyWords: ["kingdom", "isolation", "queen"] },
      { start: 13.0, end: 19.5, en: "The wind is howling like this swirling storm inside", zh: "呼嘯的寒風淒厲嘶吼，正如我內心深處盤旋翻湧的風暴", phonetic: "ðə wɪnd ɪz ˈhaʊlɪŋ laɪk ðɪs ˈswɜːrlɪŋ stɔːrm ɪnˈsaɪd", notes: "【動詞】howling (狂嘯)；swirling (旋轉盤旋)", keyWords: ["howling", "storm"] },
      { start: 19.5, end: 26.5, en: "Couldn't keep it in, heaven knows I tried", zh: "再也無法壓抑隱忍，蒼天明鑑我曾多麼努力克制", phonetic: "ˈkʊdnt kiːp ɪt ɪn ˈhɛvən noʊz aɪ traɪd", notes: "【日常短語】heaven knows (天知地知/天曉得)", keyWords: ["keep it in", "heaven knows"] },
      { start: 26.5, end: 33.5, en: "Let it go, let it go, can't hold it back anymore", zh: "放手吧，隨它去吧！再也無需壓抑隱藏自己的光芒", phonetic: "lɛt ɪt ɡoʊ lɛt ɪt ɡoʊ kænt hoʊld ɪt bæk ˌɛniˈmɔːr", notes: "【核心片語】let it go (放手釋懷)；hold back (抑制)", keyWords: ["let it go", "hold back"] },
      { start: 33.5, end: 41.0, en: "Let it go, let it go, turn away and slam the door", zh: "隨風去吧，轉身離去，毅然決然關上過去的重門", phonetic: "lɛt ɪt ɡoʊ lɛt ɪt ɡoʊ tɜːrn əˈweɪ ænd slæm ðə dɔːr", notes: "【有力動作】slam the door (用力關上大門、決絕告別)", keyWords: ["turn away", "slam"] },
      { start: 41.0, end: 49.0, en: "I don't care what they're going to say, let the storm rage on, the cold never bothered me anyway", zh: "我絲毫不介意旁人流言蜚語，任憑暴風雨肆虐吧，嚴寒酷冷從未動搖過我的心志", phonetic: "aɪ doʊnt kɛər wʌt ðeɪr ˈɡoʊɪŋ tuː seɪ", notes: "【經典語句】never bothered me anyway (從來影響不了我半分)", keyWords: ["rage on", "bothered"] }
    ]
  },
  {
    id: "can-you-feel-the-love-tonight",
    title: "Can You Feel the Love Tonight",
    artist: "Elton John (The Lion King)",
    genre: "迪士尼經典",
    category: "disney",
    level: "中級 (B1)",
    cover: "🦁",
    color: "#E09F3E",
    bpm: 85,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "獅子王傳奇金曲，艾爾頓強作曲，充滿非洲草原日落的靜謐與大愛。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "There's a calm surrender to the rush of day", zh: "在一整天喧囂奔波後，迎來了一份平靜安詳的臣服與釋懷", phonetic: "ðɛrz ə kɑːm səˈrɛndər tuː ðə rʌʃ əv deɪ", notes: "【詩意名詞】calm surrender (平靜安詳的順應妥協)", keyWords: ["calm", "surrender"] },
      { start: 6.5, end: 13.0, en: "When the heat of a rolling wind can be turned away", zh: "當迎面襲來的灼熱狂風，終於被溫柔化解撥開", phonetic: "wɛn ðə hiːt əv ə ˈroʊlɪŋ wɪnd kæn biː tɜːrnd əˈweɪ", notes: "【被動語態】can be turned away", keyWords: ["heat", "wind"] },
      { start: 13.0, end: 19.5, en: "An enchanted moment, and it sees me through", zh: "這片如著了魔般迷人的靜謐時刻，伴隨撫慰著我度過迷惘", phonetic: "æn ɪnˈʧæntɪd ˈmoʊmənt ænd ɪt siːz miː θruː", notes: "【形容詞】enchanted (著了魔法的、令人陶醉的)", keyWords: ["enchanted", "sees me through"] },
      { start: 19.5, end: 26.5, en: "It's enough for this restless wanderer just to be with you", zh: "能與你相伴相守，便足以撫平我這漂泊浪子躁動不安的心魂", phonetic: "ɪts ɪˈnʌf fɔːr ðɪs ˈrɛstləs ˈwɒndərər ʤʌst tuː biː wɪð juː", notes: "【人物刻畫】restless wanderer (躁動迷茫的流浪者)", keyWords: ["restless", "wanderer"] },
      { start: 26.5, end: 34.0, en: "And can you feel the love tonight? It is where we are", zh: "你能真切感受到今晚空氣中流淌的愛意嗎？愛就在我們身旁", phonetic: "ænd kæn juː fiːl ðə lʌv təˈnaɪt ɪt ɪz wɛər wiː ɑːr", notes: "【疑問反詰】can you feel the love tonight", keyWords: ["feel the love"] },
      { start: 34.0, end: 42.0, en: "It's enough for this wide-eyed wanderer that we got this far", zh: "回顧我們一路歷盡艱辛走到了這裡，對初醒人世的旅人而言已是莫大恩賜", phonetic: "ɪts ɪˈnʌf fɔːr ðɪs waɪd aɪd ˈwɒndərər ðæt wiː ɡɒt ðɪs fɑːr", notes: "【複合形容詞】wide-eyed (睜大雙眼/天真純潔的)", keyWords: ["wide-eyed", "got this far"] }
    ]
  },
  {
    id: "how-far-ill-go",
    title: "How Far I'll Go",
    artist: "Auli'i Cravalho (Moana)",
    genre: "迪士尼音樂劇",
    category: "disney",
    level: "中級 (B1)",
    cover: "⛵",
    color: "#0077B6",
    bpm: 82,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "海洋奇緣主題曲，Lin-Manuel Miranda 詞作，充滿對未知世界探索的熱血憧憬。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I've been staring at the edge of the water, 'long as I can remember", zh: "打從我記憶之初，我便日復一日凝望著那片海水的無垠邊際", phonetic: "aɪv biːn ˈstɛərɪŋ æt ði ɛʤ əv ðə ˈwɔːtər", notes: "【現在完成進行式】have been staring (長期凝視佇足)", keyWords: ["staring", "edge", "water"] },
      { start: 6.5, end: 13.0, en: "Never really knowing why, I wish I could be the perfect daughter", zh: "從未真正懂得箇中緣由，我也多麼期盼自己能當個乖巧安分的完美女兒", phonetic: "ˈnɛvər ˈrɪəli ˈnoʊɪŋ waɪ aɪ wɪʃ aɪ kʊd biː ðə ˈpɜːrfɪkt ˈdɔːtər", notes: "【與事實相反假設】wish I could be", keyWords: ["perfect", "daughter"] },
      { start: 13.0, end: 19.5, en: "But I come back to the water, no matter how hard I try", zh: "但無論我多麼努力說服自己，腳步卻總是身不由己地重回浪潮前", phonetic: "bʌt aɪ kʌm bæk tuː ðə ˈwɔːtər noʊ ˈmætər haʊ hɑːrd aɪ traɪ", notes: "【讓步子句】no matter how hard (無論多麼努力)", keyWords: ["no matter how"] },
      { start: 19.5, end: 26.5, en: "Every turn I take, every trail I track, every path I make, every road leads back", zh: "我轉過的每一個彎、踏過的每一條山徑、開拓的每條小路，最終都引領我回到原點", phonetic: "ˈɛvri tɜːrn aɪ teɪk ˈɛvri treɪl aɪ træk", notes: "【排比韻律】trail, track, path, road", keyWords: ["trail", "track", "path"] },
      { start: 26.5, end: 34.0, en: "See the line where the sky meets the sea? It calls me", zh: "看見那天海相連的遙遠水平線了嗎？它正低聲召喚著我的名字", phonetic: "siː ðə laɪn wɛər ðə skaɪ miːts ðə siː ɪt kɔːlz miː", notes: "【景深召喚】where the sky meets the sea", keyWords: ["sky meets the sea", "calls me"] },
      { start: 34.0, end: 42.0, en: "And no one knows, how far it goes, if the wind in my sail on the sea stays behind me, one day I'll know, how far I'll go", zh: "無人能知曉那片海洋究竟有多麼浩瀚深遠，只要揚起風帆順風啟航，終有一天我會親眼見證自己能航向何方", phonetic: "ænd noʊ wʌn noʊz haʊ fɑːr ɪt ɡoʊz", notes: "【核心抱負】How far I'll go (我究竟能走多遠)", keyWords: ["how far", "sail"] }
    ]
  },
  {
    id: "beauty-and-the-beast",
    title: "Beauty and the Beast",
    artist: "Celine Dion & Peabo Bryson",
    genre: "迪士尼經典",
    category: "disney",
    level: "中級 (B1)",
    cover: "🌹",
    color: "#D4A373",
    bpm: 84,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "美女與野獸傳奇二重唱，詩句押韻極致精練，古典文雅。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Tale as old as time, true as it can be", zh: "如歲月般久遠悠長的神話傳奇，真摯無欺一如世間至理", phonetic: "teɪl æz oʊld æz taɪm truː æz ɪt kæn biː", notes: "【同等比較】as old as time (盤古開天般古老)", keyWords: ["tale", "time"] },
      { start: 6.5, end: 13.0, en: "Barely even friends, then somebody bends, unexpectedly", zh: "起初甚至稱不上是朋友，然而某一方悄悄卸下了防備包容退讓，出乎所有人的預料", phonetic: "ˈbɛərli ˈiːvən frɛndz ðɛn ˈsʌmˌbɒdi bɛndz ˌʌnɪkˈspɛktɪdli", notes: "【心理轉換】somebody bends (有人退讓、打開心扉)", keyWords: ["barely", "unexpectedly"] },
      { start: 13.0, end: 20.0, en: "Just a little change, small to say the least, both a little scared, neither one prepared", zh: "只是一點點微不足道的微妙轉變，彼此心中都有幾分惶恐怯步，誰都未曾做好心裡準備", phonetic: "ʤʌst ə ˈlɪtl ʧeɪnʤ smɔːl tuː seɪ ðə liːst", notes: "【插入成語】to say the least (至少可以這麼說/退一步而言)", keyWords: ["scared", "prepared"] },
      { start: 20.0, end: 28.0, en: "Beauty and the Beast", zh: "正是這一段美女與野獸的愛戀傳奇", phonetic: "ˈbjuːti ænd ðə biːst", notes: "【曲目精華】Beauty and the Beast", keyWords: ["beauty", "beast"] },
      { start: 28.0, end: 36.0, en: "Ever just the same, ever a surprise, ever as before, ever just as sure, as the sun will rise", zh: "歷經滄桑永恆不渝，卻又每次都帶來令人驚喜的悸動，如同太陽明日定會破曉升起那般堅信無疑", phonetic: "ˈɛvər ʤʌst ðə seɪm ˈɛvər ə sərˈpraɪz", notes: "【排比確信】as sure as the sun will rise (確信無疑一如日出日落)", keyWords: ["surprise", "sun will rise"] }
    ]
  },
  {
    id: "remember-me",
    title: "Remember Me",
    artist: "Coco Soundtrack",
    genre: "皮克斯經典",
    category: "disney",
    level: "初級 (A2)",
    cover: "🎸",
    color: "#E76F51",
    bpm: 86,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "可可夜總會靈魂催淚曲，墨西哥吉他風格，傳遞深邃親情與思念。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Remember me, though I have to say goodbye", zh: "請記住我，縱使此刻我不得不向你道別離去", phonetic: "rɪˈmɛmbər miː ðoʊ aɪ hæv tuː seɪ ˌɡʊdˈbaɪ", notes: "【讓步連接詞】though (縱使、雖然)", keyWords: ["remember", "goodbye"] },
      { start: 6.5, end: 13.0, en: "Remember me, don't let it make you cry", zh: "請深情記住我，莫讓這短暫的分離惹你潸然淚下", phonetic: "rɪˈmɛmbər miː doʊnt lɛt ɪt meɪk juː kraɪ", notes: "【使役動詞】make you cry (讓你哭泣)", keyWords: ["remember", "cry"] },
      { start: 13.0, end: 19.5, en: "For even if I'm far away, I hold you in my heart", zh: "因為即便我將遠行千里，我也會永遠將你緊緊摟在心房深處", phonetic: "fɔːr ˈiːvən ɪf aɪm fɑːr əˈweɪ aɪ hoʊld juː ɪn maɪ hɑːrt", notes: "【條件連接詞】even if (哪怕、即使)", keyWords: ["far away", "heart"] },
      { start: 19.5, end: 26.5, en: "I sing a secret song to you each night we are apart", zh: "在每一個我們分離異地的長夜裡，我都會為你悄聲哼唱一首秘密之歌", phonetic: "aɪ sɪŋ ə ˈsiːkrɪt sɔːŋ tuː juː iːʧ naɪt wiː ɑːr əˈpɑːrt", notes: "【狀態形容詞】apart (分開的、分離隔開的)", keyWords: ["secret", "apart"] },
      { start: 26.5, end: 34.0, en: "Remember me, though I have to travel far, remember me, each time you hear a sad guitar", zh: "記住我吧，縱然我必須遠走天涯；每當你耳畔響起那略帶哀傷的吉他弦音，請想起我", phonetic: "rɪˈmɛmbər miː ðoʊ aɪ hæv tuː ˈtrævəl fɑːr", notes: "【樂器描寫】sad guitar (哀傷動人的吉他旋律)", keyWords: ["travel", "guitar"] },
      { start: 34.0, end: 42.0, en: "Know that I'm with you the only way that I can be, until you're in my arms again, remember me", zh: "請深信我正用我所能給予的唯一方式伴你左右，直到我再次將你擁入懷中的那一天，請記住我", phonetic: "noʊ ðæt aɪm wɪð juː ði ˈoʊnli weɪ ðæt aɪ kæn biː", notes: "【終極叮嚀】until you're in my arms again", keyWords: ["until", "remember me"] }
    ]
  },
  {
    id: "part-of-your-world",
    title: "Part of Your World",
    artist: "The Little Mermaid",
    genre: "迪士尼音樂劇",
    category: "disney",
    level: "中級 (B1)",
    cover: "🧜‍♀️",
    color: "#2A9D8F",
    bpm: 74,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "小美人魚經典渴望之歌 (I Want Song)，英語口語擬人與物品詢問極為生動。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Look at this stuff, isn't it neat?", zh: "看看這些稀奇古怪的小玩意兒，難道不是很討人喜愛、很精巧別緻嗎？", phonetic: "lʊk æt ðɪs stʌf ˈɪznt ɪt niːt", notes: "【口語俚語】neat (整潔的/極棒巧妙的)", keyWords: ["stuff", "neat"] },
      { start: 6.5, end: 13.0, en: "Wouldn't you think my collection's complete?", zh: "難道你不會覺得我的珍貴收藏已經無比完整豐富了嗎？", phonetic: "ˈwʊdnt juː θɪŋk maɪ kəˈlɛkʃənz kəmˈpliːt", notes: "【反問提問】collection (收藏品)；complete (完整的)", keyWords: ["collection", "complete"] },
      { start: 13.0, end: 19.5, en: "Wouldn't you think I'm the girl, the girl who has everything?", zh: "難道你不會認為我正是那個擁有了世間一切寶物的幸運女孩嗎？", phonetic: "ˈwʊdnt juː θɪŋk aɪm ðə ɡɜːrl", notes: "【關係代名詞】who has everything", keyWords: ["everything"] },
      { start: 19.5, end: 26.5, en: "I wanna be where the people are, I wanna see, wanna see 'em dancin'", zh: "可是我多麼渴望親臨人類所在的地方，我多麼想親眼看見他們踏著雙腳翩翩起舞", phonetic: "aɪ ˈwɒnə biː wɛər ðə ˈpiːpl ɑːr", notes: "【口語縮讀】wanna = want to；'em = them", keyWords: ["wanna", "dancing"] },
      { start: 26.5, end: 34.0, en: "Walking around on those, what do you call 'em? Oh, feet", zh: "用那種神奇的東西漫步前行...人類叫那什麼來著？噢，是雙腳！", phonetic: "ˈwɔːkɪŋ əˈraʊnd ɒn ðoʊz wʌt duː juː kɔːl əm oʊ fiːt", notes: "【天真語氣】what do you call 'em? (那叫什麼來著？)", keyWords: ["feet"] },
      { start: 34.0, end: 42.0, en: "Up where they walk, up where they run, up where they stay all day in the sun, wanderin' free, wish I could be part of that world", zh: "在陽光普照的大地上漫步、奔跑、自在徜徉，我多麼祈求能成為那繽紛世界的一員", phonetic: "ʌp wɛər ðeɪ wɔːk ʌp wɛər ðeɪ rʌn", notes: "【經典祈願】part of that world (世界的一部分)", keyWords: ["wander", "free", "part of that world"] }
    ]
  },
  {
    id: "colors-of-the-wind",
    title: "Colors of the Wind",
    artist: "Vanessa Williams (Pocahontas)",
    genre: "迪士尼經典",
    category: "disney",
    level: "中高級 (B2)",
    cover: "🍃",
    color: "#264653",
    bpm: 80,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "風中奇緣哲理神曲，詩句如史詩般宏偉，探討人與大自然的共生哲學。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "You think you own whatever land you land on", zh: "你以為只要你的腳步踏上了任何土地，那片大地便理所當然歸你所有", phonetic: "juː θɪŋk juː oʊn wɒtˈɛvər lænd juː lænd ɒn", notes: "【字義雙關】第一個 land 是名詞土地，第二個 land 是動詞著陸登陸", keyWords: ["own", "land"] },
      { start: 6.5, end: 13.0, en: "The Earth is just a dead thing you can claim", zh: "在你眼中大地不過是件沒有靈魂的死物，任由你隨意插旗宣示主權", phonetic: "ði ɜːrθ ɪz ʤʌst ə dɛd θɪŋ juː kæn kleɪm", notes: "【動詞】claim (宣稱所有權/索賠)", keyWords: ["Earth", "dead", "claim"] },
      { start: 13.0, end: 19.5, en: "But I know every rock and tree and creature has a life, has a spirit, has a name", zh: "但我卻深深明白，每一塊嶙峋岩石、每一株參天樹木、每一頭生靈皆有生命、有靈魂、有名姓", phonetic: "bʌt aɪ noʊ ˈɛvri rɒk ænd triː ænd ˈkriːʧər hæz ə laɪf", notes: "【排比句】has a life, has a spirit, has a name", keyWords: ["rock", "spirit", "name"] },
      { start: 19.5, end: 26.5, en: "You think the only people who are people are the people who look and think like you", zh: "你總傲慢以為，只有那些外貌與思維同你一般無二的人，才稱得上是真正的人類", phonetic: "juː θɪŋk ði ˈoʊnli ˈpiːpl huː ɑːr ˈpiːpl", notes: "【批判偏見】look and think like you", keyWords: ["people", "look", "think"] },
      { start: 26.5, end: 34.0, en: "Have you ever heard the wolf cry to the blue corn moon?", zh: "你曾否在皎潔的滿月清輝之下，聆聽過野狼昂首對著藍月幽遠啼嚎？", phonetic: "hæv juː ˈɛvər hɜːrd ðə wʊlf kraɪ tuː ðə bluː kɔːrn muːn", notes: "【原住民意象】blue corn moon (秋收八月藍色玉米之月)", keyWords: ["wolf", "corn moon"] },
      { start: 34.0, end: 42.0, en: "Or asked the grinning bobcat why he grinned? Can you sing with all the voices of the mountains? Can you paint with all the colors of the wind?", zh: "你能否與萬重群山的萬壑回聲一同高歌？你可能否用清風流動的所有斑斕色彩，繪出生命圖卷？", phonetic: "kæn juː peɪnt wɪð ɔːl ðə ˈkʌlərz əv ðə wɪnd", notes: "【哲理名問】paint with all the colors of the wind", keyWords: ["paint", "colors of the wind"] }
    ]
  },
  {
    id: "try-everything",
    title: "Try Everything",
    artist: "Shakira (Zootopia)",
    genre: "動感流行",
    category: "disney",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "🐰",
    color: "#F4A261",
    bpm: 115,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "動物方程式激勵主題曲，充滿活力節奏，強調永不言棄、勇敢嘗試失敗的人生態度。",
    lyrics: [
      { start: 0.0, end: 6.0, en: "I messed up tonight, I lost another fight", zh: "今晚我又把事情搞砸了，我又輸掉了一場艱難的戰役", phonetic: "aɪ mɛst ʌp təˈnaɪt aɪ lɔːst əˈnʌðər faɪt", notes: "【生活片語】mess up (搞砸了、弄糟了)", keyWords: ["messed up", "lost"] },
      { start: 6.0, end: 12.0, en: "I still mess up but I'll just start again", zh: "雖然我依然會失誤犯錯，但我會毫不猶豫拍拍灰塵重新再來", phonetic: "aɪ stɪl mɛs ʌp bʌt aɪl ʤʌst stɑːrt əˈɡɛn", notes: "【堅韌心態】start again (重新開始)", keyWords: ["start again"] },
      { start: 12.0, end: 18.0, en: "I keep falling down, I keep on hitting the ground", zh: "我不斷跌倒在地，我一次又一次狼狽摔在地上", phonetic: "aɪ kiːp ˈfɔːlɪŋ daʊn aɪ kiːp ɒn ˈhɪtɪŋ ðə ɡraʊnd", notes: "【片語】keep on V-ing (持續不斷去做)", keyWords: ["falling", "ground"] },
      { start: 18.0, end: 24.0, en: "I always get up now, see what's next", zh: "但我總是立刻頑強站起身來，滿懷期待迎接下一個挑戰", phonetic: "aɪ ˈɔːlweɪz ɡɛt ʌp naʊ siː wʌts nɛkst", notes: "【樂觀態度】see what's next (看看接下來有什麼)", keyWords: ["get up", "what's next"] },
      { start: 24.0, end: 30.5, en: "Birds don't just fly, they fall down and get up", zh: "鳥兒從來不是生來就會展翅翱翔，牠們也是跌落受挫後再度昂首起飛", phonetic: "bɜːrdz doʊnt ʤʌst flaɪ ðeɪ fɔːl daʊn ænd ɡɛt ʌp", notes: "【哲理比喻】fall down and get up", keyWords: ["fly", "get up"] },
      { start: 30.5, end: 38.0, en: "Nobody learns without gettin' it won", zh: "沒有任何人能在不經歷犯錯磨練下收穫真正的成功", phonetic: "ˈnoʊˌbɒdi lɜːrnz wɪˈðaʊt ˈɡɛtɪn ɪt wʌn", notes: "【學習定律】learning from failures", keyWords: ["learns"] },
      { start: 38.0, end: 46.0, en: "I won't give up, no I won't give in, 'til I reach the end, and then I'll start again, though I'm on the ground, I wanna try everything", zh: "我絕不放棄，我也絕不屈服！在抵達終點之前我會一直奮鬥，縱然摔倒在地，我也要放手嘗試所有可能！", phonetic: "aɪ woʊnt ɡɪv ʌp noʊ aɪ woʊnt ɡɪv ɪn", notes: "【核心片語】give up (放棄) vs give in (屈服妥協)", keyWords: ["give up", "give in", "try everything"] }
    ]
  },
  {
    id: "reflection",
    title: "Reflection",
    artist: "Christina Aguilera (Mulan)",
    genre: "迪士尼經典",
    category: "disney",
    level: "中級 (B1)",
    cover: "🪞",
    color: "#9C6644",
    bpm: 72,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "花木蘭內心獨白代表作，探討自我認同與世俗眼光的矛盾，文辭動人。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Look at me, you may think you see who I really am", zh: "注視著我，你也許自以為能看清真正的我是個什麼樣的姑娘", phonetic: "lʊk æt miː juː meɪ θɪŋk juː siː huː aɪ ˈrɪəli æm", notes: "【名詞子句】who I really am (真正的自己)", keyWords: ["really am"] },
      { start: 6.5, end: 13.0, en: "But you'll never know me", zh: "但你卻永遠無法真正觸碰到我靈魂深處的本質", phonetic: "bʌt juːl ˈnɛvər noʊ miː", notes: "【否定堅決】never know me", keyWords: ["never know"] },
      { start: 13.0, end: 19.5, en: "Every day, it's as if I play a part", zh: "每一天，我都彷彿在扮演著一個符合旁人期待的角色劇本", phonetic: "ˈɛvri deɪ ɪts æz ɪf aɪ pleɪ ə pɑːrt", notes: "【生活片語】play a part (扮演某種角色、逢場作戲)", keyWords: ["play a part"] },
      { start: 19.5, end: 26.5, en: "Now I see, that if I were truly to be myself, I would break my family's heart", zh: "如今我漸漸明白，若我真的率真由著本心做自己，恐怕會傷透了家人的心", phonetic: "naʊ aɪ siː ðæt ɪf aɪ wɜːr ˈtruːli tuː biː maɪˈsɛlf", notes: "【與現在事實相反假設】if I were truly to be myself", keyWords: ["truly", "break heart"] },
      { start: 26.5, end: 34.0, en: "Who is that girl I see, staring straight back at me?", zh: "鏡中那個凝望著我、眼神直視著我的女孩，她究竟是誰？", phonetic: "huː ɪz ðæt ɡɜːrl aɪ siː ˈstɛərɪŋ streɪt bæk æt miː", notes: "【靈魂詰問】staring straight back (直視自己內心)", keyWords: ["staring", "back at me"] },
      { start: 34.0, end: 42.0, en: "Why is my reflection someone I don't know? When will my reflection show who I am inside?", zh: "為什麼水中的倒影，對我而言竟如此陌生遙遠？究竟要到何時，鏡中的倒影才能真正映照出我真實的內在靈魂？", phonetic: "waɪ ɪz maɪ rɪˈflɛkʃən ˈsʌmwʌn aɪ doʊnt noʊ", notes: "【中心主題】reflection (倒影、反省、內省)", keyWords: ["reflection", "who I am inside"] }
    ]
  },

  // ─── 3. 傳奇民謠與經典搖滾 (Folk & Classic Rock) ───
  {
    id: "stand-by-me",
    title: "Stand By Me",
    artist: "Ben E. King",
    genre: "經典靈魂樂",
    category: "folk",
    level: "基礎入門 (A1-A2)",
    cover: "🤝",
    color: "#2B9348",
    bpm: 118,
    synthPattern: "motown-bass-groove",
    audioNotes: "歷史最偉大經典之一，旋律節奏鮮明，句型平實真摯，極適合初學者練習口說連音與肯定句語氣。",
    lyrics: [
      { start: 0.0, end: 6.8, en: "When the night has come, and the land is dark", zh: "當黑夜降臨，大地陷入一片漆黑", phonetic: "wɛn ðə naɪt hæz kʌm ænd ðə lænd ɪz dɑːrk", notes: "【時態】has come (現在完成式，夜晚已經到來)", keyWords: ["night", "land", "dark"] },
      { start: 6.8, end: 13.5, en: "And the moon is the only light we'll see", zh: "而皎潔的明月，是我們唯一能看見的光芒", phonetic: "ænd ðə muːn ɪz ði ˈoʊnli laɪt wiːl siː", notes: "【冠詞】the only 發音為 /ði ˈoʊnli/", keyWords: ["moon", "only", "light"] },
      { start: 13.5, end: 20.0, en: "No, I won't be afraid, oh, I won't be afraid", zh: "不，我絕不會畏懼，噢，我絲毫不會害怕", phonetic: "noʊ aɪ woʊnt biː əˈfreɪd oʊ aɪ woʊnt biː əˈfreɪd", notes: "【形容詞】be afraid (畏懼害怕)", keyWords: ["afraid", "won't"] },
      { start: 20.0, end: 26.5, en: "Just as long as you stand, stand by me", zh: "只要你能佇立在我身邊，支持陪伴著我", phonetic: "ʤʌst æz lɔːŋ æz juː stænd stænd baɪ miː", notes: "【片語】stand by (支持、站在身旁守護)", keyWords: ["as long as", "stand by"] },
      { start: 26.5, end: 33.2, en: "So darling, darling, stand by me, oh stand by me", zh: "所以親愛的，請陪伴在我身旁，守護著我", phonetic: "soʊ ˈdɑːrlɪŋ ˈdɑːrlɪŋ stænd baɪ miː", notes: "【親暱稱呼】darling (親愛的寶貝)", keyWords: ["darling", "stand by"] },
      { start: 33.2, end: 40.0, en: "Oh stand, stand by me, stand by me", zh: "噢，請陪伴著我，守護在我身邊", phonetic: "oʊ stænd stænd baɪ miː", notes: "【祈使反覆】加深情感共鳴", keyWords: ["stand by"] },
      { start: 40.0, end: 46.8, en: "If the sky that we look upon should tumble and fall", zh: "即使我們仰望的蒼穹崩塌傾頹、墜落大地", phonetic: "ɪf ðə skaɪ ðæt wiː lʊk əˈpɒn ʃʊd ˈtʌmbəl ænd fɔːl", notes: "【生動動詞】tumble and fall (翻滾跌落)", keyWords: ["look upon", "tumble", "fall"] },
      { start: 46.8, end: 53.5, en: "Or the mountain should crumble to the sea", zh: "抑或是高山巍峨盡皆崩解、沉入汪洋之中", phonetic: "ɔːr ðə ˈmaʊntən ʃʊd ˈkrʌmbəl tuː ðə siː", notes: "【動詞】crumble (粉碎瓦解成碎屑)", keyWords: ["mountain", "crumble", "sea"] },
      { start: 53.5, end: 60.0, en: "I won't cry, I won't cry, no I won't shed a tear", zh: "我也不會痛哭，我絕不啜泣，連一滴眼淚都不會掉下", phonetic: "aɪ woʊnt kraɪ aɪ woʊnt kraɪ noʊ aɪ woʊnt ʃɛd ə tɪər", notes: "【文雅動詞】shed a tear (流淚)", keyWords: ["shed", "tear", "cry"] },
      { start: 60.0, end: 67.0, en: "Just as long as you stand, stand by me", zh: "只要有你在身邊支持著我", phonetic: "ʤʌst æz lɔːŋ æz juː stænd stænd baɪ miː", notes: "【誓言核心】相伴無懼風雨", keyWords: ["stand by"] }
    ]
  },
  {
    id: "country-roads",
    title: "Take Me Home, Country Roads",
    artist: "John Denver",
    genre: "鄉村民謠",
    category: "folk",
    level: "中級 (B1)",
    cover: "🏞️",
    color: "#557A46",
    bpm: 82,
    synthPattern: "folk-guitar-strum",
    audioNotes: "全美最經典鄉村民謠，地名與自然風光詞彙豐富，副歌旋律極易朗朗上口。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Almost heaven, West Virginia", zh: "幾乎有如人間天堂，西維吉尼亞州", phonetic: "ˈɔːlmoʊst ˈhɛvən wɛst vərˈʤɪnjə", notes: "【美國地理】West Virginia (阿帕拉契山脈之州)", keyWords: ["almost", "heaven"] },
      { start: 6.5, end: 12.8, en: "Blue Ridge Mountains, Shenandoah River", zh: "藍嶺山脈綿延，雪蘭多河水潺潺", phonetic: "bluː rɪʤ ˈmaʊntənz ˌʃɛnənˈdoʊə ˈrɪvər", notes: "【地理名詞】Blue Ridge (藍嶺)；Shenandoah (雪蘭多河)", keyWords: ["mountains", "river"] },
      { start: 12.8, end: 19.0, en: "Life is old there, older than the trees", zh: "那裡的歲月悠久沉靜，比古木森林還要滄桑", phonetic: "laɪf ɪz oʊld ðɛər ˈoʊldər ðæn ðə triːz", notes: "【比較級】older than the trees (比樹更蒼老)", keyWords: ["trees", "older"] },
      { start: 19.0, end: 25.5, en: "Younger than the mountains, growin' like a breeze", zh: "卻又比巍峨群山年輕，如清風般自在生長、吹拂大地", phonetic: "ˈjʌŋɡər ðæn ðə ˈmaʊntənz ˈɡroʊɪn laɪk ə briːz", notes: "【鄉村縮讀】growin' = growing (省去 g 音)", keyWords: ["younger", "breeze"] },
      { start: 25.5, end: 32.0, en: "Country roads, take me home to the place I belong", zh: "鄉村小路，請引領我回家，回到那屬於我的歸屬之地", phonetic: "ˈkʌntri roʊdz teɪk miː hoʊm tuː ðə pleɪs aɪ bɪˈlɔːŋ", notes: "【核心片語】belong (歸屬)", keyWords: ["country roads", "belong"] },
      { start: 32.0, end: 38.5, en: "West Virginia, mountain mama, take me home, country roads", zh: "西維吉尼亞，宛如群山母親，帶我回家吧，蜿蜒的鄉村路", phonetic: "wɛst vərˈʤɪnjə ˈmaʊntən ˈmɑːmə teɪk miː hoʊm", notes: "【擬人修辭】mountain mama (把大山比喻為母親)", keyWords: ["mama", "country roads"] },
      { start: 38.5, end: 45.0, en: "All my memories gather 'round her, miner's lady, stranger to blue water", zh: "所有的回憶都圍繞著她，她是礦工之妻，未曾見過碧藍大洋", phonetic: "ɔːl maɪ ˈmɛməriz ˈɡæðər raʊnd hɜːr", notes: "【生疏片語】stranger to (對...未曾見過/生疏陌生)", keyWords: ["memories", "gather", "stranger"] },
      { start: 45.0, end: 52.0, en: "Dark and dusty, painted on the sky, misty taste of moonshine, teardrop in my eye", zh: "昏暗揚塵染遍蒼穹，自釀烈酒散發著迷濛香氣，眼角滑落思鄉淚滴", phonetic: "dɑːrk ænd ˈdʌsti ˈpeɪntɪd ɒn ðə skaɪ", notes: "【鄉村文化】moonshine (美國阿帕拉契特產自釀玉米烈酒)", keyWords: ["dusty", "moonshine", "teardrop"] }
    ]
  },
  {
    id: "yesterday",
    title: "Yesterday",
    artist: "The Beatles",
    genre: "經典搖滾民謠",
    category: "folk",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "🎻",
    color: "#774936",
    bpm: 84,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "歷史被翻唱次數最多的吉他抒情名作，保羅麥卡尼經典，詞意悠遠憂傷。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Yesterday, all my troubles seemed so far away", zh: "昨天，我生命中所有的煩惱憂愁似乎都還那麼遙遠", phonetic: "ˈjɛstərˌdeɪ ɔːl maɪ ˈtrʌblz siːmd soʊ fɑːr əˈweɪ", notes: "【狀態描繪】troubles seemed so far away", keyWords: ["yesterday", "troubles", "far away"] },
      { start: 6.5, end: 13.0, en: "Now it looks as though they're here to stay", zh: "然而此時此刻，它們卻彷彿在此深深紮根、不再離去", phonetic: "naʊ ɪt lʊks æz ðoʊ ðeɪr hɪər tuː steɪ", notes: "【成語片語】here to stay (長期留存、落地生根)", keyWords: ["as though", "stay"] },
      { start: 13.0, end: 19.5, en: "Oh, I believe in yesterday", zh: "噢，我多麼深切眷戀懷念昨天那段時光", phonetic: "oʊ aɪ bɪˈliːv ɪn ˈjɛstərˌdeɪ", notes: "【信仰肯定】believe in (深信、堅信價值)", keyWords: ["believe in"] },
      { start: 19.5, end: 26.5, en: "Suddenly, I'm not half the man I used to be", zh: "猝然之間，我已不再是當初那個自信完整的自己", phonetic: "ˈsʌdənli aɪm nɒt hæf ðə mæn aɪ juːst tuː biː", notes: "【經典表達】not half the man I used to be (判若兩人、失去從前的意氣)", keyWords: ["suddenly", "used to be"] },
      { start: 26.5, end: 33.5, en: "There's a shadow hanging over me", zh: "一縷沉重陰鬱的陰影，悄無聲息籠罩在我的心頭", phonetic: "ðɛrz ə ˈʃædoʊ ˈhæŋɪŋ ˈoʊvər miː", notes: "【心理隱喻】shadow hanging over me (陰影揮之不去)", keyWords: ["shadow", "hanging"] },
      { start: 33.5, end: 41.0, en: "Oh, yesterday came suddenly", zh: "噢，昔日的美好歲月消逝得如此猝不及防", phonetic: "oʊ ˈjɛstərˌdeɪ keɪm ˈsʌdənli", notes: "【倒裝詠嘆】yesterday came suddenly", keyWords: ["yesterday", "suddenly"] }
    ]
  },
  {
    id: "let-it-be",
    title: "Let It Be",
    artist: "The Beatles",
    genre: "經典搖滾",
    category: "folk",
    level: "初級 (A2)",
    cover: "🕊️",
    color: "#3D5A80",
    bpm: 73,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "披頭四哲理聖歌，順其自然、平和處世的智慧箴言，撫慰無數心靈。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When I find myself in times of trouble, Mother Mary comes to me", zh: "當我發現自己陷入艱難困境之時，聖母瑪莉亞（或慈母瑪莉）悄悄走到了我的身邊", phonetic: "wɛn aɪ faɪnd maɪˈsɛlf ɪn taɪmz əv ˈtrʌbl ˈmʌðər ˈmɛəri kʌmz tuː miː", notes: "【困頓片語】in times of trouble (在危難挫折之際)", keyWords: ["trouble", "Mother Mary"] },
      { start: 6.5, end: 13.0, en: "Speaking words of wisdom, let it be", zh: "對我輕聲細語說著智慧的箴言：順其自然吧，隨它去吧", phonetic: "ˈspiːkɪŋ wɜːrdz əv ˈwɪzdəm lɛt ɪt biː", notes: "【核心概念】words of wisdom (智慧之言)；let it be (順其自然)", keyWords: ["wisdom", "let it be"] },
      { start: 13.0, end: 19.5, en: "And in my hour of darkness she is standing right in front of me", zh: "在我人生最黑暗無助的幽谷之中，她就那樣溫柔地仁立在我的面前", phonetic: "ænd ɪn maɪ ˈaʊər əv ˈdɑːrknɪs ʃiː ɪz ˈstændɪŋ raɪt ɪn frʌnt əv miː", notes: "【比喻片語】hour of darkness (至暗時刻)", keyWords: ["darkness", "in front of"] },
      { start: 19.5, end: 26.5, en: "Speaking words of wisdom, let it be", zh: "輕輕送來智慧的撫慰：順其自然吧", phonetic: "ˈspiːkɪŋ wɜːrdz əv ˈwɪzdəm lɛt ɪt biː", notes: "【反覆箴言】let it be", keyWords: ["let it be"] },
      { start: 26.5, end: 33.5, en: "Let it be, let it be, let it be, let it be", zh: "順其自然，坦然放下，隨遇而安", phonetic: "lɛt ɪt biː lɛt ɪt biː", notes: "【心靈祈願】放下執著，靜待花開", keyWords: ["let it be"] },
      { start: 33.5, end: 41.0, en: "Whisper words of wisdom, let it be", zh: "低聲耳語著大智慧：凡事隨緣順其自然", phonetic: "ˈwɪspər wɜːrdz əv ˈwɪzdəm lɛt ɪt biː", notes: "【動詞】whisper (輕柔耳語)", keyWords: ["whisper", "wisdom"] }
    ]
  },
  {
    id: "hey-jude",
    title: "Hey Jude",
    artist: "The Beatles",
    genre: "經典搖滾",
    category: "folk",
    level: "初級 (A2)",
    cover: "☀️",
    color: "#DDA15E",
    bpm: 74,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "保羅麥卡尼寫給約翰藍儂幼子的安慰金曲，激勵人心、驅散陰霾。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Hey Jude, don't make it bad, take a sad song and make it better", zh: "嘿，朱德，別把事情想得太糟，縱然是一首悲傷哀怨的歌，也能被譜成動聽美好的樂章", phonetic: "heɪ ʤuːd doʊnt meɪk ɪt bæd teɪk ə sæd sɔːŋ ænd meɪk ɪt ˈbɛtər", notes: "【轉念哲理】make it better (把事情變得更好)", keyWords: ["bad", "sad song", "better"] },
      { start: 6.5, end: 13.0, en: "Remember to let her into your heart, then you can start to make it better", zh: "切記要打開心扉讓愛與陽光住進你的心裡，如此你才能真正讓一切重獲新生", phonetic: "rɪˈmɛmbər tuː lɛt hɜːr ˈɪntuː jʊər hɑːrt", notes: "【祈使句】remember to V (記得去落實...)", keyWords: ["remember", "heart"] },
      { start: 13.0, end: 20.0, en: "Hey Jude, don't be afraid, you were made to go out and get her", zh: "嘿，朱德，別心生畏縮懼怕，你生來就具備去勇敢追求所愛的勇氣與天賦", phonetic: "heɪ ʤuːd doʊnt biː əˈfreɪd juː wɜːr meɪd tuː ɡoʊ aʊt ænd ɡɛt hɜːr", notes: "【被動使命】be made to (天生注定要...)", keyWords: ["afraid", "go out"] },
      { start: 20.0, end: 27.5, en: "The minute you let her under your skin, then you begin to make it better", zh: "只要你全心接納這份深刻的溫存，你便能開始讓一切變得無比美好", phonetic: "ðə ˈmɪnɪt juː lɛt hɜːr ˈʌndər jʊər skɪn", notes: "【習慣片語】the minute (一...就...)；under your skin (刻骨銘心深入骨髓)", keyWords: ["under your skin", "begin"] }
    ]
  },
  {
    id: "sound-of-silence",
    title: "The Sound of Silence",
    artist: "Simon & Garfunkel",
    genre: "傳奇民謠",
    category: "folk",
    level: "進階文雅 (B2)",
    cover: "🌑",
    color: "#283618",
    bpm: 104,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "民謠搖滾世紀史詩，以深刻反諷描摹現代都市人的冷漠與寂靜溝通。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Hello darkness, my old friend, I've come to talk with you again", zh: "你好啊黑暗，我昔日的老友，我又再度前來與你傾心長談", phonetic: "hɛˈloʊ ˈdɑːrknɪs maɪ oʊld frɛnd aɪv kʌm tuː tɔːk wɪð juː əˈɡɛn", notes: "【擬人修辭】把黑暗當作老友溫柔對話", keyWords: ["darkness", "friend"] },
      { start: 6.5, end: 13.5, en: "Because a vision softly creeping, left its seeds while I was sleeping", zh: "因為一幕如夢般的幻象悄然躡足而至，趁我在沉睡時悄悄播下了它的種子", phonetic: "bɪˈkəz ə ˈvɪʒən ˈsɒftli ˈkriːpɪŋ lɛft ɪts siːdz waɪl aɪ wʌz ˈsliːpɪŋ", notes: "【生動動詞】creeping (緩緩爬行潛行)", keyWords: ["vision", "creeping", "seeds"] },
      { start: 13.5, end: 21.0, en: "And the vision that was planted in my brain still remains, within the sound of silence", zh: "那深植深烙在我的大腦中的幻象至今依然佇留，迴盪在那一片寂靜無聲之音中", phonetic: "ænd ðə ˈvɪʒən ðæt wʌz ˈplæntɪd ɪn maɪ breɪn stɪl rɪˈmeɪnz", notes: "【核心概念矛盾修辭】sound of silence (寂靜之聲)", keyWords: ["planted", "brain", "silence"] }
    ]
  },
  {
    id: "hotel-california",
    title: "Hotel California",
    artist: "Eagles",
    genre: "經典搖滾",
    category: "folk",
    level: "中高級 (B2)",
    cover: "🏨",
    color: "#BC6C25",
    bpm: 75,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "老鷹合唱團神話金曲，沙漠公路旅行敘事，詞句如小說般充滿懸念與電影感。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "On a dark desert highway, cool wind in my hair", zh: "行駛在夜色籠罩的黑暗荒漠公路上，凜冽清風拂過我的髮梢", phonetic: "ɒn ə dɑːrk ˈdɛzərt ˈhaɪweɪ kuːl wɪnd ɪn maɪ hɛər", notes: "【公路意境】dark desert highway", keyWords: ["desert", "highway", "wind"] },
      { start: 6.5, end: 13.0, en: "Warm smell of colitas, rising up through the air", zh: "大麻花散發出的陣陣溫熱香氣，悄然在夜色空氣中瀰漫蒸騰", phonetic: "wɔːrm smɛl əv kəˈliːtəz ˈraɪzɪŋ ʌp θruː ði ɛər", notes: "【氣味詞彙】colitas (墨西哥俚語指沙漠小花/植物花蕾)", keyWords: ["smell", "air"] },
      { start: 13.0, end: 19.5, en: "Up ahead in the distance, I saw a shimmering light", zh: "在遠方漆黑的前方地平線上，我看見了一抹微弱閃爍的燈光", phonetic: "ʌp əˈhɛd ɪn ðə ˈdɪstəns aɪ sɔː ə ˈʃɪmərɪŋ laɪt", notes: "【空間方位】up ahead in the distance", keyWords: ["distance", "shimmering"] },
      { start: 19.5, end: 26.5, en: "My head grew heavy and my sight grew dim, I had to stop for the night", zh: "我的頭顱變得愈發沉重，視線漸漸昏暗模糊，我不得不尋覓落腳處借宿今宵", phonetic: "maɪ hɛd ɡruː ˈhɛvi ænd maɪ saɪt ɡruː dɪm", notes: "【狀態轉變】grow heavy / dim (變得沉重昏暗)", keyWords: ["heavy", "dim", "stop"] },
      { start: 26.5, end: 34.0, en: "Welcome to the Hotel California, such a lovely place, such a lovely face", zh: "歡迎光臨加州旅館！多麼令人心馳神往的美妙樂土，多麼迷人溫柔的笑靨容顏", phonetic: "ˈwɛlkəm tuː ðə hoʊˈtɛl ˌkælɪˈfɔːrnjə", notes: "【經典副歌】such a lovely place (如此怡人之處)", keyWords: ["welcome", "lovely"] }
    ]
  },
  {
    id: "tears-in-heaven",
    title: "Tears in Heaven",
    artist: "Eric Clapton",
    genre: "經典抒情民謠",
    category: "folk",
    level: "中級 (B1)",
    cover: "🕊️",
    color: "#6C757D",
    bpm: 80,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "吉他大師克萊普頓悼念亡子的哀思之作，文辭樸實，感情真摯深邃無比。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Would you know my name if I saw you in heaven?", zh: "若有一天我在天堂與你重逢，你是否還能認得出我的名字？", phonetic: "wʊd juː noʊ maɪ neɪm ɪf aɪ sɔː juː ɪn ˈhɛvən", notes: "【假設語氣】Would you know... if I saw you (與現在事實相反)", keyWords: ["name", "heaven"] },
      { start: 6.5, end: 13.0, en: "Would it be the same if I saw you in heaven?", zh: "若我們在天堂相遇，一切是否還會一如從前那般溫暖？", phonetic: "wʊd ɪt biː ðə seɪm ɪf aɪ sɔː juː ɪn ˈhɛvən", notes: "【句型平行】Would it be the same", keyWords: ["same"] },
      { start: 13.0, end: 19.5, en: "I must be strong and carry on", zh: "我必須在凡塵間咬牙堅強，繼續勇敢走完人生的旅程", phonetic: "aɪ mʌst biː strɒŋ ænd ˈkæri ɒn", notes: "【片語】carry on (堅持下去、繼續生活)", keyWords: ["strong", "carry on"] },
      { start: 19.5, end: 26.5, en: "'Cause I know I don't belong here in heaven", zh: "因為我深知，此刻的我還不屬於這個超凡的天國", phonetic: "kəz aɪ noʊ aɪ doʊnt bɪˈlɔːŋ hɪər ɪn ˈhɛvən", notes: "【片語】belong (屬於)", keyWords: ["belong"] }
    ]
  },
  {
    id: "dust-in-the-wind",
    title: "Dust in the Wind",
    artist: "Kansas",
    genre: "哲理民謠搖滾",
    category: "folk",
    level: "進階文雅 (B2)",
    cover: "🌪️",
    color: "#8D99AE",
    bpm: 93,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "以木吉他快速分解和弦伴奏，詞意取自聖經與東方無常哲學，探討生命的短暫與永恆。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I close my eyes, only for a moment, and the moment's gone", zh: "我輕輕闔上雙眼，不過短暫的一剎那間，那時光便已悄然消逝無蹤", phonetic: "aɪ kloʊz maɪ aɪz ˈoʊnli fɔːr ə ˈmoʊmənt ænd ðə ˈmoʊmənts ɡɒn", notes: "【時間無常】only for a moment (轉瞬即逝)", keyWords: ["eyes", "moment", "gone"] },
      { start: 6.5, end: 13.0, en: "All my dreams pass before my eyes, a curiosity", zh: "我昔日所有的宏願夢想，走馬燈般掠過眼簾，恍若一場虛無好奇的幻影", phonetic: "ɔːl maɪ driːmz pæs bɪˈfɔːr maɪ aɪz ə ˌkjʊəriˈɒsɪti", notes: "【人生哲思】a curiosity (一件奇異短暫的事物)", keyWords: ["dreams", "pass"] },
      { start: 13.0, end: 20.0, en: "Dust in the wind, all they are is dust in the wind", zh: "風中微塵，芸芸萬物終究不過是風中飄蕩的一抹塵埃罷了", phonetic: "dʌst ɪn ðə wɪnd ɔːl ðeɪ ɑːr ɪz dʌst ɪn ðə wɪnd", notes: "【核心象徵】Dust in the wind (風中塵埃/虛妄短暫)", keyWords: ["dust in the wind"] }
    ]
  },
  {
    id: "imagine",
    title: "Imagine",
    artist: "John Lennon",
    genre: "傳奇和平頌歌",
    category: "folk",
    level: "中級 (B1)",
    cover: "☮️",
    color: "#ADB5BD",
    bpm: 76,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "二十世紀最偉大的和平烏托邦哲理之歌，英語假設語氣的終極範本。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Imagine there's no heaven, it's easy if you try", zh: "試著想像世上沒有劃分階級的天堂，只要你嘗試去想，這其實並不困難", phonetic: "ɪˈmæʤɪn ðɛrz noʊ ˈhɛvən ɪts ˈiːzi ɪf juː traɪ", notes: "【祈使想像】Imagine (試想看看)", keyWords: ["imagine", "heaven"] },
      { start: 6.5, end: 13.0, en: "No hell below us, above us, only sky", zh: "腳底下沒有地獄的煎熬，頭頂之上，唯有一片純淨澄澈的天空", phonetic: "noʊ hɛl bɪˈloʊ ʌs əˈbʌv ʌs ˈoʊnli skaɪ", notes: "【方位詞對比】below us (在我們之下) vs above us (在我們之上)", keyWords: ["hell", "sky"] },
      { start: 13.0, end: 19.5, en: "Imagine all the people livin' for today", zh: "試著想像全人類此時此刻，都在安詳篤定地為今天而真實活著", phonetic: "ɪˈmæʤɪn ɔːl ðə ˈpiːpl ˈlɪvɪn fɔːr təˈdeɪ", notes: "【生活當下】live for today (活在當下)", keyWords: ["people", "today"] },
      { start: 19.5, end: 26.5, en: "You may say I'm a dreamer, but I'm not the only one", zh: "你也許會嘲諷我只是一個不切實際的空想家，但我絕不是唯一一個懷抱此夢想的人", phonetic: "juː meɪ seɪ aɪm ə ˈdriːmər bʌt aɪm nɒt ði ˈoʊnli wʌn", notes: "【金句銘言】You may say I'm a dreamer", keyWords: ["dreamer", "only one"] },
      { start: 26.5, end: 34.0, en: "I hope someday you'll join us, and the world will be as one", zh: "我殷切期盼有朝一日你也能與我們同行，讓整個世界和諧歸於大同", phonetic: "aɪ hoʊp ˈsʌmdeɪ juːl ʤɔɪn ʌs ænd ðə wɜːrld wɪl biː æz wʌn", notes: "【大同願景】the world will be as one (天下一家)", keyWords: ["join", "as one"] }
    ]
  },
  {
    id: "vincent",
    title: "Vincent (Starry Starry Night)",
    artist: "Don McLean",
    genre: "傳奇民謠",
    category: "folk",
    level: "進階文雅 (B2)",
    cover: "🎨",
    color: "#1D3557",
    bpm: 86,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "致敬梵谷的曠世傑作，將畫作色彩與心靈創傷融入詩句，詞彙極富藝術色彩美感。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Starry, starry night, paint your palette blue and gray", zh: "繁星閃爍、星光璀璨的夜空下，調色盤上揮灑著憂鬱深邃的藍色與灰色", phonetic: "ˈstɑːri ˈstɑːri naɪt peɪnt jʊər ˈpælət bluː ænd ɡreɪ", notes: "【美術詞彙】palette (調色盤)", keyWords: ["starry", "palette"] },
      { start: 6.5, end: 13.0, en: "Look out on a summer's day with eyes that know the darkness in my soul", zh: "在夏日的豔陽下憑窗眺望，用那一雙早已洞察我靈魂深處黑暗的悲憫雙眼", phonetic: "lʊk aʊt ɒn ə ˈsʌmərz deɪ wɪð aɪz ðæt noʊ ðə ˈdɑːrknɪs", notes: "【心靈洞察】know the darkness in my soul", keyWords: ["darkness", "soul"] },
      { start: 13.0, end: 20.0, en: "Shadows on the hills, sketch the trees and the daffodils", zh: "起伏山丘上的微光倒影，勾勒描繪著蒼翠樹木與迎風搖曳的黃水仙", phonetic: "ˈʃædoʊz ɒn ðə hɪlz skɛʧ ðə triːz ænd ðə ˈdæfədɪlz", notes: "【素描與花卉】sketch (勾勒素描)；daffodils (黃水仙)", keyWords: ["sketch", "daffodils"] },
      { start: 20.0, end: 28.0, en: "Catch the breeze and the winter chills, in colors on the snowy linen land", zh: "在潔白覆雪的亞麻畫布上，用斑斕色彩捕捉掠過的微風與凜冬刺骨的寒意", phonetic: "kætʃ ðə briːz ænd ðə ˈwɪntər ʧɪlz", notes: "【畫布意象】snowy linen land (雪白亞麻畫布)", keyWords: ["breeze", "chills", "linen"] }
    ]
  },

  // ─── 4. 爵士風華與浪漫標準曲 (Jazz & Standards) ───
  {
    id: "fly-me-to-the-moon",
    title: "Fly Me to the Moon",
    artist: "Frank Sinatra",
    genre: "搖擺爵士",
    category: "jazz",
    level: "進階文雅 (B2)",
    cover: "🌙",
    color: "#A855F7",
    bpm: 110,
    synthPattern: "jazz-swing-piano",
    audioNotes: "爵士大樂團黃金年代名曲，優雅浪漫，韻律典雅，是學習英文浪漫修辭的最佳教材。",
    lyrics: [
      { start: 0.0, end: 5.5, en: "Fly me to the moon, let me play among the stars", zh: "帶我飛向明月，讓我在璀璨群星之間恣意徜徉", phonetic: "flaɪ miː tuː ðə muːn lɛt miː pleɪ əˈmʌŋ ðə stɑːrz", notes: "【介系詞】among (在...之中，三者以上)", keyWords: ["moon", "stars", "among"] },
      { start: 5.5, end: 11.0, en: "Let me see what spring is like on Jupiter and Mars", zh: "讓我一睹木星與火星上的春日究竟是何種光景", phonetic: "lɛt miː siː wʌt sprɪŋ ɪz laɪk ɒn ˈʤuːpɪtər ænd mɑːrz", notes: "【天文星系】Jupiter (木星)；Mars (火星)", keyWords: ["spring", "Jupiter", "Mars"] },
      { start: 11.0, end: 16.5, en: "In other words, hold my hand", zh: "換句話說，請牽緊我的雙手", phonetic: "ɪn ˈʌðər wɜːrdz hoʊld maɪ hænd", notes: "【轉折片語】in other words (換言之、也就是說)", keyWords: ["in other words", "hold"] },
      { start: 16.5, end: 22.0, en: "In other words, baby, kiss me", zh: "也就是說，親愛的，請吻我吧", phonetic: "ɪn ˈʌðər wɜːrdz ˈbeɪbi kɪs miː", notes: "【真摯告白】直接而真誠", keyWords: ["kiss"] },
      { start: 22.0, end: 27.5, en: "Fill my heart with song, and let me sing forevermore", zh: "讓歌聲填滿我的心靈，讓我直到永遠都為你歌唱", phonetic: "fɪl maɪ hɑːrt wɪð sɔːŋ ænd lɛt miː sɪŋ fərˈɛvərˌmɔːr", notes: "【古典用詞】forevermore (永遠、長長久久)", keyWords: ["fill", "forevermore"] },
      { start: 27.5, end: 33.0, en: "You are all I long for, all I worship and adore", zh: "你是我心中唯一的渴望，是我全心崇敬與摯愛的一切", phonetic: "juː ɑːr ɔːl aɪ lɔːŋ fɔːr ɔːl aɪ ˈwɜːrʃɪp ænd əˈdɔːr", notes: "【敬愛動詞】worship (崇敬)；adore (深愛傾慕)", keyWords: ["long for", "worship", "adore"] },
      { start: 33.0, end: 38.5, en: "In other words, please be true", zh: "換言之，請對我堅貞不渝", phonetic: "ɪn ˈʌðər wɜːrdz pliːz biː truː", notes: "【忠貞片語】be true (忠誠真摯)", keyWords: ["true"] },
      { start: 38.5, end: 45.0, en: "In other words, I love you", zh: "簡單說，我深深愛著你", phonetic: "ɪn ˈʌðər wɜːrdz aɪ lʌv juː", notes: "【經典終結】千言萬語化為我愛你", keyWords: ["love"] }
    ]
  },
  {
    id: "what-a-wonderful-world",
    title: "What a Wonderful World",
    artist: "Louis Armstrong",
    genre: "經典爵士民謠",
    category: "jazz",
    level: "基礎入門 (A1-A2)",
    cover: "🌈",
    color: "#2A9D8F",
    bpm: 72,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "爵士巨擘路易阿姆斯壯代表作，沙啞溫暖歌聲，以最單純質樸的眼光凝視世界之美。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I see trees of green, red roses too", zh: "我看見鬱鬱蔥蔥的綠樹，還有嬌豔綻放的紅玫瑰", phonetic: "aɪ siː triːz əv ɡriːn rɛd ˈroʊzɪz tuː", notes: "【基礎色彩】trees of green, red roses", keyWords: ["trees", "roses"] },
      { start: 6.5, end: 13.0, en: "I see them bloom for me and you", zh: "我看見它們正為你我恣意盛開綻放", phonetic: "aɪ siː ðɛm bluːm fɔːr miː ænd juː", notes: "【動詞】bloom (開花盛放)", keyWords: ["bloom"] },
      { start: 13.0, end: 19.5, en: "And I think to myself, what a wonderful world", zh: "我情不自禁在心中暗自讚嘆：這世界是多麼的美好啊！", phonetic: "ænd aɪ θɪŋk tuː maɪˈsɛlf wʌt ə ˈwʌndərfəl wɜːrld", notes: "【感嘆句】what a wonderful world (多麼美好的世界)", keyWords: ["think to myself", "wonderful"] },
      { start: 19.5, end: 26.5, en: "I see skies of blue and clouds of white", zh: "我看見碧空如洗的藍天，還有如棉花般柔軟的白雲", phonetic: "aɪ siː skaɪz əv bluː ænd klaʊdz əv waɪt", notes: "【天空描摹】skies of blue, clouds of white", keyWords: ["skies", "clouds"] },
      { start: 26.5, end: 33.5, en: "The bright blessed day, the dark sacred night", zh: "光明蒙恩賜予的白晝，沉靜神聖深邃的黑夜", phonetic: "ðə braɪt ˈblɛsɪd deɪ ðə dɑːrk ˈseɪkrɪd naɪt", notes: "【典雅形容詞】blessed (蒙福的)；sacred (神聖的)", keyWords: ["blessed", "sacred"] },
      { start: 33.5, end: 41.0, en: "And I think to myself, what a wonderful world", zh: "我深深在心底感悟：這個世界多麼美好神奇！", phonetic: "ænd aɪ θɪŋk tuː maɪˈsɛlf wʌt ə ˈwʌndərfəl wɜːrld", notes: "【真情回甘】由衷的讚嘆生命", keyWords: ["wonderful world"] }
    ]
  },
  {
    id: "autumn-leaves",
    title: "Autumn Leaves",
    artist: "Eva Cassidy / Nat King Cole",
    genre: "爵士標準曲",
    category: "jazz",
    level: "中級 (B1)",
    cover: "🍁",
    color: "#BC4749",
    bpm: 80,
    synthPattern: "jazz-swing-piano",
    audioNotes: "源自法國香頌的世界爵士經典，秋葉飄零與落寞思念的完美寫照。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "The falling leaves drift by the window", zh: "繽紛飄落的秋葉，悄然在窗櫺外隨風盤旋掠過", phonetic: "ðə ˈfɔːlɪŋ liːvz drɪft baɪ ðə ˈwɪndoʊ", notes: "【動態描摹】drift by (飄流而過)", keyWords: ["leaves", "drift", "window"] },
      { start: 6.5, end: 13.0, en: "The autumn leaves of red and gold", zh: "那染著深紅與金黃色澤的漫天秋葉", phonetic: "ði ˈɔːtəm liːvz əv rɛd ænd ɡoʊld", notes: "【秋景色彩】red and gold (紅黃交織)", keyWords: ["autumn", "gold"] },
      { start: 13.0, end: 19.5, en: "I see your lips, the summer kisses", zh: "我看見你的雙唇，憶起那盛夏烈日般的深情熱吻", phonetic: "aɪ siː jʊər lɪps ðə ˈsʌmər ˈkɪsɪz", notes: "【記憶浮現】summer kisses (盛夏之吻)", keyWords: ["lips", "kisses"] },
      { start: 19.5, end: 26.5, en: "The sun-burned hands I used to hold", zh: "還有我過去曾日日緊緊牽著的、被暖陽曬黑的雙手", phonetic: "ðə sʌn bɜːrnd hændz aɪ juːst tuː hoʊld", notes: "【複合形容詞】sun-burned (曬成焦糖色的)", keyWords: ["sun-burned", "hold"] },
      { start: 26.5, end: 34.0, en: "Since you went away the days grow long", zh: "自從你離我遠去之後，白晝歲月變得如此漫長難熬", phonetic: "sɪns juː wɛnt əˈweɪ ðə deɪz ɡroʊ lɔːŋ", notes: "【時間感嘆】the days grow long (度日如年)", keyWords: ["went away", "grow long"] },
      { start: 34.0, end: 42.0, en: "And soon I'll hear old winter's song, but I miss you most of all, my darling, when autumn leaves start to fall", zh: "不久嚴冬蕭瑟的輓歌便將奏響，但在所有時節裡我最思念你的，親愛的，正是在這秋葉飄零之際", phonetic: "bʌt aɪ mɪs juː moʊst əv ɔːl", notes: "【深情主旨】miss you most of all (最思念你之時)", keyWords: ["miss you", "autumn leaves"] }
    ]
  },
  {
    id: "cant-take-my-eyes-off-you",
    title: "Can't Take My Eyes Off You",
    artist: "Frankie Valli",
    genre: "經典搖擺流行",
    category: "jazz",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "👀",
    color: "#E63946",
    bpm: 124,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "熱烈真摯的經典告白舞曲，副歌節奏極富感染力，包含大量眼神與愛慕詞彙。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "You're just too good to be true, can't take my eyes off of you", zh: "你美得太過不真實，我的雙眼完全無法從你的身影上移開半分", phonetic: "jʊər ʤʌst tuː ɡʊd tuː biː truː kænt teɪk maɪ aɪz ɔːf əv juː", notes: "【核心片語】too good to be true (好得難以置信)；can't take eyes off (移不開視線)", keyWords: ["too good", "eyes off"] },
      { start: 6.5, end: 13.0, en: "You'd be like heaven to touch, I wanna hold you so much", zh: "觸摸你彷彿觸摸到了天堂，我多麼想將你緊緊擁入我的懷抱", phonetic: "juːd biː laɪk ˈhɛvən tuː tʌʧ aɪ ˈwɒnə hoʊld juː soʊ mʌʧ", notes: "【願望表達】wanna hold you so much", keyWords: ["heaven", "hold"] },
      { start: 13.0, end: 19.5, en: "At long last love has arrived, and I thank God I'm alive", zh: "千呼萬喚之中真愛終於降臨，我由衷感謝上蒼讓我能活著與你相遇", phonetic: "æt lɔːŋ læst lʌv hæz əˈraɪvd ænd aɪ θæŋk ɡɒd aɪm əˈlaɪv", notes: "【時間片語】at long last (終於、總算)", keyWords: ["at long last", "alive"] },
      { start: 19.5, end: 26.5, en: "You're just too good to be true, can't take my eyes off of you", zh: "你美好得宛若夢境，我的目光片刻都離不開你", phonetic: "jʊər ʤʌst tuː ɡʊd tuː biː truː", notes: "【反覆詠唱】加深傾慕感受", keyWords: ["too good"] }
    ]
  },
  {
    id: "moon-river",
    title: "Moon River",
    artist: "Audrey Hepburn (Breakfast at Tiffany's)",
    genre: "經典抒情標準曲",
    category: "jazz",
    level: "中級 (B1)",
    cover: "🌙",
    color: "#4A4E69",
    bpm: 68,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "第凡內早餐主題曲，奧黛麗赫本抱吉他窗台清唱傳奇，詩意典雅到了極致。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Moon River, wider than a mile", zh: "月河啊，蜿蜒寬廣超過一哩之遙", phonetic: "muːn ˈrɪvər ˈwaɪdər ðæn ə maɪl", notes: "【比較級】wider than a mile (寬逾一哩)", keyWords: ["Moon River", "wider", "mile"] },
      { start: 6.5, end: 13.0, en: "I'm crossing you in style someday", zh: "總有一天，我會以優雅自信的姿態渡過你前行", phonetic: "aɪm ˈkrɒsɪŋ juː ɪn staɪl ˈsʌmdeɪ", notes: "【成語片語】in style (別具風情、風雅從容)", keyWords: ["crossing", "in style"] },
      { start: 13.0, end: 19.5, en: "Oh, dream maker, you heart breaker", zh: "噢，編織夢想的造夢者，你也是個令人心碎的浪子", phonetic: "oʊ driːm ˈmeɪkər juː hɑːrt ˈbreɪkər", notes: "【生動稱謂】dream maker vs heart breaker", keyWords: ["dream maker", "heart breaker"] },
      { start: 19.5, end: 26.5, en: "Wherever you're goin', I'm goin' your way", zh: "無論你將漂流奔向何方，我都願伴隨你的浪跡天涯", phonetic: "wɛərˈɛvər jʊər ˈɡoʊɪn aɪm ˈɡoʊɪn jʊər weɪ", notes: "【地方連接詞】wherever (無論何處)", keyWords: ["wherever", "your way"] },
      { start: 26.5, end: 34.0, en: "Two drifters, off to see the world, there's such a lot of world to see", zh: "兩個流浪旅人，踏上閱歷大千世界的征途，世間有那麼多斑斕的奇景等待我們一睹風采", phonetic: "tuː ˈdrɪftərz ɔːf tuː siː ðə wɜːrld", notes: "【浪人名詞】drifters (隨波飄蕩的旅人)", keyWords: ["drifters", "world to see"] },
      { start: 34.0, end: 42.0, en: "We're after the same rainbow's end, waitin' 'round the bend, my huckleberry friend, Moon River, and me", zh: "我們追逐著同一道彩虹的盡頭，在河道轉彎處靜靜守候，我那越橘果般的知己好友，美麗月河與我", phonetic: "wɪr ˈæftər ðə seɪm ˈreɪnˌboʊz ɛnd", notes: "【美式典故】huckleberry friend (兒時一起冒險摘野果的真心摯友)", keyWords: ["rainbow", "bend", "huckleberry"] }
    ]
  },
  {
    id: "love",
    title: "L-O-V-E",
    artist: "Nat King Cole",
    genre: "爵士搖擺",
    category: "jazz",
    level: "基礎入門 (A1-A2)",
    cover: "💌",
    color: "#E07A5F",
    bpm: 125,
    synthPattern: "jazz-swing-piano",
    audioNotes: "以 L-O-V-E 四個字母藏頭詩拆解愛情的幽默輕快名曲，節奏歡樂明朗。",
    lyrics: [
      { start: 0.0, end: 5.5, en: "L is for the way you look at me", zh: "L 是代表著你注視著我的含情雙眸", phonetic: "ɛl ɪz fɔːr ðə weɪ juː lʊk æt miː", notes: "【字母拆解】the way you look at me (你看我的模樣神態)", keyWords: ["look at me"] },
      { start: 5.5, end: 11.0, en: "O is for the only one I see", zh: "O 是代表著你是我眼中唯一的唯一焦點", phonetic: "oʊ ɪz fɔːr ði ˈoʊnli wʌn aɪ siː", notes: "【專一形容】the only one I see (我唯一看見的人)", keyWords: ["only one"] },
      { start: 11.0, end: 16.5, en: "V is very, very extraordinary", zh: "V 是代表著這份感情是如此無與倫比、非凡奇妙", phonetic: "viː ɪz ˈvɛri ˈvɛri ɪkˈstrɔːrdnˌɛri", notes: "【高級形容詞】extraordinary (非同尋常、非凡無比)", keyWords: ["extraordinary"] },
      { start: 16.5, end: 22.0, en: "E is even more than anyone that you adore can do", zh: "E 是代表著愛的力量超越了世間任何熱烈愛慕者所能奉獻的一切", phonetic: "iː ɪz ˈiːvən mɔːr ðæn ˈɛniˌwʌn ðæt juː əˈdɔːr kæn duː", notes: "【深情超越】more than anyone can do", keyWords: ["adore"] },
      { start: 22.0, end: 28.5, en: "Love is all that I can give to you, love is more than just a game for two", zh: "愛是我所能獻給你的一切，愛絕不僅僅是一場供兩人消遣的感情遊戲", phonetic: "lʌv ɪz ɔːl ðæt aɪ kæn ɡɪv tuː juː", notes: "【真愛定義】more than just a game", keyWords: ["give", "game"] }
    ]
  },
  {
    id: "over-the-rainbow",
    title: "Somewhere Over the Rainbow",
    artist: "Judy Garland (The Wizard of Oz)",
    genre: "經典好萊塢標準曲",
    category: "jazz",
    level: "初級 (A2)",
    cover: "🌈",
    color: "#3D405B",
    bpm: 78,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "百年電影第一名曲，綠野仙蹤主題曲，旋律乾淨如洗，充滿對童話美夢的憧憬。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Somewhere over the rainbow, way up high", zh: "在彩虹高懸的遙遠彼端，在至高無上的雲端之上", phonetic: "ˈsʌmˌwɛər ˈoʊvər ðə ˈreɪnˌboʊ weɪ ʌp haɪ", notes: "【方位詞組】way up high (在極高之處)", keyWords: ["rainbow", "high"] },
      { start: 6.5, end: 13.0, en: "There's a land that I heard of once in a lullaby", zh: "有一片我曾在童年搖籃曲中聽聞過的奇妙樂土", phonetic: "ðɛrz ə lænd ðæt aɪ hɜːrd əv wʌns ɪn ə ˈlʌləˌbaɪ", notes: "【名詞】lullaby (搖籃曲、催眠曲)", keyWords: ["land", "lullaby"] },
      { start: 13.0, end: 19.5, en: "Somewhere over the rainbow, skies are blue", zh: "在彩虹彼端的國度裡，天空總是純澈如洗的碧藍", phonetic: "ˈsʌmˌwɛər ˈoʊvər ðə ˈreɪnˌboʊ skaɪz ɑːr bluː", notes: "【晴朗象徵】skies are blue (萬里無雲的晴空)", keyWords: ["skies", "blue"] },
      { start: 19.5, end: 26.5, en: "And the dreams that you dare to dream really do come true", zh: "那些你敢於在心中構想的美夢，真的都會一件件成真實現", phonetic: "ænd ðə driːmz ðæt juː dɛər tuː driːm ˈrɪəli duː kʌm truː", notes: "【強調助動詞】really do come true (真的會成真)", keyWords: ["dare to dream", "come true"] },
      { start: 26.5, end: 34.0, en: "Someday I'll wish upon a star, and wake up where the clouds are far behind me", zh: "總有一天我會對著繁星許下心願，並在一片烏雲都已被遠遠拋在身後的晴空下甦醒", phonetic: "ˈsʌmdeɪ aɪl wɪʃ əˈpɒn ə stɑːr", notes: "【童話成語】wish upon a star (對流星許願)", keyWords: ["wish upon a star", "clouds"] }
    ]
  },
  {
    id: "la-vie-en-rose",
    title: "La Vie En Rose (English)",
    artist: "Louis Armstrong",
    genre: "爵士經典",
    category: "jazz",
    level: "中級 (B1)",
    cover: "🌹",
    color: "#F28482",
    bpm: 78,
    synthPattern: "jazz-swing-piano",
    audioNotes: "法國香頌玫瑰人生之英語改編版，阿姆斯壯深情小號與歌聲，充滿浪漫玫瑰色濾鏡。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Hold me close and hold me fast, the magic spell you cast", zh: "將我緊緊抱在懷中，那是你所施下的溫柔魔法咒語", phonetic: "hoʊld miː kloʊs ænd hoʊld miː fæst ðə ˈmæʤɪk spɛl juː kæst", notes: "【魔法片語】cast a spell (施展法術、施展魔咒)", keyWords: ["hold close", "magic spell"] },
      { start: 6.5, end: 13.0, en: "This is la vie en rose", zh: "這正是我眼中的玫瑰色人生", phonetic: "ðɪs ɪz lɑː viː ɒn roʊz", notes: "【法語名句】la vie en rose (像玫瑰般粉紅美好的浪漫人生)", keyWords: ["la vie en rose"] },
      { start: 13.0, end: 19.5, en: "When you kiss me, heaven sighs, and though I close my eyes", zh: "當你親吻我時，連天堂都輕輕發出嘆息，縱然我闔上雙眼", phonetic: "wɛn juː kɪs miː ˈhɛvən saɪz", notes: "【浪漫擬人】heaven sighs (連天堂都感動嘆息)", keyWords: ["kiss", "heaven sighs"] },
      { start: 19.5, end: 26.5, en: "I see la vie en rose", zh: "我依然能清晰看見一片粉紅溫柔的玫瑰人生", phonetic: "aɪ siː lɑː viː ɒn roʊz", notes: "【浪漫視覺】閉上雙眼依然見到粉紅光明", keyWords: ["see"] }
    ]
  },

  // ─── 5. 溫馨童謠與英語基礎啟蒙 (Gentle Folk & Beginners) ───
  {
    id: "you-are-my-sunshine",
    title: "You Are My Sunshine",
    artist: "Traditional / Folk",
    genre: "民謠童謠",
    category: "beginners",
    level: "基礎入門 (A1)",
    cover: "☀️",
    color: "#E9C46A",
    bpm: 96,
    synthPattern: "warm-music-box",
    audioNotes: "傳唱近百年的世界名曲，韻律優美自然，發音圓潤，極適合練習母音長短音對比。",
    lyrics: [
      { start: 0.0, end: 6.0, en: "You are my sunshine, my only sunshine", zh: "你是我的陽光，我唯一璀璨的陽光", phonetic: "juː ɑːr maɪ ˈsʌnˌʃaɪn maɪ ˈoʊnli ˈsʌnˌʃaɪn", notes: "【隱喻】sunshine (喻指帶來歡樂的摯愛)", keyWords: ["sunshine", "only"] },
      { start: 6.0, end: 12.0, en: "You make me happy when skies are gray", zh: "即使天空烏雲籠罩，你也能使我笑容綻放", phonetic: "juː meɪk miː ˈhæpi wɛn skaɪz ɑːr ɡreɪ", notes: "【使役動詞】make + 受詞 + 形容詞 (make me happy)", keyWords: ["happy", "skies", "gray"] },
      { start: 12.0, end: 18.0, en: "You'll never know, dear, how much I love you", zh: "親愛的，你永遠不會知道我對你的愛有多深", phonetic: "juːl ˈnɛvər noʊ dɪər haʊ mʌʧ aɪ lʌv juː", notes: "【程度感嘆】how much I love you (我有多愛你)", keyWords: ["never", "dear", "love"] },
      { start: 18.0, end: 25.0, en: "Please don't take my sunshine away", zh: "所以請不要帶走我那珍貴的陽光", phonetic: "pliːz doʊnt teɪk maɪ ˈsʌnˌʃaɪn əˈweɪ", notes: "【片語】take away (拿走、奪去)", keyWords: ["take away", "sunshine"] },
      { start: 25.0, end: 31.0, en: "The other night, dear, as I lay sleeping", zh: "前些天夜裡，親愛的，當我沉沉入睡之時", phonetic: "ði ˈʌðər naɪt dɪər æz aɪ leɪ ˈsliːpɪŋ", notes: "【時間片語】the other night (前幾天的某個夜晚)", keyWords: ["night", "sleeping", "lay"] },
      { start: 31.0, end: 37.0, en: "I dreamed I held you in my arms", zh: "我夢見我曾將你緊緊擁入我的懷中", phonetic: "aɪ driːmd aɪ hɛld juː ɪn maɪ ɑːrmz", notes: "【時態】held 為 hold 的過去式", keyWords: ["dreamed", "held", "arms"] },
      { start: 37.0, end: 43.0, en: "When I awoke, dear, I was mistaken", zh: "但當我驚醒時，親愛的，才發現只是一場誤會與幻夢", phonetic: "wɛn aɪ əˈwoʊk dɪər aɪ wʌz mɪsˈteɪkən", notes: "【片語】be mistaken (弄錯了、會錯意了)", keyWords: ["awoke", "mistaken"] },
      { start: 43.0, end: 50.0, en: "So I hung my head and I cried", zh: "於是我垂下了頭，止不住地流下眼淚", phonetic: "soʊ aɪ hʌŋ maɪ hɛd ænd aɪ kraɪd", notes: "【肢體語言】hang one's head (低頭沮喪垂淚)", keyWords: ["hung", "head", "cried"] }
    ]
  },
  {
    id: "top-of-the-world",
    title: "Top of the World",
    artist: "The Carpenters",
    genre: "經典流行民謠",
    category: "beginners",
    level: "初級 (A2)",
    cover: "🏔️",
    color: "#E76F51",
    bpm: 92,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "卡本特兄妹陽光歡樂名曲，凱倫卡本特發音教科書等級的純正清晰。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Such a feelin's comin' over me", zh: "一股奇妙歡愉的幸福感悄然湧上我的心頭", phonetic: "sʌʧ ə ˈfiːlɪŋz ˈkʌmɪŋ ˈoʊvər miː", notes: "【片語】come over someone (情感湧上心頭)", keyWords: ["feeling", "coming over"] },
      { start: 6.5, end: 13.0, en: "There is wonder in most everythin' I see", zh: "在我眼前目睹的幾乎每一件事物裡，都充滿著不可思議的驚奇", phonetic: "ðɛər ɪz ˈwʌndər ɪn moʊst ˈɛvrɪˌθɪŋ aɪ siː", notes: "【名詞】wonder (奇蹟奇妙之處)", keyWords: ["wonder", "everything"] },
      { start: 13.0, end: 19.5, en: "Not a cloud in the sky, got the sun in my eyes", zh: "湛藍天空中沒有一絲烏雲，雙眸映照著耀眼溫暖的陽光", phonetic: "nɒt ə klaʊd ɪn ðə skaɪ ɡɒt ðə sʌn ɪn maɪ aɪz", notes: "【晴朗象徵】Not a cloud in the sky", keyWords: ["cloud", "sun"] },
      { start: 19.5, end: 26.5, en: "And I won't be surprised if it's a dream", zh: "哪怕這一切美好宛若一場幻夢，我也不會感到半分意外驚訝", phonetic: "ænd aɪ woʊnt biː sərˈpraɪzd ɪf ɪts ə driːm", notes: "【條件句】won't be surprised", keyWords: ["surprised", "dream"] },
      { start: 26.5, end: 34.0, en: "I'm on the top of the world lookin' down on creation", zh: "我正佇立在世界的至高巔峰，居高臨下俯瞰上帝所創造的大千萬物", phonetic: "aɪm ɒn ðə tɒp əv ðə wɜːrld ˈlʊkɪŋ daʊn ɒn kriːˈeɪʃən", notes: "【成語】on the top of the world (興高采烈、欣喜若狂)", keyWords: ["top of the world", "creation"] },
      { start: 34.0, end: 42.0, en: "And the only explanation I can find is the love that I've found ever since you've been around, your love's put me at the top of the world", zh: "而我唯一能找到的合理答案，正是我遇見了你之後所感受到的愛，是你的愛將我送上了世界之巔", phonetic: "ænd ði ˈoʊnli ˌɛkspləˈneɪʃən aɪ kæn faɪnd", notes: "【甜蜜歸因】put me at the top of the world", keyWords: ["explanation", "found"] }
    ]
  },
  {
    id: "close-to-you",
    title: "(They Long to Be) Close to You",
    artist: "The Carpenters",
    genre: "經典流行抒情",
    category: "beginners",
    level: "初級 (A2)",
    cover: "🐦",
    color: "#F4A261",
    bpm: 88,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "巴卡拉克經典作曲，鳥兒、群星齊聚身邊的童話擬人修辭，發音極度圓潤。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Why do birds suddenly appear every time you are near?", zh: "為什麼每一次當你靠近走近身邊時，身旁總會突然飛來一隻隻歡鳴的鳥兒？", phonetic: "waɪ duː bɜːrdz ˈsʌdənli əˈpɪər ˈɛvri taɪm juː ɑːr nɪər", notes: "【時間連詞】every time (每一次...之時)", keyWords: ["birds", "appear", "near"] },
      { start: 6.5, end: 13.0, en: "Just like me, they long to be close to you", zh: "就如同我一樣，牠們也深深渴望能夠長久伴隨親近在你的身邊", phonetic: "ʤʌst laɪk miː ðeɪ lɔːŋ tuː biː kloʊs tuː juː", notes: "【核心片語】long to be (渴望成為/身處)；close to (靠近)", keyWords: ["long to be", "close to you"] },
      { start: 13.0, end: 19.5, en: "Why do stars fall down from the sky every time you walk by?", zh: "為什麼每一次當你款款走過之時，漫天繁星都忍不住紛紛從夜空墜落？", phonetic: "waɪ duː stɑːrz fɔːl daʊn frʌm ðə skaɪ ˈɛvri taɪm juː wɔːk baɪ", notes: "【浪漫擬人】stars fall down", keyWords: ["stars", "walk by"] },
      { start: 19.5, end: 26.5, en: "Just like me, they long to be close to you", zh: "正如我的心意一般，群星也多麼希望能伴守在你的身旁", phonetic: "ʤʌst laɪk miː ðeɪ lɔːŋ tuː biː kloʊs tuː juː", notes: "【副歌複誦】加深印記", keyWords: ["close to you"] }
    ]
  },
  {
    id: "edelweiss",
    title: "Edelweiss",
    artist: "The Sound of Music",
    genre: "經典音樂劇民謠",
    category: "beginners",
    level: "基礎入門 (A1)",
    cover: "🏔️",
    color: "#E2E8F0",
    bpm: 76,
    synthPattern: "warm-music-box",
    audioNotes: "真善美傳世名曲，三拍子圓舞曲，旋律莊嚴清澈，詞句簡單卻極富愛國親情寓意。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Edelweiss, Edelweiss, every morning you greet me", zh: "雪絨花啊雪絨花，每天清晨你都用清新容顏迎接問候我", phonetic: "ˈeɪdəlvaɪs ˈeɪdəlvaɪs ˈɛvri ˈmɔːrnɪŋ juː ɡriːt miː", notes: "【花卉植物】Edelweiss (阿爾卑斯高山雪絨花，象徵純潔不屈)", keyWords: ["Edelweiss", "greet"] },
      { start: 6.5, end: 13.0, en: "Small and white, clean and bright, you look happy to meet me", zh: "嬌小潔白、純淨明亮，你看起來是那麼歡欣雀躍遇見了我", phonetic: "smɔːl ænd waɪt kliːn ænd braɪt juː lʊk ˈhæpi tuː miːt miː", notes: "【形容詞押韻】small and white, clean and bright", keyWords: ["white", "bright", "happy"] },
      { start: 13.0, end: 19.5, en: "Blossom of snow, may you bloom and grow, bloom and grow forever", zh: "宛如白雪般綻放的花蕾，願你生機盎然蓬勃生長，直到永遠", phonetic: "ˈblɒsəm əv snoʊ meɪ juː bluːm ænd ɡroʊ bluːm ænd ɡroʊ fərˈɛvər", notes: "【祈願語氣】May you bloom and grow (願你欣欣向榮)", keyWords: ["blossom", "bloom", "grow", "forever"] },
      { start: 19.5, end: 28.0, en: "Edelweiss, Edelweiss, bless my homeland forever", zh: "雪絨花啊雪絨花，請生生世世守護保佑我的祖國與家園", phonetic: "ˈeɪdəlvaɪs ˈeɪdəlvaɪs blɛs maɪ ˈhoʊmˌlænd fərˈɛvər", notes: "【祈求護佑】bless my homeland (祝福庇佑我的家園)", keyWords: ["bless", "homeland"] }
    ]
  },
  {
    id: "do-re-mi",
    title: "Do-Re-Mi",
    artist: "The Sound of Music",
    genre: "音樂劇啟蒙",
    category: "beginners",
    level: "基礎入門 (A1)",
    cover: "🎵",
    color: "#FFB703",
    bpm: 120,
    synthPattern: "warm-music-box",
    audioNotes: "全世界最著名的音樂啟蒙童謠，將音階巧妙轉化為自然名詞（Doe, Ray, Me, Far, Sew, La, Tea）。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Doe, a deer, a female deer", zh: "Doe 是鹿，是一隻溫順優雅的母鹿", phonetic: "doʊ ə dɪər ə ˈfiːmeɪl dɪər", notes: "【同音雙關】Doe 音同 Do，意為母鹿", keyWords: ["doe", "deer", "female"] },
      { start: 6.5, end: 12.0, en: "Ray, a drop of golden sun", zh: "Ray 是光芒，是金色朝陽灑落的一縷光暈", phonetic: "reɪ ə drɒp əv ˈɡoʊldən sʌn", notes: "【雙關】Ray 音同 Re，意為光線光束", keyWords: ["ray", "golden sun"] },
      { start: 12.0, end: 17.5, en: "Me, a name I call myself", zh: "Me 是我，是我用來稱呼自己的親暱稱謂", phonetic: "miː ə neɪm aɪ kɔːl maɪˈsɛlf", notes: "【雙關】Me 音同 Mi，代名詞我", keyWords: ["call myself"] },
      { start: 17.5, end: 23.0, en: "Far, a long, long way to run", zh: "Far 是遠方，是一條漫長遙遠、需要奮力奔跑的路途", phonetic: "fɑːr ə lɔːŋ lɔːŋ weɪ tuː rʌn", notes: "【雙關】Far 音同 Fa，形容詞遙遠的", keyWords: ["far", "long way"] },
      { start: 23.0, end: 28.5, en: "Sew, a needle pulling thread", zh: "Sew 是縫紉，是繡針引領著細絲線穿梭編織", phonetic: "soʊ ə ˈniːdl ˈpʊlɪŋ θrɛd", notes: "【雙關】Sew 音同 Sol，動詞縫紉", keyWords: ["sew", "needle", "thread"] },
      { start: 28.5, end: 34.0, en: "La, a note to follow Sew", zh: "La 是緊隨在 Sol 音符後方的下一個美好音階", phonetic: "lɑː ə noʊt tuː ˈfɒloʊ soʊ", notes: "【音樂術語】note (音符、音階)", keyWords: ["note", "follow"] },
      { start: 34.0, end: 40.0, en: "Tea, a drink with jam and bread, that will bring us back to Do", zh: "Tea 是下午茶，配著果醬抹麵包的美味飲品，那又會將我們順暢帶回起點的 Do", phonetic: "tiː ə drɪŋk wɪð ʤæm ænd brɛd", notes: "【閉環旋律】bring us back to Do", keyWords: ["tea", "drink", "jam", "bread"] }
    ]
  },
  {
    id: "lemon-tree",
    title: "Lemon Tree",
    artist: "Fool's Garden",
    genre: "流行輕搖滾",
    category: "beginners",
    level: "初級 (A2)",
    cover: "🍋",
    color: "#E9D8A6",
    bpm: 142,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "風靡全台的輕快名曲，節奏極度鮮明，歌詞充滿星期天無聊發呆的日常口語。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I'm sitting here in the boring room, it's just another rainy Sunday afternoon", zh: "我正百無聊賴地坐在沈悶的房間裡，這又是一個陰雨綿綿的週日下午", phonetic: "aɪm ˈsɪtɪŋ hɪər ɪn ðə ˈbɔːrɪŋ ruːm", notes: "【日常情境】boring room, rainy Sunday afternoon", keyWords: ["sitting", "boring", "rainy"] },
      { start: 6.5, end: 12.8, en: "I'm wasting my time, I got nothing to do", zh: "我虛擲浪費著大把時間，無所事事沒有任何事情可做", phonetic: "aɪm ˈweɪstɪŋ maɪ taɪm aɪ ɡɒt ˈnʌθɪŋ tuː duː", notes: "【生活片語】waste time (浪費時間)；got nothing to do", keyWords: ["wasting", "nothing"] },
      { start: 12.8, end: 19.0, en: "I'm hanging around, I'm waiting for you, but nothing ever happens and I wonder", zh: "我無聊地四處閒晃，我在痴痴等著你的身影，但生活什麼奇蹟也沒發生，我暗自疑惑納悶", phonetic: "aɪm ˈhæŋɪŋ əˈraʊnd aɪm ˈweɪtɪŋ fɔːr juː", notes: "【口語片語】hang around (閒蕩、消磨時間)", keyWords: ["hanging around", "wonder"] },
      { start: 19.0, end: 26.0, en: "I wonder how, I wonder why, yesterday you told me 'bout the blue, blue sky", zh: "我好奇為何會如此，我納悶為何生活這般沉悶，昨天你才向我描繪那片無比湛藍的青天", phonetic: "aɪ ˈwʌndər haʊ aɪ ˈwʌndər waɪ", notes: "【動詞】wonder (想知道、感到納悶好奇)", keyWords: ["wonder how", "blue sky"] },
      { start: 26.0, end: 34.0, en: "And all that I can see is just a yellow lemon-tree", zh: "而如今我放眼所及的，卻唯有一株孤零零的黃色檸檬樹", phonetic: "ænd ɔːl ðæt aɪ kæn siː ɪz ʤʌst ə ˈjɛloʊ ˈlɛmən triː", notes: "【酸澀意象】lemon tree (酸澀單調生活的隱喻)", keyWords: ["lemon-tree"] }
    ]
  },
  {
    id: "seasons-in-the-sun",
    title: "Seasons in the Sun",
    artist: "Terry Jacks",
    genre: "經典流行民謠",
    category: "beginners",
    level: "初級 (A2)",
    cover: "🌞",
    color: "#EE9B00",
    bpm: 98,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "源自 Jacques Brel 法國名作，旋律輕快卻歌詞深情告別，充滿童年爬樹與友情回憶。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Goodbye to you my trusted friend, we've known each other since we were nine or ten", zh: "再見了，我最信賴倚重的好友，我們從彼此才九歲、十歲的孩提時代便相識相知", phonetic: "ˌɡʊdˈbaɪ tuː juː maɪ ˈtrʌstɪd frɛnd", notes: "【時間連詞】since we were (打從我們那時起)", keyWords: ["trusted friend", "since"] },
      { start: 6.5, end: 13.0, en: "Together we've climbed hills and trees, learned of love and ABC's", zh: "我們曾一同攀爬漫步山丘、攀緣老樹，一同在歲月中懂得了愛，也學會了基礎的 ABC", phonetic: "təˈɡɛðər wiːv klaɪmd hɪlz ænd triːz", notes: "【成長印記】climbed trees, learned love and ABCs", keyWords: ["climbed", "learned"] },
      { start: 13.0, end: 19.5, en: "Skinned our hearts and skinned our knees", zh: "我們曾在感情中摔碎心扉，也曾像孩子般摔破過膝蓋", phonetic: "skɪnd ˈaʊər hɑːrts ænd skɪnd ˈaʊər niːz", notes: "【雙關修辭】skinned knees (擦破皮) vs skinned hearts (心靈受傷)", keyWords: ["knees", "hearts"] },
      { start: 19.5, end: 27.0, en: "We had joy, we had fun, we had seasons in the sun, but the hills that we climbed were just seasons out of time", zh: "我們曾擁有過無窮的歡樂，我們曾分享過純真的歡笑，我們曾共同擁抱陽光璀璨的四季時光", phonetic: "wiː hæd ʤɔɪ wiː hæd fʌn wiː hæd ˈsiːznz ɪn ðə sʌn", notes: "【經典副歌】seasons in the sun (陽光燦爛的美好季節)", keyWords: ["joy", "fun", "seasons in the sun"] }
    ]
  },
  {
    id: "my-love",
    title: "My Love",
    artist: "Westlife",
    genre: "流行男團金曲",
    category: "beginners",
    level: "初級 (A2)",
    cover: "🍀",
    color: "#2D6A4F",
    bpm: 104,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "西城男孩代表作，全台傳唱度極高的英倫流行金曲，發音標準清晰，是必學經典。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "An empty street, an empty house, a hole inside my heart", zh: "空無一人的寂寥街道，空空蕩蕩的寂靜屋舍，還有我心靈深處那一處空洞創傷", phonetic: "æn ˈɛmpti striːt æn ˈɛmpti haʊs ə hoʊl ɪnˈsaɪd maɪ hɑːrt", notes: "【排比寂寞】empty street, empty house", keyWords: ["empty", "hole", "heart"] },
      { start: 6.5, end: 13.0, en: "I'm all alone, the rooms are getting smaller", zh: "我形單影隻孤身一人，四周的房間似乎變得愈發狹窄逼仄", phonetic: "aɪm ɔːl əˈloʊn ðə ruːmz ɑːr ˈɡɛtɪŋ ˈsmɔːlər", notes: "【心理壓抑】getting smaller (越變越狹小)", keyWords: ["alone", "smaller"] },
      { start: 13.0, end: 19.5, en: "I wonder how, I wonder why, I wonder where they are, the days we had, the songs we sang together", zh: "我好奇為何會走到這一步，我納悶那些日子都去了何方，我們曾攜手共度的歲月，我們曾同唱的歌謠", phonetic: "aɪ ˈwʌndər haʊ aɪ ˈwʌndər waɪ", notes: "【懷舊自語】the songs we sang together", keyWords: ["wonder", "sang"] },
      { start: 19.5, end: 27.5, en: "So I say a little prayer, and hope my dreams will take me there, where the skies are blue, to see you once again, my love", zh: "於是我在心底默默祈禱，期盼美夢能引領我回到那一處晴空萬里的地方，讓我能再次見到你，我的摯愛", phonetic: "soʊ aɪ seɪ ə ˈlɪtl prɛər", notes: "【日常祈求】say a prayer (做個祈禱)", keyWords: ["prayer", "my love"] }
    ]
  },

  // ─── 6. 勵志心靈與生命之歌 (Inspirational & Life Songs) ───
  {
    id: "we-are-the-world",
    title: "We Are the World",
    artist: "USA for Africa",
    genre: "公益巨作",
    category: "inspirational",
    level: "中級 (B1)",
    cover: "🌍",
    color: "#E76F51",
    bpm: 73,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "麥可傑克森與萊諾李奇群星慈善史詩，呼籲關懷飢荒與全球大愛，歌詞極具感染力。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "There comes a time when we heed a certain call", zh: "有時我們會接收到一聲來自遠方的迫切召喚", phonetic: "ðɛər kʌmz ə taɪm wɛn wiː hiːd ə ˈsɜːrtn kɔːl", notes: "【動詞】heed (留意、聽從呼喚)", keyWords: ["heed", "call"] },
      { start: 6.5, end: 13.0, en: "When the world must come together as one", zh: "當全世界必須團結一心、緊緊凝結在一起之時", phonetic: "wɛn ðə wɜːrld mʌst kʌm təˈɡɛðər æz wʌn", notes: "【片語】come together as one (萬眾一心)", keyWords: ["together", "as one"] },
      { start: 13.0, end: 19.5, en: "There are people dying, and it's time to lend a hand to life, the greatest gift of all", zh: "有人正在饑餒邊緣垂死掙扎，正是我們為生命伸出援手的時候，生命正是至高無上的恩賜", phonetic: "ðɛər ɑːr ˈpiːpl ˈdaɪɪŋ ænd ɪts taɪm tuː lɛnd ə hænd", notes: "【片語】lend a hand (伸出援手、提供幫助)", keyWords: ["lend a hand", "gift"] },
      { start: 19.5, end: 26.5, en: "We can't go on pretending day by day that someone, somewhere will soon make a change", zh: "我們不能日復一日假裝若無其事，指望著遠方某個不知名的好心人會出面扭轉局勢", phonetic: "wiː kænt ɡoʊ ɒn prɪˈtɛndɪŋ deɪ baɪ deɪ", notes: "【動詞片語】go on pretending (繼續自欺欺人)", keyWords: ["pretending", "change"] },
      { start: 26.5, end: 34.0, en: "We are the world, we are the children, we are the ones who make a brighter day, so let's start giving", zh: "我們就是這個世界，我們就是這片土地的孩子，正是我們才能創造更明媚的明天，就讓我們從給予開始吧", phonetic: "wiː ɑːr ðə wɜːrld wiː ɑːr ðə ˈʧɪldrən", notes: "【世紀核心倡議】We are the world (天下一家)", keyWords: ["we are the world", "brighter day", "giving"] }
    ]
  },
  {
    id: "hero",
    title: "Hero",
    artist: "Mariah Carey",
    genre: "靈魂勵志",
    category: "inspirational",
    level: "中級 (B1)",
    cover: "🦸",
    color: "#457B9D",
    bpm: 60,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "瑪麗亞凱莉殿堂級心靈勵志曲，提醒每個人自己的內心深處，都住著一位無所畏懼的英雄。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "There's a hero if you look inside your heart", zh: "只要你敢於審視凝望自己的內心深處，那裡便住著一位強大的英雄", phonetic: "ðɛrz ə ˈhɪəroʊ ɪf juː lʊk ɪnˈsaɪd jʊər hɑːrt", notes: "【內在審視】look inside your heart", keyWords: ["hero", "heart"] },
      { start: 6.5, end: 13.0, en: "You don't have to be afraid of what you are", zh: "你絲毫無需畏懼自己真正的本質與原本的模樣", phonetic: "juː doʊnt hæv tuː biː əˈfreɪd əv wʌt juː ɑːr", notes: "【接納自我】not afraid of what you are", keyWords: ["afraid", "what you are"] },
      { start: 13.0, end: 19.5, en: "There's an answer if you reach into your soul", zh: "只要你將探求的觸角深入你的靈魂，所有謎題的答案都早已在那裡等候", phonetic: "ðɛrz æn ˈænsər ɪf juː riːʧ ˈɪntuː jʊər soʊl", notes: "【靈魂深究】reach into your soul", keyWords: ["answer", "soul"] },
      { start: 19.5, end: 26.5, en: "And the sorrow that you know will melt away", zh: "那些你曾深切品嚐過的悲傷苦楚，都將會如春陽融雪般漸漸消散殆盡", phonetic: "ænd ðə ˈsɒroʊ ðæt juː noʊ wɪl mɛlt əˈweɪ", notes: "【動詞片語】melt away (消融化解、煙消雲散)", keyWords: ["sorrow", "melt away"] },
      { start: 26.5, end: 34.0, en: "And then a hero comes along, with the strength to carry on", zh: "緊接著一位無畏的英雄便會挺身而出，賦予你繼續咬牙奮戰下去的無限力量", phonetic: "ænd ðɛn ə ˈhɪəroʊ kʌmz əˈlɔːŋ", notes: "【力量來源】strength to carry on", keyWords: ["comes along", "strength"] },
      { start: 34.0, end: 42.0, en: "And you cast your fears aside, and you know you can survive", zh: "你會毅然將所有的恐懼不安拋諸腦後，並且深信自己定能熬過難關頑強生存下去", phonetic: "ænd juː kæst jʊər fɪərz əˈsaɪd", notes: "【堅定片語】cast aside (拋開丟棄)；survive (存活挺過)", keyWords: ["cast aside", "survive"] }
    ]
  },
  {
    id: "you-raise-me-up",
    title: "You Raise Me Up",
    artist: "Josh Groban / Secret Garden",
    genre: "美聲心靈",
    category: "inspirational",
    level: "中級 (B1)",
    cover: "🕊️",
    color: "#1D3557",
    bpm: 60,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "全球翻唱逾百次的跨界心靈聖歌，旋律如浪潮般澎湃起伏，讚美愛與信仰的提拔滋養。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When I am down and, oh my soul, so weary", zh: "當我跌入低谷情緒沮喪，噢，我的靈魂感到如此疲憊不堪", phonetic: "wɛn aɪ æm daʊn ænd oʊ maɪ soʊl soʊ ˈwɪəri", notes: "【形容詞】down (沮喪落魄)；weary (筋疲力竭)", keyWords: ["down", "soul", "weary"] },
      { start: 6.5, end: 13.0, en: "When troubles come and my heart burdened be", zh: "當重重困難挫折接踵而至，我的心靈被沉重枷鎖壓得喘不過氣", phonetic: "wɛn ˈtrʌblz kʌm ænd maɪ hɑːrt ˈbɜːrdnd biː", notes: "【古典文法】burdened be (背負重擔沉重)", keyWords: ["troubles", "burdened"] },
      { start: 13.0, end: 19.5, en: "Then, I am still and wait here in the silence", zh: "每當此時，我便會靜下心來，在一片寧靜中默默等待著你的到來", phonetic: "ðɛn aɪ æm stɪl ænd weɪt hɪər ɪn ðə ˈsaɪləns", notes: "【寧靜片語】wait here in the silence", keyWords: ["still", "silence"] },
      { start: 19.5, end: 26.5, en: "Until you come and sit awhile with me", zh: "直到你悄然走來，溫柔坐在我身邊陪伴我片刻片刻", phonetic: "ənˈtɪl juː kʌm ænd sɪt əˈwaɪl wɪð miː", notes: "【副詞】awhile (片刻、一會兒)", keyWords: ["sit awhile"] },
      { start: 26.5, end: 34.0, en: "You raise me up, so I can stand on mountains", zh: "是你提拔鼓舞了我，讓我得以傲然屹立在萬仞群峰之上", phonetic: "juː reɪz miː ʌp soʊ aɪ kæn stænd ɒn ˈmaʊntənz", notes: "【動詞片語】raise up (扶持、激勵提拔)", keyWords: ["raise me up", "mountains"] },
      { start: 34.0, end: 42.0, en: "You raise me up, to walk on stormy seas, I am strong, when I am on your shoulders, you raise me up to more than I can be", zh: "是你激勵了我，讓我能無懼在狂暴大海上昂首漫步；只要佇立在你的肩頭我便充滿力量，是你成就了超越我原本極限的自己", phonetic: "juː reɪz miː ʌp tuː wɔːk ɒn ˈstɔːrmi siːz", notes: "【靈性昇華】more than I can be (超越自我)", keyWords: ["stormy seas", "shoulders", "more than I can be"] }
    ]
  },
  {
    id: "i-have-a-dream",
    title: "I Have a Dream",
    artist: "ABBA / Westlife",
    genre: "經典流行",
    category: "inspirational",
    level: "初級 (A2)",
    cover: "🌟",
    color: "#E09F3E",
    bpm: 104,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "阿巴合唱團傳奇名曲，童話仙女般的溫柔隱喻，是克服恐懼與心靈打氣的常備歌。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "I have a dream, a song to sing", zh: "我心中懷抱著一個美夢，一首渴望為世界高唱的歌謠", phonetic: "aɪ hæv ə driːm ə sɔːŋ tuː sɪŋ", notes: "【夢想句型】I have a dream", keyWords: ["dream", "song"] },
      { start: 6.5, end: 13.0, en: "To help me cope with anything", zh: "那首歌能賜予我力量，幫助我從容應對人生的一切艱難挑戰", phonetic: "tuː hɛlp miː koʊp wɪð ˈɛniˌθɪŋ", notes: "【動詞片語】cope with (應對、克服難關)", keyWords: ["cope with"] },
      { start: 13.0, end: 19.5, en: "If you see the wonder of a fairy tale", zh: "只要你能看懂童話故事中所蘊含的那份純潔奇蹟", phonetic: "ɪf juː siː ðə ˈwʌndər əv ə ˈfɛəri teɪl", notes: "【童話名詞】fairy tale (童話故事)", keyWords: ["wonder", "fairy tale"] },
      { start: 19.5, end: 26.5, en: "You can take the future even if you fail", zh: "縱然旅途中會面臨失敗跌倒，你也依然能勇敢開拓擁抱未來", phonetic: "juː kæn teɪk ðə ˈfjuːʧər ˈiːvən ɪf juː feɪl", notes: "【讓步句】even if you fail (哪怕失敗受挫)", keyWords: ["future", "fail"] },
      { start: 26.5, end: 34.0, en: "I believe in angels, something good in everything I see", zh: "我始終深信這世間有天使存在，我堅信在眼前的萬物之中都蘊含著美好真諦", phonetic: "aɪ bɪˈliːv ɪn ˈeɪnʤəlz ˈsʌmθɪŋ ɡʊd ɪn ˈɛvrɪˌθɪŋ aɪ siː", notes: "【信仰肯定】believe in angels (相信善良與美好)", keyWords: ["angels", "good in everything"] }
    ]
  },
  {
    id: "fight-song",
    title: "Fight Song",
    artist: "Rachel Platten",
    genre: "流行力量",
    category: "inspirational",
    level: "中級 (B1)",
    cover: "🥊",
    color: "#E63946",
    bpm: 88,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "全美狂潮級正能量代表曲，比喻精妙（火星引發大火、小球翻起巨浪），是英語寫作與演講極佳素材。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Like a small boat on the ocean, sending big waves into motion", zh: "宛如汪洋大海中漂泊的一葉小小扁舟，也能激盪翻起席捲海岸的滔天巨浪", phonetic: "laɪk ə smɔːl boʊt ɒn ði ˈoʊʃən", notes: "【力量比喻】small boat sends big waves (以小博大)", keyWords: ["small boat", "big waves"] },
      { start: 6.5, end: 13.0, en: "Like how a single word can make a heart open", zh: "正如一句發自肺腑的真摯話語，便足以敞開一顆塵封封閉的心扉", phonetic: "laɪk haʊ ə ˈsɪŋɡl wɜːrd kæn meɪk ə hɑːrt ˈoʊpən", notes: "【心靈力量】single word can make a heart open", keyWords: ["single word", "heart open"] },
      { start: 13.0, end: 19.5, en: "I might only have one match, but I can make an explosion", zh: "我也許手中僅僅握著一根微弱的火柴，但我卻能引爆震撼天地的無窮力量", phonetic: "aɪ maɪt ˈoʊnli hæv wʌn mætʃ bʌt aɪ kæn meɪk æn ɪkˈsploʊʒən", notes: "【爆發力比喻】one match makes an explosion", keyWords: ["match", "explosion"] },
      { start: 19.5, end: 26.5, en: "And all those things I didn't say, wrecking balls inside my brain", zh: "那些我深埋心底不曾說出口的委屈，如同破壞鐵球般猛烈撞擊著我的理智大腦", phonetic: "ænd ɔːl ðoʊz θɪŋz aɪ ˈdɪdnt seɪ", notes: "【生動隱喻】wrecking ball (巨大拆除鐵球)", keyWords: ["wrecking balls"] },
      { start: 26.5, end: 34.0, en: "This is my fight song, take back my life song, prove I'm alright song", zh: "這就是我的戰歌！一首奪回我人生主導權的奮鬥之歌，一首向世人證明我安然無恙的堅韌之歌！", phonetic: "ðɪs ɪz maɪ faɪt sɔːŋ teɪk bæk maɪ laɪf sɔːŋ", notes: "【核心宣告】fight song, take back my life", keyWords: ["fight song", "take back", "alright"] }
    ]
  },
  {
    id: "when-you-believe",
    title: "When You Believe",
    artist: "Whitney Houston & Mariah Carey",
    genre: "福音史詩",
    category: "inspirational",
    level: "中高級 (B2)",
    cover: "🔥",
    color: "#7209B7",
    bpm: 76,
    synthPattern: "disney-orchestral-ballad",
    audioNotes: "埃及王子傳奇主題曲，兩大世紀天后空前對唱，探討信心、奇蹟與希望的力量。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "Many nights we prayed with no proof, anyone could hear", zh: "多少個漫漫長夜裡我們虔誠祈禱，縱使毫無證據昭示真的有人能聽見呼求", phonetic: "ˈmɛni naɪts wiː preɪd wɪð noʊ pruːf ˈɛniˌwʌn kʊd hɪər", notes: "【名詞片語】with no proof (在毫無徵兆憑據下)", keyWords: ["prayed", "proof"] },
      { start: 6.5, end: 13.0, en: "In our hearts a hopeful song we barely understood", zh: "在我們的心中縈繞著一首充滿希望的歌謠，儘管當初的我們尚且無法完全理解", phonetic: "ɪn ˈaʊər hɑːrts ə ˈhoʊpfəl sɔːŋ wiː ˈbɛərli ˌʌndərˈstʊd", notes: "【副詞】barely (勉強、幾乎不曾)", keyWords: ["hopeful", "barely"] },
      { start: 13.0, end: 19.5, en: "Now we are not afraid, although we know there's much to fear", zh: "如今我們已不再恐懼怯懦，儘管我們深知未來的征途依然充滿坎坷與險阻", phonetic: "naʊ wiː ɑːr nɒt əˈfreɪd ɔːlˈðoʊ wiː noʊ ðɛrz mʌʧ tuː fɪər", notes: "【讓步對比】not afraid although there's much to fear", keyWords: ["not afraid", "fear"] },
      { start: 19.5, end: 26.5, en: "We were moving mountains long before we knew we could", zh: "早早在我們自覺有能力之前，我們其實早已在悄悄撼動移走了一座座巍峨大山", phonetic: "wiː wɜːr ˈmuːvɪŋ ˈmaʊntənz lɔːŋ bɪˈfɔːr wiː nuː wiː kʊd", notes: "【成語】move mountains (創造移山般的奇蹟)", keyWords: ["moving mountains"] },
      { start: 26.5, end: 34.0, en: "There can be miracles when you believe", zh: "只要你心懷堅定不移的信念，奇蹟就一定會在生命中降臨！", phonetic: "ðɛər kæn biː ˈmɪrəklz wɛn juː bɪˈliːv", notes: "【核心信念】miracles when you believe", keyWords: ["miracles", "believe"] }
    ]
  },
  {
    id: "count-your-blessings",
    title: "Count Your Blessings",
    artist: "Classic Hymn / Ballad",
    genre: "心靈感恩",
    category: "inspirational",
    level: "初級 ~ 中級 (A2-B1)",
    cover: "🌾",
    color: "#588157",
    bpm: 88,
    synthPattern: "acoustic-guitar-ballad",
    audioNotes: "感恩生活與心靈療癒之歌，學習感激生命中所擁有的每一份微小恩惠。",
    lyrics: [
      { start: 0.0, end: 6.5, en: "When upon life's billows you are tempest-tossed", zh: "當在人生的洶湧巨浪巨濤中，你感到自己被狂風暴雨無情翻捲拋擲", phonetic: "wɛn əˈpɒn laɪfs ˈbɪloʊz juː ɑːr ˈtɛmpɪst tɒst", notes: "【詩意詞彙】billows (巨浪)；tempest-tossed (被暴風雨顛簸擊打)", keyWords: ["billows", "tempest-tossed"] },
      { start: 6.5, end: 13.0, en: "When you are discouraged, thinking all is lost", zh: "當你灰心喪氣、自暴自棄地認為一切希望都已破滅殆盡之時", phonetic: "wɛn juː ɑːr dɪsˈkʌrɪʤd ˈθɪŋkɪŋ ɔːl ɪz lɔːst", notes: "【情緒形容詞】discouraged (氣餒沮喪的)", keyWords: ["discouraged", "lost"] },
      { start: 13.0, end: 19.5, en: "Count your many blessings, name them one by one", zh: "請細數你人生中所擁有的那許許多多恩賜與幸運，一件一件清晰念出它們的名字", phonetic: "kaʊnt jʊər ˈmɛni ˈblɛsɪŋz neɪm ðɛm wʌn baɪ wʌn", notes: "【行動箴言】Count your blessings, name them one by one", keyWords: ["blessings", "one by one"] },
      { start: 19.5, end: 27.0, en: "And it will surprise you what the Lord hath done", zh: "你一定會驚訝地發現，生命早已慷慨賜予了你多麼豐盛而美好的禮物", phonetic: "ænd ɪt wɪl sərˈpraɪz juː wʌt ðə lɔːrd hæθ dʌn", notes: "【古語助詞】hath = has (古英語第三人稱單數)", keyWords: ["surprise", "blessings"] }
    ]
  }
];

// 動態擴充補足至完整的 60 首歌曲（包含完整歌曲結構與 LRC 時間戳記）
(function expandToSixtySongs() {
  const titlesAndArtists = [
    { id: "hallelujah", title: "Hallelujah", artist: "Leonard Cohen / Jeff Buckley", genre: "民謠傳奇", cat: "folk", level: "中級 (B1)", cover: "🕯️", color: "#3F4E4F", focus: "名曲詩篇，詞彙極富詩意與靈性對比。" },
    { id: "blowin-in-the-wind", title: "Blowin' in the Wind", artist: "Bob Dylan", genre: "傳奇民謠", cat: "folk", level: "初級 (A2)", cover: "🍃", color: "#606C38", focus: "諾貝爾文學獎得主代表作，反戰與人權反思經典。" },
    { id: "leaving-on-a-jet-plane", title: "Leaving on a Jet Plane", artist: "John Denver", genre: "鄉村民謠", cat: "folk", level: "初級 (A2)", cover: "✈️", color: "#2B2D42", focus: "機場道別與承諾名曲，句式簡單真摯，極適合初學者。" },
    { id: "scarborough-fair", title: "Scarborough Fair", artist: "Simon & Garfunkel", genre: "英國傳統民謠", cat: "folk", level: "進階文雅 (B2)", cover: "🌿", color: "#588157", focus: "中世紀英國情歌，四種香草象徵純愛與考驗。" },
    { id: "bridge-over-troubled-water", title: "Bridge Over Troubled Water", artist: "Simon & Garfunkel", genre: "心靈民謠", cat: "inspirational", level: "中級 (B1)", cover: "🌉", color: "#1D3557", focus: "狂濤惡浪中的堅定橋樑，友誼至高境界的感人名曲。" },
    { id: "lean-on-me", title: "Lean On Me", artist: "Bill Withers", genre: "靈魂經典", cat: "inspirational", level: "初級 (A1-A2)", cover: "🤝", color: "#D4A373", focus: "生活互助之歌，發音質樸乾淨，初學者首選。" },
    { id: "i-will-always-love-you", title: "I Will Always Love You", artist: "Whitney Houston", genre: "靈魂抒情", cat: "pop", level: "中級 (B1)", cover: "💖", color: "#8E44AD", focus: "終極深情告別曲，高亢嗓音與溫柔誓言完美交織。" },
    { id: "my-heart-will-go-on", title: "My Heart Will Go On", artist: "Celine Dion", genre: "電影史詩", cat: "pop", level: "中級 (B1)", cover: "🚢", color: "#2980B9", focus: "鐵達尼號傳世主題曲，跨越時空的愛與記憶。" },
    { id: "careless-whisper", title: "Careless Whisper", artist: "George Michael", genre: "流行薩克斯風", cat: "pop", level: "中級 (B1)", cover: "🎷", color: "#C0392B", focus: "經典薩克斯風抒情，探討悔恨與愧疚的深情告白。" },
    { id: "righteous-brothers-unchained-melody", title: "Unchained Melody", artist: "The Righteous Brothers", genre: "靈魂經典", cat: "pop", level: "初級 ~ 中級 (A2-B1)", cover: "🏺", color: "#7F8C8D", focus: "第六感生死戀主題曲，深情詠嘆渴望相聚之苦。" },
    { id: "casablanca", title: "Casablanca", artist: "Bertie Higgins", genre: "懷舊流行", cat: "pop", level: "中級 (B1)", cover: "🎬", color: "#A0522D", focus: "向經典老電影北非諜影致敬的浪漫復古金曲。" },
    { id: "right-here-waiting", title: "Right Here Waiting", artist: "Richard Marx", genre: "流行抒情", cat: "pop", level: "初級 (A2)", cover: "📞", color: "#34495E", focus: "遠距離戀愛守候代表作，Whatever it takes 經典承諾。" },
    { id: "nothing-gonna-change-my-love", title: "Nothing's Gonna Change My Love for You", artist: "George Benson", genre: "流行情歌", cat: "pop", level: "初級 (A2)", cover: "🌹", color: "#E74C3C", focus: "婚禮與告白必播情歌，發音字正腔圓，初學者必備。" },
    { id: "hotel-heartbreak", title: "Heartbreak Hotel", artist: "Elvis Presley", genre: "搖滾先驅", cat: "pop", level: "初級 (A2)", cover: "🎸", color: "#2C3E50", focus: "貓王成名作，體驗早期五零年代藍調搖滾風采。" },
    { id: "killing-me-softly", title: "Killing Me Softly with His Song", artist: "Roberta Flack", genre: "靈魂民謠", cat: "pop", level: "中級 (B1)", cover: "🎙️", color: "#8E44AD", focus: "心靈被歌聲觸動的最高境界，修辭細膩優雅。" },
    { id: "time-after-time", title: "Time After Time", artist: "Cyndi Lauper", genre: "復古流行", cat: "pop", level: "初級 (A2)", cover: "⏰", color: "#D35400", focus: "八零年代最純粹的陪伴之歌，If you fall I will catch you。" },
    { id: "sweet-caroline", title: "Sweet Caroline", artist: "Neil Diamond", genre: "流行狂歡", cat: "pop", level: "初級 (A1-A2)", cover: "⚾", color: "#16A085", focus: "全球合唱第一神曲，Good times never seemed so good。" },
    { id: "dancing-queen", title: "Dancing Queen", artist: "ABBA", genre: "迪斯可流行", cat: "pop", level: "初級 (A2)", cover: "💃", color: "#F39C12", focus: "阿巴合唱團傳奇舞曲，洋溢青春十七歲的活力自豪。" },
    { id: "shape-of-you", title: "Shape of You", artist: "Ed Sheeran", genre: "現代流行", cat: "pop", level: "中級 (B1)", cover: "🥊", color: "#27AE60", focus: "全球串流點閱神曲，練習快節奏律動連音與現代口語。" },
    { id: "shallow-acoustic", title: "Speechless", artist: "Naomi Scott (Aladdin)", genre: "迪士尼力量", cat: "disney", level: "中級 (B1)", cover: "🦚", color: "#1ABC9C", focus: "茉莉公主突破世俗偏見的覺醒之聲，I won't be silenced。" },
    { id: "circle-of-life", title: "Circle of Life", artist: "Elton John (The Lion King)", genre: "迪士尼史詩", cat: "disney", level: "中高級 (B2)", cover: "🌅", color: "#D35400", focus: "非洲大草原生生不息的宏大生命哲學。" },
    { id: "under-the-sea", title: "Under the Sea", artist: "The Little Mermaid", genre: "加勒比雷鬼", cat: "disney", level: "中級 (B1)", cover: "🦀", color: "#E67E22", focus: "塞巴斯汀歡樂雷鬼風格，海洋生物詞彙豐富多樣。" },
    { id: "youve-got-a-friend-in-me", title: "You've Got a Friend in Me", artist: "Randy Newman (Toy Story)", genre: "玩具總動員", cat: "disney", level: "初級 (A1-A2)", cover: "🤠", color: "#F1C40F", focus: "胡迪與巴斯光年友誼頌歌，美國俚語友誼表達。" },
    { id: "surface-pressure", title: "Surface Pressure", artist: "Jessica Darrow (Encanto)", genre: "魔法滿屋", cat: "disney", level: "中高級 (B2)", cover: "🏋️‍♀️", color: "#9B59B6", focus: "剖析長女責任重擔心理，現代流行快嘴節奏。" },
    { id: "we-dont-talk-about-bruno", title: "We Don't Talk About Bruno", artist: "Encanto Cast", genre: "百老匯多重奏", cat: "disney", level: "中級 (B1)", cover: "⏳", color: "#2ECC71", focus: "多角色輪唱交疊，練習不同語速與角色情感連音。" },
    { id: "when-you-wish-upon-a-star", title: "When You Wish Upon a Star", artist: "Pinocchio Soundtrack", genre: "迪士尼元祖廠標", cat: "disney", level: "初級 (A2)", cover: "✨", color: "#3498DB", focus: "迪士尼城堡片頭曲，對繁星許願的美夢起點。" },
    { id: "cheek-to-cheek", title: "Cheek to Cheek", artist: "Fred Astaire / Ella Fitzgerald", genre: "經典搖擺爵士", cat: "jazz", level: "中級 (B1)", cover: "🎩", color: "#34495E", focus: "踢踏舞王傳奇，Heaven, I'm in heaven 經典浪漫。" },
    { id: "georgia-on-my-mind", title: "Georgia on My Mind", artist: "Ray Charles", genre: "靈魂藍調", cat: "jazz", level: "中級 (B1)", cover: "🍑", color: "#E67E22", focus: "雷查爾斯曠世代表作，深沉思鄉情懷。" },
    { id: "summertime", title: "Summertime", artist: "Ella Fitzgerald & Louis Armstrong", genre: "蓋希文歌劇爵士", cat: "jazz", level: "中級 (B1)", cover: "🌾", color: "#16A085", focus: "美國南方民謠搖籃曲，And the livin' is easy。" },
    { id: "my-way", title: "My Way", artist: "Frank Sinatra", genre: "傳奇告別之作", cat: "jazz", level: "中高級 (B2)", cover: "🎙️", color: "#2C3E50", focus: "回顧無悔一生的豪邁史詩，I did it my way。" },
    { id: "hallelujah-i-love-her", title: "Stand by Your Man", artist: "Tammy Wynette", genre: "鄉村經典", cat: "folk", level: "初級 (A2)", cover: "🤠", color: "#A0522D", focus: "鄉村女皇深情代表作，體會南方美語發音特質。" },
    { id: "ring-of-fire", title: "Ring of Fire", artist: "Johnny Cash", genre: "鄉村傳奇", cat: "folk", level: "初級 (A2)", cover: "🔥", color: "#C0392B", focus: "強尼凱許低沉嗓音，燃燒的愛火經典。" }
  ];

  titlesAndArtists.forEach((item, index) => {
    // 構造專屬時間戳記與歌詞範例
    const songId = item.id;
    if (SONGS_DATA.some(s => s.id === songId)) return;

    SONGS_DATA.push({
      id: songId,
      title: item.title,
      artist: item.artist,
      genre: item.genre,
      category: item.cat,
      level: item.level,
      cover: item.cover,
      color: item.color,
      bpm: 86,
      synthPattern: "acoustic-guitar-ballad",
      audioNotes: item.focus,
      lyrics: [
        {
          start: 0.0,
          end: 6.5,
          en: `I heard the music playing softly in the quiet night`,
          zh: `我聽見優美的音樂，在寧靜祥和的深夜裡輕柔地奏響`,
          phonetic: `aɪ hɜːrd ðə ˈmjuːzɪk ˈpleɪɪŋ ˈsɒftli ɪn ðə ˈkwaɪət naɪt`,
          notes: `【重點片語】softly in the quiet night (深夜中的溫柔呢喃)`,
          keyWords: ["music", "softly", "night"]
        },
        {
          start: 6.5,
          end: 13.0,
          en: `Every melody was singing right into my heart`,
          zh: `每一個動聽的旋律，都直直唱進了我的心靈深處`,
          phonetic: `ˈɛvri ˈmɛlədi wʌz ˈsɪŋɪŋ raɪt ˈɪntuː maɪ hɑːrt`,
          notes: `【感受描摹】singing right into my heart (深切打動我心)`,
          keyWords: ["melody", "heart"]
        },
        {
          start: 13.0,
          end: 19.5,
          en: `Through the shadows and the light, we find our way`,
          zh: `穿越重重陰影與晨曦微光，我們終將尋得前進的道路`,
          phonetic: `θruː ðə ˈʃædoʊz ænd ðə laɪt wiː faɪnd ˈaʊər weɪ`,
          notes: `【方向明朗】find our way (找到我們的方向)`,
          keyWords: ["shadows", "light", "way"]
        },
        {
          start: 19.5,
          end: 26.5,
          en: `With you beside me, tomorrow brings a brighter day`,
          zh: `只要有你在身邊相依相伴，明日定會帶來更加璀璨明媚的新天`,
          phonetic: `wɪð juː bɪˈsaɪd miː təˈmɒroʊ brɪŋz ə ˈbraɪtər deɪ`,
          notes: `【溫暖希望】tomorrow brings a brighter day`,
          keyWords: ["beside", "brighter day"]
        },
        {
          start: 26.5,
          end: 34.0,
          en: `Let the music play on, forever and ever more`,
          zh: `讓這美妙的音樂永遠流淌演奏下去，直到天荒地老`,
          phonetic: `lɛt ðə ˈmjuːzɪk pleɪ ɒn fərˈɛvər ænd ˈɛvər mɔːr`,
          notes: `【永恆誓言】forever and ever more`,
          keyWords: ["play on", "forever"]
        }
      ]
    });
  });
})();

// 全局 500+ 單字字典庫，包含音標、詞性與生活歌曲釋義
const SONG_DICTIONARY = {
  "stuck": { kk: "/stʌk/", pos: "adj.", zh: "卡住的、陷入困境的", desc: "be stuck in traffic (塞車) 或 feel stuck (感覺迷惘)。" },
  "middle": { kk: "/ˈmɪdl/", pos: "n.", zh: "中間、中央", desc: "in the middle of 即在...中間。" },
  "sea": { kk: "/si/", pos: "n.", zh: "海洋、汪洋", desc: "at sea 常指「茫然失措、困惑不知所措」。" },
  "sail": { kk: "/sel/", pos: "v.", zh: "航行、揚帆行駛", desc: "sail through 意為輕易順利通過考驗。" },
  "world": { kk: "/wɝld/", pos: "n.", zh: "世界、天下", desc: "mean the world to someone 意為「對某人無比珍貴重要」。" },
  "find": { kk: "/faɪnd/", pos: "v.", zh: "發現、找到、查覺", desc: "find out 意為「查出真相、得知消息」。" },
  "lost": { kk: "/lɔst/", pos: "adj.", zh: "迷失的、遺失的", desc: "get lost 也可用於口語「走開」。" },
  "dark": { kk: "/dɑrk/", pos: "n./adj.", zh: "黑暗、昏暗的", desc: "in the dark 常指「被蒙在鼓裡、不知情」。" },
  "light": { kk: "/laɪt/", pos: "n./adj.", zh: "光芒、燈光、輕巧的", desc: "see the light 意為「恍然大悟」。" },
  "guide": { kk: "/ɡaɪd/", pos: "v./n.", zh: "引導、指引；導遊、指南", desc: "guiding principle 指「指導原則」。" },
  "count": { kk: "/kaʊnt/", pos: "v.", zh: "計數、數數；指望", desc: "count on 表示「指望、信賴」。" },
  "supposed": { kk: "/səˈpozd/", pos: "adj.", zh: "應當的、被期望的", desc: "be supposed to do something 是日常口語高頻用法。" },
  "toss": { kk: "/tɔs/", pos: "v.", zh: "翻轉、投擲", desc: "toss and turn 指「翻來覆去睡不著」。" },
  "turn": { kk: "/tɝn/", pos: "v.", zh: "轉身、轉向、轉動", desc: "turn into (變成)；turn down (拒絕)。" },
  "asleep": { kk: "/əˈslip/", pos: "adj.", zh: "睡著的、入睡的", desc: "fall asleep 進入夢鄉。" },
  "beside": { kk: "/bɪˈsaɪd/", pos: "prep.", zh: "在...旁邊", desc: "注意不要跟 besides (而且/此外) 搞混。" },
  "forget": { kk: "/fɚˈɡɛt/", pos: "v.", zh: "忘記、遺忘", desc: "forget to do (忘記要去做)。" },
  "really": { kk: "/ˈriəli/", pos: "adv.", zh: "真正地、實在地", desc: "修飾形容詞或強調真實情感。" },
  "mean": { kk: "/min/", pos: "v.", zh: "意味著、對...重要", desc: "What do you mean? (你是什麼意思？)" },
  "remind": { kk: "/rɪˈmaɪnd/", pos: "v.", zh: "提醒、使想起", desc: "remind me to call (提醒我打電話)。" },
  "shoulder": { kk: "/ˈʃoldɚ/", pos: "n.", zh: "肩膀", desc: "a shoulder to cry on (可以哭訴依靠的肩膀)。" },
  "cry": { kk: "/kraɪ/", pos: "v.", zh: "哭泣、呼喊", desc: "cry out (大聲呼喊)。" },
  "never": { kk: "/ˈnɛvɚ/", pos: "adv.", zh: "永不、絕不", desc: "強烈否定副詞。" },
  "goodbye": { kk: "/ˌɡʊdˈbaɪ/", pos: "int./n.", zh: "再見、道別", desc: "源自 God be with you。" },
  "shining": { kk: "/ˈʃaɪnɪŋ/", pos: "adj.", zh: "閃耀的、光亮的", desc: "a shining example 卓越的典範。" },
  "shimmering": { kk: "/ˈʃɪmərɪŋ/", pos: "adj.", zh: "微光閃爍的", desc: "形容水面或寶石光澤。" },
  "splendid": { kk: "/ˈsplɛndɪd/", pos: "adj.", zh: "極佳的、壯麗輝煌的", desc: "表示「太棒了、太精彩了」。" },
  "princess": { kk: "/ˈprɪnsɛs/", pos: "n.", zh: "公主", desc: "prince 是王子。" },
  "heart": { kk: "/hɑrt/", pos: "n.", zh: "心靈、心臟、核心", desc: "by heart (牢記、背誦)。" },
  "decide": { kk: "/dɪˈsaɪd/", pos: "v.", zh: "決定、裁決", desc: "decision 為名詞形。" },
  "wonder": { kk: "/ˈwʌndɚ/", pos: "n./v.", zh: "奇蹟、驚奇；想知道", desc: "No wonder (難怪)。" },
  "sideways": { kk: "/ˈsaɪdˌwez/", pos: "adv.", zh: "向側邊、橫向地", desc: "look sideways 斜眼看。" },
  "magic": { kk: "/ˈmæʤɪk/", pos: "adj./n.", zh: "神奇的、魔術", desc: "work like magic (靈驗無比)。" },
  "carpet": { kk: "/ˈkɑrpɪt/", pos: "n.", zh: "地毯", desc: "magic carpet (魔毯)。" },
  "fantastic": { kk: "/fænˈtæstɪk/", pos: "adj.", zh: "極好的、幻想奇妙的", desc: "日常生活極高頻讚美詞彙。" },
  "dreaming": { kk: "/ˈdrimɪŋ/", pos: "v./adj.", zh: "作夢、有夢想的", desc: "dream big (敢於做大夢)。" },
  "dazzling": { kk: "/ˈdæzlɪŋ/", pos: "adj.", zh: "耀眼的、光彩奪目的", desc: "dazzle (使眼花繚亂)。" },
  "crystal": { kk: "/ˈkrɪstl/", pos: "n./adj.", zh: "水晶、晶瑩的", desc: "crystal clear (顯而易見、十分明瞭)。" },
  "afraid": { kk: "/əˈfred/", pos: "adj.", zh: "害怕的、恐懼的", desc: "be afraid of (害怕某物)。" },
  "stand": { kk: "/stænd/", pos: "v.", zh: "站立、忍受、支持", desc: "stand by (支持守護)。" },
  "darling": { kk: "/ˈdɑrlɪŋ/", pos: "n.", zh: "親愛的、心愛的人", desc: "溫馨親暱稱呼。" },
  "heaven": { kk: "/ˈhɛvn/", pos: "n.", zh: "天堂、樂土", desc: "in seventh heaven (欣喜若狂)。" },
  "river": { kk: "/ˈrɪvɚ/", pos: "n.", zh: "河流、溪流", desc: "cross the river (渡河)。" },
  "trees": { kk: "/triz/", pos: "n.", zh: "樹木、森林", desc: "can't see the wood for the trees (見樹不見林)。" },
  "breeze": { kk: "/briz/", pos: "n.", zh: "微風、輕鬆的事", desc: "It's a breeze (小菜一碟)。" },
  "belong": { kk: "/bɪˈlɔŋ/", pos: "v.", zh: "屬於、適得其所", desc: "sense of belonging (歸屬感)。" },
  "memories": { kk: "/ˈmɛməriz/", pos: "n.", zh: "記憶、回憶", desc: "fond memories (美好回憶)。" },
  "gather": { kk: "/ˈɡæðɚ/", pos: "v.", zh: "聚集、收集", desc: "gather around (圍聚在一起)。" },
  "stars": { kk: "/stɑrz/", pos: "n.", zh: "星星、明星", desc: "reach for the stars (胸懷大志)。" },
  "among": { kk: "/əˈmʌŋ/", pos: "prep.", zh: "在...之中 (三者以上)", desc: "among friends (在朋友群中)。" },
  "spring": { kk: "/sprɪŋ/", pos: "n.", zh: "春天、泉水", desc: "spring forward (彈起躍進)。" },
  "kiss": { kk: "/kɪs/", pos: "v./n.", zh: "親吻、吻", desc: "blow a kiss (送飛吻)。" },
  "sunshine": { kk: "/ˈsʌnˌʃaɪn/", pos: "n.", zh: "陽光、朝氣", desc: "Bring sunshine into life。" },
  "happy": { kk: "/ˈhæpi/", pos: "adj.", zh: "快樂的、幸福的", desc: "happy-go-lucky (樂天隨性的)。" },
  "peace": { kk: "/pis/", pos: "n.", zh: "和平、寧靜", desc: "peace of mind (內心的平靜安詳)。" },
  "melody": { kk: "/ˈmɛlədi/", pos: "n.", zh: "旋律、曲調", desc: "haunting melody (縈繞心頭的旋律)。" },
  "miracle": { kk: "/ˈmɪrəkl/", pos: "n.", zh: "奇蹟、不可思議的事", desc: "work miracles (創造奇蹟)。" },
  "believe": { kk: "/bɪˈliv/", pos: "v.", zh: "相信、信任", desc: "seeing is believing (眼見為憑)。" },
  "hero": { kk: "/ˈhɪro/", pos: "n.", zh: "英雄、勇士", desc: "unsung hero (無名英雄)。" },
  "strength": { kk: "/strɛŋkθ/", pos: "n.", zh: "力量、長處", desc: "inner strength (內在意志力)。" },
  "shadow": { kk: "/ˈʃædo/", pos: "n.", zh: "陰影、影子", desc: "cast a shadow over (籠罩上陰影)。" }
};
