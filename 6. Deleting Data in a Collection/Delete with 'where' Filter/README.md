# Deleting Data from a Collection in ChromaDB

This tutorial will guide you through deleting data from a collection in ChromaDB.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    We add six raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Deleting Items that Match the Where Filter**

    ChromaDB allows you to delete items from a collection that match specific criteria using the `delete` method. In this example, we delete all items from the collection where the speaker is "Agent Smith".

    The `delete` method takes a `where` parameter, which is a dictionary specifying the metadata field and its corresponding value for filtering. All items that match the specified criteria will be deleted from the collection.

    Use cases for deleting data from a collection include:

    - **Data Cleanup**: You can delete specific items or subsets of data from a collection to keep your data clean and up-to-date.
    - **Data Privacy**: In cases where certain data needs to be removed for privacy or compliance reasons, the `delete` method allows you to selectively remove sensitive information from the collection.

    Feel free to modify the where filter in the `delete` method to delete items based on different metadata criteria.

    After deletion, you can count the remaining items in the collection using the `count` method to verify the changes.