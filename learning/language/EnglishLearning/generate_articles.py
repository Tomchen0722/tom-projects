# -*- coding: utf-8 -*-
"""文章生成器：以模板組合產生 1980 篇分級文章（英文＋繁中），
與 articles_curated.json（20 篇精選）合併成 articles.json（共 2000 篇）。"""
import json
import os
import random

BASE = os.path.dirname(os.path.abspath(__file__))
CURATED = os.path.join(BASE, "articles_curated.json")
OUT = os.path.join(BASE, "articles.json")
PER_TEMPLATE = 165  # 4 模板 × 3 級 × 165 = 1980
rng = random.Random(20260718)

# ============================================================ 素材庫 ====
CITIES = [("Paris","巴黎"),("Tokyo","東京"),("London","倫敦"),("New York","紐約"),("Rome","羅馬"),
("Sydney","雪梨"),("Seoul","首爾"),("Bangkok","曼谷"),("Singapore","新加坡"),("Kyoto","京都"),
("Barcelona","巴塞隆納"),("Vienna","維也納"),("Prague","布拉格"),("Amsterdam","阿姆斯特丹"),("Venice","威尼斯"),
("San Francisco","舊金山"),("Vancouver","溫哥華"),("Hong Kong","香港"),("Osaka","大阪"),("Bali","峇里島"),
("Hawaii","夏威夷"),("Okinawa","沖繩"),("Queenstown","皇后鎮"),("Zurich","蘇黎世"),("Munich","慕尼黑"),
("Lisbon","里斯本"),("Athens","雅典"),("Cairo","開羅"),("Istanbul","伊斯坦堡"),("Dubai","杜拜"),
("Taipei","台北"),("Tainan","台南"),("Hualien","花蓮")]
COMPANIONS = [("my family","家人"),("my best friend","最好的朋友"),("my parents","父母"),
("my classmates","同學們"),("my sister","姊姊"),("my brother","哥哥")]
TRANSPORTS = [("plane","飛機"),("train","火車"),("bus","巴士"),("high-speed rail","高鐵"),("ferry","渡輪")]
LOCAL_FOODS = [("noodles","麵"),("seafood","海鮮"),("street food","街頭小吃"),("desserts","甜點"),
("dumplings","餃子"),("grilled meat","烤肉"),("fresh fruit","新鮮水果"),("ice cream","冰淇淋"),
("hot pot","火鍋"),("local snacks","當地點心"),("bread","麵包"),("cheese","起司")]
SIGHTS = [("an old temple","一座古老的寺廟"),("a famous museum","一間著名的博物館"),
("a beautiful beach","一片美麗的海灘"),("a big night market","一個大夜市"),
("a historic castle","一座歷史悠久的城堡"),("a quiet lake","一座寧靜的湖"),
("a tall tower","一座高塔"),("a lovely old street","一條可愛的老街"),
("a huge park","一座大公園"),("a colorful harbor","一個色彩繽紛的港口")]
PETS = [("dog","狗"),("cat","貓"),("rabbit","兔子"),("parrot","鸚鵡"),("hamster","倉鼠"),
("goldfish","金魚"),("turtle","烏龜"),("hedgehog","刺蝟")]
PET_NAMES = ["Lucky","Coco","Momo","Snowy","Toto","Ball","Mochi","Kiki","Latte","Cookie",
"Pudding","Nono","Happy","Sunny","QQ","Doudou","Milo","Bobo","Nini","Tangtang"]
PET_TRAITS = [("very clever","非常聰明"),("a little shy","有點害羞"),("full of energy","精力充沛"),
("quiet and gentle","安靜又溫柔"),("naughty but cute","調皮但可愛"),("always hungry","總是肚子餓")]
PET_ACTS = [("chases the ball in the living room","在客廳追球"),
("sleeps on my bed all afternoon","整個下午都睡在我床上"),
("waits for me at the door every day","每天在門口等我"),
("hides my socks under the sofa","把我的襪子藏到沙發下"),
("watches birds by the window","在窗邊看小鳥"),
("follows me around the house","在家裡跟著我到處走")]
SKILLS_A = [("swim","游泳"),("cook","做菜"),("ride a bike","騎腳踏車"),("play the guitar","彈吉他"),
("draw","畫畫"),("dance","跳舞"),("skate","溜冰"),("take photos","攝影"),
("bake bread","烤麵包"),("play chess","下棋"),("play badminton","打羽球"),("make dumplings","包餃子")]
TEACHERS = [("my father","爸爸"),("my mother","媽媽"),("my teacher","老師"),("my best friend","好朋友")]
WEATHERS = [("rainy","下雨的"),("sunny","晴朗的"),("windy","颳風的"),("snowy","下雪的"),("cloudy","多雲的"),("stormy","暴風雨的")]
HOME_ACTS = [("read comic books","看漫畫"),("bake cookies","烤餅乾"),("watch old movies","看老電影"),
("play board games","玩桌遊"),("draw pictures","畫畫"),("listen to music","聽音樂"),
("clean my room","整理房間"),("write letters","寫信"),("do a puzzle","拼拼圖"),("make hot soup","煮熱湯")]
ACTIVITIES_B = [("jogging","慢跑"),("swimming","游泳"),("reading","閱讀"),("yoga","瑜伽"),
("hiking","健行"),("cycling","騎自行車"),("meditation","冥想"),("gardening","園藝"),
("dancing","跳舞"),("cooking at home","在家做菜"),("keeping a diary","寫日記"),
("learning languages","學習語言"),("playing chess","下棋"),("volunteering","當志工")]
BENEFITS = [("it strengthens your heart and improves your sleep","它能強化心臟並改善睡眠"),
("it reduces stress after a long day","它能減輕一整天下來的壓力"),
("it helps you focus better at work or school","它能幫助你在工作或課業上更專注"),
("it brings you closer to friends who share the same interest","它能讓你和志同道合的朋友更親近"),
("it teaches you patience and discipline","它能培養你的耐心與自律"),
("it gives your brain a healthy break from screens","它能讓大腦健康地遠離螢幕休息"),
("it builds confidence step by step","它能一步步建立自信"),
("it costs almost nothing to start","開始幾乎不需要任何花費")]
COUNTRIES = [("Japan","日本"),("France","法國"),("Italy","義大利"),("Thailand","泰國"),("Korea","韓國"),
("Spain","西班牙"),("Germany","德國"),("Vietnam","越南"),("India","印度"),("Turkey","土耳其"),
("Mexico","墨西哥"),("Greece","希臘"),("Portugal","葡萄牙"),("Egypt","埃及"),("Brazil","巴西"),
("Australia","澳洲"),("Canada","加拿大"),("Switzerland","瑞士"),("Morocco","摩洛哥"),("Peru","祕魯"),
("Iceland","冰島"),("New Zealand","紐西蘭")]
CULTURE_POINTS = [("people take off their shoes before entering a home","人們進屋前會先脫鞋"),
("meals are shared and eaten slowly with family","餐點是與家人共享、慢慢享用的"),
("markets open early and are full of fresh local food","市場很早開門，滿是新鮮的當地食物"),
("old festivals are still celebrated in every town","每個城鎮仍會慶祝古老的節慶"),
("strangers greet each other warmly on the street","陌生人在街上會熱情地打招呼"),
("tea or coffee is offered to every guest","每位客人都會被奉上茶或咖啡"),
("music and dancing are part of daily life","音樂和舞蹈是日常生活的一部分"),
("history is protected in beautiful old buildings","歷史被保存在美麗的老建築中")]
SKILLS_B = [("English listening","英文聽力"),("vocabulary","單字量"),("writing","寫作能力"),
("time management","時間管理"),("memory","記憶力"),("focus","專注力"),
("public speaking","公開演說"),("reading speed","閱讀速度"),("pronunciation","發音"),("note-taking","筆記技巧")]
TIPS = [("practice a little every single day instead of cramming once a week","每天練習一點點，而不是一週猛讀一次"),
("set a small, clear goal before you start each session","每次開始前先設定一個小而明確的目標"),
("review what you learned before going to bed","睡前複習當天學到的內容"),
("track your progress in a notebook so you can see how far you have come","用筆記本記錄進度，讓自己看見成長"),
("find a partner who wants to improve too","找一個也想進步的夥伴"),
("turn off your phone for twenty-five minutes and work in short sprints","關掉手機二十五分鐘，用短衝刺的方式練習"),
("reward yourself after finishing a difficult task","完成困難任務後給自己一點獎勵"),
("do not be afraid of mistakes - they show you what to fix next","別害怕犯錯——錯誤會告訴你下一步該修正什麼")]
CHALLENGES = [("marathon","馬拉松"),("job interview","工作面試"),("English speech","英文演講"),
("flight abroad","出國航班"),("cooking contest","料理比賽"),("big exam","大考"),
("camping trip","露營之旅"),("part-time job","打工"),("bicycle race","自行車比賽"),
("piano recital","鋼琴發表會"),("mountain hike","登山健行"),("class presentation","課堂報告")]
TECHS = [("artificial intelligence","人工智慧"),("electric vehicles","電動車"),("renewable energy","再生能源"),
("space travel","太空旅行"),("virtual reality","虛擬實境"),("robotics","機器人技術"),
("biotechnology","生物科技"),("quantum computing","量子運算"),("smart homes","智慧家庭"),
("delivery drones","送貨無人機"),("digital currency","數位貨幣"),("3D printing","3D 列印"),
("wearable devices","穿戴式裝置"),("online education","線上教育"),("telemedicine","遠距醫療")]
TECH_PROS = [("it could make services cheaper and available to far more people","它可能讓服務更便宜、讓更多人能夠使用"),
("it may free workers from dangerous or repetitive tasks","它或許能讓工作者擺脫危險或重複性的工作"),
("it opens doors for small companies to compete with giants","它讓小公司也有機會與巨頭競爭"),
("it could help us use resources far more efficiently","它可能幫助我們更有效率地使用資源"),
("early results in hospitals and schools are already promising","它在醫院與學校的初步成果已相當令人期待")]
TECH_CONS = [("the technology is still expensive and imperfect","這項技術仍然昂貴且不完美"),
("rules and laws have not caught up with the change","法規尚未跟上變化的腳步"),
("some workers may lose their jobs during the transition","部分工作者可能在轉型過程中失業"),
("privacy and safety questions remain unanswered","隱私與安全的疑慮仍未解決"),
("society needs time to build trust in it","社會需要時間建立對它的信任")]
ISSUES = [("urban traffic","城市交通"),("an aging society","高齡化社會"),("plastic pollution","塑膠污染"),
("food waste","食物浪費"),("information overload","資訊過載"),("work-life balance","工作與生活的平衡"),
("climate change","氣候變遷"),("housing affordability","居住負擔"),("cyber security","網路安全"),
("fake news","假新聞"),("water shortage","水資源短缺"),("youth unemployment","青年失業")]
ISSUE_ACTS = [("governments can set clearer rules and invest in long-term solutions","政府可以制定更明確的規範並投資長期解方"),
("schools can teach the next generation to face it early","學校可以及早教導下一代面對它"),
("companies should treat it as a responsibility, not just a cost","企業應把它視為責任，而不只是成本"),
("each of us can change one small daily habit","我們每個人都可以改變一個小小的日常習慣"),
("communities can share resources and ideas instead of working alone","社區之間可以共享資源與想法，而不是單打獨鬥")]
INVENTIONS = [("the printing press","印刷術"),("the internet","網際網路"),("the smartphone","智慧型手機"),
("the airplane","飛機"),("electricity","電力"),("the automobile","汽車"),
("vaccines","疫苗"),("the camera","相機"),("the refrigerator","冰箱"),
("the television","電視"),("the computer","電腦"),("antibiotics","抗生素"),
("the telephone","電話"),("social media","社群媒體")]
DEBATES = [("work a four-day week","實施週休三日"),("ban plastic bags","禁用塑膠袋"),
("learn coding at school","在學校學寫程式"),("live without cash","過無現金生活"),
("allow phones in class","允許課堂使用手機"),("work from home permanently","永久在家工作"),
("make museums free","博物館免費開放"),("limit screen time for children","限制兒童螢幕時間"),
("tax sugary drinks","對含糖飲料課稅"),("require volunteer service","規定志工服務"),
("keep zoos open","繼續開放動物園"),("build more nuclear plants","興建更多核電廠")]
PRO_ARGS = [("supporters believe it would improve health and happiness over time","支持者認為長期而言它能提升健康與幸福感"),
("it could save money and resources for everyone involved","它可能為所有相關的人省下金錢與資源"),
("studies in several countries show encouraging early results","數個國家的研究顯示出令人鼓舞的初步結果"),
("it would push society to try new and creative solutions","它會促使社會嘗試新穎且有創意的解方")]
CON_ARGS = [("critics worry that the costs would fall on those least able to pay","批評者擔心成本會落在最無力負擔的人身上"),
("the change could be hard to enforce fairly","這項改變可能難以公平執行"),
("some fear it solves one problem but creates another","有人擔心它解決了一個問題卻製造了另一個"),
("older systems and habits are difficult to replace quickly","舊有的制度與習慣難以快速取代")]
MONTHS = [("last summer","去年夏天"),("last winter","去年冬天"),("last spring","去年春天"),
("last October","去年十月"),("last month","上個月"),("during the New Year holiday","新年假期期間")]
FEELINGS = [("It was one of the happiest times of my life","那是我人生中最快樂的時光之一"),
("I will never forget that wonderful trip","我永遠不會忘記那趟美好的旅程"),
("Just thinking about it still makes me smile","光是回想起來仍讓我微笑"),
("It taught me how big and interesting the world is","它讓我明白世界多麼廣大又有趣")]

