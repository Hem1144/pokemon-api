from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    image: str

    class Config:
        orm_mode = True  