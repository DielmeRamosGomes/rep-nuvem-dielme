import random

while(input("Deseja continuar executando?[sim, nao]: ").lower() != 'nao'):
    numero_aleatorio = random.randint(1, 100)
    numero = int(input("Digite um número entre 1 e 100: "))
    numero_tentativas = 1
    while numero != numero_aleatorio:
        if numero < numero_aleatorio:
            print("O número aleatório é maior!")
        else:
            print("O número aleatório é menor!")
        numero = int(input("Digite um número entre 1 e 100: "))
        numero_tentativas = numero_tentativas + 1
        if numero_tentativas > 5:
            break
    if numero_tentativas > 5:
        print(f"Você perdeu! e o número aleatório é: {numero_aleatorio}")
    else:
        print(f"Você ganhou! em {numero_tentativas} tentativas e o número aleatório é: {numero_aleatorio}")