# ============================================================ 模板 ====

def pick(pool, n, r):
    return r.sample(pool, n)


def t_trip(r):
    city = r.choice(CITIES); comp = r.choice(COMPANIONS); tr = r.choice(TRANSPORTS)
    m = r.choice(MONTHS); food = r.choice(LOCAL_FOODS); sight = r.choice(SIGHTS)
    feel = r.choice(FEELINGS); hours = r.randint(2, 9)
    return {
        "title": f"My Trip to {city[0]}", "title_zh": f"我的{city[1]}之旅", "level": "初級",
        "paragraphs": [
            {"en": f"{m[0].capitalize()}, I visited {city[0]} with {comp[0]}. We went there by {tr[0]}. The trip took about {hours} hours, but I was too excited to feel tired.",
             "zh": f"{m[1]}，我和{comp[1]}一起去了{city[1]}。我們搭{tr[1]}前往，路程大約花了{hours}個小時，但我興奮得一點也不覺得累。"},
            {"en": f"On the first day, we saw {sight[0]}. It was even more beautiful than the photos online. Later, we tried the famous local {food[0]}. The taste was amazing, and we ordered more.",
             "zh": f"第一天，我們參觀了{sight[1]}。它比網路上的照片更美。之後我們品嚐了當地著名的{food[1]}，味道好極了，我們又多點了一些。"},
            {"en": f"Time passed so quickly. Before we left, we bought some small gifts for our friends. {feel[0]}. I hope I can visit {city[0]} again someday.",
             "zh": f"時間過得好快。離開前，我們買了一些小禮物送給朋友。{feel[1]}。希望有一天我能再訪{city[1]}。"}]}


