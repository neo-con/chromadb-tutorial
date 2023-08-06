# Deleting Items from a Collection by ID in ChromaDB

This tutorial will guide you through deleting items from a collection by their IDs in ChromaDB.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `trinity`.

2. **Adding Raw Documents**

    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID.

3. **Deleting Items from a Collection by ID**

    We can delete specific items from the collection by their IDs using the `delete` method. In this example, we delete the item with the ID "quote_3".

    The `delete` method removes the specified items from the collection permanently.

    Use cases for deleting items by ID include:

    - **Data Management**: You can remove specific items from the collection to manage and maintain the data in ChromaDB.
    - **Data Cleanup**: Deleting items by ID allows you to clean up the collection and remove unwanted or outdated data.

    Feel free to modify the IDs in the `delete` method to delete different items from the collection.

    After deleting the item, we retrieve the remaining items from the collection using the `get` method to verify the deletion.

Please refer to the `delete_by_id.py` file for the complete Python code used in this tutorial.