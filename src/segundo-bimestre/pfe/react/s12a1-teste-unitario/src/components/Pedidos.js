function calcularTotalPedido(produtos) {
    return produtos.reduce((total, produto) => total + produto.preco, 0);
  }
  
  function aplicarDesconto(total, desconto) {
    if (desconto > total) {
      throw new Error('Desconto maior que o total');
    }
    return total - desconto;
  }
  
  export default { calcularTotalPedido, aplicarDesconto };
  