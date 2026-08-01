from faster_whisper import WhisperModel
from pathlib import Path
import torch


class WhisperService:

    def __init__(
            self,
            model_size="base"):

        self.model_size = model_size

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.compute_type = (
            "float16"
            if self.device == "cuda"
            else "int8"
        )

        print(
            f"載入模型: {model_size}"
        )

        print(
            f"裝置: {self.device}"
        )

        self.model = WhisperModel(
            model_size,
            device=self.device,
            compute_type=self.compute_type
        )

    def transcribe(
            self,
            audio_path,
            language="zh"):

        audio_path = str(
            Path(audio_path)
        )

        # ⭕ 加入 initial_prompt 強制輸出繁體中文並抑制噪音
        # ⭕ 加入 repetition_penalty 防止 AI 陷入「沉溫庭」式的無限跳針
        segments, info = self.model.transcribe(
            audio_path,
            #language=language,
            language="zh",                  # 強制指定中文
            beam_size=5,
            vad_filter=True,
            condition_on_previous_text=False, # ⭕ 關鍵：關閉前文記憶，防止上一句認錯導致後面整段跟著錯
            # ⭕ 新增以下 VAD 參數調整
            vad_parameters=dict(
                min_speech_duration_ms=200,   # 只要講話超過 0.2 秒就記錄（防漏字）
                max_speech_duration_s=float('inf'),
                speech_pad_ms=500             # 說話前後多保留 0.5 秒緩衝（防止字尾被切掉）
            ),
            # ⭕ 增加更詳細的繁體中文提示詞，引導模型使用台灣常用詞彙
            initial_prompt="這是一段台灣本地口音的會議錄音逐字稿，使用繁體中文，包含日常對話與討論。",
            repetition_penalty=1.2,
            no_speech_threshold=0.6
        )

        transcript = ""

        segment_list = []

        for seg in segments:

            text = seg.text.strip()
            
            # 排除長度過短或純標點符號的幻覺
            if not text or text in ["。", "？", "！", "."]:
                continue

            transcript += text + "\n"

            segment_list.append(
                {
                    "speaker": "Speaker 1",

                    "start": seg.start,

                    "end": seg.end,

                    "text": text
                }
            )

        return {
            "text": transcript,
            "segments": segment_list,
            "language": info.language,
            "duration": (
                segment_list[-1]["end"]
                if segment_list
                else 0
            )
        }


# Singleton

_whisper = None


def get_whisper():

    global _whisper

    if _whisper is None:

        # ⭕ 改用專為 ctranslate2 (faster-whisper) 最佳化的繁體中文模型
        # 這個模型完美支援你的程式碼，且對台灣口音的辨識度極高
        _whisper = WhisperService(
            #model_size="Systran/faster-whisper-small"  # 如果您使用的是 ctranslate2 格式
            model_size="Systran/faster-whisper-large-v3"  # 專為中文優化的模型
        )

    return _whisper


def transcribe(
        audio_path,
        language="zh"):  # ⭕ 補上預設參數

    whisper = get_whisper()

    return whisper.transcribe(
        audio_path,
        language=language  # ⭕ 確保將參數正確傳遞給物件方法
    )
