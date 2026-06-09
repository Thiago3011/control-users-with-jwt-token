from fastapi.routing import APIRouter
from models.User import User
from services import user_services

router = APIRouter(
    prefix="/user", 
    tags=["user"]
)

@router.get("/")
def get_user():
    return user_services.get_users()

@router.post("/")
def register_user(new_user: User):
    return user_services.register_user(new_user)