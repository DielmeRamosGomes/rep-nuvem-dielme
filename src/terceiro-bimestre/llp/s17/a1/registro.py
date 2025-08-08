while True:
    cargo = input("Digite o cargo do funcionário [gerente/funcionario]: ")
    dia = input("Digite o dia da semana [segunda/terca/quarta/quinta/sexta]: ")
    if cargo.lower() == "gerente":
        print(f"O gerente tem acesso irrestrito no {dia}.")
        break
    elif cargo.lower() == "funcionario":
        if dia in ["segunda", "terca", "quarta", "quinta", "sexta"]:
            print(f"O funcionário tem acesso irrestrito no {dia}.")
            break
        elif dia in ["sabado", "domingo"]:
            print(f"O funcionário não tem acesso no {dia}.")
            break
        
        