
def verifica_senha(senha):
    try:
        alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
        digitos = "0123456789"
        caracteres_especiais = "!@#$"
        if len(senha) != 12:
            return "Senha invalida: A senha deve ter exatamente 12 caracteres."
        elif not verifica_letras(senha, alfabeto_maiusculo):
            return "Senha invalida: A senha deve conter pelo menos uma letra maiuscula."
        elif not verifica_letras(senha, alfabeto_minusculo):
            return "Senha invalida: A senha deve conter pelo menos uma letra minuscula."
        elif not verifica_letras(senha, digitos):
            return "Senha invalida: A senha deve conter pelo menos um digito."
        elif not verifica_letras(senha, caracteres_especiais):
            return "Senha invalida: A senha deve conter pelo menos um caractere especial."
        else:
            return "Senha foi considerada forte."
    except TypeError:
        return "Erro: A senha deve ser uma string."

def verifica_letras(senha, alfabeto):
    for char in senha:
        if char in alfabeto:
            return True
    return False

print(verifica_senha("Abcdefghij1!"))