def t_pet(r):
    pet = r.choice(PETS); name = r.choice(PET_NAMES); trait = r.choice(PET_TRAITS)
    a1, a2 = pick(PET_ACTS, 2, r)
    return {
        "title": f"My {pet[0].capitalize()} {name}", "title_zh": f"我的{pet[1]}{name}", "level": "初級",
        "paragraphs": [
            {"en": f"I have a {pet[0]} named {name}. {name} is {trait[0]}. Everyone in my family loves {name} very much.",
             "zh": f"我有一隻{pet[1]}，名叫{name}。{name}{trait[1]}。我們全家人都非常愛{name}。"},
            {"en": f"Every day, {name} {a1[0]}. Sometimes {name} also {a2[0]}. When I do my homework, {name} sits quietly beside me like a little guard.",
             "zh": f"每天，{name}都會{a1[1]}。有時候{name}也會{a2[1]}。我寫作業時，{name}會像個小守衛一樣安靜地坐在我旁邊。"},
            {"en": f"Taking care of a pet is not always easy, but {name} gives me so much happiness. A pet is not just an animal - it is family.",
             "zh": f"照顧寵物並不總是容易，但{name}帶給我好多快樂。寵物不只是動物——牠是家人。"}]}


def t_learn(r):
    sk = r.choice(SKILLS_A); tch = r.choice(TEACHERS); weeks = r.randint(2, 10)
    return {
        "title": f"Learning to {sk[0].capitalize()}", "title_zh": f"學{sk[1]}", "level": "初級",
        "paragraphs": [
            {"en": f"This year, I decided to learn to {sk[0]}. {tch[0].capitalize()} offered to teach me. At first, I thought it would be easy, but I was wrong.",
             "zh": f"今年，我決定要學{sk[1]}。{tch[1]}主動說要教我。一開始我以為很簡單，但我錯了。"},
            {"en": f"In the first week, I made many mistakes and almost gave up. {tch[0].capitalize()} smiled and said, \"Everyone starts badly. Just keep practicing.\" So I practiced a little every day.",
             "zh": f"第一週，我犯了很多錯，差點放棄。{tch[1]}微笑著說：「每個人一開始都做不好，繼續練習就對了。」於是我每天練習一點點。"},
            {"en": f"After about {weeks} weeks, something wonderful happened - I could really {sk[0]}! Now I understand: if you practice every day, nothing is impossible.",
             "zh": f"大約{weeks}週後，美好的事發生了——我真的會{sk[1]}了！現在我明白：只要每天練習，沒有什麼是不可能的。"}]}


