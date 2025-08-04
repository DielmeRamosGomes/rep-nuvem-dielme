import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css'
import Login from './components/Login.jsx';

function App() {

  return (
    <div className="app-container">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
