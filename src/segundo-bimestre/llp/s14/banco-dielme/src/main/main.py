import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.models.Usuario import Usuario
from src.models.Conta import Conta
from src.models.Banco import Banco

def main():
    usuario = Usuario("Dielme", "dielme@exemplo.com", "1234")
    usuario2 = Usuario("Carlos", "carlos@exemplo.com", "5678")
    
    conta = Conta("0097-3", "77774-9", usuario, 100.0)
    conta2 = Conta("0097-4", "77774-8", usuario2, 200.0)
    
    banco = Banco()
    banco.adicionar_conta(conta)
    banco.adicionar_conta(conta2)
    
    print(f"Entre com o Email e a Senha para acessar o banco.\n")
    email = input("Email: ")
    senha = input("Senha: ")
    print(banco.listar_conta(email, senha))
    
    
if __name__=="__main__":
     main()


