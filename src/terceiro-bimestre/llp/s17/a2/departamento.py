departamento = input("Digite um departamento (DS, M, RH, PD): ").upper()
if departamento == "DS":
    print("Recomendado os Laptops")
elif departamento == "M":
    print("Recomendado os Tablets")
elif departamento == "RH":
    print("Recomendado os computadores desktop")
elif departamento == "PD":
    print("Recomendado equipamentos de ultima geração")
else:
    print("Departamento não encontrado")
