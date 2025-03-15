json_data = '''
{
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
}
'''

data = json.loads(json_data)

# Iterate through the list of users and access dynamic data
for user in data.get("users", []):
    name = user.get("name", "Unknown")
    age = user.get("age", "Unknown")
    print(f"Name: {name}, Age: {age}")