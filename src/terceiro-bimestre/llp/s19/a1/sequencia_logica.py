numero_N = int(input("Digite um número N [2, 999]: "))
while numero_N <= 1 or numero_N >= 1000:
    numero_N = int(input("Número inválido! Digite um número N [2, 999]: "))
for i in range(1, numero_N + 1):
    print(i, i**2, i**3)
    print(i, (i**2)+1, (i**3)+1)




