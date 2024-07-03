from fastapi import FastAPI
from app.routers import pokemon
from app.db import init_db, SessionLocal
from app.routers.pokemon import fetch_and_store_pokemon_data

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    async with SessionLocal() as session:
        await fetch_and_store_pokemon_data(session)

# API versioning
app.include_router(pokemon.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
