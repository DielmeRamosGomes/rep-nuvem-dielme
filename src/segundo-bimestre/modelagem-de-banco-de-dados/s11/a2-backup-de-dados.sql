-- Criação do banco de dados
create database empresa_dados;

-- Selecionar o banco de dados
use empresa_dados;

-- Criação da tabela de clientes
CREATE TABLE
    empresa_dados.clientes (
        id_cliente INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        email VARCHAR(100),
        cidade VARCHAR(50)
    );

-- Criação da tabela de produtos
CREATE TABLE
    empresa_dados.produtos (
        id_produto INT PRIMARY KEY AUTO_INCREMENT,
        nome_produto VARCHAR(100),
        preco DECIMAL(10, 2),
        estoque INT
    );

-- Inserção de alguns dados nas tabelas
INSERT INTO
    empresa_dados.clientes (nome, email, cidade)
VALUES
    ('Carlos Silva', 'carlos@email.com', 'São Paulo'),
    ('Ana Souza', 'ana@email.com', 'Rio de Janeiro');

INSERT INTO
    empresa_dados.produtos (nome_produto, preco, estoque)
VALUES
    ('Notebook', 2500.00, 10),
    ('Smartphone', 1500.00, 25);

select
    *
from
    empresa_dados.clientes;

select
    *
from
    empresa_dados.produtos;

-- comando para backup do banco de dados
-- cd C:\xampp\mysql\bin
-- mysqldump -u root -p empresa_dados > backup_empresa_dados.sql