const header = document.querySelector('.header');

header.addEventListener('click', function() {
    const novaCor = geraCorAleatoria();
    header.style.backgroundColor = novaCor;
});

function geraCorAleatoria() {
    let cor = '#';
    let letras = '0123456789ABCDEF';
    for (let i = 0; i < 6; i++) {
        cor += letras[Math.floor(Math.random() * 16)];
    }
    return cor;
}

