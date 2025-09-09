from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

from base import Base
from pedido import Pedido
from item import Item

pedido_item_table = Table(
    'PEDIDO_ITEM', Base.metadata,
    Column('pedido_id', Integer, ForeignKey('PEDIDO.ID')),
    Column('item_id', Integer, ForeignKey('ITEM.ID'))
)

engine = create_engine('sqlite:///banco_de_dados_pedido_item.db')
Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("--- Teste de Mapeamento Associação N:N ---")

    item1 = Item()
    item2 = Item()
    pedido1 = Pedido()

    pedido1.itens.append(item1)
    pedido1.itens.append(item2)

    session.add(pedido1)
    session.commit()
    print(f"Pedido {pedido1.id} e seus itens associados adicionados com sucesso!")

    pedido_salvo = session.query(Pedido).filter_by(id=pedido1.id).first()
    if pedido_salvo:
        print(f"Pedido {pedido_salvo.id} encontrado.")
        print(f"Este pedido tem {len(pedido_salvo.itens)} itens associados.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    session.rollback()

finally:
    session.close()