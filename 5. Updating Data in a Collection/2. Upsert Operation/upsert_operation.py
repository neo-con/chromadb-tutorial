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

# Upsert operation
matrix_collection.upsert(
    ids=["quote_2", "quote_4"],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    documents=[
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "I'm going to enjoy watching you die, Mr. Anderson.",
    ],
)

# Retrieve updated items from the collection
items = matrix_collection.get(ids=["quote_2", "quote_4"])

print(items)