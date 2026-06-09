from typing import TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.pokemon import Pokemon


class Trainer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    pokemons: List["Pokemon"] = Relationship(back_populates="trainer")
