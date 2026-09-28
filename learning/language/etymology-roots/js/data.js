// ==========================================
// 字根字首構詞辭典大庫 (EtymoRoots Master Dataset)
// 包含 44 組核心字根字首、完整構詞公式、KK/IPA音標、文法微觀剖析與情境閱讀
// 總收錄單字數：229 個精選核心衍生單字
// ==========================================

const ETYMO_DATA = [
  {
    "id": "tele",
    "name": "tele-",
    "type": "prefix",
    "typeLabel": "希臘語字首 (Greek Prefix)",
    "etymology": "源自古希臘語「τῆλε」(tēle)，核心概念為「遠、遙遠、在遠距離之外 (far, at a distance)」。",
    "originMeaning": "遠距離、遙遠",
    "phonetic": "/ˈtɛli/ 或 /ˈtɛlə/",
    "icon": "📡",
    "color": "#D97706",
    "summary": "用於表示跨越遙遠空間進行的傳遞、觀測、感知或移動。",
    "words": [
      {
        "word": "telephone",
        "kk": "[ˈtɛləˌfon]",
        "ipa": "/ˈtɛləˌfoʊn/",
        "pos": "n. / v.",
        "meaning": "電話；(v.) 打電話給...",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "phone",
              "role": "base",
              "meaning": "聲音、語音 (希臘語 phōnē)"
            }
          ],
          "resultMeaning": "將遠方的聲音即時傳遞過來的裝置 ➔「電話」"
        },
        "sentence": "The young inventor picked up the telephone to confirm whether his patent application had been approved by the federal office.",
        "sentenceZh": "這位年輕發明家拿起電話，確認他的專利申請是否已獲得聯邦辦公室核准。",
        "grammar": {
          "pattern": "S + Vt + O + Adv Clause of Purpose (主詞 + 及物動詞 + 受詞 + 目的狀詞與名詞子句)",
          "breakdown": [
            {
              "part": "The young inventor",
              "role": "主詞 (Subject)",
              "note": "名詞片語，包含定冠詞與修飾形容詞 young。"
            },
            {
              "part": "picked up",
              "role": "及物動詞片語 (Phrasal Verb)",
              "note": "過去簡單式，表示拿起通話筒的連續動作。"
            },
            {
              "part": "the telephone",
              "role": "直接受詞 (Direct Object)",
              "note": "由 tele- + phone 構成的複合名詞。"
            },
            {
              "part": "to confirm",
              "role": "不定詞狀詞 (Infinitive of Purpose)",
              "note": "表動作目的「為了確認...」。"
            },
            {
              "part": "whether his patent application had been approved",
              "role": "受詞名詞子句 (Noun Clause)",
              "note": "whether 引導名詞子句作 confirm 之受詞；子句使用「過去完成被動態 (had been approved)」表示在 picked up 之前已完成之動作。"
            },
            {
              "part": "by the federal office",
              "role": "介系詞片語 (Agent)",
              "note": "被動態之施事者 (Agent)。"
            }
          ],
          "keyPoints": [
            "【時態搭配】：過去式 picked up 與過去完成被動態 had been approved 形成時間先後對比。",
            "【固定句型】：confirm + whether/if... 表示「確認是否...」。",
            "【詞源延伸】：phone 亦見於 symphony (交響樂)、microphone (麥克風)、phonetics (語音學)。"
          ]
        }
      },
      {
        "word": "telescope",
        "kk": "[ˈtɛləˌskop]",
        "ipa": "/ˈtɛləˌskoʊp/",
        "pos": "n.",
        "meaning": "望遠鏡、天文望遠鏡",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "scope",
              "role": "base",
              "meaning": "看、觀察儀器 (希臘語 skopein)"
            }
          ],
          "resultMeaning": "觀測遙遠星體或物體的儀器 ➔「望遠鏡」"
        },
        "sentence": "Through the high-powered telescope, the astronomer observed a distant spiral galaxy that had remained hidden for centuries.",
        "sentenceZh": "透過這架高倍率望遠鏡，天文學家觀測到一個隱匿了數個世紀之久的遙遠螺旋星系。",
        "grammar": {
          "pattern": "Adverbial Phrase + S + Vt + O + Relative Clause (介系詞狀詞 + 主詞 + 及物動詞 + 受詞 + 關係子句)",
          "breakdown": [
            {
              "part": "Through the high-powered telescope",
              "role": "方式狀詞 (Adverbial of Means)",
              "note": "介系詞 through 表示藉由某種儀器媒介，置於句首加強語氣。"
            },
            {
              "part": "the astronomer",
              "role": "主詞 (Subject)",
              "note": "專指天文學家 (astro [星星] + nomer [研究者])。"
            },
            {
              "part": "observed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "及物動詞，過去式，受詞為星系。"
            },
            {
              "part": "a distant spiral galaxy",
              "role": "直接受詞 (Direct Object)",
              "note": "雙重形容詞 distant (遙遠) 與 spiral (螺旋狀) 修飾 galaxy。"
            },
            {
              "part": "that had remained hidden for centuries",
              "role": "限定關係子句 (Defining Relative Clause)",
              "note": "that 為主格關代，先行詞為 a distant spiral galaxy；remained 為連綴動詞，hidden 為分詞補語。"
            }
          ],
          "keyPoints": [
            "【連綴動詞結構】：remain + adjective (hidden)，表示保持某種狀態。",
            "【時間介系詞】：for centuries 表示時間的持續長度（數百年之久）。",
            "【詞源延伸】：scope 同時也是顯微鏡 microscope (micro 微小 + scope 觀察) 的字根。"
          ]
        }
      },
      {
        "word": "television",
        "kk": "[ˈtɛləˌvɪʒən]",
        "ipa": "/ˈtɛləˌvɪʒn/",
        "pos": "n.",
        "meaning": "電視、電視機、電視廣播",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "vision",
              "role": "base",
              "meaning": "視覺、影像 (拉丁語 visio / videre 看)"
            }
          ],
          "resultMeaning": "將遠方的影像即時傳送至螢幕眼前的科技 ➔「電視」"
        },
        "sentence": "The momentous announcement was broadcast live on television, captivating millions of viewers across the continent.",
        "sentenceZh": "這項重大公告在電視上現場直播，吸引了整個大陸數百萬觀眾的目光。",
        "grammar": {
          "pattern": "S + Passive Predicate + Adverbial + Participial Construction (主詞 + 被動謂語 + 狀詞 + 現在分詞構句)",
          "breakdown": [
            {
              "part": "The momentous announcement",
              "role": "主詞 (Subject)",
              "note": "momentous (重大、具歷史意義的) 作形容詞修飾 announcement。"
            },
            {
              "part": "was broadcast",
              "role": "被動動詞 (Passive Predicate)",
              "note": "broadcast 過去式與過去分詞同形 (broadcast-broadcast-broadcast)。"
            },
            {
              "part": "live on television",
              "role": "方式與地點副詞 (Adverbials)",
              "note": "live 作副詞意為「現場實況地」，on television 為傳播媒介介系詞片語。"
            },
            {
              "part": "captivating millions of viewers across the continent",
              "role": "現在分詞構句 (Participle Clause)",
              "note": "表伴隨結果（Result/Attendant Circumstance），相當於 and it captivated..."
            }
          ],
          "keyPoints": [
            "【動詞特殊三態】：broadcast 常用同形 broadcast，避免寫成 broadcasted。",
            "【分詞構句應用】：現在分詞片語簡化了對等子句，使句子節奏緊湊流暢。",
            "【詞源延伸】：vision 衍生自拉丁語 videre (看)，同源字如 visible (可見的)、visit (拜訪)、provide (預見/提供)。"
          ]
        }
      },
      {
        "word": "telegram",
        "kk": "[ˈtɛləˌgræm]",
        "ipa": "/ˈtɛləˌɡræm/",
        "pos": "n.",
        "meaning": "電報",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "gram",
              "role": "base",
              "meaning": "文字、寫作 (希臘語 gramma)"
            }
          ],
          "resultMeaning": "透過遠距電信線路傳遞過來的文字書信 ➔「電報」"
        },
        "sentence": "Before modern digital networks existed, diplomats relied on encrypted telegrams to transmit urgent state secrets.",
        "sentenceZh": "在現代數位網路存在之前，外交官依靠加密電報來傳送緊急的國家機密。",
        "grammar": {
          "pattern": "Time Adverbial Clause + S + Vi + Prep Phrase + Infinitive of Purpose (時間副詞子句 + 主詞 + 不及物動詞 + 介系詞片語 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Before modern digital networks existed",
              "role": "時間副詞子句 (Time Clause)",
              "note": "Before 引導從屬子句，述說歷史背景。"
            },
            {
              "part": "diplomats",
              "role": "主要子句主詞 (Subject)",
              "note": "複數名詞「外交官」。"
            },
            {
              "part": "relied on",
              "role": "不及物動詞片語 (Phrasal Verb)",
              "note": "rely on 為固定搭配，表示「依賴、倚靠」。"
            },
            {
              "part": "encrypted telegrams",
              "role": "受詞 (Object of Preposition)",
              "note": "encrypted (加密的) 為過去分詞轉化形容詞。"
            },
            {
              "part": "to transmit urgent state secrets",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "不定詞片語表 transmit (傳輸) 之目的。"
            }
          ],
          "keyPoints": [
            "【分詞修飾】：encrypted (被加密的) 作前置修飾名詞 telegrams。",
            "【詞根網絡】：-gram (寫下的字/圖)，同根字如 diagram (圖表)、program (程式/節目)、grammar (文法)。"
          ]
        }
      },
      {
        "word": "telepathy",
        "kk": "[təˈlɛpəθi]",
        "ipa": "/təˈlɛpəθi/",
        "pos": "n.",
        "meaning": "心靈感應、遠距知覺",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "pathy",
              "role": "base",
              "meaning": "感受、情感 (希臘語 pathos)"
            }
          ],
          "resultMeaning": "跨越遠距空間直接感受他人的思緒 ➔「心靈感應」"
        },
        "sentence": "Although mainstream scientists remain skeptical about telepathy, identical twins often report an instinctive mental resonance.",
        "sentenceZh": "儘管主流科學家對心靈感應依然持懷疑態度，但同卵雙胞胎常聲稱彼此有一種本能的思維共鳴。",
        "grammar": {
          "pattern": "Concessive Clause + S + Vt + O (讓步副詞子句 + 主詞 + 及物動詞 + 受詞)",
          "breakdown": [
            {
              "part": "Although mainstream scientists remain skeptical about telepathy",
              "role": "讓步副詞子句 (Clause of Concession)",
              "note": "Although 引導子句；remain 為連綴動詞，skeptical 為形容詞主詞補語，固定搭配介系詞 about。"
            },
            {
              "part": "identical twins",
              "role": "主要子句主詞 (Subject)",
              "note": "同卵雙胞胎。"
            },
            {
              "part": "often report",
              "role": "謂語動詞 (Predicate Verb)",
              "note": "頻率副詞 often 置於一般動詞 report 之前。"
            },
            {
              "part": "an instinctive mental resonance",
              "role": "受詞 (Direct Object)",
              "note": "instinctive (本能的) 與 mental (心理的) 共同修飾 resonance (共鳴)。"
            }
          ],
          "keyPoints": [
            "【連綴動詞搭配】：remain + adj. + about...，表示對某事維持某種評價態度。",
            "【詞根網絡】：-pathy (情感/痛苦)，同根字如 sympathy (同情心)、empathy (同理心)、apathy (漠不關心)。"
          ]
        }
      },
      {
        "word": "teleport",
        "kk": "[ˈtɛləˌpɔrt]",
        "ipa": "/ˈtɛləpɔːrt/",
        "pos": "v. / n.",
        "meaning": "(v.) 瞬間移動、心靈傳送；(n.) 傳送",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (希臘語 tēle)"
            },
            {
              "text": "port",
              "role": "base",
              "meaning": "運送、搬移 (拉丁語 portare)"
            }
          ],
          "resultMeaning": "將物質或人體瞬間搬移至遠方 ➔「瞬間移動」"
        },
        "sentence": "In theoretical physics, subatomic particles can teleport across quantum energy barriers without traversing the physical distance.",
        "sentenceZh": "在理論物理學中，亞原子粒子能夠穿過量子能量壁壘進行瞬間移動，而無需實際穿越物理距離。",
        "grammar": {
          "pattern": "Domain Adverbial + S + Modal + Vi + Directional Preposition + Without-Gerund (領域狀詞 + 主詞 + 助動詞 + 不及物動詞 + 介系詞方向片語 + 否定伴隨動名詞)",
          "breakdown": [
            {
              "part": "In theoretical physics",
              "role": "領域狀詞 (Domain Adverbial)",
              "note": "設定陳述成立的科學語境。"
            },
            {
              "part": "subatomic particles",
              "role": "主詞 (Subject)",
              "note": "sub- (次/亞) + atomic (原子的) + particles (粒子)。"
            },
            {
              "part": "can teleport",
              "role": "謂語 (Modal Predicate)",
              "note": "情態助動詞 can + 原形動詞 teleport。"
            },
            {
              "part": "across quantum energy barriers",
              "role": "空間介系詞片語 (Directional Prep Phrase)",
              "note": "across 表示穿過或跨越障礙。"
            },
            {
              "part": "without traversing the physical distance",
              "role": "否定伴隨狀詞 (Adverbial of Condition/Manner)",
              "note": "介系詞 without 後接動名詞 traversing。"
            }
          ],
          "keyPoints": [
            "【否定伴隨結構】：without + V-ing，表達「在未執行某動作的前提下」。",
            "【雙重字根融合】：希臘語 tele- (遠) 與拉丁語 portare (運送) 的現代科學新創詞。"
          ]
        }
      },
      {
        "word": "telemetry",
        "kk": "[təˈlɛmətri]",
        "ipa": "/təˈlɛmɪtri/",
        "pos": "n.",
        "meaning": "遙測技術、遙感勘測",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離"
            },
            {
              "text": "metry",
              "role": "suffix",
              "meaning": "測量、計量 (希臘語 metron)"
            }
          ],
          "resultMeaning": "自遠方自動測量並傳回數據之技術 ➔「遙測」"
        },
        "sentence": "The space agency received real-time telemetry from the Martian rover as it descended through the thin atmosphere.",
        "sentenceZh": "太空總署在火星探測車穿過稀薄大氣層下降時，接收到了來自探測車的即時遙測數據。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Adv Clause of Time",
          "breakdown": [
            {
              "part": "The space agency",
              "role": "主詞 (Subject)",
              "note": "主詞名詞片語。"
            },
            {
              "part": "received",
              "role": "及物動詞 (Transitive Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "real-time telemetry",
              "role": "受詞 (Object)",
              "note": "複合名詞片語。"
            },
            {
              "part": "from the Martian rover",
              "role": "來源介系詞片語",
              "note": "修飾 telemetry 之來源。"
            },
            {
              "part": "as it descended through the thin atmosphere",
              "role": "時間副詞子句",
              "note": "as 引導表「當...之際」。"
            }
          ],
          "keyPoints": [
            "【字尾延伸】：-metry 表示「測量學」，如 geometry (幾何學)、optometry (驗光學)。",
            "【介系詞搭配】：receive something from... 表示「從某處收到某物」。"
          ]
        }
      },
      {
        "word": "teleconference",
        "kk": "[ˈtɛləˌkɑnfərəns]",
        "ipa": "/ˈtɛləˌkɑːnfərəns/",
        "pos": "n. / v.",
        "meaning": "遠距視訊/電話會議；開遠距會議",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離"
            },
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同 (together)"
            },
            {
              "text": "fer",
              "role": "root",
              "meaning": "帶來、聚集 (bear)"
            },
            {
              "text": "-ence",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "將遠距分散的人聚集開會 ➔「遠距視訊會議」"
        },
        "sentence": "Global executives held an urgent teleconference to address the sudden disruption in the maritime supply chain.",
        "sentenceZh": "全球高階主管召開緊急遠距視訊會議，以因應海運供應鏈的突發中斷。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive Phrase of Purpose",
          "breakdown": [
            {
              "part": "Global executives",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "held",
              "role": "及物動詞 (Verb)",
              "note": "hold an urgent conference 慣用動詞。"
            },
            {
              "part": "an urgent teleconference",
              "role": "直接受詞 (Direct Object)",
              "note": "帶有形容詞 urgent 修飾。"
            },
            {
              "part": "to address the sudden disruption in the maritime supply chain",
              "role": "不定詞目的狀語",
              "note": "address 為及物動詞，意為「著手處理、因應」。"
            }
          ],
          "keyPoints": [
            "【字根分析】：conference 源於 con- (一起) + fer (帶來) + -ence，聚集眾人意見之意。",
            "【商務動詞】：address 在此為「處理、應對」之高頻用法，而非演講或地址。"
          ]
        }
      }
    ],
    "article": {
      "title": "Echoes Across the Void: The Tele- Revolution",
      "titleZh": "跨越虛空的迴響：遠距溝通的文明革命",
      "intro": "人類文明的躍進，本質上就是一場克服「空間距離 (tele)」的史詩奮鬥。從古希臘字根 tele- 萌發的那一刻起，語言便預示了人類對連結宇宙深處的渴望。",
      "paragraphs": [
        {
          "en": "Long before modern satellites orbited our planet, ancient scholars could only dream of witnessing phenomena occurring beyond human eyesight. Through the earliest optical telescope, Galileo first unveiled mountains on the Moon, proving that humanity could bridge distant celestial frontiers.",
          "zh": "早在現代人造衛星環繞地球運行之前，古代學者只能夢想目睹超越人類肉眼所能及的遙遠現象。藉由最初的光學望遠鏡，伽利略首次揭開了月球表面的山脈，證明了人類能跨越遙遠的天體疆界。"
        },
        {
          "en": "As industrial commerce expanded across continents, diplomats urgently required instantaneous communication. The invention of the telegram allowed coded electrical pulses to transmit critical decisions within hours instead of weeks, laying the groundwork for the modern information highway.",
          "zh": "隨著工業商業版圖跨越各大洲擴張，外交官迫切需要即時通訊。電報的發明使得編碼電脈衝能在數小時內（而非數週）傳送關鍵決策，為現代資訊高速公路奠定了基石。"
        },
        {
          "en": "Soon, Alexander Graham Bell revolutionized human intimacy with the telephone, enabling people to hear the vocal inflections of their loved ones from thousands of miles away. Decades later, television brought living history into every household, transforming isolated communities into a global village.",
          "zh": "不久之後，亞歷山大·貝爾以電話徹底改變了人與人之間的親密連結，讓人們在數千英里之外也能聽見摯愛之人話語中的抑揚頓挫。數十年後，電視更將活生生的歷史帶進千家萬戶，把孤立的社群轉化為地球村。"
        },
        {
          "en": "Today, visionary physicists explore whether quantum entanglement might allow information to teleport across the universe, while mystics still ponder the mysteries of telepathy. Regardless of where technology leads us, the Greek prefix tele- will always remind us that human curiosity never stops reaching toward the distant unknown.",
          "zh": "今天，富有遠見的物理學家正在探索量子糾纏是否能使資訊在全宇宙進行瞬間傳送，而神秘學家依然沉思著心靈感應的奧秘。無論科技將我們帶往何方，希臘語字首 tele- 將永遠提醒著我們：人類對遙遠未知的探索好奇心永無止境。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What fundamental human challenge does the prefix 'tele-' address in the article?",
          "qZh": "文章中字首 'tele-' 主要解決了人類哪項基本挑戰？",
          "options": [
            "A. Overcoming physical spatial distance (克服實體空間距離)",
            "B. Generating artificial intelligence (製造人工智慧)",
            "C. Healing chronic medical illnesses (治療慢性疾病)",
            "D. Exploring underwater caverns (探索水下洞穴)"
          ],
          "answer": 0,
          "explanation": "文中開宗明義指出人類文明就是一場克服「空間距離 (tele)」的奮鬥。"
        },
        {
          "q": "According to the passage, how did the telegram transform communication compared to earlier eras?",
          "qZh": "根據文章，電報相比於早期時代如何轉變了通訊方式？",
          "options": [
            "A. It transmitted high-definition color images across space.",
            "B. It reduced message transmission time from weeks to mere hours. (將訊息傳送時間從數週縮短至數小時)",
            "C. It replaced all spoken verbal languages.",
            "D. It allowed physical teleportation of heavy cargo."
          ],
          "answer": 1,
          "explanation": "文中述及電報能讓編碼電脈衝在「within hours instead of weeks」傳送關鍵決策。"
        }
      ]
    }
  },
  {
    "id": "prot",
    "name": "prot- / proto-",
    "type": "prefix",
    "typeLabel": "希臘語字首 (Greek Prefix)",
    "etymology": "源自古希臘語「πρῶτος」(prôtos)，原意為「第一、最初、最前、原始、始祖 (first, earliest, original)」。亦延伸至拉丁語系 pro- (向前、防衛)。",
    "originMeaning": "第一、最初、原始、前鋒",
    "phonetic": "/ˈproʊtə/ 或 /ˈproʊtoʊ/",
    "icon": "🥇",
    "color": "#059669",
    "summary": "用於表示生命、科技、文學或法規之演進起點，或最先開創、領銜的第一個原型。",
    "words": [
      {
        "word": "prototype",
        "kk": "[ˈprotəˌtaɪp]",
        "ipa": "/ˈproʊtəˌtaɪp/",
        "pos": "n. / v.",
        "meaning": "原型、雛形、典型樣品；(v.) 製作原型",
        "formula": {
          "parts": [
            {
              "text": "proto-",
              "role": "prefix",
              "meaning": "最初、第一 (希臘語 prôtos)"
            },
            {
              "text": "type",
              "role": "base",
              "meaning": "模型、樣態 (希臘語 typos 烙印/鑄模)"
            }
          ],
          "resultMeaning": "最初鑄造出來的第一個樣品模型 ➔「原型、雛形」"
        },
        "sentence": "The aerospace engineers subjected the working prototype to rigorous wind tunnel testing before launching mass production.",
        "sentenceZh": "航太工程師在展開量產之前，對該運作原型進行了嚴格的風洞測試。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Prepositional Gerund (主詞 + 及物動詞 + 受詞 + 介系詞片語 + 介系詞動名詞時間片語)",
          "breakdown": [
            {
              "part": "The aerospace engineers",
              "role": "主詞 (Subject)",
              "note": "複合名詞詞組作句子的執行主體。"
            },
            {
              "part": "subjected",
              "role": "及物動詞 (Transitive Verb)",
              "note": "固定動詞片語搭配 subject A to B (使 A 經受/遭受 B)。"
            },
            {
              "part": "the working prototype",
              "role": "受詞 A (Object)",
              "note": "working 作現在分詞形容詞，表示「具備實際運作功能的」。"
            },
            {
              "part": "to rigorous wind tunnel testing",
              "role": "受格補語介系詞片語 (Prepositional Phrase)",
              "note": "to 為介系詞，接測試著名詞片語。"
            },
            {
              "part": "before launching mass production",
              "role": "時間狀詞 (Time Adverbial)",
              "note": "before 作介系詞，後接動名詞 launching。"
            }
          ],
          "keyPoints": [
            "【關鍵動詞片語】：subject something to something (使...經歷/遭受檢驗或考驗)。",
            "【分詞轉形容詞】：working prototype (工作原型、功能性雛形)。",
            "【詞根探討】：type 原意為敲擊出的印記，如 archetype (原型典型)、stereotype (刻板印象)。"
          ]
        }
      },
      {
        "word": "protagonist",
        "kk": "[proˈtæɡənɪst]",
        "ipa": "/proʊˈtæɡənɪst/",
        "pos": "n.",
        "meaning": "主角、主人公、領導者、主要宣倡者",
        "formula": {
          "parts": [
            {
              "text": "prot-",
              "role": "prefix",
              "meaning": "第一、首要 (希臘語 prôtos)"
            },
            {
              "text": "agonist",
              "role": "base",
              "meaning": "奮鬥者、演員 (希臘語 agōnistēs 競賽者)"
            }
          ],
          "resultMeaning": "戲劇舞台上第一位上場奮鬥的主要角色 ➔「主角」"
        },
        "sentence": "Throughout the epic novel, the flawed protagonist struggles against moral dilemmas while seeking redemption for his past mistakes.",
        "sentenceZh": "在整部史詩小說中，這位帶有缺陷的主角在道德困境中掙扎，同時為自己過去的過錯尋求救贖。",
        "grammar": {
          "pattern": "Time Adverbial + S + Vi + Prep Phrase + Elliptical Time Clause (時間狀詞 + 主詞 + 不及物動詞 + 介系詞片語 + 精簡時間子句)",
          "breakdown": [
            {
              "part": "Throughout the epic novel",
              "role": "範圍狀詞 (Adverbial of Range)",
              "note": "介系詞 throughout 表貫穿整部作品。"
            },
            {
              "part": "the flawed protagonist",
              "role": "主詞 (Subject)",
              "note": "flawed (有缺點的、不完美的) 修飾主角。"
            },
            {
              "part": "struggles against",
              "role": "動詞與介系詞 (Verb + Preposition)",
              "note": "struggle against 表與困境對抗 (亦可搭配 struggle with)。"
            },
            {
              "part": "moral dilemmas",
              "role": "介系詞受詞 (Object)",
              "note": "dilemma 為進退兩難之困境。"
            },
            {
              "part": "while seeking redemption for his past mistakes",
              "role": "精簡分詞狀詞 (Conjunction + Participle)",
              "note": "保留連接詞 while，省略主詞與 be 動詞 [while he is seeking...]。"
            }
          ],
          "keyPoints": [
            "【角色對稱概念】：protagonist (主角) 對立面為 antagonist (反派主角；anti- 反對 + agonist)。",
            "【狀詞子句精簡】：while + V-ing 為寫作常見的高階句型，使行文更精煉。"
          ]
        }
      },
      {
        "word": "protocol",
        "kk": "[ˈprotəˌkɔl]",
        "ipa": "/ˈproʊtəkɑːl/",
        "pos": "n.",
        "meaning": "協議、規程、禮賓守則、通訊協定",
        "formula": {
          "parts": [
            {
              "text": "proto-",
              "role": "prefix",
              "meaning": "最初、卷首 (希臘語 prôtos)"
            },
            {
              "text": "col",
              "role": "base",
              "meaning": "膠水、黏附紙張 (希臘語 kolla 膠水)"
            }
          ],
          "resultMeaning": "黏在古代手稿第一頁記載內容總結與守則的卷首文檔 ➔「協議、規範」"
        },
        "sentence": "Medical researchers must adhere strictly to international safety protocols when conducting genetic experiments.",
        "sentenceZh": "醫學研究人員在進行基因實驗時，必須嚴格遵守國際安全規範。",
        "grammar": {
          "pattern": "S + Modal + Vi + Adv + Prep Phrase + Reduced Time Clause (主詞 + 助動詞 + 不及物動詞 + 副詞 + 介系詞片語 + 時間分詞精簡子句)",
          "breakdown": [
            {
              "part": "Medical researchers",
              "role": "主詞 (Subject)",
              "note": "醫學研究人員。"
            },
            {
              "part": "must adhere",
              "role": "情態謂語動詞 (Modal Verb + Base Verb)",
              "note": "must 強調義務責任，adhere 為不及物動詞。"
            },
            {
              "part": "strictly",
              "role": "修飾副詞 (Adverb of Manner)",
              "note": "置於動詞與介系詞之間，加強執行標準。"
            },
            {
              "part": "to international safety protocols",
              "role": "介系詞受詞 (Prepositional Object)",
              "note": "adhere to 為不可分割的固定片語「恪守、遵循」。"
            },
            {
              "part": "when conducting genetic experiments",
              "role": "時間分詞狀詞 (Adverbial Participle)",
              "note": "when + V-ing，表「當進行...之時」。"
            }
          ],
          "keyPoints": [
            "【固定搭配詞組】：adhere to protocol (恪遵規程)、breach of protocol (違反協議)。",
            "【多領域含意】：在外交指「外交禮儀」；在網路工程指「通訊協定 (如 HTTP/IP)」；在醫學指「臨床試驗規範」。"
          ]
        }
      },
      {
        "word": "protect",
        "kk": "[prəˈtɛkt]",
        "ipa": "/prəˈtɛkt/",
        "pos": "v.",
        "meaning": "保護、防衛、庇護",
        "formula": {
          "parts": [
            {
              "text": "pro- / prot-",
              "role": "prefix",
              "meaning": "在前面、向前 (拉丁/希臘語 pro)"
            },
            {
              "text": "tect",
              "role": "base",
              "meaning": "覆蓋、蓋屋頂 (拉丁語 tegere 遮蓋)"
            }
          ],
          "resultMeaning": "在正前方撐起遮陽避雨的防護掩體 ➔「保護、防衛」"
        },
        "sentence": "Deploying comprehensive firewalls protects sensitive database records against unauthorized digital intrusions.",
        "sentenceZh": "部署全面的防火牆能保護敏感的資料庫紀錄免遭未經授權的數位入侵。",
        "grammar": {
          "pattern": "Gerund Subject + Vt + O + Prep Phrase against Danger (動名詞主詞 + 及物動詞 + 受詞 + 防護對象介系詞片語)",
          "breakdown": [
            {
              "part": "Deploying comprehensive firewalls",
              "role": "動名詞片語主詞 (Gerund Subject)",
              "note": "動名詞片語作主詞，文法上一律視為「第三人稱單數」。"
            },
            {
              "part": "protects",
              "role": "及物動詞 (Transitive Verb)",
              "note": "配合單數動名詞主詞，動詞加 s。"
            },
            {
              "part": "sensitive database records",
              "role": "受詞 (Direct Object)",
              "note": "受保護的實體對象。"
            },
            {
              "part": "against unauthorized digital intrusions",
              "role": "防護目標介系詞片語 (Prepositional Phrase)",
              "note": "protect A against/from B 為標準搭配，against 表抵禦外力危害。"
            }
          ],
          "keyPoints": [
            "【動名詞主詞主謂一致性】：Gerund subject takes a singular verb (Deploying... protects)。",
            "【介系詞搭配】：protect [受詞] against [威脅] 或 protect [受詞] from [傷害]。",
            "【詞根網絡】：tect (覆蓋)，同源字有 detect (de 去除 + tect 覆蓋 = 揭發/偵測)、architect (archi 總裁 + tect 建造覆蓋者 = 建築師)。"
          ]
        }
      },
      {
        "word": "protozoan",
        "kk": "[ˌprotəˈzoən]",
        "ipa": "/ˌproʊtəˈzoʊən/",
        "pos": "n.",
        "meaning": "原生動物（單細胞真核微生物）",
        "formula": {
          "parts": [
            {
              "text": "proto-",
              "role": "prefix",
              "meaning": "最原始的 (希臘語 prôtos)"
            },
            {
              "text": "zoan",
              "role": "base",
              "meaning": "動物 (希臘語 zōion)"
            }
          ],
          "resultMeaning": "地球生命演化史上最初始出現的微小動物個體 ➔「原生動物」"
        },
        "sentence": "Under the optical microscope, the biology students observed microscopic protozoans propelling themselves with microscopic flagella.",
        "sentenceZh": "在光學顯微鏡下，生物學系學生觀察到微小的原生動物正借助纖細的鞭毛推進身體。",
        "grammar": {
          "pattern": "Prep Phrase + S + Vt + O + Objective Complement (介系詞狀詞 + 主詞 + 感官/及物動詞 + 受詞 + 現在分詞受詞補語)",
          "breakdown": [
            {
              "part": "Under the optical microscope",
              "role": "地點狀詞 (Adverbial of Place)",
              "note": "指出觀察儀器環境。"
            },
            {
              "part": "the biology students",
              "role": "主詞 (Subject)",
              "note": "執行觀察的群體。"
            },
            {
              "part": "observed",
              "role": "感官/及物動詞 (Sensory Verb)",
              "note": "過去式動詞。"
            },
            {
              "part": "microscopic protozoans",
              "role": "直接受詞 (Direct Object)",
              "note": "被觀察的對象。"
            },
            {
              "part": "propelling themselves with microscopic flagella",
              "role": "受詞補語 (Objective Complement)",
              "note": "現在分詞片語作受詞補語，強調動作正在活躍進行中 (observe + O + V-ing)。"
            }
          ],
          "keyPoints": [
            "【感官動詞句型】：observe / watch / see + O + V-ing，強調主動正在發生的動作畫面感。",
            "【生物構詞學】：proto- (最原始) + zoo/zoa (動物，如 zoology 動物學)。"
          ]
        }
      },
      {
        "word": "proton",
        "kk": "[ˈproˌtɑn]",
        "ipa": "/ˈproʊtɑːn/",
        "pos": "n.",
        "meaning": "質子 (原子核中帶正電荷的基本粒子)",
        "formula": {
          "parts": [
            {
              "text": "prot-",
              "role": "root",
              "meaning": "最初、第一 (希臘語 prōtos)"
            },
            {
              "text": "-on",
              "role": "suffix",
              "meaning": "物理粒子字尾 (subatomic particle)"
            }
          ],
          "resultMeaning": "物質中最基本、最原初的核粒子 ➔「質子」"
        },
        "sentence": "A hydrogen atom typically consists of a single proton and one orbiting electron.",
        "sentenceZh": "一個氫原子通常由單一個質子與一顆軌道電子所構成。",
        "grammar": {
          "pattern": "S + Adv + Vi + Prep Phrase (consists of)",
          "breakdown": [
            {
              "part": "A hydrogen atom",
              "role": "主詞 (Subject)",
              "note": "單數名詞片語。"
            },
            {
              "part": "typically",
              "role": "頻率副詞",
              "note": "修飾動詞 consists。"
            },
            {
              "part": "consists of",
              "role": "不及物動詞片語",
              "note": "意為「由...組成」，不可用於被動態。"
            },
            {
              "part": "a single proton and one orbiting electron",
              "role": "介系詞受詞",
              "note": "由 and 連接兩項並列成分；orbiting 為現在分詞作形容詞。"
            }
          ],
          "keyPoints": [
            "【文法盲點】：consist of (由...構成) 不可寫作 is consisted of，常見同義句型為 be composed of 或 comprise。",
            "【粒子字尾】：-on 常見於物理學粒子，如 electron (電子)、neutron (中子)、photon (光子)。"
          ]
        }
      },
      {
        "word": "protoplasm",
        "kk": "[ˈprotəˌplæzəm]",
        "ipa": "/ˈproʊtəˌplæzəm/",
        "pos": "n.",
        "meaning": "原生質、原形質 (細胞活質)",
        "formula": {
          "parts": [
            {
              "text": "proto-",
              "role": "prefix",
              "meaning": "原始、第一 (first)"
            },
            {
              "text": "plasm",
              "role": "base",
              "meaning": "成形物、塑造質 (希臘語 plasma)"
            }
          ],
          "resultMeaning": "生物生命活動最初成形之基本物質 ➔「原生質」"
        },
        "sentence": "Under the microscope, scientists observed the streaming movement of protoplasm within the living plant cell.",
        "sentenceZh": "在顯微鏡下，科學家觀察到活體植物細胞內原生質的流動現象。",
        "grammar": {
          "pattern": "Prep Phrase + S + Vt + O + Prep Phrase",
          "breakdown": [
            {
              "part": "Under the microscope",
              "role": "地點介系詞片語",
              "note": "置於句首作情境狀語。"
            },
            {
              "part": "scientists",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "observed",
              "role": "及物動詞 (Verb)",
              "note": "表示觀察行為。"
            },
            {
              "part": "the streaming movement of protoplasm",
              "role": "直接受詞",
              "note": "streaming 為現在分詞修飾 movement。"
            },
            {
              "part": "within the living plant cell",
              "role": "地點介系詞片語",
              "note": "修飾 movement 發生的位置。"
            }
          ],
          "keyPoints": [
            "【字根家族】：plasma (血漿、電漿)、plastic (可塑的、塑膠) 皆源自希臘語 plassein (塑造、成形)。",
            "【文法修飾】：streaming 與 living 皆為現在分詞作前置修飾語，表正在進行的生動狀態。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Genesis of Innovation: From Prototype to Pioneer",
      "titleZh": "創新的原點：從雛形打造到科技先驅",
      "intro": "任何偉大的發明與故事，最初都是從一塊不起眼的「原始模型 (prototype)」或微不足道的「原始起點 (proto-)」開始萌芽。",
      "paragraphs": [
        {
          "en": "Every transformative technological revolution begins with a fragile prototype. In a modest laboratory surrounded by circuit boards, our brilliant protagonist spent years fine-tuning a revolutionary solar energy converter, determined to solve the energy crisis.",
          "zh": "每場具變革性的科技革命，皆始於一件脆弱的原型。在被電路板環繞的簡樸實驗室裡，我們才華洋溢的主角耗費了數年微調一套革命性的太陽能轉換器，下定決心要解決能源危機。"
        },
        {
          "en": "Before conducting live trials, the research team established an uncompromising safety protocol to protect their high-voltage capacitors against unexpected electrical surges. Without rigorous discipline, months of delicate engineering could vanish in a single spark.",
          "zh": "在進行現場實測之前，研究團隊確立了毫不妥協的安全規程，以保護其高壓電容器免於遭受意外的電壓突波。如果沒有嚴謹的紀律，數個月精雕細琢的工程成果可能會在單一火花中化為烏有。"
        },
        {
          "en": "Interestingly, the inventor drew inspiration from nature's earliest evolutionary architects: simple single-celled protozoans that had survived in hostile geothermal vents for billions of years by utilizing thermal gradients.",
          "zh": "有趣的是，這位發明家從大自然最初始的演化建築師中汲取靈感：那些利用熱梯度、在惡劣地熱噴口中繁衍生存了數十億年的微小單細胞原生動物。"
        },
        {
          "en": "By mimicking these primitive biological mechanisms, the team successfully engineered a machine capable of producing clean energy with zero emissions. Thus, what once existed merely as a rough sketch became a global milestone, demonstrating how honoring the original spirit of 'proto-' can reshape human destiny.",
          "zh": "藉由模仿這些原始的生物機制，團隊成功打造出一台能以零排放產生純淨能源的機器。就這樣，曾經只是一張粗糙草圖的事物變成了全球的里程碑，展現出崇尚「proto- (原始開創)」精神如何重塑人類的命運。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What role did protozoans play in the protagonist's technological breakthrough?",
          "qZh": "原生動物在主角的科技突破中扮演了什麼角色？",
          "options": [
            "A. They provided biological inspiration for thermal energy utilization. (為熱能利用提供了仿生靈感)",
            "B. They contaminated the solar panels and delayed the project.",
            "C. They were cloned to create living batteries.",
            "D. They functioned as tiny computers."
          ],
          "answer": 0,
          "explanation": "文中第三段指出發明家從「simple single-celled protozoans」利用熱梯度的生存機制中汲取了靈感。"
        },
        {
          "q": "Why was establishing a strict protocol essential before running live trials?",
          "qZh": "為什麼在進行實測前建立嚴格的規程至關重要？",
          "options": [
            "A. To apply for government patents in advance.",
            "B. To protect fragile equipment against electrical surges. (保護設備免於電壓突波損壞)",
            "C. To hire more actors for the documentary.",
            "D. To advertise the product to the public."
          ],
          "answer": 1,
          "explanation": "文中第二段指出團隊制定規程是為了「to protect their high-voltage capacitors against unexpected electrical surges」。"
        }
      ]
    }
  },
  {
    "id": "spect",
    "name": "spect / spic",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「specere」(視、看、注視、觀察)，延伸形為 spectare 與 spicere。",
    "originMeaning": "看、視察、觀察、景象",
    "phonetic": "/spɛkt/",
    "icon": "🔍",
    "color": "#2563EB",
    "summary": "與眼睛視線、內心省察、外在景觀及檢驗審視密切相關的超高頻核心字根。",
    "words": [
      {
        "word": "inspect",
        "kk": "[ɪnˈspɛkt]",
        "ipa": "/ɪnˈspɛkt/",
        "pos": "v.",
        "meaning": "檢查、視察、檢驗",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "進入內部 (拉丁語 in)"
            },
            {
              "text": "spect",
              "role": "root",
              "meaning": "看 (拉丁語 specere)"
            }
          ],
          "resultMeaning": "深入到事物內部仔細查看 ➔「檢查、視察」"
        },
        "sentence": "Senior aviation safety regulators inspect every turbine blade thoroughly before granting commercial flight authorization.",
        "sentenceZh": "資深航空安全監管人員在頒發商業飛行許可之前，會徹底檢查每一個渦輪葉片。",
        "grammar": {
          "pattern": "S + Vt + O + Adv + Prepositional Gerund Clause (主詞 + 及物動詞 + 受詞 + 程度副詞 + 介系詞動名詞子句)",
          "breakdown": [
            {
              "part": "Senior aviation safety regulators",
              "role": "主詞 (Subject)",
              "note": "名詞片語，包含多重修飾名詞與形容詞。"
            },
            {
              "part": "inspect",
              "role": "及物動詞 (Transitive Verb)",
              "note": "現在簡單式，表達例行性制度與規定。"
            },
            {
              "part": "every turbine blade",
              "role": "受詞 (Direct Object)",
              "note": "every 後接單數可數名詞 blade。"
            },
            {
              "part": "thoroughly",
              "role": "方式副詞 (Adverb of Manner)",
              "note": "修飾 inspect，表示「徹底、周延地」。"
            },
            {
              "part": "before granting commercial flight authorization",
              "role": "時間狀詞 (Time Adverbial)",
              "note": "before 作介系詞，後接動名詞 granting 與雙受詞語境。"
            }
          ],
          "keyPoints": [
            "【主客語搭配】：inspect the premises (檢查廠區)、inspect for defects (檢查缺陷)。",
            "【衍生字族】：inspector (檢查員)、inspection (檢驗工作)。"
          ]
        }
      },
      {
        "word": "respect",
        "kk": "[rɪˈspɛkt]",
        "ipa": "/rɪˈspɛkt/",
        "pos": "v. / n.",
        "meaning": "尊敬、尊重、敬佩；(n.) 尊重、方面",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再、回頭 (拉丁語 re-)"
            },
            {
              "text": "spect",
              "role": "root",
              "meaning": "看 (拉丁語 specere)"
            }
          ],
          "resultMeaning": "回過頭來再三注視並敬仰 ➔「尊敬、尊重」"
        },
        "sentence": "True collaborative leadership requires that senior executives respect diverse opinions voiced by frontline employees.",
        "sentenceZh": "真正的協同領導力要求高階主管尊重前線基層員工所表達的不同觀點。",
        "grammar": {
          "pattern": "S + Vt + Subjunctive That-Clause (主詞 + 及物動詞 + 意志要求假設語氣名詞子句)",
          "breakdown": [
            {
              "part": "True collaborative leadership",
              "role": "主詞 (Subject)",
              "note": "抽象名詞片語。"
            },
            {
              "part": "requires",
              "role": "及物動詞 (Transitive Verb of Demand)",
              "note": "表要求/命令動詞，後接 that 子句需用虛擬語氣 (should + 原形動詞，should 常省略)。"
            },
            {
              "part": "that senior executives (should) respect",
              "role": "名詞子句與動詞原形 (Subjunctive Mood)",
              "note": "子句謂語動詞使用原形 respect。"
            },
            {
              "part": "diverse opinions",
              "role": "子句受詞 (Object)",
              "note": "多元意見。"
            },
            {
              "part": "voiced by frontline employees",
              "role": "過去分詞後位修飾 (Past Participial Modifier)",
              "note": "修飾 opinions，相當於 which are voiced by..."
            }
          ],
          "keyPoints": [
            "【特殊假設語氣 (Subjunctive Mood)】：require / demand / suggest + that + S + (should) + V-base。",
            "【過去分詞後置修飾】：opinions voiced by... 展現道地寫作修辭。"
          ]
        }
      },
      {
        "word": "retrospect",
        "kk": "[ˈrɛtrəˌspɛkt]",
        "ipa": "/ˈrɛtrəspɛkt/",
        "pos": "n.",
        "meaning": "回顧、回想、追溯",
        "formula": {
          "parts": [
            {
              "text": "retro-",
              "role": "prefix",
              "meaning": "向後、往回 (拉丁語 retro)"
            },
            {
              "text": "spect",
              "role": "root",
              "meaning": "看 (拉丁語 specere)"
            }
          ],
          "resultMeaning": "回頭看過往走過的路與經歷 ➔「回顧、回憶」"
        },
        "sentence": "In retrospect, the financial crisis of that decade served as a painful catalyst for reforming global banking standards.",
        "sentenceZh": "回想起來，那個十年的金融危機成為改革全球銀行標準的痛苦催化劑。",
        "grammar": {
          "pattern": "Adverbial Idiom + S + Vi + Prep Phrase (成語狀詞 + 主詞 + 不及物動詞 + 介系詞受詞補語)",
          "breakdown": [
            {
              "part": "In retrospect",
              "role": "慣用片語狀詞 (Idiomatic Adverbial)",
              "note": "固定片語「回首過去、事後反思」，常置於句首。"
            },
            {
              "part": "the financial crisis of that decade",
              "role": "主詞 (Subject)",
              "note": "介系詞片語 of that decade 修飾 crisis。"
            },
            {
              "part": "served as",
              "role": "動詞片語 (Phrasal Verb)",
              "note": "serve as 表示「充當、擔任、發揮...作用」。"
            },
            {
              "part": "a painful catalyst",
              "role": "介系詞受詞 (Object of Prep)",
              "note": "catalyst (催化劑) 作隱喻。"
            },
            {
              "part": "for reforming global banking standards",
              "role": "目的介系詞片語 (Prepositional Modifier)",
              "note": "for 後接動名詞 reforming。"
            }
          ],
          "keyPoints": [
            "【高分寫作必備片語】：In retrospect,...（回顧過去...）。",
            "【同根形容詞】：retrospective (回顧的、懷舊的；n. 回顧展)。"
          ]
        }
      },
      {
        "word": "spectacle",
        "kk": "[ˈspɛktək!]",
        "ipa": "/ˈspɛktəkl/",
        "pos": "n.",
        "meaning": "奇觀、壯觀景象；(複數 spectacles) 眼鏡",
        "formula": {
          "parts": [
            {
              "text": "spect",
              "role": "root",
              "meaning": "看 (拉丁語 specere)"
            },
            {
              "text": "-acle",
              "role": "suffix",
              "meaning": "器具、場景、事物 (名詞字尾)"
            }
          ],
          "resultMeaning": "吸引大眾駐足觀看的事物與盛大場面 ➔「奇觀、壯觀場面」"
        },
        "sentence": "The vibrant annual lantern festival created an unforgettable visual spectacle that attracted travelers from across the world.",
        "sentenceZh": "一年一度生氣盎然的花燈節營造了一場令人難忘的視覺盛宴，吸引了來自世界各地的旅人。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 關係子句)",
          "breakdown": [
            {
              "part": "The vibrant annual lantern festival",
              "role": "主詞 (Subject)",
              "note": "triple modifiers (vibrant, annual, lantern) 修飾 festival。"
            },
            {
              "part": "created",
              "role": "及物動詞 (Transitive Verb)",
              "note": "過去式。"
            },
            {
              "part": "an unforgettable visual spectacle",
              "role": "直接受詞 (Direct Object)",
              "note": "unforgettable (不可磨滅的) + visual (視覺的) + spectacle (奇觀)。"
            },
            {
              "part": "that attracted travelers from across the world",
              "role": "限定關係子句 (Defining Relative Clause)",
              "note": "that 引導子句修飾 spectacle，attracted 為子句動詞。"
            }
          ],
          "keyPoints": [
            "【字義分化】：單數通常指「盛大奇觀、景象」；複數 spectacles 在傳統英式英語中意為「眼鏡」(= glasses)。",
            "【形容詞衍生】：spectacular (壯麗的、宏偉的)。"
          ]
        }
      },
      {
        "word": "prospect",
        "kk": "[ˈprɑspɛkt]",
        "ipa": "/ˈprɑːspɛkt/",
        "pos": "n. / v.",
        "meaning": "(n.) 前景、前途、展望、潛在客戶；(v.) 探勘",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前 (拉丁語 pro)"
            },
            {
              "text": "spect",
              "role": "root",
              "meaning": "看 (拉丁語 specere)"
            }
          ],
          "resultMeaning": "向前眺望未來遠景 ➔「前景、展望」"
        },
        "sentence": "Economic analysts remain optimistic about the company's long-term commercial prospects despite short-term inflation headwinds.",
        "sentenceZh": "儘管面臨短期通膨阻力，經濟分析師對該公司的長期商業前景依然抱持樂觀態度。",
        "grammar": {
          "pattern": "S + Linking Verb + Predicate Adjective + Prep Phrase + Concessive Prep Phrase (主詞 + 連綴動詞 + 形容詞補語 + 介系詞片語 + 讓步介系詞片語)",
          "breakdown": [
            {
              "part": "Economic analysts",
              "role": "主詞 (Subject)",
              "note": "經濟分析師。"
            },
            {
              "part": "remain",
              "role": "連綴動詞 (Linking Verb)",
              "note": "保持某狀態。"
            },
            {
              "part": "optimistic",
              "role": "主詞補語 (Subject Complement)",
              "note": "形容詞，固定搭配介系詞 about。"
            },
            {
              "part": "about the company's long-term commercial prospects",
              "role": "介系詞對象片語 (Prepositional Phrase)",
              "note": "prospects 常用複數表示事業與市場前景。"
            },
            {
              "part": "despite short-term inflation headwinds",
              "role": "讓步介系詞片語 (Concessive Prepositional Phrase)",
              "note": "despite 為介系詞，後接名詞片語 headwinds (逆風/阻力)。"
            }
          ],
          "keyPoints": [
            "【介系詞對比】：despite 為介系詞 (接名詞)，although 為從屬連接詞 (接完整子句)。",
            "【衍生形容詞】：prospective (預期的、未來的，如 prospective students 準新生)。"
          ]
        }
      },
      {
        "word": "spectator",
        "kk": "[ˈspɛkˌtetɚ]",
        "ipa": "/ˈspɛkteɪtər/",
        "pos": "n.",
        "meaning": "現場觀眾、旁觀者",
        "formula": {
          "parts": [
            {
              "text": "spect",
              "role": "root",
              "meaning": "觀看 (look)"
            },
            {
              "text": "-ator",
              "role": "suffix",
              "meaning": "從事...的人 (person who)"
            }
          ],
          "resultMeaning": "在現場專注觀看比賽或表演的人 ➔「現場觀眾」"
        },
        "sentence": "Tens of thousands of spectators cheered enthusiastically when the home team scored the decisive goal in injury time.",
        "sentenceZh": "當主隊在傷停補時攻入決定性的一球時，數以萬計的現場觀眾爆發出熱烈歡呼。",
        "grammar": {
          "pattern": "S + Vi + Adv + Adv Clause of Time (when...)",
          "breakdown": [
            {
              "part": "Tens of thousands of spectators",
              "role": "主詞 (Subject)",
              "note": "表龐大數量「數以萬計的觀眾」。"
            },
            {
              "part": "cheered",
              "role": "不及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "enthusiastically",
              "role": "副詞 (Adverb)",
              "note": "修飾動詞 cheered。"
            },
            {
              "part": "when the home team scored the decisive goal in injury time",
              "role": "時間副詞子句",
              "note": "when 引導子句，scored 為及物動詞，the decisive goal 為受詞。"
            }
          ],
          "keyPoints": [
            "【觀眾詞彙辨析】：spectator 指「體育賽事現場觀眾」；audience 指「音樂會/演講/戲劇觀眾」；viewer 指「電視/線上影片觀眾」。",
            "【時間搭配】：injury time 為足球術語「傷停補時」。"
          ]
        }
      },
      {
        "word": "conspicuous",
        "kk": "[kənˈspɪkjʊəs]",
        "ipa": "/kənˈspɪkjuəs/",
        "pos": "adj.",
        "meaning": "顯眼的、引人注目的、顯著的",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "完全、強調 (thoroughly)"
            },
            {
              "text": "spic (spect)",
              "role": "root",
              "meaning": "看見 (look, see)"
            },
            {
              "text": "-uous",
              "role": "suffix",
              "meaning": "充滿...特質的形容詞字尾"
            }
          ],
          "resultMeaning": "完全能被每個人清楚看見的 ➔「顯眼的、引人注目的」"
        },
        "sentence": "Her brightly colored jacket made her conspicuous among the crowd of commuters dressed entirely in dark coats.",
        "sentenceZh": "在一群全穿著深色大衣的通勤人群中，她亮麗的外套使她顯得格外引人注目。",
        "grammar": {
          "pattern": "S + Vt + O + OC (形容詞受詞補語) + Prep Phrase",
          "breakdown": [
            {
              "part": "Her brightly colored jacket",
              "role": "主詞 (Subject)",
              "note": "複合形容詞 brightly colored 修飾 jacket。"
            },
            {
              "part": "made",
              "role": "使役動詞 (Causative Verb)",
              "note": "make + O + Adj (使受詞呈現某種狀態)。"
            },
            {
              "part": "her",
              "role": "直接受詞 (Object)",
              "note": "人稱代名詞受格。"
            },
            {
              "part": "conspicuous",
              "role": "受詞補語 (Objective Complement)",
              "note": "形容詞補語補充說明受詞 her 之狀態。"
            },
            {
              "part": "among the crowd of commuters dressed entirely in dark coats",
              "role": "介系詞片語",
              "note": "dressed entirely in dark coats 為過去分詞片語修飾 commuters。"
            }
          ],
          "keyPoints": [
            "【五大句型】：S + make + O + Adj.，使受詞處於某種狀態，conspicuous 作受詞補語。",
            "【詞源變體】：spect 與 spic 同源互換，如 despise (蔑視)、auspicious (吉兆的)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Architecture of Observation: Living Through the Lens of 'Spect'",
      "titleZh": "觀察的建築學：以觀照字根重省人生",
      "intro": "「看 (spect)」不僅僅是視網膜接收光影，更是一種深入內部 (inspect)、反省過往 (retrospect) 與眺望未來 (prospect) 的心靈智慧。",
      "paragraphs": [
        {
          "en": "Every morning, city engineers inspect railway tracks and suspension bridges across the metropolitan harbor. Their relentless scrutiny ensures that millions of commuters can cross deep waters safely every day without pondering the fragile spectacle beneath their feet.",
          "zh": "每天清晨，城市工程師都會視察大都會海港沿線的鐵軌與懸索吊橋。他們堅持不懈的嚴格檢驗，確保了數百萬通勤族每天能平安橫渡深水，而無需擔憂腳下那令人屏息的壯觀景象。"
        },
        {
          "en": "In retrospect, human civilization has always flourished when architects and philosophers treated nature with profound respect. Whenever builders neglected the environmental balance in pursuit of rapid profits, catastrophic floods inevitably reminded them of their shortsightedness.",
          "zh": "回想起來，當建築師與哲學家對大自然抱持著深厚敬意時，人類文明總是繁榮昌盛。每當建造者為了追求速成利益而忽視環境平衡時，災難性的洪患總會無情地提醒他們當初的短視近利。"
        },
        {
          "en": "As we stand on the threshold of a new millennium, investors eagerly assess the bright prospect of renewable energy. By learning from historical failures and looking ahead with humility, we can transform today's ecological challenges into tomorrow's enduring triumph.",
          "zh": "當我們站在新千禧年的門檻上，投資人熱切評估著再生能源的璀璨前景。藉由從歷史挫敗中學習並以謙卑之心遠眺前方，我們能將今日的生態挑戰化為明日持久的勝利。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "According to the article, why are the engineers' inspections vital?",
          "qZh": "根據文章，為何工程師的視察至關重要？",
          "options": [
            "A. They guarantee safe transit for millions of commuters. (確保數百萬通勤族平安通行)",
            "B. They allow companies to sell tickets at higher prices.",
            "C. They discover sunken pirate treasures.",
            "D. They design artificial intelligence robots."
          ],
          "answer": 0,
          "explanation": "文中第一段指出工程師的嚴謹檢驗「ensures that millions of commuters can cross deep waters safely」。"
        }
      ]
    }
  },
  {
    "id": "dict",
    "name": "dict / dic",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「dicere / dictare」(說、宣布、斷言、宣告)。",
    "originMeaning": "說、言說、宣布、口述",
    "phonetic": "/dɪkt/",
    "icon": "🗣️",
    "color": "#7C3AED",
    "summary": "構成法律宣告、預言語意、權威口述以及字詞表達等核心單字。",
    "words": [
      {
        "word": "predict",
        "kk": "[prɪˈdɪkt]",
        "ipa": "/prɪˈdɪkt/",
        "pos": "v.",
        "meaning": "預測、預言",
        "formula": {
          "parts": [
            {
              "text": "pre-",
              "role": "prefix",
              "meaning": "在之前、預先 (拉丁語 prae)"
            },
            {
              "text": "dict",
              "role": "root",
              "meaning": "說 (拉丁語 dicere)"
            }
          ],
          "resultMeaning": "在事情發生前就先說出來 ➔「預測、預言」"
        },
        "sentence": "Advanced computational models can accurately predict seasonal typhoon trajectories using real-time atmospheric telemetry.",
        "sentenceZh": "先進的計算模型能運用即時大氣遙測資料，精確預測季節性颱風的路徑走勢。",
        "grammar": {
          "pattern": "S + Modal + Adv + Vt + O + Prepositional Gerund (主詞 + 助動詞 + 程度副詞 + 及物動詞 + 受詞 + 方式介系詞動名詞)",
          "breakdown": [
            {
              "part": "Advanced computational models",
              "role": "主詞 (Subject)",
              "note": "名詞片語，包含分詞形容詞 advanced 與形容詞 computational。"
            },
            {
              "part": "can accurately predict",
              "role": "謂語 (Modal Predicate)",
              "note": "情態助動詞 can + 副詞 accurately 修飾動詞 predict。"
            },
            {
              "part": "seasonal typhoon trajectories",
              "role": "直接受詞 (Direct Object)",
              "note": "trajectories (移動軌跡/路徑)。"
            },
            {
              "part": "using real-time atmospheric telemetry",
              "role": "方式狀詞片語 (Participial Adverbial)",
              "note": "現在分詞 using 表藉由某手段。"
            }
          ],
          "keyPoints": [
            "【同義辨析】：predict (基於數據或經驗之科學預測)、prophesy (宗教神諭式的預言)。",
            "【衍生字詞】：predictable (可預見的)、prediction (預測詞)。"
          ]
        }
      },
      {
        "word": "contradict",
        "kk": "[ˌkɑntrəˈdɪkt]",
        "ipa": "/ˌkɑːntrəˈdɪkt/",
        "pos": "v.",
        "meaning": "矛盾、反駁、與...相抵觸",
        "formula": {
          "parts": [
            {
              "text": "contra-",
              "role": "prefix",
              "meaning": "反對、相對 (拉丁語 contra)"
            },
            {
              "text": "dict",
              "role": "root",
              "meaning": "說 (拉丁語 dicere)"
            }
          ],
          "resultMeaning": "說反話、與別人對著說 ➔「反駁、相抵觸」"
        },
        "sentence": "The suspect's testimony blatantly contradicted the empirical physical evidence uncovered by forensic investigators.",
        "sentenceZh": "嫌疑犯的證詞與鑑識調查人員發現的實質客觀物證產生了公然的抵觸矛盾。",
        "grammar": {
          "pattern": "S + Adv + Vt + O + Participial Modifier (主詞 + 程度副詞 + 及物動詞 + 受詞 + 過去分詞後位修飾)",
          "breakdown": [
            {
              "part": "The suspect's testimony",
              "role": "主詞 (Subject)",
              "note": "所有格名詞片語。"
            },
            {
              "part": "blatantly contradicted",
              "role": "謂語 (Predicate)",
              "note": "blatantly (公然地、明目張膽地) 修飾及物動詞 contradicted。"
            },
            {
              "part": "the empirical physical evidence",
              "role": "直接受詞 (Direct Object)",
              "note": "empirical (經驗的、實證的) + physical (實體的) + evidence (證據，不可數)。"
            },
            {
              "part": "uncovered by forensic investigators",
              "role": "分詞後位修飾 (Past Participle Phrase)",
              "note": "修飾 evidence，相當於 which was uncovered by..."
            }
          ],
          "keyPoints": [
            "【文法注意】：contradict 為及物動詞，直接接受詞 (不要多加 with 或 against)。",
            "【衍生形容詞】：contradictory (矛盾的、互相衝突的)。"
          ]
        }
      },
      {
        "word": "verdict",
        "kk": "[ˈvɝdɪkt]",
        "ipa": "/ˈvɜːrdɪkt/",
        "pos": "n.",
        "meaning": "裁決、判決、定論",
        "formula": {
          "parts": [
            {
              "text": "ver-",
              "role": "root",
              "meaning": "真實 (拉丁語 verus)"
            },
            {
              "text": "dict",
              "role": "root",
              "meaning": "說 (拉丁語 dicere)"
            }
          ],
          "resultMeaning": "說出查核過後的真實之言 ➔「法庭裁決、定論」"
        },
        "sentence": "After three days of intensive deliberation, the jury announced a unanimous guilty verdict in the high-profile fraud trial.",
        "sentenceZh": "經過三天緊張的密集審議後，陪審團在這場備受矚目的詐欺審判中宣布了一致的有罪判決。",
        "grammar": {
          "pattern": "Time Prep Phrase + S + Vt + O + Locative Prep Phrase (時間介系詞片語 + 主詞 + 及物動詞 + 受詞 + 審理環境介系詞片語)",
          "breakdown": [
            {
              "part": "After three days of intensive deliberation",
              "role": "時間狀詞 (Time Adverbial)",
              "note": "介系詞 after 後接時間名詞片語。"
            },
            {
              "part": "the jury",
              "role": "主詞 (Subject)",
              "note": "陪審團 (集合名詞，在此視為單一整體)。"
            },
            {
              "part": "announced",
              "role": "及物動詞 (Transitive Verb)",
              "note": "宣告。"
            },
            {
              "part": "a unanimous guilty verdict",
              "role": "直接受詞 (Direct Object)",
              "note": "unanimous (全體一致的) + guilty (有罪的) + verdict (裁決)。"
            },
            {
              "part": "in the high-profile fraud trial",
              "role": "範圍介系詞片語 (Contextual Prepositional Phrase)",
              "note": "high-profile (引人注目的、高調的)。"
            }
          ],
          "keyPoints": [
            "【固定搭配動詞】：reach a verdict (達成判決)、deliver / return a verdict (宣讀判決)。",
            "【詞根探討】：ver- (真實)，如 verify (核實)、veracity (誠實/真實性)。"
          ]
        }
      },
      {
        "word": "dictate",
        "kk": "[ˈdɪkˌtet]",
        "ipa": "/ˈdɪkteɪt/",
        "pos": "v. / n.",
        "meaning": "(v.) 口述、聽寫、命令、支配；(n.) 命令、原則",
        "formula": {
          "parts": [
            {
              "text": "dict",
              "role": "root",
              "meaning": "說 (拉丁語 dicere)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "依據自己的話語命令他人聽從並寫下 ➔「口述、支配、命令」"
        },
        "sentence": "Market supply and consumer demand ultimately dictate the fluctuating retail prices of agricultural commodities.",
        "sentenceZh": "市場供應量與消費者需求量最終決定並支配著農產品浮動的零售價格。",
        "grammar": {
          "pattern": "Compound Subject + Adv + Vt + O (對等複合主詞 + 副詞 + 及物動詞 + 受詞)",
          "breakdown": [
            {
              "part": "Market supply and consumer demand",
              "role": "對等主詞 (Compound Subject)",
              "note": "由 and 連接兩大經濟概念，謂語使用複數形式。"
            },
            {
              "part": "ultimately",
              "role": "時間/修飾副詞 (Adverb of Degree)",
              "note": "表示「歸根究底、最終」。"
            },
            {
              "part": "dictate",
              "role": "及物動詞 (Transitive Verb)",
              "note": "在此引申為「支配、主導、決定」(= determine)。"
            },
            {
              "part": "the fluctuating retail prices of agricultural commodities",
              "role": "受詞 (Direct Object)",
              "note": "fluctuating (浮動的) 作現在分詞形容詞。"
            }
          ],
          "keyPoints": [
            "【字義引申】：由「口述聽寫」引申為「由上而下決定權威方針」。",
            "【衍生字詞】：dictator (獨裁者)、dictatorship (獨裁政權)。"
          ]
        }
      },
      {
        "word": "dictionary",
        "kk": "[ˈdɪkʃənˌɛri]",
        "ipa": "/ˈdɪkʃəneri/",
        "pos": "n.",
        "meaning": "字典、詞典",
        "formula": {
          "parts": [
            {
              "text": "dict",
              "role": "root",
              "meaning": "說、言詞 (say, speak)"
            },
            {
              "text": "-ion",
              "role": "suffix",
              "meaning": "名詞字尾 (action/state)"
            },
            {
              "text": "-ary",
              "role": "suffix",
              "meaning": "集合、存放之地 (place/collection)"
            }
          ],
          "resultMeaning": "將所有說出的字詞及其用法彙編成冊 ➔「字典」"
        },
        "sentence": "Whenever linguistic scholars encounter archaic idioms, they consult an authoritative etymological dictionary.",
        "sentenceZh": "每當語言學者遇到古老成語時，他們都會查閱權威的詞源字典。",
        "grammar": {
          "pattern": "Adv Clause of Condition/Time + S + Vt + O",
          "breakdown": [
            {
              "part": "Whenever linguistic scholars encounter archaic idioms",
              "role": "條件/時間副詞子句",
              "note": "whenever (每當) 引導子句，scholars 為主詞，encounter 為動詞。"
            },
            {
              "part": "they",
              "role": "主要子句主詞",
              "note": "代名詞指稱 scholars。"
            },
            {
              "part": "consult",
              "role": "及物動詞 (Verb)",
              "note": "意為「查閱 (字典/資料)」或「諮詢 (專家)」。"
            },
            {
              "part": "an authoritative etymological dictionary",
              "role": "受詞 (Object)",
              "note": "名詞片語，包含雙重修飾詞 authoritative 與 etymological。"
            }
          ],
          "keyPoints": [
            "【動詞用法】：consult a dictionary / consult a doctor，皆直接加受詞，不需加介系詞 to 或 with。",
            "【字尾延伸】：-ary 表「地點或收藏處」，如 library (圖書館)、mortuary (太平間)。"
          ]
        }
      },
      {
        "word": "dedicate",
        "kk": "[ˈdɛdəˌket]",
        "ipa": "/ˈdɛdɪkeɪt/",
        "pos": "v.",
        "meaning": "奉獻、致力於、將(著作)獻給",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "完全、鄭重 (down, thoroughly)"
            },
            {
              "text": "dic (dict)",
              "role": "root",
              "meaning": "宣告、陳述 (declare, proclaim)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "動詞字尾"
            }
          ],
          "resultMeaning": "鄭重向大眾宣告自己的誓約與心志 ➔「奉獻、致力於」"
        },
        "sentence": "The humanitarian doctor decided to dedicate her entire career to treating underprivileged patients in rural communities.",
        "sentenceZh": "這位人道主義醫生決定將其整個職業生涯奉獻給鄉村社區的弱勢病患治療。",
        "grammar": {
          "pattern": "S + Vt + Infinitive Phrase (to dedicate A to B)",
          "breakdown": [
            {
              "part": "The humanitarian doctor",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "decided",
              "role": "及物動詞 (Verb)",
              "note": "後接不定詞作受詞。"
            },
            {
              "part": "to dedicate her entire career",
              "role": "不定詞片語 (受詞 A)",
              "note": "dedicate A to B 結構。"
            },
            {
              "part": "to treating underprivileged patients in rural communities",
              "role": "介系詞片語 (對象 B)",
              "note": "to 為介系詞，後接動名詞 treating。"
            }
          ],
          "keyPoints": [
            "【文法陷阱】：dedicate A to B 中的 to 為「介系詞」，後面必須接動名詞 (V-ing) 或名詞，不可接原形動詞！",
            "【同義延伸】：devote A to B, commit oneself to B 具完全相同文法規則。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Power of the Spoken Word: Dictating Truth and Justice",
      "titleZh": "言語的力量：宣告真理與正義",
      "intro": "在古代社會，話語一旦說出 (dict) 就具有法律與契約的效力。從法官的裁決 (verdict) 到先知的預言 (predict)，言語重塑著人類命運。",
      "paragraphs": [
        {
          "en": "Throughout history, rulers sought to dictate the laws of the land, demanding that their decrees be recorded without questioning. However, courageous philosophers often dared to contradict tyranny with unyielding moral convictions.",
          "zh": "縱觀歷史，統治者總試圖口述並強行制定國家的法律，要求他們的法令不容置疑地被記錄下來。然而，勇敢的哲學家經常敢於以不屈的道德信念反駁暴政。"
        },
        {
          "en": "In modern democracies, no single voice can arbitrary predict the fate of the innocent. Only after transparent cross-examination can an impartial jury deliver a solemn verdict based purely upon substantiated facts.",
          "zh": "在現代民主體制中，沒有任何單一聲音能武斷預言無辜者的命運。只有在透明的交互詰問之後，公正的陪審團才能純粹依據經證實的事實作出莊嚴的判決。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What does the word 'contradict' mean in the context of opposing tyranny?",
          "qZh": "在對抗暴政的語境中，'contradict' 的意涵為何？",
          "options": [
            "A. To agree completely and sign the contract.",
            "B. To speak out against and oppose tyranny. (發聲反對並抵觸暴政)",
            "C. To run away from responsibility.",
            "D. To dictate taxes to citizens."
          ],
          "answer": 1,
          "explanation": "文中指出勇敢的哲學家敢於以道德信念「contradict tyranny」(公開反駁並抗拒暴政)。"
        }
      ]
    }
  },
  {
    "id": "port",
    "name": "port",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「portare」(搬運、攜帶、運送)，以及名詞「portus」(港口、門戶)。",
    "originMeaning": "搬運、運送、攜帶、港口",
    "phonetic": "/pɔːrt/",
    "icon": "🚢",
    "color": "#0284C7",
    "summary": "物流貿易、地理空間轉移及隨身攜帶科技的核心字根。",
    "words": [
      {
        "word": "transport",
        "kk": "[trænsˈpɔrt]",
        "ipa": "/trænsˈpɔːrt/",
        "pos": "v. / n.",
        "meaning": "運輸、運送；(n.) 交通工具、運輸系統",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "穿過、跨越 (拉丁語 trans)"
            },
            {
              "text": "port",
              "role": "root",
              "meaning": "搬運 (拉丁語 portare)"
            }
          ],
          "resultMeaning": "將貨物或人員搬運跨越不同地域 ➔「運輸、運送」"
        },
        "sentence": "High-speed electric freight trains transport agricultural harvests from rural farming regions to coastal metropolitan hubs.",
        "sentenceZh": "高速電力貨運列車將農村耕作地區採收的農作物運送至沿海大都會樞紐。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Prep Phrase (主詞 + 及物動詞 + 受詞 + 出發地片語 + 目的地片語)",
          "breakdown": [
            {
              "part": "High-speed electric freight trains",
              "role": "主詞 (Subject)",
              "note": "包含三個前置修飾語 (high-speed, electric, freight) 的複合主詞片語。"
            },
            {
              "part": "transport",
              "role": "及物動詞 (Transitive Verb)",
              "note": "現在簡單式，主詞為複數 trains。"
            },
            {
              "part": "agricultural harvests",
              "role": "直接受詞 (Direct Object)",
              "note": "農業收穫作物。"
            },
            {
              "part": "from rural farming regions",
              "role": "起點介系詞片語 (Source Prep Phrase)",
              "note": "from 表來源起點。"
            },
            {
              "part": "to coastal metropolitan hubs",
              "role": "終點介系詞片語 (Destination Prep Phrase)",
              "note": "to 表抵達目標。"
            }
          ],
          "keyPoints": [
            "【經典移動介系詞對】：transport A from [起點] to [終點]。",
            "【衍生名詞】：transportation (運輸工具、交通運輸網)。"
          ]
        }
      },
      {
        "word": "export",
        "kk": "[ˈɛkspɔrt] (n.) / [ɪkˈspɔrt] (v.)",
        "ipa": "/ˈɛkspɔːrt/ (n.) / /ɪkˈspɔːrt/ (v.)",
        "pos": "v. / n.",
        "meaning": "出口、輸出；(n.) 出口商品",
        "formula": {
          "parts": [
            {
              "text": "ex-",
              "role": "prefix",
              "meaning": "向外、出 (拉丁語 ex)"
            },
            {
              "text": "port",
              "role": "root",
              "meaning": "港口/運送 (拉丁語 portare)"
            }
          ],
          "resultMeaning": "將國內物產經由港口運送到國外 ➔「出口、輸出」"
        },
        "sentence": "The manufacturing powerhouse exports advanced semiconductor chips to tech companies situated across fifty countries.",
        "sentenceZh": "這座製造業重鎮將先進的半導體晶片出口至分佈於五十個國家的科技公司。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Participle Modifier (主詞 + 及物動詞 + 受詞 + 接收對象片語 + 過去分詞後位修飾)",
          "breakdown": [
            {
              "part": "The manufacturing powerhouse",
              "role": "主詞 (Subject)",
              "note": "powerhouse 喻指產業巨擘、核心重鎮。"
            },
            {
              "part": "exports",
              "role": "及物動詞 (Transitive Verb)",
              "note": "第三人稱單數現在式。"
            },
            {
              "part": "advanced semiconductor chips",
              "role": "直接受詞 (Direct Object)",
              "note": "先進半導體晶片。"
            },
            {
              "part": "to tech companies",
              "role": "介系詞對象 (Prepositional Object)",
              "note": "to 表輸出目標對象。"
            },
            {
              "part": "situated across fifty countries",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "修飾 companies，相當於 which are situated across..."
            }
          ],
          "keyPoints": [
            "【重音轉移規律】：名詞時重音在第一音節 /ˈɛkspɔːrt/；動詞時重音在第二音節 /ɪkˈspɔːrt/。",
            "【對立詞彙】：import (進口；im- 進入 + port)。"
          ]
        }
      },
      {
        "word": "portable",
        "kk": "[ˈpɔrtəb!]",
        "ipa": "/ˈpɔːrtəbl/",
        "pos": "adj.",
        "meaning": "便攜式的、可輕易攜帶的、手提的",
        "formula": {
          "parts": [
            {
              "text": "port",
              "role": "root",
              "meaning": "攜帶 (拉丁語 portare)"
            },
            {
              "text": "-able",
              "role": "suffix",
              "meaning": "能夠...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "能夠輕鬆隨身攜帶行走的 ➔「便攜的、輕便的」"
        },
        "sentence": "The humanitarian medical team brought portable ultrasound devices to assist displaced refugees in remote mountain encampments.",
        "sentenceZh": "人道醫療小組攜帶便攜式超音波設備，前往偏遠山區營地協助流離失所的難民。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的狀詞不定詞片語)",
          "breakdown": [
            {
              "part": "The humanitarian medical team",
              "role": "主詞 (Subject)",
              "note": "人道醫療團隊。"
            },
            {
              "part": "brought",
              "role": "及物動詞 (Transitive Verb)",
              "note": "bring 的過去式。"
            },
            {
              "part": "portable ultrasound devices",
              "role": "直接受詞 (Direct Object)",
              "note": "portable (便攜的) 修飾儀器設備。"
            },
            {
              "part": "to assist displaced refugees in remote mountain encampments",
              "role": "目的狀詞 (Infinitive Phrase)",
              "note": "displaced (流離失所的) 為過去分詞轉形容詞；in encampments 表地點。"
            }
          ],
          "keyPoints": [
            "【構詞尾碼】：-able 具備被動受身與潛能含意 (can be carried)。",
            "【衍生名詞】：portability (便攜性、易攜帶特質)。"
          ]
        }
      },
      {
        "word": "import",
        "kk": "[ˈɪmˌport]",
        "ipa": "/ˈɪmpɔːrt/",
        "pos": "v. / n.",
        "meaning": "進口、輸入；(n.) 進口商品、重要性",
        "formula": {
          "parts": [
            {
              "text": "im- (in-)",
              "role": "prefix",
              "meaning": "向內、進入 (into)"
            },
            {
              "text": "port",
              "role": "root",
              "meaning": "搬運、港口 (carry, harbor)"
            }
          ],
          "resultMeaning": "由海外運入國內港口 ➔「進口、輸入」"
        },
        "sentence": "Because the island nation lacks domestic petroleum reserves, it must import crude oil from overseas suppliers.",
        "sentenceZh": "由於這個島國缺乏國內石油儲備，它必須從海外供應商進口原油。",
        "grammar": {
          "pattern": "Adv Clause of Reason (Because...) + S + Modal + Vt + O + Prep Phrase",
          "breakdown": [
            {
              "part": "Because the island nation lacks domestic petroleum reserves",
              "role": "原因副詞子句",
              "note": "Because 引導原因子句，lacks 為及物動詞。"
            },
            {
              "part": "it",
              "role": "主要子句主詞",
              "note": "代名詞指 the island nation。"
            },
            {
              "part": "must import",
              "role": "動詞片語 (Verb)",
              "note": "情態助動詞 must + 原形動詞 import。"
            },
            {
              "part": "crude oil",
              "role": "直接受詞 (Direct Object)",
              "note": "意為「原油」。"
            },
            {
              "part": "from overseas suppliers",
              "role": "來源介系詞片語",
              "note": "表貨物進口來源。"
            }
          ],
          "keyPoints": [
            "【重音規則】：import 當動詞時重音在第二音節 [ɪmˈpɔrt]，當名詞時重音在第一音節 [ˈɪmport]（前名後動規則）。",
            "【反義對比】：import (輸入) vs. export (輸出)。"
          ]
        }
      },
      {
        "word": "support",
        "kk": "[səˈport]",
        "ipa": "/səˈpɔːrt/",
        "pos": "v. / n.",
        "meaning": "支持、支撐、扶養",
        "formula": {
          "parts": [
            {
              "text": "sup- (sub-)",
              "role": "prefix",
              "meaning": "在下方 (under, beneath)"
            },
            {
              "text": "port",
              "role": "root",
              "meaning": "承載、支撐 (carry, bear)"
            }
          ],
          "resultMeaning": "在下方用力扛起、承載重物 ➔「支撐、支持」"
        },
        "sentence": "Several reinforced concrete pillars were erected underneath the bridge to support the massive vehicular traffic.",
        "sentenceZh": "橋樑下方豎立了數根鋼筋混凝土支柱，以支撐龐大的車輛交通流量。",
        "grammar": {
          "pattern": "S + Passive Verb + Prep Phrase + Infinitive Phrase of Purpose",
          "breakdown": [
            {
              "part": "Several reinforced concrete pillars",
              "role": "主詞 (Subject)",
              "note": "reinforced concrete (鋼筋混凝土) 修飾 pillars。"
            },
            {
              "part": "were erected",
              "role": "被動態謂語動詞",
              "note": "erect (立起、豎立) 之過去被動態。"
            },
            {
              "part": "underneath the bridge",
              "role": "地點介系詞片語",
              "note": "修飾豎立位置。"
            },
            {
              "part": "to support the massive vehicular traffic",
              "role": "不定詞目的狀語",
              "note": "to 表目的，support 接受詞 traffic。"
            }
          ],
          "keyPoints": [
            "【字首同化】：sub- 在 p 開頭的根詞前同化為 sup- (如 support, suppress)。",
            "【多重語義】：support 可表物理支撐、金錢扶養 (support a family)、精神論點支持 (support a theory)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Merchant of the Global Harbor: Porting Wealth Across Oceans",
      "titleZh": "世界港灣的貿易篇章：穿梭大洋的物資流動",
      "intro": "自大航海時代以來，港口 (port) 與運載 (port) 連結了原本隔絕的大陸，推動了全球化的商業動脈。",
      "paragraphs": [
        {
          "en": "Deep-water harbors serve as the beating heart of global commerce, where gigantic container ships transport millions of tons of food, textiles, and minerals every day across stormy oceans.",
          "zh": "深水海港是全球商業跳動的心臟，巨大的貨櫃輪每天在此運載著數百萬噸的糧食、紡織品與礦物，橫越波濤洶湧的大洋。"
        },
        {
          "en": "Nations that successfully export manufactured electronics while importing raw materials steadily enhance their economic resilience, proving that mastery over the logistics of 'port' defines national prosperity.",
          "zh": "那些成功出口高精密電子產品並同時進口原料的國家，穩步增強了其經濟韌性，證明了掌握「運送與港口 (port)」的物流實力定義了國家的繁榮興盛。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What defines national prosperity according to the article?",
          "qZh": "根據文章，何種能力定義了國家的繁榮？",
          "options": [
            "A. Mastery over logistics, transport, and international export/import. (掌握物流、運輸與進出口實力)",
            "B. Total isolation from world trade.",
            "C. Replacing human sailors with robots.",
            "D. Ceasing all manufacturing."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「mastery over the logistics of 'port' defines national prosperity」。"
        }
      ]
    }
  },
  {
    "id": "bio",
    "name": "bio",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「βίος」(bíos)，意指「生命、生物、人類的一生 (life, living organisms)」。",
    "originMeaning": "生命、生物、一生",
    "phonetic": "/ˈbaɪoʊ/",
    "icon": "🧬",
    "color": "#16A34A",
    "summary": "涵蓋生命科學、生態環保、生平傳記與醫藥健康的最關鍵字根。",
    "words": [
      {
        "word": "biology",
        "kk": "[baɪˈɑlədʒi]",
        "ipa": "/baɪˈɑːlədʒi/",
        "pos": "n.",
        "meaning": "生物學",
        "formula": {
          "parts": [
            {
              "text": "bio-",
              "role": "root",
              "meaning": "生命、生物 (希臘語 bíos)"
            },
            {
              "text": "-logy",
              "role": "suffix",
              "meaning": "學問、學科 (希臘語 logos 言說/研究)"
            }
          ],
          "resultMeaning": "探討研究一切生命有機體奧秘的學門 ➔「生物學」"
        },
        "sentence": "Modern molecular biology investigates how microscopic cellular structures encode genetic instructions.",
        "sentenceZh": "現代分子生物學探討微觀的細胞結構如何編碼遺傳指令。",
        "grammar": {
          "pattern": "S + Vt + Wh-Noun Clause (主詞 + 及物動詞 + Wh-引導的受詞名詞子句)",
          "breakdown": [
            {
              "part": "Modern molecular biology",
              "role": "主詞 (Subject)",
              "note": "專門學門名詞片語。"
            },
            {
              "part": "investigates",
              "role": "及物動詞 (Transitive Verb)",
              "note": "第三人稱單數現在式。"
            },
            {
              "part": "how microscopic cellular structures encode genetic instructions",
              "role": "名詞子句受詞 (Noun Clause as Object)",
              "note": "how 為疑問副詞引導間接問句/名詞子句；structures 為子句主詞，encode 為及物動詞。"
            }
          ],
          "keyPoints": [
            "【名詞子句結構】：investigate + how + S + V (探究...如何運作)。",
            "【字根尾碼】：-logy 表示學門，如 geology (地質學)、psychology (心理學)。"
          ]
        }
      },
      {
        "word": "biodiversity",
        "kk": "[ˌbaɪodaɪˈvɝsəti]",
        "ipa": "/ˌbaɪoʊdaɪˈvɜːrsəti/",
        "pos": "n.",
        "meaning": "生物多樣性",
        "formula": {
          "parts": [
            {
              "text": "bio-",
              "role": "root",
              "meaning": "生命 (希臘語 bíos)"
            },
            {
              "text": "diversity",
              "role": "base",
              "meaning": "多樣性 (拉丁語 diversitas)"
            }
          ],
          "resultMeaning": "生態系中所有生命物種的豐富多元性 ➔「生物多樣性」"
        },
        "sentence": "Conserving coastal rainforests protects endangered wildlife and safeguards irreplaceable global biodiversity.",
        "sentenceZh": "保育沿海雨林能保護瀕危野生動物，並守護不可替代的全球生物多樣性。",
        "grammar": {
          "pattern": "Gerund Subject + Vt1 + O1 + and + Vt2 + O2 (動名詞主詞 + 第一及物動詞 + 受詞1 + 對等連接詞 + 第二及物動詞 + 受詞2)",
          "breakdown": [
            {
              "part": "Conserving coastal rainforests",
              "role": "動名詞主詞 (Gerund Subject)",
              "note": "單數概念主詞。"
            },
            {
              "part": "protects endangered wildlife",
              "role": "第一個謂語對 (First Predicate)",
              "note": "protects 加 s；wildlife 為集合名詞。"
            },
            {
              "part": "and safeguards",
              "role": "對等動詞 (Coordinated Verb)",
              "note": "safeguards 保持單數一致性。"
            },
            {
              "part": "irreplaceable global biodiversity",
              "role": "第二受詞 (Second Object)",
              "note": "irreplaceable (不可替代的；ir- 不 + replace 替代 + able 能)。"
            }
          ],
          "keyPoints": [
            "【動態對稱】：protects... and safeguards... 形成力量均勻的排比對稱動詞片語。",
            "【多樣性構詞】：di- (分開) + vertere (轉向) ➔ diversity (多樣、多元)。"
          ]
        }
      },
      {
        "word": "antibiotic",
        "kk": "[ˌæntɪbaɪˈɑtɪk]",
        "ipa": "/ˌæntibaɪˈɑːtɪk/",
        "pos": "n. / adj.",
        "meaning": "抗生素；(adj.) 抗菌的",
        "formula": {
          "parts": [
            {
              "text": "anti-",
              "role": "prefix",
              "meaning": "反對、對抗 (希臘語 anti)"
            },
            {
              "text": "bio",
              "role": "root",
              "meaning": "生命、微生物 (希臘語 bíos)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "...的製劑、藥劑 (字尾)"
            }
          ],
          "resultMeaning": "用以對抗有害微生物細菌生命的藥劑 ➔「抗生素」"
        },
        "sentence": "Physicians urge patients to complete their prescribed antibiotic course to curb bacterial drug resistance.",
        "sentenceZh": "醫師力勸病患服完所開立的抗生素療程，以遏制細菌產生抗藥性。",
        "grammar": {
          "pattern": "S + Vt + O + to-Infinitive + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 受詞補語不定詞 + 目的狀詞不定詞)",
          "breakdown": [
            {
              "part": "Physicians",
              "role": "主詞 (Subject)",
              "note": "內科醫師。"
            },
            {
              "part": "urge",
              "role": "及物動詞 (Transitive Verb)",
              "note": "搭配句型 urge somebody to do something。"
            },
            {
              "part": "patients",
              "role": "受詞 (Direct Object)",
              "note": "病患。"
            },
            {
              "part": "to complete their prescribed antibiotic course",
              "role": "受詞補語 (Objective Complement)",
              "note": "prescribed (所處方的) 為過去分詞修飾療程 course。"
            },
            {
              "part": "to curb bacterial drug resistance",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "curb (抑制、遏止)。"
            }
          ],
          "keyPoints": [
            "【動詞句型】：urge / advise / persuade + someone + to V。",
            "【醫學術語】：antibiotic resistance (抗生素抗藥性)。"
          ]
        }
      },
      {
        "word": "biography",
        "kk": "[baɪˈɑgrəfi]",
        "ipa": "/baɪˈɑːɡrəfi/",
        "pos": "n.",
        "meaning": "傳記、傳記文學",
        "formula": {
          "parts": [
            {
              "text": "bio-",
              "role": "root",
              "meaning": "一生、生命 (希臘語 bíos)"
            },
            {
              "text": "graphy",
              "role": "suffix/base",
              "meaning": "書寫、記錄 (希臘語 graphein)"
            }
          ],
          "resultMeaning": "書寫記錄某人一生的著作 ➔「傳記」"
        },
        "sentence": "The Pulitzer-winning biography vividly chronicled the turbulent personal life of the reclusive philosopher.",
        "sentenceZh": "這部榮獲普立茲獎的傳記生動記錄了這位隱世哲學家動盪波折的個人生活。",
        "grammar": {
          "pattern": "S + Adv + Vt + O (主詞 + 方式副詞 + 及物動詞 + 受詞)",
          "breakdown": [
            {
              "part": "The Pulitzer-winning biography",
              "role": "主詞 (Subject)",
              "note": "複合形容詞 Pulitzer-winning 修飾 biography。"
            },
            {
              "part": "vividly",
              "role": "副詞 (Adverb of Manner)",
              "note": "生動栩栩如生地修飾 chronicled。"
            },
            {
              "part": "chronicled",
              "role": "及物動詞 (Transitive Verb)",
              "note": "編年史般詳盡記載。"
            },
            {
              "part": "the turbulent personal life of the reclusive philosopher",
              "role": "受詞 (Direct Object)",
              "note": "turbulent (動盪的)；reclusive (隱遁孤僻的)。"
            }
          ],
          "keyPoints": [
            "【同源自傳對比】：autobiography (auto 自己 + bio 生命 + graphy 寫 = 自傳)。",
            "【動詞詞根跨界】：chronicled 本身源於 chron (時間) 字根！"
          ]
        }
      },
      {
        "word": "biosphere",
        "kk": "[ˈbaɪəˌsfɪr]",
        "ipa": "/ˈbaɪoʊsfɪr/",
        "pos": "n.",
        "meaning": "生物圈 (地球上所有生物及其生存環境)",
        "formula": {
          "parts": [
            {
              "text": "bio-",
              "role": "root",
              "meaning": "生命 (life)"
            },
            {
              "text": "sphere",
              "role": "base",
              "meaning": "球體、範圍 (globe, ball)"
            }
          ],
          "resultMeaning": "地球表面包含一切活體生命的球狀生態層 ➔「生物圈」"
        },
        "sentence": "Human industrial emissions have exerted unprecedented ecological stress on the delicate balance of our global biosphere.",
        "sentenceZh": "人類工業排放對全球生物圈的微妙平衡施加了前所未有的生態壓力。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase",
          "breakdown": [
            {
              "part": "Human industrial emissions",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "have exerted",
              "role": "及物動詞 (Verb)",
              "note": "現在完成式，exert pressure/stress on 常用搭配。"
            },
            {
              "part": "unprecedented ecological stress",
              "role": "受詞 (Object)",
              "note": "unprecedented (史無前例的) 修飾 stress。"
            },
            {
              "part": "on the delicate balance of our global biosphere",
              "role": "介系詞片語",
              "note": "on 表作用對象。"
            }
          ],
          "keyPoints": [
            "【動詞搭配】：exert ... on ... 為高級學術英文搭配，表示「對...施加(壓力、影響)」。",
            "【地球圈層】：atmosphere (大氣圈)、hydrosphere (水圈)、lithosphere (岩石圈)、biosphere (生物圈)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Living Web: Celebrating the Symphony of Bios",
      "titleZh": "生命之網：譜寫生命的交響詩",
      "intro": "從單細胞真核菌落到寫下厚重自傳的智慧靈長類，字根 bio- 見證了三十八億年生命演化的壯麗奇蹟。",
      "paragraphs": [
        {
          "en": "Without the discoveries of modern biology, humanity would remain helpless in the face of microscopic pathogens. When Alexander Fleming discovered the world's first effective antibiotic, he inaugurated an era where once-fatal bacterial infections could be cured in days.",
          "zh": "沒有現代生物學的各項發現，人類在微觀病原體面前仍將束手無策。當亞歷山大·弗萊明發現世界上第一種有效抗生素時，他開啟了一個曾被視為絕症的細菌感染能在數天內治癒的新紀元。"
        },
        {
          "en": "Today, preserving the precious biodiversity of coral reefs and old-growth canopies is no longer merely an academic issue. It is a shared ecological obligation to ensure that future generations can inherit a flourishing biosphere.",
          "zh": "今日，守護珊瑚礁與原始林冠珍貴的生物多樣性已不再僅僅是學術議題，而是一項共同的生態責任，旨在確保後代子孫能繼承一個繁榮生息的生物圈。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What medical milestone did the discovery of antibiotics achieve?",
          "qZh": "抗生素的發現達成了什麼醫療里程碑？",
          "options": [
            "A. Curing once-fatal bacterial infections within days. (數天內治癒曾為致命絕症的細菌感染)",
            "B. Eliminating all common colds immediately.",
            "C. Replacing healthy red blood cells.",
            "D. Allowing humans to breathe underwater."
          ],
          "answer": 0,
          "explanation": "文中第一段指出抗生素的發現「inaugurated an era where once-fatal bacterial infections could be cured in days」。"
        }
      ]
    }
  },
  {
    "id": "auto",
    "name": "auto-",
    "type": "prefix",
    "typeLabel": "希臘語字首 (Greek Prefix)",
    "etymology": "源自古希臘語「αὐτός」(autós)，原意為「自己、本人、獨立自發 (self, same, spontaneous)」。",
    "originMeaning": "自己、自發、自動、獨立",
    "phonetic": "/ˈɔːtoʊ/",
    "icon": "⚙️",
    "color": "#EA580C",
    "summary": "廣泛應用於人工智慧、自動化控制、自主性與個人創作的核心字首。",
    "words": [
      {
        "word": "automatic",
        "kk": "[ˌɔtəˈmætɪk]",
        "ipa": "/ˌɔːtəˈmætɪk/",
        "pos": "adj.",
        "meaning": "自動的、自發的、無意識的",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自己、獨立 (希臘語 autós)"
            },
            {
              "text": "mat",
              "role": "base",
              "meaning": "思考、意願、運動 (希臘語 matos 動作/自發)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "具備自主思考機制能自己運動運轉的 ➔「自動的」"
        },
        "sentence": "The manufacturing facility upgraded its conveyor lines with automatic sensors that detect microscopic structural flaws.",
        "sentenceZh": "該製造工廠以能偵測微觀結構瑕疵的自動感測器，升級了其輸送帶生產線。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase with Relative Clause (主詞 + 及物動詞 + 受詞 + 介系詞片語 + 關係子句)",
          "breakdown": [
            {
              "part": "The manufacturing facility",
              "role": "主詞 (Subject)",
              "note": "製造廠房設施。"
            },
            {
              "part": "upgraded",
              "role": "及物動詞 (Transitive Verb)",
              "note": "upgrade A with B (以 B 升級 A)。"
            },
            {
              "part": "its conveyor lines",
              "role": "直接受詞 (Direct Object)",
              "note": "輸送帶生產線。"
            },
            {
              "part": "with automatic sensors",
              "role": "介系詞工具片語 (Prepositional Instrument)",
              "note": "automatic 修飾 sensors。"
            },
            {
              "part": "that detect microscopic structural flaws",
              "role": "限定關係子句 (Relative Clause)",
              "note": "that 指代複數 sensors，子句動詞為原形 detect。"
            }
          ],
          "keyPoints": [
            "【動詞句型】：upgrade A with B (以 B 裝備/升級 A)。",
            "【反義字】：manual (手動的；源自 manus 手)。"
          ]
        }
      },
      {
        "word": "autonomy",
        "kk": "[ɔˈtɑnəmi]",
        "ipa": "/ɔːˈtɑːnəmi/",
        "pos": "n.",
        "meaning": "自治、自治權、自主性、獨立決策權",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自己 (希臘語 autós)"
            },
            {
              "text": "nomy",
              "role": "root",
              "meaning": "法律、規則 (希臘語 nomos 法則)"
            }
          ],
          "resultMeaning": "自己給自己制定法則自行治理 ➔「自治、自主權」"
        },
        "sentence": "Fostering employee autonomy often stimulates breakthrough innovation within technology research startups.",
        "sentenceZh": "培養員工的自主獨立性，往往能在科技研發新創公司中激發突破性的創新。",
        "grammar": {
          "pattern": "Gerund Subject + Adv + Vt + O + Prepositional Location (動名詞主詞 + 頻率副詞 + 及物動詞 + 受詞 + 地點介系詞片語)",
          "breakdown": [
            {
              "part": "Fostering employee autonomy",
              "role": "動名詞片語主詞 (Gerund Subject)",
              "note": "單數動名詞概念。"
            },
            {
              "part": "often stimulates",
              "role": "謂語 (Predicate)",
              "note": "stimulates (加 s 配合動名詞主詞)。"
            },
            {
              "part": "breakthrough innovation",
              "role": "直接受詞 (Direct Object)",
              "note": "breakthrough (突破性的) 作形容詞修飾 innovation。"
            },
            {
              "part": "within technology research startups",
              "role": "地點範圍片語 (Prepositional Modifier)",
              "note": "在科技新創中。"
            }
          ],
          "keyPoints": [
            "【詞根網絡】：-nomy (法則/管理)，同根字如 astronomy (astro 星星 + nomy 法則 = 天文學)、economy (oikos 家 + nomy 法則 = 經濟學)。",
            "【形容詞型態】：autonomous (自治的、自主的，如 autonomous vehicles 自動駕駛車)。"
          ]
        }
      },
      {
        "word": "autopilot",
        "kk": "[ˈɔtoˌpaɪlət]",
        "ipa": "/ˈɔːtoʊpaɪlət/",
        "pos": "n.",
        "meaning": "自動駕駛系統；(引申) 慣性無意識狀態",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自動、自己 (希臘語 autós)"
            },
            {
              "text": "pilot",
              "role": "base",
              "meaning": "飛行員、舵手 (義大利語 pilota)"
            }
          ],
          "resultMeaning": "代替人類飛行員進行自動姿態導航的裝置 ➔「自動駕駛」"
        },
        "sentence": "Modern passenger aircraft can cruise safely on autopilot while aviators monitor navigation displays for severe turbulence.",
        "sentenceZh": "現代客機能在自動駕駛模式下安全平穩巡航，同時飛行員監控導航螢幕以防遭遇劇烈亂流。",
        "grammar": {
          "pattern": "S + Modal + Vi + Adv + Prep Phrase + While-Clause (主詞 + 助動詞 + 不及物動詞 + 副詞 + 介系詞片語 + While時間子句)",
          "breakdown": [
            {
              "part": "Modern passenger aircraft",
              "role": "主詞 (Subject)",
              "note": "aircraft 單複數同形，此處作複數。"
            },
            {
              "part": "can cruise",
              "role": "謂語 (Modal Predicate)",
              "note": "cruise 不及物動詞表巡航。"
            },
            {
              "part": "safely on autopilot",
              "role": "方式副詞與片語 (Adverbials)",
              "note": "on autopilot (處於自動駕駛狀態)。"
            },
            {
              "part": "while aviators monitor navigation displays",
              "role": "時間對稱子句 (Time Clause)",
              "note": "while 連接詞表示兩件事情同時進行。"
            },
            {
              "part": "for severe turbulence",
              "role": "目的/防範介系詞片語 (Prepositional Phrase)",
              "note": "monitor... for... (監控防範...現象)。"
            }
          ],
          "keyPoints": [
            "【常用生活引申片語】：be on autopilot (心不在焉、憑習慣機械式地做事)。",
            "【名詞單複數】：aircraft 單複數同形，不加 s。"
          ]
        }
      },
      {
        "word": "autograph",
        "kk": "[ˈɔtəˌgræf]",
        "ipa": "/ˈɔːtəɡræf/",
        "pos": "n. / v.",
        "meaning": "親筆簽名；親筆書寫/簽名",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自己、親自 (self)"
            },
            {
              "text": "graph",
              "role": "root",
              "meaning": "書寫、畫 (write)"
            }
          ],
          "resultMeaning": "由本人親手書寫留念的名字 ➔「親筆簽名」"
        },
        "sentence": "Eager fans waited patiently behind the security barrier hoping that the renowned author would sign an autograph.",
        "sentenceZh": "熱切的書迷們耐心地在防護欄後等待，希望這位知名作家能為他們親筆簽名。",
        "grammar": {
          "pattern": "S + Vi + Adv + Prep Phrase + Participle Phrase (hoping that...)",
          "breakdown": [
            {
              "part": "Eager fans",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "waited",
              "role": "不及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "patiently",
              "role": "情狀副詞",
              "note": "修飾 waited。"
            },
            {
              "part": "behind the security barrier",
              "role": "地點介系詞片語",
              "note": "修飾等待位置。"
            },
            {
              "part": "hoping that the renowned author would sign an autograph",
              "role": "現在分詞伴隨狀語",
              "note": "hoping 引導名詞子句作 hope 之受詞。"
            }
          ],
          "keyPoints": [
            "【簽名詞彙辨析】：autograph 多指名流明星的「題名、親筆簽名紀念」；signature 則指法律契約、公文上的「簽字」。",
            "【分詞構句】：hoping that... 是現在分詞伴隨動作，主詞與主要句主詞 fans 相同。"
          ]
        }
      },
      {
        "word": "automobile",
        "kk": "[ˈɔtəməˌbil]",
        "ipa": "/ˈɔːtəməbiːl/",
        "pos": "n.",
        "meaning": "汽車、機動車輛",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自己、自發 (self)"
            },
            {
              "text": "mobile",
              "role": "root",
              "meaning": "移動的 (movable)"
            }
          ],
          "resultMeaning": "毋須依靠牛馬牲畜拉曳、能自行前進移動之車輛 ➔「汽車」"
        },
        "sentence": "The mass adoption of the commercial automobile revolutionized personal transportation and suburban urban development.",
        "sentenceZh": "商用汽車的大規模普及徹底變革了個人交通運輸與郊區都市發展。",
        "grammar": {
          "pattern": "S + Vt (revolutionized) + O (transportation and development)",
          "breakdown": [
            {
              "part": "The mass adoption of the commercial automobile",
              "role": "主詞 (Subject)",
              "note": "mass adoption (大規模採用普及)。"
            },
            {
              "part": "revolutionized",
              "role": "及物動詞 (Verb)",
              "note": "意為「徹底變革」。"
            },
            {
              "part": "personal transportation and suburban urban development",
              "role": "受詞 (Object)",
              "note": "and 連接兩組受詞片語。"
            }
          ],
          "keyPoints": [
            "【移動字根】：mob / mot / mov 表移動，如 mobile (移動的)、motion (運動)、motivate (激發動力)。",
            "【工業史名詞】：automobile industry (汽車工業)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Autonomous Frontier: Machines and the Self",
      "titleZh": "自主新前沿：機械自律與人之主體",
      "intro": "字首 auto- 象徵著脫離外在牽制、追尋自主運轉的野心。從希臘城邦的自治 (autonomy) 到今日無人載具的自動駕駛 (autopilot)，自我力量持續進化。",
      "paragraphs": [
        {
          "en": "In modern factories, automatic assembly lines perform intricate precision tasks twenty-four hours a day without human fatigue. Robotic arms weld steel frames with microscopic tolerance, demonstrating the pinnacle of mechanical self-regulation.",
          "zh": "在現代工廠中，自動化組裝線每天二十四小時執行著錯綜複雜的精密任務而毫無人為疲憊。機械手臂以微米級的公差焊接鋼架，展現了機械自主調控的巔峰。"
        },
        {
          "en": "However, ethical thinkers caution that human beings should never put their moral discernment on autopilot. While artificial systems enjoy increasing operational autonomy, the ultimate responsibility for human destiny must always rest within our own conscious hands.",
          "zh": "然而，倫理學者提出告誡：人類絕不能將自身的道德辨別力置於「慣性自動導航」狀態。儘管人工智慧系統享有日益增長的操作自主權，人類命運的終極責任仍必須永遠掌握在我們自己自覺的雙手中。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What warning do ethical thinkers provide regarding 'autopilot'?",
          "qZh": "倫理學者針對「自動駕駛/無意識狀態」提出了什麼警告？",
          "options": [
            "A. Humans should never put their moral discernment on autopilot. (人類絕不應將道德辨別力置於無意識慣性中)",
            "B. Airplanes should completely ban automatic pilots.",
            "C. Robots should replace human judges in courtrooms.",
            "D. Factory machines must be operated by coal."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「ethical thinkers caution that human beings should never put their moral discernment on autopilot」。"
        }
      ]
    }
  },
  {
    "id": "chron",
    "name": "chron",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘神話時間之神與名詞「χρόνος」(khrónos)，意指「時間、時序 (time)」。",
    "originMeaning": "時間、時代、時序",
    "phonetic": "/krɑːn/",
    "icon": "⏱️",
    "color": "#E11D48",
    "summary": "記錄歷史演進、時間同步、長期慢性狀態與編年史的核心字根。",
    "words": [
      {
        "word": "chronology",
        "kk": "[krəˈnɑlədʒi]",
        "ipa": "/krəˈnɑːlədʒi/",
        "pos": "n.",
        "meaning": "年代學、年代順序、年表",
        "formula": {
          "parts": [
            {
              "text": "chron",
              "role": "root",
              "meaning": "時間 (希臘語 khrónos)"
            },
            {
              "text": "-ology",
              "role": "suffix",
              "meaning": "學問、研究 (希臘語 logos)"
            }
          ],
          "resultMeaning": "研究事件在時間長河中先後排列順序的學問 ➔「年代學、時序表」"
        },
        "sentence": "Archaeologists reconstructed the chronology of ancient Egyptian dynasties by cross-referencing astronomical records with radiocarbon dating.",
        "sentenceZh": "考古學家藉由將天文紀錄與放射性碳定年法相互參照，重建了古埃及各王朝的歷史年代順序表。",
        "grammar": {
          "pattern": "S + Vt + O + Means Participial Phrase (主詞 + 及物動詞 + 受詞 + 方式分詞介系詞片語)",
          "breakdown": [
            {
              "part": "Archaeologists",
              "role": "主詞 (Subject)",
              "note": "考古學家 (archaeo 古代 + logist 研究者)。"
            },
            {
              "part": "reconstructed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "過去式。"
            },
            {
              "part": "the chronology of ancient Egyptian dynasties",
              "role": "直接受詞 (Direct Object)",
              "note": "年代順序表。"
            },
            {
              "part": "by cross-referencing astronomical records with radiocarbon dating",
              "role": "方式介系詞片語 (By + Gerund)",
              "note": "cross-reference A with B (將 A 與 B 交互對照)。"
            }
          ],
          "keyPoints": [
            "【高階搭配片語】：by cross-referencing A with B (藉由將 A 與 B 相互對照)。",
            "【形容詞】：chronological (按時間順序排列的，如 in chronological order)。"
          ]
        }
      },
      {
        "word": "synchronize",
        "kk": "[ˈsɪŋkrəˌnaɪz]",
        "ipa": "/ˈsɪŋkrənaɪz/",
        "pos": "v.",
        "meaning": "使同步、同時發生",
        "formula": {
          "parts": [
            {
              "text": "syn-",
              "role": "prefix",
              "meaning": "共同、一起 (希臘語 syn)"
            },
            {
              "text": "chron",
              "role": "root",
              "meaning": "時間 (希臘語 khrónos)"
            },
            {
              "text": "-ize",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "使不同的鐘錶與動作歸攏在同一個時間點進行 ➔「使同步」"
        },
        "sentence": "Telecommunication satellites synchronize their atomic clocks to ensure millisecond GPS triangulation accuracy.",
        "sentenceZh": "電信衛星同步其原子鐘，以確保毫秒級的全球衛星定位三角測量精準度。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Telecommunication satellites",
              "role": "主詞 (Subject)",
              "note": "複數主詞 (tele- + communicate)。"
            },
            {
              "part": "synchronize",
              "role": "及物動詞 (Transitive Verb)",
              "note": "原形動詞。"
            },
            {
              "part": "their atomic clocks",
              "role": "直接受詞 (Direct Object)",
              "note": "原子鐘。"
            },
            {
              "part": "to ensure millisecond GPS triangulation accuracy",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "ensure 接著名詞片語 accuracy。"
            }
          ],
          "keyPoints": [
            "【縮寫常見語】：雲端備份常用的 sync 即為 synchronize 的簡寫！",
            "【反義詞】：asynchronous (非同步的；a- 無/非 + synchronize)。"
          ]
        }
      },
      {
        "word": "chronic",
        "kk": "[ˈkrɑnɪk]",
        "ipa": "/ˈkrɑːnɪk/",
        "pos": "adj.",
        "meaning": "慢性的、長期的、難以根除的",
        "formula": {
          "parts": [
            {
              "text": "chron",
              "role": "root",
              "meaning": "時間 (希臘語 khrónos)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "拖延拉扯很長時間難以痊癒的 ➔「慢性的、長期的」"
        },
        "sentence": "Urban sociologists warn that chronic traffic congestion inflicts staggering economic losses on developing metropolitan regions.",
        "sentenceZh": "都市社會學家提出警告，長期的交通擁堵會給發展中的大都會地區帶來驚人的經濟損失。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause (主詞 + 及物動詞 + That引導之受詞名詞子句)",
          "breakdown": [
            {
              "part": "Urban sociologists",
              "role": "主詞 (Subject)",
              "note": "都市社會學家。"
            },
            {
              "part": "warn",
              "role": "及物動詞 (Transitive Verb)",
              "note": "警告。"
            },
            {
              "part": "that chronic traffic congestion inflicts staggering economic losses on developing metropolitan regions",
              "role": "名詞子句受詞 (Noun Clause)",
              "note": "子句主詞 congestion，動詞 inflicts (inflict A on B 施加損失於某地)。"
            }
          ],
          "keyPoints": [
            "【固定搭配詞組】：inflict losses on... (對...造成損失)。",
            "【醫學對比】：chronic disease (慢性病) vs. acute disease (急性病)。"
          ]
        }
      },
      {
        "word": "chronicle",
        "kk": "[ˈkrɑnɪk!]",
        "ipa": "/ˈkrɑːnɪkl/",
        "pos": "n. / v.",
        "meaning": "編年史、歷史記事；(v.) 依時下記錄",
        "formula": {
          "parts": [
            {
              "text": "chron",
              "role": "root",
              "meaning": "時間 (time)"
            },
            {
              "text": "-icle",
              "role": "suffix",
              "meaning": "小事物、集合名詞字尾"
            }
          ],
          "resultMeaning": "按照時間順序忠實記錄下來之歷史記事 ➔「編年史」"
        },
        "sentence": "The medieval monks compiled a detailed chronicle that recorded both celestial phenomena and dynastic succession.",
        "sentenceZh": "中世紀僧侶編撰了一部詳盡的編年史，記載了天文異象與王朝更迭。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (that recorded...)",
          "breakdown": [
            {
              "part": "The medieval monks",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "compiled",
              "role": "及物動詞 (Verb)",
              "note": "意為「編撰、彙整」。"
            },
            {
              "part": "a detailed chronicle",
              "role": "受詞 (Object)",
              "note": "名詞片語。"
            },
            {
              "part": "that recorded both celestial phenomena and dynastic succession",
              "role": "關係子句 (修飾 chronicle)",
              "note": "that 作主格關代；both... and... 連接兩項名詞受詞。"
            }
          ],
          "keyPoints": [
            "【複數型態】：phenomena 為 phenomenon 的希臘語中性複數不規則變化！",
            "【文法結構】：both A and B 形成嚴格對等結構，此處為 celestial phenomena 與 dynastic succession 兩組名詞片語對等。"
          ]
        }
      },
      {
        "word": "anachronism",
        "kk": "[əˈnækrəˌnɪzəm]",
        "ipa": "/əˈnækrənɪzəm/",
        "pos": "n.",
        "meaning": "時代錯誤、年代倒置、不合時宜的人事物",
        "formula": {
          "parts": [
            {
              "text": "ana-",
              "role": "prefix",
              "meaning": "向後、倒退、相反 (back, backward)"
            },
            {
              "text": "chron",
              "role": "root",
              "meaning": "時間 (time)"
            },
            {
              "text": "-ism",
              "role": "suffix",
              "meaning": "名詞字尾 (state/practice)"
            }
          ],
          "resultMeaning": "時間軸倒置錯置、出現在不對年代的事物 ➔「時代錯誤、不合時宜的事物」"
        },
        "sentence": "Depicting wristwatches on Roman soldiers in historical epic films is a glaring anachronism criticized by historians.",
        "sentenceZh": "在歷史史詩電影中描繪羅馬士兵佩戴手錶，是遭受歷史學家嚴厲批評的顯眼時代錯誤。",
        "grammar": {
          "pattern": "S (Gerund Phrase) + Linking Verb (is) + SC (a glaring anachronism) + Participle Phrase (criticized by...)",
          "breakdown": [
            {
              "part": "Depicting wristwatches on Roman soldiers in historical epic films",
              "role": "動名詞片語主詞",
              "note": "單數動名詞作主詞。"
            },
            {
              "part": "is",
              "role": "連綴動詞 (Verb)",
              "note": "單數動詞。"
            },
            {
              "part": "a glaring anachronism",
              "role": "主詞補語 (Subject Complement)",
              "note": "glaring (刺眼的、顯而易見的)。"
            },
            {
              "part": "criticized by historians",
              "role": "過去分詞片語修飾 anachronism",
              "note": "criticized (受批評的)。"
            }
          ],
          "keyPoints": [
            "【形容詞派生】：anachronistic (時代倒置的、落伍的)。",
            "【文法動名詞主詞】：動名詞片語作主詞時，謂語動詞一律視為第三人稱單數 (is)。"
          ]
        }
      }
    ],
    "article": {
      "title": "Guardians of the River of Time: The Measure of Chronos",
      "titleZh": "時間之河的守護者：度量克羅諾斯之律",
      "intro": "希臘人敬畏時間神 Chronos，深知生命、歷史與文明皆流淌在時序 (chron) 的刻度之中。",
      "paragraphs": [
        {
          "en": "From the earliest stone sundials to atomic clocks ticking aboard satellites, humanity has continually striven to synchronize our fleeting lives with the rhythm of the cosmos.",
          "zh": "從最早期的石頭日晷到衛星上滴答運轉的原子鐘，人類不斷奮力將我們短暫的生命與宇宙的節奏同步。"
        },
        {
          "en": "By cataloging world history into an accurate chronology, historians preserve the memory of ancient empires. Even when modern societies struggle against chronic economic volatility, the lessons carved into time's chronicles guide us steadily forward.",
          "zh": "藉由將世界歷史編排入精確的年代學順序表中，歷史學家得以銘存古代帝國的記憶。即使當現代社會在長期的經濟波動中掙扎奮鬥，那些銘刻在時間編年史中的教訓依然引領著我們穩步向前。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What role does an accurate chronology play for historians?",
          "qZh": "精確的年代學為歷史學家發揮了什麼作用？",
          "options": [
            "A. Preserving the memory of ancient empires across time. (跨越時間長河銘存古代帝國的記憶)",
            "B. Predicting winning lottery tickets.",
            "C. Building mechanical water clocks.",
            "D. Erasing past historical records."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「By cataloging world history into an accurate chronology, historians preserve the memory of ancient empires」。"
        }
      ]
    }
  },
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
      },
      {
        "word": "auditory",
        "kk": "[ˈɔdəˌtori]",
        "ipa": "/ˈɔːdɪtɔːri/",
        "pos": "adj.",
        "meaning": "聽覺的、聽覺器官的",
        "formula": {
          "parts": [
            {
              "text": "audit (audi)",
              "role": "root",
              "meaning": "聽 (hear)"
            },
            {
              "text": "-ory",
              "role": "suffix",
              "meaning": "與...有關的形容詞字尾"
            }
          ],
          "resultMeaning": "與耳朵及聽覺神經傳導感知相關的 ➔「聽覺的」"
        },
        "sentence": "Prolonged exposure to heavy industrial machinery can inflict irreversible trauma on human auditory nerves.",
        "sentenceZh": "長期暴露在重工業機械噪音中，會對人類聽覺神經造成不可逆的損傷。",
        "grammar": {
          "pattern": "S + Modal + Vt + O + Prep Phrase (on...)",
          "breakdown": [
            {
              "part": "Prolonged exposure to heavy industrial machinery",
              "role": "主詞 (Subject)",
              "note": "動名詞衍生名詞 exposure + 介系詞 to。"
            },
            {
              "part": "can inflict",
              "role": "動詞片語 (Verb)",
              "note": "inflict damage/trauma on 常用動詞搭配。"
            },
            {
              "part": "irreversible trauma",
              "role": "受詞 (Object)",
              "note": "irreversible (不可逆的) 修飾 trauma (創傷)。"
            },
            {
              "part": "on human auditory nerves",
              "role": "受損對象介系詞片語",
              "note": "auditory 修飾 nerves。"
            }
          ],
          "keyPoints": [
            "【動詞搭配】：inflict damage/pain/trauma on someone/something 是表示「加害、造成痛苦/損害」之標準搭配詞。",
            "【字根字尾】：-ory 表感覺器官形容詞，如 auditory (聽覺的)、sensory (感官的)、olfactory (嗅覺的)。"
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
      },
      {
        "word": "microphone",
        "kk": "[ˈmaɪkrəˌfon]",
        "ipa": "/ˈmaɪkrəfoʊn/",
        "pos": "n.",
        "meaning": "麥克風、話筒、擴音拾音器",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小、細微 (small)"
            },
            {
              "text": "phone",
              "role": "root",
              "meaning": "聲音 (sound, voice)"
            }
          ],
          "resultMeaning": "將微弱細小的聲音放大拾取並轉為電信號的裝置 ➔「麥克風」"
        },
        "sentence": "The keynote speaker adjusted the sensitive microphone before delivering her groundbreaking lecture on quantum cryptography.",
        "sentenceZh": "主講人在發表關於量子密碼學的開創性演講之前，先調整了靈敏的麥克風。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase (before + V-ing)",
          "breakdown": [
            {
              "part": "The keynote speaker",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "adjusted",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "the sensitive microphone",
              "role": "受詞 (Object)",
              "note": "由 sensitive 修飾 microphone。"
            },
            {
              "part": "before delivering her groundbreaking lecture on quantum cryptography",
              "role": "時間介系詞片語",
              "note": "before 為介系詞，後接動名詞 delivering。"
            }
          ],
          "keyPoints": [
            "【介系詞 + V-ing】：before, after, while 後接動名詞是英文極常使用的時間緊縮結構。",
            "【演講搭配】：deliver a lecture / give a speech / make a presentation 皆為道地演講動詞搭配。"
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
      },
      {
        "word": "subscribe",
        "kk": "[səbˈskraɪb]",
        "ipa": "/səbˈskraɪb/",
        "pos": "v.",
        "meaning": "訂閱、簽署、認捐；(與 to 連用) 贊同",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方 (under, beneath)"
            },
            {
              "text": "scribe",
              "role": "root",
              "meaning": "書寫 (write)"
            }
          ],
          "resultMeaning": "在文件底部簽名以示確認同意 ➔「簽字同意、定期訂閱」"
        },
        "sentence": "Many university researchers subscribe to international peer-reviewed journals to stay abreast of scientific developments.",
        "sentenceZh": "許多大學研究人員訂閱國際同儕審查期刊，以跟上最新的科學發展脈動。",
        "grammar": {
          "pattern": "S + Vi + Prep Phrase (subscribe to...) + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "Many university researchers",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "subscribe to",
              "role": "不及物動詞片語",
              "note": "subscribe 必接介系詞 to。"
            },
            {
              "part": "international peer-reviewed journals",
              "role": "介系詞受詞",
              "note": "peer-reviewed 為複合形容詞「同儕審查的」。"
            },
            {
              "part": "to stay abreast of scientific developments",
              "role": "不定詞目的狀語",
              "note": "stay abreast of (與...並駕齊驅、掌握最新進展) 為高級片語。"
            }
          ],
          "keyPoints": [
            "【重要片語】：stay/keep abreast of something 意為「及時了解、跟上...的最新消息」。",
            "【介系詞搭配】：subscribe to a magazine (訂閱雜誌)；subscribe to a belief (贊同某種理念)。"
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
      },
      {
        "word": "polyester",
        "kk": "[ˌpɑlɪˈɛstɚ]",
        "ipa": "/ˌpɑːliˈɛstər/",
        "pos": "n.",
        "meaning": "聚酯纖維、多元酯",
        "formula": {
          "parts": [
            {
              "text": "poly-",
              "role": "prefix",
              "meaning": "多重、聚合 (many)"
            },
            {
              "text": "ester",
              "role": "base",
              "meaning": "酯類化合物 (chemical ester)"
            }
          ],
          "resultMeaning": "由許多酯基重覆聚合而成的高分子材料 ➔「聚酯纖維」"
        },
        "sentence": "Athletic sportswear is frequently woven from recycled polyester because the synthetic fabric efficiently wicks away moisture.",
        "sentenceZh": "運動服裝經常以再生聚酯纖維織成，因為這種合成面料能高效排汗排濕。",
        "grammar": {
          "pattern": "S + Passive Verb + Prep Phrase + Adv Clause of Reason (because...)",
          "breakdown": [
            {
              "part": "Athletic sportswear",
              "role": "主詞 (Subject)",
              "note": "集合名詞片語。"
            },
            {
              "part": "is frequently woven",
              "role": "被動態謂語",
              "note": "weave-wove-woven 不規則三態之現在被動式。"
            },
            {
              "part": "from recycled polyester",
              "role": "原料介系詞片語",
              "note": "be woven from 表「由...編織而成」。"
            },
            {
              "part": "because the synthetic fabric efficiently wicks away moisture",
              "role": "原因副詞子句",
              "note": "wick away 表「導出、抽走(汗水)」。"
            }
          ],
          "keyPoints": [
            "【不規則動詞】：weave (編織) 的三態變化為 weave - wove - woven。",
            "【機能運動俚語】：wick away moisture (排汗吸濕) 是戶外與運動機能紡織的核心專業術語。"
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
      },
      {
        "word": "beneficial",
        "kk": "[ˌbɛnəˈfɪʃəl]",
        "ipa": "/ˌbɛnɪˈfɪʃl/",
        "pos": "adj.",
        "meaning": "有益的、有幫助的、有利的",
        "formula": {
          "parts": [
            {
              "text": "bene-",
              "role": "prefix",
              "meaning": "好、善 (good, well)"
            },
            {
              "text": "fic (fac)",
              "role": "root",
              "meaning": "做、產生 (make, do)"
            },
            {
              "text": "-ial",
              "role": "suffix",
              "meaning": "形容詞字尾"
            }
          ],
          "resultMeaning": "產生良好成果或正面利益的 ➔「有益的」"
        },
        "sentence": "Regular cardiovascular exercise has proven overwhelmingly beneficial to both mental clarity and immune resilience.",
        "sentenceZh": "有規律的有氧心血管運動已被證實對心理清晰度與免疫防禦力皆極有益處。",
        "grammar": {
          "pattern": "S + Vt + Adj Compl (beneficial) + Prep Phrase (to both A and B)",
          "breakdown": [
            {
              "part": "Regular cardiovascular exercise",
              "role": "主詞 (Subject)",
              "note": "單數名詞片語。"
            },
            {
              "part": "has proven",
              "role": "連綴動詞 (Linking Verb)",
              "note": "prove 在此作連綴動詞「證明是...」，後接形容詞補語。"
            },
            {
              "part": "overwhelmingly beneficial",
              "role": "主詞補語 (Subject Complement)",
              "note": "副詞 overwhelmingly 修飾形容詞 beneficial。"
            },
            {
              "part": "to both mental clarity and immune resilience",
              "role": "受惠對象介系詞片語",
              "note": "beneficial to... 為固定搭配；both... and... 連接兩名詞。"
            }
          ],
          "keyPoints": [
            "【連綴動詞用法】：prove / prove to be + Adj.，表「事實證明是...」，後接形容詞作補語。",
            "【介系詞搭配】：beneficial 後習慣接介系詞 to (如 beneficial to health)，不可混用 for。"
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
      },
      {
        "word": "transmit",
        "kk": "[trænsˈmɪt]",
        "ipa": "/trænzˈmɪt/",
        "pos": "v.",
        "meaning": "傳輸、播送、傳染",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "穿越、跨越 (across)"
            },
            {
              "text": "mit",
              "role": "root",
              "meaning": "發送、送出 (send)"
            }
          ],
          "resultMeaning": "將信號或病原跨越空間發送至另一端 ➔「傳輸、傳染」"
        },
        "sentence": "Fiber-optic cables can transmit massive quantities of encrypted digital data across continents in mere milliseconds.",
        "sentenceZh": "光纖電纜能在短短數毫秒內跨越大洲傳輸海量加密數位數據。",
        "grammar": {
          "pattern": "S + Modal + Vt + O + Prep Phrase + Prep Phrase",
          "breakdown": [
            {
              "part": "Fiber-optic cables",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語「光纖電纜」。"
            },
            {
              "part": "can transmit",
              "role": "動詞片語 (Verb)",
              "note": "情態助動詞 can + 原形動詞 transmit。"
            },
            {
              "part": "massive quantities of encrypted digital data",
              "role": "受詞 (Object)",
              "note": "encrypted 為過去分詞作形容詞「加密的」。"
            },
            {
              "part": "across continents",
              "role": "空間介系詞片語",
              "note": "表空間跨越。"
            },
            {
              "part": "in mere milliseconds",
              "role": "時間介系詞片語",
              "note": "mere (僅僅、只不過) 強調時間極短。"
            }
          ],
          "keyPoints": [
            "【雙寫字母規則】：transmit 過去式與現在分詞需雙寫 t：transmitted, transmitting。",
            "【字根字首】：trans- (跨越) + mit (送出)，同根字有 emit (發出)、admit (承認)、submit (提交)。"
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
  },
  {
    "id": "vis",
    "name": "vis / vid",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「videre」(看見、注視)，過去分詞形為 visum。",
    "originMeaning": "看、看見、視覺、顯現",
    "phonetic": "/vɪz/ 或 /vɪd/",
    "icon": "👁️",
    "color": "#0284C7",
    "summary": "涵蓋視覺影像、遠見規劃、監督指導、明證證據與提供預備。",
    "words": [
      {
        "word": "visible",
        "kk": "[ˈvɪzəb!]",
        "ipa": "/ˈvɪzəbl/",
        "pos": "adj.",
        "meaning": "可看見的、明顯的、能注意到的",
        "formula": {
          "parts": [
            {
              "text": "vis",
              "role": "root",
              "meaning": "看 (拉丁語 videre)"
            },
            {
              "text": "-ible",
              "role": "suffix",
              "meaning": "能...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "眼睛能夠清楚看見的 ➔「可見的、明顯的」"
        },
        "sentence": "The distant mountain peaks became clearly visible once the dense morning fog dispersed.",
        "sentenceZh": "濃密的晨霧一旦散去，遠方的山峰便清晰可見。",
        "grammar": {
          "pattern": "S + Linking Verb + Adv + Predicate Adjective + Time Clause (主詞 + 連綴動詞 + 副詞 + 形容詞補語 + 時間子句)",
          "breakdown": [
            {
              "part": "The distant mountain peaks",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "became",
              "role": "連綴動詞 (Linking Verb)",
              "note": "表狀態轉變。"
            },
            {
              "part": "clearly visible",
              "role": "主詞補語 (Subject Complement)",
              "note": "clearly (清晰地) 修飾 visible。"
            },
            {
              "part": "once the dense morning fog dispersed",
              "role": "時間副詞子句 (Time Clause)",
              "note": "once 作從屬連接詞 (一旦...就...)；dispersed (消散)。"
            }
          ],
          "keyPoints": [
            "【連接詞用法】：once 引導時間副詞子句表示「一旦發生某事」。",
            "【反義詞】：invisible (隱形的、看不見的；in- 不 + visible)。"
          ]
        }
      },
      {
        "word": "supervise",
        "kk": "[ˈsupɚˌvaɪz]",
        "ipa": "/ˈsuːpərvaɪz/",
        "pos": "v.",
        "meaning": "監督、管理、指導",
        "formula": {
          "parts": [
            {
              "text": "super-",
              "role": "prefix",
              "meaning": "在上方 (拉丁語 super)"
            },
            {
              "text": "vise",
              "role": "root",
              "meaning": "看 (拉丁語 videre)"
            }
          ],
          "resultMeaning": "由居高臨下的上方俯視監看全場進度 ➔「監督、管理」"
        },
        "sentence": "Certified project managers supervise construction operations on-site to enforce rigorous occupational safety protocols.",
        "sentenceZh": "合格認證的專案經理在現場監督施工運作，以落實嚴格的職業安全規範。",
        "grammar": {
          "pattern": "S + Vt + O + Locative Adverbial + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 地點狀詞 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Certified project managers",
              "role": "主詞 (Subject)",
              "note": "合格專案經理 (certified 為過去分詞形容詞)。"
            },
            {
              "part": "supervise",
              "role": "及物動詞 (Transitive Verb)",
              "note": "現在式動詞。"
            },
            {
              "part": "construction operations",
              "role": "受詞 (Direct Object)",
              "note": "施工營造作業。"
            },
            {
              "part": "on-site",
              "role": "地點副詞 (Locative Adverb)",
              "note": "在現場地。"
            },
            {
              "part": "to enforce rigorous occupational safety protocols",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "enforce (強制執行落實)；rigorous (嚴密的)。"
            }
          ],
          "keyPoints": [
            "【前綴空間涵義】：super- (高處/上方) + videre (注視) = 從上俯視 ➔ 監督。",
            "【衍生名詞】：supervisor (主管、指導老師)、supervision (監督工作)。"
          ]
        }
      },
      {
        "word": "evidence",
        "kk": "[ˈɛvədəns]",
        "ipa": "/ˈevɪdəns/",
        "pos": "n.",
        "meaning": "證據、明證、跡象",
        "formula": {
          "parts": [
            {
              "text": "e-",
              "role": "prefix",
              "meaning": "出、向外 (拉丁語 ex-)"
            },
            {
              "text": "vid",
              "role": "root",
              "meaning": "看 (拉丁語 videre)"
            },
            {
              "text": "-ence",
              "role": "suffix",
              "meaning": "狀態、名詞字尾"
            }
          ],
          "resultMeaning": "擺到眼前讓人看得清清楚楚的客觀事實 ➔「證據、明證」"
        },
        "sentence": "Forensic scientists uncovered conclusive genetic evidence that linked the prime suspect to the crime scene.",
        "sentenceZh": "鑑識科學家發現了決定性的基因證據，將第一嫌疑犯與犯罪現場緊密連結在一起。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 關係子句)",
          "breakdown": [
            {
              "part": "Forensic scientists",
              "role": "主詞 (Subject)",
              "note": "鑑識科學家。"
            },
            {
              "part": "uncovered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "揭露、發現。"
            },
            {
              "part": "conclusive genetic evidence",
              "role": "直接受詞 (Direct Object)",
              "note": "conclusive (決定性的、確鑿的)；evidence (不可數名詞)。"
            },
            {
              "part": "that linked the prime suspect to the crime scene",
              "role": "關係子句 (Relative Clause)",
              "note": "link A to B (將 A 連結至 B)；that 為主格關代修飾 evidence。"
            }
          ],
          "keyPoints": [
            "【名詞可數性】：evidence 為不可數名詞 (uncountable)，一條證據宜寫作 a piece of evidence。",
            "【動詞短語】：link / connect A to B (把 A 與 B 連繫起來)。"
          ]
        }
      },
      {
        "word": "provide",
        "kk": "[prəˈvaɪd]",
        "ipa": "/prəˈvaɪd/",
        "pos": "v.",
        "meaning": "提供、供給、預備",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前、預先 (拉丁語 pro)"
            },
            {
              "text": "vide",
              "role": "root",
              "meaning": "看 (拉丁語 videre)"
            }
          ],
          "resultMeaning": "預先向前看見需求而預先作好準備 ➔「提供、預備」"
        },
        "sentence": "The university library provides students with access to peer-reviewed scholarly journals across the globe.",
        "sentenceZh": "大學圖書館為學生提供獲取全球同儕審查學術期刊的查閱途徑。",
        "grammar": {
          "pattern": "S + Vt + O1 + with + O2 (主詞 + 及物動詞 + 接收者受詞 + 介系詞片語)",
          "breakdown": [
            {
              "part": "The university library",
              "role": "主詞 (Subject)",
              "note": "大學圖書館。"
            },
            {
              "part": "provides",
              "role": "及物動詞 (Transitive Verb)",
              "note": "第三人稱單數現在式。"
            },
            {
              "part": "students",
              "role": "受詞 (Object)",
              "note": "提供對象。"
            },
            {
              "part": "with access to peer-reviewed scholarly journals across the globe",
              "role": "介系詞受詞片語 (Prepositional Phrase)",
              "note": "provide somebody with something (提供某人某物)；access to (取得...的權限)。"
            }
          ],
          "keyPoints": [
            "【固定句型雙型態】：provide somebody with something = provide something for/to somebody。",
            "【名詞形式】：provision (供應品、條款)、provider (供應商)。"
          ]
        }
      },
      {
        "word": "vision",
        "kk": "[ˈvɪʒən]",
        "ipa": "/ˈvɪʒn/",
        "pos": "n.",
        "meaning": "視力、眼光、遠見、幻象",
        "formula": {
          "parts": [
            {
              "text": "vis",
              "role": "root",
              "meaning": "看 (see)"
            },
            {
              "text": "-ion",
              "role": "suffix",
              "meaning": "名詞字尾 (state/act)"
            }
          ],
          "resultMeaning": "看見世界的能力與超前構想未來的遠見 ➔「視力、遠見」"
        },
        "sentence": "A visionary leader possesses the remarkable vision to foresee technological disruptions decades before they materialize.",
        "sentenceZh": "有遠見的領導者擁有非凡的洞察力，能在技術變革實現的數十年之前便預見其發生。",
        "grammar": {
          "pattern": "S + Vt + O (the remarkable vision) + Infinitive Phrase (to foresee...)",
          "breakdown": [
            {
              "part": "A visionary leader",
              "role": "主詞 (Subject)",
              "note": "visionary 作形容詞「具前瞻遠見的」。"
            },
            {
              "part": "possesses",
              "role": "及物動詞 (Verb)",
              "note": "意為「擁有、具備」。"
            },
            {
              "part": "the remarkable vision",
              "role": "直接受詞 (Object)",
              "note": "remarkable (非凡的) 修飾 vision。"
            },
            {
              "part": "to foresee technological disruptions",
              "role": "不定詞形容詞片語",
              "note": "修飾 vision 之內涵；foresee 接 disruptions。"
            },
            {
              "part": "decades before they materialize",
              "role": "時間副詞片語",
              "note": "decades 修飾介副詞 before；materialize 意為「成真、具體化」。"
            }
          ],
          "keyPoints": [
            "【構詞派生】：vision (遠見) ➔ visionary (具遠見者/有遠見的) ➔ envision (設想、展望)。",
            "【時間修飾語】：[時間名詞複數] + before / after 表示「在...之前的數個單位時間」，如 decades before。"
          ]
        }
      },
      {
        "word": "revise",
        "kk": "[rɪˈvaɪz]",
        "ipa": "/rɪˈvaɪz/",
        "pos": "v.",
        "meaning": "修訂、修正、複習",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再、重新 (again)"
            },
            {
              "text": "vise (vis)",
              "role": "root",
              "meaning": "看、審視 (look, see)"
            }
          ],
          "resultMeaning": "重新仔細檢視並修正內容 ➔「修訂、修改」"
        },
        "sentence": "The academic committee instructed the doctoral candidate to revise her dissertation in light of the new empirical findings.",
        "sentenceZh": "學術委員會指示該博士候選人根據最新的實證研究發現來修訂她的論文。",
        "grammar": {
          "pattern": "S + Vt + O + to-V (受詞補語) + Prep Phrase",
          "breakdown": [
            {
              "part": "The academic committee",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "instructed",
              "role": "及物動詞 (Verb)",
              "note": "instruct someone to do something 句型。"
            },
            {
              "part": "the doctoral candidate",
              "role": "受詞 (Object)",
              "note": "「博士候選人」。"
            },
            {
              "part": "to revise her dissertation",
              "role": "受詞補語 (Objective Complement)",
              "note": "不定詞作補語。"
            },
            {
              "part": "in light of the new empirical findings",
              "role": "介系詞片語狀語",
              "note": "in light of 表示「鑑於、根據」。"
            }
          ],
          "keyPoints": [
            "【重要介系詞片語】：in light of something 表「鑑於、有鑑於、考量到...」。",
            "【動詞句型】：instruct / advise / urge + O + to V (指示/建議/敦促某人做某事)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Architecture of Sight and Insight: From Vision to Provision",
      "titleZh": "洞見之光：從看見到預備的生命視野",
      "intro": "「看見 (videre)」不僅是眼球接收光源，更是洞悉未來的智慧，讓我們在今日為明日提供 (provide) 庇護。",
      "paragraphs": [
        {
          "en": "Without the courage to observe reality with unclouded eyes, societies become blind to accumulating injustices. Conclusive evidence must always guide legal verdicts, ensuring that truth remains visible to all citizens.",
          "zh": "若沒有以澄澈眼光審視現實的勇氣，社會對積累的不公將變得視而不見。確鑿的證據必須始終指引法律判決，確保真理對全體公民清晰可見。"
        },
        {
          "en": "True statesmen supervise institutions with foresight, providing sustainable resources for generations not yet born, proving that the ancient root 'vis' is the bedrock of enduring leadership.",
          "zh": "真正的政治家以遠見監督體制運作，為尚未出生的後代提供永續資源，證明了古老的字根「vis」正是持久領導力的穩固基石。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What must guide legal verdicts according to the article?",
          "qZh": "根據文章，何者必須指引法律判決？",
          "options": [
            "A. Conclusive evidence to ensure visible truth. (確鑿的證據以確保真理可見)",
            "B. Arbitrary rumors from social media.",
            "C. Financial donations to politicians.",
            "D. Ancient astrological horoscopes."
          ],
          "answer": 0,
          "explanation": "文中第一段指出「Conclusive evidence must always guide legal verdicts, ensuring that truth remains visible to all citizens」。"
        }
      ]
    }
  },
  {
    "id": "geo",
    "name": "geo",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「γῆ」(gê) 或「γαῖα」(gaîa)，意為「大地、地球、土地」。",
    "originMeaning": "大地、地球、土地、地質",
    "phonetic": "/ˈdʒiːoʊ/",
    "icon": "🌍",
    "color": "#15803D",
    "summary": "涵蓋地球科學、地形地貌、測量幾何學與地緣政治的核心字根。",
    "words": [
      {
        "word": "geology",
        "kk": "[dʒɪˈɑlədʒi]",
        "ipa": "/dʒiˈɑːlədʒi/",
        "pos": "n.",
        "meaning": "地質學、地質結構",
        "formula": {
          "parts": [
            {
              "text": "geo-",
              "role": "root",
              "meaning": "地球、大地 (希臘語 gê)"
            },
            {
              "text": "-logy",
              "role": "suffix",
              "meaning": "學問、研究 (希臘語 logos)"
            }
          ],
          "resultMeaning": "研究地球物質構成與岩層演變歷史的科學 ➔「地質學」"
        },
        "sentence": "Field researchers study the dynamic geology of the volcanic island to anticipate catastrophic tectonic shifts.",
        "sentenceZh": "野外研究人員研究該火山島活躍的地質結構，以預測災難性的板塊位移。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Field researchers",
              "role": "主詞 (Subject)",
              "note": "野外研究人員。"
            },
            {
              "part": "study",
              "role": "及物動詞 (Transitive Verb)",
              "note": "研究調查。"
            },
            {
              "part": "the dynamic geology of the volcanic island",
              "role": "直接受詞 (Direct Object)",
              "note": "dynamic (動態活耀的)；volcanic island (火山島)。"
            },
            {
              "part": "to anticipate catastrophic tectonic shifts",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "anticipate (預期)；catastrophic (災難性的)；tectonic (板塊構造的)。"
            }
          ],
          "keyPoints": [
            "【專業術語】：tectonic shifts (地殼構造移動)、plate tectonics (板塊構造學)。",
            "【專家衍生】：geologist (地質學家)。"
          ]
        }
      },
      {
        "word": "geometry",
        "kk": "[dʒɪˈɑmətri]",
        "ipa": "/dʒiˈɑːmətri/",
        "pos": "n.",
        "meaning": "幾何學、幾何圖形",
        "formula": {
          "parts": [
            {
              "text": "geo-",
              "role": "root",
              "meaning": "土地、大地 (希臘語 gê)"
            },
            {
              "text": "metry",
              "role": "root/suffix",
              "meaning": "測量 (希臘語 metron 衡量)"
            }
          ],
          "resultMeaning": "源自古埃及每年尼羅河氾濫後重新劃分測量土地的學問 ➔「幾何學」"
        },
        "sentence": "Ancient Egyptian architects mastered applied geometry to align the colossal pyramid foundations with celestial constellations.",
        "sentenceZh": "古埃及建築師精通應用幾何學，將宏偉的金字塔地基與天體星座精準對齊。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Ancient Egyptian architects",
              "role": "主詞 (Subject)",
              "note": "古埃及建築師。"
            },
            {
              "part": "mastered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "精通掌握。"
            },
            {
              "part": "applied geometry",
              "role": "直接受詞 (Direct Object)",
              "note": "應用幾何學。"
            },
            {
              "part": "to align the colossal pyramid foundations with celestial constellations",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "align A with B (使 A 與 B 對齊相符)；colossal (巨大的)；celestial (天空的)。"
            }
          ],
          "keyPoints": [
            "【動詞短語搭配】：align A with B (使 A 與 B 對齊/一致)。",
            "【詞源歷史趣味】：幾何學 (geometry) 最初就是「丈量土地 (Earth measurement)」的技術！"
          ]
        }
      },
      {
        "word": "geothermal",
        "kk": "[ˌdʒioˈθɝm!]",
        "ipa": "/ˌdʒiːoʊˈθɜːrml/",
        "pos": "adj.",
        "meaning": "地熱的、利用地熱產生的",
        "formula": {
          "parts": [
            {
              "text": "geo-",
              "role": "root",
              "meaning": "地球、地層 (希臘語 gê)"
            },
            {
              "text": "therm",
              "role": "root",
              "meaning": "熱 (希臘語 thermē)"
            },
            {
              "text": "-al",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "蘊藏於地殼內部深處由地球內部產生的熱能 ➔「地熱的」"
        },
        "sentence": "Iceland harnesses geothermal energy from subterranean reservoirs to supply carbon-neutral electricity to entire communities.",
        "sentenceZh": "冰島利用地下熱水庫的地熱能源，為整個社區供應碳中和的電力。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 來源片語 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Iceland",
              "role": "主詞 (Subject)",
              "note": "冰島 (專有名詞)。"
            },
            {
              "part": "harnesses",
              "role": "及物動詞 (Transitive Verb)",
              "note": "harness (善加利用、治理駕馭)。"
            },
            {
              "part": "geothermal energy",
              "role": "直接受詞 (Direct Object)",
              "note": "地熱能。"
            },
            {
              "part": "from subterranean reservoirs",
              "role": "來源介系詞片語 (Source Phrase)",
              "note": "subterranean (地下的；sub 下 + terra 土地)。"
            },
            {
              "part": "to supply carbon-neutral electricity to entire communities",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "supply A to B (供應 A 給 B)；carbon-neutral (碳中和的)。"
            }
          ],
          "keyPoints": [
            "【雙重希臘詞根融合】：geo (大地) + therm (熱)。",
            "【高分動詞用法】：harness energy (利用能源、開發利用自然力量)。"
          ]
        }
      },
      {
        "word": "geography",
        "kk": "[dʒɪˈɑgrəfɪ]",
        "ipa": "/dʒiˈɑːɡrəfi/",
        "pos": "n.",
        "meaning": "地理學、地勢、地形",
        "formula": {
          "parts": [
            {
              "text": "geo-",
              "role": "prefix",
              "meaning": "大地、地球 (Earth)"
            },
            {
              "text": "graphy",
              "role": "root",
              "meaning": "描繪、記述 (writing, description)"
            }
          ],
          "resultMeaning": "對地球表面山川景貌與人文分布的系統記述 ➔「地理學」"
        },
        "sentence": "Physical geography examines how atmospheric currents and tectonic collisions sculpt continental topography over geological epochs.",
        "sentenceZh": "自然地理學探討大氣環流與板塊碰撞如何在漫長的地質時代中雕塑大陸地形。",
        "grammar": {
          "pattern": "S + Vt + Wh- Noun Clause (how...)",
          "breakdown": [
            {
              "part": "Physical geography",
              "role": "主詞 (Subject)",
              "note": "「自然地理學」。"
            },
            {
              "part": "examines",
              "role": "及物動詞 (Verb)",
              "note": "第三人稱單數現在式。"
            },
            {
              "part": "how atmospheric currents and tectonic collisions sculpt continental topography",
              "role": "受詞名詞子句",
              "note": "how 引導子句，sculpt 為謂語動詞。"
            },
            {
              "part": "over geological epochs",
              "role": "時間介系詞片語",
              "note": "epoch 意為「漫長地質紀元」。"
            }
          ],
          "keyPoints": [
            "【動詞生動性】：sculpt 本義為「雕刻」，在此借代為大自然營力「雕琢、塑造」地形。",
            "【學科字尾】：-graphy 多表「記述性學科」，如 geography, oceanography, topography。"
          ]
        }
      },
      {
        "word": "geopolitics",
        "kk": "[ˌdʒiəˈpɑlətɪks]",
        "ipa": "/ˌdʒiːoʊˈpɑːlətɪks/",
        "pos": "n.",
        "meaning": "地緣政治學、地緣政治局勢",
        "formula": {
          "parts": [
            {
              "text": "geo-",
              "role": "prefix",
              "meaning": "地球、地理 (Earth)"
            },
            {
              "text": "politics",
              "role": "base",
              "meaning": "政治、政局 (affairs of state)"
            }
          ],
          "resultMeaning": "探討地理位置與空間資源對國際政治權力競逐之影響 ➔「地緣政治學」"
        },
        "sentence": "Control over strategic maritime chokepoints remains a foundational pillar of global geopolitics and naval strategy.",
        "sentenceZh": "對戰略海上交通咽喉的掌控，始終是全球地緣政治與海軍戰略的基石。",
        "grammar": {
          "pattern": "S (Control over...) + Linking Verb (remains) + SC (a foundational pillar)",
          "breakdown": [
            {
              "part": "Control over strategic maritime chokepoints",
              "role": "主詞片語 (Subject)",
              "note": "chokepoint 意為「咽喉點、戰略隘口」。"
            },
            {
              "part": "remains",
              "role": "連綴動詞 (Linking Verb)",
              "note": "表「持續是、仍然是」。"
            },
            {
              "part": "a foundational pillar",
              "role": "主詞補語 (Subject Complement)",
              "note": "名詞補語，比喻核心柱石。"
            },
            {
              "part": "of global geopolitics and naval strategy",
              "role": "所有格介系詞片語",
              "note": "修飾 pillar。"
            }
          ],
          "keyPoints": [
            "【名詞單複數】：geopolitics 形式雖有 -s，但作學科或單一現象時視為「單數名詞」！",
            "【連綴動詞】：remain + Noun / remain + Adj.，表「依然保持為...」。"
          ]
        }
      }
    ],
    "article": {
      "title": "Voices of the Living Earth: The Dominion of Geo",
      "titleZh": "大地的脈動：地靈之源的探索",
      "intro": "地球 (geo-) 不只是一顆旋轉的行星，更是一部由岩石、地熱與幾何線條織就的浩瀚史書。",
      "paragraphs": [
        {
          "en": "From early Egyptian surveyors using basic geometry to retrace boundary lines after the Nile floods, to modern volcanologists exploring geothermal geysers, humanity has always sought to decipher our relationship with planet Earth.",
          "zh": "從早期埃及土地測量員在尼羅河氾濫後用基礎幾何學重新劃分邊界，到現代火山學家探索噴薄的地熱間歇泉，人類始終在努力解讀自身與這顆地球的深刻連結。"
        },
        {
          "en": "Understanding the planetary dynamics revealed through geology empowers modern engineers to build resilient infrastructure, proving that by respecting the laws of 'geo', we safeguard our shared planetary civilization.",
          "zh": "理解地質學所揭示的行星動態，能賦予現代工程師打造堅韌基礎設施的智慧，證明了唯有崇尚「大地 (geo)」的自然規律，我們才能守護共同的行星文明。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "How does understanding geology help modern engineers?",
          "qZh": "理解地質學如何幫助現代工程師？",
          "options": [
            "A. It empowers them to build resilient infrastructure. (賦予他們打造堅韌基礎設施的能力)",
            "B. It teaches them how to fly airplanes.",
            "C. It eliminates all winter blizzards.",
            "D. It replaces steel with plastic."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「Understanding the planetary dynamics revealed through geology empowers modern engineers to build resilient infrastructure」。"
        }
      ]
    }
  },
  {
    "id": "hydr",
    "name": "hydr / hydro",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「ὕδωρ」(húdōr)，原意為「水 (water)」。",
    "originMeaning": "水、液體、水力",
    "phonetic": "/ˈhaɪdrə/ 或 /ˈhaɪdroʊ/",
    "icon": "💧",
    "color": "#06B6D4",
    "summary": "涵蓋水力發電、脫水與補水醫學、氫氣元素與液壓工程的核心字根。",
    "words": [
      {
        "word": "hydrogen",
        "kk": "[ˈhaɪdrədʒən]",
        "ipa": "/ˈhaɪdrədʒən/",
        "pos": "n.",
        "meaning": "氫氣、氫元素 (H)",
        "formula": {
          "parts": [
            {
              "text": "hydro-",
              "role": "root",
              "meaning": "水 (希臘語 húdōr)"
            },
            {
              "text": "-gen",
              "role": "root",
              "meaning": "產生、生成 (希臘語 gennaō)"
            }
          ],
          "resultMeaning": "燃燒後與氧結合會生成水的一號化學元素 ➔「氫、氫氣」"
        },
        "sentence": "Green hydrogen produced via water electrolysis holds immense promise as a zero-emission transport fuel.",
        "sentenceZh": "透過水電解製造的綠氫，作為零排放交通燃料具有無比巨大的應用前景。",
        "grammar": {
          "pattern": "S + Past Participle Modifier + Vt + O + as-Phrase (主詞 + 過去分詞片語後位修飾 + 及物動詞 + 受詞 + 身分介系詞片語)",
          "breakdown": [
            {
              "part": "Green hydrogen",
              "role": "主詞 (Subject)",
              "note": "綠色氫能。"
            },
            {
              "part": "produced via water electrolysis",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "修飾 hydrogen，相當於 which is produced via..."
            },
            {
              "part": "holds",
              "role": "及物動詞 (Transitive Verb)",
              "note": "hold promise (大有希望/潛力)。"
            },
            {
              "part": "immense promise",
              "role": "直接受詞 (Direct Object)",
              "note": "immense (巨大的) 修飾 promise (前景潛力)。"
            },
            {
              "part": "as a zero-emission transport fuel",
              "role": "身分介系詞片語 (Prepositional Phrase)",
              "note": "as 表作為角色。"
            }
          ],
          "keyPoints": [
            "【慣用語搭配】：hold promise (展現希望/具有良好前景)。",
            "【雙重希臘字根】：hydro (水) + gen (產生) = 產生水者。"
          ]
        }
      },
      {
        "word": "dehydrate",
        "kk": "[diˈhaɪdret]",
        "ipa": "/diːˈhaɪdreɪt/",
        "pos": "v.",
        "meaning": "脫水、使乾燥、使失去水分",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "去除、分離 (拉丁語 de-)"
            },
            {
              "text": "hydr",
              "role": "root",
              "meaning": "水 (希臘語 húdōr)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "將物質或人體內部的水分徹底抽乾去除 ➔「脫水」"
        },
        "sentence": "Marathon athletes must hydrate regularly because severe dehydration impairs cardiovascular stamina and cognitive focus.",
        "sentenceZh": "馬拉松運動員必須定期補充水分，因為嚴重的脫水會損害心血管耐力與認知專注度。",
        "grammar": {
          "pattern": "S + Modal + Vi + Adv + Reason Adverbial Clause (主詞 + 助動詞 + 不及物動詞 + 副詞 + 原因副詞子句)",
          "breakdown": [
            {
              "part": "Marathon athletes",
              "role": "主詞 (Subject)",
              "note": "馬拉松運動員。"
            },
            {
              "part": "must hydrate",
              "role": "謂語 (Modal Predicate)",
              "note": "hydrate (補水，不及物動詞)。"
            },
            {
              "part": "regularly",
              "role": "頻率副詞 (Adverb)",
              "note": "規律地。"
            },
            {
              "part": "because severe dehydration impairs cardiovascular stamina and cognitive focus",
              "role": "原因子句 (Clause of Reason)",
              "note": "dehydration (脫水名詞主詞)；impairs (損害)；stamina (耐力)；focus (專注力)。"
            }
          ],
          "keyPoints": [
            "【成對反義】：hydrate (補水) vs. dehydrate (脫水；de- 去除)。",
            "【動詞短語】：impair stamina and focus (損及耐力與專注度)。"
          ]
        }
      },
      {
        "word": "hydraulic",
        "kk": "[haɪˈdrɔlɪk]",
        "ipa": "/haɪˈdrɔːlɪk/",
        "pos": "adj.",
        "meaning": "液壓的、水力的、水壓驅動的",
        "formula": {
          "parts": [
            {
              "text": "hydr",
              "role": "root",
              "meaning": "水、液體 (希臘語 húdōr)"
            },
            {
              "text": "aul",
              "role": "root",
              "meaning": "管、笛 (希臘語 aulos 水管/風管)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "藉由管路中液體壓力進行傳導傳動的 ➔「液壓的、水力的」"
        },
        "sentence": "Heavy earthmoving excavators rely on high-pressure hydraulic cylinders to lift massive boulders with effortless precision.",
        "sentenceZh": "重型土方挖掘機依靠高壓液壓缸，以輕鬆精準的姿態舉起巨大的巨石。",
        "grammar": {
          "pattern": "S + Vi + Prep Phrase + Infinitive of Purpose (主詞 + 不及物動詞 + 介系詞受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Heavy earthmoving excavators",
              "role": "主詞 (Subject)",
              "note": "重型挖掘機。"
            },
            {
              "part": "rely on",
              "role": "動詞片語 (Phrasal Verb)",
              "note": "依靠、倚仗。"
            },
            {
              "part": "high-pressure hydraulic cylinders",
              "role": "受詞 (Object of Prep)",
              "note": "高壓液壓汽缸。"
            },
            {
              "part": "to lift massive boulders with effortless precision",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "lift (舉起)；massive boulders (巨大滾石)；with precision (精確地)。"
            }
          ],
          "keyPoints": [
            "【工程機械術語】：hydraulic brakes (液壓煞車)、hydraulic press (液壓機)。",
            "【介系詞伴隨方式】：with effortless precision (輕鬆而精準地)。"
          ]
        }
      },
      {
        "word": "hydrant",
        "kk": "[ˈhaɪdrənt]",
        "ipa": "/ˈhaɪdrənt/",
        "pos": "n.",
        "meaning": "消防栓、消防龍頭、水龍頭",
        "formula": {
          "parts": [
            {
              "text": "hydr-",
              "role": "root",
              "meaning": "水 (water)"
            },
            {
              "text": "-ant",
              "role": "suffix",
              "meaning": "器械、用具之名詞字尾"
            }
          ],
          "resultMeaning": "自地下供水主管路引出高壓水源的器具 ➔「消防栓」"
        },
        "sentence": "Municipal ordinances strictly prohibit motorists from parking within fifteen feet of any active fire hydrant.",
        "sentenceZh": "市政法規嚴禁汽車駕駛人將車輛停放在任何有效消防栓十五英尺之內。",
        "grammar": {
          "pattern": "S + Adv + Vt (prohibit) + O + Prep Phrase (from V-ing)",
          "breakdown": [
            {
              "part": "Municipal ordinances",
              "role": "主詞 (Subject)",
              "note": "ordinance 意為「市政法令、規章」。"
            },
            {
              "part": "strictly",
              "role": "程度副詞",
              "note": "修飾 prohibit。"
            },
            {
              "part": "prohibit",
              "role": "及物動詞 (Verb)",
              "note": "prohibit A from B 句型。"
            },
            {
              "part": "motorists",
              "role": "直接受詞 (Object)",
              "note": "意指機動車輛駕駛人。"
            },
            {
              "part": "from parking within fifteen feet of any active fire hydrant",
              "role": "介系詞片語",
              "note": "from + 動名詞 parking。"
            }
          ],
          "keyPoints": [
            "【禁制動詞】：prohibit / prevent / ban / stop / forbid (forbid + to V，其餘常接 from + V-ing)。",
            "【距離介系詞】：within fifteen feet of... 表「在距離...15英尺之範圍內」。"
          ]
        }
      },
      {
        "word": "hydroelectric",
        "kk": "[ˌhaɪdroɪˈlɛktrɪk]",
        "ipa": "/ˌhaɪdroʊɪˈlɛktrɪk/",
        "pos": "adj.",
        "meaning": "水力發電的",
        "formula": {
          "parts": [
            {
              "text": "hydro-",
              "role": "prefix",
              "meaning": "水 (water)"
            },
            {
              "text": "electric",
              "role": "base",
              "meaning": "電力的 (electricity)"
            }
          ],
          "resultMeaning": "利用高處水流落差之重力位能發電的 ➔「水力發電的」"
        },
        "sentence": "The gigantic concrete dam generates clean hydroelectric energy by channeling rushing river currents through massive subterranean turbines.",
        "sentenceZh": "這座巨大的混凝土水壩藉由引導奔騰的河水穿過龐大的地下渦輪機，來產生潔淨的水力發電能源。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase of Means (by channeling...)",
          "breakdown": [
            {
              "part": "The gigantic concrete dam",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "generates",
              "role": "及物動詞 (Verb)",
              "note": "第三人稱單數。"
            },
            {
              "part": "clean hydroelectric energy",
              "role": "受詞 (Object)",
              "note": "形容詞 hydroelectric 修飾 energy。"
            },
            {
              "part": "by channeling rushing river currents through massive subterranean turbines",
              "role": "手段方法狀語",
              "note": "by + 動名詞 channeling；through 表穿過。"
            }
          ],
          "keyPoints": [
            "【手段介系詞】：by + V-ing 表示「藉由執行某動作來達成目標」。",
            "【字根疊合】：hydro- (水) + electro- (電)，現代永續能源領域最關鍵之複合詞根。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Liquid Architect: The Primordial Flow of Hydro",
      "titleZh": "流動的建築師：生命之源水之歌",
      "intro": "水 (hydr-) 是萬物之母，滋養了細胞的躍動，也承載了現代清潔能源 (hydrogen) 與重工業液壓力量的奇蹟。",
      "paragraphs": [
        {
          "en": "Without constant hydration, biological enzymes cease to catalyze essential cellular reactions. Human physiology is essentially a delicate balance of water retention, where failing to replenish fluids can dehydrate organs in mere hours.",
          "zh": "沒有持續的水分滋養，生物酵素便無法催化關鍵的細胞反應。人體生理學本質上就是一場精妙的保水平衡，若未能及時補充水分，器官在短短數小時內便會陷入脫水危機。"
        },
        {
          "en": "Beyond biology, water fluids drive global heavy machinery through hydraulic transmission, while green hydrogen promises an era free of toxic smog, proving that the flow of hydro remains humanity's greatest ally.",
          "zh": "在生物學之外，水性液體透過液壓傳動驅動著全球重型機械，而綠色氫能更昭示著一個遠離有毒煙霾的潔淨時代，證明了水的奔流依舊是人類最忠實的盟友。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "Why is water vital for cellular function according to the passage?",
          "qZh": "根據文章，為何水分對細胞功能至關重要？",
          "options": [
            "A. It allows enzymes to catalyze essential cellular reactions. (使酵素能催化關鍵細胞反應)",
            "B. It turns skin into solid diamond.",
            "C. It eliminates the need for oxygen entirely.",
            "D. It replaces all red blood cells with gold."
          ],
          "answer": 0,
          "explanation": "文中第一段指出「Without constant hydration, biological enzymes cease to catalyze essential cellular reactions」。"
        }
      ]
    }
  },
  {
    "id": "therm",
    "name": "therm / thermo",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「θερμός」(thermós)，意為「溫暖的、熱的、溫度」。",
    "originMeaning": "熱、熱量、溫度",
    "phonetic": "/θɜːrm/ 或 /ˈθɜːrmoʊ/",
    "icon": "🌡️",
    "color": "#EA580C",
    "summary": "涵蓋熱力學、溫度計、恆溫調節器與極端核熱能的核心字根。",
    "words": [
      {
        "word": "thermometer",
        "kk": "[θɚˈmɑmətɚ]",
        "ipa": "/θərˈmɑːmɪtər/",
        "pos": "n.",
        "meaning": "溫度計、體溫計",
        "formula": {
          "parts": [
            {
              "text": "thermo-",
              "role": "root",
              "meaning": "熱、溫度 (希臘語 thermós)"
            },
            {
              "text": "-meter",
              "role": "root/suffix",
              "meaning": "測量計 (希臘語 metron 衡量)"
            }
          ],
          "resultMeaning": "用以精確測量冷熱溫度高低的儀器 ➔「溫度計」"
        },
        "sentence": "The nurse used an infrared digital thermometer to check whether the feverish child required pediatric antibiotics.",
        "sentenceZh": "護理師使用紅外線數位體溫計進行量測，以確認發燒的兒童是否需要服用小兒抗生素。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose with Noun Clause (主詞 + 及物動詞 + 受詞 + 目的狀詞與 whether 間接問句名詞子句)",
          "breakdown": [
            {
              "part": "The nurse",
              "role": "主詞 (Subject)",
              "note": "護理師。"
            },
            {
              "part": "used",
              "role": "及物動詞 (Transitive Verb)",
              "note": "使用。"
            },
            {
              "part": "an infrared digital thermometer",
              "role": "直接受詞 (Direct Object)",
              "note": "infrared (紅外線的)；digital (數位的)。"
            },
            {
              "part": "to check whether the feverish child required pediatric antibiotics",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "whether 引導名詞子句作 check 的受詞；feverish (發燒的)；pediatric (小兒科的)。"
            }
          ],
          "keyPoints": [
            "【醫學複合字彙】：infrared thermometer (紅外線體溫計)、pediatric antibiotics (小兒抗生素)。",
            "【名詞子句受詞】：check + whether/if... (檢查確認是否...)。"
          ]
        }
      },
      {
        "word": "thermostat",
        "kk": "[ˈθɝməˌstæt]",
        "ipa": "/ˈθɜːrməstæt/",
        "pos": "n.",
        "meaning": "恆溫器、自動調溫裝置",
        "formula": {
          "parts": [
            {
              "text": "thermo-",
              "role": "root",
              "meaning": "溫度、熱 (希臘語 thermós)"
            },
            {
              "text": "-stat",
              "role": "root",
              "meaning": "保持靜止、穩定 (希臘語 statos 站立/穩定)"
            }
          ],
          "resultMeaning": "自動控制冷暖設備將室溫維持在固定恆常數值的裝置 ➔「恆溫器」"
        },
        "sentence": "Programmable smart thermostats optimize household energy consumption by lowering indoor temperatures during midnight hours.",
        "sentenceZh": "可程式化智慧恆溫器藉由在午夜時段調低室內溫度，大幅最佳化了家庭能源消耗。",
        "grammar": {
          "pattern": "S + Vt + O + By-Gerund Means Adverbial (主詞 + 及物動詞 + 受詞 + 方式介系詞動名詞片語)",
          "breakdown": [
            {
              "part": "Programmable smart thermostats",
              "role": "主詞 (Subject)",
              "note": "可程式化智慧恆溫器。"
            },
            {
              "part": "optimize",
              "role": "及物動詞 (Transitive Verb)",
              "note": "最佳化。"
            },
            {
              "part": "household energy consumption",
              "role": "直接受詞 (Direct Object)",
              "note": "家庭能源消耗。"
            },
            {
              "part": "by lowering indoor temperatures during midnight hours",
              "role": "方式狀詞片語 (By + Gerund)",
              "note": "by lowering... (藉由調降...)。"
            }
          ],
          "keyPoints": [
            "【字根 stat (靜止/恆定)】：如 static (靜態的)、status (地位/現狀)。",
            "【手段狀詞結構】：optimize A by doing B (藉由做 B 來優化 A)。"
          ]
        }
      },
      {
        "word": "thermal",
        "kk": "[ˈθɝməl]",
        "ipa": "/ˈθɜːrml/",
        "pos": "adj. / n.",
        "meaning": "熱的、熱能的、溫泉的；(n.) 上升熱氣流",
        "formula": {
          "parts": [
            {
              "text": "therm",
              "role": "root",
              "meaning": "熱、溫度 (heat)"
            },
            {
              "text": "-al",
              "role": "suffix",
              "meaning": "形容詞字尾 (relating to)"
            }
          ],
          "resultMeaning": "與熱度傳遞或溫度能量直接相關的 ➔「熱的、熱能的」"
        },
        "sentence": "Engineers designed a state-of-the-art thermal barrier that insulates sensitive spacecraft electronics during atmospheric reentry.",
        "sentenceZh": "工程師設計了一道最先進的隔熱屏障，在大氣層再入過程中保護太空船上靈敏的電子設備。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (that insulates...)",
          "breakdown": [
            {
              "part": "Engineers",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "designed",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "a state-of-the-art thermal barrier",
              "role": "受詞 (Object)",
              "note": "state-of-the-art 為複合形容詞「最先進的」。"
            },
            {
              "part": "that insulates sensitive spacecraft electronics during atmospheric reentry",
              "role": "關係子句",
              "note": "that 指代 barrier 作子句主詞；insulate 表「隔絕保護」。"
            }
          ],
          "keyPoints": [
            "【常用複合詞】：thermal insulation (隔熱)、thermal underwear (發熱衣)、thermal spring (溫泉)。",
            "【前綴慣用】：state-of-the-art 為常見複合形容詞，指「技術達到現階段最高水準的」。"
          ]
        }
      },
      {
        "word": "hypothermia",
        "kk": "[ˌhaɪpəˈθɝmɪə]",
        "ipa": "/ˌhaɪpoʊˈθɜːrmiə/",
        "pos": "n.",
        "meaning": "體溫過低、失溫症",
        "formula": {
          "parts": [
            {
              "text": "hypo-",
              "role": "prefix",
              "meaning": "在下方、過低 (under, deficient)"
            },
            {
              "text": "therm",
              "role": "root",
              "meaning": "熱量、體溫 (heat)"
            },
            {
              "text": "-ia",
              "role": "suffix",
              "meaning": "醫學病症字尾 (medical condition)"
            }
          ],
          "resultMeaning": "身體核心熱量散失過快導致核心體溫低於危險門檻 ➔「體溫過低、失溫症」"
        },
        "sentence": "Mountaineers caught in severe alpine blizzards must immediately set up emergency shelters to prevent fatal hypothermia.",
        "sentenceZh": "在嚴酷高山暴風雪中受困的登山客必須立即搭建緊急避難所，以防止致命的低體溫症。",
        "grammar": {
          "pattern": "S + Participle Phrase (caught in...) + Modal + Adv + Vt + O + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "Mountaineers",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "caught in severe alpine blizzards",
              "role": "過去分詞片語修飾主詞",
              "note": "be caught in 意為「遭逢、受困於」。"
            },
            {
              "part": "must immediately set up",
              "role": "動詞片語 (Verb)",
              "note": "set up 意為「搭設、建立」。"
            },
            {
              "part": "emergency shelters",
              "role": "直接受詞 (Direct Object)",
              "note": "「緊急避難所」。"
            },
            {
              "part": "to prevent fatal hypothermia",
              "role": "不定詞目的狀語",
              "note": "prevent 後接著名詞 hypothermia。"
            }
          ],
          "keyPoints": [
            "【對比字首】：hypo- (過低，如 hypothermia, hypotension 低血壓) vs. hyper- (過高，如 hyperthermia 高熱, hypertension 高血壓)。",
            "【分詞後位修飾】：caught in... 省略了 who are / who were。"
          ]
        }
      },
      {
        "word": "thermodynamics",
        "kk": "[ˌθɝmodaɪˈnæmɪks]",
        "ipa": "/ˌθɜːrmoʊdaɪˈnæmɪks/",
        "pos": "n.",
        "meaning": "熱力學",
        "formula": {
          "parts": [
            {
              "text": "thermo-",
              "role": "prefix",
              "meaning": "熱量、熱 (heat)"
            },
            {
              "text": "dynamics",
              "role": "base",
              "meaning": "動力學、力學 (power, force)"
            }
          ],
          "resultMeaning": "研究熱量與功、能量相互轉換及動力學規律之科學 ➔「熱力學」"
        },
        "sentence": "The second law of thermodynamics establishes that entropy in any isolated physical system tends to increase spontaneously over time.",
        "sentenceZh": "熱力學第二定律確立了任何孤立物理系統中的熵隨著時間推移皆傾向於自發增加。",
        "grammar": {
          "pattern": "S + Vt (establishes) + That Noun Clause (that entropy tends to increase...)",
          "breakdown": [
            {
              "part": "The second law of thermodynamics",
              "role": "主詞 (Subject)",
              "note": "專有名詞片語。"
            },
            {
              "part": "establishes",
              "role": "及物動詞 (Verb)",
              "note": "意為「確立、證明」。"
            },
            {
              "part": "that entropy in any isolated physical system tends to increase spontaneously over time",
              "role": "受詞名詞子句",
              "note": "entropy (熵)；tends to V (傾向於)；spontaneously (自發地)。"
            }
          ],
          "keyPoints": [
            "【學科字尾】：thermodynamics 形式雖有 -s，但作為一門物理學科名詞時視為單數！",
            "【科學動詞】：tend to + 原形動詞，表自然法則的普遍傾向。"
          ]
        }
      }
    ],
    "article": {
      "title": "Mastering the Fire: The Thermodynamic Cosmos",
      "titleZh": "火熱的度量：熱力學與溫度的奧秘",
      "intro": "從原始人圍繞的營火，到維持舒適居家的智慧恆溫器 (thermostat)，人類學會了如何測量與駕馭熱能 (therm-)。",
      "paragraphs": [
        {
          "en": "Temperature is the invisible pulse of matter, dictating whether liquid oceans remain liquid or freeze into impenetrable ice. The invention of the mercury thermometer granted scientists their first quantitative gauge of thermal equilibrium.",
          "zh": "溫度是物質看不見的脈搏，決定了海洋是保持液態還是凍結成難以穿透的堅冰。水銀溫度計的發明，賦予了科學家第一個測量熱平衡的量化工具。"
        },
        {
          "en": "Today, microchips manage precision thermostats in spacecraft traversing interplanetary extremes, demonstrating how mastering the root 'therm' protects human life amidst the cold vacuum of the cosmos.",
          "zh": "今天，微晶片在穿梭於行星際極端環境的太空船中控制著精密恆溫器，展現了掌握「熱能 (therm)」字根如何守護人類在冰冷宇宙真空中的生存。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What did the mercury thermometer grant scientists?",
          "qZh": "水銀溫度計賦予了科學家什麼？",
          "options": [
            "A. Their first quantitative gauge of thermal equilibrium. (測量熱平衡的第一個量化工具)",
            "B. The ability to travel through black holes.",
            "C. Total control over rainfall.",
            "D. A way to create endless gold."
          ],
          "answer": 0,
          "explanation": "文中第一段指出溫度計「granted scientists their first quantitative gauge of thermal equilibrium」。"
        }
      ]
    }
  },
  {
    "id": "graph",
    "name": "graph / gram",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「γράφειν」(gráphein)，意指「書寫、畫圖、銘刻」；延伸名詞「γράμμα」(grámma 字母/文字)。",
    "originMeaning": "寫、畫、記錄、圖像、字元",
    "phonetic": "/ɡræf/ 或 /ɡræm/",
    "icon": "📊",
    "color": "#7C3AED",
    "summary": "涵蓋照片、圖形、簽名、圖表、文法規範及電信圖象的核心字根。",
    "words": [
      {
        "word": "photograph",
        "kk": "[ˈfotəˌgræf]",
        "ipa": "/ˈfoʊtəɡræf/",
        "pos": "n. / v.",
        "meaning": "(n.) 照片；(v.) 拍照",
        "formula": {
          "parts": [
            {
              "text": "photo-",
              "role": "prefix/root",
              "meaning": "光 (希臘語 phōs/phōtos)"
            },
            {
              "text": "graph",
              "role": "root",
              "meaning": "畫、寫 (希臘語 gráphein)"
            }
          ],
          "resultMeaning": "用光線在感光底片上繪畫銘刻出的影像 ➔「照片」"
        },
        "sentence": "The war photojournalist captured a historic photograph that exposed the tragic human toll of armed conflict.",
        "sentenceZh": "這位戰地攝影記者拍下了一張歷史性的照片，揭露了武裝衝突所造成的悲慘人員代價。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 限定關係子句)",
          "breakdown": [
            {
              "part": "The war photojournalist",
              "role": "主詞 (Subject)",
              "note": "戰地攝影記者。"
            },
            {
              "part": "captured",
              "role": "及物動詞 (Transitive Verb)",
              "note": "捕捉拍下。"
            },
            {
              "part": "a historic photograph",
              "role": "直接受詞 (Direct Object)",
              "note": "historic (具歷史意義的)；photograph (照片)。"
            },
            {
              "part": "that exposed the tragic human toll of armed conflict",
              "role": "限定關係子句 (Defining Relative Clause)",
              "note": "that 為主格關代；exposed (揭露)；human toll (人員傷亡代價)。"
            }
          ],
          "keyPoints": [
            "【字首融合】：photo (光，如 photosynthesis 光合作用) + graph (畫/寫)。",
            "【易混淆形容詞】：historic (具重大歷史意義的) vs. historical (與歷史過去相關的)。"
          ]
        }
      },
      {
        "word": "autograph",
        "kk": "[ˈɔtəˌgræf]",
        "ipa": "/ˈɔːtəɡræf/",
        "pos": "n. / v.",
        "meaning": "(n.) 親筆簽名；(v.) 親自簽名",
        "formula": {
          "parts": [
            {
              "text": "auto-",
              "role": "prefix",
              "meaning": "自己、親自 (希臘語 autós)"
            },
            {
              "text": "graph",
              "role": "root",
              "meaning": "寫 (希臘語 gráphein)"
            }
          ],
          "resultMeaning": "由本人親自親手寫下的姓名 ➔「親筆簽名」"
        },
        "sentence": "Eager literary fans queued patiently outside the bookstore to receive a personalized autograph from the Nobel laureate.",
        "sentenceZh": "熱切的文學書迷在書店外耐心排隊，只為獲得諾貝爾得主的個人親筆簽名。",
        "grammar": {
          "pattern": "S + Vi + Adv + Locative Prep Phrase + Infinitive of Purpose (主詞 + 不及物動詞 + 副詞 + 地點片語 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Eager literary fans",
              "role": "主詞 (Subject)",
              "note": "熱切的文學粉絲。"
            },
            {
              "part": "queued",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "排隊 (英式常用 queue up)。"
            },
            {
              "part": "patiently",
              "role": "方式副詞 (Adverb)",
              "note": "耐心沉著地。"
            },
            {
              "part": "outside the bookstore",
              "role": "地點狀詞 (Locative Phrase)",
              "note": "在書店外。"
            },
            {
              "part": "to receive a personalized autograph from the Nobel laureate",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "personalized (客製化/題字的)；laureate (得主)。"
            }
          ],
          "keyPoints": [
            "【簽名近義辨析】：autograph (名人親筆紀念簽名) vs. signature (法律文件或帳單的正式簽名)。",
            "【雙重希臘詞根】：auto (自己) + graph (寫)。"
          ]
        }
      },
      {
        "word": "diagram",
        "kk": "[ˈdaɪəˌgræm]",
        "ipa": "/ˈdaɪəɡræm/",
        "pos": "n.",
        "meaning": "圖表、圖解、示意圖",
        "formula": {
          "parts": [
            {
              "text": "dia-",
              "role": "prefix",
              "meaning": "貫穿、在兩者之間 (希臘語 dia)"
            },
            {
              "text": "gram",
              "role": "root",
              "meaning": "寫、劃出 (希臘語 grámma)"
            }
          ],
          "resultMeaning": "橫穿勾勒出事物內部結構與運作關聯的圖示 ➔「示意圖、圖解」"
        },
        "sentence": "The engineering manual includes a schematic wiring diagram to facilitate safe electronic troubleshooting.",
        "sentenceZh": "工程手冊隨附了一份電路配線原理示意圖，以利進行安全的電子故障排除。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "The engineering manual",
              "role": "主詞 (Subject)",
              "note": "工程手冊。"
            },
            {
              "part": "includes",
              "role": "及物動詞 (Transitive Verb)",
              "note": "包含收錄。"
            },
            {
              "part": "a schematic wiring diagram",
              "role": "直接受詞 (Direct Object)",
              "note": "schematic (原理圖示的)；wiring (線路)；diagram (示意圖)。"
            },
            {
              "part": "to facilitate safe electronic troubleshooting",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "facilitate (促進、使便利)；troubleshooting (故障排除)。"
            }
          ],
          "keyPoints": [
            "【高分動詞】：facilitate (使容易/促進進行)。",
            "【同根家族】：program (程式/節目)、telegram (電報)、grammar (文法)。"
          ]
        }
      },
      {
        "word": "graphic",
        "kk": "[ˈgræfɪk]",
        "ipa": "/ˈɡræfɪk/",
        "pos": "adj. / n.",
        "meaning": "圖表的、形象生動的；(n.) 圖表、圖像",
        "formula": {
          "parts": [
            {
              "text": "graph",
              "role": "root",
              "meaning": "繪畫、書寫 (write, draw)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "形容詞字尾 (relating to)"
            }
          ],
          "resultMeaning": "如圖像畫作般歷歷在目、生動逼真的 ➔「圖表的、生動逼真的」"
        },
        "sentence": "The eyewitness provided a remarkably graphic account of the catastrophic bridge collapse.",
        "sentenceZh": "目擊者對這起災難性的橋樑坍塌事故進行了極其生動詳盡的描述。",
        "grammar": {
          "pattern": "S + Vt + O (a remarkably graphic account) + Prep Phrase",
          "breakdown": [
            {
              "part": "The eyewitness",
              "role": "主詞 (Subject)",
              "note": "單數名詞「目擊證人」。"
            },
            {
              "part": "provided",
              "role": "及物動詞 (Verb)",
              "note": "provide an account of (對...做出描述)。"
            },
            {
              "part": "a remarkably graphic account",
              "role": "受詞 (Object)",
              "note": "remarkably 為程度副詞，graphic 作形容詞「栩栩如生的、生動描繪的」。"
            },
            {
              "part": "of the catastrophic bridge collapse",
              "role": "介系詞片語",
              "note": "catastrophic (災難性的) 修飾 collapse。"
            }
          ],
          "keyPoints": [
            "【一詞多義】：graphic 作形容詞時可表示「圖形的 (graphic design)」，亦常作「細緻露骨的、生動逼真的 (graphic depiction)」。",
            "【片語搭配】：provide a graphic account of... 是新聞英文中描寫目擊證詞的典範用法。"
          ]
        }
      },
      {
        "word": "telegram",
        "kk": "[ˈtɛləˌgræm]",
        "ipa": "/ˈtɛləɡræm/",
        "pos": "n.",
        "meaning": "電報",
        "formula": {
          "parts": [
            {
              "text": "tele-",
              "role": "prefix",
              "meaning": "遠距離 (far, distant)"
            },
            {
              "text": "gram",
              "role": "root",
              "meaning": "文字、書寫記號 (writing, letter)"
            }
          ],
          "resultMeaning": "跨越遠方以電脈衝傳遞並列印出的文字訊息 ➔「電報」"
        },
        "sentence": "Before transcontinental telephone networks were developed, an urgent telegram was the fastest way to convey vital news.",
        "sentenceZh": "在跨洲電話網路發展起來之前，緊急電報是傳遞重要消息最快的方式。",
        "grammar": {
          "pattern": "Adv Clause of Time (Before...) + S + Linking Verb (was) + SC (the fastest way + to V)",
          "breakdown": [
            {
              "part": "Before transcontinental telephone networks were developed",
              "role": "時間副詞子句",
              "note": "were developed 過去被動態。"
            },
            {
              "part": "an urgent telegram",
              "role": "主要子句主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "was",
              "role": "連綴動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "the fastest way to convey vital news",
              "role": "主詞補語 (Subject Complement)",
              "note": "最高級 fastest 修飾 way；to convey 為不定詞作後位修飾。"
            }
          ],
          "keyPoints": [
            "【同源字尾】：-gram (寫成的文本，如 diagram, telegram, program) vs. -graph (寫出的工具或過程，如 telegraph, photograph)。",
            "【不定詞後位修飾】：the way to do something 是固定形容詞用法，修飾 way。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Inscribed Image: The Empire of Graph and Gram",
      "titleZh": "筆繪的印記：圖文符碼的世界",
      "intro": "從洞穴岩壁的原始刻畫，到高解析度照片 (photograph) 與數位圖表 (diagram)，字根 graph- 記錄著文明的靈魂軌跡。",
      "paragraphs": [
        {
          "en": "Humanity's defining leap occurred when our ancestors ceased to rely exclusively upon fleeting spoken words and began drawing permanent graphic symbols on cave walls, giving birth to recorded history.",
          "zh": "人類最具決定性的躍進，發生在我們的祖先不再單純依賴轉瞬即逝的口語，並開始在洞穴岩壁上繪製永久性圖形符號那一刻，這孕育了有文字記載的歷史。"
        },
        {
          "en": "Whether preserving raw human emotion in an evocative photograph or conveying intricate engineering systems through a crisp schematic diagram, the Greek root graphein empowers us to bridge minds through the immortal art of visual inscription.",
          "zh": "無論是透過一張動人的照片銘存純粹的人類情感，抑或是藉由一張清晰的原理示意圖傳遞錯綜複雜的工程系統，希臘字根 graphein 皆賦予了我們透過視覺銘刻的不朽藝術橫跨心靈的非凡力量。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What defining human leap is highlighted in the text?",
          "qZh": "文中強調了人類何種具決定性的躍進？",
          "options": [
            "A. Drawing permanent graphic symbols instead of relying solely on spoken words. (繪製永久圖形符號而非僅依賴口語)",
            "B. Discovering electricity in thunderstorms.",
            "C. Domesticating deep-sea creatures.",
            "D. Stopping the usage of all symbols."
          ],
          "answer": 0,
          "explanation": "文中第一段指出躍進始於「ceased to rely exclusively upon fleeting spoken words and began drawing permanent graphic symbols」。"
        }
      ]
    }
  },
  {
    "id": "phon",
    "name": "phon / phone",
    "type": "root",
    "typeLabel": "希臘語字根 (Greek Root)",
    "etymology": "源自古希臘語「φωνή」(phōnē)，意為「聲音、語音、樂音、講話聲」。",
    "originMeaning": "聲音、語音、發音、音響",
    "phonetic": "/foʊn/ 或 /fɑːn/",
    "icon": "🎺",
    "color": "#D97706",
    "summary": "涵蓋交響樂、語音學、擴音器、和諧悅耳之聲與刺耳雜音的核心字根。",
    "words": [
      {
        "word": "symphony",
        "kk": "[ˈsɪmfəni]",
        "ipa": "/ˈsɪmfəni/",
        "pos": "n.",
        "meaning": "交響樂、交響曲、和諧的交織組合",
        "formula": {
          "parts": [
            {
              "text": "sym-",
              "role": "prefix",
              "meaning": "共同、一起 (希臘語 syn)"
            },
            {
              "text": "phon",
              "role": "root",
              "meaning": "聲音 (希臘語 phōnē)"
            },
            {
              "text": "-y",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "眾多不同樂器的聲音共同齊鳴奏出和諧旋律 ➔「交響曲」"
        },
        "sentence": "The philharmonic orchestra performed Beethoven's Ninth Symphony to celebrate international cultural unity.",
        "sentenceZh": "愛樂管弦樂團演奏貝多芬的《第九號交響曲》，以慶祝國際文化間的和睦團結。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "The philharmonic orchestra",
              "role": "主詞 (Subject)",
              "note": "愛樂管弦樂團 (phil- 愛 + harmonic 和聲)。"
            },
            {
              "part": "performed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "演出。"
            },
            {
              "part": "Beethoven's Ninth Symphony",
              "role": "直接受詞 (Direct Object)",
              "note": "貝多芬第九交響曲。"
            },
            {
              "part": "to celebrate international cultural unity",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "celebrate (慶祝)；unity (團結一致)。"
            }
          ],
          "keyPoints": [
            "【雙重希臘詞素】：sym (共同) + phone (聲音)。",
            "【比喻用法】：a symphony of colors (繽紛絢麗色彩的完美交融)。"
          ]
        }
      },
      {
        "word": "phonetics",
        "kk": "[fəˈnɛtɪks]",
        "ipa": "/fəˈnetɪks/",
        "pos": "n.",
        "meaning": "語音學、發音系統",
        "formula": {
          "parts": [
            {
              "text": "phon",
              "role": "root",
              "meaning": "語音 (希臘語 phōnē)"
            },
            {
              "text": "-etics",
              "role": "suffix",
              "meaning": "學問、學科 (名詞字尾)"
            }
          ],
          "resultMeaning": "研究人類如何發出、傳遞並感知語言聲音的科學 ➔「語音學」"
        },
        "sentence": "Linguists apply acoustic phonetics to train neural speech synthesis engines to replicate subtle human vocal nuances.",
        "sentenceZh": "語言學家應用聲學語音學，訓練神經網路語音合成引擎精確模擬人類細微的話語抑揚頓挫。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Infinitive (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 動詞補語不定詞)",
          "breakdown": [
            {
              "part": "Linguists",
              "role": "主詞 (Subject)",
              "note": "語言學家。"
            },
            {
              "part": "apply",
              "role": "及物動詞 (Transitive Verb)",
              "note": "應用採用。"
            },
            {
              "part": "acoustic phonetics",
              "role": "直接受詞 (Direct Object)",
              "note": "聲學語音學。"
            },
            {
              "part": "to train neural speech synthesis engines",
              "role": "目的狀詞 (Infinitive)",
              "note": "train + O + to V (訓練...做...)；synthesis (合成)。"
            },
            {
              "part": "to replicate subtle human vocal nuances",
              "role": "補語不定詞 (Infinitive Complement)",
              "note": "replicate (複製再現)；nuances (細微差異)。"
            }
          ],
          "keyPoints": [
            "【學科字尾 -ics】：phonetics (語音學)、linguistics (語言學) 作單數名詞看待。",
            "【名詞搭配】：vocal nuances (話語聲調的細微韻味)。"
          ]
        }
      },
      {
        "word": "microphone",
        "kk": "[ˈmaɪkrəˌfon]",
        "ipa": "/ˈmaɪkrəfoʊn/",
        "pos": "n.",
        "meaning": "麥克風、話筒、擴音器",
        "formula": {
          "parts": [
            {
              "text": "micro-",
              "role": "prefix",
              "meaning": "微小 (希臘語 mikrós)"
            },
            {
              "text": "phone",
              "role": "root",
              "meaning": "聲音 (希臘語 phōnē)"
            }
          ],
          "resultMeaning": "將極微小的人聲轉換為電子訊號加以放大的裝置 ➔「麥克風」"
        },
        "sentence": "The keynote speaker adjusted the wireless microphone before addressing the international climate summit.",
        "sentenceZh": "主講人在向國際氣候高峰會發表演說之前，先微調了無線麥克風的收音位置。",
        "grammar": {
          "pattern": "S + Vt + O + Prepositional Gerund Time Clause (主詞 + 及物動詞 + 受詞 + 介系詞動名詞時間狀詞)",
          "breakdown": [
            {
              "part": "The keynote speaker",
              "role": "主詞 (Subject)",
              "note": "主題演說主講人。"
            },
            {
              "part": "adjusted",
              "role": "及物動詞 (Transitive Verb)",
              "note": "微調對準。"
            },
            {
              "part": "the wireless microphone",
              "role": "直接受詞 (Direct Object)",
              "note": "無線麥克風。"
            },
            {
              "part": "before addressing the international climate summit",
              "role": "時間狀詞 (Time Adverbial)",
              "note": "before 作介系詞後接動名詞 addressing (向...發表演講)；summit (高峰會議)。"
            }
          ],
          "keyPoints": [
            "【多義及物動詞】：address 此處意為「向...發表演說/對話」，而非名詞「住址」。",
            "【詞根整合】：micro (微小) + phone (聲音)。"
          ]
        }
      },
      {
        "word": "megaphone",
        "kk": "[ˈmɛgəˌfon]",
        "ipa": "/ˈmɛɡəfoʊn/",
        "pos": "n.",
        "meaning": "擴音器、大聲公、喊話筒",
        "formula": {
          "parts": [
            {
              "text": "mega-",
              "role": "prefix",
              "meaning": "巨大、宏大 (large)"
            },
            {
              "text": "phone",
              "role": "root",
              "meaning": "聲音 (sound)"
            }
          ],
          "resultMeaning": "將微小人聲擴大成巨大聲音的號角喇叭 ➔「擴音器」"
        },
        "sentence": "The rally coordinator shouted urgent instructions through a battery-powered megaphone to guide the assembling crowd safely.",
        "sentenceZh": "集會協調員透過電池驅動的擴音器大聲喊出緊急指引，以安全引導聚集的群眾。",
        "grammar": {
          "pattern": "S + Vt + O + Prep Phrase + Infinitive Phrase of Purpose",
          "breakdown": [
            {
              "part": "The rally coordinator",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "shouted",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "urgent instructions",
              "role": "直接受詞 (Direct Object)",
              "note": "urgent (緊迫的) 修飾 instructions。"
            },
            {
              "part": "through a battery-powered megaphone",
              "role": "工具介系詞片語",
              "note": "through 表示「透過...工具」。"
            },
            {
              "part": "to guide the assembling crowd safely",
              "role": "不定詞目的狀語",
              "note": "assembling 為現在分詞作前置修飾；safely 為情狀副詞。"
            }
          ],
          "keyPoints": [
            "【字首疊加】：mega- (百萬、極大，如 megabyte, megacity) + phone (聲音)。",
            "【工具介系詞】：through 常表示透過通訊或擴音工具傳播聲音。"
          ]
        }
      },
      {
        "word": "cacophony",
        "kk": "[kəˈkɑfənɪ]",
        "ipa": "/kəˈkɑːfəni/",
        "pos": "n.",
        "meaning": "刺耳的雜音、不和諧的聲音",
        "formula": {
          "parts": [
            {
              "text": "kakos (caco-)",
              "role": "prefix",
              "meaning": "惡劣的、糟糕的 (bad)"
            },
            {
              "text": "phon",
              "role": "root",
              "meaning": "聲音 (sound)"
            },
            {
              "text": "-y",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "各種惡劣混亂聲音交織而成的雜音 ➔「刺耳雜音」"
        },
        "sentence": "As the morning rush hour peaked, the pedestrian was overwhelmed by a jarring cacophony of blaring horns and screeching train brakes.",
        "sentenceZh": "隨著早晨尖峰時刻達到最高峰，這名行人被刺耳的喇叭聲與尖銳的火車剎車雜音所淹沒。",
        "grammar": {
          "pattern": "Adv Clause of Time (As...) + S + Passive Verb + Prep Phrase (by a jarring cacophony of...)",
          "breakdown": [
            {
              "part": "As the morning rush hour peaked",
              "role": "時間副詞子句",
              "note": "as 引導時間子句；peaked 作動詞「達到頂點」。"
            },
            {
              "part": "the pedestrian",
              "role": "主要句主詞 (Subject)",
              "note": "單數名詞「行人」。"
            },
            {
              "part": "was overwhelmed",
              "role": "被動態謂語動詞",
              "note": "意為「被...壓倒、充塞」。"
            },
            {
              "part": "by a jarring cacophony of blaring horns and screeching train brakes",
              "role": "施事介系詞片語",
              "note": "jarring (刺耳的) 修飾 cacophony；blaring 與 screeching 皆為現在分詞。"
            }
          ],
          "keyPoints": [
            "【對比字源】：cacophony (刺耳雜音) vs. euphony (悅耳聲音，eu- 表好)。",
            "【生動分詞修飾】：blaring horns (鳴響的喇叭) 與 screeching brakes (尖叫刺耳的剎車)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Tapestry of Sound: The Resonance of Phone",
      "titleZh": "聲動九天：語音與共鳴的奇蹟",
      "intro": "人聲是心靈的共振。透過字根 phone-，微小的話語 (microphone) 能昇華為震懾靈魂的浩瀚交響 (symphony)。",
      "paragraphs": [
        {
          "en": "In every vibrant culture, human sound transcends mere biology to become high art. When master vocalists harmonize in polyphonic symphonies, disparate acoustic vibrations fuse into a unified transcendental emotional wave.",
          "zh": "在每一個蓬勃發展的文化中，人類的聲音超越了純粹的生理現象，成為崇高的藝術。當傑出的聲樂家在複音交響曲中共同和鳴時，原本分散的聲學振動便融合為一股統一而昇華的情感波濤。"
        },
        {
          "en": "By analyzing vowel resonance through phonetics, modern engineers program sensitive microphones that transmit human passion across continents, reminding us that voice remains our most intimate instrument.",
          "zh": "藉由透過語音學分析母音共鳴，現代工程師打造出高靈敏度的麥克風，將人類的熱忱傳遞跨越各大洲，提醒著我們：聲音永遠是我們最貼近心靈的樂器。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What happens when disparate acoustic vibrations fuse in a symphony?",
          "qZh": "當交響曲中分散的聲學振動融合時會發生什麼事？",
          "options": [
            "A. They fuse into a unified transcendental emotional wave. (融合為一股統一而昇華的情感波濤)",
            "B. They shatter all glass in the hall.",
            "C. They convert into pure electricity.",
            "D. They stop all human heartbeats."
          ],
          "answer": 0,
          "explanation": "文中第一段指出振動會「fuse into a unified transcendental emotional wave」。"
        }
      ]
    }
  },
  {
    "id": "tract",
    "name": "tract",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「trahere」(拉、扯、抽取、牽引)，過去分詞為 tractum。",
    "originMeaning": "拉、扯、抽取、牽引、拖曳",
    "phonetic": "/trækt/",
    "icon": "🧲",
    "color": "#B45309",
    "summary": "涵蓋吸引、分心分神、合約簽訂、抽象概念、萃取提煉與拖拉機的核心字根。",
    "words": [
      {
        "word": "attract",
        "kk": "[əˈtrækt]",
        "ipa": "/əˈtrækt/",
        "pos": "v.",
        "meaning": "吸引、引起興趣、招引",
        "formula": {
          "parts": [
            {
              "text": "at-",
              "role": "prefix",
              "meaning": "朝向、去 (拉丁語 ad-)"
            },
            {
              "text": "tract",
              "role": "root",
              "meaning": "拉、牽引 (拉丁語 trahere)"
            }
          ],
          "resultMeaning": "朝著某個方向將人或物的注意力拉過來 ➔「吸引、引起」"
        },
        "sentence": "The scenic coastal biosphere attracts international eco-tourists fascinated by migratory marine wildlife.",
        "sentenceZh": "這處風景優美的沿海生物圈吸引了無數著迷於遷徙性海洋野生動物的國際生態遊客。",
        "grammar": {
          "pattern": "S + Vt + O + Past Participle Modifier (主詞 + 及物動詞 + 受詞 + 過去分詞片語修飾)",
          "breakdown": [
            {
              "part": "The scenic coastal biosphere",
              "role": "主詞 (Subject)",
              "note": "風景優美的沿海生物圈。"
            },
            {
              "part": "attracts",
              "role": "及物動詞 (Transitive Verb)",
              "note": "及物動詞現在式。"
            },
            {
              "part": "international eco-tourists",
              "role": "直接受詞 (Direct Object)",
              "note": "國際生態觀光客。"
            },
            {
              "part": "fascinated by migratory marine wildlife",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "fascinated by... (對...深感著迷) 修飾 tourists；migratory (遷徙性的)。"
            }
          ],
          "keyPoints": [
            "【成對分詞情感】：fascinated (感到著迷的人) vs. fascinating (令人著迷的事物)。",
            "【衍生形容詞】：attractive (有吸引力的、誘人的)。"
          ]
        }
      },
      {
        "word": "distract",
        "kk": "[dɪˈstrækt]",
        "ipa": "/dɪˈstrækt/",
        "pos": "v.",
        "meaning": "分散注意力、使分心、干擾",
        "formula": {
          "parts": [
            {
              "text": "dis-",
              "role": "prefix",
              "meaning": "分開、偏離 (拉丁語 dis-)"
            },
            {
              "text": "tract",
              "role": "root",
              "meaning": "拉 (拉丁語 trahere)"
            }
          ],
          "resultMeaning": "把原本聚焦的注意力往別的方向扯開 ➔「使分心、分散注意力」"
        },
        "sentence": "Constant digital notifications distract students from maintaining sustained cognitive focus during study sessions.",
        "sentenceZh": "綿延不絕的數位通知訊息會干擾學生，使他們在自習期間難以保持持續的認知專注。",
        "grammar": {
          "pattern": "S + Vt + O + from + Gerund (主詞 + 及物動詞 + 受詞 + from + 動名詞阻止結構)",
          "breakdown": [
            {
              "part": "Constant digital notifications",
              "role": "主詞 (Subject)",
              "note": "源源不絕的數位通知。"
            },
            {
              "part": "distract",
              "role": "及物動詞 (Transitive Verb)",
              "note": "及物動詞。"
            },
            {
              "part": "students",
              "role": "受詞 (Direct Object)",
              "note": "學生。"
            },
            {
              "part": "from maintaining sustained cognitive focus",
              "role": "阻礙介系詞片語 (Prepositional Phrase)",
              "note": "distract somebody from V-ing (使某人分心而無法做...)；sustained (持續的)。"
            }
          ],
          "keyPoints": [
            "【關鍵句型】：distract A from B (使 A 分心脫離 B)。",
            "【衍生名詞】：distraction (分心之事、干擾物)。"
          ]
        }
      },
      {
        "word": "abstract",
        "kk": "[ˈæbstrækt] (adj.) / [æbˈstrækt] (v.)",
        "ipa": "/ˈæbstrækt/ (adj.) / /æbˈstrækt/ (v.)",
        "pos": "adj. / n. / v.",
        "meaning": "(adj.) 抽象的；(n.) 論文摘要；(v.) 提取、提煉",
        "formula": {
          "parts": [
            {
              "text": "abs-",
              "role": "prefix",
              "meaning": "離開、從 (拉丁語 ab-)"
            },
            {
              "text": "tract",
              "role": "root",
              "meaning": "抽、拉 (拉丁語 trahere)"
            }
          ],
          "resultMeaning": "從無數具體繁雜的現實事物中把本質精髓抽取出來 ➔「抽象的、論文摘要」"
        },
        "sentence": "Theoretical mathematicians formulate abstract concepts that often find unexpected practical applications decades later.",
        "sentenceZh": "理論數學家構想出抽象的概念，這些概念往往在數十年後獲得意想不到的實用應用。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 限定關係子句)",
          "breakdown": [
            {
              "part": "Theoretical mathematicians",
              "role": "主詞 (Subject)",
              "note": "理論數學家。"
            },
            {
              "part": "formulate",
              "role": "及物動詞 (Transitive Verb)",
              "note": "構想制定。"
            },
            {
              "part": "abstract concepts",
              "role": "直接受詞 (Direct Object)",
              "note": "抽象概念。"
            },
            {
              "part": "that often find unexpected practical applications decades later",
              "role": "限定關係子句 (Relative Clause)",
              "note": "that 指代 concepts；applications (應用領域)；decades later (數十年後)。"
            }
          ],
          "keyPoints": [
            "【哲學對立】：abstract (抽象的) vs. concrete (具體的)。",
            "【學術生活高頻】：a research abstract 指期刊論文開頭的「論文摘要」。"
          ]
        }
      },
      {
        "word": "contract",
        "kk": "[ˈkɑntrækt]",
        "ipa": "/ˈkɑːntrækt/",
        "pos": "n. / v.",
        "meaning": "合約、契約；(v.) 收縮、縮小、感染疾病",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同 (together)"
            },
            {
              "text": "tract",
              "role": "root",
              "meaning": "拉、牽引 (draw, pull)"
            }
          ],
          "resultMeaning": "將雙方拉攏在一起共同簽署的條文；或將物體彼此向內拉攏 ➔「合約；收縮」"
        },
        "sentence": "Metals generally expand when subjected to intense heat and contract noticeably when cooled.",
        "sentenceZh": "金屬在受到強熱時通常會膨脹，而在冷卻時則會明顯收縮。",
        "grammar": {
          "pattern": "S + Adv + V1 + Elliptical Clause + and + V2 + Adv + Elliptical Clause",
          "breakdown": [
            {
              "part": "Metals",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "generally expand",
              "role": "動詞片語 1",
              "note": "expand (膨脹)。"
            },
            {
              "part": "when subjected to intense heat",
              "role": "省略時間副詞子句",
              "note": "when (they are) subjected to... 省略主格代名詞與 be 動詞。"
            },
            {
              "part": "and contract noticeably",
              "role": "對等動詞 2 與副詞",
              "note": "and 連接 expand 與 contract；noticeably (顯著地)。"
            },
            {
              "part": "when cooled",
              "role": "省略時間副詞子句",
              "note": "when (they are) cooled。"
            }
          ],
          "keyPoints": [
            "【重音變化】：名詞 contract 重音在第一音節 [ˈkɑntrækt]；動詞 contract 重音可移至第二音節 [kənˈtrækt]（特別在表收縮時）。",
            "【副詞子句省略】：when/while 後若主詞與主要句相同且動詞為 be，可省略主詞與 be 動詞。"
          ]
        }
      },
      {
        "word": "extract",
        "kk": "[ɪkˈstrækt]",
        "ipa": "/ɪkˈstrækt/",
        "pos": "v. / n.",
        "meaning": "拔出、萃取、提取；(n.) 萃取物、精華",
        "formula": {
          "parts": [
            {
              "text": "ex-",
              "role": "prefix",
              "meaning": "向外、拔出 (out)"
            },
            {
              "text": "tract",
              "role": "root",
              "meaning": "拉、抽取 (draw, pull)"
            }
          ],
          "resultMeaning": "從物質深處向外拉出或提煉 ➔「萃取、提取」"
        },
        "sentence": "Biochemists developed an eco-friendly solvent to extract potent medicinal compounds from rare medicinal herbs.",
        "sentenceZh": "生物化學家開發出一種環保溶劑，用以從珍稀草藥中萃取出高效的藥用化合物。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (to extract A from B)",
          "breakdown": [
            {
              "part": "Biochemists",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "developed",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "an eco-friendly solvent",
              "role": "受詞 (Object)",
              "note": "solvent 意為「溶劑」。"
            },
            {
              "part": "to extract potent medicinal compounds from rare medicinal herbs",
              "role": "不定詞目的狀語",
              "note": "extract A from B (從 B 萃取 A)；potent 為形容詞「強效的」。"
            }
          ],
          "keyPoints": [
            "【前名後動重音】：動詞 extract [ɪkˈstrækt] vs. 名詞 extract [ˈɛkstrækt] (如 vanilla extract 香草精)。",
            "【介系詞搭配】：extract something from somewhere 固定搭配介系詞 from。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Pull of the Mind: The Gravity of Tract",
      "titleZh": "引力之網：心靈的牽引與拉扯",
      "intro": "宇宙充斥著各種看不見的「拉力 (tract)」。我們被美好的事物吸引 (attract)，被瑣事分散心神 (distract)，也能從混亂中抽取 (abstract) 真理。",
      "paragraphs": [
        {
          "en": "Human consciousness is permanently engaged in a tug-of-war. While commercial advertisements deploy vibrant imagery to attract consumer desire, endless digital notifications constantly distract our deeper attention.",
          "zh": "人類的意識始終處於一場拔河拉鋸戰中。當商業廣告佈設鮮豔的影像以吸引消費者的慾望時，無休止的數位通知卻時刻分散著我們深度的專注。"
        },
        {
          "en": "True intellectual triumph belongs to those who can extract profound wisdom from everyday chaos, distilling fleeting noise into enduring abstract knowledge that illuminates the path ahead.",
          "zh": "真正的智慧勝利屬於那些能從日常混亂中萃取深邃真理的人，他們將轉瞬即逝的喧囂提煉為持久的抽象知識，照亮前行之路。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What is human consciousness constantly engaged in?",
          "qZh": "人類意識始終處於什麼樣的狀態中？",
          "options": [
            "A. A tug-of-war between attraction and distraction. (處於吸引與分心的拔河拉鋸戰中)",
            "B. Total sleep and hibernation.",
            "C. Building pyramids underwater.",
            "D. Memorizing random numbers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出人類意識「is permanently engaged in a tug-of-war between attraction and distraction」。"
        }
      ]
    }
  },
  {
    "id": "struct",
    "name": "struct",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「struere」(堆疊、建造、排列)，過去分詞為 structum。",
    "originMeaning": "建造、堆疊、構築、排列",
    "phonetic": "/strʌkt/",
    "icon": "🏗️",
    "color": "#0369A1",
    "summary": "涵蓋建築施工、破壞摧毀、結構組織、指導教學及基礎設施的核心字根。",
    "words": [
      {
        "word": "construct",
        "kk": "[kənˈstrʌkt]",
        "ipa": "/kənˈstrʌkt/",
        "pos": "v. / n.",
        "meaning": "(v.) 建造、構築、構想；(n.) 構想概念",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同、聚集 (拉丁語 com-)"
            },
            {
              "text": "struct",
              "role": "root",
              "meaning": "堆疊、建造 (拉丁語 struere)"
            }
          ],
          "resultMeaning": "把各種磚瓦木料聚集堆疊在一起 ➔「建造、構築」"
        },
        "sentence": "Civil engineers plan to construct an earthquake-resistant suspension bridge spanning the turbulent oceanic strait.",
        "sentenceZh": "土木工程師計畫建造一座橫跨洶湧海峽的抗震懸索吊橋。",
        "grammar": {
          "pattern": "S + Vt + Infinitive Object + Participle Modifier (主詞 + 及物動詞 + 不定詞受詞 + 現在分詞後位修飾)",
          "breakdown": [
            {
              "part": "Civil engineers",
              "role": "主詞 (Subject)",
              "note": "土木工程師。"
            },
            {
              "part": "plan",
              "role": "及物動詞 (Transitive Verb)",
              "note": "計畫，接不定詞受詞。"
            },
            {
              "part": "to construct an earthquake-resistant suspension bridge",
              "role": "不定詞受詞 (Infinitive Object)",
              "note": "earthquake-resistant (抗震的)；suspension bridge (懸索吊橋)。"
            },
            {
              "part": "spanning the turbulent oceanic strait",
              "role": "現在分詞片語修飾 (Participial Phrase)",
              "note": "span (橫跨)；turbulent (洶湧險惡的)；strait (海峽)。"
            }
          ],
          "keyPoints": [
            "【成對反義】：construct (建設) vs. destruct (破壞、摧毀；de- 消除)。",
            "【名詞衍生】：construction (營建業、構造物)、constructive (建設性的)。"
          ]
        }
      },
      {
        "word": "structure",
        "kk": "[ˈstrʌktʃɚ]",
        "ipa": "/ˈstrʌktʃər/",
        "pos": "n. / v.",
        "meaning": "(n.) 結構、體系、建築物；(v.) 組織安排",
        "formula": {
          "parts": [
            {
              "text": "struct",
              "role": "root",
              "meaning": "建造 (拉丁語 struere)"
            },
            {
              "text": "-ure",
              "role": "suffix",
              "meaning": "行為的結果、結構 (名詞字尾)"
            }
          ],
          "resultMeaning": "各部件按嚴謹規律堆疊形成的完整體系 ➔「結構、架構」"
        },
        "sentence": "The molecular structure of carbon nanotubes gives them extraordinary tensile strength and thermal conductivity.",
        "sentenceZh": "碳奈米管的分子結構賦予了它們超凡的抗拉強度與導熱性能。",
        "grammar": {
          "pattern": "S + Vt + IO + DO (主詞 + 雙賓及物動詞 + 間接受詞 + 直接受詞)",
          "breakdown": [
            {
              "part": "The molecular structure of carbon nanotubes",
              "role": "主詞 (Subject)",
              "note": "碳奈米管之分子結構。"
            },
            {
              "part": "gives",
              "role": "授與動詞 (Ditransitive Verb)",
              "note": "give + IO + DO。"
            },
            {
              "part": "them",
              "role": "間接受詞 (Indirect Object)",
              "note": "指代 nanotubes。"
            },
            {
              "part": "extraordinary tensile strength and thermal conductivity",
              "role": "直接受詞 (Direct Object)",
              "note": "tensile strength (抗拉伸強度)；thermal conductivity (導熱係數)。"
            }
          ],
          "keyPoints": [
            "【雙賓語五大句型】：S + V + IO + DO (授予某人/物某項屬性)。",
            "【專業物理字彙】：tensile (張力的、抗拉的)。"
          ]
        }
      },
      {
        "word": "infrastructure",
        "kk": "[ˈɪnfrəˌstrʌktʃɚ]",
        "ipa": "/ˈɪnfrəstrʌktʃər/",
        "pos": "n.",
        "meaning": "基礎設施、公共建設、底層架構",
        "formula": {
          "parts": [
            {
              "text": "infra-",
              "role": "prefix",
              "meaning": "在下方、基礎 (拉丁語 infra)"
            },
            {
              "text": "structure",
              "role": "base",
              "meaning": "結構建築 (拉丁語 struere)"
            }
          ],
          "resultMeaning": "支撐整個國家與社會在上層運轉的最底層實體骨幹 ➔「基礎設施」"
        },
        "sentence": "Modernizing water and electrical infrastructure requires multi-billion-dollar investments from both public and private sectors.",
        "sentenceZh": "自來水與電力基礎設施的現代化更新，需要來自公私部門數十億美元的龐大投資。",
        "grammar": {
          "pattern": "Gerund Subject + Vt + O + Prep Phrase (動名詞片語主詞 + 及物動詞 + 受詞 + 來源介系詞片語)",
          "breakdown": [
            {
              "part": "Modernizing water and electrical infrastructure",
              "role": "動名詞主詞 (Gerund Subject)",
              "note": "單數動名詞概念，謂語動詞加 s。"
            },
            {
              "part": "requires",
              "role": "及物動詞 (Transitive Verb)",
              "note": "需要。"
            },
            {
              "part": "multi-billion-dollar investments",
              "role": "直接受詞 (Direct Object)",
              "note": "複合形容詞修飾投資。"
            },
            {
              "part": "from both public and private sectors",
              "role": "來源介系詞片語 (Prepositional Phrase)",
              "note": "both A and B (公私部門雙方)。"
            }
          ],
          "keyPoints": [
            "【拉丁前綴 infra-】：意為「在...之下」，如 infrared (紅外線；在紅光頻率下方)。",
            "【經濟名詞】：critical infrastructure (關鍵基礎設施)。"
          ]
        }
      },
      {
        "word": "instruct",
        "kk": "[ɪnˈstrʌkt]",
        "ipa": "/ɪnˈstrʌkt/",
        "pos": "v.",
        "meaning": "指示、命令、教授、指導",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "向內、進入 (into, upon)"
            },
            {
              "text": "struct",
              "role": "root",
              "meaning": "建造、構築 (build)"
            }
          ],
          "resultMeaning": "在他人心中逐步構築知識體系或行動準則 ➔「指導、指示」"
        },
        "sentence": "The experienced pilot instructed the flight cadet on how to recover from an aerodynamic stall safely.",
        "sentenceZh": "經驗豐富的飛行員指導飛行學員如何安全地從空氣動力失速狀態中改出恢復。",
        "grammar": {
          "pattern": "S + Vt + O (cadet) + Prep Phrase (on how to V)",
          "breakdown": [
            {
              "part": "The experienced pilot",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "instructed",
              "role": "及物動詞 (Verb)",
              "note": "instruct someone on something。"
            },
            {
              "part": "the flight cadet",
              "role": "受詞 (Object)",
              "note": "cadet 意為「軍校學員、實習生」。"
            },
            {
              "part": "on how to recover from an aerodynamic stall safely",
              "role": "介系詞片語",
              "note": "on 表主題；how to recover 為疑問詞 + 不定詞片語。"
            }
          ],
          "keyPoints": [
            "【疑問詞 + 不定詞】：how to recover 作介系詞 on 的受詞，文法上等同於名詞子句 how he should recover。",
            "【名詞衍生】：instructor (講師、教練)、instruction (指引、指示)、instructive (有啟發性的)。"
          ]
        }
      },
      {
        "word": "destruct",
        "kk": "[dɪˈstrʌkt]",
        "ipa": "/dɪˈstrʌkt/",
        "pos": "v. / adj.",
        "meaning": "破壞、自毀；(adj.) 毀滅性的",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "向下、瓦解 (down, away)"
            },
            {
              "text": "struct",
              "role": "root",
              "meaning": "建造、建築 (build)"
            }
          ],
          "resultMeaning": "將原已構築好的物體徹底拆解垮塌 ➔「破壞、毀滅」"
        },
        "sentence": "If the test rocket deviates dangerously from its planned flight corridor, mission control can trigger its self-destruct mechanism.",
        "sentenceZh": "若測試火箭危險地偏離既定飛行走廊，任務控制中心可觸發其自毀機制。",
        "grammar": {
          "pattern": "Conditional Clause (If...) + S + Modal + Vt + O",
          "breakdown": [
            {
              "part": "If the test rocket deviates dangerously from its planned flight corridor",
              "role": "條件副詞子句",
              "note": "deviate from 表「偏離」。"
            },
            {
              "part": "mission control",
              "role": "主要句主詞 (Subject)",
              "note": "複合名詞「任務管制中心」。"
            },
            {
              "part": "can trigger",
              "role": "動詞片語 (Verb)",
              "note": "trigger (觸發、引動)。"
            },
            {
              "part": "its self-destruct mechanism",
              "role": "受詞 (Object)",
              "note": "self-destruct 在此複合修飾 mechanism。"
            }
          ],
          "keyPoints": [
            "【反義詞對】：construct (建造) vs. destruct / destroy (毀滅)。",
            "【常見複合名詞】：self-destruct button (自毀按鈕)、destructive behavior (破壞性行為)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Pillars of Civilization: The Legacy of Struct",
      "titleZh": "文明的基石：構築未來的宏偉架構",
      "intro": "人類文明就是一部不斷「堆疊與構築 (struct)」的歷程。從原始茅舍到現代超高摩天大樓與數位底層架構 (infrastructure)，結構支撐著夢想。",
      "paragraphs": [
        {
          "en": "Every monumental achievement begins with foundational planning. Civil engineers must first understand the geological forces beneath their feet before they can safely construct soaring bridges and sustainable transport systems.",
          "zh": "每項不朽的成就皆始於打好根基的規劃。土木工程師在能安全地建造高聳的橋樑與永續的運輸系統之前，必須先明晰腳下地質力量的運作。"
        },
        {
          "en": "Similarly, democratic societies flourish only when their constitutional structures remain resilient against tyranny. By continually modernizing both physical infrastructure and moral institutions, we build a scaffold for perpetual progress.",
          "zh": "同樣地，民主社會只有在其憲政結構對暴政保持堅韌抗性時才能蓬勃發展。藉由不斷現代化有形的基礎設施與無形的道德體制，我們為永續進步搭建了堅實的鷹架。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "When do democratic societies flourish according to the text?",
          "qZh": "根據文章，民主社會何時才能蓬勃發展？",
          "options": [
            "A. When their constitutional structures remain resilient against tyranny. (當其憲政結構對暴政保持堅韌抗性時)",
            "B. When all buildings are torn down.",
            "C. When libraries stop lending books.",
            "D. When roads are replaced by dirt paths."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「democratic societies flourish only when their constitutional structures remain resilient against tyranny」。"
        }
      ]
    }
  },
  {
    "id": "ject",
    "name": "ject",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「jacere」(投、擲、射、扔出)，過去分詞形為 jactum，複合時常轉為 -ject-。",
    "originMeaning": "投、擲、拋、射、扔出",
    "phonetic": "/dʒɛkt/",
    "icon": "🚀",
    "color": "#E11D48",
    "summary": "涵蓋拒絕扔回、注射射入、彈射噴出、投影射出及物體客觀存在的核心字根。",
    "words": [
      {
        "word": "reject",
        "kk": "[rɪˈdʒɛkt]",
        "ipa": "/rɪˈdʒɛkt/",
        "pos": "v. / n.",
        "meaning": "(v.) 拒絕、駁回、拋棄；(n.) 不合格品",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "回、向後 (拉丁語 re-)"
            },
            {
              "text": "ject",
              "role": "root",
              "meaning": "扔、拋 (拉丁語 jacere)"
            }
          ],
          "resultMeaning": "將不合適的提案或物品直接扔回去 ➔「拒絕、駁回」"
        },
        "sentence": "The university ethics committee voted unanimously to reject the controversial proposal due to safety hazards.",
        "sentenceZh": "大學倫理委員會一致表決駁回這項因存在安全隱患而引發爭議的提案。",
        "grammar": {
          "pattern": "S + Vi + Adv + Infinitive Object + Prep Phrase (主詞 + 不及物動詞 + 副詞 + 不定詞受詞 + 原因介系詞片語)",
          "breakdown": [
            {
              "part": "The university ethics committee",
              "role": "主詞 (Subject)",
              "note": "大學倫理委員會。"
            },
            {
              "part": "voted",
              "role": "動詞 (Verb)",
              "note": "vote to V (表決去做...)。"
            },
            {
              "part": "unanimously",
              "role": "方式副詞 (Adverb of Manner)",
              "note": "無異議地、全體一致地。"
            },
            {
              "part": "to reject the controversial proposal",
              "role": "不定詞受詞 (Infinitive)",
              "note": "reject (駁回)；controversial (具爭議的)。"
            },
            {
              "part": "due to safety hazards",
              "role": "原因介系詞片語 (Adverbial of Reason)",
              "note": "due to (因為、由於)；hazards (危害/隱患)。"
            }
          ],
          "keyPoints": [
            "【投票句型】：vote unanimously to V (一致投票贊成去...)。",
            "【原因介系詞】：due to / because of / owing to + Noun。"
          ]
        }
      },
      {
        "word": "inject",
        "kk": "[ɪnˈdʒɛkt]",
        "ipa": "/ɪnˈdʒekt/",
        "pos": "v.",
        "meaning": "注射、注入（資金、活力）、射入",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "進入、朝內 (拉丁語 in-)"
            },
            {
              "text": "ject",
              "role": "root",
              "meaning": "射、投 (拉丁語 jacere)"
            }
          ],
          "resultMeaning": "將藥劑或新活力深深射入內部 ➔「注射、注入」"
        },
        "sentence": "Venture capitalists injected fifty million dollars of seed funding into the promising green tech startup.",
        "sentenceZh": "創投家向這家前途光明的綠能科技新創公司注入了五千萬美元的種子資金。",
        "grammar": {
          "pattern": "S + Vt + O + into + Destination Phrase (主詞 + 及物動詞 + 受詞 + 注入目標介系詞片語)",
          "breakdown": [
            {
              "part": "Venture capitalists",
              "role": "主詞 (Subject)",
              "note": "創投資本家。"
            },
            {
              "part": "injected",
              "role": "及物動詞 (Transitive Verb)",
              "note": "inject A into B (將 A 注入 B)。"
            },
            {
              "part": "fifty million dollars of seed funding",
              "role": "直接受詞 (Direct Object)",
              "note": "種子輪創投資金。"
            },
            {
              "part": "into the promising green tech startup",
              "role": "接收目標介系詞片語 (Prepositional Phrase)",
              "note": "promising (大有可為的)；startup (新創公司)。"
            }
          ],
          "keyPoints": [
            "【商業與醫學雙用】：醫學上指 inject a vaccine (注射疫苗)；金融上指 inject capital (注入資本)。",
            "【衍生名詞】：injection (注射劑、注資行動)。"
          ]
        }
      },
      {
        "word": "eject",
        "kk": "[ɪˈdʒɛkt]",
        "ipa": "/ɪˈdʒekt/",
        "pos": "v.",
        "meaning": "彈出、逐出、噴射出",
        "formula": {
          "parts": [
            {
              "text": "e-",
              "role": "prefix",
              "meaning": "出、向外 (拉丁語 ex-)"
            },
            {
              "text": "ject",
              "role": "root",
              "meaning": "拋、投 (拉丁語 jacere)"
            }
          ],
          "resultMeaning": "在緊急狀況下將人員或物件向外猛力拋出 ➔「彈出、逐出」"
        },
        "sentence": "When catastrophic engine failure occurred, the fighter pilot pulled the emergency lever to eject safely from the cockpit.",
        "sentenceZh": "當災難性的發動機故障發生時，戰鬥機飛行員拉動緊急拉桿，安全地從駕駛艙彈射逃生。",
        "grammar": {
          "pattern": "Time Adverbial Clause + S + Vt + O + Infinitive of Purpose (時間副詞子句 + 主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "When catastrophic engine failure occurred",
              "role": "時間副詞子句 (Time Clause)",
              "note": "when 從屬連接詞；occurred (發生，不及物動詞)。"
            },
            {
              "part": "the fighter pilot",
              "role": "主要子句主詞 (Subject)",
              "note": "戰鬥機飛行員。"
            },
            {
              "part": "pulled",
              "role": "及物動詞 (Transitive Verb)",
              "note": "拉動。"
            },
            {
              "part": "the emergency lever",
              "role": "直接受詞 (Direct Object)",
              "note": "緊急控制桿。"
            },
            {
              "part": "to eject safely from the cockpit",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "eject (彈射)；cockpit (飛機駕駛艙)。"
            }
          ],
          "keyPoints": [
            "【航空專業術語】：ejection seat (彈射座椅)。",
            "【電腦光碟機/隨身碟】：安全退出硬體亦使用 Eject 指令！"
          ]
        }
      },
      {
        "word": "project",
        "kk": "[ˈprɑdʒɛkt]",
        "ipa": "/ˈprɑːdʒɛkt/",
        "pos": "n. / v.",
        "meaning": "專案、企劃；(v.) 投射、放映、預測",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前 (forward)"
            },
            {
              "text": "ject",
              "role": "root",
              "meaning": "拋、投 (throw)"
            }
          ],
          "resultMeaning": "向前拋擲出的構想，或將光線影像向前投射 ➔「專案企劃；投射、預測」"
        },
        "sentence": "Financial analysts project that quarterly revenues will surge significantly following the nationwide product rollout.",
        "sentenceZh": "財務分析師預測，隨著全國產品上市推廣，季度營收將大幅攀升。",
        "grammar": {
          "pattern": "S + Vt (project) + That Noun Clause (that revenues will surge...)",
          "breakdown": [
            {
              "part": "Financial analysts",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "project",
              "role": "及物動詞 (Verb)",
              "note": "重音在第二音節 [prəˈdʒɛkt]，意為「預測」。"
            },
            {
              "part": "that quarterly revenues will surge significantly",
              "role": "受詞名詞子句",
              "note": "that 引導子句；surge (激增) 為不及物動詞。"
            },
            {
              "part": "following the nationwide product rollout",
              "role": "時間介系詞片語",
              "note": "following 相當於 after。"
            }
          ],
          "keyPoints": [
            "【前名後動重音典範】：名詞 a project [ˈprɑdʒɛkt] vs. 動詞 to project [prəˈdʒɛkt]。",
            "【介系詞轉化】：following 常直接用作介系詞，意思等同於 after。"
          ]
        }
      },
      {
        "word": "subject",
        "kk": "[ˈsʌbdʒɪkt]",
        "ipa": "/ˈsʌbdʒɪkt/",
        "pos": "n. / v. / adj.",
        "meaning": "主題、學科、臣民、受試者；(v.) 使臣服、使遭受；(adj.) 易受...的",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方 (under)"
            },
            {
              "text": "ject",
              "role": "root",
              "meaning": "投擲 (throw)"
            }
          ],
          "resultMeaning": "投置於他人權威管轄之下的人 ➔「臣民、主題；(v.) 使臣服」"
        },
        "sentence": "All imported electrical appliances are subject to rigorous safety inspection before entering commercial retail markets.",
        "sentenceZh": "所有進口電器在進入商業零售市場前，皆須接受嚴格的安全檢驗。",
        "grammar": {
          "pattern": "S + Linking Verb (are) + Adj Phrase (subject to...) + Prep Phrase (before + V-ing)",
          "breakdown": [
            {
              "part": "All imported electrical appliances",
              "role": "主詞 (Subject)",
              "note": "imported 作形容詞修飾 appliances。"
            },
            {
              "part": "are",
              "role": "連綴動詞",
              "note": "現在式複數。"
            },
            {
              "part": "subject to rigorous safety inspection",
              "role": "主詞補語 (形容詞片語)",
              "note": "be subject to 意為「須蒙受、受...管轄拘束」。"
            },
            {
              "part": "before entering commercial retail markets",
              "role": "時間介系詞片語",
              "note": "before 為介系詞接動名詞 entering。"
            }
          ],
          "keyPoints": [
            "【核心片語】：be subject to + N. 表「視...而定、須接受...約束、易受...影響」，to 為介系詞。",
            "【重音變化】：名詞/形容詞 subject [ˈsʌbdʒɪkt] vs. 及物動詞 subject [səbˈdʒɛkt] (如 subject someone to torture)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Trajectory of Will: The Thrust of Ject",
      "titleZh": "意志的彈道軌跡：投射與射擊的哲思",
      "intro": "思想與命運如同被拋射出的箭矢 (ject)。我們拒絕 (reject) 虛假，向未來注入 (inject) 勇氣，在逆境中彈射 (eject) 昇華。",
      "paragraphs": [
        {
          "en": "Life constantly propels us forward into uncharted horizons. When obsolete doctrines threaten social progress, ethical citizens must boldly reject dogma and inject vibrant innovative thinking into civic dialogue.",
          "zh": "生活不斷驅使著我們向前邁入未知的地平線。當過時陳腐的信條威脅到社會進步時，具有良知的公民必須勇敢地駁回教條，並將蓬勃創新的思維注入公民對話中。"
        },
        {
          "en": "Like a pilot trained to eject from danger without hesitation, true wisdom lies in knowing when to abandon failing trajectories, preserving our vitality for tomorrow's bolder flights.",
          "zh": "就像受過嚴格訓練、在危險面前毫不猶豫彈射逃生的飛行員一樣，真正的智慧在於懂得何時放棄失敗的軌跡，為明日更英勇的翱翔儲存生命的生機。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What should ethical citizens do when obsolete doctrines threaten progress?",
          "qZh": "當過時信條威脅進步時，良知公民應當如何應對？",
          "options": [
            "A. Reject dogma and inject innovative thinking into civic dialogue. (駁回教條並將創新思維注入公民對話)",
            "B. Surrender and stop thinking completely.",
            "C. Close all schools and universities.",
            "D. Destroy digital computers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出公民應「boldly reject dogma and inject vibrant innovative thinking into civic dialogue」。"
        }
      ]
    }
  },
  {
    "id": "duc",
    "name": "duc / duct",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「ducere」(引導、率領、帶領)，過去分詞為 ductum。",
    "originMeaning": "引導、帶領、傳導、率領",
    "phonetic": "/dʌk/ 或 /dʌkt/",
    "icon": "🧭",
    "color": "#2563EB",
    "summary": "涵蓋教育啟蒙、引介、傳導能量、生產製造、扣除減少及演繹推理的核心字根。",
    "words": [
      {
        "word": "educate",
        "kk": "[ˈɛdʒʊˌket]",
        "ipa": "/ˈedʒukeɪt/",
        "pos": "v.",
        "meaning": "教育、啟發、培養",
        "formula": {
          "parts": [
            {
              "text": "e-",
              "role": "prefix",
              "meaning": "出、向外 (拉丁語 ex-)"
            },
            {
              "text": "duc",
              "role": "root",
              "meaning": "引導 (拉丁語 ducere)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "將一個人內心蘊藏的潛能與天賦引導誘發出來 ➔「教育、啟迪」"
        },
        "sentence": "Visionary universities educate aspiring scholars not merely to memorize facts, but to challenge orthodox assumptions.",
        "sentenceZh": "富有遠見的大學教育懷抱抱負的學者，不僅僅是背誦既定事實，更是去質疑正統傳統的預設前提。",
        "grammar": {
          "pattern": "S + Vt + O + not merely to V1 + but to V2 (主詞 + 及物動詞 + 受詞 + 不僅是去做1 + 更是去做2)",
          "breakdown": [
            {
              "part": "Visionary universities",
              "role": "主詞 (Subject)",
              "note": "有遠見的大學。"
            },
            {
              "part": "educate",
              "role": "及物動詞 (Transitive Verb)",
              "note": "及物動詞。"
            },
            {
              "part": "aspiring scholars",
              "role": "直接受詞 (Direct Object)",
              "note": "aspiring (有抱負的) 為現在分詞作形容詞。"
            },
            {
              "part": "not merely to memorize facts",
              "role": "對等目的不定詞 1 (Parallel Infinitive 1)",
              "note": "not merely (不僅僅)。"
            },
            {
              "part": "but to challenge orthodox assumptions",
              "role": "對等目的不定詞 2 (Parallel Infinitive 2)",
              "note": "but (而且/更)；orthodox (正統正宗的)；assumptions (假定)。"
            }
          ],
          "keyPoints": [
            "【平行對稱結構】：not merely to V1, but to V2 (不僅要...更要...)。",
            "【詞源哲學真諦】：教育 (education) 原意為「引導出來 (lead out)」，而非填鴨灌輸！"
          ]
        }
      },
      {
        "word": "conduct",
        "kk": "[kənˈdʌkt] (v.) / [ˈkɑndʌkt] (n.)",
        "ipa": "/kənˈdʌkt/ (v.) / /ˈkɑːndʌkt/ (n.)",
        "pos": "v. / n.",
        "meaning": "(v.) 執行、引導、指揮樂隊、導電；(n.) 行為品行",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同、一起 (拉丁語 com-)"
            },
            {
              "text": "duct",
              "role": "root",
              "meaning": "引導、帶領 (拉丁語 ducere)"
            }
          ],
          "resultMeaning": "帶領眾人整齊劃一地共同前進 ➔「執行、指揮、導引」"
        },
        "sentence": "Independent oversight commissions conduct rigorous inquiries to verify compliance with statutory environmental mandates.",
        "sentenceZh": "獨立監督委員會展開嚴謹調查，以核查是否恪遵法定環境指令規範。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Independent oversight commissions",
              "role": "主詞 (Subject)",
              "note": "獨立監督委員會。"
            },
            {
              "part": "conduct",
              "role": "及物動詞 (Transitive Verb)",
              "note": "執行進行。"
            },
            {
              "part": "rigorous inquiries",
              "role": "直接受詞 (Direct Object)",
              "note": "嚴密調查。"
            },
            {
              "part": "to verify compliance with statutory environmental mandates",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "verify (核實)；compliance with (恪遵)；statutory (法定的)。"
            }
          ],
          "keyPoints": [
            "【高頻商務搭配】：conduct research / inquiries / surveys (執行研究/調查)。",
            "【物理學衍生】：semiconductor (半導體；semi- 一半 + conductor 導體)。"
          ]
        }
      },
      {
        "word": "produce",
        "kk": "[prəˈdus] (v.) / [ˈprɑdus] (n.)",
        "ipa": "/prəˈduːs/ (v.) / /ˈproʊduːs/ (n.)",
        "pos": "v. / n.",
        "meaning": "(v.) 生產、製造、出示；(n.) 農產品",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前 (拉丁語 pro)"
            },
            {
              "text": "duce",
              "role": "root",
              "meaning": "引導、帶來 (拉丁語 ducere)"
            }
          ],
          "resultMeaning": "將原料帶向前台轉化為現成物品 ➔「生產、製造」"
        },
        "sentence": "Advanced vertical aeroponic farms produce abundant organic crops using ninety percent less water than traditional agriculture.",
        "sentenceZh": "先進的垂直氣霧耕農場運用比傳統農業少百分之九十的水資源，生產出充沛的有機作物。",
        "grammar": {
          "pattern": "S + Vt + O + Participial Comparative Adverbial (主詞 + 及物動詞 + 受詞 + 比較分詞狀詞)",
          "breakdown": [
            {
              "part": "Advanced vertical aeroponic farms",
              "role": "主詞 (Subject)",
              "note": "垂直氣霧耕農場。"
            },
            {
              "part": "produce",
              "role": "及物動詞 (Transitive Verb)",
              "note": "生產。"
            },
            {
              "part": "abundant organic crops",
              "role": "直接受詞 (Direct Object)",
              "note": "充沛有機農作物。"
            },
            {
              "part": "using ninety percent less water than traditional agriculture",
              "role": "方式比較狀詞 (Participial Phrase)",
              "note": "using 表手段；less water than... 表比較級。"
            }
          ],
          "keyPoints": [
            "【重音詞性轉換】：動詞重音在後 /prəˈduːs/；名詞重音在前 /ˈproʊduːs/（專指新鮮蔬果農產品）。",
            "【衍生名詞】：productivity (生產力)、production (生產作業)。"
          ]
        }
      },
      {
        "word": "introduce",
        "kk": "[ˌɪntrəˈdjus]",
        "ipa": "/ˌɪntrəˈduːs/",
        "pos": "v.",
        "meaning": "介紹、引進、採用、推行",
        "formula": {
          "parts": [
            {
              "text": "intro-",
              "role": "prefix",
              "meaning": "向內、進入 (within, inward)"
            },
            {
              "text": "duce",
              "role": "root",
              "meaning": "引導、帶領 (lead)"
            }
          ],
          "resultMeaning": "引導帶領某人或新事物進入新領域 ➔「介紹、引進」"
        },
        "sentence": "The hospital introduced a computerized triage algorithm to streamline patient intake and optimize emergency care.",
        "sentenceZh": "該醫院引進了一套電腦化檢傷分類演算法，以簡化病患接收流程並最佳化急診照護。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (to streamline... and optimize...)",
          "breakdown": [
            {
              "part": "The hospital",
              "role": "主詞 (Subject)",
              "note": "單數名詞。"
            },
            {
              "part": "introduced",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "a computerized triage algorithm",
              "role": "受詞 (Object)",
              "note": "computerized 為過去分詞形容詞「電腦化的」。"
            },
            {
              "part": "to streamline patient intake and optimize emergency care",
              "role": "不定詞目的狀語",
              "note": "and 連接兩個並列不定詞 streamline 與 optimize。"
            }
          ],
          "keyPoints": [
            "【名詞衍生】：introduction (介紹、引言)、introductory (入門的、序論的)。",
            "【字根家族】：conduce (有助於)、deduce (推論)、induce (誘導)、seduce (誘惑)。"
          ]
        }
      },
      {
        "word": "deduce",
        "kk": "[dɪˈdjus]",
        "ipa": "/dɪˈduːs/",
        "pos": "v.",
        "meaning": "推論、演繹、推斷",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "向下、自... (down from)"
            },
            {
              "text": "duce",
              "role": "root",
              "meaning": "引導 (lead)"
            }
          ],
          "resultMeaning": "自一般性前提向下引出具體結論 ➔「演繹、推斷」"
        },
        "sentence": "From the chemical residues left at the scene, forensic detectives were able to deduce the exact explosive compound used.",
        "sentenceZh": "從現場殘留的化學殘渣中，鑑識警探得以推斷出所使用的確切炸藥成分。",
        "grammar": {
          "pattern": "Prep Phrase + S + Modal Verb (were able to deduce) + O",
          "breakdown": [
            {
              "part": "From the chemical residues left at the scene",
              "role": "來源介系詞片語",
              "note": "left at the scene 為過去分詞片語修飾 residues。"
            },
            {
              "part": "forensic detectives",
              "role": "主詞 (Subject)",
              "note": "forensic (法醫鑑識的)。"
            },
            {
              "part": "were able to deduce",
              "role": "動詞片語 (Verb)",
              "note": "be able to 表能力。"
            },
            {
              "part": "the exact explosive compound used",
              "role": "受詞 (Object)",
              "note": "used 為過去分詞後位修飾 compound。"
            }
          ],
          "keyPoints": [
            "【邏輯哲學】：deduction (演繹法：由普遍到特殊) vs. induction (歸納法：由個別到普遍)。",
            "【分詞後位修飾】：residues (which were) left at the scene，後位分詞使句子簡潔凝鍊。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Guiding Light: The Leadership of Duc and Duct",
      "titleZh": "引領之光：導引與啟發的藝術",
      "intro": "字根 duc- 揭示了人類文明發展的核心動力：真正的偉大不在於強制統治，而在於啟發式的引導 (educate)。",
      "paragraphs": [
        {
          "en": "The ancient Latin root ducere reminds us that genuine education is never the forcible stuffing of inert data into passive minds; it is the art of leading latent potential outward into brilliance.",
          "zh": "古拉丁字根 ducere 提醒著我們：真正的教育從不是將僵死無生氣的數據強行塞進被動的大腦，而是將潛在的天賦引導向外、綻放光芒的崇高藝術。"
        },
        {
          "en": "From conducting complex scientific inquiries with integrity to producing sustainable agricultural yields, leaders who master the gentle art of guidance elevate human enterprise toward lasting enlightenment.",
          "zh": "從以正直誠信開展複雜的科學調查，到生產永續充沛的農業收穫，深諳溫和引導藝術的領導者將人類事業推向持久的啟蒙與繁榮。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What is genuine education according to the text?",
          "qZh": "根據文章，真正的教育是什麼？",
          "options": [
            "A. The art of leading latent potential outward into brilliance. (將潛在天賦引導向外綻放光芒的藝術)",
            "B. Forcibly stuffing inert data into passive minds.",
            "C. Buying expensive school uniforms.",
            "D. Memorizing encyclopedia page numbers."
          ],
          "answer": 0,
          "explanation": "文中第一段指出教育是「the art of leading latent potential outward into brilliance」。"
        }
      ]
    }
  },
  {
    "id": "capt",
    "name": "cap / capt / cept",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「capere」(抓取、捉拿、接收)，過去分詞形為 captum，複合字中常變形為 -cept- 或 -ceiv-。",
    "originMeaning": "抓取、捉拿、接收、領會",
    "phonetic": "/kæp/ 或 /kæpt/ 或 /sɛpt/",
    "icon": "🎣",
    "color": "#059669",
    "summary": "涵蓋俘獲逮捕、接受承納、概念領悟、攔截攔阻與感知感觸的核心字根。",
    "words": [
      {
        "word": "capture",
        "kk": "[ˈkæptʃɚ]",
        "ipa": "/ˈkæptʃər/",
        "pos": "v. / n.",
        "meaning": "(v.) 俘獲、捕獲、奪取、精確呈現；(n.) 捕獲",
        "formula": {
          "parts": [
            {
              "text": "capt",
              "role": "root",
              "meaning": "抓取 (拉丁語 capere)"
            },
            {
              "text": "-ure",
              "role": "suffix",
              "meaning": "行為、結果 (名詞/動詞字尾)"
            }
          ],
          "resultMeaning": "伸手用力將人、動物或影像抓牢 ➔「捕獲、俘獲、捕捉」"
        },
        "sentence": "Wildlife cinematographers waited patiently for weeks in sub-zero blizzards to capture footage of the elusive snow leopard.",
        "sentenceZh": "野生動物攝影師在零度以下的暴風雪中耐心守候了數週，只為捕捉那行蹤隱匿雪豹的珍貴鏡頭畫面。",
        "grammar": {
          "pattern": "S + Vi + Adv + Time Prep Phrase + Locative Phrase + Infinitive of Purpose (主詞 + 不及物動詞 + 副詞 + 時間片語 + 地點片語 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Wildlife cinematographers",
              "role": "主詞 (Subject)",
              "note": "野生動物攝影師。"
            },
            {
              "part": "waited",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "等待。"
            },
            {
              "part": "patiently",
              "role": "副詞 (Adverb of Manner)",
              "note": "耐心地。"
            },
            {
              "part": "for weeks in sub-zero blizzards",
              "role": "時間與環境狀詞 (Adverbials)",
              "note": "sub-zero (零度以下的)；blizzards (暴風雪)。"
            },
            {
              "part": "to capture footage of the elusive snow leopard",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "capture footage (捕捉鏡頭)；elusive (難以捉摸尋獲的)。"
            }
          ],
          "keyPoints": [
            "【比喻動詞】：capture 除了捕獲野獸，常指 capture the essence / mood (捕捉精髓/情調)。",
            "【同源變形】：captive (俘虜)、captivate (使著迷/俘獲芳心)。"
          ]
        }
      },
      {
        "word": "concept",
        "kk": "[ˈkɑnsɛpt]",
        "ipa": "/ˈkɑːnsept/",
        "pos": "n.",
        "meaning": "概念、觀念、思想雛形",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同、完全 (拉丁語 com-)"
            },
            {
              "text": "cept",
              "role": "root",
              "meaning": "抓取、領會 (拉丁語 capere)"
            }
          ],
          "resultMeaning": "在大腦心智中將事物的各項屬性抓攏融合 ➔「概念、觀念」"
        },
        "sentence": "Albert Einstein introduced the revolutionary concept that gravity results from the curvature of four-dimensional spacetime.",
        "sentenceZh": "愛因斯坦提出了革命性的概念：重力是由於四維時空的彎曲所造成的。",
        "grammar": {
          "pattern": "S + Vt + O + Appositive That-Clause (主詞 + 及物動詞 + 受詞 + 同位語名詞子句)",
          "breakdown": [
            {
              "part": "Albert Einstein",
              "role": "主詞 (Subject)",
              "note": "愛因斯坦。"
            },
            {
              "part": "introduced",
              "role": "及物動詞 (Transitive Verb)",
              "note": "引進提出。"
            },
            {
              "part": "the revolutionary concept",
              "role": "受詞 (Direct Object)",
              "note": "革命性概念。"
            },
            {
              "part": "that gravity results from the curvature of four-dimensional spacetime",
              "role": "同位語子句 (Appositive Clause)",
              "note": "that 為同位語連接詞，完整陳述 concept 之實質內容；result from (起因於)；curvature (曲率/彎曲)。"
            }
          ],
          "keyPoints": [
            "【同位語子句】：concept that + 完整子句 (進階英文寫作核心句型)。",
            "【動詞短語】：result from (由...引起) vs. result in (導致...結果)。"
          ]
        }
      },
      {
        "word": "intercept",
        "kk": "[ˌɪntɚˈsɛpt]",
        "ipa": "/ˌɪntərˈsept/",
        "pos": "v. / n.",
        "meaning": "攔截、截擊、截聽訊號",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間 (拉丁語 inter)"
            },
            {
              "text": "cept",
              "role": "root",
              "meaning": "抓取 (拉丁語 capere)"
            }
          ],
          "resultMeaning": "在目標物抵達目的地之前於半途出手抓截 ➔「攔截、截擊」"
        },
        "sentence": "Naval defense destroyers deployed radar-guided missiles to intercept incoming supersonic projectiles before they reached the fleet.",
        "sentenceZh": "海軍防衛驅逐艦發射雷達導引飛彈，在來襲的超音速砲彈抵達艦隊之前將其於半途攔截。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Time Clause (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 時間子句)",
          "breakdown": [
            {
              "part": "Naval defense destroyers",
              "role": "主詞 (Subject)",
              "note": "海軍防衛驅逐艦。"
            },
            {
              "part": "deployed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "部署發射。"
            },
            {
              "part": "radar-guided missiles",
              "role": "直接受詞 (Direct Object)",
              "note": "雷達導引飛彈。"
            },
            {
              "part": "to intercept incoming supersonic projectiles",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "incoming (來襲的)；supersonic (超音速的)；projectiles (拋射彈藥)。"
            },
            {
              "part": "before they reached the fleet",
              "role": "時間副詞子句 (Time Clause)",
              "note": "before 引導時間子句；reach 為及物動詞。"
            }
          ],
          "keyPoints": [
            "【前綴空間】：inter- (在兩者之間半路) + cept (抓取) = 半途攔截。",
            "【情報科技語境】：intercept an encrypted transmission (截獲一條加密通信)。"
          ]
        }
      },
      {
        "word": "accept",
        "kk": "[əkˈsɛpt]",
        "ipa": "/əkˈsɛpt/",
        "pos": "v.",
        "meaning": "接受、領受、認可、承認",
        "formula": {
          "parts": [
            {
              "text": "ac- (ad-)",
              "role": "prefix",
              "meaning": "朝向、往 (to, toward)"
            },
            {
              "text": "cept (cap)",
              "role": "root",
              "meaning": "拿取、捉握 (take, receive)"
            }
          ],
          "resultMeaning": "伸出雙手主動迎上前去拿取 ➔「接受、認可」"
        },
        "sentence": "The prestigious university offered him a full fellowship, which he gladly decided to accept without hesitation.",
        "sentenceZh": "這所享譽盛名的大學為他提供了全額獎學金，他毫不猶豫地欣然決定接受。",
        "grammar": {
          "pattern": "S1 + Vt1 + IO + DO + Non-restrictive Relative Clause (which he...)",
          "breakdown": [
            {
              "part": "The prestigious university",
              "role": "主詞 (Subject)",
              "note": "prestigious (聲望崇高的)。"
            },
            {
              "part": "offered",
              "role": "授與動詞 (Ditransitive Verb)",
              "note": "offer + 人 + 物。"
            },
            {
              "part": "him",
              "role": "間接受詞 (Indirect Object)",
              "note": "代名詞受格。"
            },
            {
              "part": "a full fellowship",
              "role": "直接受詞 (Direct Object)",
              "note": "fellowship (研究獎學金)。"
            },
            {
              "part": "which he gladly decided to accept without hesitation",
              "role": "非限定關係代名詞子句",
              "note": "which 指稱 fellowship 作 accept 之受詞。"
            }
          ],
          "keyPoints": [
            "【易混淆字】：accept (接受) vs. except (除...之外)。",
            "【同根派生】：acceptable (可接受的)、acceptance (接受、認同)。"
          ]
        }
      },
      {
        "word": "susceptible",
        "kk": "[səˈsɛptəb!]",
        "ipa": "/səˈsɛptəbl/",
        "pos": "adj.",
        "meaning": "易受影響的、易受感染的、過敏的",
        "formula": {
          "parts": [
            {
              "text": "sus- (sub-)",
              "role": "prefix",
              "meaning": "在下方 (under)"
            },
            {
              "text": "cept",
              "role": "root",
              "meaning": "抓取、承受 (take, receive)"
            },
            {
              "text": "-ible",
              "role": "suffix",
              "meaning": "能夠被...的形容詞字尾"
            }
          ],
          "resultMeaning": "處在下方極容易被外界病原或情緒抓住影響的 ➔「易受感染的、脆弱的」"
        },
        "sentence": "Unvaccinated elderly individuals remain exceptionally susceptible to severe respiratory infections during the winter months.",
        "sentenceZh": "未接種疫苗的年長者在冬季期間對嚴重的呼吸道感染依然極其脆弱易感。",
        "grammar": {
          "pattern": "S + Linking Verb (remain) + SC (susceptible to...) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "Unvaccinated elderly individuals",
              "role": "主詞 (Subject)",
              "note": "unvaccinated (未接種疫苗的)。"
            },
            {
              "part": "remain",
              "role": "連綴動詞 (Linking Verb)",
              "note": "表狀態持續。"
            },
            {
              "part": "exceptionally susceptible to severe respiratory infections",
              "role": "主詞補語 (形容詞片語)",
              "note": "exceptionally (格外地)；susceptible to 為固定介系詞搭配。"
            },
            {
              "part": "during the winter months",
              "role": "時間介系詞片語",
              "note": "修飾感染高發期。"
            }
          ],
          "keyPoints": [
            "【介系詞搭配】：susceptible to + N. (易受...傷害或感染的)，to 必為介系詞！",
            "【近義詞辨析】：vulnerable to (易脆弱受傷的)、prone to (傾向於...的)。"
          ]
        }
      }
    ],
    "article": {
      "title": "Grasping Reality: The Architecture of Capt and Cept",
      "titleZh": "捉捕真實：領悟與掌握的心智旅程",
      "intro": "從原始獵人捕獲 (capture) 獵物，到現代物理學家領會抽象概念 (concept)，字根 cap- 代表人類心智伸出雙手掌握世界的野心。",
      "paragraphs": [
        {
          "en": "To grasp an idea is fundamentally an act of mental hunting. When early philosophers formulated the first mathematical concepts, they captured universal truths that had hovered invisibly since the dawn of creation.",
          "zh": "掌握一個思想本質上是一場心靈的狩獵。當早期哲學家構想出最早的數學概念時，他們捕獲了自創世以來便隱隱漂浮於虛空之中的宇宙真理。"
        },
        {
          "en": "In modern defense and cybersecurity, our survival depends upon the ability to intercept malicious threats before they inflict damage, proving that our capacity to seize the moment defines civilization's endurance.",
          "zh": "在現代國防與網路安全中，我們的生存仰賴於在惡意威脅造成破壞之前將其成功攔截的能力，證明了我們審時度勢、把握當下的實力定義了文明的存續。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What did early philosophers capture when formulating mathematical concepts?",
          "qZh": "早期哲學家在構想數學概念時捕獲了什麼？",
          "options": [
            "A. Universal truths that had hovered invisibly since the dawn of creation. (自創世以來便隱隱漂浮的宇宙真理)",
            "B. Large physical herds of elephants.",
            "C. Golden coins minted by emperors.",
            "D. Cold winter snowfalls."
          ],
          "answer": 0,
          "explanation": "文中第一段指出哲學家「captured universal truths that had hovered invisibly since the dawn of creation」。"
        }
      ]
    }
  },
  {
    "id": "ced",
    "name": "ced / ceed / cess",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「cedere」(走、前進、讓步、退讓)，過去分詞為 cessum。",
    "originMeaning": "走、前進、讓步、通達",
    "phonetic": "/siːd/ 或 /sɛs/",
    "icon": "🚶",
    "color": "#4F46E5",
    "summary": "涵蓋前進繼續、走在前面超越、取得通行權限、經濟衰退及妥協讓步。",
    "words": [
      {
        "word": "proceed",
        "kk": "[prəˈsid]",
        "ipa": "/prəˈsiːd/",
        "pos": "v.",
        "meaning": "繼續進行、前進、著手進行",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前 (拉丁語 pro)"
            },
            {
              "text": "ceed",
              "role": "root",
              "meaning": "走 (拉丁語 cedere)"
            }
          ],
          "resultMeaning": "跨出腳步往前走 ➔「前進、繼續進行」"
        },
        "sentence": "After passing rigorous safety checks, the space crew received final clearance to proceed with the launch countdown.",
        "sentenceZh": "在通過嚴格的安全檢查後，太空人員獲得了繼續進行發射倒數計時的最終許可。",
        "grammar": {
          "pattern": "Prepositional Gerund Adverbial + S + Vt + O + Infinitive Complement (介系詞動名詞狀詞 + 主詞 + 及物動詞 + 受詞 + 不定詞補語)",
          "breakdown": [
            {
              "part": "After passing rigorous safety checks",
              "role": "時間狀詞 (Time Adverbial)",
              "note": "After 後接動名詞 passing。"
            },
            {
              "part": "the space crew",
              "role": "主詞 (Subject)",
              "note": "太空機組人員 (集合名詞)。"
            },
            {
              "part": "received",
              "role": "及物動詞 (Transitive Verb)",
              "note": "獲得。"
            },
            {
              "part": "final clearance",
              "role": "直接受詞 (Direct Object)",
              "note": "最終許可放行。"
            },
            {
              "part": "to proceed with the launch countdown",
              "role": "不定詞補語 (Infinitive Complement)",
              "note": "proceed with... (繼續進行某事)；launch countdown (發射倒數)。"
            }
          ],
          "keyPoints": [
            "【固定搭配介系詞】：proceed with something (繼續著手進行某事)；proceed to a place (前往某地)。",
            "【易混淆同音字】：proceed (前進) vs. precede (走在...之前)。"
          ]
        }
      },
      {
        "word": "access",
        "kk": "[ˈæksɛs]",
        "ipa": "/ˈækses/",
        "pos": "n. / v.",
        "meaning": "(n.) 進入權限、通道、查閱權；(v.) 獲取、讀取",
        "formula": {
          "parts": [
            {
              "text": "ac-",
              "role": "prefix",
              "meaning": "朝向 (拉丁語 ad-)"
            },
            {
              "text": "cess",
              "role": "root",
              "meaning": "走 (拉丁語 cedere)"
            }
          ],
          "resultMeaning": "能夠走進某個場所或資料庫的途徑 ➔「進入權、存取」"
        },
        "sentence": "Strict biometric encryption ensures that only authorized personnel gain access to classified government servers.",
        "sentenceZh": "嚴密的生物辨識加密技術確保只有經授權人員才能取得存取機密政府伺服器的權限。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause (主詞 + 及物動詞 + That名詞子句受詞)",
          "breakdown": [
            {
              "part": "Strict biometric encryption",
              "role": "主詞 (Subject)",
              "note": "嚴格生物辨識加密。"
            },
            {
              "part": "ensures",
              "role": "及物動詞 (Transitive Verb)",
              "note": "確保。"
            },
            {
              "part": "that only authorized personnel gain access to classified government servers",
              "role": "名詞子句 (Noun Clause)",
              "note": "authorized (經授權的)；gain access to (取得進入/使用...的權限)；classified (機密的)。"
            }
          ],
          "keyPoints": [
            "【不可數與介系詞搭配】：gain / have access to + Noun (取得對...的存取權，介系詞必用 to)。",
            "【形容詞形式】：accessible (易接近的、無障礙的)。"
          ]
        }
      },
      {
        "word": "recession",
        "kk": "[rɪˈsɛʃən]",
        "ipa": "/rɪˈseʃn/",
        "pos": "n.",
        "meaning": "經濟衰退、後退、撤回",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "向後 (拉丁語 re-)"
            },
            {
              "text": "cess",
              "role": "root",
              "meaning": "走 (拉丁語 cedere)"
            },
            {
              "text": "-ion",
              "role": "suffix",
              "meaning": "狀態 (名詞字尾)"
            }
          ],
          "resultMeaning": "經濟繁榮腳步倒退不前 ➔「經濟衰退、蕭條」"
        },
        "sentence": "Central banks lowered benchmark interest rates to stimulate business hiring during the global economic recession.",
        "sentenceZh": "央行調降基準利率，以在眼前這場全球經濟衰退期間刺激企業聘僱力道。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Time Prep Phrase (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 時間介系詞片語)",
          "breakdown": [
            {
              "part": "Central banks",
              "role": "主詞 (Subject)",
              "note": "各國央行。"
            },
            {
              "part": "lowered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "調降。"
            },
            {
              "part": "benchmark interest rates",
              "role": "直接受詞 (Direct Object)",
              "note": "基準利率。"
            },
            {
              "part": "to stimulate business hiring",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "stimulate (激勵/刺激)；hiring (招募僱用)。"
            },
            {
              "part": "during the global economic recession",
              "role": "時間介系詞片語 (Time Phrase)",
              "note": "recession (經濟衰退)。"
            }
          ],
          "keyPoints": [
            "【經濟學嚴謹定義】：連續兩個季度 GDP 負成長通常被定義為 recession。",
            "【同根對比】：process (前進進程) vs. recession (後退衰退)。"
          ]
        }
      },
      {
        "word": "precede",
        "kk": "[prɪˈsid]",
        "ipa": "/prɪˈsiːd/",
        "pos": "v.",
        "meaning": "在...之前、早於、先於",
        "formula": {
          "parts": [
            {
              "text": "pre-",
              "role": "prefix",
              "meaning": "在...之前 (before)"
            },
            {
              "text": "cede",
              "role": "root",
              "meaning": "走、行進 (go)"
            }
          ],
          "resultMeaning": "走在其他人或事件的前面 ➔「在...之前、先於」"
        },
        "sentence": "A brief period of heavy silence usually precedes the sudden arrival of a torrential summer thunderstorm.",
        "sentenceZh": "短暫沉重的寂靜通常預示著夏季狂暴雷陣雨的突降。",
        "grammar": {
          "pattern": "S + Adv + Vt (precedes) + O",
          "breakdown": [
            {
              "part": "A brief period of heavy silence",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "usually",
              "role": "頻率副詞",
              "note": "修飾動詞 precedes。"
            },
            {
              "part": "precedes",
              "role": "及物動詞 (Verb)",
              "note": "第三人稱單數現在式。"
            },
            {
              "part": "the sudden arrival of a torrential summer thunderstorm",
              "role": "受詞 (Object)",
              "note": "torrential (傾盆狂暴的) 修飾 thunderstorm。"
            }
          ],
          "keyPoints": [
            "【同源詞派生】：precedent (先例)、unprecedented (史無前例的)。",
            "【及物動詞用法】：precede 為及物動詞，直接接賓語，不需加介系詞 before。"
          ]
        }
      },
      {
        "word": "exceed",
        "kk": "[ɪkˈsid]",
        "ipa": "/ɪkˈsiːd/",
        "pos": "v.",
        "meaning": "超過、超越、勝過",
        "formula": {
          "parts": [
            {
              "text": "ex-",
              "role": "prefix",
              "meaning": "向外、超出 (out, beyond)"
            },
            {
              "text": "ceed",
              "role": "root",
              "meaning": "行進、走 (go)"
            }
          ],
          "resultMeaning": "走出界線之外、跨越門檻 ➔「超越、超過」"
        },
        "sentence": "Quarterly sales figures exceeded the most optimistic forecasts formulated by Wall Street analysts.",
        "sentenceZh": "季度銷售額超過了華爾街分析師所做出的最樂觀預測。",
        "grammar": {
          "pattern": "S + Vt + O + Participle Phrase (formulated by...)",
          "breakdown": [
            {
              "part": "Quarterly sales figures",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "exceeded",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "the most optimistic forecasts",
              "role": "直接受詞 (Direct Object)",
              "note": "最高級 most optimistic。"
            },
            {
              "part": "formulated by Wall Street analysts",
              "role": "過去分詞片語修飾 forecasts",
              "note": "formulate (制定、構思)。"
            }
          ],
          "keyPoints": [
            "【副詞衍生】：exceedingly (極其、非常，如 exceedingly difficult)。",
            "【及物動詞】：exceed 直接加受詞，不可加 than。"
          ]
        }
      }
    ],
    "article": {
      "title": "The March of Destiny: The Movement of Cede and Cess",
      "titleZh": "命運的步伐：進退通達的律動",
      "intro": "前進 (proceed)、通達 (access) 與暫時的退步 (recession)，構成了人類歷史如鐘擺般的律動。",
      "paragraphs": [
        {
          "en": "Progress is rarely a straight line; it is a dynamic rhythm of advance and concession. When societies experience an economic recession, resilient leaders refuse to despair, restructuring institutions so that subsequent generations may proceed with greater confidence.",
          "zh": "進步鮮少是一條筆直的坦途，而是一場前進與退讓交織的動態節奏。當社會經歷經濟衰退時，堅韌的領導者拒絕陷入絕望，而是重組體制，以便後續世代能以更堅定的信心繼續前行。"
        },
        {
          "en": "By guaranteeing universal access to knowledge and justice, we pave a broad avenue where every individual can succeed, proving that the courage to move forward defines the human spirit.",
          "zh": "藉由保障所有人獲取知識與正義的普遍途徑，我們鋪就了一條讓每個人都能獲得成功的寬廣康莊大道，證明了勇往直前的氣魄定義了人類的精神。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What do resilient leaders do during an economic recession?",
          "qZh": "堅韌的領導者在經濟衰退時會怎麼做？",
          "options": [
            "A. Restructure institutions so future generations proceed with confidence. (重組體制以便後代自信前行)",
            "B. Give up and resign immediately.",
            "C. Stop all school education.",
            "D. Burn all books in public squares."
          ],
          "answer": 0,
          "explanation": "文中第一段指出領導者會「restructuring institutions so that subsequent generations may proceed with greater confidence」。"
        }
      ]
    }
  },
  {
    "id": "mit",
    "name": "mit / miss",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「mittere」(派遣、發送、送出、放行)，過去分詞形為 missum。",
    "originMeaning": "送、派遣、發射、放行",
    "phonetic": "/mɪt/ 或 /mɪs/",
    "icon": "✉️",
    "color": "#0891B2",
    "summary": "涵蓋傳送發射、承認接納、散發排出、允許放行、使命任務與承諾投入。",
    "words": [
      {
        "word": "transmit",
        "kk": "[trænsˈmɪt]",
        "ipa": "/trænzˈmɪt/",
        "pos": "v.",
        "meaning": "傳送、傳播、傳輸（信號、疾病、能量）",
        "formula": {
          "parts": [
            {
              "text": "trans-",
              "role": "prefix",
              "meaning": "跨越、穿過 (拉丁語 trans-)"
            },
            {
              "text": "mit",
              "role": "root",
              "meaning": "送 (拉丁語 mittere)"
            }
          ],
          "resultMeaning": "將訊號或物質跨越空間距離發送出去 ➔「傳送、傳輸」"
        },
        "sentence": "Deep-space radio arrays transmit ultra-high-frequency telemetry across millions of kilometers of interplanetary void.",
        "sentenceZh": "深空無線電陣列跨越數百萬公里的行星際虛空，傳輸超高頻遙測資料。",
        "grammar": {
          "pattern": "S + Vt + O + across-Directional Phrase (主詞 + 及物動詞 + 受詞 + 跨越空間介系詞片語)",
          "breakdown": [
            {
              "part": "Deep-space radio arrays",
              "role": "主詞 (Subject)",
              "note": "深空無線電陣列天線。"
            },
            {
              "part": "transmit",
              "role": "及物動詞 (Transitive Verb)",
              "note": "傳輸。"
            },
            {
              "part": "ultra-high-frequency telemetry",
              "role": "直接受詞 (Direct Object)",
              "note": "超高頻遙測資訊。"
            },
            {
              "part": "across millions of kilometers of interplanetary void",
              "role": "空間介系詞片語 (Directional Phrase)",
              "note": "across (跨越)；interplanetary void (行星際虛空)。"
            }
          ],
          "keyPoints": [
            "【醫學與通訊雙高頻】：transmit a virus (傳播病毒)；transmit data (傳輸數據)。",
            "【名詞衍生】：transmission (變速箱、傳播、發射)。"
          ]
        }
      },
      {
        "word": "mission",
        "kk": "[ˈmɪʃən]",
        "ipa": "/ˈmɪʃn/",
        "pos": "n.",
        "meaning": "使命、任務、代表團、太空飛行任務",
        "formula": {
          "parts": [
            {
              "text": "miss",
              "role": "root",
              "meaning": "派遣、發送 (拉丁語 mittere)"
            },
            {
              "text": "-ion",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "被長官或國家賦予重任派遣出去完成的目標 ➔「使命、任務」"
        },
        "sentence": "The humanitarian medical mission delivered vital vaccines to children living in remote equatorial archipelagos.",
        "sentenceZh": "這支人道醫療代表團將關鍵疫苗運送給生活在偏遠赤道群島上的孩童。",
        "grammar": {
          "pattern": "S + Vt + O + to-Recipient Phrase + Participle Modifier (主詞 + 及物動詞 + 受詞 + 接收對象片語 + 現在分詞修飾)",
          "breakdown": [
            {
              "part": "The humanitarian medical mission",
              "role": "主詞 (Subject)",
              "note": "人道醫療任務團。"
            },
            {
              "part": "delivered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "運送分發。"
            },
            {
              "part": "vital vaccines",
              "role": "直接受詞 (Direct Object)",
              "note": "vital (至關重要的) 修飾疫苗。"
            },
            {
              "part": "to children",
              "role": "受贈者介系詞片語 (Prepositional Object)",
              "note": "to 表對象。"
            },
            {
              "part": "living in remote equatorial archipelagos",
              "role": "現在分詞後位修飾 (Participial Modifier)",
              "note": "修飾 children；equatorial archipelagos (赤道群島)。"
            }
          ],
          "keyPoints": [
            "【商務常見語彙】：mission statement (企業宗旨聲明/使命宣言)。",
            "【航太用語】：mission control (任務控制中心)。"
          ]
        }
      },
      {
        "word": "dismiss",
        "kk": "[dɪsˈmɪs]",
        "ipa": "/dɪsˈmɪs/",
        "pos": "v.",
        "meaning": "駁回、解散、開除、不予考慮",
        "formula": {
          "parts": [
            {
              "text": "dis-",
              "role": "prefix",
              "meaning": "分開、離開 (拉丁語 dis-)"
            },
            {
              "text": "miss",
              "role": "root",
              "meaning": "送出 (拉丁語 mittere)"
            }
          ],
          "resultMeaning": "讓集結的人員分散走開，或將無稽之談直接送走拋在一旁 ➔「解散、駁回」"
        },
        "sentence": "The federal appellate judge dismissed the baseless lawsuit without prejudice due to lack of evidence.",
        "sentenceZh": "聯邦上訴法院法官以缺乏證據為由，裁定駁回這起毫無根據的訴訟（保留再次起訴權利）。",
        "grammar": {
          "pattern": "S + Vt + O + Adverbial Idiom + Reason Phrase (主詞 + 及物動詞 + 受詞 + 法律成語狀詞 + 原因介系詞片語)",
          "breakdown": [
            {
              "part": "The federal appellate judge",
              "role": "主詞 (Subject)",
              "note": "聯邦上訴法院法官。"
            },
            {
              "part": "dismissed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "駁回訴訟。"
            },
            {
              "part": "the baseless lawsuit",
              "role": "直接受詞 (Direct Object)",
              "note": "baseless (毫無根據的)；lawsuit (訴訟案)。"
            },
            {
              "part": "without prejudice",
              "role": "法律成語狀詞 (Legal Idiom)",
              "note": "無實體裁決確定效力/保留權利地。"
            },
            {
              "part": "due to lack of evidence",
              "role": "原因狀詞 (Adverbial of Reason)",
              "note": "due to (因)；lack of evidence (缺乏證據)。"
            }
          ],
          "keyPoints": [
            "【職場與法律雙義】：在職場指 dismiss an employee (開除解雇)；在法庭指 dismiss a charge/case (撤案駁回)。",
            "【心理心態】：dismiss an idea (對某想法不予採納/視為無稽之談)。"
          ]
        }
      },
      {
        "word": "submit",
        "kk": "[səbˈmɪt]",
        "ipa": "/səbˈmɪt/",
        "pos": "v.",
        "meaning": "提交、呈遞；(與 to 連用) 屈服、順從",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方 (under)"
            },
            {
              "text": "mit",
              "role": "root",
              "meaning": "送出 (send)"
            }
          ],
          "resultMeaning": "將文件自下而上呈遞給主管；或將自己置於他人管轄之下 ➔「提交；屈服」"
        },
        "sentence": "Applicants are required to submit their certified academic transcripts before the midnight deadline.",
        "sentenceZh": "申請人必須在午夜截止時間之前提交經認證的學業成績單。",
        "grammar": {
          "pattern": "S + Passive Verb (are required) + to-V (to submit O) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "Applicants",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "are required to submit",
              "role": "被動態謂語",
              "note": "require someone to do something 的被動式。"
            },
            {
              "part": "their certified academic transcripts",
              "role": "受詞 (Object)",
              "note": "certified (認證的) 修飾 transcripts (成績單)。"
            },
            {
              "part": "before the midnight deadline",
              "role": "時間介系詞片語",
              "note": "before 表截止期限之前。"
            }
          ],
          "keyPoints": [
            "【詞義雙軌】：submit a proposal (提交提案) vs. submit to authority (屈服於權威)。",
            "【雙寫字母規則】：submitted, submitting, submission (名詞)。"
          ]
        }
      },
      {
        "word": "admit",
        "kk": "[ədˈmɪt]",
        "ipa": "/ədˈmɪt/",
        "pos": "v.",
        "meaning": "承認、准許進入、收容",
        "formula": {
          "parts": [
            {
              "text": "ad-",
              "role": "prefix",
              "meaning": "朝向、往 (to, toward)"
            },
            {
              "text": "mit",
              "role": "root",
              "meaning": "放行、送出 (send, let go)"
            }
          ],
          "resultMeaning": "朝著某人放行、准許其走入大門 ➔「准許進入、承認」"
        },
        "sentence": "After intense interrogation, the defendant reluctantly admitted taking the confidential documents from the corporate archive.",
        "sentenceZh": "經過嚴厲訊問後，被告勉強承認從公司檔案館拿走了機密文件。",
        "grammar": {
          "pattern": "Prep Phrase + S + Adv + Vt (admitted) + Gerund Phrase (taking O...)",
          "breakdown": [
            {
              "part": "After intense interrogation",
              "role": "時間介系詞片語",
              "note": "interrogation (訊問、審訊)。"
            },
            {
              "part": "the defendant",
              "role": "主詞 (Subject)",
              "note": "「被告」。"
            },
            {
              "part": "reluctantly",
              "role": "情狀副詞",
              "note": "修飾 admitted。"
            },
            {
              "part": "admitted",
              "role": "及物動詞 (Verb)",
              "note": "admit 後接動名詞 (V-ing) 作受詞。"
            },
            {
              "part": "taking the confidential documents from the corporate archive",
              "role": "動名詞片語受詞",
              "note": "taking 接受詞 documents。"
            }
          ],
          "keyPoints": [
            "【文法關鍵】：admit 後接動名詞 (admit doing something) 或 that 子句，不可接 to + 原形動詞！",
            "【名詞衍生】：admission (入場費、准許入學、自白坦承)。"
          ]
        }
      }
    ],
    "article": {
      "title": "Messengers Across the Stars: The Delivery of Mit and Miss",
      "titleZh": "跨越星海的信使：發送與使命的遠征",
      "intro": "從古代奔馳萬里的傳令驛馬，到穿越深空發射 (transmit) 訊號的探測飛船，字根 mit- 承載著人類派遣與使命 (mission) 的永恆渴望。",
      "paragraphs": [
        {
          "en": "Human progress has always depended on our capacity to send forth ideas and resources. When humanitarian teams embark on emergency medical missions, they transmit not merely life-saving supplies, but profound hope to stranded populations.",
          "zh": "人類的進步始終仰賴於我們向外發送思想與資源的能力。當人道救援團隊啟程執行緊急醫療任務時，他們所傳遞的不僅僅是救命物資，更向受困群眾傳送了深沉而堅定的希望。"
        },
        {
          "en": "At the same time, maintaining intellectual clarity requires us to promptly dismiss groundless falsehoods, ensuring that the signals we beam into the future remain authentic and resonant.",
          "zh": "與此同時，保持心智的澄澈明晰要求我們及時摒棄毫無根據的虛妄言論，以確保我們向未來發送的信號永遠真實而深具共鳴。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What do humanitarian teams transmit besides life-saving supplies?",
          "qZh": "人道團隊除了救命物資之外還傳送了什麼？",
          "options": [
            "A. Profound hope to stranded populations. (向受困群眾傳送深沉的希望)",
            "B. Heavy golden bricks.",
            "C. Ancient stone weapons.",
            "D. Poisonous chemical gas."
          ],
          "answer": 0,
          "explanation": "文中第一段指出他們「transmit not merely life-saving supplies, but profound hope to stranded populations」。"
        }
      ]
    }
  },
  {
    "id": "cred",
    "name": "cred",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「credere」(相信、信任、託付)。",
    "originMeaning": "相信、信任、信用、信譽",
    "phonetic": "/krɛd/",
    "icon": "🤝",
    "color": "#059669",
    "summary": "涵蓋信用憑據、可信度、難以置信的奇蹟、宗教信條與專業證照證書。",
    "words": [
      {
        "word": "credible",
        "kk": "[ˈkrɛdəb!]",
        "ipa": "/ˈkredəbl/",
        "pos": "adj.",
        "meaning": "可信的、可靠的、令人信服的",
        "formula": {
          "parts": [
            {
              "text": "cred",
              "role": "root",
              "meaning": "相信 (拉丁語 credere)"
            },
            {
              "text": "-ible",
              "role": "suffix",
              "meaning": "能夠...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "足以被他人完全信賴相信的 ➔「可信的、可靠的」"
        },
        "sentence": "Investigative journalists corroborate multiple independent sources before publishing credible reports on political corruption.",
        "sentenceZh": "調查記者在發表有關政治腐敗的可靠報導之前，會先向多方獨立消息來源進行核實確證。",
        "grammar": {
          "pattern": "S + Vt + O + Prepositional Gerund Time Clause (主詞 + 及物動詞 + 受詞 + 介系詞動名詞時間狀詞)",
          "breakdown": [
            {
              "part": "Investigative journalists",
              "role": "主詞 (Subject)",
              "note": "調查記者。"
            },
            {
              "part": "corroborate",
              "role": "及物動詞 (Transitive Verb)",
              "note": "核實、證實 (高階及物動詞)。"
            },
            {
              "part": "multiple independent sources",
              "role": "直接受詞 (Direct Object)",
              "note": "多方獨立消息來源。"
            },
            {
              "part": "before publishing credible reports on political corruption",
              "role": "時間狀詞 (Time Phrase)",
              "note": "before 作介系詞接動名詞 publishing；credible (可信的)；corruption (貪腐)。"
            }
          ],
          "keyPoints": [
            "【反義成對詞】：credible (可信的) vs. incredible (難以置信的/驚人的)。",
            "【衍生名詞】：credibility (可信度、信譽；如 credibility gap 信任差距)。"
          ]
        }
      },
      {
        "word": "credential",
        "kk": "[krəˈdɛnʃəl]",
        "ipa": "/krəˈdenʃl/",
        "pos": "n.",
        "meaning": "憑證、證書、資歷證明（常用複數 credentials）",
        "formula": {
          "parts": [
            {
              "text": "cred",
              "role": "root",
              "meaning": "信任 (拉丁語 credere)"
            },
            {
              "text": "-ential",
              "role": "suffix",
              "meaning": "具有...性質的事物 (名詞字尾)"
            }
          ],
          "resultMeaning": "用以證明個人身分與能力值得被信任的文件 ➔「憑證、資歷證明」"
        },
        "sentence": "The cyber-security system validates digital credentials before granting access to confidential cloud databases.",
        "sentenceZh": "資安系統在授予機密雲端資料庫存取權限之前，會先驗證數位憑證。",
        "grammar": {
          "pattern": "S + Vt + O + Time Prepositional Gerund (主詞 + 及物動詞 + 受詞 + 時間介系詞動名詞片語)",
          "breakdown": [
            {
              "part": "The cyber-security system",
              "role": "主詞 (Subject)",
              "note": "網路安全系統。"
            },
            {
              "part": "validates",
              "role": "及物動詞 (Transitive Verb)",
              "note": "驗證核可。"
            },
            {
              "part": "digital credentials",
              "role": "直接受詞 (Direct Object)",
              "note": "數位憑證/密碼身分認證。"
            },
            {
              "part": "before granting access to confidential cloud databases",
              "role": "時間狀詞 (Time Phrase)",
              "note": "grant access to (授予存取權限)；confidential (機密的)。"
            }
          ],
          "keyPoints": [
            "【資訊安全高頻】：login credentials 專指使用者登入帳號密碼與憑證。",
            "【履歷求職語義】：academic / professional credentials (學術/專業資歷)。"
          ]
        }
      },
      {
        "word": "incredible",
        "kk": "[ɪnˈkrɛdəb!]",
        "ipa": "/ɪnˈkrɛdəbl/",
        "pos": "adj.",
        "meaning": "難以置信的、驚人的、極妙的",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "不、非 (not)"
            },
            {
              "text": "cred",
              "role": "root",
              "meaning": "相信 (believe)"
            },
            {
              "text": "-ible",
              "role": "suffix",
              "meaning": "能夠被...的 (able to be)"
            }
          ],
          "resultMeaning": "超乎常理令人完全無法置信的 ➔「難以置信的、極佳的」"
        },
        "sentence": "The rescue team demonstrated incredible courage while navigating through the raging floodwaters to evacuate stranded villagers.",
        "sentenceZh": "救援隊在狂暴的洪水中航行以撤離受困村民時，展現了令人難以置信的勇氣。",
        "grammar": {
          "pattern": "S + Vt + O (incredible courage) + Adv Clause (while navigating...) + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "The rescue team",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "demonstrated",
              "role": "及物動詞 (Verb)",
              "note": "意為「展現、彰顯」。"
            },
            {
              "part": "incredible courage",
              "role": "直接受詞 (Object)",
              "note": "courage 為不可數名詞。"
            },
            {
              "part": "while navigating through the raging floodwaters",
              "role": "分詞省略狀語",
              "note": "while (they were) navigating...；raging 表洶湧的。"
            },
            {
              "part": "to evacuate stranded villagers",
              "role": "不定詞目的狀語",
              "note": "stranded 為形容詞「滯留受困的」。"
            }
          ],
          "keyPoints": [
            "【語義演變】：incredible 原指「不可置信、虛假的」，現代口語常用於讚美「驚人卓越的」。",
            "【分詞後位省略】：stranded 指 (villagers who were) stranded。"
          ]
        }
      },
      {
        "word": "creed",
        "kk": "[krid]",
        "ipa": "/kriːd/",
        "pos": "n.",
        "meaning": "信條、教義、綱領",
        "formula": {
          "parts": [
            {
              "text": "creed (cred)",
              "role": "root",
              "meaning": "相信、誓言 (believe)"
            }
          ],
          "resultMeaning": "內心深處堅定不移的信仰與道德誓言 ➔「信條、教義」"
        },
        "sentence": "The organization's charter affirms equal dignity for every individual regardless of race, religion, or personal creed.",
        "sentenceZh": "該組織的章程肯定了每個人的平等尊嚴，無論其種族、宗教或個人信仰信條為何。",
        "grammar": {
          "pattern": "S + Vt (affirms) + O + Prep Phrase (regardless of...)",
          "breakdown": [
            {
              "part": "The organization's charter",
              "role": "主詞 (Subject)",
              "note": "charter (憲章、章程)。"
            },
            {
              "part": "affirms",
              "role": "及物動詞 (Verb)",
              "note": "意為「肯定、確認」。"
            },
            {
              "part": "equal dignity for every individual",
              "role": "受詞 (Object)",
              "note": "dignity (尊嚴)。"
            },
            {
              "part": "regardless of race, religion, or personal creed",
              "role": "介系詞片語狀語",
              "note": "regardless of 表「不管、不論」；A, B, or C 三者並列。"
            }
          ],
          "keyPoints": [
            "【重要介系詞片語】：regardless of something = irrespective of something，表「不論、不管...」。",
            "【同根家族】：credible (可信的)、credence (信任)、credulous (輕信的)。"
          ]
        }
      },
      {
        "word": "credit",
        "kk": "[ˈkrɛdɪt]",
        "ipa": "/ˈkrɛdɪt/",
        "pos": "n. / v.",
        "meaning": "信用、信譽、學分、讚揚；(v.) 歸功於、記入貸方",
        "formula": {
          "parts": [
            {
              "text": "cred",
              "role": "root",
              "meaning": "相信 (believe)"
            },
            {
              "text": "-it",
              "role": "suffix",
              "meaning": "名詞/動詞字尾"
            }
          ],
          "resultMeaning": "基於他人對你信任而給予的信譽或延期付款額度 ➔「信用、信譽」"
        },
        "sentence": "The modest lead scientist refused personal accolades, insisting on giving full credit to her dedicated research assistants.",
        "sentenceZh": "這位謙遜的首席科學家拒絕了個人讚譽，堅持將全部功勞歸於她敬業的研究助理們。",
        "grammar": {
          "pattern": "S + V1 (refused O) + Participle Phrase (insisting on giving O to...)",
          "breakdown": [
            {
              "part": "The modest lead scientist",
              "role": "主詞 (Subject)",
              "note": "modest (謙虛的)；lead (帶領的、首席的)。"
            },
            {
              "part": "refused",
              "role": "及物動詞 1 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "personal accolades",
              "role": "受詞 1 (Object)",
              "note": "accolades (讚揚、嘉獎)。"
            },
            {
              "part": "insisting on giving full credit to her dedicated research assistants",
              "role": "現在分詞伴隨狀語",
              "note": "insist on + V-ing；give credit to someone (歸功於某人)。"
            }
          ],
          "keyPoints": [
            "【高頻搭配】：give credit to someone (將功勞歸於某人)；credit A with B (將 B 歸功於 A)。",
            "【介系詞受詞】：insist on 後接動名詞 (giving)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Currency of Trust: The Sacred Bond of Cred",
      "titleZh": "信任的通貨：信譽與憑據的靈魂契約",
      "intro": "在所有人類制度的底層，最寶貴的資產從不是黃金，而是「信任 (cred)」。",
      "paragraphs": [
        {
          "en": "Civilization stands upon a foundation of mutual trust. When financial institutions extend credit, or when historians rely on credible original documents, society moves forward in synchronized harmony.",
          "zh": "人類文明矗立在相互信任的基石之上。當金融機構發放信用貸款，或當歷史學家依賴可信的原始文獻時，社會便在同步和諧中穩步前進。"
        },
        {
          "en": "In an age besieged by algorithmic disinformation, verifying authentic credentials is our primary civic armor, reminding us that honoring truth is the ultimate expression of the root credere.",
          "zh": "在一個遭受演算法虛假訊息圍困的時代，核驗真實憑據是我們首要的公民盔甲，提醒著我們：崇尚真實正是字根 credere 最崇高的體現。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What is our primary civic armor in an age of disinformation?",
          "qZh": "在虛假訊息時代，我們首要的公民盔甲是什麼？",
          "options": [
            "A. Verifying authentic credentials. (核驗真實憑據與消息信譽)",
            "B. Believing everything online immediately.",
            "C. Buying fake passports.",
            "D. Ignoring all legal contracts."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「verifying authentic credentials is our primary civic armor」。"
        }
      ]
    }
  },
  {
    "id": "cur",
    "name": "cur / curs",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「currere」(奔跑、流動、疾馳)，過去分詞為 cursum。",
    "originMeaning": "跑、流動、奔馳、流向",
    "phonetic": "/kɜːr/ 或 /kɜːrs/",
    "icon": "🏃",
    "color": "#E11D48",
    "summary": "涵蓋洋流電流、發生、同時發生、游標奔跑、信使奔馳與學校課程走勢。",
    "words": [
      {
        "word": "current",
        "kk": "[ˈkɝənt]",
        "ipa": "/ˈkɜːrənt/",
        "pos": "n. / adj.",
        "meaning": "(n.) 水流、潮流、電流、思潮；(adj.) 當前的、現行的",
        "formula": {
          "parts": [
            {
              "text": "cur",
              "role": "root",
              "meaning": "跑、流動 (拉丁語 currere)"
            },
            {
              "text": "-ent",
              "role": "suffix",
              "meaning": "...的、事物 (形容詞/名詞字尾)"
            }
          ],
          "resultMeaning": "正在奔流前行中的潮水或正發生的時勢 ➔「水流、電流、當前的」"
        },
        "sentence": "Oceanographers mapped the warm Atlantic Gulf Stream current to evaluate its moderating impact on Northern European climates.",
        "sentenceZh": "海洋學家繪製了大西洋暖流灣流的流動路徑，以評估其對北歐氣候的溫和調節作用。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Oceanographers",
              "role": "主詞 (Subject)",
              "note": "海洋學家。"
            },
            {
              "part": "mapped",
              "role": "及物動詞 (Transitive Verb)",
              "note": "測繪出。"
            },
            {
              "part": "the warm Atlantic Gulf Stream current",
              "role": "直接受詞 (Direct Object)",
              "note": "大西洋墨西哥灣暖流 (Gulf Stream current)。"
            },
            {
              "part": "to evaluate its moderating impact on Northern European climates",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "evaluate (評估)；moderating (緩和調節的)；impact on (對...的衝擊影響)。"
            }
          ],
          "keyPoints": [
            "【多學科核心】：物理學指 electric current (電流)；海洋學指 ocean current (洋流)；社會學指 current trends (當前潮流趨勢)。",
            "【衍生副詞】：currently (目前當前地)。"
          ]
        }
      },
      {
        "word": "occur",
        "kk": "[əˈkɝ]",
        "ipa": "/əˈkɜːr/",
        "pos": "v.",
        "meaning": "發生、出現、被想到（不及物動詞）",
        "formula": {
          "parts": [
            {
              "text": "oc-",
              "role": "prefix",
              "meaning": "朝著...迎面 (拉丁語 ob-)"
            },
            {
              "text": "cur",
              "role": "root",
              "meaning": "跑 (拉丁語 currere)"
            }
          ],
          "resultMeaning": "事情迎面奔跑過來迎頭遇上 ➔「發生、出現」"
        },
        "sentence": "Major tectonic earthquakes occur primarily along active faults situated at the boundaries of colliding continental plates.",
        "sentenceZh": "重大地質板塊地震主要發生在位於相互碰撞大陸板塊邊界上的活斷層帶。",
        "grammar": {
          "pattern": "S + Vi + Adv + Locative Prep Phrase + Past Participle Modifier (主詞 + 不及物動詞 + 頻率副詞 + 地點片語 + 過去分詞片語後位修飾)",
          "breakdown": [
            {
              "part": "Major tectonic earthquakes",
              "role": "主詞 (Subject)",
              "note": "重大地殼板塊地震。"
            },
            {
              "part": "occur",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "純不及物動詞，嚴禁使用被動態！"
            },
            {
              "part": "primarily",
              "role": "修飾副詞 (Adverb of Degree)",
              "note": "主要地。"
            },
            {
              "part": "along active faults",
              "role": "地點狀詞 (Locative Phrase)",
              "note": "沿著活動斷層 (faults 斷層)。"
            },
            {
              "part": "situated at the boundaries of colliding continental plates",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "situated at... (坐落於...) 修飾 faults；colliding (碰撞中的)。"
            }
          ],
          "keyPoints": [
            "【重大文法禁忌】：occur, happen, take place 為純不及物動詞，絕不可寫成被動態 (如 was occurred 是嚴重錯誤！)。",
            "【特殊句型】：It occurred to me that... (我突然心頭靈光一閃想到...)。"
          ]
        }
      },
      {
        "word": "currency",
        "kk": "[ˈkɝənsɪ]",
        "ipa": "/ˈkɜːrənsi/",
        "pos": "n.",
        "meaning": "貨幣、流通、時效性",
        "formula": {
          "parts": [
            {
              "text": "cur",
              "role": "root",
              "meaning": "流動、奔跑 (run, flow)"
            },
            {
              "text": "-ency",
              "role": "suffix",
              "meaning": "名詞字尾 (state/quality)"
            }
          ],
          "resultMeaning": "在市場與交易網絡中不斷流轉運行的媒介 ➔「貨幣、流通」"
        },
        "sentence": "During hyperinflationary crises, merchants often lose faith in domestic fiat currency and demand payment in gold or foreign exchange.",
        "sentenceZh": "在惡性通貨膨脹危機期間，商家往往對國內法定貨幣失去信心，並要求以黃金或外匯進行支付。",
        "grammar": {
          "pattern": "Prep Phrase + S + V1 (lose faith in O) + and + V2 (demand O)",
          "breakdown": [
            {
              "part": "During hyperinflationary crises",
              "role": "時間介系詞片語",
              "note": "crises 為 crisis 的不規則複數。"
            },
            {
              "part": "merchants",
              "role": "主詞 (Subject)",
              "note": "複數名詞「商人」。"
            },
            {
              "part": "often lose faith in domestic fiat currency",
              "role": "第一謂語動詞片語",
              "note": "lose faith in 表「對...喪失信心」。"
            },
            {
              "part": "and demand payment in gold or foreign exchange",
              "role": "第二對等謂語動詞片語",
              "note": "demand 後直接接受詞 payment；in gold 表支付貨幣方式。"
            }
          ],
          "keyPoints": [
            "【希臘/拉丁複數】：crisis ➔ crises；basis ➔ bases；thesis ➔ theses。",
            "【支付介系詞】：pay in cash (付現)、pay by credit card (刷卡)、pay in currency (以貨幣支付)。"
          ]
        }
      },
      {
        "word": "precursor",
        "kk": "[prɪˈkɝsɚ]",
        "ipa": "/prɪˈkɜːrsər/",
        "pos": "n.",
        "meaning": "先驅、前兆、前身、母體分子",
        "formula": {
          "parts": [
            {
              "text": "pre-",
              "role": "prefix",
              "meaning": "在前面 (before)"
            },
            {
              "text": "curs",
              "role": "root",
              "meaning": "跑 (run)"
            },
            {
              "text": "-or",
              "role": "suffix",
              "meaning": "人或事物 (agent/thing)"
            }
          ],
          "resultMeaning": "跑在最前方開闢道路的人事物 ➔「先驅、前身、前兆」"
        },
        "sentence": "The early mechanical computing engine built by Charles Babbage is universally recognized as the direct precursor of modern digital computers.",
        "sentenceZh": "由查爾斯·巴貝奇建造的早期機械計算機，被公認為現代數位電腦的直接前身。",
        "grammar": {
          "pattern": "S + Participle Phrase (built by...) + Passive Verb (is recognized as) + SC",
          "breakdown": [
            {
              "part": "The early mechanical computing engine",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "built by Charles Babbage",
              "role": "過去分詞片語修飾 engine",
              "note": "built 為過去分詞。"
            },
            {
              "part": "is universally recognized as",
              "role": "被動動詞片語",
              "note": "be recognized as 表「被公認為...」。"
            },
            {
              "part": "the direct precursor of modern digital computers",
              "role": "受詞/主詞補語",
              "note": "precursor 意為「前驅事物」。"
            }
          ],
          "keyPoints": [
            "【動詞句型】：recognize A as B (認可 A 為 B) ➔ A is recognized as B。",
            "【同根詞彙】：excursion (遠足)、concur (贊同、同時發生)、recur (復發)。"
          ]
        }
      },
      {
        "word": "recur",
        "kk": "[rɪˈkɝ]",
        "ipa": "/rɪˈkɜːr/",
        "pos": "v.",
        "meaning": "重現、再發、循環發生",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再次 (again)"
            },
            {
              "text": "cur",
              "role": "root",
              "meaning": "跑、流動 (run)"
            }
          ],
          "resultMeaning": "時間流轉後再次跑回來發生 ➔「重現、復發」"
        },
        "sentence": "Without permanent structural reforms, fiscal deficits will inevitably recur in upcoming budget cycles.",
        "sentenceZh": "若不進行永久性的結構性改革，財政赤字在未來的預算週期中將不可避免地再次發生。",
        "grammar": {
          "pattern": "Prep Phrase (Without...) + S + Adv + Modal + Vi (recur) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "Without permanent structural reforms",
              "role": "條件介系詞片語",
              "note": "Without 引導隱含條件。"
            },
            {
              "part": "fiscal deficits",
              "role": "主詞 (Subject)",
              "note": "「財政赤字」。"
            },
            {
              "part": "will inevitably recur",
              "role": "動詞片語 (Verb)",
              "note": "inevitably (無可避免地) 修飾 recur。"
            },
            {
              "part": "in upcoming budget cycles",
              "role": "時間介系詞片語",
              "note": "upcoming (即將到來的)。"
            }
          ],
          "keyPoints": [
            "【雙寫字母規則】：recurred, recurring (如 recurring nightmare 重複出現的噩夢)。",
            "【名詞衍生】：recurrence (重現、再發)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Rivers of Motion: The Flow of Cur and Curs",
      "titleZh": "奔流的江河：跑動與時運的流淌",
      "intro": "宇宙沒有任何一刻是靜止的，一切皆在奔馳 (currere)。從浩蕩洋流 (current) 到突發的機緣 (occur)，生命就是一場向前奔跑的歷程。",
      "paragraphs": [
        {
          "en": "Beneath the placid surface of the deep sea, relentless thermal currents circulate heat across polar frontiers, sustaining planetary life in an unbroken circulatory marathon.",
          "zh": "在深邃海洋平靜的表層之下，不知疲倦的熱力洋流在極地邊疆之間循環輸送熱量，在一場不曾中斷的循環馬拉松中維繫著整個行星的生機。"
        },
        {
          "en": "When unexpected challenges occur in human history, our resilience determines our trajectory. By harnessing the flow of the current rather than fighting fruitlessly against the tide, we navigate stormy waters into tranquil harbors.",
          "zh": "當不可預見的挑戰在人類歷史中發生時，我們的堅韌決定了命運的軌跡。藉由順應時代潮流的前行而非徒勞對抗狂瀾，我們終能引領風暴中的航船駛入安寧的避風港灣。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What circulates heat across polar frontiers under the sea?",
          "qZh": "海底之下是什麼在極地邊疆之間循環輸送熱量？",
          "options": [
            "A. Relentless thermal currents. (不知疲倦的熱力洋流)",
            "B. Giant wooden paddles.",
            "C. Underground diesel generators.",
            "D. Sunken gold treasures."
          ],
          "answer": 0,
          "explanation": "文中第一段指出「relentless thermal currents circulate heat across polar frontiers」。"
        }
      ]
    }
  },
  {
    "id": "fac",
    "name": "fac / fact / fect",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「facere」(做、製作、造就、使成)，過去分詞為 factum，複合字中常變為 -fect- 或 -fic-。",
    "originMeaning": "做、製作、造就、使發生、作用",
    "phonetic": "/fæk/ 或 /fækt/ 或 /fɛkt/",
    "icon": "🏭",
    "color": "#D97706",
    "summary": "涵蓋工廠製造、人造文物、缺陷瑕疵、影響作用、效率與足夠充沛。",
    "words": [
      {
        "word": "factory",
        "kk": "[ˈfæktri]",
        "ipa": "/ˈfæktri/",
        "pos": "n.",
        "meaning": "工廠、製造廠",
        "formula": {
          "parts": [
            {
              "text": "fact",
              "role": "root",
              "meaning": "製作 (拉丁語 facere)"
            },
            {
              "text": "-ory",
              "role": "suffix",
              "meaning": "地點、場所 (名詞字尾)"
            }
          ],
          "resultMeaning": "專門集中機器與工人進行各類物品製作的場所 ➔「工廠」"
        },
        "sentence": "The state-of-the-art gigafactory deploys robotic assembly lines to manufacture lithium battery cells at scale.",
        "sentenceZh": "這座最先進的超級工廠部署機器人組裝線，以大規模生產製造鋰電池電芯。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Manner Phrase (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 規模狀詞)",
          "breakdown": [
            {
              "part": "The state-of-the-art gigafactory",
              "role": "主詞 (Subject)",
              "note": "state-of-the-art (最先進頂尖的)；gigafactory (超級工廠)。"
            },
            {
              "part": "deploys",
              "role": "及物動詞 (Transitive Verb)",
              "note": "部署應用。"
            },
            {
              "part": "robotic assembly lines",
              "role": "直接受詞 (Direct Object)",
              "note": "機器人自動組裝生產線。"
            },
            {
              "part": "to manufacture lithium battery cells at scale",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "manufacture (製造；manu 手 + fact 製作)；at scale (大規模地)。"
            }
          ],
          "keyPoints": [
            "【複合字源同現】：manufacture (手作 ➔ 大規模製造) 與 factory 皆含 fact 字根！",
            "【成語片語】：at scale (具經濟規模地)。"
          ]
        }
      },
      {
        "word": "effect",
        "kk": "[ɪˈfɛkt]",
        "ipa": "/ɪˈfekt/",
        "pos": "n. / v.",
        "meaning": "(n.) 效果、影響、作用；(v.) 促成、實現（如 effect change）",
        "formula": {
          "parts": [
            {
              "text": "ef-",
              "role": "prefix",
              "meaning": "出、做出 (拉丁語 ex-)"
            },
            {
              "text": "fect",
              "role": "root",
              "meaning": "做 (拉丁語 facere)"
            }
          ],
          "resultMeaning": "事情做出來所產生顯現於外的最終結果 ➔「效果、影響」"
        },
        "sentence": "Clinical trials demonstrated that the experimental vaccine produced a pronounced therapeutic effect against the viral variant.",
        "sentenceZh": "臨床試驗證實，該試驗性疫苗對此病毒變異株產生了顯著的治療效果。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause (主詞 + 及物動詞 + That名詞子句受詞)",
          "breakdown": [
            {
              "part": "Clinical trials",
              "role": "主詞 (Subject)",
              "note": "臨床試驗。"
            },
            {
              "part": "demonstrated",
              "role": "及物動詞 (Transitive Verb)",
              "note": "證實展現。"
            },
            {
              "part": "that the experimental vaccine produced a pronounced therapeutic effect against the viral variant",
              "role": "名詞子句 (Noun Clause)",
              "note": "experimental (實驗性的)；produced (產生)；pronounced (顯著的)；therapeutic effect (療效)；against (抵禦/針對)。"
            }
          ],
          "keyPoints": [
            "【名詞 effect vs. 動詞 affect】：affect 通常作動詞 (影響某物)；effect 通常作名詞 (產生某效果)。",
            "【搭配片語】：have a significant effect on... (對...產生重大影響)。"
          ]
        }
      },
      {
        "word": "manufacture",
        "kk": "[ˌmænjəˈfæktʃɚ]",
        "ipa": "/ˌmænjuˈfæktʃər/",
        "pos": "v. / n.",
        "meaning": "大量製造、加工生產；(n.) 製造業、加工品",
        "formula": {
          "parts": [
            {
              "text": "manu-",
              "role": "prefix",
              "meaning": "手 (hand)"
            },
            {
              "text": "fact",
              "role": "root",
              "meaning": "做、製作 (make, do)"
            },
            {
              "text": "-ure",
              "role": "suffix",
              "meaning": "行為或產物名詞字尾"
            }
          ],
          "resultMeaning": "原指手工精細打造，後延伸為工廠大規模生產 ➔「製造、加工生產」"
        },
        "sentence": "The advanced fabrication facility utilizes robotic precision to manufacture millions of microprocessors each month.",
        "sentenceZh": "這座先進的製造工廠利用機器人精密技術，每月生產數百萬顆微處理器。",
        "grammar": {
          "pattern": "S + Vt + O (precision) + Infinitive of Purpose (to manufacture O) + Adv",
          "breakdown": [
            {
              "part": "The advanced fabrication facility",
              "role": "主詞 (Subject)",
              "note": "facility 意為「設施、廠房」。"
            },
            {
              "part": "utilizes",
              "role": "及物動詞 (Verb)",
              "note": "utilize (善加利用)。"
            },
            {
              "part": "robotic precision",
              "role": "受詞 (Object)",
              "note": "precision (精密性)。"
            },
            {
              "part": "to manufacture millions of microprocessors",
              "role": "不定詞目的狀語",
              "note": "manufacture 接受詞 microprocessors。"
            },
            {
              "part": "each month",
              "role": "時間副詞片語",
              "note": "修飾頻率。"
            }
          ],
          "keyPoints": [
            "【手字根】：manu- (手)，如 manuscript (手稿)、manual (手冊、手工的)、manicure (修甲)。",
            "【大數表達】：millions of + 複數名詞，指「數以百萬計的」。"
          ]
        }
      },
      {
        "word": "defect",
        "kk": "[ˈdiˌfɛkt]",
        "ipa": "/ˈdiːfɛkt/",
        "pos": "n. / v.",
        "meaning": "缺陷、瑕疵、故障；(v.) 叛逃、背叛",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "離開、缺失 (down, away)"
            },
            {
              "text": "fect (fac)",
              "role": "root",
              "meaning": "做 (make, do)"
            }
          ],
          "resultMeaning": "製作過程中有缺失未完成的部分 ➔「缺陷、瑕疵」"
        },
        "sentence": "Quality assurance inspectors immediately recalled the entire batch upon detecting a critical structural defect.",
        "sentenceZh": "品管檢查員在發現關鍵結構缺陷後，立即召回了整批產品。",
        "grammar": {
          "pattern": "S + Adv + Vt (recalled) + O + Prep Phrase (upon detecting O)",
          "breakdown": [
            {
              "part": "Quality assurance inspectors",
              "role": "主詞 (Subject)",
              "note": "品管檢查員。"
            },
            {
              "part": "immediately",
              "role": "時間副詞",
              "note": "修飾 recalled。"
            },
            {
              "part": "recalled",
              "role": "及物動詞 (Verb)",
              "note": "召回(瑕疵品)。"
            },
            {
              "part": "the entire batch",
              "role": "受詞 (Object)",
              "note": "batch (一批貨物)。"
            },
            {
              "part": "upon detecting a critical structural defect",
              "role": "時間狀語片語",
              "note": "upon + V-ing 表「一...就...」。"
            }
          ],
          "keyPoints": [
            "【重要句型】：upon / on + V-ing 表示「一...立刻...」，等同於 as soon as 主詞 + 動詞。",
            "【重音對比】：名詞 a defect [ˈdiˌfɛkt] vs. 動詞 to defect (叛逃) [dɪˈfɛkt]。"
          ]
        }
      },
      {
        "word": "perfect",
        "kk": "[ˈpɝfɪkt]",
        "ipa": "/ˈpɜːrfɪkt/",
        "pos": "adj. / v.",
        "meaning": "完美的、無瑕的；(v.) 使完美、改善",
        "formula": {
          "parts": [
            {
              "text": "per-",
              "role": "prefix",
              "meaning": "徹底、完全 (thoroughly)"
            },
            {
              "text": "fect (fac)",
              "role": "root",
              "meaning": "做 (make, do)"
            }
          ],
          "resultMeaning": "徹頭徹尾完全做好的 ➔「完美的；使完善」"
        },
        "sentence": "The concert pianist practiced for decades to perfect his interpretation of Chopin's intricate nocturnes.",
        "sentenceZh": "這位音樂會鋼琴家苦練了數十年，以使其對蕭邦複雜夜曲的詮釋臻於完美。",
        "grammar": {
          "pattern": "S + Vi (practiced) + Prep Phrase of Duration + Infinitive of Purpose (to perfect O)",
          "breakdown": [
            {
              "part": "The concert pianist",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "practiced",
              "role": "不及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "for decades",
              "role": "時間長度介系詞片語",
              "note": "表歷時數十年。"
            },
            {
              "part": "to perfect his interpretation of Chopin's intricate nocturnes",
              "role": "不定詞目的狀語",
              "note": "perfect 作及物動詞 [pɚˈfɛkt]；intricate (複雜精緻的)。"
            }
          ],
          "keyPoints": [
            "【前名/形後動重音典範】：形容詞 perfect [ˈpɝfɪkt] vs. 及物動詞 to perfect [pɚˈfɛkt]！",
            "【字尾名詞】：perfection (完美)、perfectionist (完美主義者)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Workshop of the Gods: The Alchemy of Fac and Fact",
      "titleZh": "造物者的工坊：製作與造就的熔爐",
      "intro": "人類與其他物種最大的不同，在於我們能將大腦中的奇思妙想動手做出來 (facere)。",
      "paragraphs": [
        {
          "en": "From early artisans chiseling stone tools to modern technicians overseeing automated factories, the instinct to fabricate solutions defines our evolutionary arc.",
          "zh": "從早期工匠鑿刻石器，到現代技術人員監督自動化工廠，親手打造解方與工具的本能，深刻定義了我們演化的歷程軌跡。"
        },
        {
          "en": "Every scientific formula must eventually produce a tangible beneficial effect upon human suffering; otherwise, engineering remains an empty monument to vanity.",
          "zh": "每一個科學公式最終都必須對緩解人類苦難產生實質的有益效果，否則，工程製造只不過是一座通向虛榮的空洞碑石。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What must every scientific formula eventually produce?",
          "qZh": "每個科學公式最終都必須產生什麼？",
          "options": [
            "A. A tangible beneficial effect upon human suffering. (對緩解人類苦難產生實質有益效果)",
            "B. Heavy taxes on bread.",
            "C. Endless wars between nations.",
            "D. Poisonous chemical clouds."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「Every scientific formula must eventually produce a tangible beneficial effect upon human suffering」。"
        }
      ]
    }
  },
  {
    "id": "gen",
    "name": "gen / gener",
    "type": "root",
    "typeLabel": "拉丁與希臘雙源字根 (Greek & Latin Root)",
    "etymology": "源自希臘語「γένος」(génos) 及拉丁語「genus / generis」(出生、產生、種類、出身)。",
    "originMeaning": "出生、產生、種類、生成、種族",
    "phonetic": "/dʒɛn/ 或 /ˈdʒɛnər/",
    "icon": "🧬",
    "color": "#16A34A",
    "summary": "涵蓋發電機、世代同堂、基因遺傳、創世紀起源、同類總稱與真誠原生的核心字根。",
    "words": [
      {
        "word": "generate",
        "kk": "[ˈdʒɛnəˌret]",
        "ipa": "/ˈdʒenəreɪt/",
        "pos": "v.",
        "meaning": "產生、引起、發電、生成",
        "formula": {
          "parts": [
            {
              "text": "gener",
              "role": "root",
              "meaning": "產生 (拉丁語 genus)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "促使某事物誕生並產生運作能量 ➔「產生、生成、發電」"
        },
        "sentence": "Offshore wind turbines generate clean electricity while displacing thousands of tons of carbon emissions annually.",
        "sentenceZh": "離岸風力渦輪機在發出純淨電力的同時，每年取代了數千噸的碳排放量。",
        "grammar": {
          "pattern": "S + Vt + O + While-Participial Clause (主詞 + 及物動詞 + 受詞 + While分詞伴隨狀詞)",
          "breakdown": [
            {
              "part": "Offshore wind turbines",
              "role": "主詞 (Subject)",
              "note": "離岸風力發電機組。"
            },
            {
              "part": "generate",
              "role": "及物動詞 (Transitive Verb)",
              "note": "發電產生。"
            },
            {
              "part": "clean electricity",
              "role": "直接受詞 (Direct Object)",
              "note": "潔淨電力。"
            },
            {
              "part": "while displacing thousands of tons of carbon emissions annually",
              "role": "伴隨分詞狀詞 (Participial Clause)",
              "note": "while 保留連接詞；displacing (取代置換)；annually (每年地)。"
            }
          ],
          "keyPoints": [
            "【高分動詞搭配】：generate revenue (創造營收)、generate interest (引起興趣)。",
            "【衍生名詞】：generator (發電機)、generation (世代/產生)。"
          ]
        }
      },
      {
        "word": "genuine",
        "kk": "[ˈdʒɛnjʊɪn]",
        "ipa": "/ˈdʒenjuɪn/",
        "pos": "adj.",
        "meaning": "真正的、真誠的、非偽造的、血統純正的",
        "formula": {
          "parts": [
            {
              "text": "gen-",
              "role": "root",
              "meaning": "出生、血統 (拉丁語 genuinus 天生純正的)"
            },
            {
              "text": "-ine",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "如同天生血統般自然真實、不加虛飾偽裝 ➔「真正的、真誠的」"
        },
        "sentence": "Antique appraisers verified that the Renaissance oil painting was a genuine masterpiece crafted by Leonardo da Vinci.",
        "sentenceZh": "古董鑑定家證實該文藝復興時期的油畫是一件由達文西親手創作的真正傳世傑作。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause with Past Participle Modifier (主詞 + 及物動詞 + That名詞子句 + 分詞修飾)",
          "breakdown": [
            {
              "part": "Antique appraisers",
              "role": "主詞 (Subject)",
              "note": "古董鑑定師。"
            },
            {
              "part": "verified",
              "role": "及物動詞 (Transitive Verb)",
              "note": "核實證實。"
            },
            {
              "part": "that the Renaissance oil painting was a genuine masterpiece",
              "role": "名詞子句 (Noun Clause)",
              "note": "genuine (名副其實/真品的)；masterpiece (傑作)。"
            },
            {
              "part": "crafted by Leonardo da Vinci",
              "role": "過去分詞片語修飾 (Past Participle Phrase)",
              "note": "crafted by... (由...精心創作)。"
            }
          ],
          "keyPoints": [
            "【反義字對比】：genuine (真品/真誠的) vs. counterfeit (仿冒贗品) / fake。",
            "【副詞形式】：genuinely (由衷地、真誠地)。"
          ]
        }
      },
      {
        "word": "generation",
        "kk": "[ˌdʒɛnəˈreʃən]",
        "ipa": "/ˌdʒɛnəˈreɪʃn/",
        "pos": "n.",
        "meaning": "世代、輩、產生、發電",
        "formula": {
          "parts": [
            {
              "text": "gen-",
              "role": "root",
              "meaning": "出生、產生 (birth, produce)"
            },
            {
              "text": "-ation",
              "role": "suffix",
              "meaning": "名詞字尾 (act/process)"
            }
          ],
          "resultMeaning": "同一個時期誕生並共同成長的人群 ➔「世代、產生」"
        },
        "sentence": "Each younger generation inevitably brings fresh perspectives and transformative technologies to the workplace.",
        "sentenceZh": "每個較年輕的世代都無可避免地為職場帶來嶄新的視角與變革性的科技。",
        "grammar": {
          "pattern": "S + Adv + Vt (brings) + O (perspectives and technologies) + Prep Phrase",
          "breakdown": [
            {
              "part": "Each younger generation",
              "role": "主詞 (Subject)",
              "note": "Each 後接單數名詞。"
            },
            {
              "part": "inevitably",
              "role": "副詞 (Adverb)",
              "note": "修飾 brings。"
            },
            {
              "part": "brings",
              "role": "及物動詞 (Verb)",
              "note": "單數動詞。"
            },
            {
              "part": "fresh perspectives and transformative technologies",
              "role": "受詞 (Object)",
              "note": "由 and 連接兩項名詞片語。"
            },
            {
              "part": "to the workplace",
              "role": "目的地介系詞片語",
              "note": "bring A to B。"
            }
          ],
          "keyPoints": [
            "【一詞雙義】：generation 可表「世代族群 (Generation Z)」，亦可表能源「發電 (power generation)」。",
            "【主謂一致】：Each + 單數名詞，謂語動詞必須使用第三人稱單數形式 (brings)。"
          ]
        }
      },
      {
        "word": "generic",
        "kk": "[dʒəˈnɛrɪk]",
        "ipa": "/dʒəˈnɛrɪk/",
        "pos": "adj. / n.",
        "meaning": "通用的、一般的、非專利特許的；(n.) 學名藥",
        "formula": {
          "parts": [
            {
              "text": "gener (gen)",
              "role": "root",
              "meaning": "種類、屬 (kind, class)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "形容詞字尾 (pertaining to)"
            }
          ],
          "resultMeaning": "屬於整個類別全體而非單一特定品牌的 ➔「通用的、學名藥」"
        },
        "sentence": "Once the pharmaceutical patent expires, healthcare providers typically prescribe generic medications to lower medical costs.",
        "sentenceZh": "一旦該藥物專利過期，醫療機構通常會開立學名藥以降低病患醫療成本。",
        "grammar": {
          "pattern": "Adv Clause of Time (Once...) + S + Adv + Vt (prescribe) + O + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "Once the pharmaceutical patent expires",
              "role": "時間條件副詞子句",
              "note": "Once 作連接詞表「一旦...」。"
            },
            {
              "part": "healthcare providers",
              "role": "主要句主詞 (Subject)",
              "note": "複數名詞片語「醫療提供者」。"
            },
            {
              "part": "typically prescribe",
              "role": "動詞片語 (Verb)",
              "note": "prescribe (開處方)。"
            },
            {
              "part": "generic medications",
              "role": "受詞 (Object)",
              "note": "「非專利學名藥」。"
            },
            {
              "part": "to lower medical costs",
              "role": "不定詞目的狀語",
              "note": "to + 原形動詞 lower (降低)。"
            }
          ],
          "keyPoints": [
            "【連接詞用法】：Once 作從屬連接詞，意為「一旦...就...」，引導之副詞子句用現在式代替未來式。",
            "【醫藥名詞】：generic drugs / generic medications 專指專利過期後的「學名藥」。"
          ]
        }
      },
      {
        "word": "generous",
        "kk": "[ˈdʒɛnərəs]",
        "ipa": "/ˈdʒɛnərəs/",
        "pos": "adj.",
        "meaning": "慷慨的、大方的、豐富充沛的",
        "formula": {
          "parts": [
            {
              "text": "gener (gen)",
              "role": "root",
              "meaning": "出身、族類 (noble birth)"
            },
            {
              "text": "-ous",
              "role": "suffix",
              "meaning": "充滿...特質的形容詞字尾"
            }
          ],
          "resultMeaning": "原指具有貴族高貴品格氣度、不吝給予 ➔「慷慨大方的」"
        },
        "sentence": "A generous philanthropic donation enabled the children's hospital to acquire advanced pediatric imaging scanners.",
        "sentenceZh": "一筆慷慨的慈善捐款使得該兒童醫院能夠添購先進的兒科造影掃描儀。",
        "grammar": {
          "pattern": "S + Vt (enabled) + O (hospital) + to-V (to acquire O)",
          "breakdown": [
            {
              "part": "A generous philanthropic donation",
              "role": "主詞 (Subject)",
              "note": "philanthropic (慈善博愛的)；donation (捐贈)。"
            },
            {
              "part": "enabled",
              "role": "使役動詞 (Verb)",
              "note": "enable + O + to V 句型。"
            },
            {
              "part": "the children's hospital",
              "role": "受詞 (Object)",
              "note": "名詞片語。"
            },
            {
              "part": "to acquire advanced pediatric imaging scanners",
              "role": "受詞補語",
              "note": "acquire (獲得)；pediatric (小兒科的)。"
            }
          ],
          "keyPoints": [
            "【使役動詞句型】：enable someone to do something (使某人能夠做某事)。",
            "【名詞衍生】：generosity (慷慨、寬厚)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Seeds of Origin: The Genesis of Gen",
      "titleZh": "起源的火種：生命與創生之律",
      "intro": "萬物皆有其「源頭與本質 (gen-)」。從產生 (generate) 綠色電能到追求真誠 (genuine) 的品德，字根 gen- 見證了生命的初衷。",
      "paragraphs": [
        {
          "en": "From the first genesis of microbial cells in primordial oceans to successive generations of human scholars passing torches of reason, the root gen signifies continuous rebirth.",
          "zh": "從原始大洋中微生物細胞的最初創生，到一代又一代人類學者接續傳遞理性的火炬，字根 gen- 象徵著綿延不絕的再生與新生。"
        },
        {
          "en": "In a world often seduced by synthetic illusions, holding fast to genuine human empathy and generating renewable solutions remains our greatest moral obligation.",
          "zh": "在一個經常被人工虛妄幻象所誘惑的世界裡，堅守真實真誠的人類同理心，並持續創造再生解方，依然是我們最崇高的道德責任。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What does the root 'gen' signify according to the passage?",
          "qZh": "根據文章，字根 'gen' 象徵著什麼？",
          "options": [
            "A. Continuous rebirth and renewal across generations. (跨世代綿延不絕的再生與新生)",
            "B. Total freezing of ocean tides.",
            "C. Replacing human words with mechanical beeps.",
            "D. Stopping all electrical currents."
          ],
          "answer": 0,
          "explanation": "文中第一段指出字根 gen-「signifies continuous rebirth」。"
        }
      ]
    }
  },
  {
    "id": "log",
    "name": "log / logy / loqu",
    "type": "root",
    "typeLabel": "希臘與拉丁雙源字根 (Greek logos & Latin loqui)",
    "etymology": "希臘語「λόγος」(lógos，言說、理性、學問、邏輯)；拉丁語動詞「loqui」(說話)。",
    "originMeaning": "言說、對話、理性、學科、邏輯",
    "phonetic": "/lɑːɡ/ 或 /lɑːdʒi/ 或 /ˈloʊkw/",
    "icon": "💬",
    "color": "#7C3AED",
    "summary": "涵蓋雙向對話、獨白、雄辯口才、邏輯推理、致歉道歉與各科學門。",
    "words": [
      {
        "word": "dialogue",
        "kk": "[ˈdaɪəˌlɔg]",
        "ipa": "/ˈdaɪəlɔːɡ/",
        "pos": "n.",
        "meaning": "對話、交流對談、雙方協商",
        "formula": {
          "parts": [
            {
              "text": "dia-",
              "role": "prefix",
              "meaning": "在兩者之間、跨越 (希臘語 dia)"
            },
            {
              "text": "logue",
              "role": "root",
              "meaning": "說話、言語 (希臘語 logos)"
            }
          ],
          "resultMeaning": "在不同立場的兩方或多方之間進行溝通交流 ➔「對話、協商」"
        },
        "sentence": "Constructive diplomatic dialogue is indispensable to avert armed conflict and resolve territorial disputes peacefully.",
        "sentenceZh": "建設性的外交對話是避免武裝衝突並和平化解領土爭端的不可或缺之途徑。",
        "grammar": {
          "pattern": "S + Linking Verb + Predicate Adjective + Compound Infinitive of Purpose (主詞 + 連綴動詞 + 形容詞補語 + 複合目的不定詞)",
          "breakdown": [
            {
              "part": "Constructive diplomatic dialogue",
              "role": "主詞 (Subject)",
              "note": "建設性外交對話。"
            },
            {
              "part": "is",
              "role": "連綴動詞 (Linking Verb)",
              "note": "be 動詞。"
            },
            {
              "part": "indispensable",
              "role": "主詞補語 (Subject Complement)",
              "note": "不可或缺的 (in- 不 + dispense 分發/免除 + able)。"
            },
            {
              "part": "to avert armed conflict and resolve territorial disputes peacefully",
              "role": "目的狀詞 (Compound Infinitive)",
              "note": "to avert A and resolve B (避開 A 並化解 B)；peacefully (和平地)。"
            }
          ],
          "keyPoints": [
            "【對比結構】：dialogue (雙向對話) vs. monologue (獨白；mono- 單一)。",
            "【核心高頻形容詞】：indispensable to / for... (對...不可或缺的)。"
          ]
        }
      },
      {
        "word": "eloquent",
        "kk": "[ˈɛləkwənt]",
        "ipa": "/ˈeləkwənt/",
        "pos": "adj.",
        "meaning": "雄辯的、口才流利的、動人的",
        "formula": {
          "parts": [
            {
              "text": "e-",
              "role": "prefix",
              "meaning": "出、向外 (拉丁語 ex-)"
            },
            {
              "text": "loqu",
              "role": "root",
              "meaning": "說話 (拉丁語 loqui)"
            },
            {
              "text": "-ent",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "話語流暢滔滔不絕向外奔湧而出 ➔「雄辯的、口才流利的」"
        },
        "sentence": "The civil rights leader delivered an eloquent speech that galvanized millions to march peacefully for constitutional equality.",
        "sentenceZh": "民權領袖發表了一篇雄辯動人的演說，激勵了數百萬人為憲政平等走上街頭和平遊行。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 關係子句 + 目的不定詞)",
          "breakdown": [
            {
              "part": "The civil rights leader",
              "role": "主詞 (Subject)",
              "note": "民權運動領袖。"
            },
            {
              "part": "delivered",
              "role": "及物動詞 (Transitive Verb)",
              "note": "deliver a speech (發表演說)。"
            },
            {
              "part": "an eloquent speech",
              "role": "直接受詞 (Direct Object)",
              "note": "eloquent (雄辯動人的)。"
            },
            {
              "part": "that galvanized millions to march peacefully for constitutional equality",
              "role": "關係子句 (Relative Clause)",
              "note": "galvanize + O + to V (激勵鼓舞某人去做...)；peacefully (和平地)。"
            }
          ],
          "keyPoints": [
            "【名詞衍生】：eloquence (雄辯、口才)。",
            "【拉丁字根 loqui 系列】：colloquial (口語的；com 共同 + loqui 說話)。"
          ]
        }
      },
      {
        "word": "apology",
        "kk": "[əˈpɑlədʒɪ]",
        "ipa": "/əˈpɑːlədʒi/",
        "pos": "n.",
        "meaning": "道歉、歉意、辯護文章",
        "formula": {
          "parts": [
            {
              "text": "apo-",
              "role": "prefix",
              "meaning": "離開、防禦 (away, off)"
            },
            {
              "text": "log",
              "role": "root",
              "meaning": "說話、言語 (speech, word)"
            },
            {
              "text": "-y",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "以說話言語防禦申辯、或卸下過錯懇求諒解 ➔「道歉、辯解」"
        },
        "sentence": "The chief executive issued an unreserved public apology for the severe software glitch that paralyzed airline bookings.",
        "sentenceZh": "該執行長針對癱瘓了航空公司訂位系統的嚴重軟體故障，發表了毫無保留的公開道歉。",
        "grammar": {
          "pattern": "S + Vt (issued) + O (apology) + Prep Phrase (for...) + Relative Clause (that paralyzed...)",
          "breakdown": [
            {
              "part": "The chief executive",
              "role": "主詞 (Subject)",
              "note": "單數名詞片語。"
            },
            {
              "part": "issued",
              "role": "及物動詞 (Verb)",
              "note": "issue an apology (發表道歉聲明)。"
            },
            {
              "part": "an unreserved public apology",
              "role": "直接受詞 (Object)",
              "note": "unreserved 表「毫無保留的」。"
            },
            {
              "part": "for the severe software glitch",
              "role": "原因介系詞片語",
              "note": "glitch (小故障、失靈)。"
            },
            {
              "part": "that paralyzed airline bookings",
              "role": "關係子句修飾 glitch",
              "note": "that 作主格關代；paralyzed (癱瘓)。"
            }
          ],
          "keyPoints": [
            "【動詞搭配】：issue / offer / make an apology to someone for something。",
            "【歷史語義】：古典哲學中 Apology 指「申辯文」，如柏拉圖的《蘇格拉底的申辯》 (Apology of Socrates)。"
          ]
        }
      },
      {
        "word": "monologue",
        "kk": "[ˈmɑnəˌlɔg]",
        "ipa": "/ˈmɑːnəlɔːɡ/",
        "pos": "n.",
        "meaning": "獨白、長篇獨角戲",
        "formula": {
          "parts": [
            {
              "text": "mono-",
              "role": "prefix",
              "meaning": "單一 (alone, single)"
            },
            {
              "text": "logue (log)",
              "role": "root",
              "meaning": "說話 (speech, speak)"
            }
          ],
          "resultMeaning": "單獨一人在台上滔滔不絕講述的言論 ➔「獨白」"
        },
        "sentence": "The Shakespearean actor held the entire theater spellbound during his passionate delivery of Hamlet's soliloquy monologue.",
        "sentenceZh": "這位莎士比亞演員在熱情演繹哈姆雷特的自白獨白時，讓整座劇院的觀眾聽得如癡如醉。",
        "grammar": {
          "pattern": "S + Vt (held) + O + OC (spellbound) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "The Shakespearean actor",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "held",
              "role": "及物動詞 (Verb)",
              "note": "hold someone spellbound 慣用語。"
            },
            {
              "part": "the entire theater",
              "role": "受詞 (Object)",
              "note": "轉喻劇院內全體觀眾。"
            },
            {
              "part": "spellbound",
              "role": "受詞補語 (Objective Complement)",
              "note": "形容詞補語「入迷的、著魔的」。"
            },
            {
              "part": "during his passionate delivery of Hamlet's soliloquy monologue",
              "role": "時間介系詞片語",
              "note": "delivery 表「發表、演講表現」。"
            }
          ],
          "keyPoints": [
            "【精彩五大句型】：hold + O + spellbound (使某人著迷入神)，spellbound 作受詞補語。",
            "【對比字首】：monologue (一人獨白) vs. dialogue (兩人對話) vs. prologue (開場序白)。"
          ]
        }
      },
      {
        "word": "logic",
        "kk": "[ˈlɑdʒɪk]",
        "ipa": "/ˈlɑːdʒɪk/",
        "pos": "n.",
        "meaning": "邏輯、邏輯學、條理性、合理性",
        "formula": {
          "parts": [
            {
              "text": "log-",
              "role": "root",
              "meaning": "話語、理性思考 (speech, reason)"
            },
            {
              "text": "-ic",
              "role": "suffix",
              "meaning": "學術或性質名詞字尾"
            }
          ],
          "resultMeaning": "合乎理性推理秩序的思想法則 ➔「邏輯、邏輯學」"
        },
        "sentence": "Sound philosophical logic requires that every assertion be substantiated by verifiable evidence.",
        "sentenceZh": "健全的哲學邏輯要求每項主張都必須由可驗證的證據加以證實。",
        "grammar": {
          "pattern": "S + Vt (requires) + That Clause with Subjunctive Mood (that every assertion be...)",
          "breakdown": [
            {
              "part": "Sound philosophical logic",
              "role": "主詞 (Subject)",
              "note": "sound 作形容詞「健全嚴謹的」。"
            },
            {
              "part": "requires",
              "role": "要求動詞 (Verb)",
              "note": "引導要求建議意志之 that 子句。"
            },
            {
              "part": "that every assertion be substantiated",
              "role": "虛擬式受詞子句",
              "note": "require that + S + (should) + 原形動詞 be substantiated (省略 should)。"
            },
            {
              "part": "by verifiable evidence",
              "role": "施事介系詞片語",
              "note": "verifiable (可查證的)；evidence (不可數名詞)。"
            }
          ],
          "keyPoints": [
            "【重大文法點：假設語氣虛擬式】：require / insist / suggest / recommend + that + S + (should) + V 原形動詞！",
            "【形容詞衍生】：logical (合乎邏輯的) vs. illogical (不合邏輯的)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Gift of Logos: The Power of Speech and Reason",
      "titleZh": "理性的賜福：言說與邏輯的永恆殿堂",
      "intro": "「Logos」是古希臘哲學最神聖的字眼：它既是語言 (speech)，也是宇宙運行的最高理性 (reason)。",
      "paragraphs": [
        {
          "en": "In ancient Athens, citizens gathered in open agoras to engage in passionate dialogue, believing that competing ideas, when refined through logic and eloquent persuasion, would forge wise civic policies.",
          "zh": "在古代雅典，公民齊聚在露天廣場展開熱烈的對話，相信相互交鋒的觀點一旦經過邏輯與雄辯說服的淬鍊，便能鑄就睿智的公民政策。"
        },
        {
          "en": "Whenever hatred threatens to silence reason, returning to the spirit of logos empowers us to bridge deep fractures with empathy, proving that civilized words are mightier than weapons.",
          "zh": "每當仇恨企圖使理性噤聲之時，重返 logos 的精神賦予了我們以同理心彌合深刻裂痕的力量，證明了文明的話語永遠比武器更具摧枯拉朽的感召力。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "Why did Athenian citizens gather in agoras to engage in dialogue?",
          "qZh": "為什麼雅典公民聚集在廣場展開對話？",
          "options": [
            "A. To forge wise civic policies through logic and persuasion. (透過邏輯與說服鑄就睿智的公民政策)",
            "B. To trade horses and camels.",
            "C. To escape paying national taxes.",
            "D. To hide from sunlight."
          ],
          "answer": 0,
          "explanation": "文中第一段指出公民對話是為了「forge wise civic policies」。"
        }
      ]
    }
  },
  {
    "id": "ped",
    "name": "ped / pod",
    "type": "root",
    "typeLabel": "拉丁與希臘雙源字根 (Latin pes & Greek pous)",
    "etymology": "拉丁語「pes / pedis」(腳)；希臘語「πούς / ποδός」(poús / podós，腳)。",
    "originMeaning": "腳、足部、腳步、行走",
    "phonetic": "/pɛd/ 或 /pɑːd/",
    "icon": "👟",
    "color": "#0284C7",
    "summary": "涵蓋行人漫步、踏板驅動、底座基石、阻礙絆腳、加速推進與三腳架。",
    "words": [
      {
        "word": "pedestrian",
        "kk": "[pəˈdɛstrɪən]",
        "ipa": "/pəˈdestriən/",
        "pos": "n. / adj.",
        "meaning": "(n.) 行人、步行者；(adj.) 徒步的、平淡無奇的",
        "formula": {
          "parts": [
            {
              "text": "ped-",
              "role": "root",
              "meaning": "腳 (拉丁語 pes/pedis)"
            },
            {
              "text": "-estrian",
              "role": "suffix",
              "meaning": "從事...行動的人 (名詞字尾)"
            }
          ],
          "resultMeaning": "完全靠雙腳在街道上行走的過路人 ➔「行人」"
        },
        "sentence": "Urban redesigners created wide pedestrian plazas to reduce vehicular congestion and encourage active commuting.",
        "sentenceZh": "都市重整規劃師打造了寬敞的行人徒步廣場，以減少車輛擁堵並鼓勵活力通勤。",
        "grammar": {
          "pattern": "S + Vt + O + Compound Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 對等目的不定詞片語)",
          "breakdown": [
            {
              "part": "Urban redesigners",
              "role": "主詞 (Subject)",
              "note": "都市規劃設計師。"
            },
            {
              "part": "created",
              "role": "及物動詞 (Transitive Verb)",
              "note": "打造建立。"
            },
            {
              "part": "wide pedestrian plazas",
              "role": "直接受詞 (Direct Object)",
              "note": "wide (寬敞的)；pedestrian plazas (行人徒步廣場)。"
            },
            {
              "part": "to reduce vehicular congestion and encourage active commuting",
              "role": "對等目的狀詞 (Compound Infinitives)",
              "note": "to reduce A and [to] encourage B (減少 A 並提倡 B)；vehicular (車輛的)；commuting (通勤)。"
            }
          ],
          "keyPoints": [
            "【比喻形容詞】：pedestrian 作形容詞亦可指「平淡乏味的、毫無創意的 (pedestrian writing)」。",
            "【相關專有名詞】：pedestrian crossing (行人穿越道/斑馬線)。"
          ]
        }
      },
      {
        "word": "expedite",
        "kk": "[ˈɛkspəˌdaɪt]",
        "ipa": "/ˈekspədaɪt/",
        "pos": "v.",
        "meaning": "加速、加快進度、迅速完成",
        "formula": {
          "parts": [
            {
              "text": "ex-",
              "role": "prefix",
              "meaning": "出、解脫 (拉丁語 ex-)"
            },
            {
              "text": "ped",
              "role": "root",
              "meaning": "腳 (拉丁語 pes/pedis)"
            },
            {
              "text": "-ite",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "將深陷泥淖的雙腳拔出，讓腳步能飛快奔馳 ➔「加速、迅速完成」"
        },
        "sentence": "Diplomats worked around the clock to expedite the processing of emergency travel visas for stranded refugees.",
        "sentenceZh": "外交官日以繼夜地工作，以加快審理滯留難民的緊急旅行簽證手續。",
        "grammar": {
          "pattern": "S + Vi + Idiomatic Adverbial + Infinitive of Purpose (主詞 + 不及物動詞 + 成語時間狀詞 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Diplomats",
              "role": "主詞 (Subject)",
              "note": "外交官。"
            },
            {
              "part": "worked",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "工作。"
            },
            {
              "part": "around the clock",
              "role": "時間副詞成語 (Idiomatic Adverbial)",
              "note": "夜以繼日、二十四小時不間斷地。"
            },
            {
              "part": "to expedite the processing of emergency travel visas",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "expedite (加速)；processing (審理程序)；visas (簽證)。"
            }
          ],
          "keyPoints": [
            "【成對反義字】：impede (阻礙；im- 困入 + ped 腳 = 絆腳) vs. expedite (加速解套)。",
            "【形容詞形式】：expeditious (迅速敏捷的)。"
          ]
        }
      },
      {
        "word": "pedal",
        "kk": "[ˈpɛd!]",
        "ipa": "/ˈpɛdl/",
        "pos": "n. / v.",
        "meaning": "踏板；(v.) 踩踏板、踩自行車",
        "formula": {
          "parts": [
            {
              "text": "ped",
              "role": "root",
              "meaning": "腳、足 (foot)"
            },
            {
              "text": "-al",
              "role": "suffix",
              "meaning": "名詞/形容詞字尾"
            }
          ],
          "resultMeaning": "專門用腳踩踏操控的槓桿板機 ➔「踏板」"
        },
        "sentence": "Cyclists must pedal steadily to maintain momentum when ascending a steep mountain incline.",
        "sentenceZh": "自行車騎士在攀爬陡峭山坡時，必須平穩踩踏以保持前進動量。",
        "grammar": {
          "pattern": "S + Modal + Vi (pedal) + Adv + Infinitive of Purpose + Adv Clause of Time",
          "breakdown": [
            {
              "part": "Cyclists",
              "role": "主詞 (Subject)",
              "note": "複數名詞「騎自行車者」。"
            },
            {
              "part": "must pedal",
              "role": "動詞片語 (Verb)",
              "note": "情態助動詞 must + 原形動詞 pedal。"
            },
            {
              "part": "steadily",
              "role": "情狀副詞",
              "note": "修飾 pedal。"
            },
            {
              "part": "to maintain momentum",
              "role": "不定詞目的狀語",
              "note": "momentum (動量、動力)。"
            },
            {
              "part": "when ascending a steep mountain incline",
              "role": "時間副詞省略子句",
              "note": "when (they are) ascending...；ascending 意為「攀爬上升」。"
            }
          ],
          "keyPoints": [
            "【器官字根辨析】：ped- 拉丁語指「腳」 (如 pedestrian, pedal)；但希臘語 ped- 亦可指「兒童」 (如 pediatrician 小兒科醫師)。",
            "【動詞短語】：put the pedal to the metal 是美語俚語「油門踩到底、全力加速」。"
          ]
        }
      },
      {
        "word": "podium",
        "kk": "[ˈpodɪəm]",
        "ipa": "/ˈpoʊdiəm/",
        "pos": "n.",
        "meaning": "講台、演講台、指揮台、頒獎台",
        "formula": {
          "parts": [
            {
              "text": "pod-",
              "role": "root",
              "meaning": "足、腳底 (foot)"
            },
            {
              "text": "-ium",
              "role": "suffix",
              "meaning": "場所、平台 (place/platform)"
            }
          ],
          "resultMeaning": "墊在雙腳下方令人站立抬高的演說或領獎平台 ➔「講台、領獎台」"
        },
        "sentence": "The Olympic champion stepped onto the gold medal podium as her national anthem echoed throughout the arena.",
        "sentenceZh": "當國歌在整個場館中迴盪時，奧運冠軍登上了金牌領獎台。",
        "grammar": {
          "pattern": "S + Vi (stepped) + Prep Phrase (onto the podium) + Adv Clause of Time (as...)",
          "breakdown": [
            {
              "part": "The Olympic champion",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "stepped",
              "role": "不及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "onto the gold medal podium",
              "role": "方向介系詞片語",
              "note": "onto 表登上表面。"
            },
            {
              "part": "as her national anthem echoed throughout the arena",
              "role": "時間副詞子句",
              "note": "as 引導時間子句；anthem (國歌)；echoed (迴盪)。"
            }
          ],
          "keyPoints": [
            "【字根字尾】：pod (腳) + -ium (場所平台，如 stadium 體育場、aquarium 水族館)。",
            "【體育片語】：reach the podium 指「獲得前三名獎牌登上領獎台」。"
          ]
        }
      },
      {
        "word": "tripod",
        "kk": "[ˈtraɪˌpɑd]",
        "ipa": "/ˈtraɪpɑːd/",
        "pos": "n.",
        "meaning": "三腳架",
        "formula": {
          "parts": [
            {
              "text": "tri-",
              "role": "prefix",
              "meaning": "三 (three)"
            },
            {
              "text": "pod (ped)",
              "role": "root",
              "meaning": "腳、足 (foot)"
            }
          ],
          "resultMeaning": "具備三隻支撐支腳的穩定器械支架 ➔「三腳架」"
        },
        "sentence": "Photographers mount heavy telephoto lenses onto a sturdy tripod to eliminate handheld camera shake during long exposures.",
        "sentenceZh": "攝影師將沉重的望遠鏡頭安裝在堅固的三腳架上，以消除長時間曝光期間的手持相機晃動。",
        "grammar": {
          "pattern": "S + Vt (mount A onto B) + Infinitive of Purpose (to eliminate O) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "Photographers",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "mount",
              "role": "及物動詞 (Verb)",
              "note": "mount A onto B (將 A 安裝固定在 B 上)。"
            },
            {
              "part": "heavy telephoto lenses",
              "role": "受詞 (Object)",
              "note": "telephoto (望遠的)；lenses (鏡頭複數)。"
            },
            {
              "part": "onto a sturdy tripod",
              "role": "方向介系詞片語",
              "note": "sturdy (結實堅固的)。"
            },
            {
              "part": "to eliminate handheld camera shake",
              "role": "不定詞目的狀語",
              "note": "eliminate (消除)。"
            },
            {
              "part": "during long exposures",
              "role": "時間介系詞片語",
              "note": "exposures (曝光)。"
            }
          ],
          "keyPoints": [
            "【字首字根】：tri- (三) + pod (足)，同類字如 monologue (單)、dialogue (雙)、tripod (三)、polygon (多)。",
            "【動詞用法】：mount A onto/on B 是固定工藝與攝影搭配詞。"
          ]
        }
      }
    ],
    "article": {
      "title": "Footsteps of the Wanderer: The Journey of Ped and Pod",
      "titleZh": "行者的足跡：步履與前行的旅途",
      "intro": "人類文明是踏著雙腳 (ped-) 一步步丈量出來的。從步行者 (pedestrian) 到加速奔馳 (expedite)，每一步都是向著未知的跋涉。",
      "paragraphs": [
        {
          "en": "Before mechanical locomotives conquered continents, every migration was forged by human footsteps. Walking at the pedestrian pace allowed our ancestors to attune their senses to every change in soil, wind, and stars.",
          "zh": "在機械火車征服各大洲之前，每一次遷徙都是由人類的腳步所踏出來的。以步行者的步伐前行，讓我們的祖先得以將感官調節至與土壤、微風與星辰的每一絲變化共鳴。"
        },
        {
          "en": "Even as we build ultra-fast technologies to expedite international commerce, carving out tranquil pedestrian zones in cities reminds us of our humble earthly origin on two feet.",
          "zh": "即使當我們打造超高速科技以加速國際商業的流轉，在城市中留出寧靜的行人徒步區，依然提醒著我們依靠雙腳行走於大地之上的謙卑源起。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What did walking at a pedestrian pace allow our ancestors to do?",
          "qZh": "以步行者的步伐行走讓我們的祖先得以做到什麼？",
          "options": [
            "A. Attune their senses to changes in soil, wind, and stars. (將感官與土壤、微風、星辰變化共鳴)",
            "B. Fly above the clouds immediately.",
            "C. Build underwater submarines.",
            "D. Forget all spoken words."
          ],
          "answer": 0,
          "explanation": "文中第一段指出步行「allowed our ancestors to attune their senses to every change in soil, wind, and stars」。"
        }
      ]
    }
  },
  {
    "id": "sens",
    "name": "sens / sent",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「sentire」(感受、感覺、感知、思想)，過去分詞形為 sensum。",
    "originMeaning": "感受、感覺、知覺、情感、意見",
    "phonetic": "/sɛns/ 或 /sɛnt/",
    "icon": "🌸",
    "color": "#E11D48",
    "summary": "涵蓋五官感官、敏感敏銳、情感心緒、同意贊同、反對異議與共識共鳴。",
    "words": [
      {
        "word": "sensitive",
        "kk": "[ˈsɛnsətɪv]",
        "ipa": "/ˈsensətɪv/",
        "pos": "adj.",
        "meaning": "敏感的、靈敏的、體貼敏銳的、機密的",
        "formula": {
          "parts": [
            {
              "text": "sens",
              "role": "root",
              "meaning": "感覺 (拉丁語 sentire)"
            },
            {
              "text": "-itive",
              "role": "suffix",
              "meaning": "具備...特質的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "能夠敏銳捕捉外部微小刺激變化的 ➔「敏感的、靈敏的」"
        },
        "sentence": "Highly sensitive satellite infrared sensors detect early temperature anomalies that precede catastrophic wildfires.",
        "sentenceZh": "高度靈敏的衛星紅外線感測器能偵測到在災難性野火爆發前出現的早期異常升溫。",
        "grammar": {
          "pattern": "S + Vt + O + Relative Clause (主詞 + 及物動詞 + 受詞 + 限定關係子句)",
          "breakdown": [
            {
              "part": "Highly sensitive satellite infrared sensors",
              "role": "主詞 (Subject)",
              "note": "高靈敏度衛星紅外線感測器。"
            },
            {
              "part": "detect",
              "role": "及物動詞 (Transitive Verb)",
              "note": "偵測發現。"
            },
            {
              "part": "early temperature anomalies",
              "role": "直接受詞 (Direct Object)",
              "note": "早期溫度異常 (anomalies 異常現象)。"
            },
            {
              "part": "that precede catastrophic wildfires",
              "role": "限定關係子句 (Relative Clause)",
              "note": "that 指代 anomalies；precede (在...之前發生)；catastrophic (災難性的)。"
            }
          ],
          "keyPoints": [
            "【易混淆形容詞】：sensitive (敏感靈敏的) vs. sensible (明智理智的；源自 sense 理性)。",
            "【及物動詞先行】：precede something (在某事之前發生/早於)。"
          ]
        }
      },
      {
        "word": "consensus",
        "kk": "[kənˈsɛnsəs]",
        "ipa": "/kənˈsensəs/",
        "pos": "n.",
        "meaning": "共識、一致意見",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同、一起 (拉丁語 com-)"
            },
            {
              "text": "sens",
              "role": "root",
              "meaning": "感覺、想法 (拉丁語 sentire)"
            },
            {
              "text": "-us",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "眾人內心的想法與感受融洽歸攏於一處 ➔「共識」"
        },
        "sentence": "After days of rigorous debate, delegates forged a broad consensus on binding carbon reduction targets.",
        "sentenceZh": "經過數天的激烈辯論，各國代表在具約束力的碳減排目標上達成了廣泛共識。",
        "grammar": {
          "pattern": "Time Adverbial Phrase + S + Vt + O + on-Topic Phrase (時間介系詞片語 + 主詞 + 及物動詞 + 受詞 + 主題介系詞片語)",
          "breakdown": [
            {
              "part": "After days of rigorous debate",
              "role": "時間狀詞 (Time Phrase)",
              "note": "經過數日激烈辯論。"
            },
            {
              "part": "delegates",
              "role": "主詞 (Subject)",
              "note": "各國代表。"
            },
            {
              "part": "forged",
              "role": "及物動詞 (Transitive Verb)",
              "note": "forge a consensus (艱辛打造成就共識)。"
            },
            {
              "part": "a broad consensus",
              "role": "直接受詞 (Direct Object)",
              "note": "廣泛共識。"
            },
            {
              "part": "on binding carbon reduction targets",
              "role": "主題介系詞片語 (Topic Phrase)",
              "note": "binding (具法律約束力的) 為現在分詞作形容詞；reduction targets (減排目標)。"
            }
          ],
          "keyPoints": [
            "【高分動詞搭配】：reach / build / forge a consensus (達成/建立共識)。",
            "【介系詞搭配】：consensus on / about an issue。"
          ]
        }
      },
      {
        "word": "sentiment",
        "kk": "[ˈsɛntəmənt]",
        "ipa": "/ˈsɛntɪmənt/",
        "pos": "n.",
        "meaning": "情感、感性、觀點、情緒",
        "formula": {
          "parts": [
            {
              "text": "sent (sens)",
              "role": "root",
              "meaning": "感覺、感受 (feel)"
            },
            {
              "text": "-ment",
              "role": "suffix",
              "meaning": "名詞字尾 (state/act)"
            }
          ],
          "resultMeaning": "內心所萌生出的情感或對事態的總體觀感 ➔「情緒、觀點」"
        },
        "sentence": "Investor sentiment rebounded sharply after the central bank signaled an imminent reduction in borrowing rates.",
        "sentenceZh": "在央行暗示即將調降借貸利率後，投資人情緒大幅回升。",
        "grammar": {
          "pattern": "S + Vi (rebounded) + Adv + Adv Clause of Time (after...)",
          "breakdown": [
            {
              "part": "Investor sentiment",
              "role": "主詞 (Subject)",
              "note": "「投資人情緒、市場氛圍」。"
            },
            {
              "part": "rebounded",
              "role": "不及物動詞 (Verb)",
              "note": "意為「反彈回升」。"
            },
            {
              "part": "sharply",
              "role": "程度副詞",
              "note": "修飾 rebounded。"
            },
            {
              "part": "after the central bank signaled an imminent reduction in borrowing rates",
              "role": "時間副詞子句",
              "note": "imminent 表「即將來臨的」；reduction in 表「...的縮減」。"
            }
          ],
          "keyPoints": [
            "【財經高頻詞】：market sentiment (市場情緒)、consumer sentiment (消費者信心)。",
            "【同根派生】：sentimental (多愁善感的)、sentimentality (多愁善感)。"
          ]
        }
      },
      {
        "word": "dissent",
        "kk": "[dɪˈsɛnt]",
        "ipa": "/dɪˈsɛnt/",
        "pos": "n. / v.",
        "meaning": "異議、不同意、反對意見",
        "formula": {
          "parts": [
            {
              "text": "dis-",
              "role": "prefix",
              "meaning": "分離、不同 (apart, differently)"
            },
            {
              "text": "sent",
              "role": "root",
              "meaning": "感受、思想 (feel, think)"
            }
          ],
          "resultMeaning": "與大眾感覺不同、持有分離意見 ➔「異議、反對」"
        },
        "sentence": "In a robust constitutional democracy, peaceful political dissent is safeguarded as a fundamental civic right.",
        "sentenceZh": "在健全的憲政民主體制中，和平的政治異議被保障為基本公民權利。",
        "grammar": {
          "pattern": "Prep Phrase + S + Passive Verb (is safeguarded) + Prep Phrase (as...)",
          "breakdown": [
            {
              "part": "In a robust constitutional democracy",
              "role": "情境介系詞片語",
              "note": "robust (健全穩固的)。"
            },
            {
              "part": "peaceful political dissent",
              "role": "主詞 (Subject)",
              "note": "dissent 作不可數名詞。"
            },
            {
              "part": "is safeguarded",
              "role": "被動態謂語",
              "note": "safeguard (捍衛、保護)。"
            },
            {
              "part": "as a fundamental civic right",
              "role": "身份介系詞片語",
              "note": "civic (公民的)。"
            }
          ],
          "keyPoints": [
            "【詞彙對比】：assent / consent (同意) vs. dissent (異議) vs. resent (怨恨)。",
            "【司法名詞】：dissenting opinion 專指大法官判決中的「不同意見書」。"
          ]
        }
      },
      {
        "word": "sensation",
        "kk": "[sɛnˈseʃən]",
        "ipa": "/sɛnˈseɪʃn/",
        "pos": "n.",
        "meaning": "感覺、知覺、轟動、造成轟動的人事物",
        "formula": {
          "parts": [
            {
              "text": "sens-",
              "role": "root",
              "meaning": "感覺 (feel)"
            },
            {
              "text": "-ation",
              "role": "suffix",
              "meaning": "名詞字尾 (state/event)"
            }
          ],
          "resultMeaning": "刺激感官所產生的強烈感覺，或引發全社會震撼關注的事件 ➔「感覺、轟動」"
        },
        "sentence": "The prodigy's virtuosic violin recital created an international sensation among classical music connoisseurs.",
        "sentenceZh": "這位神童精湛的小提琴獨奏會在古典音樂鑑賞家中引起了國際轟動。",
        "grammar": {
          "pattern": "S + Vt (created) + O (an international sensation) + Prep Phrase",
          "breakdown": [
            {
              "part": "The prodigy's virtuosic violin recital",
              "role": "主詞 (Subject)",
              "note": "prodigy (神童)；virtuosic (技巧精湛的)；recital (獨奏會)。"
            },
            {
              "part": "created",
              "role": "及物動詞 (Verb)",
              "note": "create a sensation (造成轟動)。"
            },
            {
              "part": "an international sensation",
              "role": "直接受詞 (Direct Object)",
              "note": "名詞片語。"
            },
            {
              "part": "among classical music connoisseurs",
              "role": "群體介系詞片語",
              "note": "connoisseurs (鑑賞家、行家)。"
            }
          ],
          "keyPoints": [
            "【高頻慣用片語】：create / cause a sensation 表「引起社會轟動」。",
            "【派生形容詞】：sensational (轟動的、聳人聽聞的)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Symphony of Feeling: The Resonance of Sens and Sent",
      "titleZh": "感受的交響：心緒與共識的靈光",
      "intro": "人類不僅用邏輯理解世界，更用「感受 (sentire)」撫摸宇宙。從靈敏的感官 (sensitive) 到眾志成城的共識 (consensus)，心靈創造奇蹟。",
      "paragraphs": [
        {
          "en": "To be human is to feel deeply. While scientific instruments provide sensitive measurements of physical matter, our emotional sentiments connect us across cultural divides.",
          "zh": "作為人類，就意味著能深刻感知。當科學儀器對物質實體提供極其靈敏的測量時，我們的情感心緒則將我們跨越文化分歧緊密相連。"
        },
        {
          "en": "Democratic governance reaches its pinnacle when diverse communities move past bitter resentment and forge an enduring consensus grounded in mutual respect and shared human dignity.",
          "zh": "當多元社群告別苦澀的怨恨，並在相互尊重與共同的人格尊嚴基礎上鑄就持久共識之時，民主治理便攀登至最巔峰的境界。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "When does democratic governance reach its pinnacle according to the text?",
          "qZh": "根據文章，民主治理何時攀登至最巔峰境界？",
          "options": [
            "A. When diverse communities forge an enduring consensus grounded in mutual respect. (當多元社群在相互尊重基礎上鑄就持久共識之時)",
            "B. When one ruler commands all speech.",
            "C. When libraries are locked forever.",
            "D. When scientific instruments are destroyed."
          ],
          "answer": 0,
          "explanation": "文中第二段指出民主治理於「forge an enduring consensus grounded in mutual respect」時達到巔峰。"
        }
      ]
    }
  },
  {
    "id": "fin",
    "name": "fin",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語名詞「finis」(邊界、界限、終點、目標、結束)。",
    "originMeaning": "界限、終點、結束、精確劃分",
    "phonetic": "/fɪn/ 或 /faɪn/",
    "icon": "🏁",
    "color": "#059669",
    "summary": "涵蓋最終結局、無限永恆、精準定義、精雕細琢與劃定界限範圍。",
    "words": [
      {
        "word": "define",
        "kk": "[dɪˈfaɪn]",
        "ipa": "/dɪˈfaɪn/",
        "pos": "v.",
        "meaning": "定義、界定、闡明、劃定界限",
        "formula": {
          "parts": [
            {
              "text": "de-",
              "role": "prefix",
              "meaning": "完全、向下 (拉丁語 de-)"
            },
            {
              "text": "fine",
              "role": "root",
              "meaning": "界限 (拉丁語 finis)"
            }
          ],
          "resultMeaning": "徹底劃出事物清楚的邊界邊線 ➔「定義、界定」"
        },
        "sentence": "Philosophers continually redefine ethical values to address novel dilemmas spawned by artificial intelligence.",
        "sentenceZh": "哲學家持續重新界定倫理價值，以因應由人工智慧所衍生出的嶄新道德困境。",
        "grammar": {
          "pattern": "S + Adv + Vt + O + Infinitive of Purpose with Participle (主詞 + 頻率副詞 + 及物動詞 + 受詞 + 目的不定詞與分詞後位修飾)",
          "breakdown": [
            {
              "part": "Philosophers",
              "role": "主詞 (Subject)",
              "note": "哲學家。"
            },
            {
              "part": "continually",
              "role": "頻率副詞 (Adverb of Frequency)",
              "note": "持續不斷地。"
            },
            {
              "part": "redefine",
              "role": "及物動詞 (Transitive Verb)",
              "note": "重新界定 (re- 再 + define)。"
            },
            {
              "part": "ethical values",
              "role": "直接受詞 (Direct Object)",
              "note": "倫理價值觀。"
            },
            {
              "part": "to address novel dilemmas spawned by artificial intelligence",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "address (因應處理)；novel dilemmas (嶄新困境)；spawned by... (由...催生出的，過去分詞修飾)。"
            }
          ],
          "keyPoints": [
            "【名詞形式】：definition (定義；high-definition 高解析度/高畫質 HD)。",
            "【形容詞衍生】：definitive (決定性的、最權威的)。"
          ]
        }
      },
      {
        "word": "infinite",
        "kk": "[ˈɪnfənɪt]",
        "ipa": "/ˈɪnfɪnət/",
        "pos": "adj.",
        "meaning": "無限的、無窮盡的、無邊無際的",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "無、不 (拉丁語 in-)"
            },
            {
              "text": "fin",
              "role": "root",
              "meaning": "界限、終點 (拉丁語 finis)"
            },
            {
              "text": "-ite",
              "role": "suffix",
              "meaning": "...的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "沒有任何邊界邊緣與終點的 ➔「無限的、無窮的」"
        },
        "sentence": "Cosmologists ponder whether our expanding observable universe is merely a bubble within an infinite multiverse.",
        "sentenceZh": "宇宙學家思考著我們這座不斷膨脹的可觀測宇宙，是否僅僅是無窮多重宇宙中的一個微小氣泡。",
        "grammar": {
          "pattern": "S + Vt + Wh-Noun Clause (主詞 + 及物動詞 + Whether引導之間接問句名詞子句受詞)",
          "breakdown": [
            {
              "part": "Cosmologists",
              "role": "主詞 (Subject)",
              "note": "宇宙學家。"
            },
            {
              "part": "ponder",
              "role": "及物動詞 (Transitive Verb)",
              "note": "深思沉吟。"
            },
            {
              "part": "whether our expanding observable universe is merely a bubble within an infinite multiverse",
              "role": "受詞名詞子句 (Noun Clause as Object)",
              "note": "expanding (膨脹中的)；observable (可觀測的)；bubble (氣泡)；infinite multiverse (無限多元宇宙)。"
            }
          ],
          "keyPoints": [
            "【發音重音規律】：finite 重音在前讀 /ˈfaɪnaɪt/；infinite 發音為 /ˈɪnfɪnət/ (注意母音變化！)。",
            "【成對反義】：finite (有限的) vs. infinite (無限的)。"
          ]
        }
      },
      {
        "word": "finish",
        "kk": "[ˈfɪnɪʃ]",
        "ipa": "/ˈfɪnɪʃ/",
        "pos": "v. / n.",
        "meaning": "完成、結束；(n.) 結尾、終點線、拋光飾面",
        "formula": {
          "parts": [
            {
              "text": "fin",
              "role": "root",
              "meaning": "邊界、終點 (end, limit)"
            },
            {
              "text": "-ish",
              "role": "suffix",
              "meaning": "動詞字尾 (cause to be)"
            }
          ],
          "resultMeaning": "達到邊界使事情完全畫下句點 ➔「完成、結束」"
        },
        "sentence": "The marathon runner summoned her remaining strength to cross the finish line just under three hours.",
        "sentenceZh": "這位馬拉松跑者凝聚了她僅存的體力，在不到三小時內衝過了終點線。",
        "grammar": {
          "pattern": "S + Vt (summoned) + O + Infinitive of Purpose (to cross O) + Prep Phrase",
          "breakdown": [
            {
              "part": "The marathon runner",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "summoned",
              "role": "及物動詞 (Verb)",
              "note": "summon strength (鼓起勇氣/力量)。"
            },
            {
              "part": "her remaining strength",
              "role": "受詞 (Object)",
              "note": "remaining 為現在分詞作形容詞「剩餘的」。"
            },
            {
              "part": "to cross the finish line",
              "role": "不定詞目的狀語",
              "note": "finish line (終點線)。"
            },
            {
              "part": "just under three hours",
              "role": "時間介系詞片語",
              "note": "under 表少於。"
            }
          ],
          "keyPoints": [
            "【動詞句型】：finish doing something，finish 後接動名詞 (V-ing)，不可接 to V！",
            "【精緻詞彙】：summon one's strength / courage 是描寫運動員與英雄故事的高級表達。"
          ]
        }
      },
      {
        "word": "confine",
        "kk": "[kənˈfaɪn]",
        "ipa": "/kənˈfaɪn/",
        "pos": "v. / n.",
        "meaning": "限制、禁閉、侷限於；(n.) 界限、範圍",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "完全、共同 (together, completely)"
            },
            {
              "text": "fine (fin)",
              "role": "root",
              "meaning": "界線 (border, boundary)"
            }
          ],
          "resultMeaning": "將人或事物完全拘束限制在邊界之內 ➔「限制、禁閉」"
        },
        "sentence": "The medical officer advised the infected patient to confine himself to his living quarters until the contagious period elapsed.",
        "sentenceZh": "醫官建議該名受感染病患在傳染期結束前，將自己限制在居住居所內隔離。",
        "grammar": {
          "pattern": "S + Vt (advised) + O + to-V (to confine O to...) + Prep/Adv Clause of Time",
          "breakdown": [
            {
              "part": "The medical officer",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "advised",
              "role": "及物動詞 (Verb)",
              "note": "advise + O + to V。"
            },
            {
              "part": "the infected patient",
              "role": "受詞 (Object)",
              "note": "infected 作形容詞。"
            },
            {
              "part": "to confine himself to his living quarters",
              "role": "受詞補語",
              "note": "confine A to B (將 A 限制在 B)。"
            },
            {
              "part": "until the contagious period elapsed",
              "role": "時間副詞子句",
              "note": "elapsed 表「時間流逝、過去」。"
            }
          ],
          "keyPoints": [
            "【固定搭配】：confine A to B (將 A 侷限於 B 之內)，to 為介系詞。",
            "【重音對比】：動詞 confine [kənˈfaɪn] vs. 名詞 confines (界限、範圍) [ˈkɑnfaɪnz] (如 beyond the confines of Earth)。"
          ]
        }
      },
      {
        "word": "final",
        "kk": "[ˈfaɪn!]",
        "ipa": "/ˈfaɪnl/",
        "pos": "adj. / n.",
        "meaning": "最終的、決定性的；(n.) 決賽、期末考",
        "formula": {
          "parts": [
            {
              "text": "fin",
              "role": "root",
              "meaning": "終點、邊界 (end)"
            },
            {
              "text": "-al",
              "role": "suffix",
              "meaning": "形容詞字尾"
            }
          ],
          "resultMeaning": "到達終點、無可更改的 ➔「最終的、決賽」"
        },
        "sentence": "The supreme court issued its final ruling, officially terminating years of bitter patent litigation.",
        "sentenceZh": "最高法院做出了最終裁決，正式終結了長達數年的激烈專利訴訟。",
        "grammar": {
          "pattern": "S + Vt (issued) + O (ruling) + Participle Phrase (officially terminating O)",
          "breakdown": [
            {
              "part": "The supreme court",
              "role": "主詞 (Subject)",
              "note": "最高法院。"
            },
            {
              "part": "issued",
              "role": "及物動詞 (Verb)",
              "note": "做出、發布。"
            },
            {
              "part": "its final ruling",
              "role": "直接受詞 (Direct Object)",
              "note": "ruling (司法裁定)。"
            },
            {
              "part": "officially terminating years of bitter patent litigation",
              "role": "現在分詞結果狀語",
              "note": "terminating 接受詞 litigation (訴訟)。"
            }
          ],
          "keyPoints": [
            "【分詞表結果】：現在分詞片語 terminating... 作結果副詞狀語，表示發布判決所帶來的自然結果。",
            "【衍生詞】：finalize (使定案)、finally (最終)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Boundary and the Abyss: The Journey of Fin",
      "titleZh": "邊界與深淵：有限與永恆的對話",
      "intro": "界限 (finis) 給予事物形體與定義 (define)，而超越界限，我們瞥見了無垠宇宙的無限 (infinite) 莊嚴。",
      "paragraphs": [
        {
          "en": "Human life is exquisitely finite; our days are bounded by birth and mortality. Yet, within these defined boundaries, human creativity continually reaches toward infinite aspirations.",
          "zh": "人類的生命精緻而有限，我們的歲月被出生與死亡劃定了邊界。然而，恰恰在這些被界定的界限之內，人類的創造力不斷向著無限的抱負伸展。"
        },
        {
          "en": "By defining our ethical responsibilities with clarity, we transform the fleeting nature of our mortal existence into an enduring legacy that echoes across time.",
          "zh": "藉由澄澈地界定我們的道德責任，我們將肉身存在的轉瞬即逝，轉化為在時空長河中永恆迴盪的不朽遺產。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What does human creativity reach toward according to the passage?",
          "qZh": "根據文章，人類的創造力向著什麼伸展？",
          "options": [
            "A. Infinite aspirations. (無限的抱負與憧憬)",
            "B. Complete silence.",
            "C. Total darkness.",
            "D. Cold stone walls."
          ],
          "answer": 0,
          "explanation": "文中第一段指出人類創造力「continually reaches toward infinite aspirations」。"
        }
      ]
    }
  },
  {
    "id": "jur",
    "name": "jur / jud / jus",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語名詞「jus / juris」(法律、正義、公理) 及「judex」(法官)。",
    "originMeaning": "法律、正義、公正、裁斷、發誓",
    "phonetic": "/dʒʊər/ 或 /dʒʌdʒ/ 或 /dʒʌs/",
    "icon": "⚖️",
    "color": "#7C3AED",
    "summary": "涵蓋司法審判、正義公理、合理辯護、陪審團審議與司法管轄權。",
    "words": [
      {
        "word": "justice",
        "kk": "[ˈdʒʌstɪs]",
        "ipa": "/ˈdʒʌstɪs/",
        "pos": "n.",
        "meaning": "正義、公平、司法人員、大法官",
        "formula": {
          "parts": [
            {
              "text": "just",
              "role": "root",
              "meaning": "正義、公正 (拉丁語 jus)"
            },
            {
              "text": "-ice",
              "role": "suffix",
              "meaning": "性質、狀態 (名詞字尾)"
            }
          ],
          "resultMeaning": "維護社會公理道德與法律秩序的崇高原則 ➔「正義、公道」"
        },
        "sentence": "Independent constitutional courts uphold justice by protecting vulnerable minority populations against state overreach.",
        "sentenceZh": "獨立的憲法法院藉由保護弱勢少數群體免受國家權力過度侵害，以捍衛司法正義。",
        "grammar": {
          "pattern": "S + Vt + O + Means Prepositional Gerund (主詞 + 及物動詞 + 受詞 + 方式介系詞動名詞片語)",
          "breakdown": [
            {
              "part": "Independent constitutional courts",
              "role": "主詞 (Subject)",
              "note": "獨立憲法法院。"
            },
            {
              "part": "uphold",
              "role": "及物動詞 (Transitive Verb)",
              "note": "捍衛、支持。"
            },
            {
              "part": "justice",
              "role": "直接受詞 (Direct Object)",
              "note": "正義公道。"
            },
            {
              "part": "by protecting vulnerable minority populations against state overreach",
              "role": "方式狀詞片語 (By + Gerund)",
              "note": "protect A against B (保護 A 免於 B 侵害)；overreach (權力逾越/濫權)。"
            }
          ],
          "keyPoints": [
            "【動詞短語搭配】：uphold / administer justice (維護/伸張正義)。",
            "【職稱涵義】：在美國最高法院，大法官的尊稱為 Supreme Court Justice。"
          ]
        }
      },
      {
        "word": "justify",
        "kk": "[ˈdʒʌstəˌfaɪ]",
        "ipa": "/ˈdʒʌstɪfaɪ/",
        "pos": "v.",
        "meaning": "證明...是合理的、為...辯護、使正當化",
        "formula": {
          "parts": [
            {
              "text": "just",
              "role": "root",
              "meaning": "公正、正當 (拉丁語 jus)"
            },
            {
              "text": "-ify",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "提出充分合法的理由證明其正當無誤 ➔「證明...合理、辯護」"
        },
        "sentence": "Military commanders must present indisputable legal rationale to justify tactical interventions under international law.",
        "sentenceZh": "軍事指揮官必須提出無可爭辯的法律理據，以在國際法架構下證明戰術干預的正當性。",
        "grammar": {
          "pattern": "S + Modal + Vt + O + Infinitive of Purpose + Prep Phrase (主詞 + 助動詞 + 及物動詞 + 受詞 + 目的不定詞 + 法律依據介系詞片語)",
          "breakdown": [
            {
              "part": "Military commanders",
              "role": "主詞 (Subject)",
              "note": "軍事指揮官。"
            },
            {
              "part": "must present",
              "role": "情態謂語 (Modal Predicate)",
              "note": "必須提出。"
            },
            {
              "part": "indisputable legal rationale",
              "role": "直接受詞 (Direct Object)",
              "note": "indisputable (無可置疑的)；rationale (根本理由/依據)。"
            },
            {
              "part": "to justify tactical interventions",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "justify (證明正當)；interventions (軍事干預)。"
            },
            {
              "part": "under international law",
              "role": "依據介系詞片語 (Prepositional Phrase)",
              "note": "在國際法架構下。"
            }
          ],
          "keyPoints": [
            "【高階字彙搭配】：justify the cost / expense (證明花費是合情合理的)。",
            "【衍生形容詞】：justifiable (有充分理由的、可正當化的)。"
          ]
        }
      },
      {
        "word": "jury",
        "kk": "[ˈdʒʊrɪ]",
        "ipa": "/ˈdʒʊri/",
        "pos": "n.",
        "meaning": "陪審團、評判委員會",
        "formula": {
          "parts": [
            {
              "text": "jur-",
              "role": "root",
              "meaning": "誓約、法律 (swear, law)"
            },
            {
              "text": "-y",
              "role": "suffix",
              "meaning": "集合名詞字尾"
            }
          ],
          "resultMeaning": "宣誓誓言並依據法律事實評判是非之公民群體 ➔「陪審團」"
        },
        "sentence": "After three days of rigorous deliberation, the sequestered jury reached a unanimous verdict of not guilty.",
        "sentenceZh": "經過三天嚴格審議後，被隔離的陪審團達成了無罪的一致裁決。",
        "grammar": {
          "pattern": "Prep Phrase + S + Vt (reached) + O (a unanimous verdict of...)",
          "breakdown": [
            {
              "part": "After three days of rigorous deliberation",
              "role": "時間介系詞片語",
              "note": "deliberation 表「審議、深思熟慮」。"
            },
            {
              "part": "the sequestered jury",
              "role": "主詞 (Subject)",
              "note": "sequestered 為過去分詞作形容詞「被隔離看管的」。"
            },
            {
              "part": "reached",
              "role": "及物動詞 (Verb)",
              "note": "reach a verdict 為固定搭配。"
            },
            {
              "part": "a unanimous verdict of not guilty",
              "role": "直接受詞 (Direct Object)",
              "note": "unanimous (全體一致的)；verdict (裁決)。"
            }
          ],
          "keyPoints": [
            "【司法搭配詞】：reach a verdict (達成裁決)、sequester a jury (隔離陪審團防洩密)。",
            "【同根派生】：perjury (偽證罪，per- 破壞 + jury 誓約)。"
          ]
        }
      },
      {
        "word": "prejudice",
        "kk": "[ˈprɛdʒədɪs]",
        "ipa": "/ˈpredʒudɪs/",
        "pos": "n. / v.",
        "meaning": "偏見、歧視；(v.) 使抱持偏見、損害權益",
        "formula": {
          "parts": [
            {
              "text": "pre-",
              "role": "prefix",
              "meaning": "事先 (before)"
            },
            {
              "text": "jud (jur)",
              "role": "root",
              "meaning": "審判、評判 (judge)"
            },
            {
              "text": "-ice",
              "role": "suffix",
              "meaning": "名詞字尾"
            }
          ],
          "resultMeaning": "在掌握全面事實之前便先行妄下定論 ➔「偏見、歧視」"
        },
        "sentence": "Education remains the most effective antidote against deep-seated racial prejudice and discriminatory stereotypes.",
        "sentenceZh": "教育依然是對抗根深蒂固的種族偏見與歧視性刻板印象最有效的解藥。",
        "grammar": {
          "pattern": "S + Linking Verb (remains) + SC (the most effective antidote) + Prep Phrase (against...)",
          "breakdown": [
            {
              "part": "Education",
              "role": "主詞 (Subject)",
              "note": "不可數抽象名詞。"
            },
            {
              "part": "remains",
              "role": "連綴動詞 (Linking Verb)",
              "note": "表狀態維持。"
            },
            {
              "part": "the most effective antidote",
              "role": "主詞補語 (Subject Complement)",
              "note": "antidote (解毒劑、對策)。"
            },
            {
              "part": "against deep-seated racial prejudice and discriminatory stereotypes",
              "role": "對抗介系詞片語",
              "note": "deep-seated (根深蒂固的)；prejudice and stereotypes 並列。"
            }
          ],
          "keyPoints": [
            "【文學典故】：珍·奧斯汀名作《傲慢與偏見》即為 Pride and Prejudice。",
            "【介系詞搭配】：prejudice against someone / without prejudice to something (在不損害...的前提下)。"
          ]
        }
      },
      {
        "word": "judge",
        "kk": "[dʒʌdʒ]",
        "ipa": "/dʒʌdʒ/",
        "pos": "n. / v.",
        "meaning": "法官、裁判、評判員；(v.) 判斷、審判、評定",
        "formula": {
          "parts": [
            {
              "text": "jud (jur)",
              "role": "root",
              "meaning": "法律、正義 (law, right)"
            },
            {
              "text": "ge",
              "role": "suffix",
              "meaning": "言詞、執行者"
            }
          ],
          "resultMeaning": "在法庭上執法宣告公正判決的人 ➔「法官、評判員；審判」"
        },
        "sentence": "A distinguished federal judge presided over the high-profile antitrust trial with scrupulous impartiality.",
        "sentenceZh": "一位傑出的聯邦法官以嚴謹的公正態度主持了這場備受矚目的反壟斷審判。",
        "grammar": {
          "pattern": "S + Vi (presided over O) + Prep Phrase of Manner",
          "breakdown": [
            {
              "part": "A distinguished federal judge",
              "role": "主詞 (Subject)",
              "note": "distinguished (卓越尊貴的)。"
            },
            {
              "part": "presided over",
              "role": "不及物動詞片語 (Verb)",
              "note": "preside over 表「主持(會議/審判)」。"
            },
            {
              "part": "the high-profile antitrust trial",
              "role": "介系詞受詞",
              "note": "high-profile (備受矚目的)；antitrust (反壟斷的)。"
            },
            {
              "part": "with scrupulous impartiality",
              "role": "態度介系詞片語",
              "note": "scrupulous (絲不苟的)；impartiality (不偏不倚的公正)。"
            }
          ],
          "keyPoints": [
            "【動詞片語】：preside over a meeting / a court trial 是標準司法與行政片語。",
            "【名詞衍生】：judgment (判斷、判決書，注意英美常拼作 judgment，不帶中間 e)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Scales of Righteousness: The Inscription of Jus and Jud",
      "titleZh": "正義的天平：法律與公理的裁斷",
      "intro": "「正義 (jus)」是人類社會擺脫弱肉強食叢林法則的唯一屏障。法律的尊嚴在於公平裁決，而非強權的私利。",
      "paragraphs": [
        {
          "en": "Without an impartial judicial system, civilization degenerates into lawless chaos where the powerful oppress the weak without consequence. True justice must be blind to wealth and lineage.",
          "zh": "若沒有公正無私的司法體系，文明將墮入毫無法治的混亂深淵，強者將得以肆意壓迫弱者而無需承擔任何後果。真正的正義必須無視財富與血統。"
        },
        {
          "en": "Every government policy must continuously justify its moral legitimacy in the courtroom of public conscience, ensuring that the spirit of 'jus' protects human dignity for all.",
          "zh": "每一項政府政策都必須在公眾良知的法庭上持續證明其道德正當性，以確保「正義 (jus)」的精神平等守護所有人的尊嚴。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What must true justice be blind to according to the text?",
          "qZh": "根據文章，真正的正義必須無視什麼？",
          "options": [
            "A. Wealth and lineage. (財富與血統出身)",
            "B. Written constitutions.",
            "C. Fair public trials.",
            "D. Truthful evidence."
          ],
          "answer": 0,
          "explanation": "文中第一段指出「True justice must be blind to wealth and lineage」。"
        }
      ]
    }
  },
  {
    "id": "form",
    "name": "form",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語名詞「forma」(形狀、外表、模型、樣式)。",
    "originMeaning": "形狀、樣式、模樣、形成",
    "phonetic": "/fɔːrm/",
    "icon": "📐",
    "color": "#0891B2",
    "summary": "涵蓋改革變革、通知告知、順從符合、制服統一與公式配方。",
    "words": [
      {
        "word": "reform",
        "kk": "[rɪˈfɔrm]",
        "ipa": "/rɪˈfɔːrm/",
        "pos": "v. / n.",
        "meaning": "改革、革新、重塑形態、改過自新",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再次、重新 (拉丁語 re-)"
            },
            {
              "text": "form",
              "role": "root",
              "meaning": "形狀、體制 (拉丁語 forma)"
            }
          ],
          "resultMeaning": "將陳舊不良的體制重新塑造出全新良好的形貌 ➔「改革、革新」"
        },
        "sentence": "The newly elected parliament enacted far-reaching constitutional legislation to reform taxation policies.",
        "sentenceZh": "新當選的國會頒布了影響深遠的憲政法案，以大刀闊斧改革稅收政策。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "The newly elected parliament",
              "role": "主詞 (Subject)",
              "note": "新當選國會。"
            },
            {
              "part": "enacted",
              "role": "及物動詞 (Transitive Verb)",
              "note": "頒布立法 (enact legislation)。"
            },
            {
              "part": "far-reaching constitutional legislation",
              "role": "直接受詞 (Direct Object)",
              "note": "far-reaching (影響深遠的)；legislation (法律/法規)。"
            },
            {
              "part": "to reform taxation policies",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "reform (改革)；taxation policies (稅務政策)。"
            }
          ],
          "keyPoints": [
            "【立法院常用動詞搭配】：enact / pass legislation (頒布通過法規)。",
            "【政治名詞】：reformer (改革者)、reformist (改革派的)。"
          ]
        }
      },
      {
        "word": "conform",
        "kk": "[kənˈfɔrm]",
        "ipa": "/kənˈfɔːrm/",
        "pos": "v.",
        "meaning": "符合、順從、遵照、與...一致",
        "formula": {
          "parts": [
            {
              "text": "con-",
              "role": "prefix",
              "meaning": "共同、完全 (拉丁語 com-)"
            },
            {
              "text": "form",
              "role": "root",
              "meaning": "形狀、規格 (拉丁語 forma)"
            }
          ],
          "resultMeaning": "使自己的言行或規格完全符合既定的標準模具 ➔「符合、順從」"
        },
        "sentence": "All architectural structural blueprints must conform strictly to municipal seismic building codes.",
        "sentenceZh": "所有建築結構藍圖必須嚴格符合市立抗震建築法規標準。",
        "grammar": {
          "pattern": "S + Modal + Vi + Adv + to-Prepositional Object (主詞 + 助動詞 + 不及物動詞 + 副詞 + 介系詞受詞)",
          "breakdown": [
            {
              "part": "All architectural structural blueprints",
              "role": "主詞 (Subject)",
              "note": "建築結構藍圖。"
            },
            {
              "part": "must conform",
              "role": "情態謂語 (Modal Predicate)",
              "note": "conform 為不及物動詞，固定接介系詞 to。"
            },
            {
              "part": "strictly",
              "role": "修飾副詞 (Adverb)",
              "note": "嚴格地。"
            },
            {
              "part": "to municipal seismic building codes",
              "role": "介系詞受詞 (Prepositional Object)",
              "note": "seismic (地震的/耐震的)；codes (規範守則)。"
            }
          ],
          "keyPoints": [
            "【固定搭配介系詞】：conform to / with regulations (遵照符合法規)。",
            "【社會學概念】：conformity (順從性、從眾行為)。"
          ]
        }
      },
      {
        "word": "perform",
        "kk": "[pɚˈfɔrm]",
        "ipa": "/pərˈfɔːrm/",
        "pos": "v.",
        "meaning": "執行、履行、表演、運轉",
        "formula": {
          "parts": [
            {
              "text": "per-",
              "role": "prefix",
              "meaning": "徹底、完全 (through, completely)"
            },
            {
              "text": "form",
              "role": "root",
              "meaning": "形式、成形 (form)"
            }
          ],
          "resultMeaning": "徹底把計畫形式落實為具體行動與演出 ➔「執行、履行、表演」"
        },
        "sentence": "Surgeons must perform complex microvascular surgery with unflinching concentration under high magnification.",
        "sentenceZh": "外科醫師必須在高倍放大鏡下，以毫不動搖的專注力進行複雜的微血管手術。",
        "grammar": {
          "pattern": "S + Modal + Vt (perform) + O (surgery) + Prep Phrase of Manner + Prep Phrase",
          "breakdown": [
            {
              "part": "Surgeons",
              "role": "主詞 (Subject)",
              "note": "複數名詞「外科醫師」。"
            },
            {
              "part": "must perform",
              "role": "動詞片語 (Verb)",
              "note": "perform an operation / surgery 常用動詞搭配。"
            },
            {
              "part": "complex microvascular surgery",
              "role": "直接受詞 (Direct Object)",
              "note": "microvascular (微血管的)。"
            },
            {
              "part": "with unflinching concentration",
              "role": "方法態度介系詞片語",
              "note": "unflinching (不退縮動搖的)。"
            },
            {
              "part": "under high magnification",
              "role": "條件介系詞片語",
              "note": "magnification (放大倍率)。"
            }
          ],
          "keyPoints": [
            "【多功能及物動詞】：perform a task (執行任務)、perform an experiment (進行實驗)、perform a symphony (演奏交響樂)。",
            "【派生詞】：performance (績效、表現、表演)、performer (表演者)。"
          ]
        }
      },
      {
        "word": "uniform",
        "kk": "[ˈjunəˌfɔrm]",
        "ipa": "/ˈjuːnɪfɔːrm/",
        "pos": "n. / adj.",
        "meaning": "制服；(adj.) 統一的、均勻一致的",
        "formula": {
          "parts": [
            {
              "text": "uni-",
              "role": "prefix",
              "meaning": "單一 (one)"
            },
            {
              "text": "form",
              "role": "root",
              "meaning": "形狀、樣式 (shape, form)"
            }
          ],
          "resultMeaning": "所有人穿著完全相同之單一樣式服裝 ➔「制服；統一均勻的」"
        },
        "sentence": "The industrial heating oven ensures uniform temperature distribution across the entire surface of the semiconductor wafer.",
        "sentenceZh": "該工業加熱爐確保了半導體晶圓整個表面具有均勻一致的溫度分佈。",
        "grammar": {
          "pattern": "S + Vt (ensures) + O (uniform temperature distribution) + Prep Phrase",
          "breakdown": [
            {
              "part": "The industrial heating oven",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "ensures",
              "role": "及物動詞 (Verb)",
              "note": "意為「確保、擔保」。"
            },
            {
              "part": "uniform temperature distribution",
              "role": "直接受詞 (Direct Object)",
              "note": "uniform 作形容詞「均勻一致的」。"
            },
            {
              "part": "across the entire surface of the semiconductor wafer",
              "role": "空間介系詞片語",
              "note": "wafer (晶圓)。"
            }
          ],
          "keyPoints": [
            "【形容詞義項】：uniform 作名詞是「制服」，作形容詞則表「均勻的、一律的」(uniform velocity 等速度)。",
            "【副詞衍生】：uniformly (均勻地、一致地)。"
          ]
        }
      },
      {
        "word": "formula",
        "kk": "[ˈfɔrmjələ]",
        "ipa": "/ˈfɔːrmjələ/",
        "pos": "n.",
        "meaning": "公式、配方、方案、客套話",
        "formula": {
          "parts": [
            {
              "text": "form",
              "role": "root",
              "meaning": "形式、規律 (form, pattern)"
            },
            {
              "text": "-ula",
              "role": "suffix",
              "meaning": "指小詞字尾 (small/exact rule)"
            }
          ],
          "resultMeaning": "規範事物精密結構與成分比率的標準形式 ➔「公式、配方」"
        },
        "sentence": "The beverage manufacturer safeguards its secret botanical formula within an ultra-secure vault.",
        "sentenceZh": "該飲料製造商將其秘密草本配方嚴密保管在極度安全的保險庫中。",
        "grammar": {
          "pattern": "S + Vt (safeguards) + O (formula) + Prep Phrase of Place",
          "breakdown": [
            {
              "part": "The beverage manufacturer",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "safeguards",
              "role": "及物動詞 (Verb)",
              "note": "意為「保衛、妥善守護」。"
            },
            {
              "part": "its secret botanical formula",
              "role": "直接受詞 (Direct Object)",
              "note": "botanical (植物性的、草本的)。"
            },
            {
              "part": "within an ultra-secure vault",
              "role": "地點介系詞片語",
              "note": "vault (金庫、地窖)。"
            }
          ],
          "keyPoints": [
            "【複數形式】：formula 的複數可為 regular 的 formulas，亦可為拉丁文複數 formulae！",
            "【動詞衍生】：formulate (構思規劃、配製)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Shaping of Destiny: The Crucible of Form",
      "titleZh": "命運的塑形：體制與形態的蛻變",
      "intro": "事物之存在始於「形態 (forma)」。改革者勇於重塑 (reform) 舊規，而工匠嚴格遵守 (conform) 安全法則。",
      "paragraphs": [
        {
          "en": "Human progress is an art of reshaping. When rigid customs cease to serve the common welfare, courageous reformers reshape outdated traditions into inclusive modern frameworks.",
          "zh": "人類的進步是一門重塑體制的藝術。當僵化的習俗不再能造福大眾福祉時，勇敢的改革者會將過時的傳統重新塑造成包容的現代框架。"
        },
        {
          "en": "Yet, in engineering and constitutional law, blueprints must always conform to unbending principles of integrity, proving that true freedom requires disciplined structural harmony.",
          "zh": "然而，在工程與憲政法律中，藍圖必須始終遵循堅定不移的誠信原則，證明了真正的自由必然需要嚴守紀律的結構和諧。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What do blueprints in engineering and law always need to do?",
          "qZh": "工程與法律中的藍圖必須始終做到什麼？",
          "options": [
            "A. Conform to unbending principles of integrity. (遵循堅定不移的誠信原則)",
            "B. Change randomly every hour.",
            "C. Disappear into thin air.",
            "D. Ignore all mathematical calculations."
          ],
          "answer": 0,
          "explanation": "文中第二段指出「blueprints must always conform to unbending principles of integrity」。"
        }
      ]
    }
  },
  {
    "id": "nov",
    "name": "nov",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語形容詞「novus」(新的、新鮮的、罕見的)。",
    "originMeaning": "新、創新、初學、前所未見",
    "phonetic": "/nɑːv/",
    "icon": "✨",
    "color": "#D97706",
    "summary": "涵蓋創新發明、初學者新秀、翻修翻新、新穎小說與超新星爆發。",
    "words": [
      {
        "word": "innovate",
        "kk": "[ˈɪnəˌvet]",
        "ipa": "/ˈɪnəveɪt/",
        "pos": "v.",
        "meaning": "創新、革新、引進新事物",
        "formula": {
          "parts": [
            {
              "text": "in-",
              "role": "prefix",
              "meaning": "進入、朝內 (拉丁語 in-)"
            },
            {
              "text": "nov",
              "role": "root",
              "meaning": "新 (拉丁語 novus)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "使成為、動詞字尾"
            }
          ],
          "resultMeaning": "將嶄新的元素注入既有的領域中 ➔「創新、革新」"
        },
        "sentence": "Forward-thinking technology enterprises must continually innovate to maintain competitive leadership in global artificial intelligence markets.",
        "sentenceZh": "具前瞻思維的科技企業必須持續不斷地創新，以在全球人工智慧市場中保持競爭領先地位。",
        "grammar": {
          "pattern": "S + Modal + Adv + Vi + Infinitive of Purpose (主詞 + 助動詞 + 副詞 + 不及物動詞 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Forward-thinking technology enterprises",
              "role": "主詞 (Subject)",
              "note": "前瞻科技企業。"
            },
            {
              "part": "must continually innovate",
              "role": "謂語 (Modal Predicate)",
              "note": "continually (持續地) 修飾動詞。"
            },
            {
              "part": "to maintain competitive leadership in global artificial intelligence markets",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "competitive leadership (競爭領導力)；in markets (在市場中)。"
            }
          ],
          "keyPoints": [
            "【名詞與形容詞】：innovation (創新技術/作為)、innovative (具創新思維的)。",
            "【動詞用法】：既可作及物動詞 (innovate a product)，亦常作不及物動詞 (innovate to survive)。"
          ]
        }
      },
      {
        "word": "renovate",
        "kk": "[ˈrɛnəˌvet]",
        "ipa": "/ˈrenəveɪt/",
        "pos": "v.",
        "meaning": "翻新、整修（老舊建築）、重煥生機",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再次、重新 (拉丁語 re-)"
            },
            {
              "text": "nov",
              "role": "root",
              "meaning": "新 (拉丁語 novus)"
            },
            {
              "text": "-ate",
              "role": "suffix",
              "meaning": "動詞字尾"
            }
          ],
          "resultMeaning": "使老舊斑駁的建築物再次煥然一新 ➔「翻新、整修」"
        },
        "sentence": "Urban preservationists secured philanthropic funding to renovate the crumbling historical opera theater.",
        "sentenceZh": "城市古蹟保護專家獲得了慈善資金，著手整修那座日益坍塌的老舊歷史歌劇院。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Urban preservationists",
              "role": "主詞 (Subject)",
              "note": "城市古蹟保護人士。"
            },
            {
              "part": "secured",
              "role": "及物動詞 (Transitive Verb)",
              "note": "secure funding (成功爭取到資金)。"
            },
            {
              "part": "philanthropic funding",
              "role": "直接受詞 (Direct Object)",
              "note": "慈善捐助款項。"
            },
            {
              "part": "to renovate the crumbling historical opera theater",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "renovate (翻新)；crumbling (斑駁瓦解中的)；opera theater (歌劇院)。"
            }
          ],
          "keyPoints": [
            "【高分動詞搭配】：secure funding (確保取得資金)。",
            "【建築工程常用名詞】：renovation (整修翻新工程)。"
          ]
        }
      },
      {
        "word": "novelty",
        "kk": "[ˈnɑv!tɪ]",
        "ipa": "/ˈnɑːvlti/",
        "pos": "n.",
        "meaning": "新奇、新穎、新奇事物、小玩意",
        "formula": {
          "parts": [
            {
              "text": "novel (nov)",
              "role": "root",
              "meaning": "新奇 (new)"
            },
            {
              "text": "-ty",
              "role": "suffix",
              "meaning": "抽象名詞字尾 (state/quality)"
            }
          ],
          "resultMeaning": "前所未見的全新獨特性質 ➔「新奇、新穎事物」"
        },
        "sentence": "While the technological gadget enjoyed brisk sales initially, its novelty quickly wore off after several weeks.",
        "sentenceZh": "儘管這款科技小工具最初銷量極佳，但幾週後其新鮮感便迅速消退了。",
        "grammar": {
          "pattern": "Adv Clause of Concession (While...) + S + Adv + Vi (wore off) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "While the technological gadget enjoyed brisk sales initially",
              "role": "讓步副詞子句",
              "note": "while 作「雖然、儘管」；brisk sales (熱銷)。"
            },
            {
              "part": "its novelty",
              "role": "主要句主詞 (Subject)",
              "note": "名詞「新奇感」。"
            },
            {
              "part": "quickly",
              "role": "副詞 (Adverb)",
              "note": "修飾 wore off。"
            },
            {
              "part": "wore off",
              "role": "不及物動詞片語 (Verb)",
              "note": "wear off 意為「逐漸消退、磨滅」。"
            },
            {
              "part": "after several weeks",
              "role": "時間介系詞片語",
              "note": "修飾消退的時間跨度。"
            }
          ],
          "keyPoints": [
            "【動詞片語】：wear off 表「(藥效、熱情、新鮮感) 逐漸消退消失」。",
            "【讓步連接詞】：while 置於句首常用以表對比讓步，相當於 although。"
          ]
        }
      },
      {
        "word": "novice",
        "kk": "[ˈnɑvɪs]",
        "ipa": "/ˈnɑːvɪs/",
        "pos": "n. / adj.",
        "meaning": "新手、初學者；(adj.) 初學的",
        "formula": {
          "parts": [
            {
              "text": "nov-",
              "role": "root",
              "meaning": "新 (new)"
            },
            {
              "text": "-ice",
              "role": "suffix",
              "meaning": "人稱或抽象字尾"
            }
          ],
          "resultMeaning": "剛踏入某項技術領域的新面孔 ➔「新手、初學者」"
        },
        "sentence": "Even a novice programmer can build functional interactive prototypes by leveraging modern artificial intelligence assistants.",
        "sentenceZh": "即使是初學程式設計的新手，也能藉由善用現代人工智慧助手來建構功能齊全的互動原型。",
        "grammar": {
          "pattern": "S + Modal + Vt (build) + O (prototypes) + Prep Phrase of Means (by leveraging...)",
          "breakdown": [
            {
              "part": "Even a novice programmer",
              "role": "主詞 (Subject)",
              "note": "novice 作前置形容詞修飾 programmer。"
            },
            {
              "part": "can build",
              "role": "動詞片語 (Verb)",
              "note": "情態助動詞 can + 原形動詞 build。"
            },
            {
              "part": "functional interactive prototypes",
              "role": "受詞 (Object)",
              "note": "雙重形容詞修飾 prototypes。"
            },
            {
              "part": "by leveraging modern artificial intelligence assistants",
              "role": "手段介系詞片語",
              "note": "by + 動名詞 leveraging (槓桿利用、充分利用)。"
            }
          ],
          "keyPoints": [
            "【程度級別對比】：novice (初學者) ➔ intermediate (中級者) ➔ expert / veteran (專家、老手)。",
            "【現代動詞】：leverage 作及物動詞表示「善加利用現有資源以發揮最大效益」。"
          ]
        }
      },
      {
        "word": "novel",
        "kk": "[ˈnɑv!]",
        "ipa": "/ˈnɑːvl/",
        "pos": "adj. / n.",
        "meaning": "新穎的、新奇的；(n.) 長篇小說",
        "formula": {
          "parts": [
            {
              "text": "nov-",
              "role": "root",
              "meaning": "新 (new)"
            },
            {
              "text": "-el",
              "role": "suffix",
              "meaning": "小事物、形容詞字尾"
            }
          ],
          "resultMeaning": "帶來前所未見之全新視角與故事 ➔「新奇的；長篇小說」"
        },
        "sentence": "The pharmaceutical team discovered a novel therapeutic pathway that suppresses tumor angiogenesis without damaging healthy tissue.",
        "sentenceZh": "該製藥團隊發現了一種新穎的治療途徑，能在不損害健康組織的情況下抑制腫瘤血管生成。",
        "grammar": {
          "pattern": "S + Vt (discovered) + O (a novel therapeutic pathway) + Relative Clause (that suppresses O without V-ing)",
          "breakdown": [
            {
              "part": "The pharmaceutical team",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "discovered",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "a novel therapeutic pathway",
              "role": "受詞 (Object)",
              "note": "novel 作形容詞「新穎未見的」；therapeutic (治療的)。"
            },
            {
              "part": "that suppresses tumor angiogenesis without damaging healthy tissue",
              "role": "關係子句修飾 pathway",
              "note": "that 作主格關代；without + 動名詞 damaging。"
            }
          ],
          "keyPoints": [
            "【學術英文用法】：novel 作形容詞指「全新原創的」(如 a novel coronavirus 新型冠狀病毒)。",
            "【小說體裁】：novel (長篇小說) vs. novella (中篇小說) vs. short story (短篇故事)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Dawn of the New: The Spark of Nov",
      "titleZh": "嶄新的拂曉：創生與革新的火花",
      "intro": "世界永遠渴望「新意 (novus)」。創新 (innovate) 推動科技躍進，而翻新 (renovate) 讓古老歷史獲得重生。",
      "paragraphs": [
        {
          "en": "Human history is propelled by the courage to seek the novel. Without pioneers daring to innovate beyond established orthodoxy, our ancestors would never have mastered fire, agriculture, or electricity.",
          "zh": "人類歷史是由敢於尋求新事物的勇氣所推動的。如果沒有先驅者敢於超越既有正統教條勇於創新，我們的祖先便永遠無法掌握火、農業或電力。"
        },
        {
          "en": "Equally vital is the wisdom to renovate what is venerable. By infusing ancient traditions with fresh vitality, we ensure that the flame of human culture burns ever brighter across passing eras.",
          "zh": "同樣至關重要的，是整修與煥發古老事物的智慧。藉由將嶄新的活力注入悠久的傳統之中，我們確保了人類文化的薪火在流轉的時代中燃燒得更加璀璨。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What propelled human history according to the text?",
          "qZh": "根據文章，是什麼推動了人類歷史？",
          "options": [
            "A. The courage to seek the novel and innovate beyond orthodoxy. (敢於尋求新意並超越正統創新的勇氣)",
            "B. Strict adherence to ancient superstition.",
            "C. Forbidding young people from thinking.",
            "D. Burning all new inventions."
          ],
          "answer": 0,
          "explanation": "文中第一段指出歷史是「propelled by the courage to seek the novel」。"
        }
      ]
    }
  },
  {
    "id": "pel",
    "name": "pel / puls",
    "type": "root",
    "typeLabel": "拉丁語字根 (Latin Root)",
    "etymology": "源自拉丁語動詞「pellere」(推、驅使、推動、衝擊)，過去分詞形為 pulsum。",
    "originMeaning": "推、驅使、衝擊、脈動",
    "phonetic": "/pɛl/ 或 /pʌls/",
    "icon": "⚡",
    "color": "#E11D48",
    "summary": "涵蓋推進發動、擊退排斥、強迫驅使、脈搏跳動與衝動驅力。",
    "words": [
      {
        "word": "propel",
        "kk": "[prəˈpɛl]",
        "ipa": "/prəˈpel/",
        "pos": "v.",
        "meaning": "推進、推動、驅使向前",
        "formula": {
          "parts": [
            {
              "text": "pro-",
              "role": "prefix",
              "meaning": "向前 (拉丁語 pro)"
            },
            {
              "text": "pel",
              "role": "root",
              "meaning": "推 (拉丁語 pellere)"
            }
          ],
          "resultMeaning": "用力在後方往前推使其加速前進 ➔「推進、推動」"
        },
        "sentence": "Ion thrusters emit high-speed charged xenon particles to propel scientific probes across deep space.",
        "sentenceZh": "離子推進器噴射高速帶電氙粒子，以在深空中推進科學探測船。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Locative Phrase (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 地點空間片語)",
          "breakdown": [
            {
              "part": "Ion thrusters",
              "role": "主詞 (Subject)",
              "note": "離子推進器。"
            },
            {
              "part": "emit",
              "role": "及物動詞 (Transitive Verb)",
              "note": "噴射散發。"
            },
            {
              "part": "high-speed charged xenon particles",
              "role": "直接受詞 (Direct Object)",
              "note": "高速帶電氙粒子。"
            },
            {
              "part": "to propel scientific probes across deep space",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "propel (推進)；probes (探測太空船)；across deep space (穿越深空)。"
            }
          ],
          "keyPoints": [
            "【名詞衍生】：propeller (螺旋槳)、propulsion (推進系統動力)。",
            "【比喻動詞】：propel somebody to fame (將某人推上名聲巔峰)。"
          ]
        }
      },
      {
        "word": "repel",
        "kk": "[rɪˈpɛl]",
        "ipa": "/rɪˈpel/",
        "pos": "v.",
        "meaning": "擊退、驅除、排斥（磁性）、使厭惡",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "反向、回 (拉丁語 re-)"
            },
            {
              "text": "pel",
              "role": "root",
              "meaning": "推 (拉丁語 pellere)"
            }
          ],
          "resultMeaning": "迎頭把外來侵犯的力量朝反方向推回去 ➔「擊退、排斥」"
        },
        "sentence": "In physics, identical magnetic poles naturally repel each other with an electrostatic force proportional to their proximity.",
        "sentenceZh": "在物理學中，相同的磁極會依其接近程度自然以靜電力相互排斥。",
        "grammar": {
          "pattern": "Domain Phrase + S + Adv + Vt + O + with-Instrument Phrase + Postpositive Adjective (領域狀詞 + 主詞 + 副詞 + 及物動詞 + 受詞 + 工具片語 + 後置形容詞修飾)",
          "breakdown": [
            {
              "part": "In physics",
              "role": "領域狀詞 (Domain Phrase)",
              "note": "在物理學中。"
            },
            {
              "part": "identical magnetic poles",
              "role": "主詞 (Subject)",
              "note": "同名磁極。"
            },
            {
              "part": "naturally",
              "role": "副詞 (Adverb)",
              "note": "自然而然地。"
            },
            {
              "part": "repel",
              "role": "及物動詞 (Transitive Verb)",
              "note": "排斥、互推。"
            },
            {
              "part": "each other",
              "role": "相互代名詞受詞 (Reciprocal Object)",
              "note": "彼此、互相。"
            },
            {
              "part": "with an electrostatic force",
              "role": "方式工具狀詞 (Instrumental Phrase)",
              "note": "以靜電力。"
            },
            {
              "part": "proportional to their proximity",
              "role": "後位形容詞修飾 (Adjective Phrase)",
              "note": "proportional to... (與...成比例) 修飾 force；proximity (親近/接近度)。"
            }
          ],
          "keyPoints": [
            "【成對反義】：attract (吸引) vs. repel (排斥；同名相斥、異名相吸)。",
            "【日用品常備】：mosquito repellent (防蚊驅蚊液)。"
          ]
        }
      },
      {
        "word": "compel",
        "kk": "[kəmˈpɛl]",
        "ipa": "/kəmˈpel/",
        "pos": "v.",
        "meaning": "強迫、迫使、促使",
        "formula": {
          "parts": [
            {
              "text": "com-",
              "role": "prefix",
              "meaning": "共同、完全 (together, thoroughly)"
            },
            {
              "text": "pel",
              "role": "root",
              "meaning": "驅策、推動 (drive, push)"
            }
          ],
          "resultMeaning": "自四周強力推擠驅趕迫使其前進 ➔「強迫、迫使」"
        },
        "sentence": "Mounting ecological evidence compelled municipal policymakers to enact immediate bans on single-use plastics.",
        "sentenceZh": "越來越多的生態證據迫使市政決策者立即頒布一次性塑膠禁用令。",
        "grammar": {
          "pattern": "S + Vt (compelled) + O (policymakers) + to-V (to enact O)",
          "breakdown": [
            {
              "part": "Mounting ecological evidence",
              "role": "主詞 (Subject)",
              "note": "mounting 為現在分詞作形容詞「與日俱增的」。"
            },
            {
              "part": "compelled",
              "role": "及物動詞 (Verb)",
              "note": "compel + O + to V 句型。"
            },
            {
              "part": "municipal policymakers",
              "role": "受詞 (Object)",
              "note": "「市政決策者」。"
            },
            {
              "part": "to enact immediate bans on single-use plastics",
              "role": "受詞補語 (Infinitive Complement)",
              "note": "enact (制定、頒布法令)；bans on 表針對...的禁令。"
            }
          ],
          "keyPoints": [
            "【五大句型】：compel someone to do something (迫使某人做某事)，被動為 be compelled to V。",
            "【形容詞衍生】：compelling (引人入勝的、令人信服的，如 compelling argument)。"
          ]
        }
      },
      {
        "word": "impulse",
        "kk": "[ˈɪmˌpʌls]",
        "ipa": "/ˈɪmpʌls/",
        "pos": "n.",
        "meaning": "衝動、一陣念頭、神經脈衝、推動力",
        "formula": {
          "parts": [
            {
              "text": "im- (in-)",
              "role": "prefix",
              "meaning": "向內 (into, upon)"
            },
            {
              "text": "pulse (pel)",
              "role": "root",
              "meaning": "推、驅動 (push, drive)"
            }
          ],
          "resultMeaning": "自內心深處突然爆發出的推動力量或電信號 ➔「衝動、脈衝」"
        },
        "sentence": "Consumers are frequently targeted by algorithmic marketing designed to stimulate spontaneous impulse buying.",
        "sentenceZh": "消費者經常成為旨在刺激自發性衝動購買的演算法行銷目標。",
        "grammar": {
          "pattern": "S + Passive Verb (are targeted) + Prep Phrase (by...) + Participle Phrase (designed to...)",
          "breakdown": [
            {
              "part": "Consumers",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "are frequently targeted",
              "role": "現在被動態",
              "note": "target 作動詞「鎖定為目標」。"
            },
            {
              "part": "by algorithmic marketing",
              "role": "施事介系詞片語",
              "note": "algorithmic (演算法的)。"
            },
            {
              "part": "designed to stimulate spontaneous impulse buying",
              "role": "過去分詞片語修飾 marketing",
              "note": "designed to V；impulse buying (衝動性購買)。"
            }
          ],
          "keyPoints": [
            "【商務常見字】：impulse buying / impulse purchase (衝動性消費購買)。",
            "【生物醫學義】：nerve impulse 專指生物神經系統中的「神經脈衝傳導」。"
          ]
        }
      },
      {
        "word": "expel",
        "kk": "[ɪkˈspɛl]",
        "ipa": "/ɪkˈspel/",
        "pos": "v.",
        "meaning": "驅逐、開除、排出(氣體/液體)",
        "formula": {
          "parts": [
            {
              "text": "ex-",
              "role": "prefix",
              "meaning": "向外 (out)"
            },
            {
              "text": "pel",
              "role": "root",
              "meaning": "推、驅策 (drive, push)"
            }
          ],
          "resultMeaning": "強力將人或物驅離推擠到門外 ➔「驅逐、開除、排出」"
        },
        "sentence": "The disciplinary board voted unanimously to expel the student after uncovering systematic academic dishonesty.",
        "sentenceZh": "紀律委員會在查獲系統性學術不端行為後，全體一致投票開除該名學生。",
        "grammar": {
          "pattern": "S + Vi (voted) + Adv + Infinitive of Result/Purpose (to expel O) + Prep Phrase (after uncovering O)",
          "breakdown": [
            {
              "part": "The disciplinary board",
              "role": "主詞 (Subject)",
              "note": "「紀律委員會」。"
            },
            {
              "part": "voted",
              "role": "不及物動詞 (Verb)",
              "note": "vote to do something。"
            },
            {
              "part": "unanimously",
              "role": "情狀副詞",
              "note": "修飾 voted。"
            },
            {
              "part": "to expel the student",
              "role": "不定詞片語",
              "note": "expel 接受詞 student。"
            },
            {
              "part": "after uncovering systematic academic dishonesty",
              "role": "時間介系詞片語",
              "note": "after 為介系詞接動名詞 uncovering。"
            }
          ],
          "keyPoints": [
            "【雙寫字母規則】：expelled, expelling, expulsion (名詞變化)。",
            "【同義辨析】：expel (開除驅逐) vs. dispel (驅散疑慮) vs. repel (擊退反擊)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Dynamic Impulse: The Drive of Pel and Puls",
      "titleZh": "動力與脈動：推動宇宙前行的無形之手",
      "intro": "宇宙本質上是一張巨大的「推動力 (pel-)」之網：離子推進器驅動飛船前行 (propel)，同名磁極相互排斥 (repel)。",
      "paragraphs": [
        {
          "en": "Every journey demands an initial impulse. In space exploration, advanced propulsion systems convert electrical energy into thrust, propelling scientific probes toward outer stellar frontiers.",
          "zh": "每一次遠征皆需要最初的衝力推動。在太空探索中，先進的推進系統將電能轉化為推力，驅使科學探測器飛向遙遠的恆星邊疆。"
        },
        {
          "en": "In moral life, an enlightened conscience acts like an invisible shield, repelling toxic malice and compelling us to act with noble courage for the common good.",
          "zh": "在道德生活中，覺醒的良知如同一道無形的護盾，擊退有毒的惡意，並驅使我們為了公共利益而展現崇高的勇氣。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What does an enlightened conscience do like an invisible shield?",
          "qZh": "覺醒的良知如同一道無形護盾能發揮什麼作用？",
          "options": [
            "A. Repelling toxic malice and compelling noble courage. (擊退惡意並驅使崇高的勇氣)",
            "B. Collecting gold in underground caves.",
            "C. Turning water into petroleum.",
            "D. Stopping the clock from ticking."
          ],
          "answer": 0,
          "explanation": "文中第二段指出良知「repelling toxic malice and compelling us to act with noble courage」。"
        }
      ]
    }
  },
  {
    "id": "sub",
    "name": "sub-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語介系詞「sub」(在...下方、次級、靠近 under, below, beneath)。",
    "originMeaning": "在...下方、次等、潛在、從屬",
    "phonetic": "/sʌb/",
    "icon": "🚇",
    "color": "#0284C7",
    "summary": "涵蓋潛水艇、地鐵軌道、潛意識、替代物與部屬下級的關鍵字首。",
    "words": [
      {
        "word": "submarine",
        "kk": "[ˈsʌbməˌrin]",
        "ipa": "/ˌsʌbməˈriːn/",
        "pos": "n. / adj.",
        "meaning": "(n.) 潛水艇；(adj.) 水下的、海底的",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在...下方 (拉丁語 sub)"
            },
            {
              "text": "marine",
              "role": "base",
              "meaning": "海洋的 (拉丁語 mare 海)"
            }
          ],
          "resultMeaning": "能夠完全潛入海面水層下方航行的艦艇 ➔「潛水艇」"
        },
        "sentence": "Deep-sea oceanographic submarines dive thousands of meters below sea level to investigate abyssal geothermal vents.",
        "sentenceZh": "深海海洋考察潛水艇潛入海平面以下數千公尺，以調查深淵地熱噴口。",
        "grammar": {
          "pattern": "S + Vi + Adverbial Measure Phrase + Infinitive of Purpose (主詞 + 不及物動詞 + 深度狀詞 + 目的不定詞)",
          "breakdown": [
            {
              "part": "Deep-sea oceanographic submarines",
              "role": "主詞 (Subject)",
              "note": "深海海洋考察潛水艇。"
            },
            {
              "part": "dive",
              "role": "不及物動詞 (Intransitive Verb)",
              "note": "潛水、下潛。"
            },
            {
              "part": "thousands of meters below sea level",
              "role": "深度介系詞狀詞 (Adverbial of Measure)",
              "note": "海平面下數千公尺。"
            },
            {
              "part": "to investigate abyssal geothermal vents",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "investigate (調查)；abyssal (深淵無底的)；geothermal vents (地熱噴孔)。"
            }
          ],
          "keyPoints": [
            "【詞根網絡】：sub- (下方) + mare (海洋，如 maritime 海事的)。",
            "【科技生活】：submarine cable 專指橫越全球大洋底層的「海底光纖電纜」。"
          ]
        }
      },
      {
        "word": "subconscious",
        "kk": "[sʌbˈkɑnʃəs]",
        "ipa": "/ˌsʌbˈkɑːnʃəs/",
        "pos": "adj. / n.",
        "meaning": "(adj.) 潛意識的、下意識的；(n.) 潛意識",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在...下方 (拉丁語 sub)"
            },
            {
              "text": "conscious",
              "role": "base",
              "meaning": "有意識的 (拉丁語 conscire 覺察)"
            }
          ],
          "resultMeaning": "潛藏在日常顯意識思維冰山下方的隱匿心智層面 ➔「潛意識」"
        },
        "sentence": "Cognitive psychologists reveal that subconscious behavioral biases often steer everyday financial decisions without conscious awareness.",
        "sentenceZh": "認知心理學家揭示，潛意識的行為偏誤往往在沒有意識自覺的情況下，左右著日常的財務決策。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause + without-Phrase (主詞 + 及物動詞 + That名詞子句 + 伴隨否定介系詞片語)",
          "breakdown": [
            {
              "part": "Cognitive psychologists",
              "role": "主詞 (Subject)",
              "note": "認知心理學家。"
            },
            {
              "part": "reveal",
              "role": "及物動詞 (Transitive Verb)",
              "note": "揭示表明。"
            },
            {
              "part": "that subconscious behavioral biases often steer everyday financial decisions",
              "role": "名詞子句 (Noun Clause)",
              "note": "biases (偏誤)；steer (操舵/引導)；financial decisions (財務決策)。"
            },
            {
              "part": "without conscious awareness",
              "role": "否定伴隨狀詞 (Adverbial of Manner)",
              "note": "在毫無顯意識覺察的情況下。"
            }
          ],
          "keyPoints": [
            "【心理學術語】：unconscious (無意識的) vs. subconscious (潛意識的) vs. conscious (顯意識的)。",
            "【動詞短語】：steer decisions (引導決策走向)。"
          ]
        }
      },
      {
        "word": "substitute",
        "kk": "[ˈsʌbstəˌtjut]",
        "ipa": "/ˈsʌbstɪtuːt/",
        "pos": "v. / n.",
        "meaning": "代替、替換；(n.) 代替品、替補球員",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方、代替 (under, in place of)"
            },
            {
              "text": "stat / stit",
              "role": "root",
              "meaning": "站立、設置 (stand, put)"
            },
            {
              "text": "-ute",
              "role": "suffix",
              "meaning": "動詞/名詞字尾"
            }
          ],
          "resultMeaning": "站在原位下方準備隨時替換上場 ➔「代替、替補」"
        },
        "sentence": "Culinary chefs frequently substitute Greek yogurt for sour cream to achieve a lighter texture with fewer calories.",
        "sentenceZh": "烹飪名廚經常以希臘優格取代酸奶油，以達成熱量更低且更輕盈的口感質地。",
        "grammar": {
          "pattern": "S + Adv + Vt (substitute A for B) + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "Culinary chefs",
              "role": "主詞 (Subject)",
              "note": "名詞片語。"
            },
            {
              "part": "frequently substitute",
              "role": "動詞片語 (Verb)",
              "note": "substitute A for B 句型。"
            },
            {
              "part": "Greek yogurt",
              "role": "受詞 A (新採用物)",
              "note": "希臘優格。"
            },
            {
              "part": "for sour cream",
              "role": "被取代對象 B",
              "note": "for 表被替代者。"
            },
            {
              "part": "to achieve a lighter texture with fewer calories",
              "role": "不定詞目的狀語",
              "note": "texture (質地口感)；calories 為可數名詞。"
            }
          ],
          "keyPoints": [
            "【文法大陷阱】：substitute A for B = 用 A 取代 B (A 是新的，B 被換掉)；對比 replace B with A！",
            "【可數性】：fewer calories (calorie 為可數名詞，故用 fewer 修飾，不用 less)。"
          ]
        }
      },
      {
        "word": "submerge",
        "kk": "[səbˈmɝdʒ]",
        "ipa": "/səbˈmɜːrdʒ/",
        "pos": "v.",
        "meaning": "浸沒、淹沒、潛入水中、完全隱沒",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方 (under)"
            },
            {
              "text": "merge",
              "role": "root",
              "meaning": "沉入、浸入 (dip, plunge)"
            }
          ],
          "resultMeaning": "完全沉浸在水面或液體之下 ➔「淹沒、浸入」"
        },
        "sentence": "The torrential tidal surge completely submerged low-lying coastal villages within a matter of minutes.",
        "sentenceZh": "狂暴的風暴潮在短短幾分鐘之內便將地勢低窪的沿海村莊徹底淹沒。",
        "grammar": {
          "pattern": "S + Adv + Vt (submerged) + O + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "The torrential tidal surge",
              "role": "主詞 (Subject)",
              "note": "名詞片語「狂暴潮湧」。"
            },
            {
              "part": "completely",
              "role": "程度副詞",
              "note": "修飾 submerged。"
            },
            {
              "part": "submerged",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "low-lying coastal villages",
              "role": "受詞 (Object)",
              "note": "low-lying (地勢低窪的)。"
            },
            {
              "part": "within a matter of minutes",
              "role": "時間介系詞片語",
              "note": "in a matter of... 表「在短短...之內」。"
            }
          ],
          "keyPoints": [
            "【同根辨析】：submerge (沉入水中) vs. emerge (浮現、浮出水面，e- 向外 + merge)。",
            "【固定片語】：in/within a matter of minutes/seconds 表示「在短短幾分鐘/幾秒鐘之內」。"
          ]
        }
      },
      {
        "word": "subway",
        "kk": "[ˈsʌbˌwe]",
        "ipa": "/ˈsʌbweɪ/",
        "pos": "n.",
        "meaning": "地鐵、地下鐵路、地下行人通道",
        "formula": {
          "parts": [
            {
              "text": "sub-",
              "role": "prefix",
              "meaning": "在下方 (under)"
            },
            {
              "text": "way",
              "role": "base",
              "meaning": "道路、途徑 (way, path)"
            }
          ],
          "resultMeaning": "建造於地面馬路下方的軌道交通系統 ➔「地鐵」"
        },
        "sentence": "Millions of urban commuters rely on the metropolitan subway system to bypass congested morning traffic grids.",
        "sentenceZh": "數百萬都市通勤者仰賴大眾地鐵系統，以避開早晨壅塞的交通路網。",
        "grammar": {
          "pattern": "S + Vi (rely on O) + Infinitive of Purpose (to bypass O)",
          "breakdown": [
            {
              "part": "Millions of urban commuters",
              "role": "主詞 (Subject)",
              "note": "複數名詞片語。"
            },
            {
              "part": "rely on",
              "role": "不及物動詞片語 (Verb)",
              "note": "rely on (依賴、仰仗)。"
            },
            {
              "part": "the metropolitan subway system",
              "role": "介系詞受詞",
              "note": "metropolitan (大都會的)。"
            },
            {
              "part": "to bypass congested morning traffic grids",
              "role": "不定詞目的狀語",
              "note": "bypass (繞過、避開)；congested (壅塞的)。"
            }
          ],
          "keyPoints": [
            "【英美用語差異】：美式英語用 subway；英式英語用 underground 或 the tube；法語捷運系統稱 metro。",
            "【動詞短語】：rely on / depend on 皆接介系詞 on。"
          ]
        }
      }
    ],
    "article": {
      "title": "Beneath the Surface: The Hidden Domain of Sub",
      "titleZh": "地表之下：潛藏水與心智的暗流",
      "intro": "真實的龐大體積往往潛伏在水平面之下 (sub-)。如同巨大的深海潛艇 (submarine) 與幽深的潛意識 (subconscious)。",
      "paragraphs": [
        {
          "en": "Human perception naturally fixates upon that which glitters on the surface. Yet, as deep-sea submarines explore the pitch-black abyss, they uncover vibrant ecosystems that thrive completely detached from sunlight.",
          "zh": "人類的感知天生容易聚焦在表面閃爍的光影上。然而，正如深海潛水艇在漆黑深淵中的探索一樣，它們發現了完全脫離陽光照射、卻欣欣向榮的蓬勃生態系。"
        },
        {
          "en": "Likewise, profound behavioral transformations require exploring the subconscious currents of the human mind, proving that exploring the depths of 'sub' reveals the foundational architecture of reality.",
          "zh": "同樣地，深刻的行為蛻變需要探索人類心靈的潛意識暗流，證明了深入探勘「下方 (sub)」的維度，才能真正揭開現實背後的基石架構。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What do deep-sea submarines uncover in the pitch-black abyss?",
          "qZh": "深海潛水艇在漆黑深淵中發現了什麼？",
          "options": [
            "A. Vibrant ecosystems that thrive detached from sunlight. (脫離陽光照射卻欣欣向榮的生態系)",
            "B. Sunken plastic bottles only.",
            "C. Nuclear power plants.",
            "D. Frozen ice kingdoms."
          ],
          "answer": 0,
          "explanation": "文中第一段指出潛艇發現了「vibrant ecosystems that thrive completely detached from sunlight」。"
        }
      ]
    }
  },
  {
    "id": "re",
    "name": "re-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語字首「re-」(再、重新、回、反向 again, back, backward)。",
    "originMeaning": "再、重新、回頭、反覆",
    "phonetic": "/riː/ 或 /rɪ/",
    "icon": "🔄",
    "color": "#059669",
    "summary": "英文使用頻率第一名的高產字首：代表重塑、恢復、反思、再生與復興。",
    "words": [
      {
        "word": "restore",
        "kk": "[rɪˈstɔr]",
        "ipa": "/rɪˈstɔːr/",
        "pos": "v.",
        "meaning": "恢復、修復、重建、歸還",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "回、再次 (拉丁語 re-)"
            },
            {
              "text": "store",
              "role": "root",
              "meaning": "立起、建立 (拉丁語 restaurare 重新建立)"
            }
          ],
          "resultMeaning": "將殘破衰退的事物重新扶起恢復原本樣貌 ➔「修復、恢復」"
        },
        "sentence": "Ecological reforestation initiatives restore degraded wetlands to bring back endangered bird species.",
        "sentenceZh": "生態重新造林倡議致力於修復退化的濕地，以使瀕危鳥類重返棲息地。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose (主詞 + 及物動詞 + 受詞 + 目的不定詞片語)",
          "breakdown": [
            {
              "part": "Ecological reforestation initiatives",
              "role": "主詞 (Subject)",
              "note": "生態重新造林倡議措施。"
            },
            {
              "part": "restore",
              "role": "及物動詞 (Transitive Verb)",
              "note": "修復恢復。"
            },
            {
              "part": "degraded wetlands",
              "role": "直接受詞 (Direct Object)",
              "note": "degraded (退化損害的)；wetlands (濕地)。"
            },
            {
              "part": "to bring back endangered bird species",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "bring back (帶回)；endangered species (瀕危物種)。"
            }
          ],
          "keyPoints": [
            "【雙重 re- 前綴同現】：reforestation (re 再 + forest 森林) 與 restore 皆含 re-！",
            "【高分名詞搭配】：restoration of heritage (文化遺產的修復)。"
          ]
        }
      },
      {
        "word": "revive",
        "kk": "[rɪˈvaɪv]",
        "ipa": "/rɪˈvaɪv/",
        "pos": "v.",
        "meaning": "復甦、使甦醒、使重新繁榮、重新振作",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再次 (拉丁語 re-)"
            },
            {
              "text": "vive",
              "role": "root",
              "meaning": "生命、活 (拉丁語 vivere 活著)"
            }
          ],
          "resultMeaning": "將瀕臨死亡的事物再次注入生命之火 ➔「復甦、甦醒」"
        },
        "sentence": "Paramedics performed immediate CPR to revive the unconscious diver pulled from icy coastal waters.",
        "sentenceZh": "醫護人員立即實施心肺復甦術，使從冰冷沿海水域中救起的失去知覺潛水員恢復甦醒。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive of Purpose + Past Participle Modifier (主詞 + 及物動詞 + 受詞 + 目的不定詞 + 過去分詞片語修飾)",
          "breakdown": [
            {
              "part": "Paramedics",
              "role": "主詞 (Subject)",
              "note": "緊急救護醫護人員。"
            },
            {
              "part": "performed",
              "role": "及物動詞 (Transitive Verb)",
              "note": "執行進行。"
            },
            {
              "part": "immediate CPR",
              "role": "直接受詞 (Direct Object)",
              "note": "心肺復甦術 (Cardiopulmonary Resuscitation)。"
            },
            {
              "part": "to revive the unconscious diver",
              "role": "目的狀詞 (Infinitive of Purpose)",
              "note": "revive (使甦醒)；unconscious diver (昏迷潛水員)。"
            },
            {
              "part": "pulled from icy coastal waters",
              "role": "分詞片語修飾 (Past Participle Phrase)",
              "note": "修飾 diver，相當於 who was pulled from..."
            }
          ],
          "keyPoints": [
            "【拉丁字根 vivere (活著)】：survive (在...之上活下來 ➔ 生存)、vivid (栩栩如生鮮豔的)。",
            "【名詞形式】：revival (復興、重振，如 cultural revival 文化復興)。"
          ]
        }
      },
      {
        "word": "renew",
        "kk": "[rɪˈnju]",
        "ipa": "/rɪˈnuː/",
        "pos": "v.",
        "meaning": "更新、使重獲新生、續簽、重新開始",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "再、重新 (again)"
            },
            {
              "text": "new",
              "role": "base",
              "meaning": "新 (new)"
            }
          ],
          "resultMeaning": "使原本老舊的事物再度變得煥然一新 ➔「更新、續約」"
        },
        "sentence": "Tenants must officially notify the landlord two months in advance if they intend to renew their residential lease.",
        "sentenceZh": "房客若有意續簽住宅租約，必須提前兩個月正式通知房東。",
        "grammar": {
          "pattern": "S + Modal + Adv + Vt (notify) + O (landlord) + Adv + Conditional Clause (if...)",
          "breakdown": [
            {
              "part": "Tenants",
              "role": "主詞 (Subject)",
              "note": "複數名詞「房客」。"
            },
            {
              "part": "must officially notify",
              "role": "動詞片語 (Verb)",
              "note": "notify someone (通知某人)。"
            },
            {
              "part": "the landlord",
              "role": "受詞 (Object)",
              "note": "「房東」。"
            },
            {
              "part": "two months in advance",
              "role": "時間副詞片語",
              "note": "in advance (提前)。"
            },
            {
              "part": "if they intend to renew their residential lease",
              "role": "條件副詞子句",
              "note": "intend to V (打算)；lease (租約)。"
            }
          ],
          "keyPoints": [
            "【時間搭配】：[一段時間] + in advance，如 two weeks in advance (提前兩週)。",
            "【衍生名詞/形容詞】：renewal (續約、更新)、renewable energy (再生能源)。"
          ]
        }
      },
      {
        "word": "reflect",
        "kk": "[rɪˈflɛkt]",
        "ipa": "/rɪˈflɛkt/",
        "pos": "v.",
        "meaning": "反射、反映、反思、沉思",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "往回 (back)"
            },
            {
              "text": "flect",
              "role": "root",
              "meaning": "彎曲、折射 (bend)"
            }
          ],
          "resultMeaning": "光線折回反射；或將思緒折返回來自我省察 ➔「反射；深思、反省」"
        },
        "sentence": "After the project concluded, the development team convened to reflect on operational challenges and document key learnings.",
        "sentenceZh": "專案結束後，開發團隊齊聚一堂，共同反思營運挑戰並記錄關鍵學習心得。",
        "grammar": {
          "pattern": "Adv Clause of Time (After...) + S + Vi (convened) + Infinitive of Purpose (to reflect on... and document...)",
          "breakdown": [
            {
              "part": "After the project concluded",
              "role": "時間副詞子句",
              "note": "concluded (結束)。"
            },
            {
              "part": "the development team",
              "role": "主要句主詞 (Subject)",
              "note": "集合名詞。"
            },
            {
              "part": "convened",
              "role": "不及物動詞 (Verb)",
              "note": "意為「集會、召集開會」。"
            },
            {
              "part": "to reflect on operational challenges",
              "role": "不定詞目的狀語 1",
              "note": "reflect on + N. 表「深思反省...」。"
            },
            {
              "part": "and document key learnings",
              "role": "對等不定詞目的狀語 2",
              "note": "document 作及物動詞「記錄歸檔」。"
            }
          ],
          "keyPoints": [
            "【介系詞搭配】：reflect on / upon something 專指「對某事進行深入反省或思考」。",
            "【折疊字根】：flect / flex 表彎曲，如 flexible (有彈性的)、deflect (偏折)、inflection (音調轉折)。"
          ]
        }
      },
      {
        "word": "return",
        "kk": "[rɪˈtɝn]",
        "ipa": "/rɪˈtɜːrn/",
        "pos": "v. / n.",
        "meaning": "返回、歸還、回饋；(n.) 收益、回報、歸還",
        "formula": {
          "parts": [
            {
              "text": "re-",
              "role": "prefix",
              "meaning": "回、再 (back, again)"
            },
            {
              "text": "turn",
              "role": "base",
              "meaning": "轉向、轉動 (turn)"
            }
          ],
          "resultMeaning": "轉身向後走回原點 ➔「返回、歸還、回報」"
        },
        "sentence": "The international diplomat pledged to return to the negotiating table once a verifiable ceasefire had been declared.",
        "sentenceZh": "這位國際外交官承諾，一旦宣布了可查證的停火協議，他將重返談判桌。",
        "grammar": {
          "pattern": "S + Vt (pledged) + to-V (to return to...) + Adv Clause of Time (once...)",
          "breakdown": [
            {
              "part": "The international diplomat",
              "role": "主詞 (Subject)",
              "note": "diplomat (外交官)。"
            },
            {
              "part": "pledged",
              "role": "及物動詞 (Verb)",
              "note": "pledge to do something (承諾、宣誓做某事)。"
            },
            {
              "part": "to return to the negotiating table",
              "role": "不定詞受詞",
              "note": "return to (回到...)。"
            },
            {
              "part": "once a verifiable ceasefire had been declared",
              "role": "時間副詞子句",
              "note": "once 表一旦；had been declared 為過去完成被動態。"
            }
          ],
          "keyPoints": [
            "【時態先後關係】：pledged (過去式承諾) vs. had been declared (在此之前已先被宣布停火)。",
            "【財經常見義】：return on investment (投資報酬率 ROI)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Circle of Renewal: The Eternity of Re-",
      "titleZh": "復興之環：再生的永恆之歌",
      "intro": "宇宙沒有絕對的終結，唯有永恆的「重來 (re-)」。冬去春來，生命在大地上不斷修復 (restore) 與復甦 (revive)。",
      "paragraphs": [
        {
          "en": "Destruction is never the final chapter in the book of life. When wildfires scour ancient forests, dormant seeds buried deep in the ash seize the rains to restore the verdant canopy with renewed vigor.",
          "zh": "毀滅絕非生命之書的最終篇章。當野火肆虐古老森林後，深埋在灰燼中的休眠種子會把握雨水的滋潤，以重生的活力修復那片青翠的林冠。"
        },
        {
          "en": "Human history shares this cyclical triumph. Whenever crisis shatters our peace, our collective resolve revives cultural bonds, proving that the prefix 're-' is the eternal heartbeat of hope.",
          "zh": "人類歷史同樣體現著這種周而復始的勝利。每當危機擊碎我們的和平時，我們集體的堅定意志便會重振文化連結，證明了字首「re-」正是希望永不熄滅的心跳。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What do dormant seeds do after wildfires scour forests?",
          "qZh": "野火肆虐森林後，休眠種子會怎麼做？",
          "options": [
            "A. Seize rains to restore the verdant canopy with renewed vigor. (把握雨水滋潤以重生的活力修復青翠林冠)",
            "B. Fly away into outer space.",
            "C. Turn into solid iron stones.",
            "D. Stop growing forever."
          ],
          "answer": 0,
          "explanation": "文中第一段指出種子會「seize the rains to restore the verdant canopy with renewed vigor」。"
        }
      ]
    }
  },
  {
    "id": "inter",
    "name": "inter-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語介系詞「inter」(在...之間、相互、彼此 between, among)。",
    "originMeaning": "在...之間、相互、跨越兩者",
    "phonetic": "/ˈɪntɚ/",
    "icon": "🌐",
    "color": "#2563EB",
    "summary": "全球化國際體系、網際網路、互動合作、干涉干預與從中調停的核心字首。",
    "words": [
      {
        "word": "interact",
        "kk": "[ˌɪntɚˈækt]",
        "ipa": "/ˌɪntərˈækt/",
        "pos": "v.",
        "meaning": "互相作用、交流互動、相互影響",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間 (拉丁語 inter)"
            },
            {
              "text": "act",
              "role": "base",
              "meaning": "行動 (拉丁語 agere 做/行動)"
            }
          ],
          "resultMeaning": "在兩個或多個個體之間彼此相互行動產生影響 ➔「互動、交互作用」"
        },
        "sentence": "Collaborative software platforms enable geographically dispersed researchers to interact seamlessly in real time.",
        "sentenceZh": "協同軟體平台使地理上分散在各地的研究人員能夠即時進行無縫的交流互動。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive Complement + Manner Phrase (主詞 + 及物動詞 + 受詞 + 不定詞補語 + 方式狀詞)",
          "breakdown": [
            {
              "part": "Collaborative software platforms",
              "role": "主詞 (Subject)",
              "note": "協同軟體平台。"
            },
            {
              "part": "enable",
              "role": "使動及物動詞 (Causative/Enabling Verb)",
              "note": "enable + O + to V (使...能夠做...)。"
            },
            {
              "part": "geographically dispersed researchers",
              "role": "直接受詞 (Direct Object)",
              "note": "地理上分散的研究人員 (dispersed 過去分詞作形容詞)。"
            },
            {
              "part": "to interact seamlessly in real time",
              "role": "受詞補語 (Objective Complement)",
              "note": "interact (互動)；seamlessly (無縫地)；in real time (即時地)。"
            }
          ],
          "keyPoints": [
            "【高階使動句型】：enable somebody to do something。",
            "【介系詞搭配】：interact with somebody / something (與...互動)。"
          ]
        }
      },
      {
        "word": "interfere",
        "kk": "[ˌɪntɚˈfɪr]",
        "ipa": "/ˌɪntərˈfɪr/",
        "pos": "v.",
        "meaning": "干涉、干擾、妨礙（不及物動詞）",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間 (拉丁語 inter)"
            },
            {
              "text": "fere",
              "role": "root",
              "meaning": "敲擊 (拉丁語 ferire 打擊)"
            }
          ],
          "resultMeaning": "硬插進別人兩造中間進行敲打干擾 ➔「干涉、妨礙」"
        },
        "sentence": "Sovereign nations sign treaties agreeing not to interfere unlawfully in the domestic democratic elections of neighboring states.",
        "sentenceZh": "主權國家簽署條約，一致同意絕不非法干涉鄰國國內的民主選舉。",
        "grammar": {
          "pattern": "S + Vt + O + Participle Complement + Infinitive (主詞 + 及物動詞 + 受詞 + 分詞補語 + 否定不定詞)",
          "breakdown": [
            {
              "part": "Sovereign nations",
              "role": "主詞 (Subject)",
              "note": "主權國家。"
            },
            {
              "part": "sign",
              "role": "及物動詞 (Transitive Verb)",
              "note": "簽署。"
            },
            {
              "part": "treaties",
              "role": "直接受詞 (Direct Object)",
              "note": "條約。"
            },
            {
              "part": "agreeing not to interfere unlawfully in the domestic democratic elections of neighboring states",
              "role": "現在分詞伴隨修飾 (Participial Phrase)",
              "note": "agree not to V (同意不去...)；interfere in (干預涉足，介系詞用 in)。"
            }
          ],
          "keyPoints": [
            "【介系詞搭配】：interfere in politics/affairs (干預涉入某事)；interfere with a plan (妨礙計畫順利進行)。",
            "【名詞形式】：interference (干涉、訊號干擾)。"
          ]
        }
      },
      {
        "word": "international",
        "kk": "[ˌɪntɚˈnæʃən!]",
        "ipa": "/ˌɪntərˈnæʃnəl/",
        "pos": "adj.",
        "meaning": "國際的、跨國的、世界性的",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間 (between, among)"
            },
            {
              "text": "nation",
              "role": "root",
              "meaning": "國家、民族 (nation)"
            },
            {
              "text": "-al",
              "role": "suffix",
              "meaning": "形容詞字尾"
            }
          ],
          "resultMeaning": "發生或建立在各主權國家彼此之間的 ➔「國際的、跨國的」"
        },
        "sentence": "The humanitarian summit brought together international delegates to draft comprehensive treaties on climate migration.",
        "sentenceZh": "這場人道主義高峰會匯聚了國際各國代表，共同起草關於氣候難民遷移的全面性條約。",
        "grammar": {
          "pattern": "S + Vt (brought together) + O (delegates) + Infinitive of Purpose (to draft...)",
          "breakdown": [
            {
              "part": "The humanitarian summit",
              "role": "主詞 (Subject)",
              "note": "summit (高峰會議)。"
            },
            {
              "part": "brought together",
              "role": "動詞片語 (Verb)",
              "note": "bring together 表「聚集、凝聚」。"
            },
            {
              "part": "international delegates",
              "role": "受詞 (Object)",
              "note": "delegates (代表)。"
            },
            {
              "part": "to draft comprehensive treaties on climate migration",
              "role": "不定詞目的狀語",
              "note": "draft (起草)；treaties (條約)。"
            }
          ],
          "keyPoints": [
            "【字首辨析】：inter- (在...之間，如 international 跨國的) vs. intra- (在內部，如 intranational 國內的, intravenous 靜脈內的)。",
            "【名詞衍生】：internationalism (國際主義)、internationalize (使國際化)。"
          ]
        }
      },
      {
        "word": "intersect",
        "kk": "[ˌɪntɚˈsɛkt]",
        "ipa": "/ˌɪntərˈsekt/",
        "pos": "v.",
        "meaning": "相交、交叉、貫穿、交會",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間 (between)"
            },
            {
              "text": "sect",
              "role": "root",
              "meaning": "切割、劃分 (cut)"
            }
          ],
          "resultMeaning": "彼此切割穿透並交會於同一點 ➔「相交、交會」"
        },
        "sentence": "Urban planners designed a multi-level rotary where two major transcontinental expressways intersect.",
        "sentenceZh": "都市規劃師在兩條主要跨洲高速公路交會處設計了一座多層立體圓環。",
        "grammar": {
          "pattern": "S + Vt (designed) + O (rotary) + Relative Adverb Clause (where two expressways intersect)",
          "breakdown": [
            {
              "part": "Urban planners",
              "role": "主詞 (Subject)",
              "note": "複數名詞「都市規劃師」。"
            },
            {
              "part": "designed",
              "role": "及物動詞 (Verb)",
              "note": "過去簡單式。"
            },
            {
              "part": "a multi-level rotary",
              "role": "直接受詞 (Direct Object)",
              "note": "rotary (環島、圓環路口)。"
            },
            {
              "part": "where two major transcontinental expressways intersect",
              "role": "關係副詞子句修飾 rotary",
              "note": "where 指地點；intersect 為不及物動詞。"
            }
          ],
          "keyPoints": [
            "【切割字根】：sect 表切割，如 section (部分)、dissect (解剖)、sector (部門/扇形)。",
            "【名詞衍生】：intersection (十字路口、交集)。"
          ]
        }
      },
      {
        "word": "interview",
        "kk": "[ˈɪntɚˌvju]",
        "ipa": "/ˈɪntərvjuː/",
        "pos": "n. / v.",
        "meaning": "面試、訪談、採訪；(v.) 對...進行面試/訪談",
        "formula": {
          "parts": [
            {
              "text": "inter-",
              "role": "prefix",
              "meaning": "在...之間、互相 (between, mutually)"
            },
            {
              "text": "view",
              "role": "root",
              "meaning": "看、審視 (see, look)"
            }
          ],
          "resultMeaning": "兩人在彼此面對面之間相互審視評估 ➔「面試、訪談」"
        },
        "sentence": "The panel of senior managers will interview shortlisted applicants tomorrow afternoon to assess their leadership capabilities.",
        "sentenceZh": "高階主管評審團將於明日下午面試入圍的申請者，以評估他們的領導才能。",
        "grammar": {
          "pattern": "S + Modal + Vt (interview) + O + Adv of Time + Infinitive of Purpose",
          "breakdown": [
            {
              "part": "The panel of senior managers",
              "role": "主詞 (Subject)",
              "note": "panel (小組、遴選團)。"
            },
            {
              "part": "will interview",
              "role": "動詞片語 (Verb)",
              "note": "未來式。"
            },
            {
              "part": "shortlisted applicants",
              "role": "直接受詞 (Direct Object)",
              "note": "shortlisted 作形容詞「入選決選名單的」。"
            },
            {
              "part": "tomorrow afternoon",
              "role": "時間副詞片語",
              "note": "修飾時間。"
            },
            {
              "part": "to assess their leadership capabilities",
              "role": "不定詞目的狀語",
              "note": "assess (評估)。"
            }
          ],
          "keyPoints": [
            "【詞源巧思】：inter (互相) + view (看)，兩人面對面彼此觀察相看！",
            "【人稱辨析】：interviewer (面試官) vs. interviewee (受試者)。"
          ]
        }
      }
    ],
    "article": {
      "title": "The Web of Connection: The Crossroads of Inter",
      "titleZh": "連結的網絡：彼此交織的生命十字路",
      "intro": "沒有任何個體是一座孤島。字首 inter- 構築了全人類相互交流 (interact) 與跨界合作的宏偉網絡。",
      "paragraphs": [
        {
          "en": "Modern life is entirely defined by interconnected networks. From international trade routes to satellite constellations, our prosperity thrives upon the seamless capacity to communicate across borders.",
          "zh": "現代生活完全被相互連結的網絡所定義。從國際貿易路線到衛星星座，我們的繁榮奠基於跨越國界無縫溝通的能力。"
        },
        {
          "en": "While respecting boundaries by refusing to interfere in sovereign freedoms, we must continually foster cross-cultural interactions, ensuring that our shared planet remains an open dialogue rather than isolated camps.",
          "zh": "在透過拒絕非法干預主權自由來尊重邊界的同時，我們必須不斷促進跨文化交流互動，確保我們共有的地球維持開放對話的姿態，而非分裂為封閉的陣營。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What defines modern life according to the article?",
          "qZh": "根據文章，何者定義了現代生活？",
          "options": [
            "A. Interconnected networks and cross-border communication. (相互連結的網絡與跨界溝通)",
            "B. Complete isolation in mountain caves.",
            "C. Stopping all scientific trade.",
            "D. Abandoning internet technology."
          ],
          "answer": 0,
          "explanation": "文中第一段指出現代生活「is entirely defined by interconnected networks」。"
        }
      ]
    }
  },
  {
    "id": "mal",
    "name": "mal- / male-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語副詞/形容詞「malus / male」(惡、壞、不良、不當 bad, evil, badly)。",
    "originMeaning": "惡、壞、不良、失常、有害",
    "phonetic": "/mæl/ 或 /ˈmæli/",
    "icon": "⚠️",
    "color": "#DC2626",
    "summary": "涵蓋機器故障失靈、營養不良、惡意惡毒、惡性腫瘤與弊端弊案。",
    "words": [
      {
        "word": "malfunction",
        "kk": "[mælˈfʌŋkʃən]",
        "ipa": "/ˌmælˈfʌŋkʃn/",
        "pos": "v. / n.",
        "meaning": "(v.) 發生故障、運作失靈；(n.) 故障、功能障礙",
        "formula": {
          "parts": [
            {
              "text": "mal-",
              "role": "prefix",
              "meaning": "壞、不良 (拉丁語 malus)"
            },
            {
              "text": "function",
              "role": "base",
              "meaning": "功能、運作 (拉丁語 functio 履行職責)"
            }
          ],
          "resultMeaning": "機器或器官的功能運轉陷入不良失常狀態 ➔「故障、運作失靈」"
        },
        "sentence": "A minor electrical malfunction in the cooling circuit forced the chemical plant to shut down its reactors automatically.",
        "sentenceZh": "冷卻電路中一處微小的電氣故障，迫使該化學工廠自動關閉其反應爐。",
        "grammar": {
          "pattern": "S + Vt + O + Infinitive Complement + Adv (主詞 + 及物動詞 + 受詞 + 不定詞補語 + 方式副詞)",
          "breakdown": [
            {
              "part": "A minor electrical malfunction in the cooling circuit",
              "role": "主詞 (Subject)",
              "note": "冷卻電路中的微小電氣故障。"
            },
            {
              "part": "forced",
              "role": "及物動詞 (Transitive Verb)",
              "note": "force + O + to V (迫使...做...)。"
            },
            {
              "part": "the chemical plant",
              "role": "直接受詞 (Direct Object)",
              "note": "化學工廠。"
            },
            {
              "part": "to shut down its reactors",
              "role": "受詞補語 (Objective Complement)",
              "note": "shut down (關閉停機)；reactors (反應爐)。"
            },
            {
              "part": "automatically",
              "role": "副詞 (Adverb of Manner)",
              "note": "自動地。"
            }
          ],
          "keyPoints": [
            "【前綴對稱】：bene- (良好功能) vs. mal- (功能失常 malfunction)。",
            "【及物使動句型】：force somebody/something to do something。"
          ]
        }
      },
      {
        "word": "malicious",
        "kk": "[məˈlɪʃəs]",
        "ipa": "/məˈlɪʃəs/",
        "pos": "adj.",
        "meaning": "懷有惡意的、惡毒的、蓄意危害的",
        "formula": {
          "parts": [
            {
              "text": "mal-",
              "role": "prefix",
              "meaning": "壞、惡 (拉丁語 malus)"
            },
            {
              "text": "-icious",
              "role": "suffix",
              "meaning": "充滿...特質的 (形容詞字尾)"
            }
          ],
          "resultMeaning": "心胸中充滿了想加害傷害他人之惡毒念頭的 ➔「懷有惡意的、惡毒的」"
        },
        "sentence": "Cybersecurity firewalls blocked an onslaught of malicious spyware packets engineered by criminal syndicates.",
        "sentenceZh": "網路安全防火牆阻擋了一波由犯罪集團精心設計的惡意間諜軟體資料封包的猛烈攻擊。",
        "grammar": {
          "pattern": "S + Vt + O + Past Participle Modifier (主詞 + 及物動詞 + 受詞 + 過去分詞片語修飾)",
          "breakdown": [
            {
              "part": "Cybersecurity firewalls",
              "role": "主詞 (Subject)",
              "note": "網路安全防火牆。"
            },
            {
              "part": "blocked",
              "role": "及物動詞 (Transitive Verb)",
              "note": "阻擋攔截。"
            },
            {
              "part": "an onslaught of malicious spyware packets",
              "role": "直接受詞 (Direct Object)",
              "note": "onslaught (猛攻突襲)；malicious (惡意的)；spyware (間諜軟體)。"
            },
            {
              "part": "engineered by criminal syndicates",
              "role": "過去分詞片語修飾 (Past Participle Phrase)",
              "note": "engineered by... (由...精心編寫打造)；syndicates (犯罪集團/辛迪加)。"
            }
          ],
          "keyPoints": [
            "【資安高頻簡寫】：malicious software 在資訊科學中直接簡寫為 malware (惡意軟體)！",
            "【成對反義詞】：benevolent (仁慈善良的) vs. malicious (蓄意惡毒的)。"
          ]
        }
      },
      {
        "word": "malnutrition",
        "kk": "[ˌmælnjuˈtrɪʃən]",
        "ipa": "/ˌmælnuːˈtrɪʃn/",
        "pos": "n.",
        "meaning": "營養不良",
        "formula": {
          "parts": [
            {
              "text": "mal-",
              "role": "prefix",
              "meaning": "壞、不良 (bad, abnormal)"
            },
            {
              "text": "nutrition",
              "role": "base",
              "meaning": "營養 (nourishment)"
            }
          ],
          "resultMeaning": "身體攝取的營養失調或極度匱乏 ➔「營養不良」"
        },
        "sentence": "Prolonged agricultural droughts in sub-Saharan regions have triggered acute child malnutrition across vulnerable communities.",
        "sentenceZh": "撒哈拉以南非洲地區長期的農業乾旱，在脆弱社區引發了嚴重的兒童營養不良危機。",
        "grammar": {
          "pattern": "S + Vt (have triggered) + O (malnutrition) + Prep Phrase",
          "breakdown": [
            {
              "part": "Prolonged agricultural droughts in sub-Saharan regions",
              "role": "主詞 (Subject)",
              "note": "prolonged (長期的)；droughts (乾旱)。"
            },
            {
              "part": "have triggered",
              "role": "及物動詞 (Verb)",
              "note": "現在完成式。"
            },
            {
              "part": "acute child malnutrition",
              "role": "直接受詞 (Direct Object)",
              "note": "acute (急性的、嚴重的)。"
            },
            {
              "part": "across vulnerable communities",
              "role": "地點介系詞片語",
              "note": "vulnerable (脆弱的)。"
            }
          ],
          "keyPoints": [
            "【字首家族】：mal- (惡劣)，如 malpractice (瀆職)、maltreat (虐待)、malodor (惡臭)。",
            "【醫學形容詞】：acute (急性的) vs. chronic (慢性的)。"
          ]
        }
      },
      {
        "word": "malpractice",
        "kk": "[mælˈpræktɪs]",
        "ipa": "/mælˈpræktɪs/",
        "pos": "n.",
        "meaning": "玩忽職守、醫療疏失、瀆職行徑",
        "formula": {
          "parts": [
            {
              "text": "mal-",
              "role": "prefix",
              "meaning": "不良、壞 (bad)"
            },
            {
              "text": "practice",
              "role": "base",
              "meaning": "業務實踐、執業 (action, conduct)"
            }
          ],
          "resultMeaning": "專業人員背離職業規範的失職犯罪行為 ➔「玩忽職守、醫療疏失」"
        },
        "sentence": "Physicians carry comprehensive insurance to protect themselves against catastrophic medical malpractice lawsuits.",
        "sentenceZh": "執業醫師購買全額保險，以保護自己免於災難性的醫療過失訴訟。",
        "grammar": {
          "pattern": "S + Vt (carry) + O (insurance) + Infinitive of Purpose (to protect oneself against...)",
          "breakdown": [
            {
              "part": "Physicians",
              "role": "主詞 (Subject)",
              "note": "「內科醫生」。"
            },
            {
              "part": "carry",
              "role": "及物動詞 (Verb)",
              "note": "carry insurance (投保、持有保險)。"
            },
            {
              "part": "comprehensive insurance",
              "role": "受詞 (Object)",
              "note": "「綜合/全額保險」。"
            },
            {
              "part": "to protect themselves against catastrophic medical malpractice lawsuits",
              "role": "不定詞目的狀語",
              "note": "protect A against B (保護 A 免於 B)。"
            }
          ],
          "keyPoints": [
            "【動詞用法】：carry insurance 是專業保險慣用動詞，表示「持有...保單」。",
            "【介系詞搭配】：protect / guard someone against / from something。"
          ]
        }
      },
      {
        "word": "malaria",
        "kk": "[məˈlɛrɪə]",
        "ipa": "/məˈleriə/",
        "pos": "n.",
        "meaning": "瘧疾 (由瘧蚊叮咬傳播之寄生蟲熱病)",
        "formula": {
          "parts": [
            {
              "text": "mal-",
              "role": "prefix",
              "meaning": "壞、不良 (bad)"
            },
            {
              "text": "aria (air)",
              "role": "base",
              "meaning": "空氣 (air)"
            }
          ],
          "resultMeaning": "古代羅馬人認為源自沼澤惡臭腐敗空氣所致之熱病 ➔「瘧疾」"
        },
        "sentence": "The distribution of insecticide-treated bed nets has dramatically curtailed the spread of malaria in tropical villages.",
        "sentenceZh": "經殺蟲劑處理之防蚊帳的分發，極大幅度地遏制了熱帶村落中瘧疾的傳播。",
        "grammar": {
          "pattern": "S + Vt (has curtailed) + O (the spread of malaria) + Prep Phrase of Place",
          "breakdown": [
            {
              "part": "The distribution of insecticide-treated bed nets",
              "role": "主詞 (Subject)",
              "note": "insecticide-treated (經殺蟲劑處理的)。"
            },
            {
              "part": "has dramatically curtailed",
              "role": "現在完成動詞片語",
              "note": "dramatically (劇烈地)；curtailed (縮減、遏止)。"
            },
            {
              "part": "the spread of malaria",
              "role": "直接受詞 (Direct Object)",
              "note": "spread 作名詞。"
            },
            {
              "part": "in tropical villages",
              "role": "地點介系詞片語",
              "note": "tropical (熱帶的)。"
            }
          ],
          "keyPoints": [
            "【醫學歷史詞源】：源自義大利語 mala aria (壞空氣)，印證了古代瘴氣學說對現代醫學詞彙的影響！",
            "【及物動詞】：curtail 表示「削減、遏制、截斷」。"
          ]
        }
      }
    ],
    "article": {
      "title": "Shadows in the Code: The Vigilance Against Mal-",
      "titleZh": "暗影之隙：防範惡意與故障的警鐘",
      "intro": "正如光明伴隨陰影，文明的精密體系亦時刻面臨著失靈 (malfunction) 與惡意 (malicious) 的考驗。",
      "paragraphs": [
        {
          "en": "In every sophisticated complex system, failure rarely arrives unannounced; it begins as a micro-level malfunction that goes unaddressed until catastrophic failure ensues.",
          "zh": "在每一個高度精密的複雜系統中，災難鮮少是不告而至的，它最初往往只是一個未被及時處理的微小故障，直到最終釀成災難性的崩潰。"
        },
        {
          "en": "By identifying malicious digital incursions with vigilant vigilance and remedying technical faults promptly, engineers safeguard human infrastructure against the destructive shadow of 'mal'.",
          "zh": "藉由以高度的警惕辨識出惡意數位入侵，並及時修復技術缺陷，工程師守護著人類的基礎設施免於陷入「惡與缺陷 (mal)」的破壞性陰影之中。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "How does failure typically begin in complex systems according to the passage?",
          "qZh": "根據文章，複雜系統中的失敗通常是如何開始的？",
          "options": [
            "A. As an unaddressed micro-level malfunction. (最初作為一個未被處理的微小故障)",
            "B. As a sudden thunderstorm from outer space.",
            "C. By deliberate government law.",
            "D. As pure divine intervention."
          ],
          "answer": 0,
          "explanation": "文中第一段指出失敗「begins as a micro-level malfunction that goes unaddressed」。"
        }
      ]
    }
  },
  {
    "id": "super",
    "name": "super- / sur-",
    "type": "prefix",
    "typeLabel": "拉丁語字首 (Latin Prefix)",
    "etymology": "源自拉丁語介系詞「super」(在...之上、超越、過度 above, over, beyond)。",
    "originMeaning": "在...之上、超越、過度、頂尖",
    "phonetic": "/ˈsuːpər/ 或 /sɜːr/",
    "icon": "🌟",
    "color": "#D97706",
    "summary": "涵蓋超自然現象、優等卓越、監督俯察、地表表層與剩餘盈餘。",
    "words": [
      {
        "word": "superior",
        "kk": "[sʊˈpɪrɪɚ]",
        "ipa": "/suːˈpɪriər/",
        "pos": "adj. / n.",
        "meaning": "(adj.) 卓越的、優越的、級別更高的；(n.) 上司長官",
        "formula": {
          "parts": [
            {
              "text": "super-",
              "role": "prefix",
              "meaning": "在...之上 (拉丁語 super)"
            },
            {
              "text": "-ior",
              "role": "suffix",
              "meaning": "比較級字尾 (拉丁語形容詞比較級)"
            }
          ],
          "resultMeaning": "位置、品質或位階凌駕在他人之上的 ➔「卓越的、優越的、上級」"
        },
        "sentence": "Rigorous laboratory testing proved that the new ceramic composite exhibits superior durability under extreme thermal stress.",
        "sentenceZh": "嚴謹的實驗室測試證實，這種新型陶瓷複合材料在極端熱應力下展現出更優越的耐用度。",
        "grammar": {
          "pattern": "S + Vt + That-Noun Clause + Under-Phrase (主詞 + 及物動詞 + That名詞子句 + 條件介系詞片語)",
          "breakdown": [
            {
              "part": "Rigorous laboratory testing",
              "role": "主詞 (Subject)",
              "note": "嚴格的實驗室檢驗測試。"
            },
            {
              "part": "proved",
              "role": "及物動詞 (Transitive Verb)",
              "note": "證實證明。"
            },
            {
              "part": "that the new ceramic composite exhibits superior durability",
              "role": "名詞子句 (Noun Clause)",
              "note": "ceramic composite (陶瓷複合材料)；exhibits (展現)；superior (優越的)；durability (耐用度)。"
            },
            {
              "part": "under extreme thermal stress",
              "role": "條件介系詞片語 (Condition Phrase)",
              "note": "在極端熱應力環境下。"
            }
          ],
          "keyPoints": [
            "【拉丁比較級特殊介系詞】：superior to (優於...)，比較對象必須搭配 to，嚴禁使用 than！",
            "【成對反義詞】：superior (優於) vs. inferior (劣於；inferior to)。"
          ]
        }
      },
      {
        "word": "surplus",
        "kk": "[ˈsɝpləs]",
        "ipa": "/ˈsɜːrpləs/",
        "pos": "n. / adj.",
        "meaning": "(n.) 盈餘、剩餘、過剩；(adj.) 剩餘過剩的",
        "formula": {
          "parts": [
            {
              "text": "sur-",
              "role": "prefix",
              "meaning": "在...之上、超過 (拉丁語 super 經法語縮寫)"
            },
            {
              "text": "plus",
              "role": "base",
              "meaning": "更多 (拉丁語 plus)"
            }
          ],
          "resultMeaning": "數量已經超過了原本額度多出於其上的部分 ➔「盈餘、過剩」"
        },
        "sentence": "Thanks to record agricultural harvests, the regional food cooperative exported its grain surplus to drought-stricken neighbors.",
        "sentenceZh": "多虧了創紀錄的豐沛農產收穫，該區域糧食合作社將過剩盈餘的穀物出口至遭受旱災的鄰近地區。",
        "grammar": {
          "pattern": "Prepositional Cause Phrase + S + Vt + O + to-Recipient Phrase (原因介系詞成語 + 主詞 + 及物動詞 + 受詞 + 接收對象介系詞片語)",
          "breakdown": [
            {
              "part": "Thanks to record agricultural harvests",
              "role": "原因狀詞 (Adverbial of Cause)",
              "note": "Thanks to (多虧/幸虧)；harvests (農作收成)。"
            },
            {
              "part": "the regional food cooperative",
              "role": "主詞 (Subject)",
              "note": "區域食品合作社。"
            },
            {
              "part": "exported",
              "role": "及物動詞 (Transitive Verb)",
              "note": "出口外銷。"
            },
            {
              "part": "its grain surplus",
              "role": "直接受詞 (Direct Object)",
              "note": "穀物過剩盈餘。"
            },
            {
              "part": "to drought-stricken neighbors",
              "role": "接收端介系詞片語 (Prepositional Phrase)",
              "note": "drought-stricken (遭受乾旱侵襲的) 為複合形容詞修飾鄰居/鄰國。"
            }
          ],
          "keyPoints": [
            "【經濟學重要指標】：budget surplus (預算盈餘) vs. budget deficit (預算赤字)。",
            "【前綴變體】：sur- 即為 super- 的法語變形，同見於 surface (表面；sur + face 臉/表面)。"
          ]
        }
      },
      {
        "word": "supervise",
        "kk": "[ˈsupɚˌvaɪz]",
        "ipa": "/ˈsuːpərvaɪz/",
        "pos": "v.",
        "meaning": "監督、指導、管理",
        "formula": {
          "parts": [
            {
              "text": "super-",
              "role": "prefix",
              "meaning": "在上方 (above, over)"
            },
            {
              "text": "vise (vis)",
              "role": "root",
              "meaning": "看 (look, see)"
            }
          ],
          "resultMeaning": "居高臨下隨時看顧視察整個運作過程 ➔「監督、指導」"
        },
        "sentence": "The chief civil engineer will directly supervise the installation of structural cables along the suspension bridge.",
        "sentenceZh": "總土木工程師將親自直接監督沿著懸索橋安裝結構鋼纜的作業。",
        "grammar": {
          "pattern": "S + Modal + Adv + Vt (supervise) + O (installation) + Prep Phrase",
          "breakdown": [
            {
              "part": "The chief civil engineer",
              "role": "主詞 (Subject)",
              "note": "civil engineer (土木工程師)。"
            },
            {
              "part": "will directly supervise",
              "role": "動詞片語 (Verb)",
              "note": "directly 作情狀副詞。"
            },
            {
              "part": "the installation of structural cables",
              "role": "直接受詞 (Direct Object)",
              "note": "installation (安裝作業)。"
            },
            {
              "part": "along the suspension bridge",
              "role": "空間介系詞片語",
              "note": "suspension bridge (懸索橋)。"
            }
          ],
          "keyPoints": [
            "【名詞衍生】：supervisor (主管、指導教授)、supervision (監督)。",
            "【字首疊加】：super- (在上方) + vis (看)，字面即「在上位者看顧」。"
          ]
        }
      },
      {
        "word": "supernatural",
        "kk": "[ˌsupɚˈnætʃərəl]",
        "ipa": "/ˌsuːpərˈnætʃrəl/",
        "pos": "adj. / n.",
        "meaning": "超自然的、神異的；(n.) 超自然力量",
        "formula": {
          "parts": [
            {
              "text": "super-",
              "role": "prefix",
              "meaning": "超越、在...之上 (above, beyond)"
            },
            {
              "text": "natural",
              "role": "base",
              "meaning": "大自然的、物理法則的 (nature)"
            }
          ],
          "resultMeaning": "超越常態自然界已知科學與物理法則的 ➔「超自然的」"
        },
        "sentence": "Ancient civilizations often attributed unexplainable celestial eclipses to supernatural intervention by angered deities.",
        "sentenceZh": "古代文明常常將無法解釋的天體日食月食歸咎於被激怒神明的超自然介入。",
        "grammar": {
          "pattern": "S + Adv + Vt (attributed A to B) + Prep Phrase (by...)",
          "breakdown": [
            {
              "part": "Ancient civilizations",
              "role": "主詞 (Subject)",
              "note": "複數名詞。"
            },
            {
              "part": "often attributed",
              "role": "動詞片語 (Verb)",
              "note": "attribute A to B 句型。"
            },
            {
              "part": "unexplainable celestial eclipses",
              "role": "直接受詞 A",
              "note": "eclipses (日蝕、月蝕)。"
            },
            {
              "part": "to supernatural intervention",
              "role": "歸因對象 B",
              "note": "supernatural 作形容詞修飾 intervention (介入)。"
            },
            {
              "part": "by angered deities",
              "role": "施事介系詞片語",
              "note": "angered 作形容詞「被觸怒的」；deities (神明)。"
            }
          ],
          "keyPoints": [
            "【重要句型】：attribute A to B = 把 A 歸因於 B，to 為介系詞。",
            "【近義詞比對】：supernatural (超自然的神鬼奇幻) vs. paranormal (超常超心理學現象)。"
          ]
        }
      },
      {
        "word": "surface",
        "kk": "[ˈsɝfɪs]",
        "ipa": "/ˈsɜːrfɪs/",
        "pos": "n. / v. / adj.",
        "meaning": "表面、外表；(v.) 浮出水面、顯露；(adj.) 表面的",
        "formula": {
          "parts": [
            {
              "text": "sur- (super-)",
              "role": "prefix",
              "meaning": "在上面 (above, over)"
            },
            {
              "text": "face",
              "role": "base",
              "meaning": "臉面、外觀 (face)"
            }
          ],
          "resultMeaning": "位於最外層朝上的臉面 ➔「表面、外表；浮出水面」"
        },
        "sentence": "The submarine surfaced quietly under the cover of night after completing its reconnaissance patrol.",
        "sentenceZh": "潛水艇在完成偵察巡邏任務後，在夜色的掩護下悄無聲息地浮出了水面。",
        "grammar": {
          "pattern": "S + Vi (surfaced) + Adv + Prep Phrase (under the cover of night) + Prep Phrase of Time",
          "breakdown": [
            {
              "part": "The submarine",
              "role": "主詞 (Subject)",
              "note": "單數名詞「潛水艇」。"
            },
            {
              "part": "surfaced",
              "role": "不及物動詞 (Verb)",
              "note": "過去簡單式「浮上水面」。"
            },
            {
              "part": "quietly",
              "role": "情狀副詞",
              "note": "修飾 surfaced。"
            },
            {
              "part": "under the cover of night",
              "role": "情境介系詞片語",
              "note": "under the cover of (在...掩護下)。"
            },
            {
              "part": "after completing its reconnaissance patrol",
              "role": "時間介系詞片語",
              "note": "reconnaissance (偵察)；patrol (巡邏)。"
            }
          ],
          "keyPoints": [
            "【成語片語】：scratch the surface (僅觸及皮毛、蜻蜓點水)。",
            "【動詞用法】：surface 作動詞除「浮出水面」外，亦常指「(問題、爭議、真相) 浮出檯面、暴露出來」。"
          ]
        }
      }
    ],
    "article": {
      "title": "Above and Beyond: The Ascendance of Super and Sur",
      "titleZh": "凌越巔峰：超越與盈餘之光",
      "intro": "人類的精神永遠渴望「超越 (super-)」平庸的引力，追求卓越 (superior) 的品質並將富足盈餘 (surplus) 散播給世界。",
      "paragraphs": [
        {
          "en": "True excellence is not born from effortless fortune; it is achieved when dedicated scholars and engineers push beyond the baseline to craft superior solutions that elevate collective life.",
          "zh": "真正的卓越並非源自不勞而獲的僥倖，而是在專注的學者與工程師跨越基準線、打造出能提升大眾集體生活的卓越解方之時方能成就。"
        },
        {
          "en": "When prosperous societies accumulate a moral surplus of compassion and wealth, they share it generously with suffering neighbors, proving that climbing higher is meaningful only when we lift others with us.",
          "zh": "當繁榮的社會積累了富足的同情心與財富盈餘時，他們慷慨地與受難的鄰舍分享，證明了向上攀登唯有在攜手托舉他人共同前行時才具有真正的意義。"
        }
      ],
      "comprehensionQuestions": [
        {
          "q": "What should prosperous societies do with their moral surplus according to the text?",
          "qZh": "根據文章，繁榮社會應當如何運用其道德盈餘？",
          "options": [
            "A. Share it generously with suffering neighbors. (慷慨地與受難鄰舍分享)",
            "B. Lock it away in secret subterranean vaults.",
            "C. Build tall walls to keep everyone out.",
            "D. Burn it in public bonfires."
          ],
          "answer": 0,
          "explanation": "文中第二段指出繁榮社會應「share it generously with suffering neighbors」。"
        }
      ]
    }
  }
];

// 支援瀏覽器與 Node.js 雙環境
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ETYMO_DATA };
}
