from pydantic import BaseModel

class StudentCreate(BaseModel):
    name : str
    id : int
    dept : str


class StudentResponse(BaseModel):
    name:str
    dept:str

    class Config:
        orm_model = True





