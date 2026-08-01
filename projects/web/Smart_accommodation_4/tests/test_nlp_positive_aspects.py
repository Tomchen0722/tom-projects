"""租客入口「住客常提到的優點」純邏輯與計分隔離測試。"""
from __future__ import annotations

import pandas as pd
import pytest

from modules import nlp_analysis as nlp
from modules import tenant_scoring as ts


def _reviews(texts, listing_id=101, start="2026-01-01"):
    dates = pd.date_range(start, periods=len(texts), freq="D")
    return pd.DataFrame({
        "listing_id": [listing_id] * len(texts),
        "id": range(1, len(texts) + 1),
        "date": dates,
        "comments": texts,
        "cleaned_comments": texts,
        "language_type": [
            "mixed_zh_en" if any("\u4e00" <= ch <= "\u9fff" for ch in text)
            and any(ch.isascii() and ch.isalpha() for ch in text)
            else "zh" if any("\u4e00" <= ch <= "\u9fff" for ch in text)
            else "en"
            for text in texts
        ],
    })


def _sentiment(label="正面", valid=True, reason=None, analyzer="test"):
    compound = {"正面": 0.8, "中立": 0.0, "負面": -0.8}.get(label, 0.0)
    return {
        "compound": compound,
        "pos": 1.0 if label == "正面" else 0.0,
        "neg": 1.0 if label == "負面" else 0.0,
        "neu": 1.0 if label == "中立" else 0.0,
        "label": label,
        "valid": valid,
        "reason": reason,
        "analyzer": analyzer,
    }


def test_analyze_recent_reviews_uses_newest_twenty(monkeypatch):
    df = _reviews([f"clean room {i}" for i in range(25)])
    monkeypatch.setattr(nlp, "analyze_sentiment",
                        lambda text, lang="en": _sentiment())

    result = nlp.analyze_recent_reviews(df, 101, window=20)

    assert result["total_reviews"] == 25
    assert result["sampled_count"] == 20
    assert result["analyzable_count"] == 20
    assert result["rows"]["id"].tolist() == list(range(25, 5, -1))


def test_positive_aspects_are_per_review_and_bilingual(monkeypatch):
    df = _reviews([
        "the room was clean clean clean and very comfortable",
        "Clean and spotless. Close to MRT.",
        "房間乾淨又舒適，離捷運很近",
        "The friendly host was helpful",
        "環境安靜而且物超所值",
    ])
    monkeypatch.setattr(nlp, "analyze_sentiment",
                        lambda text, lang="en": _sentiment())

    result = nlp.listing_positive_aspect_summary(df, 101)
    items = {item["key"]: item for item in result["items"]}

    assert result["status"] == "ok"
    assert result["positive_count"] == 5
    assert items["cleanliness"]["mentions"] == 3
    assert items["comfort"]["mentions"] == 2
    assert items["mrt_access"]["mentions"] == 2
    assert items["host_service"]["mentions"] == 1
    assert items["quietness"]["mentions"] == 1
    assert items["value"]["mentions"] == 1
    assert items["cleanliness"]["coverage"] == pytest.approx(3 / 5)
    assert all(item["mentions"] <= result["positive_count"]
               for item in result["items"])
    assert not {"and", "the", "to", "is", "very", "was"} & set(items)


@pytest.mark.parametrize(
    ("count", "expected"),
    [(0, "no_reviews"), (1, "positive_sample_too_small"),
     (2, "positive_sample_too_small"), (3, "low_sample"),
     (4, "low_sample"), (5, "ok")],
)
def test_positive_sample_display_states(monkeypatch, count, expected):
    variants = [
        "The room was clean and bright.",
        "A spotless room with fresh sheets.",
        "Everything was clean and well maintained.",
        "The clean apartment felt welcoming.",
        "We found the room clean throughout.",
    ]
    df = _reviews(variants[:count])
    monkeypatch.setattr(nlp, "analyze_sentiment",
                        lambda text, lang="en": _sentiment())

    result = nlp.listing_positive_aspect_summary(df, 101)

    assert result["status"] == expected
    if count <= 2:
        assert result["items"] == []
    if 1 <= count <= 2:
        assert len(result["positive_snippets"]) == count


