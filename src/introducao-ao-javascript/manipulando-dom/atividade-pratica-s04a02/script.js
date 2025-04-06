const botao = document.getElementById('botao');
const paragrafo = document.getElementById('paragrafo');

botao.addEventListener('click', () => {
  paragrafo.textContent = 'Parágrafo Alterado!';
});

