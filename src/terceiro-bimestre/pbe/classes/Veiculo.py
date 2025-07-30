class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
        
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano
    
    def ligar(self):
        print(f"{self.get_modelo()} está ligado.")
        
    def desligar(self):
        print(f"{self.get_modelo()} está desligado.")
      
    def exibir_detalhes(self):
        print(f"Marca: {self.get_marca()}, Modelo: {self.get_modelo()}, Ano: {self.get_ano()}\n")

carro = Veiculo("Toyota", "Corolla", 2020)
carro2 = Veiculo("Honda", "Civic", 2021)
carro.set_ano(2022)

carro.exibir_detalhes()
carro2.exibir_detalhes()




