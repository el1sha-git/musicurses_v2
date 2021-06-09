from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from app.db.base import Base, database
from app.schemas.user import UserDB
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class UserTable(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "m_user"
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    phone_number = Column(String(length=18), nullable=False)
    birth_date = Column(Date, nullable=False)

    avatar = relationship("UserAvatar", back_populates="user")


class UserAvatar(Base):
    __tablename__ = 'avatar'
    id = Column(Integer, primary_key=True)
    path = Column(String(length=100), nullable=False)
    user_id = Column(Integer, ForeignKey("m_user.id"))

    user = relationship("UserTable", back_populates="avatar")


users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)
