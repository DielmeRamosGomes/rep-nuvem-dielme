
const express = require("express");
const app = express();

const port = 3000;

app.use(express.static("public"));

// rota para exibir produtos
app.get("/listarprodutos", (req, res) => {
    const produtos = [
        {"id": 1, "nome": "Computador", "preco": 1000.0},
        {"id": 2, "nome": "Notebook", "preco": 2000.0},
        {"id": 3, "nome": "Tablet", "preco": 500.0}
    ];
    res.json(produtos);
});

// Página inicial que exibe os produtos
app.get('/', (req, res) => {
    res.send(`
      <html>
        <head>
          <title>E-commerce</title>
        </head>
        <body>
          <h1>Lista de Produtos</h1>
          <ul id="products-list"></ul>
  
          <script>
            fetch('/products')
              .then(response => response.json())
              .then(products => {
                const list = document.getElementById('products-list');
                products.forEach(product => {
                  const li = document.createElement('li');
                  li.innerHTML = product.name + ' - R$ ' + product.price + ' <button>Adicionar ao Carrinho</button>';
                  list.appendChild(li);
                });
              });
          </script>
        </body>
      </html>
    `);
  });

// inica o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