def test_only_valid_positive_reviews_feed_aspects(monkeypatch):
    df = _reviews([
        "clean positive",
        "clean neutral",
        "clean negative",
        "clean unsupported",
    ])

    def fake_analyze(text, lang="en"):
        if "positive" in text:
            return _sentiment("正面")
        if "neutral" in text:
            return _sentiment("中立")
        if "negative" in text:
            return _sentiment("負面")
        return _sentiment("無法分析", valid=False,
                          reason="unsupported_language", analyzer="none")

    monkeypatch.setattr(nlp, "analyze_sentiment", fake_analyze)

    result = nlp.listing_positive_aspect_summary(df, 101)

    assert result["analyzable_count"] == 3
    assert result["positive_count"] == 1
    assert result["status"] == "positive_sample_too_small"
    assert len(result["positive_snippets"]) == 1


def test_generic_positive_words_do_not_invent_aspects(monkeypatch):
    df = _reviews([
        "Great nice good.",
        "Really great and nice.",
        "Good, truly nice.",
        "An excellent stay.",
        "Amazing and lovely.",
    ])
    monkeypatch.setattr(nlp, "analyze_sentiment",
                        lambda text, lang="en": _sentiment())

    result = nlp.listing_positive_aspect_summary(df, 101)

    assert result["status"] == "no_recognized_aspects"
    assert result["items"] == []


def test_analyzer_missing_is_not_neutral(monkeypatch):
    monkeypatch.setattr(nlp, "_vader", None)

    result = nlp.analyze_sentiment("A clean and comfortable room.", lang="en")

    assert result["valid"] is False
    assert result["label"] == "無法分析"
    assert result["reason"] == "analyzer_missing"


def test_mixed_language_combines_vader_and_chinese_signal(monkeypatch):
    class FakeVader:
        @staticmethod
        def polarity_scores(text):
            return {"compound": -0.6, "pos": 0.0, "neg": 0.6, "neu": 0.4}

    monkeypatch.setattr(nlp, "_vader", FakeVader())
    monkeypatch.setattr(nlp, "_has_jieba", True)
    monkeypatch.setattr(nlp, "_zh_sentiment_score", lambda text: 0.8)

    result = nlp.analyze_sentiment(
        "The entrance was confusing, 但是房間乾淨舒適。",
        lang="mixed_zh_en",
    )

    assert result["valid"] is True
    assert result["analyzer"] == "vader+zh_lexicon"
    assert result["compound"] == pytest.approx(0.1)
    assert result["label"] == "正面"


def test_duplicate_positive_reviews_count_once(monkeypatch):
    df = _reviews([
        "The room was clean and comfortable.",
        "The room was clean and comfortable.",
        "Close to the MRT and very clean.",
        "A friendly host welcomed us.",
        "The quiet apartment was spacious.",
    ])
    monkeypatch.setattr(nlp, "analyze_sentiment",
                        lambda text, lang="en": _sentiment())

    result = nlp.listing_positive_aspect_summary(df, 101)

    assert result["positive_count"] == 4
    assert result["duplicate_positive_count"] == 1
    assert result["status"] == "low_sample"
    cleanliness = next(
        item for item in result["items"] if item["key"] == "cleanliness"
    )
    assert cleanliness["mentions"] == 2


def test_existing_listing_summary_keeps_legacy_neutral_fallback(monkeypatch):
    df = _reviews(["Unsupported but non-empty review."])
    df["language_type"] = "other"
    monkeypatch.setattr(nlp, "_vader", None)

    result = nlp.listing_review_summary(df, 101)

    assert result["total_reviews"] == 1
    assert result["pos_pct"] == 0
    assert result["neg_pct"] == 0
    assert result["neu_pct"] == 100
    assert result["avg_sentiment"] == 0


def test_shared_recent_window_preserves_reputation_score(monkeypatch):
    labels = ["正面"] * 14 + ["中立"] * 4 + ["負面"] * 2
    # Newest review is the final element; all 20 are inside the scoring window.
    df = _reviews([f"{label} review {i}" for i, label in enumerate(labels)])

    def fake_analyze(text, lang="en"):
        label = text.split()[0]
        return _sentiment(label)

    monkeypatch.setattr(nlp, "analyze_sentiment", fake_analyze)

    breakdown = ts.review_sentiment_breakdown(df, 101, window=20)
    reputation, details = ts.reputation_score(
        rating=4.7,
        pos_n=breakdown["pos_n"],
        neg_n=breakdown["neg_n"],
        n_analyzable=breakdown["n_analyzable"],
        n_total=breakdown["n_total"],
    )

    assert breakdown == {
        "pos_n": 14,
        "neg_n": 2,
        "neu_n": 4,
        "n_analyzable": 20,
        "n_total": 20,
    }
    assert details["N"] == pytest.approx(1.6)
    assert reputation == pytest.approx(4.1)
