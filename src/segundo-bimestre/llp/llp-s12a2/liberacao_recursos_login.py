lista_usuarios = [
    {"nome": "Ana", "senha": 1234, "pais": "Brasil"},
    {"nome": "Bruno", "senha": 4567, "pais": "Polonia"},
    {"nome": "Carlos", "senha": 7890, "pais": "Alemanha"},
    {"nome": "Diana", "senha": 7898, "pais": "Franca"},
    {"nome": "Eduardo", "senha": 1234, "pais": "Italia"}
]

lista_recursos = [
    {"pais": "Brasil", "recurso": "Recurso A"},
    {"pais": "Polonia", "recurso": "Recurso B"},
    {"pais": "Alemanha", "recurso": "Recurso C"},
    {"pais": "Franca", "recurso": "Recurso D"},
    {"pais": "Italia", "recurso": "Recurso E"}
]

nome_usuario = input("Digite seu nome de usuário: ").lower()
senha_usuario = int(input("Digite sua senha: "))
usuario_nao_encontrado = True
for usuario in lista_usuarios:
    if usuario["nome"].lower() == nome_usuario and usuario["senha"] == senha_usuario:
        usuario_nao_encontrado = False
        print(f"Bem-vindo, {usuario['nome']}! Você está logado.")
        for recurso in lista_recursos:
            if usuario["pais"].lower() == recurso["pais"].lower():
                print(f"O usuario {usuario['nome']} é do país {usuario['pais']}.")
                print(f"Recursos disponíveis para você: {recurso["recurso"]}")
                break
        break
if usuario_nao_encontrado:
    print("Usuário ou senha incorretos. Tente novamente.")

