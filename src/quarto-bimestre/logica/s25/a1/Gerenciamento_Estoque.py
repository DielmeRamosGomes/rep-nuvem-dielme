class Produto:
    def __init__(self, id, nome, quantidade):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade

    def getId(self):
        return self.__id
    
    def getNome(self):
        return self.__nome
    
    def getQuantidade(self):
        return self.__quantidade
    
    def setRetirar(self, quantidade):
        self.__quantidade -= quantidade
        
    def setAdicionar(self, quantidade):
        self.__quantidade += quantidade
    
    def exibirDetalhes(self):
        print("Detalhes do Produto:")
        print(f"ID: {self.getId()}")
        print(f"Produto: {self.getNome()}")
        print(f"Quantidade em estoque: {self.getQuantidade()}")

class Estoque:
    def __init__(self):
        self.__produtos = []

    def add_produto(self, produto):
        self.__produtos.append(produto)
    
    def buscar_produto(self, id):
        for produto in self.__produtos:
            if produto.getId() == id:
                return produto
        return None
    
    def atualizar_estoque(self, id, quantidade):
        produto = self.buscar_produto(id)
        if produto:
            produto.setRetirar(quantidade)
        else:
            print("Produto não encontrado.")
            
    def adicionar_estoque(self, id, quantidade):
        produto = self.buscar_produto(id)
        if produto:
            produto.setAdicionar(quantidade)
        else:
            print("Produto não encontrado.")
    
    def mostrar_produto(self, id):
        produto = self.buscar_produto(id)
        if produto:
            produto.exibirDetalhes()
            print("----------------------------------------")
        else:
            print("Produto não encontrado.")
    
    def exibir_estoque(self):
        print("Estoque Atual:")
        for produto in self.__produtos:
            produto.exibirDetalhes()
            print("----------------------------------------")
        
produto1 = Produto(1, "Caneta", 20)
produto2 = Produto(2, "Caderno", 15)
produto3 = Produto(3, "Borracha", 10)
produto4 = Produto(4, "Lápis", 30)
produto5 = Produto(5, "Mochila", 5)

estoque = Estoque()
estoque.add_produto(produto1)
estoque.add_produto(produto2)
estoque.add_produto(produto3)
estoque.add_produto(produto4)
estoque.add_produto(produto5)

#estoque.atualizar_estoque(1, 3)  # Retirar 3 canetas
#estoque.mostrar_produto(1)  # Mostrar detalhes da caneta

#estoque.atualizar_estoque(4, 2)  # Retirar 2 Lápis
#estoque.mostrar_produto(4)  # Mostrar detalhes do Lápis

#estoque.adicionar_estoque(5, 10)  # Adicionar 10 mochilas
#estoque.mostrar_produto(5)  # Mostrar detalhes da mochila

estoque.exibir_estoque()  # Exibir todo o estoque