
# Mini Semantic Search Engine using FAISS

## Overview

This project implements a mini semantic search engine using Python, Sentence Transformers, and FAISS.

The system converts knowledge-base sentences and user queries into numerical embeddings and uses FAISS to retrieve the most semantically similar sentences.

## Technologies Used

- Python
- NumPy
- Sentence Transformers
- FAISS
- all-MiniLM-L6-v2

## Project Architecture

Knowledge Base
        ↓
Embedding Model
        ↓
Document Embeddings
        ↓
Normalization
        ↓
FAISS Index
        ↓
User Query
        ↓
Query Embedding
        ↓
Normalization
        ↓
Similarity Search
        ↓
Top 3 Results

## Embedding Model

The project uses the `all-MiniLM-L6-v2` Sentence Transformer model.

Each sentence is converted into a 384-dimensional embedding.

With 10 knowledge-base sentences, the embedding matrix has the shape:

`(10, 384)`

## FAISS Index

The project uses:

`faiss.IndexFlatL2(384)`

The document embeddings are normalized before being added to the index.

The query embedding is also normalized before performing the search.

## Knowledge Base

The knowledge base contains customer-support information related to:

- Password reset
- Login issues
- Account management
- Billing
- Invoices
- Refunds
- Two-factor authentication
- Payment failures

## Features

- Generate text embeddings
- Normalize embeddings
- Store vectors using FAISS
- Perform semantic similarity search
- Retrieve Top 3 results
- Interactive CLI
- Exit using `exit`

## Example Queries

- I forgot my password
- How can I get my money back?
- My card payment is not working
- I want to change my email address
- Where can I find my invoices?

## Assignment Tasks Completed

- [x] Generate embeddings
- [x] Verify embedding shape
- [x] Normalize embeddings
- [x] Create FAISS index
- [x] Add vectors to FAISS
- [x] Perform Top 3 semantic search
- [x] Test multiple queries
- [x] Build interactive CLI
- [x] Answer theory questions
