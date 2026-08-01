"""
NLP Analysis Module — Sentiment analysis & keyword extraction.
Uses VADER for English, keyword-based rules + jieba for Chinese.
"""
import html
import pandas as pd
import numpy as np
import re
from collections import Counter

# ─── Sentiment Analyzers ────────────────────────────────────────
try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    _vader = SentimentIntensityAnalyzer()
except ImportError:
    _vader = None

try:
    import jieba
    _has_jieba = True
except ImportError:
    _has_jieba = False

# ─── Chinese sentiment lexicon (common positive/negative words) ─
_ZH_POS = set([
    "乾淨", "整潔", "舒適", "方便", "便利", "親切", "友善", "溫馨", "安靜",
    "推薦", "喜歡", "滿意", "讚", "棒", "優", "好", "完美", "貼心",
    "寬敞", "明亮", "新", "美", "讚嘆", "值得", "感謝", "開心", "愉快",
    "優秀", "超棒", "很好", "不錯", "划算", "超值", "很棒", "極佳",
    "清潔", "設備齊全", "交通方便", "位置好", "nice", "good", "great",
    "perfect", "excellent", "amazing", "wonderful", "love", "lovely",
    "clean", "comfortable", "convenient", "friendly", "quiet", "recommend",
    "beautiful", "spacious", "helpful", "cozy", "awesome",
])

_ZH_NEG = set([
    "髒", "吵", "噪音", "臭", "差", "破", "舊", "爛", "小",
    "不乾淨", "不方便", "不好", "失望", "難過", "糟", "問題",
    "蟑螂", "漏水", "霉", "黴", "潮濕", "壞", "不推薦", "不舒服",
    "太貴", "不值", "態度差", "冷氣壞", "熱水不夠", "危險",
    "dirty", "noisy", "bad", "poor", "terrible", "horrible", "worst",
    "disappointed", "uncomfortable", "expensive", "broken", "smell",
    "cockroach", "bug", "mold", "cold", "hot", "rude", "dangerous",
])

# ─── Stopwords ──────────────────────────────────────────────────
_EN_STOP = set([
    "the", "a", "an", "is", "was", "were", "are", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "must", "can", "could", "to", "of", "in",
    "for", "on", "with", "at", "by", "from", "as", "into", "through",
    "during", "before", "after", "above", "below", "between", "out",
    "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than", "too", "very", "just", "don",
    "now", "i", "me", "my", "we", "our", "you", "your", "he", "him",
    "his", "she", "her", "it", "its", "they", "them", "their", "this",
    "that", "these", "those", "am", "and", "but", "if", "or", "because",
    "until", "while", "about", "up", "also", "get", "got", "much",
    "really", "even", "one", "two", "like", "go", "going", "went",
    "stay", "stayed", "place", "room", "apartment", "host", "airbnb",
])

_ZH_STOP = set([
    "的", "了", "在", "是", "我", "有", "和", "就", "不", "人",
    "都", "一", "一個", "上", "也", "很", "到", "說", "要",
    "去", "你", "會", "著", "沒有", "看", "好", "自己", "這",
    "他", "她", "們", "那", "這個", "但", "吧", "啊", "呢",
    "嗎", "把", "被", "讓", "給", "跟", "還", "從", "對",
    "得", "過", "可以", "比較", "而且", "如果", "因為", "所以",
    "雖然", "但是", "然後", "之後", "以後", "已經", "正在",
])

# ─── Tenant positive-aspect rules ───────────────────────────────
POSITIVE_ASPECT_RULES_VERSION = "tenant-positive-aspects-v1.0"

