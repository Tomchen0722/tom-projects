import customtkinter as ctk
from ui.message_widget import MessageWidget


class ChatArea(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F8F9FA")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="#F8F9FA"
        )
        self.scroll.grid(row=0, column=0, sticky="nsew")

        # welcome message
        self.add_message("Welcome to LLM Professional V2 🚀", is_user=False)

    # =========================
    # PUBLIC API
    # =========================

    def add_user_message(self, text: str):
        self.add_message(text, is_user=True)

    def add_ai_message(self, text: str):
        self.add_message(text, is_user=False)

    # =========================
    # INTERNAL CORE METHOD
    # =========================

    def add_message(self, text: str, is_user: bool):

        msg = MessageWidget(
            self.scroll,
            text=text,
            is_user=is_user
        )

        msg.pack(
            fill="x",
            pady=5,
            padx=10,
            anchor="e" if is_user else "w"
        )

    def update_last_ai(self, text):
        # 簡化版：先清空最後一則再更新
        if len(self.scroll.winfo_children()) > 0:
            last = self.scroll.winfo_children()[-1]
            last.destroy()

        self.add_message(text, is_user=False)
        self.scroll.update_idletasks()
        self.scroll._parent_canvas.yview_moveto(1.0)