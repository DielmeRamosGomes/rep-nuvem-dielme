from src.models.Conta import Conta
from src.models.Usuario import Usuario

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

    def listar_conta(self, email, senha):
        for conta in self.lista_contas:
            if conta.getUsuario().getEmail() == email and conta.getUsuario().getSenha() == senha:
                return f"\n Bem-vindo ao Banco, {conta.getUsuario().getNome()}!\n" + conta.getUsuario().mostrar_usuario() + f"\n Agência: {conta.getAgencia()}, Número: {conta.getNumero()}, Saldo: {conta.getSaldo()}\n"
            else:
                return "\n Conta não encontrada ou credenciais inválidas.\n"