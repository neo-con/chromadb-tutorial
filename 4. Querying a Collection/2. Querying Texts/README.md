# Querying by a Set of Query Texts in ChromaDB

This tutorial will guide you through querying a collection in ChromaDB using a set of query texts as input, demonstrating semantic search capabilities.

## 1. Creating a Collection

```python
client = chromadb.Client()

morpheus_collection = client.create_collection(
    name="morpheus", metadata={"hnsw:space": "cosine"}
)
```

We start by initializing the ChromaDB client and creating a collection named `morpheus`. We set the distance function to `"cosine"` for this collection, which is suitable for semantic similarity searches.

## 2. Adding Raw Documents

```python
morpheus_collection.add(
    documents=[
        "This is your last chance. After this, there is no turning back.",
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)
```

We add three raw documents (famous quotes from "The Matrix") to our collection using the `add` method. Each document is associated with a unique id.

## 3. Querying by a Set of Query Texts

```python
results = morpheus_collection.query(
    query_texts=["Make a choice"],
    n_results=2,
)

print(results)
```

We can query the collection using semantic search with the `query` method. This will return the closest matches based on meaning, not just exact text matching. In this example, we query the collection with the text "Tell me about making a choice". We specify that we want to retrieve 2 results (`n_results=2`).

The results will include the ids, metadatas (if provided), and documents of the semantically closest matches. The order of the results is based on their semantic similarity to the query text, with the most relevant results appearing first.

> **Note:** This example demonstrates semantic search. The query "Make a choice" doesn't appear verbatim in any of the documents, but ChromaDB will return the most semantically relevant results.

Please refer to the `query_by_texts.py` file for the complete Python code used in this tutorial.