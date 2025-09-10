const btnEnviar = document.querySelector('#btn-enviar');
const paragrafoFrase = document.querySelector('#paragrafo-frase');
const inputFrase = document.querySelector('#input-frase');

btnEnviar.addEventListener('click', () => {
    let novaCor = corAleatoria();
    paragrafoFrase.style.backgroundColor = novaCor;
    paragrafoFrase.innerText = inputFrase.value
});

function corAleatoria() {
    let cor = '#';
    let algarismos = '0123456789ABCDEF';
    for (let i = 0 ; i < 6 ; i++) {
        cor += algarismos[Math.floor(Math.random() * 16)]
    }
    return cor;
}
