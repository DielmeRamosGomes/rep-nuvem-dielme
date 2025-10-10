import random

def matriz_aleatoria(matriz, dim_linha, dim_coluna):
    for i in range(dim_linha):
        for j in range(dim_coluna):
            matriz[i][j] = random.randint(0, 10)
    return matriz

def soma_matrizes(matriz, matriz2, dim_linha, dim_coluna):
    matriz_resultado = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    for i in range(dim_linha):
        for j in range(dim_coluna):
            matriz_resultado[i][j] = matriz[i][j] + matriz2[i][j]
    return matriz_resultado

def exibir_matriz(matriz, dim_linha, dim_coluna):
    for i in range(dim_linha):
        for j in range(dim_coluna):
            print(matriz[i][j], end=' ')
        print()

def menu():
    while True:
        try:
            dim_linha = int(input("\nDigite a quantidade de linhas da matriz 1: "))
            dim_coluna = int(input("\nDigite a quantidade de colunas da matriz 1: "))
            matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
            dim_linha2 = int(input("\nDigite a quantidade de linhas da matriz 2: "))
            dim_coluna2 = int(input("\nDigite a quantidade de colunas da matriz 2: "))
            while dim_linha != dim_linha2 or dim_coluna != dim_coluna2:
                print("\nAs matrizes devem ter as mesmas dimensões para serem somadas.")
                dim_linha2 = int(input("\nDigite a quantidade de linhas da matriz 2: "))
                dim_coluna2 = int(input("\nDigite a quantidade de colunas da matriz 2: "))
            matriz2 = [[0 for _ in range(dim_coluna2)] for _ in range(dim_linha2)]
            matriz = matriz_aleatoria(matriz, dim_linha, dim_coluna)
            matriz2 = matriz_aleatoria(matriz2, dim_linha2, dim_coluna2)
            matriz_resultado = soma_matrizes(matriz, matriz2, dim_linha, dim_coluna)
            print("\nMatriz 1:")
            exibir_matriz(matriz, dim_linha, dim_coluna)
            print("\nMatriz 2:")
            exibir_matriz(matriz2, dim_linha2, dim_coluna2)
            print("\nMatriz Resultante (Soma):")
            exibir_matriz(matriz_resultado, dim_linha, dim_coluna)
        except ValueError:
            print("\nEntrada inválida. Por favor, insira números inteiros.")
            return
        continua = input("\nDeseja continuar? (s/n): ").strip().lower()
        if continua == 'n':
            break 

if __name__ == "__main__":
    menu()



