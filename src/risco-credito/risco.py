score = -1
divida = True

if score > 700 and divida == False:
    print("Baixo Risco")
elif (score >= 500 and score <=700 and divida == True) or (score > 700 and divida == True):
    print("Médio Risco")
elif (score > 0 and score < 500 and divida == True) or (score >= 500 and score <=700 and divida == True):
    print("Alto Risco")
else:
    print("Não foi possivel definir o crédito")





