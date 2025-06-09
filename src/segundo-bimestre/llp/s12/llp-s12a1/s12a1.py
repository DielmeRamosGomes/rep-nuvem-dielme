numeros = [1, 2, 3, 4, 'cinco']
# Filtrando apenas os números da lista
numeros_filtrados = [num for num in numeros if isinstance(num, (int, float))]
# Calculando a soma e a quantidade de números
soma = sum(numeros_filtrados)
quantidade = len(numeros_filtrados)
# Calculando a média
if quantidade > 0:
    media = soma / quantidade
else:
    media = None
print(f"A média dos números é: {media}")




