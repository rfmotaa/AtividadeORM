from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    tipo = Column('TIPO', String(50))
    __mapper_args__ = {
        'polymorphic_on': tipo,
        'polymorphic_identity': 'cliente'
    }