# 主題規則只接受具體、可解釋的正面線索。great / nice / good 等籠統詞
# 不單獨成為主題，避免把情緒詞誤當成房源優點。
_POSITIVE_ASPECT_RULES = (
    {
        "key": "cleanliness",
        "label": "環境乾淨",
        "patterns": (
            r"\bclean(?:ed|liness)?\b", r"\bspotless\b",
            r"\bwell[\s-]?maintained\b",
        ),
        "zh_terms": ("乾淨", "整潔", "清潔", "一塵不染"),
    },
    {
        "key": "location",
        "label": "地點便利",
        "patterns": (
            r"\bconvenient(?:ly)? located\b",
            r"\b(?:great|good|excellent|central) location\b",
            r"\blocation (?:is |was )?(?:great|good|excellent|convenient)\b",
            r"\bwell located\b",
        ),
        "zh_terms": ("地點方便", "地點便利", "位置方便", "位置便利", "交通便利"),
    },
    {
        "key": "mrt_access",
        "label": "鄰近捷運",
        "patterns": (
            r"\b(?:near|nearby|close to|next to) (?:the )?"
            r"(?:mrt|metro|subway|station)\b",
            r"\b(?:mrt|metro|subway) (?:nearby|station)\b",
            r"\bwalking distance (?:from|to) (?:the )?"
            r"(?:mrt|metro|subway|station)\b",
        ),
        "zh_terms": ("鄰近捷運", "靠近捷運", "捷運很近", "近捷運",
                     "鄰近地鐵", "靠近地鐵", "地鐵很近", "近地鐵"),
    },
    {
        "key": "comfort",
        "label": "居住舒適",
        "patterns": (
            r"\bcomfortable\b", r"\bcomfy\b", r"\bcozy\b",
            r"\bcosy\b", r"\brestful\b",
        ),
        "zh_terms": ("舒適", "舒服", "溫馨", "好睡"),
    },
    {
        "key": "host_service",
        "label": "房東友善",
        "patterns": (
            r"\b(?:friendly|helpful|kind|responsive) host\b",
            r"\bhost (?:is |was )?(?:friendly|helpful|kind|responsive|great)\b",
        ),
        "zh_terms": ("房東友善", "房東親切", "房東熱心", "房東貼心",
                     "房東回覆快速", "服務親切"),
    },
    {
        "key": "quietness",
        "label": "環境安靜",
        "patterns": (r"\bquiet\b", r"\bpeaceful\b", r"\bcalm\b"),
        "zh_terms": ("安靜", "寧靜", "清幽"),
    },
    {
        "key": "spaciousness",
        "label": "空間寬敞",
        "patterns": (
            r"\bspacious\b", r"\broomy\b", r"\blarge room\b",
            r"\bplenty of space\b",
        ),
        "zh_terms": ("寬敞", "空間大", "空間寬敞"),
    },
    {
        "key": "value",
        "label": "價格划算",
        "patterns": (
            r"\b(?:good|great|excellent) value\b", r"\bvalue for money\b",
            r"\bworth (?:it|the price)\b", r"\baffordable\b",
        ),
        "zh_terms": ("划算", "超值", "物超所值", "性價比高"),
    },
)

_URL_RE = re.compile(r"(?:https?://|www\.)\S+", re.IGNORECASE)
_EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")
_PHONE_RE = re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)")


# ─── Core Analysis Functions ────────────────────────────────────

def _unanalyzable(reason):
    """Return an explicit non-neutral analysis failure."""
    return {
        "compound": 0.0,
        "pos": 0.0,
        "neg": 0.0,
        "neu": 0.0,
        "label": "無法分析",
        "valid": False,
        "reason": reason,
        "analyzer": "none",
    }


