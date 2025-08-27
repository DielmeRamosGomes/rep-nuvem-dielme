class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__preco = preco

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def get_preco(self):
        return self.__preco
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao

    def set_preco(self, preco):
        self.__preco = preco

    def get_detalhes(self):
        print(f"\nTítulo: {self.get_titulo()}")
        print(f"Autor: {self.get_autor()}")
        print(f"Ano de Publicação: {self.get_ano_publicacao()}")
        print(f"Preço: {self.get_preco()}\n")

harry_potter_I = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 39.90)
harry_potter_I.get_detalhes()

harry_potter_II = Livro("Harry Potter e a Câmara Secreta", "J.K. Rowling", 1998, 42.90)
harry_potter_II.get_detalhes()
