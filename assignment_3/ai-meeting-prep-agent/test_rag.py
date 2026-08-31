from rag.vector_store import VectorStore


vector_store = VectorStore()


query = "What are the current issues and risks for Acme Corp?"

results = vector_store.search(
    collection_type="client",
    query=query,
    n_results=3
)


print("\nSEARCH RESULTS:\n")

for i, document in enumerate(results["documents"][0], start=1):

    print(f"--- Result {i} ---")
    print(document)
    print()