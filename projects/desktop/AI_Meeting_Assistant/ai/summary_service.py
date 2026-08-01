import os
from openai import OpenAI


class SummaryService:

    def __init__(self):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "找不到 OPENAI_API_KEY"
            )

        self.client = OpenAI(
            api_key=api_key
        )

    def generate_summary(
            self,
            transcript: str):

        if not transcript.strip():

            return "沒有逐字稿內容"

        prompt = f"""
你是一位專業會議助理。

請分析以下會議逐字稿。

輸出格式：

# 會議摘要
(簡短摘要)

# 重點事項
- item1
- item2

# 結論
(會議結論)

逐字稿：

{transcript}
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        return response.output_text

    def generate_title(
            self,
            transcript: str):

        prompt = f"""
請根據以下會議內容，
產生 20 個字以內的會議名稱。

只輸出標題，不要其他內容。

逐字稿：

{transcript}
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        return response.output_text.strip()


_summary = None


def get_summary_service():

    global _summary

    if _summary is None:

        _summary = SummaryService()

    return _summary


def generate_summary(
        transcript):

    return (
        get_summary_service()
        .generate_summary(transcript)
    )


def generate_title(
        transcript):

    return (
        get_summary_service()
        .generate_title(transcript)
    )