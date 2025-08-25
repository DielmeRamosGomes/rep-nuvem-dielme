// npm install mysql2
// npm install express
// npm install cors

import express from 'express';
import Conexao from './Conexao.js';
import cors from 'cors';
import Livros from './Livros.js';

const app = express();
//const cors = cors();

// use middleware cors
app.use(cors(
  {
    origin: 'http://127.0.0.1:5500/src/terceiro-bimestre/pbe/s17/a1/front-end/index.html'
  })
);

// Middleware para analisar o corpo da requisição como JSON
app.use(express.json());

let lista_livros = [];

async function usarConexao() {
  const conexao = new Conexao('localhost', 3307, 'root', '', 'db_livros');
  const pool = await conexao.conectar();
  const connection = await pool.getConnection();
  return connection;
}

app.get('/listarlivros', (req, res) => {
  usarConexao()
    .then(connection => {
      return connection.query('SELECT * FROM db_livros.livros');
    })
    .then(([rows]) => {
      res.json(rows);
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

  lista_livros.push(novoLivro);

  try {
    const connection = await usarConexao();
    const [rows] = await connection.query('INSERT INTO db_livros.livros(nome, editora, ano) VALUES (?, ?, ?);',
      [nome, editora, ano]
    );
    console.log(rows);
    connection.release();
    res.status(201).json({ message: 'livro cadastrado com sucesso!', livro: novoLivro });
  } catch (error) {
    console.error('Erro ao inserir livro:', error);
    res.status(500).json({ error: 'Erro ao inserir o livro no banco de dados' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando: http://localhost:${PORT}/listarprodutos`);
});


