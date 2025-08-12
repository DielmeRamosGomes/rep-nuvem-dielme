class Candidato:
    def __init__(self, nome, nome_vice, partido, numero, cargo):
        self.__nome = nome
        self.__nome_vice = nome_vice
        self.__partido = partido
        self.__numero = numero
        self.__cargo = cargo
        
    def get_nome(self):
        return self.__nome
    
    def get_nome_vice(self):
        return self.__nome_vice
    
    def get_partido(self):
        return self.__partido
    
    def get_numero(self):
        return self.__numero
    
    def get_cargo(self):
        return self.__cargo
    
    def mostrar_detalhes(self):
        print(f"\nNome: {self.get_nome()}")
        print(f"Vice: {self.get_nome_vice()}")
        print(f"Partido: {self.get_partido()}")
        print(f"Número: {self.get_numero()}")
        print(f"Cargo: {self.get_cargo()}\n")
    
candidato = Candidato("João Silva", "Maria Souza", "Partido A", 34, "Presidente")

candidato.mostrar_detalhes()

