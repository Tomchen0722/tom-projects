class Memory:
    
    def __init__(self):
        self.messages = []

    def add_user(self, text: str):
        self.messages.append({"role": "user", "content": text})

    def add_ai(self, text: str):
        self.messages.append({"role": "assistant", "content": text})

    def get_history(self):
        return self.messages