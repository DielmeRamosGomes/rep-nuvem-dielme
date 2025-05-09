import graphene

# Modelo do produto
class Produto(graphene.ObjectType):
    id = graphene.Int()
    nome = graphene.String()
    preco = graphene.Float()    

# Lista inicial de produtos (simulando de banco de dados)
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 50.00},
    {"id": 2, "nome": "Tênis", "preco": 120.00}
]

# Queries (Consultas)
class Query(graphene.ObjectType):
    produto = graphene.Field(Produto, id=graphene.Int())
    produtos = graphene.List(Produto)

    # Retorna um produto por ID
    def resolve_produto(root, _, id):
        return next((p for p in produtos if p['id'] == id), None)

    # Retorna todos os produtos
    def resolve_produtos(root, _):
        return produtos

# Mutations (Modificações)
class AdicionarProduto(graphene.Mutation):
    class Arguments:
        nome = graphene.String(required=True)
        preco = graphene.Float(required=True)

    produto = graphene.Field(Produto)

    # Adiciona um novo produto
    def mutate(root,_, nome, preco):
        novo_produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
        produtos.append(novo_produto)
        return AdicionarProduto(produto=novo_produto)

class Mutation(graphene.ObjectType):
    adicionar_produto = AdicionarProduto.Field()

# Schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Servidor Flask para rodar a API GraphQL
from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)




