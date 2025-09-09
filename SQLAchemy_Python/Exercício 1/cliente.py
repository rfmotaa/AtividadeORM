from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'CLIENTE'

    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"<Cliente(id='{self.id}', nome='{self.nome}')>"