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
        "Unfortunately, no one can be told what the Matrix is",
        "You hear that Mr. Anderson?... That is the sound of inevitability...",
        "You are a plague, Mr. Anderson. You and your kind are a cancer of this planet.",
    ],
    metadatas=[
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Morpheus"},
        {"category": "quote", "speaker": "Agent Smith"},
        {"category": "quote", "speaker": "Agent Smith"},
    ],
    ids=["quote_1", "quote_2", "quote_3", "quote_4", "quote_5"],
)

# Querying with where filters
results = matrix_collection.query(
    query_texts=["What is the Matrix?"],
    where={"speaker": "Morpheus"},
    n_results=2,
)

print(results)