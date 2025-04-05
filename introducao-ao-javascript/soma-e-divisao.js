import {createInterface} from 'readline';

const readLine = createInterface({
    input: process.stdin,
    output: process.stdout
});

readLine.question(`Digite o número de vezes que deseja fazer a soma e divisão: `,(entrada) => {
    let n_vezes = parseInt(entrada);
    if (isNaN(n_vezes)) {
        console.log(`Entrada inválida!`);
        readLine.close();
        return;
    }
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
    readLine.close();
});







