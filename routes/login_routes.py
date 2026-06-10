from fastapi.routing import APIRouter
from fastapi import Depends
from models.LoginRequest import LoginRequest
from services import auth_services, token_handler

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(login_data: LoginRequest):
    return auth_services.login(login_data)

@router.get("/me")
def get_me(current_user: str = Depends(token_handler.get_user_with_token)):
    return current_user