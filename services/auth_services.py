from models.LoginRequest import LoginRequest
from database import users
from services import token_handler, security_handler
from fastapi import HTTPException

def login(login_data: LoginRequest):
    for user in users:
        if user.email == login_data.email:
            if security_handler.verify_user_password(login_data.password, user.password):  
                
                return {
                    "user_name": user.name,
                    "token_type": "bearer",
                    "token": token_handler.create_access_token(user.id)
                }
                
            raise HTTPException(status_code=401, detail="Invalid credentials")
    raise HTTPException(status_code=401, detail="Invalid credentials")