import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import BakedGood as BakedGoodModel, db
from sqlalchemy.orm import Session


class BakedGood(SQLAlchemyObjectType):
    class Meta:
        model = BakedGoodModel


class Query(graphene.ObjectType):
    baked_goods = graphene.List(BakedGood)

    def resolve_baked_goods(self, info):
        return db.session.execute(db.select(BakedGoodModel)).scalars()


class AddBakedGood(graphene.Mutation):
    class Arguments:
        item_name = graphene.String(required=True)
        item_price = graphene.Float(required=True)
        item_quantity = graphene.Int(required=True)
        item_category = graphene.String(required=True)

    baked_good = graphene.Field(BakedGood)

    def mutate(self, info, item_name, item_price, item_quantity, item_category):
        with Session(db.engine) as session:
            with session.begin():
                baked_good = BakedGoodModel(
                    item_name=item_name,
                    item_price=item_price,
                    item_quantity=item_quantity,
                    item_category=item_category
                )
                session.add(baked_good)
            session.refresh(baked_good)
        return AddBakedGood(baked_good=baked_good)


class UpdateBakedGood(graphene.Mutation):
    class Arguments:
        item_name = graphene.String(required=True)
        item_price = graphene.Float()
        item_quantity = graphene.Int()
        item_category = graphene.String()

    baked_good = graphene.Field(BakedGood)

    def mutate(self, info, item_name, item_price=None, item_quantity=None, item_category=None):
        with Session(db.engine) as session:
            baked_good = session.get(BakedGoodModel, item_name)
            if not baked_good:
                raise Exception("BakedGood not found")

            if item_price is not None:
                baked_good.item_price = item_price
            if item_quantity is not None:
                baked_good.item_quantity = item_quantity
            if item_category is not None:
                baked_good.item_category = item_category

            session.commit()
            session.refresh(baked_good)
        return UpdateBakedGood(baked_good=baked_good)


class DeleteBakedGood(graphene.Mutation):
    class Arguments:
        item_name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, item_name):
        with Session(db.engine) as session:
            baked_good = session.get(BakedGoodModel, item_name)
            if not baked_good:
                raise Exception("BakedGood not found")

            session.delete(baked_good)
            session.commit()
        return DeleteBakedGood(success=True)

class Mutation(graphene.ObjectType):
    create_baked_good = AddBakedGood.Field()
    update_baked_good = UpdateBakedGood.Field()
    delete_baked_good = DeleteBakedGood.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
