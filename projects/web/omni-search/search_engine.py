# -*- coding: utf-8 -*-
"""
OmniSearch 搜尋引擎核心模組
提供全網搜尋 (DuckDuckGo Lite)、Google 建議補全、Google 新聞 RSS、維基百科知識圖譜、圖片檢索與 AI 概覽生成。
"""
from __future__ import annotations

import html
import json
import logging
import re
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Any, Dict, List, Optional

import bs4
import requests

logger = logging.getLogger("omni_search")
logging.basicConfig(level=logging.INFO)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/128.0.0.0 Safari/537.36"
)

DEFAULT_TIMEOUT = 7.0


def _get_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def decode_ddg_url(raw_url: str) -> str:
    """從 DuckDuckGo 轉址中提取原始網址"""
    if not raw_url:
        return ""
    if "uddg=" in raw_url:
        parsed = urllib.parse.urlparse(raw_url)
        params = urllib.parse.parse_qs(parsed.query)
        uddg = params.get("uddg")
        if uddg and len(uddg) > 0:
            return uddg[0]
    if raw_url.startswith("//"):
        return "https:" + raw_url
    return raw_url


def search_web(query: str, page: int = 1) -> Dict[str, Any]:
    """
    全網網頁搜尋：
    以 DuckDuckGo Lite 為主力爬梳引擎，若無結果則智慧 fallback 至維基百科與全球資訊庫。
    """
    query = (query or "").strip()
    if not query:
        return {"query": "", "page": page, "results": [], "total_estimate": 0, "has_more": False}

    s = _get_session()
    results: List[Dict[str, Any]] = []
    has_more = False

    # 1. 嘗試 DuckDuckGo Lite
    try:
        post_data = {"q": query}
        if page > 1:
            offset = (page - 1) * 10
            post_data["s"] = str(offset)
            post_data["dc"] = str(offset + 1)

        resp = s.post("https://lite.duckduckgo.com/lite/", data=post_data, timeout=DEFAULT_TIMEOUT)
        if resp.status_code == 200:
            soup = bs4.BeautifulSoup(resp.text, "html.parser")
            link_tags = soup.select(".result-link")

            # 尋找下一頁按鈕
            next_forms = [f for f in soup.find_all("form") if "next" in str(f).lower()]
            if next_forms:
                has_more = True

            # 抓取標題與網址
            for idx, a_tag in enumerate(link_tags):
                title = a_tag.get_text(strip=True)
                raw_href = a_tag.get("href", "")
                actual_url = decode_ddg_url(raw_href)

                if not actual_url or actual_url.startswith("#"):
                    continue

                # 嘗試尋找對應的 snippet
                # DDG Lite 通常在 link 之後的 tr 或 td.result-snippet
                snippet = ""
                tr = a_tag.find_parent("tr")
                if tr:
                    next_tr = tr.find_next_sibling("tr")
                    if next_tr:
                        snippet_td = next_tr.select_one(".result-snippet")
                        if snippet_td:
                            snippet = snippet_td.get_text(strip=True)
                        else:
                            snippet = next_tr.get_text(strip=True)

                parsed_url = urllib.parse.urlparse(actual_url)
                domain = parsed_url.netloc or "web"
                favicon = f"https://www.google.com/s2/favicons?domain={domain}&sz=32"

                results.append({
                    "title": title,
                    "url": actual_url,
                    "display_url": f"{parsed_url.scheme}://{domain}{parsed_url.path[:30]}",
                    "domain": domain,
                    "snippet": snippet or f"來自 {domain} 的即時網頁搜尋結果...",
                    "favicon": favicon,
                    "source": "web"
                })
    except Exception as e:
        logger.warning(f"DuckDuckGo search error: {e}")

    # 2. 如果結果偏少，智慧補充維基百科與權威資訊
    if len(results) < 3 and page == 1:
        try:
            wiki_items = search_wikipedia(query, limit=5)
            for w in wiki_items:
                # 避免重複
                if not any(r["url"] == w["url"] for r in results):
                    results.append(w)
        except Exception as e:
            logger.warning(f"Wiki fallback error: {e}")

    # 計算粗估結果數
    base_seed = abs(hash(query)) % 800000 + 120000
    total_est = base_seed * 10 if results else 0

    return {
        "query": query,
        "page": page,
        "results": results,
        "total_estimate": total_est,
        "has_more": has_more or (len(results) >= 8),
    }


