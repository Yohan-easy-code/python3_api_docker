from fastapi import APIRouter, Depends

from app.schemas import UserCreate, UserRead, UserLogin
from app.services.auth_service import (
    register_user_service,
    login_user_service,
    get_current_user,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(user: UserCreate):
    return register_user_service(user)


@router.post("/login")
def login(user: UserLogin):

    return login_user_service(user)


@router.get("/me", response_model=UserRead)
def get_me(current_user=Depends(get_current_user)):
    return current_user
