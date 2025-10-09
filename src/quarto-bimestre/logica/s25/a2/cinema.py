# Inicializa a matriz cinema como uma lista de listas (5 linhas x 8 colunas)
cinema = [[0 for _ in range(8)] for _ in range(5)]

def reservar_assento(linha, coluna):
    posicao_l = linha - 1
    posicao_c = coluna - 1
    if 0 <= posicao_l < 5 and 0 <= posicao_c < 8:
        if cinema[posicao_l][posicao_c] == 0:
            cinema[posicao_l][posicao_c] = 1
            print(f"Assento na linha {linha}, coluna {coluna} reservado com sucesso.")
        else:
            print(f"Assento na linha {linha}, coluna {coluna} já está reservado.")
    else:
        print("Posição inválida. Tente novamente.")

def cancelar_assento(linha, coluna):
    posicao_l = linha - 1
    posicao_c = coluna - 1
    if 0 <= posicao_l < 5 and 0 <= posicao_c < 8:
        if cinema[posicao_l][posicao_c] == 1:
            cinema[posicao_l][posicao_c] = 0
            print(f"Assento na linha {linha}, coluna {coluna} teve a reserva cancelada com sucesso.")
        else:
            print(f"Assento na linha {linha}, coluna {coluna} não está reservado.")
    else:
        print("Posição inválida. Tente novamente.")

def exibir_mapa():
    print("Mapa de assentos do cinema:")
    print("  0 1 2 3 4 5 6 7")
    for i in range(5):
        linha = str(i + 1) + " "
        for j in range(8):
            if cinema[i][j] == 0:
                linha += "O "
            else:
                linha += "X "
        print(linha)

def execucao(opcao, linha, coluna):
    if opcao == 1:
        reservar_assento(linha, coluna)
    elif opcao == 2:
        cancelar_assento(linha, coluna)
    else:
        print("Opção inválida. Tente novamente.")

def mostrar_opcao():
    print("Escolha uma opção:")
    print("1 - Reservar assento")
    print("2 - Cancelar reserva")
    opcao = int(input("Digite a opção desejada (1 ou 2): "))
    while opcao not in [1, 2]:
        print("Opção inválida. Tente novamente.")
        opcao = int(input("Digite a opção desejada (1 ou 2): "))
    return opcao
  
def main():
    while True:
        print("Bem-vindo ao sistema de reservas do cinema!")
        exibir_mapa()
        opcao = mostrar_opcao()
        linha = int(input("Digite a fileira do assento (1-5): "))
        while linha < 1 or linha > 5:
            print("Fileira inválida. Tente novamente.")
            linha = int(input("Digite a fileira do assento (1-5): "))
        coluna = int(input("Digite o assento (1-8): "))
        while coluna < 1 or coluna > 8:
            print("Assento inválido. Tente novamente.")
            coluna = int(input("Digite o assento (1-8): "))
        execucao(opcao, linha, coluna)
        exibir_mapa()
        continua = input("Deseja continuar executando? [s/n]: ").lower()
        if continua == 'n':
            print("Encerrando o sistema de reservas. Até logo!")
            break

if __name__ == "__main__":
    main()

