def acender_luzes():
    return "Luzes acesas"

def ajustar_termostato(temperatura):
    return f"Termostato ajustado para {temperatura} graus"

def tocar_musica(musica):
    return f"Tocando {musica}"

def comando_nao_encontrado():
    return "Comando não reconhecido"

# Dicionário simulando SWITCH
comandos = {
    "acender luzes": acender_luzes,
    "ajustar termostato": ajustar_termostato,
    "tocar música": tocar_musica
}

# Função para processar comandos
def processar_comando(comando, *args):
    acao = comandos.get(comando, comando_nao_encontrado)
    return acao(*args)

# Exemplo de uso
print(processar_comando("acender luzes"))
print(processar_comando("ajustar termostato", 22))
print(processar_comando("tocar música", "Beethoven"))
print(processar_comando("abrir portas"))



