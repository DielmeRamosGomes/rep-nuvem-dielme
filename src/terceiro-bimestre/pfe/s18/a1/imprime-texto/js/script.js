const btnEnviar = document.querySelector('#btn-enviar');
const paragrafoFrase = document.querySelector('#paragrafo-frase');
const inputFrase = document.querySelector('#input-frase');

btnEnviar.addEventListener('click', () =>{
    paragrafoFrase.innerText = inputFrase.value
});

