from models.Usuario import Usuario

def main():
    usuario = Usuario("Dielme", "dielme@exemplo.com", "1234")
    print(usuario.mostrar_usuario())

if __name__=="__main__":
     main()