def analyze_sentiment(text, lang="en"):
    """
    Analyze sentiment of a single text.
    Returns scores plus explicit valid/reason/analyzer status.
    """
    if not isinstance(text, str) or not text.strip():
        return _unanalyzable("empty_text")
    if len(text.strip()) < 3:
        return _unanalyzable("too_short")

    lang = str(lang or "other")
    if lang == "en":
        if _vader is None:
            return _unanalyzable("analyzer_missing")
        scores = _vader.polarity_scores(text)
        compound = scores["compound"]
        analyzer = "vader"
    elif lang == "mixed_zh_en":
        if _vader is None or not _has_jieba:
            return _unanalyzable("analyzer_missing")
        vader_scores = _vader.polarity_scores(text)
        zh_compound = _zh_sentiment_score(text)
        compound = vader_scores["compound"]
        scores = vader_scores
        if zh_compound:
            compound = (compound + zh_compound) / 2
            scores = {
                "pos": max(0, compound),
                "neg": abs(min(0, compound)),
                "neu": 1 - abs(compound),
            }
        analyzer = "vader+zh_lexicon"
    elif lang == "zh":
        if not _has_jieba:
            return _unanalyzable("analyzer_missing")
        compound = _zh_sentiment_score(text)
        scores = {"pos": max(0, compound), "neg": abs(min(0, compound)),
                  "neu": 1 - abs(compound)}
        analyzer = "zh_lexicon"
    else:
        return _unanalyzable("unsupported_language")

    if compound >= 0.05:
        label = "正面"
    elif compound <= -0.05:
        label = "負面"
    else:
        label = "中立"

    return {
        "compound": round(compound, 4),
        "pos": round(scores.get("pos", 0), 4),
        "neg": round(scores.get("neg", 0), 4),
        "neu": round(scores.get("neu", 0), 4),
        "label": label,
        "valid": True,
        "reason": None,
        "analyzer": analyzer,
    }


def _analyze_sentiment_legacy(text, lang="en"):
    """Preserve pre-v1 behavior for non-tenant summary callers."""
    if not isinstance(text, str) or len(text.strip()) < 3:
        return {
            "compound": 0.0, "pos": 0.0, "neg": 0.0,
            "neu": 1.0, "label": "中立",
        }

    if lang in ("en", "mixed_zh_en") and _vader:
        scores = _vader.polarity_scores(text)
        compound = scores["compound"]
    elif lang == "zh":
        compound = _zh_sentiment_score(text)
        scores = {
            "pos": max(0, compound),
            "neg": abs(min(0, compound)),
            "neu": 1 - abs(compound),
        }
    elif _vader:
        scores = _vader.polarity_scores(text)
        compound = scores["compound"]
    else:
        compound = 0.0
        scores = {"pos": 0.0, "neg": 0.0, "neu": 1.0}

    if compound >= 0.05:
        label = "正面"
    elif compound <= -0.05:
        label = "負面"
    else:
        label = "中立"
    return {
        "compound": round(compound, 4),
        "pos": round(scores.get("pos", 0), 4),
        "neg": round(scores.get("neg", 0), 4),
        "neu": round(scores.get("neu", 0), 4),
        "label": label,
    }


def _zh_sentiment_score(text):
    """Simple Chinese sentiment scoring using keyword matching."""
    if not _has_jieba:
        return 0.0
    words = set(jieba.lcut(text))
    pos_count = len(words & _ZH_POS)
    neg_count = len(words & _ZH_NEG)
    total = pos_count + neg_count
    if total == 0:
        return 0.0
    return (pos_count - neg_count) / max(total, 1) * 0.8


def batch_sentiment(df, text_col="cleaned_comments", lang_col="language_type",
                    sample_n=None, analyzer=None):
    """
    Batch sentiment analysis on a DataFrame.
    Returns DataFrame with sentiment columns added.
    """
    if sample_n and len(df) > sample_n:
        df = df.sample(sample_n, random_state=42)

    analyzer = analyzer or analyze_sentiment
    results = []
    for _, row in df.iterrows():
        text = row.get(text_col, "")
        lang = row.get(lang_col, "en")
        text = "" if pd.isna(text) else str(text)
        lang = "other" if pd.isna(lang) else str(lang)
        s = analyzer(text, lang=lang)
        results.append(s)

    sent_df = pd.DataFrame(results, index=df.index)
    return pd.concat([df, sent_df], axis=1)


