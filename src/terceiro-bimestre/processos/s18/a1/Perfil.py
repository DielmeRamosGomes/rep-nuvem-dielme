class Perfil():
    def __init__(self, id, nome, nome_da_conta, email, senha):
        self.__id = id
        self.__nome = nome
        self.__nome_da_conta = nome_da_conta
        self.__email = email
        self.__senha = senha
        self.__curtidas = 0

    def get_nome(self):
        return self.__nome
    
    def get_nome_da_conta(self):
        return self.__nome_da_conta

    def get_curtidas(self):
        return self.__curtidas
    
    def set_curtidas(self): 
        self.__curtidas += 1

perfil_douglas = Perfil(1, "Douglas Silva", "@douglinha", "douglas@exemplo.com", "senha123")

for i in range(1, 11):
    perfil_douglas.set_curtidas()

print(f"\nO perfil {perfil_douglas.get_nome_da_conta()} tem um número de curtidas igual a {perfil_douglas.get_curtidas()}")

