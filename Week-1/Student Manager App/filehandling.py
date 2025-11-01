import json
import os

data_file= "D:\\Coding\\VS CODE\\Python\\Week-1\\Student Manager App\\studentslist.json"

# This function loads student data from a JSON file
def load_data():
    if os.path.exists(data_file):
        with open( data_file, "r") as file:
            return json.load(file)        
    return []

# this function saves student data to a json file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)