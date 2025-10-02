// Constantes para elementos do DOM
const loginContainer = document.getElementById('login-container');
const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const messageElement = document.getElementById('message');

const protectedContent = document.getElementById('protected-content');
const logoutButton = document.getElementById('logout-button');
const fetchDataButton = document.getElementById('fetch-data-button');
const protectedDataMessage = document.getElementById('protected-data-message');

// --- Funções de Utilitário ---

/**
 * Pega o token JWT armazenado no LocalStorage.
 */
function getToken() {
    return localStorage.getItem('authToken');
}

/**
 * Armazena o token JWT no LocalStorage.
 */
function setToken(token) {
    localStorage.setItem('authToken', token);
}

/**
 * Remove o token JWT do LocalStorage.
 */
function removeToken() {
    localStorage.removeItem('authToken');
}

/**
 * Atualiza a interface do usuário com base no status de login.
 */
function updateUI() {
    const token = getToken();

    if (token) {
        // Logado: Esconde o login e mostra o conteúdo protegido
        loginContainer.classList.add('hidden');
        protectedContent.classList.remove('hidden');
    } else {
        // Deslogado: Mostra o login e esconde o conteúdo protegido
        loginContainer.classList.remove('hidden');
        protectedContent.classList.add('hidden');
    }
    messageElement.textContent = ''; // Limpa qualquer mensagem de erro
}


// --- Simulação de Back-end (Mock) ---

// Simula a chamada de API de login
async function mockLogin(username, password) {
    // Apenas para fins de demonstração, aceite qualquer usuário/senha não-vazio.
    if (username && password) {
        // Em uma aplicação real, aqui você faria um POST para sua API.
        console.log(`Tentando login com: ${username}/${password}`);
        
        // Simula o retorno de um JWT após autenticação bem-sucedida.
        // **Este é um token de exemplo/mock. Não é real.**
        const mockJwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyMywiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yP' + username;
        
        return { success: true, token: mockJwt };
    } else {
        return { success: false, message: 'Usuário ou senha inválidos.' };
    }
}

// Simula a chamada de API para dados protegidos
async function mockFetchProtectedData() {
    const token = getToken();

    if (!token) {
        // Se não houver token, o acesso é negado (ou redireciona para login)
        return { success: false, message: 'Não autorizado. Faça login novamente.' };
    }

    // Em uma aplicação real, o header de Autorização é essencial para o JWT
    const headers = {
        'Authorization': `Bearer ${token}` // Formato padrão para enviar o JWT
    };

    // Simulação da chamada de API
    console.log("Chamada de API para dados protegidos com header:", headers.Authorization);
    
    // Simula uma resposta de sucesso
    return { success: true, data: 'Dados confidenciais carregados com sucesso! (Token: ' + token.substring(0, 20) + '...)', status: 200 };
}


// --- Manipuladores de Eventos ---

// 1. Lida com o Envio do Formulário de Login
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    messageElement.textContent = 'Autenticando...';

    const username = usernameInput.value;
    const password = passwordInput.value;

    try {
        const response = await mockLogin(username, password);

        if (response.success) {
            setToken(response.token); // Armazena o JWT
            updateUI();
            usernameInput.value = ''; // Limpa o formulário
            passwordInput.value = '';
        } else {
            messageElement.textContent = response.message || 'Erro ao fazer login.';
        }
    } catch (error) {
        messageElement.textContent = 'Erro de rede ou servidor.';
        console.error('Erro de login:', error);
    }
});

// 2. Lida com a Busca de Dados Protegidos
fetchDataButton.addEventListener('click', async () => {
    protectedDataMessage.textContent = 'Buscando dados...';
    
    const response = await mockFetchProtectedData();

    if (response.success) {
        protectedDataMessage.textContent = response.data;
    } else {
        // Se a chamada falhar (ex: token inválido ou expirado), desloga o usuário
        protectedDataMessage.textContent = `Erro: ${response.message}`;
        if (response.status === 401 || response.status === 403) {
             handleLogout(); // Força o logout se a API indicar token inválido
        }
    }
});

// 3. Lida com o Logout
function handleLogout() {
    removeToken(); // Remove o JWT do LocalStorage
    updateUI();
    protectedDataMessage.textContent = 'Carregando dados...'; // Reseta o texto
    alert('Você foi desconectado!');
}

logoutButton.addEventListener('click', handleLogout);

// --- Inicialização ---
document.addEventListener('DOMContentLoaded', updateUI); // Verifica o status de login ao carregar a páginaF

