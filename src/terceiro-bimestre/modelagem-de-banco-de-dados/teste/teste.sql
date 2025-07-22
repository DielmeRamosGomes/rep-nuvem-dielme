create database if not exists db_teste;

create table if not exists db_teste.clientes (
    id int primary key auto_increment,
    nome varchar(100) not null,
    idade int not null,
    ativo boolean not null default true
);

insert into db_teste.clientes (nome, idade) values
('João', 30),
('Maria', 25),
('Pedro', 40);

select * from db_teste.clientes;



