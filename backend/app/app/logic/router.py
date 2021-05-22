from fastapi import APIRouter
from app.logic.api import api_coms
from app.logic.auth.router import user

router = APIRouter()

router.include_router(api_coms.router, prefix="/api")
router.include_router(user.router)
