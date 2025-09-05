from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial=0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial

    def emitir_cheque(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor:
            self.saldo -= valor
            self.registrar_transacao("Emissão de Cheque", valor)
        else:
            print("Limite de cheque especial excedido.")