def t_weather(r):
    w = r.choice(WEATHERS); a1, a2 = pick(HOME_ACTS, 2, r); comp = r.choice(COMPANIONS)
    return {
        "title": f"A {w[0].capitalize()} Day", "title_zh": f"{w[1]}一天", "level": "初級",
        "paragraphs": [
            {"en": f"Last Saturday was a {w[0]} day, so we could not go out as planned. I felt a little sad at first, looking out of the window.",
             "zh": f"上週六是{w[1]}一天，我們無法照計畫出門。一開始我望著窗外，覺得有點難過。"},
            {"en": f"Then {comp[0]} had a great idea: we could {a1[0]} together at home. Later, we also {a2[0]}. The living room was full of laughter all afternoon.",
             "zh": f"接著{comp[1]}想到一個好主意：我們可以一起在家{a1[1]}。後來我們還{a2[1]}。整個下午客廳都充滿了笑聲。"},
            {"en": "That day I learned something important: a good day does not depend on the weather. It depends on the people you spend it with.",
             "zh": "那天我學到重要的一課：美好的一天不取決於天氣，而取決於和你共度的人。"}]}


def t_benefit(r):
    act = r.choice(ACTIVITIES_B); b1, b2, b3 = pick(BENEFITS, 3, r)
    return {
        "title": f"Why {act[0].title()} Is Good for You", "title_zh": f"為什麼{act[1]}對你有益", "level": "中級",
        "paragraphs": [
            {"en": f"In our busy modern life, many people are rediscovering {act[0]}. It requires no special talent, and almost anyone can begin this week.",
             "zh": f"在忙碌的現代生活中，許多人重新發現了{act[1]}的好處。它不需要特殊天分，幾乎任何人本週就能開始。"},
            {"en": f"The benefits are greater than most people expect. First, {b1[0]}. Second, {b2[0]}. Research also suggests that {b3[0]}.",
             "zh": f"它的好處比多數人想像的更多。首先，{b1[1]}。其次，{b2[1]}。研究也指出，{b3[1]}。"},
            {"en": f"You do not need to be perfect at it - you only need to start. Try {act[0]} for just fifteen minutes tomorrow, and let the habit grow from there.",
             "zh": f"你不需要做得完美——只需要開始。明天先試著{act[1]}十五分鐘，讓習慣從那裡慢慢成長。"}]}


