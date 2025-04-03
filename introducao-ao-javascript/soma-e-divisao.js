let n_vezes = 3;
let a = 1;
let b = n_vezes;
let resultado = 0;
contador_a = 1;
contador_b = n_vezes;

while (contador_a <= n_vezes) {
    resultado = resultado + (a/b);
    contador_a = contador_a + 1;
    contador_b = contador_b - 1;
    a = contador_a;
    b = contador_b;
}
console.log(`Resultado = ${resultado}`);







