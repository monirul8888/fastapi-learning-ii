from .. import models, schemas
from ..database import get_db
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/students", response_model=List [schemas.StudentResponse])
def get_student(db : Session = Depends(get_db)):
    st = db.query(models.Student2).all()
    return st


@router.get("/students/{id}", response_model=schemas.StudentResponse)
def get_student(id : int, db : Session = Depends(get_db), ):
    student = db.query(models.Student2).filter(models.Student2.id == id).first()
    return student


@router.post("/students", response_model=schemas.StudentResponse)
def create_student(student : schemas.CreateStudent, db : Session = Depends(get_db)):
    new_st = models.Student2(**student.model_dump())
    db.add(new_st)
    db.commit()
    db.refresh(new_st)
    return new_st