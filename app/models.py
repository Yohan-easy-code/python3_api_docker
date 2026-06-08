from sqlmodel import SQLModel, Field


class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    hp: int
    pokemon_type: str
    level: int = 1
    attack: str
    mana: int
    capa: str
