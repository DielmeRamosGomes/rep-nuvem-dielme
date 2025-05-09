class Lampada():
    def __init__(self):
        self.estado = False

    def alterar_estado_ligado(self):
        if self.estado == False:
            self.estado = True
            return self.estado

    def alterar_estado_desligado(self):
        if self.estado == True:
            self.estado = False
            print(f"Lampada Desligada")

lampada = Lampada()
print(f"A lâmpada está ligada? {lampada.alterar_estado_ligado()}") 
print(f"A lâmpada está ligada? {lampada.alterar_estado_desligado()}") 




