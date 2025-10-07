import Livro from './Livro.js';
import Biblioteca from './Biblioteca.js'
import Usuario from './Usuario.js';

const livro = new Livro(1, "Harry Potter I", "JK Rowling", "1993-09-01", "Rocco", "Fantasia");
// livro.getInformacoes();
const livro2 = new Livro(2, "Harry Potter II", "JK Rowling", "1994-09-01", "Rocco", "Fantasia");
const biblioteca = new Biblioteca();
biblioteca.adicionar_livro(livro);
biblioteca.adicionar_livro(livro2);
// biblioteca.remover_livro(2);
//biblioteca.mostrar_catalogo_livros();
const usuario = new Usuario(1, "Dielme", "dielme@exemplo.com", "1234");
const usuario2 = new Usuario(2, "João", "joao@exemplo.com", "5678");
biblioteca.adicionar_usuario(usuario);
biblioteca.adicionar_usuario(usuario2);
//biblioteca.remover_usuario(3);
//biblioteca.mostrar_catalogo_usuarios();


