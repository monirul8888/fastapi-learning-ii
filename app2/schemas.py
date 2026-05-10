from pydantic import BaseModel, EmailStr

class CreateStudent(BaseModel):
    name : str
    id : int
    dept : str

class StudentResponse(CreateStudent):
    class Config:
        orm_model = True


class CreateUser(BaseModel):
    email : EmailStr
    password : str
    

