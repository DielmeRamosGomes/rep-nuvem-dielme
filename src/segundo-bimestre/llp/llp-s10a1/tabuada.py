while input("Deseja continuar? (sim/nao): ").lower() != 'nao':
    numero = int(input("Digite um número: "))
    print(f"Tabuada do numero: {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")




