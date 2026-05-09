from fastapi import FastAPI, Depends
from pydantic import BaseModel
import psycopg2
import time
from psycopg2.extras import RealDictCursor 
from . import models

from sqlalchemy.orm import session
from .database import engine, get_db



app = FastAPI()

models.Base.metadata.create_all(bind = engine)


class Student(BaseModel):
    name : str
    id : int
    dept : str

@app.get("/data")
def students(db:session = Depends(get_db)):
    return {"status" : "Connected Table"}


@app.post("/students")
def CreateStudent(student : Student, db: session = Depends(get_db)):
    new_student = models.Student(
        name = student.name,
        id = student.id,
        dept = student.dept,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"New Student " : new_student}






while True:
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "university",
            user = "postgres",
            password = "1234",
            cursor_factory = RealDictCursor
        )

        cursor = conn.cursor()

        print("Successfully Connected To The Database")
        break
    except Exception as error:
        print("Database Connection Failed")
        print("Error : ", error)
        time.sleep(2)





@app.get("/")
def home():
    return {"msg" : "Welcome To FastAPI Learning"}

@app.get("/about")
def about():
    return{"Name" : "Md. Monirul Islam",
           "Department": "CSE"}


@app.post("/post")
def create_student(post : Student):
    cursor.execute(""" INSERT INTO STUDENT (NAME, ID, DEPT) VALUES(%s, %s, %s) RETURNING * """,
                    (post.name, post.id, post.dept) )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data" : new_post}



@app.get("/student")
def student():
    cursor.execute(""" SELECT * FROM STUDENT """)
    data = cursor.fetchall()

    return {"Data" : data}


@app.get("/student/{id}")
def student(id : int):
    cursor.execute(""" SELECT * FROM STUDENT WHERE id = %s """, (id,))
    data = cursor.fetchone()



    return {"Data" : data}


