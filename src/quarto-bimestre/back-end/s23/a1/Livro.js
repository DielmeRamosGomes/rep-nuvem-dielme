class Livro {
    constructor(id, nome, autor, categoria) {
        this.id = id;
        this.nome = nome;
        this.autor = autor;
        this.categoria = categoria;
    }

    getId() {
        return this.id;
    }

    getNome() {
        return this.nome;
    }

    getAutor() {
        return this.autor;
    }

    getCategoria() {
        return this.categoria;
    }

    setId(id) {
        this.id = id;
    }

    setNome(nome) {
        this.nome = nome
    }

    setAutor(autor) {
        this.autor = autor;
    }

    setCategoria(categoria) {
        this.categoria = categoria;
    }

    exibirDetalhes() {
        console.log(`ID: ${this.getId()}`);
        console.log(`Nome: ${this.getNome()}`);
        console.log(`Autor: ${this.getAutor()}`);
        console.log(`Categoria: ${this.getCategoria()}`);
    }
}
export default Livro;



