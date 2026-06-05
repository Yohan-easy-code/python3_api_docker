from sqlmodel import SQLModel


class PokemonCreate(SQLModel):
    name: str
    hp: int
    pokemon_type: str


class PokemonUpdate(SQLModel):
    name: str
    hp: int
    pokemon_type: str


class PokemonRead(SQLModel):
    id: int
    name: str
    hp: int
    pokemon_type: str
