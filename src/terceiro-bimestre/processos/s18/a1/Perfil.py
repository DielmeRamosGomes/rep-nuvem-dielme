class Perfil():
    def __init__(self, nome, nome_da_conta):
        self.__nome = nome
        self.__nome_da_conta = nome_da_conta
        self.__curtidas = 0

    def get_nome(self):
        return self.__nome
    
    def get_nome_da_conta(self):
        return self.__nome_da_conta

    def get_curtidas(self):
        return self.__curtidas
    
    def set_curtidas(self):
        self.__curtidas += 1

perfil_douglas = Perfil("Douglas Silva", "@douglinha")
perfil_douglas.set_curtidas()
perfil_douglas.set_curtidas()
perfil_douglas.set_curtidas()
print(f"\nO perfil {perfil_douglas.get_nome_da_conta()} tem um número de curtidas igual a {perfil_douglas.get_curtidas()}")

