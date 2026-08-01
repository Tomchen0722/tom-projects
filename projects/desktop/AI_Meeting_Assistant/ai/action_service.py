import json
import os

from openai import OpenAI


class ActionService:

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

    def extract_actions(
            self,
            transcript: str):

        prompt = f"""
請從以下逐字稿中擷取待辦事項。

回傳 JSON：

[
  {{
    "owner":"",
    "task":"",
    "deadline":""
  }}
]

若無資料請回傳 []。

逐字稿：

{transcript}
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        try:
            return json.loads(
                response.output_text
            )
        except:
            return []

    def extract_decisions(
            self,
            transcript: str):

        prompt = f"""
請找出會議已確認的決策事項。

回傳 JSON：

[
  {{
    "decision":""
  }}
]

若無資料請回傳 []。

逐字稿：

{transcript}
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        try:
            return json.loads(
                response.output_text
            )
        except:
            return []


_action = None


def get_action_service():

    global _action

    if _action is None:

        _action = ActionService()

    return _action


def extract_actions(
        transcript):

    return (
        get_action_service()
        .extract_actions(transcript)
    )


def extract_decisions(
        transcript):

    return (
        get_action_service()
        .extract_decisions(transcript)
    )