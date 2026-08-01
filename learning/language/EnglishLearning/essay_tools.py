# -*- coding: utf-8 -*-
"""完整寫作強化：📄 一鍵生成範文（英中對照）、🧑‍🏫 批閱文章（統計/詞彙分級/拼字/文法/評分）。
由 main.py 呼叫 attach(app, nb)，把按鈕加進既有的「完整寫作」分頁。"""
import datetime
import os
import random
import re
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESSAY_DIR = os.path.join(BASE_DIR, "essays")

# ------------------------------------------------------------ 範文庫（英中對照） ----
MODEL_ESSAYS = {
"My favorite hobby and why I enjoy it.": [
 {"en": "My favorite hobby is drawing. I started when I was seven, copying cartoon characters from television, and I have never stopped since then.",
  "zh": "我最喜歡的嗜好是畫畫。我七歲時開始，從模仿電視上的卡通人物畫起，從那之後就再也沒有停過。"},
 {"en": "Drawing makes me calm. When I sit down with a pencil, the noisy world becomes quiet, and one hour passes like five minutes. It also teaches me to observe carefully. Most people walk past a tree without looking, but I notice the shape of its branches and the color of its leaves.",
  "zh": "畫畫讓我平靜。當我拿著鉛筆坐下來，喧鬧的世界就變得安靜，一個小時像五分鐘一樣飛逝。它也教我仔細觀察。大多數人經過一棵樹時不會多看一眼，但我會注意到樹枝的形狀和葉子的顏色。"},
 {"en": "My sketchbook is like a diary without words. When I turn its pages, I can remember exactly where I was and how I felt. That is why drawing is not just a hobby to me - it is a way to keep my memories alive.",
  "zh": "我的素描本就像一本沒有文字的日記。翻開它，我能清楚記得當時身在何處、心情如何。這就是為什麼畫畫對我而言不只是嗜好——它是讓回憶保持鮮活的方式。"}],
"Describe your best friend.": [
 {"en": "My best friend is Kevin. We met on the first day of junior high school, when neither of us knew anyone in the class. He borrowed my eraser, and somehow we have been talking ever since.",
  "zh": "我最好的朋友是凱文。我們在國中開學第一天認識，當時我們在班上誰都不認識。他向我借了一塊橡皮擦，不知不覺我們就一直聊到現在。"},
 {"en": "Kevin is patient and honest. When I make a mistake, he tells me directly, but never in a mean way. He is also the funniest person I know; even our teachers cannot help laughing at his jokes. We play basketball on weekends and help each other with homework during the week.",
  "zh": "凱文既有耐心又誠實。當我犯錯時，他會直接告訴我，但從不刻薄。他也是我認識最風趣的人，連老師都會被他的笑話逗笑。我們週末一起打籃球，平日互相幫忙寫作業。"},
 {"en": "A good friend is hard to find and easy to keep, if you treat him well. I am lucky that a small eraser brought me a friendship that I believe will last for many years.",
  "zh": "好朋友難尋，但只要真心相待就容易長久。我很幸運，一塊小小的橡皮擦帶給我一段我相信會持續多年的友誼。"}],
"A place I want to visit someday.": [
 {"en": "The place I most want to visit is Iceland. I first saw it in a documentary: black beaches, blue ice caves, and the green northern lights dancing in the dark sky. Since that day, the picture has stayed in my mind.",
  "zh": "我最想造訪的地方是冰島。我第一次看到它是在一部紀錄片裡：黑色的沙灘、藍色的冰洞，還有在黑夜中舞動的綠色極光。從那天起，那幅畫面就一直留在我腦海裡。"},
 {"en": "There are three things I want to do there. First, I want to watch the northern lights with my own eyes, not through a screen. Second, I want to bathe in a hot spring while the air around me is freezing. Third, I want to stand in a place with no buildings and no cars, and listen to complete silence.",
  "zh": "在那裡我想做三件事。第一，我想親眼看極光，而不是透過螢幕。第二，我想在凍人的空氣中泡溫泉。第三，我想站在一個沒有建築、沒有車輛的地方，聆聽全然的寂靜。"},
 {"en": "Traveling is not only about taking photos. I believe a place like Iceland can teach me how large and quiet the world really is. I am saving money for this dream, and I hope to make it come true before I turn thirty.",
  "zh": "旅行不只是拍照。我相信冰島這樣的地方能讓我體會世界有多遼闊、多安靜。我正在為這個夢想存錢，希望能在三十歲前實現它。"}],
"What did you do last weekend?": [
 {"en": "Last weekend was simple, but I enjoyed every minute of it. On Saturday morning, I helped my mother clean the apartment. We opened all the windows, and the whole house smelled like fresh air and soap.",
  "zh": "上個週末很平凡，但我享受其中的每一分鐘。星期六早上，我幫媽媽打掃公寓。我們打開所有窗戶，整個家充滿了新鮮空氣和肥皂的味道。"},
 {"en": "In the afternoon, I met two classmates at the library. We studied for our English test for two hours, and then rewarded ourselves with fried chicken and bubble tea. On Sunday, my father drove us to the riverside park. I rode a bicycle along the water while my parents walked behind me, talking and laughing.",
  "zh": "下午，我和兩位同學約在圖書館。我們為英文考試唸了兩小時的書，然後用炸雞和珍珠奶茶犒賞自己。星期天，爸爸開車帶我們去河濱公園。我沿著河邊騎腳踏車，父母走在後面有說有笑。"},
 {"en": "Nothing special happened, and that is exactly the point. A weekend does not need to be exciting to be good. Clean rooms, warm food, and family time are enough to fill my heart before a new week begins.",
  "zh": "沒有發生什麼特別的事，而這正是重點。週末不需要刺激才算美好。乾淨的房間、溫熱的食物和家人相處的時光，就足以在新的一週開始前填滿我的心。"}],
"The most delicious food I have ever eaten.": [
 {"en": "The most delicious food I have ever eaten was a bowl of beef noodle soup in a tiny shop near my grandmother's house. The shop has only four tables, and the owner, an old man with white hair, has been cooking the same dish for forty years.",
  "zh": "我吃過最美味的食物，是外婆家附近一間小店的牛肉麵。那間店只有四張桌子，老闆是位白髮老先生，同一道料理他煮了四十年。"},
 {"en": "The soup is dark and rich, with a smell that reaches the street corner. The beef is so soft that it almost melts, and the noodles are chewy and fresh. Every time I visit, the owner adds an extra piece of beef to my bowl and says, \"Growing kids need to eat more.\"",
  "zh": "湯頭色深味濃，香氣飄到街角。牛肉軟嫩得幾乎入口即化，麵條又Q又新鮮。每次我去，老闆都會多放一塊牛肉到我碗裡，說：「發育中的孩子要多吃一點。」"},
 {"en": "I have eaten in fancy restaurants since then, but nothing compares to that small shop. Maybe the secret ingredient is not in the soup at all. It is the memory of sitting there with my grandmother, blowing on the hot noodles, feeling completely at home.",
  "zh": "後來我也去過高級餐廳，但沒有一家比得上那間小店。也許祕密配方根本不在湯裡，而是和外婆一起坐在那裡、吹著熱騰騰的麵、感到無比自在的回憶。"}],
"If I had one million dollars, I would...": [
 {"en": "If I had one million dollars, I would not buy a sports car or a big house. Money like that is a tool, and I want to use it carefully.",
  "zh": "如果我有一百萬美元，我不會買跑車或大房子。這樣的錢是一種工具，我想謹慎地使用它。"},
 {"en": "First, I would give half of it to my parents so they could retire earlier. They have worked hard for more than twenty years, and I want them to rest while they are still healthy. Second, I would use thirty percent for my own education, perhaps studying abroad for two years. Knowledge stays with me forever, and no one can take it away.",
  "zh": "首先，我會把一半給父母，讓他們可以提早退休。他們辛勤工作了二十多年，我希望他們趁身體還健康時好好休息。其次，我會把百分之三十用在自己的教育上，也許出國留學兩年。知識會永遠跟著我，誰也拿不走。"},
 {"en": "With the last twenty percent, I would start a small library in my neighborhood, full of comfortable chairs and good books, free for everyone. A million dollars can disappear quickly, but a place that helps children fall in love with reading could change lives for fifty years. That, I think, is the best deal money can buy.",
  "zh": "最後的百分之二十，我會在社區開一間小圖書館，擺滿舒適的椅子和好書，免費開放給所有人。一百萬可能很快就花完，但一個讓孩子愛上閱讀的地方，能改變人們五十年的人生。我想，這是金錢能買到最划算的交易。"}],
"How technology changes our daily life.": [
 {"en": "Technology has quietly rewritten almost every hour of our day. We wake up to phone alarms instead of roosters, order lunch with two taps, and talk face to face with friends who live on the other side of the planet.",
  "zh": "科技悄悄改寫了我們一天中的幾乎每個小時。我們被手機鬧鐘而非公雞叫醒，點兩下就能訂午餐，還能和住在地球另一端的朋友面對面交談。"},
 {"en": "The benefits are real. Information that once took a week to find now takes seconds. My grandmother video-calls her sister in Canada every night, something impossible in her youth. However, the costs are real too. Many of us check our phones a hundred times a day, and quiet moments for thinking have become rare. We are more connected to the world, yet sometimes less connected to the people sitting beside us.",
  "zh": "好處是真實的。過去要花一週才找得到的資訊，現在幾秒鐘就有。我的奶奶每晚和在加拿大的妹妹視訊，這在她年輕時是不可能的事。然而，代價也是真實的。許多人一天看手機上百次，安靜思考的時刻變得稀有。我們與世界更緊密相連，卻有時和身旁的人更疏遠。"},
 {"en": "Technology itself is neither good nor bad; it simply makes everything faster and easier, including our bad habits. The real question is not what technology can do, but what we choose to do with it. The smartest device in the room should still be the human being holding it.",
  "zh": "科技本身無所謂好壞；它只是讓一切更快、更容易——包括我們的壞習慣。真正的問題不是科技能做什麼，而是我們選擇用它做什麼。房間裡最聰明的裝置，應該仍是拿著它的那個人。"}],
"The advantages and disadvantages of working from home.": [
 {"en": "Working from home has become common since the pandemic, and people still argue about whether it is a blessing or a trap.",
  "zh": "自疫情以來，在家工作變得普遍，但人們仍在爭論它究竟是福音還是陷阱。"},
 {"en": "The advantages are easy to see. Workers save hours of commuting time, wear comfortable clothes, and arrange their day with more freedom. Parents can pick up their children from school, and lunch comes from their own kitchen instead of an expensive shop. On the other hand, the disadvantages appear slowly. The border between work and rest disappears, and some people find themselves answering emails at midnight. Teamwork becomes harder, new employees learn more slowly without office conversations, and loneliness can quietly grow.",
  "zh": "優點顯而易見。工作者省下數小時通勤時間、穿著舒適的衣服、更自由地安排一天。父母可以接孩子放學，午餐來自自家廚房而非昂貴的店家。另一方面，缺點是慢慢浮現的。工作與休息的界線消失，有些人發現自己半夜還在回信。團隊合作變得困難，新進員工少了辦公室的交流學得更慢，孤獨感也可能悄悄滋長。"},
 {"en": "In my view, the best answer is balance. A few days at home for focused work, and a few days in the office for meetings and friendship, seem to combine the strengths of both worlds. The future of work is probably not a place at all, but a schedule we design wisely.",
  "zh": "在我看來，最好的答案是平衡。幾天在家專注工作，幾天進辦公室開會、維繫情誼，似乎能結合兩個世界的優點。工作的未來也許根本不是一個地點，而是一張我們聰明設計的時間表。"}],
"An unforgettable experience in my life.": [
 {"en": "The most unforgettable experience of my life happened on a school hiking trip two years ago. Halfway up the mountain, dark clouds rolled in, and rain poured down without warning.",
  "zh": "我人生中最難忘的經歷，發生在兩年前的學校登山活動。爬到半山腰時，烏雲湧來，大雨毫無預警地傾盆而下。"},
 {"en": "Our group hurried into a small wooden shelter. We were cold, wet, and a little scared. Then our teacher did something unexpected: she started to sing. One by one, we joined her. For an hour, the rain hit the roof like drums while twenty shivering students sang every song we knew. When the sky finally cleared, a double rainbow stretched across the valley, and we walked down the mountain with our wet shoes and loud laughter.",
  "zh": "我們一群人趕緊躲進一間小木屋。大家又冷又濕，還有點害怕。這時老師做了一件出乎意料的事：她開始唱歌。我們一個接一個加入。整整一小時，雨點像鼓聲般打在屋頂上，二十個發抖的學生唱遍了所有會唱的歌。天空終於放晴時，一道雙彩虹橫跨山谷，我們踩著濕透的鞋、帶著響亮的笑聲走下山。"},
 {"en": "I have forgotten many sunny days, but I will never forget that storm. It taught me that the best moments in life are often hiding inside the worst ones, waiting for someone brave enough to start singing.",
  "zh": "許多晴天我都忘了，但那場暴風雨我永遠不會忘。它教會我：人生最美好的時刻常常藏在最糟的時刻裡，等著一個夠勇敢、願意先開口唱歌的人。"}],
"My goals for the next five years.": [
 {"en": "People say that a goal without a plan is only a wish, so I have divided my next five years into three clear steps.",
  "zh": "人們說，沒有計畫的目標只是願望，所以我把未來五年分成三個明確的階段。"},
 {"en": "In the first two years, my goal is to improve my English until I can speak it with confidence. I will study one hour every day and take a speaking test every six months to measure my progress. In the following two years, I want to develop a professional skill, learning design software and building small projects of my own. In the final year, I plan to combine both abilities to find a job that connects me with the wider world, and to save enough money for my first trip abroad.",
  "zh": "頭兩年，我的目標是把英文練到能自信開口。我會每天讀一小時，每半年參加一次口說測驗來檢視進度。接下來兩年，我想培養一項專業技能，學習設計軟體並做出自己的小作品。最後一年，我計畫結合這兩項能力，找到一份能連結更廣大世界的工作，並存夠錢完成第一次出國旅行。"},
 {"en": "Five years sounds long, but it is only about 1,800 days. If I waste ten minutes, it seems like nothing; if I use ten minutes well every day, it becomes three hundred hours. My plan is simple: make time my friend, not my enemy.",
  "zh": "五年聽起來很長，其實只有約一千八百天。浪費十分鐘看似沒什麼；但每天善用十分鐘，就是三百個小時。我的計畫很簡單：讓時間成為我的朋友，而不是敵人。"}],
}

