from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cliente import Cliente, Base
from juridico import Juridico
from fisico import Fisico

engine = create_engine('sqlite:///banco_de_dados_heranca.db')
Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("--- Teste de Mapeamento de Herança ---")
    
    cliente_juridico = Juridico(nome='Empresa X', cnpj='11.111.111/0001-11')
    cliente_fisico = Fisico(nome='Maria Oliveira', cpf='222.222.222-22')

    session.add_all([cliente_juridico, cliente_fisico])
    session.commit()
    print("Clientes jurídico e físico adicionados com sucesso!")

    todos_clientes = session.query(Cliente).all()
    print("\nClientes no banco de dados:")
    for cliente in todos_clientes:
        if isinstance(cliente, Juridico):
            print(f"  - Jurídico: {cliente.nome}, CNPJ: {cliente.cnpj}")
        elif isinstance(cliente, Fisico):
            print(f"  - Físico: {cliente.nome}, CPF: {cliente.cpf}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    session.rollback()

finally:
    session.close()