import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
neo_collection = client.create_collection(name="neo")

# Adding embeddings and metadata
neo_collection.add(
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    metadatas=[{"quote": "I know kung fu."}, {"quote": "There is no spoon."}],
    ids=["quote_1", "quote_2"]
)

# Querying by a set of query_embeddings
results = neo_collection.query(
    query_embeddings=[[0.6, 0.1, 0.9]],
    n_results=1
)

print(results)