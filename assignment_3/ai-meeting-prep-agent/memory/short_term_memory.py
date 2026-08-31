class ShortTermMemory:

    def __init__(self):
        self.conversation = []


    def add_message(self, role, content):

        self.conversation.append({
            "role": role,
            "content": content
        })


    def get_conversation(self):

        return self.conversation


    def get_context(self):

        context = ""

        for message in self.conversation:

            context += (
                f"{message['role'].upper()}: "
                f"{message['content']}\n"
            )

        return context


    def clear_memory(self):

        self.conversation = []