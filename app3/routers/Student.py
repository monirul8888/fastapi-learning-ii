from fastapi import APIRouter, Depends
from ..models import Student
from ..database import get_db
from ..schemas import StudentCreate, StudentResponse
from typing import List
from sqlalchemy.orm import Session
from .. import models

router = APIRouter()


@router.post("/students", response_model=StudentResponse)
def create_student(student : StudentCreate,
                   db: Session = Depends(get_db)):
    new_student = models.Student(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.get("/students",
         response_model=List [StudentResponse])
def students_get(db : Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@router.get("/students/{id}",
         response_model=StudentResponse)
def students_get(id: int,
                 db : Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    return student