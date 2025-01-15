# Vector Database Exploration

This repository is dedicated to understanding and experimenting with vector databases (VectorDB) based on my personal learning journey. The content will cover various topics, providing explanations and practical implementations to help grasp the concepts and applications of VectorDB.

---

## Introduction to VectorDB

Vector databases are similar to traditional databases, but with a key difference in the way data is stored and retrieved. While traditional databases primarily deal with text and search operations are performed using indexes, VectorDBs can store diverse types of data (e.g., text, images, documents) as vector embeddings. This allows for efficient retrieval using semantic search.

### Key Concepts:
- **Vector Embeddings**: Numerical values representing data, used to find relations and directions between entities in multidimensional space.
- **Applications**:
  - Retrieval-Augmented Generation (RAG) applications
  - Recommendation engines

---

## Getting Started

### Installing ChromaDB
ChromaDB is a popular vector database that simplifies vector storage and retrieval. To install it, run:

```bash
pip install chromadb
```

---

## Day 1: Initial Setup and Querying

### File: `1.py`

#### Steps Covered:

1. **Creating an Instance**:
   - Start by creating an instance of the ChromaDB client.
   
2. **Creating a Collection**:
   - Use `get_or_create_collection()` to create or fetch an existing collection.
     - If a collection with the same name exists, it will be reused.
     - Alternatively, you can use `create_collection()` to always create a new collection.

3. **Uploading Data**:
   - Prepare your sample data and loop through it to upload each item.
   - Provide both `id` and the corresponding document for each entry.

4. **Querying the Collection**:
   - Perform a search using `collection.query()`.
   - Arguments:
     - **`query_texts`**: The search text for querying.
     - **`n_results`**: The number of results to retrieve, ordered by vector distance.

---

This is just the beginning of the exploration. Stay tuned as we dive deeper into advanced concepts and practical use cases of vector databases!

