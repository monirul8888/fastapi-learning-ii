from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import psycopg2
import time
from psycopg2.extras import RealDictCursor 
from . import models, schemas

from sqlalchemy.orm import Session
from .database import engine, get_db


app = FastAPI()

models.Base.metadata.create_all(bind = engine)


@app.get("/data")
def students(db:Session = Depends(get_db)):
    return {"status" : "Connected Table"}


@app.post("/students", response_model=schemas.StudentResponse)
def CreateStudent(student : schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# @app.get("/students")
# def get_students(db : session = Depends(get_db)):
#     students = db.query(models.Student).all()

#     return {"Students" : students}

# @app.get("/students/{id}")
# def get_students(id : int, db : session = Depends(get_db)):
#     students = db.query(models.Student).filter(models.Student.id == id).first()

#     return {"Student ", students}

# @app.put("/students/{id}")
# def update_students(id : int, update_student : Student, db : session = Depends(get_db)):

#     st_query = db.query(models.Student).filter(models.Student.id == id)
#     st = st_query.first()

#     if not st:
#         raise HTTPException(status_code=404, detail= f"Student with {id} Not Found")
    
#     update_data = update_student.model_dump()

#     st_query.update(update_data, synchronize_session = False )

#     db.commit()
#     db.refresh(st)

#     return {"Updated Student ": st}



# @app.delete("/students/{id}")
# def delete_students(id : int, db : session = Depends(get_db)):

#     st_query = db.query(models.Student).filter(models.Student.id == id)
#     st = st_query.first()

#     if not st:
#         raise HTTPException(status_code=404, detail= f"Student with {id} Not Found")
#     st_query.delete(synchronize_session = False )
#     db.commit()
    
#     return {"msg" , f"Student ID = {id} Deleted Successfully"}

    






