from ContaBancaria import ContaBancaria
#from ContaCorrente import ContaCorrente

if __name__=="__main__":
    conta1 = ContaBancaria("0002", 200)
    conta1.consultar_saldo()

    #conta2 = ContaCorrente("0001")
    #print("Saldo antes de depositar dinheiro")
    #conta2.consultar_saldo()
    #conta2.depositar(100)
    #print("Saldo depois de depositar R$ 100.00")
    #conta2.consultar_saldo()

    
