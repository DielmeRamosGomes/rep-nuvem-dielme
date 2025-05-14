# pip install -r requirements.txt

import graphene

#  Define o tipo de objeto para um produto, com os campos id, nome e preco.
class Produto(graphene.ObjectType):
    id = graphene.Int()
    nome = graphene.String()
    preco = graphene.Float()

# AdicionarProduto: Define uma mutação (uma operação que modifica dados).
# Arguments: Especifica os argumentos necessários para adicionar um produto (nome e preco, ambos obrigatórios).
class AdicionarProduto(graphene.Mutation):
    class Arguments:
        nome = graphene.String(required=True)
        preco = graphene.Float(required=True)

    # produto: Define o tipo de objeto retornado após a mutação (um objeto Produto).
    produto = graphene.Field(Produto)

    # mutate: A função que realmente adiciona o produto à nossa lista produtos (simulando um banco de dados) e retorna o novo produto.
    def mutate(root, _, nome, preco):
        novo_produto = Produto(id=len(produtos) + 1, nome=nome, preco=preco)
        produtos.append(novo_produto)
        return AdicionarProduto(produto=novo_produto)

# Query: Define as consultas que podemos fazer.
class Query(graphene.ObjectType):
    # Uma lista de todos os produtos.
    todos_produtos = graphene.List(Produto)

    # lista todos os produtos
    def lista_todos_produtos(root, info):
        return produtos
    
# Mutation: Agrupa todas as mutações disponíveis.
class Mutation(graphene.ObjectType):
    adicionar_produto = AdicionarProduto.Field()

# Cria uma instância do esquema GraphQL, combinando as consultas e mutações.
schema = graphene.Schema(query=Query, mutation=Mutation)
produtos = [
    Produto(nome="Camiseta", preco=50.00),
    Produto(nome="Tênis", preco=120.00),
    Produto(nome="Calça", preco=80.00)
]  # Lista para armazenar produtos (simulando um banco de dados)


