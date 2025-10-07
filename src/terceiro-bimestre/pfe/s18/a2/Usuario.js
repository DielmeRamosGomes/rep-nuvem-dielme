class Usuario {
    constructor(id, nome, email, senha) {
        this.__id = id;
        this.__nome = nome;
        this.__email = email;
        this.__senha = senha;
    }

    getId() {
        return this.__id;
    }

    getNome() {
        return this.__nome;
    }

    getEmail() {
        return this.__email;
    }

    getSenha() {
        return this.__senha;
    }

    getInformacoes() {
        console.log(`Id: ${this.__id}`);
        console.log(`Nome: ${this.__nome}`);
        console.log(`Email: ${this.__email}`);
        //console.log(`Senha: ${this.__senha}`);
    }

}
export default Usuario;