# ------------------------------------------------------------ 批閱資料 ----
FUNCTION_WORDS = set("""a an the i you he she it we they me him her us them my your his its our their mine yours
this that these those who whom whose which what when where why how and or but so because if although while until
unless than then also too very really quite just only even still yet never always often sometimes usually again
not no nor is are was were am be been being do does did done have has had having will would shall should can could
may might must need dare to of in on at by for with about against between into through during before after above
below from up down out off over under once here there all any both each few more most other some such as same
one two three four five six seven eight nine ten eleven twelve twenty thirty forty fifty hundred thousand million
first second third monday tuesday wednesday thursday friday saturday sunday january february march april may june
july august september october november december mr mrs ms dr ok okay yes no oh wow hello hi bye goodbye
went gone saw seen ate eaten got gotten took taken came come made knew known wrote written read said told thought
bought brought taught caught felt kept left met paid sat set stood found heard held lost meant sent spent won
children men women feet teeth mice people isn't aren't wasn't weren't don't doesn't didn't won't wouldn't can't
couldn't shouldn't mustn't haven't hasn't hadn't i'm i've i'll i'd you're you've we're they're he's she's it's
that's there's let's cannot gonna wanna e.g i.e etc""".split())

IRREG_PAST = "went|saw|ate|did|had|made|got|took|came|wrote|knew|bought|thought|felt|found|heard|said|told|kept|left|met|paid|sat|stood|spoke|broke|chose|drove|fell|flew|forgot|gave|grew|ran|sang|slept|swam|threw|woke|wore|won"

