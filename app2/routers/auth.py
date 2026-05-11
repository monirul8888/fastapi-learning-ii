from fastapi import FastAPI, HTTPException, status, APIRouter, Depends, Response
from fastapi.security import  OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from .. import database, models, utils, schemas, oauth2
from ..database import get_db
from datetime import timedelta

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def user_login(user_cred : OAuth2PasswordRequestForm=Depends() , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"User {user_cred.email} Not Found")
    
    if not utils.verify_password(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"User {user_cred.email} Not Found")
    
    access_token = oauth2.create_access_token(
        data = {
            "user_id": user.id,
            
        },
        expires_delta=timedelta(minutes=oauth2.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {"Access Token" : access_token,
            "Token Type" : "berear"}