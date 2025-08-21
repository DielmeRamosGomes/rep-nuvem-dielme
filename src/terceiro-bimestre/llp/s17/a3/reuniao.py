numero_pessoas = int(input("Digite o numero de pessoas na reunião: "))
tipo_reuniao = input("Digite o tipo da reunião [normal, executiva]").lower()

if numero_pessoas >= 1 and numero_pessoas <= 5:
    print("Reunião na sala pequena")
elif numero_pessoas > 5 and numero_pessoas <= 15:
    print("Reunião na sala média")
elif numero_pessoas > 15 or tipo_reuniao == "executiva":
    print("Reunião na sala grande")
else:
    print("Reunião cancelada")


