import jwt
from datetime import datetime, timedelta

class AuthManager:
    CHAVE_SECRETA = "sua-chave-secreta-altamente-segura-do-provedor"
    ALGORITMO = "HS256"
    
    @staticmethod
    def gerar_token_jwt(id_usuario):
        payload = {
            'sub': str(id_usuario),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        return jwt.encode(payload, AuthManager.CHAVE_SECRETA, algorithm=AuthManager.ALGORITMO)

    @staticmethod
    def validar_token(token):
        return jwt.decode(token, AuthManager.CHAVE_SECRETA, algorithms=[AuthManager.ALGORITMO])

