def aplicar_desconto(tipo_cliente, valor):
    if tipo_cliente == "estudante":
        return valor * 0.9
    elif tipo_cliente == "membro":
        return valor * 0.85
    elif tipo_cliente == "vip":
        return valor * 0.8
    else:
        return valor
valor_descontado = aplicar_desconto("membro", 100)
print(valor_descontado)


