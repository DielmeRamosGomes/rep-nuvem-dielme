matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

matriz2 = [['X' for _ in range(3)] for _ in range(3)]

def exibir_matriz(matriz):
    print("  0 1 2")
    for linha in range(3):
        print(linha, end=' ')        
        for coluna in range(3):
            print(matriz[linha][coluna], end=' ')
        print()

exibir_matriz(matriz2)
