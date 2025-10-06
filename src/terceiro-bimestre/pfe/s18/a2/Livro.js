class Livro {
    constructor(id, titulo, autor, anoPublicacao, editora, genero) {
        this.__id = id; 
        this.__titulo = titulo;
        this.__autor = autor;
        this.__anoPublicacao = anoPublicacao;
        this.__editora = editora;
        this.__genero = genero;
    }

    getId() {
        return this.__id;
    }

    getTitulo() {
        return this.__titulo;
    }

    getAutor() {
        return this.__autor;
    }

    getAnoPublicacao() {
        return this.__anoPublicacao;
    }

    getEditora() {
        return this.__editora;
    }

    getGenero() {
        return this.__genero;
    }

    getInformacoes() {
        console.log(`Id: ${this.getId()}`);
        console.log(`Título: ${this.getTitulo()}`);
        console.log(`Autor: ${this.getAutor()}`);
        console.log(`Ano de Publicação: ${this.getAnoPublicacao()}`);
        console.log(`Editora: ${this.getEditora()}`);
        console.log(`Gênero: ${this.getGenero()}`);
    }
}
export default Livro;






