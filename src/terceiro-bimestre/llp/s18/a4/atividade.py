num_competidores_C = int(input("Digite o número de competidores [1, 1000]: "))
while num_competidores_C < 1 or num_competidores_C > 1000:
    num_competidores_C = int(input("Digite o número de competidores [1, 1000]: "))

qtd_folha_P = int(input("Digite a quantidade de folhas compradas [1, 1000]: "))
while qtd_folha_P < 1 or qtd_folha_P > 1000:
    qtd_folha_P = int(input("Digite a quantidade de folhas compradas [1, 1000]: "))

qtd_folha_recebida_F = int(input("Digite a quantidade de folhas recebidas por competidor [1, 1000]: "))
while qtd_folha_recebida_F < 1 or qtd_folha_recebida_F > 1000:
    qtd_folha_recebida_F = int(input("Digite a quantidade de folhas recebidas por competidor [1, 1000]: "))
    
total_folha_necessaria = num_competidores_C * qtd_folha_recebida_F
if total_folha_necessaria <= qtd_folha_P:
    print("S")
else:
    print("N") 