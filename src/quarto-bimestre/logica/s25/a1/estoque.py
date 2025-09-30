estoque = [20, 15, 10, 30, 5]

def atualizar_estoque(elemento, quantidade):
    posicao = elemento - 1
    if 0 <= posicao < len(estoque):
        estoque[posicao] -= quantidade
    else:
        print("Elemento inválido!")

def adicionar_estoque(elemento, quantidade):
    posicao = elemento - 1
    if 0 <= posicao < len(estoque):
        estoque[posicao] += quantidade
    else:
        print("Elemento inválido!")

def exibir_estoque():
    print(f"Estoque atual: {estoque}")

print("Estoque inicial:")
exibir_estoque()
atualizar_estoque(1, 3)
atualizar_estoque(4, 2)
adicionar_estoque(5, 10)
print("Estoque após atualizações:")
exibir_estoque()