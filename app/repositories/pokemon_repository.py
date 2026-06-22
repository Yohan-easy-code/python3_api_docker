from sqlmodel import Session, select

from fastapi import HTTPException

from app.database import engine
from app.models.pokemon import Pokemon


def create_pokemon_repository(pokemon):

    with Session(engine) as session:

        session.add(pokemon)

        session.commit()

        session.refresh(pokemon)

        return pokemon


def get_pokemons_repository(
    offset: int = 0,
    limit: int = 10,
    pokemon_type: str | None = None,
    level: int | None = None,
    sort_by: str | None = None,
    order: str | None = None,
):

    with Session(engine) as session:
        statement = select(Pokemon)

        if pokemon_type is not None:
            statement = statement.where(Pokemon.pokemon_type == pokemon_type)

        if level is not None:
            statement = statement.where(Pokemon.level == level)

        if sort_by is not None:

            column = getattr(Pokemon, sort_by)

            if order == "desc":

                statement = statement.order_by(column.desc())

            else:

                statement = statement.order_by(column.asc())

        statement = statement.offset(offset).limit(limit)

        return session.exec(statement).all()


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


def search_pokemons_by_name_repository(name: str):
    with Session(engine) as session:
        statement = select(Pokemon).where(Pokemon.name.ilike(f"%{name}%"))

        return session.exec(statement).all()
