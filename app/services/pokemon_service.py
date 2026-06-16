from sqlmodel import Session, select
from fastapi import HTTPException

from app.database import engine
from app.models.pokemon import Pokemon
from app.schemas import PokemonCreate, PokemonUpdate
from app.repositories.pokemon_repository import (
    create_pokemon_repository,
    get_pokemon_repository,
    update_pokemon_repository,
)
from app.repositories.trainer_repository import (
    get_trainer_repository,
    count_pokemons_by_trainer_repository,
)


def create_pokemon_service(pokemon: PokemonCreate):

    if pokemon.trainer_id is not None:
        trainer = get_trainer_repository(pokemon.trainer_id)

        if trainer is None:

            raise HTTPException(status_code=404, detail="Trainer not found")

        pokemon_count = count_pokemons_by_trainer_repository(pokemon.trainer_id)

        if pokemon_count >= 6:

            raise HTTPException(
                status_code=400, detail="Trainer already has 6 pokemons"
            )

    db_pokemon = Pokemon(
        name=pokemon.name,
        hp=pokemon.hp,
        pokemon_type=pokemon.pokemon_type,
        level=pokemon.level,
        attack=pokemon.attack,
        mana=pokemon.mana,
        capa=pokemon.capa,
        trainer_id=pokemon.trainer_id,
    )

    return create_pokemon_repository(db_pokemon)


def get_pokemons_service():

    with Session(engine) as session:

        pokemons = session.exec(select(Pokemon)).all()

        return pokemons


def get_pokemon_service(pokemon_id: int):
    with Session(engine) as session:
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        return pokemon


def put_update_pokemon_service(pokemon_id: int, updated_pokemon: PokemonUpdate):
    with Session(engine) as session:
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        pokemon.name = updated_pokemon.name
        pokemon.hp = updated_pokemon.hp
        pokemon.pokemon_type = updated_pokemon.pokemon_type

        session.add(pokemon)
        session.commit()
        session.refresh(pokemon)

        return pokemon


def delete_pokemon_service(pokemon_id: int):
    with Session(engine) as session:
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        session.delete(pokemon)
        session.commit()

        return {"message": "Pokemon deleted"}


def assign_trainer_service(pokemon_id: int, trainer_id: int):

    pokemon = get_pokemon_repository(pokemon_id)

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    trainer = get_trainer_repository(trainer_id)

    if trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")

    pokemon_count = count_pokemons_by_trainer_repository(trainer_id)

    if pokemon_count >= 6:

        raise HTTPException(status_code=400, detail="Trainer already has 6 pokemons")

    pokemon.trainer_id = trainer_id

    return update_pokemon_repository(pokemon)
