from fastapi import FastAPI
from app.core.config import POSTGRES_USER
app = FastAPI()

@app.get("/")
async def root():
    return {"message": str(POSTGRES_USER)}