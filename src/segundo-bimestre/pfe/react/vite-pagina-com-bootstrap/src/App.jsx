import { useState } from 'react'
import './App.css'

function App() {

  return (
    <div className="App">
      <header class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">WebSolutions</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Serviços</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Contato</a></li>
            </ul>
        </div>
      </header>
      <main class="container mt-5">
        <section class="jumbotron text-center">
            <h1 class="display-4">Bem-vindo à WebSolutions</h1>
            <p class="lead">Soluções em desenvolvimento web para todos os tipos de negócios.</p>
            <a href="#" class="btn btn-primary btn-lg">Saiba Mais</a>
        </section>
        <section class="row mt-5">
            <div class="col-md-4">
                <div class="card">
                    
                    <div class="card-body">
                        <h5 class="card-title">Serviço 1</h5>
                        <p class="card-text">Descrição do serviço 1.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="text-center mt-5">
        <p>&copy; 2024 WebSolutions. Todos os direitos reservados.</p>
    </footer>
    </div>
  );
}

export default App;
