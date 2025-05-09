class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

pessoa = Pessoa("João", 30)
print(f"O nome da pessoa é: {pessoa.get_nome()}")
print(f"A idade da pessoa é: {pessoa.get_idade()}")

