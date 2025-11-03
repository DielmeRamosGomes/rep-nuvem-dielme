import random

matriz = []

def cria_matriz(matriz, dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    return matriz

def matriz_aleatoria(matriz, dim_linha, dim_coluna):
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz[linha][coluna] = random.randint(0, 9)
        return matriz
    
def imprimir_matriz(matriz, dim_linha, dim_coluna):
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=" ")
        print()

def soma_matriz(matriz1, matriz2):
    dim_linha = len(matriz1)
    dim_coluna = len(matriz1[0])
    resultado = cria_matriz(matriz1, dim_linha, dim_coluna)
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            resultado[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
    return resultado