create database if not exists db_teste;
create database if not exists db_teste2

create table if not exists db_teste.clientes_online (
    id int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(100) not null unique,
    cidade varchar(100) not null
);

select * from db_teste.clientes_online;

insert into db_teste.clientes_online(id, nome, email, cidade)
    values(6, "ricardo", "ricardo@exemplo.com", "São Paulo");




