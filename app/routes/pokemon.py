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
)

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.post("/")
def create_pokemon(pokemon: PokemonCreate):

    return create_pokemon_service(pokemon)


@router.get("/")
def get_pokemons():
    return get_pokemons_service()


@router.get("/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    return get_pokemon_service(pokemon_id)


@router.put("/{pokemon_id}")
def update_pokemon(pokemon_id: int, updated_pokemon: PokemonUpdate):
    return put_update_pokemon_service(pokemon_id, updated_pokemon)


@router.delete("/{pokemon_id}")
def delete_pokemon(pokemon_id: int):
    return delete_pokemon_service(pokemon_id)
