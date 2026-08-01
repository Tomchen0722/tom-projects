# -*- coding: utf-8 -*-
"""🧭 提示寫作分頁：題目 + 中文段落大綱 + 句型開頭 + 建議單字，一步步引導完成英文作文。
由 main.py 於啟動時呼叫 attach(app, notebook) 掛載。"""
import datetime
import os
import random
import re
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESSAY_DIR = os.path.join(BASE_DIR, "essays")

FONT = ("Microsoft JhengHei UI", 11)

TOPICS = [
{"level":"初級","title":"My Best Friend","title_zh":"我最好的朋友","outline":[
 "第1段：他/她是誰？長什麼樣子？你們怎麼認識的？",
 "第2段：他/她的個性如何？你們常一起做什麼？",
 "第3段：為什麼他/她對你很重要？"],
 "starters":["My best friend is...","We met when...","He/She always...","We like to ... together.","I am lucky to have..."],
 "words":["kind","funny","helpful","honest","share","together","special","smile"]},
{"level":"初級","title":"My Favorite Food","title_zh":"我最喜歡的食物","outline":[
 "第1段：你最喜歡的食物是什麼？第一次吃是什麼時候？",
 "第2段：它的味道、外觀？在哪裡吃得到？",
 "第3段：為什麼它對你特別？"],
 "starters":["My favorite food is...","I first tried it when...","It tastes...","Every time I eat it, I..."],
 "words":["delicious","sweet","spicy","smell","taste","restaurant","cook","enjoy"]},
{"level":"初級","title":"A Happy Day","title_zh":"快樂的一天","outline":[
 "第1段：那是哪一天？和誰在一起？",
 "第2段：發生了什麼事？（按時間順序寫 2-3 件事）",
 "第3段：你的心情如何？為什麼難忘？"],
 "starters":["Last ..., I ...","In the morning, we...","After that, ...","At the end of the day, ...","I will never forget..."],
 "words":["excited","laugh","surprise","wonderful","remember","weather","favorite","fun"]},
{"level":"初級","title":"My Family","title_zh":"我的家庭","outline":[
 "第1段：你家有幾個人？分別是誰？",
 "第2段：介紹 2-3 位家人（工作、個性、喜好）",
 "第3段：你們常一起做什麼？你愛你的家嗎？"],
 "starters":["There are ... people in my family.","My father/mother is...","On weekends, we usually...","I love my family because..."],
 "words":["parents","brother","sister","work","cook","dinner","weekend","love"]},
{"level":"初級","title":"My Dream Job","title_zh":"我的夢想職業","outline":[
 "第1段：你的夢想職業是什麼？何時開始有這個夢想？",
 "第2段：為什麼喜歡？需要什麼能力？",
 "第3段：你現在可以怎麼準備？"],
 "starters":["When I grow up, I want to be...","I started to dream about this when...","To be a good ..., I need to...","From now on, I will..."],
 "words":["dream","future","study","practice","help","important","hope","work hard"]},
{"level":"初級","title":"My School Life","title_zh":"我的學校生活","outline":[
 "第1段：你的學校是什麼樣子？你幾點到校？",
 "第2段：你最喜歡的科目和老師？",
 "第3段：下課或放學後做什麼？"],
 "starters":["My school is...","My favorite subject is...","After class, my friends and I...","School life is ... because..."],
 "words":["subject","teacher","classmate","playground","library","interesting","learn","busy"]},
{"level":"中級","title":"A Person I Admire","title_zh":"我敬佩的人","outline":[
 "第1段：這個人是誰？（家人/名人/老師都可以）用一句話說出你敬佩他的原因",
 "第2段：舉 1-2 個具體事例，說明他做了什麼",
 "第3段：他如何影響你？你想學習他哪一點？"],
 "starters":["The person I admire most is...","What impresses me most is that...","For example, once he/she...","Because of him/her, I have learned to..."],
 "words":["admire","respect","brave","determined","influence","example","give up","achieve"]},
{"level":"中級","title":"The Importance of Exercise","title_zh":"運動的重要性","outline":[
 "第1段：現代人普遍缺乏運動的現象",
 "第2段：運動的 2-3 個好處（身體、心情、社交）",
 "第3段：給讀者的建議（從小習慣開始）"],
 "starters":["Nowadays, many people...","First of all, exercise can...","In addition, ...","Therefore, I suggest that..."],
 "words":["healthy","energy","reduce stress","regular","habit","benefit","suggest","at least"]},
{"level":"中級","title":"An Unforgettable Trip","title_zh":"難忘的旅行","outline":[
 "第1段：何時？去哪裡？和誰？為什麼去？",
 "第2段：旅程中最深刻的 1-2 個時刻（用細節描寫：看到、聽到、吃到什麼）",
 "第3段：這趟旅行帶給你什麼改變或體悟？"],
 "starters":["Last ..., I took a trip to...","The most unforgettable moment was when...","I still remember the smell/sound/taste of...","This trip taught me that..."],
 "words":["scenery","local","experience","culture","memory","explore","amazing","broaden"]},
{"level":"中級","title":"My Way of Learning English","title_zh":"我的英文學習方法","outline":[
 "第1段：你學英文多久了？遇過什麼困難？",
 "第2段：你用什麼方法？（聽歌/看影片/背單字/找語伴…舉 2-3 個）哪個最有效？",
 "第3段：給其他學習者的建議"],
 "starters":["I have been learning English for...","At first, I found ... difficult.","My favorite way to learn is...","If you also want to improve, ..."],
 "words":["vocabulary","practice","improve","fluent","confidence","mistake","progress","keep on"]},
{"level":"中級","title":"Living with a Smartphone","title_zh":"與智慧型手機共處","outline":[
 "第1段：手機在你生活中扮演什麼角色？一天用多久？",
 "第2段：好處與壞處各舉 1-2 個（用自己的經驗當例子）",
 "第3段：你如何找到平衡？"],
 "starters":["My smartphone is...","On one hand, it helps me...","On the other hand, I sometimes...","To find a balance, I have decided to..."],
 "words":["convenient","addicted","screen time","distract","connect","balance","control","turn off"]},
{"level":"進階","title":"Should Students Have Part-time Jobs?","title_zh":"學生該打工嗎？","outline":[
 "第1段：點出議題與正反立場的存在，表明你的立場",
 "第2段：支持你立場的 2 個論點（附例子或推理）",
 "第3段：承認對方觀點有其道理，但說明為何你的立場更站得住腳，總結"],
 "starters":["Whether students should ... has long been debated.","In my opinion, ...","First, ... For instance, ...","Admittedly, ... However, ...","In conclusion, ..."],
 "words":["independence","responsibility","time management","academic","income","experience","priority","outweigh"]},
{"level":"進階","title":"Technology and Human Connection","title_zh":"科技與人際連結","outline":[
 "第1段：描述一個場景：餐桌上每個人都在滑手機。提出問題：科技拉近還是疏遠了我們？",
 "第2段：科技拉近距離的例子 vs. 疏遠的例子",
 "第3段：你的結論：問題不在科技本身，而在使用方式" ],
 "starters":["Picture this: a family sits at dinner, ...","There is no doubt that technology allows us to...","Yet at the same time, ...","Ultimately, the question is not whether..., but how..."],
 "words":["genuine","interaction","isolated","virtual","face-to-face","meaningful","presence","intentionally"]},
{"level":"進階","title":"A Problem in My City and How to Solve It","title_zh":"我的城市的一個問題與解方","outline":[
 "第1段：具體描述問題（交通/垃圾/房價/噪音…）與它造成的影響",
 "第2段：分析原因（至少 2 個層面）",
 "第3段：提出可行的解決方案（政府/社區/個人各能做什麼）"],
 "starters":["Anyone who lives in ... has experienced...","The root causes are not hard to find.","One practical solution would be...","Change will not happen overnight, but..."],
 "words":["infrastructure","policy","residents","invest","awareness","implement","gradually","cooperation"]},
{"level":"進階","title":"What Success Means to Me","title_zh":"成功對我的意義","outline":[
 "第1段：社會通常如何定義成功（金錢/地位）？你是否認同？",
 "第2段：你自己的定義，用一個人物或親身經歷佐證",
 "第3段：這個定義如何影響你的選擇與生活方式？"],
 "starters":["Society often measures success by...","To me, however, success means...","I once met/read about someone who...","With this definition in mind, I choose to..."],
 "words":["definition","wealth","fulfillment","pursue","values","sacrifice","content","in the long run"]},
{"level":"進階","title":"Learning from Failure","title_zh":"從失敗中學習","outline":[
 "第1段：人人都怕失敗，但失敗真的只是壞事嗎？",
 "第2段：描述你的一次失敗經驗：發生什麼、當下感受",
 "第3段：你從中學到什麼？它如何改變你後來的行動？"],
 "starters":["Nobody enjoys failing, yet...","I learned this lesson the hard way when...","At that moment, I felt...","Looking back, that failure taught me..."],
 "words":["setback","disappointed","reflect","resilience","adjust","opportunity","growth","perspective"]},
]