def t_country(r):
    c = r.choice(COUNTRIES); p1, p2, p3 = pick(CULTURE_POINTS, 3, r)
    return {
        "title": f"A Glimpse of Life in {c[0]}", "title_zh": f"一窺{c[1]}的生活", "level": "中級",
        "paragraphs": [
            {"en": f"Every country has its own rhythm of life, and {c[0]} is no exception. Visitors often notice small details that locals no longer see.",
             "zh": f"每個國家都有自己的生活節奏，{c[1]}也不例外。旅人常會注意到當地人早已習以為常的小細節。"},
            {"en": f"For example, in {c[0]}, {p1[0]}. It is also common that {p2[0]}. Perhaps most charming of all, {p3[0]}.",
             "zh": f"舉例來說，在{c[1]}，{p1[1]}。此外，{p2[1]}也很常見。也許最迷人的是，{p3[1]}。"},
            {"en": "Learning about another culture is like holding up a mirror: it shows us that our own \"normal\" is just one of many ways to live. That may be the greatest gift of travel.",
             "zh": "認識另一種文化就像舉起一面鏡子：它讓我們明白，自己的「日常」只是眾多生活方式之一。這或許就是旅行最大的禮物。"}]}


def t_improve(r):
    sk = r.choice(SKILLS_B); t1, t2, t3 = pick(TIPS, 3, r)
    return {
        "title": f"How to Improve Your {sk[0].title()}", "title_zh": f"如何提升你的{sk[1]}", "level": "中級",
        "paragraphs": [
            {"en": f"Many learners feel stuck with their {sk[0]}. They work hard but see little progress, and slowly they lose heart. The problem is usually the method, not the effort.",
             "zh": f"許多學習者覺得自己的{sk[1]}停滯不前。他們很努力卻看不到進步，漸漸失去信心。問題通常出在方法，而不是努力。"},
            {"en": f"Here are three habits that actually work. One: {t1[0]}. Two: {t2[0]}. Three: {t3[0]}.",
             "zh": f"以下是三個真正有效的習慣。第一：{t1[1]}。第二：{t2[1]}。第三：{t3[1]}。"},
            {"en": f"Improvement is rarely dramatic; it arrives quietly, week by week. Choose one habit above, apply it to your {sk[0]} today, and trust the process.",
             "zh": f"進步很少是戲劇性的；它總是一週一週安靜地到來。從上面選一個習慣，今天就用在你的{sk[1]}上，然後相信這個過程。"}]}


