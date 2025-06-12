// npm install react-router-dom
import Cadastro from "./Cadastro";
import { useNavigate } from 'react-router-dom';

function Configuracao() {
    // navigate é usado para redirecionar o usuário para outra rota
    const navigate = useNavigate();

    const btnSelecionar = (event) => {
        event.preventDefault(); // Impede o envio do formulário

        const form = document.getElementById('formConfiguracao');
        const formData = new FormData(form);
        const usuarioSelecionado = formData.get('usuario');

        if (usuarioSelecionado === "administrador") {
            navigate('/cadastro'); // Redireciona para a rota de cadastro
        }
        else if (usuarioSelecionado === "gerente") {
            navigate('/gerente');
        }
        else if (usuarioSelecionado === "usuario") {
            navigate('/usuario');
        }

        console.log(`Usuário selecionado: ${usuarioSelecionado}`);

    };

    return (
        <div className="configuracao-container">
            <h1>Escolha um usuario</h1>
            <form id='formConfiguracao'>
                <div id='configuracao'>
                    <ul id='listaDeUsuarios'>
                        <li> <input type="radio" id="usuario1" name="usuario" value="administrador" required />{"Administrador"}</li>
                        <li> <input type="radio" id="usuario2" name="usuario" value="gerente" required />{"Gerente"}</li>
                        <li> <input type="radio" id="usuario3" name="usuario" value="usuario" required />{"Usuario"}</li>
                    </ul>
                    <button id='buttonSelecionar' type="submit" onClick={btnSelecionar}>Selecionar</button>
                </div>
            </form>
        </div>
    );
}
export default Configuracao;