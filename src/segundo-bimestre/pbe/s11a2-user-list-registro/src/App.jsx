import { Route, BrowserRouter, Routes } from 'react-router-dom';
import './App.css'
import Configuracao from './components/Configuracao';
import Cadastro from './components/Cadastro';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Configuracao />} />
        <Route path="/cadastro" element={<Cadastro />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
