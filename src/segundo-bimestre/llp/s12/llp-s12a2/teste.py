e_dia = True
temperatura = 22  # Temperatura em graus Celsius
if e_dia:
    if temperatura > 25:
        print("Ligando o ar-condicionado.")
    elif temperatura < 20:
        print("Ligando o aquecedor.")
    else:
        print("Temperatura confortável. Não fazendo nada.")
else:
    print("É noite. Controlador de clima em modo de economia de energia.")