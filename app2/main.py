from fastapi import FastAPI, Depends

from .routers import student, user
from . import models, schemas
from .database import get_db, engine
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind = engine)

app.include_router(student.router)
app.include_router(user.router)



@app.get("/")
def home(db : Session = Depends(get_db) ):
    return {"msg" : "Welcome To FastAPI App 2"}



