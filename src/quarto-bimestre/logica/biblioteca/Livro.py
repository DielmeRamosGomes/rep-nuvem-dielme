class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponivel = True

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_ano_publicacao(self):
        return self.ano_publicacao
    
    def get_genero(self):
        return self.genero
    
    def is_disponivel(self):
        return self.disponivel
    
    def mostrar_livro(self):
        print(f"Título: {self.get_titulo()}")
        print(f"Autor: {self.get_autor()}")
        print(f"Ano de Publicação: {self.get_ano_publicacao()}")
        print(f"Gênero: {self.get_genero()}")
        print(f"Disponível: {'Sim' if self.is_disponivel() else 'Não'}")
