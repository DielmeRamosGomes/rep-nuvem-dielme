"use strict";
exports.__esModule = true;
var Usuario = /** @class */ (function () {
    function Usuario(id, nome, email, senha, tipoUsuario) {
        this.id = id;
        this.email = email;
        this.nome = nome;
        this.senha = senha;
        this.tipoUsuario = tipoUsuario;
    }
    Usuario.prototype.getId = function () {
        return this.id;
    };
    Usuario.prototype.getNome = function () {
        return this.nome;
    };
    Usuario.prototype.getEmail = function () {
        return this.email;
    };
    Usuario.prototype.getTipoUsuario = function () {
        return this.tipoUsuario;
    };
    Usuario.prototype.getSenha = function (tipoUsuario) {
        if (tipoUsuario === 1) {
            return this.senha;
        }
        else {
            console.log("\nA senha s\u00F3 pode ser mostrada a um usu\u00E1rio que \u00E9 Administrador");
        }
    };
    Usuario.prototype.exibirDetalhes = function (tipoUsuario) {
        console.log("\nID: " + this.getId());
        console.log("Nome: " + this.getNome());
        console.log("Email: " + this.getEmail());
        console.log("Senha: " + this.getSenha(tipoUsuario));
        console.log("TipoUsuario: " + this.getTipoUsuario() + "\n");
    };
    return Usuario;
}());
exports["default"] = Usuario;
