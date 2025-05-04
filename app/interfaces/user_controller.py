from fastapi import APIRouter, HTTPException
from app.use_cases.user_usecase import UserUseCase
from app.infrastructure.user_repository_impl import InMemoryUserRepository

router = APIRouter()
use_case = UserUseCase(InMemoryUserRepository())

@router.get("/users")
def get_users():
    return use_case.get_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        return use_case.get_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
