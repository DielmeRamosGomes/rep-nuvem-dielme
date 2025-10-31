import random

def criar_matriz(dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    return matriz

def matriz_aleatoria(matriz, dim_linha, dim_coluna):
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz[linha][coluna] = random.randint(1, 100)
    return matriz
    
def soma_linha(matriz, dim_linha, dim_coluna, pos_linha):
    soma = 0
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            if linha == pos_linha:
                soma += matriz[linha][coluna]
    return soma

def opcoes():
    print("Escolha uma opção: ")
    print("1 - Calcular a soma dos elementos de uma linha específica")
    print("2 - Calcular a média dos elementos de uma linha específica")
    escolha = int(input("Digite 1 ou 2: "))
    return escolha

def execucao(matriz, dim_linha, dim_coluna, pos_linha, escolha):
    if escolha == 1:
        resultado = soma_linha(matriz, dim_linha, dim_coluna, pos_linha)
        print(f"A soma dos elementos da linha é  = {resultado}")
    elif escolha == 2:
        soma = soma_linha(matriz, dim_linha, dim_coluna, pos_linha)
        media = soma / dim_coluna
        print(f"A média dos elementos da linha é  = {media}")
        
def main():
    while True:
        dim_linha = int(input("Digite a dimensão de linhas da matriz: "))
        dim_coluna = int(input("Digite a dimensão de colunas da matriz: "))
        matriz = criar_matriz(dim_linha, dim_coluna)
        matriz = matriz_aleatoria(matriz, dim_linha, dim_coluna)
        print("Matriz gerada:")
        for linha in matriz:
            print(linha)
        pos_linha = int(input(f"Digite a posição da linha (0 a {dim_linha - 1}): "))
        escolha = opcoes()
        execucao(matriz, dim_linha, dim_coluna, pos_linha, escolha)
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break   