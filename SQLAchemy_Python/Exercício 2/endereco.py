from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Endereco(Base):
    __tablename__ = 'ENDERECO'
    id = Column('ID', Integer, primary_key=True)
    rua = Column('RUA', String(255))
    numero = Column('NUMERO', Integer)

    cliente = relationship("Cliente", back_populates="endereco")

    def __repr__(self):
        return f"<Endereco(id='{self.id}', rua='{self.rua}', numero='{self.numero}')>"