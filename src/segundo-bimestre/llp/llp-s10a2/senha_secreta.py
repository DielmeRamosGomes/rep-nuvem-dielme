import random
import string

print("Bem-vindo ao jogo da senha secreta!")
print("Você tem 5 tentativas para acertar a senha secreta.")
while input("Deseja executar novamente?[sim, nao]: ").lower() != "nao":
    numero_tentativas = 1
    print(f"Tentativa numero: {numero_tentativas}")
    senha = input("Digite uma senha secreta com 8 caracteres: ")
    caracteres = string.ascii_letters + string.digits
    string_aleatoria = ''.join(random.choice(caracteres) for i in range(1, 9)) 
    while senha != string_aleatoria:
        numero_tentativas = numero_tentativas + 1
        if numero_tentativas > 5:
            break
        print(f"Tentativa: {numero_tentativas}")
        senha = input("Digite a senha secreta: ")
    if numero_tentativas > 5:
        print("Você perdeu!")
        print(f"A senha gerada foi: {string_aleatoria}")
    else:
        print("Você ganhou!")
        print(f"A senha secreta era: {senha}")
        print(f"A senha gerada foi: {string_aleatoria}")





