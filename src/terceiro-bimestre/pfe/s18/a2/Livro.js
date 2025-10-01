class Livro {
    constructor(titulo, autor, anoPublicacao, editora, genero) {
        this.__titulo = titulo;
        this.__autor = autor;
        this.__anoPublicacao = anoPublicacao;
        this.__editora = editora;
        this.__genero = genero;
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
        console.log(`Título: ${this.getTitulo()}`);
        console.log(`Autor: ${this.getAutor()}`);
        console.log(`Ano de Publicação: ${this.getAnoPublicacao()}`);
        console.log(`Editora: ${this.getEditora()}`);
        console.log(`Gênero: ${this.getGenero()}`);
    }
}
export default Livro;






