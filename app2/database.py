from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "postgresql://postgres:1234@localhost/university"
engine = create_engine(url)

sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = declarative_base(sessionLocal)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
