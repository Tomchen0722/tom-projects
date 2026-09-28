/**
 * 字根字首魔法學院 (EtymoRoots Master)
 * 詞庫核心資料庫：涵蓋字首、字根、造字形態公式、KK/IPA音標、繁中詳解、例句及深度文法解析、主題篇章短文
 */
const ETYMO_DATA = [
  {
    id: "tele",
    name: "tele-",
    type: "prefix",
    typeLabel: "希臘語字首 (Greek Prefix)",
    etymology: "源自古希臘語「τῆλε」(tēle)，核心概念為「遠、遙遠、在遠距離之外 (far, at a distance)」。",
    originMeaning: "遠距離、遙遠",
    phonetic: "/ˈtɛli/ 或 /ˈtɛlə/",
    icon: "📡",
    color: "#D97706",
    summary: "用於表示跨越遙遠空間進行的傳遞、觀測、感知或移動。",
    words: [
      {
        word: "telephone",
        kk: "[ˈtɛləˌfon]",
        ipa: "/ˈtɛləˌfoʊn/",
        pos: "n. / v.",
        meaning: "電話；(v.) 打電話給...",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "phone", role: "base", meaning: "聲音、語音 (希臘語 phōnē)" }
          ],
          resultMeaning: "將遠方的聲音即時傳遞過來的裝置 ➔「電話」"
        },
        sentence: "The young inventor picked up the telephone to confirm whether his patent application had been approved by the federal office.",
        sentenceZh: "這位年輕發明家拿起電話，確認他的專利申請是否已獲得聯邦辦公室核准。",
        grammar: {
          pattern: "S + Vt + O + Adv Clause of Purpose (主詞 + 及物動詞 + 受詞 + 目的狀詞與名詞子句)",
          breakdown: [
            { part: "The young inventor", role: "主詞 (Subject)", note: "名詞片語，包含定冠詞與修飾形容詞 young。" },
            { part: "picked up", role: "及物動詞片語 (Phrasal Verb)", note: "過去簡單式，表示拿起通話筒的連續動作。" },
            { part: "the telephone", role: "直接受詞 (Direct Object)", note: "由 tele- + phone 構成的複合名詞。" },
            { part: "to confirm", role: "不定詞狀詞 (Infinitive of Purpose)", note: "表動作目的「為了確認...」。" },
            { part: "whether his patent application had been approved", role: "受詞名詞子句 (Noun Clause)", note: "whether 引導名詞子句作 confirm 之受詞；子句使用「過去完成被動態 (had been approved)」表示在 picked up 之前已完成之動作。" },
            { part: "by the federal office", role: "介系詞片語 (Agent)", note: "被動態之施事者 (Agent)。" }
          ],
          keyPoints: [
            "【時態搭配】：過去式 picked up 與過去完成被動態 had been approved 形成時間先後對比。",
            "【固定句型】：confirm + whether/if... 表示「確認是否...」。",
            "【詞源延伸】：phone 亦見於 symphony (交響樂)、microphone (麥克風)、phonetics (語音學)。"
          ]
        }
      },
      {
        word: "telescope",
        kk: "[ˈtɛləˌskop]",
        ipa: "/ˈtɛləˌskoʊp/",
        pos: "n.",
        meaning: "望遠鏡、天文望遠鏡",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "scope", role: "base", meaning: "看、觀察儀器 (希臘語 skopein)" }
          ],
          resultMeaning: "觀測遙遠星體或物體的儀器 ➔「望遠鏡」"
        },
        sentence: "Through the high-powered telescope, the astronomer observed a distant spiral galaxy that had remained hidden for centuries.",
        sentenceZh: "透過這架高倍率望遠鏡，天文學家觀測到一個隱匿了數個世紀之久的遙遠螺旋星系。",
        grammar: {
          pattern: "Adverbial Phrase + S + Vt + O + Relative Clause (介系詞狀詞 + 主詞 + 及物動詞 + 受詞 + 關係子句)",
          breakdown: [
            { part: "Through the high-powered telescope", role: "方式狀詞 (Adverbial of Means)", note: "介系詞 through 表示藉由某種儀器媒介，置於句首加強語氣。" },
            { part: "the astronomer", role: "主詞 (Subject)", note: "專指天文學家 (astro [星星] + nomer [研究者])。" },
            { part: "observed", role: "及物動詞 (Transitive Verb)", note: "及物動詞，過去式，受詞為星系。" },
            { part: "a distant spiral galaxy", role: "直接受詞 (Direct Object)", note: "雙重形容詞 distant (遙遠) 與 spiral (螺旋狀) 修飾 galaxy。" },
            { part: "that had remained hidden for centuries", role: "限定關係子句 (Defining Relative Clause)", note: "that 為主格關代，先行詞為 a distant spiral galaxy；remained 為連綴動詞，hidden 為分詞補語。" }
          ],
          keyPoints: [
            "【連綴動詞結構】：remain + adjective (hidden)，表示保持某種狀態。",
            "【時間介系詞】：for centuries 表示時間的持續長度（數百年之久）。",
            "【詞源延伸】：scope 同時也是顯微鏡 microscope (micro 微小 + scope 觀察) 的字根。"
          ]
        }
      },
      {
        word: "television",
        kk: "[ˈtɛləˌvɪʒən]",
        ipa: "/ˈtɛləˌvɪʒn/",
        pos: "n.",
        meaning: "電視、電視機、電視廣播",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "vision", role: "base", meaning: "視覺、影像 (拉丁語 visio / videre 看)" }
          ],
          resultMeaning: "將遠方的影像即時傳送至螢幕眼前的科技 ➔「電視」"
        },
        sentence: "The momentous announcement was broadcast live on television, captivating millions of viewers across the continent.",
        sentenceZh: "這項重大公告在電視上現場直播，吸引了整個大陸數百萬觀眾的目光。",
        grammar: {
          pattern: "S + Passive Predicate + Adverbial + Participial Construction (主詞 + 被動謂語 + 狀詞 + 現在分詞構句)",
          breakdown: [
            { part: "The momentous announcement", role: "主詞 (Subject)", note: "momentous (重大、具歷史意義的) 作形容詞修飾 announcement。" },
            { part: "was broadcast", role: "被動動詞 (Passive Predicate)", note: "broadcast 過去式與過去分詞同形 (broadcast-broadcast-broadcast)。" },
            { part: "live on television", role: "方式與地點副詞 (Adverbials)", note: "live 作副詞意為「現場實況地」，on television 為傳播媒介介系詞片語。" },
            { part: "captivating millions of viewers across the continent", role: "現在分詞構句 (Participle Clause)", note: "表伴隨結果（Result/Attendant Circumstance），相當於 and it captivated..." }
          ],
          keyPoints: [
            "【動詞特殊三態】：broadcast 常用同形 broadcast，避免寫成 broadcasted。",
            "【分詞構句應用】：現在分詞片語簡化了對等子句，使句子節奏緊湊流暢。",
            "【詞源延伸】：vision 衍生自拉丁語 videre (看)，同源字如 visible (可見的)、visit (拜訪)、provide (預見/提供)。"
          ]
        }
      },
      {
        word: "telegram",
        kk: "[ˈtɛləˌgræm]",
        ipa: "/ˈtɛləˌɡræm/",
        pos: "n.",
        meaning: "電報",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "gram", role: "base", meaning: "文字、寫作 (希臘語 gramma)" }
          ],
          resultMeaning: "透過遠距電信線路傳遞過來的文字書信 ➔「電報」"
        },
        sentence: "Before modern digital networks existed, diplomats relied on encrypted telegrams to transmit urgent state secrets.",
        sentenceZh: "在現代數位網路存在之前，外交官依靠加密電報來傳送緊急的國家機密。",
        grammar: {
          pattern: "Time Adverbial Clause + S + Vi + Prep Phrase + Infinitive of Purpose (時間副詞子句 + 主詞 + 不及物動詞 + 介系詞片語 + 目的不定詞)",
          breakdown: [
            { part: "Before modern digital networks existed", role: "時間副詞子句 (Time Clause)", note: "Before 引導從屬子句，述說歷史背景。" },
            { part: "diplomats", role: "主要子句主詞 (Subject)", note: "複數名詞「外交官」。" },
            { part: "relied on", role: "不及物動詞片語 (Phrasal Verb)", note: "rely on 為固定搭配，表示「依賴、倚靠」。" },
            { part: "encrypted telegrams", role: "受詞 (Object of Preposition)", note: "encrypted (加密的) 為過去分詞轉化形容詞。" },
            { part: "to transmit urgent state secrets", role: "目的狀詞 (Infinitive of Purpose)", note: "不定詞片語表 transmit (傳輸) 之目的。" }
          ],
          keyPoints: [
            "【分詞修飾】：encrypted (被加密的) 作前置修飾名詞 telegrams。",
            "【詞根網絡】：-gram (寫下的字/圖)，同根字如 diagram (圖表)、program (程式/節目)、grammar (文法)。"
          ]
        }
      },
      {
        word: "telepathy",
        kk: "[təˈlɛpəθi]",
        ipa: "/təˈlɛpəθi/",
        pos: "n.",
        meaning: "心靈感應、遠距知覺",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "pathy", role: "base", meaning: "感受、情感 (希臘語 pathos)" }
          ],
          resultMeaning: "跨越遠距空間直接感受他人的思緒 ➔「心靈感應」"
        },
        sentence: "Although mainstream scientists remain skeptical about telepathy, identical twins often report an instinctive mental resonance.",
        sentenceZh: "儘管主流科學家對心靈感應依然持懷疑態度，但同卵雙胞胎常聲稱彼此有一種本能的思維共鳴。",
        grammar: {
          pattern: "Concessive Clause + S + Vt + O (讓步副詞子句 + 主詞 + 及物動詞 + 受詞)",
          breakdown: [
            { part: "Although mainstream scientists remain skeptical about telepathy", role: "讓步副詞子句 (Clause of Concession)", note: "Although 引導子句；remain 為連綴動詞，skeptical 為形容詞主詞補語，固定搭配介系詞 about。" },
            { part: "identical twins", role: "主要子句主詞 (Subject)", note: "同卵雙胞胎。" },
            { part: "often report", role: "謂語動詞 (Predicate Verb)", note: "頻率副詞 often 置於一般動詞 report 之前。" },
            { part: "an instinctive mental resonance", role: "受詞 (Direct Object)", note: "instinctive (本能的) 與 mental (心理的) 共同修飾 resonance (共鳴)。" }
          ],
          keyPoints: [
            "【連綴動詞搭配】：remain + adj. + about...，表示對某事維持某種評價態度。",
            "【詞根網絡】：-pathy (情感/痛苦)，同根字如 sympathy (同情心)、empathy (同理心)、apathy (漠不關心)。"
          ]
        }
      },
      {
        word: "teleport",
        kk: "[ˈtɛləˌpɔrt]",
        ipa: "/ˈtɛləpɔːrt/",
        pos: "v. / n.",
        meaning: "(v.) 瞬間移動、心靈傳送；(n.) 傳送",
        formula: {
          parts: [
            { text: "tele-", role: "prefix", meaning: "遠距離 (希臘語 tēle)" },
            { text: "port", role: "base", meaning: "運送、搬移 (拉丁語 portare)" }
          ],
          resultMeaning: "將物質或人體瞬間搬移至遠方 ➔「瞬間移動」"
        },
        sentence: "In theoretical physics, subatomic particles can teleport across quantum energy barriers without traversing the physical distance.",
        sentenceZh: "在理論物理學中，亞原子粒子能夠穿過量子能量壁壘進行瞬間移動，而無需實際穿越物理距離。",
        grammar: {
          pattern: "Domain Adverbial + S + Modal + Vi + Directional Preposition + Without-Gerund (領域狀詞 + 主詞 + 助動詞 + 不及物動詞 + 介系詞方向片語 + 否定伴隨動名詞)",
          breakdown: [
            { part: "In theoretical physics", role: "領域狀詞 (Domain Adverbial)", note: "設定陳述成立的科學語境。" },
            { part: "subatomic particles", role: "主詞 (Subject)", note: "sub- (次/亞) + atomic (原子的) + particles (粒子)。" },
            { part: "can teleport", role: "謂語 (Modal Predicate)", note: "情態助動詞 can + 原形動詞 teleport。" },
            { part: "across quantum energy barriers", role: "空間介系詞片語 (Directional Prep Phrase)", note: "across 表示穿過或跨越障礙。" },
            { part: "without traversing the physical distance", role: "否定伴隨狀詞 (Adverbial of Condition/Manner)", note: "介系詞 without 後接動名詞 traversing。" }
          ],
          keyPoints: [
            "【否定伴隨結構】：without + V-ing，表達「在未執行某動作的前提下」。",
            "【雙重字根融合】：希臘語 tele- (遠) 與拉丁語 portare (運送) 的現代科學新創詞。"
          ]
        }
      }
    ],
    article: {
      title: "Echoes Across the Void: The Tele- Revolution",
      titleZh: "跨越虛空的迴響：遠距溝通的文明革命",
      intro: "人類文明的躍進，本質上就是一場克服「空間距離 (tele)」的史詩奮鬥。從古希臘字根 tele- 萌發的那一刻起，語言便預示了人類對連結宇宙深處的渴望。",
      paragraphs: [
        {
          en: "Long before modern satellites orbited our planet, ancient scholars could only dream of witnessing phenomena occurring beyond human eyesight. Through the earliest optical telescope, Galileo first unveiled mountains on the Moon, proving that humanity could bridge distant celestial frontiers.",
          zh: "早在現代人造衛星環繞地球運行之前，古代學者只能夢想目睹超越人類肉眼所能及的遙遠現象。藉由最初的光學望遠鏡，伽利略首次揭開了月球表面的山脈，證明了人類能跨越遙遠的天體疆界。"
        },
        {
          en: "As industrial commerce expanded across continents, diplomats urgently required instantaneous communication. The invention of the telegram allowed coded electrical pulses to transmit critical decisions within hours instead of weeks, laying the groundwork for the modern information highway.",
          zh: "隨著工業商業版圖跨越各大洲擴張，外交官迫切需要即時通訊。電報的發明使得編碼電脈衝能在數小時內（而非數週）傳送關鍵決策，為現代資訊高速公路奠定了基石。"
        },
        {
          en: "Soon, Alexander Graham Bell revolutionized human intimacy with the telephone, enabling people to hear the vocal inflections of their loved ones from thousands of miles away. Decades later, television brought living history into every household, transforming isolated communities into a global village.",
          zh: "不久之後，亞歷山大·貝爾以電話徹底改變了人與人之間的親密連結，讓人們在數千英里之外也能聽見摯愛之人話語中的抑揚頓挫。數十年後，電視更將活生生的歷史帶進千家萬戶，把孤立的社群轉化為地球村。"
        },
        {
          en: "Today, visionary physicists explore whether quantum entanglement might allow information to teleport across the universe, while mystics still ponder the mysteries of telepathy. Regardless of where technology leads us, the Greek prefix tele- will always remind us that human curiosity never stops reaching toward the distant unknown.",
          zh: "今天，富有遠見的物理學家正在探索量子糾纏是否能使資訊在全宇宙進行瞬間傳送，而神秘學家依然沉思著心靈感應的奧秘。無論科技將我們帶往何方，希臘語字首 tele- 將永遠提醒著我們：人類對遙遠未知的探索好奇心永無止境。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What fundamental human challenge does the prefix 'tele-' address in the article?",
          qZh: "文章中字首 'tele-' 主要解決了人類哪項基本挑戰？",
          options: [
            "A. Overcoming physical spatial distance (克服實體空間距離)",
            "B. Generating artificial intelligence (製造人工智慧)",
            "C. Healing chronic medical illnesses (治療慢性疾病)",
            "D. Exploring underwater caverns (探索水下洞穴)"
          ],
          answer: 0,
          explanation: "文中開宗明義指出人類文明就是一場克服「空間距離 (tele)」的奮鬥。"
        },
        {
          q: "According to the passage, how did the telegram transform communication compared to earlier eras?",
          qZh: "根據文章，電報相比於早期時代如何轉變了通訊方式？",
          options: [
            "A. It transmitted high-definition color images across space.",
            "B. It reduced message transmission time from weeks to mere hours. (將訊息傳送時間從數週縮短至數小時)",
            "C. It replaced all spoken verbal languages.",
            "D. It allowed physical teleportation of heavy cargo."
          ],
          answer: 1,
          explanation: "文中述及電報能讓編碼電脈衝在「within hours instead of weeks」傳送關鍵決策。"
        }
      ]
    }
  },
  {
    id: "prot",
    name: "prot- / proto-",
    type: "prefix",
    typeLabel: "希臘語字首 (Greek Prefix)",
    etymology: "源自古希臘語「πρῶτος」(prôtos)，原意為「第一、最初、最前、原始、始祖 (first, earliest, original)」。亦延伸至拉丁語系 pro- (向前、防衛)。",
    originMeaning: "第一、最初、原始、前鋒",
    phonetic: "/ˈproʊtə/ 或 /ˈproʊtoʊ/",
    icon: "🥇",
    color: "#059669",
    summary: "用於表示生命、科技、文學或法規之演進起點，或最先開創、領銜的第一個原型。",
    words: [
      {
        word: "prototype",
        kk: "[ˈprotəˌtaɪp]",
        ipa: "/ˈproʊtəˌtaɪp/",
        pos: "n. / v.",
        meaning: "原型、雛形、典型樣品；(v.) 製作原型",
        formula: {
          parts: [
            { text: "proto-", role: "prefix", meaning: "最初、第一 (希臘語 prôtos)" },
            { text: "type", role: "base", meaning: "模型、樣態 (希臘語 typos 烙印/鑄模)" }
          ],
          resultMeaning: "最初鑄造出來的第一個樣品模型 ➔「原型、雛形」"
        },
        sentence: "The aerospace engineers subjected the working prototype to rigorous wind tunnel testing before launching mass production.",
        sentenceZh: "航太工程師在展開量產之前，對該運作原型進行了嚴格的風洞測試。",
        grammar: {
          pattern: "S + Vt + O + Prep Phrase + Prepositional Gerund (主詞 + 及物動詞 + 受詞 + 介系詞片語 + 介系詞動名詞時間片語)",
          breakdown: [
            { part: "The aerospace engineers", role: "主詞 (Subject)", note: "複合名詞詞組作句子的執行主體。" },
            { part: "subjected", role: "及物動詞 (Transitive Verb)", note: "固定動詞片語搭配 subject A to B (使 A 經受/遭受 B)。" },
            { part: "the working prototype", role: "受詞 A (Object)", note: "working 作現在分詞形容詞，表示「具備實際運作功能的」。" },
            { part: "to rigorous wind tunnel testing", role: "受格補語介系詞片語 (Prepositional Phrase)", note: "to 為介系詞，接測試著名詞片語。" },
            { part: "before launching mass production", role: "時間狀詞 (Time Adverbial)", note: "before 作介系詞，後接動名詞 launching。" }
          ],
          keyPoints: [
            "【關鍵動詞片語】：subject something to something (使...經歷/遭受檢驗或考驗)。",
            "【分詞轉形容詞】：working prototype (工作原型、功能性雛形)。",
            "【詞根探討】：type 原意為敲擊出的印記，如 archetype (原型典型)、stereotype (刻板印象)。"
          ]
        }
      },
      {
        word: "protagonist",
        kk: "[proˈtæɡənɪst]",
        ipa: "/proʊˈtæɡənɪst/",
        pos: "n.",
        meaning: "主角、主人公、領導者、主要宣倡者",
        formula: {
          parts: [
            { text: "prot-", role: "prefix", meaning: "第一、首要 (希臘語 prôtos)" },
            { text: "agonist", role: "base", meaning: "奮鬥者、演員 (希臘語 agōnistēs 競賽者)" }
          ],
          resultMeaning: "戲劇舞台上第一位上場奮鬥的主要角色 ➔「主角」"
        },
        sentence: "Throughout the epic novel, the flawed protagonist struggles against moral dilemmas while seeking redemption for his past mistakes.",
        sentenceZh: "在整部史詩小說中，這位帶有缺陷的主角在道德困境中掙扎，同時為自己過去的過錯尋求救贖。",
        grammar: {
          pattern: "Time Adverbial + S + Vi + Prep Phrase + Elliptical Time Clause (時間狀詞 + 主詞 + 不及物動詞 + 介系詞片語 + 精簡時間子句)",
          breakdown: [
            { part: "Throughout the epic novel", role: "範圍狀詞 (Adverbial of Range)", note: "介系詞 throughout 表貫穿整部作品。" },
            { part: "the flawed protagonist", role: "主詞 (Subject)", note: "flawed (有缺點的、不完美的) 修飾主角。" },
            { part: "struggles against", role: "動詞與介系詞 (Verb + Preposition)", note: "struggle against 表與困境對抗 (亦可搭配 struggle with)。" },
            { part: "moral dilemmas", role: "介系詞受詞 (Object)", note: "dilemma 為進退兩難之困境。" },
            { part: "while seeking redemption for his past mistakes", role: "精簡分詞狀詞 (Conjunction + Participle)", note: "保留連接詞 while，省略主詞與 be 動詞 [while he is seeking...]。" }
          ],
          keyPoints: [
            "【角色對稱概念】：protagonist (主角) 對立面為 antagonist (反派主角；anti- 反對 + agonist)。",
            "【狀詞子句精簡】：while + V-ing 為寫作常見的高階句型，使行文更精煉。"
          ]
        }
      },
      {
        word: "protocol",
        kk: "[ˈprotəˌkɔl]",
        ipa: "/ˈproʊtəkɑːl/",
        pos: "n.",
        meaning: "協議、規程、禮賓守則、通訊協定",
        formula: {
          parts: [
            { text: "proto-", role: "prefix", meaning: "最初、卷首 (希臘語 prôtos)" },
            { text: "col", role: "base", meaning: "膠水、黏附紙張 (希臘語 kolla 膠水)" }
          ],
          resultMeaning: "黏在古代手稿第一頁記載內容總結與守則的卷首文檔 ➔「協議、規範」"
        },
        sentence: "Medical researchers must adhere strictly to international safety protocols when conducting genetic experiments.",
        sentenceZh: "醫學研究人員在進行基因實驗時，必須嚴格遵守國際安全規範。",
        grammar: {
          pattern: "S + Modal + Vi + Adv + Prep Phrase + Reduced Time Clause (主詞 + 助動詞 + 不及物動詞 + 副詞 + 介系詞片語 + 時間分詞精簡子句)",
          breakdown: [
            { part: "Medical researchers", role: "主詞 (Subject)", note: "醫學研究人員。" },
            { part: "must adhere", role: "情態謂語動詞 (Modal Verb + Base Verb)", note: "must 強調義務責任，adhere 為不及物動詞。" },
            { part: "strictly", role: "修飾副詞 (Adverb of Manner)", note: "置於動詞與介系詞之間，加強執行標準。" },
            { part: "to international safety protocols", role: "介系詞受詞 (Prepositional Object)", note: "adhere to 為不可分割的固定片語「恪守、遵循」。" },
            { part: "when conducting genetic experiments", role: "時間分詞狀詞 (Adverbial Participle)", note: "when + V-ing，表「當進行...之時」。" }
          ],
          keyPoints: [
            "【固定搭配詞組】：adhere to protocol (恪遵規程)、breach of protocol (違反協議)。",
            "【多領域含意】：在外交指「外交禮儀」；在網路工程指「通訊協定 (如 HTTP/IP)」；在醫學指「臨床試驗規範」。"
          ]
        }
      },
      {
        word: "protect",
        kk: "[prəˈtɛkt]",
        ipa: "/prəˈtɛkt/",
        pos: "v.",
        meaning: "保護、防衛、庇護",
        formula: {
          parts: [
            { text: "pro- / prot-", role: "prefix", meaning: "在前面、向前 (拉丁/希臘語 pro)" },
            { text: "tect", role: "base", meaning: "覆蓋、蓋屋頂 (拉丁語 tegere 遮蓋)" }
          ],
          resultMeaning: "在正前方撐起遮陽避雨的防護掩體 ➔「保護、防衛」"
        },
        sentence: "Deploying comprehensive firewalls protects sensitive database records against unauthorized digital intrusions.",
        sentenceZh: "部署全面的防火牆能保護敏感的資料庫紀錄免遭未經授權的數位入侵。",
        grammar: {
          pattern: "Gerund Subject + Vt + O + Prep Phrase against Danger (動名詞主詞 + 及物動詞 + 受詞 + 防護對象介系詞片語)",
          breakdown: [
            { part: "Deploying comprehensive firewalls", role: "動名詞片語主詞 (Gerund Subject)", note: "動名詞片語作主詞，文法上一律視為「第三人稱單數」。" },
            { part: "protects", role: "及物動詞 (Transitive Verb)", note: "配合單數動名詞主詞，動詞加 s。" },
            { part: "sensitive database records", role: "受詞 (Direct Object)", note: "受保護的實體對象。" },
            { part: "against unauthorized digital intrusions", role: "防護目標介系詞片語 (Prepositional Phrase)", note: "protect A against/from B 為標準搭配，against 表抵禦外力危害。" }
          ],
          keyPoints: [
            "【動名詞主詞主謂一致性】：Gerund subject takes a singular verb (Deploying... protects)。",
            "【介系詞搭配】：protect [受詞] against [威脅] 或 protect [受詞] from [傷害]。",
            "【詞根網絡】：tect (覆蓋)，同源字有 detect (de 去除 + tect 覆蓋 = 揭發/偵測)、architect (archi 總裁 + tect 建造覆蓋者 = 建築師)。"
          ]
        }
      },
      {
        word: "protozoan",
        kk: "[ˌprotəˈzoən]",
        ipa: "/ˌproʊtəˈzoʊən/",
        pos: "n.",
        meaning: "原生動物（單細胞真核微生物）",
        formula: {
          parts: [
            { text: "proto-", role: "prefix", meaning: "最原始的 (希臘語 prôtos)" },
            { text: "zoan", role: "base", meaning: "動物 (希臘語 zōion)" }
          ],
          resultMeaning: "地球生命演化史上最初始出現的微小動物個體 ➔「原生動物」"
        },
        sentence: "Under the optical microscope, the biology students observed microscopic protozoans propelling themselves with microscopic flagella.",
        sentenceZh: "在光學顯微鏡下，生物學系學生觀察到微小的原生動物正借助纖細的鞭毛推進身體。",
        grammar: {
          pattern: "Prep Phrase + S + Vt + O + Objective Complement (介系詞狀詞 + 主詞 + 感官/及物動詞 + 受詞 + 現在分詞受詞補語)",
          breakdown: [
            { part: "Under the optical microscope", role: "地點狀詞 (Adverbial of Place)", note: "指出觀察儀器環境。" },
            { part: "the biology students", role: "主詞 (Subject)", note: "執行觀察的群體。" },
            { part: "observed", role: "感官/及物動詞 (Sensory Verb)", note: "過去式動詞。" },
            { part: "microscopic protozoans", role: "直接受詞 (Direct Object)", note: "被觀察的對象。" },
            { part: "propelling themselves with microscopic flagella", role: "受詞補語 (Objective Complement)", note: "現在分詞片語作受詞補語，強調動作正在活躍進行中 (observe + O + V-ing)。" }
          ],
          keyPoints: [
            "【感官動詞句型】：observe / watch / see + O + V-ing，強調主動正在發生的動作畫面感。",
            "【生物構詞學】：proto- (最原始) + zoo/zoa (動物，如 zoology 動物學)。"
          ]
        }
      }
    ],
    article: {
      title: "The Genesis of Innovation: From Prototype to Pioneer",
      titleZh: "創新的原點：從雛形打造到科技先驅",
      intro: "任何偉大的發明與故事，最初都是從一塊不起眼的「原始模型 (prototype)」或微不足道的「原始起點 (proto-)」開始萌芽。",
      paragraphs: [
        {
          en: "Every transformative technological revolution begins with a fragile prototype. In a modest laboratory surrounded by circuit boards, our brilliant protagonist spent years fine-tuning a revolutionary solar energy converter, determined to solve the energy crisis.",
          zh: "每場具變革性的科技革命，皆始於一件脆弱的原型。在被電路板環繞的簡樸實驗室裡，我們才華洋溢的主角耗費了數年微調一套革命性的太陽能轉換器，下定決心要解決能源危機。"
        },
        {
          en: "Before conducting live trials, the research team established an uncompromising safety protocol to protect their high-voltage capacitors against unexpected electrical surges. Without rigorous discipline, months of delicate engineering could vanish in a single spark.",
          zh: "在進行現場實測之前，研究團隊確立了毫不妥協的安全規程，以保護其高壓電容器免於遭受意外的電壓突波。如果沒有嚴謹的紀律，數個月精雕細琢的工程成果可能會在單一火花中化為烏有。"
        },
        {
          en: "Interestingly, the inventor drew inspiration from nature's earliest evolutionary architects: simple single-celled protozoans that had survived in hostile geothermal vents for billions of years by utilizing thermal gradients.",
          zh: "有趣的是，這位發明家從大自然最初始的演化建築師中汲取靈感：那些利用熱梯度、在惡劣地熱噴口中繁衍生存了數十億年的微小單細胞原生動物。"
        },
        {
          en: "By mimicking these primitive biological mechanisms, the team successfully engineered a machine capable of producing clean energy with zero emissions. Thus, what once existed merely as a rough sketch became a global milestone, demonstrating how honoring the original spirit of 'proto-' can reshape human destiny.",
          zh: "藉由模仿這些原始的生物機制，團隊成功打造出一台能以零排放產生純淨能源的機器。就這樣，曾經只是一張粗糙草圖的事物變成了全球的里程碑，展現出崇尚「proto- (原始開創)」精神如何重塑人類的命運。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What role did protozoans play in the protagonist's technological breakthrough?",
          qZh: "原生動物在主角的科技突破中扮演了什麼角色？",
          options: [
            "A. They provided biological inspiration for thermal energy utilization. (為熱能利用提供了仿生靈感)",
            "B. They contaminated the solar panels and delayed the project.",
            "C. They were cloned to create living batteries.",
            "D. They functioned as tiny computers."
          ],
          answer: 0,
          explanation: "文中第三段指出發明家從「simple single-celled protozoans」利用熱梯度的生存機制中汲取了靈感。"
        },
        {
          q: "Why was establishing a strict protocol essential before running live trials?",
          qZh: "為什麼在進行實測前建立嚴格的規程至關重要？",
          options: [
            "A. To apply for government patents in advance.",
            "B. To protect fragile equipment against electrical surges. (保護設備免於電壓突波損壞)",
            "C. To hire more actors for the documentary.",
            "D. To advertise the product to the public."
          ],
          answer: 1,
          explanation: "文中第二段指出團隊制定規程是為了「to protect their high-voltage capacitors against unexpected electrical surges」。"
        }
      ]
    }
  },
  {
    id: "spect",
    name: "spect / spic",
    type: "root",
    typeLabel: "拉丁語字根 (Latin Root)",
    etymology: "源自拉丁語動詞「specere」(視、看、注視、觀察)，延伸形為 spectare 與 spicere。",
    originMeaning: "看、視察、觀察、景象",
    phonetic: "/spɛkt/",
    icon: "🔍",
    color: "#2563EB",
    summary: "與眼睛視線、內心省察、外在景觀及檢驗審視密切相關的超高頻核心字根。",
    words: [
      {
        word: "inspect",
        kk: "[ɪnˈspɛkt]",
        ipa: "/ɪnˈspɛkt/",
        pos: "v.",
        meaning: "檢查、視察、檢驗",
        formula: {
          parts: [
            { text: "in-", role: "prefix", meaning: "進入內部 (拉丁語 in)" },
            { text: "spect", role: "root", meaning: "看 (拉丁語 specere)" }
          ],
          resultMeaning: "深入到事物內部仔細查看 ➔「檢查、視察」"
        },
        sentence: "Senior aviation safety regulators inspect every turbine blade thoroughly before granting commercial flight authorization.",
        sentenceZh: "資深航空安全監管人員在頒發商業飛行許可之前，會徹底檢查每一個渦輪葉片。",
        grammar: {
          pattern: "S + Vt + O + Adv + Prepositional Gerund Clause (主詞 + 及物動詞 + 受詞 + 程度副詞 + 介系詞動名詞子句)",
          breakdown: [
            { part: "Senior aviation safety regulators", role: "主詞 (Subject)", note: "名詞片語，包含多重修飾名詞與形容詞。" },
            { part: "inspect", role: "及物動詞 (Transitive Verb)", note: "現在簡單式，表達例行性制度與規定。" },
            { part: "every turbine blade", role: "受詞 (Direct Object)", note: "every 後接單數可數名詞 blade。" },
            { part: "thoroughly", role: "方式副詞 (Adverb of Manner)", note: "修飾 inspect，表示「徹底、周延地」。" },
            { part: "before granting commercial flight authorization", role: "時間狀詞 (Time Adverbial)", note: "before 作介系詞，後接動名詞 granting 與雙受詞語境。" }
          ],
          keyPoints: [
            "【主客語搭配】：inspect the premises (檢查廠區)、inspect for defects (檢查缺陷)。",
            "【衍生字族】：inspector (檢查員)、inspection (檢驗工作)。"
          ]
        }
      },
      {
        word: "respect",
        kk: "[rɪˈspɛkt]",
        ipa: "/rɪˈspɛkt/",
        pos: "v. / n.",
        meaning: "尊敬、尊重、敬佩；(n.) 尊重、方面",
        formula: {
          parts: [
            { text: "re-", role: "prefix", meaning: "再、回頭 (拉丁語 re-)" },
            { text: "spect", role: "root", meaning: "看 (拉丁語 specere)" }
          ],
          resultMeaning: "回過頭來再三注視並敬仰 ➔「尊敬、尊重」"
        },
        sentence: "True collaborative leadership requires that senior executives respect diverse opinions voiced by frontline employees.",
        sentenceZh: "真正的協同領導力要求高階主管尊重前線基層員工所表達的不同觀點。",
        grammar: {
          pattern: "S + Vt + Subjunctive That-Clause (主詞 + 及物動詞 + 意志要求假設語氣名詞子句)",
          breakdown: [
            { part: "True collaborative leadership", role: "主詞 (Subject)", note: "抽象名詞片語。" },
            { part: "requires", role: "及物動詞 (Transitive Verb of Demand)", note: "表要求/命令動詞，後接 that 子句需用虛擬語氣 (should + 原形動詞，should 常省略)。" },
            { part: "that senior executives (should) respect", role: "名詞子句與動詞原形 (Subjunctive Mood)", note: "子句謂語動詞使用原形 respect。" },
            { part: "diverse opinions", role: "子句受詞 (Object)", note: "多元意見。" },
            { part: "voiced by frontline employees", role: "過去分詞後位修飾 (Past Participial Modifier)", note: "修飾 opinions，相當於 which are voiced by..." }
          ],
          keyPoints: [
            "【特殊假設語氣 (Subjunctive Mood)】：require / demand / suggest + that + S + (should) + V-base。",
            "【過去分詞後置修飾】：opinions voiced by... 展現道地寫作修辭。"
          ]
        }
      },
      {
        word: "retrospect",
        kk: "[ˈrɛtrəˌspɛkt]",
        ipa: "/ˈrɛtrəspɛkt/",
        pos: "n.",
        meaning: "回顧、回想、追溯",
        formula: {
          parts: [
            { text: "retro-", role: "prefix", meaning: "向後、往回 (拉丁語 retro)" },
            { text: "spect", role: "root", meaning: "看 (拉丁語 specere)" }
          ],
          resultMeaning: "回頭看過往走過的路與經歷 ➔「回顧、回憶」"
        },
        sentence: "In retrospect, the financial crisis of that decade served as a painful catalyst for reforming global banking standards.",
        sentenceZh: "回想起來，那個十年的金融危機成為改革全球銀行標準的痛苦催化劑。",
        grammar: {
          pattern: "Adverbial Idiom + S + Vi + Prep Phrase (成語狀詞 + 主詞 + 不及物動詞 + 介系詞受詞補語)",
          breakdown: [
            { part: "In retrospect", role: "慣用片語狀詞 (Idiomatic Adverbial)", note: "固定片語「回首過去、事後反思」，常置於句首。" },
            { part: "the financial crisis of that decade", role: "主詞 (Subject)", note: "介系詞片語 of that decade 修飾 crisis。" },
            { part: "served as", role: "動詞片語 (Phrasal Verb)", note: "serve as 表示「充當、擔任、發揮...作用」。" },
            { part: "a painful catalyst", role: "介系詞受詞 (Object of Prep)", note: "catalyst (催化劑) 作隱喻。" },
            { part: "for reforming global banking standards", role: "目的介系詞片語 (Prepositional Modifier)", note: "for 後接動名詞 reforming。" }
          ],
          keyPoints: [
            "【高分寫作必備片語】：In retrospect,...（回顧過去...）。",
            "【同根形容詞】：retrospective (回顧的、懷舊的；n. 回顧展)。"
          ]
        }
      },
      {
        word: "spectacle",
        kk: "[ˈspɛktək!]",
        ipa: "/ˈspɛktəkl/",
        pos: "n.",
        meaning: "奇觀、壯觀景象；(複數 spectacles) 眼鏡",
        formula: {
          parts: [
            { text: "spect", role: "root", meaning: "看 (拉丁語 specere)" },
            { text: "-acle", role: "suffix", meaning: "器具、場景、事物 (名詞字尾)" }
          ],
          resultMeaning: "吸引大眾駐足觀看的事物與盛大場面 ➔「奇觀、壯觀場面」"
        },
        sentence: "The vibrant annual lantern festival created an unforgettable visual spectacle that attracted travelers from across the world.",
        sentenceZh: "一年一度生氣盎然的花燈節營造了一場令人難忘的視覺盛宴，吸引了來自世界各地的旅人。",
        grammar: {
          pattern: "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 關係子句)",
          breakdown: [
            { part: "The vibrant annual lantern festival", role: "主詞 (Subject)", note: "triple modifiers (vibrant, annual, lantern) 修飾 festival。" },
            { part: "created", role: "及物動詞 (Transitive Verb)", note: "過去式。" },
            { part: "an unforgettable visual spectacle", role: "直接受詞 (Direct Object)", note: "unforgettable (不可磨滅的) + visual (視覺的) + spectacle (奇觀)。" },
            { part: "that attracted travelers from across the world", role: "限定關係子句 (Defining Relative Clause)", note: "that 引導子句修飾 spectacle，attracted 為子句動詞。" }
          ],
          keyPoints: [
            "【字義分化】：單數通常指「盛大奇觀、景象」；複數 spectacles 在傳統英式英語中意為「眼鏡」(= glasses)。",
            "【形容詞衍生】：spectacular (壯麗的、宏偉的)。"
          ]
        }
      },
      {
        word: "prospect",
        kk: "[ˈprɑspɛkt]",
        ipa: "/ˈprɑːspɛkt/",
        pos: "n. / v.",
        meaning: "(n.) 前景、前途、展望、潛在客戶；(v.) 探勘",
        formula: {
          parts: [
            { text: "pro-", role: "prefix", meaning: "向前 (拉丁語 pro)" },
            { text: "spect", role: "root", meaning: "看 (拉丁語 specere)" }
          ],
          resultMeaning: "向前眺望未來遠景 ➔「前景、展望」"
        },
        sentence: "Economic analysts remain optimistic about the company's long-term commercial prospects despite short-term inflation headwinds.",
        sentenceZh: "儘管面臨短期通膨阻力，經濟分析師對該公司的長期商業前景依然抱持樂觀態度。",
        grammar: {
          pattern: "S + Linking Verb + Predicate Adjective + Prep Phrase + Concessive Prep Phrase (主詞 + 連綴動詞 + 形容詞補語 + 介系詞片語 + 讓步介系詞片語)",
          breakdown: [
            { part: "Economic analysts", role: "主詞 (Subject)", note: "經濟分析師。" },
            { part: "remain", role: "連綴動詞 (Linking Verb)", note: "保持某狀態。" },
            { part: "optimistic", role: "主詞補語 (Subject Complement)", note: "形容詞，固定搭配介系詞 about。" },
            { part: "about the company's long-term commercial prospects", role: "介系詞對象片語 (Prepositional Phrase)", note: "prospects 常用複數表示事業與市場前景。" },
            { part: "despite short-term inflation headwinds", role: "讓步介系詞片語 (Concessive Prepositional Phrase)", note: "despite 為介系詞，後接名詞片語 headwinds (逆風/阻力)。" }
          ],
          keyPoints: [
            "【介系詞對比】：despite 為介系詞 (接名詞)，although 為從屬連接詞 (接完整子句)。",
            "【衍生形容詞】：prospective (預期的、未來的，如 prospective students 準新生)。"
          ]
        }
      }
    ],
    article: {
      title: "The Architecture of Observation: Living Through the Lens of 'Spect'",
      titleZh: "觀察的建築學：以觀照字根重省人生",
      intro: "「看 (spect)」不僅僅是視網膜接收光影，更是一種深入內部 (inspect)、反省過往 (retrospect) 與眺望未來 (prospect) 的心靈智慧。",
      paragraphs: [
        {
          en: "Every morning, city engineers inspect railway tracks and suspension bridges across the metropolitan harbor. Their relentless scrutiny ensures that millions of commuters can cross deep waters safely every day without pondering the fragile spectacle beneath their feet.",
          zh: "每天清晨，城市工程師都會視察大都會海港沿線的鐵軌與懸索吊橋。他們堅持不懈的嚴格檢驗，確保了數百萬通勤族每天能平安橫渡深水，而無需擔憂腳下那令人屏息的壯觀景象。"
        },
        {
          en: "In retrospect, human civilization has always flourished when architects and philosophers treated nature with profound respect. Whenever builders neglected the environmental balance in pursuit of rapid profits, catastrophic floods inevitably reminded them of their shortsightedness.",
          zh: "回想起來，當建築師與哲學家對大自然抱持著深厚敬意時，人類文明總是繁榮昌盛。每當建造者為了追求速成利益而忽視環境平衡時，災難性的洪患總會無情地提醒他們當初的短視近利。"
        },
        {
          en: "As we stand on the threshold of a new millennium, investors eagerly assess the bright prospect of renewable energy. By learning from historical failures and looking ahead with humility, we can transform today's ecological challenges into tomorrow's enduring triumph.",
          zh: "當我們站在新千禧年的門檻上，投資人熱切評估著再生能源的璀璨前景。藉由從歷史挫敗中學習並以謙卑之心遠眺前方，我們能將今日的生態挑戰化為明日持久的勝利。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "According to the article, why are the engineers' inspections vital?",
          qZh: "根據文章，為何工程師的視察至關重要？",
          options: [
            "A. They guarantee safe transit for millions of commuters. (確保數百萬通勤族平安通行)",
            "B. They allow companies to sell tickets at higher prices.",
            "C. They discover sunken pirate treasures.",
            "D. They design artificial intelligence robots."
          ],
          answer: 0,
          explanation: "文中第一段指出工程師的嚴謹檢驗「ensures that millions of commuters can cross deep waters safely」。"
        }
      ]
    }
  },
  {
    id: "dict",
    name: "dict / dic",
    type: "root",
    typeLabel: "拉丁語字根 (Latin Root)",
    etymology: "源自拉丁語動詞「dicere / dictare」(說、宣布、斷言、宣告)。",
    originMeaning: "說、言說、宣布、口述",
    phonetic: "/dɪkt/",
    icon: "🗣️",
    color: "#7C3AED",
    summary: "構成法律宣告、預言語意、權威口述以及字詞表達等核心單字。",
    words: [
      {
        word: "predict",
        kk: "[prɪˈdɪkt]",
        ipa: "/prɪˈdɪkt/",
        pos: "v.",
        meaning: "預測、預言",
        formula: {
          parts: [
            { text: "pre-", role: "prefix", meaning: "在之前、預先 (拉丁語 prae)" },
            { text: "dict", role: "root", meaning: "說 (拉丁語 dicere)" }
          ],
          resultMeaning: "在事情發生前就先說出來 ➔「預測、預言」"
        },
        sentence: "Advanced computational models can accurately predict seasonal typhoon trajectories using real-time atmospheric telemetry.",
        sentenceZh: "先進的計算模型能運用即時大氣遙測資料，精確預測季節性颱風的路徑走勢。",
        grammar: {
          pattern: "S + Modal + Adv + Vt + O + Prepositional Gerund (主詞 + 助動詞 + 程度副詞 + 及物動詞 + 受詞 + 方式介系詞動名詞)",
          breakdown: [
            { part: "Advanced computational models", role: "主詞 (Subject)", note: "名詞片語，包含分詞形容詞 advanced 與形容詞 computational。" },
            { part: "can accurately predict", role: "謂語 (Modal Predicate)", note: "情態助動詞 can + 副詞 accurately 修飾動詞 predict。" },
            { part: "seasonal typhoon trajectories", role: "直接受詞 (Direct Object)", note: "trajectories (移動軌跡/路徑)。" },
            { part: "using real-time atmospheric telemetry", role: "方式狀詞片語 (Participial Adverbial)", note: "現在分詞 using 表藉由某手段。" }
          ],
          keyPoints: [
            "【同義辨析】：predict (基於數據或經驗之科學預測)、prophesy (宗教神諭式的預言)。",
            "【衍生字詞】：predictable (可預見的)、prediction (預測詞)。"
          ]
        }
      },
      {
        word: "contradict",
        kk: "[ˌkɑntrəˈdɪkt]",
        ipa: "/ˌkɑːntrəˈdɪkt/",
        pos: "v.",
        meaning: "矛盾、反駁、與...相抵觸",
        formula: {
          parts: [
            { text: "contra-", role: "prefix", meaning: "反對、相對 (拉丁語 contra)" },
            { text: "dict", role: "root", meaning: "說 (拉丁語 dicere)" }
          ],
          resultMeaning: "說反話、與別人對著說 ➔「反駁、相抵觸」"
        },
        sentence: "The suspect's testimony blatantly contradicted the empirical physical evidence uncovered by forensic investigators.",
        sentenceZh: "嫌疑犯的證詞與鑑識調查人員發現的實質客觀物證產生了公然的抵觸矛盾。",
        grammar: {
          pattern: "S + Adv + Vt + O + Participial Modifier (主詞 + 程度副詞 + 及物動詞 + 受詞 + 過去分詞後位修飾)",
          breakdown: [
            { part: "The suspect's testimony", role: "主詞 (Subject)", note: "所有格名詞片語。" },
            { part: "blatantly contradicted", role: "謂語 (Predicate)", note: "blatantly (公然地、明目張膽地) 修飾及物動詞 contradicted。" },
            { part: "the empirical physical evidence", role: "直接受詞 (Direct Object)", note: "empirical (經驗的、實證的) + physical (實體的) + evidence (證據，不可數)。" },
            { part: "uncovered by forensic investigators", role: "分詞後位修飾 (Past Participle Phrase)", note: "修飾 evidence，相當於 which was uncovered by..." }
          ],
          keyPoints: [
            "【文法注意】：contradict 為及物動詞，直接接受詞 (不要多加 with 或 against)。",
            "【衍生形容詞】：contradictory (矛盾的、互相衝突的)。"
          ]
        }
      },
      {
        word: "verdict",
        kk: "[ˈvɝdɪkt]",
        ipa: "/ˈvɜːrdɪkt/",
        pos: "n.",
        meaning: "裁決、判決、定論",
        formula: {
          parts: [
            { text: "ver-", role: "root", meaning: "真實 (拉丁語 verus)" },
            { text: "dict", role: "root", meaning: "說 (拉丁語 dicere)" }
          ],
          resultMeaning: "說出查核過後的真實之言 ➔「法庭裁決、定論」"
        },
        sentence: "After three days of intensive deliberation, the jury announced a unanimous guilty verdict in the high-profile fraud trial.",
        sentenceZh: "經過三天緊張的密集審議後，陪審團在這場備受矚目的詐欺審判中宣布了一致的有罪判決。",
        grammar: {
          pattern: "Time Prep Phrase + S + Vt + O + Locative Prep Phrase (時間介系詞片語 + 主詞 + 及物動詞 + 受詞 + 審理環境介系詞片語)",
          breakdown: [
            { part: "After three days of intensive deliberation", role: "時間狀詞 (Time Adverbial)", note: "介系詞 after 後接時間名詞片語。" },
            { part: "the jury", role: "主詞 (Subject)", note: "陪審團 (集合名詞，在此視為單一整體)。" },
            { part: "announced", role: "及物動詞 (Transitive Verb)", note: "宣告。" },
            { part: "a unanimous guilty verdict", role: "直接受詞 (Direct Object)", note: "unanimous (全體一致的) + guilty (有罪的) + verdict (裁決)。" },
            { part: "in the high-profile fraud trial", role: "範圍介系詞片語 (Contextual Prepositional Phrase)", note: "high-profile (引人注目的、高調的)。" }
          ],
          keyPoints: [
            "【固定搭配動詞】：reach a verdict (達成判決)、deliver / return a verdict (宣讀判決)。",
            "【詞根探討】：ver- (真實)，如 verify (核實)、veracity (誠實/真實性)。"
          ]
        }
      },
      {
        word: "dictate",
        kk: "[ˈdɪkˌtet]",
        ipa: "/ˈdɪkteɪt/",
        pos: "v. / n.",
        meaning: "(v.) 口述、聽寫、命令、支配；(n.) 命令、原則",
        formula: {
          parts: [
            { text: "dict", role: "root", meaning: "說 (拉丁語 dicere)" },
            { text: "-ate", role: "suffix", meaning: "使成為、動詞字尾" }
          ],
          resultMeaning: "依據自己的話語命令他人聽從並寫下 ➔「口述、支配、命令」"
        },
        sentence: "Market supply and consumer demand ultimately dictate the fluctuating retail prices of agricultural commodities.",
        sentenceZh: "市場供應量與消費者需求量最終決定並支配著農產品浮動的零售價格。",
        grammar: {
          pattern: "Compound Subject + Adv + Vt + O (對等複合主詞 + 副詞 + 及物動詞 + 受詞)",
          breakdown: [
            { part: "Market supply and consumer demand", role: "對等主詞 (Compound Subject)", note: "由 and 連接兩大經濟概念，謂語使用複數形式。" },
            { part: "ultimately", role: "時間/修飾副詞 (Adverb of Degree)", note: "表示「歸根究底、最終」。" },
            { part: "dictate", role: "及物動詞 (Transitive Verb)", note: "在此引申為「支配、主導、決定」(= determine)。" },
            { part: "the fluctuating retail prices of agricultural commodities", role: "受詞 (Direct Object)", note: "fluctuating (浮動的) 作現在分詞形容詞。" }
          ],
          keyPoints: [
            "【字義引申】：由「口述聽寫」引申為「由上而下決定權威方針」。",
            "【衍生字詞】：dictator (獨裁者)、dictatorship (獨裁政權)。"
          ]
        }
      }
    ],
    article: {
      title: "The Power of the Spoken Word: Dictating Truth and Justice",
      titleZh: "言語的力量：宣告真理與正義",
      intro: "在古代社會，話語一旦說出 (dict) 就具有法律與契約的效力。從法官的裁決 (verdict) 到先知的預言 (predict)，言語重塑著人類命運。",
      paragraphs: [
        {
          en: "Throughout history, rulers sought to dictate the laws of the land, demanding that their decrees be recorded without questioning. However, courageous philosophers often dared to contradict tyranny with unyielding moral convictions.",
          zh: "縱觀歷史，統治者總試圖口述並強行制定國家的法律，要求他們的法令不容置疑地被記錄下來。然而，勇敢的哲學家經常敢於以不屈的道德信念反駁暴政。"
        },
        {
          en: "In modern democracies, no single voice can arbitrary predict the fate of the innocent. Only after transparent cross-examination can an impartial jury deliver a solemn verdict based purely upon substantiated facts.",
          zh: "在現代民主體制中，沒有任何單一聲音能武斷預言無辜者的命運。只有在透明的交互詰問之後，公正的陪審團才能純粹依據經證實的事實作出莊嚴的判決。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What does the word 'contradict' mean in the context of opposing tyranny?",
          qZh: "在對抗暴政的語境中，'contradict' 的意涵為何？",
          options: [
            "A. To agree completely and sign the contract.",
            "B. To speak out against and oppose tyranny. (發聲反對並抵觸暴政)",
            "C. To run away from responsibility.",
            "D. To dictate taxes to citizens."
          ],
          answer: 1,
          explanation: "文中指出勇敢的哲學家敢於以道德信念「contradict tyranny」(公開反駁並抗拒暴政)。"
        }
      ]
    }
  },
  {
    id: "port",
    name: "port",
    type: "root",
    typeLabel: "拉丁語字根 (Latin Root)",
    etymology: "源自拉丁語動詞「portare」(搬運、攜帶、運送)，以及名詞「portus」(港口、門戶)。",
    originMeaning: "搬運、運送、攜帶、港口",
    phonetic: "/pɔːrt/",
    icon: "🚢",
    color: "#0284C7",
    summary: "物流貿易、地理空間轉移及隨身攜帶科技的核心字根。",
    words: [
      {
        word: "transport",
        kk: "[trænsˈpɔrt]",
        ipa: "/trænsˈpɔːrt/",
        pos: "v. / n.",
        meaning: "運輸、運送；(n.) 交通工具、運輸系統",
        formula: {
          parts: [
            { text: "trans-", role: "prefix", meaning: "穿過、跨越 (拉丁語 trans)" },
            { text: "port", role: "root", meaning: "搬運 (拉丁語 portare)" }
          ],
          resultMeaning: "將貨物或人員搬運跨越不同地域 ➔「運輸、運送」"
        },
        sentence: "High-speed electric freight trains transport agricultural harvests from rural farming regions to coastal metropolitan hubs.",
        sentenceZh: "高速電力貨運列車將農村耕作地區採收的農作物運送至沿海大都會樞紐。",
        grammar: {
          pattern: "S + Vt + O + Prep Phrase + Prep Phrase (主詞 + 及物動詞 + 受詞 + 出發地片語 + 目的地片語)",
          breakdown: [
            { part: "High-speed electric freight trains", role: "主詞 (Subject)", note: "包含三個前置修飾語 (high-speed, electric, freight) 的複合主詞片語。" },
            { part: "transport", role: "及物動詞 (Transitive Verb)", note: "現在簡單式，主詞為複數 trains。" },
            { part: "agricultural harvests", role: "直接受詞 (Direct Object)", note: "農業收穫作物。" },
            { part: "from rural farming regions", role: "起點介系詞片語 (Source Prep Phrase)", note: "from 表來源起點。" },
            { part: "to coastal metropolitan hubs", role: "終點介系詞片語 (Destination Prep Phrase)", note: "to 表抵達目標。" }
          ],
          keyPoints: [
            "【經典移動介系詞對】：transport A from [起點] to [終點]。",
            "【衍生名詞】：transportation (運輸工具、交通運輸網)。"
          ]
        }
      },
      {
        word: "export",
        kk: "[ˈɛkspɔrt] (n.) / [ɪkˈspɔrt] (v.)",
        ipa: "/ˈɛkspɔːrt/ (n.) / /ɪkˈspɔːrt/ (v.)",
        pos: "v. / n.",
        meaning: "出口、輸出；(n.) 出口商品",
        formula: {
          parts: [
            { text: "ex-", role: "prefix", meaning: "向外、出 (拉丁語 ex)" },
            { text: "port", role: "root", meaning: "港口/運送 (拉丁語 portare)" }
          ],
          resultMeaning: "將國內物產經由港口運送到國外 ➔「出口、輸出」"
        },
        sentence: "The manufacturing powerhouse exports advanced semiconductor chips to tech companies situated across fifty countries.",
        sentenceZh: "這座製造業重鎮將先進的半導體晶片出口至分佈於五十個國家的科技公司。",
        grammar: {
          pattern: "S + Vt + O + Prep Phrase + Participle Modifier (主詞 + 及物動詞 + 受詞 + 接收對象片語 + 過去分詞後位修飾)",
          breakdown: [
            { part: "The manufacturing powerhouse", role: "主詞 (Subject)", note: "powerhouse 喻指產業巨擘、核心重鎮。" },
            { part: "exports", role: "及物動詞 (Transitive Verb)", note: "第三人稱單數現在式。" },
            { part: "advanced semiconductor chips", role: "直接受詞 (Direct Object)", note: "先進半導體晶片。" },
            { part: "to tech companies", role: "介系詞對象 (Prepositional Object)", note: "to 表輸出目標對象。" },
            { part: "situated across fifty countries", role: "分詞片語修飾 (Past Participle Phrase)", note: "修飾 companies，相當於 which are situated across..." }
          ],
          keyPoints: [
            "【重音轉移規律】：名詞時重音在第一音節 /ˈɛkspɔːrt/；動詞時重音在第二音節 /ɪkˈspɔːrt/。",
            "【對立詞彙】：import (進口；im- 進入 + port)。"
          ]
        }
      },
      {
        word: "portable",
        kk: "[ˈpɔrtəb!]",
        ipa: "/ˈpɔːrtəbl/",
        pos: "adj.",
        meaning: "便攜式的、可輕易攜帶的、手提的",
        formula: {
          parts: [
            { text: "port", role: "root", meaning: "攜帶 (拉丁語 portare)" },
            { text: "-able", role: "suffix", meaning: "能夠...的 (形容詞字尾)" }
          ],
          resultMeaning: "能夠輕鬆隨身攜帶行走的 ➔「便攜的、輕便的」"
        },
        sentence: "The humanitarian medical team brought portable ultrasound devices to assist displaced refugees in remote mountain encampments.",
        sentenceZh: "人道醫療小組攜帶便攜式超音波設備，前往偏遠山區營地協助流離失所的難民。",
        grammar: {
          pattern: "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的狀詞不定詞片語)",
          breakdown: [
            { part: "The humanitarian medical team", role: "主詞 (Subject)", note: "人道醫療團隊。" },
            { part: "brought", role: "及物動詞 (Transitive Verb)", note: "bring 的過去式。" },
            { part: "portable ultrasound devices", role: "直接受詞 (Direct Object)", note: "portable (便攜的) 修飾儀器設備。" },
            { part: "to assist displaced refugees in remote mountain encampments", role: "目的狀詞 (Infinitive Phrase)", note: "displaced (流離失所的) 為過去分詞轉形容詞；in encampments 表地點。" }
          ],
          keyPoints: [
            "【構詞尾碼】：-able 具備被動受身與潛能含意 (can be carried)。",
            "【衍生名詞】：portability (便攜性、易攜帶特質)。"
          ]
        }
      }
    ],
    article: {
      title: "The Merchant of the Global Harbor: Porting Wealth Across Oceans",
      titleZh: "世界港灣的貿易篇章：穿梭大洋的物資流動",
      intro: "自大航海時代以來，港口 (port) 與運載 (port) 連結了原本隔絕的大陸，推動了全球化的商業動脈。",
      paragraphs: [
        {
          en: "Deep-water harbors serve as the beating heart of global commerce, where gigantic container ships transport millions of tons of food, textiles, and minerals every day across stormy oceans.",
          zh: "深水海港是全球商業跳動的心臟，巨大的貨櫃輪每天在此運載著數百萬噸的糧食、紡織品與礦物，橫越波濤洶湧的大洋。"
        },
        {
          en: "Nations that successfully export manufactured electronics while importing raw materials steadily enhance their economic resilience, proving that mastery over the logistics of 'port' defines national prosperity.",
          zh: "那些成功出口高精密電子產品並同時進口原料的國家，穩步增強了其經濟韌性，證明了掌握「運送與港口 (port)」的物流實力定義了國家的繁榮興盛。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What defines national prosperity according to the article?",
          qZh: "根據文章，何種能力定義了國家的繁榮？",
          options: [
            "A. Mastery over logistics, transport, and international export/import. (掌握物流、運輸與進出口實力)",
            "B. Total isolation from world trade.",
            "C. Replacing human sailors with robots.",
            "D. Ceasing all manufacturing."
          ],
          answer: 0,
          explanation: "文中第二段指出「mastery over the logistics of 'port' defines national prosperity」。"
        }
      ]
    }
  },
  {
    id: "bio",
    name: "bio",
    type: "root",
    typeLabel: "希臘語字根 (Greek Root)",
    etymology: "源自古希臘語「βίος」(bíos)，意指「生命、生物、人類的一生 (life, living organisms)」。",
    originMeaning: "生命、生物、一生",
    phonetic: "/ˈbaɪoʊ/",
    icon: "🧬",
    color: "#16A34A",
    summary: "涵蓋生命科學、生態環保、生平傳記與醫藥健康的最關鍵字根。",
    words: [
      {
        word: "biology",
        kk: "[baɪˈɑlədʒi]",
        ipa: "/baɪˈɑːlədʒi/",
        pos: "n.",
        meaning: "生物學",
        formula: {
          parts: [
            { text: "bio-", role: "root", meaning: "生命、生物 (希臘語 bíos)" },
            { text: "-logy", role: "suffix", meaning: "學問、學科 (希臘語 logos 言說/研究)" }
          ],
          resultMeaning: "探討研究一切生命有機體奧秘的學門 ➔「生物學」"
        },
        sentence: "Modern molecular biology investigates how microscopic cellular structures encode genetic instructions.",
        sentenceZh: "現代分子生物學探討微觀的細胞結構如何編碼遺傳指令。",
        grammar: {
          pattern: "S + Vt + Wh-Noun Clause (主詞 + 及物動詞 + Wh-引導的受詞名詞子句)",
          breakdown: [
            { part: "Modern molecular biology", role: "主詞 (Subject)", note: "專門學門名詞片語。" },
            { part: "investigates", role: "及物動詞 (Transitive Verb)", note: "第三人稱單數現在式。" },
            { part: "how microscopic cellular structures encode genetic instructions", role: "名詞子句受詞 (Noun Clause as Object)", note: "how 為疑問副詞引導間接問句/名詞子句；structures 為子句主詞，encode 為及物動詞。" }
          ],
          keyPoints: [
            "【名詞子句結構】：investigate + how + S + V (探究...如何運作)。",
            "【字根尾碼】：-logy 表示學門，如 geology (地質學)、psychology (心理學)。"
          ]
        }
      },
      {
        word: "biodiversity",
        kk: "[ˌbaɪodaɪˈvɝsəti]",
        ipa: "/ˌbaɪoʊdaɪˈvɜːrsəti/",
        pos: "n.",
        meaning: "生物多樣性",
        formula: {
          parts: [
            { text: "bio-", role: "root", meaning: "生命 (希臘語 bíos)" },
            { text: "diversity", role: "base", meaning: "多樣性 (拉丁語 diversitas)" }
          ],
          resultMeaning: "生態系中所有生命物種的豐富多元性 ➔「生物多樣性」"
        },
        sentence: "Conserving coastal rainforests protects endangered wildlife and safeguards irreplaceable global biodiversity.",
        sentenceZh: "保育沿海雨林能保護瀕危野生動物，並守護不可替代的全球生物多樣性。",
        grammar: {
          pattern: "Gerund Subject + Vt1 + O1 + and + Vt2 + O2 (動名詞主詞 + 第一及物動詞 + 受詞1 + 對等連接詞 + 第二及物動詞 + 受詞2)",
          breakdown: [
            { part: "Conserving coastal rainforests", role: "動名詞主詞 (Gerund Subject)", note: "單數概念主詞。" },
            { part: "protects endangered wildlife", role: "第一個謂語對 (First Predicate)", note: "protects 加 s；wildlife 為集合名詞。" },
            { part: "and safeguards", role: "對等動詞 (Coordinated Verb)", note: "safeguards 保持單數一致性。" },
            { part: "irreplaceable global biodiversity", role: "第二受詞 (Second Object)", note: "irreplaceable (不可替代的；ir- 不 + replace 替代 + able 能)。" }
          ],
          keyPoints: [
            "【動態對稱】：protects... and safeguards... 形成力量均勻的排比對稱動詞片語。",
            "【多樣性構詞】：di- (分開) + vertere (轉向) ➔ diversity (多樣、多元)。"
          ]
        }
      },
      {
        word: "antibiotic",
        kk: "[ˌæntɪbaɪˈɑtɪk]",
        ipa: "/ˌæntibaɪˈɑːtɪk/",
        pos: "n. / adj.",
        meaning: "抗生素；(adj.) 抗菌的",
        formula: {
          parts: [
            { text: "anti-", role: "prefix", meaning: "反對、對抗 (希臘語 anti)" },
            { text: "bio", role: "root", meaning: "生命、微生物 (希臘語 bíos)" },
            { text: "-ic", role: "suffix", meaning: "...的製劑、藥劑 (字尾)" }
          ],
          resultMeaning: "用以對抗有害微生物細菌生命的藥劑 ➔「抗生素」"
        },
        sentence: "Physicians urge patients to complete their prescribed antibiotic course to curb bacterial drug resistance.",
        sentenceZh: "醫師力勸病患服完所開立的抗生素療程，以遏制細菌產生抗藥性。",
        grammar: {
          pattern: "S + Vt + O + to-Infinitive + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 受詞補語不定詞 + 目的狀詞不定詞)",
          breakdown: [
            { part: "Physicians", role: "主詞 (Subject)", note: "內科醫師。" },
            { part: "urge", role: "及物動詞 (Transitive Verb)", note: "搭配句型 urge somebody to do something。" },
            { part: "patients", role: "受詞 (Direct Object)", note: "病患。" },
            { part: "to complete their prescribed antibiotic course", role: "受詞補語 (Objective Complement)", note: "prescribed (所處方的) 為過去分詞修飾療程 course。" },
            { part: "to curb bacterial drug resistance", role: "目的狀詞 (Infinitive of Purpose)", note: "curb (抑制、遏止)。" }
          ],
          keyPoints: [
            "【動詞句型】：urge / advise / persuade + someone + to V。",
            "【醫學術語】：antibiotic resistance (抗生素抗藥性)。"
          ]
        }
      },
      {
        word: "biography",
        kk: "[baɪˈɑgrəfi]",
        ipa: "/baɪˈɑːɡrəfi/",
        pos: "n.",
        meaning: "傳記、傳記文學",
        formula: {
          parts: [
            { text: "bio-", role: "root", meaning: "一生、生命 (希臘語 bíos)" },
            { text: "graphy", role: "suffix/base", meaning: "書寫、記錄 (希臘語 graphein)" }
          ],
          resultMeaning: "書寫記錄某人一生的著作 ➔「傳記」"
        },
        sentence: "The Pulitzer-winning biography vividly chronicled the turbulent personal life of the reclusive philosopher.",
        sentenceZh: "這部榮獲普立茲獎的傳記生動記錄了這位隱世哲學家動盪波折的個人生活。",
        grammar: {
          pattern: "S + Adv + Vt + O (主詞 + 方式副詞 + 及物動詞 + 受詞)",
          breakdown: [
            { part: "The Pulitzer-winning biography", role: "主詞 (Subject)", note: "複合形容詞 Pulitzer-winning 修飾 biography。" },
            { part: "vividly", role: "副詞 (Adverb of Manner)", note: "生動栩栩如生地修飾 chronicled。" },
            { part: "chronicled", role: "及物動詞 (Transitive Verb)", note: "編年史般詳盡記載。" },
            { part: "the turbulent personal life of the reclusive philosopher", role: "受詞 (Direct Object)", note: "turbulent (動盪的)；reclusive (隱遁孤僻的)。" }
          ],
          keyPoints: [
            "【同源自傳對比】：autobiography (auto 自己 + bio 生命 + graphy 寫 = 自傳)。",
            "【動詞詞根跨界】：chronicled 本身源於 chron (時間) 字根！"
          ]
        }
      }
    ],
    article: {
      title: "The Living Web: Celebrating the Symphony of Bios",
      titleZh: "生命之網：譜寫生命的交響詩",
      intro: "從單細胞真核菌落到寫下厚重自傳的智慧靈長類，字根 bio- 見證了三十八億年生命演化的壯麗奇蹟。",
      paragraphs: [
        {
          en: "Without the discoveries of modern biology, humanity would remain helpless in the face of microscopic pathogens. When Alexander Fleming discovered the world's first effective antibiotic, he inaugurated an era where once-fatal bacterial infections could be cured in days.",
          zh: "沒有現代生物學的各項發現，人類在微觀病原體面前仍將束手無策。當亞歷山大·弗萊明發現世界上第一種有效抗生素時，他開啟了一個曾被視為絕症的細菌感染能在數天內治癒的新紀元。"
        },
        {
          en: "Today, preserving the precious biodiversity of coral reefs and old-growth canopies is no longer merely an academic issue. It is a shared ecological obligation to ensure that future generations can inherit a flourishing biosphere.",
          zh: "今日，守護珊瑚礁與原始林冠珍貴的生物多樣性已不再僅僅是學術議題，而是一項共同的生態責任，旨在確保後代子孫能繼承一個繁榮生息的生物圈。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What medical milestone did the discovery of antibiotics achieve?",
          qZh: "抗生素的發現達成了什麼醫療里程碑？",
          options: [
            "A. Curing once-fatal bacterial infections within days. (數天內治癒曾為致命絕症的細菌感染)",
            "B. Eliminating all common colds immediately.",
            "C. Replacing healthy red blood cells.",
            "D. Allowing humans to breathe underwater."
          ],
          answer: 0,
          explanation: "文中第一段指出抗生素的發現「inaugurated an era where once-fatal bacterial infections could be cured in days」。"
        }
      ]
    }
  },
  {
    id: "auto",
    name: "auto-",
    type: "prefix",
    typeLabel: "希臘語字首 (Greek Prefix)",
    etymology: "源自古希臘語「αὐτός」(autós)，原意為「自己、本人、獨立自發 (self, same, spontaneous)」。",
    originMeaning: "自己、自發、自動、獨立",
    phonetic: "/ˈɔːtoʊ/",
    icon: "⚙️",
    color: "#EA580C",
    summary: "廣泛應用於人工智慧、自動化控制、自主性與個人創作的核心字首。",
    words: [
      {
        word: "automatic",
        kk: "[ˌɔtəˈmætɪk]",
        ipa: "/ˌɔːtəˈmætɪk/",
        pos: "adj.",
        meaning: "自動的、自發的、無意識的",
        formula: {
          parts: [
            { text: "auto-", role: "prefix", meaning: "自己、獨立 (希臘語 autós)" },
            { text: "mat", role: "base", meaning: "思考、意願、運動 (希臘語 matos 動作/自發)" },
            { text: "-ic", role: "suffix", meaning: "...的 (形容詞字尾)" }
          ],
          resultMeaning: "具備自主思考機制能自己運動運轉的 ➔「自動的」"
        },
        sentence: "The manufacturing facility upgraded its conveyor lines with automatic sensors that detect microscopic structural flaws.",
        sentenceZh: "該製造工廠以能偵測微觀結構瑕疵的自動感測器，升級了其輸送帶生產線。",
        grammar: {
          pattern: "S + Vt + O + Prep Phrase with Relative Clause (主詞 + 及物動詞 + 受詞 + 介系詞片語 + 關係子句)",
          breakdown: [
            { part: "The manufacturing facility", role: "主詞 (Subject)", note: "製造廠房設施。" },
            { part: "upgraded", role: "及物動詞 (Transitive Verb)", note: "upgrade A with B (以 B 升級 A)。" },
            { part: "its conveyor lines", role: "直接受詞 (Direct Object)", note: "輸送帶生產線。" },
            { part: "with automatic sensors", role: "介系詞工具片語 (Prepositional Instrument)", note: "automatic 修飾 sensors。" },
            { part: "that detect microscopic structural flaws", role: "限定關係子句 (Relative Clause)", note: "that 指代複數 sensors，子句動詞為原形 detect。" }
          ],
          keyPoints: [
            "【動詞句型】：upgrade A with B (以 B 裝備/升級 A)。",
            "【反義字】：manual (手動的；源自 manus 手)。"
          ]
        }
      },
      {
        word: "autonomy",
        kk: "[ɔˈtɑnəmi]",
        ipa: "/ɔːˈtɑːnəmi/",
        pos: "n.",
        meaning: "自治、自治權、自主性、獨立決策權",
        formula: {
          parts: [
            { text: "auto-", role: "prefix", meaning: "自己 (希臘語 autós)" },
            { text: "nomy", role: "root", meaning: "法律、規則 (希臘語 nomos 法則)" }
          ],
          resultMeaning: "自己給自己制定法則自行治理 ➔「自治、自主權」"
        },
        sentence: "Fostering employee autonomy often stimulates breakthrough innovation within technology research startups.",
        sentenceZh: "培養員工的自主獨立性，往往能在科技研發新創公司中激發突破性的創新。",
        grammar: {
          pattern: "Gerund Subject + Adv + Vt + O + Prepositional Location (動名詞主詞 + 頻率副詞 + 及物動詞 + 受詞 + 地點介系詞片語)",
          breakdown: [
            { part: "Fostering employee autonomy", role: "動名詞片語主詞 (Gerund Subject)", note: "單數動名詞概念。" },
            { part: "often stimulates", role: "謂語 (Predicate)", note: "stimulates (加 s 配合動名詞主詞)。" },
            { part: "breakthrough innovation", role: "直接受詞 (Direct Object)", note: "breakthrough (突破性的) 作形容詞修飾 innovation。" },
            { part: "within technology research startups", role: "地點範圍片語 (Prepositional Modifier)", note: "在科技新創中。" }
          ],
          keyPoints: [
            "【詞根網絡】：-nomy (法則/管理)，同根字如 astronomy (astro 星星 + nomy 法則 = 天文學)、economy (oikos 家 + nomy 法則 = 經濟學)。",
            "【形容詞型態】：autonomous (自治的、自主的，如 autonomous vehicles 自動駕駛車)。"
          ]
        }
      },
      {
        word: "autopilot",
        kk: "[ˈɔtoˌpaɪlət]",
        ipa: "/ˈɔːtoʊpaɪlət/",
        pos: "n.",
        meaning: "自動駕駛系統；(引申) 慣性無意識狀態",
        formula: {
          parts: [
            { text: "auto-", role: "prefix", meaning: "自動、自己 (希臘語 autós)" },
            { text: "pilot", role: "base", meaning: "飛行員、舵手 (義大利語 pilota)" }
          ],
          resultMeaning: "代替人類飛行員進行自動姿態導航的裝置 ➔「自動駕駛」"
        },
        sentence: "Modern passenger aircraft can cruise safely on autopilot while aviators monitor navigation displays for severe turbulence.",
        sentenceZh: "現代客機能在自動駕駛模式下安全平穩巡航，同時飛行員監控導航螢幕以防遭遇劇烈亂流。",
        grammar: {
          pattern: "S + Modal + Vi + Adv + Prep Phrase + While-Clause (主詞 + 助動詞 + 不及物動詞 + 副詞 + 介系詞片語 + While時間子句)",
          breakdown: [
            { part: "Modern passenger aircraft", role: "主詞 (Subject)", note: "aircraft 單複數同形，此處作複數。" },
            { part: "can cruise", role: "謂語 (Modal Predicate)", note: "cruise 不及物動詞表巡航。" },
            { part: "safely on autopilot", role: "方式副詞與片語 (Adverbials)", note: "on autopilot (處於自動駕駛狀態)。" },
            { part: "while aviators monitor navigation displays", role: "時間對稱子句 (Time Clause)", note: "while 連接詞表示兩件事情同時進行。" },
            { part: "for severe turbulence", role: "目的/防範介系詞片語 (Prepositional Phrase)", note: "monitor... for... (監控防範...現象)。" }
          ],
          keyPoints: [
            "【常用生活引申片語】：be on autopilot (心不在焉、憑習慣機械式地做事)。",
            "【名詞單複數】：aircraft 單複數同形，不加 s。"
          ]
        }
      }
    ],
    article: {
      title: "The Autonomous Frontier: Machines and the Self",
      titleZh: "自主新前沿：機械自律與人之主體",
      intro: "字首 auto- 象徵著脫離外在牽制、追尋自主運轉的野心。從希臘城邦的自治 (autonomy) 到今日無人載具的自動駕駛 (autopilot)，自我力量持續進化。",
      paragraphs: [
        {
          en: "In modern factories, automatic assembly lines perform intricate precision tasks twenty-four hours a day without human fatigue. Robotic arms weld steel frames with microscopic tolerance, demonstrating the pinnacle of mechanical self-regulation.",
          zh: "在現代工廠中，自動化組裝線每天二十四小時執行著錯綜複雜的精密任務而毫無人為疲憊。機械手臂以微米級的公差焊接鋼架，展現了機械自主調控的巔峰。"
        },
        {
          en: "However, ethical thinkers caution that human beings should never put their moral discernment on autopilot. While artificial systems enjoy increasing operational autonomy, the ultimate responsibility for human destiny must always rest within our own conscious hands.",
          zh: "然而，倫理學者提出告誡：人類絕不能將自身的道德辨別力置於「慣性自動導航」狀態。儘管人工智慧系統享有日益增長的操作自主權，人類命運的終極責任仍必須永遠掌握在我們自己自覺的雙手中。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What warning do ethical thinkers provide regarding 'autopilot'?",
          qZh: "倫理學者針對「自動駕駛/無意識狀態」提出了什麼警告？",
          options: [
            "A. Humans should never put their moral discernment on autopilot. (人類絕不應將道德辨別力置於無意識慣性中)",
            "B. Airplanes should completely ban automatic pilots.",
            "C. Robots should replace human judges in courtrooms.",
            "D. Factory machines must be operated by coal."
          ],
          answer: 0,
          explanation: "文中第二段指出「ethical thinkers caution that human beings should never put their moral discernment on autopilot」。"
        }
      ]
    }
  },
  {
    id: "chron",
    name: "chron",
    type: "root",
    typeLabel: "希臘語字根 (Greek Root)",
    etymology: "源自古希臘神話時間之神與名詞「χρόνος」(khrónos)，意指「時間、時序 (time)」。",
    originMeaning: "時間、時代、時序",
    phonetic: "/krɑːn/",
    icon: "⏱️",
    color: "#E11D48",
    summary: "記錄歷史演進、時間同步、長期慢性狀態與編年史的核心字根。",
    words: [
      {
        word: "chronology",
        kk: "[krəˈnɑlədʒi]",
        ipa: "/krəˈnɑːlədʒi/",
        pos: "n.",
        meaning: "年代學、年代順序、年表",
        formula: {
          parts: [
            { text: "chron", role: "root", meaning: "時間 (希臘語 khrónos)" },
            { text: "-ology", role: "suffix", meaning: "學問、研究 (希臘語 logos)" }
          ],
          resultMeaning: "研究事件在時間長河中先後排列順序的學問 ➔「年代學、時序表」"
        },
        sentence: "Archaeologists reconstructed the chronology of ancient Egyptian dynasties by cross-referencing astronomical records with radiocarbon dating.",
        sentenceZh: "考古學家藉由將天文紀錄與放射性碳定年法相互參照，重建了古埃及各王朝的歷史年代順序表。",
        grammar: {
          pattern: "S + Vt + O + Means Participial Phrase (主詞 + 及物動詞 + 受詞 + 方式分詞介系詞片語)",
          breakdown: [
            { part: "Archaeologists", role: "主詞 (Subject)", note: "考古學家 (archaeo 古代 + logist 研究者)。" },
            { part: "reconstructed", role: "及物動詞 (Transitive Verb)", note: "過去式。" },
            { part: "the chronology of ancient Egyptian dynasties", role: "直接受詞 (Direct Object)", note: "年代順序表。" },
            { part: "by cross-referencing astronomical records with radiocarbon dating", role: "方式介系詞片語 (By + Gerund)", note: "cross-reference A with B (將 A 與 B 交互對照)。" }
          ],
          keyPoints: [
            "【高階搭配片語】：by cross-referencing A with B (藉由將 A 與 B 相互對照)。",
            "【形容詞】：chronological (按時間順序排列的，如 in chronological order)。"
          ]
        }
      },
      {
        word: "synchronize",
        kk: "[ˈsɪŋkrəˌnaɪz]",
        ipa: "/ˈsɪŋkrənaɪz/",
        pos: "v.",
        meaning: "使同步、同時發生",
        formula: {
          parts: [
            { text: "syn-", role: "prefix", meaning: "共同、一起 (希臘語 syn)" },
            { text: "chron", role: "root", meaning: "時間 (希臘語 khrónos)" },
            { text: "-ize", role: "suffix", meaning: "使成為、動詞字尾" }
          ],
          resultMeaning: "使不同的鐘錶與動作歸攏在同一個時間點進行 ➔「使同步」"
        },
        sentence: "Telecommunication satellites synchronize their atomic clocks to ensure millisecond GPS triangulation accuracy.",
        sentenceZh: "電信衛星同步其原子鐘，以確保毫秒級的全球衛星定位三角測量精準度。",
        grammar: {
          pattern: "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          breakdown: [
            { part: "Telecommunication satellites", role: "主詞 (Subject)", note: "複數主詞 (tele- + communicate)。" },
            { part: "synchronize", role: "及物動詞 (Transitive Verb)", note: "原形動詞。" },
            { part: "their atomic clocks", role: "直接受詞 (Direct Object)", note: "原子鐘。" },
            { part: "to ensure millisecond GPS triangulation accuracy", role: "目的狀詞 (Infinitive of Purpose)", note: "ensure 接著名詞片語 accuracy。" }
          ],
          keyPoints: [
            "【縮寫常見語】：雲端備份常用的 sync 即為 synchronize 的簡寫！",
            "【反義詞】：asynchronous (非同步的；a- 無/非 + synchronize)。"
          ]
        }
      },
      {
        word: "chronic",
        kk: "[ˈkrɑnɪk]",
        ipa: "/ˈkrɑːnɪk/",
        pos: "adj.",
        meaning: "慢性的、長期的、難以根除的",
        formula: {
          parts: [
            { text: "chron", role: "root", meaning: "時間 (希臘語 khrónos)" },
            { text: "-ic", role: "suffix", meaning: "...的 (形容詞字尾)" }
          ],
          resultMeaning: "拖延拉扯很長時間難以痊癒的 ➔「慢性的、長期的」"
        },
        sentence: "Urban sociologists warn that chronic traffic congestion inflicts staggering economic losses on developing metropolitan regions.",
        sentenceZh: "都市社會學家提出警告，長期的交通擁堵會給發展中的大都會地區帶來驚人的經濟損失。",
        grammar: {
          pattern: "S + Vt + That-Noun Clause (主詞 + 及物動詞 + That引導之受詞名詞子句)",
          breakdown: [
            { part: "Urban sociologists", role: "主詞 (Subject)", note: "都市社會學家。" },
            { part: "warn", role: "及物動詞 (Transitive Verb)", note: "警告。" },
            { part: "that chronic traffic congestion inflicts staggering economic losses on developing metropolitan regions", role: "名詞子句受詞 (Noun Clause)", note: "子句主詞 congestion，動詞 inflicts (inflict A on B 施加損失於某地)。" }
          ],
          keyPoints: [
            "【固定搭配詞組】：inflict losses on... (對...造成損失)。",
            "【醫學對比】：chronic disease (慢性病) vs. acute disease (急性病)。"
          ]
        }
      }
    ],
    article: {
      title: "Guardians of the River of Time: The Measure of Chronos",
      titleZh: "時間之河的守護者：度量克羅諾斯之律",
      intro: "希臘人敬畏時間神 Chronos，深知生命、歷史與文明皆流淌在時序 (chron) 的刻度之中。",
      paragraphs: [
        {
          en: "From the earliest stone sundials to atomic clocks ticking aboard satellites, humanity has continually striven to synchronize our fleeting lives with the rhythm of the cosmos.",
          zh: "從最早期的石頭日晷到衛星上滴答運轉的原子鐘，人類不斷奮力將我們短暫的生命與宇宙的節奏同步。"
        },
        {
          en: "By cataloging world history into an accurate chronology, historians preserve the memory of ancient empires. Even when modern societies struggle against chronic economic volatility, the lessons carved into time's chronicles guide us steadily forward.",
          zh: "藉由將世界歷史編排入精確的年代學順序表中，歷史學家得以銘存古代帝國的記憶。即使當現代社會在長期的經濟波動中掙扎奮鬥，那些銘刻在時間編年史中的教訓依然引領著我們穩步向前。"
        }
      ],
      comprehensionQuestions: [
        {
          q: "What role does an accurate chronology play for historians?",
          qZh: "精確的年代學為歷史學家發揮了什麼作用？",
          options: [
            "A. Preserving the memory of ancient empires across time. (跨越時間長河銘存古代帝國的記憶)",
            "B. Predicting winning lottery tickets.",
            "C. Building mechanical water clocks.",
            "D. Erasing past historical records."
          ],
          answer: 0,
          explanation: "文中第二段指出「By cataloging world history into an accurate chronology, historians preserve the memory of ancient empires」。"
        }
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ETYMO_DATA };
}
