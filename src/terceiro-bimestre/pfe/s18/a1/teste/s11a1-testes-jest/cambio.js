const axios = require('axios');

async function calcularTotalComTaxaDeCambio(produtos, moeda) {
  const total = produtos.reduce((total, produto) => total + produto.preco, 0);
  const resposta = await axios.get(`https://api.exchangerate-api.com/${moeda}`);
  const taxaDeCambio = resposta.data.taxa;
  return total * taxaDeCambio;
}

module.exports = { calcularTotalComTaxaDeCambio };

