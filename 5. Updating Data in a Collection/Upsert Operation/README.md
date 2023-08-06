# Upsert Operation in ChromaDB

This tutorial will guide you through performing an upsert operation in ChromaDB to update existing items or add new items to a collection.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Upsert Operation**

    ChromaDB supports the upsert operation, which allows us to update existing items or add new items to a collection. In this example, we perform an upsert operation on two items with IDs "quote_2" and "quote_4".

    The `upsert` method takes the IDs, embeddings, metadatas, and documents of the items to be updated or added. If an ID already exists in the collection, the corresponding item will be updated. If an ID does not exist, a new item will be added.

    Use cases for the upsert operation include:

    - **Updating Existing Items**: You can update specific items in the collection by providing their IDs along with the updated embeddings, metadatas, and documents.
    - **Adding New Items**: You can add new items to the collection by providing their IDs along with the corresponding embeddings, metadatas, and documents.

    Feel free to modify the IDs, embeddings, metadatas, and documents in the `upsert` method to update existing items or add new items to the collection.