const userAdmin = document.querySelector('#user1');
const userGerente = document.querySelector('#user2');
const userFuncionario = document.querySelector('#user3');

const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');

const loginButton = document.querySelector(".button-login");

const users = [
  {
    nome: "Dielme",
    cargo: "Administrador",
    email: "dielme@exemplo.com",
    password: "123",
  },
  {
    nome: "Maria",
    cargo: "Gerente",
    email: "maria@exemplo.com",
    password: "1234",
  },
  {
    nome: "João",
    cargo: "Funcionario",
    email: "joao@exemplo.com",
    password: "12345",
  },
];

loginButton.addEventListener("click", (event) => {
  event.preventDefault();

  const email = emailInput.value;
  const password = passwordInput.value;
  
  for (let i = 0; i < users.length; i++) {
    if (
      users[i].email === email &&
      users[i].password === password &&
      ((users[i].cargo === "Administrador" && userAdmin.checked) ||
        (users[i].cargo === "Gerente" && userGerente.checked) ||
        (users[i].cargo === "Funcionario" && userFuncionario.checked))
    ) {
      alert(
        `Login bem-sucedido!\n Bem vindo! ${users[i].nome} \n Redirecionando para a página do usuário ${users[i].cargo}`
      );
      return;
    }
  }
  alert("Email ou senha incorretos. Tente novamente.");
});
