import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
trinity_collection = client.create_collection(name="trinity")

# Add the raw documents
trinity_collection.add(
    documents=[
        "Dodge this.",
        "I think they're trying to tell us something.",
        "Neo, no one has ever done this before.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Retrieve items from the collection by id
items = trinity_collection.get(ids=["quote_1", "quote_3"])

print(items)