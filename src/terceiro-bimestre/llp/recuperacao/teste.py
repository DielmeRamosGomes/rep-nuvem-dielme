# questão 1
while True:
    try:
        numero_participantes = int(input("Digite o número de participantes da reuniao: "))
        while numero_participantes <= 1 or numero_participantes >= 1000:
            numero_participantes = int(input("Digite o número de participantes da reuniao: "))
        tipo_reuniao = input("Digite o tipo de reunião [normal, executiva, festiva, trabalho]: ").strip().lower()
        if (2 <= numero_participantes <= 20) and tipo_reuniao == "executiva":
            print("A sala escolhida é a pequena")
        else:
            print("Reunião cancelada!")
        if numero_participantes > 1 or numero_participantes < 1000:
            break
    except ValueError:
        print("Digite um número válido!")












