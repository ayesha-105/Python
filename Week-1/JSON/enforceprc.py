import json

file_path = "D:\\Coding\\VS CODE\\Python\\Week-1\\JSON\\data.json"

# Read JSON data
with open(file_path, "r") as file:
    data = json.load(file)

# Define required keys (schema)
required_keys = ["name", "age", "country"]

# Validation check
for key in required_keys:
    if key not in data:
        print(f"Missing key: {key}")
    else:
        print(f"{key} is present")

print("Validation complete")
