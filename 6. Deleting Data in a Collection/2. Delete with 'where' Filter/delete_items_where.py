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
        "It seems that you've been living two lives.",
        "I believe that, as a species, human beings define their reality through misery and suffering",
        "Human beings are a disease, a cancer of this planet.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4", "quote_5", "quote_6"],
)

# Deleting items that match the where filter
matrix_collection.delete(where={"speaker": "Agent Smith"})

# Counting items in the collection after deletion
item_count = matrix_collection.count()
print(f"Count of items in collection: {item_count}")
