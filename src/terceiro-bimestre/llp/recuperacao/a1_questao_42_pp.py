valor_total = int(input("Digite o valor total da compra: "))
valor_total_anterior = valor_total
desconto = 0
desconto_fidelidade = 0.05  #5% de desconto clube de fidelidade
fidelidade = input("O cliente pertence ao clube de fidelidade? (sim/nao): ").strip().lower()
if valor_total > 200:
    desconto = 0.15  #15% de desconto
    valor_total = valor_total - (valor_total * desconto)
    if fidelidade == "sim":
        valor_total = valor_total - (valor_total * desconto_fidelidade)
elif valor_total >= 100.01 and valor_total <= 200:
    desconto = 0.10  #10% de desconto
    valor_total = valor_total - (valor_total * desconto)
    if fidelidade == "sim":
        valor_total = valor_total - (valor_total * desconto_fidelidade)
elif valor_total >= 50 and valor_total <= 100:
    desconto = 0.05
    valor_total = valor_total - (valor_total * desconto)
    if fidelidade == "sim":
        valor_total = valor_total - (valor_total * desconto_fidelidade)
else:
    if fidelidade == "sim":
        valor_total = valor_total - (valor_total * desconto_fidelidade)
        
print(f"Valor total da compra antes do desconto: R$ {valor_total_anterior}")
print(f"Desconto aplicado: {int(desconto * 100)}%")
if fidelidade == "sim":
    print(f"Desconto adicional por fidelidade: {int(desconto_fidelidade * 100)}%")
else:
    print("Cliente não pertence ao clube de fidelidade, sem desconto adicional.")
print(f"Valor total da compra após o desconto: R$ {valor_total}")

