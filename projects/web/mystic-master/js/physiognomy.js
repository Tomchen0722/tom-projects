// ==========================================================================
// 相術乾坤殿：正統手相（Palmistry）與面相（Physiognomy）專業大師系統
// 融合古典相法（麻衣、柳莊、神相鐵關刀）與現代認知神經學、微表情行為學
// ==========================================================================

const PhysiognomySystem = {
    // 手相篇：三大主線、三大副線與八大掌丘
    palmistry: {
        lines: [
            {
                id: "life",
                name: "生命線（Life Line）",
                color: "#10b981",
                origin: "虎口（食指與大拇指之間）弧形環繞金星丘延伸至手腕",
                classical: "主精力強弱、生命體魄本質、抗病免疫力與元氣底蘊。非單純預測壽數長短，而是表徵生命活力之充沛度與抗挫折生理承載力。",
                proSignificance: "生理能量儲備與心理韌性基石。弧度深長圓潤且包覆廣大金星丘者，代表體魄雄健、精力充沛，具備應對長週期商戰與高壓決策的超凡續航力；若起端鎖鏈或斷續，提示早年需注重規律作息與心血管調養，防範過勞透支。",
                patterns: [
                    { type: "深長圓潤且無雜紋", desc: "先天元氣充盈，生理與心理抗壓韌性頂尖，具備長線搏擊商海、承擔重大責任之體魄。" },
                    { type: "起端成鎖鏈狀交錯", desc: "早年體質較為敏感，需注重自律神經與腸胃調攝，成年後生活規律即可固本培元。" },
                    { type: "末端分叉奔向月丘", desc: "古典稱之為「驛馬遠行紋」。適應全新環境與跨國開拓能力極強，宜出外闖蕩立業，遠方發展成就斐然。" }
                ]
            },
            {
                id: "head",
                name: "智慧線 / 頭腦線（Head Line）",
                color: "#3b82f6",
                origin: "與生命線同源或微起其上，橫貫手掌中央平原延伸",
                classical: "主思維邏輯、決策定力、智力結構與專業偏向。是辨析一個人認知模式、風控直覺與戰略視野的核心指標。",
                proSignificance: "核心大腦神經認知模型與戰略演算法。筆直貫穿掌心者，代表極致的理性客觀、數據因果思維與雷厲風行的商業決斷力；末端平緩下垂至月丘者，代表兼具邏輯演算與宏觀戰略洞察的全面型舵手；雙重智慧線者更是文韜武略、多線程併行運作的商業奇才。",
                patterns: [
                    { type: "筆直橫跨掌面（理性實幹型）", desc: "冷靜沈著、重視客觀事實與量化數據，在金融投資、軟體架構、企業治理與司法決策中極具建樹。" },
                    { type: "平緩下垂至月丘（文理通才型）", desc: "兼具剛性邏輯與敏銳人文共情，善於在錯綜複雜的局勢中跨界整合，是頂級戰略智囊與高階領袖之相。" },
                    { type: "末端分叉呈燕尾狀（決策博弈型）", desc: "具備多維博弈思維，能同時看穿事情正反兩面，長於商務談判、國際公關與突發危機斡旋。" }
                ]
            },
            {
                id: "heart",
                name: "感情線（Heart Line）",
                color: "#ec4899",
                origin: "從小指下方外緣啟程，橫向朝食指或中指基底延伸",
                classical: "主情感感知、同理心深度、人際界限感、忠誠度與心理防線。",
                proSignificance: "情商共振中樞與組織心理界限。線條深秀平直延伸至食指基底者，為人重情重義、崇尚崇高信義與社會使命；止於中指下方者，處事冷靜克制、不易被情感裹挾；支線豐潤者，具備強烈的親和力與號召力，善於凝聚忠誠團隊。",
                patterns: [
                    { type: "延伸至食指與中指之間（平衡中庸）", desc: "情商極高，處事溫潤有禮且堅守原則底線，善於平衡家庭責任與團隊利益，人際關係極為長青。" },
                    { type: "直達食指根部木星丘（崇高抱負）", desc: "胸懷大志，追求純粹真誠之合作契約，具備高度道德責任感，對欺騙背叛零容忍。" },
                    { type: "末端向上生出羽狀細紋（樂觀開朗）", desc: "自帶強大社交魅力與親和感染力，能迅速融洽人際氣氛，在公眾演說與團隊激勵中深得人心。" }
                ]
            },
            {
                id: "fate",
                name: "事業線 / 玉柱命運線（Fate Line）",
                color: "#f59e0b",
                origin: "由掌底手腕上方垂直向上，朝中指土星丘攀升",
                classical: "主自我志向清晰度、自驅力強弱、社會責任感與主線目標之執行推進。",
                proSignificance: "自律執行引擎與終身成就軌跡。線條筆直深秀貫穿掌心者，代表強烈的使命感與終生奮鬥志向，不需外力督促即能堅定不移推進行業大局；若掌中線條由淺入深，代表先歷磨礪而後建立豐碑的大器晚成之局。",
                patterns: [
                    { type: "筆直深秀直上中指土星丘", desc: "目標極度清晰堅定，自律自持，步步為營，是建立實體基業與長青產業的典型棟樑之相。" },
                    { type: "由月丘斜向升起（貴人相助）", desc: "大眾緣與跨界助力強勁，事業騰飛多得行業長輩引路與大眾信任，利於公眾事業與合夥運營。" },
                    { type: "多段重疊或波折推進", desc: "代表多階段的戰略轉軌與跨界再造，每一次人生轉型皆能沉澱更宏闊的格局與洞見。" }
                ]
            },
            {
                id: "sun",
                name: "太陽線 / 成功名譽線（Sun Line）",
                color: "#eab308",
                origin: "無名指下方垂直下行的秀麗紋路",
                classical: "主才華展現、公眾認可、行業威望、藝術品味與名譽光環。",
                proSignificance: "個人品牌聲望與資本認可光環。具備清晰太陽線者，代表其專業才能極易受到行業推崇與廣泛認可，自帶不可替代的個人無形資產與信任背書。",
                patterns: [
                    { type: "深秀直貫無名指基底", desc: "行業聲望昭彰，自帶權威公信力，容易在所屬領域脫穎而出並享受崇高社會地位。" },
                    { type: "雙線平行升起（雙星拱照）", desc: "多才多藝，兼具扎實硬實力與高超公眾影響力，在主業豐碩的同時亦開闢顯赫第二曲線。" }
                ]
            }
        ],

        // 八大掌丘能量分佈
        mounts: [
            { id: "jupiter", name: "木星丘", pos: "食指基底", element: "木", icon: "🌱", meaning: "統率野心・威望抱負・領袖志向", proGuide: "豐盈飽滿者具備開闢新局的政治與商業抱負，善於登高一呼、引領組織破局；平坦者性情謙和內斂，適合專精於高階專業顧問或技術深耕。" },
            { id: "saturn", name: "土星丘", pos: "中指基底", element: "土", icon: "⛰️", meaning: "審慎深思・自律堅守・孤獨耐受", proGuide: "主掌坐冷板凳的深度研究定力與長線風控。飽滿端正者耐得住寂寞、恪守紀律，是科研泰斗、哲學家與深度資本操盤手的必備底蘊。" },
            { id: "apollo", name: "太陽丘", pos: "無名指基底", element: "火", icon: "☀️", meaning: "聲望名譽・藝術審美・光明坦蕩", proGuide: "品牌光環與商業魅力的發源地！充盈隆起者審美品味卓絕、為人坦蕩自信，具備化平庸為神奇的品牌賦能天賦。" },
            { id: "mercury", name: "水星丘", pos: "小指基底", element: "水", icon: "💧", meaning: "商業機敏・財帛運籌・辯才斡旋", proGuide: "掌管商業嗅覺與合約談判。飽滿紅潤者思維敏捷、言辭精煉具穿透力，在商海博弈與資本運作中如魚得水。" },
            { id: "venus", name: "金星丘", pos: "大拇指大魚際", element: "金", icon: "❤️", meaning: "生命元氣・熱忱博愛・體魄根基", proGuide: "生命力的大水庫！肌肉厚實有彈性且色澤潤亮者，睡眠機能極佳、體能澎湃，處事溫暖誠摯，具備承受極限壓力的生理資本。" },
            { id: "luna", name: "月丘", pos: "掌外側手腕上方小魚際", element: "水", icon: "🌙", meaning: "直覺靈感・全球視野・戰略想像", proGuide: "頂層創新與遠行探索的發源地！飽滿豐碩者具備跨國經營的宏觀眼界與突破性直覺，在藝術哲學、全球市場或顛覆性賽道具非凡洞察。" },
            { id: "mars1", name: "第一火星丘", pos: "虎口內部近掌心處", element: "火", icon: "⚔️", meaning: "進取魄力・主動攻堅・敢於亮劍", proGuide: "代表臨危不亂的決策殺氣與主動開闢市場的進取魄力。充實者敢於承擔重大決策風險，是市場拓荒主帥。" },
            { id: "mars2", name: "第二火星丘", pos: "小指下方感情線與智慧線之間", element: "火", icon: "🛡️", meaning: "防禦堅守・堅毅忍耐・心性定力", proGuide: "代表咬緊牙關穿越週期的防禦韌性。充實者在市場大逆境或危機衝擊下能臨危不亂、從容守護核心盤，轉危為安。" }
        ],

        // 五行掌型專業辨識
        handTypes: [
            { type: "金形掌（方正乾健）", traits: "掌方指方、肉實骨堅、掌色白潤有光", modernRole: "企業執行長 / 金融精算巨擘 / 司法檢察官", proProfile: "行事法度森嚴、邏輯因果嚴密、一諾千金。注重制度化管理與標準作業程序（SOP），以實戰數據與鐵血紀律引領組織。" },
            { type: "木形掌（修長雅致）", traits: "掌長指長、指節微隆、掌紋深細秀麗", modernRole: "戰略思想家 / 前沿科學家 / 品牌文化架構師", proProfile: "求知深邃、思辨深刻，長於洞悉事物本質。具有強烈的學者氣象與文化情操，宜引領研發智庫或高階理念創新。" },
            { type: "水形掌（圓潤靈動）", traits: "掌肉豐厚柔軟、指根粗指尖細圓潤滑", modernRole: "資深外交家 / 資本並購撮合人 / 公關領袖", proProfile: "如水隨形，適應力登峰造極，情商智商深不可測。長於在多方錯綜複雜的利益格局中調和鼎鼐，化干戈為玉帛。" },
            { type: "火形掌（銳利熱烈）", traits: "掌長指短、指尖尖圓、掌面溫潤帶紅", modernRole: "創新開拓者 / 演說演繹家 / 商業先鋒主帥", proProfile: "行動迅疾如風、熱忱澎湃，具備強大的公眾感染力與破局爆發力。長於在短兵相接中奪取關鍵戰略窗口。" },
            { type: "土形掌（厚重沉穩）", traits: "手掌厚重寬闊、肌理沉實、握力敦厚沉穩", modernRole: "實業興邦家 / 重資產運營總裁 / 長青家族掌舵", proProfile: "腳踏實地、深謀遠慮，從不投機冒進。雖不以奇巧見長，然其抗風險底盤與後勁極深，是成就百年基業的長青之相。" }
        ]
    },

    // 面相篇：三停六府與五官十二宮
    physiognomy: {
        threeZones: [
            {
                name: "上停（天庭：髮際至印堂眉毛）",
                age: "15 歲 ～ 30 歲（青年運・早年機遇與智慧）",
                concept: "前額葉發育、大腦認知邏輯、原生底蘊與早年聲望考運",
                proGuide: "《麻衣相法》云：「天庭飽滿，地閣方圓。」額頭開闊明潤、無深痕惡疤者，代表大腦前額葉認知發育超卓，長於系統性邏輯思辨與戰略推演。印堂（兩眉之間命宮）開闊平滿容兩指、氣色光澤瑩潤者，代表心智舒展、事業機遇暢通無阻。",
                tuningTip: "注重深層睡眠！熬夜損耗腎精，易致天庭暗沉泛青；早晨以溫熱毛巾敷額、梳理頭皮經絡，能改善前額血流，迅速凝神聚氣。"
            },
            {
                name: "中停（眉毛至鼻頭準頭）",
                age: "31 歲 ～ 50 歲（壯年運・事業奮鬥與財帛主位）",
                concept: "意志立柱、自尊魄力、中運奮鬥與資本累積實質成敗",
                proGuide: "由眉（保壽）、眼（監察）、鼻（審辨）、顴（權柄）構成。鼻樑挺拔如懸膽、顴骨微聳有豐肉包覆者，抗挫折與自主創業成事之野心極強。在商戰與職場中代表面臨重壓時咬緊牙關、力挽狂瀾的大將風骨。",
                tuningTip: "端正脊椎體態！長期含胸駝背壓迫頸動脈血供，使中停氣色萎靡。挺胸拔背、目光凝視平遠，自能凝斂昂揚意志與權力氣度。"
            },
            {
                name: "下停（人中、嘴唇至下巴地閣）",
                age: "51 歲以後（晚年運・基業守成與晚景承載）",
                concept: "耐力底蘊、團隊忠誠、組織承載力與終身成果封存",
                proGuide: "下巴（地閣）方圓敦厚、雙唇方正有稜角者，處事有始有終，善於蓄積資本與培植組織梯隊。代表年輕時雖經波折，往後人生必有福厚延綿之大器晚成格局。",
                tuningTip: "日常放鬆咬肌！避免習慣性緊咬牙根或抿嘴角冷笑，保持平靜祥和之面部微表情，使下庭骨肉舒展，凝聚晚成之厚德福氣。"
            }
        ],

        fiveOfficials: [
            {
                name: "耳（採聽官）",
                element: "水",
                icon: "👂",
                meaning: "先天腎氣・聞過則喜・策略傾聽",
                features: "耳輪分明、耳垂厚實如珠、耳高齊眉者，腎氣充沛、善於博採眾長、聽取逆耳忠言；耳廓翻飛反骨者，性情執拗，需防任性孤行。"
            },
            {
                name: "眉（保壽官）",
                element: "木",
                icon: "✨",
                meaning: "同僚人緣・情緒自律・風度修養",
                features: "眉長過目、根根順生如新月者，性格溫潤中正、情緒管理登峰造極，一生盟友知己眾多；眉毛雜亂逆生或鎖印相連者，性躁心急，需修持沉靜心性。"
            },
            {
                name: "眼（監察官）",
                element: "火",
                icon: "👁️",
                meaning: "神定氣靜・洞察機先・善惡決斷（面相之靈魂）",
                features: "相法一千處，不如看眼神一眼！雙眸黑白分明、瞳仁清澈含光、久視不脫者，心神凝定、洞悉世事，決策精準如神；眼神遊移閃爍者，心神散亂，難以委以重任。"
            },
            {
                name: "鼻（審辨官）",
                element: "土",
                icon: "👃",
                meaning: "自尊自信・人格支柱・財帛宮位",
                features: "山根挺拔貫頂、準頭圓潤有肉、鼻翼豐厚收斂者，自我意志如中流砥柱，善於資本運作且開支有度；鼻孔仰露孔薄者，花銷隨性，宜建立硬性資產定投機制。"
            },
            {
                name: "口（出納官）",
                element: "水",
                icon: "👄",
                meaning: "言語法令・契約誠信・福澤享用",
                features: "上下唇厚薄均勻、輪廓明晰如仰月、口角微揚者，言出必踐、幽默有道、深具公信力與領導魅力；雙唇尖薄傾斜者，易引發言語是非與合約紛爭。"
            }
        ],

        // 相由心生與現代神經行為學對照
        mindsetPrinciples: [
            {
                ancient: "有心無相，相逐心生；有相無心，相隨心滅。",
                modernScience: "神經可塑性（Neuroplasticity）與微表情神經回饋機制：長期的焦慮恐懼與敵意會導致面部表情肌群慢性痙攣，使印堂緊鎖、顴肌僵硬、眼神枯竭；而持之以恆的正念定力、宏觀胸襟與健康生活，能直接改善大腦前額葉血供與自律神經平衡，使面部氣色潤澤、神光內斂。",
                actionGuide: "每日清晨淨面之際，正視鏡中神態，深呼吸調勻氣息，舒展雙眉以寬印堂，挺拔脊背——此乃透過神經反饋調節迷走神經張力的頂級身心校準儀式！"
            }
        ]
    },

    // ======================================================================
    // 智能掌紋影像分析與吉凶精論引擎（PalmAnalyzer）
    // ======================================================================
    palmAnalyzer: {
        // 預設三大經典掌相範本
        presets: {
            leader: {
                id: "leader",
                title: "乾元亨通・帝王實業型掌相",
                handType: "金形掌（方正乾健）",
                score: 96,
                auspiciousTier: "上上吉・乾健鼎盛富貴格",
                bgTone: "#f5ece3",
                accentColor: "#b4532a",
                features: {
                    career: "自掌底坎宮深秀挺拔直貫土星丘，穿越智慧線與感情線無雜紋阻滯，35歲前奠基雄厚，35~50歲勢如破竹，晚年基業長青，為典型建立長青產業之主帥相。",
                    life: "弧形深圓開闊，牢牢包覆豐滿之金星丘，生命元氣充盈澎湃，睡眠機能與抗壓韌性卓越，能從容應對長週期商海博弈與重大決策高壓。",
                    head: "筆直端正橫貫掌面平原，邏輯因果嚴密、風控直覺敏銳，崇尚制度化治理與量化事實，絕不投機冒進。",
                    heart: "平直直上食指根部木星丘，胸懷萬里抱負，處事重誠守信，深具社會責任感與組織統御號召力。",
                    sun: "無名指太陽丘下端正秀麗，行業公信力昭彰，自帶貴人信賴光環與無形品牌資產。"
                },
                mountsFocus: "木星丘與金星丘尤為隆起充實，代表權威抱負與充沛元氣高度結合。"
            },
            pioneer: {
                id: "pioneer",
                title: "破局先鋒・文韜武略型掌相",
                handType: "木火交輝（修長敏銳）",
                score: 93,
                auspiciousTier: "大吉・日麗中天破局格",
                bgTone: "#f7efe8",
                accentColor: "#5b7052",
                features: {
                    career: "自太陰丘（月丘）斜向長驅升起，大眾人緣極佳，得行業長輩指引與跨界貴人鼎力相助，30歲後迎來第一波重大爆發窗口，善於在變革中乘風破浪。",
                    life: "起端成秀美圓弧，末端奔向月丘呈『驛馬遠行紋』，適應新環境與國際開拓能力非凡，利於跨國開疆闢土或遠方立業。",
                    head: "平緩下垂至月丘，末端分叉呈『燕尾博弈紋』，兼具剛性邏輯演算與宏觀戰略直覺，長於商業談判、多方斡旋與創新賽道破局。",
                    heart: "端點延伸至食指與中指之間，情商極高，進退有度，善於平衡組織激勵與制度防線，人脈網絡極為長青。",
                    sun: "雙秀並行，主業豐厚同時開闢顯赫第二增長曲線，在跨領域中皆能享有崇高行業美譽。"
                },
                mountsFocus: "月丘與第一火星丘充盈，代表全球戰略視野與臨危不亂的進取殺氣。"
            },
            strategist: {
                id: "strategist",
                title: "深謀遠慮・富貴大儒型掌相",
                handType: "水木相涵（圓潤深邃）",
                score: 95,
                auspiciousTier: "極秀・明珠出海謀略格",
                bgTone: "#f3ede4",
                accentColor: "#c88a35",
                features: {
                    career: "早期線條含蓄內斂，過智慧線（35歲）後驟顯深秀挺拔，為典型『大器晚成、積健為雄』之局。歷練越深則氣場越宏闊，厚積薄發不可限量。",
                    life: "弧線寬廣溫潤，金星丘肉厚富有彈性，具備極強的心理抗挫折承載力與長期主義定力，耐受長期高強度研發或資本佈局。",
                    head: "深長微曲直入太陰丘深處，思維深邃莫測，善於洞察事物底層邏輯與歷史週期，為頂級智庫、哲學家與深度資本操盤手之標配。",
                    heart: "柔和向上環抱中指與食指，大音希聲、大象無形，善於聚攏各方奇才並調和鼎鼐，化干戈為玉帛。",
                    sun: "深聚太陽丘，信用價值極高，享有頂層資本與學術權威的終身信任背書。"
                },
                mountsFocus: "土星丘與水星丘特別端正，代表孤獨研究的定力與高超商業財帛調度能力。"
            }
        },

        // 電腦視覺手掌輪廓與暗紋掃描萃取器（Computer Vision Crease & Landmark Detector）
        detectPalmFeaturesFromImage: function(ctx, w, h, preferredHandSide) {
            const imgData = ctx.getImageData(0, 0, w, h);
            const data = imgData.data;

            // 1. 膚色空間判定（有效分離各類背景、坐墊與冷白日光環境）
            const skinMask = new Uint8Array(w * h);
            const gray = new Float32Array(w * h);
            let skinCount = 0;

            for (let y = 0; y < h; y++) {
                for (let x = 0; x < w; x++) {
                    const idx = (y * w + x) * 4;
                    const r = data[idx];
                    const g = data[idx + 1];
                    const b = data[idx + 2];
                    gray[y * w + x] = 0.299 * r + 0.587 * g + 0.114 * b;

                    // 膚色判定：手掌特徵為紅光顯著高於綠光，過濾綠黃坐墊
                    const isSkin = ((r - g) >= 8) && (r > 60) && (b > 35);
                    if (isSkin) {
                        skinMask[y * w + x] = 1;
                        skinCount++;
                    }
                }
            }

            // 2. 判定左手或右手 (Left Hand vs Right Hand Orientation)
            // 比較上方兩側角落膚色比例：左手上方左側為虎口外緣空隙（低膚色），右上側為小指與掌緣（高膚色）
            const cornerW = Math.max(10, Math.round(w * 0.25));
            const cornerH = Math.max(10, Math.round(h * 0.25));
            let tlSkin = 0, trSkin = 0;
            for (let y = 0; y < cornerH; y++) {
                for (let x = 0; x < cornerW; x++) {
                    if (skinMask[y * w + x]) tlSkin++;
                    if (skinMask[y * w + (w - 1 - x)]) trSkin++;
                }
            }

            let isLeftHand = tlSkin <= trSkin;
            if (preferredHandSide === "left") isLeftHand = true;
            if (preferredHandSide === "right") isLeftHand = false;

            // 3. 局部暗線微紋掃描取樣函式 (Local Dark Crease Valley Scanner)
            const R = Math.max(3, Math.round(w / 55));
            const findDarkestPointInBox = (x1, y1, x2, y2, defaultX, defaultY) => {
                let bestX = defaultX;
                let bestY = defaultY;
                let maxScore = -999;
                const step = 2;
                const startX = Math.max(R + 1, Math.round(x1));
                const endX = Math.min(w - R - 2, Math.round(x2));
                const startY = Math.max(R + 1, Math.round(y1));
                const endY = Math.min(h - R - 2, Math.round(y2));

                for (let y = startY; y <= endY; y += step) {
                    for (let x = startX; x <= endX; x += step) {
                        const centerVal = gray[y * w + x];
                        const avgNeighbor = (
                            gray[(y - R) * w + x] + gray[(y + R) * w + x] +
                            gray[y * w + (x - R)] + gray[y * w + (x + R)]
                        ) / 4;
                        const score = avgNeighbor - centerVal; // 越暗 score 越正
                        if (score > maxScore && score > 2.0) {
                            maxScore = score;
                            bestX = x;
                            bestY = y;
                        }
                    }
                }
                return { x: Math.round(bestX), y: Math.round(bestY), score: maxScore };
            };

            // 4. 根據解剖學掌骨比例與暗紋掃描定位主副線
            let lines = {};
            let mounts = [];

            if (isLeftHand) {
                // ===== 左手配置（大拇指在左側，小指在右側） =====
                // 1. 感情線（天紋）：從小指下方外緣（右上側）橫向左延伸，微拱向食指與中指下方
                const heartStart = findDarkestPointInBox(
                    w * 0.78, h * 0.22, w * 0.94, h * 0.35,
                    Math.round(w * 0.88), Math.round(h * 0.29)
                );
                const heartCp1 = findDarkestPointInBox(
                    w * 0.58, h * 0.22, w * 0.74, h * 0.34,
                    Math.round(w * 0.66), Math.round(h * 0.28)
                );
                const heartEnd = findDarkestPointInBox(
                    w * 0.40, h * 0.14, w * 0.54, h * 0.26,
                    Math.round(w * 0.47), Math.round(h * 0.20)
                );

                // 2. 智慧線（人紋）：從虎口（左側食指與拇指間）橫貫掌心向右下平緩微降
                const headStart = findDarkestPointInBox(
                    w * 0.28, h * 0.34, w * 0.40, h * 0.44,
                    Math.round(w * 0.34), Math.round(h * 0.39)
                );
                const headCp1 = findDarkestPointInBox(
                    w * 0.46, h * 0.40, w * 0.60, h * 0.52,
                    Math.round(w * 0.53), Math.round(h * 0.46)
                );
                const headEnd = findDarkestPointInBox(
                    w * 0.65, h * 0.45, w * 0.82, h * 0.58,
                    Math.round(w * 0.74), Math.round(h * 0.51)
                );

                // 3. 生命線（地紋）：與智慧線同源於虎口，弧形向下環繞金星丘（拇指大魚際）
                const lifeStart = { x: headStart.x, y: headStart.y };
                const lifeCp1 = findDarkestPointInBox(
                    w * 0.36, h * 0.50, w * 0.48, h * 0.64,
                    Math.round(w * 0.42), Math.round(h * 0.57)
                );
                const lifeCp2 = findDarkestPointInBox(
                    w * 0.32, h * 0.68, w * 0.44, h * 0.82,
                    Math.round(w * 0.38), Math.round(h * 0.75)
                );
                const lifeEnd = findDarkestPointInBox(
                    w * 0.24, h * 0.78, w * 0.36, h * 0.90,
                    Math.round(w * 0.30), Math.round(h * 0.84)
                );

                // 4. 事業線（玉柱命運線）：由手腕掌底中央垂直升向中指下方土星丘
                const fateStart = findDarkestPointInBox(
                    w * 0.46, h * 0.74, w * 0.58, h * 0.88,
                    Math.round(w * 0.52), Math.round(h * 0.80)
                );
                const fateCp1 = findDarkestPointInBox(
                    w * 0.48, h * 0.40, w * 0.58, h * 0.52,
                    Math.round(w * 0.53), Math.round(h * 0.46)
                );
                const fateEnd = findDarkestPointInBox(
                    w * 0.46, h * 0.16, w * 0.56, h * 0.28,
                    Math.round(w * 0.51), Math.round(h * 0.22)
                );

                // 5. 太陽線（六秀線）：無名指下方垂直下行
                const sunStart = { x: Math.round(w * 0.65), y: Math.round(h * 0.45) };
                const sunEnd = { x: Math.round(w * 0.65), y: Math.round(h * 0.22) };

                lines = {
                    life: { start: lifeStart, cp1: lifeCp1, cp2: lifeCp2, end: lifeEnd },
                    head: { start: headStart, cp1: headCp1, end: headEnd },
                    heart: { start: heartStart, cp1: heartCp1, end: heartEnd },
                    fate: { start: fateStart, cp1: fateCp1, end: fateEnd },
                    sun: { start: sunStart, end: sunEnd }
                };

                // 八大掌丘座標（左手）
                mounts = [
                    { id: "jupiter", name: "木星丘", x: Math.round(w * 0.36), y: Math.round(h * 0.21), r: Math.round(w * 0.08), element: "木", icon: "🌱", role: "統率雄心・權柄抱負", score: 95 },
                    { id: "saturn", name: "土星丘", x: Math.round(w * 0.51), y: Math.round(h * 0.19), r: Math.round(w * 0.08), element: "土", icon: "⛰️", role: "深謀沉潛・風控紀律", score: 92 },
                    { id: "apollo", name: "太陽丘", x: Math.round(w * 0.66), y: Math.round(h * 0.21), r: Math.round(w * 0.08), element: "火", icon: "☀️", role: "行業名望・無形資產", score: 94 },
                    { id: "mercury", name: "水星丘", x: Math.round(w * 0.81), y: Math.round(h * 0.25), r: Math.round(w * 0.07), element: "水", icon: "💧", role: "財帛商機・合約談判", score: 91 },
                    { id: "venus", name: "金星丘", x: Math.round(w * 0.26), y: Math.round(h * 0.58), r: Math.round(w * 0.14), element: "金", icon: "❤️", role: "元氣底蘊・生理抗壓", score: 96 },
                    { id: "luna", name: "月丘", x: Math.round(w * 0.75), y: Math.round(h * 0.66), r: Math.round(w * 0.13), element: "水", icon: "🌙", role: "全球視野・戰略直覺", score: 93 },
                    { id: "mars1", name: "第一火星丘", x: Math.round(w * 0.34), y: Math.round(h * 0.38), r: Math.round(w * 0.07), element: "火", icon: "⚔️", role: "進取魄力・開闢主帥", score: 90 },
                    { id: "mars2", name: "第二火星丘", x: Math.round(w * 0.78), y: Math.round(h * 0.42), r: Math.round(w * 0.07), element: "火", icon: "🛡️", role: "危機防禦・抗壓堅守", score: 92 }
                ];
            } else {
                // ===== 右手配置（大拇指在右側，小指在左側） =====
                // 1. 感情線（天紋）：從小指下方外緣（左上側）橫向右延伸
                const heartStart = findDarkestPointInBox(
                    w * 0.06, h * 0.22, w * 0.22, h * 0.35,
                    Math.round(w * 0.12), Math.round(h * 0.29)
                );
                const heartCp1 = findDarkestPointInBox(
                    w * 0.26, h * 0.22, w * 0.42, h * 0.34,
                    Math.round(w * 0.34), Math.round(h * 0.28)
                );
                const heartEnd = findDarkestPointInBox(
                    w * 0.46, h * 0.14, w * 0.60, h * 0.26,
                    Math.round(w * 0.53), Math.round(h * 0.20)
                );

                // 2. 智慧線（人紋）：從右側虎口橫貫掌心向左下微垂
                const headStart = findDarkestPointInBox(
                    w * 0.60, h * 0.34, w * 0.72, h * 0.44,
                    Math.round(w * 0.66), Math.round(h * 0.39)
                );
                const headCp1 = findDarkestPointInBox(
                    w * 0.40, h * 0.40, w * 0.54, h * 0.52,
                    Math.round(w * 0.47), Math.round(h * 0.46)
                );
                const headEnd = findDarkestPointInBox(
                    w * 0.18, h * 0.45, w * 0.35, h * 0.58,
                    Math.round(w * 0.26), Math.round(h * 0.51)
                );

                // 3. 生命線（地紋）：右側虎口向下環繞金星丘
                const lifeStart = { x: headStart.x, y: headStart.y };
                const lifeCp1 = findDarkestPointInBox(
                    w * 0.52, h * 0.50, w * 0.64, h * 0.64,
                    Math.round(w * 0.58), Math.round(h * 0.57)
                );
                const lifeCp2 = findDarkestPointInBox(
                    w * 0.56, h * 0.68, w * 0.68, h * 0.82,
                    Math.round(w * 0.62), Math.round(h * 0.75)
                );
                const lifeEnd = findDarkestPointInBox(
                    w * 0.64, h * 0.78, w * 0.76, h * 0.90,
                    Math.round(w * 0.70), Math.round(h * 0.84)
                );

                // 4. 事業線：由手腕掌底中央升向中指下方
                const fateStart = findDarkestPointInBox(
                    w * 0.42, h * 0.74, w * 0.54, h * 0.88,
                    Math.round(w * 0.48), Math.round(h * 0.80)
                );
                const fateCp1 = findDarkestPointInBox(
                    w * 0.42, h * 0.40, w * 0.52, h * 0.52,
                    Math.round(w * 0.47), Math.round(h * 0.46)
                );
                const fateEnd = findDarkestPointInBox(
                    w * 0.44, h * 0.16, w * 0.54, h * 0.28,
                    Math.round(w * 0.49), Math.round(h * 0.22)
                );

                // 5. 太陽線
                const sunStart = { x: Math.round(w * 0.35), y: Math.round(h * 0.45) };
                const sunEnd = { x: Math.round(w * 0.35), y: Math.round(h * 0.22) };

                lines = {
                    life: { start: lifeStart, cp1: lifeCp1, cp2: lifeCp2, end: lifeEnd },
                    head: { start: headStart, cp1: headCp1, end: headEnd },
                    heart: { start: heartStart, cp1: heartCp1, end: heartEnd },
                    fate: { start: fateStart, cp1: fateCp1, end: fateEnd },
                    sun: { start: sunStart, end: sunEnd }
                };

                // 八大掌丘座標（右手）
                mounts = [
                    { id: "jupiter", name: "木星丘", x: Math.round(w * 0.64), y: Math.round(h * 0.21), r: Math.round(w * 0.08), element: "木", icon: "🌱", role: "統率雄心・權柄抱負", score: 95 },
                    { id: "saturn", name: "土星丘", x: Math.round(w * 0.49), y: Math.round(h * 0.19), r: Math.round(w * 0.08), element: "土", icon: "⛰️", role: "深謀沉潛・風控紀律", score: 92 },
                    { id: "apollo", name: "太陽丘", x: Math.round(w * 0.34), y: Math.round(h * 0.21), r: Math.round(w * 0.08), element: "火", icon: "☀️", role: "行業名望・無形資產", score: 94 },
                    { id: "mercury", name: "水星丘", x: Math.round(w * 0.19), y: Math.round(h * 0.25), r: Math.round(w * 0.07), element: "水", icon: "💧", role: "財帛商機・合約談判", score: 91 },
                    { id: "venus", name: "金星丘", x: Math.round(w * 0.74), y: Math.round(h * 0.58), r: Math.round(w * 0.14), element: "金", icon: "❤️", role: "元氣底蘊・生理抗壓", score: 96 },
                    { id: "luna", name: "月丘", x: Math.round(w * 0.25), y: Math.round(h * 0.66), r: Math.round(w * 0.13), element: "水", icon: "🌙", role: "全球視野・戰略直覺", score: 93 },
                    { id: "mars1", name: "第一火星丘", x: Math.round(w * 0.66), y: Math.round(h * 0.38), r: Math.round(w * 0.07), element: "火", icon: "⚔️", role: "進取魄力・開闢主帥", score: 90 },
                    { id: "mars2", name: "第二火星丘", x: Math.round(w * 0.22), y: Math.round(h * 0.42), r: Math.round(w * 0.07), element: "火", icon: "🛡️", role: "危機防禦・抗壓堅守", score: 92 }
                ];
            }

            // 5. 計算流年節點
            this.recalculateAges(lines);

            return {
                isLeftHand,
                bounds: { w, h },
                lines,
                mounts
            };
        },

        // 動態重算貝茲曲線沿線流年節點（支援拖曳後即時聯動）
        recalculateAges: function(lines) {
            const bezierPt = (p0, p1, p2, p3, t) => {
                const mt = 1 - t;
                return {
                    x: Math.round(mt * mt * mt * p0.x + 3 * mt * mt * t * p1.x + 3 * mt * t * t * p2.x + t * t * t * p3.x),
                    y: Math.round(mt * mt * mt * p0.y + 3 * mt * mt * t * p1.y + 3 * mt * t * t * p2.y + t * t * t * p3.y)
                };
            };

            const quadPt = (p0, p1, p2, t) => {
                const mt = 1 - t;
                return {
                    x: Math.round(mt * mt * p0.x + 2 * mt * t * p1.x + t * t * p2.x),
                    y: Math.round(mt * mt * p0.y + 2 * mt * t * p1.y + t * t * p2.y)
                };
            };

            if (lines.life) {
                const p0 = lines.life.start;
                const p1 = lines.life.cp1;
                const p2 = lines.life.cp2;
                const p3 = lines.life.end;
                lines.life.ages = [
                    { age: 20, ...bezierPt(p0, p1, p2, p3, 0.18), desc: "青年奠基・元氣充沛立身" },
                    { age: 30, ...bezierPt(p0, p1, p2, p3, 0.34), desc: "立業搏擊・身心抗壓高峰" },
                    { age: 40, ...bezierPt(p0, p1, p2, p3, 0.50), desc: "不惑厚重・自律調養關鍵" },
                    { age: 50, ...bezierPt(p0, p1, p2, p3, 0.66), desc: "知命鼎盛・固本培元守成" },
                    { age: 60, ...bezierPt(p0, p1, p2, p3, 0.80), desc: "耳順泰然・元氣綿長益壽" },
                    { age: 70, ...bezierPt(p0, p1, p2, p3, 0.94), desc: "古稀享福・福澤深厚安祥" }
                ];
            }

            if (lines.fate) {
                const fp0 = lines.fate.start;
                const fp1 = lines.fate.cp1;
                const fp2 = lines.fate.end;
                lines.fate.ages = [
                    { age: 30, ...quadPt(fp0, fp1, fp2, 0.40), desc: "三十立志・主幹成形扎根" },
                    { age: 35, ...quadPt(fp0, fp1, fp2, 0.58), desc: "交會人紋・重大戰略轉折破局" },
                    { age: 50, ...quadPt(fp0, fp1, fp2, 0.80), desc: "交會天紋・基業鼎盛名望長青" }
                ];
            }
        },

        // 分析圖像並生成座標、幾何與全息診斷報告
        analyzeImage: function(canvas, imgElement, presetKey, preferredHandSide) {
            const w = canvas.width;
            const h = canvas.height;
            const seed = presetKey || (imgElement ? (imgElement.src ? imgElement.src.length % 97 : 42) : 42);

            let isPreset = false;
            let presetData = null;
            if (presetKey && this.presets[presetKey]) {
                isPreset = true;
                presetData = this.presets[presetKey];
            }

            let geomResult;

            if (isPreset) {
                // 預設經典範本掌相幾何
                const cx = w * 0.48;
                const cy = h * 0.54;
                const palmW = w * 0.62;
                const palmH = h * 0.56;
                const wristY = cy + palmH * 0.44;
                const knuckleY = cy - palmH * 0.44;

                const lifeStart = { x: Math.round(cx - palmW * 0.22), y: Math.round(knuckleY + palmH * 0.28) };
                const lifeCp1 = { x: Math.round(cx - palmW * 0.05), y: Math.round(cy - palmH * 0.05) };
                const lifeCp2 = { x: Math.round(cx - palmW * 0.06), y: Math.round(cy + palmH * 0.28) };
                const lifeEnd = presetKey === "pioneer" 
                    ? { x: Math.round(cx + palmW * 0.12), y: Math.round(wristY - palmH * 0.02) }
                    : { x: Math.round(cx - palmW * 0.15), y: Math.round(wristY - palmH * 0.04) };

                const lifeAges = [
                    { age: 20, x: Math.round(cx - palmW * 0.18), y: Math.round(knuckleY + palmH * 0.38), desc: "青年立基期・精力充沛奠基" },
                    { age: 30, x: Math.round(cx - palmW * 0.11), y: Math.round(cy - palmH * 0.02), desc: "立業搏擊期・身心抗壓峰值" },
                    { age: 40, x: Math.round(cx - palmW * 0.07), y: Math.round(cy + palmH * 0.14), desc: "不惑厚重期・自律調養關鍵" },
                    { age: 50, x: Math.round(cx - palmW * 0.08), y: Math.round(cy + palmH * 0.26), desc: "知命鼎盛期・固本培元守成" },
                    { age: 60, x: Math.round(cx - palmW * 0.11), y: Math.round(cy + palmH * 0.35), desc: "耳順泰然期・元氣綿長益壽" },
                    { age: 70, x: Math.round(cx - palmW * 0.14), y: Math.round(wristY - palmH * 0.08), desc: "古稀享福期・福澤深厚安祥" }
                ];

                const headStart = { x: Math.round(cx - palmW * 0.22), y: Math.round(knuckleY + palmH * 0.30) };
                const headCp1 = { x: Math.round(cx - palmW * 0.04), y: Math.round(cy + palmH * 0.02) };
                const headEnd = presetKey === "leader"
                    ? { x: Math.round(cx + palmW * 0.34), y: Math.round(cy + palmH * 0.06) }
                    : (presetKey === "pioneer"
                        ? { x: Math.round(cx + palmW * 0.30), y: Math.round(cy + palmH * 0.22) }
                        : { x: Math.round(cx + palmW * 0.28), y: Math.round(cy + palmH * 0.16) });

                const heartStart = { x: Math.round(cx + palmW * 0.38), y: Math.round(knuckleY + palmH * 0.24) };
                const heartCp1 = { x: Math.round(cx + palmW * 0.08), y: Math.round(knuckleY + palmH * 0.18) };
                const heartEnd = presetKey === "leader"
                    ? { x: Math.round(cx - palmW * 0.14), y: Math.round(knuckleY + palmH * 0.04) }
                    : { x: Math.round(cx - palmW * 0.08), y: Math.round(knuckleY + palmH * 0.08) };

                const fateStart = presetKey === "pioneer"
                    ? { x: Math.round(cx + palmW * 0.20), y: Math.round(wristY - palmH * 0.06) }
                    : { x: Math.round(cx + palmW * 0.02), y: Math.round(wristY - palmH * 0.04) };
                const fateCp1 = { x: Math.round(cx + palmW * 0.01), y: Math.round(cy + palmH * 0.18) };
                const fateEnd = { x: Math.round(cx - palmW * 0.02), y: Math.round(knuckleY + palmH * 0.04) };
                const fateAges = [
                    { age: 30, x: Math.round(cx + palmW * 0.01), y: Math.round(cy + palmH * 0.16), desc: "三十立志・主幹成形破土" },
                    { age: 35, x: Math.round(cx), y: Math.round(cy + palmH * 0.03), desc: "交會智慧線・重大戰略轉折與破局" },
                    { age: 50, x: Math.round(cx - palmW * 0.01), y: Math.round(knuckleY + palmH * 0.14), desc: "交會感情線・基業穩固與鼎盛榮耀" }
                ];

                const sunStart = { x: Math.round(cx + palmW * 0.15), y: Math.round(cy + palmH * 0.10) };
                const sunEnd = { x: Math.round(cx + palmW * 0.14), y: Math.round(knuckleY + palmH * 0.06) };

                const mounts = [
                    { id: "jupiter", name: "木星丘", x: Math.round(cx - palmW * 0.14), y: Math.round(knuckleY + palmH * 0.06), r: palmW * 0.09, element: "木", icon: "🌱", role: "權柄統率・雄心壯志", score: 95 },
                    { id: "saturn", name: "土星丘", x: Math.round(cx - palmW * 0.02), y: Math.round(knuckleY + palmH * 0.04), r: palmW * 0.08, element: "土", icon: "⛰️", role: "深謀沉潛・風控紀律", score: 92 },
                    { id: "apollo", name: "太陽丘", x: Math.round(cx + palmW * 0.14), y: Math.round(knuckleY + palmH * 0.06), r: palmW * 0.08, element: "火", icon: "☀️", role: "行業名望・無形資產", score: 94 },
                    { id: "mercury", name: "水星丘", x: Math.round(cx + palmW * 0.28), y: Math.round(knuckleY + palmH * 0.12), r: palmW * 0.07, element: "水", icon: "💧", role: "財帛商機・合約談判", score: 91 },
                    { id: "venus", name: "金星丘", x: Math.round(cx - palmW * 0.15), y: Math.round(cy + palmH * 0.16), r: palmW * 0.14, element: "金", icon: "❤️", role: "元氣庫存・心理韌性", score: 96 },
                    { id: "luna", name: "月丘", x: Math.round(cx + palmW * 0.22), y: Math.round(cy + palmH * 0.24), r: palmW * 0.13, element: "水", icon: "🌙", role: "全球視野・戰略直覺", score: 93 },
                    { id: "mars1", name: "第一火星丘", x: Math.round(cx - palmW * 0.16), y: Math.round(cy - palmH * 0.06), r: palmW * 0.07, element: "火", icon: "⚔️", role: "進取魄力・開闢先鋒", score: 90 },
                    { id: "mars2", name: "第二火星丘", x: Math.round(cx + palmW * 0.26), y: Math.round(cy + palmH * 0.06), r: palmW * 0.07, element: "火", icon: "🛡️", role: "危機防禦・抗壓堅守", score: 92 }
                ];

                geomResult = {
                    isLeftHand: true,
                    bounds: { cx, cy, palmW, palmH, wristY, knuckleY },
                    lines: {
                        life: { start: lifeStart, cp1: lifeCp1, cp2: lifeCp2, end: lifeEnd, ages: lifeAges },
                        head: { start: headStart, cp1: headCp1, end: headEnd },
                        heart: { start: heartStart, cp1: heartCp1, end: heartEnd },
                        fate: { start: fateStart, cp1: fateCp1, end: fateEnd, ages: fateAges },
                        sun: { start: sunStart, end: sunEnd }
                    },
                    mounts
                };
            } else {
                // 真實照片電腦視覺動態辨識與掌紋暗線掃描
                const ctx = canvas.getContext("2d");
                geomResult = this.detectPalmFeaturesFromImage(ctx, w, h, preferredHandSide);
            }

            // 整合生成正統大師診斷數據
            const score = presetData ? presetData.score : (89 + (seed % 9));
            const auspiciousTier = presetData ? presetData.auspiciousTier : (
                score >= 94 ? "上上吉・乾健鼎盛富貴格" : (score >= 90 ? "大吉・明珠出海破局格" : "吉格・厚積薄發長青格")
            );
            const handType = presetData ? presetData.handType : (
                seed % 3 === 0 ? "金形掌（方正乾健）" : (seed % 3 === 1 ? "木形掌（修長清秀）" : "土形掌（厚重沉雄）")
            );
            const handSideText = geomResult.isLeftHand ? "左手（先天命格・先天元氣秉賦）" : "右手（後天修為・事業實戰運籌）";

            const report = {
                score: score,
                auspiciousTier: auspiciousTier,
                handType: handType,
                handSide: handSideText,
                isLeftHand: geomResult.isLeftHand,
                title: presetData ? presetData.title : `天造英華・${handSideText.split("（")[0]}相法大吉格`,
                summary: `此掌相骨相清奇，肌理潤澤彈韌。電腦視覺精準捕捉掌心平原與三大主線深秀明澈之暗紋走勢，玉柱事業線縱貫乾坤，展現出「自律甚嚴、志向高遠、厚積薄發」之棟樑格局。`,
                careerLine: {
                    name: "玉柱命運線（事業線）",
                    startPoint: geomResult.isLeftHand ? "掌底坎宮筆直挺拔貫頂" : "自掌底手腕上方長驅直上",
                    trend: "直指中指土星丘基底，中途穩健貫通智慧線與感情線",
                    analysis: presetData ? presetData.features.career : "玉柱線深秀直貫掌心，象徵自驅力極度充沛，行事目標明確、不為外界浮躁雜音所惑。35歲交會智慧線處紋理深秀，提示35歲前後將迎來事業重大戰略破局與自主掌舵窗口；50歲後更臻爐火純青，乃成大器、立長青基業之吉相。",
                    keyAges: [
                        { age: "30歲前", desc: "厚植技術根基、廣結行業善緣，此時玉柱線穩步扎根，蓄勢待發。" },
                        { age: "35~50歲", desc: "事業黃金爆發期！掌權執柄、開疆闢土，面臨重大賽道躍遷與資產積累關鍵期。" },
                        { age: "50歲後", desc: "基業大成，轉向策略治理、資本賦能與培育後進，享豐碩威望。" }
                    ]
                },
                lifeLine: {
                    name: "生命線（地紋）",
                    feature: presetData ? presetData.features.life : "弧形深長圓潤，環抱廣大金星丘，色澤潤紅無雜煞鎖鏈紋",
                    analysis: "地紋為一身元氣之源！此線弧度寬闊飽滿，代表心肺精力澎湃、神經系統耐壓度極佳。無論面對多繁複的商務決策或長週期攻堅，皆具備充足的生理資本。惟須注意在 42~45 歲中年交會期調勻作息，防範因事業進取心過烈導致之精力透支。",
                    healthTip: "日常宜持之以恆進行有氧鍛鍊與正念深呼吸，維護金星丘之氣血飽滿，此乃終生事業馳騁之最大本錢。"
                },
                headLine: {
                    name: "智慧線（人紋）",
                    feature: presetData ? presetData.features.head : "深長秀麗橫貫掌心，末端平緩微降至月丘",
                    analysis: "大腦神經認知網絡卓越！既有冷靜客觀的量化分析與風控意識，又兼具宏觀戰略前瞻與直覺審美。在複雜商務博弈中能一眼看穿事物底層因果，決策果斷精準，具備高階決策者之中流砥柱定力。"
                },
                heartLine: {
                    name: "感情線（天紋）",
                    feature: presetData ? presetData.features.heart : "起於小指外側，平順流暢伸向食指木星丘",
                    analysis: "情商極高且邊界清晰！處事有情有義而不濫情，恪守契約誠信。在組織管理中善於激發同仁向心力，具備強大的人格號召力與忠誠團隊凝聚力。"
                },
                sunLine: {
                    name: "太陽線（成功名譽線）",
                    feature: presetData ? presetData.features.sun : "端正豎立於無名指下方太陽丘，清晰泛光",
                    analysis: "主行業聲望威名與公信力資產！具備此線者極易贏得行業頂層與大眾之深切信任，無形聲望極易轉化為實質商業護城河，利於打造權威個人品牌。"
                },
                mountsFocus: presetData ? presetData.mountsFocus : "木星丘（志向權威）、土星丘（深謀耐受）與金星丘（元氣底蘊）格外充實，三嶽朝拱，大成之兆。"
            };

            return {
                geometry: geomResult,
                report: report
            };
        },

        // 在 Canvas 上繪製經典範本手相（高擬真高質感手掌向量）
        drawPresetToCanvas: function(presetKey, canvas) {
            const ctx = canvas.getContext("2d");
            const w = canvas.width;
            const h = canvas.height;
            const preset = this.presets[presetKey] || this.presets.leader;

            ctx.clearRect(0, 0, w, h);

            // 1. 和風柔和漸層背景
            const bgGrad = ctx.createLinearGradient(0, 0, w, h);
            bgGrad.addColorStop(0, "#fcf9f2");
            bgGrad.addColorStop(1, "#f3ecdf");
            ctx.fillStyle = bgGrad;
            ctx.fillRect(0, 0, w, h);

            // 2. 繪製精緻手掌輪廓底圖
            ctx.save();
            ctx.shadowColor = "rgba(90, 60, 40, 0.12)";
            ctx.shadowBlur = 24;
            ctx.shadowOffsetY = 8;

            ctx.fillStyle = preset.bgTone || "#f6ede3";
            ctx.strokeStyle = preset.accentColor || "#b4532a";
            ctx.lineWidth = 3.2;
            ctx.lineJoin = "round";
            ctx.lineCap = "round";

            ctx.beginPath();
            // 拇指
            ctx.moveTo(w * 0.24, h * 0.65);
            ctx.bezierCurveTo(w * 0.16, h * 0.52, w * 0.14, h * 0.38, w * 0.18, h * 0.30);
            ctx.bezierCurveTo(w * 0.20, h * 0.26, w * 0.26, h * 0.27, w * 0.28, h * 0.34);
            ctx.lineTo(w * 0.32, h * 0.46);

            // 食指
            ctx.bezierCurveTo(w * 0.32, h * 0.35, w * 0.34, h * 0.18, w * 0.38, h * 0.13);
            ctx.bezierCurveTo(w * 0.40, h * 0.09, w * 0.45, h * 0.10, w * 0.46, h * 0.15);
            ctx.lineTo(w * 0.47, h * 0.43);

            // 中指
            ctx.bezierCurveTo(w * 0.48, h * 0.30, w * 0.50, h * 0.12, w * 0.53, h * 0.07);
            ctx.bezierCurveTo(w * 0.55, h * 0.04, w * 0.60, h * 0.05, w * 0.61, h * 0.11);
            ctx.lineTo(w * 0.60, h * 0.44);

            // 無名指
            ctx.bezierCurveTo(w * 0.62, h * 0.32, w * 0.65, h * 0.17, w * 0.69, h * 0.14);
            ctx.bezierCurveTo(w * 0.72, h * 0.12, w * 0.76, h * 0.14, w * 0.75, h * 0.20);
            ctx.lineTo(w * 0.72, h * 0.47);

            // 小指
            ctx.bezierCurveTo(w * 0.75, h * 0.38, w * 0.81, h * 0.28, w * 0.84, h * 0.29);
            ctx.bezierCurveTo(w * 0.87, h * 0.31, w * 0.87, h * 0.37, w * 0.83, h * 0.47);
            ctx.bezierCurveTo(w * 0.87, h * 0.55, w * 0.88, h * 0.65, w * 0.85, h * 0.78);

            // 掌底腕部
            ctx.bezierCurveTo(w * 0.82, h * 0.90, w * 0.73, h * 0.96, w * 0.60, h * 0.97);
            ctx.lineTo(w * 0.38, h * 0.97);
            ctx.bezierCurveTo(w * 0.26, h * 0.94, w * 0.23, h * 0.82, w * 0.24, h * 0.65);
            ctx.closePath();

            ctx.fill();
            ctx.stroke();
            ctx.restore();

            // 繪製手掌自然紋理與肌膚光澤
            const skinShine = ctx.createRadialGradient(w * 0.48, h * 0.55, 20, w * 0.48, h * 0.55, w * 0.35);
            skinShine.addColorStop(0, "rgba(255, 255, 255, 0.45)");
            skinShine.addColorStop(1, "rgba(240, 220, 200, 0)");
            ctx.fillStyle = skinShine;
            ctx.fillRect(0, 0, w, h);

            // 手腕腕褶紋（坎宮玉帶紋）
            ctx.strokeStyle = "rgba(180, 83, 42, 0.35)";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(w * 0.49, h * 0.98, w * 0.25, Math.PI * 1.15, Math.PI * 1.85);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(w * 0.49, h * 1.01, w * 0.27, Math.PI * 1.18, Math.PI * 1.82);
            ctx.stroke();
        },

        // 疊加繪製掃描線條、線上深度解說標籤、掌丘標籤與流年刻度
        renderOverlays: function(canvas, analysis, layers, activeHighlight, isCalibMode) {
            const ctx = canvas.getContext("2d");
            const geom = analysis.geometry;
            const lines = geom.lines;
            const mounts = geom.mounts;

            // 輔助繪製圓滑發光貝茲曲線
            const drawGlowPath = (pts, color, width, isDashed = false, isGlow = false) => {
                ctx.save();
                ctx.beginPath();
                ctx.strokeStyle = color;
                ctx.lineWidth = isGlow ? width * 1.8 : width;
                ctx.lineCap = "round";
                ctx.lineJoin = "round";
                if (isDashed) ctx.setLineDash([8, 4]);

                if (isGlow) {
                    ctx.shadowColor = color;
                    ctx.shadowBlur = 16;
                } else {
                    ctx.shadowColor = "rgba(0, 0, 0, 0.35)";
                    ctx.shadowBlur = 4;
                }

                ctx.moveTo(pts.start.x, pts.start.y);
                if (pts.cp2) {
                    ctx.bezierCurveTo(pts.cp1.x, pts.cp1.y, pts.cp2.x, pts.cp2.y, pts.end.x, pts.end.y);
                } else if (pts.cp1) {
                    ctx.quadraticCurveTo(pts.cp1.x, pts.cp1.y, pts.end.x, pts.end.y);
                } else {
                    ctx.lineTo(pts.end.x, pts.end.y);
                }
                ctx.stroke();
                ctx.restore();
            };

            // 輔助繪製精緻線上解說徽章標籤 (Callout Badge on Line)
            const drawLineBadge = (x, y, text, subtext, color, bgColor) => {
                ctx.save();
                ctx.font = "bold 12px 'Noto Serif TC', sans-serif";
                const textW = ctx.measureText(text).width;
                ctx.font = "10px sans-serif";
                const subW = subtext ? ctx.measureText(subtext).width : 0;
                const boxW = Math.max(textW, subW) + 20;
                const boxH = subtext ? 32 : 22;

                let drawX = x;
                let drawY = y - boxH / 2;
                if (drawX + boxW > canvas.width - 10) drawX = canvas.width - boxW - 10;
                if (drawX < 10) drawX = 10;
                if (drawY < 10) drawY = 10;

                // 膠囊底色
                ctx.fillStyle = bgColor || "rgba(255, 255, 255, 0.92)";
                ctx.strokeStyle = color;
                ctx.lineWidth = 1.6;
                ctx.shadowColor = "rgba(0, 0, 0, 0.25)";
                ctx.shadowBlur = 8;

                ctx.beginPath();
                ctx.roundRect(drawX, drawY, boxW, boxH, 8);
                ctx.fill();
                ctx.stroke();

                // 主標題
                ctx.shadowBlur = 0;
                ctx.fillStyle = color;
                ctx.font = "bold 11.5px 'Noto Serif TC', sans-serif";
                ctx.fillText(text, drawX + 10, drawY + (subtext ? 13 : 15));

                // 副說明
                if (subtext) {
                    ctx.fillStyle = "#443831";
                    ctx.font = "9.5px sans-serif";
                    ctx.fillText(subtext, drawX + 10, drawY + 26);
                }
                ctx.restore();
            };

            // 輔助繪製可拖曳微調控制節點 (Draggable Anchor Pins)
            const drawCalibHandle = (pt, color, label) => {
                ctx.save();
                ctx.fillStyle = "#ffffff";
                ctx.strokeStyle = color;
                ctx.lineWidth = 2.5;
                ctx.shadowColor = color;
                ctx.shadowBlur = 10;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 7, 0, Math.PI * 2);
                ctx.fill();
                ctx.stroke();

                ctx.fillStyle = color;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 3.5, 0, Math.PI * 2);
                ctx.fill();

                if (label) {
                    ctx.shadowBlur = 0;
                    ctx.fillStyle = "#292524";
                    ctx.font = "bold 10px sans-serif";
                    ctx.fillText(label, pt.x + 9, pt.y + 4);
                }
                ctx.restore();
            };

            // 1. 生命線（綠色）
            if (layers.all || layers.life) {
                const hl = activeHighlight === "life";
                drawGlowPath(lines.life, "#10b981", hl ? 6.0 : 4.5, false, hl);
                
                // 線上解說標籤
                drawLineBadge(
                    lines.life.cp2.x - 110, lines.life.cp2.y,
                    "🌿 地紋・生命線",
                    "元氣庫存・心理抗壓韌性卓越",
                    "#047857",
                    "rgba(240, 253, 244, 0.95)"
                );

                // 繪製流年歲數刻度節點
                if (layers.all || layers.ages || layers.life) {
                    lines.life.ages.forEach(item => {
                        ctx.save();
                        ctx.fillStyle = "#10b981";
                        ctx.strokeStyle = "#ffffff";
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.arc(item.x, item.y, 5, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.stroke();

                        ctx.fillStyle = "#064e3b";
                        ctx.font = "bold 10.5px sans-serif";
                        ctx.fillText(`${item.age}歲`, item.x - 26, item.y + 3.5);
                        ctx.restore();
                    });
                }

                // 微調手柄
                if (isCalibMode) {
                    drawCalibHandle(lines.life.start, "#10b981", "生命起點");
                    drawCalibHandle(lines.life.cp1, "#10b981", "弧度1");
                    drawCalibHandle(lines.life.cp2, "#10b981", "弧度2");
                    drawCalibHandle(lines.life.end, "#10b981", "生命終點");
                }
            }

            // 2. 智慧線（藍色）
            if (layers.all || layers.head) {
                const hl = activeHighlight === "head";
                drawGlowPath(lines.head, "#2563eb", hl ? 6.0 : 4.5, false, hl);
                
                // 線上解說標籤
                drawLineBadge(
                    lines.head.end.x - 20, lines.head.end.y + 12,
                    "🧠 人紋・智慧線",
                    "決策定力・量化因果與戰略洞察",
                    "#1d4ed8",
                    "rgba(239, 246, 255, 0.95)"
                );

                if (isCalibMode) {
                    drawCalibHandle(lines.head.start, "#2563eb", "智慧起點");
                    drawCalibHandle(lines.head.cp1, "#2563eb", "中段");
                    drawCalibHandle(lines.head.end, "#2563eb", "智慧終點");
                }
            }

            // 3. 感情線（洋紅色）
            if (layers.all || layers.heart) {
                const hl = activeHighlight === "heart";
                drawGlowPath(lines.heart, "#db2777", hl ? 6.0 : 4.5, false, hl);
                
                // 線上解說標籤
                drawLineBadge(
                    lines.heart.cp1.x - 30, lines.heart.cp1.y - 32,
                    "❤️ 天紋・感情線",
                    "情商共振・守諾重信・人脈長青",
                    "#be185d",
                    "rgba(253, 242, 248, 0.95)"
                );

                if (isCalibMode) {
                    drawCalibHandle(lines.heart.start, "#db2777", "感情起點");
                    drawCalibHandle(lines.heart.cp1, "#db2777", "中段");
                    drawCalibHandle(lines.heart.end, "#db2777", "感情終點");
                }
            }

            // 4. 事業線（琥珀金）
            if (layers.all || layers.fate) {
                const hl = activeHighlight === "fate";
                drawGlowPath(lines.fate, "#d97706", hl ? 6.0 : 4.2, true, hl);
                
                // 線上解說標籤
                drawLineBadge(
                    lines.fate.start.x + 12, lines.fate.start.y - 10,
                    "💼 玉柱・事業線",
                    "終身成就軌跡・自律自驅主帥",
                    "#b45309",
                    "rgba(254, 243, 199, 0.95)"
                );

                // 事業線關鍵轉折節點
                if (layers.all || layers.ages || layers.fate) {
                    lines.fate.ages.forEach(node => {
                        ctx.save();
                        ctx.fillStyle = "#d97706";
                        ctx.strokeStyle = "#ffffff";
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.arc(node.x, node.y, 6, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.stroke();

                        ctx.fillStyle = "#78350f";
                        ctx.font = "bold 11px sans-serif";
                        ctx.fillText(`⚡${node.age}歲`, node.x + 8, node.y + 4);
                        ctx.restore();
                    });
                }

                if (isCalibMode) {
                    drawCalibHandle(lines.fate.start, "#d97706", "事業起點");
                    drawCalibHandle(lines.fate.cp1, "#d97706", "35歲轉折");
                    drawCalibHandle(lines.fate.end, "#d97706", "事業終點");
                }
            }

            // 5. 太陽線（山吹黃）
            if (layers.all || layers.sun) {
                const hl = activeHighlight === "sun";
                drawGlowPath(lines.sun, "#ca8a04", hl ? 5.2 : 3.5, true, hl);
                
                // 線上解說標籤
                drawLineBadge(
                    lines.sun.end.x - 30, lines.sun.end.y - 28,
                    "☀️ 六秀・太陽線",
                    "行業名望・貴人相助無形資產",
                    "#854d0e",
                    "rgba(254, 252, 232, 0.95)"
                );

                if (isCalibMode) {
                    drawCalibHandle(lines.sun.start, "#ca8a04", "太陽起");
                    drawCalibHandle(lines.sun.end, "#ca8a04", "太陽終");
                }
            }

            // 6. 八大掌丘光環與文字
            if (layers.all || layers.mounts) {
                mounts.forEach(m => {
                    ctx.save();
                    ctx.strokeStyle = "rgba(180, 83, 42, 0.45)";
                    ctx.fillStyle = "rgba(255, 255, 255, 0.55)";
                    ctx.setLineDash([3, 3]);
                    ctx.lineWidth = 1.4;
                    ctx.beginPath();
                    ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.stroke();

                    // 掌丘名稱標籤
                    ctx.fillStyle = "#78350f";
                    ctx.font = "bold 11px 'Noto Serif TC', sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(`${m.icon} ${m.name}`, m.x, m.y + 4);
                    ctx.restore();
                });
            }
        }
    }
};

window.PhysiognomySystem = PhysiognomySystem;
