from src.models.Conta import Conta

class Banco:
    def __init__(self):
        self.lista_contas = [Conta]

    def adicionar_conta(self, conta: Conta):
        self.lista_contas.append(conta)

    def remover_conta(self, conta: Conta):
        if conta in self.lista_contas:
            self.lista_contas.remove(conta)
        else:
            print("Conta não encontrada.")

