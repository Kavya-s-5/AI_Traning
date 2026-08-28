
# FAISS and Semantic Search — Theory Answers

## Q1. What is the difference between IndexFlatL2 and IndexFlatIP in FAISS? When would you use each?

### IndexFlatL2

`IndexFlatL2` uses L2 (Euclidean) distance to compare vectors.

A smaller L2 distance means that two vectors are more similar.

It performs an exact nearest-neighbour search by comparing the query with the vectors stored in the index.

It can be used when Euclidean distance is the required similarity measure.

### IndexFlatIP

`IndexFlatIP` uses Inner Product (dot product) to compare vectors.

A larger inner product means greater similarity.

When embeddings are normalized to unit length, inner product is equivalent to cosine similarity.

Therefore, `IndexFlatIP` is commonly used when we want cosine-similarity-based retrieval with normalized embeddings.

### Comparison

| Index | Similarity Measure | Better Result |
|---|---|---|
| `IndexFlatL2` | L2 / Euclidean distance | Lower |
| `IndexFlatIP` | Inner Product | Higher |

---

## Q2. Why do we normalise embeddings before adding them to FAISS when we want cosine similarity?

Cosine similarity measures the angle between two vectors rather than their magnitude.

The formula is:

`Cosine Similarity = (A · B) / (||A|| × ||B||)`

When vectors are normalized, their magnitude becomes 1.

Therefore, the cosine similarity can be represented using the inner product of the normalized vectors.

In this assignment, we use normalized embeddings with `IndexFlatL2`. For unit-normalized vectors, L2 distance and cosine similarity produce the same ranking of vectors.

Therefore, normalization allows us to perform similarity search while reducing the effect of vector magnitude.

---

## Q3. FAISS uses ANN (Approximate Nearest Neighbour) search. What does "approximate" mean here and why is it acceptable?

Approximate Nearest Neighbour (ANN) search means that a search algorithm may return highly similar vectors without guaranteeing that they are the mathematically exact nearest neighbours.

This approach is useful for very large datasets because exact search can become expensive when millions or billions of vectors are stored.

ANN methods trade a small amount of retrieval accuracy for significantly faster search.

For applications such as semantic search and RAG, retrieving highly relevant documents quickly is often more useful than spending significantly more time finding the mathematically exact nearest neighbour.

### Important Note

`IndexFlatL2` itself performs exact nearest-neighbour search. It is not an approximate index.

FAISS also provides approximate indexing methods such as IVF and HNSW that are designed for large-scale approximate nearest-neighbour search.
