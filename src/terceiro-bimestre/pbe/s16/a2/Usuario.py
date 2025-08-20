import jwt
from AuthManager import AuthManager

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    def get_dados(self, token):
        try:
            auth_payload = AuthManager.validar_token(token)
            if auth_payload.get('sub') == str(self.__id):
                print("Token válido. Acesso concedido.")
                return {
                    "id": self.get_id(),
                    "nome": self.get_nome(),
                    "email": self.get_email(),
                    "senha": self.get_senha()
                }
            else:
                print("Token válido, mas pertence a outro usuário. Acesso negado.")
                return None
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            print("Token inválido ou expirado. Acesso negado.")
            return None
        
usuario = Usuario(id=1, nome="Dielme Ramos Gomes", email="dielme@exemplo.com", senha="123456")

print(f"Usuário tenta acessar dados sem um token")
print(f"Resultado: {usuario.get_dados(token=None)} \n")

print("O usuário faz login via OAuth 2.0 e obtém o token")
token_valido = AuthManager.gerar_token_jwt(id_usuario=1)
print(f"O token JWT gerado: {token_valido} \n")

print("O usuário tenta acessar os dados com o token válido")
print(f"Resultado: {usuario.get_dados(token=token_valido)} \n")

print("O usuário tenta usar um token de outro usuário")
token_de_outro_usuario = AuthManager.gerar_token_jwt(id_usuario=999)
print(f"Resultado: {usuario.get_dados(token=token_de_outro_usuario)}")


