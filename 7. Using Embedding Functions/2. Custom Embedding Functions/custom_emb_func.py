import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

# Define a custom embedding function
class SimpleEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        # For simplicity, we're using the length of each text as its embedding
        # NOTE: This is not a valid embedding function for real-world use!
        return [[len(text)] for text in texts]

# Initialize ChromaDB client
client = chromadb.Client()

# Create a collection with the custom embedding function
matrix_quotes = client.create_collection(
    name="matrix_quotes",
    embedding_function=SimpleEmbeddingFunction()
)

# Add documents to the collection
matrix_quotes.add(
    documents=[
        "I know kung fu.",
        "There is no spoon.",
        "The Matrix has you.",
        "Follow the white rabbit."
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4"]
)

# Retrieve items from the collection
items = matrix_quotes.get(include=['embeddings', 'documents'])

# Print each item's details
for item in items['ids']:
    index = items['ids'].index(item)
    print(f"ID: {item}")
    print(f"Document: {items['documents'][index]}")
    print(f"Embedding: {items['embeddings'][index]}")
    print("---")

# Perform a query on the collection
results = matrix_quotes.query(
    query_texts=["What do you know?"],
    n_results=2
)

# Print query results
print("Query Results:")
print(results)