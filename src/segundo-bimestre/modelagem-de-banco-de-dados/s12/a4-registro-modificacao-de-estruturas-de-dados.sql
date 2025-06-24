-- nova da empresa TechFix
-- olhar roteiro da aula s12a4
create database if not exists techfix;

CREATE TABLE
    techfix.clientes (
        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        cidade VARCHAR(50),
        data_nascimento DATE
    );

CREATE TABLE
    techfix.produtos (
        id_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(100) NOT NULL,
        preco DECIMAL(10, 2) NOT NULL,
        fabricante VARCHAR(50),
        estoque INT
    );

CREATE TABLE
    techfix.pedidos (
        id_pedido INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT,
        data_pedido DATE,
        valor_total DECIMAL(10, 2),
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
    );

select * from techfix.clientes;

ALTER TABLE techfix.clientes
ADD COLUMN telefone_secundario VARCHAR(15);

ALTER TABLE techfix.produtos 
DROP COLUMN fabricante;

ALTER TABLE techfix.pedidos 
MODIFY COLUMN data_pedido DATETIME;

ALTER TABLE techfix.produtos 
ADD COLUMN peso DECIMAL(5,2), 
ADD COLUMN dimensao VARCHAR(50);

ALTER TABLE techfix.clientes 
MODIFY COLUMN nome VARCHAR(100);

