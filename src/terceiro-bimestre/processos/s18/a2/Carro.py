class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_cor(self):
        return self.__cor

    def get_preco(self):
        return self.__preco

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_ano(self, ano):
        self.__ano = ano

    def set_cor(self, cor):
        self.__cor = cor

    def set_preco(self, preco):
        self.__preco = preco

    def get_detalhes(self):
        print(f"\nMarca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Ano: {self.get_ano()}")
        print(f"Cor: {self.get_cor()}")
        print(f"Preço: {self.get_preco()}\n")

#palio = Carro("Fiat", "Palio", 2020, "Prata", 30000)
#palio.get_detalhes()

