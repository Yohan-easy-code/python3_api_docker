from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from app.database import engine
from app.models.pokemon import Pokemon
from app.schemas import PokemonCreate, PokemonUpdate, PokemonRead
from app.services.pokemon_service import (
    create_pokemon_service,
    get_pokemons_service,
    get_pokemon_service,
    put_update_pokemon_service,
    delete_pokemon_service,
    assign_trainer_service,
    search_pokemons_by_name_service,
)
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.post("/", response_model=PokemonRead)
def create_pokemon(
    pokemon: PokemonCreate,
    current_user=Depends(get_current_user),
):
    return create_pokemon_service(pokemon, current_user.id)


@router.get("/", response_model=list[PokemonRead])
def get_pokemons(
    offset: int = 0,
    limit: int = 10,
    pokemon_type: str | None = None,
    level: int | None = None,
    sort_by: str | None = None,
    order: str | None = None,
):
    return get_pokemons_service(offset, limit, pokemon_type, level, sort_by, order)


@router.get("/search")
def search_pokemons(name: str):
    return search_pokemons_by_name_service(name)


@router.get("/{pokemon_id}", response_model=PokemonRead)
def get_pokemon(pokemon_id: int):
    return get_pokemon_service(pokemon_id)


@router.put("/{pokemon_id}")
def update_pokemon(
    pokemon_id: int,
    updated_pokemon: PokemonUpdate,
    current_user=Depends(get_current_user),
):
    return put_update_pokemon_service(pokemon_id, updated_pokemon, current_user)


@router.put("/{pokemon_id}/trainer/{trainer_id}")
def assign_trainer(
    pokemon_id: int,
    trainer_id: int,
    current_user=Depends(get_current_user),
):
    return assign_trainer_service(pokemon_id, trainer_id, current_user)


@router.delete("/{pokemon_id}")
def delete_pokemon(
    pokemon_id: int,
    current_user=Depends(get_current_user),
):
    return delete_pokemon_service(pokemon_id, current_user)
