import json

file_path= "D:\\Coding\\VS CODE\\Python\\Week-1\\JSON\\nesteddata.json"

# read data
with open(file_path, "r") as file:
    data= json.load(file) 

print("Original data:")
print(data)

# accessing nested data
print("Student name:", data["student"]["name"])
print("Student city:", data["student"]["address"]["city"])

# updating nested data 
with open(file_path, "w") as file:
    data["student"]["marks"]["math"]=95
    data["student"]["address"]["postal_code"]= "560001"
    json.dump(data, file, indent=4)

print("Updated data successfully.")

#  Pretty-print (show in console nicely formatted)
print(json.dumps(data, indent=4))
