create database if not exists db_tech;

CREATE TABLE
    if not exists db_tech.Clientes (
        cliente_id INT auto_increment PRIMARY KEY,
        nome VARCHAR(50) not null,
        email VARCHAR(50) not null,
        telefone VARCHAR(15) not null
    );

CREATE TABLE
    if not exists db_tech.Produtos (
        produto_id INT auto_increment PRIMARY KEY,
        nome VARCHAR(50) not null,
        preco DECIMAL(10, 2) not null,
        categoria VARCHAR(30) not null
    );

CREATE TABLE
    if not exists db_tech.Pedidos (
        pedido_id INT auto_increment PRIMARY KEY,
        data DATE not null,
        cliente_id INT not null,
        status VARCHAR(20) not null,
        FOREIGN KEY (cliente_id) REFERENCES db_tech.Clientes (cliente_id)
    );

CREATE TABLE
    if not exists db_tech.Itens_Pedido (
        item_id INT auto_increment PRIMARY KEY,
        pedido_id INT not null,
        produto_id INT not null,
        quantidade INT not null,
        preco_unitario DECIMAL(10, 2) not null,
        FOREIGN KEY (pedido_id) REFERENCES db_tech.Pedidos (pedido_id),
        FOREIGN KEY (produto_id) REFERENCES db_tech.Produtos (produto_id)
    );

create procedure if not exists db_tech.add_cliente(
    ac_nome VARCHAR(50),
    ac_email VARCHAR(50),
    ac_telefone VARCHAR(15)
)
begin
    insert into db_tech.Clientes (nome, email, telefone)
        values (ac_nome, ac_email, ac_telefone);
end;

call db_tech.add_cliente('Ana Silva','ana@exemplo.com', '12987654321');
call db_tech.add_cliente('Bruno Souza','bruno@exemplo.com', '12912345678');
select * from db_tech.Clientes;

create procedure if not exists db_tech.add_produto(
    ap_nome VARCHAR(50),
    ap_preco DECIMAL(10, 2),
    ap_categoria VARCHAR(30)
)
begin
    insert into db_tech.Produtos (nome, preco, categoria)
        values (ap_nome, ap_preco, ap_categoria);
end;

call db_tech.add_produto('Notebook', 3500.00, 'Eletrônicos');
call db_tech.add_produto('Smartphone', 1500.00, 'Eletrônicos');
select * from db_tech.Produtos;

create procedure if not exists db_tech.add_pedido(
    ap_data DATE,
    ap_cliente_id INT,
    ap_status VARCHAR(20)
)
begin
    insert into db_tech.Pedidos (data, cliente_id, status)
        values (ap_data, ap_cliente_id, ap_status);
end;

call db_tech.add_pedido('2024-06-01', 1, 'Pendente');
call db_tech.add_pedido('2024-06-02', 2, 'Enviado');
select * from db_tech.Pedidos;

create procedure if not exists db_tech.add_item_pedido(
    aip_pedido_id INT,
    aip_produto_id INT,
    aip_quantidade INT,
    aip_preco_unitario DECIMAL(10, 2)
)
begin
    insert into db_tech.Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
        values (aip_pedido_id, aip_produto_id, aip_quantidade, aip_preco_unitario);
end;

call db_tech.add_item_pedido(1, 1, 1, 3500.00);
call db_tech.add_item_pedido(1, 2, 2, 1500.00);


