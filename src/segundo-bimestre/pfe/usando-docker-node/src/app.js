const htpp = require('http');
const hostname = '0.0.0.0';
// importe para docker
const port = 3000;

const server = htpp.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello node a partir de Docker\n');
    }
);

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
    }
);



