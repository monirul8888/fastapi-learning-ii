from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . database import get_db

app = FastAPI()

@app.get("/about")
def About():
    return {"msg" : "Monirul Islam"}

@app.get("/")
def home(db : Session = Depends(get_db)):
    return {"msg" : "Databased Connected"}