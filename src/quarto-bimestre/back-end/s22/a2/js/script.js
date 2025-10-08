const nomeUsuario = document.querySelector('#nome-usuario');
const titulo = document.querySelector('#titulo');
const btnBuscar = document.querySelector('#btn-buscar');

// Acessando a variável global do CDN 
const octokit = new Octokit(); 

async function fetchUserRepos(nomeUsuarioString) {
    const listElement = document.getElementById('repo-list');
    listElement.innerHTML = '<li>Carregando repositórios...</li>';
    try {
        // 2. Chama um método específico do SDK para a API
        // O SDK lida com a URL completa, headers e parsing do JSON
        const response = await octokit.rest.repos.listForUser({
            username: nomeUsuarioString,
            sort: 'updated',
            per_page: 10,
        });

        // 3. Verifica a resposta (O SDK geralmente facilita o tratamento de erros)
        const repos = response.data;
        listElement.innerHTML = ''; // Limpa a mensagem de carregamento

        if (repos.length === 0) {
            listElement.innerHTML = `<li>Nenhum repositório público encontrado para ${nomeUsuarioString}.</li>`;
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
    const nomeUsuarioValor = nomeUsuario.value.trim();
    if (nomeUsuarioValor === '') {
        alert('Por favor, digite um nome de usuário do GitHub.');
        return;
    }
    titulo.textContent = `Repositórios do Usuário: ${nomeUsuarioValor}`;
    fetchUserRepos(nomeUsuarioValor);
});