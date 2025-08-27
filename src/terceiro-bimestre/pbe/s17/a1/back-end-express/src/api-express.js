// npm install mysql2
// npm install express
// npm install cors

import express from 'express';
import Conexao from './Conexao.js';
import cors from 'cors';
import Livros from './Livros.js';

const app = express();

// use middleware cors
app.use(cors({
  origin: 'http://127.0.0.1:5500' // Apenas a origem, sem o caminho do arquivo
}));

// Middleware para analisar o corpo da requisição como JSON
app.use(express.json());

async function usarConexao() {
  const conexao = new Conexao('localhost', 3307, 'root', '1234', 'db_livros');
  const pool = await conexao.conectar();
  const connection = await pool.getConnection();
  return connection;
}

app.get('/listarlivros', (req, res) => {
  usarConexao()
    .then(connection => {
      return connection.query('select * from db_livros.mostrar_livros')
        .then(([rows]) => {
          connection.release();
          res.json(rows);
        });
    })
    .catch(error => {
      console.error('Erro ao listar livros:', error);
      res.status(500).json({ error: 'Erro ao listar livros' });
    });
});

app.post('/cadastrarlivro', async (req, res) => {
  let { nome, editora, ano } = req.body;

  if (!nome || !editora || !ano) {
    return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
  }

  let novoLivro = new Livros(nome, editora, ano);

  try {
    const connection = await usarConexao();
    const [rows] = await connection.query('call db_livros.add_livro(?, ?, ?)',
      [nome, editora, ano]
    );
    console.log(rows);
    connection.release();
    res.status(201).json({ message: 'Livro cadastrado com sucesso!', livro: novoLivro });
  } catch (error) {
    console.error('Erro ao inserir livro:', error);
    res.status(500).json({ error: 'Erro ao inserir o livro no banco de dados' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando: http://localhost:${PORT}/listarlivros`);
});