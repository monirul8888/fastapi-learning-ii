from sqlalchemy import Column, Float, Integer, String
from .database import Base

class Student(Base):
    __tablename__ = "students3"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable= False)


    
