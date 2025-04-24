class Candidato:
    def __init__(self, cand_numero, cand_partido, cand_nome, cand_vice):
        self.cand_numero = cand_numero
        self.cand_partido = cand_partido
        self.cand_nome = cand_nome
        self.cand_vice = cand_vice

    def exibe_canditado(self):
        print(f"Numero: {self.cand_numero}")
        print(f"Partido: {self.cand_partido}")
        print(f"Nome: {self.cand_nome}")
        print(f"Nome do Vice: {self.cand_vice}")

canditato1 = Candidato(1, "Partido B", "Carlos", "Maria")
canditato2 = Candidato(2, "Partido C", "Joao", "Igor")
canditato2.exibe_canditado()



