from fastapi import APIRouter
from app.models import User

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Tortoise!"}

@router.post("/users/")
async def create_user(username: str, email: str):
    user = await User.create(username=username, email=email)
    return {"id": user.id, "username": user.username, "email": user.email}
