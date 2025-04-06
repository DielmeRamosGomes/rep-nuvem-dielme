numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
opcao = input("digite uma operação: ")
resultado = 0

if opcao == "+":
     resultado =  numero1 + numero2
     print(f"Resultado é {resultado}")
elif opcao == "*":
     resultado = numero1 * numero2
     print(f"Resultado é {resultado}")
else:
    print("Não foi possivel fazer a operação")




