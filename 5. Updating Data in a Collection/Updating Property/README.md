# Updating Data in a Collection - Updating Any Property of Items in a Collection

This tutorial will guide you through updating any property of items in a collection in ChromaDB.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Updating Items in the Collection**

    ChromaDB allows us to update any property of items in a collection using the `update` method. In this example, we update the metadata and document of an item with the ID "quote_2". We change the speaker from "Morpheus" to "Neo" and update the document text.

4. **Retrieving Updated Items from the Collection**

    We can retrieve the updated item from the collection using the `get` method. In this case, we retrieve the item with the ID "quote_2" to see the changes.

    Use cases for updating data in a collection include:

    - **Correcting or Modifying Existing Data**: If there are errors or changes in the metadata or documents, you can update the items in the collection to reflect the corrected or modified information.
    - **Keeping Data Up-to-Date**: As new information becomes available, you can update the items in the collection to ensure that the data remains accurate and relevant.

    Feel free to modify the update parameters in the `update` method to experiment with updating different properties of items in the collection.