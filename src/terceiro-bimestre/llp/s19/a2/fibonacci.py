def fibonacci(n):
    primeiro = 0
    segundo = 1
    if n_esimo_termo_N == 0:
        print(f"Fib({n_esimo_termo_N}) = {primeiro}")
    elif n_esimo_termo_N == 1:
        print(f"Fib({n_esimo_termo_N}) = {segundo}")
    elif n_esimo_termo_N >= 2:
        for j in range(2, n_esimo_termo_N + 1):
            proximo = primeiro + segundo
            primeiro = segundo
            segundo = proximo
            print(f"Fib({n_esimo_termo_N}) = {proximo}")

num_caso_de_teste_T = int(input("Digite o número de casos de teste: "))
for i in range(1, num_caso_de_teste_T+1):
    n_esimo_termo_N = int(input("Digite o valor do N-ésimo termo [0, 60]: "))
    try:
        if 0 <= n_esimo_termo_N <= 60:  
            fibonacci(n_esimo_termo_N)
        else:
            print("Valor inválido! Digite um número entre 0 e 60.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")      
    


