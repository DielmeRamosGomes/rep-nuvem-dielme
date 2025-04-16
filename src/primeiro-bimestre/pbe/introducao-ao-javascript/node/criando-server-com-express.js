// execute o comando na raiz do projeto npm install express para instalar o express

import express from 'express';
const app = express();

app.get('/produtos', (req, res) => {
    const produtos = [
        { cod_produto: 1, nome: 'Camiseta', preco: 29.99},
        { cod_produto: 2, nome: 'Calça Jeans', preco: 89.99},
        { cod_produto: 3, nome: 'Tênis', preco: 119.99}
    ];
    res.json(produtos);
});

const port = 3000;
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/produtos`);
});








