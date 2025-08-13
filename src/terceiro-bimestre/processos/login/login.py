nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

nome1 = "Miguel"
email1 = "miguel@exemplo.com"
senha1 = "123456"

if email == email1 and senha == senha1:
    print("Login realizado com sucesso!")
    print(f"Bem-vindo, {nome1}!")
else:
    print("Dados incorretos. Tente novamente.")
