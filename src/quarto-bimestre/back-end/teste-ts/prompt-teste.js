// npm install prompt-sync
import promptSync from 'prompt-sync';

const prompt = promptSync();
const nome = prompt('Qual o seu nome?: ');
do {
    const nome = prompt('Qual o seu nome?: ');
}while (nome !== 'dielme');
console.log(`Olá, ${nome} Seja bem-vindo!`);

