
def process_order(user_id, product_id, payment_info):
    if not (user_id and product_id and payment_info):
        return "Dados Invalidos!"
    print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado")
    return "Pedido confirmado com sucesso!"

resultado = process_order(1, 101, "crédito")
print(resultado)








