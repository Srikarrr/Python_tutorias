def safely_access_json(json_data, key):
    try:
        return json_data[key]
    except KeyError:
        return None  # Return None or any default value you prefer

# Example dynamic JSON
json_data = {
    "user": {"name": "Alice", "age": 30},
    "address": {"city": "New York"}
}

# Accessing dynamic fields
user_name = safely_access_json(json_data, "user")["name"] if safely_access_json(json_data, "user") else "No name"
user_age = safely_access_json(json_data, "user")["age"] if safely_access_json(json_data, "user") else "No age"
print(f"User Name: {user_name}, User Age: {user_age}")