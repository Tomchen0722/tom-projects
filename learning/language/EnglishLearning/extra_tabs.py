# -*- coding: utf-8 -*-
"""擴充分頁：🧠 圖像記憶（emoji 聯想 + 音節拆解 + 聯想筆記）、👄 嘴型發音（KK 母音/子音圖解）。
由 main.py 於啟動時呼叫 attach(app, notebook) 掛載。"""
import json
import os
import random
import re
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MNEMO_FILE = os.path.join(BASE_DIR, "mnemonics.json")
MEMORY_FILE = os.path.join(BASE_DIR, "memory_progress.json")

FONT = ("Microsoft JhengHei UI", 11)

# ---------------------------------------------------------- Emoji 圖像庫 ----
EMOJI_MAP = {
"apple":"🍎","banana":"🍌","orange":"🍊","grape":"🍇","lemon":"🍋","peach":"🍑","strawberry":"🍓","watermelon":"🍉","cherry":"🍒","pineapple":"🍍",
"bread":"🍞","cake":"🎂","cookie":"🍪","candy":"🍬","chocolate":"🍫","egg":"🥚","cheese":"🧀","hamburger":"🍔","pizza":"🍕","noodle":"🍜",
"rice":"🍚","soup":"🍲","salad":"🥗","sandwich":"🥪","ice":"🧊","milk":"🥛","coffee":"☕","tea":"🍵","juice":"🧃","water":"💧",
"fish":"🐟","chicken":"🐔","beef":"🥩","pork":"🥓","meat":"🍖","vegetable":"🥦","potato":"🥔","tomato":"🍅","corn":"🌽","carrot":"🥕",
"dog":"🐶","cat":"🐱","bird":"🐦","horse":"🐴","cow":"🐮","pig":"🐷","sheep":"🐑","goat":"🐐","rabbit":"🐰","mouse":"🐭",
"lion":"🦁","tiger":"🐯","bear":"🐻","elephant":"🐘","monkey":"🐵","panda":"🐼","fox":"🦊","wolf":"🐺","deer":"🦌","snake":"🐍",
"frog":"🐸","turtle":"🐢","whale":"🐳","dolphin":"🐬","shark":"🦈","octopus":"🐙","bee":"🐝","ant":"🐜","butterfly":"🦋","spider":"🕷",
"duck":"🦆","eagle":"🦅","owl":"🦉","penguin":"🐧","chick":"🐤","dragon":"🐉","dinosaur":"🦖","camel":"🐫","zebra":"🦓","giraffe":"🦒",
"sun":"☀️","moon":"🌙","star":"⭐","cloud":"☁️","rain":"🌧","snow":"❄️","wind":"🌬","storm":"⛈","rainbow":"🌈","lightning":"⚡",
"fire":"🔥","mountain":"⛰","river":"🏞","sea":"🌊","ocean":"🌊","beach":"🏖","island":"🏝","forest":"🌲","tree":"🌳","flower":"🌸",
"grass":"🌱","leaf":"🍃","rose":"🌹","earth":"🌍","world":"🌍","sky":"🌌","desert":"🏜","volcano":"🌋","wave":"🌊","stone":"🪨",
"house":"🏠","home":"🏠","school":"🏫","hospital":"🏥","bank":"🏦","hotel":"🏨","church":"⛪","factory":"🏭","office":"🏢","store":"🏪",
"shop":"🛍","market":"🛒","restaurant":"🍽","library":"📚","museum":"🏛","castle":"🏰","tower":"🗼","bridge":"🌉","road":"🛣","building":"🏢",
"city":"🏙","farm":"🚜","garden":"🏡","park":"🌳","zoo":"🦁","station":"🚉","airport":"✈️","temple":"🏯","stadium":"🏟","prison":"🔒",
"car":"🚗","bus":"🚌","train":"🚆","plane":"✈️","airplane":"✈️","ship":"🚢","boat":"⛵","bicycle":"🚲","bike":"🚲","motorcycle":"🏍",
"taxi":"🚕","truck":"🚚","subway":"🚇","rocket":"🚀","helicopter":"🚁","ambulance":"🚑","wheel":"🛞","engine":"⚙️","traffic":"🚦","ticket":"🎫",
"book":"📖","pen":"🖊","pencil":"✏️","paper":"📄","letter":"✉️","envelope":"✉️","notebook":"📓","map":"🗺","newspaper":"📰","magazine":"📰",
"computer":"💻","phone":"📱","telephone":"☎️","television":"📺","radio":"📻","camera":"📷","clock":"🕐","watch":"⌚","calendar":"📅","battery":"🔋",
"key":"🔑","lock":"🔒","door":"🚪","window":"🪟","bed":"🛏","chair":"🪑","table":"🪑","desk":"🖥","lamp":"💡","light":"💡",
"mirror":"🪞","umbrella":"☂️","bag":"👜","box":"📦","gift":"🎁","present":"🎁","bottle":"🍾","cup":"🥤","glass":"🥛","plate":"🍽",
"knife":"🔪","spoon":"🥄","fork":"🍴","scissors":"✂️","hammer":"🔨","tool":"🛠","brush":"🖌","soap":"🧼","towel":"🧻","broom":"🧹",
"money":"💰","dollar":"💵","coin":"🪙","gold":"🥇","diamond":"💎","ring":"💍","crown":"👑","medal":"🏅","trophy":"🏆","flag":"🚩",
"heart":"❤️","smile":"😊","laugh":"😂","cry":"😢","angry":"😠","happy":"😄","sad":"😢","love":"❤️","kiss":"💋","sleep":"😴",
"eye":"👁","ear":"👂","nose":"👃","mouth":"👄","hand":"✋","foot":"🦶","leg":"🦵","arm":"💪","finger":"👆","tooth":"🦷",
"hair":"💇","face":"🙂","head":"🗣","brain":"🧠","bone":"🦴","blood":"🩸","muscle":"💪","body":"🧍","skin":"🖐","tongue":"👅",
"baby":"👶","boy":"👦","girl":"👧","man":"👨","woman":"👩","father":"👨","mother":"👩","family":"👨‍👩‍👧","friend":"🤝","people":"👥",
"king":"🤴","queen":"👸","doctor":"🧑‍⚕️","nurse":"🧑‍⚕️","teacher":"🧑‍🏫","student":"🧑‍🎓","police":"👮","farmer":"🧑‍🌾","cook":"🧑‍🍳","chef":"🧑‍🍳",
"soldier":"💂","worker":"👷","artist":"🧑‍🎨","singer":"🎤","dancer":"💃","pilot":"🧑‍✈️","judge":"🧑‍⚖️","scientist":"🧑‍🔬","engineer":"🧑‍💻","waiter":"🧑‍🍳",
"run":"🏃","walk":"🚶","swim":"🏊","dance":"💃","sing":"🎤","jump":"🤸","climb":"🧗","ride":"🚴","drive":"🚗","fly":"🛫",
"eat":"🍽","drink":"🥤","cook":"🍳","read":"📖","write":"✍️","draw":"🎨","paint":"🎨","play":"🎮","work":"💼","study":"📚",
"listen":"👂","speak":"🗣","talk":"💬","see":"👀","look":"👀","watch":"👀","think":"🤔","dream":"💭","laugh":"😆","shout":"📢",
"buy":"🛒","sell":"🏷","pay":"💳","give":"🎁","win":"🏆","lose":"😞","fight":"🥊","kick":"🦵","throw":"🤾","catch":"🧤",
"open":"📂","close":"📁","cut":"✂️","wash":"🧼","clean":"🧹","build":"🏗","break":"💥","fix":"🔧","push":"👐","pull":"🪢",
"music":"🎵","song":"🎶","guitar":"🎸","piano":"🎹","drum":"🥁","violin":"🎻","movie":"🎬","film":"🎞","game":"🎮","toy":"🧸",
"ball":"⚽","football":"⚽","basketball":"🏀","baseball":"⚾","tennis":"🎾","golf":"⛳","boxing":"🥊","ski":"🎿","skate":"⛸","surf":"🏄",
"art":"🎨","photo":"📸","picture":"🖼","dance":"💃","party":"🎉","festival":"🎊","holiday":"🏖","travel":"🧳","camp":"🏕","picnic":"🧺",
"time":"⏰","morning":"🌅","night":"🌃","evening":"🌆","noon":"🕛","spring":"🌸","summer":"☀️","autumn":"🍂","fall":"🍂","winter":"⛄",
"today":"📅","tomorrow":"➡️","yesterday":"⬅️","week":"🗓","month":"📆","year":"🎊","hour":"🕐","minute":"⏱","second":"⏲","birthday":"🎂",
"hot":"🥵","cold":"🥶","warm":"🌤","cool":"😎","big":"🐘","small":"🐜","fast":"⚡","slow":"🐌","new":"✨","old":"🏚",
"good":"👍","bad":"👎","strong":"💪","weak":"🥀","tall":"🦒","short":"🐜","heavy":"🏋","rich":"💰","poor":"🪙","beautiful":"🌺",
"dark":"🌑","bright":"💡","clean":"✨","dirty":"🧹","empty":"🕳","full":"🈵","quiet":"🤫","loud":"📢","safe":"🛡","dangerous":"⚠️",
"fire":"🔥","smoke":"💨","bomb":"💣","gun":"🔫","war":"⚔️","peace":"🕊","danger":"⚠️","death":"💀","ghost":"👻","magic":"🪄",
"science":"🔬","math":"🔢","number":"🔢","history":"📜","language":"🗣","english":"🇬🇧","test":"📝","exam":"📝","question":"❓","answer":"✅",
"idea":"💡","plan":"📋","goal":"🎯","target":"🎯","success":"🏆","dream":"🌠","future":"🔮","secret":"🤐","news":"📰","message":"💬",
"email":"📧","internet":"🌐","robot":"🤖","machine":"⚙️","energy":"⚡","electricity":"⚡","medicine":"💊","hospital":"🏥","virus":"🦠","health":"🩺",
"star":"⭐","space":"🚀","planet":"🪐","alien":"👽","angel":"👼","seed":"🌰","egg":"🥚","nest":"🪺","web":"🕸","hole":"🕳",
"queue":"🧍‍🧍","line":"📏","circle":"⭕","square":"⬜","triangle":"🔺","arrow":"➡️","cross":"❌","check":"✅","zero":"0️⃣","hundred":"💯",
}

