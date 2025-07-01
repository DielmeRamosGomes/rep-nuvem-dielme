class Usuario:
    def __init__(self, nome, email, senha):
        self.__codigo_usuario = 0
        self.setCodigoUsuario()
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def getCodigoUsuario(self):
        return self.__codigo_usuario

    def setCodigoUsuario(self):
        if self.__codigo_usuario == 0:
            self.__codigo_usuario += 1
        else:
            self.__codigo_usuario += 1
        
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
        
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
        
    def getSenha(self):
        return self.__senha
    
    def setSenha(self, senha):
        self.__senha = senha
        
    def mostrar_usuario(self):
        return f"Código: {self.getCodigoUsuario()}, Nome: {self.getNome()}, Email: {self.getEmail()}"
