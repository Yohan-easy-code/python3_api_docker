from sqlmodel import Session, select

from app.database import engine
from app.models import RevokedToken


def create_revoked_token_repository(token: str):
    revoked_token = RevokedToken(token=token)

    with Session(engine) as session:
        session.add(revoked_token)
        session.commit()
        session.refresh(revoked_token)

        return revoked_token


def get_revoked_token_repository(token: str):
    with Session(engine) as session:
        statement = select(RevokedToken).where(RevokedToken.token == token)
        return session.exec(statement).first()
