let anguloX = 0;
let anguloY = 0;

const cubo = document.querySelector('.cubo');
const btnCubo = document.querySelector('#btn-cubo');
const btnReset = document.querySelector('#btn-reset');
const pTempo = document.querySelector('#paragrafo-tempo-ms');
const btnDiminuir = document.querySelector('#btn-diminuir');
let tempo_ms = 50;

let intervalId;

function startRotationInterval() {
  if (intervalId) clearInterval(intervalId);
  intervalId = setInterval(() => {
    anguloX += 1;
    anguloY += 1;
    cubo.style.transform = `rotateX(${anguloX}deg) rotateY(${anguloY}deg)`;
  }, tempo_ms);
}

btnCubo.addEventListener('click', () => {
  if (tempo_ms > 1) {
    tempo_ms -= 1;
    pTempo.textContent = `${tempo_ms}ms`;
    startRotationInterval();
  }
  console.log(`tempo_ms: ${tempo_ms}`);
});

btnReset.addEventListener('click', () => {
  tempo_ms = 50;
  startRotationInterval();
  pTempo.textContent = `${tempo_ms}ms`;
  console.log(`tempo_ms: ${tempo_ms}`);
});

btnDiminuir.addEventListener('click', () => {
  if (tempo_ms > 1) {
    tempo_ms += 1;
    pTempo.textContent = `${tempo_ms}ms`;
    startRotationInterval();
  }
  console.log(`tempo_ms: ${tempo_ms}`);
});

// Gira o cubo a cada 50ms
startRotationInterval();

