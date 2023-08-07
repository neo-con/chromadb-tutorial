# Deleting Items from a Collection by ID in ChromaDB

This tutorial will guide you through deleting items from a collection by their IDs in ChromaDB.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/1.%20Delete%20by%20ID/delete_by_id.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `trinity`.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/1.%20Delete%20by%20ID/delete_by_id.py#L9-L17
    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID.

3. **Deleting Items from a Collection by ID**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/1.%20Delete%20by%20ID/delete_by_id.py#L19-L20
    We can delete specific items from the collection by their IDs using the `delete` method. In this example, we delete the item with the ID "quote_3".

    The `delete` method removes the specified items from the collection permanently.

    💡 Use cases for deleting items by ID include:

    >- **Data Management**: You can remove specific items from the collection to manage and maintain the data in ChromaDB.
    >- **Data Cleanup**: Deleting items by ID allows you to clean up the collection and remove unwanted or outdated data.

    Feel free to modify the IDs in the `delete` method to delete different items from the collection.

    After deleting the item, we retrieve the remaining items from the collection using the `get` method to verify the deletion.

Please refer to the `delete_by_id.py` file for the complete Python code used in this tutorial.