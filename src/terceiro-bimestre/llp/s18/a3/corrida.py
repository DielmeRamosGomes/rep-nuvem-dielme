correr_C = int(input("Quantos metros o corredor correu?[1, 10^8]: "))
while correr_C < 1 or correr_C > 10**8:
    correr_C = int(input("Quantos metros o corredor correu?[1, 10^8]: "))

comprimento_N = int(input("Qual o comprimento da pista?[1, 100]: "))
while comprimento_N < 1 or comprimento_N > 101:
    comprimento_N = int(input("Qual o comprimento da pista?[1, 100]: "))

ponto_termino = correr_C % comprimento_N
print(f"O ponto de término do corredor é: {ponto_termino}")



