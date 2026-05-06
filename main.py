from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg" : "Welcome To FastAPI Learning"}

@app.get("/about")
def about():
    return{"Name" : "Md. Monirul Islam",
           "Department": "CSE"}