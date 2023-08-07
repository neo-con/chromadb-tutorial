# Choosing Which Data is Returned from a Collection in ChromaDB

This tutorial will guide you through choosing which data is returned from a collection in ChromaDB.

1. **Creating a Collection**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/4.%20Choosing%20Returned%20Data/choose_data.py#L3-L7
    We start by initializing the ChromaDB client and creating a collection named `morpheus`.

2. **Adding Raw Documents**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/4.%20Choosing%20Returned%20Data/choose_data.py#L9-L17
    We add three raw documents to our collection using the `add` method. Each document is associated with a unique ID.

3. **Querying the Collection by Text and Choosing Data to be Returned**

    https://github.com/neo-con/chromadb-tutorial/blob/19fe2c99dc1aa9fe0e1aac930fbef84536759dec/4.%20Querying%20a%20Collection/4.%20Choosing%20Returned%20Data/choose_data.py#L19-L24
    We can query the collection by text using the `query` method. In this example, we search for the phrase "take the red pill" and ask for one result. Additionally, we specify that we only want the distances and embeddings to be returned by including them in the `include` parameter.

    The `query` method will return a dictionary with the selected data (distances and embeddings) for the closest match to the query text.

    💡 Use cases for choosing which data is returned include:

    >- **Selective Data Retrieval**: By specifying the desired data in the `include` parameter, you can retrieve only the necessary information, reducing network traffic and improving performance.
    >- **Data Privacy and Security**: You can exclude sensitive information from being returned, ensuring that only the necessary and non-sensitive data is exposed.
    >- **Efficiency and Resource Optimization**: By selecting specific data, you can optimize resource usage and improve the efficiency of your application.

    Feel free to modify the query text, the number of results, and the `include` parameter to select different data to be returned.