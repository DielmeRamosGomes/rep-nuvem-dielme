class Biblioteca {
  constructor() {
    this.__livros = [];
    this.__usuarios = [];
  }

  adicionar_usuario(usuario) {
    this.__usuarios.push(usuario);
  }

  remover_usuario(id) {
    let usuario = this.busca_usuario(id);
    if (usuario) {
      this.__usuarios.pop(usuario);
    } else {
      console.log(`Usuário com o Id = ${id} não encontrado`);
    }
  }

  busca_usuario(id) {
    return this.__usuarios.find((usuario) => usuario.getId() === id) || null;
  }

  mostrar_catalogo_usuarios() {
    this.__usuarios.forEach((usuario) => {
      console.log(`Id: ${usuario.getId()}`);
      console.log(`Nome: ${usuario.getNome()}`);
      console.log(`Email: ${usuario.getEmail()}`);
      console.log("--------------------------------------");
    });
  }

  adicionar_livro(livro) {
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
}
export default Biblioteca;
