class Candidato:
    def __init__(self, nome_candidato, nome_vice_candidato, nome_partido, numero_partido):
        self.__nome_candidato = nome_candidato
        self.__nome_vice_candidato = nome_vice_candidato
        self.__nome_partido = nome_partido
        self.__numero_partido = numero_partido

    def getNomeCandidato(self):
        return self.__nome_candidato

    def setNomeCandidato(self, nome_candidato):
        self.__nome_candidato = nome_candidato

    def getNomeViceCandidato(self):
        return self.__nome_vice_candidato
    
    def setNomeViceCandidato(self, nome_vice_candidato):
        self.__nome_vice_candidato = nome_vice_candidato

    def getNomePartido(self):
        return self.__nome_partido
    
    def setNomePartido(self, nome_partido):
        self.__nome_partido = nome_partido

    def getNumeroPartido(self):
        return self.__numero_partido
    
    def setNumeroPartido(self, numero_partido):
        self.__numero_partido = numero_partido

    def monstrarDados(self):
        print(f"Nome do Candidato: {self.__nome_candidato}")
        print(f"Nome do Vice Candidato: {self.__nome_vice_candidato}")
        print(f"Nome do Partido: {self.__nome_partido}")
        print(f"Número do Partido: {self.__numero_partido} \n")

candidato = Candidato("Guilherme", "Rafael", "Partido Verde", 12345)
print("Dados do Candidato: \n")
candidato.monstrarDados()

