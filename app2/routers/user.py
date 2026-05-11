from .. import models, schemas
from fastapi import HTTPException, status, APIRouter
from ..database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from .. import utils

router = APIRouter()

@router.post("/user", response_model=schemas.UserResponse)
def create_user(user : schemas.CreateUser, db : Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email {user.email} already taken"
        )

    hashedPassword = utils.hash_password(user.password)
    user.password = hashedPassword
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

