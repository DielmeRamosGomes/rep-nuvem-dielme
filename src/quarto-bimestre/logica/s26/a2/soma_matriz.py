import random

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

def escolhas():
    print("1 - Somar duas matrizes")
    print("2 - Multiplicar duas matrizes")
    print("3 - Subtrair duas matrizes")
    print("4 - Sair do programa")

def execucao(opcao):
    matriz = []
    if opcao == 1:
        try:
            print("\nSoma de duas matrizes selecionada.")
            dim_linha = int(input("\nDigite a quantidade de linhas das matrizes: "))
            dim_coluna = int(input("\nDigite a quantidade de colunas da matrizes: "))
            matriz1 = cria_matriz(matriz, dim_linha, dim_coluna)
            matriz2 = cria_matriz(matriz, dim_linha, dim_coluna)
            matriz1 = matriz_aleatoria(matriz1, dim_linha, dim_coluna)
            matriz2 = matriz_aleatoria(matriz2, dim_linha, dim_coluna)
            matriz = soma_matriz(matriz1, matriz2)
            print("\nMatriz 1:")
            imprimir_matriz(matriz1, dim_linha, dim_coluna)
            print("\nMatriz 2:")
            imprimir_matriz(matriz2, dim_linha, dim_coluna)
            print("\nResultado da soma das matrizes:")
            imprimir_matriz(matriz, dim_linha, dim_coluna)
        except ValueError:
            print("Por favor, insira valores inteiros válidos para as dimensões.")
    else:
        print("Opção inválida ou não implementada.")

def main():
    while True:
        escolhas()
        opcao = int(input("\nEscolha uma opção: "))
        execucao(opcao)
        continua = input("Deseja continuar? (s/n): ").lower()
        if continua == 'n':
            break
    
    