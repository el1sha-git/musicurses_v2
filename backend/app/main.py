from fastapi import FastAPI
from app.core.config import POSTGRES_USER
from app.logic import router
from app.db.base import database

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await database.connect()

app.include_router(router.router)
