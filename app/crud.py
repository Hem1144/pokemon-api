from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Pokemon

async def get_pokemons(db: AsyncSession):
    result = await db.execute(select(Pokemon))
    return result.scalars().all()

async def get_pokemons_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Pokemon).where(Pokemon.name.ilike(f"%{name}%")))
    return result.scalars().all()

async def get_pokemons_by_type(db: AsyncSession, type: str):
    result = await db.execute(select(Pokemon).where(Pokemon.type.ilike(f"%{type}%")))
    return result.scalars().all()

async def get_pokemons_by_name_and_type(db: AsyncSession, name: str, type: str):
    result = await db.execute(select(Pokemon).where(Pokemon.name.ilike(f"%{name}%"), Pokemon.type.ilike(f"%{type}%")))
    return result.scalars().all()

async def create_pokemon(db: AsyncSession, pokemon: Pokemon):
    db.add(pokemon)
    await db.commit()
    await db.refresh(pokemon)
    return pokemon