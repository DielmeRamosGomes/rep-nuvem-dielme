const nomeUsuario = document.querySelector('#nome-usuario');
const titulo = document.querySelector('#titulo');
const btnBuscar = document.querySelector('#btn-buscar');

// Acessando a variável global do CDN
const { Octokit } = window; 
const octokit = new Octokit(); 


async function fetchUserRepos() {
    const listElement = document.getElementById('repo-list');
    listElement.innerHTML = '<li>Carregando repositórios...</li>';
    try {
        // 2. Chama um método específico do SDK para a API
        // O SDK lida com a URL completa, headers e parsing do JSON
        const response = await octokit.request('GET /users/{username}/repos', {
            username: nomeUsuario.value,
            sort: 'updated',
            per_page: 5,
            headers: {
                'X-GitHub-Api-Version': '2022-11-28'
            }
        });

        // 3. Verifica a resposta (O SDK geralmente facilita o tratamento de erros)
        const repos = response.data;
        listElement.innerHTML = ''; // Limpa a mensagem de carregamento

        if (repos.length === 0) {
            listElement.innerHTML = `<li>Nenhum repositório público encontrado para ${GITHUB_USERNAME}.</li>`;
            return;
        }

        // 4. Exibe os dados
        repos.forEach(repo => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `
                <a href="${repo.html_url}" target="_blank">
                    <strong>${repo.name}</strong>
                </a> 
                (${repo.stargazers_count} Estrelas)
            `;
            listElement.appendChild(listItem);
        });

    } catch (error) {
        console.error('Erro ao buscar repositórios do GitHub:', error);
        listElement.innerHTML = `<li>Erro: Falha ao carregar repositórios. ${error.message}</li>`;
    }
}

btnBuscar.addEventListener('click', () => {
    if (nomeUsuario.value.trim() === '') {
        alert('Por favor, digite um nome de usuário do GitHub.');
        return;
    }
    else {
        titulo.textContent = `Repositórios do Usuário: ${nomeUsuario.value}`;
        fetchUserRepos();
    }
});