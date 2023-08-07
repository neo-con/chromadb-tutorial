# Using OpenAI Embedding Function in ChromaDB

This tutorial will guide you through using the OpenAI embedding function in ChromaDB.

❗ Before diving into the tutorial, ensure that you have the required openai Python package installed. If you haven't, you can quickly install it using pip:

```pip install openai```

Once you have `openai` installed, follow the steps below to use the OpenAI embedding function in ChromaDB.

1. **Creating a Collection with OpenAI Embedding Function**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/7.%20Using%20Embedding%20Functions/1.%20OpenAI/openai_emb_func.py#L4-L11
    We start by initializing the ChromaDB client and the OpenAI embedding function. For the OpenAI embedding function, you need to provide your OpenAI API key and the model name. In this example, we use the "text-embedding-ada-002" model.

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/7.%20Using%20Embedding%20Functions/1.%20OpenAI/openai_emb_func.py#L13-L17
    We then create a collection named `matrix` with the OpenAI embedding function.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/7.%20Using%20Embedding%20Functions/1.%20OpenAI/openai_emb_func.py#L19-L27
    We add two famous quotes from "The Matrix" to our collection using the `add` method. Each document is associated with a unique id. Since we have set the OpenAI embedding function for our collection, Chroma will automatically use it to embed these documents.

3. **Querying by a Set of Query Texts**

    https://github.com/neo-con/chromadb-tutorial/blob/12ffea8f20af03de10dbec0f7bcd02b888f6b402/7.%20Using%20Embedding%20Functions/1.%20OpenAI/openai_emb_func.py#L29-L32
    We can query the collection by a set of query texts using the `query` method. Chroma will first embed each query text with the collection's embedding function (in this case, the OpenAI embedding function), and then perform the query with the generated embedding. In this example, we query the collection with the text "What is the Matrix?" and ask for two results.

Please refer to the `openai_emb_func.py` file for the complete Python code used in this tutorial.
