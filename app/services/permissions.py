from fastapi import HTTPException


def check_pokemon_owner_or_admin(pokemon, current_user):
    if current_user.role != "admin" and pokemon.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")


def check_admin(current_user):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")
