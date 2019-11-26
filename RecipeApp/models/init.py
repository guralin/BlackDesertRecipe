import sys

from sqlalchemy import Column, Integer, String, Float, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base

from setting import Base
from setting import ENGINE


class Item(Base):
    __tablename__ = 'item'

    item_id = Column('item_id', Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False, unique=True)
    detail = Column('detail', String(512))
    NPC_price = Column('NPC_price', Integer)
    exchange_price = Column('exchange_price', Integer)

    def __repr__(self):
        return f"<Item(item_id={self.item_id}, name={self.name}, detail={self.detail}, NPC_price{self.NPC_price}, exchange_price={self.exchange_price})>"
        


class Recipe(Base):
    __tablename__ = 'recipe'

    recipe_id = Column('recipe_id', Integer, Sequence('recipe_id_seq'), primary_key=True)
    category_id = Column('category_id', Integer, nullable=False)
    finished_item_id = Column('finished_item_id', Integer,nullable=False)
    material_id = Column('material_id', Integer,nullable=False)
    material_count = Column('material_count', Integer,nullable=False)

    def __repr__(self):
        return f"<Recipe(recipe_id={self.recipe_id}, category_id={self.category_id}, finished_item_id={self.finished_item_id}, material_id={self.material_id}, material_count={self.material_count})>"

class Category(Base):
    __tablename__ = "category"
    category_id = Column('category_id', Integer, primary_key=True)
    category_name = Column('category_name', String(128), nullable=False)

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, category_name={self.category_name})>"


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
