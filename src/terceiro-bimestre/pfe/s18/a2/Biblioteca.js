class Biblioteca {
    constructor() {
        this.__livros = [];
    }

    adicionar_livro(livro) {
        this.__livros.push(livro);
    }

    remover_livro(id) {
        let livro = this.busca_livro(id);
        if (livro) {
            this.__livros.pop(livro);
        }
        else {
            console.log(`Livro com o Id = ${id} não encontrado`);
        }
        
    }

    busca_livro(id) {
        return this.__livros.find(livro => 
            livro.getId() === id) || null;
    }

    mostrar_catalogo_livros() {
        this.__livros.forEach(livro => {
            livro.getInformacoes();
            console.log("--------------------------------------");
        });
    }
}
export default Biblioteca;
