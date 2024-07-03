# app/routers/pokemon.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app import crud
from app.schemas import Pokemon as PokemonSchema
from app.models import Pokemon as PokemonModel
from app.db import SessionLocal
import httpx

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

async def fetch_and_store_pokemon_data(db: AsyncSession):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=100")
        response.raise_for_status()
        data = response.json()
        for result in data["results"]:
            pokemon_data = await fetch_pokemon_data(result["url"])
            if pokemon_data:
                await crud.create_pokemon(db, PokemonModel(**pokemon_data))

async def fetch_pokemon_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        types = [type_info["type"]["name"] for type_info in data["types"]]
        return {
            "id": data["id"],
            "name": data["name"],
            "type": ", ".join(types),
            "image": data["sprites"]["front_default"],
        }

@router.get("/pokemons", response_model=List[PokemonSchema])
async def read_pokemons(
    name: Optional[str] = Query(None, min_length=1),
    type: Optional[str] = Query(None, min_length=1),
    db: AsyncSession = Depends(get_db)
):
    if name and type:
        return await crud.get_pokemons_by_name_and_type(db, name, type)
    elif name:
        return await crud.get_pokemons_by_name(db, name)
    elif type:
        return await crud.get_pokemons_by_type(db, type)
    else:
        return await crud.get_pokemons(db)

# New endpoint for fetching Pokemon by name and type
@router.get("/pokemons/filter", response_model=List[PokemonSchema])
async def filter_pokemons(
    name: Optional[str] = Query(None, min_length=1),
    type: Optional[str] = Query(None, min_length=1),
    db: AsyncSession = Depends(get_db)
):
    if name and type:
        return await crud.get_pokemons_by_name_and_type(db, name, type)
    elif name:
        return await crud.get_pokemons_by_name(db, name)
    elif type:
        return await crud.get_pokemons_by_type(db, type)
    else:
        return []
