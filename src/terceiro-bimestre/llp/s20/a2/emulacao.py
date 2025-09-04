import random
numeros = []
for i in range(1, 11):
    numeros.append(random.randint(1, 100))

numeros.append(-1)
for numero in numeros:
    if numero < 0:
        print(f"Encotrado número negativo: {numero} parando processo")
        break
    if numero % 2 == 0:
        print(f"Número par encontrado: {numero}. Pulando para a próxima interação")
        continue
    print(f"Processando o número: {numero}")
        
        
        