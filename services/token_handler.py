import os
from dotenv import load_dotenv
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import Depends, HTTPException
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from services.formatter import format_user
from services.user_finder import find_user
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is not set")

ALGORITHM = "HS256"

# Dependency used by FastAPI to extract the JWT token
bearer_scheme = HTTPBearer()

def get_bearer_token(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
) -> str:
    return credentials.credentials

def create_access_token(user_id: int) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(seconds=40) 
    payload = {
        "user_id": user_id,
        "exp": expiration_time
    }
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, [ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")

def get_user_with_token(db: Session, token: str):
        decoded_token = decode_access_token(token)
        decoded_user_id = decoded_token["user_id"]
        
        user = find_user(decoded_user_id, db)
            
        return format_user(user)
            