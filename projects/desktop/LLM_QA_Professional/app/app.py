from ui.main_window import MainWindow
from services.chat_service import ChatService


class App:

    def __init__(self):
        self.chat_service = ChatService()

        self.window = MainWindow(
            on_send=self.on_send
        )

    def on_send(self, text: str):

        self.window.chat_area.add_user_message(text)

        def stream_callback(output):
            self.window.chat_area.update_last_ai(output)

        # 缺金鑰或 API 出錯時把原因顯示在對話區，不要讓整個視窗崩掉
        try:
            self.chat_service.chat(
                text,
                stream_callback=stream_callback
            )
        except Exception as exc:
            self.window.chat_area.update_last_ai(
                "【無法取得回覆】\n\n%s" % exc
            )

    def run(self):
        self.window.mainloop()