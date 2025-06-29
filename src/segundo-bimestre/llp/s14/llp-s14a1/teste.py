def calcular_multa(tipo_livro, dias_atraso):
    
    categorias = {
        'ficção': lambda dias: dias * 0.50,
        'não ficção': lambda dias: dias * 0.60,
        'referência': lambda dias: 0.00
    }
    

    if tipo_livro in categorias:
        return categorias[tipo_livro](dias_atraso)
    else:
        
        return "Categoria de livro inválida."


tipo_livro = input("Digite a categoria do livro (ficção, não ficção, referência): ").strip().lower()
dias_atraso = int(input("Digite o número de dias de atraso: "))

multa = calcular_multa(tipo_livro, dias_atraso)

if isinstance(multa, float):
    print(f"A multa é: R$ {multa:.2f}")
else:
    print(multa)