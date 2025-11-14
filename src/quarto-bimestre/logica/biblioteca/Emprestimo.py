class Emprestimo:
    def __init__(self, id, usuario, livro, data_emprestimo, data_devolucao):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def get_id(self):
        return self.id
    
    def get_usuario(self):
        return self.usuario
    
    def get_livro(self):
        return self.livro
    
    def get_data_emprestimo(self):
        return self.data_emprestimo
    
    def get_data_devolucao(self):
        return self.data_devolucao

    def mostrar_emprestimo(self):
        print(f"\nID Empréstimo: {self.get_id()}")
        print(f"\nUsuário")
        self.get_usuario().mostra_usuario()
        print(f"\nLivro")
        self.get_livro().mostrar_livro()
        print(f"\nData de Empréstimo: {self.get_data_emprestimo()}")
        print(f"Data de Devolução: {self.get_data_devolucao()}")


