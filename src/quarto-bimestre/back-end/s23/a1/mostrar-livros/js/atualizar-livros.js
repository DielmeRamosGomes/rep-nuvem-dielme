const btnCadastro = document.querySelector('.btn-cadastrar');
const idLivro = document.querySelector('#id-livro');
const nomeLivro = document.querySelector('#nome-livro');
const autorLivro = document.querySelector('#autor-livro');
const categoriaLivro = document.querySelector('#categoria-livro');
const formCadastro = document.querySelector('.form-cadastro');
const pLivroCadastrado = document.querySelector('#livro-cadastrado');

async function fetchAtualizarLivro() {
    let resposta = null;
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
        resposta = await fetch('http://localhost:3000/atualizarlivros', {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(livro)
    });
    if (!resposta.ok) {
        const erroData = await resposta.json(); // Tenta ler o corpo do erro (se houver)
        pLivroCadastrado.textContent = `Erro HTTP! Status: ${resposta.status} - Mensagem: ${erroData.message || 'Desconhecida'}`;
        throw new Error(`Erro HTTP! Status: ${resposta.status} - Mensagem: ${erroData.message || 'Desconhecida'}`); 
    }
    pLivroCadastrado.textContent = `Livro atualizado com sucesso`;
    } catch (error) {
        console.log(`Erro ao atualizar livro: ${error}`);
        pLivroCadastrado.textContent = `Erro ao atualizar livro`;
    }  
}

btnCadastro.addEventListener('click', (e) => {
    e.preventDefault();
    fetchAtualizarLivro();
});

