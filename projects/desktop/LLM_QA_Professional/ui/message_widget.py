import customtkinter as ctk


class MessageWidget(ctk.CTkFrame):

    def __init__(self, master, text, is_user=False):
        super().__init__(master)

        self.is_user = is_user

        self.configure(fg_color="transparent")

        bubble_color = "#DCF2FF" if is_user else "#FFFFFF"
        text_color = "#1F2937"

        self.bubble = ctk.CTkFrame(
            self,
            fg_color=bubble_color,
            corner_radius=12
        )

        self.bubble.pack(
            anchor="e" if is_user else "w",
            padx=10,
            pady=5,
            fill="x"
        )

        self.label = ctk.CTkLabel(
            self.bubble,
            text=text,
            wraplength=600,
            justify="left",
            text_color=text_color,
            font=("Microsoft JhengHei", 14)
        )

        self.label.pack(padx=10, pady=8)