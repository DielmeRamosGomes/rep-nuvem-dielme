class Pessoa:
    def __init__(self, nome, idade, ativo):
        self.__nome = nome
        self.__idade = idade
        self.__ativo = ativo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        self.__idade = idade
        
    def getAtivo(self):
        return self.__ativo
    
    def setAtivo(self, ativo):
        self.__ativo = ativo
        
    def mostrar_dados(self):
        print(f"\n Nome: {self.__nome}, Idade: {self.__idade}, Ativo: {self.__ativo} \n")

pessoa = Pessoa('Carlos', 31, True)
pessoa2 = Pessoa('João', 25, False)
pessoa.mostrar_dados()
pessoa2.mostrar_dados()

