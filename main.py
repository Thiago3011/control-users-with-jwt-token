from fastapi import FastAPI
from routes import user_routes, login_routes
from database import engine, Base
from models.db.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(login_routes.router)

@app.get("/")
def home():
    return "Server Online"