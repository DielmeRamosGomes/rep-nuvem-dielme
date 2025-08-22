pessoas_3_link = int(input("Numero de pessoas [1, 1000]: "))
while pessoas_3_link < 0 or pessoas_3_link > 1001:
    pessoas_3_link = int(input("Numero de pessoas [1, 1000]: "))
    
pessoas_2_link = 2 * pessoas_3_link
pessoas_1_link = 2 * pessoas_2_link
print(f"{pessoas_1_link} pessoas clicaram no primeiro link")




