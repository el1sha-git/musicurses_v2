from pydantic import BaseModel

from typing import List

class Song(BaseModel):
    id: int
    title: str
    path: str

    class Config:
        orm_mode = True

class Songs(BaseModel):
    __root__: List[Song]

