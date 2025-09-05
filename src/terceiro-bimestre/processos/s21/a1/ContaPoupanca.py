from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * (taxa_juros / 100)
        self.saldo += juros
        self.registrar_transacao("Juros Mensais", juros)






