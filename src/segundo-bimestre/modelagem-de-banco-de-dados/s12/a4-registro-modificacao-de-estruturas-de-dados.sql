-- nova da empresa TechFix
-- olhar roteiro da aula s12a4
create database if not exists techfix;

CREATE TABLE
    clientes (
        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        cidade VARCHAR(50),
        data_nascimento DATE
    );

CREATE TABLE
    produtos (
        id_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(100) NOT NULL,
        preco DECIMAL(10, 2) NOT NULL,
        fabricante VARCHAR(50),
        estoque INT
    );

CREATE TABLE
    pedidos (
        id_pedido INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT,
        data_pedido DATE,
        valor_total DECIMAL(10, 2),
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
    );