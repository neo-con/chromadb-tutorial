# Adding Embeddings and Metadata to Collections in ChromaDB

This tutorial will guide you through adding embeddings and metadata to a collection in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
locations_collection = client.create_collection(name="locations")
```

We start by initializing the ChromaDB client and creating a collection named `locations`.

## 2. Adding Embeddings and Metadata

```python
locations_collection.add(
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    metadatas=[
        {"location": "Zion", "description": "Last human city"},
        {"location": "Machine City", "description": "City inhabited by machines"},
    ],
    ids=["loc_1", "loc_2"],
)
```

We add two **hypothetical embeddings** (representing coordinates) and associated metadata (information about locations in the Matrix universe) to our collection using the `add` method. Each embedding and metadata is associated with a unique id.

💡 Adding just metadata and no documents can be useful in several scenarios:

- **External Document Storage**: The actual documents might be stored in an external system due to their size or for security reasons. In this case, the metadata can include a reference or a link to the actual document in the external system.
- **Privacy Concerns**: In some cases, due to privacy concerns or regulations, the actual documents cannot be stored. However, the metadata, which does not contain sensitive information, can be stored and used for analysis.
- **Efficiency**: Storing and retrieving metadata can be more efficient than dealing with large documents, especially when the documents are not needed for the analysis or operations being performed.
- **Pre-processed Data**: In some cases, the documents might have been pre-processed into a more useful form (like embeddings) and the original documents are no longer needed. The metadata can provide additional context for the pre-processed data.

## 3. Counting Items in a Collection

```python
item_count = locations_collection.count()
print(f"Count of items in collection: {item_count}")
```

We can count the number of items in a collection using the `count` method. Since we have added two embeddings to our collection, the count returns `2`.

## 4. Retrieving Items from a Collection

```python
items = locations_collection.get()
print(items)
```

We can retrieve all items from a collection using the `get` method. By default, this will return a dictionary with the ids, metadatas, and documents (in our case, None) of the items in the collection.

Please refer to the `add_emb_meta.py` file for the complete Python code used in this tutorial.