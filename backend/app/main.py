from fastapi import FastAPI
from app.core.config import POSTGRES_USER, origins
from app.logic import router
from app.db.base import database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await database.connect()

app.include_router(router.router)