def t_first(r):
    ch = r.choice(CHALLENGES)
    return {
        "title": f"My First {ch[0].title()}", "title_zh": f"我的第一次{ch[1]}", "level": "中級",
        "paragraphs": [
            {"en": f"I still remember the morning of my first {ch[0]}. My hands were cold, my heart was racing, and a small voice in my head kept asking, \"What if I fail?\"",
             "zh": f"我仍記得第一次{ch[1]}那天早上。我的手冰冷，心跳加速，腦中有個小聲音不斷問：「如果失敗了怎麼辦？」"},
            {"en": "Once it began, however, something surprising happened. I was too busy to be afraid. Every small step took all my attention, and the fear quietly stepped aside. I made mistakes, of course - but none of them ended the world.",
             "zh": "然而一旦開始，令人意外的事發生了。我忙得沒有時間害怕。每一個小步驟都佔據了我的注意力，恐懼就悄悄退到一旁。我當然犯了錯——但沒有一個錯讓世界毀滅。"},
            {"en": f"Looking back, that {ch[0]} taught me a lesson no book could: courage is not the absence of fear. It is deciding that something matters more than fear.",
             "zh": f"回頭看，那次{ch[1]}教會我書本學不到的一課：勇氣不是沒有恐懼，而是決定有些事比恐懼更重要。"}]}


