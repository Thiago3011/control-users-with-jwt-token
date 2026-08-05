from jose import jwt
from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from services.formatter import format_user
from services.user_finder import find_user
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "minha_chave"
ALGORITHM = "HS256"

# Dependency used by FastAPI to extract the JWT token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(user_id: int) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(seconds=40) 
    payload = {
        "user_id": user_id,
        "exp": expiration_time
    }
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, [ALGORITHM])

def get_user_with_token(db: Session, token: str):
        decoded_token = decode_access_token(token)
        decoded_user_id = decoded_token["user_id"]
        
        user = find_user(decoded_user_id, db)
            
        return format_user(user)
            