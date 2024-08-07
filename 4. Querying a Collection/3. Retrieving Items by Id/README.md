# Retrieving Items from a Collection by ID in ChromaDB

This tutorial will guide you through retrieving items from a collection by their IDs in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
trinity_collection = client.create_collection(name="trinity")
```

We start by initializing the ChromaDB client and creating a collection named `trinity`.

## 2. Adding Raw Documents

```python
trinity_collection.add(
    documents=[
        "Dodge this.",
        "I think they're trying to tell us something.",
        "Neo, no one has ever done this before.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)
```

We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID.

## 3. Retrieving Items from a Collection by ID

```python
items = trinity_collection.get(ids=["quote_1", "quote_3"])
print(items)
```

We can retrieve specific items from the collection by their IDs using the `get` method. In this example, we retrieve items with the IDs "quote_1" and "quote_3".

The `get` method returns a dictionary with the IDs, embeddings, metadatas, and documents of the retrieved items.

### Use Cases for Retrieving Items by ID

- **Specific Document Retrieval**: If you have the IDs of specific documents you want to retrieve, you can use the `get` method to fetch those documents from the collection.
- **Data Validation**: You can use the `get` method to validate the existence and retrieve specific items based on their IDs, ensuring the integrity of your data.
- **Selective Analysis**: By retrieving specific items from the collection, you can perform targeted analysis or operations on those particular documents.

> **Tip**: Feel free to modify the IDs in the `get` method to retrieve different items from the collection. Experiment with different IDs to explore how ChromaDB allows you to retrieve specific items based on their unique identifiers.