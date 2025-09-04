def menu_alexa():
    print("\n----------Menu Alexa------------")
    print("1. Ligar Tv")
    print("2. Ligar PlayStation")
    print("3. Ligar Som")
    print("4 . Sair do menu")
    print("----------------------------------\n")

def escolha_tv():
    return "A TV foi ligada"

def escolha_playstation():
    return "O PlayStation foi ligado"

def escolha_som():
    return "O Som foi ligado"

def escolha_sair():
    return "Saindo do menu tchau!"

def padrao():
    return "Opção invalida tente novamente"
    
def executar_menu():
    menu = {
        "1": escolha_tv(),
        "2": escolha_playstation(),
        "3": escolha_som(),
        "4": escolha_sair()
    }
    while True:
        menu_alexa()
        escolha = input("Escolha uma opção: ")
        acao = menu.get(escolha, padrao)
        print(f"Ação do menu: {acao}")
        if acao == "Saindo do menu tchau!":
            break
        print()
        
#Inicia a execução do menu
if __name__=="__main__":   
    executar_menu()