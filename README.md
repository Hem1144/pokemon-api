### Create virtual environment in windows OS

python -m venv venv
source venv/Scripts/activate

### Configure poetry for project set-up

pip install poery
poetry init
poetry add uvicorn fastapi sqlalchemy[asyncio] asyncpg

### To run project

uvicorn app.main:app --reload
