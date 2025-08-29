const buttonCor = document.querySelector('.button-cor');
const colorBox = document.querySelector('#colorBox');
const pNewColor = document.querySelector('#p-new-color');
const h1Title = document.querySelector('.h1-title');

buttonCor.addEventListener('click', () => {
    const novaCor = geraCorAleatoria();
    colorBox.style.backgroundColor = novaCor;
    pNewColor.textContent = `Cor: ${novaCor}`;
    h1Title.style.color = novaCor;
    buttonCor.style.backgroundColor = novaCor;
});

buttonCor.addEventListener('mouseover', () => {
    buttonCor.style.padding = '20px';
});

buttonCor.addEventListener('mouseout', () => {
    buttonCor.style.padding = '10px';
});

function geraCorAleatoria() {
    let cor = '#';
    let letras = '0123456789ABCDEF';
    for (let i = 0; i < 6; i++) {
        cor += letras[Math.floor(Math.random() * 16)];
    }
    return cor;
}
