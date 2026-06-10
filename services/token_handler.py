from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from datetime import datetime, timezone, timedelta
from database import users

SECRET_KEY = "minha_chave"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(user_id):
    expiration_time = datetime.now(timezone.utc) + timedelta(seconds=40) 
    payload = {
        "user_id": user_id,
        "exp": expiration_time
    }
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def decode_access_token(token: str = Depends(oauth2_scheme)):
    return jwt.decode(token, SECRET_KEY, [ALGORITHM])

def get_user_with_token(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = decode_access_token(token)
        decoded_user_id = decoded_token["user_id"]
        
        for user in users:
            if user.id == decoded_user_id:
                return {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "phone": user.phone,
                    "status": user.status,
                    "creation_date": user.creation_date,
                    "update_date": user.update_date,
                }
    except JWTError:
       raise HTTPException(detail="Invalid or expired token", status_code=401)
    
    raise HTTPException(detail="User not found", status_code=401)
    
    