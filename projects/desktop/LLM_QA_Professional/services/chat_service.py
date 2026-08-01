from services.memory import Memory
from services.prompt_builder import PromptBuilder
from services.llm_service import LLMService


class ChatService:

    def __init__(self):
        self.memory = Memory()
        self.builder = PromptBuilder()
        self.llm = LLMService()

    def chat(self, user_input: str, stream_callback=None):

        # 1. memory
        self.memory.add_user(user_input)

        # 2. build prompt
        messages = self.builder.build(
            self.memory.get_history(),
            user_input
        )

        # 3. LLM generate
        response = self.llm.generate(messages)

        # 4. memory save
        self.memory.add_ai(response)

        # 5. fake streaming
        if stream_callback:
            self.fake_stream(response, stream_callback)

        return response

    def fake_stream(self, text, callback):

        buffer = ""

        for char in text:
            buffer += char
            callback(buffer)