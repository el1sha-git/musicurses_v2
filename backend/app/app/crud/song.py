from sqlalchemy.orm import Session
from app.models.song import Song, songs


def create_song(db: Session, name, path):
    song = Song(title=name, path=path)
    db.add(song)
    db.commit()
    db.refresh(song)
    return song


def crud_get_all_songs(db: Session):
    return db.query(Song).all()


async def crud_delete_song(db: Session, uri: str):
    d = songs.delete().where(songs.c.path == uri)
    db.execute(d)
    db.commit()
