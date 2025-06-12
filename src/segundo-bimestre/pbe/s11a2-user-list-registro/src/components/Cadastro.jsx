import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Cadastro() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    if (usuarios.length > 0) {
      console.log("Usuários Atualmente Cadastrados:");
      usuarios.forEach((usuario) => {
        console.log(`  Cargo: ${usuario.cargo}, Nome: ${usuario.nome}, Email: ${usuario.email}`);
      });
      console.log("--------------------------------------------");
    }
  }, [usuarios]); // O array de dependências '[usuarios]' faz com que o useEffect rode quando 'usuarios' mudar.

  const addUsuario = (usuario) => {
    setUsuarios((prevUsuarios) => [...prevUsuarios, usuario]); 
  };

  const cadastrarUsuario = (event) => {
    event.preventDefault(); // Impede o envio do formulário

    const form = document.getElementById('formCadastro');
    const formData = new FormData(form);

    const usuario = {
      cargo: formData.get('cargo'),
      nome: formData.get('nome'),
      email: formData.get('email'),
      senha: formData.get('senha')
    };

    addUsuario(usuario);

    //alert(`Usuário cadastrado com sucesso!\nCargo: ${usuario.cargo}\nNome: ${usuario.nome}\nEmail: ${usuario.email}`);
    form.reset(); // Limpa o formulário após o cadastro
  };

  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
      </nav>
      <h1>Cadastro de usuário</h1>
      <form id='formCadastro' onSubmit={cadastrarUsuario}>
        <div id='cadastro'>
          <ul id='listaDeCargos'>
            <li> <input type="radio" id="cargo1" name="cargo" value="Administrador" required />{"Administrador"}</li>
            <li> <input type="radio" id="cargo2" name="cargo" value="Gerente" required />{"Gerente"}</li>
            <li> <input type="radio" id="cargo3" name="cargo" value="Usuario" required />{"Usuário"}</li>
          </ul>
          <label htmlFor="nome">Nome: </label>
          <input type="text" id="nome" name="nome" required />
          <br />
          <label htmlFor="email">Email: </label>
          <input type="email" id="email" name="email" required />
          <br />
          <label htmlFor="senha">Senha: </label>
          <input type="password" id="senha" name="senha" required />
          <br />
          <button id='buttonCadastrar' type="submit">Cadastrar</button>
        </div>
      </form>
    </div>
  );
}
export default Cadastro;



