from ContaBancaria import ContaBancaria

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta):
        super().__init__(numero_conta)
        self.investimentos = []
    
    def realizar_investimento(self, produto, valor):
        # Lógica para realizar o investimento
        self.investimentos.append({"Produto": produto, "Valor": valor})
        self.registrar_transacao("Investimento", valor)