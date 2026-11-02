# -*- coding: utf-8 -*-
"""
OmniSearch 全球萬維搜尋引擎 — 本機服務器
提供高速網頁檢索、即時搜尋補全、Google 新聞 RSS、維基百科知識圖譜與 AI 概覽 API。
啟動：python app.py → http://127.0.0.1:7050
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

# 確保可載入同目錄模組
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

import search_engine

app = Flask(__name__, static_folder="static", static_url_path="")


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.get("/")
def index():
    """首頁：服務靜態頁面"""
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/search")
def api_search():
    """
    綜合搜尋端點：
    支援全部網頁、新聞、圖片、維基百科分頁查詢，
    並於首頁結果附帶 AI 概覽 (AI Overview) 與 Google 風格知識圖譜。
    """
    start_time = time.time()
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "all").strip().lower()
    page = int(request.args.get("page", 1))

    if not query:
        return jsonify({
            "ok": True,
            "query": "",
            "category": category,
            "page": page,
            "results": [],
            "total_estimate": 0,
            "has_more": False,
            "elapsed_sec": 0.0,
            "ai_overview": None,
            "knowledge_card": None,
            "related_queries": [],
        })

    # 分類查詢
    if category == "news":
        news_items = search_engine.search_news(query)
        elapsed = round(time.time() - start_time, 3)
        return jsonify({
            "ok": True,
            "query": query,
            "category": "news",
            "page": page,
            "results": news_items,
            "total_estimate": len(news_items),
            "has_more": False,
            "elapsed_sec": elapsed,
            "ai_overview": None,
            "knowledge_card": None,
            "related_queries": [],
        })

    elif category == "images":
        img_items = search_engine.search_images(query)
        elapsed = round(time.time() - start_time, 3)
        return jsonify({
            "ok": True,
            "query": query,
            "category": "images",
            "page": page,
            "results": img_items,
            "total_estimate": len(img_items),
            "has_more": False,
            "elapsed_sec": elapsed,
            "ai_overview": None,
            "knowledge_card": None,
            "related_queries": [],
        })

    elif category == "knowledge":
        wiki_items = search_engine.search_wikipedia(query, limit=15)
        knowledge = search_engine.get_knowledge_card(query)
        elapsed = round(time.time() - start_time, 3)
        return jsonify({
            "ok": True,
            "query": query,
            "category": "knowledge",
            "page": page,
            "results": wiki_items,
            "total_estimate": len(wiki_items),
            "has_more": False,
            "elapsed_sec": elapsed,
            "ai_overview": None,
            "knowledge_card": knowledge,
            "related_queries": [],
        })

    # 預設：全部網頁搜尋 (all)
    web_data = search_engine.search_web(query, page=page)
    results = web_data.get("results", [])

    knowledge = None
    ai_overview = None
    related = []

    # 第一頁時提供知識圖譜卡片、AI 摘要與相關搜尋
    if page == 1:
        try:
            knowledge = search_engine.get_knowledge_card(query)
        except Exception:
            knowledge = None

        try:
            ai_overview = search_engine.generate_ai_overview(query, results, knowledge)
        except Exception:
            ai_overview = None

        try:
            suggs = search_engine.get_suggestions(query)
            related = [s for s in suggs if s.lower() != query.lower()][:8]
        except Exception:
            related = []

    elapsed = round(time.time() - start_time, 3)

    return jsonify({
        "ok": True,
        "query": query,
        "category": "all",
        "page": page,
        "results": results,
        "total_estimate": web_data.get("total_estimate", len(results) * 1000),
        "has_more": web_data.get("has_more", False),
        "elapsed_sec": elapsed,
        "ai_overview": ai_overview,
        "knowledge_card": knowledge,
        "related_queries": related,
    })


@app.get("/api/suggest")
def api_suggest():
    """即時搜尋關鍵字補全"""
    query = request.args.get("q", "").strip()
    suggestions = search_engine.get_suggestions(query)
    return jsonify({
        "ok": True,
        "query": query,
        "suggestions": suggestions,
    })


@app.get("/api/preview")
def api_preview():
    """網頁速覽器：以閱讀模式呈現目標網頁段落"""
    url = request.args.get("url", "").strip()
    data = search_engine.preview_webpage(url)
    return jsonify(data)


@app.get("/api/lucky")
def api_lucky():
    """好手氣 (I'm Feeling Lucky)：直接導向第一個最相關網頁"""
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"ok": False, "url": "/"})

    web_data = search_engine.search_web(query, page=1)
    results = web_data.get("results", [])
    if results and results[0].get("url"):
        return jsonify({"ok": True, "url": results[0]["url"]})

    # 若無直接結果，導向維基百科
    return jsonify({
        "ok": True,
        "url": f"https://zh.wikipedia.org/wiki/{query}"
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok", "app": "OmniSearch", "timestamp": time.time()})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7050))
    print(f"==================================================")
    print(f"  OmniSearch 全球萬維搜尋引擎 已就緒！")
    print(f"  本機網址: http://127.0.0.1:{port}")
    print(f"==================================================")
    app.run(host="0.0.0.0", port=port, debug=False)
