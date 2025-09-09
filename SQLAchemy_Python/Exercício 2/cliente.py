from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    endereco_id = Column('ENDERECO_ID', Integer, ForeignKey('ENDERECO.ID'))

    endereco = relationship("Endereco", back_populates="cliente")

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"<Cliente(id='{self.id}', nome='{self.nome}')>"