class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAno(self):
        return self.__ano
    
    def setMarca(self, marca):
        self.__marca = marca
        
    def setModelo(self, modelo):
        self.__modelo = modelo
        
    def setAno(self, ano):
        self.__ano = ano
    
    def exibirDetalhes(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Ano: {self.__ano}")
    
    def ligar_motor(self):
        print(f"Motor do {self.__modelo} ligado")
    
    def desligar_motor(self):
        print(f"Motor do {self.__modelo} desligado")
    
carro = Carro("Toyota", "Corolla", 2020)
carro1 = Carro("Honda", "Civic", 2021)   
carro.exibirDetalhes()
carro.ligar_motor()
carro1.exibirDetalhes()
carro1.desligar_motor()
