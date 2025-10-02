matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

matriz2 = [['X' for _ in range(3)] for _ in range(3)]

def exibir_matriz(matriz):
    print("  1 2 3")
    for linha in range(3):
        print(linha + 1, end=' ')        
        for coluna in range(3):
            print(matriz[linha][coluna], end=' ')
        print()

exibir_matriz(matriz2)
