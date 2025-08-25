let anguloX = 0;
let anguloY = 0;

const cubo = document.querySelector('.cubo');

// Gira o cubo a cada 50ms
setInterval(() => {
  anguloX += 1;
  anguloY += 1;
  cubo.style.transform = `rotateX(${anguloX}deg) rotateY(${anguloY}deg)`;
}, 30);

