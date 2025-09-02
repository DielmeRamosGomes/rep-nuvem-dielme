
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    n = int(input("Número inválido. Digite um número inteiro positivo: "))
print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")  

