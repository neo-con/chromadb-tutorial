# Using OpenAI Embedding Function in ChromaDB

This tutorial will guide you through using the OpenAI embedding function in ChromaDB.

1. **Creating a Collection with OpenAI Embedding Function**

    We start by initializing the ChromaDB client and the OpenAI embedding function. For the OpenAI embedding function, you need to provide your OpenAI API key and the model name. In this example, we use the "text-embedding-ada-002" model.

    We then create a collection named `matrix` with the OpenAI embedding function.

2. **Adding Raw Documents**

    We add two famous quotes from "The Matrix" to our collection using the `add` method. Each document is associated with a unique id. Since we have set the OpenAI embedding function for our collection, Chroma will automatically use it to embed these documents.

3. **Querying by a Set of Query Texts**

    We can query the collection by a set of query texts using the `query` method. Chroma will first embed each query text with the collection's embedding function (in this case, the OpenAI embedding function), and then perform the query with the generated embedding. In this example, we query the collection with the text "What is the Matrix?" and ask for two results.

Please refer to the `openai_emb_func.py` file for the complete Python code used in this tutorial.
