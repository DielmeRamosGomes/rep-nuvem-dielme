import random

def cria_matriz(dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            numero = random.randint(0, 9)
            matriz[linha][coluna] = numero
    return matriz

def exibir_matriz(matriz, dim_linha, dim_coluna):
    print(dimensao_coluna(dim_coluna))
    for linha in range(dim_linha):
        print(linha, end=' ')        
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end=' ')
        print()

def dimensao_coluna(dim_coluna):
    numeros = '  '
    for coluna in range(dim_coluna):
        numeros += str(coluna) + ' '
    return numeros

def execucao():
    while True:
        dim_linha = int(input("Digite a dimensão de linhas da matriz: "))
        dim_coluna = int(input("Digite a dimensão de colunas da matriz: "))
        matriz = cria_matriz(dim_linha, dim_coluna)
        exibir_matriz(matriz, dim_linha, dim_coluna)
        continua = input("Deseja criar outra matriz? (s/n) ").lower()
        if continua == 'n':
            break
        
if __name__ == "__main__":
    execucao()
        