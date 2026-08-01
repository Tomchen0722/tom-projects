
def merge_segments(
        whisper_segments,
        speaker_segments):

    merged = []

    for w in whisper_segments:

        speaker_name = "Unknown"

        for s in speaker_segments:

            overlap = (
                w["start"] >= s["start"]
                and
                w["end"] <= s["end"]
            )

            if overlap:

                speaker_name = s["speaker"]

                break

        merged.append(
            {
                "speaker": speaker_name,
                "start": w["start"],
                "end": w["end"],
                "text": w["text"]
            }
        )

    return merged
#------------------------------------------------------------
#顯示逐字稿
#-------------------------------------------------------------
