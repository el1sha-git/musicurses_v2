""" This file commutation all urls from api"""
from fastapi import APIRouter
from app.logic.api.user import user
from app.logic.api.song import song
from app.logic.api.search import search

router = APIRouter()

router.include_router(user.router, prefix="/user", tags=['User'])
router.include_router(song.router, prefix="/song", tags=['Song'])
router.include_router(search.router, prefix="/search", tags=['Search'])