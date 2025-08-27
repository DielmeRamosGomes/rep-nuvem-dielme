const btnLivro = document.querySelector('#btn-livro');

btnLivro.addEventListener('click', function (event) {
    event.preventDefault();
    const formLivro = document.querySelector('.form-livros');
    const formData = new FormData(formLivro);

    const livro = {
        nome: formData.get('nome'),
        editora: formData.get('editora'),
        ano: formData.get('ano') 
    };
    
    // Verificação de dados antes de enviar a requisição
    if (!livro.nome || !livro.editora || !livro.ano) {
      console.error('Por favor, preencha todos os campos!');
      return;
    }

    console.log('Dados do livro a ser enviado: ', livro);

    fetch('http://localhost:3000/cadastrarlivro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(livro)
    })
        .then(response => {
            if (response.status === 400) {
                return response.json().then(data => {
                    console.error('Erro 400 (Bad Request):', data.message);
                });
            }
            if (!response.ok) {
                throw new Error('Erro na requisição: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log('Livro cadastrado com sucesso:', data);
            alert('Livro cadastrado com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao cadastrar livro:', error);
        });

    fetch('http://localhost:3000/listarlivros')
        .then(response => response.json())
        .then(data => {
            console.log('Livros cadastrados:', data);
        })
        .catch(error => {
            console.error('Erro ao listar livros:', error);
        });
});