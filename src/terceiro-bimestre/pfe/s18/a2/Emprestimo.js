import Livro from './Livro.js';
import Usuario from './Usuario.js';

class Emprestimo {
  constructor(id, livro, usuario, data_emprestimo, data_devolucao) {
    this.__id = id;
    this.__livros = [];
    this.__livros.add_livro(livro);
    this.__usuario = usuario;
    this.__data_emprestimo = data_emprestimo;
    this.__data_devolucao = data_devolucao;
  }

  getId() {
    return this.__id;
  }

  getDataEmprestimo() {
    return this.__data_emprestimo;
  }

  getDataDevolucao() {
    return this.__data_devolucao;
  }

  add_livro(livro) {
    this.__livros.push(livro);
  }

  remover_livro(id) {
    let livro = this.busca_livro(id);
    if (livro) {
      this.__livros.pop(livro);
    } else {
      console.log(`Livro com o Id = ${id} não encontrado`);
    }
  }

  busca_livro(id) {
    return this.__livros.find((livro) => livro.getId() === id) || null;
  }

  mostrar_catalogo_livros() {
    this.__livros.forEach((livro) => {
      livro.getInformacoes();
      console.log("--------------------------------------");
    });
  }

  exibir_emprestimo() {
    console.log(`ID: ${this.getId()}`);
    this.mostrar_catalogo_livros();
    this.__usuario.getInformacoes();
    this.getDataEmprestimo();
    this.getDataDevolucao();
  }

}
