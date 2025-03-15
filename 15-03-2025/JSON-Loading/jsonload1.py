import json

# Load JSON from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the data
print(data["name"])  # Output: John
print(data["address"]["city"])  # Output: New York