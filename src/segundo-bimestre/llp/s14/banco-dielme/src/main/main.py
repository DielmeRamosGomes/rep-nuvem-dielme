import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.models.Usuario import Usuario
from src.models.Conta import Conta
from src.models.Banco import Banco

def main():
    usuario = Usuario("Dielme", "dielme@exemplo.com", "1234")
    conta = Conta("0097-3", "77774-9", usuario, 100.0)
    banco = Banco()
    banco.adicionar_conta(conta)
    
    print(f"Entre com o Email e a Senha para acessar o banco.\n")
    email = input("Email: ")
    senha = input("Senha: ")
    if email == conta.getUsuario().getEmail() and senha == conta.getUsuario().getSenha():
        print(f"Bem-vindo ao Banco, {usuario.getNome()}!")

if __name__=="__main__":
     main()


