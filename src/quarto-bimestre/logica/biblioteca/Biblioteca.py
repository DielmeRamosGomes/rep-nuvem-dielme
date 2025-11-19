class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.get_id() == id:
                return usuario
        return
    
    def remover_usuario(self, id):
        usuario = self.buscar_usuario(id)
        self.usuarios.remove(usuario)
    
    def mostra_usuarios(self):
        for usuario in self.usuarios:
            usuario.mostra_usuario()
            print("------------------------------------")    
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def mostra_livros(self):
        for livro in self.livros:
            livro.mostrar_livro()
            print("------------------------------------")    
    
    def buscar_livro(self, id):
        for livro in self.livros:
            if livro.get_id() == id:
                return livro
        return
    
    def buscar_livro_genero(self, genero):
        livros_por_genero = []
        for livro in self.livros:
            if livro.get_genero().lower() == genero.lower():
                livros_por_genero.append(livro)
        if livros_por_genero != []:
            self.mostra_livros_por_genero(livros_por_genero)
        else:
            print("Não existem livros com esse Gênero!")
    
    def mostra_livros_por_genero(self, livros):
        for livro in livros:
            livro.mostrar_livro()
            print("------------------------------------")
    
    def remover_livro(self, id):
        livro = self.buscar_livro(id)
        self.livros.remove(livro)
    
    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo) 
        
    def mostrar_emprestimos(self):
        for emprestimo in self.emprestimos:
            emprestimo.mostrar_emprestimo()  
            print("------------------------------------")
        
        
        
        