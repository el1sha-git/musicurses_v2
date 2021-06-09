from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from app.db.base import Base

class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    path = Column(String(length=100), nullable=False)


songs = Song.__table__

class Playlist(Base):
    __tablename__ = 'playlist'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    desc = Column(Text, nullable=True)
