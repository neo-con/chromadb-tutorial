# Adding Document-Associated Embeddings to Collections in ChromaDB

This tutorial will guide you through adding document-associated embeddings to a collection in ChromaDB.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/2.%20Adding%20Document-Associated%20Embeddings/add_doc_emb.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `morpheus`.

2. **Adding Document-Associated Embeddings**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/2.%20Adding%20Document-Associated%20Embeddings/add_doc_emb.py#L9-L17
    We add two famous quotes from the character Morpheus to our collection using the `add` method. Each document is associated with a unique id and an embedding. The embeddings are lists of numbers that represent the semantic content of the documents. Please note that in this example, we are using hypothetical embeddings for illustrative purposes.

3. **Counting Items in a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/2.%20Adding%20Document-Associated%20Embeddings/add_doc_emb.py#L19-L21
    We can count the number of items in a collection using the `count` method. Since we have added two documents to our collection, the count returns `2`.

4. **Retrieving Items from a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/2.%20Adding%20Document-Associated%20Embeddings/add_doc_emb.py#L23-L25
    We can retrieve all items from a collection using the `get` method. By default, this will return a dictionary with the ids, metadatas (if included) and documents of the items in the collection.

Please refer to the `add_doc_emb.py` file for the complete Python code used in this tutorial.