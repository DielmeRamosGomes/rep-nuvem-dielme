from Carro import Carro

class Estoque:
    def __init__(self):
        self.__carros = [Carro]

    def adicionar_carro(self, carro):
        self.__carros.append(carro)
        print(f"\nCarro da marca {carro.get_marca()} e modelo {carro.get_modelo()} foi adicionado ao estoque.\n")

    def remover_carro(self, carro):
        self.__carros.remove(carro)
        print(f"\nCarro da marca {carro.get_marca()} e modelo {carro.get_modelo()} foi removido do estoque.\n")

    def listar_carros(self):
        for carro in self.__carros:
            print(carro.get_detalhes())

palio = Carro("Fiat", "Palio", 2020, "Prata", 30000)
estoque = Estoque()
estoque.adicionar_carro(palio)

