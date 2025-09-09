# pedido.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Pedido(Base):
    __tablename__ = 'PEDIDO'
    id = Column('ID', Integer, primary_key=True)
    cliente_id = Column('C_ID', Integer, ForeignKey('CLIENTE.ID'))

    cliente = relationship("Cliente", back_populates="pedidos") 