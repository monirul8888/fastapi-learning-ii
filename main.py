from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name : str
    id : int
    dept : str


@app.get("/")
def home():
    return {"msg" : "Welcome To FastAPI Learning"}

@app.get("/about")
def about():
    return{"Name" : "Md. Monirul Islam",
           "Department": "CSE"}


@app.post("/post")
def create_student(post : Student):
    return {"data" : post}


