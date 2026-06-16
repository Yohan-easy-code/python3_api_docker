from sqlmodel import Session

from app.database import engine
from app.models.pokemon import Pokemon


def create_pokemon_repository(pokemon):

    with Session(engine) as session:

        session.add(pokemon)

        session.commit()

        session.refresh(pokemon)

        return pokemon


def get_pokemon_repository(pokemon_id: int):

    with Session(engine) as session:

        return session.get(Pokemon, pokemon_id)


def update_pokemon_repository(pokemon: Pokemon):

    with Session(engine) as session:
        db_pokemon = session.get(Pokemon, pokemon.id)
        db_pokemon.trainer_id = pokemon.trainer_id

        session.add(db_pokemon)
        session.commit()
        session.refresh(db_pokemon)

        return db_pokemon
