pagamento = "CARTAO_CREDITO"
opcao = "VISTA"
if pagamento == "CARTAO_CREDITO":
    if opcao == "VISTA":
        print("Pagamento feito com cartao de credito a vista")
    elif opcao == "PARCELADO":
        print("Pagamento parcelado")
elif pagamento == "CARTAO_DEBITO":
    print("Pagamento feito com débito")
elif pagamento == "PIX":
    if opcao == "VISTA":
        print("Pix feito a vista")
    elif opcao == "PARCELADO":
        print("Pix Parcelado")
else:
    print("Erro não foi possível realizar pagamento")




