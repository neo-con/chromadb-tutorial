import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
trinity_collection = client.create_collection(name="trinity")

# Add the raw documents
trinity_collection.add(
    documents=[
        "I know why you're here, Neo.",
        "The answer is out there, Neo. It's looking for you. And it will find you if you want it to.",
        "Neo, no one has ever done this before.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Delete items from the collection by id
trinity_collection.delete(ids=["quote_3"])

# Retrieve items from the collection
items = trinity_collection.get()

print(items)