from fastapi import FastAPI

from app.routes.pokemon import router as pokemon_router

app = FastAPI(title="Pokemon API")


@app.get("/")
def home():
    return {"message": "Pokemon API is running"}


app.include_router(pokemon_router)
