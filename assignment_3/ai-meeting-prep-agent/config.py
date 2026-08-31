import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CHROMA_DB_PATH = "chroma_db"

CLIENT_DOCUMENTS_PATH = "data/client_documents"

MEETING_NOTES_PATH = "data/meeting_notes"