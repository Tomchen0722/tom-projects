import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=260, fg_color="#FFFFFF")

        self.grid_propagate(False)

        self.title = ctk.CTkLabel(
            self,
            text="Chats",
            font=("Microsoft JhengHei", 16, "bold")
        )
        self.title.pack(pady=10)

        self.new_chat = ctk.CTkButton(
            self,
            text="+ New Chat"
        )
        self.new_chat.pack(pady=10, padx=10, fill="x")

        for i in range(5):
            btn = ctk.CTkButton(
                self,
                text=f"Chat {i+1}",
                fg_color="transparent",
                text_color="black",
                anchor="w"
            )
            btn.pack(fill="x", padx=10, pady=5)