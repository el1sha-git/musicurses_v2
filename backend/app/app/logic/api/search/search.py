from fastapi import APIRouter

router = APIRouter()

@router.get('/get_similar')
async def echo(text: str):
    return {"Input": text}