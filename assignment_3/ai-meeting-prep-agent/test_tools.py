from tools.document_search import search_client_documents
from tools.meeting_notes import search_meeting_notes


print("\n========== CLIENT DOCUMENT SEARCH ==========\n")

client_results = search_client_documents(
    "What are the current issues and project risks for Acme Corp?"
)

print(client_results)


print("\n========== MEETING NOTES SEARCH ==========\n")

meeting_results = search_meeting_notes(
    "What action items are still open for Acme Corp?"
)

print(meeting_results)