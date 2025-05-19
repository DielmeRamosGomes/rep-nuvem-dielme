// npm install redux react-redux
// npm install @reduxjs/toolkit

import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addItem, removeItem } from './redux/cartActions.js';
import './App.css'

const ShoppingCart = () => {
  // useSelector para acessar o estado do carrinho
  const cartItems = useSelector((state) => state.cartItems);
  const dispatch = useDispatch();

  // Função para adicionar item ao carrinho
  const handleAddItem = () => {
    const newItem = {
      id: 1,
      name: 'Laptop',
      price: 1500
    };
    dispatch(addItem(newItem));
  };

  // Função para remover item do carrinho
  const handleRemoveItem = (id) => {
    dispatch(removeItem(id));
  };

  return (
    <div>
      <h1>Carrinho de Compras</h1>
      <button onClick={handleAddItem}>Adicionar Item</button>
      <ul>
        {cartItems.map((item) => (
          <li key={item.id}>
            {item.name} - {item.quantity} x R${item.price} 
            <button onClick={() => handleRemoveItem(item.id)}>Remover</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShoppingCart;

