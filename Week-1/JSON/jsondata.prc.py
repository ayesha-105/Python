import json

file_path = "D:\\Coding\\VS CODE\\Python\\Week-1\\JSON\\data.json"

# read JSON data from a file
with open(file_path, "r") as file:
    data = json.load(file)
    print(data)

# update JSON data
with open(file_path, "w") as file:
    data["country"]= "Pakistan"
    json.dump(data, file, indent=4)  #dump mean to write data into file, indent = 4 is used to format the data with 4 spaces

 # Delete Height Key
# with open(file_path, "w") as file:     # I'm commenting this block of code to avoid error because height key is already deleted
#     del data["height"]
#     json.dump(data, file, indent=4)

# Read data
with open(file_path, "r") as file:
    data = json.load(file)
    print(data)

# print specific data
print("Name:", data["name"])
print("Age:", data["age"])
print("Country:", data["country"])              