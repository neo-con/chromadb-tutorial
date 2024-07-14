# Using Where Filters in ChromaDB

This tutorial will guide you through using where filters in ChromaDB to filter and query items based on specific metadata criteria.

## 1. Creating a Collection

```python
import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
matrix_collection = client.create_collection(name="matrix", metadata={"hnsw:space": "cosine"})
```

We start by initializing the ChromaDB client and creating a collection named `matrix`.

## 2. Adding Raw Documents

```python
matrix_collection.add(
    documents=[
        "The Matrix is everywhere, it is all around us.",
        "You can see it when you look out your window or when you turn on your television.",
        "Unfortunately, no one can be told what the Matrix is",
        "You hear that Mr. Anderson?... That is the sound of inevitability...",
        "You are a plague, Mr. Anderson. You and your kind are a cancer of this planet.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4", "quote_5"],
)
```

We add five raw documents (quotes from "The Matrix") to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

## 3. Using Where Filters

```python
results = matrix_collection.query(
    query_texts=["What is the Matrix?"],
    where={"speaker": "Morpheus"},
    n_results=2,
)

print(results)
```

ChromaDB supports filtering queries by metadata using where filters. In this example, we query the collection with a query text "What is the Matrix?" and filter the results based on the speaker being "Morpheus".

The `query` method takes a `where` parameter, which is a dictionary specifying the metadata field and its corresponding value for filtering. The results will include only the items that match the specified criteria.

### Use cases for using where filters include:

- **Metadata-based Filtering**: You can filter items based on specific metadata fields, such as speaker, category, or any other relevant criteria.
- **Targeted Analysis**: By filtering the results using where filters, you can perform targeted analysis or operations on specific subsets of the data that meet certain metadata criteria.

> Feel free to modify the where filters in the `query` method to explore different filtering options. Experiment with different metadata fields and values to see how ChromaDB allows you to filter and query items based on specific metadata criteria.