#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
資安自學院 CyberSec Academy
==========================
一個用 Python (Flask) 寫成的資安自學網站。
涵蓋：Linux、CompTIA Network+/Security+/Linux+/CySA+、Cisco CCNA、
      EC-Council CND、EC-Council CEH，從零基礎到企業應用。

啟動方式：
    pip install -r requirements.txt
    python app.py
然後打開瀏覽器 http://127.0.0.1:5000
"""

import json
import os
import re
import copy
from datetime import datetime

from flask import Flask, jsonify, render_template, request, send_from_directory

from content import TRACKS, GLOSSARY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


# ---------------------------------------------------------------------------
# 課程索引（把 content/ 裡的資料整理成快速查詢用的字典）
# ---------------------------------------------------------------------------
CHAPTER_INDEX = {}          # chapter_id -> chapter dict
CHAPTER_TRACK = {}          # chapter_id -> track dict
TERMINAL_DB = {}            # 指令字串 -> 模擬輸出

for _track in TRACKS:
    for _ch in _track["chapters"]:
        CHAPTER_INDEX[_ch["id"]] = _ch
        CHAPTER_TRACK[_ch["id"]] = _track
        for _lab in _ch.get("labs", []):
            for _step in _lab.get("steps", []):
                key = _step["cmd"].strip()
                if key and key not in TERMINAL_DB:
                    TERMINAL_DB[key] = _step.get("output", "")

TOTAL_CHAPTERS = len(CHAPTER_INDEX)
TOTAL_QUIZ = sum(len(c.get("quiz", [])) for c in CHAPTER_INDEX.values())


# ---------------------------------------------------------------------------
# 進度儲存（存成本機 JSON 檔，不需要資料庫）
# ---------------------------------------------------------------------------
DEFAULT_PROGRESS = {
    "read": {},        # chapter_id -> ISO 時間字串
    "quiz": {},        # chapter_id -> {"score": n, "total": n, "at": iso}
    "notes": {},       # chapter_id -> 使用者筆記
    "bookmarks": [],   # chapter_id 清單
    "streak": {"days": []},
}


def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_progress():
    _ensure_data_dir()
    if not os.path.exists(PROGRESS_FILE):
        return copy.deepcopy(DEFAULT_PROGRESS)
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return copy.deepcopy(DEFAULT_PROGRESS)
    merged = copy.deepcopy(DEFAULT_PROGRESS)
    merged.update(data)
    return merged


def save_progress(data):
    _ensure_data_dir()
    tmp = PROGRESS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, PROGRESS_FILE)


def _touch_streak(data):
    today = datetime.now().strftime("%Y-%m-%d")
    days = data.setdefault("streak", {}).setdefault("days", [])
    if today not in days:
        days.append(today)
        data["streak"]["days"] = sorted(days)[-400:]


# ---------------------------------------------------------------------------
# 對外 API
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/curriculum")
def api_curriculum():
    """回傳整份課程大綱（不含測驗答案，避免直接被看光）。"""
    out = []
    for track in TRACKS:
        chapters = []
        for ch in track["chapters"]:
            chapters.append({
                "id": ch["id"],
                "title": ch["title"],
                "subtitle": ch.get("subtitle", ""),
                "level": ch.get("level", "入門"),
                "minutes": ch.get("minutes", 20),
                "summary": ch.get("summary", ""),
                "quizCount": len(ch.get("quiz", [])),
                "labCount": len(ch.get("labs", [])),
                "keywords": ch.get("keywords", []),
            })
        out.append({
            "id": track["id"],
            "title": track["title"],
            "code": track.get("code", ""),
            "tagline": track.get("tagline", ""),
            "stage": track.get("stage", 1),
            "stageName": track.get("stageName", ""),
            "color": track.get("color", "cyan"),
            "goal": track.get("goal", ""),
            "chapters": chapters,
        })
    return jsonify({
        "tracks": out,
        "totals": {"chapters": TOTAL_CHAPTERS, "quiz": TOTAL_QUIZ,
                   "tracks": len(TRACKS)},
    })


@app.route("/api/chapter/<chapter_id>")
def api_chapter(chapter_id):
    ch = CHAPTER_INDEX.get(chapter_id)
    if not ch:
        return jsonify({"error": "找不到這個章節"}), 404
    track = CHAPTER_TRACK[chapter_id]
    payload = copy.deepcopy(ch)
    # 測驗題只送題目與選項，答案留在伺服器端
    payload["quiz"] = [
        {"id": i, "q": q["q"], "options": q["options"]}
        for i, q in enumerate(ch.get("quiz", []))
    ]
    payload["track"] = {"id": track["id"], "title": track["title"],
                        "color": track.get("color", "cyan")}
    ids = [c["id"] for c in track["chapters"]]
    pos = ids.index(chapter_id)
    payload["prev"] = ids[pos - 1] if pos > 0 else None
    payload["next"] = ids[pos + 1] if pos < len(ids) - 1 else None
    return jsonify(payload)


@app.route("/api/quiz/<chapter_id>", methods=["POST"])
def api_quiz(chapter_id):
    ch = CHAPTER_INDEX.get(chapter_id)
    if not ch:
        return jsonify({"error": "找不到這個章節"}), 404
    body = request.get_json(silent=True) or {}
    answers = body.get("answers", {})
    quiz = ch.get("quiz", [])
    results = []
    score = 0
    for i, q in enumerate(quiz):
        picked = answers.get(str(i), answers.get(i))
        correct = (picked == q["answer"])
        if correct:
            score += 1
        results.append({
            "id": i,
            "correct": correct,
            "picked": picked,
            "answer": q["answer"],
            "why": q.get("why", ""),
        })
    data = load_progress()
    prev = data["quiz"].get(chapter_id, {})
    best = max(score, prev.get("best", 0))
    data["quiz"][chapter_id] = {
        "score": score, "total": len(quiz), "best": best,
        "at": datetime.now().isoformat(timespec="seconds"),
    }
    _touch_streak(data)
    save_progress(data)
    return jsonify({"score": score, "total": len(quiz),
                    "best": best, "results": results})


@app.route("/api/progress", methods=["GET", "POST"])
def api_progress():
    data = load_progress()
    if request.method == "POST":
        body = request.get_json(silent=True) or {}
        action = body.get("action")
        cid = body.get("chapterId")
        if action == "read" and cid in CHAPTER_INDEX:
            data["read"][cid] = datetime.now().isoformat(timespec="seconds")
            _touch_streak(data)
        elif action == "unread" and cid in data["read"]:
            data["read"].pop(cid, None)
        elif action == "bookmark" and cid in CHAPTER_INDEX:
            if cid in data["bookmarks"]:
                data["bookmarks"].remove(cid)
            else:
                data["bookmarks"].append(cid)
        elif action == "note" and cid in CHAPTER_INDEX:
            text = (body.get("text") or "").strip()
            if text:
                data["notes"][cid] = text
            else:
                data["notes"].pop(cid, None)
        elif action == "reset":
            data = copy.deepcopy(DEFAULT_PROGRESS)
        save_progress(data)

    read_n = len(data["read"])
    quiz_score = sum(v.get("best", 0) for v in data["quiz"].values())
    per_track = {}
    for track in TRACKS:
        ids = [c["id"] for c in track["chapters"]]
        done = sum(1 for i in ids if i in data["read"])
        per_track[track["id"]] = {"done": done, "total": len(ids)}
    return jsonify({
        "read": data["read"],
        "quiz": data["quiz"],
        "notes": data["notes"],
        "bookmarks": data["bookmarks"],
        "streakDays": len(data.get("streak", {}).get("days", [])),
        "stats": {
            "chaptersDone": read_n,
            "chaptersTotal": TOTAL_CHAPTERS,
            "quizScore": quiz_score,
            "quizTotal": TOTAL_QUIZ,
            "percent": round(read_n / TOTAL_CHAPTERS * 100) if TOTAL_CHAPTERS else 0,
        },
        "perTrack": per_track,
    })


@app.route("/api/terminal", methods=["POST"])
def api_terminal():
    """模擬終端機：用查表的方式回傳「這個指令長什麼樣子」。

    這是教學用的沙盒，不會真的在你的電腦上執行任何指令，
    所以可以放心亂打。
    """
    body = request.get_json(silent=True) or {}
    cmd = (body.get("cmd") or "").strip()
    if not cmd:
        return jsonify({"output": "", "found": True})

    low = cmd.lower()
    if low in ("help", "?", "說明"):
        return jsonify({"output": _terminal_help(), "found": True})
    if low in ("clear", "cls"):
        return jsonify({"output": "", "clear": True, "found": True})
    if low == "whoami":
        return jsonify({"output": "student", "found": True})
    if low == "pwd":
        return jsonify({"output": "/home/student", "found": True})
    if low.startswith("man "):
        return jsonify({"output": _fake_man(cmd[4:].strip()), "found": True})

    if cmd in TERMINAL_DB:
        return jsonify({"output": TERMINAL_DB[cmd], "found": True})

    norm = re.sub(r"\s+", " ", low)
    for key, val in TERMINAL_DB.items():
        if re.sub(r"\s+", " ", key.lower()) == norm:
            return jsonify({"output": val, "found": True})

    head = low.split()[0]
    hits = [k for k in TERMINAL_DB if k.lower().startswith(head)]
    if hits:
        sample = hits[0]
        return jsonify({
            "output": ("[模擬器] 沒有一模一樣的預錄輸出，"
                       "但課程裡有相近的範例：\n  $ %s\n\n%s"
                       % (sample, TERMINAL_DB[sample])),
            "found": False,
        })
    return jsonify({
        "output": ("[模擬器] 查不到 %s 的預錄輸出。\n"
                   "輸入 help 看可用指令，或到任何章節的「動手做」"
                   "區塊點指令自動帶入。" % cmd),
        "found": False,
    })


def _terminal_help():
    lines = [
        "資安自學院 · 模擬終端機",
        "──────────────────────────────",
        "這是教學沙盒，不會真的動到你的電腦。",
        "",
        "內建指令： help / clear / whoami / pwd / man <指令>",
        "",
        "課程中已預錄 %d 條指令的示範輸出，例如：" % len(TERMINAL_DB),
    ]
    for cmd in list(TERMINAL_DB.keys())[:14]:
        lines.append("  $ " + cmd)
    lines.append("  ...（在各章節「動手做」點指令即可帶入）")
    return "\n".join(lines)


def _fake_man(target):
    entry = GLOSSARY.get(target.lower())
    if entry:
        return "%s\n%s\n%s" % (target.upper(), "─" * 30, entry)
    return ("找不到 %s 的說明頁。試試： nmap, iptables, ss, journalctl, "
            "chmod, tcpdump" % target)


@app.route("/api/search")
def api_search():
    q = (request.args.get("q") or "").strip().lower()
    if len(q) < 1:
        return jsonify({"results": []})
    results = []
    for cid, ch in CHAPTER_INDEX.items():
        track = CHAPTER_TRACK[cid]
        haystack = " ".join([
            ch["title"], ch.get("subtitle", ""), ch.get("summary", ""),
            " ".join(ch.get("keywords", [])),
            " ".join(s.get("heading", "") for s in ch.get("sections", [])),
        ]).lower()
        if q in haystack:
            results.append({
                "id": cid, "title": ch["title"],
                "track": track["title"], "color": track.get("color", "cyan"),
                "summary": ch.get("summary", ""),
            })
    return jsonify({"results": results[:40]})


@app.route("/api/glossary")
def api_glossary():
    items = [{"term": k, "desc": v} for k, v in sorted(GLOSSARY.items())]
    return jsonify({"items": items})


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.svg",
        mimetype="image/svg+xml")


def main():
    _ensure_data_dir()
    print("=" * 62)
    print("  資安自學院 CyberSec Academy")
    print("=" * 62)
    print("  學習路線：%d 條" % len(TRACKS))
    print("  章節總數：%d 章" % TOTAL_CHAPTERS)
    print("  測驗題數：%d 題" % TOTAL_QUIZ)
    print("  模擬指令：%d 條" % len(TERMINAL_DB))
    # 由 Project Hub 啟動時會指派 PORT；單獨執行時沿用預設的 5000
    port = int(os.environ.get("PORT", 5000))
    print("-" * 62)
    print("  請用瀏覽器打開： http://127.0.0.1:%d" % port)
    print("  要停止伺服器，在這個視窗按 Ctrl + C")
    print("=" * 62)
    app.run(host="127.0.0.1", port=port, debug=False)


if __name__ == "__main__":
    main()
