import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from rag.vector_store import VectorStore
from config import CLIENT_DOCUMENTS_PATH, MEETING_NOTES_PATH


def read_and_ingest(folder_path, collection_type):

    vector_store = VectorStore()

    for filename in os.listdir(folder_path):

        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            document_id = f"{collection_type}_{filename}"

            metadata = {
                "source": filename
            }

            vector_store.add_document(
                collection_type=collection_type,
                document=content,
                metadata=metadata,
                document_id=document_id
            )

            print(f"Added: {filename}")


if __name__ == "__main__":

    print("\nIngesting Client Documents...\n")

    read_and_ingest(
        CLIENT_DOCUMENTS_PATH,
        "client"
    )

    print("\nIngesting Meeting Notes...\n")

    read_and_ingest(
        MEETING_NOTES_PATH,
        "meeting"
    )

    print("\nAll documents successfully added to ChromaDB!")