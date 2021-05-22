from fastapi import APIRouter, Depends
from app.schemas.user import User
from app.logic.deps import get_current_active_user

router = APIRouter()

@router.get('/', response_model=User)
def user_data(user: User = Depends(get_current_active_user)):
    return user

