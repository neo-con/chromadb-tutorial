# Using Custom Embedding Functions in ChromaDB

This tutorial demonstrates how to use a custom embedding function with a collection in ChromaDB.

## 1. Importing Required Libraries

First, let's import the necessary libraries:

```python
import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
```

## 2. Defining a Custom Embedding Function

We'll create a custom embedding function that implements the `EmbeddingFunction` protocol:

```python
class SimpleEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        return [[len(text)] for text in texts]
```

This function takes a list of texts and returns a list of embeddings. For simplicity, our example uses the length of each text as its embedding.

> ⚠️ **WARNING**: This is not a valid embedding function for real-world use. It's a simplified example for demonstration purposes only.

## 3. Creating a Collection with a Custom Embedding Function

Now, let's initialize the ChromaDB client and create a collection:

```python
client = chromadb.Client()
matrix_quotes = client.create_collection(
    name="matrix_quotes",
    embedding_function=SimpleEmbeddingFunction()
)
```

## 4. Adding Documents to the Collection

We'll add some famous quotes from "The Matrix" to our collection:

```python
matrix_quotes.add(
    documents=[
        "I know kung fu.",
        "There is no spoon.",
        "The Matrix has you.",
        "Follow the white rabbit."
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4"]
)
```

## 5. Retrieving Items from the Collection

Let's retrieve the items and their embeddings from the collection:

```python
items = matrix_quotes.get(include=['embeddings', 'documents'])
for item in items['ids']:
    index = items['ids'].index(item)
    print(f"ID: {item}")
    print(f"Document: {items['documents'][index]}")
    print(f"Embedding: {items['embeddings'][index]}")
    print("---")
```

## 6. Querying the Collection

Finally, let's perform a query on our collection:

```python
results = matrix_quotes.query(
    query_texts=["What do you know?"],
    n_results=2
)
print("Query Results:")
print(results)
```

---

Custom embedding functions are powerful tools when you need to define your own method of converting texts into numerical representations. They can be particularly useful for domain-specific applications or when you want to use a specific NLP technique.

For the complete Python code used in this tutorial, please refer to the `custom_emb_func.py` file.