def extract_keywords(texts, lang="en", top_n=20):
    """
    Extract top keywords from a list of texts.
    Returns list of (word, count) tuples.
    """
    word_counts = Counter()

    for text in texts:
        if not isinstance(text, str):
            continue
        text = text.lower().strip()

        if lang == "zh" and _has_jieba:
            words = jieba.lcut(text)
            words = [w for w in words if len(w) >= 2 and w not in _ZH_STOP
                     and not re.match(r'^[\d\s\W]+$', w)]
        else:
            words = re.findall(r'[a-z]+', text)
            words = [w for w in words if len(w) >= 3 and w not in _EN_STOP]

        word_counts.update(words)

    return word_counts.most_common(top_n)


def analyze_recent_reviews(reviews_df, listing_id, window=20):
    """Analyze one listing's newest review window with explicit validity."""
    window = max(1, int(window))
    lr = reviews_df[reviews_df["listing_id"] == listing_id].copy()
    total_reviews = int(len(lr))
    if "date" in lr.columns:
        lr = lr.sort_values("date", ascending=False, na_position="last")
    sampled = lr.head(window).copy()

    if sampled.empty:
        rows = sampled.copy()
        for col, dtype in (
            ("compound", "float64"), ("pos", "float64"), ("neg", "float64"),
            ("neu", "float64"), ("label", "object"), ("valid", "bool"),
            ("reason", "object"), ("analyzer", "object"),
        ):
            rows[col] = pd.Series(index=rows.index, dtype=dtype)
    else:
        cleaned = pd.Series("", index=sampled.index, dtype=object)
        if "cleaned_comments" in sampled.columns:
            cleaned = sampled["cleaned_comments"].fillna("").astype(str).str.strip()
        if "comments" in sampled.columns:
            raw = sampled["comments"].fillna("").astype(str).str.strip()
            cleaned = cleaned.mask(cleaned.eq(""), raw)
        sampled["_analysis_text"] = cleaned
        rows = batch_sentiment(sampled, text_col="_analysis_text",
                               lang_col="language_type")

    valid = rows["valid"].fillna(False).astype(bool) if "valid" in rows else pd.Series(
        False, index=rows.index)
    analyzers = sorted({
        str(value)
        for value in rows.loc[valid, "analyzer"].dropna().tolist()
        if str(value) != "none"
    }) if "analyzer" in rows else []
    return {
        "listing_id": int(listing_id),
        "window_size": window,
        "total_reviews": total_reviews,
        "sampled_count": int(len(rows)),
        "analyzable_count": int(valid.sum()),
        "unanalyzable_count": int((~valid).sum()),
        "analyzers": analyzers,
        "rows": rows,
    }


