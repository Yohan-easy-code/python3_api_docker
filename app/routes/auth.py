from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas import (
    UserCreate,
    UserResponse,
    UserLogin,
    UserRead,
    RefreshTokenRequest,
)
from app.services.auth_service import (
    register_user_service,
    login_user_service,
    get_current_user,
    refresh_access_token_service,
    logout_user_service,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(user: UserCreate):
    return register_user_service(user)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    return login_user_service(form_data)


@router.get("/me", response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return current_user


@router.post("/refresh")
def refresh_token(token_data: RefreshTokenRequest):
    return refresh_access_token_service(token_data)


@router.post("/logout")
def logout(token_data: RefreshTokenRequest):
    return logout_user_service(token_data)
