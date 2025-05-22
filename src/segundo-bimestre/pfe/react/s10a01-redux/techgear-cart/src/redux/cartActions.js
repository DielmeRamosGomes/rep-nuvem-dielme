// Action para adicionar item ao carrinho
export const addItem = (item) => {
  return {
    type: 'ADD_ITEM',
    payload: item
  };
};

// Action para remover item do carrinho
export const removeItem = (id) => {
  return {
    type: 'REMOVE_ITEM',
    payload: { id }
  };
};



