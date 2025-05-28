pedido = float(input("Digite o valor do pedido: "))
clube_fidelidade = input("O cliente é do clube de fidelidade? (sim/nao): ").lower()
taxa_entrega = 5
desconto = 2
if pedido < 10:
    if clube_fidelidade == "sim":
        taxa_entrega = taxa_entrega - desconto
        pedido = pedido + taxa_entrega
        print(f"Pedido = {pedido} e a Taxa de Entrega = {taxa_entrega}")
    else:
        print(f"Pedido = {pedido} e a Taxa de Entrega = {taxa_entrega}")
if pedido >= 10 and pedido < 20:
    if clube_fidelidade == "sim":
        taxa_entrega = 3
        taxa_entrega = taxa_entrega - desconto
        pedido = pedido + taxa_entrega
        print(f"Pedido = {pedido} e a Taxa de Entrega = {taxa_entrega}")
    else:
        taxa_entrega = 3
        print(f"Pedido = {pedido} e a Taxa de Entrega = {taxa_entrega}")
else:
    taxa_entrega = 0
    pedido = pedido + taxa_entrega
    print(f"Pedido = {pedido} e a Taxa de Entrega = {taxa_entrega}")