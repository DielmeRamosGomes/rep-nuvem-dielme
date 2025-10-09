matriz = [
    [22, 25, 28, 32],
    [20, 23, 26, 30],
    [18, 22, 25, 29]
]

def matriz_transposta(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    matriz_transposta = [[0 for _ in range(linha)] for _ in range(coluna)]
    for i in range(linha):
        for j in range(coluna):
            matriz_transposta[j][i] = matriz[i][j]
    return matriz_transposta

def exibir_matriz(matriz, linha, coluna):
    for i in range(linha):        
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()

def menu():
    print("Matriz original:")
    exibir_matriz(matriz, 3, 4)
    print("\nMatriz transposta:")
    exibir_matriz(matriz_transposta(matriz), 4, 3)
    
if __name__ == "__main__":
    menu()    