def t_future(r):
    tech = r.choice(TECHS); p1, p2 = pick(TECH_PROS, 2, r); c1, c2 = pick(TECH_CONS, 2, r)
    return {
        "title": f"The Future of {tech[0].title()}", "title_zh": f"{tech[1]}的未來", "level": "進階",
        "paragraphs": [
            {"en": f"Few technologies attract as much attention today as {tech[0]}. Investment is pouring in, headlines alternate between excitement and alarm, and ordinary people wonder how their lives will change.",
             "zh": f"當今很少有科技像{tech[1]}這樣吸引目光。資金不斷湧入，新聞標題在興奮與警告之間擺盪，一般人則想知道自己的生活將如何改變。"},
            {"en": f"The optimistic case is compelling: {p1[0]}, and {p2[0]}. Yet the concerns deserve equal attention - {c1[0]}, and {c2[0]}.",
             "zh": f"樂觀的理由很有說服力：{p1[1]}，而且{p2[1]}。然而疑慮同樣值得重視——{c1[1]}，而且{c2[1]}。"},
            {"en": f"The future of {tech[0]} will probably be neither utopia nor disaster. Like every powerful tool before it, its impact will depend less on the technology itself than on the wisdom of the people who use it.",
             "zh": f"{tech[1]}的未來大概既非烏托邦也非災難。如同以往每一項強大的工具，它的影響與其說取決於技術本身，不如說取決於使用它的人是否有智慧。"}]}


def t_issue(r):
    iss = r.choice(ISSUES); a1, a2 = pick(ISSUE_ACTS, 2, r)
    return {
        "title": f"Facing the Challenge of {iss[0].title()}", "title_zh": f"面對{iss[1]}的挑戰", "level": "進階",
        "paragraphs": [
            {"en": f"Among the many problems modern society faces, {iss[0]} stands out because it touches almost everyone, yet no single person can solve it alone. Ignoring it only makes the eventual cost higher.",
             "zh": f"在現代社會面臨的眾多問題中，{iss[1]}格外突出，因為它幾乎影響每一個人，卻沒有任何個人能獨力解決。忽視它只會讓最終的代價更高。"},
            {"en": f"Progress is possible, but it requires action on several levels at once. {a1[0].capitalize()}. At the same time, {a2[0]}.",
             "zh": f"進展是可能的，但需要多個層面同時行動。{a1[1]}。與此同時，{a2[1]}。"},
            {"en": f"History shows that societies can change faster than anyone expects once enough people decide the problem is theirs. {iss[0].capitalize()} will test whether we make that decision in time.",
             "zh": f"歷史證明，一旦有夠多人把問題當成自己的事，社會的改變會比任何人預期的更快。{iss[1]}將考驗我們能否及時做出這個決定。"}]}


def t_invention(r):
    inv = r.choice(INVENTIONS)
    return {
        "title": f"How {inv[0].title()} Changed the World", "title_zh": f"{inv[1]}如何改變世界", "level": "進階",
        "paragraphs": [
            {"en": f"It is difficult for us to imagine daily life before {inv[0]}. Yet for most of human history, people lived, worked, and dreamed without it, organizing their world around entirely different limits.",
             "zh": f"我們很難想像沒有{inv[1]}的日常生活。然而在人類歷史的大部分時間裡，人們在沒有它的情況下生活、工作、作夢，圍繞著完全不同的限制安排世界。"},
            {"en": f"When {inv[0]} arrived, the change was not instant - early versions were clumsy, expensive, and widely doubted. But step by step it reshaped how people spend their time, whom they can reach, and what they believe is possible.",
             "zh": f"當{inv[1]}問世時，改變並非一蹴可幾——早期的版本笨拙、昂貴，且普遍受到質疑。但它一步步重塑了人們運用時間的方式、能夠接觸的對象，以及對「可能」的想像。"},
            {"en": f"The story of {inv[0]} carries a lesson for every new technology we meet today: revolutions rarely announce themselves. They begin as toys, tools, or curiosities - and quietly become the ground we stand on.",
             "zh": f"{inv[1]}的故事為我們今天遇到的每一項新科技留下一課：革命很少會預先宣告。它們以玩具、工具或新奇玩意的姿態出現——然後悄悄變成我們腳下的地基。"}]}