# ------------------------------------------------------------ KK 音標資料 ----
# shape: open 開口度0-1, round 圓唇0-1, spread 嘴角展開0-1
# tongue: high-front/mid-front/low-front/central/high-back/mid-back/low-back/curl/tip-up/tip-between/back-up/none
# closed: 雙唇緊閉, lipteeth: 上齒觸下唇, nasal: 鼻音
VOWELS = [
("i","長母音","see / tea / need","嘴角用力向兩側展開像微笑，開口很小，舌位高而前。發長音「一—」。",{"open":0.15,"round":0,"spread":1.0,"tongue":"high-front"}),
("ɪ","短母音","sit / big / ship","比 /i/ 放鬆，嘴角略展，開口稍大，短促輕快。",{"open":0.3,"round":0,"spread":0.6,"tongue":"high-front"}),
("e","雙母音","day / name / rain","從 /e/ 滑向 /ɪ/：先開口中等、嘴角展開，再慢慢合小。",{"open":0.45,"round":0,"spread":0.7,"tongue":"mid-front"}),
("ɛ","短母音","bed / head / pen","開口中等，嘴角微展，舌位中前，短音「ㄝ」。",{"open":0.5,"round":0,"spread":0.5,"tongue":"mid-front"}),
("æ","短母音","cat / apple / bad","嘴巴上下張大、嘴角同時向外展，像咬大蘋果，舌位低前。",{"open":0.8,"round":0,"spread":0.8,"tongue":"low-front"}),
("ɑ","長母音","hot / father / car","嘴巴張到最大，舌頭放低放平靠後，從喉嚨發「啊—」。",{"open":1.0,"round":0.1,"spread":0.2,"tongue":"low-back"}),
("ɔ","長母音","law / dog / ball","嘴唇略收圓並微向前突出，開口中大，「ㄛ—」。",{"open":0.65,"round":0.6,"spread":0,"tongue":"mid-back"}),
("o","雙母音","go / home / boat","從 /o/ 滑向 /ʊ/：嘴唇收圓，開口由中變小。",{"open":0.5,"round":0.8,"spread":0,"tongue":"mid-back"}),
("ʊ","短母音","book / good / put","嘴唇放鬆微圓，開口小，短促，不用力。",{"open":0.3,"round":0.5,"spread":0,"tongue":"high-back"}),
("u","長母音","food / blue / school","嘴唇用力收圓向前突出成小孔，像吹口哨，「屋—」。",{"open":0.2,"round":1.0,"spread":0,"tongue":"high-back"}),
("ʌ","短母音","cup / love / bus","嘴巴自然半開、完全放鬆，舌位中央，短音「ㄚ」。",{"open":0.5,"round":0,"spread":0.2,"tongue":"central"}),
("ə","輕母音","about / ago / sofa","全英文最放鬆的音：嘴微開，輕輕一帶而過（非重音）。",{"open":0.3,"round":0,"spread":0.1,"tongue":"central"}),
("ɚ","捲舌音","teacher / doctor","輕音 /ə/ 加捲舌：嘴微開，舌尖向上向後捲，不碰上顎。",{"open":0.3,"round":0.2,"spread":0,"tongue":"curl"}),
("ɝ","捲舌音","bird / work / learn","重音捲舌：嘴微開略圓，舌中部隆起、舌尖上捲，「ㄦ—」。",{"open":0.35,"round":0.3,"spread":0,"tongue":"curl"}),
("aɪ","雙母音","time / my / eye","從大開口 /a/ 滑到 /ɪ/：下巴由張大到快閉上，「愛」。",{"open":0.9,"round":0,"spread":0.4,"tongue":"low-front"}),
("aʊ","雙母音","house / now / cow","從 /a/ 滑向圓唇 /ʊ/：先張大再收圓，「凹」。",{"open":0.9,"round":0.3,"spread":0.1,"tongue":"low-back"}),
("ɔɪ","雙母音","boy / coin / toy","從圓唇 /ɔ/ 滑向 /ɪ/：先圓後展，「ㄛ一」。",{"open":0.6,"round":0.6,"spread":0.2,"tongue":"mid-back"}),
]
CONSONANTS = [
("p","無聲","pen / apple / map","雙唇緊閉憋氣，突然放開爆出氣流。聲帶不振動、送氣強。",{"open":0,"round":0,"spread":0.2,"closed":True}),
("b","有聲","book / baby / job","嘴型同 /p/：雙唇緊閉再爆開，但聲帶振動、不送氣。",{"open":0,"round":0,"spread":0.2,"closed":True}),
("t","無聲","ten / water / cat","舌尖抵住上齒齦，憋氣後彈開，送氣。聲帶不振動。",{"open":0.35,"round":0,"spread":0.3,"tongue":"tip-up","teeth":True}),
("d","有聲","dog / daddy / red","嘴型同 /t/：舌尖彈上齒齦，聲帶振動。",{"open":0.35,"round":0,"spread":0.3,"tongue":"tip-up","teeth":True}),
("k","無聲","cat / key / book","舌後部抵住軟顎（喉嚨上方）憋氣後彈開，送氣。",{"open":0.45,"round":0,"spread":0.2,"tongue":"back-up"}),
("g","有聲","go / big / game","嘴型同 /k/：舌後彈軟顎，聲帶振動。",{"open":0.45,"round":0,"spread":0.2,"tongue":"back-up"}),
("f","無聲","fish / phone / life","上排牙齒輕咬下嘴唇，氣流從縫隙摩擦而出。",{"open":0.25,"round":0,"spread":0.2,"lipteeth":True}),
("v","有聲","very / love / five","嘴型同 /f/：上齒觸下唇，加上聲帶振動（嘴唇會麻麻的）。",{"open":0.25,"round":0,"spread":0.2,"lipteeth":True}),
("θ","無聲","think / three / mouth","舌尖輕輕放在上下齒之間，向外吹氣。中文沒有這個音！",{"open":0.3,"round":0,"spread":0.3,"tongue":"tip-between","teeth":True}),
("ð","有聲","this / mother / that","嘴型同 /θ/：舌尖在齒間，聲帶振動。",{"open":0.3,"round":0,"spread":0.3,"tongue":"tip-between","teeth":True}),
("s","無聲","sun / bus / class","舌尖靠近上齒齦（不碰到），氣流從細縫擠出「嘶」。",{"open":0.2,"round":0,"spread":0.5,"teeth":True,"tongue":"tip-up"}),
("z","有聲","zoo / easy / nose","嘴型同 /s/：加聲帶振動，像蜜蜂「嗡嗡」。",{"open":0.2,"round":0,"spread":0.5,"teeth":True,"tongue":"tip-up"}),
("ʃ","無聲","she / fish / shop","嘴唇略圓向前突，舌面抬近硬顎，發「噓—」。",{"open":0.3,"round":0.7,"spread":0,"tongue":"mid-front"}),
("ʒ","有聲","measure / vision","嘴型同 /ʃ/：加聲帶振動。",{"open":0.3,"round":0.7,"spread":0,"tongue":"mid-front"}),
("tʃ","無聲","chair / teacher / watch","/t/+/ʃ/ 連發：嘴唇略圓，舌尖先抵齒齦再摩擦，「去」。",{"open":0.3,"round":0.6,"spread":0,"tongue":"tip-up"}),
("dʒ","有聲","job / age / juice","嘴型同 /tʃ/：加聲帶振動，「舉」。",{"open":0.3,"round":0.6,"spread":0,"tongue":"tip-up"}),
("m","鼻音","man / home / summer","雙唇閉合，氣流改從鼻子出來，發出哼鳴「嗯」。",{"open":0,"round":0,"spread":0.2,"closed":True,"nasal":True}),
("n","鼻音","no / sun / dinner","嘴微開，舌尖抵上齒齦，氣流從鼻子出。",{"open":0.3,"round":0,"spread":0.2,"tongue":"tip-up","nasal":True}),
("ŋ","鼻音","sing / long / king","嘴微開，舌後部抵軟顎，鼻音「ㄥ」。舌尖不動！",{"open":0.4,"round":0,"spread":0.2,"tongue":"back-up","nasal":True}),
("l","邊音","love / ball / yellow","舌尖抵上齒齦，氣流從舌頭兩側流出。字尾時舌尖也要抵住。",{"open":0.4,"round":0,"spread":0.2,"tongue":"tip-up"}),
("r","捲舌","red / car / sorry","舌尖向後捲起、不碰任何地方，嘴唇微圓前突。",{"open":0.35,"round":0.5,"spread":0,"tongue":"curl"}),
("j","半母音","yes / year / yellow","舌面靠近硬顎後快速滑開，像很快的「一」。",{"open":0.25,"round":0,"spread":0.7,"tongue":"high-front"}),
("w","半母音","we / water / away","嘴唇用力收圓突出，再快速滑開，像很快的「屋」。",{"open":0.2,"round":1.0,"spread":0,"tongue":"high-back"}),
("h","無聲","hat / hello / who","嘴型跟著後面的母音，輕輕呵氣即可，不要摩擦喉嚨。",{"open":0.5,"round":0,"spread":0.2}),
]

