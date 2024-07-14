import chromadb
import chromadb.utils.embedding_functions as embedding_functions

# Initialize ChromaDB client
client = chromadb.Client()

# Initialize OpenAI embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="USE YOUR OPEN-AI KEY",
    model_name="text-embedding-3-small",
)

# Create the collection with the OpenAI embedding function
matrix_collection = client.create_collection(
    name="matrix",
    embedding_function=openai_ef,
)

# Add the raw documents
matrix_collection.add(
    documents=[
        "The Matrix is all around us.",
        "What you know you can't explain, but you feel it",
        "There is a difference between knowing the path and walking the path",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)

# Querying by a set of query_texts
results = matrix_collection.query(query_texts=["What is the Matrix?"], n_results=2)

print(results)