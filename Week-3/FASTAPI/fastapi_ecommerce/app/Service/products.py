import json
from pathlib import Path
from typing import List, Dict

data_file= Path(__file__).parent.parent / "Data" / "products.json"  #fetch the products.json file   

def load_products() -> List[Dict]:
    if data_file.exists():
        with open(data_file, "r") as file:
            return json.load(file)
    
    return []  # Return empty list if file does not exist

def get_all_products() -> List[Dict]:
    return load_products()

