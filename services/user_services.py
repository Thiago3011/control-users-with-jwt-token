from models.db.user import User
from models.schemas.User import UserCreate, UserUpdate
from services import security_handler
from fastapi import HTTPException
from datetime import timezone, datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session
from services.formatter import format_user
from services.user_finder import find_user

def get_user(user_id: int, db: Session) -> dict:
    user = find_user(user_id, db)
    
    return format_user(user)

def get_users(db: Session) -> list[dict]:
    db_users_data = db.query(User).all()
            
    return [
        format_user(user)
        for user in db_users_data
    ]

def register_user(new_user: UserCreate, db: Session):
    existing_user = db.query(User).filter(or_(User.email == new_user.email, User.phone == new_user.phone)).first()
    if existing_user: 
        raise HTTPException(status_code=409, detail="User already exists")
        
    user = User(
        name=new_user.name,
        email=new_user.email,
        phone=new_user.phone,
        password=security_handler.hash_password(new_user.password),
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return format_user(user)

def update_user(user_id: int, user_data: UserUpdate, db: Session):
    
    user = find_user(user_id, db)
    
    updated_data = user_data.model_dump(exclude_unset=True)

    for field, value in updated_data.items():
        if field == "password":
            value = security_handler.hash_password(value)
        setattr(user, field, value)

    user.update_date = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(user)
    return format_user(user)

def delete_user(user_id: int, db: Session):
    user = find_user(user_id, db)

    db.delete(user)
    db.commit()
    
    return {"message": f"User ({user.email}) deleted"}
