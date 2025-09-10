lista = []
while True:
    nome = input("Digite um nome: ")
    lista.append(nome)
    print(f"Lista = {lista}")
    continua = input("Deseja continuar?[sim, nao]: ").lower()
    print()
    if continua == 'nao':
        break




