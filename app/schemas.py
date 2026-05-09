from pydantic import BaseModel

class StudentCreate(BaseModel):
    name : str
    id : int
    dept : str


class StudentResponse(StudentCreate):
   

    class Config:
        orm_model = True





