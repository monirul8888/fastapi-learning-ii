from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . database import get_db, engine
from . import models, schemas
from typing import List

app = FastAPI()
models.Base.metadata.create_all(bind = engine)
@app.get("/")
def home(db : Session = Depends(get_db) ):
    return {"msg" : "Welcome To FastAPI App 2"}

@app.get("/students", response_model=List [schemas.StudentResponse])
def get_student(db : Session = Depends(get_db)):
    st = db.query(models.Student2).all()
    return st


@app.get("/students/{id}", response_model=schemas.StudentResponse)
def get_student(id : int, db : Session = Depends(get_db), ):
    student = db.query(models.Student2).filter(models.Student2.id == id).first()
    return student


@app.post("/students", response_model=schemas.StudentResponse)
def create_student(student : schemas.CreateStudent, db : Session = Depends(get_db)):
    new_st = models.Student2(**student.model_dump())
    db.add(new_st)
    db.commit()
    db.refresh(new_st)
    return new_st



@app.post("/user", response_model=schemas.UserResponse)
def create_user(user : schemas.CreateUser, db : Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

