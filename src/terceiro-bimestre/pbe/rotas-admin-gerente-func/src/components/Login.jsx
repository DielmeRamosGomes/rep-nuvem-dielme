import "./Login.css";
import React, { useState } from "react";

function Login() {
  const [redirect, setRedirect] = useState("");

  const buttonClick = (event) => {
    event.preventDefault(); // Impede o envio do formulário

    const form = document.querySelector(".login-form");
    const formData = new FormData(form);
    const user = formData.get("usuario");

    if (user === "admin") {
      console.log("Redirecionando para a página do administrador...");
      setRedirect((prev) => "Redirecionando para a página do administrador...");
    } else if (user === "gerente") {
      console.log("Redirecionando para a página do gerente...");
      setRedirect((prev) => "Redirecionando para a página do gerente...");
    } else if (user === "funcionario") {
      console.log("Redirecionando para a página do funcionário...");
      setRedirect((prev) => "Redirecionando para a página do funcionário...");
    }
  };

  return (
    <div className="login-container">
      <form className="login-form">
        <h2>Login</h2>
        <div className="form-group-radio">
          <ul className="user-options">
            <li>
              <input
                type="radio"
                id="admin"
                name="usuario"
                value="admin"
                required
              />
              {"Administrador"}
            </li>

            <li>
              <input
                type="radio"
                id="gerente"
                name="usuario"
                value="gerente"
                required
              />
              {"Gerente"}
            </li>
            <li>
              <input
                type="radio"
                id="funcionario"
                name="usuario"
                value="funcionario"
                required
              />
              {"Funcionário"}
            </li>
          </ul>
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" required />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" required />
        </div>
        <button className="login-button" onClick={buttonClick} type="submit">
          Login
        </button>
      </form>
      <p>{redirect}</p>
    </div>
  );
}
export default Login;
