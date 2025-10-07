class Emprestimo {
    constructor(id, livro, usuario, data_emprestimo, data_devolucao) {
        this.__id = id;
        this.__livro = [];
        this.__livro.add_livro(livro);
        this.__usuario = usuario;
        this.__data_emprestimo = data_emprestimo;
        this.__data_devolucao = data_devolucao;
    }

    getId() {
        return this.__id;
    }

    add_livro(livro) {
        this.__livro.push(livro);
    }

    


}


