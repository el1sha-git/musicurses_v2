from typing import Generator
from app.db.base import SessionLocal
from app.logic.auth import backends


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

get_current_active_user = backends.fastapi_users.get_current_active_user
current_user = backends.fastapi_users.current_user