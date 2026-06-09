from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.trainer import Trainer


class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    hp: int
    pokemon_type: str
    level: int = 1
    attack: str
    mana: int
    capa: str

    trainer_id: int | None = Field(default=None, foreign_key="trainer.id")

    trainer: Optional["Trainer"] = Relationship(back_populates="pokemons")
