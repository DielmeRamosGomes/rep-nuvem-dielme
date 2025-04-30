class Lampada():
    def __init__(self):
        self.estado = False

    def alterar_estado(self):
        if self.estado == False:
            self.estado = True
            return "Lampada ligada"
        else:
            self.estado = False
            return "Lampada Desligada"

lampada = Lampada()
print(lampada.alterar_estado()) # lampada ligada
print(lampada.alterar_estado()) # lampada Desligada



