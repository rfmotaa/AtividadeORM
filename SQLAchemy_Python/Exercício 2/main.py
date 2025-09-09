from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from cliente import Cliente
from endereco import Endereco

engine = create_engine('sqlite:///banco_de_dados_cliente_endereco.db')

Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("--- Teste de Mapeamento Associação 1:1 ---")

    novo_endereco = Endereco(rua='Avenida Brasil', numero=100)
    novo_cliente = Cliente(nome='Ana Souza')
    novo_cliente.endereco = novo_endereco

    session.add(novo_cliente)
    session.commit()
    print(f"Cliente '{novo_cliente.nome}' e Endereço associado adicionados com sucesso!")

    cliente_salvo = session.query(Cliente).filter_by(nome='Ana Souza').first()
    if cliente_salvo:
        print(f"Cliente encontrado: {cliente_salvo.nome}")
        print(f"Endereço do cliente: Rua {cliente_salvo.endereco.rua}, Número {cliente_salvo.endereco.numero}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    session.rollback()

finally:
    session.close()