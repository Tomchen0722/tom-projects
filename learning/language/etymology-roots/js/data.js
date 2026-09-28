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
,
  {
    "id": "audi",
    "name": "audi / audit",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「audire」(聽、傾聽、聽審)。",
    "originMeaning": "聽、聲音、聽覺、查核",
    "phonetic": "/ˈɔːdi/ 或 /ˈɔːdɪt/",
    "icon": "🎧",
    "color": "#0D9488",
    "summary": "與聲音傳導、聽覺感知、大型聽眾聚集場所及帳務聽審審計密切相關。",
    "words": [
      {
        "word": "audible",
        "kk": "[ˈɔdəb!]",
        "ipa": "/ˈɔːdəbl/",
        "pos": "adj.",
        "meaning": "聽得見的、音量清晰的",
        "formula": {
          "parts": [
            {
              "text": "audi",
              "role": "root",
              "meaning": "聽 (拉丁語 audire)"
            },
            {
              "text": "-able",
              "role": "suffix",
              "meaning": "能夠...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "能夠被人類耳朵清晰聽見的 ➔「聽得見的」"
        },
        "sentence": "The whisper was barely audible above the roaring engine noise inside the crowded hangar.",
        "sentenceZh": "在擁擠機庫內引擎轟鳴的喧囂聲中，那低語聲幾乎微弱得聽不見。",
        "grammar": {
          "pattern": "S + Linking Verb + Adv + Predicate Adjective + Prep Phrase (主詞 + 連綴動詞 + 程度副詞 + 形容詞補語 + 介系詞片語)",
          "breakdown": [
            {
              "part": "The whisper",
              "role": "主詞 (Subject)",
              "note": "名詞「低語聲」。"
            },
            {
              "part": "was",
              "role": "連綴動詞 (Linking Verb)",
              "note": "be 動詞過去式。"
            },
            {
              "part": "barely audible",
              "role": "主詞補語 (Subject Complement)",
              "note": "否定副詞 barely (幾乎不) 修飾形容詞 audible。"
            },
            {
              "part": "above the roaring engine noise",
              "role": "比較介系詞片語 (Prepositional Phrase)",
              "note": "above 表聲音穿透高過於另一背景噪音；roaring 為現在分詞作形容詞。"
            },
            {
              "part": "inside the crowded hangar",
              "role": "地點介系詞片語 (Locative Adverbial)",
              "note": "crowded (擁擠的) 修飾機庫 hangar。"
            }
          ],
          "keyPoints": [
            "【否定副詞用法】：barely / scarcely / hardly 均帶有準否定意味 (幾乎不)。",
            "【字根反義詞】：inaudible (聽不見的；in- 不 + audible)。"
          ]
        }
      },
      {
        "word": "audience",
        "kk": "[ˈɔdɪəns]",
        "ipa": "/ˈɔːdiəns/",
        "pos": "n.",
        "meaning": "觀眾、聽眾、讀者群",
        "formula": {
          "parts": [
            {
              "text": "audi",
              "role": "root",
              "meaning": "聽 (拉丁語 audire)"
            },
            {
              "text": "-ence",
              "role": "suffix",
              "meaning": "性質、狀態、群體 (名詞字尾)"
            }
          ],
          "resultMeaning": "聚在一起專注傾聽音樂演說的人群 ➔「聽眾、觀眾」"
        },
        "sentence": "The mesmerizing symphony held the captivated audience spellbound throughout the entire ninety-minute recital.",
        "sentenceZh": "這部引人入勝的交響樂在長達九十分鐘的整場演奏會中，讓全體陶醉的聽眾聽得如痴如醉。",
        "grammar": {
          "pattern": "S + Vt + O + Object Complement + Time Adverbial (主詞 + 及物動詞 + 受詞 + 受詞補語 + 時間狀詞)",
          "breakdown": [
            {
              "part": "The mesmerizing symphony",
              "role": "主詞 (Subject)",
              "note": "mesmerizing (令人著迷的) 為現在分詞形容詞。"
            },
            {
              "part": "held",
              "role": "及物動詞 (Transitive Verb)",
              "note": "hold 的過去式，用於 hold + O + adj. 句型。"
            },
            {
              "part": "the captivated audience",
              "role": "直接受詞 (Direct Object)",
              "note": "captivated (被深深吸引的) 為過去分詞修飾 audience。"
            },
            {
              "part": "spellbound",
              "role": "受詞補語 (Object Complement)",
              "note": "形容詞，表示「被符咒吸引般出神的」。"
            },
            {
              "part": "throughout the entire ninety-minute recital",
              "role": "時間介系詞片語 (Time Adverbial)",
              "note": "throughout 表貫穿整場演出。"
            }
          ],
          "keyPoints": [
            "【及物使動句型】：hold somebody spellbound (使某人看得入迷/聽得出神)。",
            "【集合名詞概念】：audience 若強調整體視為單數，強調個別成員視為複數。"
          ]
        }
      },
      {
        "word": "auditorium",
        "kk": "[ˌɔdəˈtorɪəm]",
        "ipa": "/ˌɔːdɪˈtɔːriəm/",
        "pos": "n.",
        "meaning": "禮堂、音樂廳、觀眾席",
        "formula": {
          "parts": [
            {
              "text": "audit",
              "role": "root",
              "meaning": "聽 (拉丁語 audire)"
            },
            {
              "text": "-orium",
              "role": "suffix",
              "meaning": "場所、建築地點 (名詞字尾)"
            }
          ],
          "resultMeaning": "專門用來供人們坐著聆聽大型音樂與演說的場所 ➔「大禮堂、音樂廳」"
        },
        "sentence": "Acoustic architects engineered the spacious auditorium to reflect pure harmonic frequencies evenly to every seat.",
        "sentenceZh": "聲學建築師設計這座寬敞的音樂大禮堂，旨在將純淨的和聲頻率均勻反射到每一個座位。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Adverbial (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 副詞與介系詞受詞)",
          "breakdown": [
            {
              "part": "Acoustic architects",
              "role": "主詞 (Subject)",
              "note": "聲學工程建築師。"
            },
            {
              "part": "engineered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "在此作動詞「精心設計規劃」。"
            },
            {
              "part": "the spacious auditorium",
              "role": "受詞 (Direct Object)",
              "note": "spacious (寬敞的) 修飾禮堂。"
            },
            {
              "part": "to reflect pure harmonic frequencies",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "不定詞片語表設計目的。"
            },
            {
              "part": "evenly to every seat",
              "role": "方式與方向狀詞 (Adverbials)",
              "note": "evenly (均勻地) 修飾 reflect；to every seat 表接受端。"
            }
          ],
          "keyPoints": [
            "【場所字尾 -orium】：同源場所詞如 sanatorium (療養院)、planetarium (天文館)。",
            "【及物動詞轉用】：engineer 作動詞表示「以工程技術精準打造」。"
          ]
        }
      },
      {
        "word": "audit",
        "kk": "[ˈɔdɪt]",
        "ipa": "/ˈɔːdɪt/",
        "pos": "v. / n.",
        "meaning": "(v.) 查核、審計帳目、旁聽課程；(n.) 審計、查帳",
        "formula": {
          "parts": [
            {
              "text": "audit",
              "role": "root",
              "meaning": "聽審、聽取陳述 (拉丁語 audire)"
            }
          ],
          "resultMeaning": "古代官員親自坐堂聽取受查人口頭報告帳務收支 ➔「審計、查帳」"
        },
        "sentence": "Independent certified accountants audit corporate financial ledgers to detect irregularities and verify fiscal transparency.",
        "sentenceZh": "獨立執業會計師查核企業財務總帳，以偵測有無不法違規並核實財政透明度。",
        "grammar": {
          "pattern": "S + Vt + O + Compound Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 對等目的不定詞片語)",
          "breakdown": [
            {
              "part": "Independent certified accountants",
              "role": "主詞 (Subject)",
              "note": "獨立執業會計師 (certified 為合格認證的)。"
            },
            {
              "part": "audit",
              "role": "及物動詞 (Transitive Verb)",
              "note": "審計查核。"
            },
            {
              "part": "corporate financial ledgers",
              "role": "直接受詞 (Direct Object)",
              "note": "企業財務總帳簿。"
            },
            {
              "part": "to detect irregularities and verify fiscal transparency",
              "role": "對等目的狀詞 (Coordinated Infinitives)",
              "note": "to detect A and [to] verify B，第二個 to 省略。"
            }
          ],
          "keyPoints": [
            "【詞源歷史趣味】：古羅馬時期大多帳目是由管家「口述口報」，主考官藉由「聽 (audire)」來核查，因而衍生出今日的審計 audit！",
            "【大學教育用法】：audit a course 代表「旁聽課程」（只聽不計學分）。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Symphony of the Audible Realm: The Art of Listening",
      "titleZh": "傾聽之聲：音響與聽覺的文明樂章",
      "intro": "從母親溫柔可聞的搖籃曲 (audible)，到宏偉禮堂 (auditorium) 裡萬人屏息的交響樂，字根 audi- 訴說著人類用耳朵探索世界的深情記憶。",
      "paragraphs": [
        {
          "en": "Inside the grand concert auditorium, a hushed silence fell as the conductor raised his baton. When the soloist struck the opening piano chord, the notes resonated with crystal clarity, remaining distinctly audible even to listeners perched in the highest balconies.",
          "zh": "在宏偉的音樂大禮堂內，當指揮舉起指揮棒時，全場頓時肅靜無聲。當鋼琴獨奏家彈響開場和弦時，音符帶著水晶般的澄澈迴響共鳴，即便是坐在最高層看台上的聽眾也能清晰聽聞。"
        },
        {
          "en": "The enthralled audience listened breathlessly as harmonious overtones wove an emotional narrative. Meanwhile, in business institutions outside the concert hall, meticulous regulators continually audit balances, reminding us that listening with honesty underpins both art and society.",
          "zh": "陶醉的觀眾屏氣凝神地傾聽著，和諧的和聲織就出一幅動人的情感畫卷。與此同時，在音樂廳之外的商業機構中，嚴謹的監管者持續查核帳目，提醒著我們：真誠的傾聽與審視，是支撐藝術與社會共同前行的基石。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "Why was the piano chord remarkable inside the auditorium?",
          "qZh": "為什麼大禮堂內的鋼琴和弦如此引人注目？",
          "options": [
            "A. It was distinctly audible even to listeners in the highest balconies. (即便利在最高看台也清晰可聞)",
            "B. It broke the microphone instantly.",
            "C. It was completely silent.",
            "D. It played backward automatically."
          ],
          "answer": 0,
          "explanation": "文中第一段指出和弦「remaining distinctly audible even to listeners perched in the highest balconies」。"
        }
      ]
    }
  },
  {
    "id": "micro",
    "name": "micro-",
    "type": "prefix",
    "typeLabel": "希臘語字首 (Greek Prefix)",
    "etymology": "源自古希臘語「μικρός」(mikrós)，原意為「微小、微細、極小 (small, minute)」，在科學度量衡中代表百萬分之一 (10^-6)。",
    "originMeaning": "微小、微型、百萬分之一",
    "phonetic": "/ˈmaɪkroʊ/",
    "icon": "🔬",
    "color": "#4F46E5",
    "summary": "用於表示肉眼不可見的微觀粒子、精密晶片、微生物或微小世界之縮影。",
    "words": [
      {
        "word": "microscope",
        "kk": "[ˈmaɪkrəˌskop]",
        "ipa": "/ˈmaɪkrəskoʊp/",
        "pos": "n.",
        "meaning": "顯微鏡",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小 (希臘語 mikrós)"
            },
            {
              "text": "scope",
              "role": "base",
              "meaning": "觀察儀器 (希臘語 skopein 看)"
            }
          ],
          "resultMeaning": "用以觀察微小肉眼不可見物體的儀器 ➔「顯微鏡」"
        },
        "sentence": "Using an advanced electron microscope, virologists observed the intricate protein spikes of the novel pathogen.",
        "sentenceZh": "病毒學家運用先進的電子顯微鏡，觀察了該新型病原體錯綜複雜的突刺蛋白結構。",
        "grammar": {
          "pattern": "Participial Instrument Phrase + S + Vt + O (分詞工具狀詞 + 主詞 + 及物動詞 + 受詞)",
          "breakdown": [
            {
              "part": "Using an advanced electron microscope",
              "role": "方式狀詞 (Participial Adverbial)",
              "note": "現在分詞片語表示藉由某工具手段。"
            },
            {
              "part": "virologists",
              "role": "主詞 (Subject)",
              "note": "病毒學家。"
            },
            {
              "part": "observed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "觀察。"
            },
            {
              "part": "the intricate protein spikes of the novel pathogen",
              "role": "直接受詞 (Direct Object)",
              "note": "intricate (錯綜複雜的)；novel (新型的)。"
            }
          ],
          "keyPoints": [
            "【雙重對比】：telescope (遠看 ➔ 望遠鏡) vs. microscope (微看 ➔ 顯微鏡)。",
            "【多義字彙】：novel 在此作形容詞「新型的原創的」，而非名詞「小說」。"
          ]
        }
      },
      {
        "word": "microchip",
        "kk": "[ˈmaɪkroˌtʃɪp]",
        "ipa": "/ˈmaɪkroʊtʃɪp/",
        "pos": "n.",
        "meaning": "微晶片、微型積體電路片",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小 (希臘語 mikrós)"
            },
            {
              "text": "chip",
              "role": "base",
              "meaning": "薄片、碎片 (日耳曼語 kipp 碎削)"
            }
          ],
          "resultMeaning": "集成數十億個微米級電晶體的矽薄片 ➔「微晶片」"
        },
        "sentence": "A fingernail-sized silicon microchip contains billions of transistors capable of processing complex cryptographic algorithms.",
        "sentenceZh": "一枚僅有指甲大小的矽微晶片，容納著數十億個能處理複雜密碼學演算法的電晶體。",
        "grammar": {
          "pattern": "S + Vt + O + Adjective Modifier (主詞 + 及物動詞 + 受詞 + 形容詞片語後位修飾)",
          "breakdown": [
            {
              "part": "A fingernail-sized silicon microchip",
              "role": "主詞 (Subject)",
              "note": "複合形容詞 fingernail-sized 與材料名詞 silicon 共同修飾 microchip。"
            },
            {
              "part": "contains",
              "role": "及物動詞 (Transitive Verb)",
              "note": "單數現在式。"
            },
            {
              "part": "billions of transistors",
              "role": "直接受詞 (Direct Object)",
              "note": "數十億個電晶體。"
            },
            {
              "part": "capable of processing complex cryptographic algorithms",
              "role": "後位修飾形容詞片語 (Post-nominal Adjective Phrase)",
              "note": "修飾 transistors，相當於 which are capable of..."
            }
          ],
          "keyPoints": [
            "【固定搭配詞組】：be capable of + V-ing (具備...的能力)。",
            "【科技構詞法】：microprocessor (微處理器)、microelectronics (微電子學)。"
          ]
        }
      },
      {
        "word": "microcosm",
        "kk": "[ˈmaɪkrəˌkɑzəm]",
        "ipa": "/ˈmaɪkrəˌkɑːzəm/",
        "pos": "n.",
        "meaning": "微觀世界、小宇宙、縮影",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小 (希臘語 mikrós)"
            },
            {
              "text": "cosm",
              "role": "base",
              "meaning": "宇宙、世界 (希臘語 kosmos 秩序/宇宙)"
            }
          ],
          "resultMeaning": "濃縮並反映宏觀大宇宙全部法則的微小個體 ➔「小宇宙、微觀縮影」"
        },
        "sentence": "Sociologists consider the diverse multicultural classroom a vibrant microcosm of twenty-first-century urban society.",
        "sentenceZh": "社會學家將這個多元文化的班級視為二十一世紀城市社會生機勃勃的縮影。",
        "grammar": {
          "pattern": "S + Vt + O + Object Complement (主詞 + 及物動詞 + 受詞 + 受詞補語)",
          "breakdown": [
            {
              "part": "Sociologists",
              "role": "主詞 (Subject)",
              "note": "社會學家。"
            },
            {
              "part": "consider",
              "role": "及物動詞 (Transitive Verb)",
              "note": "接 consider A (to be) B 句型。"
            },
            {
              "part": "the diverse multicultural classroom",
              "role": "受詞 A (Direct Object)",
              "note": "多元文化教室。"
            },
            {
              "part": "a vibrant microcosm of twenty-first-century urban society",
              "role": "受詞補語 B (Objective Complement)",
              "note": "名詞補語說明 A 的屬性縮影。"
            }
          ],
          "keyPoints": [
            "【對稱概念】：microcosm (微觀縮影) vs. macrocosm (宏觀大宇宙；macro- 巨大)。",
            "【名詞句型】：consider A B (將 A 視為 B，省略 to be)。"
          ]
        }
      },
      {
        "word": "microorganism",
        "kk": "[ˌmaɪkroˈɔrgənˌɪzəm]",
        "ipa": "/ˌmaɪkroʊˈɔːrɡənɪzəm/",
        "pos": "n.",
        "meaning": "微生物（細菌、病毒、真菌統稱）",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小 (希臘語 mikrós)"
            },
            {
              "text": "organism",
              "role": "base",
              "meaning": "有機體、生物 (希臘語 organon 工具/器官)"
            }
          ],
          "resultMeaning": "肉眼難以辨識必須藉由儀器觀察的微小生命體 ➔「微生物」"
        },
        "sentence": "Beneficial soil microorganisms decompose fallen leaves into fertile nutrients that nourish majestic forest canopies.",
        "sentenceZh": "有益的土壤微生物將落葉分解為肥沃的養分，滋養著雄偉的森林林冠。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Relative Clause (主詞 + 及物動詞 + 受詞 + 產物介系詞片語 + 關係子句)",
          "breakdown": [
            {
              "part": "Beneficial soil microorganisms",
              "role": "主詞 (Subject)",
              "note": "有益的土壤微生物 (複數)。"
            },
            {
              "part": "decompose",
              "role": "及物動詞 (Transitive Verb)",
              "note": "分解。"
            },
            {
              "part": "fallen leaves",
              "role": "受詞 (Direct Object)",
              "note": "落葉 (fallen 為過去分詞轉形容詞)。"
            },
            {
              "part": "into fertile nutrients",
              "role": "轉變結果介系詞片語 (Prepositional Phrase)",
              "note": "decompose A into B (將 A 分解轉化為 B)。"
            },
            {
              "part": "that nourish majestic forest canopies",
              "role": "限定關係子句 (Relative Clause)",
              "note": "that 指代 nutrients，子句動詞為原形 nourish。"
            }
          ],
          "keyPoints": [
            "【動詞片語搭配】：decompose / transform A into B (將 A 轉化分解為 B)。",
            "【分詞狀態】：fallen leaves (已掉落的葉片；過去分詞表完成狀態)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Wonders of the Micro Realm: Revealing the Invisible",
      "titleZh": "微觀之境：揭開肉眼不及的浩瀚宇宙",
      "intro": "宇宙最深奧的秘密，往往並非隱藏在遙遠的星雲中，而是蟄伏於微米 (micro-) 等級的微觀世界。",
      "paragraphs": [
        {
          "en": "Until Dutch scientist Antonie van Leeuwenhoek looked through his handcrafted microscope in the seventeenth century, humans were oblivious to the bustling civilizations of microorganisms thriving inside a single drop of pond water.",
          "zh": "直到十七世紀荷蘭科學家雷文霍克透過他手工打造的顯微鏡觀察之前，人類對在一滴池塘水中蓬勃繁衍的微生物熱鬧文明全然一無所知。"
        },
        {
          "en": "In the contemporary digital era, that same fascination with the minute drives our technological frontier. By carving microscopic architectures onto silicon microchips, engineers condense the computing prowess of an entire supercomputer into a handheld smartphone, proving that the microcosm holds the key to the future.",
          "zh": "在當代數位時代，對微小事物同樣的著迷正推動著我們的科技前沿。藉由在矽微晶片上雕刻微觀結構，工程師將整座超級電腦的運算實力濃縮進掌上智慧型手機中，證明了微觀世界掌握著通往未來的鑰匙。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What technological breakthrough was achieved by carving architectures onto microchips?",
          "qZh": "藉由在微晶片上雕刻微觀架構達成了什麼科技突破？",
          "options": [
            "A. Condensing supercomputer computing prowess into handheld smartphones. (將超級電腦的運算實力濃縮入掌上手機)",
            "B. Freezing pond water permanently.",
            "C. Replacing human teachers in classrooms.",
            "D. Stopping the flow of time."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「condense the computing prowess of an entire supercomputer into a handheld smartphone」。"
        }
      ]
    }
  },
  {
    "id": "scrib",
    "name": "scrib / script",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「scribere」(書寫、銘刻)，過去分詞為 scriptum。",
    "originMeaning": "寫、記錄、銘刻、文字",
    "phonetic": "/skraɪb/ 或 /skrɪpt/",
    "icon": "✍️",
    "color": "#BE185D",
    "summary": "涵蓋文字書寫、手稿、處方箋開立、描述、官方文字紀錄及訂閱服務。",
    "words": [
      {
        "word": "describe",
        "kk": "[dɪˈskraɪb]",
        "ipa": "/dɪˈskraɪb/",
        "pos": "v.",
        "meaning": "描寫、描述、描繪",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "向下、詳盡 (拉丁語 de-)"
            },
            {
              "text": "scribe",
              "role": "root",
              "meaning": "寫 (拉丁語 scribere)"
            }
          ],
          "resultMeaning": "將細節由上而下詳盡書寫記錄在紙上 ➔「描寫、描述」"
        },
        "sentence": "Eyewitnesses struggled to describe the elusive astronomical phenomenon because words felt inadequate to capture its radiant grandeur.",
        "sentenceZh": "目擊者難以描摹那罕見難逢的天文現象，因為任何言語詞彙似乎都不足以捕捉其耀眼奪目的壯麗。",
        "grammar": {
          "pattern": "S + Vi + Infinitive Complement + Reason Adverbial Clause (主詞 + 不及物動詞 + 不定詞補語 + 原因副詞子句)",
          "breakdown": [
            {
              "part": "Eyewitnesses",
              "role": "主詞 (Subject)",
              "note": "目擊者。"
            },
            {
              "part": "struggled",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "搭配 struggle to V (吃力艱難地進行某事)。"
            },
            {
              "part": "to describe the elusive astronomical phenomenon",
              "role": "不定詞受詞/補語 (Infinitive)",
              "note": "elusive (難以捉摸的)；phenomenon 單數名詞 (複數 phenomena)。"
            },
            {
              "part": "because words felt inadequate to capture its radiant grandeur",
              "role": "原因副詞子句 (Clause of Reason)",
              "note": "because 引導子句；felt 為連綴動詞，inadequate (不足的) 為補語，後接不定詞 to capture。"
            }
          ],
          "keyPoints": [
            "【動詞搭配句型】：struggle to V (竭力/吃力地做某事)。",
            "【希臘單複數名詞】：phenomenon (單數) ➔ phenomena (複數)。"
          ]
        }
      },
      {
        "word": "prescribe",
        "kk": "[prɪˈskraɪb]",
        "ipa": "/prɪˈskraɪb/",
        "pos": "v.",
        "meaning": "開處方、開藥、規定、指示",
        "formula": {
          "parts": [
            {
              "text": "pre-",
              "role": "prefix",
              "meaning": "在之前、預先 (拉丁語 prae)"
            },
            {
              "text": "scribe",
              "role": "root",
              "meaning": "寫 (拉丁語 scribere)"
            }
          ],
          "resultMeaning": "在病患服藥之前由醫師預先寫下指示與用藥明細 ➔「開處方、規定」"
        },
        "sentence": "Specialist physicians prescribe tailored rehabilitation regimens to accelerate recovery following orthopedic surgery.",
        "sentenceZh": "專科醫師開立量身定制的復健方案，以加速骨科手術後的康復進程。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Time Prep Phrase (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 時間介系詞片語)",
          "breakdown": [
            {
              "part": "Specialist physicians",
              "role": "主詞 (Subject)",
              "note": "專科醫師。"
            },
            {
              "part": "prescribe",
              "role": "及物動詞 (Transitive Verb)",
              "note": "開立處方。"
            },
            {
              "part": "tailored rehabilitation regimens",
              "role": "直接受詞 (Direct Object)",
              "note": "tailored (量身打造的) 為分詞形容詞；regimen (養生/療程方案)。"
            },
            {
              "part": "to accelerate recovery",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "加速康復。"
            },
            {
              "part": "following orthopedic surgery",
              "role": "時間介系詞片語 (Time Prepositional Phrase)",
              "note": "following 作介系詞相當於 after (在...之後)。"
            }
          ],
          "keyPoints": [
            "【介系詞轉用】：following 在正式學術與醫學英文中常作介系詞 (= after)。",
            "【衍生名詞】：prescription (處方籤；script 形態回歸)。"
          ]
        }
      },
      {
        "word": "manuscript",
        "kk": "[ˈmænjəˌskrɪpt]",
        "ipa": "/ˈmænjuskrɪpt/",
        "pos": "n.",
        "meaning": "手稿、原稿、底稿",
        "formula": {
          "parts": [
            {
              "text": "manu",
              "role": "root",
              "meaning": "手 (拉丁語 manus 手)"
            },
            {
              "text": "script",
              "role": "root",
              "meaning": "寫 (拉丁語 scribere)"
            }
          ],
          "resultMeaning": "由作者親手逐字寫下的原始書稿 ➔「手稿、原稿」"
        },
        "sentence": "The museum curator preserved the fragile centuries-old manuscript in a climate-controlled vault to prevent parchment degradation.",
        "sentenceZh": "博物館館長將這份具有數百年歷史的脆弱古手稿保存在恆溫恆濕的保險庫中，以防止羊皮紙退化損壞。",
        "grammar": {
          "pattern": "S + Vt + O + Locative Prep Phrase + Infinitive of Negative Purpose (主詞 + 及物動詞 + 受詞 + 地點片語 + 否定防範目的狀詞)",
          "breakdown": [
            {
              "part": "The museum curator",
              "role": "主詞 (Subject)",
              "note": "博物館策展人/館長。"
            },
            {
              "part": "preserved",
              "role": "及物動詞 (Transitive Verb)",
              "note": "妥善保存。"
            },
            {
              "part": "the fragile centuries-old manuscript",
              "role": "直接受詞 (Direct Object)",
              "note": "複合形容詞 centuries-old 修飾手稿。"
            },
            {
              "part": "in a climate-controlled vault",
              "role": "地點介系詞片語 (Locative Phrase)",
              "note": "複合形容詞 climate-controlled (溫濕度調控的)。"
            },
            {
              "part": "to prevent parchment degradation",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "prevent 後接名詞受詞 degradation。"
            }
          ],
          "keyPoints": [
            "【雙重拉丁詞根】：manus (手，如 manual 手動的、manufacture 製造) + scriptum (書寫)。",
            "【材料歷史】：古手稿多書寫於羊皮紙 (parchment) 或莎草紙 (papyrus) 上。"
          ]
        }
      },
      {
        "word": "transcript",
        "kk": "[ˈtrænˌskrɪpt]",
        "ipa": "/ˈtrænskrɪpt/",
        "pos": "n.",
        "meaning": "文字記錄、逐字謄本、成績單",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "跨越、轉化 (拉丁語 trans-)"
            },
            {
              "text": "script",
              "role": "root",
              "meaning": "寫 (拉丁語 scribere)"
            }
          ],
          "resultMeaning": "將口頭語音或正式檔案轉錄寫成紙本文字 ➔「逐字記錄、成績單」"
        },
        "sentence": "Graduate school admissions committees require an official academic transcript stamped by the university registrar.",
        "sentenceZh": "研究所入學評審委員會要求提供一份蓋有大學註冊組戳印的官方正式學術成績單。",
        "grammar": {
          "pattern": "S + Vt + O + Participial Modifier (主詞 + 及物動詞 + 受詞 + 過去分詞片語後位修飾)",
          "breakdown": [
            {
              "part": "Graduate school admissions committees",
              "role": "主詞 (Subject)",
              "note": "複數委員會主詞。"
            },
            {
              "part": "require",
              "role": "及物動詞 (Transitive Verb)",
              "note": "要求。"
            },
            {
              "part": "an official academic transcript",
              "role": "直接受詞 (Direct Object)",
              "note": "正式學業成績謄本。"
            },
            {
              "part": "stamped by the university registrar",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "stamped (蓋印的) 修飾 transcript，by 引導施印機構。"
            }
          ],
          "keyPoints": [
            "【生活高頻語義】：在求學申請中 transcript 專指「成績單」；在法庭與採訪中指「逐字稿、聽證記錄」。",
            "【動詞形式】：transcribe (轉錄、謄寫；-scribe 結尾)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Inscribed Soul: How Writing Anchors Civilization",
      "titleZh": "銘刻的心靈：文字與書寫的永恆對話",
      "intro": "言語如風拂過，而文字一旦被銘刻 (scrib / script)，思想便跨越了時空的禁錮，化作永恆的印記。",
      "paragraphs": [
        {
          "en": "Before Gutenberg revolutionized movable type, medieval monks spent grueling decades in monastic scriptoriums, painstakingly copying religious manuscripts letter by letter with quills under flickering candlelight.",
          "zh": "在古騰堡革新活字印刷術之前，中世紀修士在修道院抄經室裡度過漫長艱辛的數十年，在搖曳的燭光下用羽毛筆一字一字苦心孤詣地謄抄宗教手稿。"
        },
        {
          "en": "Even in our paperless digital age, the imperative to write endures. When doctors prescribe life-saving remedies or journalists transcribe verbatim interviews, the ancient Latin root scribere continues to guarantee precision and accountability across human society.",
          "zh": "即使在我們無紙化的數位時代，書寫記錄的必要性依舊永存。當醫生開立挽救生命的處方，或記者謄寫一字不差的訪談逐字稿時，古拉丁字根 scribere 依然持續為人類社會捍衛著精確性與信實度。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "How did medieval monks copy manuscripts before the printing press?",
          "qZh": "在印刷機問世前，中世紀修士是如何抄寫手稿的？",
          "options": [
            "A. Painstakingly letter by letter with quills under candlelight. (燭光下用羽毛筆一字一字苦心謄寫)",
            "B. Using electric photocopy machines.",
            "C. By memorizing and reciting orally.",
            "D. Via computerized laser engravers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出修士「painstakingly copying religious manuscripts letter by letter with quills under flickering candlelight」。"
        }
      ]
    }
  },
  {
    "id": "poly",
    "name": "poly-",
    "type": "prefix",
    "typeLabel": "希臘語字首 (Greek Prefix)",
    "etymology": "源自古希臘語「πολύς」(polús)，原意為「多、眾多、多元 (many, much, multiple)」。",
    "originMeaning": "多、多重、多元",
    "phonetic": "/ˈpɑːli/",
    "icon": "🌈",
    "color": "#C026D3",
    "summary": "形容由多個單元組成的化學結構、幾何形狀、複音旋律或精通多種語言的能力。",
    "words": [
      {
        "word": "polyglot",
        "kk": "[ˈpɑlɪˌglɑt]",
        "ipa": "/ˈpɑːliɡlɑːt/",
        "pos": "n. / adj.",
        "meaning": "(n.) 精通多種語言的人；(adj.) 通曉數種語言的",
        "formula": {
          "parts": [
            {
              "text": "poly-",
              "role": "prefix",
              "meaning": "多、多重 (希臘語 polús)"
            },
            {
              "text": "glot",
              "role": "base",
              "meaning": "語言、舌頭 (希臘語 glōtta 舌/語言)"
            }
          ],
          "resultMeaning": "擁有能靈活切換多種不同舌頭語言能力的人 ➔「精通多種語言者」"
        },
        "sentence": "Fluent in seven languages, the diplomatic polyglot effortlessly mediated the delicate multilateral peace negotiations.",
        "sentenceZh": "這位精通七國語言的外交博學通譯人才，毫不費力地居中協調了這場微妙的多邊和平談判。",
        "grammar": {
          "pattern": "Adjective Phrase + S + Adv + Vt + O (形容詞修飾短語 + 主詞 + 方式副詞 + 及物動詞 + 受詞)",
          "breakdown": [
            {
              "part": "Fluent in seven languages",
              "role": "主詞修飾形容詞片語 (Appositive Adjective Phrase)",
              "note": "置於句首作補充修飾，fluent in + 語言。"
            },
            {
              "part": "the diplomatic polyglot",
              "role": "主詞 (Subject)",
              "note": "diplomatic (具外交長才的) 修飾多語專家。"
            },
            {
              "part": "effortlessly",
              "role": "方式副詞 (Adverb of Manner)",
              "note": "修飾及物動詞 mediated (居中調解)。"
            },
            {
              "part": "mediated",
              "role": "及物動詞 (Transitive Verb)",
              "note": "過去式。"
            },
            {
              "part": "the delicate multilateral peace negotiations",
              "role": "受詞 (Direct Object)",
              "note": "multilateral (multi- 多 + lateral 邊 = 多邊的)；delicate (微妙脆弱的)。"
            }
          ],
          "keyPoints": [
            "【前置形容詞補語】：Fluent in seven languages 置首精準傳達主角背景。",
            "【詞根網絡】：glot (語言/舌頭)，如 epiglottis (會厭軟骨)、glossary (詞彙表)。"
          ]
        }
      },
      {
        "word": "polygon",
        "kk": "[ˈpɑlɪˌgɑn]",
        "ipa": "/ˈpɑːliɡɑːn/",
        "pos": "n.",
        "meaning": "多邊形（幾何學）",
        "formula": {
          "parts": [
            {
              "text": "poly-",
              "role": "prefix",
              "meaning": "多 (希臘語 polús)"
            },
            {
              "text": "gon",
              "role": "base",
              "meaning": "角、轉折點 (希臘語 gōnia 角度)"
            }
          ],
          "resultMeaning": "由多條直線段封閉相連、擁有多個內角的幾何圖形 ➔「多邊形」"
        },
        "sentence": "Video game rendering engines assemble millions of tiny textured polygons to create realistic three-dimensional characters.",
        "sentenceZh": "電玩遊戲渲染引擎組合數百萬個微小的紋理多邊形，以創造栩栩如生的三維立體角色。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Video game rendering engines",
              "role": "主詞 (Subject)",
              "note": "遊戲渲染引擎 (rendering 為現在分詞作形容詞)。"
            },
            {
              "part": "assemble",
              "role": "及物動詞 (Transitive Verb)",
              "note": "組裝集合。"
            },
            {
              "part": "millions of tiny textured polygons",
              "role": "直接受詞 (Direct Object)",
              "note": "textured (具有材質紋理的) 修飾 polygons。"
            },
            {
              "part": "to create realistic three-dimensional characters",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "realistic (擬真的、逼真的)。"
            }
          ],
          "keyPoints": [
            "【角字根 -gon】：hexagon (六邊形；hexa- 6)、pentagon (五角形/美國五角大廈；penta- 5)。",
            "【電腦圖形學】：現代 3D 建模基本單元就是多邊形面 (polygonal mesh)。"
          ]
        }
      },
      {
        "word": "polymer",
        "kk": "[ˈpɑləmɚ]",
        "ipa": "/ˈpɑːlɪmər/",
        "pos": "n.",
        "meaning": "聚合物、高分子化合物",
        "formula": {
          "parts": [
            {
              "text": "poly-",
              "role": "prefix",
              "meaning": "多 (希臘語 polús)"
            },
            {
              "text": "mer",
              "role": "base",
              "meaning": "部分、單元 (希臘語 meros 零件/部分)"
            }
          ],
          "resultMeaning": "由許多相同或相似的小分子重複單元鏈接而成的大分子 ➔「聚合物」"
        },
        "sentence": "Materials scientists synthesized a heat-resistant synthetic polymer suitable for insulating aerospace electrical conduits.",
        "sentenceZh": "材料科學家合成出一種適用於航太電氣管道絕緣的耐熱型合成聚合物。",
        "grammar": {
          "pattern": "S + Vt + O + Postpositive Adjective Phrase (主詞 + 及物動詞 + 受詞 + 形容詞片語後位修飾)",
          "breakdown": [
            {
              "part": "Materials scientists",
              "role": "主詞 (Subject)",
              "note": "材料科學家。"
            },
            {
              "part": "synthesized",
              "role": "及物動詞 (Transitive Verb)",
              "note": "化學合成。"
            },
            {
              "part": "a heat-resistant synthetic polymer",
              "role": "直接受詞 (Direct Object)",
              "note": "heat-resistant (耐熱的) 為複合形容詞。"
            },
            {
              "part": "suitable for insulating aerospace electrical conduits",
              "role": "後位修飾片語 (Adjective Phrase)",
              "note": "suitable for + V-ing (適於...)，insulating (絕緣防護)。"
            }
          ],
          "keyPoints": [
            "【化學構詞網絡】：monomer (單體；mono- 1) ➔ polymer (聚合物；poly- 多)。",
            "【複合形容詞】：Noun + Adjective (如 heat-resistant 耐熱、water-resistant 防水)。"
          ]
        }
      },
      {
        "word": "polyphony",
        "kk": "[pəˈlɪfəni]",
        "ipa": "/pəˈlɪfəni/",
        "pos": "n.",
        "meaning": "複音音樂、多聲部音樂、多元對話性",
        "formula": {
          "parts": [
            {
              "text": "poly-",
              "role": "prefix",
              "meaning": "多 (希臘語 polús)"
            },
            {
              "text": "phon",
              "role": "base",
              "meaning": "聲音 (希臘語 phōnē)"
            },
            {
              "text": "-y",
              "role": "suffix",
              "meaning": "狀態、名詞字尾"
            }
          ],
          "resultMeaning": "多種獨立旋律線條交織重疊的和鳴之聲 ➔「複音音樂、多元對位」"
        },
        "sentence": "Bach's magnificent choral compositions mastered intricate counterpoint, transforming sacred polyphony into celestial acoustic architecture.",
        "sentenceZh": "巴哈宏偉的合唱作品精通錯綜複雜的對位法，將神聖的複音音樂昇華為宛若來自天界的聽覺建築。",
        "grammar": {
          "pattern": "S + Vt + O + Participial Transformation Phrase (主詞 + 及物動詞 + 受詞 + 分詞結果轉化片語)",
          "breakdown": [
            {
              "part": "Bach's magnificent choral compositions",
              "role": "主詞 (Subject)",
              "note": "巴哈宏偉合唱作品。"
            },
            {
              "part": "mastered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "精通掌握。"
            },
            {
              "part": "intricate counterpoint",
              "role": "直接受詞 (Direct Object)",
              "note": "錯綜複雜的對位法。"
            },
            {
              "part": "transforming sacred polyphony into celestial acoustic architecture",
              "role": "現在分詞伴隨結果 (Participle Clause)",
              "note": "transform A into B (將 A 轉變為 B)。"
            }
          ],
          "keyPoints": [
            "【雙重字根融合】：poly- (多) + phone (聲音)，對立於 monophony (單音音樂；mono- 單一)。",
            "【哲學文學隱喻】：文學家常以 polyphony 比喻小說中容納不同階層與多元思想的「眾聲喧嘩」。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Tapestry of the Multitude: The Power of Poly-",
      "titleZh": "眾聲喧嘩的織錦：多元交融的力量",
      "intro": "宇宙絕非由單調均質的孤音組成，而是由無數個體、旋律與視角共同激盪出的豐富交響曲 (poly-)。",
      "paragraphs": [
        {
          "en": "In a rapidly integrating world, monolithic perspectives can no longer navigate global turbulence. A gifted polyglot does far more than translate vocabulary; they bridge divergent cultural histories and foster mutual empathy across oceans.",
          "zh": "在迅速整合的現代世界中，單一孤立的視角已無法應對全球動盪。一位天賦異稟的多語通才所做的遠不止是翻譯單字，他們在各大洋之間架起不同文化歷史的橋樑，滋養彼此的同理共鳴。"
        },
        {
          "en": "From the mathematical harmony of complex polygons to the polyphony of baroque cathedral chorales, embracing multiplicity expands the horizon of human consciousness. When diverse voices harmonize rather than collide, civilization reaches its highest resonance.",
          "zh": "從複雜多邊形展現的數學和諧，到巴洛克大教堂合唱曲的複音交鳴，包容多元性拓寬了人類意識的地平線。當多元的聲音選擇和諧共鳴而非彼此碰撞時，文明便達到了最輝煌的極致。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "According to the passage, what is the deeper value of a polyglot?",
          "qZh": "根據文章，多語人才更深層的價值是什麼？",
          "options": [
            "A. Bridging divergent cultural histories and fostering empathy. (架起不同文化歷史橋樑並滋養同理心)",
            "B. Collecting ancient golden coins.",
            "C. Replacing human musicians with synthesizers.",
            "D. Memorizing dictionary page numbers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出多語人才「bridge divergent cultural histories and foster mutual empathy across oceans」。"
        }
      ]
    }
  },
  {
    "id": "bene",
    "name": "bene-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語副詞「bene」(好、善、優、令人滿意地 well, good)。",
    "originMeaning": "善、良、好、有益",
    "phonetic": "/ˈbɛni/ 或 /ˈbɛnə/",
    "icon": "💖",
    "color": "#059669",
    "summary": "代表善意、慈善救濟、良性醫學診斷及帶來好處的益處福利。",
    "words": [
      {
        "word": "benefit",
        "kk": "[ˈbɛnəfɪt]",
        "ipa": "/ˈbɛnɪfɪt/",
        "pos": "n. / v.",
        "meaning": "(n.) 益處、福利、好處；(v.) 得益於、使受惠",
        "formula": {
          "parts": [
            {
              "text": "bene-",
              "role": "prefix",
              "meaning": "好、善 (拉丁語 bene)"
            },
            {
              "text": "fit",
              "role": "base",
              "meaning": "做、造 (拉丁語 facere 做/製成)"
            }
          ],
          "resultMeaning": "做出好的事情而使人蒙受好處 ➔「益處、受惠」"
        },
        "sentence": "Investing in green municipal parks yields enduring public health benefits for urban residents of all generations.",
        "sentenceZh": "投資建設綠色市立公園，能為各世代的城市居民帶來持久的公共健康福祉。",
        "grammar": {
          "pattern": "Gerund Subject + Vt + O + Prep Phrase (動名詞片語主詞 + 及物動詞 + 受詞 + 受惠群體介系詞片語)",
          "breakdown": [
            {
              "part": "Investing in green municipal parks",
              "role": "動名詞片語主詞 (Gerund Subject)",
              "note": "invest in + 名詞 (投資於...)；動名詞視為單數主詞。"
            },
            {
              "part": "yields",
              "role": "及物動詞 (Transitive Verb)",
              "note": "yields (產生、帶來效益)，加 s 配合單數動名詞主詞。"
            },
            {
              "part": "enduring public health benefits",
              "role": "直接受詞 (Direct Object)",
              "note": "enduring (持久的) 為現在分詞作形容詞修飾 benefits。"
            },
            {
              "part": "for urban residents of all generations",
              "role": "受惠目標介系詞片語 (Prepositional Modifier)",
              "note": "for 表受益對象。"
            }
          ],
          "keyPoints": [
            "【動態動詞搭配】：yield / reap / enjoy benefits (產生/獲得效益)。",
            "【動名詞主謂一致】：Investing... 主詞一律採用第三人稱單數動詞 (yields)。"
          ]
        }
      },
      {
        "word": "benevolent",
        "kk": "[bəˈnɛvələnt]",
        "ipa": "/bəˈnɛvələnt/",
        "pos": "adj.",
        "meaning": "仁慈的、好心的、慈善的",
        "formula": {
          "parts": [
            {
              "text": "bene-",
              "role": "prefix",
              "meaning": "善、好 (拉丁語 bene)"
            },
            {
              "text": "vol",
              "role": "root",
              "meaning": "意願、想 (拉丁語 velle 願意)"
            },
            {
              "text": "-ent",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "滿懷良好心意、希望他人幸福的 ➔「仁慈的、善意的」"
        },
        "sentence": "The benevolent philanthropist anonymously endowed scholarships to support gifted students facing acute financial hardship.",
        "sentenceZh": "這位仁慈的慈善家匿名捐贈獎學金，以資助面臨嚴重經濟困境的有天賦學子。",
        "grammar": {
          "pattern": "S + Adv + Vt + O + Infinitive of Purpose with Participle Modifier (主詞 + 方式副詞 + 及物動詞 + 受詞 + 目的狀詞與分詞後位修飾)",
          "breakdown": [
            {
              "part": "The benevolent philanthropist",
              "role": "主詞 (Subject)",
              "note": "benevolent (仁慈的) 修飾 philanthropist (慈善家)。"
            },
            {
              "part": "anonymously",
              "role": "副詞 (Adverb of Manner)",
              "note": "修飾及物動詞 endowed (匿名地)。"
            },
            {
              "part": "endowed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "捐贈基金/創立。"
            },
            {
              "part": "scholarships",
              "role": "直接受詞 (Direct Object)",
              "note": "獎學金。"
            },
            {
              "part": "to support gifted students facing acute financial hardship",
              "role": "目的狀詞片語 (Infinitive Phrase)",
              "note": "facing (面臨著) 為現在分詞修飾 students；acute (劇烈的、嚴峻的)。"
            }
          ],
          "keyPoints": [
            "【對立詞首對比】：benevolent (仁慈善意的) vs. malevolent (惡毒有害的；mal- 壞)。",
            "【名詞衍生】：benevolence (仁慈、博愛之心)。"
          ]
        }
      },
      {
        "word": "benefactor",
        "kk": "[ˈbɛnəˌfæktɚ]",
        "ipa": "/ˈbɛnɪfæktər/",
        "pos": "n.",
        "meaning": "恩人、贊助者、行善者",
        "formula": {
          "parts": [
            {
              "text": "bene-",
              "role": "prefix",
              "meaning": "善、好 (拉丁語 bene)"
            },
            {
              "text": "fact",
              "role": "root",
              "meaning": "做 (拉丁語 facere)"
            },
            {
              "text": "-or",
              "role": "suffix",
              "meaning": "人 (名詞字尾)"
            }
          ],
          "resultMeaning": "做出善行義舉幫助他人的人 ➔「恩人、贊助者」"
        },
        "sentence": "Without the generous financial backing of an anonymous benefactor, the groundbreaking research lab would have closed permanently.",
        "sentenceZh": "如果沒有一位匿名恩人的慷慨資助，這座開創性的研究實驗室原本早就被迫永久關閉了。",
        "grammar": {
          "pattern": "Prepositional Hypothesis + S + Modal Perfect Passive (介系詞假設虛擬片語 + 主詞 + 與過去相反的假設語氣謂語)",
          "breakdown": [
            {
              "part": "Without the generous financial backing of an anonymous benefactor",
              "role": "與過去相反的假設條件狀詞 (Prepositional Condition)",
              "note": "Without 相當於 If it had not been for... (若非當時有...)。"
            },
            {
              "part": "the groundbreaking research lab",
              "role": "主詞 (Subject)",
              "note": "開創性研究實驗室。"
            },
            {
              "part": "would have closed",
              "role": "假設語氣謂語 (Subjunctive Predicate)",
              "note": "would have + p.p. 表對過去事實相反之推測結果（實際上未關閉）。"
            },
            {
              "part": "permanently",
              "role": "副詞 (Adverb of Manner)",
              "note": "永久地。"
            }
          ],
          "keyPoints": [
            "【與過去相反之假設語氣】：Without + N, S + would have + p.p. (若非當初...原本就已經...)。",
            "【字根對立】：benefactor (行善贊助者) vs. malefactor (作惡犯罪者；male- 壞)。"
          ]
        }
      },
      {
        "word": "benign",
        "kk": "[bɪˈnaɪn]",
        "ipa": "/bɪˈnaɪn/",
        "pos": "adj.",
        "meaning": "良性的（醫學）、和藹仁慈的、溫和無害的",
        "formula": {
          "parts": [
            {
              "text": "bene-",
              "role": "prefix",
              "meaning": "善、良 (拉丁語 bene)"
            },
            {
              "text": "gen",
              "role": "root",
              "meaning": "產生、出身 (拉丁語 genus 出身/種類)"
            }
          ],
          "resultMeaning": "天性溫和沒有侵害威脅的 ➔「良性的、和藹的」"
        },
        "sentence": "To the immense relief of the anxious family, the surgical biopsy confirmed that the tumor was entirely benign.",
        "sentenceZh": "令焦急家屬感到無比寬慰的是，手術切片檢查證實該腫瘤完全屬於良性。",
        "grammar": {
          "pattern": "Emotional Prep Phrase + S + Vt + Noun Clause (情緒情感狀詞 + 主詞 + 及物動詞 + 受詞名詞子句)",
          "breakdown": [
            {
              "part": "To the immense relief of the anxious family",
              "role": "情緒結果狀詞 (Adverbial of Feeling)",
              "note": "To one's + emotional noun (令某人感到...的是)；immense (巨大的)。"
            },
            {
              "part": "the surgical biopsy",
              "role": "主詞 (Subject)",
              "note": "手術組織活檢切片。"
            },
            {
              "part": "confirmed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "證實。"
            },
            {
              "part": "that the tumor was entirely benign",
              "role": "名詞子句受詞 (Noun Clause)",
              "note": "that 引導完整子句；was 為連綴動詞，entirely 為程度副詞修飾形容詞補語 benign。"
            }
          ],
          "keyPoints": [
            "【高階情感介系詞句型】：To one's relief / delight / astonishment (令某人欣慰/高興/驚訝的是...)。",
            "【醫學專用反義對比】：benign tumor (良性腫瘤) vs. malignant tumor (惡性腫瘤)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Architecture of Good Will: The Benevolent Ripple",
      "titleZh": "善意的建築學：良善力量的連鎖漣漪",
      "intro": "一個真誠的善舉 (benefit) 如同投入平靜湖面的石子，能激起跨越世代的無盡漣漪 (bene-)。",
      "paragraphs": [
        {
          "en": "In the history of public health, selfless actions have often altered the fate of continents. When a benevolent benefactor funded the construction of modern sewage treatment in the nineteenth century, waterborne cholera epidemics plummeted, delivering immeasurable benefits to millions.",
          "zh": "在公共衛生史中，無私的善行往往改變了整個大陸的命運。當一位仁慈的恩人在十九世紀資助建設現代化污水處理設施時，水源性霍亂傳染病大幅驟降，為數百萬人帶來了無可估量的福祉。"
        },
        {
          "en": "Benevolence is never mere passive sentiment; it is an active moral force. Whether manifesting as a physician delivering the comforting news of a benign diagnosis or a volunteer mentoring underprivileged youths, the spirit of bene- proves that genuine progress is measured by how deeply we care for one another.",
          "zh": "良善絕非被動的情感，而是一種主動的道德力量。無論是體現為醫生傳達良性診斷的寬慰喜訊，抑或是志工輔導弱勢青少年，bene- 的精神皆證明了真正的進步取決於我們彼此關懷的深度。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What impact did the benefactor's funding of sewage treatment have in the nineteenth century?",
          "qZh": "十九世紀恩人資助污水處理帶來了什麼影響？",
          "options": [
            "A. Waterborne cholera epidemics plummeted, delivering massive public health benefits. (水源性霍亂驟降，帶來巨大健康福祉)",
            "B. All hospitals were closed immediately.",
            "C. Taxes were raised tenfold.",
            "D. Sea levels rose dramatically."
          ],
          "answer": 0,
          "explanation": "文中第一段指出「waterborne cholera epidemics plummeted, delivering immeasurable benefits to millions」。"
        }
      ]
    }
  },
  {
    "id": "trans",
    "name": "trans-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語介系詞「trans」(穿過、跨越、轉移、超越 across, beyond, through)。",
    "originMeaning": "穿過、跨越、轉變、超越",
    "phonetic": "/trænz/ 或 /træns/",
    "icon": "🌉",
    "color": "#2563EB",
    "summary": "表示空間跨越轉移、語言文字轉譯、物質形態徹底蛻變或商業交易流程。",
    "words": [
      {
        "word": "transform",
        "kk": "[trænsˈfɔrm]",
        "ipa": "/trænsˈfɔːrm/",
        "pos": "v.",
        "meaning": "使徹底改變、使轉變形態、蛻變",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "轉移、跨越 (拉丁語 trans-)"
            },
            {
              "text": "form",
              "role": "base",
              "meaning": "形狀、外貌 (拉丁語 forma 模樣)"
            }
          ],
          "resultMeaning": "從一種形態跨越轉變成全新的另一種模樣 ➔「徹底轉變、轉化」"
        },
        "sentence": "Adopting renewable clean energy infrastructure can transform deteriorating industrial rust belts into thriving eco-technology hubs.",
        "sentenceZh": "採用再生純淨能源基礎設施，能將日漸衰頹的工業鏽帶轉型為蓬勃發展的生態科技樞紐。",
        "grammar": {
          "pattern": "Gerund Subject + Modal + Vt + O + into + Result Noun Phrase (動名詞主詞 + 助動詞 + 及物動詞 + 受詞 + into + 結果名詞片語)",
          "breakdown": [
            {
              "part": "Adopting renewable clean energy infrastructure",
              "role": "動名詞片語主詞 (Gerund Subject)",
              "note": "包含多重形容詞修飾 infrastructure。"
            },
            {
              "part": "can transform",
              "role": "謂語 (Modal Predicate)",
              "note": "情態助動詞 can + 動詞 transform。"
            },
            {
              "part": "deteriorating industrial rust belts",
              "role": "直接受詞 (Direct Object)",
              "note": "deteriorating (衰退退化中的) 為現在分詞作形容詞。"
            },
            {
              "part": "into thriving eco-technology hubs",
              "role": "轉化結果介系詞片語 (Prepositional Phrase)",
              "note": "transform A into B (將 A 徹底改造成 B)；thriving (繁榮的)。"
            }
          ],
          "keyPoints": [
            "【關鍵轉化動詞】：transform A into B (使 A 徹底改頭換面成為 B)。",
            "【現在分詞對比】：deteriorating (正在衰敗) vs. thriving (欣欣向榮)。"
          ]
        }
      },
      {
        "word": "translate",
        "kk": "[trænsˈlet]",
        "ipa": "/trænsˈleɪt/",
        "pos": "v.",
        "meaning": "翻譯、轉化、轉譯為行動",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "跨越、轉移 (拉丁語 trans-)"
            },
            {
              "text": "late",
              "role": "root",
              "meaning": "攜帶、傳遞 (拉丁語 latus 承載/搬運)"
            }
          ],
          "resultMeaning": "將一種語言的思想含意搬運跨越到另一種語言 ➔「翻譯、轉化」"
        },
        "sentence": "Effective organizational leaders know how to translate ambitious strategic visions into concrete daily execution milestones.",
        "sentenceZh": "高效的組織領導者深諳如何將宏偉的策略願景轉化為具體的日常執行里程碑。",
        "grammar": {
          "pattern": "S + Vt + Wh-Infinitive Object (主詞 + 及物動詞 + Wh-不定詞複合受詞)",
          "breakdown": [
            {
              "part": "Effective organizational leaders",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "know",
              "role": "及物動詞 (Transitive Verb)",
              "note": "知道、掌握。"
            },
            {
              "part": "how to translate ambitious strategic visions into concrete daily execution milestones",
              "role": "受詞 (Object of know)",
              "note": "how to V 作名詞片語受詞；translate A into B (將 A 轉譯/轉化為 B)。"
            }
          ],
          "keyPoints": [
            "【名詞片語受詞】：know + how to V (知道如何做...)。",
            "【引申意義】：translate 除了語言翻譯，商務寫作中極常用於「將概念轉化為實際成果」(translate into action/results)。"
          ]
        }
      },
      {
        "word": "transparent",
        "kk": "[trænsˈpɛrənt]",
        "ipa": "/trænsˈpærənt/",
        "pos": "adj.",
        "meaning": "透明的、光線可穿透的、清澈公開的、坦誠的",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "穿透 (拉丁語 trans-)"
            },
            {
              "text": "parent",
              "role": "root",
              "meaning": "顯露、看見 (拉丁語 parere 出現/被看見)"
            }
          ],
          "resultMeaning": "光線與視線能夠徹底穿透讓人看清內部 ➔「透明的、公開坦誠的」"
        },
        "sentence": "The newly reformed procurement policy mandates transparent bidding procedures to eliminate bribery and favoritism.",
        "sentenceZh": "這項新改革的採購政策強制要求公開透明的招標程序，以根除賄賂與徇私舞弊。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的狀詞不定詞片語)",
          "breakdown": [
            {
              "part": "The newly reformed procurement policy",
              "role": "主詞 (Subject)",
              "note": "newly (副詞) + reformed (過去分詞) + procurement (採購) + policy。"
            },
            {
              "part": "mandates",
              "role": "及物動詞 (Transitive Verb)",
              "note": "強制要求規定。"
            },
            {
              "part": "transparent bidding procedures",
              "role": "直接受詞 (Direct Object)",
              "note": "transparent (公開透明的) 修飾招標程序。"
            },
            {
              "part": "to eliminate bribery and favoritism",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "eliminate (根除)；bribery (賄賂)；favoritism (偏袒/徇私)。"
            }
          ],
          "keyPoints": [
            "【雙重字意】：物理上指「清澈透光的 (transparent glass)」；社會制度上指「透明公正公開的 (transparent governance)」之反義詞為 opaque (不透明晦暗的)。",
            "【名詞形式】：transparency (透明度)。"
          ]
        }
      },
      {
        "word": "transaction",
        "kk": "[trænˈzækʃən]",
        "ipa": "/trænˈzækʃn/",
        "pos": "n.",
        "meaning": "交易、業務買賣、辦理手續",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "跨越、在兩者之間 (拉丁語 trans-)"
            },
            {
              "text": "action",
              "role": "base",
              "meaning": "行動、運作 (拉丁語 agere 做/驅動)"
            }
          ],
          "resultMeaning": "在買賣雙方彼此之間穿梭進行的商業行動 ➔「交易、買賣業務」"
        },
        "sentence": "Advanced cryptographic blockchain protocols verify each monetary transaction within seconds, preventing double-spending and fraud.",
        "sentenceZh": "先進的密碼學區塊鏈協定能在數秒內驗證每筆貨幣交易，防範雙重支付與詐欺行為。",
        "grammar": {
          "pattern": "S + Vt + O + Time Prep Phrase + Participial Prevention Phrase (主詞 + 及物動詞 + 受詞 + 時間片語 + 現在分詞防範狀詞)",
          "breakdown": [
            {
              "part": "Advanced cryptographic blockchain protocols",
              "role": "主詞 (Subject)",
              "note": "複數主詞名詞片語。"
            },
            {
              "part": "verify",
              "role": "及物動詞 (Transitive Verb)",
              "note": "查核驗證。"
            },
            {
              "part": "each monetary transaction",
              "role": "直接受詞 (Direct Object)",
              "note": "each 後接單數名詞 transaction。"
            },
            {
              "part": "within seconds",
              "role": "時間狀詞 (Time Phrase)",
              "note": "在數秒之內。"
            },
            {
              "part": "preventing double-spending and fraud",
              "role": "現在分詞伴隨結果 (Participle Clause)",
              "note": "表同時達成的防杜效果。"
            }
          ],
          "keyPoints": [
            "【金融科技搭配】：financial transaction (金融交易)、transaction fee (交易手續費)。",
            "【動詞形式】：transact (辦理、進行交易)。"
          ]
        }
      }
    ],
    "article": {
      "title": "Bridging Across Horizons: The Transformative Journey",
      "titleZh": "橫越地平線：轉變與貫通的旅程",
      "intro": "「跨越 (trans-)」是宇宙中最具動態美感的生命狀態：河流穿過山谷，思想轉譯為言語，生命在蛻變中新生。",
      "paragraphs": [
        {
          "en": "Human history has never been static; it is an enduring epic of continuous transformation. When early merchant caravans transported silk across forbidding desert trade routes, they did far more than conduct commercial transactions—they translated foreign philosophies, irrevocably transforming world cultures.",
          "zh": "人類歷史從不是靜止的，而是一部持續蛻變的宏偉史詩。當早期商隊沿著險惡的沙漠貿易路線運載絲綢時，他們所做的遠不止是進行商業交易——他們轉譯著異邦的哲學，深刻且不可逆地重塑了世界文化。"
        },
        {
          "en": "In our hyper-connected contemporary landscape, embracing transparent institutions and cross-cultural dialogue remains our highest calling. By actively tearing down ideological barriers and crossing uncharted oceans, humanity transforms ancient divisions into a luminous tapestry of shared progress.",
          "zh": "在當今高度互聯的時代風貌中，擁抱透明公開的體制與跨文化對話依然是我們最崇高的使命。藉由主動打破意識形態壁壘、跨越未知的海洋，人類將古老的分歧轉變為共同繁榮的璀璨織錦。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What did early merchant caravans achieve beyond mere commercial transactions?",
          "qZh": "早期商隊除了單純的商業交易外，還達成了什麼？",
          "options": [
            "A. They translated foreign philosophies, transforming world cultures. (轉譯外國哲學，深刻轉型世界文化)",
            "B. They destroyed desert ecosystems.",
            "C. They established space satellites.",
            "D. They invented plastic polymers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出商隊「did far more than conduct commercial transactions—they translated foreign philosophies, irrevocably transforming world cultures」。"
        }
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ETYMO_DATA };
}
