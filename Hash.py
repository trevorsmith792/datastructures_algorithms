# Creating a hash table (using Python's built-in dictionary)
hash_table = {}

# Inserting key-value pairs
hash_table["apple"] = 10
hash_table["banana"] = 20
hash_table["orange"] = 30

# Retrieving a value by key
print(hash_table["apple"])  # Output: 10

# Checking if a key exists
if "banana" in hash_table:
    print("Banana is in the hash table.")  # Output: Banana is in the hash table.

# Deleting a key-value pair
del hash_table["orange"]
print(hash_table)  # Output: {'apple': 10, 'banana': 20}

# Updating a value
hash_table["banana"] = 25
print(hash_table["banana"])  # Output: 25
