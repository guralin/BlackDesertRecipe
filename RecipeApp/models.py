import sys

from sqlalchemy import Column, Integer, String, Float, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base

from setting import Base
from setting import ENGINE


class Item(Base):
    __tablename__ = 'item'

    p_id = Column('id', Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False)
    detail = Column('detail', String(512))
    NPC_price = Column('NPC_price', Integer)
    exchange_price = Column('exchange_price', Integer)

    def __repr__(self):
        #TODO:f""形式でできるとわかったら必ずリファクタリングする
        return "<Item(p_id='%s', name='%s', detail='%s' NPC_price='%s' exchange_price='%s')>" %(self.p_id, self.name, self.detail, self.NPC_price, self.exchange_price)

class Recipe(Base):
    __tablename__ = 'recipe'

    recipe_id = Column('recipe_id', Integer, Sequence('recipe_id_seq'), primary_key=True)
    category_id = Column('category', Integer)
    finished_item = Column('finished_item', Integer)
    material_1_id = Column('material_1_id', Integer)
    material_2_id = Column('material_2_id', Integer)
    material_3_id = Column('material_3_id', Integer)
    material_4_id = Column('material_4_id', Integer)
    material_5_id = Column('material_5_id', Integer)
    material_6_id = Column('material_6_id', Integer)
    material_1_count = Column('material_1_count', Integer)
    material_2_count = Column('material_2_count', Integer)
    material_3_count = Column('material_3_count', Integer)
    material_4_count = Column('material_4_count', Integer)
    material_5_count = Column('material_5_count', Integer)
    material_6_count = Column('material_6_count', Integer)

    def __repr__(self):
        return f"<Recipe(recipe_id={self.recipe_id}, category_id={self.category_id}, finished_item={self.finished_item}, material_1_id={self.material_1_id}, material_2_id={self.material_2_id}, material_3_id={self.material_3_id}, material_4_id={self.material_4_id}, material_5_id={self.material_5_id}, material_6_id={self.material_6_id})>"

class Category(Base):
    __tablename__ = "category"
    category_id = Column('category_id', Integer, primary_key=True)
    category_name = Column('category_name', String(128))

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, category_name={self.category_name})>"


def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
