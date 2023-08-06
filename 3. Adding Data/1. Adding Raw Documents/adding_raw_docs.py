import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
neo_collection = client.create_collection(name="neo")

# Adding raw documents
neo_collection.add(
    documents=["I know kung fu.", "There is no spoon."], ids=["quote_1", "quote_2"]
)

# Counting items in a collection
item_count = neo_collection.count()
print(f"Count of items in collection: {item_count}")

# Get items from the collection
items = neo_collection.get()
print(items)

# Or we can use the peek method
neo_collection.peek(limit=5)
