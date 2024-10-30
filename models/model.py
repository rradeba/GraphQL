from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Genre(Base):
    __tablename__ = 'genres'
    
    genre_id: Mapped[int] = mapped_column(primary_key=True)
    genre_name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    
    movies = relationship('MovieGenre', back_populates='genre')

class Movie(Base):
    __tablename__ = 'movies'
    
    movie_id: Mapped[int] = mapped_column(primary_key=True)
    movie_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    
    genres = relationship('MovieGenre', back_populates='movie')

class MovieGenre(Base):
    __tablename__ = 'movie_genre'
    
    movie_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('movies.movie_id'), primary_key=True)
    genre_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('genres.genre_id'), primary_key=True)

    movie = relationship(Movie, back_populates='genres')
    genre = relationship(Genre, back_populates='movies')


