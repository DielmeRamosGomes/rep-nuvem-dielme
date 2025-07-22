while True:
    try:
        num = int(input("Digite um número inteiro positivo (0 para sair): "))
        if num == 0:
            print("Saindo do programa.")
            break
        elif num < 0:
            print("Por favor, digite um número positivo.")
        else:
            print(f"Você digitou o número: {num}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")




