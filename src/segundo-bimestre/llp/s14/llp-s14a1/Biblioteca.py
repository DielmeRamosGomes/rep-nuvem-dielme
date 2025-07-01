from abc import ABC, abstractmethod

class FuncionalidadesBiblioteca(ABC):
    @abstractmethod
    def adicionar_livro(self, livro):
        pass
    
    @abstractmethod
    def remover_livro(self, codigo):
        pass
    
    @abstractmethod
    def getLivros(self):
        pass
    
    @abstractmethod
    def getLivros(self, codigo_usuario):
        pass
    
class Biblioteca(FuncionalidadesBiblioteca):
    def __init__(self):
        self.__livros = [Livros]
        self.__usuarios = [Usuario]
        self.__emprestimos = [Emprestimo]
    
    def buscar_usuario(self, codigo_usuario):
        if len(self.__usuarios) == 0:
            return "Nenhum usuário cadastrado."
        elif codigo_usuario < 0 or codigo_usuario >= len(self.__usuarios):
            return "Código inválido."
        elif self.__usuarios[codigo_usuario] is None:
            return "Usuário não encontrado."
        else:
            for usuario in self.__usuarios:
                if usuario.getCodigoUsuario() == codigo_usuario:
                    return usuario
    
    def buscar_livro(self, codigo_livro):
        if len(self.__livros) == 0:
            return "Nenhum livro cadastrado."
        elif codigo_livro < 0 or codigo_livro >= len(self.__livros):
            return "Código inválido."
        elif self.__livros[codigo_livro] is None:
            return "Livro não encontrado."
        else:
            for livro in self.__livros:
                if livro.getCodigo() == codigo_livro:
                    return livro
    
    def mostrar_emprestimo(self, emprestimo):
        usuario = self.buscar_usuario(emprestimo.getCodigoUsuario())
        livro = self.buscar_livro(emprestimo.getCodigoLivro())
        print(f"Usuário: {usuario.getNome()} (Código: {usuario.getCodigoUsuario()})")
        print(f"Livro: {livro.getTitulo()} (Código: {livro.getCodigo()})")
        print(f"Data de Empréstimo: {emprestimo.getDataEmprestimo()}")
        print(f"Data de Devolução: {emprestimo.getDataDevolucao()}")
        
    def adicionar_emprestimo(self, emprestimo):
            self.__emprestimos.append(emprestimo)
    
    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        
    def remover_usuario(self, codigo_usuario):
        if len(self.__usuarios) == 0:
            return "Nenhum usuário cadastrado."
        elif codigo_usuario < 0 or codigo_usuario >= len(self.__usuarios):
            return "Código inválido."
        elif self.__usuarios[codigo_usuario] is None:
            return "Usuário não encontrado."
        else:
            for usuario in self.__usuarios:
                if usuario.getCodigoUsuario() == codigo_usuario:
                    self.__usuarios.remove(usuario)
                    return "Usuário removido com sucesso."
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        
    def remover_livro(self, codigo):
        if len(self.__livros) == 0:
            return "Nenhum livro cadastrado."
        elif codigo < 0 or codigo >= len(self.__livros):
            return "Código inválido."
        elif self.__livros[codigo] is None:
            return "Livro não encontrado."
        else:
            for livro in self.__livros:
                if livro.getCodigo() == codigo:
                    self.__livros.remove(livro)
                    return "Livro removido com sucesso."
            
    def getLivros(self):
        if len(self.__livros) == 0:
            return "Nenhum livro cadastrado."
        else:
            for livro in self.__livros:
                print(f"Código: {livro.getCodigo()}")
                print(f"Título: {livro.getTitulo()}")
                print(f"Autor: {livro.getAutor()}")
                print(f"Ano: {livro.getAno()}")
                print(f"Descrição: {livro.getDescricao()}")
                print("-----------------------------")

class Livros:
    def __init__(self,codigo, titulo, autor, ano, descricao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__descricao = descricao

    def getCodigo(self):
        return self.__codigo
    
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getAno(self):
        return self.__ano
    
    def getDescricao(self):
        return self.__descricao
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
        
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setAutor(self, autor):
        self.__autor = autor

    def setAno(self, ano):
        self.__ano = ano
        
    def setDescricao(self, descricao):
        self.__descricao = descricao
        
class Usuario:
    def __init__(self, codigo_usuario ,nome, email, senha):
        self.__codigo_usuario = codigo_usuario
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def getCodigoUsuario(self):
        return self.__codigo_usuario
    
    def getSenha(self):
        return self.__senha
    
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email
    
    def setCodigoUsuario(self, codigo_usuario):
        self.__codigo_usuario = codigo_usuario
    
    def setNome(self, nome):
        self.__nome = nome
        
    def setEmail(self, email):
        self.__email = email    
      
    def setSenha(self, senha):
        self.__senha = senha

class Emprestimo:
    def __init__(self, codigo_usuario, codigo_livro, data_emprestimo, data_devolucao):
        self.__codigo_usuario = codigo_usuario
        self.__codigo_livro = codigo_livro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
    
    def getCodigoUsuario(self):
        return self.__codigo_usuario
    
    def getCodigoLivro(self):
        return self.__codigo_livro
    
    def getDataEmprestimo(self):
        return self.__data_emprestimo
    
    def getDataDevolucao(self):
        return self.__data_devolucao
    
biblioteca = Biblioteca()
usuario = Usuario(1, "Dielme", "dielme@exemplo.com", "1234")    
livro = Livros(1, "Aprendendo Python", "Azuma", "2025", "Livro sobre Python")
livro2 = Livros(2, "Aprendendo Java", "Akira", "2025", "Livro sobre Java")
emprestimo = Emprestimo(1, 1, "2025-06-29", "2025-07-05")
biblioteca.adicionar_usuario(usuario)
biblioteca.adicionar_livro(livro)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_emprestimo(emprestimo)

biblioteca.getLivros()



