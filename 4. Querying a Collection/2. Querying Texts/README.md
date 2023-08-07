# Querying by a Set of Query Texts in ChromaDB

This tutorial will guide you through querying a collection in ChromaDB using a set of query texts as input.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/2.%20Querying%20Texts/query_texts.py#L3-L9
    We start by initializing the ChromaDB client and creating a collection named `morpheus`. We also set the distance function to `"cosine"` for this collection.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/2.%20Querying%20Texts/query_texts.py#L11-L19
    We add three raw documents (famous quotes from "The Matrix") to our collection using the `add` method. Each document is associated with a unique id.

3. **Querying by a Set of Query Texts**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/2.%20Querying%20Texts/query_texts.py#L21-L27
    We can query the collection by a set of query texts using the `query` method. This will return the closest matches to each query text. In this example, we query the collection with the text "Take the red pill". We specify that we want to retrieve 2 results (`n_results=2`).

    The results will include the ids, metadatas (if provided), and documents of the closest matches. The order of the results is based on their similarity to the query text, with the most similar results appearing first.

    Feel free to modify the query text and the number of results to see different outcomes. 

Please refer to the `query_by_texts.py` file for the complete Python code used in this tutorial.
