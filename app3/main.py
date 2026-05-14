from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . database import get_db, Base, engine
from typing import List
from .routers import Student

app = FastAPI()
Base.metadata.create_all(bind = engine)

app.include_router(Student.router)


@app.get("/about/")
def About():
#     return {"msg" : "Monirul Islam"}

# @app.get("/")
# def home(db : Session = Depends(get_db)):
#     return {"msg" : "Databased Connected"}


