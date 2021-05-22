from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from app.core.config import SECRET, JWT_LIFETIME_SECONDS
from app.models.user import user_db
from app.schemas.user import *


jwt_authentication = JWTAuthentication(
    secret=SECRET,
    lifetime_seconds=JWT_LIFETIME_SECONDS
    )

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
