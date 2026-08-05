from models.db.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException

def find_user(user_id: int, db: Session) -> User:
    user = db.query(User).filter(User.id == user_id).first()
        
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user