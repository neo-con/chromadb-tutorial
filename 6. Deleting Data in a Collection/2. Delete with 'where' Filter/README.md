# Deleting Data from a Collection in ChromaDB

This tutorial will guide you through deleting data from a collection in ChromaDB.

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
matrix_collection.add(
    documents=[
        "The Matrix is everywhere, it is all around us.",
        "You can see it when you look out your window or when you turn on your television.",
        "You can feel it when you go to work, when you go to church, when you pay your taxes.",
        "It seems that you've been living two lives.",
        "I believe that, as a species, human beings define their reality through misery and suffering",
        "Human beings are a disease, a cancer of this planet.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4", "quote_5", "quote_6"],
)
```

We add six raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

## 3. Deleting Items that Match the Where Filter

```python
matrix_collection.delete(where={"speaker": "Agent Smith"})
```

ChromaDB allows you to delete items from a collection that match specific criteria using the `delete` method. In this example, we delete all items from the collection where the speaker is "Agent Smith".

The `delete` method takes a `where` parameter, which is a dictionary specifying the metadata field and its corresponding value for filtering. All items that match the specified criteria will be deleted from the collection.

### Use cases for deleting data from a collection include:

- **Data Cleanup**: You can delete specific items or subsets of data from a collection to keep your data clean and up-to-date.
- **Data Privacy**: In cases where certain data needs to be removed for privacy or compliance reasons, the `delete` method allows you to selectively remove sensitive information from the collection.

> Feel free to modify the where filter in the `delete` method to delete items based on different metadata criteria.

```python
# Counting items in the collection after deletion
item_count = matrix_collection.count()
print(f"Count of items in collection: {item_count}")
```

After deletion, you can count the remaining items in the collection using the `count` method to verify the changes.