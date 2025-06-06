def controlar_climatizacao(temperatura, hora):
    """
    Controle do ar-condicionado e aquecedor baseado em temperatura e hora do dia.

    Args:
        temperatura (float): Temperatura atual em graus Celsius.
        hora (int): Hora do dia (0-23).
    """

    # Verificar se é dia ou noite
    dia = 6 <= hora < 18

    # Controlar o ar-condicionado e aquecedor
    if temperatura > 28:
        print("Ligar ar-condicionado")
    elif temperatura < 20:
        print("Ligar aquecedor")
    else:
        print("Nenhum dispositivo a ser ligado")

# Exemplo de uso
temperatura_atual = 22
hora_atual = 12

controlar_climatizacao(temperatura_atual, hora_atual)

# Outro exemplo
temperatura_atual = 29
hora_atual = 19

controlar_climatizacao(temperatura_atual, hora_atual)

# Outro exemplo
temperatura_atual = 18
hora_atual = 23

controlar_climatizacao(temperatura_atual, hora_atual)