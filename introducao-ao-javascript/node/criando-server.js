import http from 'http';

// Criando um servidor HTTP
const server  = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader({'Content-Type': 'text/plain'});
    res.end('Bem-vindo ao meu servidor Node.js!');
});

// Definindo a porta do servidor
const port = 3000;
server.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});









