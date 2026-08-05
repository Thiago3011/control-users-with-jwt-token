from models.db.user import User

def format_user(user: User) -> dict:
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "status": user.status,
        "creation_date": user.creation_date,
        "update_date": user.update_date,
    }
