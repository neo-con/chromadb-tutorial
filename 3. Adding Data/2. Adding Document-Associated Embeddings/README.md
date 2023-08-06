# Adding Document-Associated Embeddings to Collections in ChromaDB

This tutorial will guide you through adding document-associated embeddings to a collection in ChromaDB.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `morpheus`.

2. **Adding Document-Associated Embeddings**

    We add two famous quotes from the character Morpheus in "The Matrix" to our collection using the `add` method. Each document is associated with a unique id and an embedding. The embeddings are lists of numbers that represent the semantic content of the documents. Please note that in this example, we are using hypothetical embeddings for illustrative purposes.

3. **Counting Items in a Collection**

    We can count the number of items in a collection using the `count` method. Since we have added two documents to our collection, the count returns `2`.

4. **Retrieving Items from a Collection**

    We can retrieve all items from a collection using the `get` method. By default, this will return a dictionary with the ids, metadatas (if included) and documents of the items in the collection.

Please refer to the `add_doc_emb.py` file for the complete Python code used in this tutorial.