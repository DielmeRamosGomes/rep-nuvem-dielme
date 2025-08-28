// http://127.0.0.1:5500/src/terceiro-bimestre/pfe/teste/index.html

const button = document.querySelector('#btn-click');
const resetButton = document.querySelector('#btn-reset');
const number = document.querySelector('.number-h2');

if (button && number && resetButton) {
    button.addEventListener('click', () => {
        number.textContent = parseInt(number.textContent) + 1;
    });

    resetButton.addEventListener('click', () => {
        number.textContent = '0';
    });
}



