from sqlmodel import Session, select

from app.database import engine
from app.models import User


def create_user_repository(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        return user


def get_user_by_email_repository(email: str):
    with Session(engine) as session:
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()
