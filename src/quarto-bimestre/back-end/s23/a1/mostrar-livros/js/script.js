const btnBuscarLivro = document.querySelector('#btn-buscar');
const idLivro = document.querySelector('#id-livro');
const nomeLivro = document.querySelector('#nome-livro');
const autorLivro = document.querySelector('#autor-livro');
const categoriaLivro = document.querySelector('#categoria-livro');
const card = document.querySelector('.card');

function fetchBuscarLivros() {
    fetch('http://localhost:3000/listarlivros')
        .then(resposta => {
            if (!resposta.ok) {
                throw new Error(`Erro de rede: ${resposta.statusText}`);
            }
            return resposta.json();
        })
        .then(dado => {
            card.innerHTML = ``;

            dado.forEach(livro => {
                const novoCard = document.createElement('form');
                novoCard.classList.add('card');

                novoCard.innerHTML = `
                    <h1 id="id-livro">ID: ${livro.id}</h1>
                    <h2 id="nome-livro">Nome: ${livro.nome}</h2>
                    <h3 id="autor-livro">Autor: ${livro.autor}</h3>
                    <h4 id="categoria">Categoria: ${livro.categoria}</h4>
                `;
                card.appendChild(novoCard);
            });
        })
        .catch(error => {
            console.log(`Houve um problema com a operação fetch: ${error}`);
            idLivro.textContent = `Erro ao se conectar com o servidor`;
        });
}

btnBuscarLivro.addEventListener('click', fetchBuscarLivros);

