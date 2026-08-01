# -*- coding: utf-8 -*-
"""
英文學習系統 English Learning System
功能：字庫瀏覽(發音/例句)、文章導讀、單字測驗、聽音練習、發音練習、英文寫作
發音使用 Windows 內建語音 (System.Speech)，免安裝任何套件。
執行：python main.py
"""
import json
import os
import sys
import random
import difflib
import datetime
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDBANK_FILE = os.path.join(BASE_DIR, "wordbank.json")
ARTICLES_FILE = os.path.join(BASE_DIR, "articles.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "progress.json")
ESSAY_DIR = os.path.join(BASE_DIR, "essays")

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

FONT = ("Microsoft JhengHei UI", 11)
FONT_BIG = ("Microsoft JhengHei UI", 20, "bold")
FONT_WORD = ("Segoe UI", 24, "bold")


# ---------------------------------------------------------------- 語音 ----
def _ps_run(script, timeout=30):
    """執行 PowerShell 腳本並回傳 stdout。"""
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
            capture_output=True, text=True, timeout=timeout,
            creationflags=CREATE_NO_WINDOW, encoding="utf-8", errors="replace",
        )
        return (r.stdout or "").strip()
    except Exception:
        return ""


def _ps_quote(text):
    return "'" + text.replace("'", "''") + "'"


_speak_lock = threading.Lock()
_speak_procs = []


def stop_speaking():
    """停止所有進行中的朗讀。"""
    with _speak_lock:
        for p in _speak_procs:
            try:
                p.kill()
            except Exception:
                pass
        _speak_procs.clear()


def speak(text, rate=0, timeout=600):
    """用 Windows 內建 TTS 朗讀英文（背景執行緒，不卡住介面）。rate: -10~10"""
    def _worker():
        script = (
            "Add-Type -AssemblyName System.Speech; "
            "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            "$v = $s.GetInstalledVoices() | Where-Object { $_.VoiceInfo.Culture.Name -like 'en*' } "
            "| Select-Object -First 1; "
            "if ($v) { $s.SelectVoice($v.VoiceInfo.Name) } "
            f"$s.Rate = {int(rate)}; "
            f"$s.Speak({_ps_quote(text)});"
        )
        p = None
        try:
            p = subprocess.Popen(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                creationflags=CREATE_NO_WINDOW)
            with _speak_lock:
                _speak_procs.append(p)
            p.wait(timeout=timeout)
        except Exception:
            pass
        finally:
            with _speak_lock:
                if p is not None and p in _speak_procs:
                    _speak_procs.remove(p)
    threading.Thread(target=_worker, daemon=True).start()


def recognize_speech(timeout_sec=6):
    """用 Windows 內建語音辨識聽麥克風，回傳辨識出的英文文字（失敗回傳 ''）。"""
    script = (
        "Add-Type -AssemblyName System.Speech; "
        "try { "
        "$culture = New-Object System.Globalization.CultureInfo('en-US'); "
        "$rec = New-Object System.Speech.Recognition.SpeechRecognitionEngine($culture); "
        "} catch { "
        "$rec = New-Object System.Speech.Recognition.SpeechRecognitionEngine; "
        "} "
        "$rec.LoadGrammar((New-Object System.Speech.Recognition.DictationGrammar)); "
        "$rec.SetInputToDefaultAudioDevice(); "
        f"$result = $rec.Recognize([TimeSpan]::FromSeconds({int(timeout_sec)})); "
        "if ($result) { Write-Output $result.Text }"
    )
    return _ps_run(script, timeout=timeout_sec + 15)


def similarity(a, b):
    norm = lambda s: " ".join("".join(c.lower() for c in s if c.isalnum() or c.isspace()).split())
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


# ---------------------------------------------------------------- 資料 ----
def load_wordbank():
    with open(WORDBANK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_articles():
    try:
        with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"quiz": {"correct": 0, "total": 0},
            "listening": {"correct": 0, "total": 0},
            "pronunciation": {"good": 0, "total": 0}}


