import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
morpheus_collection = client.create_collection(
    name="morpheus", metadata={"hnsw:space": "cosine"}
)

# Add the raw documents
morpheus_collection.add(
    documents=[
        "This is your last chance. After this, there is no turning back.",
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Querying by a set of query_texts
results = morpheus_collection.query(
    query_texts=["Take the red pill"],
    n_results=2,
)

print(results)
