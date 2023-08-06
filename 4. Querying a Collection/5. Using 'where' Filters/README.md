# Using Where Filters in ChromaDB

This tutorial will guide you through using where filters in ChromaDB to filter and query items based on specific metadata criteria.

1. **Creating a Collection**

    We start by initializing the ChromaDB client and creating a collection named `matrix`.

2. **Adding Raw Documents**

    We add five raw documents (quotes from "The Matrix") to our collection using the `add` method. Each document is associated with a unique ID and has metadata including the category and speaker.

3. **Using Where Filters**

    ChromaDB supports filtering queries by metadata using where filters. In this example, we query the collection for with a query text "What is the Matrix" and filter the results based on the speaker being "Morpheus".

    The `query` method takes a `where` parameter, which is a dictionary specifying the metadata field and its corresponding value for filtering. The results will include only the items that match the specified criteria.

    Use cases for using where filters include:

    - **Metadata-based Filtering**: You can filter items based on specific metadata fields, such as speaker, category, or any other relevant criteria.
    - **Targeted Analysis**: By filtering the results using where filters, you can perform targeted analysis or operations on specific subsets of the data that meet certain metadata criteria.

    Feel free to modify the where filters in the `query` method to explore different filtering options. Experiment with different metadata fields and values to see how ChromaDB allows you to filter and query items based on specific metadata criteria.