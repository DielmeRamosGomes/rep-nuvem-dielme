def processar_texto(texto):
    return texto.upper()

def processar_numero(numero):
    return numero * 2

def padrao():
    return "Opção inválida"

switch = {
    "texto": processar_texto,
    "numero": processar_numero
}

# Exemplo de uso
entrada = "texto"
valor = "Olá Mundo"
resultado = switch.get(entrada, padrao)(valor)
print(resultado)


