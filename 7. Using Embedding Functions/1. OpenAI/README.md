# Using OpenAI Embedding Function in ChromaDB

This tutorial will guide you through using the OpenAI embedding function in ChromaDB.

> ❗ Before diving into the tutorial, ensure that you have the required `openai` Python package installed. If you haven't, you can quickly install it using pip:

```bash
pip install openai
```

Once you have `openai` installed, follow the steps below to use the OpenAI embedding function in ChromaDB.

## 1. Creating a Collection with OpenAI Embedding Function

First, we need to initialize the ChromaDB client and the OpenAI embedding function. For the OpenAI embedding function, you need to provide your OpenAI API key and the model name. In this example, we use the "text-embedding-3-small" model.

```python
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

# Initialize ChromaDB client
client = chromadb.Client()

# Initialize OpenAI embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="USE YOUR OPEN-AI KEY",
    model_name="text-embedding-3-small",
)

# Create the collection with the OpenAI embedding function
matrix_collection = client.create_collection(
    name="matrix",
    embedding_function=openai_ef,
)
```

## 2. Adding Raw Documents

Next, we add three famous quotes from "The Matrix" to our collection using the `add` method. Each document is associated with a unique id. Since we have set the OpenAI embedding function for our collection, Chroma will automatically use it to embed these documents.

```python
matrix_collection.add(
    documents=[
        "The Matrix is all around us.",
        "What you know you can't explain, but you feel it",
        "There is a difference between knowing the path and walking the path",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)
```

## 3. Querying by a Set of Query Texts

We can query the collection by a set of query texts using the `query` method. Chroma will first embed each query text with the collection's embedding function (in this case, the OpenAI embedding function), and then perform the query with the generated embedding. In this example, we query the collection with the text "What is the Matrix?" and ask for two results.

```python
results = matrix_collection.query(query_texts=["What is the Matrix?"], n_results=2)
print(results)
```

Please refer to the complete Python code used in this tutorial for a full implementation.
