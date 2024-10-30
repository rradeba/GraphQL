import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.model import Movie as MovieModel, Genre as GenreModel, MovieGenre as MovieGenreModel
from sqlalchemy.orm import Session
from models.model import db  

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class GenreType(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel

class MovieGenre(SQLAlchemyObjectType):
    class Meta:
        model = MovieGenreModel

class Query(graphene.ObjectType):
    movies_by_genre = graphene.List(MovieType, genre_id=graphene.Int(required=True))
    genres_by_movie = graphene.List(GenreType, movie_id=graphene.Int(required=True))

    def resolve_movies_by_genre(self, info, genre_id):
        return MovieModel.query.join(MovieGenreModel).filter(MovieGenreModel.genre_id == genre_id).all()

    def resolve_genres_by_movie(self, info, movie_id):
        return GenreModel.query.join(MovieGenreModel).filter(MovieGenreModel.movie_id == movie_id).all()


