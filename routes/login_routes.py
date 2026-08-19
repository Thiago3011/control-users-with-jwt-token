from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from models.schemas.LoginRequest import LoginRequest
from services import auth_services, token_handler
from database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", summary="Login user", description="Log in the user with the provided information.")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return auth_services.login(login_data, db)

@router.get("/me", summary="Get me", description="Get the actual logged user by his valid and not expired token.")
def get_me(db: Session = Depends(get_db), token: str = Depends(token_handler.get_bearer_token)):
    return token_handler.get_user_with_token(db, token)