import random

def lista_aleatoria(num):
    lista = []
    for i in range(num):
        lista.append(random.randint(1, 100))
    print(f"Lista desordenada: {lista}")
    return lista

def ordenar(lista):
    lista.sort()
    print(f"Lista ordenada = {lista}")

def executar():
    while True:
        num = int(input("Digite a quatidade de numeros da lista: "))
        lista = lista_aleatoria(num)
        ordenar(lista)
        continua = input("Deseja continuar?[s, n]: ").lower()
        if continua == 'n':
            break         

executar()

