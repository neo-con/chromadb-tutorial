# Working with Collections in ChromaDB

This tutorial will guide you through creating, inspecting, and deleting collections, as well as changing the distance function in ChromaDB.

## 1. Creating a Collection

```python
client = chromadb.Client()
neo_collection = client.create_collection(name="neo")
```

We start by initializing the ChromaDB client and creating a collection named `neo`.

## 2. Inspecting a Collection

```python
print(neo_collection)
```

To inspect a collection, we simply print the collection object. This will show us the name, id, and metadata of the collection.

## 3. Modifying a Collection

```python
neo_collection.modify(name="mr_anderson")
print(neo_collection)
```

Collections can be modified using the `modify` method. In this case, we change the name of our collection from `neo` to `mr_anderson`.

## 4. Counting Items in a Collection

```python
item_count = neo_collection.count()
print(f"Count of items in collection: {item_count}")
```

We can count the number of items in a collection using the `count` method. Since we have not added any items to our collection yet, the count returns `0`.

## 5. Get or Create a Collection and Change the Distance Function

```python
trinity_collection = client.get_or_create_collection(
    name="trinity", metadata={"hnsw:space": "cosine"}
)
print(trinity_collection)
```

In ChromaDB, the distance function determines how the "distance" or "difference" between two items in the collection is calculated. This is crucial when performing operations like querying for similar items. 

The default distance function in ChromaDB is `"l2"`, which stands for Euclidean distance. It's a common measure of distance in a plane. 

However, sometimes other measures of distance might be more appropriate, depending on the nature of the data in the collection. 

In this tutorial, we use the `get_or_create_collection` method to either get an existing collection named `trinity` or create it if it doesn't exist. We set the distance function to `"cosine"`. The Cosine distance is a measure of similarity between two vectors by taking the cosine of the angle between them. This can be useful in many domains including text analysis where high dimensionality and sparsity are common. 

You can choose the distance function that best suits your needs when creating a collection. Other valid options for the distance function include `"ip"` (Inner Product).

> Remember, the choice of distance function can significantly influence the results of your queries, so choose wisely!

## 6. Deleting a Collection

```python
try:
    client.delete_collection(name="mr_anderson")
    print("Mr. Anderson collection deleted.")
except ValueError as e:
    print(f"Error: {e}")
```

We attempt to delete the `mr_anderson` collection using the `delete_collection` method. Please note that `delete_collection` raises a `ValueError` if the collection does not exist. In our Python code, we handle this potential error using a `try/except` block. If the collection is successfully deleted, we print a success message. If the collection does not exist, we print the error message.

Please refer to the `matrix_collections.py` file for the complete Python code used in this tutorial.