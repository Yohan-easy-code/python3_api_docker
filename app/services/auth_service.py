from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

import os
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime, timedelta, timezone
from jose import jwt

from app.models import User
from app.schemas import UserCreate
from app.repositories.user_repository import (
    create_user_repository,
    get_user_by_email_repository,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_user_service(user: UserCreate):
    existing_user = get_user_by_email_repository(user.email)

    if existing_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)

    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
    )

    return create_user_repository(db_user)


def login_user_service(form_data):
    user = get_user_by_email_repository(form_data.username)

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    is_password_valid = pwd_context.verify(form_data.password, user.hashed_password)

    if is_password_valid is False:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except Exception:
        raise credentials_exception

    user = get_user_by_email_repository(email)

    if user is None:
        raise credentials_exception

    return user
