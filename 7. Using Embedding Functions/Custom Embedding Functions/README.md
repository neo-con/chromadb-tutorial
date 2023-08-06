# Using Custom Embedding Functions in ChromaDB

This tutorial will guide you through using a custom embedding function with a collection in ChromaDB.

1. **Defining a Custom Embedding Function**

    We start by defining a custom embedding function that implements the `EmbeddingFunction` protocol. This function takes a list of texts and returns a list of embeddings. For simplicity, in our example, the embedding of a text is just the length of the text. THIS IS NOT A VALID EMBEDDING FUNCTION.

2. **Creating a Collection with a Custom Embedding Function**

    We initialize the ChromaDB client and create a collection named `neo`, passing our custom embedding function to the `create_collection` method.

3. **Adding Raw Documents**

    We add two famous quotes from "The Matrix" to our collection using the `add` method. Each document is associated with a unique id. Since we have supplied a custom embedding function to our collection, ChromaDB will use this function to generate the embeddings for our documents.

4. **Retrieving Items from a Collection**

    We can retrieve all items from a collection using the `get` method. This will return a dictionary with the ids, embeddings, metadatas, and documents of the items in the collection. You will notice that the embeddings are just the lengths of the texts, as defined by our custom embedding function.

Custom embedding functions can be very useful when you want to define your own method of converting texts into numerical representations. For example, you might want to use a specific Natural Language Processing (NLP) technique, or you might have a domain-specific method of generating embeddings.

Please refer to the `custom_emb_func.py` file for the complete Python code used in this tutorial.