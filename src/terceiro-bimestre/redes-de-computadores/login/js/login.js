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

users = {
  admin: {
    email: "dielme@example.com",
    password: "123"
  },
  gerente: {
    email: "maria@example.com",
    password: "1234"
  },
  funcionario: {
    email: "joao@example.com",
    password: "12345"
  }
}

loginButton.addEventListener("click", (event) => {
  event.preventDefault();

  const email = emailInput.value;
  const password = passwordInput.value;

  if (email === user.email && password === user.password && (userAdmin.checked || userGerente.checked || userFuncionario.checked)) {
    alert(`Bem-vindo, ${user.name}! Você está logado como ${user.cargo}.`);
  } else {
    alert("Por favor, selecione um cargo.");
  }
});
