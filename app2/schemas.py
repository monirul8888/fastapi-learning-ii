from pydantic import BaseModel

class CreateStudent(BaseModel):
    name : str
    id : int
    dept : str

class StudentResponse(CreateStudent):
    class Config:
        orm_model = True

