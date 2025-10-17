import Usuario from "./Usuario.js";
import TipoUsuario from "./TipoUsuario.js";

const usuario = new Usuario(1, 'Dielme', 'dielme@exemplo.com', '1234', TipoUsuario.Administrador);
usuario.exibirDetalhes(usuario.getTipoUsuario());




