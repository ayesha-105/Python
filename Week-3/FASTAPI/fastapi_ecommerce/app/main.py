from fastapi import FastAPI 
from Service.products import get_all_products

app = FastAPI()   #object of FastAPI class

@app.get("/")      #static route handle request

def root():
    return {"messsage": "Welcome to FastAPI"}  #resopnse

# @app.get("/product/{id}")    #dynamic route handle request

# def get_Products(id: int):              #function to get product by id
#     products= ["Laptop", "Mouse", "Keyboard", "Monitor"]
#     return products[id] 
   
@app.get("/products")    
def get_products():
    return get_all_products()