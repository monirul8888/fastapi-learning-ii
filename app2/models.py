from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text, ForeignKey
from . database import Base


class Student2(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dept = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)

class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))




