import { calcularTotalPedido, aplicarDesconto } from './Pedidos.js';

describe('Função calcularTotalPedido', () => {
  test('Deve calcular o total corretamente para uma lista de produtos', () => {
    const produtos = [
      { nome: 'Produto A', preco: 100 },
      { nome: 'Produto B', preco: 200 },
    ];
    const total = calcularTotalPedido(produtos);
    expect(total).toBe(300);
  });

  test('Deve retornar 0 para uma lista vazia de produtos', () => {
    const total = calcularTotalPedido([]);
    expect(total).toBe(0);
  });
});

describe('Função aplicarDesconto', () => {
  test('Deve aplicar o desconto corretamente', () => {
    const total = aplicarDesconto(300, 50);
    expect(total).toBe(250);
  });

  test('Deve lançar erro se o desconto for maior que o total', () => {
    expect(() => aplicarDesconto(100, 200)).toThrow('Desconto maior que o total');
  });
});



