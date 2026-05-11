from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

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

class UserResponse(BaseModel):
    email : EmailStr
    id : int
    created_at : datetime
    class Config:
        orm_model = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None




