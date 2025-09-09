from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from cliente import Cliente
from pedido import Pedido

engine = create_engine('sqlite:///banco_de_dados_cliente_pedido.db')

Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("--- Teste de Mapeamento Associação 1:N ---")

    novo_cliente = Cliente(nome='Roberto Silva')
    pedido1 = Pedido()
    pedido2 = Pedido()

    novo_cliente.pedidos.append(pedido1)
    novo_cliente.pedidos.append(pedido2)

    session.add_all([novo_cliente])
    session.commit()
    print(f"Cliente '{novo_cliente.nome}' e seus pedidos adicionados com sucesso!")

    cliente_salvo = session.query(Cliente).filter_by(nome='Roberto Silva').first()
    if cliente_salvo:
        print(f"Cliente encontrado: {cliente_salvo.nome}")
        print(f"Número de pedidos: {len(cliente_salvo.pedidos)}")
        for pedido in cliente_salvo.pedidos:
            print(f"  - ID do Pedido: {pedido.id}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    session.rollback()

finally:
    session.close()