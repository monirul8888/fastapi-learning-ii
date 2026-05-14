from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . database import get_db, Base, engine
from .schemas import StudentCreate, StudentResponse
from . import models
from typing import List

app = FastAPI()
Base.metadata.create_all(bind = engine)


@app.get("/about/")
def About():
    return {"msg" : "Monirul Islam"}

@app.get("/")
def home(db : Session = Depends(get_db)):
    return {"msg" : "Databased Connected"}


@app.post("/students", response_model=StudentResponse)
def create_student(student : StudentCreate,
                   db: Session = Depends(get_db)):
    new_student = models.Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get("/students",
         response_model=List [StudentResponse])
def students_get(db : Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@app.get("/students/{id}",
         response_model=StudentResponse)
def students_get(id: int,
                 db : Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    return student