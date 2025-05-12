while input("Deseja continuar? (s/n): ").lower() != "n":
    idade = int(input("Digite a idade: "))
    categoria = ""
    if idade > 0 and idade <= 12:
        categoria = "Criança"
    elif idade > 12 and idade <= 17:
        categoria = "Adolescente"
    elif idade > 17 and idade <= 64:
        categoria = "Adulto"
    elif idade > 64:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida!"
    if categoria == "Idade inválida!":
        print(categoria)
    else:
        print(f"A idade é {idade} e a categoria é: {categoria}")

    