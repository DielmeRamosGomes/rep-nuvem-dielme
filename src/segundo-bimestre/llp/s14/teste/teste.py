def calcular_tempo_preparo(pedido, acompanhamento=False, horario=None):
    tempos = {
        'hamburguer': 10,
        'pizza': 20,
        'salada': 5
    }
    tempo_base = tempos.get(pedido.lower(), 15)
    if acompanhamento:
        tempo_base += 5
        
    if horario in range(12, 15) or horario in range(19, 22):
        tempo_base += 10

    return tempo_base

tempo = calcular_tempo_preparo('pastel', False, 13)  # Exemplo de uso
print(f'Tempo de preparo: {tempo} minutos')  # Exibe o tempo de preparo calculado

