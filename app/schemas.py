from sqlmodel import SQLModel


class PokemonCreate(SQLModel):
    name: str
    hp: int
    pokemon_type: str
    level: int
    attack: str
    mana: int
    capa: str
    trainer_id: int | None = None


class PokemonUpdate(SQLModel):
    name: str
    hp: int
    pokemon_type: str


class PokemonRead(SQLModel):
    id: int
    name: str
    hp: int
    pokemon_type: str
    level: int
    attack: str
    mana: int
    capa: str
    trainer_id: int | None = None


class TrainerReadWithPokemons(SQLModel):
    id: int
    name: str
    pokemons: list[PokemonRead] = []


class TrainerCreate(SQLModel):
    name: str


class TrainerUpdate(SQLModel):
    name: str


class TrainerRead(SQLModel):
    id: int
    name: str
