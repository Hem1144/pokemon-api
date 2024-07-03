### Create virtual environment in windows OS

python -m venv venv
source venv/Scripts/activate

### Configure poetry for project set-up

pip install poery
poetry init
poetry add uvicorn fastapi sqlalchemy[asyncio] asyncpg

### To run project

uvicorn app.main:app --reload

### Add database connection string in .env file

DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase

### Download the necessary packages for the project run this command

pip install -r requirements.txt

### Limit the number of Pokemons list in the database by setting limit=desired_limit upto 100000 in routers/pokemon.py file, here i set limit=100

https://pokeapi.co/api/v2/pokemon?limit=100

### API for Pokemons list that will come from Postgres databse

http://127.0.0.1:8000/api/v1/pokemons

### To see list of pokemons with their name by following query params

http://127.0.0.1:8000/api/v1/pokemons?name=any_name

### To see list of pokemons with their name and type by following query params

http://127.0.0.1:8000/api/v1/pokemons?name=some_name&type=some_type