def _clean_aspect_text(value):
    """Normalize review text before topic matching or snippet display."""
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    text = _URL_RE.sub(" ", text)
    text = _EMAIL_RE.sub(" ", text)
    text = _PHONE_RE.sub(" ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _aspect_keys(text):
    """Map one review to a set of concrete bilingual positive-aspect keys."""
    normalized = _clean_aspect_text(text).lower()
    if not normalized:
        return set()
    keys = set()
    for rule in _POSITIVE_ASPECT_RULES:
        english_hit = any(re.search(pattern, normalized)
                          for pattern in rule["patterns"])
        chinese_hit = any(term in normalized for term in rule["zh_terms"])
        if english_hit or chinese_hit:
            keys.add(rule["key"])
    return keys


def _safe_snippet(text, maxlen=150):
    snippet = _clean_aspect_text(text)
    if len(snippet) > maxlen:
        snippet = snippet[:maxlen].rstrip() + "…"
    return snippet


def listing_positive_aspect_summary(
        reviews_df, listing_id, window=20,
        rule_version=POSITIVE_ASPECT_RULES_VERSION):
    """Build the tenant-facing positive-aspect summary for one listing."""
    analysis = analyze_recent_reviews(reviews_df, listing_id, window=window)
    rows = analysis["rows"]
    valid = rows[rows["valid"].fillna(False).astype(bool)]
    positive = valid[valid["label"] == "正面"].copy()
    text_col = ("_analysis_text" if "_analysis_text" in positive.columns
                else "cleaned_comments" if "cleaned_comments" in positive.columns
                else "comments")

    mention_counts = Counter()
    matched_positive_count = 0
    snippets = []
    seen_positive = set()
    for value in positive.get(text_col, pd.Series(dtype=object)).tolist():
        text = "" if pd.isna(value) else str(value)
        signature = _clean_aspect_text(text).casefold()
        if not signature or signature in seen_positive:
            continue
        seen_positive.add(signature)
        keys = _aspect_keys(text)
        if keys:
            matched_positive_count += 1
            mention_counts.update(keys)
        snippet = _safe_snippet(text)
        if snippet and len(snippets) < 2:
            snippets.append(snippet)
    positive_count = int(len(seen_positive))
    duplicate_positive_count = int(len(positive) - positive_count)

    order = {rule["key"]: i for i, rule in enumerate(_POSITIVE_ASPECT_RULES)}
    labels = {rule["key"]: rule["label"] for rule in _POSITIVE_ASPECT_RULES}
    items = [
        {
            "key": key,
            "label": labels[key],
            "mentions": int(count),
            "coverage": round(count / positive_count, 4),
        }
        for key, count in sorted(
            mention_counts.items(),
            key=lambda pair: (-pair[1], order[pair[0]]),
        )[:8]
    ] if positive_count else []

    if analysis["total_reviews"] == 0:
        status = "no_reviews"
    elif analysis["analyzable_count"] == 0:
        status = "no_analyzable_reviews"
    elif positive_count == 0:
        status = "no_positive_reviews"
    elif positive_count <= 2:
        status = "positive_sample_too_small"
        items = []
    elif not items:
        status = "no_recognized_aspects"
    elif positive_count <= 4:
        status = "low_sample"
    else:
        status = "ok"

    warning = {
        "positive_sample_too_small": "正面評論樣本較少，改以摘錄呈現。",
        "low_sample": "樣本較少，結果僅供參考。",
        "no_recognized_aspects": "正面評論中尚無法整理出具體優點。",
    }.get(status)

    return {
        "listing_id": int(listing_id),
        "status": status,
        "rule_version": str(rule_version),
        "window_size": analysis["window_size"],
        "total_reviews": analysis["total_reviews"],
        "sampled_count": analysis["sampled_count"],
        "analyzable_count": analysis["analyzable_count"],
        "unanalyzable_count": analysis["unanalyzable_count"],
        "analyzers": analysis["analyzers"],
        "positive_count": positive_count,
        "duplicate_positive_count": duplicate_positive_count,
        "matched_positive_count": int(matched_positive_count),
        "items": items,
        "positive_snippets": snippets if positive_count <= 2 else [],
        "warnings": [warning] if warning else [],
    }


def listing_review_summary(reviews_df, listing_id):
    """
    Generate NLP summary for a specific listing's reviews.
    Returns dict with sentiment stats and keywords.
    """
    lr = reviews_df[reviews_df["listing_id"] == listing_id].copy()
    if lr.empty:
        return {
            "total_reviews": 0,
            "avg_sentiment": 0,
            "pos_pct": 0, "neg_pct": 0, "neu_pct": 0,
            "pos_keywords": [], "neg_keywords": [],
            "sample_pos": "", "sample_neg": "",
        }

    # Analyze sentiment
    analyzed = batch_sentiment(
        lr, sample_n=200, analyzer=_analyze_sentiment_legacy,
    )
    total = len(analyzed)
    pos_n = (analyzed["label"] == "正面").sum()
    neg_n = (analyzed["label"] == "負面").sum()

    # Extract keywords by sentiment
    pos_texts = analyzed[analyzed["label"] == "正面"]["cleaned_comments"].tolist()
    neg_texts = analyzed[analyzed["label"] == "負面"]["cleaned_comments"].tolist()

    # Determine dominant language
    lang_mode = lr["language_type"].mode()
    dominant_lang = lang_mode.iloc[0] if len(lang_mode) > 0 else "en"

    pos_kw = extract_keywords(pos_texts, lang=dominant_lang, top_n=10)
    neg_kw = extract_keywords(neg_texts, lang=dominant_lang, top_n=10)

    # Get sample reviews
    sample_pos = ""
    sample_neg = ""
    if pos_texts:
        sample_pos = max(pos_texts[:10], key=lambda x: len(str(x)) if isinstance(x, str) else 0, default="")
        if isinstance(sample_pos, str) and len(sample_pos) > 150:
            sample_pos = sample_pos[:150] + "…"
    if neg_texts:
        sample_neg = max(neg_texts[:10], key=lambda x: len(str(x)) if isinstance(x, str) else 0, default="")
        if isinstance(sample_neg, str) and len(sample_neg) > 150:
            sample_neg = sample_neg[:150] + "…"

    return {
        "total_reviews": total,
        "avg_sentiment": round(analyzed["compound"].mean(), 3),
        "pos_pct": round(pos_n / total * 100, 1) if total > 0 else 0,
        "neg_pct": round(neg_n / total * 100, 1) if total > 0 else 0,
        "neu_pct": round((total - pos_n - neg_n) / total * 100, 1) if total > 0 else 0,
        "pos_keywords": pos_kw,
        "neg_keywords": neg_kw,
        "sample_pos": sample_pos,
        "sample_neg": sample_neg,
    }


def global_sentiment_stats(reviews_df, sample_n=10000):
    """
    Compute global sentiment statistics for the admin dashboard.
    Samples reviews for performance.
    """
    sampled = reviews_df.sample(min(sample_n, len(reviews_df)), random_state=42)
    analyzed = batch_sentiment(sampled, analyzer=_analyze_sentiment_legacy)

    total = len(analyzed)
    pos_n = (analyzed["label"] == "正面").sum()
    neg_n = (analyzed["label"] == "負面").sum()
    neu_n = total - pos_n - neg_n

    # Per-language breakdown
    lang_stats = {}
    for lang in analyzed["language_type"].unique():
        lang_data = analyzed[analyzed["language_type"] == lang]
        lt = len(lang_data)
        lang_stats[str(lang)] = {
            "count": lt,
            "avg_sentiment": round(lang_data["compound"].mean(), 3),
            "pos_pct": round((lang_data["label"] == "正面").sum() / lt * 100, 1) if lt > 0 else 0,
        }

    # All keywords
    all_pos = analyzed[analyzed["label"] == "正面"]["cleaned_comments"].tolist()
    all_neg = analyzed[analyzed["label"] == "負面"]["cleaned_comments"].tolist()

    return {
        "total_sampled": total,
        "avg_sentiment": round(analyzed["compound"].mean(), 3),
        "pos_n": int(pos_n), "neg_n": int(neg_n), "neu_n": int(neu_n),
        "pos_pct": round(pos_n / total * 100, 1),
        "neg_pct": round(neg_n / total * 100, 1),
        "neu_pct": round(neu_n / total * 100, 1),
        "lang_stats": lang_stats,
        "pos_keywords_en": extract_keywords(all_pos, lang="en", top_n=25),
        "neg_keywords_en": extract_keywords(all_neg, lang="en", top_n=25),
        "pos_keywords_zh": extract_keywords(all_pos, lang="zh", top_n=25),
        "neg_keywords_zh": extract_keywords(all_neg, lang="zh", top_n=25),
        "sentiment_series": analyzed,
    }


def recent_review_snippets(reviews_df, listing_id, n=6, maxlen=150):
    """
    Return up to n recent review comment snippets (plain strings) for a
    listing, newest first, for the hover-preview tooltip.
    """
    r = reviews_df[reviews_df["listing_id"] == listing_id]
    if r.empty:
        return []
    if "date" in r.columns:
        r = r.sort_values("date", ascending=False)
    col = "comments" if "comments" in r.columns else "cleaned_comments"
    out = []
    for c in r[col].head(n).tolist():
        s = " ".join(str(c).split()).strip()
        if not s:
            continue
        if len(s) > maxlen:
            s = s[:maxlen] + "…"
        out.append(s)
    return out
