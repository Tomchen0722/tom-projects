from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL


class MissingAPIKey(RuntimeError):
    """沒有設定 OPENAI_API_KEY 時丟出，訊息直接拿去顯示給使用者看。"""


class LLMService:

    def __init__(self):

        # 客戶端改成第一次真的要發問時才建立。
        # 原本在這裡就 new OpenAI()，只要少了金鑰整個程式會在啟動階段掛掉，
        # 連介面都看不到；延後之後沒有金鑰也能開起來瀏覽。
        self.client = None

        self.model = OPENAI_MODEL

    def _ensure_client(self):

        if self.client is not None:
            return self.client

        if not OPENAI_API_KEY:
            raise MissingAPIKey(
                "尚未設定 OpenAI API 金鑰。\n\n"
                "請在專案資料夾建立 .env 檔並加入這一行：\n"
                "    OPENAI_API_KEY=sk-你的金鑰\n\n"
                "存檔後重新啟動本程式即可使用問答功能。"
            )

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        return self.client

    def generate(self, messages):

        """
        一次取得完整回應（chat_service 走的是這條路）。
        """

        client = self._ensure_client()

        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content

    def stream(self, messages, callback):

        """
        真 streaming GPT 回應
        """

        client = self._ensure_client()

        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True
        )

        buffer = ""

        for chunk in response:

            delta = chunk.choices[0].delta.content

            if delta:

                buffer += delta
                callback(buffer)

        return buffer
