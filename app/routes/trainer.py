from fastapi import APIRouter, Depends

from app.schemas import TrainerCreate, TrainerReadWithPokemons, TrainerRead
from app.services.trainer_service import (
    create_trainer_service,
    get_trainers_service,
    get_trainer_service,
    delete_trainer_service,
)
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/trainers", tags=["Trainers"])


@router.post("/", response_model=list[TrainerRead])
def create_trainer(trainer: TrainerCreate, current_user=Depends(get_current_user)):
    return create_trainer_service(trainer)


@router.get("/", response_model=list[TrainerRead])
def get_trainers():
    return get_trainers_service()


@router.get("/{trainer_id}", response_model=TrainerReadWithPokemons)
def get_trainer(trainer_id: int):
    return get_trainer_service(trainer_id)


@router.delete("/{trainer_id}")
def delete_trainer(trainer_id: int, current_user=Depends(get_current_user)):
    return delete_trainer_service(trainer_id)
