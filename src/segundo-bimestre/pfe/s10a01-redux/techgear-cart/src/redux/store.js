import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './cartReducer.js';

// Crie a Store e associe o reducer usando configureStore
const store = configureStore({
  reducer: cartReducer
});

export default store;


