
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
# Access using key
print(d["name"])
# Access using get()
print(d.get("name"))

#Adding and update Dictionary Items

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# Adding a new key-value pair
d["age"] = 22
# Updating an existing value
d[1] = "Python dict"
print(d)

#O/P {1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}

#Removing Dictionary Items

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)


