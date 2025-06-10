class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email

lista_usuarios = [Usuario]  

def adicionar_usuario(usuario):
    lista_usuarios.append(usuario)

def remover_usuario(usario):
    if usario in lista_usuarios:
        lista_usuarios.remove(usario)
    else:
        print("Usuário não encontrado na lista.")

def padrao():
    print("Opção inválida")

def exibir():
    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in lista_usuarios:
            print(f"Nome: {usuario.getNome()}, Email: {usuario.getEmail()}")

comandos = {
    "adicionar": adicionar_usuario,
    "remover": remover_usuario
}
usuario1 = Usuario("Carlos", "carlos@exemplo.com", 1234)
comandos.get("adicionar", padrao)(usuario1)
exibir()
