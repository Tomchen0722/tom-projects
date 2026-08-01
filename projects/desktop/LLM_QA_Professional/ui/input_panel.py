import customtkinter as ctk


class InputPanel(ctk.CTkFrame):

    def __init__(self, master, send_callback):
        super().__init__(master, height=70, fg_color="#FFFFFF")

        self.send_callback = send_callback

        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="輸入訊息..."
        )
        self.entry.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

        self.send_btn = ctk.CTkButton(
            self,
            text="Send",
            width=100,
            command=self.send_message
        )
        self.send_btn.grid(row=0, column=1, padx=10)

    def send_message(self):

        text = self.entry.get().strip()

        if not text:
            return

        self.send_callback(text)
        self.entry.delete(0, "end")