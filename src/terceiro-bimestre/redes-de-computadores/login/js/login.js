const userAdmin = document.querySelector('.users[type="radio"]:nth-child(1)');
const userGerente = document.querySelector('.users[type="radio"]:nth-child(2)');
const userFuncionario = document.querySelector(
  '.users[type="radio"]:nth-child(3)'
);

const emailInput = document.querySelector(
  'input-email-senha[type="email"]:nth-child(1)'
);
const passwordInput = document.querySelector(
  'input-password-senha[type="password"]:nth-child(2)'
);

const loginButton = document.querySelector(".button-login");

users = [
  {
    email: "dielme@example.com",
    password: "123",
  },
  {
    email: "maria@example.com",
    password: "1234",
  },
  {
    email: "joao@example.com",
    password: "12345",
  },
];

loginButton.addEventListener("click", (event) => {
  event.preventDefault();

  const email = emailInput.value;
  const password = passwordInput.value;

  for (let i = 0; i < users.length; i++) {
    if (users[i].email === email && users[i].password === password) {
      alert("Login bem-sucedido!");
      return;
    }
  }
  alert("Email ou senha incorretos. Tente novamente.");
  
});
