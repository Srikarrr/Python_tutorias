def get_nested_value(json_data, key):
    """Recursive function to handle nested keys."""
    if isinstance(json_data, dict):
        for k, v in json_data.items():
            if k == key:
                return v
            elif isinstance(v, dict):
                return get_nested_value(v, key) #recursion
    return None  # Return None if the key is not found

# Example nested JSON
nested_json = {
    "level1": {
        "level2": {
            "level3": {
                "target": "Found me!"
            }
        }
    }
}

# Access nested value
result = get_nested_value(nested_json, "target")
print(result)  # Output: Found me!
