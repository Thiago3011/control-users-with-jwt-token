from models.User import User, UserUpdate
from database import users
from services import security_handler
from fastapi import HTTPException
from datetime import timezone, datetime

def find_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return None

def get_user(user_id: int):
    user = find_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "status": user.status,
        "creation_date": user.creation_date,
        "update_date": user.update_date,
    }

def get_users():
    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "status": user.status,
            "creation_date": user.creation_date,
            "update_date": user.update_date,
        }
        for user in users
    ]


def register_user(new_user: User):
    for user in users:
        if user.email == new_user.email:
            raise HTTPException(status_code=409, detail="User already exists")

    user = User(
        id=len(users) + 1,
        name=new_user.name,
        email=new_user.email,
        phone=new_user.phone,
        password=security_handler.hash_password(new_user.password),
    )

    users.append(user)

    return {"message": "User registered successfully!"}


def update_user(user_id: int, user_data: UserUpdate):
    user = find_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_data = user_data.model_dump(exclude_unset=True)

    for field, value in updated_data.items():
        if field == "password":
            value = security_handler.hash_password(value)
        setattr(user, field, value)

    user.update_date = datetime.now(timezone.utc)
    return {"message": "User update successfully!"}

def delete_user(user_id: int):
    user = find_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    users.remove(user)
    
    return {"message": f"User ({user.email}) deleted"}