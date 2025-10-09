matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

matriz2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
    ]

def somar_matrizes(matriz1, matriz2):
    resultado = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado

def exibir_matriz(matriz):
    print("  0  1  2")
    for linha in range(3):
        print(linha, end=' ')        
        for coluna in range(3):
            print(matriz[linha][coluna], end=' ')
        print()

resultado = somar_matrizes(matriz1, matriz2)
exibir_matriz(resultado)



