from sqlmodel import Session, select

from app.database import engine
from app.models import Trainer


def create_trainer_repository(trainer: Trainer):
    with Session(engine) as session:
        session.add(trainer)
        session.commit()
        session.refresh(trainer)

        return trainer


def get_trainers_repository():
    with Session(engine) as session:
        return session.exec(select(Trainer)).all()


def get_trainer_repository(trainer_id: int):
    with Session(engine) as session:
        return session.get(Trainer, trainer_id)
