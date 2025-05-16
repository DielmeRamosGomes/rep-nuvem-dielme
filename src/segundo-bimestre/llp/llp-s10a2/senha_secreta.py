import random
import string

while input("Deseja executar novamente?[sim, nao]:  ").lower() != "nao":
    senha = input("Digite a senha secreta: ")
    caracteres = string.ascii_letters + string.digits
    string_aleatoria = ''.join(random.choice(caracteres) for i in range(senha)) 
    while senha != string_aleatoria:






