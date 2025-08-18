const celula1 = document.querySelector('.celula1');
const celula2 = document.querySelector('.celula2');
const celula3 = document.querySelector('.celula3');
const celula4 = document.querySelector('.celula4');
const celula5 = document.querySelector('.celula5');
const celula6 = document.querySelector('.celula6');
const celula7 = document.querySelector('.celula7');
const celula8 = document.querySelector('.celula8');
const celula9 = document.querySelector('.celula9');

const paragrafoCelula1 = document.querySelector('#paragrafo-celula1');
const paragrafoCelula2 = document.querySelector('#paragrafo-celula2');
const paragrafoCelula3 = document.querySelector('#paragrafo-celula3');
const paragrafoCelula4 = document.querySelector('#paragrafo-celula4');
const paragrafoCelula5 = document.querySelector('#paragrafo-celula5');
const paragrafoCelula6 = document.querySelector('#paragrafo-celula6');
const paragrafoCelula7 = document.querySelector('#paragrafo-celula7');
const paragrafoCelula8 = document.querySelector('#paragrafo-celula8');
const paragrafoCelula9 = document.querySelector('#paragrafo-celula9');

const buttonReset = document.querySelector('.button-reset');
const paragrafoVencedor = document.querySelector('#vencedor');
const gridContainer = document.querySelector('.grid-container');
let statusJogador = ["", "", "", "", "", "", "", "", ""];
let jogadorAtual = "X";

function verificaPosicao() {
    if (statusJogador[0] != "" && statusJogador[1] != "" && statusJogador[2] != "") {
        verificaGanhador();
    }
    if (statusJogador[3] != "" && statusJogador[4] != "" && statusJogador[5] != "") {
        verificaGanhador();
    }
    if (statusJogador[6] != "" && statusJogador[7] != "" && statusJogador[8] != "") {
        verificaGanhador();
    }
    if (statusJogador[0] != "" && statusJogador[3] != "" && statusJogador[6] != "") {
        verificaGanhador();
    }
    if (statusJogador[1] != "" && statusJogador[4] != "" && statusJogador[7] != "") {
        verificaGanhador();
    }
    if (statusJogador[2] != "" && statusJogador[5] != "" && statusJogador[8] != "") {
        verificaGanhador();
    }
    if (statusJogador[0] != "" && statusJogador[4] != "" && statusJogador[8] != "") {
        verificaGanhador();
    }
    if (statusJogador[2] != "" && statusJogador[4] != "" && statusJogador[6] != "") {
        verificaGanhador();
    }
}

function verificaGanhador() {
    let ganhou = false;
    if (statusJogador[0] === "X" && statusJogador[1] === "X" && statusJogador[2] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[0] === "O" && statusJogador[1] === "O" && statusJogador[2] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[3] === "X" && statusJogador[4] === "X" && statusJogador[5] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[3] === "O" && statusJogador[4] === "O" && statusJogador[5] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[6] === "X" && statusJogador[7] === "X" && statusJogador[8] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[6] === "O" && statusJogador[7] === "O" && statusJogador[8] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[0] === "X" && statusJogador[3] === "X" && statusJogador[6] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[0] === "O" && statusJogador[3] === "O" && statusJogador[6] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[1] === "X" && statusJogador[4] === "X" && statusJogador[7] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[1] === "O" && statusJogador[4] === "O" && statusJogador[7] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[2] === "X" && statusJogador[5] === "X" && statusJogador[8] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[2] === "O" && statusJogador[5] === "O" && statusJogador[8] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[0] === "X" && statusJogador[4] === "X" && statusJogador[8] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[0] === "O" && statusJogador[4] === "O" && statusJogador[8] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
    else if (statusJogador[2] === "X" && statusJogador[4] === "X" && statusJogador[6] === "X") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns X é Vencedor!";
    }
    else if (statusJogador[2] === "O" && statusJogador[4] === "O" && statusJogador[6] === "O") {
        ganhou = true;
        paragrafoVencedor.textContent = "Parabéns O é Vencedor!";
    }
}

function resetGame() {
    paragrafoCelula1.textContent = "";
    paragrafoCelula2.textContent = "";
    paragrafoCelula3.textContent = "";
    paragrafoCelula4.textContent = "";
    paragrafoCelula5.textContent = "";
    paragrafoCelula6.textContent = "";
    paragrafoCelula7.textContent = "";
    paragrafoCelula8.textContent = "";
    paragrafoCelula9.textContent = "";
}

celula1.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula1.textContent = jogadorAtual;
        statusJogador[0] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula1.textContent = jogadorAtual;
        statusJogador[0] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula2.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula2.textContent = jogadorAtual;
        statusJogador[1] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula2.textContent = jogadorAtual;
        statusJogador[1] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula3.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula3.textContent = jogadorAtual;
        statusJogador[2] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula3.textContent = jogadorAtual;
        statusJogador[2] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula4.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula4.textContent = jogadorAtual;
        statusJogador[3] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula4.textContent = jogadorAtual;
        statusJogador[3] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula5.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula5.textContent = jogadorAtual;
        statusJogador[4] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula5.textContent = jogadorAtual;
        statusJogador[4] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula6.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula6.textContent = jogadorAtual;
        statusJogador[5] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula6.textContent = jogadorAtual;
        statusJogador[5] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula7.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula7.textContent = jogadorAtual;
        statusJogador[6] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula7.textContent = jogadorAtual;
        statusJogador[6] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula8.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula8.textContent = jogadorAtual;
        statusJogador[7] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula8.textContent = jogadorAtual;
        statusJogador[7] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

celula9.addEventListener('click', function (event) {
    if (jogadorAtual === "X") {
        paragrafoCelula9.textContent = jogadorAtual;
        statusJogador[8] = "X";
        jogadorAtual = "O";
    }
    else {
        paragrafoCelula9.textContent = jogadorAtual;
        statusJogador[8] = "O";
        jogadorAtual = "X";
    }
    verificaPosicao();
});

buttonReset.addEventListener('click', () => {
    resetGame();
    paragrafoVencedor.textContent = "";
    statusJogador = ["", "", "", "", "", "", "", "", ""];
});
