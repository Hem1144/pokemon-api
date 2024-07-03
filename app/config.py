from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')

settings = Settings()
