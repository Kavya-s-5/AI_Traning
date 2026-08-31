from memory.long_term_memory import LongTermMemory


def save_client_memory(client_name, information):

    memory = LongTermMemory()

    memory.save_memory(
        client_name,
        information
    )

    return "Memory saved successfully."


def retrieve_client_memory(client_name):

    memory = LongTermMemory()

    memories = memory.get_memories(client_name)

    if not memories:
        return "No previous memories found."

    formatted_memories = "\n".join(
        f"- {memory}"
        for memory in memories
    )

    return formatted_memories