from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session
from sqlmodel import select

app = FastAPI()


class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    hp: int
    pokemon_type: str


sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/pokemon")
def create_pokemon(pokemon: Pokemon):
    with Session(engine) as session:
        session.add(pokemon)
        session.commit()
        session.refresh(pokemon)

        return pokemon


@app.get("/pokemons")
def get_pokemons():

    with Session(engine) as session:

        pokemons = session.exec(select(Pokemon)).all()

        return pokemons


@app.get("/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id: int):

    with Session(engine) as session:

        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        return pokemon


@app.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, updated_pokemon: Pokemon):

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


@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):

    with Session(engine) as session:

        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        session.delete(pokemon)
        session.commit()

        return {"message": "Pokemon deleted"}
