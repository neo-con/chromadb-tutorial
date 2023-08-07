# Deleting Data from a Collection in ChromaDB

This tutorial will guide you through deleting data from a collection in ChromaDB.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/2.%20Delete%20with%20'where'%20Filter/delete_items_where.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/2.%20Delete%20with%20'where'%20Filter/delete_items_where.py#L9-L28
    We add six raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Deleting Items that Match the Where Filter**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/2.%20Delete%20with%20'where'%20Filter/delete_items_where.py#L30-L31
    ChromaDB allows you to delete items from a collection that match specific criteria using the `delete` method. In this example, we delete all items from the collection where the speaker is "Agent Smith".

    The `delete` method takes a `where` parameter, which is a dictionary specifying the metadata field and its corresponding value for filtering. All items that match the specified criteria will be deleted from the collection.

    💡 Use cases for deleting data from a collection include:

    >- **Data Cleanup**: You can delete specific items or subsets of data from a collection to keep your data clean and up-to-date.
    >- **Data Privacy**: In cases where certain data needs to be removed for privacy or compliance reasons, the `delete` method allows you to selectively remove sensitive information from the collection.

    Feel free to modify the where filter in the `delete` method to delete items based on different metadata criteria.

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/6.%20Deleting%20Data%20in%20a%20Collection/2.%20Delete%20with%20'where'%20Filter/delete_items_where.py#L33-L35
    After deletion, you can count the remaining items in the collection using the `count` method to verify the changes.