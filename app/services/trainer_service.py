from fastapi import HTTPException

from app.models import Trainer
from app.schemas import TrainerCreate
from app.repositories.trainer_repository import (
    create_trainer_repository,
    get_trainers_repository,
    get_trainer_repository,
)


def create_trainer_service(trainer: TrainerCreate):
    db_trainer = Trainer(name=trainer.name)

    return create_trainer_repository(db_trainer)


def get_trainers_service():
    return get_trainers_repository()


def get_trainer_service(trainer_id: int):
    trainer = get_trainer_repository(trainer_id)

    if trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")

    return trainer
