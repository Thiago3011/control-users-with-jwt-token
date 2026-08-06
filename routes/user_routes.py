from fastapi.routing import APIRouter
from fastapi import Depends
from models.schemas.User import UserCreate, UserUpdate
from services import user_services
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user", 
    tags=["user"]
)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_services.get_user(user_id, db)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return user_services.get_users(db)

@router.post("/", status_code=201)
def register_user(new_user: UserCreate, db: Session = Depends(get_db)):
    return user_services.register_user(new_user, db)

@router.patch("/{user_id}")
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    return user_services.update_user(user_id, user_data, db)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_services.delete_user(user_id, db)