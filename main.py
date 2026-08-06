from fastapi import FastAPI
from routes import user_routes, login_routes
from database import engine, Base
from models.db.user import User
from exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="User Management API",
    description="""
    REST API for user management and JWT authentication.

    ## Features

    - User CRUD
    - JWT Authentication
    - Protected routes
    """,
    version="1.0.0",
    contact={
        "name": "Thiago Henrique",
        "email": "thiago.silva1001@outlook.com",
    },
)

register_exception_handlers(app)

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(login_routes.router)

@app.get("/")
def home():
    return "Server Online"