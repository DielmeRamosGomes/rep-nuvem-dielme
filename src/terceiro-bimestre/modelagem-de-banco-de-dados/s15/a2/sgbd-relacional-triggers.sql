create database if not exists db_tech_solutions;

create table
    if not exists db_tech_solutions.clientes (
        id int auto_increment primary key,
        nome varchar(100) not null,
        email varchar(100) not null unique,
        senha varchar(100) not null
    );

create table
    if not exists db_tech_solutions.produtos (
        id int auto_increment primary key,
        nome varchar(100) not null,
        descricao varchar(255),
        preco_unitario decimal(5, 2) not null
    );

create table
    if not exists db_tech_solutions.vendas (
        id int auto_increment primary key,
        cliente_id int not null,
        data_venda datetime not null,
        foreign key (cliente_id) references db_tech_solutions.clientes (id)
    );

create table
    if not exists db_tech_solutions.item_venda (
        id int auto_increment primary key,
        produto_id int not null,
        venda_id int not null,
        quantidade int not null,
        foreign key (venda_id) references db_tech_solutions.vendas (id),
        foreign key (produto_id) references db_tech_solutions.produtos (id)
    );

    

