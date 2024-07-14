# Choosing Which Data is Returned from a Collection in ChromaDB

This tutorial will guide you through choosing which data is returned from a collection in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
morpheus_collection = client.create_collection(name="morpheus", metadata={"hnsw:space": "cosine"})
```

We start by initializing the ChromaDB client and creating a collection named `morpheus`.

## 2. Adding Raw Documents

```python
morpheus_collection.add(
    documents=[
        "This is your last chance. After this, there is no turning back.",
        "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe.",
        "You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes.",
    ],
    ids=["quote_1", "quote_2", "quote_3"],
)
```

We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID.

## 3. Querying the Collection by Text and Choosing Data to be Returned

```python
results = morpheus_collection.query(
    query_texts=["make a choice"], n_results=1, include=["distances", "embeddings"]
)
```

We can query the collection by text using the `query` method. In this example, we search for the phrase "make a choice" and ask for one result. Additionally, we specify that we only want the distances and embeddings to be returned by including them in the `include` parameter.

The `query` method will return a dictionary with the selected data (distances and embeddings) for the closest match to the query text.

### Use cases for choosing which data is returned:

1. **Selective Data Retrieval**:
   - Retrieve only document IDs for quick reference checks
   - Fetch embeddings for further processing or visualization
   - Get distances to analyze similarity scores without full content

2. **Data Privacy and Security**:
   - Return only non-sensitive metadata while excluding document content
   - Provide aggregated results without exposing individual data points
   - Implement role-based access control by returning different data based on user permissions

3. **Efficiency and Resource Optimization**:
   - Retrieve only document IDs for initial filtering, then fetch full content as needed
   - Return summarized data for large-scale analytics without transferring entire documents
   - Optimize mobile app performance by requesting minimal data for display

4. **Custom Application Needs**:
   - Fetch only specific metadata fields relevant to the current user interface
   - Retrieve embeddings for local similarity comparisons or clustering
   - Return document snippets for search result previews without full content

5. **Debugging and Monitoring**:
   - Include internal scores or rankings for system performance analysis
   - Return processing timestamps to monitor query latency
   - Fetch version information to ensure data consistency across updates

Remember to adjust the `include` parameter in your query to match your specific use case requirements.