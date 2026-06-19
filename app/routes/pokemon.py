from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from app.database import engine
from app.models.pokemon import Pokemon
from app.schemas import PokemonCreate, PokemonUpdate
from app.services.pokemon_service import (
    create_pokemon_service,
    get_pokemons_service,
    get_pokemon_service,
    put_update_pokemon_service,
    delete_pokemon_service,
    assign_trainer_service,
    search_pokemons_by_name_service,
)

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.post("/")
def create_pokemon(pokemon: PokemonCreate):

    return create_pokemon_service(pokemon)


@router.get("/")
def get_pokemons(
    offset: int = 0,
    limit: int = 10,
    pokemon_type: str | None = None,
    level: int | None = None,
):
    return get_pokemons_service(offset, limit, pokemon_type, level)


@router.get("/search")
def search_pokemons(name: str):
    return search_pokemons_by_name_service(name)


@router.get("/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    return get_pokemon_service(pokemon_id)


@router.put("/{pokemon_id}")
def update_pokemon(pokemon_id: int, updated_pokemon: PokemonUpdate):
    return put_update_pokemon_service(pokemon_id, updated_pokemon)


@router.put("/{pokemon_id}/trainer/{trainer_id}")
def assign_trainer(pokemon_id: int, trainer_id: int):
    return assign_trainer_service(pokemon_id, trainer_id)


@router.delete("/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    return delete_pokemon_service(pokemon_id)
