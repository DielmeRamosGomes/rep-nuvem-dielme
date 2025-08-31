
async function fetchWeather(city) {
    const apiKey = '9fa13f1e1e9678135d65dc70ac6e7a69';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=pt_br`;

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Cidade não encontrada ou erro na API');
        }
        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        displayError(error.message);
    }
}

async function axiosWeather(city) {
    const apiKey = '9fa13f1e1e9678135d65dc70ac6e7a69';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=pt_br`;

    try {
        const response = await axios.get(url);
        displayWeather(response.data);
    } catch (error) {
        if (error.response) {
            displayError('Erro: ' + (error.response.data.message || 'Cidade não encontrada ou erro na API'));
        } else {
            displayError(error.message);
        }
    }
}

function displayWeather(data) {
    const resultDiv = document.querySelector('#result');
    resultDiv.innerHTML =
        `<h2 style="color: black;">Clima em: ${data.name}</h2>
        <p style="color: black;">Temperatura: ${data.main.temp}°C</p>
        <p style="color: black;">Umidade: ${data.main.humidity}%</p>
        <p style="color: black;">Descrição: ${data.weather[0].description}</p>`;
    document.querySelector('#error').innerHTML = '';  // Limpa mensagens de erro
}

function displayError(message) {
    const errorDiv = document.querySelector('#error');
    errorDiv.innerHTML = `<p style="color: red;">Erro: ${message}</p>`;
    document.querySelector('#result').innerHTML = '';  // Limpa resultados de clima
}

function getWeather() {
    const city = document.querySelector('#city').value;
    const method = document.querySelector('#method').value;

    if (!city) {
        displayError('Por favor, insira o nome de uma cidade');
        return;
    }

    if (method === 'fetch') {
        fetchWeather(city);
    } else if (method === 'axios') {
        axiosWeather(city);
    }
}

/*
1. Qual é a diferença entre fetch e axios para realizar 
requisições HTTP em JavaScript?
R.: A principal diferença é que Fetch é uma API nativa do 
navegador para fazer requisições HTTP, enquanto Axios é uma 
biblioteca de terceiros.
Fetch retorna uma Promise que só rejeita em caso de falha na 
rede, exigindo a checagem manual do response.ok para erros HTTP
 (como 404). Axios, por sua vez, rejeita a Promise 
 automaticamente para códigos de status simplificando o 
 tratamento de erros.

2. Por que é importante tratar erros ao realizar requisições 
para uma API? Como isso pode ser feito no código?
R.: É crucial tratar erros para garantir a confiabilidade e a 
estabilidade da sua aplicação. Sem o tratamento adequado, falhas como uma API fora do ar, 
dados inválidos ou um erro de rede podem travar a aplicação, 
resultar em uma experiência ruim para o usuário e até mesmo 
causar problemas de segurança. Tratar os erros permite que você 
forneça feedback claro ao usuário, tente novamente a requisição 
ou execute um plano de contingência.


3. O que significa o parâmetro units=metric na URL da API 
OpenWeatherMap e qual é a sua importância?
R.: O parâmetro units=metric na URL da API OpenWeatherMap 
significa que as informações de temperatura, velocidade do 
vento e outras grandezas serão retornadas no sistema de 
unidades métricas global com grau celsius velocidade m/s. 
*/ 



