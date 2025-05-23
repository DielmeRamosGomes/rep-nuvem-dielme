from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Conectar ao MongoDB
uri = 'mongodb+srv://dielme:1234@cluster0.g8uqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['ecommerce']
produtos_collection = db['produtos']
pedidos_collection = db['pedidos']
historico_collection = db['historico_transacoes']

# Função para processar compra com transação
def processar_compra(cliente_id, produto_id, quantidade):
    session = client.start_session()
    try:
        with session.start_transaction():
            # Atualizar o estoque do produto
            produto = produtos_collection.find_one({"_id": ObjectId(produto_id)}, session=session)
            if produto["estoque"] < quantidade:
                raise Exception("Estoque insuficiente!")
            
            produtos_collection.update_one(
                {"_id": ObjectId(produto_id)},
                {"$inc": {"estoque": -quantidade}},
                session=session
            )

            # Registrar o pedido
            pedido = {
                "cliente_id": cliente_id,
                "produto_id": produto_id,
                "quantidade": quantidade,
                "status": "Confirmado"
            }
            pedidos_collection.insert_one(pedido, session=session)

            # Atualizar histórico de transações do cliente
            historico = {
                "cliente_id": cliente_id,
                "produto_id": produto_id,
                "quantidade": quantidade,
                "tipo_transacao": "Compra"
            }
            historico_collection.insert_one(historico, session=session)

        session.commit_transaction()
        print("Transação realizada com sucesso!")

    except (PyMongoError, Exception) as e:
        session.abort_transaction()
        print(f"Erro na transação: {e}")

    finally:
        session.end_session()

# Simulação de uma compra
processar_compra(cliente_id=1, produto_id="682fc6c799e6c61526eda12e", quantidade=5)




