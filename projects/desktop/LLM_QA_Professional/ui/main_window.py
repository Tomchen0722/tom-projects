import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.toolbar import Toolbar
from ui.chat_area import ChatArea
from ui.input_panel import InputPanel


class MainWindow(ctk.CTk):

    def __init__(self, on_send):
        super().__init__()

        # ======================
        # Window config
        # ======================
        self.title("LLM Professional Edition V2")
        self.geometry("1200x800")
        self.configure(fg_color="#F8F9FA")

        self.on_send = on_send

        # ======================
        # Layout (Grid System)
        # ======================
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ======================
        # UI Components
        # ======================

        self.toolbar = Toolbar(self)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=1, column=0, sticky="ns")

        self.chat_area = ChatArea(self)
        self.chat_area.grid(row=1, column=1, sticky="nsew")

        self.input_panel = InputPanel(self, self.handle_send)
        self.input_panel.grid(row=2, column=1, sticky="ew")

    # ======================
    # Event Handler
    # ======================

    def handle_send(self, text: str):

        # 1. 顯示 user message
        self.chat_area.add_user_message(text)

        # 2. AI placeholder
        self.chat_area.add_ai_message("Thinking...")

        # 3. streaming callback（由 app layer 控制更新）
        def stream_callback(output):
            self.chat_area.update_last_ai(output)

        # 4. 呼叫上層 App（避免 circular import）
        if self.on_send:
            self.on_send(text)