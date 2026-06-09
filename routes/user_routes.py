from fastapi.routing import APIRouter
from models.User import User, UserUpdate
from services import user_services

router = APIRouter(
    prefix="/user", 
    tags=["user"]
)

@router.get("/{user_id}")
def get_user(user_id: int):
    return user_services.get_user(user_id)

@router.get("/")
def get_users():
    return user_services.get_users()

@router.post("/")
def register_user(new_user: User):
    return user_services.register_user(new_user)

@router.patch("/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    return user_services.update_user(user_id, user_data)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return user_services.delete_user(user_id)