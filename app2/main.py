from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . database import get_db, engine
from . import models, schemas

app = FastAPI()
models.Base.metadata.create_all(bind = engine)
@app.get("/")
def home(db : Session = Depends(get_db) ):
    return {"msg" : "Welcome To FastAPI App 2"}