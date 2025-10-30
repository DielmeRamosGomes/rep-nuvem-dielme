N = []
V = int(input("Digite um valor inteiro: "))
while V > 50:
    V = int(input("Valor inválido! Digite um valor inteiro menor ou igual a 50: "))
N.append(V)
for i in range(10):
    N.append(N[i] * 2)

print(f"Lista N: {N}")

