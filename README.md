# Mini RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot that answers questions from a Machine Learning PDF document.

## Objective

The project demonstrates the complete RAG pipeline:

PDF → Text Extraction → Text Chunking → Embeddings → FAISS Vector Database → Semantic Search → Context Retrieval → Gemini LLM → Final Answer

## Technologies Used

- Python
- Jupyter Notebook
- PyPDF
- LangChain
- Google Gemini
- Gemini Embeddings
- FAISS
- ipywidgets

## RAG Pipeline

### 1. PDF Text Extraction

The PDF document is loaded using PyPDF and its text is extracted page by page.

### 2. Text Chunking

The extracted text is divided into smaller overlapping chunks using `RecursiveCharacterTextSplitter`.

### 3. Embeddings

Gemini Embeddings convert each text chunk into a numerical vector representation.

### 4. Vector Database

The embeddings are stored in a FAISS vector database.

### 5. Semantic Search

When a user asks a question, FAISS retrieves the most relevant chunks from the document.

### 6. Context Retrieval

The retrieved chunks are combined into a context that is provided to the language model.

### 7. Answer Generation

Google Gemini generates the final answer using the retrieved document context.

## Project Structure

```text
mini-rag-chatbot/
│
├── Mini_RAG_Chatbot.ipynb
├── README.md
├── requirements.txt
├── .gitignore
│
├── sample_data/
│   └── machine_learning_chapter1.pdf
│
└── screenshots/

