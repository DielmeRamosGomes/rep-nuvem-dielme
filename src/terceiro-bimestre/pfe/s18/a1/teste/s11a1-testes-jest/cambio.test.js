const { calcularTotalComTaxaDeCambio } = require('./cambio');
const axios = require('axios');

// Mock da biblioteca axios
jest.mock('axios');

describe('Função calcularTotalComTaxaDeCambio', () => {
  test('Deve calcular o total em outra moeda utilizando a taxa de câmbio simulada', async () => {
    const produtos = [
      { nome: 'Produto A', preco: 100 },
      { nome: 'Produto B', preco: 200 },
    ];

    // Simula a resposta da API de taxa de câmbio
    axios.get.mockResolvedValue({ data: { taxa: 5 } });

    const totalConvertido = await calcularTotalComTaxaDeCambio(produtos, 'USD');
    expect(totalConvertido).toBe(1500);  // (100 + 200) * 5
  });
});
