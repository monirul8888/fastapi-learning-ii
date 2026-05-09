from pydantic import BaseModel

class StudentCreate(BaseModel):
    name : str
    id : int
    dept : str


class StudentResponse(StudentCreate):
    cgpa:float

    class config:
        orm_model = True

        



