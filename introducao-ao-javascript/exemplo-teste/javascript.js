import { createInterface } from 'readline';
const rl = createInterface({
    input: process.stdin,
    output: process.stdout
});

let numero;
let resultado;
let numeros = [];

function lerNumeros() {
    rl.question(`Digite um número: `, (entrada) => {
        numero = parseFloat(entrada);
        if(isNaN(numero)) {
            console.log("Entrada inválida. Por favor, insira um número."); 
            rl1.close();
            return;
        }
        else {
            numeros.push(numero);
            if(numeros.length < 2) {
                lerNumeros();
            }
            else{
                if (numeros[0] >= numeros[1]) {
                    resultado = numeros[0] + numeros[1];
                    console.log(`O resultado da soma é = ${resultado}`);
                }
                else {
                    resultado = numeros[1] - numeros[0];
                    console.log(`O resultado da subtração é = ${resultado}`);
                }

            }
        }
    });
}
    
lerNumeros();



