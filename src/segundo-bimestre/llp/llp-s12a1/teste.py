temperatura = int(input("Qual é a temperatura atual? "))
esta_chovendo = input("Está chovendo? (sim/não) ") == 'sim'
if temperatura > 30:
    print("Está quente.")
    if esta_chovendo == 'sim':
        print("E também está chovendo. Você deve ficar dentro de casa.")
elif 20 <= temperatura <= 30:
    print("A temperatura está agradável.")
    if esta_chovendo == 'sim':
        print("Mas está chovendo. Leve um guarda-chuva.")
else:
    print("Está frio.")
    if esta_chovendo == 'sim':
        print("E também está chovendo. Fique quente e seco dentro de casa.")