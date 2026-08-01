import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.toolbar import Toolbar
from ui.chat_area import ChatArea
from ui.input_panel import InputPanel
from ui.main_window import MainWindow


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("LLM Professional V2")
        self.geometry("1200x800")

        self.configure(fg_color="#F8F9FA")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # UI
        self.toolbar = Toolbar(self)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=1, column=0, sticky="ns")

        self.chat_area = ChatArea(self)
        self.chat_area.grid(row=1, column=1, sticky="nsew")

        self.input_panel = InputPanel(self, self.on_send)
        self.input_panel.grid(row=2, column=1, sticky="ew")

    def on_send(self, text):

        # user message
        self.chat_area.add_user_message(text)

        # fake AI reply (Phase 1)
        self.chat_area.add_ai_message(f"AI: {text}")

class App(MainWindow):
    
    def __init__(self):
        super().__init__()

        self.chat_service = ChatService()

    def on_send(self, text):

        self.chat_area.add_user_message(text)

        # AI thinking placeholder
        self.chat_area.add_ai_message("Thinking...")

        def stream_callback(output):
            self.chat_area.add_ai_message(output)

        response = self.chat_service.chat(
            text,
            stream_callback=stream_callback
        )