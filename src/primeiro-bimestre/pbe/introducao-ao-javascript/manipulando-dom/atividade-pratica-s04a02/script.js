const botao = document.getElementById('botao');
const botaoVolta = document.getElementById('botao-volta');
const paragrafo = document.getElementById('paragrafo');

botao.addEventListener('click', () => {
  paragrafo.textContent = 'Parágrafo Alterado!';
});

botaoVolta.addEventListener('click', () => {
  paragrafo.textContent = 'Olá bem-vindo ao site!';
});

