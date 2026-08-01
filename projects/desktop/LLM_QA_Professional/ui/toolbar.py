import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=50, fg_color="#FFFFFF")

        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(
            self,
            text="🤖 LLM Professional V2",
            font=("Microsoft JhengHei", 18, "bold")
        )

        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="w")