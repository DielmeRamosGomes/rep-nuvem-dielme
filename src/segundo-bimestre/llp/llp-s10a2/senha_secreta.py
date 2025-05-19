import random
import string

while input("Deseja executar novamente?[sim, nao]:  ").lower() != "nao":
    senha = input("Digite a senha secreta: ")
    caracteres = string.ascii_letters + string.digits
    string_aleatoria = ''.join(random.choice(caracteres) for i in range(senha)) 
    numero_tentativas = 1
    while senha != string_aleatoria:
        if numero_tentativas > 5:
            break
        numero_tentativas = numero_tentativas + 1
    if numero_tentativas > 5:
        print("Você perdeu!")
    else:
        print("Você ganhou!")
        print(f"A senha secreta era: {senha}")
        print(f"A senha gerada foi: {string_aleatoria}")





