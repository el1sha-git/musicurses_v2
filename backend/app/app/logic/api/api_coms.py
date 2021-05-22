""" This file commutation all urls from api"""
from fastapi import APIRouter
from app.logic.api.user import user

router = APIRouter()

router.include_router(user.router, prefix="/user", tags=['User'])
