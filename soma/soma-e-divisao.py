n_vezes = float(input("Digite o numero de vezes: "));
numero_a = 0
numero_b = 0
contador = 1
contador_b = n_vezes
resultado = 0
while (contador <= n_vezes):
    numero_a = contador
    numero_b = contador_b
    resultado = resultado + numero_a/numero_b
    contador = contador + 1
    contador_b = contador_b - 1
print(f"Resultato = {resultado}")


