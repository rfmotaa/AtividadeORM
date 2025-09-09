from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from base import Base

class Item(Base):
    __tablename__ = 'ITEM'
    id = Column('ID', Integer, primary_key=True)
    pedidos = relationship("Pedido", secondary="PEDIDO_ITEM", back_populates="itens")