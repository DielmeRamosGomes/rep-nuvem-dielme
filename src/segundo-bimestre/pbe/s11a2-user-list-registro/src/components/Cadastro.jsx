import React from 'react';

function Cadastro() {

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

    console.log(usuario);
    alert(`Usuário cadastrado com sucesso!\nCargo: ${usuario.cargo}\nNome: ${usuario.nome}\nEmail: ${usuario.email}`);
  };

  return (
    <div>
      <h1>Cadastro de usuário</h1>
        <form id='formCadastro'>
            <div id='cadastro'>
                <ul id='listaDeCargos'>
                    <li> <input type="radio" id="cargo1" name="cargo" value="Gerente" required />Gerente</li>
                    <li> <input type="radio" id="cargo2" name="cargo" value="Administrador" required />Administrador</li>
                    <li> <input type="radio" id="cargo3" name="cargo" value="Usuario" required />Usuário</li>
                </ul>
                <label htmlFor="nome">Nome: </label>
                <input type="text" id="nome" name="nome" required />
                <br/>
                <label htmlFor="email">Email: </label>
                <input type="email" id="email" name="email" required />
                <br/>
                <label htmlFor="senha">Senha: </label>
                <input type="password" id="senha" name="senha" required />
                <br/>
                <button id='buttonCadastrar' type="submit" onClick={cadastrarUsuario}>Cadastrar</button>
            </div>
        </form>
    </div>
  );
}
export default Cadastro;



