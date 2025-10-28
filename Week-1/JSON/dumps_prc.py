import json

data={"name": "Ayesha Malik",
     "age": 20,
     "city": "Karachi",
     "isstudent": True
}

# convert python object to a JSON string
json_string= json.dumps(data)

print("Python JSON string:", json_string)  
print("Python object:", data)

