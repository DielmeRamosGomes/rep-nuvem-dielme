import React, { useEffect, useState } from "react";
import "./App.css";
import Button from "./components/Button.jsx";
import Square from "./components/Square.jsx";

function App() {
  const [numberClick, setNumberClick] = useState(0);
  const [corAtual, setCorAtual] = useState("blue");

  const gerarCorAleatoria = () => {
    const letras = "0123456789ABCDEF";
    let cor = "#";
    for (let i = 0; i < 6; i++) {
      cor += letras[Math.floor(Math.random() * 16)];
    }
    return cor;
  };

  const clickButton = () => {
    setNumberClick((prev) => prev + 1);
    setCorAtual(gerarCorAleatoria());
  };

  const resetButton = () => {
    setNumberClick(0);
    setCorAtual("blue");
  };

  useEffect(() => {}, [numberClick]);

  return (
    <div className="app-container">
      <h1>Exemplo de Props e State e UseEffect</h1>
      <div className="button-group">
        <Button onClick={clickButton} label="Clique Aqui" />
        <Button onClick={resetButton} label="Reset" />
      </div>
      <h2 className="h2-number-click">{numberClick}</h2>
      <p>Cor atual: {corAtual}</p>
      <Square corAtual={corAtual} />
    </div>
  );
}

export default App;
