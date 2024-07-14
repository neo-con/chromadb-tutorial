# Updating Data in a Collection: Updating Any Property of Items in a Collection

This tutorial will guide you through updating any property of items in a collection in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
matrix_collection = client.create_collection(name="matrix")
```

We start by initializing the ChromaDB client and creating a collection named `matrix`.

## 2. Adding Raw Documents

```python
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

## 3. Updating Items in the Collection

```python
matrix_collection.update(
    ids=["quote_2"],
    metadatas=[{"category": "quote", "speaker": "Morpheus"}],
    documents=["The Matrix is a system, Neo. That system is our enemy."],
)
```

ChromaDB allows us to update any property of items in a collection using the `update` method. In this example, we update the metadata and document of an item with the ID "quote_2". We keep the speaker as "Morpheus" and update the document text.

## 4. Retrieving Updated Items from the Collection

```python
items = matrix_collection.get(ids=["quote_2"])
print(items)
```

We can retrieve the updated item from the collection using the `get` method. In this case, we retrieve the item with the ID "quote_2" to see the changes.

### Use Cases for Updating Data in a Collection

- **Correcting or Modifying Existing Data**: If there are errors or changes in the metadata or documents, you can update the items in the collection to reflect the corrected or modified information.
- **Keeping Data Up-to-Date**: As new information becomes available, you can update the items in the collection to ensure that the data remains accurate and relevant.

> **Tip**: Feel free to modify the update parameters in the `update` method to experiment with updating different properties of items in the collection.