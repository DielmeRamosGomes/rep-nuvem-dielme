class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
class Biblioteca():
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        for livro in self.livros:
            print(f"Titulo: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")

livro = Livro("Narnia", "Guilherme", 1994)
livro2 = Livro("crepusculo", "rafael", 2010)
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()









