from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer, ForeignKey

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

    trainer_id: int | None = Field(
        default=None,
        sa_column=Column(
            Integer, ForeignKey("trainer.id", ondelete="SET NULL"), nullable=True
        ),
    )
    created_by: int | None = Field(default=None, foreign_key="users.id")

    trainer: Optional["Trainer"] = Relationship(back_populates="pokemons")
