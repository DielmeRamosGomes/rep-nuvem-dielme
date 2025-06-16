import random
matriz_aleatoria = [[random.randint(0, 100) for _ in range(3)] for _ in range(3)]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def exibir_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(f"matriz_aleatoria[{matriz.index(linha)}][{linha.index(coluna)}] = {matriz[matriz.index(linha)][linha.index(coluna)]}", end=" ")
            print('\n')

exibir_matriz(matriz_aleatoria)

# 1 2 3
# 4 5 6
# 7 8 9