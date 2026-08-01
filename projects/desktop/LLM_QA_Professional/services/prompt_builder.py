class PromptBuilder:
    
    def build(self, history, user_input: str):

        system_prompt = {
            "role": "system",
            "content": "你是一個專業 AI 助手，回答需清楚簡潔。"
        }

        messages = [system_prompt]

        messages.extend(history)

        messages.append({
            "role": "user",
            "content": user_input
        })

        return messages