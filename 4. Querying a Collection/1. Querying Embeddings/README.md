# Querying a Collection by a Set of Query Embeddings in ChromaDB

This tutorial will guide you through querying a collection by a set of query embeddings in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
neo_collection = client.create_collection(name="neo")
```

We start by initializing the ChromaDB client and creating a collection named `neo`.

## 2. Adding Embeddings and Metadata

```python
neo_collection.add(
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    metadatas=[{"quote": "I know kung fu."}, {"quote": "There is no spoon."}],
    ids=["quote_1", "quote_2"]
)
```

We add two **hypothetical embeddings** and associated metadata (famous quotes from "The Matrix") to our collection using the `add` method. Each embedding and metadata is associated with a unique id.

## 3. Querying by a Set of Query Embeddings

```python
results = neo_collection.query(
    query_embeddings=[[0.1, 0.2, 0.3]],
    n_results=1
)

print(results)
```

We can query the collection by a set of query embeddings using the `query` method. This will return the closest matches to each query embedding. In this example, we query the collection with one of the embeddings we added earlier and ask for one result.

You will notice that the distance returned in the results is `0`. This is because the query embedding is exactly the same as one of the embeddings in the collection. The distance is a measure of how similar the query embedding is to the embeddings in the collection:

- A distance of `0` means the embeddings are identical
- Larger distances indicate less similarity

> **Note:** Feel free to experiment with the numbers in the query embedding to see how the distance changes. Remember, the closer the distance is to `0`, the more similar the query embedding is to the embeddings in the collection.