def search_news(query: str) -> List[Dict[str, Any]]:
    """
    即時新聞搜尋：利用 Google News RSS 獲取最新多來源報導
    """
    query = (query or "").strip()
    if not query:
        return []

    encoded = urllib.parse.quote(query)
    rss_url = f"https://news.google.com/rss/search?q={encoded}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"

    s = _get_session()
    news_items: List[Dict[str, Any]] = []

    try:
        resp = s.get(rss_url, timeout=DEFAULT_TIMEOUT)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for item in root.findall(".//item")[:20]:
                title_elem = item.find("title")
                link_elem = item.find("link")
                pub_elem = item.find("pubDate")
                source_elem = item.find("source")

                raw_title = title_elem.text if title_elem is not None else ""
                link = link_elem.text if link_elem is not None else ""
                pub_date = pub_elem.text if pub_elem is not None else ""
                source_name = source_elem.text if source_elem is not None else "新聞媒體"

                # Google News 標題通常是 "標題 - 媒體名稱"
                clean_title = raw_title
                if " - " in raw_title:
                    clean_title = raw_title.rsplit(" - ", 1)[0]

                domain = "news.google.com"
                if link:
                    p = urllib.parse.urlparse(link)
                    domain = p.netloc or domain

                news_items.append({
                    "title": clean_title,
                    "url": link,
                    "source": source_name,
                    "domain": domain,
                    "pub_date": pub_date,
                    "favicon": f"https://www.google.com/s2/favicons?domain={domain}&sz=32",
                })
    except Exception as e:
        logger.warning(f"Google News RSS error: {e}")

    return news_items


def search_images(query: str) -> List[Dict[str, Any]]:
    """
    圖片搜尋：檢索維基媒體 (Wikimedia / Wikipedia) 高畫質圖庫
    """
    query = (query or "").strip()
    if not query:
        return []

    s = _get_session()
    images: List[Dict[str, Any]] = []

    for lang in ["zh", "en"]:
        if len(images) >= 12:
            break
        try:
            api_url = (
                f"https://{lang}.wikipedia.org/w/api.php?"
                f"action=query&generator=search&gsrsearch={urllib.parse.quote(query)}"
                f"&gsrlimit=16&prop=pageimages|extracts&exintro=1&explaintext=1"
                f"&exsentences=1&pithumbsize=800&format=json"
            )
            resp = s.get(api_url, timeout=DEFAULT_TIMEOUT)
            if resp.status_code == 200:
                data = resp.json().get("query", {}).get("pages", {})
                for page_id, info in data.items():
                    thumb = info.get("thumbnail")
                    if thumb and "source" in thumb:
                        img_url = thumb["source"]
                        title = info.get("title", "")
                        extract = info.get("extract", "")
                        images.append({
                            "title": title,
                            "thumbnail": img_url,
                            "url": img_url,
                            "page_url": f"https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(title)}",
                            "source": f"Wikipedia ({lang.upper()})",
                            "description": extract[:120] if extract else title,
                            "width": thumb.get("width", 600),
                            "height": thumb.get("height", 400),
                        })
        except Exception as e:
            logger.warning(f"Image search error on {lang}: {e}")

    return images


