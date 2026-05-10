from sqlalchemy import Column, Integer, String, Float
from . database import Base

class Student2(Base):
    __tablename__ = "students3"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dept = Column(String, nullable=False)

