import random

def criar_matriz(dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    return matriz

def matriz_aleatoria(dim_linha, dim_coluna):
    matriz = criar_matriz(dim_linha, dim_coluna)
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz[linha][coluna] = random.randint(0, 100)
    return matriz

def imprimir_matriz(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    print(f"\nMatriz gerada com Dimensões: {dim_linha} x {dim_coluna}")
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end="  ")
        print()

def menu():
    while True:
        try:
            dim_linha = int(input("Digite o número de linhas da matriz: "))
            dim_coluna = int(input("Digite o número de colunas da matriz: "))
            matriz = matriz_aleatoria(dim_linha, dim_coluna)
            imprimir_matriz(matriz)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
        continuar = input("Deseja gerar outra matriz? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    menu()

