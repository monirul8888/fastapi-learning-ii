from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import time

from psycopg2.extras import RealDictCursor 

app = FastAPI()


class Student(BaseModel):
    name : str
    id : int
    dept : str


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
    return {"data" : post}



@app.get("/student")
def student():
    cursor.execute(""" SELECT * FROM STUDENT """)
    data = cursor.fetchall()

    return {"Data" : data}


