while input("Deseja continuar? (s/n): ").lower() != 'n':
    numero = int(input("Digite um número: "))
    print(f"Tabuadas do numero: {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")




