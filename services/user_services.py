from models.User import User
from database import users
from services import security_handler
from fastapi import HTTPException

def get_users():
    return [
        {
            "id": user.id, 
            "name": user.name, 
            "email": user.email,
            "phone": user.phone,
            "status": user.status,
            "creation_date": user.creation_date
        } for user in users
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
             password=security_handler.hash_password(new_user.password)
        )

        users.append(user)

        return {"message": "User registered successfully!"}