GRAMMAR_RULES = [
 (r"\ba\s+(?=[aeiouAEIOU])(?!(one|uni|use|user|usu|eu)\w*)\w+", "「a」後接母音開頭的字 → 通常應改用「an」"),
 (r"\ban\s+(?![aeiouAEIOU]|hour|honest|honor|heir)\w+", "「an」後接子音開頭的字 → 通常應改用「a」"),
 (r"\b[Hh]e (don't|have|do|are|were|go|like|want|say|think)\b", "he 是第三人稱單數 → 動詞要加 s（如 doesn't/has/goes）"),
 (r"\b[Ss]he (don't|have|do|are|were|go|like|want|say|think)\b", "she 是第三人稱單數 → 動詞要加 s（如 doesn't/has/goes）"),
 (r"\b[Ii]t (don't|have|do|are|were)\b", "it 是第三人稱單數 → 動詞要加 s（如 doesn't/has）"),
 (r"\bI (is|has|does|are)\b", "I 後面的 be 動詞/助動詞用 am/have/do"),
 (r"\b(We|You|They|we|you|they) (is|was|has|does)\b", "複數主詞後動詞不加 s（用 are/were/have/do）"),
 (r"\b(the|a|an|to|in|of|and|is|are|was|it|that|for|with|on) \1\b", "重複的字（如 the the）"),
 (r"\balot\b", "alot → 應拆成兩個字「a lot」"),
 (r"\bmore (better|worse|bigger|smaller|easier|harder|faster|slower|happier)\b", "比較級不能加 more（better 本身已是比較級）"),
 (rf"\b(didn't|doesn't|don't) ({IRREG_PAST})\b", "didn't/doesn't/don't 後面要接原形動詞"),
 (rf"\bto ({IRREG_PAST})\b", "to 後面要接原形動詞（不定詞）"),
 (r",(?=[A-Za-z])", "逗號後面要空一格"),
 (r"\s+,", "逗號前面不要空格"),
 (r"\b(everyone|everybody|someone|somebody|nobody) (are|were|have)\b", "everyone/somebody 等視為單數 → 用 is/was/has"),
 (r"\bpeoples\b", "people 已是複數，不加 s"),
 (r"\bvery like\b", "very like → 應說 like ... very much 或 really like"),
 (r"\bmore easy\b", "more easy → easier"),
 (r"\bfunner\b", "funner → more fun"),
]


