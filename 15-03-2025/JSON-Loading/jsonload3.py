import json
import requests

# Example: Loading dynamic JSON from an API endpoint
response = requests.get("https://api.example.com/data")

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()  # or json.loads(response.text) if needed

    # Access dynamic keys
    name = get_value(data, "user.name", "Unknown")
    print(f"Name: {name}")
else:
    print("Failed to retrieve data")
