// npm install express
// npm install cors
import express from 'express';
import cors from 'cors';
import Livro from './Livro.js';

const app = express();

// use middleware cors
app.use(cors({
  origin: 'http://127.0.0.1:5500' // Apenas a origem, sem o caminho do arquivo
}));

// Middleware para analisar o corpo da requisição como JSON
app.use(express.json());

const livros = [];

const livro1 = new Livro(1, "Harry Potter I", "JK Rowling", "Fantasia");
const livro2 = new Livro(2, "Harry Potter II", "JK Rowling", "Fantasia");
livros.push(livro1);
livros.push(livro2);

function atualizarLivro(id, nome, autor, categoria) {
  const livro = livros.find(livro => livro.getId() === id);
  if (!livro) {
    return null;
  }
  livro.setNome(nome);
  livro.setAutor(autor);
  livro.setCategoria(categoria);
  return livro;
}

app.get('/listarlivros', (req, res) => {
  try {
    res.json(livros);
  } catch (error) {
    console.error('Erro ao listar livros:', error);
    res.status(500).json({ error: 'Erro ao listar livros' });
  }
});

app.post('/cadastrarlivros', (req, res) => {
  try {
    let { id, nome, autor, categoria } = req.body;

    if (!id || !nome || !autor || !categoria) {
      return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
    }
    let novoLivro = new Livro(id, nome, autor, categoria);
    livros.push(novoLivro);
    res.status(201).json({ message: 'Livro cadastrado com sucesso!', livro: novoLivro });
  } catch (error) {
    console.error(`Erro ao cadastrar livro ${error}`);
    res.status(500).json({ error: 'Erro ao cadastrar livro' });
  }
});

app.put('/atualizarlivros', (req, res) => {
  try {
    let { id, nome, autor, categoria } = req.body;

    if (!id || !nome || !autor || !categoria) {
      return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
    }
    let livroAtualizado = atualizarLivro(id, nome, autor, categoria);
    
    if (livroAtualizado === null) {
      return res.status(404).json({ message: 'Livro não encontrado!' });
    } else {
      res.status(201).json({ message: 'Livro atualizado com sucesso!', livro: livroAtualizado });
    }
  } catch (error) {
    console.error(`Erro ao atualizar livro ${error}`);
    res.status(500).json({ error: 'Erro ao atualizar livro' });
  }
});

app.delete('/deletarlivros', (req, res) => {

});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando: http://localhost:${PORT}`);
});


