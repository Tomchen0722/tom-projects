from collections import Counter
import jieba


def keyword_analysis(
        transcript,
        top_n=20):

    words = jieba.cut(
        transcript
    )

    stop_words = {
        "的",
        "了",
        "是",
        "我們",
        "你們",
        "這個",
        "那個"
    }

    result = []

    for w in words:

        w = w.strip()

        if len(w) < 2:
            continue

        if w in stop_words:
            continue

        result.append(w)

    counter = Counter(
        result
    )

    return counter.most_common(
        top_n
    )


def speaker_statistics(
        segments):

    stats = {}

    for seg in segments:

        speaker = seg["speaker"]

        duration = (
            seg["end"]
            - seg["start"]
        )

        stats[speaker] = (
            stats.get(
                speaker,
                0
            )
            + duration
        )

    total = sum(
        stats.values()
    )

    result = {}

    for k, v in stats.items():

        result[k] = round(
            v / total * 100,
            2
        )

    return result