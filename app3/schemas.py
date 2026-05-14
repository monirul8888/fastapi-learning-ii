from pydantic import BaseModel

class StudentCreate(BaseModel):
    id : int
    name : str

class StudentResponse(StudentCreate):
    class Config:
        orm_model = True