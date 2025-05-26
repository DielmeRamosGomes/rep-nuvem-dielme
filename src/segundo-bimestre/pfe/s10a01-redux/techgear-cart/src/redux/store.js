import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './cartReducer.js';
import { composeWithDevTools } from '@redux-devtools/extension';
import logger from 'redux-logger';

// Crie a Store e associe o reducer usando configureStore
const store = configureStore({
  reducer: cartReducer,
  compose: composeWithDevTools(logger)
});

export default store;


