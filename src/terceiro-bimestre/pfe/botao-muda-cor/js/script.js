const buttonCor = document.querySelector('.button-cor');
const colorBox = document.querySelector('#colorBox');
const pNewColor = document.querySelector('#p-new-color');

buttonCor.addEventListener('click', () => {
    const novaCor = geraCorAleatoria();
    colorBox.style.backgroundColor = novaCor;
    pNewColor.textContent = `Cor: ${novaCor}`;
});

function geraCorAleatoria() {
    let cor = '#';
    let letras = '0123456789ABCDEF';
    for (let i = 0; i < 6; i++) {
        cor += letras[Math.floor(Math.random() * 16)];
    }
    return cor;
}
