from fastapi import FastAPI

from app.routes.pokemon import router as pokemon_router
from app.routes.trainer import router as trainer_router
from app.routes.auth import router as auth_router

app = FastAPI(title="Pokemon API")


@app.get("/")
def home():
    return {"message": "Pokemon API is running"}


app.include_router(pokemon_router)
app.include_router(trainer_router)
app.include_router(auth_router)
