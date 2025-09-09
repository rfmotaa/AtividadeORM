from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from base import Base

class Pedido(Base):
    __tablename__ = 'PEDIDO'
    id = Column('ID', Integer, primary_key=True)
    itens = relationship("Item", secondary="PEDIDO_ITEM", back_populates="pedidos")