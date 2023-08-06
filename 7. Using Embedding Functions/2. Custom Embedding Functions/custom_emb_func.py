import chromadb
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

# Define a custom embedding function
class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        # For simplicity, let's just use the length of each text as the embedding
        # NOT AN ACTUAL CUSTOM EMBEDDING
        return [[len(text)] for text in texts]

# Initialize ChromaDB client
client = chromadb.Client()

# Create a collection with the custom embedding function
neo_collection = client.create_collection(name="neo", embedding_function=MyEmbeddingFunction())

# Adding raw documents
neo_collection.add(
    documents=["I know kung fu.", "There is no spoon."],
    ids=["quote_1", "quote_2"]
)

# Get items from the collection
items = neo_collection.get(include=['embeddings'])
print(items)