def attach(app, nb):
    import main as M

    tab = ttk.Frame(nb)
    nb.add(tab, text=" 🧭 提示寫作 ")

    state = {"topic": None}

    left = ttk.Frame(tab)
    left.pack(side="left", fill="y", padx=8, pady=8)
    ttk.Label(left, text="題目（依程度）", font=("Microsoft JhengHei UI", 11, "bold")).pack(anchor="w")
    lb = tk.Listbox(left, font=FONT, width=34, height=18)
    lb.pack(fill="y", expand=True, pady=4)
    for t in TOPICS:
        lb.insert("end", f'[{t["level"]}] {t["title_zh"]}')
    ttk.Button(left, text="🎲 隨機題目", command=lambda: pick_random()).pack(fill="x")

    right = ttk.Frame(tab)
    right.pack(side="left", fill="both", expand=True, padx=8, pady=8)

    title_lbl = tk.Label(right, text="請從左側選擇題目", font=("Segoe UI", 16, "bold"), fg="#1a5fb4")
    title_lbl.pack(anchor="w")

    guide = tk.Text(right, height=7, font=("Microsoft JhengHei UI", 10), wrap="word",
                    bg="#f6f8fa", relief="flat", padx=8, pady=6)
    guide.configure(state="disabled")
    guide.pack(fill="x", pady=4)

    helper = ttk.Frame(right)
    helper.pack(fill="x")
    ttk.Label(helper, text="句型（點擊插入）：", font=("Microsoft JhengHei UI", 9)).pack(anchor="w")
    starter_fr = ttk.Frame(helper)
    starter_fr.pack(fill="x")
    ttk.Label(helper, text="建議單字（點擊插入、右鍵發音）：", font=("Microsoft JhengHei UI", 9)).pack(anchor="w")
    words_fr = ttk.Frame(helper)
    words_fr.pack(fill="x")

    editor = scrolledtext.ScrolledText(right, font=("Segoe UI", 12), wrap="word", height=10, undo=True)
    editor.pack(fill="both", expand=True, pady=4)

    bottom = ttk.Frame(right)
    bottom.pack(fill="x")
    count_lbl = tk.Label(bottom, text="字數：0", font=FONT)
    count_lbl.pack(side="left")
    fb = tk.Label(right, text="", font=("Microsoft JhengHei UI", 10), justify="left",
                  wraplength=640, fg="#555")
    fb.pack(fill="x", pady=(2, 6))

    def refresh_count(_e=None):
        count_lbl.config(text=f"字數：{len(editor.get('1.0', 'end').split())}")

    editor.bind("<KeyRelease>", refresh_count)

    def insert_text(txt):
        editor.insert("insert", txt + " ")
        editor.focus_set()
        refresh_count()

    def show_topic(t):
        state["topic"] = t
        title_lbl.config(text=f'{t["title"]}　{t["title_zh"]}　（{t["level"]}）')
        guide.configure(state="normal")
        guide.delete("1.0", "end")
        guide.insert("end", "📋 段落大綱提示：\n" + "\n".join("  " + o for o in t["outline"]))
        guide.configure(state="disabled")
        for c in starter_fr.winfo_children():
            c.destroy()
        for s in t["starters"]:
            b = tk.Button(starter_fr, text=s, font=("Segoe UI", 9), relief="groove",
                          command=lambda x=s: insert_text(x))
            b.pack(side="left", padx=2, pady=2)
        for c in words_fr.winfo_children():
            c.destroy()
        for w in t["words"]:
            b = tk.Button(words_fr, text=w, font=("Segoe UI", 9), fg="#1a5fb4", relief="groove",
                          command=lambda x=w: insert_text(x))
            b.bind("<Button-3>", lambda e, x=w: M.speak(x))
            b.pack(side="left", padx=2, pady=2)
        fb.config(text="")

    def on_select(_e=None):
        sel = lb.curselection()
        if sel:
            show_topic(TOPICS[sel[0]])

    def pick_random():
        i = random.randrange(len(TOPICS))
        lb.selection_clear(0, "end")
        lb.selection_set(i)
        lb.see(i)
        show_topic(TOPICS[i])

    lb.bind("<<ListboxSelect>>", on_select)

    def check():
        text = editor.get("1.0", "end").strip()
        if not text:
            fb.config(text="尚未輸入內容", fg="#c01c28")
            return
        t = state["topic"]
        issues = []
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        paras = [p for p in text.split("\n") if p.strip()]
        n = len(text.split())
        if t and len(paras) < len(t["outline"]):
            issues.append(f"大綱建議 {len(t['outline'])} 段，目前只有 {len(paras)} 段（用空行分段）")
        if n < 60:
            issues.append(f"目前 {n} 字，建議至少寫 60-120 字")
        for s in sentences:
            if s and s[0].islower():
                issues.append(f"句首建議大寫：「{s[:36]}…」" if len(s) > 36 else f"句首建議大寫：「{s}」")
        if re.search(r"\bi\b", text):
            issues.append("「I」（我）應該大寫")
        used = [w for w in (t["words"] if t else []) if re.search(r"\b" + re.escape(w.split()[0]) + r"\w*\b", text, re.I)]
        tip = f"✔ 已用到建議單字：{', '.join(used)}" if used else "提示：試著用用看上面的建議單字！"
        if issues:
            fb.config(text="檢查結果：\n" + "\n".join("• " + i for i in issues) + "\n" + tip, fg="#c01c28")
        else:
            fb.config(text=f"✅ 結構完整！共 {n} 字、{len(sentences)} 句、{len(paras)} 段。{tip}", fg="#26a269")

    def save():
        text = editor.get("1.0", "end").strip()
        if not text:
            messagebox.showinfo("提示", "尚未輸入內容")
            return
        os.makedirs(ESSAY_DIR, exist_ok=True)
        t = state["topic"]
        name = datetime.datetime.now().strftime("guided_%Y%m%d_%H%M%S.txt")
        path = os.path.join(ESSAY_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write((t["title"] + " " + t["title_zh"] if t else "自由題") + "\n" + "=" * 40 + "\n" + text + "\n")
        messagebox.showinfo("已儲存", f"作文已儲存至：\n{path}")

    ttk.Button(bottom, text="🔎 檢查結構", command=check).pack(side="right", padx=3)
    ttk.Button(bottom, text="🔊 朗讀", command=lambda: editor.get("1.0", "end").strip() and M.speak(editor.get("1.0", "end").strip())).pack(side="right", padx=3)
    ttk.Button(bottom, text="💾 儲存", command=save).pack(side="right", padx=3)
