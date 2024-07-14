# Upsert Operation in ChromaDB

This tutorial will guide you through performing an upsert operation in ChromaDB to update existing items or add new items to a collection.

## 1. Creating a Collection

```python
import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
matrix_collection = client.create_collection(name="matrix")
```

We start by initializing the ChromaDB client and creating a collection named `matrix`.

## 2. Adding Raw Documents

```python
# Add the raw documents
matrix_collection.add(
    documents=[
        "The Matrix is everywhere, it is all around us.",
        "You can see it when you look out your window or when you turn on your television.",
        "You can feel it when you go to work, when you go to church, when you pay your taxes.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)
```

We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

## 3. Upsert Operation

```python
# Upsert operation
matrix_collection.upsert(
    ids=["quote_2", "quote_4"],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    documents=[
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "I'm going to enjoy watching you die, Mr. Anderson.",
    ],
)
```

ChromaDB supports the upsert operation, which allows us to update existing items or add new items to a collection. In this example, we perform an upsert operation on two items with IDs "quote_2" and "quote_4".

The `upsert` method takes the IDs, embeddings, metadatas, and documents of the items to be updated or added. If an ID already exists in the collection, the corresponding item will be updated. If an ID does not exist, a new item will be added.

## 4. Retrieving Updated Items from the Collection

```python
# Retrieve updated items from the collection
items = matrix_collection.get(ids=["quote_2", "quote_4"])

print(items)
```

We can retrieve the updated item from the collection using the `get` method. In this case, we retrieve the newly upserted items with the ID "quote_2" and "quote_4" to see the changes.

### Use cases for the upsert operation include:

- **Updating Existing Items**: You can update specific items in the collection by providing their IDs along with the updated embeddings, metadatas, and documents.
- **Adding New Items**: You can add new items to the collection by providing their IDs along with the corresponding embeddings, metadatas, and documents.

> Feel free to modify the IDs, embeddings, metadatas, and documents in the `upsert` method to update existing items or add new items to the collection.