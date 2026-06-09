from fastapi import APIRouter

from app.schemas import TrainerCreate
from app.services.trainer_service import (
    create_trainer_service,
    get_trainers_service,
    get_trainer_service,
)

router = APIRouter(prefix="/trainers", tags=["Trainers"])


@router.post("/")
def create_trainer(trainer: TrainerCreate):
    return create_trainer_service(trainer)


@router.get("/")
def get_trainers():
    return get_trainers_service()


@router.get("/{trainer_id}")
def get_trainer(trainer_id: int):
    return get_trainer_service(trainer_id)