def t_debate(r):
    d = r.choice(DEBATES); p1, p2 = pick(PRO_ARGS, 2, r); c1, c2 = pick(CON_ARGS, 2, r)
    return {
        "title": f"Should We {d[0].capitalize()}?", "title_zh": f"我們應該{d[1]}嗎？", "level": "進階",
        "paragraphs": [
            {"en": f"The question of whether we should {d[0]} has moved from casual conversation into serious public debate. Both sides raise points that deserve honest consideration.",
             "zh": f"「我們是否應該{d[1]}」這個問題，已從閒聊話題變成嚴肅的公共辯論。正反雙方都提出了值得認真思考的論點。"},
            {"en": f"On one hand, {p1[0]}, and {p2[0]}. On the other hand, {c1[0]}, while {c2[0]}.",
             "zh": f"一方面，{p1[1]}，而且{p2[1]}。另一方面，{c1[1]}，同時{c2[1]}。"},
            {"en": "Perhaps the wisest path is neither blind enthusiasm nor automatic rejection, but small, honest experiments: try the idea at a limited scale, measure the results, and let evidence - not slogans - make the final decision.",
             "zh": "也許最明智的路既不是盲目擁抱，也不是直接否決，而是小規模的誠實實驗：在有限範圍內嘗試、衡量結果，讓證據——而不是口號——做出最終決定。"}]}


TEMPLATES = [t_trip, t_pet, t_learn, t_weather,
             t_benefit, t_country, t_improve, t_first,
             t_future, t_issue, t_invention, t_debate]


def main():
    curated = []
    if os.path.exists(CURATED):
        curated = json.load(open(CURATED, encoding="utf-8"))
    for a in curated:
        a["source"] = "精選"
        if not a["title"].startswith("★"):
            a["title"] = "★ " + a["title"]

    generated, seen = [], set()
    for tmpl in TEMPLATES:
        count, tries = 0, 0
        while count < PER_TEMPLATE and tries < PER_TEMPLATE * 60:
            tries += 1
            art = tmpl(rng)
            key = json.dumps([p["en"] for p in art["paragraphs"]], ensure_ascii=False)
            if key in seen:
                continue
            seen.add(key)
            art["source"] = "生成"
            generated.append(art)
            count += 1
        if count < PER_TEMPLATE:
            print("WARN", tmpl.__name__, "only", count)

    # 不足 1980 篇時，用其他模板補足
    tries = 0
    while len(generated) < 1980 and tries < 400000:
        tries += 1
        art = rng.choice(TEMPLATES)(rng)
        key = json.dumps([p["en"] for p in art["paragraphs"]], ensure_ascii=False)
        if key in seen:
            continue
        seen.add(key)
        art["source"] = "生成"
        generated.append(art)

    # 同名文章加編號
    title_count = {}
    for a in generated:
        t = a["title"]
        title_count[t] = title_count.get(t, 0) + 1
        if title_count[t] > 1:
            a["title"] = f"{t} ({title_count[t]})"

    allarts = curated + generated
    json.dump(allarts, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    lv = {}
    for a in allarts:
        lv[a["level"]] = lv.get(a["level"], 0) + 1
    print("DONE total", len(allarts), lv)


if __name__ == "__main__":
    main()
