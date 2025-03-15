import json

# Sample dynamic JSON data
json_data = '''
{
  "user": {
    "name": "Alice",
    "age": 25
  },
  "profile": {
    "location": "London"
  },
  "timestamp": "2025-03-15T10:00:00Z"
}
'''

# Load the JSON string into a Python dictionary
data = json.loads(json_data)

# Accessing different keys dynamically (safely)
def get_value(json_data, key, default=None):
    """Safely retrieve a value from dynamic JSON."""
    keys = key.split(".")
    for k in keys:
        if isinstance(json_data, dict) and k in json_data:
            json_data = json_data[k]
        else:
            return default
    return json_data

# Retrieve values dynamically
name = get_value(data, "user.name")  # Output: Alice
location = get_value(data, "profile.location", "Unknown")  # Output: London
timestamp = get_value(data, "timestamp")  # Output: 2025-03-15T10:00:00Z
unknown_field = get_value(data, "unknown.field", "Not Found")  # Output: Not Found

print(f"Name: {name}")
print(f"Location: {location}")
print(f"Timestamp: {timestamp}")
print(f"Unknown Field: {unknown_field}")


#json.loads(): This method is used when the JSON is in a string format (instead of being in a file). It parses the JSON and returns a Python dictionary.
#Dynamic Key Access:
#get_value() function is designed to safely retrieve values from a JSON structure, even if the key path is nested.
#The function get_value(json_data, key) splits the key by dots (e.g., "user.name"), then traverses the dictionary accordingly.
#If a key doesn’t exist at any point, it returns a default value (None or "Not Found").
#Safe Access with Default Values:
#By using get_value, we avoid issues where keys might be missing or structures might be different across API responses or data sources.