class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_senha(self):
        return self.senha

    def mostra_usuario(self):
        print(f"ID: {self.get_id()}")
        print(f"Nome: {self.get_nome()}")
        print(f"Email: {self.get_email()}")
        
                