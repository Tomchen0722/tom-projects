import os
from pathlib import Path

from pyannote.audio import Pipeline

# 權杖從專案資料夾的 .env 讀取，不寫在程式碼裡（.env 已被 .gitignore 排除）。
# 沒裝 python-dotenv 也沒關係，會退回讀系統環境變數。
try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass


class SpeakerService:

    def __init__(self):

        token = os.getenv(
            "HF_TOKEN"
        )

        if not token:
            raise ValueError(
                "找不到 HF_TOKEN，無法使用講者分離功能。\n\n"
                "設定方式：\n"
                "  1. 到 https://huggingface.co/settings/tokens 建立一組 read 權杖\n"
                "  2. 在 AI_Meeting_Assistant 資料夾建立 .env，寫入這一行：\n"
                "       HF_TOKEN=hf_你的權杖\n"
                "  3. 到 https://huggingface.co/pyannote/speaker-diarization-3.1\n"
                "     同意模型的使用條款，否則權杖無法下載模型\n\n"
                "設定完成後重新啟動程式即可。"
            )

        self.pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=token
        )

    def diarize(
            self,
            audio_path):

        diarization = self.pipeline(
            audio_path
        )

        results = []

        for turn, _, speaker in diarization.itertracks(
                yield_label=True):

            results.append(
                {
                    "speaker": speaker,
                    "start": turn.start,
                    "end": turn.end
                }
            )

        return results


_speaker = None


def get_speaker_service():

    global _speaker

    if _speaker is None:

        _speaker = SpeakerService()

    return _speaker


def diarize(audio_path):

    return (
        get_speaker_service()
        .diarize(audio_path)
    )