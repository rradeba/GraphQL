import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.model import Genre as GenreModel, db
from sqlalchemy.orm import Session


class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel


class Query(graphene.ObjectType):
    genres = graphene.List(Genre)

    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars()


class CreateGenre(graphene.Mutation):
    class Arguments:
        genre_id = graphene.Int(required=True)
        genre_name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, genre_id, genre_name):
        if not genre_name:
            raise Exception("Genre empty.")
        if len(genre_name) > 100: 
            raise Exception("Genre greater than 100 characters.")

        with Session(db.engine) as session:
            with session.begin():
                genre = GenreModel(
                    genre_id=genre_id,
                    genre_name=genre_name
                )
                session.add(genre)
            session.refresh(genre)
        return CreateGenre(genre=genre)


class UpdateGenre(graphene.Mutation):
    class Arguments:
        genre_id = graphene.Int(required=True)
        genre_name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, genre_id, genre_name):
        if not genre_name:
            raise Exception("Genre empty.")
        if len(genre_name) > 100:  
            raise Exception("Genre greater than 100 characters.")

        with Session(db.engine) as session:
            genre = session.get(GenreModel, genre_id)
            if not genre:
                raise Exception("Genre not found.")

            genre.genre_name = genre_name
            session.commit()
            session.refresh(genre)
        return UpdateGenre(genre=genre)


class DeleteGenre(graphene.Mutation):
    class Arguments:
        genre_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, genre_id):
        with Session(db.engine) as session:
            genre = session.get(GenreModel, genre_id)
            if not genre:
                raise Exception("Genre ID not found.")

            session.delete(genre)
            session.commit()
        return DeleteGenre(success=True)


class Mutation(graphene.ObjectType):
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
