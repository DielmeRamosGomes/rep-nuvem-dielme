def aplicar_desconto(tipo_cliente, valor):
    descontos = {
        "estudante": lambda v: v * 0.9,
        "membro": lambda v: v * 0.85,
        "vip": lambda v: v * 0.8
    }
    return descontos.get(tipo_cliente, lambda v: v)(valor)

valor_descontado = aplicar_desconto("membro", 100)
print(valor_descontado)


