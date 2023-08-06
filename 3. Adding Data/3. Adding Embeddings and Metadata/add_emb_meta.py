import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
locations_collection = client.create_collection(name="locations")

# Adding embeddings and metadata
locations_collection.add(
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    metadatas=[
        {"location": "Zion", "description": "Last human city"},
        {"location": "Machine City", "description": "City inhabited by machines"},
    ],
    ids=["loc_1", "loc_2"],
)

# Counting items in a collection
item_count = locations_collection.count()
print(f"Count of items in collection: {item_count}")

# Get items from the collection
items = locations_collection.get()
print(items)
