// npm install mysql2
// npm install express
// npm install cors

import express from 'express';
import Produto from './Produto.js';
import Conexao from './Conexao.js';
import cors from 'cors';
//import Usuario from './Usuario.js';

const app = express();
//const cors = cors();

// use middleware cors
app.use(cors(
  {
    origin: 'http://http://127.0.0.1:5500/'
  })
);

// Middleware para analisar o corpo da requisição como JSON
app.use(express.json());

let lista_produtos = [];
let lista_usuarios = [];

async function usarConexao() {
  const conexao = new Conexao('localhost', 3306, 'root', '', 'estoque');
  const pool = await conexao.conectar();
  const connection = await pool.getConnection();
  return connection;
}

app.get('/listarusuarios', (req, res) => {
  //res.json(lista_produtos);
  usarConexao()
    .then(connection => {
      return connection.query('SELECT * FROM estoque.usuarios');
    })
    .then(([rows]) => {
      res.json(rows);
    })
    .catch(error => {
      console.error('Erro ao listar usuarios:', error);
      res.status(500).json({ error: 'Erro ao listar usuarios' });
    });
});

app.post('/cadastrarusuario', async (req, res) => {
  let { id, nome, email, senha, data_cadastro, ativo } = req.body;

  if (!id || !nome || !email || !senha || !data_cadastro || ativo === undefined) {
    return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
  }

  let novoUsuario = new Usuario(id, nome, email, senha, data_cadastro, ativo);

  lista_usuarios.push(novoUsuario);

  try {
    const connection = await usarConexao();
    const [rows] = await connection.query('INSERT INTO estoque.usuarios(id, nome, email, senha, data_cadastro, ativo) VALUES (?, ?, ?, ?, ?, ?);',
      [id, nome, email, senha, data_cadastro, ativo]
    );
    console.log(rows);
    connection.release();
    res.status(201).json({ message: 'Usuário cadastrado com sucesso!', produto: novoProduto });
  } catch (error) {
    console.error('Erro ao inserir usuário:', error);
    res.status(500).json({ error: 'Erro ao inserir o usuário no banco de dados' });
  }
});

app.get('/listarprodutos', (req, res) => {
  //res.json(lista_produtos);
  usarConexao()
    .then(connection => {
      return connection.query('SELECT * FROM estoque.produtos');
    })
    .then(([rows]) => {
      res.json(rows);
    })
    .catch(error => {
      console.error('Erro ao listar produtos:', error);
      res.status(500).json({ error: 'Erro ao listar produtos' });
    });
});

app.post('/cadastrarproduto', async (req, res) => {
  let { id, nome, imagem} = req.body;

  if (!id|| !nome || !imagem) {
    return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
  }

  let novoProduto = new Produto(_id_produto, _nome, _descricao, _id_vendedor, _data_cadastro, _ativo);

  lista_produtos.push(novoProduto);

  try {
    const connection = await usarConexao();
    const [rows] = await connection.query('INSERT INTO estoque.produtos(id_produto, nome, descricao, id_vendedor, data_cadastro, ativo) VALUES (?, ?, ?, ?, ?, ?);',
      [_id_produto, _nome, _descricao, _id_vendedor, _data_cadastro, _ativo]
    );
    console.log(rows);
    connection.release();
    res.status(201).json({ message: 'Produto cadastrado com sucesso!', produto: novoProduto });
  } catch (error) {
    console.error('Erro ao inserir produto:', error);
    res.status(500).json({ error: 'Erro ao inserir o produto no banco de dados' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando: http://localhost:${PORT}/cadastrarproduto`);
});





