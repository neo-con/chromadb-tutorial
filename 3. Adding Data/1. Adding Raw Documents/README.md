# Adding Raw Documents to Collections in ChromaDB

This tutorial will guide you through adding raw documents to a collection in ChromaDB.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/1.%20Adding%20Raw%20Documents/adding_raw_docs.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `neo`.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/1.%20Adding%20Raw%20Documents/adding_raw_docs.py#L9-L12
    We add two famous quotes from "The Matrix" to our collection using the `add` method. Each document is associated with a unique id. Importantly, when embeddings are not passed to the `add` method, ChromaDB automatically embeds these documents for us. By default, ChromaDB uses sentence transformer for embedding if no specific embedding function is supplied during the collection creation.

3. **Counting Items in a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/1.%20Adding%20Raw%20Documents/adding_raw_docs.py#L14-L16
    We can count the number of items in a collection using the `count` method. Since we have added two documents to our collection, the count returns `2`.

4. **Retrieving Items from a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/1.%20Adding%20Raw%20Documents/adding_raw_docs.py#L18-L20
    We can retrieve all items from a collection using the `get` method. By default, this will return a dictionary with the ids, metadatas (if included), and documents of the items in the collection.

4. **Take a peek at a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/630e85d7be622f180784c25b9ae2e275844f9e4d/3.%20Adding%20Data/1.%20Adding%20Raw%20Documents/adding_raw_docs.py#L22-L23
    We can also use the `peek` method to return the first 10 items from a collection. By default, this will return a dictionary with the ids, metadatas (if provided) and documents of the items in the collection. The main difference in `peek` and `get` methods is that the `get` method allows for more arguments, whereas the `peek` method only takes `limit`, which is simply the the number of results to return.

Please refer to the `adding_raw_docs.py` file for the complete Python code used in this tutorial.