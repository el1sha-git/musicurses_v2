from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from app.logic.deps import get_db
from app.logic.deps import current_user
from app.schemas.user import User
import aiofiles

from app.utils.name import get_song_name
from app.crud.song import *
from app.schemas.song import *

SONGS_URL = 'app/data/songs/'

router = APIRouter()


@router.get("/")
async def get_song(path: str):
    return FileResponse(path)


@router.post("/", response_model=Song)
async def upload_song(
        name: str,
        db: Session = Depends(get_db),
        file: UploadFile = File(...),
        user: User = Depends(current_user(active=True, superuser=True))
    ):

    new_filename = get_song_name(name, file.filename)

    async with aiofiles.open(SONGS_URL + new_filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    return create_song(db, name, SONGS_URL + new_filename)


@router.delete('/', status_code=205)
async def delete_song(path: str, db: Session = Depends(get_db)):
    await crud_delete_song(db, path)
    await aiofiles.os.remove(path)
    return {"Remove "+path: "OK"}


@router.get("/all_songs", response_model=Songs)
async def get_all_songs(db: Session = Depends(get_db)):
    return crud_get_all_songs(db)


@router.get("/song")
async def get_all_songs():
    return FileResponse('app/data/songs/satisfy.mp3')

