import random

qtd_intervalo_tempo_N = int(input("Digite a quantidade de intervalos de tempo [1, 1000]: "))
while qtd_intervalo_tempo_N < 0 or qtd_intervalo_tempo_N > 1001:
    qtd_intervalo_tempo_N = int(input("Digite a quantidade de intervalos de tempo [1, 1000]: "))

distancia_percorrida_KM = 0
for i in range(1, qtd_intervalo_tempo_N+1):
    tempo_T = random.randint(1, 100)
    velocidade_media_V = random.randint(0, 120)
    print(f"Intervalo: {i} | Tempo: {tempo_T} * velocidade: {velocidade_media_V} = {tempo_T * velocidade_media_V}")
    distancia_percorrida_KM += tempo_T * velocidade_media_V
print(f"Distância total percorrida em Km é igual a {distancia_percorrida_KM}\n")

