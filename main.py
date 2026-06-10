from fastapi import FastAPI
from routes import user_routes, login_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(login_routes.router)

@app.get("/")
def home():
    return "Server Online"