const btnLivro = document.querySelector('#btn-livro');

btnLivro.addEventListener('click', function (event) {
    event.preventDefault();
    const formLivro = document.querySelector('.form-livros');
    const formData = new FormData(formLivro);
    const livro = {
        nome: formData.get('#nome-livro'),
        editora: formData.get('#editora-livro'),
        ano: formData.get('#ano-livro')
    };

    fetch('http://localhost:3000/cadastrarlivro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(livro)
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

