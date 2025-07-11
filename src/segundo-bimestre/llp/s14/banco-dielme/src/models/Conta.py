import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.Usuario import Usuario

class Conta:
    def __init__(self, agencia: str, numero: str, usuario: Usuario, saldo: float):
        self.__agencia = agencia
        self.__numero = numero
        self.__usuario = usuario
        self.__saldo = self.__setSaldo(saldo)
        
    def getAgencia(self):
        return self.__agencia
    
    def getNumero(self):
        return self.__numero
    
    def getSaldo(self):
        return self.__saldo
    
    def __setSaldo(self, valor: float):
        if valor < 50.0:
            self.__saldo = 50.0
        else:
            self.__saldo = valor
        return self.__saldo
        
    def getUsuario(self):
        return self.__usuario
    