def _tokens(text):
    return re.findall(r"[A-Za-z']+", text)


def _norm(w):
    w = w.lower().strip("'")
    for suf in ("'s", "s'", "n't", "'re", "'ve", "'ll", "'d", "'m"):
        if w.endswith(suf):
            w = w[: -len(suf)]
    return w


def _stem_candidates(w):
    out = {w}
    for suf in ("s", "es", "ed", "d", "ing", "er", "est", "ly"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            base = w[: -len(suf)]
            out.add(base)
            out.add(base + "e")
            if len(base) >= 2 and base[-1] == base[-2]:
                out.add(base[:-1])  # running -> run
    if w.endswith("ies"):
        out.add(w[:-3] + "y")
    return out


def review_essay(text, wordbank):
    """回傳批閱報告文字。"""
    known = set(FUNCTION_WORDS)
    level_of = {}
    for lv, words in wordbank.items():
        for w in words:
            lw = w["word"].lower()
            known.add(lw)
            level_of.setdefault(lw, lv)

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    paras = [p for p in text.split("\n") if p.strip()]
    toks = _tokens(text)
    n = len(toks)
    uniq = {_norm(t) for t in toks}
    ttr = len(uniq) / n if n else 0
    lens = [len(_tokens(s)) for s in sentences] or [0]
    avg_len = sum(lens) / len(lens)

    lv_count = {"初級": 0, "中級": 0, "進階": 0}
    adv_used = []
    for t in set(_norm(x) for x in toks):
        for c in _stem_candidates(t):
            if c in level_of:
                lv_count[level_of[c]] += 1
                if level_of[c] == "進階":
                    adv_used.append(c)
                break

    suspects = []
    for t in toks:
        if t[0].isupper():
            continue
        nt = _norm(t)
        if len(nt) < 3 or not nt.isalpha():
            continue
        if not (_stem_candidates(nt) & known):
            if nt not in suspects:
                suspects.append(nt)

    grammar_hits = []
    for pat, msg in GRAMMAR_RULES:
        for m in re.finditer(pat, text):
            frag = m.group(0).strip()
            grammar_hits.append(f"「{frag}」：{msg}")
    for s in sentences:
        if s and s[0].islower():
            grammar_hits.append(f"「{s[:30]}…」：句首字母建議大寫" if len(s) > 30 else f"「{s}」：句首字母建議大寫")
    if re.search(r"\bi\b", text):
        grammar_hits.append("「i」：代名詞 I 一律大寫")
    long_s = [s for s in sentences if len(_tokens(s)) > 32]

    score = 100
    if n < 50: score -= 20
    elif n < 80: score -= 8
    score -= min(30, len(grammar_hits) * 4)
    score -= min(15, len(suspects) * 3)
    score -= min(10, len(long_s) * 3)
    if ttr >= 0.6 and n >= 80: score += 4
    if lv_count["進階"] >= 3: score += 4
    if len(paras) >= 3: score += 2
    score = max(30, min(100, score))
    grade = ("A+" if score >= 95 else "A" if score >= 88 else "B+" if score >= 80
             else "B" if score >= 70 else "C+" if score >= 60 else "C")

    L = []
    L.append("═" * 46)
    L.append(f"  🧑‍🏫 批閱報告　　總分：{score} 分（{grade}）")
    L.append("═" * 46)
    L.append("")
    L.append("📊 基本統計")
    L.append(f"　字數 {n}｜句數 {len(sentences)}｜段落 {len(paras)}｜平均句長 {avg_len:.1f} 字")
    L.append(f"　詞彙多樣性 {ttr:.0%}（不重複字 / 總字數，60% 以上佳）")
    L.append("")
    L.append("📚 詞彙分析")
    L.append(f"　初級字 {lv_count['初級']}｜中級字 {lv_count['中級']}｜進階字 {lv_count['進階']}")
    if adv_used:
        L.append(f"　👍 用到進階詞彙：{', '.join(sorted(adv_used)[:12])}")
    else:
        L.append("　💡 建議：試著加入 2-3 個中/進階單字，讓文章更有深度")
    L.append("")
    L.append("🔍 拼字疑慮" + ("（字庫中查不到，請確認）" if suspects else ""))
    L.append("　" + (", ".join(suspects[:12]) if suspects else "沒有發現 ✔"))
    L.append("")
    L.append(f"✏️ 文法與格式建議（{len(grammar_hits)} 項）")
    if grammar_hits:
        for g in grammar_hits[:15]:
            L.append("　• " + g)
        if len(grammar_hits) > 15:
            L.append(f"　…另有 {len(grammar_hits) - 15} 項")
    else:
        L.append("　沒有發現常見錯誤 ✔")
    if long_s:
        L.append(f"　• 有 {len(long_s)} 句超過 32 字，建議拆成兩句")
    L.append("")
    L.append("🏆 總評")
    if score >= 88:
        L.append("　結構完整、錯誤很少，繼續保持！下一步可挑戰更長的論說文。")
    elif score >= 70:
        L.append("　整體不錯！先修正上面的文法建議，再多用幾個進階單字，分數會明顯提升。")
    else:
        L.append("　別灰心，寫作是練出來的。建議先修正文法項目、把文章寫到 80 字以上，再批閱一次。")
    return "\n".join(L)


# ------------------------------------------------------------ 掛載 ----
def attach(app, nb):
    import main as M

    bar = ttk.Frame(app.tab_write)
    bar.pack(fill="x", padx=10, pady=(0, 8))
    tk.Label(bar, text="AI 助手：", font=("Microsoft JhengHei UI", 10, "bold"),
             fg="#1a5fb4").pack(side="left")

    def current_prompt():
        t = app.write_prompt_lbl.cget("text")
        for p in MODEL_ESSAYS:
            if p in t:
                return p
        return None

    def gen_essay():
        p = current_prompt()
        if p is None:
            p = random.choice(list(MODEL_ESSAYS))
            app.write_prompt_lbl.config(text="題目：" + p)
        paras = MODEL_ESSAYS[p]
        essay_en = "\n\n".join(x["en"] for x in paras)

        win = tk.Toplevel(app)
        win.title("📄 範文參考（英中對照）")
        win.geometry("760x580")
        tk.Label(win, text=p, font=("Segoe UI", 13, "bold"), fg="#1a5fb4",
                 wraplength=720, justify="left").pack(anchor="w", padx=12, pady=(10, 4))

        st = scrolledtext.ScrolledText(win, font=("Segoe UI", 12), wrap="word")
        st.tag_configure("en", font=("Segoe UI", 12), spacing1=6)
        st.tag_configure("zh", font=("Microsoft JhengHei UI", 11), foreground="#1a5fb4", spacing3=10)
        st.pack(fill="both", expand=True, padx=12, pady=4)

        show_zh = tk.BooleanVar(value=True)

        def render():
            st.configure(state="normal")
            st.delete("1.0", "end")
            for x in paras:
                st.insert("end", x["en"] + "\n", "en")
                if show_zh.get():
                    st.insert("end", x["zh"] + "\n", "zh")
                st.insert("end", "\n")
            st.configure(state="disabled")

        render()

        fr = ttk.Frame(win)
        fr.pack(pady=8)
        ttk.Checkbutton(fr, text="顯示繁中翻譯", variable=show_zh,
                        command=render).pack(side="left", padx=6)
        ttk.Button(fr, text="🔊 朗讀範文", command=lambda: M.speak(essay_en)).pack(side="left", padx=4)
        ttk.Button(fr, text="🐢 慢速朗讀", command=lambda: M.speak(essay_en, -3)).pack(side="left", padx=4)
        ttk.Button(fr, text="⏹ 停止", command=M.stop_speaking).pack(side="left", padx=4)

        def apply_to_editor():
            if app.write_text.get("1.0", "end").strip():
                if not messagebox.askyesno("確認", "編輯器已有內容，要覆蓋成範文（純英文）嗎？", parent=win):
                    return
            app.write_text.delete("1.0", "end")
            app.write_text.insert("1.0", essay_en)
            app.write_count()
            win.destroy()

        ttk.Button(fr, text="⬇ 套用到編輯器", command=apply_to_editor).pack(side="left", padx=4)
        tk.Label(win, text="提示：先讀英文段落，再看中文對照確認理解。照抄學不到東西——讀完後用自己的話重寫一遍最有效。",
                 font=("Microsoft JhengHei UI", 9), fg="#888", wraplength=720).pack(pady=(0, 8))

    def review():
        text = app.write_text.get("1.0", "end").strip()
        if not text:
            messagebox.showinfo("提示", "請先在編輯器寫一些內容再批閱")
            return
        report = review_essay(text, app.wordbank)

        win = tk.Toplevel(app)
        win.title("🧑‍🏫 批閱報告")
        win.geometry("680x560")
        st = scrolledtext.ScrolledText(win, font=("Microsoft JhengHei UI", 11), wrap="word")
        st.insert("1.0", report)
        st.configure(state="disabled")
        st.pack(fill="both", expand=True, padx=10, pady=8)

        def save_report():
            os.makedirs(ESSAY_DIR, exist_ok=True)
            name = datetime.datetime.now().strftime("review_%Y%m%d_%H%M%S.txt")
            path = os.path.join(ESSAY_DIR, name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(app.write_prompt_lbl.cget("text") + "\n" + "=" * 40 + "\n"
                        + text + "\n\n" + report + "\n")
            messagebox.showinfo("已儲存", f"作文與批閱報告已儲存至：\n{path}", parent=win)

        ttk.Button(win, text="💾 儲存作文＋報告", command=save_report).pack(pady=(0, 10))

    ttk.Button(bar, text="📄 一鍵生成範文", command=gen_essay).pack(side="left", padx=4)
    ttk.Button(bar, text="🧑‍🏫 批閱文章", command=review).pack(side="left", padx=4)
    tk.Label(bar, text="（生成範文＝依目前題目給一篇英中對照參考作文；批閱＝評分＋詞彙／拼字／文法建議）",
             font=("Microsoft JhengHei UI", 9), fg="#888").pack(side="left", padx=6)