def save_progress(p):
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(p, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ---------------------------------------------------------------- App ----
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("英文學習系統  English Learning System")
        self.geometry("1020x700")
        self.minsize(880, 620)
        try:
            self.wordbank = load_wordbank()
        except Exception as e:
            messagebox.showerror("錯誤", f"無法讀取字庫 wordbank.json：{e}")
            self.destroy()
            return
        self.progress = load_progress()
        self.articles = load_articles()
        self.levels = list(self.wordbank.keys())

        style = ttk.Style(self)
        style.configure("TNotebook.Tab", font=FONT, padding=(14, 6))
        style.configure("TButton", font=FONT)
        style.configure("TLabel", font=FONT)
        style.configure("TRadiobutton", font=FONT)

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=6, pady=6)
        self.tab_bank = ttk.Frame(nb)
        self.tab_read = ttk.Frame(nb)
        self.tab_quiz = ttk.Frame(nb)
        self.tab_listen = ttk.Frame(nb)
        self.tab_pron = ttk.Frame(nb)
        self.tab_write = ttk.Frame(nb)
        nb.add(self.tab_bank, text=" 📖 字庫與例句 ")
        nb.add(self.tab_read, text=" 📚 文章導讀 ")
        nb.add(self.tab_quiz, text=" 📝 單字測驗 ")
        nb.add(self.tab_listen, text=" 🎧 聽音練習 ")
        nb.add(self.tab_pron, text=" 🎤 發音練習 ")
        nb.add(self.tab_write, text=" ✍ 完整寫作 ")

        self.build_bank()
        self.build_read()
        self.build_quiz()
        self.build_listen()
        self.build_pron()
        self.build_write()
        try:
            import extra_tabs
            extra_tabs.attach(self, nb)
        except Exception as _e:
            print('extra_tabs load error:', _e)
        try:
            import writing_plus
            writing_plus.attach(self, nb)
        except Exception as _e:
            print('writing_plus load error:', _e)
        try:
            import essay_tools
            essay_tools.attach(self, nb)
        except Exception as _e:
            print('essay_tools load error:', _e)

        self.status = tk.Label(self, anchor="w", font=("Microsoft JhengHei UI", 9), fg="#555")
        self.status.pack(fill="x", side="bottom")
        self.update_status()

    def update_status(self):
        p = self.progress
        n_words = sum(len(v) for v in self.wordbank.values())
        self.status.config(text=(
            f"  字庫 {n_words} 字、文章 {len(self.articles)} 篇 ─ "
            f"單字測驗 {p['quiz']['correct']}/{p['quiz']['total']}"
            f"　聽音練習 {p['listening']['correct']}/{p['listening']['total']}"
            f"　發音達標 {p['pronunciation']['good']}/{p['pronunciation']['total']}"))

    def all_words(self, level=None):
        if level and level in self.wordbank:
            return [(level, w) for w in self.wordbank[level]]
        out = []
        for lv in self.levels:
            out.extend((lv, w) for w in self.wordbank[lv])
        return out

    # ------------------------------------------------------ 字庫與例句 ----
    def build_bank(self):
        f = self.tab_bank
        left = ttk.Frame(f)
        left.pack(side="left", fill="y", padx=8, pady=8)

        top = ttk.Frame(left)
        top.pack(fill="x")
        ttk.Label(top, text="程度：").pack(side="left")
        self.bank_level = tk.StringVar(value="全部")
        cb = ttk.Combobox(top, textvariable=self.bank_level, state="readonly",
                          values=["全部"] + self.levels, width=8, font=FONT)
        cb.pack(side="left")
        cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_bank_list())

        self.bank_search = tk.StringVar()
        se = ttk.Entry(left, textvariable=self.bank_search, font=FONT)
        se.pack(fill="x", pady=(6, 2))
        self.bank_search.trace_add("write", lambda *a: self.refresh_bank_list())
        ttk.Label(left, text="↑ 搜尋單字或中文", foreground="#888").pack(anchor="w")

        self.bank_list = tk.Listbox(left, font=("Segoe UI", 12), width=26, height=24)
        self.bank_list.pack(fill="both", expand=True, pady=6)
        self.bank_list.bind("<<ListboxSelect>>", self.on_bank_select)

        right = ttk.Frame(f)
        right.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        self.bank_word_lbl = tk.Label(right, text="請從左側選擇單字", font=FONT_WORD, fg="#1a5fb4")
        self.bank_word_lbl.pack(anchor="w")
        self.bank_ipa_lbl = tk.Label(right, text="", font=("Segoe UI", 14), fg="#666")
        self.bank_ipa_lbl.pack(anchor="w")
        self.bank_zh_lbl = tk.Label(right, text="", font=("Microsoft JhengHei UI", 14),
                                    wraplength=600, justify="left")
        self.bank_zh_lbl.pack(anchor="w", pady=(2, 8))

        btns = ttk.Frame(right)
        btns.pack(anchor="w", pady=4)
        ttk.Button(btns, text="🔊 發音", command=self.bank_speak).pack(side="left", padx=2)
        ttk.Button(btns, text="🐢 慢速發音", command=lambda: self.bank_speak(-4)).pack(side="left", padx=2)

        ttk.Label(right, text="例句 Examples", font=("Microsoft JhengHei UI", 12, "bold")).pack(anchor="w", pady=(10, 2))
        self.bank_ex_frame = ttk.Frame(right)
        self.bank_ex_frame.pack(fill="both", expand=True, anchor="w")
        self._bank_items = []
        self.refresh_bank_list()

    def refresh_bank_list(self):
        lv = self.bank_level.get()
        q = self.bank_search.get().strip().lower()
        items = self.all_words(None if lv == "全部" else lv)
        if q:
            items = [(l, w) for l, w in items
                     if q in w["word"].lower() or q in w["zh"]]
        self._bank_items = items
        self.bank_list.delete(0, "end")
        for l, w in items:
            self.bank_list.insert("end", f"{w['word']}  ({l})")

    def on_bank_select(self, _e=None):
        sel = self.bank_list.curselection()
        if not sel:
            return
        _, w = self._bank_items[sel[0]]
        self.bank_current = w
        self.bank_word_lbl.config(text=w["word"])
        self.bank_ipa_lbl.config(text=f'{w["ipa"]}   {w["pos"]}')
        self.bank_zh_lbl.config(text=w["zh"])
        for child in self.bank_ex_frame.winfo_children():
            child.destroy()
        if not w.get("examples"):
            tk.Label(self.bank_ex_frame, text="（此單字暫無例句）", font=FONT,
                     fg="#888").pack(anchor="w")
        for ex in w.get("examples", []):
            row = ttk.Frame(self.bank_ex_frame)
            row.pack(fill="x", anchor="w", pady=3)
            ttk.Button(row, text="🔊", width=3,
                       command=lambda t=ex["en"]: speak(t)).pack(side="left", padx=(0, 6))
            txt = tk.Label(row, text=f'{ex["en"]}\n{ex["zh"]}', font=FONT,
                           justify="left", anchor="w", wraplength=560)
            txt.pack(side="left", anchor="w")

    def bank_speak(self, rate=0):
        w = getattr(self, "bank_current", None)
        if w:
            speak(w["word"], rate)

    # ------------------------------------------------------ 文章導讀 ----
    def build_read(self):
        f = self.tab_read
        left = ttk.Frame(f)
        left.pack(side="left", fill="y", padx=8, pady=8)

        top = ttk.Frame(left)
        top.pack(fill="x")
        ttk.Label(top, text="程度：").pack(side="left")
        self.read_level = tk.StringVar(value="全部")
        cb = ttk.Combobox(top, textvariable=self.read_level, state="readonly",
                          values=["全部"] + self.levels, width=8, font=FONT)
        cb.pack(side="left")
        cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_read_list())

        self.read_search = tk.StringVar()
        _se = ttk.Entry(left, textvariable=self.read_search, font=FONT)
        _se.pack(fill="x", pady=(6, 0))
        self.read_search.trace_add("write", lambda *a: self.refresh_read_list())
        ttk.Label(left, text="↑ 搜尋文章標題", foreground="#888").pack(anchor="w")
        self.read_list = tk.Listbox(left, font=FONT, width=32, height=22)
        self.read_list.pack(fill="both", expand=True, pady=6)
        self.read_list.bind("<<ListboxSelect>>", self.on_read_select)
        ttk.Button(left, text="🎲 隨機一篇", command=self.read_random).pack(fill="x")

        right = ttk.Frame(f)
        right.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        self.read_title_lbl = tk.Label(right, text="請從左側選擇文章",
                                       font=("Segoe UI", 18, "bold"), fg="#1a5fb4",
                                       wraplength=620, justify="left")
        self.read_title_lbl.pack(anchor="w")
        self.read_title_zh_lbl = tk.Label(right, text="", font=("Microsoft JhengHei UI", 12), fg="#666")
        self.read_title_zh_lbl.pack(anchor="w")

        bar = ttk.Frame(right)
        bar.pack(anchor="w", pady=6)
        ttk.Button(bar, text="🔊 朗讀全文", command=lambda: self.read_speak_all(0)).pack(side="left", padx=2)
        ttk.Button(bar, text="🐢 慢速全文", command=lambda: self.read_speak_all(-3)).pack(side="left", padx=2)
        ttk.Button(bar, text="⏹ 停止朗讀", command=stop_speaking).pack(side="left", padx=2)
        self.read_show_zh = tk.BooleanVar(value=True)
        ttk.Checkbutton(bar, text="顯示繁中翻譯", variable=self.read_show_zh,
                        command=self.render_article).pack(side="left", padx=10)

        canvas = tk.Canvas(right, highlightthickness=0)
        sb = ttk.Scrollbar(right, orient="vertical", command=canvas.yview)
        self.read_body = ttk.Frame(canvas)
        self.read_body.bind("<Configure>",
                            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.read_body, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True, pady=4)
        sb.pack(side="right", fill="y")
        self._read_canvas = canvas
        canvas.bind("<Enter>", lambda e: canvas.bind_all(
            "<MouseWheel>", lambda ev: canvas.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        self._read_items = []
        self.read_current = None
        self.refresh_read_list()

    def refresh_read_list(self):
        lv = self.read_level.get()
        items = [a for a in self.articles if lv == "全部" or a.get("level") == lv]
        q = self.read_search.get().strip().lower() if hasattr(self, "read_search") else ""
        if q:
            items = [a for a in items if q in a["title"].lower() or q in a.get("title_zh", "")]
        self._read_items = items
        self.read_list.delete(0, "end")
        for a in items:
            self.read_list.insert("end", f'[{a.get("level", "")}] {a["title"]}')

    def on_read_select(self, _e=None):
        sel = self.read_list.curselection()
        if not sel:
            return
        self.read_current = self._read_items[sel[0]]
        self.render_article()

    def read_random(self):
        if not self._read_items:
            return
        i = random.randrange(len(self._read_items))
        self.read_list.selection_clear(0, "end")
        self.read_list.selection_set(i)
        self.read_list.see(i)
        self.on_read_select()

    def render_article(self):
        a = self.read_current
        if not a:
            return
        self.read_title_lbl.config(text=a["title"])
        self.read_title_zh_lbl.config(text=f'{a.get("title_zh", "")}　（{a.get("level", "")}）')
        for c in self.read_body.winfo_children():
            c.destroy()
        show_zh = self.read_show_zh.get()
        for p in a["paragraphs"]:
            row = ttk.Frame(self.read_body)
            row.pack(fill="x", anchor="w", pady=6)
            btns = ttk.Frame(row)
            btns.pack(side="left", anchor="n", padx=(0, 8))
            ttk.Button(btns, text="🔊", width=3,
                       command=lambda t=p["en"]: (stop_speaking(), speak(t))).pack()
            ttk.Button(btns, text="🐢", width=3,
                       command=lambda t=p["en"]: (stop_speaking(), speak(t, -3))).pack(pady=2)
            col = ttk.Frame(row)
            col.pack(side="left", fill="x", expand=True)
            tk.Label(col, text=p["en"], font=("Segoe UI", 12), wraplength=560,
                     justify="left", anchor="w").pack(anchor="w", fill="x")
            if show_zh:
                tk.Label(col, text=p["zh"], font=("Microsoft JhengHei UI", 11),
                         fg="#1a5fb4", wraplength=560, justify="left",
                         anchor="w").pack(anchor="w", fill="x", pady=(2, 0))

    def read_speak_all(self, rate=0):
        a = self.read_current
        if not a:
            messagebox.showinfo("提示", "請先選擇一篇文章")
            return
        stop_speaking()
        text = a["title"] + ". " + " ".join(p["en"] for p in a["paragraphs"])
        speak(text, rate)

    # ------------------------------------------------------ 單字測驗 ----
    def build_quiz(self):
        f = self.tab_quiz
        top = ttk.Frame(f)
        top.pack(pady=10)
        ttk.Label(top, text="程度：").pack(side="left")
        self.quiz_level = tk.StringVar(value="全部")
        ttk.Combobox(top, textvariable=self.quiz_level, state="readonly",
                     values=["全部"] + self.levels, width=8, font=FONT).pack(side="left", padx=4)
        ttk.Button(top, text="開始 / 下一題", command=self.quiz_next).pack(side="left", padx=10)

        self.quiz_q_lbl = tk.Label(f, text="按「開始」出題：看中文，選出正確的英文單字",
                                   font=FONT_BIG, fg="#1a5fb4", wraplength=900)
        self.quiz_q_lbl.pack(pady=24)
        self.quiz_btn_frame = ttk.Frame(f)
        self.quiz_btn_frame.pack(pady=8)
        self.quiz_fb_lbl = tk.Label(f, text="", font=("Microsoft JhengHei UI", 14))
        self.quiz_fb_lbl.pack(pady=12)
        self.quiz_answer = None

    def quiz_next(self):
        lv = self.quiz_level.get()
        pool = [w for _, w in self.all_words(None if lv == "全部" else lv)]
        if len(pool) < 4:
            messagebox.showinfo("提示", "字庫單字不足 4 個")
            return
        answer = random.choice(pool)
        options = random.sample([w for w in pool if w["word"] != answer["word"]], 3) + [answer]
        random.shuffle(options)
        self.quiz_answer = answer
        zh_short = answer["zh"] if len(answer["zh"]) <= 30 else answer["zh"][:30] + "…"
        self.quiz_q_lbl.config(text=f'「{zh_short}」({answer["pos"]}) 的英文是？')
        self.quiz_fb_lbl.config(text="")
        for c in self.quiz_btn_frame.winfo_children():
            c.destroy()
        for opt in options:
            b = tk.Button(self.quiz_btn_frame, text=opt["word"], font=("Segoe UI", 14),
                          width=18, pady=6,
                          command=lambda o=opt: self.quiz_check(o))
            b.pack(pady=4)

    def quiz_check(self, chosen):
        if not self.quiz_answer:
            return
        ans = self.quiz_answer
        self.progress["quiz"]["total"] += 1
        if chosen["word"] == ans["word"]:
            self.progress["quiz"]["correct"] += 1
            self.quiz_fb_lbl.config(text=f'✅ 答對了！ {ans["word"]} {ans["ipa"]}', fg="#26a269")
        else:
            self.quiz_fb_lbl.config(text=f'❌ 正確答案是 {ans["word"]} {ans["ipa"]}', fg="#c01c28")
        speak(ans["word"])
        save_progress(self.progress)
        self.update_status()
        self.quiz_answer = None

    # ------------------------------------------------------ 聽音練習 ----
    def build_listen(self):
        f = self.tab_listen
        top = ttk.Frame(f)
        top.pack(pady=10)
        ttk.Label(top, text="程度：").pack(side="left")
        self.listen_level = tk.StringVar(value="全部")
        ttk.Combobox(top, textvariable=self.listen_level, state="readonly",
                     values=["全部"] + self.levels, width=8, font=FONT).pack(side="left", padx=4)
        self.listen_mode = tk.StringVar(value="word")
        ttk.Radiobutton(top, text="聽單字", variable=self.listen_mode, value="word").pack(side="left", padx=6)
        ttk.Radiobutton(top, text="聽句子", variable=self.listen_mode, value="sentence").pack(side="left")
        ttk.Button(top, text="出題並播放", command=self.listen_new).pack(side="left", padx=10)

        mid = ttk.Frame(f)
        mid.pack(pady=6)
        ttk.Button(mid, text="🔊 再聽一次", command=self.listen_replay).pack(side="left", padx=4)
        ttk.Button(mid, text="🐢 慢速播放", command=lambda: self.listen_replay(-4)).pack(side="left", padx=4)

        ttk.Label(f, text="請聽發音，輸入你聽到的內容：").pack(pady=(16, 4))
        self.listen_entry = tk.Entry(f, font=("Segoe UI", 16), width=50, justify="center")
        self.listen_entry.pack()
        self.listen_entry.bind("<Return>", lambda e: self.listen_check())
        ttk.Button(f, text="核對答案 (Enter)", command=self.listen_check).pack(pady=10)
        self.listen_fb = tk.Label(f, text="", font=("Microsoft JhengHei UI", 13), justify="left",
                                  wraplength=880)
        self.listen_fb.pack(pady=8)
        self.listen_target = None

    def listen_new(self):
        lv = self.listen_level.get()
        pool = self.all_words(None if lv == "全部" else lv)
        if self.listen_mode.get() == "sentence":
            pool = [(l, w) for l, w in pool if w.get("examples")] or pool
        _, w = random.choice(pool)
        if self.listen_mode.get() == "word" or not w.get("examples"):
            self.listen_target = w["word"]
            self.listen_hint = w["zh"]
        else:
            ex = random.choice(w["examples"])
            self.listen_target = ex["en"]
            self.listen_hint = ex["zh"]
        self.listen_entry.delete(0, "end")
        self.listen_fb.config(text="🎧 播放中… 聽完請輸入", fg="#555")
        speak(self.listen_target)

    def listen_replay(self, rate=0):
        if self.listen_target:
            speak(self.listen_target, rate)

    def listen_check(self):
        if not self.listen_target:
            return
        user = self.listen_entry.get().strip()
        if not user:
            return
        score = similarity(user, self.listen_target)
        self.progress["listening"]["total"] += 1
        if score >= 0.95:
            self.progress["listening"]["correct"] += 1
            self.listen_fb.config(text=f"✅ 完全正確！\n{self.listen_target}\n（{self.listen_hint}）", fg="#26a269")
        elif score >= 0.7:
            self.listen_fb.config(
                text=f"🔶 很接近了（相似度 {score:.0%}）\n正確答案：{self.listen_target}\n（{self.listen_hint}）",
                fg="#e5a50a")
        else:
            self.listen_fb.config(
                text=f"❌ 再加油（相似度 {score:.0%}）\n正確答案：{self.listen_target}\n（{self.listen_hint}）",
                fg="#c01c28")
        save_progress(self.progress)
        self.update_status()
        self.listen_target = None

    # ------------------------------------------------------ 發音練習 ----
    def build_pron(self):
        f = self.tab_pron
        top = ttk.Frame(f)
        top.pack(pady=10)
        ttk.Label(top, text="程度：").pack(side="left")
        self.pron_level = tk.StringVar(value="全部")
        ttk.Combobox(top, textvariable=self.pron_level, state="readonly",
                     values=["全部"] + self.levels, width=8, font=FONT).pack(side="left", padx=4)
        self.pron_mode = tk.StringVar(value="word")
        ttk.Radiobutton(top, text="唸單字", variable=self.pron_mode, value="word").pack(side="left", padx=6)
        ttk.Radiobutton(top, text="唸句子", variable=self.pron_mode, value="sentence").pack(side="left")
        ttk.Button(top, text="出題", command=self.pron_new).pack(side="left", padx=10)

        self.pron_target_lbl = tk.Label(f, text="按「出題」開始發音練習", font=FONT_BIG, fg="#1a5fb4",
                                        wraplength=800, justify="center")
        self.pron_target_lbl.pack(pady=20)
        self.pron_zh_lbl = tk.Label(f, text="", font=FONT, wraplength=800)
        self.pron_zh_lbl.pack()

        btns = ttk.Frame(f)
        btns.pack(pady=14)
        ttk.Button(btns, text="🔊 聽示範", command=self.pron_demo).pack(side="left", padx=4)
        ttk.Button(btns, text="🐢 慢速示範", command=lambda: self.pron_demo(-4)).pack(side="left", padx=4)
        self.pron_rec_btn = ttk.Button(btns, text="🎤 開始錄音辨識", command=self.pron_record)
        self.pron_rec_btn.pack(side="left", padx=12)

        self.pron_fb = tk.Label(f, text="", font=("Microsoft JhengHei UI", 13), justify="left",
                                wraplength=820)
        self.pron_fb.pack(pady=10)
        tk.Label(f, text="說明：按「開始錄音辨識」後，對著麥克風清楚唸出畫面上的內容（約 6 秒）。\n"
                         "使用 Windows 內建語音辨識，第一次使用可能需要在系統設定中啟用麥克風權限。",
                 font=("Microsoft JhengHei UI", 9), fg="#888", justify="left").pack(side="bottom", pady=8)
        self.pron_target = None

    def pron_new(self):
        lv = self.pron_level.get()
        pool = self.all_words(None if lv == "全部" else lv)
        if self.pron_mode.get() == "sentence":
            pool = [(l, w) for l, w in pool if w.get("examples")] or pool
        _, w = random.choice(pool)
        if self.pron_mode.get() == "word" or not w.get("examples"):
            self.pron_target = w["word"]
            self.pron_zh_lbl.config(text=f'{w["ipa"]}　{w["zh"]}')
        else:
            ex = random.choice(w["examples"])
            self.pron_target = ex["en"]
            self.pron_zh_lbl.config(text=ex["zh"])
        self.pron_target_lbl.config(text=self.pron_target)
        self.pron_fb.config(text="")

    def pron_demo(self, rate=0):
        if self.pron_target:
            speak(self.pron_target, rate)

    def pron_record(self):
        if not self.pron_target:
            messagebox.showinfo("提示", "請先按「出題」")
            return
        self.pron_rec_btn.config(state="disabled")
        self.pron_fb.config(text="🎤 錄音辨識中… 請清楚唸出上方內容", fg="#555")

        def _worker():
            heard = recognize_speech(6)
            self.after(0, lambda: self._pron_result(heard))

        threading.Thread(target=_worker, daemon=True).start()

    def _pron_result(self, heard):
        self.pron_rec_btn.config(state="normal")
        if not heard:
            self.pron_fb.config(
                text="⚠ 沒有辨識到聲音。請確認麥克風已連接、音量足夠，並再試一次。\n"
                     "（若持續失敗，請到 Windows 設定 > 時間與語言 > 語音，安裝英文語音辨識）",
                fg="#c01c28")
            return
        score = similarity(heard, self.pron_target)
        self.progress["pronunciation"]["total"] += 1
        if score >= 0.8:
            self.progress["pronunciation"]["good"] += 1
            fb, color = "✅ 發音很棒！", "#26a269"
        elif score >= 0.5:
            fb, color = "🔶 不錯，再多練幾次會更好", "#e5a50a"
        else:
            fb, color = "❌ 差距較大，先聽示範再模仿看看", "#c01c28"
        self.pron_fb.config(
            text=f"{fb}（相似度 {score:.0%}）\n目標：{self.pron_target}\n辨識結果：{heard}", fg=color)
        save_progress(self.progress)
        self.update_status()

    # ------------------------------------------------------ 英文寫作 ----
    WRITING_PROMPTS = [
        "My favorite hobby and why I enjoy it.",
        "Describe your best friend.",
        "A place I want to visit someday.",
        "What did you do last weekend?",
        "The most delicious food I have ever eaten.",
        "If I had one million dollars, I would...",
        "How technology changes our daily life.",
        "The advantages and disadvantages of working from home.",
        "An unforgettable experience in my life.",
        "My goals for the next five years.",
    ]

    def build_write(self):
        f = self.tab_write
        top = ttk.Frame(f)
        top.pack(fill="x", padx=10, pady=8)
        ttk.Button(top, text="🎲 隨機題目", command=self.write_new_prompt).pack(side="left")
        self.write_prompt_lbl = tk.Label(top, text="按「隨機題目」取得寫作主題，或自由書寫",
                                         font=("Microsoft JhengHei UI", 12, "bold"), fg="#1a5fb4")
        self.write_prompt_lbl.pack(side="left", padx=10)

        self.write_text = scrolledtext.ScrolledText(f, font=("Segoe UI", 13), wrap="word",
                                                    height=16, undo=True)
        self.write_text.pack(fill="both", expand=True, padx=10, pady=4)
        self.write_text.bind("<KeyRelease>", lambda e: self.write_count())

        bottom = ttk.Frame(f)
        bottom.pack(fill="x", padx=10, pady=6)
        self.write_count_lbl = tk.Label(bottom, text="字數：0", font=FONT)
        self.write_count_lbl.pack(side="left")
        ttk.Button(bottom, text="🔎 基本檢查", command=self.write_check).pack(side="right", padx=4)
        ttk.Button(bottom, text="🔊 朗讀我的作文", command=self.write_speak).pack(side="right", padx=4)
        ttk.Button(bottom, text="💾 儲存作文", command=self.write_save).pack(side="right", padx=4)

        self.write_fb = tk.Label(f, text="", font=("Microsoft JhengHei UI", 10), justify="left",
                                 anchor="w", fg="#555", wraplength=900)
        self.write_fb.pack(fill="x", padx=10, pady=(0, 8))

    def write_new_prompt(self):
        self.write_prompt_lbl.config(text="題目：" + random.choice(self.WRITING_PROMPTS))

    def write_count(self):
        n = len(self.write_text.get("1.0", "end").split())
        self.write_count_lbl.config(text=f"字數：{n}")

    def write_speak(self):
        text = self.write_text.get("1.0", "end").strip()
        if text:
            speak(text)

    def write_check(self):
        text = self.write_text.get("1.0", "end").strip()
        if not text:
            self.write_fb.config(text="尚未輸入內容")
            return
        issues = []
        import re
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        for s in sentences:
            if s and s[0].islower():
                issues.append(f"句首建議大寫：「{s[:40]}…」" if len(s) > 40 else f"句首建議大寫：「{s}」")
        if sentences and not text.rstrip().endswith((".", "!", "?")):
            issues.append("結尾似乎缺少標點符號（. ! ?）")
        if re.search(r"\bi\b", text):
            issues.append("「I」（我）應該大寫")
        if "  " in text:
            issues.append("有連續兩個空格")
        for wrong, right in [(" alot ", " a lot "), (" dont ", " don't "), (" cant ", " can't "),
                             (" im ", " I'm "), (" its a ", " it's a "), (" wont ", " won't ")]:
            if wrong in " " + text.lower() + " ":
                issues.append(f"可能拼寫問題：{wrong.strip()} → {right.strip()}")
        long_s = [s for s in sentences if len(s.split()) > 30]
        if long_s:
            issues.append(f"有 {len(long_s)} 個句子超過 30 字，建議拆短")
        n = len(text.split())
        if issues:
            self.write_fb.config(text="檢查結果：\n" + "\n".join("• " + i for i in issues), fg="#c01c28")
        else:
            self.write_fb.config(text=f"✅ 基本檢查通過！共 {n} 字、{len(sentences)} 句。繼續保持！", fg="#26a269")

    def write_save(self):
        text = self.write_text.get("1.0", "end").strip()
        if not text:
            messagebox.showinfo("提示", "尚未輸入內容")
            return
        os.makedirs(ESSAY_DIR, exist_ok=True)
        name = datetime.datetime.now().strftime("essay_%Y%m%d_%H%M%S.txt")
        path = os.path.join(ESSAY_DIR, name)
        prompt = self.write_prompt_lbl.cget("text")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(prompt + "\n" + "=" * 40 + "\n" + text + "\n")
        messagebox.showinfo("已儲存", f"作文已儲存至：\n{path}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
