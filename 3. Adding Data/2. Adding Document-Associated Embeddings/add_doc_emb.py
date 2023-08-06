import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
morpheus_collection = client.create_collection(name="morpheus")

# Adding document-associated embeddings
morpheus_collection.add(
    documents=[
        "What if I told you everything you knew was a lie.",
        "Welcome to the real world.",
    ],
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    ids=["quote_1", "quote_2"],
)

# Counting items in a collection
item_count = morpheus_collection.count()
print(f"Count of items in collection: {item_count}")

# Get items from the collection
items = morpheus_collection.get()
print(items)
