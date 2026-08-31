from tools.memory_tool import (
    save_client_memory,
    retrieve_client_memory
)


print(
    save_client_memory(
        "Acme Corp",
        "The client prefers weekly project updates."
    )
)


print(
    save_client_memory(
        "Acme Corp",
        "Sarah Johnson is concerned about potential project delays."
    )
)


print(
    save_client_memory(
        "Acme Corp",
        "The client expects early communication about project risks."
    )
)


print("\n========== RETRIEVED MEMORIES ==========\n")

memories = retrieve_client_memory(
    "Acme Corp"
)

print(memories)