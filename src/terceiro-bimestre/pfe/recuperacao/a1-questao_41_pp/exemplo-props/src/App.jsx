import React, { useState } from "react";
import "./App.css";
import Button from "./components/Button.jsx";

function App() {
  const [numberClick, setNumberClick] = useState(0);

  const clickButton = () => {
    setNumberClick((prev) => prev + 1);
  };

  const resetButton = () => {
    setNumberClick(0);
  };

  return (
    <div className="app-container">
      <h1>Exemplo de Props e State</h1>
      <div className="button-group">
        <Button onClick={clickButton} label="Clique Aqui" />
        <Button onClick={resetButton} label="Reset" />
      </div>
      <h2 className="h2-number-click">{numberClick}</h2>
    </div>
  );
}

export default App;
