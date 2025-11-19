from Biblioteca import Biblioteca
from Usuario import Usuario
from Livro import Livro
from Emprestimo import Emprestimo

if __name__=="__main__":
    biblioteca = Biblioteca()
    usuario1 = Usuario(1, "Dielme Ramos", "dielme@exemplo.com", "1234")
    usuario2 = Usuario(2, "Luis Carlos", "luis@exemplo.com", "12345")
    livro1 = Livro(1, "Harry Potter I", "JK Rowling", "1993-06-15", "Fantasia")
    livro2 = Livro(2, "Harry Potter II", "JK Rowling", "1996-07-20", "Fantasia")
    livro3 = Livro(3, "História do Futebol", "Dielme Ramos", "2025-11-19", "Esporte")
    emprestimo1 = Emprestimo(1, usuario1, livro1, "14-11-2025", "20-11-2025")
    biblioteca.adicionar_usuario(usuario1)
    biblioteca.adicionar_usuario(usuario2)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_emprestimo(emprestimo1)
    #biblioteca.mostrar_emprestimos()
    #biblioteca.mostra_usuarios()
    #biblioteca.remover_usuario(2)
    #print("\nRemovendo o usuario com o ID = 2")
    #biblioteca.mostra_usuarios()    
    #biblioteca.mostra_livros()
    #biblioteca.buscar_livro_genero("ficção")
    
    
    
    
    
    
    