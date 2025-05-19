const initialState = {
  cartItems: [] // Estado inicial do carrinho, um array vazio
};

// Reducer para gerenciar as ações no carrinho de compras
const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ADD_ITEM':
      const item = action.payload;
      // Verifique se o item já existe no carrinho
      const existingItem = state.cartItems.find((i) => i.id === item.id);
      if (existingItem) {
        // Se o item já estiver no carrinho, aumente a quantidade
        return {
          ...state,
          cartItems: state.cartItems.map((i) =>
            i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
          )
        };
      } else {
        // Se o item não existir, adicione ao carrinho
        return {
          ...state,
          cartItems: [...state.cartItems, { ...item, quantity: 1 }]
        };
      }

    case 'REMOVE_ITEM':
      return {
        ...state,
        cartItems: state.cartItems.filter((i) => i.id !== action.payload.id)
      };

    default:
      return state;
  }
};

export default cartReducer;




