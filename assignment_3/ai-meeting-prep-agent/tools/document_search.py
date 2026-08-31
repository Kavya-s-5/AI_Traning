from rag.vector_store import VectorStore


def search_client_documents(query):
    """
    Searches the client document knowledge base
    using semantic similarity search.
    """

    vector_store = VectorStore()

    results = vector_store.search(
        collection_type="client",
        query=query,
        n_results=3
    )

    documents = results["documents"][0]

    formatted_results = ""

    for i, document in enumerate(documents, start=1):
        formatted_results += f"\n--- Document {i} ---\n"
        formatted_results += document
        formatted_results += "\n"

    return formatted_results