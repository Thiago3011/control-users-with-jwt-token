from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from models.schemas.LoginRequest import LoginRequest
from services import auth_services, token_handler
from database import get_db
from services.token_handler import oauth2_scheme


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return auth_services.login(login_data, db)

@router.get("/me")
def get_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return token_handler.get_user_with_token(db, token)