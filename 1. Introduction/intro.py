import chromadb

# Initialize the ChromaDB client
client = chromadb.Client()

# Test if the service is up and running
print(client.heartbeat())