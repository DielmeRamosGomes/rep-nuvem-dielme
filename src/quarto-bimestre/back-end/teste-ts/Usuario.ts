import TipoUsuario from "./TipoUsuario.js";

class Usuario {
    private id: number;
    private nome: String;
    private email: String;
    private senha: String;
    private tipoUsuario: TipoUsuario;

    constructor(id: number, nome: String, email: String, senha: String, tipoUsuario: TipoUsuario) {
        this.id = id;
        this.email = email;
        this.nome = nome;
        this.senha = senha;
        this.tipoUsuario = tipoUsuario;    
    }

    getId() {
        return this.id;
    }

    getNome() {
        return this.nome;
    }

    getEmail() {
        return this.email;
    }

    getTipoUsuario() {
        return this.tipoUsuario;
    }

    getSenha(tipoUsuario: TipoUsuario) {
        if (tipoUsuario === 1) {
            return this.senha;
        }
        else {
            console.log(`\nA senha só pode ser mostrada a um usuário que é Administrador`)
        }
    }

    exibirDetalhes(tipoUsuario: TipoUsuario) {
        console.log(`\nID: ${this.getId()}`);
        console.log(`Nome: ${this.getNome()}`);
        console.log(`Email: ${this.getEmail()}`);
        console.log(`Senha: ${this.getSenha(tipoUsuario)}`);
        console.log(`TipoUsuario: ${this.getTipoUsuario()}\n`);

    }

}
export default Usuario;



