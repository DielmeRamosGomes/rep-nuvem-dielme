create database if not exists db_fast_tech;

CREATE TABLE
    db_fast_tech.clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100)
    );

CREATE TABLE
    db_fast_tech.produtos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        preco DECIMAL(10, 2)
    );

CREATE TABLE
    db_fast_tech.vendas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT,
        id_produto INT,
        data_venda DATE,
        quantidade INT,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id),
        FOREIGN KEY (id_produto) REFERENCES produtos (id)
    );

create procedure if not exists db_fast_tech.add_cliente(ac_nome varchar(100), ac_email varchar(100))
    begin
        insert into db_fast_tech.clientes(nome, email)
            values(ac_nome, ac_email);
    end;

call db_fast_tech.add_cliente('Lucas', 'lucas@exemplo.com');

select * from db_fast_tech.clientes;

create procedure if not exists db_fast_tech.add_produto(ap_nome varchar(100), ap_preco DECIMAL(10, 2))
    begin
        insert into db_fast_tech.produtos(nome, preco)
            values(ap_nome, ap_preco);
    end;

call db_fast_tech.add_produto('notebook', 3999.99);
call db_fast_tech.add_produto('Tablet', 2999.99);
select * from db_fast_tech.produtos;

create procedure if not exists db_fast_tech.add_venda(av_id_cliente INT,av_id_produto INT, av_data_venda DATE, av_quantidade INT)
    begin
        insert into db_fast_tech.vendas(id_cliente, id_produto, data_venda, quantidade)
            values(av_id_cliente, av_id_produto, av_data_venda, av_quantidade);
    end;

call db_fast_tech.add_venda(1, 1, '2025-08-20', 2);
call db_fast_tech.add_venda(1, 2, '2025-08-20', 3);
select * from db_fast_tech.vendas;

-- criando uma view relatório de vendas
CREATE VIEW db_fast_tech.relatorio_vendas AS
    SELECT c.nome AS cliente, p.nome AS produto, v.data_venda, v.quantidade
        FROM db_fast_tech.vendas v
            JOIN db_fast_tech.clientes c ON v.id_cliente = c.id
            JOIN db_fast_tech.produtos p ON v.id_produto = p.id;

select * from db_fast_tech.relatorio_vendas;
