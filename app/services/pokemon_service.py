from sqlmodel import Session, select

from app.database import engine
from app.models.pokemon import Pokemon
from app.schemas import PokemonCreate, PokemonUpdate
from app.repositories.pokemon_repository import create_pokemon_repository


def create_pokemon_service(pokemon: PokemonCreate):

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
