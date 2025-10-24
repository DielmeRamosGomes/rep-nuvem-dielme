const btnCadastro = document.querySelector('.btn-cadastrar');
const idLivro = document.querySelector('#id-livro');
const nomeLivro = document.querySelector('#nome-livro');
const autorLivro = document.querySelector('#autor-livro');
const categoriaLivro = document.querySelector('#categoria-livro');
const formCadastro = document.querySelector('.form-cadastro');
const pLivroCadastrado = document.querySelector('#livro-cadastrado');

function fetchCadastrarLivro() {
    pLivroCadastrado.textContent = ``;
    const formDado = new FormData(formCadastro);
    const livro = {
        id: formDado.get('id'),
        nome: formDado.get('nome'),
        autor: formDado.get('autor'),
        categoria: formDado.get('categoria')
    }
    console.log(livro);
    try {
        fetch('http://localhost:3000/cadastrarlivros', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(livro)
    });
    pLivroCadastrado.textContent = `Livro cadastrado com sucesso`;
    } catch (error) {
        console.log(`Erro ao cadastrar livro: ${error}`);
        pLivroCadastrado.textContent = `Erro ao cadastrar livro`;
    }  
}

btnCadastro.addEventListener('click', (e) => {
    e.preventDefault();
    fetchCadastrarLivro();
});
