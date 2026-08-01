import customtkinter as ctk
from ui.message_widget import MessageWidget


class ChatArea(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F8F9FA")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Scrollable container
        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="#F8F9FA"
        )
        self.scroll.grid(row=0, column=0, sticky="nsew")

        # Welcome message
        self.add_message("Welcome to LLM Professional V2 🚀", is_user=False)

    def add_message(self, text, is_user=False):

        msg = MessageWidget(self.scroll, text, is_user=is_user)
        msg.pack(fill="x", pady=5)

        self.scroll.update()
    def add_user_message(self, text):
        self.add_message(text, is_user=True)

    def add_ai_message(self, text):
        self.add_message(text, is_user=False)