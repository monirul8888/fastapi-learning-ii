from typing import List

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/", response_model=List[schemas.StudentResponse])
def get_students(
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth2.get_current_user)
):
    students = db.query(models.Student2).all()
    return students


@router.get("/{id}", response_model=schemas.StudentResponse)
def get_student_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth2.get_current_user)
):
    student = db.query(models.Student2).filter(models.Student2.id == id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found"
        )

    return student


@router.post("/", response_model=schemas.StudentResponse)
def create_student(
    student: schemas.CreateStudent,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth2.get_current_user)
):
    new_student = models.Student2(**student.model_dump())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student