from sqlmodel import Session

from app.database import engine
from app.models.pokemon import Pokemon


def create_pokemon_repository(pokemon):

    with Session(engine) as session:

        session.add(pokemon)

        session.commit()

        session.refresh(pokemon)

        return pokemon
