from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from app.database import engine
from app.models import Trainer, Pokemon


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

        statement = (
            select(Trainer)
            .where(Trainer.id == trainer_id)
            .options(selectinload(Trainer.pokemons))
        )

        return session.exec(statement).first()


def delete_trainer_repository(trainer: Trainer):
    with Session(engine) as session:
        db_trainer = session.get(Trainer, trainer.id)

        session.delete(db_trainer)
        session.commit()

        return {"message": "Trainer deleted"}


def count_pokemons_by_trainer_repository(trainer_id: int):

    with Session(engine) as session:

        pokemons = session.exec(
            select(Pokemon).where(Pokemon.trainer_id == trainer_id)
        ).all()

        return len(pokemons)
