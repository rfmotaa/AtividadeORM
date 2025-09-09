from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importa a classe Cliente do mesmo diretório
from cliente import Cliente, Base

# Configuração do banco de dados SQLite
engine = create_engine('sqlite:///banco_de_dados_cliente.db')
Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

try:
    print("--- Teste de Mapeamento Classe -> Tabela ---")
    
    novo_cliente = Cliente(nome='Carlos Almeida')
    session.add(novo_cliente)
    session.commit()
    print(f"Cliente '{novo_cliente.nome}' adicionado com sucesso!")
    
    cliente_salvo = session.query(Cliente).filter_by(nome='Carlos Almeida').first()
    if cliente_salvo:
        print(f"Cliente encontrado: ID={cliente_salvo.id}, Nome={cliente_salvo.nome}")
    
    print("\n--- Atualizando o nome do cliente ---")
    if cliente_salvo:
        cliente_salvo.nome = 'Carlos M. Almeida'
        session.commit()
        print(f"Nome atualizado para '{cliente_salvo.nome}'")

    print("\n--- Deletando o cliente ---")
    if cliente_salvo:
        session.delete(cliente_salvo)
        session.commit()
        print("Cliente deletado com sucesso!")
        
        cliente_removido = session.query(Cliente).filter_by(nome='Carlos M. Almeida').first()
        if not cliente_removido:
            print("Verificação: Cliente não existe mais no banco de dados.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    session.rollback()

finally:
    session.close()