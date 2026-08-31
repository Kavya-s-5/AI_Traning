from rag.vector_store import VectorStore


def search_meeting_notes(query):
    """
    Searches previous meeting notes
    using semantic similarity search.
    """

    vector_store = VectorStore()

    results = vector_store.search(
        collection_type="meeting",
        query=query,
        n_results=3
    )

    documents = results["documents"][0]

    formatted_results = ""

    for i, document in enumerate(documents, start=1):
        formatted_results += f"\n--- Meeting Note {i} ---\n"
        formatted_results += document
        formatted_results += "\n"

    return formatted_results