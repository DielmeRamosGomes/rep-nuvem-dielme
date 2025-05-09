import random

numero_do_usuario = int(input("Digite um número entre 1 e 100: "))
numero_aleatorio = random.randint(1, 100)
conta_tentativa = 1
while numero_do_usuario != numero_aleatorio:
    if numero_do_usuario < numero_aleatorio:
        print(f"O número é maior que {numero_do_usuario}!")
    else:
        print(f"O número é menor que {numero_do_usuario}!")
    conta_tentativa += 1
    numero_do_usuario = int(input("Digite um número entre 1 e 100: "))
print(f"Você acertou o número {numero_aleatorio} em {conta_tentativa} tentativas!")



