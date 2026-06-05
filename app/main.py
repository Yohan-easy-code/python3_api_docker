from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routes.pokemon import router as pokemon_router

app = FastAPI(title="Pokemon API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def home():
    return {"message": "Pokemon API is running"}


app.include_router(pokemon_router)
