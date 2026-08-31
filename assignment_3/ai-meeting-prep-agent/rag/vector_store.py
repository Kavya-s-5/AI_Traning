import chromadb
from google import genai

from config import GEMINI_API_KEY, CHROMA_DB_PATH


class VectorStore:

    def __init__(self):

        # Gemini client
        self.gemini_client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        # Persistent ChromaDB
        self.chroma_client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        # Collection for client documents
        self.client_collection = (
            self.chroma_client.get_or_create_collection(
                name="client_documents"
            )
        )

        # Collection for meeting notes
        self.meeting_collection = (
            self.chroma_client.get_or_create_collection(
                name="meeting_notes"
            )
        )


    def create_embedding(self, text):

        response = self.gemini_client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values


    def add_document(
        self,
        collection_type,
        document,
        metadata,
        document_id
    ):

        embedding = self.create_embedding(document)

        if collection_type == "client":
            collection = self.client_collection
        else:
            collection = self.meeting_collection

        collection.upsert(
            documents=[document],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[document_id]
        )


    def search(
        self,
        collection_type,
        query,
        n_results=3
    ):

        query_embedding = self.create_embedding(query)

        if collection_type == "client":
            collection = self.client_collection
        else:
            collection = self.meeting_collection

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results