vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def calcula_total_vendas_anual(vendas_mensais):
    resultado = 0
    for venda in vendas_mensais:
        resultado += venda
    return resultado

def media_mensal_vendas(vendas_mensais):
    total = calcula_total_vendas_anual(vendas_mensais)
    media = total / len(vendas_mensais)
    return media

def mes_maior_venda(vendas_mensais):
    maior_venda = max(vendas_mensais)
    mes = vendas_mensais.index(maior_venda) + 1
    return mes

def meses_do_ano():
    mes = mes_maior_venda(vendas_mensais)
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[mes - 1]
    
def opcoes():
    print("\nOpções disponíveis:")
    print("\n1 - Total de vendas anual")
    print("2 - Média mensal de vendas")
    print("3 - Mês com maior venda \n")

def execucao():
    try:
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            total = calcula_total_vendas_anual(vendas_mensais)
            print(f"\nTotal de vendas anual é = {total}")
        elif opcao == 2:
            media = media_mensal_vendas(vendas_mensais)
            print(f"\nMédia mensal de vendas: {media:.2f}")
        elif opcao == 3:
            mes = meses_do_ano()
            print(f"\nMês com maior venda: {mes}")
        else:
            print("\nOpção inválida. Por favor, escolha uma opção entre (1 e 3).")
    except ValueError:
        print("\nOpção inválida. Por favor, insira um número.")

def menu():
    while True:
        opcoes()
        execucao()
        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar == 'n':
            print("\nEncerrando o programa. Até mais!")
            break

if __name__ == "__main__":
    menu()    
    