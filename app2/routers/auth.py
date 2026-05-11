from fastapi import FastAPI, HTTPException, status, APIRouter, Depends, Response

from sqlalchemy.orm import Session
from .. import database, models, utils, schemas
from ..database import get_db

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def user_login(user_cred : schemas.UserLogin , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"User {user_cred.email} Not Found")
    
    if not utils.verify_password(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"User {user_cred.email} Not Found")
    
    return {"msg" : "Successfully Login"}