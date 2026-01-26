from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"messsage": "Welcome to FastAPI"}