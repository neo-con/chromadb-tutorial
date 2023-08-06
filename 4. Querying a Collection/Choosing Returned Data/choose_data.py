import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
morpheus_collection = client.create_collection(name="morpheus")

# Add the raw documents
morpheus_collection.add(
    documents=[
        "This is your last chance. After this, there is no turning back.",
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Query the collection by text and choose which data is returned
results = morpheus_collection.query(
    query_texts=["take the red pill"], n_results=1, include=["distances", "embeddings"]
)

print(results)