VOWEL_RE = re.compile(r"[aeiouy]+", re.I)


def split_syllables(word):
    """粗略音節拆解：以母音群為核心切塊。"""
    parts, last = [], 0
    ms = list(VOWEL_RE.finditer(word))
    if not ms:
        return [word]
    for i, m in enumerate(ms):
        end = m.end() if i < len(ms) - 1 else len(word)
        if i < len(ms) - 1:
            nxt = ms[i + 1].start()
            end = (m.end() + nxt + 1) // 2
        parts.append(word[last:end])
        last = end
    if last < len(word):
        parts[-1] += word[last:]
    return [p for p in parts if p]


def _load(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
    except Exception:
        pass


# ------------------------------------------------------------ 嘴型繪圖 ----
def draw_mouth(cv, shape):
    cv.delete("all")
    W, H = int(cv["width"]), int(cv["height"])
    cx, cy = W // 2, H // 2 + 10
    # 臉
    cv.create_oval(cx - 130, cy - 120, cx + 130, cy + 120, fill="#ffe0c2", outline="#e0b090", width=2)
    # 鼻子
    cv.create_line(cx, cy - 60, cx - 8, cy - 30, cx + 8, cy - 30, fill="#d0a080", width=2, smooth=True)
    op = shape.get("open", 0.3)
    rd = shape.get("round", 0)
    sp = shape.get("spread", 0.3)
    closed = shape.get("closed", False)
    mw = int(40 + sp * 55 - rd * 30)      # 嘴半寬
    mh = 4 if closed else int(6 + op * 46)  # 嘴半高
    my = cy + 45
    if closed:
        cv.create_line(cx - mw, my, cx + mw, my, fill="#c0392b", width=7, capstyle="round")
        cv.create_line(cx - mw, my - 8, cx + mw, my - 8, fill="#e8a0a0", width=3)
    else:
        # 外唇
        cv.create_oval(cx - mw - 8, my - mh - 8, cx + mw + 8, my + mh + 8, fill="#c0392b", outline="#a93226")
        # 口腔
        cv.create_oval(cx - mw, my - mh, cx + mw, my + mh, fill="#5a1a1a", outline="")
        # 牙齒
        if shape.get("teeth") or op < 0.45:
            cv.create_rectangle(cx - mw + 6, my - mh, cx + mw - 6, my - mh + max(6, int(mh * 0.35)),
                                fill="white", outline="#ddd")
        if shape.get("lipteeth"):
            cv.create_rectangle(cx - mw + 6, my - mh, cx + mw - 6, my + 2, fill="white", outline="#ddd")
            cv.create_line(cx - mw - 4, my + mh - 2, cx + mw + 4, my + mh - 2, fill="#e8836f", width=6)
        # 舌頭
        t = shape.get("tongue", "")
        tf = "#e8836f"
        if t == "tip-between":
            cv.create_oval(cx - 16, my - 8, cx + 16, my + mh + 4, fill=tf, outline="#d06050")
        elif t == "tip-up":
            cv.create_polygon(cx - 20, my + mh - 4, cx + 6, my - mh + int(mh * 0.5), cx + 22, my + mh - 4,
                              fill=tf, outline="#d06050", smooth=True)
        elif t == "curl":
            cv.create_arc(cx - 24, my - mh + 4, cx + 24, my + mh + 10, start=200, extent=200,
                          style="arc", outline=tf, width=9)
        elif t == "back-up":
            cv.create_arc(cx - 10, my - mh - 4, cx + mw + 10, my + mh, start=90, extent=120,
                          style="arc", outline=tf, width=9)
        elif t in ("high-front", "mid-front", "low-front", "central", "high-back", "mid-back", "low-back"):
            ty = {"hig": -int(mh * 0.4), "mid": 0, "low": int(mh * 0.4), "cen": 0}[t.split("-")[0][:3]]
            tx = {"front": -int(mw * 0.3), "back": int(mw * 0.3), "central": 0}.get(t.split("-")[-1], 0)
            cv.create_oval(cx + tx - 18, my + ty - 6, cx + tx + 18, my + ty + 12, fill=tf, outline="#d06050")
    # 鼻音氣流箭頭
    if shape.get("nasal"):
        cv.create_line(cx + 20, cy - 35, cx + 48, cy - 78, fill="#3584e4", width=3, arrow="last")
        cv.create_text(cx + 78, cy - 88, text="氣流→鼻", font=("Microsoft JhengHei UI", 10), fill="#3584e4")
    else:
        cv.create_line(cx, my, cx + 55, my + 48, fill="#3584e4", width=3, arrow="last")
        cv.create_text(cx + 80, my + 62, text="氣流→口", font=("Microsoft JhengHei UI", 10), fill="#3584e4")


# ------------------------------------------------------------ 掛載入口 ----
def attach(app, nb):
    import main as M  # 使用 main.py 的 speak / stop_speaking

    # ================= 🧠 圖像記憶 =================
    tab_mem = ttk.Frame(nb)
    nb.add(tab_mem, text=" 🧠 圖像記憶 ")

    mnemo = _load(MNEMO_FILE)
    mem = _load(MEMORY_FILE)
    state = {"word": None}

    top = ttk.Frame(tab_mem)
    top.pack(pady=8)
    ttk.Label(top, text="程度：").pack(side="left")
    mem_level = tk.StringVar(value="全部")
    ttk.Combobox(top, textvariable=mem_level, state="readonly",
                 values=["全部"] + app.levels, width=8, font=FONT).pack(side="left", padx=4)
    only_hard = tk.BooleanVar(value=False)
    ttk.Checkbutton(top, text="只複習「再複習」的字", variable=only_hard).pack(side="left", padx=8)

    card = tk.Frame(tab_mem, bg="white", highlightbackground="#c8c8c8", highlightthickness=1)
    card.pack(pady=6, ipadx=30, ipady=8)
    emoji_lbl = tk.Label(card, text="🧠", font=("Segoe UI Emoji", 64), bg="white")
    emoji_lbl.pack(pady=(14, 0))
    syl_txt = tk.Text(card, height=1, font=("Segoe UI", 30, "bold"), bd=0, bg="white",
                      width=22)
    syl_txt.tag_configure("c0", foreground="#1a5fb4")
    syl_txt.tag_configure("c1", foreground="#e66100")
    syl_txt.tag_configure("c2", foreground="#26a269")
    syl_txt.tag_configure("c3", foreground="#a51d2d")
    syl_txt.tag_configure("center", justify="center")
    syl_txt.configure(state="disabled")
    syl_txt.pack()
    ipa_lbl = tk.Label(card, text="", font=("Segoe UI", 14), fg="#666", bg="white")
    ipa_lbl.pack()
    zh_lbl = tk.Label(card, text="", font=("Microsoft JhengHei UI", 14), bg="white",
                      wraplength=460, justify="center")
    zh_lbl.pack(pady=4)
    ex_lbl = tk.Label(card, text="", font=("Microsoft JhengHei UI", 10), fg="#555", bg="white",
                      wraplength=460, justify="left")
    ex_lbl.pack(pady=(0, 10))

    note_fr = ttk.Frame(tab_mem)
    note_fr.pack(pady=4)
    ttk.Label(note_fr, text="我的聯想筆記：").pack(side="left")
    note_var = tk.StringVar()
    note_entry = ttk.Entry(note_fr, textvariable=note_var, font=FONT, width=42)
    note_entry.pack(side="left", padx=4)

    fb_lbl = tk.Label(tab_mem, text="", font=FONT, fg="#26a269")
    fb_lbl.pack()

    def save_note():
        w = state["word"]
        if not w:
            return
        txt = note_var.get().strip()
        if txt:
            mnemo[w["word"]] = txt
        else:
            mnemo.pop(w["word"], None)
        _save(MNEMO_FILE, mnemo)
        fb_lbl.config(text="✅ 筆記已儲存")

    ttk.Button(note_fr, text="💾 存筆記", command=save_note).pack(side="left")

    revealed = tk.BooleanVar(value=False)

    def show_card(w):
        state["word"] = w
        revealed.set(False)
        emoji_lbl.config(text=EMOJI_MAP.get(w["word"].lower(), "💭"))
        syl = split_syllables(w["word"])
        syl_txt.configure(state="normal")
        syl_txt.delete("1.0", "end")
        for i, s in enumerate(syl):
            syl_txt.insert("end", s, (f"c{i % 4}",))
            if i < len(syl) - 1:
                syl_txt.insert("end", "·", ("c3",))
        syl_txt.tag_add("center", "1.0", "end")
        syl_txt.configure(state="disabled")
        ipa_lbl.config(text=w["ipa"])
        zh_lbl.config(text="❓ 想一想圖像和音節，按「顯示意思」")
        ex_lbl.config(text="")
        note_var.set(mnemo.get(w["word"], ""))
        fb_lbl.config(text="")
        M.speak(w["word"])

    def reveal():
        w = state["word"]
        if not w:
            return
        revealed.set(True)
        zh_lbl.config(text=w["zh"])
        if w.get("examples"):
            ex = w["examples"][0]
            ex_lbl.config(text=f'{ex["en"]}\n{ex["zh"]}')

    def pick_next():
        lv = mem_level.get()
        pool = [w for _, w in app.all_words(None if lv == "全部" else lv)]
        if only_hard.get():
            hard = {k for k, v in mem.items() if v.get("again", 0) > v.get("ok", 0)}
            pool = [w for w in pool if w["word"] in hard] or pool
        if pool:
            show_card(random.choice(pool))

    def mark(kind):
        w = state["word"]
        if not w:
            return
        rec = mem.setdefault(w["word"], {"ok": 0, "again": 0})
        rec[kind] += 1
        _save(MEMORY_FILE, mem)
        pick_next()

    btns = ttk.Frame(tab_mem)
    btns.pack(pady=8)
    ttk.Button(btns, text="🎲 下一張", command=pick_next).pack(side="left", padx=4)
    ttk.Button(btns, text="🔊 發音", command=lambda: state["word"] and M.speak(state["word"]["word"])).pack(side="left", padx=4)
    ttk.Button(btns, text="👁 顯示意思", command=reveal).pack(side="left", padx=4)
    ttk.Button(btns, text="✅ 記住了", command=lambda: mark("ok")).pack(side="left", padx=12)
    ttk.Button(btns, text="🔁 再複習", command=lambda: mark("again")).pack(side="left", padx=4)

    tk.Label(tab_mem, text="圖像記憶法：先看圖像 emoji 與彩色音節，在腦中想像畫面、唸出聲音，再對答案。\n"
                           "把你的聯想寫進筆記（例如 apple → 「阿婆(a-pple)咬蘋果」），下次看到會自動帶出。",
             font=("Microsoft JhengHei UI", 9), fg="#888", justify="left").pack(side="bottom", pady=6)

    # ================= 👄 嘴型發音 =================
    tab_ph = ttk.Frame(nb)
    nb.add(tab_ph, text=" 👄 嘴型發音 ")

    left = ttk.Frame(tab_ph)
    left.pack(side="left", fill="y", padx=8, pady=8)
    ttk.Label(left, text="KK 音標（點選查看嘴型）", font=("Microsoft JhengHei UI", 11, "bold")).pack(anchor="w")
    ph_list = tk.Listbox(left, font=("Segoe UI", 13), width=24, height=26)
    ph_list.pack(fill="y", expand=True, pady=4)

    items = []
    ph_list.insert("end", "── 母音 Vowels ──")
    items.append(None)
    for v in VOWELS:
        ph_list.insert("end", f" /{v[0]}/　{v[1]}")
        items.append(v)
    ph_list.insert("end", "── 子音 Consonants ──")
    items.append(None)
    for c in CONSONANTS:
        ph_list.insert("end", f" /{c[0]}/　{c[1]}")
        items.append(c)

    right = ttk.Frame(tab_ph)
    right.pack(side="left", fill="both", expand=True, padx=8, pady=8)
    ph_sym = tk.Label(right, text="請從左側選擇音標", font=("Segoe UI", 30, "bold"), fg="#1a5fb4")
    ph_sym.pack(anchor="w")
    cv = tk.Canvas(right, width=320, height=280, bg="white", highlightbackground="#ccc")
    cv.pack(anchor="w", pady=4)
    ph_desc = tk.Label(right, text="", font=("Microsoft JhengHei UI", 12), wraplength=520,
                       justify="left")
    ph_desc.pack(anchor="w", pady=6)
    ex_fr = ttk.Frame(right)
    ex_fr.pack(anchor="w", pady=4)

    def on_ph_select(_e=None):
        sel = ph_list.curselection()
        if not sel or items[sel[0]] is None:
            return
        sym, kind, exs, desc, shape = items[sel[0]]
        ph_sym.config(text=f"/{sym}/　{kind}")
        draw_mouth(cv, shape)
        ph_desc.config(text="嘴型要領：" + desc)
        for c in ex_fr.winfo_children():
            c.destroy()
        ttk.Label(ex_fr, text="示範單字：", font=FONT).pack(side="left")
        for w in exs.split(" / "):
            b = ttk.Button(ex_fr, text=f"🔊 {w}", command=lambda t=w: M.speak(t))
            b.pack(side="left", padx=3)
        ttk.Button(ex_fr, text="🐢 慢速全部",
                   command=lambda t=exs.replace(" / ", ", "): M.speak(t, -4)).pack(side="left", padx=8)

    ph_list.bind("<<ListboxSelect>>", on_ph_select)
    tk.Label(right, text="提示：紅色=嘴唇、白色=牙齒、粉紅=舌頭位置、藍色箭頭=氣流方向。\n"
                         "「無聲」= 聲帶不振動（手摸喉嚨沒感覺）；「有聲」= 聲帶振動。",
             font=("Microsoft JhengHei UI", 9), fg="#888", justify="left").pack(side="bottom", anchor="w", pady=6)
