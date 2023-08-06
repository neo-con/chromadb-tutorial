import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create the collection
matrix_collection = client.create_collection(name="matrix")

# Add the raw documents
matrix_collection.add(
    documents=[
        "The Matrix is everywhere, it is all around us.",
        "You can see it when you look out your window or when you turn on your television.",
        "You can feel it when you go to work, when you go to church, when you pay your taxes.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Update items in the collection
matrix_collection.update(
    ids=["quote_2"],
    metadatas=[{"category": "quote", "speaker": "Morpheus"}],
    documents=["The Matrix is a system, Neo. That system is our enemy."],
)

# Retrieve updated items from the collection
items = matrix_collection.get(ids=["quote_2"])

print(items)