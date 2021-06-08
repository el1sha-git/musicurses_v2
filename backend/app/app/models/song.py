from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base

class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    