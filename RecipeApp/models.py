from sqlalchemy import Column, Integer, String, Float, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'

    p_id = Column('id', Integer, Sequence('some_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False)
    detail = Column('detail', String(512))
    NPC_price = Column('NPC_price', Integer)
    exchange_price = Column('exchange_price', Integer)

    def __repr__(self):
        return "<Item(p_id='%s', name='%s', detail='%s' NPC_price='%s' exchange_price='%s')>" %(self.p_id, self.name, self.detail, self.NPC_price, self.exchange_price)


