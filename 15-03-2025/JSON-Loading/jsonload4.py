def get_value(json_data, keys, default=None):
    """
    Recursively retrieve a value from a dynamic JSON object.
    `keys` is a list of keys to access nested data.
    """
    if not keys:
        return json_data
    key = keys[0]
    if isinstance(json_data, dict) and key in json_data:
        return get_value(json_data[key], keys[1:], default)
    elif isinstance(json_data, list) and key.isdigit():
        index = int(key)
        if 0 <= index < len(json_data):
            return get_value(json_data[index], keys[1:], default)
    return default

# Example usage
keys = ["details", "hobbies", "1"]
value = get_value(data, keys, "No value")
print(value)  # Output: hiking