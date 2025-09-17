def fibonacci(num):
    if num == 0:
        sequencia = [0]
        print(f"Fib({num}) = {sequencia}")
    elif num == 1:
        sequencia = [1]
        print(f"Fib({num}) = {sequencia}")
    elif num >= 2:
        sequencia = [0 , 1]
        for i in range(2, num+1):
            proximo = sequencia[-1] + sequencia[-2]
            sequencia.append(proximo)
        print(f"Sequência de Fibonacci = {sequencia}")

fibonacci(10)





