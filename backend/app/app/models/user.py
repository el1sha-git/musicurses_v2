from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from app.db.base import Base, database
from app.schemas.user import UserDB

from sqlalchemy import Column, String, Integer, Date

class UserTable(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "m_user"
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    phone_number = Column(String(length=18), nullable=False)
    birth_date = Column(Date, nullable=False)


users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

