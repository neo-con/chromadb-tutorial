# Upsert Operation in ChromaDB

This tutorial will guide you through performing an upsert operation in ChromaDB to update existing items or add new items to a collection.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/5.%20Updating%20Data%20in%20a%20Collection/2.%20Upsert%20Operation/upsert_operation.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/5.%20Updating%20Data%20in%20a%20Collection/2.%20Upsert%20Operation/upsert_operation.py#L9-L22
    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Upsert Operation**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/5.%20Updating%20Data%20in%20a%20Collection/2.%20Upsert%20Operation/upsert_operation.py#L24-L35
    ChromaDB supports the upsert operation, which allows us to update existing items or add new items to a collection. In this example, we perform an upsert operation on two items with IDs "quote_2" and "quote_4".

    The `upsert` method takes the IDs, embeddings, metadatas, and documents of the items to be updated or added. If an ID already exists in the collection, the corresponding item will be updated. If an ID does not exist, a new item will be added.

4. **Retrieving Updated Items from the Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/5.%20Updating%20Data%20in%20a%20Collection/2.%20Upsert%20Operation/upsert_operation.py#L37-L40
    We can retrieve the updated item from the collection using the `get` method. In this case, we retrieve the newly upserted items with the ID "quote_2" and "quote_4" to see the changes.

    💡 Use cases for the upsert operation include:

    >- **Updating Existing Items**: You can update specific items in the collection by providing their IDs along with the updated embeddings, metadatas, and documents.
    >- **Adding New Items**: You can add new items to the collection by providing their IDs along with the corresponding embeddings, metadatas, and documents.

    Feel free to modify the IDs, embeddings, metadatas, and documents in the `upsert` method to update existing items or add new items to the collection.