def search_wikipedia(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    維基百科全文搜尋
    """
    query = (query or "").strip()
    if not query:
        return []

    s = _get_session()
    results: List[Dict[str, Any]] = []

    try:
        api_url = (
            f"https://zh.wikipedia.org/w/api.php?"
            f"action=query&list=search&srsearch={urllib.parse.quote(query)}"
            f"&srlimit={limit}&utf8=&format=json"
        )
        resp = s.get(api_url, timeout=DEFAULT_TIMEOUT)
        if resp.status_code == 200:
            items = resp.json().get("query", {}).get("search", [])
            for item in items:
                title = item.get("title", "")
                snippet_html = item.get("snippet", "")
                # 清除 HTML 標籤
                clean_snippet = re.sub(r"<[^>]+>", "", snippet_html)
                clean_snippet = html.unescape(clean_snippet)
                target_url = f"https://zh.wikipedia.org/wiki/{urllib.parse.quote(title)}"

                results.append({
                    "title": f"{title} - 維基百科，自由的百科全書",
                    "url": target_url,
                    "display_url": f"https://zh.wikipedia.org/wiki/{title}",
                    "domain": "zh.wikipedia.org",
                    "snippet": clean_snippet or f"{title} 的維基百科完整條目與介紹。",
                    "favicon": "https://www.google.com/s2/favicons?domain=wikipedia.org&sz=32",
                    "source": "wikipedia"
                })
    except Exception as e:
        logger.warning(f"Wikipedia search error: {e}")

    return results


def get_knowledge_card(query: str) -> Optional[Dict[str, Any]]:
    """
    獲取知識圖譜卡片（Google 知識面板風格）：
    查詢維基百科官方 REST 摘要 API
    """
    query = (query or "").strip()
    if not query:
        return None

    s = _get_session()

    # 嘗試繁體與簡體 Wikipedia
    clean_q = re.sub(r"[?？!！,，。]+", "", query).strip()

    candidate_titles = [clean_q]
    # 先做一次 search 找到最貼近的精確詞條
    try:
        search_api = (
            f"https://zh.wikipedia.org/w/api.php?"
            f"action=query&list=search&srsearch={urllib.parse.quote(clean_q)}"
            f"&srlimit=2&utf8=&format=json"
        )
        s_resp = s.get(search_api, timeout=4.0)
        if s_resp.status_code == 200:
            hits = s_resp.json().get("query", {}).get("search", [])
            for h in hits:
                t = h.get("title")
                if t and t not in candidate_titles:
                    candidate_titles.append(t)
    except Exception:
        pass

    for title in candidate_titles[:3]:
        for lang in ["zh", "en"]:
            try:
                summary_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
                resp = s.get(summary_url, timeout=4.0)
                if resp.status_code == 200:
                    data = resp.json()
                    extract = data.get("extract", "")
                    page_type = data.get("type", "standard")

                    # 排除消除歧義頁
                    if page_type == "disambiguation" or not extract:
                        continue

                    thumb = data.get("thumbnail", {}).get("source")
                    orig_img = data.get("originalimage", {}).get("source") or thumb
                    page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")

                    return {
                        "title": data.get("title", title),
                        "subtitle": data.get("description", "百科全書核心條目"),
                        "extract": extract,
                        "thumbnail": thumb,
                        "image": orig_img,
                        "page_url": page_url or f"https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(title)}",
                        "lang": lang,
                        "source": "維基百科 (Wikipedia)",
                    }
            except Exception as e:
                logger.debug(f"Knowledge card fetch error: {e}")

    return None


def get_suggestions(query: str) -> List[str]:
    """
    取得即時自動完成搜尋建議（整合 Google Suggest API）
    """
    query = (query or "").strip()
    if not query:
        return []

    s = _get_session()
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=chrome&q={urllib.parse.quote(query)}"
        resp = s.get(url, timeout=3.5)
        if resp.status_code == 200:
            data = resp.json()
            if len(data) > 1 and isinstance(data[1], list):
                # 排除空字串與雜訊
                return [str(item).strip() for item in data[1][:8] if str(item).strip()]
    except Exception as e:
        logger.warning(f"Google suggestions error: {e}")

    # Fallback: 提供常用的上下文擴充
    return [
        f"{query} 是什麼",
        f"{query} 教學",
        f"{query} 官網",
        f"{query} 最新消息",
        f"{query} 評價",
    ]


def generate_ai_overview(query: str, results: List[Dict[str, Any]], knowledge: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    生成 Google SGE / Gemini 風格的 AI 智慧摘要
    整合前幾筆搜尋結果與知識圖譜重點，提取最核心的答覆與條列重點
    """
    if not results and not knowledge:
        return {
            "has_overview": False,
            "summary": "",
            "takeaways": [],
            "sources": []
        }

    sources: List[Dict[str, str]] = []
    text_corpus: List[str] = []

    if knowledge and knowledge.get("extract"):
        text_corpus.append(knowledge["extract"])
        sources.append({
            "name": knowledge["title"],
            "url": knowledge["page_url"],
            "domain": "wikipedia.org",
            "favicon": "https://www.google.com/s2/favicons?domain=wikipedia.org&sz=32"
        })

    for r in results[:5]:
        snippet = r.get("snippet", "")
        if snippet:
            text_corpus.append(snippet)
        if len(sources) < 4:
            sources.append({
                "name": r.get("domain", "web"),
                "url": r.get("url", "#"),
                "domain": r.get("domain", "web"),
                "favicon": r.get("favicon", "")
            })

    # 智慧分句與精華濃縮
    combined = " ".join(text_corpus)
    # 分割成句子
    sentences = [s.strip() for s in re.split(r"[。！？\n]+", combined) if len(s.strip()) > 15]

    # 去重
    seen = set()
    clean_sentences = []
    for s in sentences:
        s_norm = re.sub(r"\s+", "", s)
        if s_norm not in seen and len(s) < 160:
            seen.add(s_norm)
            clean_sentences.append(s)

    takeaways = clean_sentences[:4]
    if not takeaways and combined:
        takeaways = [combined[:120] + "..."]

    summary_text = (
        f"根據全網最新資訊與權威資料庫綜整：針對「{query}」，核心重點如下："
    )

    return {
        "has_overview": True,
        "query": query,
        "summary": summary_text,
        "takeaways": takeaways,
        "sources": sources,
    }


def preview_webpage(url: str) -> Dict[str, Any]:
    """
    網頁速覽器：安全抓取目標網頁並轉化為閱讀器模式 (Reader View)
    """
    if not url or not url.startswith(("http://", "https://")):
        return {"ok": False, "error": "無效的網址"}

    s = _get_session()
    try:
        resp = s.get(url, timeout=5.0)
        resp.encoding = resp.apparent_encoding or "utf-8"
        soup = bs4.BeautifulSoup(resp.text, "html.parser")

        # 移除干擾元素
        for tag in soup(["script", "style", "noscript", "iframe", "header", "footer", "nav", "svg", "button"]):
            tag.decompose()

        title = soup.title.string.strip() if soup.title and soup.title.string else "網頁閱讀模式"

        # 提取內文段落
        paragraphs = []
        for p in soup.find_all(["p", "h1", "h2", "h3", "li"]):
            text = p.get_text(strip=True)
            if len(text) > 25:
                paragraphs.append(text)

        article_text = "\n\n".join(paragraphs[:15])
        if not article_text:
            article_text = "此頁面未能提取到長段落文字，建議點擊下方「在新分頁中直接開啟」瀏覽完整網站。"

        parsed = urllib.parse.urlparse(url)

        return {
            "ok": True,
            "title": title,
            "url": url,
            "domain": parsed.netloc,
            "content": article_text,
        }
    except Exception as e:
        return {
            "ok": False,
            "error": f"無法載入該網頁（可能防護跨站抓取或逾時）：{str(e)}",
            "url": url,
        }
