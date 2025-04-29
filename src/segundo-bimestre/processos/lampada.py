class Lampada():
    def __init__(self):
        self.estado = False

    def alterar_estado(self):
        if self.estado == False:
            self.estado = True
            print(f"Lampada ligada")
        else:
            self.estado = False
            print(f"Lampada Desligada")

lampada = Lampada()
print(lampada.alterar_estado()) # lampada ligada
print(lampada.alterar_estado()) # lampada Desligada



