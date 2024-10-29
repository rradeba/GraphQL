from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 

class Base(DeclarativeBase):
    pass 

db = SQLAlchemy(model_class=Base)

class BakedGood(Base):

    __tablename__= 'baked_goods'
    item_name: Mapped[int] = mapped_column(primary_key=True)
    item_price: Mapped[float] = mapped_column(db.Float)
    item_quantity: Mapped[str] = mapped_column(db.Integer)
    item_category: Mapped[int] = mapped_column(db.String(255))


