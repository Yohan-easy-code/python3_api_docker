import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine

from app.main import app
from app.models import Pokemon, Trainer, User, RevokedToken

TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture()
def test_engine(monkeypatch):
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )

    SQLModel.metadata.create_all(engine)

    import app.database as database
    import app.repositories.pokemon_repository as pokemon_repository
    import app.repositories.trainer_repository as trainer_repository
    import app.repositories.user_repository as user_repository
    import app.repositories.revoked_token_repository as revoked_token_repository
    import app.services.pokemon_service as pokemon_service
    import app.services.trainer_service as trainer_service

    monkeypatch.setattr(database, "engine", engine)
    monkeypatch.setattr(pokemon_repository, "engine", engine)
    monkeypatch.setattr(trainer_repository, "engine", engine)
    monkeypatch.setattr(user_repository, "engine", engine)
    monkeypatch.setattr(revoked_token_repository, "engine", engine)
    monkeypatch.setattr(pokemon_service, "engine", engine)

    yield engine

    SQLModel.metadata.drop_all(engine)


@pytest.fixture()
def client(test_engine):
    return TestClient(app)
