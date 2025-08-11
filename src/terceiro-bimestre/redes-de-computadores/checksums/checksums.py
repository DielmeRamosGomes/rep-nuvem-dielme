def calcular_checksum(mensagem):
    checksum = 0
    for char in mensagem:
        checksum += ord(char)
    return checksum

def verificar_checksum(mensagem, checksum):
    checksum_calculado = calcular_checksum(mensagem)
    return checksum_calculado == checksum

mensagem = input("Digite a mensagem para ser enviada: ")
checksum_enviado = calcular_checksum(mensagem)
print(f"Checksum enviado: {checksum_enviado}")

mensagem_recebida = input("Digite a mensagem recebida: ")
integridade = verificar_checksum(mensagem_recebida, checksum_enviado)
print(f"Integridade verificada: {'OK: Dados recebidos corretamente' if integridade else 'Erro: dados corrompidos'}")

